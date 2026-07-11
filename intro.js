(function () {
  const intro = document.getElementById('intro');
  if (!intro) return;

  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const alreadySeen = sessionStorage.getItem('bsIntroSeen');

  if (reduceMotion || alreadySeen) {
    intro.remove();
    return;
  }

  document.documentElement.style.overflow = 'hidden';

  // snow
  const snowLayer = intro.querySelector('.snow-layer');
  const flakeCount = 46;
  for (let i = 0; i < flakeCount; i++) {
    const f = document.createElement('div');
    f.className = 'snowflake';
    const size = 2 + Math.random() * 3;
    f.style.width = size + 'px';
    f.style.height = size + 'px';
    f.style.left = Math.random() * 100 + '%';
    f.style.animationDuration = 6 + Math.random() * 6 + 's';
    f.style.animationDelay = Math.random() * 6 + 's';
    f.style.opacity = 0.4 + Math.random() * 0.5;
    snowLayer.appendChild(f);
  }

  const storyEl = intro.querySelector('.intro-story');
  const captionEl = intro.querySelector('.intro-caption');
  const titleEl = intro.querySelector('.intro-title');
  const sheepEl = intro.querySelector('.sheep');
  const skipBtn = intro.querySelector('.intro-skip');

  const lines = [
    "Once, on a cold winter night...",
    "a man came to shear the flock.",
    "Even the Blue Sheep felt the chill."
  ];

  let timers = [];
  function schedule(fn, t) { timers.push(setTimeout(fn, t)); }
  function clearAll() { timers.forEach(clearTimeout); timers = []; }

  function setCaption(text) {
    captionEl.classList.remove('show');
    schedule(() => {
      captionEl.textContent = text;
      captionEl.classList.add('show');
    }, 220);
  }

  function finish() {
    clearAll();
    intro.classList.add('intro-out');
    setTimeout(() => {
      if (intro.parentNode) intro.remove();
      document.documentElement.style.overflow = '';
    }, 900);
    sessionStorage.setItem('bsIntroSeen', '1');
  }

  function runTimeline() {
    schedule(() => setCaption(lines[0]), 150);

    schedule(() => setCaption(lines[1]), 1250);
    schedule(() => sheepEl.classList.add('shorn'), 1300);

    schedule(() => setCaption(lines[2]), 2550);
    schedule(() => sheepEl.classList.add('cold'), 2600);

    schedule(() => {
      captionEl.classList.remove('show');
      storyEl.classList.add('hide');
    }, 3700);
    schedule(() => titleEl.classList.add('show'), 4000);

    schedule(() => finish(), 5300);
  }

  skipBtn.addEventListener('click', finish);
  runTimeline();
})();
