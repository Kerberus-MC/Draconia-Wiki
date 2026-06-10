// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightLinksValidator from 'starlight-links-validator';

export default defineConfig({
  site: 'https://wiki.kerberus.gg',
  integrations: [
    starlight({
      plugins: [starlightLinksValidator()],
      title: 'Kerberus Wiki',
      description: 'Wiki hub for Kerberus Minecraft modpacks - Dragoncraft, Toothless, and PvZ Overgrowth.',
      social: [
        { icon: 'discord', label: 'Discord', href: 'https://discord.gg/draconia' },
        { icon: 'github', label: 'GitHub', href: 'https://github.com/Kerberus-MC/Draconia-Wiki' },
      ],
      editLink: {
        baseUrl: 'https://github.com/Kerberus-MC/Draconia-Wiki/edit/master/',
      },
      lastUpdated: true,
      customCss: ['./src/styles/custom.css'],
      head: [
        {
          tag: 'meta',
          attrs: { property: 'og:image', content: 'https://wiki.kerberus.gg/assets/images/og-banner.png' },
        },
        {
          tag: 'meta',
          attrs: { name: 'twitter:card', content: 'summary_large_image' },
        },
        {
          tag: 'meta',
          attrs: { name: 'theme-color', content: '#0f0f17' },
        },
      ],
      sidebar: [
        {
          label: 'Dragoncraft',
          collapsed: true,
          items: [{ label: 'Overview', slug: 'dragoncraft' }],
        },
        {
          label: 'Toothless',
          collapsed: true,
          items: [
            { label: 'Overview', slug: 'toothless' },
            { label: 'All Dragons', slug: 'toothless/dragons' },
            { label: 'Boulder Class', slug: 'toothless/dragons/boulder-class' },
            { label: 'Mystery Class', slug: 'toothless/dragons/mystery-class' },
            { label: 'Sharp Class', slug: 'toothless/dragons/sharp-class' },
            { label: 'Stoker Class', slug: 'toothless/dragons/stoker-class' },
            { label: 'Strike Class', slug: 'toothless/dragons/strike-class' },
            { label: 'Tidal Class', slug: 'toothless/dragons/tidal-class' },
            { label: 'Tracker Class', slug: 'toothless/dragons/tracker-class' },
            {
              label: 'Dragon Index',
              collapsed: true,
              items: [{ autogenerate: { directory: 'toothless/dragons/detail' } }],
            },
            { label: 'Companions', slug: 'toothless/companions' },
            { label: 'Effects', slug: 'toothless/effects' },
            { label: 'Structures', slug: 'toothless/structures' },
          ],
        },
        {
          label: 'PvZ Overgrowth',
          collapsed: true,
          items: [
            { label: 'Overview', slug: 'pvz-overgrowth' },
            { label: 'FAQ', slug: 'pvz-overgrowth/faq' },
            {
              label: 'Guides',
              items: [
                { label: 'Plant Spawn', slug: 'pvz-overgrowth/plant-spawn' },
                { label: 'Contagion', slug: 'pvz-overgrowth/contagion' },
              ],
            },
            {
              label: 'Almanac',
              items: [
                { label: 'Plants', slug: 'pvz-overgrowth/almanac/plants' },
                { label: 'Zombies', slug: 'pvz-overgrowth/almanac/zombies' },
                { label: 'PvZ Items', slug: 'pvz-overgrowth/almanac/items' },
              ],
            },
          ],
        },
      ],
    }),
  ],
});
