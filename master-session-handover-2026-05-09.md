# Master Session Handover — Layer 6 Phase 4 (continued, post-deploy iteration)

**Created:** 2026-05-09. Session ran through ~36 turns of post-Bundle-N3 deploy-readiness iteration on overview + findings + beeswarm + brain housekeeping. Context approaching limit; handover triggered.
**For:** the next master session
**Read time:** ~6 min
**Pick up at:** dispatch two pending sub-sessions (cards + scenarios) + complete the 4 remaining page iterations + final cleanup batch + deploy v1

---

## Project state in one paragraph

Synthesis site is in deploy-readiness iteration. The structural / data / methodology work is locked from prior sessions (Phases 1A → 2K + Phase 3 + Phase 3.5 + Bundle N3 v2 + brain Path-B merge). This session was page-by-page editorial polish: overview page (index.html) had hero + lede + Q&A one-liner + 4 SMs locked anew; findings.html got Italy block + Conclusion + corridor h3 + SM 2 buffer-bullets + SM 3 closing arrow rewrites; the "Active Cascade" Class IV label renamed to "Currently Failing" across all surfaces; beeswarm got its internal "Phase 2A · Problem 1 / Alternative B" subheader stripped + the 1.20 / 2.80 corridor edges explained in plain language. Plus brain housekeeping (Path-B merge brought both new skills into main; BRAIN-INDEX header now at 94; CANONICAL-COUNTS updated; linkedin-playbook em-dash row enriched with structural-rewrite discipline; Earth for All / Club of Rome flagged for Layer 7). Two sub-sessions pending dispatch (cards + scenarios) and 4 pages still to iterate (europe / methodology / sources / glossary) before final cleanup batch + deploy v1.

---

## Locked decisions this session (do not re-litigate)

| Decision | Lock |
|---|---|
| **Class IV label rename** | "Active Cascade" → "Currently Failing" (cascaded across 7 site pages + One-Pager + Long-Read + Specialist Appendix + Executive Edition + glossary.tsv + SVG exports + planning docs; internal `active_cascade` field-name preserved in SOT) |
| **Overview-page hero + lede + Q&A + 4 SMs** | Phil-locked verbatim (see index.html lines 195–252 post-edit). NEW: Q&A one-liner as 5th pyramid block between stats and 4 SMs; new lede with "Most countries can only handle some of the disruption..."; new SM 1 + SM 2 headers; new supports across all 4 SMs. "Overview" sub-heading removed (redundant). |
| **findings.html page subheader** | Aligned to index.html lede ("can only handle some of the disruption") |
| **findings.html corridor h3 (B path)** | h3 renamed "How the 36 markets split" + italic one-line definition: *"Each country sits in one of three corridors (coping / at-risk / already behind) and one of four fragility classes (whether that placement survives stress-testing under six macro shocks)."* |
| **findings.html SM 2 buffers restructure** | Prose → intro line + 2 bullets (retirement / retraining); `<ul class="sm-support" style="padding-left:1.2em;margin-top:0">` for tight nested look |
| **findings.html SM 3 closer arrow** | Em-dash → `→` arrow: "...to jurisdictions with thinner protections → stability at the price of capital-flight risk" |
| **findings.html "Most cannot absorb it all" h3** | Italic orphan promoted to proper h3 (semibold, dropped italic, max-width 760) — sits above "How the 36 markets split" h3 |
| **findings.html §1 prelude gloss** | Added inline glosses: *"three corridors (severity of AI-displacement risk) and four fragility classes (stability under stress)"* |
| **findings.html SM 2 prose anti-jargon** | "show active cascade signals" → "show signs of institutional collapse already underway" |
| **Italy block rewrite (findings.html)** | New lead: *"The outlier → Italy, with the workforce shrinking before AI displaces a single worker."* + plain-language body dropping technical Class III / regime / scenario-weight references; keeps −485,823 as punchline |
| **Conclusion rewrite (findings.html)** | "Forecasts are easy..." opening + class-by-class action implications (preservation / conditional fragilities / step-change / containment) + "dropping soon" close (replaces "scoped separately") |
| **Beeswarm fixes** | Removed "Phase 2A · Problem 1 / Alternative B" subheader; cleaned workshop-language note; aligned h3 to findings.html convention ("Lens 1 absorption ratio · 36 markets"); **added plain-language explanation of where the 1.20 / 2.80 corridor edges come from** |
| **Byline date** | April 2026 → May 2026 (cascaded all 7 site pages) |
| **Footer "Last updated"** | 2026-04-30 → 2026-05-11 (cascaded) |
| **Cite-as nomenclature** | "Layer 6 — European AI Labour Market Synthesis" → "Part 6 — ..." (cascaded across 7 site pages + One-Pager + Long-Read) |
| **launch.json** | `synthesis-site` entry added at port 3006 in worktree's `.claude/launch.json` |
| **Brain — skills** | `skills/layer-site-architecture/` v0.2.1 + `skills/analytical-prose-craft/` v0.1.0 shipped; both landed in main via Path-B merge; BRAIN-INDEX 94 / CANONICAL-COUNTS 94 |
| **Brain — em-dash row** | `skills/linkedin-playbook/references/banned-phrases.md` Tier 2 em-dash row enriched with structural-rewrite-beats-synonym-substitution discipline (3× validated in N3 long-read composition) |
| **Brain — Layer 7 flag** | Earth for All / Club of Rome logged as Phase 1 candidate response framework in `european-ai-labour-actions/RATIONALE.md` |

