/**
 * The single accessor for film data.
 *
 * Merges the committed base data (src/data/films.json) with whatever the
 * build-time Vimeo fetch resolved (src/data/vimeo.generated.json). Live API
 * values win; the committed `still` is the fallback. Every page imports from
 * here so there is one merge rule rather than one per template.
 */
import base from '../data/films.json';
import generated from '../data/vimeo.generated.json';

export const films = base.map(f => {
  const live = generated.films?.[f.slug];
  return {
    ...f,
    still: live?.still ?? f.still,
    stillWidth: live?.stillWidth ?? 1280,
    stillHeight: live?.stillHeight ?? 720,
    duration: live?.duration ?? null,
    stillIsLive: Boolean(live?.still),
  };
});

/** 5400 -> "1h 30m" · 412 -> "6m 52s" */
export function runtime(seconds) {
  if (!seconds) return null;
  const h = Math.floor(seconds / 3600);
  const m = Math.floor((seconds % 3600) / 60);
  const s = seconds % 60;
  return h ? `${h}h ${m}m` : `${m}m ${s}s`;
}

export default films;
