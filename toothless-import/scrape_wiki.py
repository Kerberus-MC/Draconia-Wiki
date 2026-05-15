"""
Scrape Archipelago Additions wiki pages for MkDocs import.
Extracts main content text and image URLs from each page.
"""
import requests
from bs4 import BeautifulSoup, NavigableString, Tag, Comment
import os
import re
import sys
import time

BASE_URL = "https://archipelagoadditions.miraheze.org"
WIKI_PATH = "/wiki/"
OUTPUT_DIR = r"D:\Git\Draconia\Draconia-Wiki\toothless-import"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

PAGES = [
    "Dragons",
    "Boulder_Class",
    "Mystery_Class",
    "Sharp_Class",
    "Stoker_Class",
    "Strike_Class",
    "Tidal_Class",
    "Tracker_Class",
    "Blocks_%26_Items",
    "Effects",
    "Structures",
    "Guides",
    "Installation_process",
    "Dragon_Rider_Companions",
    "Miscellaneous_features",
]


def clean_parser_junk(text):
    """Remove MediaWiki parser cache metadata from extracted text."""
    # Remove everything from "NewPP limit report" onwards
    idx = text.find("NewPP limit report")
    if idx != -1:
        text = text[:idx]
    # Also remove "Saved in parser cache" lines
    text = re.sub(r'Saved in parser cache.*', '', text)
    # Remove trailing whitespace
    text = text.rstrip()
    return text


def extract_text_content(soup_element):
    """Extract readable text from a BeautifulSoup element, preserving structure."""
    lines = []
    for elem in soup_element.children:
        # Skip HTML comments entirely
        if isinstance(elem, Comment):
            continue

        if isinstance(elem, NavigableString):
            text = str(elem).strip()
            if text:
                lines.append(text)
            continue

        if not isinstance(elem, Tag):
            continue

        # Skip navigation/edit/toc elements
        if elem.get('id') in ('toc', 'catlinks', 'siteSub', 'contentSub', 'jump-to-nav'):
            continue
        classes = elem.get('class') or []
        if any(c in classes for c in ['mw-editsection', 'toc', 'navbox', 'catlinks', 'printfooter', 'noprint']):
            continue

        if elem.name in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            level = int(elem.name[1])
            text = elem.get_text(strip=True)
            # Remove [edit] links from headings
            text = text.replace('[edit]', '').replace('[edit source]', '').strip()
            if text:
                lines.append("")
                lines.append("#" * level + " " + text)
                lines.append("")
        elif elem.name == 'p':
            text = elem.get_text(strip=False).strip()
            if text:
                lines.append(text)
                lines.append("")
        elif elem.name == 'ul':
            for li in elem.find_all('li', recursive=False):
                text = li.get_text(strip=True)
                if text:
                    lines.append("- " + text)
            lines.append("")
        elif elem.name == 'ol':
            for i, li in enumerate(elem.find_all('li', recursive=False), 1):
                text = li.get_text(strip=True)
                if text:
                    lines.append(f"{i}. " + text)
            lines.append("")
        elif elem.name == 'dl':
            for child in elem.children:
                if isinstance(child, Tag):
                    if child.name == 'dt':
                        lines.append("**" + child.get_text(strip=True) + "**")
                    elif child.name == 'dd':
                        lines.append("  " + child.get_text(strip=True))
            lines.append("")
        elif elem.name == 'table':
            lines.append("[TABLE]")
            # Extract table content
            for row in elem.find_all('tr'):
                cells = row.find_all(['th', 'td'])
                if cells:
                    cell_texts = [c.get_text(strip=True) for c in cells]
                    lines.append(" | ".join(cell_texts))
            lines.append("[/TABLE]")
            lines.append("")
        elif elem.name == 'div':
            # Recurse into divs (galleries, etc.)
            if 'gallery' in classes:
                lines.append("[GALLERY]")
                for img in elem.find_all('img'):
                    alt = img.get('alt', '')
                    lines.append(f"  Image: {alt}")
                lines.append("[/GALLERY]")
                lines.append("")
            else:
                inner = extract_text_content(elem)
                if inner.strip():
                    lines.append(inner)
        elif elem.name == 'figure':
            # Handle figure elements (images with captions)
            caption = elem.find('figcaption')
            img = elem.find('img')
            if img:
                alt = img.get('alt', '')
                cap = caption.get_text(strip=True) if caption else alt
                lines.append(f"[IMAGE: {cap}]")
                lines.append("")

    return "\n".join(lines)


