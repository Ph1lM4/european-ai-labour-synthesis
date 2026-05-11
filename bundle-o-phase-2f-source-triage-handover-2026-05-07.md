# Handover Prompt — Bundle O Phase 2F: New-Sources Triage (Flag-Only)

Bounded research session. Triages the 25 new Tier 1 sources from Phase 2E against the synthesis SOT to determine whether any of them carry data that would *shift* current findings if integrated, vs merely *confirm/refine* them. Flag-only — no SOT edits, no re-derivation, no source-card edits. Output is a 4-bucket triage report. If anything lands as Shifts or Contradicts, Phil decides whether to dispatch a follow-up Phase 2G to re-derive. ~2 h.

**No code task** — this is research + analytical adjudication, not code generation.

---

## Context

Phase 2E added 38 sources (25 Tier 1 + 13 Tier 2) to the synthesis bibliography after an exhaustive cross-layer audit. The audit attached source-cards to existing findings they were assumed to support. But Phase 2E did not verify whether each source's *actual data* aligns with the synthesis SOT — it verified that each source maps to a finding the synthesis already makes.

Risk: some new Tier 1 sources (especially recent empirical work like Massenkoff & McCrory 2026 and Brynjolfsson et al. 2025) carry data that, if integrated, would shift per-country placements, thresholds, or scenario probabilities. The synthesis findings are locked since Bundle V (2026-04-30); shifts would require re-derivation.

Phase 2F is the triage that splits the analytical risk from the execution cost. Pure flag-only — sub-session reviews each new Tier 1 source, categorizes, reports. No edits.

---

## START PROMPT

I need you to triage the 25 new Tier 1 sources added in Phase 2E against the synthesis SOT and report whether each *confirms*, *refines*, *shifts*, or *contradicts* the corresponding synthesis finding. No SOT edits, no source-card edits, no re-derivations — pure flag-only triage.

### Read FIRST (absolute paths)

**Synthesis SOT (read-only):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/data.json` — per-country fragility classes, baseline corridors, regime tags, scenario probability vectors, lens 1 ratios, mechanism narratives, cross-cutting findings
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — master SOT (mirrors site/data.json)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — lens-by-lens spec including thresholds (1.20 / 2.80 corridor edges, 80% retirement-offset buffer, etc.)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/findings.html` — narrative for the five mechanism findings + Italy + the two-buffers framing
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html` — eight scenarios + three regimes + per-scenario probability vectors
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/methodology.html` — five lenses + corridor-edge calibration + ninth-scenario-considered note

