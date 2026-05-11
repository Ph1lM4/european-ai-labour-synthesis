# Handover Prompt — Bundle X: Pan-European Aggregate Computation

Bounded analytical session. Computes pan-European aggregate readings (EU-27 + full 36-market) and adds them to the SOT JSON as a new `cross_cutting_findings.pan_european_aggregate` block. Downstream rendering happens in Phase 1B (new `europe.html` page) and Bundle W (deliverable docs reframe). ~45–60 min.

---

## Context

Phil-locked decision (2026-04-30 evening, master session): the Layer 6 deliverable surface needs an explicit pan-European read alongside the per-country corridor map. Two reasons:
1. **Reader need.** Executive / policy / advisory audience naturally asks "what's the European picture?" — currently the answer is scattered across `cross_cutting_findings` (zone heterogeneity, capacity gap, breach scope, squeeze cluster, class distribution) without a single aggregate anchor.
2. **Layer 7 Tier 1 dependency.** The Draghi-shaped legislative deliverable will need a single pan-European corridor + class + probability read.

Bundle X computes BOTH aggregations:
- **EU-27** (the political entity): the natural "what about the EU?" anchor
- **Pan-European 36-market** (full Layer 6 scope): EU-27 + EFTA-4 (CH, IS, LI, NO) + UK + 4 candidates (BA, MK, RS, TR)

Both readings live in the SOT; the new `europe.html` page (built in Phase 1B) renders them as parallel anchors. Phil decides which becomes the primary headline at render time.