def normalize_image_url(src):
    """Normalize an image URL to an absolute URL."""
    if not src:
        return None
    # Handle protocol-relative URLs (//static.wikitide.net/...)
    if src.startswith('//'):
        return 'https:' + src
    # Handle CDN URLs that the wiki uses
    if src.startswith('http'):
        return src
    # Handle relative paths
    if src.startswith('/w/images/') or src.startswith('/w/thumb/'):
        return BASE_URL + src
    if src.startswith('/'):
        return BASE_URL + src
    return None


def extract_images(soup_element):
    """Extract all image URLs from the content."""
    images = []
    seen_urls = set()
    for img in soup_element.find_all('img'):
        src = img.get('src', '')
        url = normalize_image_url(src)
        if url and url not in seen_urls:
            # Check if it's a content image (not a tiny UI icon)
            if 'wikitide.net' in url or 'miraheze.org' in url:
                alt = img.get('alt', '')
                images.append(f"{url}\t{alt}")
                seen_urls.add(url)
    return images


def extract_srcset_images(soup_element, existing_urls):
    """Extract higher-resolution images from srcset attributes."""
    extra = []
    seen = set(existing_urls)
    for tag in soup_element.find_all(['source', 'img']):
        srcset = tag.get('srcset', '')
        if srcset:
            for part in srcset.split(','):
                part = part.strip()
                if part:
                    raw_url = part.split()[0]
                    url = normalize_image_url(raw_url)
                    if url and url not in seen:
                        if 'wikitide.net' in url or 'miraheze.org' in url:
                            extra.append(f"{url}\thigh-res variant")
                            seen.add(url)
    return extra


def scrape_page(page_name):
    """Scrape a single wiki page."""
    url = BASE_URL + WIKI_PATH + page_name
    print(f"Fetching: {url}")

    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"  ERROR fetching {page_name}: {e}")
        return False

    soup = BeautifulSoup(resp.text, 'html.parser')

    # Find the main content div
    content_div = soup.find('div', class_='mw-parser-output')
    if not content_div:
        content_div = soup.find('div', id='mw-content-text')
        if content_div:
            inner = content_div.find('div', class_='mw-parser-output')
            if inner:
                content_div = inner

    if not content_div:
        print(f"  WARNING: No mw-parser-output found for {page_name}")
        body = soup.find('body')
        if body:
            content_div = body
        else:
            print(f"  SKIP: No content found for {page_name}")
            return False

    # Extract text
    text_content = extract_text_content(content_div)
    # Clean out parser cache junk
    text_content = clean_parser_junk(text_content)

    # Add page title
    title_elem = soup.find('h1', id='firstHeading') or soup.find('h1', class_='firstHeading')
    title = title_elem.get_text(strip=True) if title_elem else page_name.replace('_', ' ')

    full_text = f"# {title}\n\n{text_content}"

    # Extract images
    images = extract_images(content_div)
    existing_urls = {line.split('\t')[0] for line in images}
    srcset_images = extract_srcset_images(content_div, existing_urls)
    images.extend(srcset_images)

    # Clean filename
    clean_name = page_name.replace('%26', '_and_').replace('%', '_')

    # Save text content
    text_path = os.path.join(OUTPUT_DIR, f"{clean_name}.txt")
    with open(text_path, 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f"  Saved text: {text_path} ({len(full_text)} chars)")

    # Save image list
    img_path = os.path.join(OUTPUT_DIR, f"{clean_name}_images.txt")
    with open(img_path, 'w', encoding='utf-8') as f:
        for img_line in images:
            f.write(img_line + "\n")
    print(f"  Saved images: {img_path} ({len(images)} image URLs)")

    return True


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    success = 0
    failed = []

    for page in PAGES:
        ok = scrape_page(page)
        if ok:
            success += 1
        else:
            failed.append(page)
        # Be polite to the server
        time.sleep(1)

    print(f"\nDone. {success}/{len(PAGES)} pages scraped successfully.")
    if failed:
        print(f"Failed pages: {', '.join(failed)}")


if __name__ == '__main__':
    main()
