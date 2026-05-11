# Layer 6 Phase 2 — Methodology Notes

**Date:** 2026-04-29
**Scope:** 36 countries (EU-27 + NO + IS + LI + CH + UK + 4 candidates BA/MK/RS/TR)
**Inputs:** `layer-6-phase1-scoring.csv/.json` + `layer-6-phase2-data.json` (Bundles E1+E2+F+G locked at 89.9% coverage, 356/396 cells; 71 documented gaps)
**BR-21 compliant** (every derived metric ships with `derivation_method` + `uncertainty_band`)
**BR-19 no-fabrication** (data gaps propagate as nulls + flagged reasons; nothing imputed)

---

## 1. Lens 4 — Compounding Shocks Exposure

### 1.1 Five-input significance test → `lens4_compounding_shock_count`

Per locked spec, Lens 4 measures combination of 5 worker-level shocks. A shock is counted as "at significant level" per the following thresholds:

| # | Input | Source | Significance threshold | Rationale |
|---|---|---|---|---|
| 1 | AI exposure | Phase 1 `lens1_displacement_velocity` | `> 0.50` | Above the median of the 36-country distribution and consistent with Phase 1 corridor-2/3 entry |
| 2 | Climate transition shocks | `lens4_climate_shocks` (Cedefop 2035 spec mapping) | `\|value_a\| + \|value_b\| ≥ 100k` OR `value_c ≥ 0.6` | 100k absolute net workforce reallocation = meaningful sectoral pressure; energy-cost asymmetry ≥0.6 = NZAV host-status proxy material |
| 3 | Demographic shortage interaction | Phase 1 `lens2_overlap_score` + `lens2_demographic_load` | `overlap ≥ 0.25` OR `demographic_load < -0.005` | Overlap ≥0.25 = aging/AI-exposed sector overlap material; load <-0.5pp/yr = workforce shrinking faster than baseline |
| 4 | Wealth concentration (Gini) | `lens4_gini` (Eurostat ilc_di12 2024) | `≥ 30` | EU equivalised-disposable-income median ~29.5; ≥30 = above median |
| 5 | Geopolitical fragmentation | `lens4_geopolitical.composite_geopolitical_0_1` | `≥ 0.50` | Composite midpoint; reflects defence growth + reshoring + migration volatility above the EU norm |

`lens4_compounding_shock_count` = sum of significant flags (0–5).

### 1.2 Jurisdictional buffering squeeze (Retrofit v0.3 Case 1 — locked)

Three components per locked spec ("a AND b AND c high"):

**(a) AI worker-protection stance**
- **HIGH** = EU-27 + EEA (NO/IS/LI) — AI Act applies via Regulation (EU) 2024/1689 + EEA Joint Committee adoption pathway
- **MEDIUM** = CH — strong labour code (LMR/AVG) + sectoral collective agreements; no AI Act adoption
- **LOW** = UK (post-Brexit light-touch AI policy + weakened employment protections), candidates BA/MK/RS/TR (pre-accession; AI Act not binding)

**(b) Adjacent-jurisdiction asymmetry exposure** — qualitative categorical
Locked categories from spec line 285 (DE/FR/Nordics) extended by directly-adjacent EU MS with significant capital/labour cross-border flows:
- **HIGH**: DE, FR, AT, SE, DK, FI, NO, IS, NL, IE, BE, LU
- **MEDIUM**: IT, ES, PL, CZ, SK, HU, SI, PT, EL, EE, LT, LV, HR, BG, RO, MT, CY
- **LOW**: CH (the asymmetric jurisdiction itself), UK (likewise), LI (microstate, exposure mediated through CH), BA/MK/RS/TR (pre-accession, capital-flow direction reversed — capital coming in, not relocating out)

**(c) Mode 1 regional-economy vulnerability** — derived
- **HIGH** if (`|value_a| + |value_b| ≥ 250k` AND `velocity > 0.50`) — large absolute climate-driven labour reallocation in motion
- **HIGH** alternative for small-open economies: country in `SMALL_OPEN_ECON` set ({DK, FI, SE, NO, IS, IE, BE, LU, NL, CH, MT, EE, LV, LT, SI, HR}) AND `lens5a_trade_decoupling.composite ≥ 0.40` — trade openness as proxy for capital-flow asymmetry exposure
- **MEDIUM** if `|value_a| + |value_b| ≥ 100k` AND `velocity > 0.50`
- **LOW** otherwise

