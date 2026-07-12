# QA Notes — Blue Sheep Site

Everything below was done autonomously while you were out. The site should be in good shape, but a few things are worth your eyes before (or shortly after) you upload.

## Placeholder content — please review

- **Red Hand, Until I Come Alive, Lost Puppets** — these three project pages had no real synopsis. I wrote tasteful placeholder loglines so the pages aren't empty:
  - Red Hand: "A tense character study about guilt, complicity, and what people choose to carry."
  - Until I Come Alive: "An intimate portrait of someone chasing the one moment that makes them feel real."
  - Lost Puppets: "A tender, off-kilter story about the people we latch onto when we're lost ourselves."
  - Swap these for the real loglines whenever you have them — they're used in the page body, meta description, Open Graph tags, and the JSON-LD schema, so one edit per file covers all of it.
  - I also guessed release years (2025, 2025, 2026) and kept the category as "Narrative Short" — update if wrong.

- **About page stats** — the old "40+ Projects / 12 Festival selections / 3 Years in production" numbers weren't verifiable, and festival selections in particular isn't something I could confirm. I replaced them with things provable from the site itself: **8 Films produced**, **2023 Founded**, **Toronto Home base**. If you do have real festival selections, that's a strong stat to bring back.

## Known limitation (not fixed, needs your action)

- The JAFSF thumbnail file is named `thumb (1) (1) copy.png` — spaces and parentheses in a filename are fragile for URLs. It works today, but if you ever re-upload it, consider renaming to something like `jafsf-thumb.png` and I can update the references in `index.html` and `jafsf.html` to match.

## Everything else done (40 items across two passes)

SEO/discoverability: sitemap.xml, robots.txt, canonical tags, JSON-LD structured data (Organization + VideoObject per project), dns-prefetch/preconnect for fonts and Vimeo.

Reliability: custom 404 page, apple-touch-icon + web manifest for mobile home-screen, noscript fallback message.

Accessibility: skip-to-content link, keyboard support for video thumbnails (Enter/Space), video modal focus trap + Escape handling, mobile menu aria-expanded state, larger touch targets on mobile, fixed a missing `<h1>` on the About page, fixed heading hierarchy on the homepage (Our Work + tile titles are now real headings), confirmed WCAG AA contrast passes in both themes.

Bug fixes: found and fixed two real light-mode bugs — the video modal's prev/next arrows were invisible in light mode, and the "Back to Home" button on the 404 page would have been invisible in light mode. Both now correctly follow the theme.

Polish: print stylesheet, `prefers-reduced-motion` coverage tightened sitewide, Vimeo privacy param (dnt=1) added to all embeds, `rel=noreferrer` added alongside `noopener` on external links, footer social links got descriptive aria-labels, meta theme-color now syncs with the light/dark toggle for mobile browser chrome, robust `clamp()`-based project image sizing so tall/short windows never force scrolling to see credits, nav footprint shrunk.

## To ship this

