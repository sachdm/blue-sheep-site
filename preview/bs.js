/* Homepage scatter. Placement declares a column band and how much air to leave
   above; exact pixel positions are solved here against the measured height of
   each block, so tiles of any size can never collide. */
(function () {
  const COLS = 12;
  const { PLACE, FILMS, COPY } = window;
  const canvas = document.getElementById('canvas');
  const esc = s => String(s).replace(/[&<>"]/g,
    c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

  const nodes = PLACE.map(p => {
    const el = document.createElement(p.k === 'f' ? 'a' : 'div');
    el.className = 'item ' + (p.k === 'f' ? 'film' : 'blk');
    const tc = `<div class="tc">${p.tc}</div>`;
    if (p.k === 'f') {
      const f = FILMS[p.i];
      el.href = f.slug + '.html';
      el.innerHTML = tc + `
        <figure><span class="idx">${String(p.i + 1).padStart(2, '0')}</span>
          <img src="${esc(f.still)}" alt="${esc(f.title)}"></figure>
        <figcaption><span class="t">${esc(f.title)}</span>
          <span class="c">${esc(f.cat)}&nbsp;&nbsp;${f.year}</span></figcaption>`;
    } else {
      const c = COPY[p.id];
      el.innerHTML = tc + `<div class="lbl">${esc(c.l)}</div>`
        + c.p.map(x => `<p>${x}</p>`).join('');
    }
    canvas.appendChild(el);
    return el;
  });

  function layout() {
    if (matchMedia('(max-width:860px)').matches) {
      canvas.style.height = 'auto';
      nodes.forEach(n => { n.style.width = ''; n.style.left = ''; n.style.top = ''; });
      return;
    }
    const gut = parseFloat(getComputedStyle(document.documentElement)
      .getPropertyValue('--gut'));
    const W = canvas.clientWidth;
    const colW = (W - gut * (COLS - 1)) / COLS;
    const bottom = new Array(COLS).fill(0);

    PLACE.forEach((p, n) => {
      const el = nodes[n];
      el.style.width = (colW * p.w + gut * (p.w - 1)) + 'px';
      el.style.left = (colW * p.c + gut * p.c) + 'px';
      let start = 0;
      for (let c = p.c; c < p.c + p.w; c++) start = Math.max(start, bottom[c]);
      start += p.lead;
      el.style.top = start + 'px';
      const h = el.offsetHeight;
      for (let c = p.c; c < p.c + p.w; c++) bottom[c] = start + h;
    });
    canvas.style.height = Math.max(...bottom) + 'px';
  }

  // images change height once decoded — relayout when they land or fail
  let pending = canvas.querySelectorAll('img').length || 1;
  canvas.querySelectorAll('img').forEach(img => {
    const done = () => { if (--pending <= 0) layout(); };
    if (img.complete) done(); else { img.onload = done; img.onerror = done; }
  });
  layout();
  addEventListener('resize', layout);
  if (document.fonts) document.fonts.ready.then(layout);
})();
