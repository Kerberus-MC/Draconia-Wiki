---
title: Kerberus
description: Wiki hub for Kerberus Minecraft modpacks - Dragoncraft, Toothless, and PvZ Overgrowth.
template: splash
hero:
  title: Kerberus
  tagline: Minecraft modpack wiki hub
  actions:
    - text: Join our Discord
      link: https://discord.gg/draconia
      icon: discord
      variant: primary
---

<div class="kb-section">
  <h2 class="kb-h">Modpacks</h2>
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
  <h2 class="kb-h">Server Status</h2>
  <div class="kb-cards">
    <div class="kb-card kb-server" data-addr="dragoncraft.kerberus.gg">
      <img src="/assets/images/modpacks/kb-img-dragoncraft.png" alt="" width="48" height="48">
      <span class="kb-card-text">
        <strong>Dragoncraft</strong>
        <code class="kb-addr" title="Click to copy">dragoncraft.kerberus.gg</code>
        <span class="kb-status"><span class="kb-dot"></span><span class="kb-players">Checking…</span></span>
      </span>
    </div>
    <div class="kb-card kb-server" data-addr="toothless.kerberus.gg">
      <img src="/assets/images/modpacks/kb-img-toothless.png" alt="" width="48" height="48">
      <span class="kb-card-text">
        <strong>Toothless</strong>
        <code class="kb-addr" title="Click to copy">toothless.kerberus.gg</code>
        <span class="kb-status"><span class="kb-dot"></span><span class="kb-players">Checking…</span></span>
      </span>
    </div>
    <div class="kb-card kb-server" data-addr="pvz.kerberus.gg">
      <img src="/assets/images/modpacks/kb-img-pvz-overgrowth.png" alt="" width="48" height="48">
      <span class="kb-card-text">
        <strong>PvZ Overgrowth</strong>
        <code class="kb-addr" title="Click to copy">pvz.kerberus.gg</code>
        <span class="kb-status"><span class="kb-dot"></span><span class="kb-players">Checking…</span></span>
      </span>
    </div>
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
(function () {
  // Minecraft server status via mcstatus.io
  document.querySelectorAll('.kb-server').forEach(function (el) {
    var addr = el.getAttribute('data-addr');
    var dot = el.querySelector('.kb-dot');
    var pl = el.querySelector('.kb-players');
    fetch('https://api.mcstatus.io/v2/status/java/' + addr)
      .then(function (r) { return r.json(); })
      .then(function (d) {
        if (d.online) {
          dot.classList.add('kb-dot--on');
          pl.textContent = d.players.online + ' / ' + d.players.max + ' players';
        } else {
          dot.classList.add('kb-dot--off');
          pl.textContent = 'Offline';
        }
      })
      .catch(function () {
        dot.classList.add('kb-dot--off');
        pl.textContent = 'Status unavailable';
      });
  });

  // Click-to-copy server addresses
  document.querySelectorAll('.kb-addr').forEach(function (c) {
    c.addEventListener('click', function () {
      var original = c.textContent;
      navigator.clipboard.writeText(original).then(function () {
        c.textContent = 'Copied!';
        setTimeout(function () { c.textContent = original; }, 1200);
      });
    });
  });

  // Live Discord counts via invite API
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
})();
</script>
