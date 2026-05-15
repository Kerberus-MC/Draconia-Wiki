---
hide:
  - navigation
  - toc
---

<style>
.hero {
  text-align: center;
  padding: 2rem 0 1rem;
}
.hero h1 {
  font-size: 2.5rem;
  margin-bottom: 0.25rem;
}
.hero p {
  font-size: 1.1rem;
  opacity: 0.7;
  margin-top: 0;
}
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.25rem;
  margin-top: 1.5rem;
}
.card-grid a.card {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1.25rem;
  border-radius: 0.75rem;
  background: var(--md-code-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  text-decoration: none;
  color: inherit;
  transition: transform 0.15s, box-shadow 0.15s, border-color 0.15s;
}
.card-grid a.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.2);
  border-color: var(--md-accent-fg-color);
}
.card-icon img {
  width: 64px;
  height: 64px;
  border-radius: 0.5rem;
  display: block;
}
.card-icon .emoji-icon {
  font-size: 2.5rem;
  width: 64px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--md-default-fg-color--lightest);
  border-radius: 0.5rem;
}
.card-text h3 {
  margin: 0 0 0.25rem 0;
  font-size: 1.1rem;
}
.card-text p {
  margin: 0;
  opacity: 0.7;
  font-size: 0.85rem;
  line-height: 1.4;
}
.discord-banner {
  text-align: center;
  margin-top: 2rem;
  padding: 1.5rem;
  border-radius: 0.75rem;
  background: linear-gradient(135deg, #1a1a2e 0%, #2d2d4a 100%);
  border: 1px solid rgba(108, 99, 255, 0.2);
  color: white;
}
.discord-banner a {
  color: white;
  text-decoration: none;
  font-weight: 600;
  font-size: 1.1rem;
}
.discord-banner p {
  margin: 0.25rem 0 0;
  opacity: 0.85;
  font-size: 0.85rem;
}
</style>

<div class="hero">
  <h1>Draconia</h1>
  <p>Minecraft modpack wiki hub</p>
</div>

---

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

<div class="discord-banner">
  <a href="https://discord.gg/draconia" target="_blank">💬 Join our Discord</a>
  <p>Support, updates, and community.</p>
</div>
