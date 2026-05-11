# Handover Prompt — Bundle K: Klinger × ISCO-3-Digit Join for Lens 5(c) (Phase 3 Priority 2)

Self-contained prompt for a fresh session. Upgrades Lens 5(c) from the current uniform-velocity proxy (Bundle D Decision 5 deferral) to a Klinger-coordination-share-weighted, employment-weighted score per country. Independent of Bundle J — can run in parallel.

---

## START PROMPT

I need you to execute Phase 3 priority 2: replace the current Lens 5(c) AI labour load score (which uses Phase 1 velocity directly) with a proper Klinger-coordination-weighted, employment-weighted composite. Bundle D Decision 5 deferred this work to Phase 3 with the note "Lens 5(c) currently double-counts Phase 1 velocity rather than weighting by ISCO coordination-share."

This is independent of Bundle J (Phase 3 priority 1). Both can run in parallel. This bundle's output feeds Bundle L (scenario probability weighting).

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — Lens 5(c) definition; locked spec
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-klinger-isco-coordination-share.json` — 130 ISCO 3-digit codes with coordination-layer share (125 derived from ESCO at M-confidence; 5 default fallback). This is the Klinger weighting input.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-data.json` — current Lens 5(c) cells (with Phase 1 velocity proxy)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-methodology-notes.md` §2.3 — Lens 5(c) current methodology + Bundle D Decision 5 deferral note
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-scoring.csv/.json` — current `lens5_ai_labour_load` values to compare against

Do NOT modify any of those. Bundle K produces its own Phase 3 output files.

### Background — what Klinger weighting does

Klinger (2024) framework: AI capability gradient is non-uniform across occupations. Coordination-layer occupations (managers, professional advisors, regulatory, HR/legal) face a deeper compounding penalty from AI-driven labour displacement because their work is structurally more reasoning-heavy, less task-decomposable, and more sensitive to AI's capability floor on judgment-laden work.

Implication for Lens 5(c): countries with high *coordination-layer occupation density* face a different AI labour load than countries dominated by lower-coordination occupations, even at the same headline velocity. DE/AT (Beruf system + management depth), CH (financial/professional services), UK/IE (knowledge-services concentration) should score meaningfully different from countries with manufacturing or agricultural employment dominance.

The current Lens 5(c) doesn't reflect this — it uses Phase 1 country velocity uniformly. This bundle fixes that.

### Task 1 — Acquire per-country ISCO 3-digit employment shares

**Source:** Eurostat LFS occupation-employment data, ISCO 3-digit (the granularity at which the Klinger file is keyed).

**Eurostat datasets to try (in order):**
- `lfsa_egais` — annual employment by ISCO occupation, country, year. ISCO 3-digit availability varies by country.
- `lfsa_egan2` — same with NACE × ISCO 2-digit cross-tab (less granular but more reliable coverage).
- `lfsq_egan22d` — quarterly, ISCO 3-digit. Use latest available year (2024 or 2025).

