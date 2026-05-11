# Handover Prompt — Phase 3: Scenario / Regime Completeness Audit (Flag-Only)

Bounded analytical sub-session. Audits the locked 8-scenario × 3-regime taxonomy against an expanded source corpus surfaced 2026-04-30 → 2026-05-07 plus the EU Industrial Accelerator Act / Made in Europe 2.0 documents Phil surfaced 2026-05-08. **Output mode: flag-only.** No SOT edits, no source-card edits, no re-derivations. ~4–6 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).** This is mostly a reading + analytical-writing session; code-craft applies only to any inline grep/diff snippets.

---

## Context

Phases 1A → 2I closed: 7-page site, 54 primary sources, locked 8-scenario taxonomy (S1 Reinstatement Revival → S8 Polycrisis Drag), 3-regime classification (`growth_baseline` / `secular_stagnation` / `post_growth_empirical`), 4-SM methodology Minto (SM 4 = "Why eight scenarios, not more" — ninth-scenario considered-but-excluded callout). Phase 2F triage (25 new Tier 1 sources, 13 Tier 2 spot-check) returned **0 Shifts / 0 Contradicts** against existing SOT — synthesis methodologically clean.

Phil raised at master-session start 2026-05-08: with the now-expanded corpus plus the Industrial Accelerator Act PDFs, does an S9 scenario or 4th regime have empirical anchor? The current methodology SM 4 explicitly excluded three candidates with thin anchors. The 2026-04-30 → 2026-05-08 evidence accumulation potentially reopens two of them and adds one new candidate.

**This phase decides: lock taxonomy as-is, or expand before Bundle W dispatches.** If expansion, Bundle W absorbs new scenarios/regime in one pass (saves a W.1 follow-up). Phase 3 produces the recommendation; Phil locks; master executes.

---

## START PROMPT

I need you to audit the locked 8-scenario × 3-regime taxonomy against the expanded source corpus and the Industrial Accelerator Act / Made in Europe 2.0 evidence Phil surfaced 2026-05-08. **Flag-only.** Three candidates with weighted effort: primary (S9 Industrial Reconstruction), secondary (4th regime Wealth-Fund Rich), tertiary (S9 Startup-Driven Absorption revisit). Per-candidate output: lock-recommend or decline-recommend with rationale.

### Read FIRST (absolute paths)

**Existing taxonomy SOT (read for current scenario + regime structure):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — lines 7919–8080 carry S1–S8 mechanism strings; `regime_classification` per country; `regime_split` aggregate
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — lens spec (current locked)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html` — public 8-scenario render (canonical)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/methodology.html` — 4-SM Minto incl. SM 4 ninth-scenario considered-but-excluded
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-o-phase-2f-source-triage-report-2026-05-07.md` — the 0-shifts triage that cleared the synthesis methodologically (Bertheau, Massenkoff, Canaries, Ageing Report, Acemoglu/Restrepo, Bessen, Levy, OECD Surveys)

**Phase 3 mandatory inputs — Industrial Accelerator Act corpus (Phil-surfaced 2026-05-08):**

EU Commission documents (8 PDFs in `/Users/philippmaul/Downloads/`):
1. `Proposal establishing measures for industrial capacity and decarbonisation in strategic sectors .pdf` — legislative text (1.3 MB)
2. `Executive summary of the impact assessment.pdf` (276 KB)
3. `Impact assessment report.pdf` — substantive evidence base (10 MB)
4. `Subsidiarity Grid.pdf` — EU-level competence rationale (540 KB)
5. `Annexes to the proposal.pdf` (257 KB)
6. `The Industrial Accelerator Act  - factsheet.pdf` (260 KB) — note the double space in filename
7. `Questions_and_answers_on_the_Industrial_Accelerator_Act.pdf` (44 KB)
8. `Commission_proposes_Industrial_Accelerator_Act_to_strengthen_industry_and_create_jobs_in_Europe.pdf` — press release (50 KB)

External analytical / political-economy framing (6 URLs, fetch via WebFetch):
1. ECB speech 2026-02-11: `https://www.ecb.europa.eu/press/key/date/2026/html/ecb.sp260211~2822ae9612.en.html`
2. CEPA "Made in Europe 2.0": `https://cepa.org/article/made-in-europe-2-0/`
3. Bruegel: `https://www.bruegel.org/first-glance/made-europe-not-made-europe-should-guide-eu-industrial-policy`
4. EC announcement 2026-03-04: `https://commission.europa.eu/news-and-media/news/commission-proposes-new-measures-boost-eu-industry-and-jobs-2026-03-04_en`
5. EC competitiveness priorities 2024–2029: `https://commission.europa.eu/priorities-2024-2029/competitiveness_en`
6. EC Q&A: `https://ec.europa.eu/commission/presscorner/detail/en/qanda_26_516`

