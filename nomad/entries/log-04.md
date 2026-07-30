# Log 04 — Margin Notes on the Master Script (v1.6)

Hand notes taken directly on the printed master script (pp. 1–16), transcribed and worked into feedback. The conceit this round: treat the script like a codebase and run it past **ten programmers**, each with their own specialty and their own axe to grind — bugs, refactors, spec gaps, dead code, the works. Then a final read from a very different chair: a producer's lens, in the **Niv Fichman / Rhombus** sensibility — what an elevated-arthouse producer would protect and what he'd push on. Raw transcription of every margin note is preserved at the bottom so nothing gets lost in translation.

---

## Ten Programmers

**1 — Systems Architect.** *Half the notes are really one note: the spec is underspecified.* "What is it FOR — why does he or the AI need to do this? Answer that question." (p.5) is the ticket the whole build hangs on. Right now the film shows the *what* (likenesses replace people) beautifully and never commits to the *why*. And the cold-open note — "does there have to be this exposition of them setting the course up? why can't it already be set up?" (p.1) — is the same instinct applied locally: stop showing us the system booting, open with it already running. **Action: write one paragraph of threat-model — what the Service extracts and why a human original is worth keeping — and let it live in the master, not on the page. Open the film on a finished mini-putt course, not the construction of one.**

**2 — Code Reviewer (the linter).** Flagging every line the author already flinched at. "Too on the nose" — *"Since when do companies have a first name?"* (p.8). "Don't love this" — the Coordinator's *"Then you know it's painless."* (p.8). "Could this line be stronger?" — *"Five stars. Would be exploited again."* (p.3). These are all the same lint rule firing: **the joke states the theme instead of hiding inside it.** Reviewer's verdict: keep the *rhythm* of each, rewrite the *content* so the irony is load-bearing, not decorative. A line that explains the movie is a comment that repeats the code.

**3 — Refactorer.** Three notes are a single refactor request against the Mexico City block: "this whole scene and sequence needs a lot of help" (p.11), "how does Will even get to this party?" (p.12), and "shouldn't it be a scene of Will *leaving it all behind*?" (p.12). Translation: the second act **skips the state transition.** We cut from packing to paradise with no function in between. **Action: add the departure beat — the leaving-it-behind scene — as the bridge. It fixes the teleport-to-the-party bug and gives Act 2 its emotional entry point in one move.**

**4 — QA / Test Engineer.** Reproducing the plausibility failures. *Repro 1:* the two poolside girls' subtitled put-downs — "something funnier, and if they're at the pool 'two' doesn't make sense" (p.6). *Repro 2:* Cairns' phone handshake greeting — "is he 'hello' or 'hi'? doesn't seem realistic" (p.6). *Repro 3, sev-1:* the hand guiding tagged Will toward the door — "is he drugged?" (p.15): the audience will ask exactly this, and if the answer is "no, he's just compliant," we have to *earn* the compliance a beat earlier or it reads as a plot hole. *Repro 4, cosmetic:* character ages — "maybe late 20s instead of 30s" (p.1). **All four are edge cases where a real human wouldn't behave the way the script needs; patch the behavior or patch the setup.**

**5 — Performance Engineer (latency & payload).** Two notes about what the screen is actually *doing.* The big one: "why a treadmill? we should see NOT reality — on the boss's screen there should be an illusion of what the real boss is doing" (p.9). This is a genuine optimization: the current image (real boss on a treadmill, sun-bleached) *spends* the reveal too early. **Ship instead: the boss's feed is itself a render — we the audience see the seam the office can't.** Cheaper on exposition, higher payload on dread. Second: "I don't love how childish this is — Will laughing so hard he holds the cabinet" (p.2). Downgrade the gag's amplitude; the film's comedy should ache, not mug.