---

## Work in flight — two sub-sessions ready to dispatch

| Sub-session | Brief path | Effort | Status |
|---|---|---|---|
| **Cards plain-language rewrite** | `cards-plain-language-rewrite-handover-2026-05-09.md` | ~3 h | Phil will dispatch — rewrite 37 country `narrative_one_liner` fields to plain-language one-liners (where/what/lever framing); no schema change; explicit blocklist of technical terms |
| **Scenarios page editorial iteration** | `scenarios-page-iteration-handover-2026-05-09.md` | ~2–3 h | Phil will dispatch — 9 edits including a math fix (S1+S3 combined 25%→5% is wrong; SOT confirms 20%→13%) and a speed-gap explanation addition |

**Both briefs are self-contained.** New master can dispatch them in any order or parallel. Phil typically runs them himself.

---

## Pending page iterations (4 pages still to go)

Phil's flagged that these pages need editorial passes similar to what findings.html got:

1. **europe.html** — within-page Minto already matches overview SM 3; page-level prose may need review
2. **methodology.html** — 4-SM Minto already current; page-level prose may need review; carries internal-vocabulary risk
3. **sources.html** — 59 source-cards (Phase 3.5 additions integrated); per-page version-stamp may need date alignment
4. **glossary.html** — needs review for new "Currently Failing" definition addition

Pattern from this session: Phil pastes tightened locked copy → master applies → cascades to mirror surfaces. Expect 1–3 edits per page.

---

## Final cleanup batch (after all 4 pages iterate + 2 sub-sessions land)

| # | Item | Effort |
|---|---|---|
| 1 | **Italy + Conclusion propagation** to One-Pager (verbatim mirror) + Executive Edition (advisory-track plain-language); **Specialist Appendix keeps technical version** (analyst-track) | ~20 min |
| 2 | **Long-Read PDF regeneration** via `tools/long-read-pdf-gen.py` (current .md has cite-as "Part 6" + "Currently Failing" rename but .pdf is stale from before these edits) | ~5 min |
| 3 | **Footer per-page version-stamp audit** — methodology.html line 198, sources.html line 189, glossary.html line 171 carry "Version 1.0 · Last updated YYYY-MM-DD" stamps; sources.html may want revert to 2026-04-30 (not actually edited 2026-05-11) | ~5 min |
| 4 | **Deploy v1** — Phil handles git + push + Netlify deploy | Phil-managed |

---

## Open Phil-decisions surfaced this session

| # | Question | Status |
|---|---|---|
| 1 | Per-page version-stamp scope (which pages get bumped to 2026-05-11 vs which keep their actual edit date) | Surfaced; Phil hasn't locked |
| 2 | The 3 internal planning docs (`phase3-probability-findings.md`, `phase2-methodology-notes.md`, `phase3-corridor-methodology.md`) still carry "Active Cascade" — update for consistency or leave as historical record | Surfaced; Phil chose "leave" implicitly by moving on |
| 3 | "How the 36 markets split" h3 may have parallel h3 sibling "Most cannot absorb it all" h3 above it — Phil left both; visual check on preview pending | Surfaced; defer |