**Pattern:** SDMX TSV-direct-fetch (per Bundle E session 1's confirmed pattern). URL pattern:
```
https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/{dataset}/?format=TSV&compressed=false&{filters}
```

**Country scope:** EU-27 + NO + IS + LI + CH + UK + 4 candidates (BA/MK/RS/TR).
- LI proxies CH (per Phase 2 convention)
- BA/MK/RS/TR may not have full LFS coverage at 3-digit. Document as data gap; use 2-digit + Klinger 3-digit-aggregated-to-2-digit fallback if necessary.
- UK post-Brexit: may need ONS Annual Population Survey or Eurostat's UK legacy data.

**If 3-digit data is gated/unreliable for some countries:** fall back to ISCO 2-digit + aggregate Klinger coordination-share to 2-digit (employment-weighted within each 3-digit subgroup). Document the per-country granularity choice.

### Task 2 — Compute Klinger × employment composite per country

For each country:
```
lens5c_klinger_weighted = Σ_{isco3} ( employment_share_{isco3} × klinger_coordination_share_{isco3} ) × velocity_country
```

Where:
- `employment_share_{isco3}` = fraction of country employment in ISCO 3-digit code (sum to 1.0 across all ISCO codes)
- `klinger_coordination_share_{isco3}` = value from the Klinger file (0–1)
- `velocity_country` = same Phase 1 velocity used in current Lens 5(c) (so the comparison is apples-to-apples on the velocity-axis; the change is the coordination-share weighting)

Output: per-country `lens5c_klinger_weighted` value, plus `lens5c_klinger_weight` (the country's employment-weighted average coordination-share, isolated from velocity — this is the Klinger-only signal).

### Task 3 — Compare to current Lens 5(c)

For each country:
- `delta_lens5c = lens5c_klinger_weighted − current_lens5_ai_labour_load`
- Categorise as: substantial-up (delta > +0.10), substantial-down (delta < −0.10), or stable (|delta| ≤ 0.10)

**Sanity test:** DE / AT / CH / NL / UK / IE should show the largest positive deltas (high coordination-layer density). If they don't, either the Klinger data or the employment-share data is wrong — surface as methodology gap.

**Anti-sanity test:** PL / RO / BG / HR / countries with manufacturing or agricultural dominance should show the largest negative deltas (lower coordination-layer density).

### Task 4 — Recompute Lens 5 composite drag score

The Lens 5 composite drag score (per `layer-6-phase2-methodology-notes.md` §2.5) currently aggregates:
```
lens5_composite_drag = w_a × polycrisis + w_b × demographic + w_c × ai_labour + w_d × climate_net
```

Recompute with the new `ai_labour` value. Output the new composite per country, alongside the old composite for comparison. Flag countries whose composite drag score shifts substantively (>±0.10) — these are the candidates for fragility-class re-evaluation in Bundle L.

Do NOT re-run fragility-class assignment in this bundle. That's Bundle L's territory (combined with Bundle J's re-calibrated corridors).

### Required outputs

1. **`layer-6-phase3-klinger-rescaled.csv`** — 36 rows × ~10 columns:
   - country_code, country_name, lens5c_klinger_weight (employment-weighted avg coordination-share, isolated), lens5c_klinger_weighted (full score with velocity), current_lens5_ai_labour_load, delta_lens5c, classification (up/down/stable), lens5_composite_drag_old, lens5_composite_drag_new, delta_composite, notes
2. **`layer-6-phase3-klinger-rescaled.json`** — same data structured, plus metadata block with:
   - Eurostat dataset(s) used + per-country granularity choice (3-digit vs 2-digit fallback)
   - countries with data gaps + reason
   - sanity test result (DE/AT/CH/NL/UK/IE direction confirmed)
   - anti-sanity test result (PL/RO/BG/HR direction confirmed)
3. **`layer-6-phase3-klinger-findings.md`** — under 200 lines:
   - Top 5 substantial-up countries + rationale
   - Top 5 substantial-down countries + rationale
   - Sanity test result + any surprises
   - Methodology gaps surfaced (data granularity, candidate-country coverage)
   - Open questions for Bundle L

### Constraints

- BR-19: don't fabricate employment shares. If a country's 3-digit LFS data is gated or unreliable, document the gap and use the 2-digit fallback explicitly.
- BR-21: per-country provenance — `derivation_method` documents which Eurostat dataset, which year, which granularity (3-digit or 2-digit-fallback).
- Do NOT modify Klinger file, Phase 2 outputs, or locked spec.
- Phil does all git commits.
- Eurostat SDMX rate-limiting: backoff between calls; if blocked, fall back to bulk-download + local parse.

### Verification

Before declaring complete:
1. Sum of employment shares per country ≈ 1.0 (within ±0.02 tolerance after sub-totals + unknown-occupation residual).
2. Sanity test: DE/AT/CH/NL/UK/IE among top deltas (positive direction). If not, methodology gap surfaced.
3. Anti-sanity test: PL/RO/BG/HR among top deltas (negative direction). If not, surface.
4. Candidates (BA/MK/RS/TR): explicit data-gap notes if 3-digit unavailable; 2-digit fallback values present.
5. JSON validates; 36/36 countries; no fabricated values.

### When done — report back to master session with

1. Eurostat dataset(s) used + granularity choice per country
2. Sanity test result (top-up countries) + anti-sanity test result (top-down countries)
3. Top 5 substantial deltas in each direction
4. Largest composite-drag shifts (which countries, which direction)
5. Any countries where the Klinger-weighted score crosses a meaningful threshold that would change Lens 5 interpretation
6. Methodology gaps surfaced (data coverage, candidate-country granularity)
7. Open questions for Bundle L (scenario probability) — particularly: which countries' fragility class is now sensitive to Lens 5(c) re-weighting

## END PROMPT