**Important methodological caveat (encoded in the SOT block + flagged for the executive register):** a single aggregate corridor placement risks **diluting the structural-bias finding** (the analytical surface is that there's no single answer; the 36-market variation IS the read). Bundle X must include a "variation guard" — every aggregate scalar surfaces alongside the distribution it summarises, never alone.

---

## START PROMPT

I need you to compute pan-European aggregate readings (EU-27 and full 36-market) and add them to the SOT JSON. This is analytical work — no rendering, no deliverable doc updates. Phase 1B builds the dedicated `europe.html` page reading from the SOT; Bundle W (post-Phase-2) updates the deliverable docs.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — SOT JSON post-Bundle-V (S1–S8 renumbering; S3 Jobs Transform added; per-country lens findings + scenarios + regime tags). Modification surface for this bundle.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — Lens 1 displacement-velocity + absorption-capacity definitions (light update needed: schema entry for `pan_european_aggregate`).
- `/Users/philippmaul/Documents/projects/european-demographics-map/site/demographics-data.json` — Layer 4 working-age population data (population-weighting input).

### Goal — modify SOT JSON only

Add a top-level `cross_cutting_findings.pan_european_aggregate` block carrying TWO sub-blocks:

```json
"pan_european_aggregate": {
  "eu_27": {
    "scope": "EU-27 member states",
    "country_count": 27,
    "country_list": ["AT","BE","BG","CY","CZ","DE","DK","EE","EL","ES","FI","FR","HR","HU","IE","IT","LT","LU","LV","MT","NL","PL","PT","RO","SE","SI","SK"],
    "weighting_method": "working-age population, 2024 baseline",
    "weighted_lens1_ratio": <number>,
    "headline_corridor": <1|2|3>,
    "headline_corridor_label": "Managed Transition" | "Partial Absorption" | "Displacement Without Absorption",
    "class_distribution": {"I": <int>, "II": <int>, "III": <int>, "IV": <int>},
    "class_distribution_population_weighted_pct": {"I": <pct>, "II": <pct>, "III": <pct>, "IV": <pct>},
    "regime_mix": {"growth_baseline": <int>, "secular_stagnation_warning": <int>, "post_growth_empirical": <int>},
    "regime_mix_population_weighted_pct": {...},
    "weighted_scenario_probability": {
      "S1": [low, mid, high],
      "S2": [low, mid, high],
      ... S3, S4, S5, S6, S7
      "S8": [low, mid, high]   // conditional, weighted same way
    },
    "modal_scenario_under_post_growth_subset": "S2",
    "capability_floor_breach_count": 11,   // EU-27 subset of the 12-country breach list (excludes CH, IS, LI, NO, UK; includes BE, DE, DK, IE, LU, NL, SE)
    "squeeze_cluster_count": 5,   // EU-27 subset of the 8-country squeeze (excludes NO; includes BE, DE, DK, FI, FR, NL, SE)
    "_provenance": {"bundle": "X", "ingestion_date": "2026-04-30"}
  },
  "european_36": {
    "scope": "EU-27 + EFTA-4 + UK + 4 candidates (Bosnia, North Macedonia, Serbia, Turkey)",
    "country_count": 36,
    "country_list": [...all 36...],
    "weighting_method": "working-age population, 2024 baseline",
    ...same fields as eu_27 sub-block...
    "capability_floor_breach_count": 12,   // full 12-country list
    "squeeze_cluster_count": 8,   // full 8-country list
    ...
  },
  "variation_guard_note": "Every aggregate scalar above represents a population-weighted single answer; the structural finding of this synthesis is that the 36-market variation IS the analytical surface. Aggregates are reference points; they are not substitutes for the per-country reading. The class distribution (9/9/15/3) is the most honest pan-European read because it surfaces variation rather than collapsing it.",
  "headline_finding_pan_european": "<short string>: the pan-European read in one sentence — likely 'No single European corridor — the centre of gravity sits in C2 + C3, with 9 markets resilient, 9 fragile, 15 already in trouble, and 3 in active cascade.'"
}
```

### Computation tasks

1. **Population-weighting source.** Use Layer 4's `demographics-data.json` working-age (20–64) population values. If granular country-level numbers aren't in the L4 site data, fall back to Eurostat `demo_pjan` extracts in `european-demographics-map/data/eurostat/`. If a country is missing in both, flag with `data_gap_reason` and use the country count weighting (1/27 or 1/36) as a degraded fallback for that country only.

2. **Weighted Lens 1 ratio.** Per country: `lens1_ratio` (already in SOT). Aggregate = Σ(country_lens1_ratio × country_pop_weight) / Σ(country_pop_weight). Compute for both EU-27 and 36-market.

3. **Headline corridor.** Apply 1.20 / 2.80 thresholds to the weighted Lens 1 ratio. Likely C2 for both subsets, but compute it.

4. **Class distribution (count + population-weighted percentage).**
   - Count: simple count of EU-27 / 36 countries in each class.
   - Population-weighted percentage: Σ(country_pop where class=X) / total_pop × 100.

5. **Regime mix (count + population-weighted percentage).** Same shape.

6. **Weighted scenario probability vectors.** Per scenario, for each country, the SOT carries a regime tag and the probability vector for that scenario under the country's regime. The aggregate = population-weighted average of per-country probability vectors per scenario. This is the right computation: it rolls up "what's the probability of S2 under EU-27's regime mix" without reifying a regime that doesn't exist for the aggregate.

7. **Modal scenario under post-growth subset.** Within the post-growth-empirical countries inside the EU-27 (and 36) subsets, name the modal probability scenario. Should be S2 (Climate Adaptation Boom) if Bundle V's load-bearing finding holds. This is a sentinel check.

8. **Capability-floor breach count + squeeze cluster count.** Filter the existing 12-country breach list and 8-country squeeze list to EU-27 / 36-market scope. EU-27 breach: BE, DE, DK, IE, LU, NL, SE (7) plus possibly more — verify against full list. EU-27 squeeze: BE, DE, DK, FI, FR, NL, SE (7? or 8?) — verify NO is excluded, count the rest.

9. **Variation-guard note + headline finding string.** Author per the spec above.

### Methodological constraints

1. **Population-weighted is the default.** Where alternative weights (GDP, country count) would produce materially different aggregates, document both — but the published headline uses population weighting. Population is the right denominator because the analysis is about labour markets (workers, displaceable cohorts), not output.

2. **The variation guard is non-negotiable.** Every aggregate scalar in the SOT block must sit alongside the distribution it summarises. The headline corridor is meaningless without the class distribution context. Encode this in the JSON structure.

3. **No re-classification.** Bundle X computes aggregates from existing per-country readings; it does not re-place countries on the corridor map or re-class them. Per-country fragility classes stay locked at 9/9/15/3.

4. **Lens-by-lens aggregation deferred.** Bundle X computes the headline aggregates (Lens 1 ratio + class distribution + scenario probabilities). Full lens-by-lens pan-European reads (Lens 2 retirement-offset weighted average; Lens 4 squeeze incidence; Lens 5 polycrisis composite weighted average) are Bundle X.2 candidates if the deliverable surface needs them. Phase 1B's europe.html can render the existing per-lens cross-cutting findings as the lens-level pan-European reads without Bundle X.2 work.

### Verification (before reporting back)

1. SOT JSON loads round-trip cleanly via `json.load → dumps → load`.
2. New top-level path `cross_cutting_findings.pan_european_aggregate` exists with `eu_27` + `european_36` sub-blocks + `variation_guard_note` + `headline_finding_pan_european`.
3. EU-27 country list has exactly 27 entries; 36-market list has exactly 36.
4. Population weights sum to 1.0 (within ±0.001) per scope.
5. Weighted Lens 1 ratio falls in [1.0, 3.5] range (sanity check).
6. EU-27 + 36-market headline corridor placements computed (likely C2 for both; verify).
7. Class distribution sums to scope total (27 or 36).
8. Population-weighted class percentages sum to 100% (within ±0.5 pct).
9. Sentinel: modal scenario under post-growth subset is S2 (Climate Adaptation Boom). If not, surface the divergence.
10. Capability-floor breach EU-27 subset count documented (from the 12-country full list, exclude CH/IS/LI/NO/UK = 7 EU-27 countries: BE, DE, DK, IE, LU, NL, SE). Squeeze cluster EU-27 subset count documented (from 8-country full list, exclude NO = 7 EU-27 countries: BE, DE, DK, FI, FR, NL, SE).
11. `metadata.bundle_x_pan_european_aggregate` block records: rationale, weighting method, country lists, ingestion date.
12. `_provenance` sub-blocks present.
13. SOT JSON size growth < 30 KB (the new block is summary data, not per-country expansion).

### When done — report back to master session with

1. Aggregate summary — EU-27 corridor + 36-market corridor + class distribution + modal scenarios, in a single table.
2. Population-weighting method audit — which countries used Layer 4 data; which used Eurostat fallback; which (if any) hit the country-count-weighting fallback.
3. Verification checklist (1–13) — pass/fail per item.
4. Any divergences from the methodological expectations (e.g., if the modal-under-post-growth subset isn't S2; if the headline corridor surprises).
5. Knock-on flag list — what europe.html (Phase 1B) will render from this; what Bundle W (deliverable doc updates) will need to absorb.
6. Composition gaps — places where the population-weighting logic ran into thin data.
7. Variation-guard verification — confirm every scalar in the new block sits alongside distribution context (not bare).
8. Any candidate brain captures — likely none; this is mechanical aggregation.

## END PROMPT