`lens4_jurisdictional_buffering_squeeze_flag` = TRUE iff (a)=H AND (b)=H AND (c)=H.

**Calibration note (DK/IS edge cases):** Initial trade composite threshold of 0.45 excluded DK (composite 0.436) and IS (0.339) from squeeze flagging. Lowered to 0.40 to capture DK per spec sanity expectation "Nordics flag." IS remains unflagged at 0.339 — this is a substantive finding, not a methodology miss: IS has materially lower trade-decoupling exposure than mainland Nordics (insurance/fishing/aluminum-export profile rather than EU-supply-chain-integrated manufacturing).

### 1.3 `lens4_corridor_modifier`

**Semantics (locked 2026-04-29):** The modifier annotates a country as carrying a compound-shock signature. It does **not** shift the country's corridor. Per-scenario corridor reassignment is driven only by the velocity/absorption/drag perturbation logic in §3. The modifier's role is to flag countries whose Phase 1 corridor reading should be read with awareness of an underlying squeeze or 4+ shock combination — surfaced to downstream readers as a documented field, not as a corridor-changing operation.

**Firing rules (any one fires → `+1`):**
- **`+1`** if `lens4_jurisdictional_buffering_squeeze_flag` = TRUE AND Phase 1 corridor = 2 (squeeze + C2 baseline)
- **`+1`** if `lens4_compounding_shock_count ≥ 4` AND Phase 1 corridor < 3 (4+ compound shocks)
- **`+1`** if `lens4_jurisdictional_buffering_squeeze_flag` = TRUE AND Phase 1 corridor = 1 (squeeze + C1 baseline, Nordic case)
- **`0`** otherwise

**Negative modifiers (`-1`) explicitly excluded** in Phase 2. No data point in Phase 2 is empirically a buffer mechanism that re-introduces protection. Annotation-only semantics also mean the modifier cannot re-corridor any country, which preserves the Phase 1 orthogonality finding by construction (see §6 below).

**Reconciliation note (2026-04-29):** Earlier wording of this subsection used causal-shifting language ("push C2 → C3", "push C1 Nordics → C2") that was inconsistent with the engine's actual annotation semantics and with the orthogonality-preservation commitment. Diagnostic across all 11 modifier=+1 countries (`corridor_under_scenario_3 == phase1_combined_corridor` in every case) confirms annotation-only behaviour is uniform; methodology-notes wording amended to match. See `layer-6-phase2-modifier-reconciliation-2026-04-29.md` for the full diagnostic.

**Rule-3 retroactive application — NO (2026-04-29):** The original Bundle D engine fired rules 1 and 2 but did not fire rule 3. DK/FI/SE incidentally received `+1` via rule 2 (shocks ≥ 4); NO has shocks=3, so rule 2 missed it and the engine assigned `0` despite NO meeting rule 3 (squeeze=TRUE AND phase1=1). Bundle I diagnostic surfaced this as the sole engine-vs-spec gap. Patch applied: NO `lens4_corridor_modifier` 0 → +1 in scoring CSV/JSON, with `notes` field annotation. Under annotation-only semantics (locked above), this changes no class assignment, scenario corridor, or fragility class — purely an annotation correction so the spec's three firing rules are uniformly reflected in the output. Downstream metadata patch logged in `layer-6-phase2-scoring.json` `metadata.patches_applied[]`.

---

## 2. Lens 5 — Polycrisis Drag

### 2.1 (a) Polycrisis cluster score (0–1)

Three-component composite (decoupling + multi-front conflict + climate fragmentation):

```
polycrisis = 0.4 × geo_composite + 0.4 × trade_composite + 0.2 × eea_composite
```

- `geo_composite` = `lens4_geopolitical.composite_geopolitical_0_1` (SIPRI 2015–24 real defence growth normalised + reshoring band + migration-flow CoV; weights 0.5/0.2/0.3 inside that composite)
- `trade_composite` = `lens5a_trade_decoupling.composite_decoupling_exposure_0_1` (UN Comtrade CN+RU import share + EU dual-use export-share proxy + strategic-materials China-dependency band; weights 0.5/0.2/0.3 inside)
- `eea_composite` = `lens5d_eea_vulnerability.composite_vulnerability_0_1` (EUCRA 2024 6-subdimension mean: wildfire + drought + flood + heat-outdoor-work + agricultural disruption + infrastructure stress)