---

## Working-discipline notes (carry forward)

| Note | Detail |
|---|---|
| **Mirror-text propagation discipline** | When a Phil-locked element updates on index.html, scan + update mirrors in same edit pass: One-Pager (verbatim per Bundle W lock), llms.txt summary, JSON-LD description, OG/twitter meta. The findings.html within-page Minto h2s and meta descriptions are intentionally allowed to differ per the "keep wording differences" preference. |
| **Banned-phrase + structural-rewrite discipline** | linkedin-playbook em-dash row was enriched this session with the n=3-validated finding from N3 long-read: when em-dash rule fires, structural rewriting (numbered inline / bulleted list / parentheses) beats synonym substitution. Apply to any em-dash-density flags. |
| **"Already" vs "Currently" Failing** | Phil iterated this naming: "Active Cascade" → "Already Failing" → "Currently Failing." Currently Failing is the locked term. Cascade everywhere except internal SOT field-name `active_cascade`. |
| **Plain-language register for cards + advisory surfaces** | Phil's locked: no Lens N codes, no Scenario codes (S1–S8), no Corridor codes (C1–C3), no regime codes, no Klinger / Gini / ALMP / ESCO / ISCO / NACE acronyms in user-facing prose. Technical anchors live in chips, footnotes, methodology page only. |
| **Sub-session dispatch pattern** | Phil dispatches sub-sessions himself. Master drafts brief + dispatch prompt; Phil pastes into a separate session; sub-session reports back; master reviews + applies. |
| **Phil does all git commits** | Synthesis project has no `.git` locally; Phil handles git workflow for deploy. Brain repo has worktrees; Phil merged this session's brain work via Path B (file copies into main, Phil commits). |

---

## Files to read in order (next master)

1. **This handover doc** — start here
2. **`master-session-handover-2026-05-08.md`** — prior master handover; many locks still hold
3. **`cards-plain-language-rewrite-handover-2026-05-09.md`** — sub-session #1 ready to dispatch
4. **`scenarios-page-iteration-handover-2026-05-09.md`** — sub-session #2 ready to dispatch
5. **`bundle-n3-v2-iteration-report-2026-05-08.md`** — N3 v2 report (the prior major deliverable)
6. **`bundle-n3-specialist-long-read-report-2026-05-08.md`** — N3 v1 report (foundation)
7. **`site/index.html` + `site/findings.html`** — current state (canonical SOT for overview-page + Findings-page locked copy)
8. **`site/scenarios.html`** — the page sub-session #2 will iterate
9. **`europe.html` / `methodology.html` / `sources.html` / `glossary.html`** — the 4 pages still to iterate
10. **`skills/layer-site-architecture/SKILL.md` + `skills/analytical-prose-craft/SKILL.md`** — the 2 new skills shipped this session
11. **`skills/linkedin-playbook/references/banned-phrases.md`** — Tier 1/2/3 + em-dash row enrichment
12. **`european-ai-labour-actions/RATIONALE.md`** — Layer 7 scope with Earth for All flag

---

## First action for next master

1. Read this handover + the 2026-05-08 master handover.
2. Surface the 2 sub-session dispatch prompts to Phil (cards + scenarios). Phil dispatches.
3. On report-back from each sub-session, review the changes + apply Phil-iteration items.
4. After cards + scenarios land cleanly, work through europe.html / methodology.html / sources.html / glossary.html iteration with Phil (similar pattern: Phil pastes tightened copy, master applies).
5. After all pages iterate, run final cleanup batch (Italy + Conclusion propagation to One-Pager + Executive; Long-Read PDF regeneration; per-page version-stamp audit).
6. Confirm deploy-readiness checklist with Phil; Phil handles deploy.

---

*This handover is the seam between two master sessions. The current master ran ~36 turns of editorial iteration + brain housekeeping + Path-B merge. Two sub-sessions queued; 4 pages still to iterate; final cleanup + deploy after. No re-litigation needed; only forward execution.*