**Phase 2E additions (read for "how informs" mapping):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/sources.html` — the 38 new source-cards (each has an explicit "how informs" line naming the lens / scenario / finding it underpins per Phase 2E)

**Sister-layer source-cards (read for what data each source contributes):**
- `/Users/philippmaul/Documents/projects/european-ai-exposure-map/site/sources.html` (L1)
- `/Users/philippmaul/Documents/projects/european-careers-map/site/sources.html` (L2)
- `/Users/philippmaul/Documents/projects/european-disruptions-map/site/sources.html` (L3)
- `/Users/philippmaul/Documents/projects/european-demographics-map/site/sources.html` (L4)
- `/Users/philippmaul/Documents/projects/european-reskilling-map/site/sources.html` (L5)

**Project registry:**
- `/Users/philippmaul/Documents/projects/DATA-REGISTRY.md` — local copies of dataset files; check whether any of the 25 sources have downloaded data accessible offline

### Triage procedure

For each of the **25 new Tier 1 sources** (NOT the 13 Tier 2 — those are framing/contextual, unlikely to shift data; sub-session optionally sanity-checks Tier 2 only if surface inspection suggests a contradiction):

**Step 1 — Identify the synthesis finding the source maps to.**
From the synthesis sources.html "how informs" copy plus the SOT field it would feed (per-country lens 1 ratio, fragility class, regime tag, scenario probability, threshold value, etc.).

**Step 2 — Read the source's actual data summary.**
Three approaches in order of cost:
1. **Cheapest:** read the sister-layer's existing source-card "how informs" / "key findings" copy. Sister-layer cards typically name the specific number, threshold, or mechanism the source contributes.
2. **Medium:** if a local copy exists per `DATA-REGISTRY.md`, read the relevant data field directly.
3. **Heavier:** if neither yields a usable summary, read the source's abstract / methodology section / key tables (skim only — do not read papers end-to-end).

If the source's actual data cannot be verified from any of these three (paywalled, not in registry, no usable summary), flag as **"Data not directly verified — based on sister-layer mapping"** and proceed with the triage based on the sister-layer summary.

**Step 3 — Categorize.**

| Bucket | Definition | Action |
|---|---|---|
| **Confirms** | Source data aligns with the corresponding synthesis SOT field (within ±5% or within the documented CI band). | No change needed. Citation strengthens existing finding. |
| **Refines** | Source data narrows / sharpens the synthesis finding (more specific number, narrower CI, additional dimension) without changing the substantive direction. | Low-risk update candidate. Note for Phase 2G if Phil dispatches. |
| **Shifts** | Source data would change a per-country fragility-class assignment, corridor placement, regime tag, scenario-probability mid-point, or threshold value if integrated. | Phil-decision: re-derive in Phase 2G or document as known divergence. |
| **Contradicts** | Source data directly conflicts with the corresponding synthesis finding (different sign, different mechanism, different conclusion). | Phil-decision: re-derive, contest, or document as a known limit in §7 methodology. |

**Step 4 — Magnitude estimate (Shifts + Contradicts only).**

For each Shift / Contradict, name:
- Which SOT fields would change (e.g., "FR fragility-class IIa → III", "S3 mid-prob under post-growth 0.05 → 0.10–0.15", "corridor edge 1.20 → 1.10")
- How many countries / fields are affected
- Confidence: High (data is direct + verified) / Medium (data inferred from summary) / Low (data not directly verified)

### The 7 hot-spots flagged in adjudication

These are the highest-risk sources Phil flagged at dispatch time. Sub-session prioritises these first; if any land as Shifts or Contradicts, the rest of the triage may rest on the implications:

1. **Bertheau et al. 2022 (IZA DP 15033)** — A→C transition rates per country (AT/DK/FR/IT/PT/ES/SE)
2. **Massenkoff & McCrory 2026 (Anthropic Labor Market Impacts)** — entry-level AI signal
3. **Brynjolfsson, Chandar & Chen 2025 (Canaries in the Coal Mine)** — S3 Jobs Transform mechanism
4. **OECD SOCX (ALMP training-category spend)** — per-country ALMP intensity
5. **EC 2024 Ageing Report** — working-age trajectory + fiscal headroom (regime classification input)
6. **Acemoglu & Restrepo 2020 (Robots and Jobs JPE)** — C3 corridor anchor / robots-displacement thresholds
7. **ILO 2025 (Generative AI Occupational Exposure Index)** — third-index Lens 1 cross-check

Triage these 7 first; report findings; then triage the remaining 18.

### Constraints

- **No SOT edits.** `data.json`, `layer-6-deliverable-data.json`, `layer-6-lens-framework.md`, all 7 site HTML files, `sources.html` source-cards, `llms.txt` — all untouched. `git status` should show zero changes after the session.
- **No re-derivation.** Even if a Shift is obvious, do not update SOT fields. Surface the Shift in the report.
- **No source-card edits.** The Phase 2E source-cards stay as they are. If a Phase 2E "how informs" copy turns out to be wrong relative to the source's actual data, flag in the report — do not edit.
- **Honest reporting.** If data is not directly verifiable for a source, flag explicitly. Do not infer beyond what the sister-layer summary supports. Per BR-19: cite what's verified, flag the gap; do not fabricate.
- **No new tooling.** No web scraping, no paid-paper access, no API calls. Use existing local files + sister-layer summaries + DATA-REGISTRY local copies.
- **Phil does all git commits.**

### Verification (before reporting back)

1. All 25 new Tier 1 sources reviewed (or all 38 if sub-session opts to spot-check Tier 2 too).
2. Each source has a triage verdict (Confirms / Refines / Shifts / Contradicts) + a confidence level.
3. Any Shifts or Contradicts have a magnitude estimate (which SOT fields, how many countries, what direction).
4. Any "Data not directly verified" sources are flagged.
5. SOT files untouched (`md5sum site/data.json layer-6-deliverable-data.json` matches pre-session checksum).
6. No edits to source-cards in `sources.html`.
7. No edits to any site HTML or markdown.

### When done — report back to master session with

1. **4-bucket triage summary table** — 25 Tier 1 sources sorted by bucket, with confidence level per row.
2. **Hot-spot deep-dive** — the 7 flagged sources, with explicit data citation (number / threshold / mechanism summary) + comparison against current synthesis SOT.
3. **Shifts list** — every Shift verdict, with: source, SOT fields affected, direction + magnitude of shift, country count, confidence.
4. **Contradicts list** — every Contradict, with: source, finding contradicted, nature of conflict, recommended path (re-derive / contest / document as limit).
5. **Phase 2E source-card audit gap** — any Phase 2E "how informs" copy that turns out misaligned with the source's actual data (flag for follow-up correction, do not edit).
6. **Phase 2G readiness** — if any Shifts / Contradicts, scope estimate for Phase 2G re-derivation (how many SOT fields, expected complexity, blast radius across the 7 site pages + deliverable docs).
7. **Phase 2G NOT-needed verdict** — if all sources land as Confirms / Refines, explicit "no re-derivation needed; deploy as-is" recommendation.
8. **Any candidate brain captures** — likely a process pattern around bibliography-vs-data audit separation (the family with Phase 2E's sources-audit-at-phase-boundary rule).

## END PROMPT