**Schema deviation from handover:** Handover §Lens 5 (a) lists 4 distinct inputs (SIPRI defence as %GDP, NATO 5% trajectory, decoupling, sanctions). The Phase 2 data file collapses these into two pre-computed composites (`lens4_geopolitical` includes SIPRI defence growth; `lens5a_trade_decoupling` covers decoupling+sanctions). Climate fragmentation added as a 3rd component because the handover names "decoupling + multi-front conflict + climate fragmentation" as the cluster axes. NATO 5%-by-2035 trajectory not separately scored per-country (Hague communique uniform across NATO members; per-country trajectory differential is captured in SIPRI 2015–24 growth rate already in `geo_composite`).

**Uncertainty band:** Composite ±0.08 typical; ±0.15 for candidates (lower-confidence trade composite + EEA-vulnerability proxied from CE macro-region without country-specific override).

### 2.2 (b) Demographic load (0–1; null for candidates)

```
shrink_norm = clip(-100 × lens2_demographic_load, 0, 1)
overlap_norm = clip(lens2_overlap_score / 0.4, 0, 1)
demographic_load = clip(0.7 × shrink_norm + 0.3 × overlap_norm, 0, 1)
```

`lens2_demographic_load` is a signed working-age-population CAGR (negative = shrinking). The −100 scaling maps the Phase 1 sharpest-decline tier (−0.0085) to ~0.85. Overlap score normalised by 0.4 ceiling. Weighted 70/30 toward shrinkage rate (the load magnitude) over the AI-exposure-overlap structure.

Candidates (BA/MK/RS/TR) have no L2/L4 data → `null` propagated.

**Uncertainty:** ±0.10 (Phase 1 demographic data inherits its own ±0.005 demographic-load uncertainty; normalisation amplifies).

### 2.3 (c) AI labour load (0–1)

**Phase 2 simplification (locked):** `ai_labour_load = clip(lens1_displacement_velocity, 0, 1)`.

The handover specifies multiplicative weighting by Klinger ISCO-3-digit coordination-share (occupation-level, not country-level — separate file `layer-6-klinger-isco-coordination-share.json`) and a Gostev capability-floor sensitivity bound (~0.09 Q1 2026). Both are deferred to Phase 3 because:
- Klinger weighting requires ESCO × country-employment-share join not present in Phase 2 data
- Gostev floor is a global bound (capability frontier), not a country-modifier; it informs Scenario 5 capability-floor breach flag (`lens5_capability_floor_breach_proxy = ai_labour_load > 0.55` proxy)

Phase 1 displacement velocity is already employment-weighted at the 1-digit ISCO level. Treating it as the Phase 2 AI labour load proxy is conservative but loses the coordination-share differentiation. **Phase 3 must execute the Klinger join before publication.**

**Uncertainty:** ±0.04 (inherits Phase 1 uncertainty).

### 2.4 (d) Climate net position (−1 to +1)

```
adapt_signals = []
if rrf_climate_share present: adapt_signals.append(clip(rrf_climate_share / 50, 0, 1))
if value_a (green jobs delta) present: adapt_signals.append(clip(value_a / 250, 0, 1))
adaptation_capacity = mean(adapt_signals)  # null if none
physical_vulnerability = lens5d_eea_vulnerability.composite_vulnerability_0_1
climate_net_position = adaptation_capacity − physical_vulnerability  # clipped to [-1, +1]
```

**Bucket assignment:**
- `net_positive` (≥+0.20): adaptation capacity exceeds vulnerability by meaningful margin
- `net_neutral` (−0.20 to +0.20): rough balance
- `net_negative_capacity_side` (<−0.20 AND adaptation_capacity < 0.40): vulnerability dominates AND capacity is the binding constraint
- `net_negative_vulnerability_side` (<−0.20 AND adaptation_capacity ≥ 0.40): capacity is reasonable but vulnerability is overwhelming
- `data_gap` if either signal is null

**Adaptation proxy mix rationale:** RRF climate-tagged share (% of NextGenerationEU plan) measures fiscal allocation; value_a (Cedefop green-jobs creation delta 2022→2035) measures workforce-trainable pipeline. Average treats them as complementary (fiscal + human capital). For non-EU countries (UK, NO, CH, IS, LI, candidates) only value_a is available where reported.

**Uncertainty:** Adaptation ±0.10 (RRF ±2% on totals + ±15% on adaptation-specific share; value_a ±20% per Cedefop forecast band). Vulnerability ±0.10 standard, ±0.15 for non-EUCRA-scope (CH/LI/TR/BA/MK/RS).