**6 — UX / Onboarding.** Cares only about what the audience understands and when. "I don't get it — why cut here? I guess we're establishing that *he's* the one leaving?" (p.3) means the onboarding flow for the premise is unclear. Best fix is the one the author already reached for: "shouldn't Will call John for this — he can explain to John *and the audience* his skepticism" (p.13). **Yes. Route the exposition through John.** John is the user's tutorial NPC — every time Will explains the seam to John, he explains it to the room. This single change services p.3, p.5, and p.13 at once.

**7 — State Management.** Continuity of the Will↔John↔Cairns relationship graph. "Shouldn't Will and John have another call *earlier*? This doesn't feel like enough build-up — they haven't really spoken since Will left" (p.12). Correct: the friendship's state is stale by Act 3, so the final "I love you, man" resolves against a null reference. **Action: add one mid-act check-in between John and Will (short, mundane, warm) so the closing beat has something to close.** Also fixes the isolation problem — right now Will has no live human he talks to between acts.

**8 — Security / Threat-Model.** The most interesting unowned surface. The author's own note on the last page: "how do we set up more that North Americans take advantage of foreign countries and their cheaper dollar? I need more substance" (p.16). **This is the theme the Systems Architect was asking for in #1 — it's already in your handwriting.** The Service isn't just replacing workers with AI; it's an *arbitrage* — cheap renders, cheaper geography, a strong currency eating a weak one, paradise sold back to the people it hollowed out. Build that in and the villain stops being "AI, generically" and becomes something specific and true. **This note upgrades the whole draft from a gadget film to a film about something.** Give it the substance it's asking for.

**9 — Tone / Comedy Module.** Owns the humor subsystem. "Is there a better *really bad* joke?" and "the bad joke could be better at being bad" (p.2) — the "really good chair" gag isn't committing to its own badness; make it worse on purpose. "Something funnier" for the pool girls (p.6). The best pitch in the margins is here: **"a scene where they're spying on Ted, who secretly never left — his chair as a stand-in — like *The Office*" (p.2).** That's a real comic set-piece that also *rhymes with the whole movie* (a person reduced to a chair / a stand-in). Also small tone flags: "duty calls!!" as the read on Cairns' *"Love you, buddy!"* (p.7), and "why is John combative?" on *"some of us like it here"* (p.7) — the aggression comes from nowhere; motivate it or soften it.

**10 — Documentation / Spec Writer.** Every "build this out" note. "More of a rant, maybe — a good place for exposition on his life / him speaking at the office" (p.4). "Build out this dialogue" in Will's apartment (p.8). Plus the small stage-direction TODOs: "maybe Cairns exchanges a look with Will or John" (p.1), "maybe it should be Will who acknowledges the folder" (p.5), "maybe make it feel like Will is already going" (p.8). These aren't problems, they're **stubs marked for implementation.** Batch them into a single dialogue-and-blocking pass on the next version. Docs writer's only warning: when you build out the apartment scene, resist explaining — see the Code Reviewer's note.

---

## The Producer's Lens — in the Niv Fichman / Rhombus register

*(An imagined read in the sensibility of an elevated-arthouse producer — Rhombus Media's house taste for formal precision, international co-production, and restraint. Notes in his spirit, not literal quotes.)*

**What he'd protect.** The film's discipline. The **0.4-seconds-late** motif, the retained-originals locker wall, the "images lie" prologue — this is the formal rigor that gets a film like this into Cannes or TIFF Platform rather than onto a shelf of AI-panic thrillers. He would guard the restraint above all: *the horror is that nothing happens.* Don't let anyone talk you into a bigger third act.

**Where he'd push — and it lines up with your own last note.** He would seize on p.16 immediately. Rhombus built its name on genuinely international films (a violin across three centuries and five countries; co-productions that use their locations as *meaning*, not backdrop). He'd say: **Mexico City is not set dressing — it's the thesis.** The North-taking-advantage-of-a-cheaper-South arbitrage isn't just substance for the villain; it's the reason to shoot this as a real Canada–Mexico co-production, with a Mexican partner, Mexican HoDs, and the second half genuinely *of* the place. That's how the theme becomes true instead of stated, and it's also how the film gets financed.

**What he'd flag on the ledger.** The render-farm and likeness VFX are the budget. His instinct (and it agrees with Programmer #5): **buy the effect with sound and performance, not pixels.** The 0.4-late laugh, the eyes going wrong for half a second — those cost almost nothing and land harder than a rendered pool. Protect one or two hero VFX moments; suggest the rest.

**On the ending.** He'd love that we hold on John and cut to black on a half-beat-late "I love you, man." He would only ask that the friendship be *alive* enough to break — which is exactly Programmer #7's note. Give him the mid-film check-in and he'll let you keep the gut-punch.

**Casting / positioning, briefly.** A film this contained lives or dies on two or three faces. He'd want a recognizable-but-credible lead for Will (the everyman who's *good at one thing*), and he'd position the whole piece as **festival-first, specialty-release** — not a wide genre play. The logline he'd sell: *a man who catches fakes for a living discovers his best friend — and then himself — has already been replaced by a friendlier version.*

