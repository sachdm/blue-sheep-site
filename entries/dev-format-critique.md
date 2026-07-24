# Master Script — Format Critique & Fix

A pass over how the rendered script was presenting, and what "professional" requires.

## What was wrong

1. **Scanlines on the page.** The terminal CRT scanline overlay was bleeding across the white paper — the "terrible lines." Amateur, illegible. Killed on the script page.
2. **Centered dialogue.** Real screenplays never center dialogue — that reads as a stage play or a first-timer. Industry standard is fixed LEFT indents in 12pt Courier: character cue ~3.7" from the page edge, dialogue ~2.5", parenthetical ~3.1", action full width. Reformatted to true indents.
3. **UI chrome on the artifact.** "edit source ✎ · rendered from the master draft" and "The Short · rendered from master draft" were printed on the title page. A script cover carries title, author, contact — nothing else. Removed.
4. **No transitions discipline.** CUT TO:, CUT TO BLACK belong flush right in caps. Fixed.
5. **Slug/action spacing.** Tightened to standard: one blank line above a slugline, action hard against it.
6. **Wrong logo.** The page was falling back to a traced placeholder. Now points directly at the real logo.png; no fallback.

## The standard we're matching

12pt Courier, single-spaced, US-Letter proportions. Left margin wide (binding), right margin ~1". Sluglines in caps. Character cues in caps, indented. Dialogue in a ~3.3" column. Parentheticals tucked under the cue. Transitions flush right. That's what a Final Draft / Celtx PDF looks like, and that's what the page now renders.

## Notes

Notes now live in the GUTTER — grey margin beside the paper, never on the white. Written inline in the source as `[[ note ]]`; the site pulls them out and pins each one beside its line. The page stays clean; the notes ride alongside.