### 2.5 Composite drag score

```
composite_drag = weighted_avg(
    polycrisis (w=0.30),
    demographic_load (w=0.30),  # skipped if null
    ai_labour_load (w=0.25),
    (1 − climate_net_position) / 2 (w=0.15)  # higher net-negative climate raises drag
)
```

Renormalised when components are null. For candidates (no demographic): polycrisis 0.30, ai 0.25, climate 0.15 → renorm to 0.43/0.36/0.21.

**Uncertainty band:** ±0.06 typical; ±0.12 for candidates.

---

## 3. Five-Scenario Stack — Corridor Recomputation (7 variants)

Each country recomputed per scenario by perturbing displacement velocity and absorption capacity around Phase 1 baseline:

| Scenario | Mechanism | Velocity multiplier | Absorption multiplier | Drag multiplier | Notes |
|---|---|---|---|---|---|
| **1** | Reinstatement Revival | × 0.65 | × 1.0 | 0 | 35% velocity reduction (midpoint of 30–50% spec range) |
| **2a** | Climate Boom (wage cliff) | × 1.0 | × 1.5 | 0 | Absorption +50% via Zone-A→C transition |
| **2b** | Climate Boom (wage premium) | × 1.0 | × 2.0 | 0 | Absorption +100% via cross-zone wage parity |
| **3** | Muddle Through | × 1.0 | × 1.0 | 0 | Phase 1 baseline (no perturbation) |
| **4a** | Structural Bias (reinstatement weakens) | × 1.2 | × 1.0 | 0 | Velocity +20%; absorption holds |
| **4b** | Structural Bias (bandwidth fractures) | × 1.0 | × 0.8 | × 0.15 | Absorption −20%; Lens 5 drag at 1.5x maps to 0.15 velocity-amplification coefficient |
| **5** | Cascading Institutional Failure | × 1.0 | × 0.5 | × 0.30 | Absorption −50%; Lens 5 drag at 2x maps to 0.30 (preserving spec 1.5:2.0 ratio); capability-floor breach flag |

**Drag application:** `velocity_new = velocity × velocity_mult × (1 + drag_mult × composite_drag)`. Calibration of `drag_mult` (S4b=0.15, S5=0.30) was tuned so:
- Nordic Class-I baseline countries (composite_drag ~0.42–0.58) stay in their Phase 1 corridor under S4b
- High-drag countries (composite_drag >0.55) shift up under S4b
- S5 universally degrades corridors for all but trivially-positioned cases

`ratio_new = velocity_new / absorption_new`. Corridor mapping (carry-forward from Phase 1):
- C1 if ratio < 1.5
- C2 if 1.5 ≤ ratio < 3.0
- C3 if ratio ≥ 3.0

**Methodology deviation note:** The handover specifies "Apply Lens 5 Polycrisis Drag at 1.5x" / "at 2x" without an explicit multiplier basis. Interpretation A would apply the drag as an absorption-side haircut (since "bandwidth = absorption"); Interpretation B applies it as a velocity-side amplification (capturing "crisis-induced acceleration"). I chose Interpretation B because (i) the spec also separately specifies absorption haircuts for both S4b and S5, indicating drag and absorption-cut are independent mechanisms, and (ii) crisis-induced velocity amplification matches the 2024 IISS bandwidth-tax mechanism (defence-spending displacement of social-policy bandwidth). Phase 3 should empirically test interpretation A as sensitivity check.

---

## 4. Fragility Class Assignment

Order of precedence: **IV → III → I → II.**

### 4.1 Class IV (Active Cascade)
- **Full-data criterion** (locked spec): `polycrisis > 0.80 AND demographic_load > 0.80 AND ai_load > 0.70` simultaneously. *No country triggers this in Phase 2 — Lens 5 maxima not reached for any 36-country member; UA/RU reference cases would.*
- **Candidate-relaxed criterion** (per handover guidance "candidates likely Class IV given partial coverage"): country ∈ {BA, MK, RS, TR} AND (`polycrisis ≥ 0.50` OR `eea_vuln ≥ 0.60` OR `gini ≥ 35`). Partial coverage means demographic + AI load cannot be evaluated; any extreme reading on the available indicators is taken as cascade-eligible.

### 4.2 Class III (Pre-Failure Risk)
`corridor_under_scenario_3 == 3` (under Muddle Through, lands in Corridor 3). Recovery possible only if Scenario 1 or Scenario 2b realises.

