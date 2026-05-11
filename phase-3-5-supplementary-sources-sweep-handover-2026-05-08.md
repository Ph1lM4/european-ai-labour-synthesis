# Handover Prompt — Phase 3.5: Supplementary-Sources Sweep (Light-Touch)

Bounded research sub-session. Targeted WebSearch on 3 named topics to harden the Phase 3 audit verdicts and source SM 4 v2 attribution. **Output mode: flag-only, source-shortlist deliverable.** No SOT edits, no source-card edits, no re-derivations. ~3–4 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).** This is a research + analytical-writing session; code-craft applies only to inline grep/diff snippets.

---

## Research scope

**Corpus + targeted sweep on the following 3 topics. No open-ended WebSearch beyond these.**

The Phase 3 audit ([phase-3-scenario-regime-completeness-audit-report-2026-05-08.md](phase-3-scenario-regime-completeness-audit-report-2026-05-08.md)) returned three decline-recommends (S9 Industrial Reconstruction, 4th regime Wealth-Fund Rich, S9 Startup-Driven Absorption). Verdicts are robust, but the methodology SM 4 v2 callout would be stronger if it could cite counterfactual sources beyond the EC IAA corpus + existing brain triage. This sweep adds the strongest-2-3 sources per topic for SM 4 v2 attribution + verdict hardening.

---

## Context

Phase 3 ran on the EC IAA corpus (8 PDFs + 6 URLs) Phil surfaced 2026-05-08 plus existing Phase 2F triage corpus + SOT. The brief did not specify whether independent WebSearch was in scope; sub-session ran corpus-only. Phil flagged post-hoc that adjacent counterfactual evidence (IRA labour outcomes, sovereign-wealth-fund-headroom datasets, ETUC/Eurofound IAA reception) would strengthen the audit narrative without flipping any verdict.

**This phase: harden the verdicts + source SM 4 v2.** Three named topics. Strongest-2-3 sources per topic. ~3-4 h sweep. Output is a sources shortlist for SM 4 v2 attribution + a 1-paragraph verdict-robustness check per topic.

---

## START PROMPT

