/**
 * Build-time Vimeo enrichment.
 *
 * Reads src/data/films.json, asks the Vimeo API for the CURRENT thumbnail and
 * true dimensions of each film, and writes src/data/vimeo.generated.json.
 *
 * Why this exists: the stills were hardcoded i.vimeocdn.com URLs with embedded
 * hashes. Those rot silently when Vimeo re-encodes, and there is no warning —
 * the page just starts showing empty frames. Resolving them at build time means
 * the URL is always current, and the real width/height let us reserve layout
 * space so images stop popping in.
 *
 * THE TOKEN IS NEVER STORED IN THIS REPO. It arrives as the VIMEO_TOKEN
 * environment variable, injected from GitHub Actions secrets at build time.
 *
 * If VIMEO_TOKEN is absent — local builds, forks, pull requests — this exits
 * cleanly and the site falls back to the `still` URLs already in films.json.
 * A missing token degrades the site; it never breaks the build.
 */
import { readFile, writeFile } from 'node:fs/promises';

const TOKEN = process.env.VIMEO_TOKEN;
const OUT = new URL('../src/data/vimeo.generated.json', import.meta.url);

const films = JSON.parse(await readFile(new URL('../src/data/films.json', import.meta.url), 'utf8'));

if (!TOKEN) {
  console.log('[vimeo] VIMEO_TOKEN not set — falling back to the still URLs in films.json.');
  await writeFile(OUT, JSON.stringify({ generated: false, films: {} }, null, 2));
  process.exit(0);
}

/** Pick the largest thumbnail at or under `max` px wide. */
function bestSize(sizes = [], max = 1280) {
  const usable = sizes.filter(s => s.width <= max).sort((a, b) => b.width - a.width);
  return usable[0] || sizes[sizes.length - 1] || null;
}

const out = {};
let ok = 0, failed = 0;

for (const f of films) {
  if (!f.vimeoId) continue;
  // Unlisted videos are addressed as {id}:{hash}
  const ref = f.vimeoHash ? `${f.vimeoId}:${f.vimeoHash}` : f.vimeoId;
  const url = `https://api.vimeo.com/videos/${ref}?fields=name,duration,width,height,pictures.sizes`;
  try {
    const res = await fetch(url, {
      headers: { Authorization: `Bearer ${TOKEN}`, Accept: 'application/vnd.vimeo.*+json;version=3.4' },
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const v = await res.json();
    const pic = bestSize(v.pictures?.sizes);
    if (!pic?.link) throw new Error('no thumbnail in response');
    out[f.slug] = {
      still: pic.link,
      stillWidth: pic.width,
      stillHeight: pic.height,
      videoWidth: v.width ?? null,
      videoHeight: v.height ?? null,
      duration: v.duration ?? null,
      title: v.name ?? null,
    };
    ok++;
    console.log(`[vimeo] ${f.slug} → ${pic.width}px thumbnail, ${v.duration}s`);
  } catch (err) {
    failed++;
    console.warn(`[vimeo] ${f.slug} FAILED (${err.message}) — falling back to the committed still URL.`);
  }
}

await writeFile(OUT, JSON.stringify({ generated: true, at: null, films: out }, null, 2));
console.log(`[vimeo] done — ${ok} resolved, ${failed} fell back.`);

// A partial failure is survivable; a total failure with a token present is not,
// because it means the token is wrong and every image on the site would be stale.
if (TOKEN && ok === 0 && films.some(f => f.vimeoId)) {
  console.error('[vimeo] Token was present but NOTHING resolved. Check the token scopes.');
  process.exit(1);
}