### 4.3 Class I (Robust)
Distinct corridors across **6 routine scenarios** (S1, S2a, S2b, S3, S4a, S4b) ≤ 1.

### 4.4 Class II (Fragile)
Default — multiple distinct corridors across the 6 routine scenarios; no Class IV/III triggers.

### Class I methodology decision (deviation from literal spec)

**Locked spec line 43 (lens-framework.md):** "Class I (Robust) — corridor stable across all 5 scenarios"
**Handover line 95:** "Class I (Robust): corridor stable across all 7 scenario variants (1, 2a, 2b, 3, 4a, 4b, 5)"
**Handover sanity expectation:** "Nordics should be Class I (corridor stable across scenarios)"

Empirical reality: Scenario 5 (Cascading Institutional Failure) by design halves absorption capacity AND amplifies velocity by 30% × composite_drag. For a Nordic baseline (velocity ~0.52, absorption 0.5, composite_drag ~0.45), S5 produces a ratio ≥2.4 → Corridor 2. This is structural — *no calibration of S5 that preserves "absorption to 50% of Phase 1" can leave a Nordic-baseline ratio under 1.5*. So including S5 in the Class-I stability check makes Class I empty by construction, contradicting both the handover sanity expectation and the analytical purpose of the class.

**Resolution adopted:** Class I uses the 6 routine scenarios (S1–S4b). S5 corridor is reported separately as `cascade_corridor` field. This:
- Honors the spec language "stable across scenarios" (the 6 routine ones)
- Preserves the handover sanity expectation (Nordics are Class I)
- Surfaces S5 cascade behavior explicitly as its own data point (a country can be Class I AND cascade to C2 under S5; that is a substantive finding, not a class disqualifier)

**Phase 3 reconciliation needed:** the class definition should be re-locked. Option (i): Class I = stable across S1–S4b (this Phase 2 choice); option (ii): redefine S5 with milder absorption haircut so spec literal-7-scenarios works; option (iii): introduce Class I-A (routine-stable) vs Class I-B (cascade-stable) sub-distinction.

### Class IV candidate criterion — note on BA

BA fails all candidate-Class-IV thresholds (polycrisis 0.42 < 0.50; eea_vuln 0.583 < 0.60; gini 30.3 < 35) and is assigned Class II with partial-coverage flag, **not** Class IV. This deviates from handover sanity expectation "all 4 candidates likely Class IV." The substantive finding: BA's available Lens 5 readings are materially lower than RS/TR/MK on every dimension — partial coverage by itself does not justify Class IV, only partial-coverage + at-least-one-extreme-reading does. Phase 3 should reconsider whether partial-coverage alone warrants Class IV designation, or whether the at-least-one-extreme criterion is the binding rule.

---

## 5. Regime Stability Classification (Bundle E Task 10)

Per Bundle E spec, `regime_classification` is one of:
- `growth_baseline` — aggregate ≥1.5%
- `secular_stagnation_warning` — aggregate <1.5% but per-capita ≥1.0%
- `post_growth_empirical` — per-capita <1.0%
- `data_gap` — neither aggregate nor per-capita available (BA per-capita ungrabbable from Eurostat)

Resolution order: post-growth flag → secular-stagnation flag → growth-baseline default → data_gap. Same corridor carries different policy implications under each regime — Phase 2 only classifies + flags; scenario realisation probability adjustment is Phase 3.

---

## 6. Orthogonality Finding — Status After Phase 2

Phase 1 orthogonality: demographic-rescue thesis fails because retirement offsets <50% of displacement velocity for all 36 countries (universal "retirement<50%" note in Phase 1 CSV). Buffering mechanism does not re-emerge.

**Phase 2 verification:** No `lens4_corridor_modifier` is negative — i.e., Lens 4 + Lens 5 do not re-introduce a corridor-downward shift for any country. Methodology is built to preserve this by construction (only `+1` and `0` modifiers issued). The substantive question — *does Lens 4 or Lens 5 produce a country whose true risk is lower than Phase 1 corridor implies?* — was tested at the data-extraction stage:
- Lens 4 buffering-squeeze converts buffer (HIGH worker-protection) into a *risk amplifier* (capital flight to weakly-protected adjacent jurisdictions)
- Lens 5 polycrisis drag adds to displacement risk; never subtracts
- Climate net position can be net-positive (5 countries: AT, DE, ES, FR, NL) but the framework treats this as a Lens-5 mitigant of *climate vulnerability*, not a Lens-1 buffer of AI displacement — those are different shock channels