I need you to run a targeted-sweep WebSearch on three specific topics to harden the Phase 3 audit verdicts and source SM 4 v2 attribution. **Flag-only, source-shortlist deliverable.** ~3-4 h.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/phase-3-scenario-regime-completeness-audit-report-2026-05-08.md` — the audit verdicts this sweep is hardening
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/methodology.html` — SM 4 ninth-scenario callout (the surface SM 4 v2 will replace)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-o-phase-2f-source-triage-report-2026-05-07.md` — existing triage to avoid duplicating
- `/Users/philippmaul/Documents/projects/DATA-REGISTRY.md` — check before any external fetch (per `feedback_data_registry_check_first.md`)

### Three topics — strongest-2-3 sources per topic

**Topic 1 — IRA labour outcomes (US Inflation Reduction Act, 2022-2025)**

Why: the IRA is the strongest counterfactual for state-coordinated industrial buildout labour absorption — same mechanism class as the IAA but ~3 years of post-implementation labour data available. If the IRA produced a qualitatively different labour-absorption pathway than S2 Climate Adaptation Boom predicts, the Phase 3 S9 decline-recommend is weakened.

Search targets (illustrative, not exhaustive):
- US Treasury IRA implementation reports (labour-outcome data)
- BLS retrospectives on IRA-eligible sectors 2024-2025
- Bistline et al. (Princeton REPEAT Project) — IRA labour modelling vs. realised
- Goulder et al. — IRA macro-labour outcomes
- Rhodium Group / Energy Innovation tracking reports

Output per topic: 2-3 strongest sources by combination of (a) primary-data anchor, (b) recency (2024-2025 preferred), (c) labour-mechanism-relevance to the S9-vs-S2 distinction.

**Topic 2 — Sovereign-wealth / fiscal-headroom per-country proxies for the 4th regime operationalisation**

Why: the Phase 3 4th regime decline-recommend was on operationalisation-gap grounds — direction (NO/SE/DK/CH/NL distinct from DE/FR/IT under post-growth) was empirically defensible, but no per-country sovereign-wealth-headroom proxy in the surfaced corpus to threshold the regime. If a strong proxy dataset surfaces, the operationalisation-gap argument weakens; if no proxy is publicly available, the decline hardens.

Search targets:
- IMF Sovereign Wealth Fund database (if extant; check first)
- OECD net-financial-asset / sovereign-wealth datasets
- SWF Institute (`SWFI`) public data + methodology
- NBIM / Temasek / GIC / SNB labour-market-stabilisation literature
- Bank for International Settlements working papers on sovereign-wealth + fiscal-stabilisation
- Resource-rich-vs-resource-poor advanced-economy comparators (academic, IMF WP, OECD WP)

Output: which dataset (if any) provides per-country thresholdable sovereign-wealth or fiscal-headroom data for the 36-market scope (or at least for the 5 candidates: NO/SE/DK/CH/NL). 2-3 strongest sources.

**Topic 3 — ETUC / Eurofound / labour-side framing of the IAA + Made in Europe 2.0**

Why: the EC IAA corpus is the proposing-side framing. The labour-side framing (worker-protection, sectoral employment effects, distributional concerns) is a different epistemic vantage. If ETUC / Eurofound / national-trade-union positions diverge significantly from the EC labour projections, the Phase 3 mechanism-collapse-into-S2 finding may need refinement (e.g., labour-side frames the absorption as conditional on works-council mediation, which is a non-trivial mechanism component not in S2 currently).

Search targets:
- ETUC position papers on the IAA / Made in Europe 2.0 (2026 or late 2025)
- Eurofound foundation findings on EU industrial-policy labour effects
- National-level union responses (DGB Germany, CGT/CFDT France, Confindustria opposite-side as comparator)
- IndustriAll Europe positions
- Bruegel / CEPS / EUI labour-side analyses on the Accelerator Act

Output: 2-3 strongest labour-side sources. Flag any mechanism-component the Phase 3 audit would refine if the source were absorbed (e.g., "ETUC frames absorption as conditional on works-council mediation — this is currently absent from S2 mechanism string").

### Output structure (target ~50–80 lines)

Single markdown file: `phase-3-5-supplementary-sources-sweep-report-2026-05-08.md`. Mirror Phase 2F + Phase 3 report formats.

1. **TL;DR** (3–5 bullets): per-topic verdict-robustness check (verdict holds / verdict softens / verdict flips); SM 4 v2 attribution shortlist (5–7 sources max across the 3 topics)
2. **Topic 1 — IRA labour outcomes.** 2–3 sources with: full citation, primary-data anchor summary, S9-vs-S2 mechanism-relevance assessment, verdict-robustness verdict (holds / softens / flips)
3. **Topic 2 — Sovereign-wealth / fiscal-headroom proxies.** Same structure. Plus: explicit "is there a thresholdable per-country dataset for the 5 candidate markets?" answer
4. **Topic 3 — ETUC / labour-side framing.** Same structure. Plus: explicit "any mechanism-component refinement candidate for S2 mechanism string?" answer
5. **SM 4 v2 attribution shortlist.** 5–7 sources (across all 3 topics) ranked for citation in the methodology SM 4 v2 callout. Phil locks; master uses these in SM 4 v2 draft
6. **Cross-topic findings (if any).** Surface anything that emerges from comparing the 3 topics (e.g., does IRA experience inform the SWF-headroom argument?)
7. **Brain capture candidates** (if any surfaced; do not auto-write — surface for Phil per Rule 12)

### Discipline (carry forward)

- **DATA-REGISTRY.md check first.** Before any external fetch, grep `/Users/philippmaul/Documents/projects/DATA-REGISTRY.md` for the topic. Sources may already be local (per `feedback_data_registry_check_first.md`).
- **Banned-phrase scan on own draft before surfacing.** Tier 1/2/3 reference: `skills/linkedin-playbook/references/banned-phrases.md`. Grep for: `load-bearing`, `structurally`, `structural asymmetry`, `the analysis is built to surface`, `reads` as singular noun, fragment-then-colon openers.
- **BR-19 fabrication discipline.** Cite from sources read. If a source's labour-outcome claim is paraphrased from a secondary summary, flag it as such. Do not bolt in plausible-but-unverified specifics. Per `feedback_invent_by_name_similarity.md` and `feedback_curated_index_attribution_unreliable.md`.
- **Pre-read framing as invitation, not anchor** (per `feedback_preread_framing_as_invitation.md`, captured this session): the topic descriptions above carry hypotheses about what the sources will say (e.g., "IRA produced ~X jobs by sector"). Treat as hypotheses; verify against the actual sources.
- **No SOT edits.** Verify md5 checksums on `site/data.json`, `layer-6-deliverable-data.json`, `layer-6-lens-framework.md`, `site/scenarios.html`, `site/methodology.html`, `site/sources.html` are identical pre-/post-session.
- **Honest deviation reporting.** If a topic returns no strong sources, say so. Do not pad to hit 2-3 per topic. The shortlist is the deliverable; an honest "no strong source surfaced for Topic 2" is more useful than a weak third.
- **Time budget: 3-4 h.** If a topic balloons (Topic 2 SWF data scoping, in particular), surface the scoping issue and stop at the budget. Do not grind.

### Verification (close with this)

```
md5 site/data.json layer-6-deliverable-data.json layer-6-lens-framework.md \
    site/scenarios.html site/methodology.html site/sources.html
```

Match to pre-session. Flag any drift.

### Report-back format

Single markdown file: `phase-3-5-supplementary-sources-sweep-report-2026-05-08.md`. Same directory. Phil reviews → master uses SM 4 v2 attribution shortlist to draft SM 4 v2 → Phil locks SM 4 v2 → Bundle W brief edited to absorb SM 4 v2 → Bundle W dispatches.

---

## Out of scope

- SOT edits, mechanism-string edits, source-card edits (those happen in Bundle W if SM 4 v2 lock requires them)
- Brain skill enrichment — capture candidates surface for Phil per Rule 12
- Acquiring full PDFs of the surfaced sources unless trivially available (the shortlist is the deliverable; full ingestion is Phase 5+ scope if pursued)
- Sister-layer-site updates (L1–L5 stay live)

---

*This brief is the dispatch prompt for the Phase 3.5 supplementary-sources sweep. Sub-session WebSearches on 3 named topics, returns a 5-7 source shortlist for SM 4 v2 attribution + verdict-robustness check per topic. Phil reviews → master drafts SM 4 v2 → Phil locks → Bundle W absorbs.*