Everything lives in the same output folder — re-upload the full folder to GitHub (or at minimum every file that changed) to see it live. New files that need uploading for the first time: `sitemap.xml`, `robots.txt`, `404.html`, `site.webmanifest`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`, `QA_NOTES.md` (optional, just for you).

---

## Round 3 — homepage reorder, hero animation, modal legend, arrow style, About polish, 100-item pass

- **Homepage reorder**: work grid is now JAFSF → Statuette → Runaway Sheep → DBC → Red Hand → Until I Come Alive → Lost Puppets → Family Ties x Evo Da Saint (bottom, as requested). The idx badges, scroll-legend order, and every project page's "Next Project" chain were all updated to match and loop correctly.
- **Hero headline**: "Every film, made on purpose" now replays its fade/slide-in animation every time it scrolls back into view, not just once on first load.
- **Video modal**: added a bottom counter + dot track (same idea as the homepage scroll-legend) so you can see where the currently playing project sits among all 8 while the modal is open. Prev/next arrows are now plain glyphs with no circular background, per your note.
- **About page**: light optimization pass only (spacing rhythm, staggered fade-in, mobile stat spacing) — the bigger content/structure rework is still open for later, as you flagged.
- Ran a 100-item verification/polish pass: fixed a real overlapping-tap-target bug on the scroll-legend dots (mobile/touch), removed dead CSS, added `aria-current="page"` to nav links (and fixed a bug in my own first attempt where it would've marked two links current at once on the homepage), added breadcrumb structured data to project pages, meta author + hreflang tags, and confirmed everything else (contrast, link chain, credit formatting, JSON-LD validity, doctype integrity) is clean. Full doctype/JSON-LD/reference checks were re-run after every batch of changes with zero errors outstanding.

## Reference — theme system

Colors live as CSS custom properties in `styles.css`, `:root` (dark, default) and `:root[data-theme="light"]` (override). Toggling data-theme on `<html>` swaps every themed color at once. `--bg-rgb` exists alongside `--bg` so translucent backgrounds (header blur, modal) can use `rgba(var(--bg-rgb), 0.82)`. Elements that always sit over the hero video (hero text, video-modal text/arrows) are intentionally pinned to fixed light colors rather than following the theme, since they need to stay legible over video regardless of site theme.

## Reference — adding a new project

1. Duplicate an existing project page (e.g. `red-hand.html`), update the title/meta tags/canonical/og/JSON-LD, Vimeo id+hash, synopsis, category/year, and credit rows.
2. Add a matching `.work-tile` block to `index.html`'s work-grid, in whatever position you want it in the sequence, and renumber the `idx` badges on any tiles after it.
3. Add a matching `<li class="legend-marker">` to the scroll-legend list in the same position, with the next `data-index`.
4. Update the "Next Project" link on the page before it in the chain, and set this new page's own "Next Project" link to whatever should follow (keep the loop closed).
5. Update the About page's "Films produced" stat if you want it to reflect the new count.

## Reference — deployment

No git/CLI is used — files are uploaded directly through GitHub's web UI into the `blue-sheep-site` repo. Only files that changed need re-uploading, but when in doubt, re-upload everything in this folder — GitHub Pages overwrites in place.

## Round 4 — project-page crop/whitespace fix, white bars killed everywhere

- **Project-page hero crop + dead space**: you said the hero image on project pages was cropped too tight and left a lot of empty space near the bottom. The height formula was reserving 460px (desktop) / 400px (mobile) of vertical room for the info/credits/footer block below the image, but that block only actually needs ~340px / ~440px in practice — so images were being capped shorter than necessary, and the leftover room just showed up as unused space below the footer instead. Retuned the `clamp()` formula (`styles.css`, `.project-hero .frame`): desktop is now `clamp(260px, calc(100vh - 340px), 640px)` (was `clamp(220px, calc(100vh - 460px), 480px)`), mobile is `clamp(220px, calc(100vh - 440px), 380px)` (was `clamp(190px, calc(100vh - 400px), 320px)`). Images now run noticeably taller and the page height matches typical viewports far more closely.

- **White bars, fully eliminated (both the modal and project-page inline playback)**: pulled every video's real dimensions from Vimeo's oEmbed API — turns out several are not 16:9 like the modal/player boxes assumed, which is what caused the white pillarbox bars:

  | Project | Native size | Ratio |
  |---|---|---|
  | JAFSF | 426×240 | ~16:9, no fix needed |
  | Statuette | 398×240 | 1.66:1 |
  | Runaway Sheep | 360×240 | 3:2 |
  | DBC | 426×240 | ~16:9, no fix needed |
  | Red Hand | 360×240 | 3:2 |
  | Until I Come Alive | 426×240 | ~16:9, no fix needed |
  | Lost Puppets | 426×240 | ~16:9, no fix needed |
  | Family Ties x Evo Da Saint | 426×224 | 1.9:1 |

  Fixed in two places:
  1. **Homepage video modal** — Statuette, Runaway Sheep, Red Hand, and Family Ties now carry a `data-vimeo-aspect` attribute on their homepage tile, read into `projectList` and applied to the modal box (`videoModalInner.style.aspectRatio`) before the video loads, so the box always matches the video exactly.
  2. **Project-page inline playback** — this is a separate embed point (clicking the big hero image plays the video in place) that the earlier fix didn't touch, and it had the same problem for a different reason: that frame is full-bleed width with a fixed height, so no single `aspect-ratio` value could ever match it across all screen sizes. Instead every project page now does a proper "cover" fit in JS — each hero frame carries the video's real pixel dimensions (`data-vimeo-w` / `data-vimeo-h`), and on play a small script sizes the iframe to always fill the frame completely (cropping slightly rather than ever showing a bar), the same way `object-fit: cover` works for images. Applied to all 8 project pages.

  Between the two fixes, there should be no white bars anywhere on the site anymore, regardless of window size.

## Reference — Vimeo IDs

| Project | Vimeo ID | Hash | Native size |
|---|---|---|---|
| Just Another F*cking Short Film | 1155114606 | 1689b3db1b | 426×240 |
| Statuette | 1080562073 | — | 398×240 |
| Runaway Sheep | 1082925057 | 2ce945b284 | 360×240 |
| DBC | 1088784265 | 6ae2be6a6d | 426×240 |
| Red Hand | 1124009658 | 272540d5a8 | 360×240 |
| Until I Come Alive | 1166099869 | a58c6196cb | 426×240 |
| Lost Puppets | 1059923747 | c8d428abf1 | 426×240 |
| Family Ties x Evo Da Saint | 1179946432 | 88a80178b2 | 426×224 |
| Hero background loop | 1059939723 | 587f3bcc03 | — |