**Phil's framing 2026-05-08:** *"the EU is planning a Made in EU(rope) initiative (CH included)."* — Switzerland inclusion matters for the synthesis 36-market scope (the corpus must be read for CH-specific provisions or association arrangements; Industrial Reconstruction would carry CH on the optimism side, distinct from S2 Climate Adaptation Boom).

**Brain context (load if scope expands per CLAUDE.md Step 2 re-trigger):**
- `contexts/personal.md` (always loaded)
- `contexts/behavioral-rules.md` — BR-19 fabrication discipline applies throughout (cite from corpus, do not bolt in plausible-but-unverified examples; 3 BR-19 hits in Apr 15 session as a recurrence pattern)
- If the audit surfaces a regulatory-strategy angle, consult agent profiles for Eric Demuth / Käärmann (regulatory + European scaling) — flag-only, not load-and-respond

### Three candidates — weighted effort

**PRIMARY: S9 Industrial Reconstruction (high evidence, Phil-surfaced anchor)**

The Industrial Accelerator Act corpus is the empirical anchor. Triage:

1. **Mechanism distinctness vs S1 / S2 / S4** — does government-coordinated industrial buildout via subsidy + procurement + simplified permitting constitute a separate labour-absorption mechanism, or does it collapse into:
   - S1 Reinstatement (incumbent firms expand) — likely no; S1 mechanism is endogenous reinstatement, not state-coordinated
   - S2 Climate Adaptation Boom (sectoral pivot via Net-Zero Industry Act €100B) — partial overlap; the Accelerator Act is broader-than-climate (defence, semiconductors, biotech, raw materials per impact assessment scope). Read the proposal text for the strategic-sectors list and check whether overlap is partial or near-total
   - S4 Muddle Through (default residual) — likely no; the Act is an active policy intervention, not residual
2. **Per-country implication** — which of the 36 markets does the Act materially change probability for? Read for: CH inclusion mechanism (association arrangement vs. excluded), candidate-country provisions (TR/MK/RS/AL), EU-27 differentiation (programme-eligible high-coordination markets vs. liberal-market markets that may not capture flows). Flag CH-specific findings explicitly.
3. **Evidence-base strength** — the impact assessment report (10 MB) is the substantive document. Check for: labour-market projections (job-creation estimates by sector and country), absorption-channel framing (is it explicit about reskilling vs. greenfield hiring vs. internal redeployment), implementation timeline (does the 5–10 yr horizon align with synthesis Layer 6 corridor-window).
4. **Regime conditioning** — does the Act change probability vectors more under `growth_baseline`, `secular_stagnation`, or `post_growth_empirical`? Cross-reference Bruegel + CEPA framings for the political-economy view on which member states benefit asymmetrically.

Output: lock-recommend or decline-recommend S9 Industrial Reconstruction. If lock, draft (a) the SOT-style mechanism string (~80–120 words, S3-equivalent format), (b) per-regime probability vector estimate with CI band, (c) per-country corridor-implication summary for the 6–10 most-affected markets, (d) source-card draft for sources.html (Tier 1, ~5 lines per existing schema). All flag-only — Phil locks before any SOT edit.

**SECONDARY: 4th regime — Wealth-Fund Rich (medium evidence)**

Current regime structure collapses NO/SE/DK/CH/NL/LU into `post_growth_empirical` alongside DE/FR/IT/AT/FI. The hypothesis: sovereign wealth and fiscal-capacity differences are large enough that the absorption mechanism diverges. Triage:

1. **Empirical anchor** — Draghi 2024 (already Tier 1) + Treichl + Klinger captures landed in `european-ai-labour-actions/RATIONALE.md` Layer 7 evidence base. Read these for the wealth-fund-rich-vs-fiscally-constrained split rationale.
2. **Mechanism distinctness vs `post_growth_empirical`** — does separating wealth-fund-rich materially change which scenario is modal for NO/SE/DK/CH/NL vs. DE/FR/IT? Currently S2 is modal under post-growth (P(S2|post_growth)=0.30). If wealth-fund-rich permits S1 reinstatement to remain viable (fiscal headroom for ALMP + industrial policy), the modal scenario flips for the wealth-fund-rich subset.
3. **Per-country implication** — five candidates split out: NO (sovereign wealth fund), SE (large pension assets), DK (large pension assets), CH (current-account surplus, SNB reserves), NL (pension assets, current-account surplus); LU edge case (financial centre, small workforce). Check whether the L4/L5 enrichment data (Bundle P/R outputs) surfaces fiscal-headroom proxies that materially separate this subset from DE/FR/IT.
4. **Cost-benefit of expansion** — a 4th regime is more invasive than an S9 addition: every per-country regime tag re-evaluated, every probability vector re-derived (3-regime → 4-regime split). Estimate the re-derivation footprint (number of country records affected, number of SOT fields touched).