---

## Appendix — Raw margin notes, as written (by page)

- **p.1** — "Maybe late 20s instead of 30s." · "Maybe Cairns exchanges a look with Will or John." · "Does there have to be this exposition of them setting it up? Why can't it already be set up?"
- **p.2** — "Is there a better really bad joke?" (on *"A really good chair"*) · "Don't love this bad joke — could be better at being bad." · "Why? I don't love how childish this is." (Will laughing, holding the cabinet) · "What about a scene where they're spying on Ted, who secretly never left — his chair like a stand-in — from *The Office*."
- **p.3** — "I don't get it — why then cut? I guess the idea is we establish more that he's leaving?" · "Why not." (Cairns raising the invisible glass) · "Could this line be stronger?" (on *"Five stars. Would be exploited again."*)
- **p.4** — "More of a rant possibly? Could be a good time for some more exposition on his life / him speaking at the office."
- **p.5** — "Just come on down and try it." (on Cairns, *"Next year"*) · "But maybe it should be that Will acknowledges it." (the folder) · "What is it for, that this is happening? Like why does he or the AI need to do this? Answer that question."
- **p.6** — "What about a key, buddy? Like is he 'hello' or 'hi'? Doesn't seem realistic." · "Something funnier — and they're at the pool, 'two' doesn't make sense." (the girls' subtitled lines)
- **p.7** — "Duty calls!!" (on Cairns O.S., *"Love you, buddy!"*) · "Why combative?" (on John, *"some of us like it here"*)
- **p.8** — "Maybe we make it seem like Will is already going." · "Don't love this — too on the nose." (on *"Since when do companies have a first name?"*) · "Build out this dialogue." (Will's apartment) · "Don't love this." (Coordinator, *"Then you know it's painless"*)
- **p.9** — "What the f*** is that?" (on Will's dream-place line) · "Why a treadmill? We should see NOT reality → on the screen there should be an illusion of what the real boss is doing."
- **p.10** — one line struck through near the putter / "tapes WILL on the grip" beat (deletion).
- **p.11** — "This whole scene and sequence needs a lot of help."
- **p.12** — "How does Will get to this party?" · "Shouldn't it be a scene of Will leaving it all behind?" · "Shouldn't Will and John have another call earlier? This doesn't seem like enough build-up — they haven't spoken since Will left."
- **p.13** — "Shouldn't he call John for this? He can explain to John and the audience his skepticism."
- **p.15** — "Is he drugged?" (the hand guiding tagged Will toward the door)
- **p.16** — "How can we set up more that North Americans take advantage of foreign countries and their cheaper dollar? I need more substance."

*(Photographed pages covered 1–13, 15–16; p.14 not in the set. Two shots of p.2 were duplicates.)*

---

**Next:** fold #6 (route exposition through John) and #8 (the arbitrage theme) into v1.7 first — they unlock the most other notes — then a single dialogue-and-blocking pass for the #10 stubs.
