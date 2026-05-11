# Master Session Handover — Layer 6 Phase 4 (continued)

**Created:** 2026-05-08 (master session ran through 9 phases since picking up from 2026-04-30 handover; context approaching limit)
**For:** the next master session
**Read time:** ~7 min
**Pick up at:** Phil-decision on Phase 3 (scenario/regime completeness audit) before dispatching Bundle W

---

## Project state in one paragraph

Layer 6 is mid-Phase-4 deep cleanup. Since 2026-04-30, the synthesis site has gone through 9 phases (1A → 1B → 2A → 2A.2 ×4 iterations → 2B → 2C → 2D → 2E → 2F → 2H → 2I) covering site content rewrite, IA restructure, design exploration + build, ship-ready audit + cleanup, exhaustive sources audit (15 → 54 primary), source triage (0 shifts/contradicts), typography systematic alignment, container width normalisation. The 7-page site at `synthesis.nexalps.com` is structurally clean and editorially aligned. Bundle W (Minto + locked-copy + 54-source propagation across 5 deliverable docs) is brief-ready but **not yet dispatched**. Phil raised at session-start that a Phase 3 scenario/regime completeness audit should run BEFORE Bundle W, to verify the now-expanded source corpus doesn't support an S9 (e.g., Industrial Reconstruction) or 4th regime (e.g., Wealth-Fund Rich) that the synthesis hasn't captured.

---

## Locked decisions (do not re-litigate)

All Phase 1A → 2I locks from the 2026-04-30 master handover continue to hold. New locks added this session:

| Decision | Lock |
|---|---|
| **Polycrisis Drag** as S8 (was Concurrent-Crisis Cascade) | global rename complete site-side; Bundle W propagates to deliverable docs |
| **4-SM methodology Minto** | SM 1 lenses, SM 2 calibration, SM 3 known gaps, SM 4 ninth-scenario considered-but-excluded. SM 4 is the new addition (was §7 callout in Phase 1B; promoted to top Minto in Phase 2C) |
| **"read" → "this analysis"** site-wide swap | applied; "Five reads" → "Five findings" for plural usage |
| **Glossary EN/DE machinery** | stripped entirely — site is English-only |
| **Container width** | all 7 pages at 1200 px; methodology + sources widened from 760/780 px (overrode article-format convention); per-element max-width 760 px on prose paragraphs |
| **Type scale** | systematically aligned scenarios + europe + methodology + sources to canonical (10/11/12/13/14/15/16/18/20/22/24/28/36 px ladder); 5 fractional sizes rounded; 7 Aligning fixes applied |
| **Sources** | 54 primary (38 Tier 1, 16 Tier 2). Draghi 2024 added Tier 1; Brynjolfsson Li Raymond 2023 added Tier 1 as actual S3 anchor; ILO 2025 reclassified Tier 2 → Tier 1; Canaries source-card rewritten to S6/speed-gap framing (was mislabelled as S3) |
| **Site infrastructure** | netlify.toml at project root; sitemap.xml = 7 pages; llms.txt regenerated from current SOT; PostHog scroll_depth + outbound_click site-wide; second byline on all 7 pages; JSON-LD on all 7 pages (Dataset for data pages, Article for editorial); twitter:description on all 7 pages |
| **Italy block** | plain-prose lead "Italy — the workforce shrinks before AI displaces a single worker"; bold inline `−485,823` (no display-size); no eyebrow; no "load-bearing" |
| **Europe pull-quote** | italic + 20 px + orange `border-left:3px`; bold dropped |
| **Findings § Conclusion** | numbered §6 (matches §1–§5 visual weight) |
| **Banned-phrase scrub** | 0 hits site-wide for `load-bearing`, `structurally`, `structural asymmetry`, `the analysis is built to surface`. Inherited-text scan applied (per the brain rule landed 2026-05-06) |
| **Header / nav** | integrated 6-internal + 5-sister-layer nav matching demographics canonical (lines 184–210); standalone "synthesis · Part 6" wordmark removed |
| **Einfache Sprache section** | dropped from `index.html` + `findings.html` site-side; deliverable docs (`-de.md`, `-en.md`) decision still pending in Bundle W |

