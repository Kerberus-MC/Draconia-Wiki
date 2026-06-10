---
hide:
  - navigation
  - toc
---

<style>
.hero {
  text-align: center;
  padding: 4rem 0 2rem;
}
.hero h1 {
  font-size: 2.8rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  margin-bottom: 0.3rem;
  color: var(--md-default-fg-color);
}
.hero p {
  font-size: 1rem;
  color: var(--md-default-fg-color--lighter);
  margin-top: 0;
}
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1rem;
  margin: 2rem auto;
  max-width: 52rem;
}
.card-grid a.card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.25rem 1.5rem;
  border-radius: 0.75rem;
  background: var(--surface, #1c1c28);
  border: 1px solid var(--border, rgba(255,255,255,0.08));
  text-decoration: none;
  color: inherit;
  transition: all 0.2s ease;
}
.card-grid a.card:hover {
  border-color: var(--border-hover, rgba(129,140,248,0.3));
  background: var(--surface-raised, #22222e);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
}
.card-icon img {
  width: 48px;
  height: 48px;
  border-radius: 0.5rem;
  display: block;
}
.card-text h3 {
  margin: 0 0 0.15rem 0;
  font-size: 0.95rem;
  font-weight: 600;
}
.card-text p {
  margin: 0;
  color: var(--md-default-fg-color--lighter);
  font-size: 0.78rem;
  line-height: 1.4;
}
a.discord-banner {
  display: block;
  text-align: center;
  margin: 1.5rem auto 0;
  max-width: 52rem;
  padding: 1.25rem;
  border-radius: 0.75rem;
  background: var(--surface, #1c1c28);
  border: 1px solid var(--border, rgba(255,255,255,0.08));
  color: var(--md-default-fg-color);
  text-decoration: none;
  transition: all 0.2s ease;
}
a.discord-banner:hover {
  border-color: var(--border-hover, rgba(129,140,248,0.3));
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.15);
  color: var(--md-default-fg-color);
}
.discord-title {
  display: block;
  font-weight: 600;
  font-size: 0.9rem;
}
.discord-sub {
  display: block;
  margin-top: 0.2rem;
  color: var(--md-default-fg-color--lighter);
  font-size: 0.78rem;
}
</style>

<div class="hero">
  <h1>Kerberus</h1>
  <p>Minecraft modpack wiki hub</p>
</div>

<div class="card-grid">
  <a class="card" href="dragoncraft/">
    <div class="card-icon">
      <img src="/assets/images/modpacks/kb-img-dragoncraft.png" alt="Dragoncraft">
    </div>
    <div class="card-text">
      <h3>Dragoncraft</h3>
      <p>Dragons, dungeons, and loot.</p>
    </div>
  </a>
  <a class="card" href="toothless/">
    <div class="card-icon">
      <img src="/assets/images/modpacks/kb-img-toothless.png" alt="Toothless">
    </div>
    <div class="card-text">
      <h3>Toothless</h3>
      <p>Tame and ride dragons.</p>
    </div>
  </a>
  <a class="card" href="pvz-overgrowth/">
    <div class="card-icon">
      <img src="/assets/images/modpacks/kb-img-pvz-overgrowth.png" alt="PvZ Overgrowth">
    </div>
    <div class="card-text">
      <h3>PvZ Overgrowth</h3>
      <p>Plants vs Zombies in Minecraft.</p>
    </div>
  </a>
</div>

<a class="discord-banner" href="https://discord.gg/draconia" target="_blank">
  <span class="discord-title">Join our Discord</span>
  <span class="discord-sub">Support, updates, and community.</span>
</a>
