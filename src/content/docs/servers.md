---
title: Server Status
description: Live status and player counts for Kerberus Minecraft servers.
tableOfContents: false
---
Live status for our Minecraft servers. Click an address to copy it.

<div class="kb-cards kb-cards--stack">
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

:::note
Server down or wrong address? Ask in [Discord](https://discord.gg/draconia).
:::

<script>
(function () {
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

  document.querySelectorAll('.kb-addr').forEach(function (c) {
    c.addEventListener('click', function () {
      var original = c.textContent;
      navigator.clipboard.writeText(original).then(function () {
        c.textContent = 'Copied!';
        setTimeout(function () { c.textContent = original; }, 1200);
      });
    });
  });
})();
</script>