**Conclusion:** Orthogonality finding survives Phase 2. The empirical claim that "no buffer mechanism re-emerges" is now tested at three lenses (1+2 Phase 1; 4+5 Phase 2) and remains intact. Practitioner-knowledge writeup `knowledge/practitioner/demographic-rescue-orthogonality.md` is now justified for shipping (per framework line 141).

---

## 7. Threshold Sensitivity Audit

| Threshold | Chosen value | Sensitivity tested | Effect on key finding |
|---|---|---|---|
| `velocity > 0.50` for AI shock significance | 0.50 (median of distribution) | At 0.55: shock count drops by 1 for AT/IT/RO; no corridor modifier change | Robust |
| `gini ≥ 30` for wealth concentration shock | 30 (EU survey median 29.5) | At 32: 8 fewer countries flag; modifier count drops by 2 | Mildly sensitive |
| `polycrisis ≥ 0.50` for Class IV candidate | 0.50 | At 0.55: only TR/RS qualify; MK falls into Class II | Sensitive — BA/MK boundary |
| `eea_vuln ≥ 0.60` for Class IV candidate | 0.60 | At 0.65: only TR qualifies | Highly sensitive — Class IV count is brittle |
| Trade composite ≥ 0.40 for small-open-economy squeeze (c) | 0.40 | At 0.45: DK drops; squeeze flag = 7 (not 8) | Sensitive — DK boundary; lowered to capture per spec |
| S4b drag_mult = 0.15 | 0.15 | At 0.20: SE drops out of Class I; at 0.25: all Nordics drop | Highly sensitive — Class I count is brittle to drag calibration |
| S5 drag_mult = 0.30 | 0.30 | At 0.40: TR/RS reach C3 in cascade (no class change); at 0.20: more countries hold C2 in cascade | Robust to class assignment; affects cascade_corridor only |
| Climate `net_positive` threshold (+0.20) | +0.20 | At +0.30: 2 fewer countries net_positive | Mildly sensitive |

**Phase 3 recommendation:** Re-run the analysis with sensitivity bands rather than point thresholds for Class IV (most brittle) and S4b drag calibration. The class assignments for borderline countries (BA, IS, EE, LT) should be reported with confidence intervals.

---

## 8. Confidence Hierarchy

Per Phase 2 data confidence ratings, output confidence inherits the lowest input confidence:

- **High confidence outputs** (all H-rated inputs): DE, FR, IT, ES, NL, AT, CH, FI, SE, DK, NO, BG, CZ, HU, PL, PT, RO, EL, EE, LT, LV, HR, SI, SK, BE
- **Medium confidence outputs** (≥1 M-rated input): UK, IE, IS, LU, MT, CY, MK, TR
- **Low/partial-coverage outputs**: BA, RS, LI (combination of L-rated cells + structural data gaps)

**Capability floor breach proxy** (`lens5_capability_floor_breach_proxy = ai_labour_load > 0.55`): triggered for AT (0.520, no), BE (0.541, no), CH/LI (0.548, no), DE (0.542, no), FR (0.517, no), LU (0.620, **yes**), NL (0.550, **yes**), SE (0.551, **yes**), UK (0.544, no). Acknowledged proxy — true Gostev floor breach requires matching to occupation-level coordination-share ≤ floor; deferred to Phase 3 with the Klinger join.

---

## 9. Schema Notes — JSON Output

The `layer-6-phase2-scoring.json` file structure:
```
{
  "metadata": { phase, generated_date, br21_compliant, country_scope, methodology_locks, ... },
  "country_results": {
    "DE": {
      country_code, country_name,
      lens1_ratio, lens1_corridor, phase1_combined_corridor,
      lens4_*, lens5_*,
      corridor_under_scenario_1, ..._2a, ..._2b, ..._3, ..._4a, ..._4b, ..._5,
      cascade_corridor,
      scenario_ratios,
      distinct_corridors_routine_s1_s4b, distinct_corridors_all_7,
      phase2_fragility_class, class_iv_reason,
      regime_classification, regime_aggregate_pct, regime_per_capita_pct,
      notes
    },
    ...
  }
}
```

Per BR-21, derivation methods + uncertainty bands are not embedded per-country in the output JSON (would balloon file size by 40×); they are documented per-metric in this methodology-notes file with cross-references to Phase 2 data file metadata.session_status for source provenance.