---

## Phil-locked verbatim copy (still authoritative)

The 2026-04-30 master handover's Phil-locked copy is still authoritative AND has been augmented:

- **Landing hero, lede, byline** (unchanged from 2026-04-30)
- **4 drill-down page Minto headlines** (unchanged)
- **Europe page Minto open** (unchanged)
- **Silver-lining sentence** (unchanged)
- **Conclusion / Layer 7 closer** (unchanged)
- **NEW — Landing Minto pyramid SMs** (4 SMs with locked headers + supports) — verbatim in `bundle-o-phase-2b-build-handover-2026-05-06.md` and now mirrored on `index.html`
- **NEW — Italy plain-prose block** (verbatim above in Locked decisions)
- **NEW — 4-SM methodology Minto** (SM 1–4 supports, all verbatim in `bundle-w-deliverable-doc-propagation-handover-2026-05-07.md`)
- **NEW — Scenarios phrasing edit** ("growth, secular stagnation, or post-growth stage")
- **NEW — "Why eight scenarios, not more" methodology note** (verbatim, now SM 4 of methodology Minto)
- **NEW — Second byline on all 7 pages** (53 → 54 primary sources after Phase 2F follow-up)

---

## Active sequencing — where we are

| # | Bundle / phase | State |
|---|---|---|
| Phase 1A — Site content rewrite | ✅ |
| Phase 1B — IA restructure | ✅ |
| Phase 2A — Design exploration (12 mockups) | ✅ |
| Phase 2A.2 — Rastered map (4 iterations: 222 → 400 → 762 → 1850 → 1938 cells) | ✅ |
| Phase 2B — Build Phil-locked visuals into live site | ✅ (16/16 PASS) |
| Phase 2C — Editorial + style + IA cleanup | ✅ (21/21 PASS, 24 items) |
| Ship-ready audit | ✅ (24/40 PASS; 9 needs-attention; 7 missing; 3 deploy-blockers) |
| Phase 2D — Ship-ready cleanup (12 items) | ✅ (15/15 PASS) |
| Phase 2E — Sources audit (15 → 53) | ✅ (8/8 PASS, exhaustive cross-layer) |
| Phase 2F — Source triage | ✅ (7/7 PASS, **0 Shifts / 0 Contradicts**, Phase 2G NOT needed) |
| Phase 2F follow-up — Canaries fix + Brynjolfsson Li Raymond add + ILO Tier 1 + 53→54 | ✅ inline by master 2026-05-07 |
| Phase 2H — Typography pass (5 Phil-flagged + audit) | ✅ (10/10 PASS, 7 Aligning + 4 Decisions) |
| Phase 2I — Typography finish (scenarios + europe + container widening) | ✅ (8/8 PASS) |
| **Phase 3 — Scenario/regime completeness audit (Phil's 2026-05-08 question)** | ⏸ **Phil-decision pending — recommend dispatch BEFORE Bundle W** |
| Bundle W — Minto + sources + locked-copy propagation across 5 deliverable docs + One-Pager rewrite + Einfache decision | ✅ brief written (`bundle-w-deliverable-doc-propagation-handover-2026-05-07.md`) ⏸ ready to dispatch |
| Bundle N3 — Specialist Long-Read with graphics | ⏸ not yet briefed — runs after W lands |
| Deploy v1 to live `synthesis.nexalps.com` | ⏸ post-W + N3; Phil-managed git workflow |

---

## Open questions surfaced this session (Phil-decision pending)

| # | Question | Context | Status |
|---|---|---|---|
| 1 | **Phase 3 scenario/regime audit — DISPATCH** | **Phil de-facto locked 2026-05-08** by surfacing 8 PDFs + 6 URLs on the EU Industrial Accelerator Act / Made in Europe 2.0 initiative (Commission proposal 2026-03-04, Switzerland included). This is concrete empirical anchor for an S9 Industrial Reconstruction scenario — the candidate with strongest now-available evidence among the three flagged. | **Lock — dispatch Phase 3 immediately.** Brief must absorb the corpus below as mandatory inputs. |
| 2 | **Einfache deliverable docs decision** | Site-side Einfache dropped (Phase 2C). `layer-6-deliverable-document-einfache-de.md` + `-en.md` still in project. Bundle W brief default = option (b) keep + scope-mark. | Phil locks at Bundle W report-back |
| 3 | **Browser pass on Phase 2I + Phase 2F follow-up** | Phil confirmed browser pass on Phase 2H + 2I 2026-05-07. Final pass on the Italy number reduction + Canaries source-card + 54-source byline still pending; trivial. | At Phil's convenience pre-deploy |

### Phase 3 mandatory inputs (Phil-surfaced 2026-05-08)

The next master MUST hand these to the Phase 3 sub-session as primary source material for the S9 Industrial Reconstruction evaluation:

**EU Commission documents (8 PDFs in `/Users/philippmaul/Downloads/`):**

1. `Proposal establishing measures for industrial capacity and decarbonisation in strategic sectors .pdf` — the legislative proposal text
2. `Executive summary of the impact assessment.pdf`
3. `Impact assessment report.pdf` — the substantive evidence base
4. `Subsidiarity Grid.pdf` — EU-level competence rationale
5. `Annexes to the proposal.pdf` — appendices and detailed provisions
6. `The Industrial Accelerator Act  - factsheet.pdf`
7. `Questions_and_answers_on_the_Industrial_Accelerator_Act.pdf`
8. `Commission_proposes_Industrial_Accelerator_Act_to_strengthen_industry_and_create_jobs_in_Europe.pdf` — press release

**External analytical / political-economy framing (6 URLs):**

1. ECB speech, 2026-02-11: `https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp260211~2822ae9612.en.html`
2. CEPA "Made in Europe 2.0": `https://cepa.org/article/made-in-europe-2-0/`
3. Bruegel: `https://www.bruegel.org/first-glance/made-europe-not-made-europe-should-guide-eu-industrial-policy`
4. EC announcement 2026-03-04: `https://commission.europa.eu/news-and-media/news/commission-proposes-new-measures-boost-eu-industry-and-jobs-2026-03-04_en`
5. EC competitiveness priorities 2024–2029: `https://commission.europa.eu/priorities-2024-2029/competitiveness_en`
6. EC Q&A: `https://ec.europa.eu/commission/presscorner/detail/en/qanda_26_516`

**Phil's framing:** *"the EU is planning a Made in EU(rope) initiative (CH included)."* — Switzerland inclusion matters for the synthesis 36-market scope; Industrial Reconstruction would carry CH on the optimism side, distinct from S2 Climate Adaptation Boom.

### Phase 3 dispatch direction (revised post-2026-05-08 evidence surface)

The Phase 3 brief should now be scoped:

- **Primary candidate (high evidence):** S9 Industrial Reconstruction — the Industrial Accelerator Act corpus above is the empirical anchor. Triage: does the proposal's industrial-capacity-and-decarbonisation framing constitute a distinct labour-absorption mechanism vs S2 (climate sectoral pivot) and S1 (incumbent-firm reinstatement)? Likely yes — government-coordinated industrial buildout via subsidy + procurement + simplified permitting is a different mechanism.
- **Secondary candidate (medium evidence):** 4th regime — Wealth-Fund Rich. Draghi 2024 + Treichl + Klinger captures landed in Layer 7 RATIONALE.md. Triage: does separating wealth-fund-rich from generic post-growth (currently one regime) materially change scenario probability vectors for NO/SE/DK/CH/NL vs DE/FR/IT?
- **Tertiary candidate (revisit-only):** S9 Startup-Driven Absorption — methodology SM 4 already excluded for thin anchors; Brynjolfsson Li Raymond + Massenkoff McCrory + Anthropic don't change the verdict materially. Likely confirms the exclusion stands. Triage briefly.

If Phase 3 surfaces S9 Industrial Reconstruction lock + 4th regime lock, Bundle W scope expands to absorb new taxonomy across deliverable docs in one pass (saves a W.1 follow-up). If only S9 locks (4th regime declined), Bundle W still absorbs in one pass — the regime change is more invasive (every per-country regime tag re-evaluated).

---

## Brain captures landed this session (10 total)

All under `/Users/philippmaul/.claude/projects/-Users-philippmaul-Documents-second-brain/memory/`:

1. `feedback_banned_phrase_propagation.md` (2026-05-06) — banned-phrase scan must apply to inherited text
2. `feedback_mirror_text_propagation.md` (2026-05-06) — mirror-text propagation in same edit pass
3. `feedback_handover_precision_grep_over_table.md` (2026-05-07) — grep is the spec, table is sanity-check
4. `feedback_audit_at_class_at_phase_boundaries.md` (2026-05-07) — **meta-rule consolidating** Phase 2D inherited-content + 2E sources + 2H typography + 2I type-scale audits
5. `feedback_bibliography_vs_data_separation.md` (2026-05-07) — grep SOT for source's named anchor before composing source-card
6. `feedback_hot_spot_triage_first.md` (2026-05-07) — when highest-risk subset converges, drop subsequent triage depth
7. `feedback_display_size_numbers_anti_pattern.md` (2026-05-07) — body-size + bold + accent, not display-size, in body prose
8. `feedback_link_color_single_rule_failure.md` (2026-05-07) — `var(--ring)` on text reserved for active-state and inline-emphasis-number
9. `feedback_container_width_visual_rhythm.md` (2026-05-07) — container width = visual rhythm signal; line-length solved at element level
10. `feedback_fractional_pixel_sizes_clamp_only.md` (2026-05-07) — fractional pixel sizes outside `clamp()`/`calc()` are tweak artefacts; round to canonical slot

The meta-rule (#4) is the load-bearing capture — most of the others are family-instances of it.

---

## Working-discipline notes (carry forward)

| Note | Detail |
|---|---|
| **Audit-at-class beats spot-fix** (the meta-rule) | When Phil flags inconsistency at one spot, audit the whole class systematically. Phase 2D banned-phrase, Phase 2E sources, Phase 2H typography, Phase 2I type-scale all converged on the same lesson. The 4-bucket categorization (Confirms/Refines/Shifts/Contradicts or Necessary/Aligning/Decision) is the standard pattern. |
| **Inherited-text scan applies** | Banned-phrase scan must reach all surfaces, not just newly-authored text. Scan the page, not the draft. |
| **Mirror-text same-pass propagation** | When updating a Phil-locked headline / SM, scan + update every mirror surface (landing-page Minto, executive-doc opener, byline, llms.txt) in the same edit pass. |
| **Grep > table on handovers** | When a handover gives both a grep and a per-instance table, execute grep first; treat table as sanity-check. Flag stale rows in report-back. |
| **Hot-spot triage convergence** | When triaging a class for risk-of-shift, prioritise highest-risk subset first. If hot-spots converge on safe verdict, lighter (not skipped) on remainder. |
| **`var(--ring)` text reservation** | Reserved for: active nav, focus-visible, stat-card values, inline-emphasis bold-number-with-accent. Anywhere else = deviation candidate. |
| **Container width vs line-length** | Container = page-rhythm (consistent across pages). Line-length = reading-rhythm (60–80 chars). Solve independently. |
| **Phil's iteration pattern** | Iterate-on-locks. First draft → Phil-flag → redraft → Phil-polish → lock. Don't skip to "this is locked"; surface drafts as drafts. Captured throughout this session — same pattern as 2026-04-30 master handover. |
| **Phil-locked register** | Plain conversational. No "load-bearing" / "structurally" / "structural asymmetry" / "the analysis is built to surface" / "reads" as singular noun. Storytelling, not methodology paper. |
| **Sub-session honest reporting** | All sub-sessions in this run reported uncertainties cleanly (in-flight bug catches, deviation flags, "data not directly verifiable" notes per BR-19). Continue this discipline. |
| **Phil does all git commits** | Synthesis project has no `.git` locally yet — Phil pushes everything once we're done. |

---

## Files to read in order (next master)

1. **This handover doc** — start here
2. `master-session-handover-2026-04-30.md` — prior master handover (foundation; many locks still hold)
3. `layer-6-phase4-plan-2026-04-29.md` — sequencing tracker (now ~30 rows; current state at top)
4. `bundle-w-deliverable-doc-propagation-handover-2026-05-07.md` — Bundle W brief, ready to dispatch
5. `bundle-o-phase-2f-source-triage-report-2026-05-07.md` — the 0-shifts/0-contradicts triage that cleared synthesis methodologically
6. `site/index.html`, `findings.html`, `scenarios.html`, `europe.html`, `methodology.html`, `sources.html`, `glossary.html` — current site state (canonical SOT)
7. `site/data.json` + `layer-6-deliverable-data.json` — SOT data (unchanged through Phase 2I)
8. `layer-6-lens-framework.md` — lens spec (current)
9. The 10 feedback memory files in `~/.claude/projects/.../memory/feedback_*.md` — process discipline absorbed into the brain
10. `european-ai-labour-actions/RATIONALE.md` — Layer 7 evidence base (Treichl + Klinger captures landed there)

---

## First action for next master

1. Read this handover + the 2026-04-30 prior handover.
2. **Phase 3 is locked** — Phil de-facto confirmed dispatch by surfacing the 8 PDFs + 6 URLs on the EU Industrial Accelerator Act / Made in Europe 2.0 (Open Question #1, Phase 3 mandatory inputs section above). Write the Phase 3 brief absorbing this corpus + the secondary (4th regime) and tertiary (startup-driven absorption revisit) candidates.
3. Phase 3 brief structure (target ~120 lines): flag-only analytical, no SOT edits. Sub-session reads the Industrial Accelerator Act corpus end-to-end (the 8 PDFs + 6 URLs) plus existing Phase 2E/2F outputs. For each candidate (S9 Industrial Reconstruction primary; 4th regime Wealth-Fund Rich secondary; S9 Startup-Driven Absorption tertiary revisit): empirical-anchor strength assessment + mechanism-distinctness check vs existing taxonomy + per-country implication summary. Output: lock-recommend or decline-recommend per candidate with rationale.
4. Phase 3 lands → Phil reviews → locks taxonomy. If additions land, Bundle W brief gets edited to absorb new scenarios/regime; the deliverable docs propagate the new taxonomy in one pass.
5. Bundle W dispatches (existing or expanded) → lands → write Bundle N3 brief (Specialist Long-Read with graphics, ~80 lines).
6. N3 lands → browser pass + deploy v1.

---

## Available tooling for next master

The current session has **computer-use + claude-in-chrome MCP tools available** (deferred but loadable via ToolSearch). Useful for browser-pass verification of the live site. Not needed for handover writing or sub-session dispatch — but next master can use them for visual review before deploy without dispatching a separate sub-session.

---

*This handover doc is the seam between two master sessions. The current master ran 9 phases over ~36 h elapsed time, dispatching ~12 sub-sessions, locking many decisions, propagating extensive content. The next master picks up at Phil's Phase 3 question + Bundle W dispatch with full state preserved. No re-litigation needed; only forward execution.*
