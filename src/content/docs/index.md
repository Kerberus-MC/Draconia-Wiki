---
title: Kerberus
description: Wiki hub for Kerberus Minecraft modpacks - Dragoncraft, Toothless, and PvZ Overgrowth.
template: splash
hero:
  title: Kerberus
  tagline: Minecraft modpacks, servers, and community
  actions:
    - text: Join our Discord
      link: https://discord.gg/draconia
      icon: discord
      variant: primary
    - text: Server Status
      link: /servers/
      icon: right-arrow
      variant: minimal
---

<div class="kb-section">
  <h2 class="kb-h">Wikis</h2>
  <div class="kb-cards">
    <a class="kb-card" href="/dragoncraft/">
      <img src="/assets/images/modpacks/kb-img-dragoncraft.png" alt="Dragoncraft" width="48" height="48">
      <span class="kb-card-text">
        <strong>Dragoncraft</strong>
        <span>Dragons, dungeons, and loot.</span>
      </span>
    </a>
    <a class="kb-card" href="/toothless/">
      <img src="/assets/images/modpacks/kb-img-toothless.png" alt="Toothless" width="48" height="48">
      <span class="kb-card-text">
        <strong>Toothless</strong>
        <span>Tame and ride dragons.</span>
      </span>
    </a>
    <a class="kb-card" href="/pvz-overgrowth/">
      <img src="/assets/images/modpacks/kb-img-pvz-overgrowth.png" alt="PvZ Overgrowth" width="48" height="48">
      <span class="kb-card-text">
        <strong>PvZ Overgrowth</strong>
        <span>Plants vs Zombies in Minecraft.</span>
      </span>
    </a>
  </div>
</div>

<div class="kb-section">
  <h2 class="kb-h">Projects</h2>
  <p class="kb-sub">Everything we've published on CurseForge.</p>
  <div class="kb-cards kb-cards--compact">
    <a class="kb-card" href="https://www.curseforge.com/minecraft/modpacks/dragoncraft" target="_blank" rel="noopener">
      <img src="/assets/images/projects/kb-img-dragoncraft.png" alt="" width="40" height="40">
      <span class="kb-card-text">
        <strong>Dragoncraft</strong>
        <span>Modpack · 150k downloads</span>
      </span>
    </a>
    <a class="kb-card" href="https://www.curseforge.com/minecraft/modpacks/mythcraft" target="_blank" rel="noopener">
      <img src="/assets/images/projects/kb-img-mythcraft.png" alt="" width="40" height="40">
      <span class="kb-card-text">
        <strong>Mythcraft Unleashed</strong>
        <span>Modpack · 16k downloads</span>
      </span>
    </a>
    <a class="kb-card" href="https://www.curseforge.com/minecraft/modpacks/toothless" target="_blank" rel="noopener">
      <img src="/assets/images/projects/kb-img-toothless.png" alt="" width="40" height="40">
      <span class="kb-card-text">
        <strong>Toothless</strong>
        <span>Modpack · 15k downloads</span>
      </span>
    </a>
    <a class="kb-card" href="https://www.curseforge.com/minecraft/modpacks/pvz-overgrowth" target="_blank" rel="noopener">
      <img src="/assets/images/projects/kb-img-pvz-overgrowth.png" alt="" width="40" height="40">
      <span class="kb-card-text">
        <strong>PvZ Overgrowth</strong>
        <span>Modpack · 12k downloads</span>
      </span>
    </a>
    <a class="kb-card" href="https://www.curseforge.com/minecraft/modpacks/nightcraft" target="_blank" rel="noopener">
      <img src="/assets/images/projects/kb-img-nightcraft.png" alt="" width="40" height="40">
      <span class="kb-card-text">
        <strong>Nightcraft</strong>
        <span>Modpack · 2.5k downloads</span>
      </span>
    </a>
    <a class="kb-card" href="https://www.curseforge.com/minecraft/modpacks/warpdrive" target="_blank" rel="noopener">
      <img src="/assets/images/projects/kb-img-warpdrive.png" alt="" width="40" height="40">
      <span class="kb-card-text">
        <strong>WarpDrive</strong>
        <span>Modpack · 1.7k downloads</span>
      </span>
    </a>
    <a class="kb-card" href="https://www.curseforge.com/minecraft/modpacks/submerged" target="_blank" rel="noopener">
      <img src="/assets/images/projects/kb-img-submerged.png" alt="" width="40" height="40">
      <span class="kb-card-text">
        <strong>Submerged</strong>
        <span>Modpack · 784 downloads</span>
      </span>
    </a>
    <a class="kb-card" href="https://www.curseforge.com/minecraft/modpacks/comfycraft" target="_blank" rel="noopener">
      <img src="/assets/images/projects/kb-img-comfycraft.png" alt="" width="40" height="40">
      <span class="kb-card-text">
        <strong>Comfycraft</strong>
        <span>Modpack · 716 downloads</span>
      </span>
    </a>
    <a class="kb-card" href="https://www.curseforge.com/minecraft/modpacks/cobblemon-high" target="_blank" rel="noopener">
      <img src="/assets/images/projects/kb-img-cobblemon-high.png" alt="" width="40" height="40">
      <span class="kb-card-text">
        <strong>Cobblemon High</strong>
        <span>Modpack · 419 downloads</span>
      </span>
    </a>
  </div>
</div>

<div class="kb-section">
  <h2 class="kb-h">Community</h2>
  <a class="kb-discord" href="https://discord.gg/draconia" target="_blank" rel="noopener">
    <span class="kb-card-text">
      <strong id="kb-dc-name">Kerberus Discord</strong>
      <span id="kb-dc-counts" class="kb-dc-counts">Chat, support, and updates</span>
    </span>
    <span class="kb-btn kb-btn--primary">Join</span>
  </a>
</div>

<script>
fetch('https://discord.com/api/v10/invites/draconia?with_counts=true')
  .then(function (r) { return r.json(); })
  .then(function (d) {
    if (d.guild && d.guild.name) {
      document.getElementById('kb-dc-name').textContent = d.guild.name;
    }
    if (d.approximate_member_count) {
      document.getElementById('kb-dc-counts').innerHTML =
        '<span class="kb-dot kb-dot--on"></span> ' +
        d.approximate_presence_count.toLocaleString() + ' online &middot; ' +
        d.approximate_member_count.toLocaleString() + ' members';
    }
  })
  .catch(function () {});
</script>