Output: lock-recommend or decline-recommend Wealth-Fund Rich regime. If lock, draft (a) the regime definition + qualifying-criteria threshold (e.g., sovereign-wealth assets %GDP > X, or current-account surplus 5-yr avg > Y%GDP), (b) per-country reclassification list, (c) re-derivation footprint estimate, (d) modal-scenario change estimate (which countries' modal scenario flips). Flag-only.

**TERTIARY: S9 Startup-Driven Absorption (revisit-only)**

Methodology SM 4 already excluded for thin anchors. Phase 2F new sources (Brynjolfsson Li Raymond 2023 RCT, Massenkoff & McCrory 2026, Anthropic Economic Index) are productivity / entry-level / occupation-level evidence, not startup-formation evidence. Triage briefly:

1. Confirm SM 4 exclusion still stands — the new sources do not change the verdict.
2. If they do (unlikely), surface the specific finding that flips it.

Output: 1-paragraph confirm-or-flip. Most likely confirms exclusion — light effort.

### Output structure (target ~80–120 lines, flag-only report)

Mirror the Phase 2F triage report format:

1. **TL;DR** (5–7 bullets): per-candidate verdict, source-card audit gaps if any, regime-split footprint estimate, dispatch implications for Bundle W
2. **PRIMARY: S9 Industrial Reconstruction** (~30–40 lines): mechanism, distinctness check, per-country implications, evidence-base summary, regime conditioning, lock-recommend/decline + rationale, draft mechanism string + draft probability vector + draft source-card
3. **SECONDARY: 4th regime Wealth-Fund Rich** (~20–30 lines): empirical anchor, distinctness, per-country split, re-derivation footprint, modal-scenario change, lock-recommend/decline + rationale, draft regime definition
4. **TERTIARY: S9 Startup-Driven Absorption** (~5–10 lines): confirm-exclusion or flip-recommend
5. **Cross-candidate dependencies**: do S9 Industrial Reconstruction + 4th regime interact? (E.g., does the Act preferentially benefit wealth-fund-rich markets through co-financing structures?)
6. **Bundle W dispatch implication**: scope-as-written, scope-expanded-S9-only, scope-expanded-S9-plus-regime — three estimates of the propagation work
7. **Brain capture candidates** (if any surfaced; do not auto-write — surface for Phil per Rule 12)

### Discipline (carry forward from prior phases)

- **Banned-phrase scan on own draft before surfacing.** Tier 1/2/3 reference: `skills/linkedin-playbook/references/banned-phrases.md`. Run grep on the draft for: `load-bearing`, `structurally`, `structural asymmetry`, `the analysis is built to surface`, `reads` as singular noun, fragment-then-colon openers (`Below: `, `Key: `).
- **BR-19 fabrication discipline.** Cite from the corpus. If a finding is not in the 8 PDFs + 6 URLs + Phase 2F triage report, do not bolt it in. Three BR-19 hits in the Apr 15 session — this is a known recurrence pattern. If the impact assessment does not give a per-country labour estimate for CH, write "no per-country CH estimate in the impact assessment" rather than inferring.
- **Honest deviation reporting.** If the corpus is silent on a triage criterion (e.g., the Act says nothing about absorption channels, only about industrial capacity), flag the silence — do not invent.
- **No SOT edits.** Verify md5 checksums on `site/data.json`, `layer-6-deliverable-data.json`, `layer-6-lens-framework.md`, `site/scenarios.html`, `site/methodology.html`, `site/sources.html` are identical pre-/post-session.
- **Plain conversational register.** Storytelling, not methodology paper. Phil's editorial pattern is iterate-on-locks; surface drafts as drafts.
- **Audit-at-class lens** (the meta-rule from `feedback_audit_at_class_at_phase_boundaries.md`). When you find one finding that suggests S9 Industrial Reconstruction is mechanism-distinct, also audit S2 Climate Boom and S1 Reinstatement Revival mechanism strings to check whether they need refinement to preserve distinctness.

### Verification (close with this)

```
md5 site/data.json layer-6-deliverable-data.json layer-6-lens-framework.md \
    site/scenarios.html site/methodology.html site/sources.html
```

Match to pre-session run. Flag any drift.

### Report-back format

Single markdown file: `phase-3-scenario-regime-completeness-audit-report-2026-05-08.md`. Same directory. Phil reviews → locks taxonomy. Master either dispatches Bundle W as-written (all decline-recommends) or edits Bundle W to absorb new scenarios/regime in one pass.

---

## Out of scope

- SOT edits, source-card edits, re-derivations (Phase 3.G if locks land, scoped separately)
- Layer 7 / `european-ai-labour-actions/` content (the Act may have policy-response implications for Layer 7, but Layer 7 builds post-Layer-6 ship; flag-only mention is acceptable)
- Sister-layer-site updates (L1–L5 stay live; not Phase 3's concern)
- Brain skill enrichment — capture candidates surface for Phil per Rule 12, do not auto-write

---

*This brief is the dispatch prompt for the Phase 3 sub-session. Sub-session reads the Industrial Accelerator Act corpus end-to-end, triages three candidates against existing taxonomy, returns a flag-only report. Phil locks. Bundle W dispatches with or without expansion.*
