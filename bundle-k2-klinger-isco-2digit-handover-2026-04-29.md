# Handover Prompt — Bundle K-2: Klinger × ISCO 2-Digit Recompute (Bundle K Magnitude Upgrade)

Bounded recompute pass. Upgrades Bundle K's Lens 5(c) Klinger weighting from 1-digit (lower-bound directional confirmation) to 2-digit (proper magnitude signal) using the now-available `lfsa_egai2d__custom_21241431_linear_2_0.csv` full LFS extract. Independent of Bundle J + Class I decision.

---

## START PROMPT

I need you to recompute Bundle K's Lens 5(c) Klinger-weighted score at ISCO 2-digit granularity using a freshly-supplied full LFS extract. Bundle K had to use 1-digit aggregation because the Eurostat public API + databrowser default exports were gated to OC0..OC9; Phil now supplied the `__custom_` (non-default-view) extract that contains the full 43 ISCO 2-digit codes for all 38 entities × 2011–2025. This bundle replaces Bundle K's outputs in place — no separate file series.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Downloads/lfsa_egai2d__custom_21241431_linear_2_0.csv` — 85MB, 346,992 rows. Contains: 55 isco08 values (TOTAL + NRP + OC0..OC9 + 43 OC2-digit codes OC01..OC96), 38 geos (full Phase 3 scope including BA/MK/RS/TR/UK + Montenegro + EU/EA aggregates), age × sex × wstatus dimensions, 2011–2025
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-klinger-isco-coordination-share.json` — Klinger 3-digit coordination-share data (130 codes; 125 derived from ESCO at M-confidence; 5 default fallback)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-klinger-rescaled.csv` + `.json` + `findings.md` — Bundle K outputs (1-digit Klinger weighting). Recompute updates these in place.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-data.json` — current Lens 5(c) cells
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-methodology-notes.md` §2.3 — Lens 5(c) methodology
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-k-klinger-isco-join-handover-2026-04-29.md` — original Bundle K spec
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-klinger-findings.md` — what to compare against (Bundle K's lower-bound deltas + sanity test results)

### Task 1 — Filter LFS extract to the analysis slice

From the 346,992 rows, filter to:
- `age == "Y15-64"` (working-age, matches Bundle K's slice)
- `sex == "T"` (Total)
- `isco08` matches one of the 43 OC2-digit codes: `OC01, OC02, OC03, OC11, OC12, OC13, OC14, OC21, OC22, OC23, OC24, OC25, OC26, OC31, OC32, OC33, OC34, OC35, OC41, OC42, OC43, OC44, OC51, OC52, OC53, OC54, OC61, OC62, OC63, OC71, OC72, OC73, OC74, OC75, OC81, OC82, OC83, OC91, OC92, OC93, OC94, OC95, OC96`
- `geo` matches one of the 36 Phase 3 countries: `AT, BE, BG, CY, CZ, DE, DK, EE, EL, ES, FI, FR, HR, HU, IE, IT, LT, LU, LV, MT, NL, PL, PT, RO, SE, SI, SK, NO, IS, LI, CH, UK, BA, MK, RS, TR`
  - LI not in dataset → proxy CH (per Phase 2 convention)
- For each country, take the **most recent year with non-null OBS_VALUE for that country's full 43-code set** (latest available year per country; expect 2025 for most, 2024 for some, possibly 2023 for stragglers)

Verify country coverage: every Phase 3 country except LI should have data. If any Phase 3 country fails coverage check, flag explicitly.

### Task 2 — Compute employment-share-by-ISCO-2digit per country

For each country, for each of the 43 ISCO 2-digit codes:
```
employment_share_{country, isco2} = OBS_VALUE_{country, isco2, latest_year} / Σ_{isco2 ∈ 43} OBS_VALUE_{country, isco2, latest_year}
```

Sum should ≈ 1.0 per country (within ±0.02 due to NRP residual / rounding). Document the sum-residual per country in the output.

### Task 3 — Aggregate Klinger 3-digit → 2-digit (ESCO-count-weighted)

Bundle K already established ESCO-occupation-count weighting as the principled aggregation method for Klinger 3-digit → 1-digit. Same logic at 2-digit:

For each 2-digit parent code (e.g., OC25):
```
klinger_2digit_{OC25} = Σ_{isco3 ∈ children(OC25)} ( esco_count_{isco3} × klinger_3digit_{isco3} ) / Σ_{isco3 ∈ children(OC25)} esco_count_{isco3}
```

Use the same ESCO occupation counts Bundle K used (`esco_occupations_processed` field structure in `layer-6-klinger-isco-coordination-share.json`).

Output: 43 OC2-digit Klinger coordination-share values, derived from the underlying 130 3-digit Klinger values.

### Task 4 — Recompute Lens 5(c) per country

For each of the 36 countries:
```
lens5c_klinger_weight_2digit = Σ_{isco2 ∈ 43} ( employment_share_{country, isco2} × klinger_2digit_{isco2} )
lens5c_klinger_weighted_2digit = lens5c_klinger_weight_2digit × velocity_country
```

Where `velocity_country` = same Phase 1 velocity Bundle K used (the comparison axis is the coordination-share weighting, not velocity).

Output per country: `lens5c_klinger_weight_2digit` (employment-weighted average coordination-share, isolated from velocity) + `lens5c_klinger_weighted_2digit` (full score with velocity).

### Task 5 — Compare to Bundle K (1-digit) and Phase 2 baseline

For each country, compute three deltas:
- `delta_vs_phase2 = lens5c_klinger_weighted_2digit − current_lens5_ai_labour_load` (Phase 2 baseline)
- `delta_vs_K1d = lens5c_klinger_weighted_2digit − lens5c_klinger_weighted_K1d` (Bundle K 1-digit result)
- `magnitude_amplification = |delta_vs_K1d| / |Bundle K's delta_vs_phase2|` per country (how much the 2-digit recompute amplifies Bundle K's signal — expected >1 for high-coord countries, near-1 or <1 for already-low-signal countries)

Re-run Bundle K's classifications under the spec ±0.10 substantive-change threshold:
- How many countries cross the ±0.10 threshold under 2-digit (Bundle K had 0 / 36)?
- Top-5 countries by amplified delta in each direction
- DE / AT / CH / NL / UK / IE expected to amplify upward; PL / RO / BG / HR expected to amplify downward

### Task 6 — Recompute Lens 5 composite drag scores

Same logic as Bundle K Task 4: recompute `lens5_composite_drag` with the new ai_labour values:
```
lens5_composite_drag = w_a × polycrisis + w_b × demographic + w_c × ai_labour + w_d × climate_net
```

Track which countries cross substantive-change thresholds at the composite level (these are Bundle L's primary reweight candidates).

### Task 7 — Capability-floor breach proxy at 2-digit

Bundle K found capability-floor breach scope expanded 3 → 11 countries under 1-digit weighting. Recompute under 2-digit. Expected: same 11 stay flagged + possibly more (since 2-digit captures finer high-coord pulses), or possibly a refinement where some countries fall out.

Report:
- Final breach-flagged country list at 2-digit
- Comparison to Bundle K 1-digit result (which countries entered/exited the breach set)

### Required outputs

Replace Bundle K's three files in place:
1. **`layer-6-phase3-klinger-rescaled.csv`** — 36 rows × extended columns (add `_2digit` variants alongside the `_1digit` Bundle K values; both retained for traceability)
2. **`layer-6-phase3-klinger-rescaled.json`** — same data structured + metadata block updated:
   - data source: `lfsa_egai2d__custom_21241431_linear_2_0.csv`
   - granularity: 2-digit (43 codes)
   - aggregation: ESCO-count-weighted Klinger 3-digit → 2-digit
   - per-country sum-residual (employment shares sum check)
   - latest-year-per-country mapping
   - bundle_k_to_k2_amplification per country
3. **`layer-6-phase3-klinger-findings.md`** — REWRITE under 200 lines:
   - Top 5 amplified-up + top 5 amplified-down countries
   - Number crossing ±0.10 threshold at 2-digit
   - Sanity test result (DE/AT/CH/NL/UK/IE confirmation strengthened?)
   - Capability-floor breach scope at 2-digit (vs 1-digit's 3 → 11)
   - Open questions for Bundle L (now with cleaner magnitude signal)

Preserve Bundle K's findings as a SECTION inside the rewritten findings.md (clearly labelled "Bundle K 1-digit lower-bound result, retained for comparison").

### Constraints

- BR-19 no fabrication: per-country employment shares must come from the supplied LFS file; no estimation
- BR-21 per-country provenance: `derivation_method` documents granularity (2-digit), data file, year used, ESCO-count-weighted Klinger aggregation
- LI: explicit proxy-CH note + null where appropriate
- Do NOT modify Klinger file, locked spec, or Phase 2 outputs (only Bundle K's three Phase 3 outputs are replaced in place)
- Phil does all git commits

### Verification

1. Sum of employment shares per country ≈ 1.0 (±0.02). If any country fails, surface as data anomaly.
2. Sanity test (DE/AT/CH/NL/UK/IE upward direction): all 6 should show MORE positive deltas at 2-digit than at 1-digit. If not, methodology gap surfaced.
3. Anti-sanity test (PL/RO/BG/HR): all 4 should show MORE negative deltas at 2-digit. HR might still hover near zero.
4. Baseline reproduction: Bundle K's 1-digit result should be reproducible from the same engine with isco08 filter restricted to OC0..OC9 + sum-aggregation. Spot-check one country (DE) that 1-digit recompute matches Bundle K's published value.
5. JSON validates; 36/36 countries; no fabricated values.

### When done — report back to master session with

1. Sanity test result (high-coord amplification strengthened? by how much?)
2. Number of countries crossing ±0.10 substantive-change threshold at 2-digit (Bundle K had 0)
3. Top 5 amplified-up + top 5 amplified-down deltas
4. Capability-floor breach scope at 2-digit + delta from Bundle K's 11
5. Largest composite-drag shifts at 2-digit
6. Whether any country crosses a corridor- or class-relevant threshold under the upgraded magnitude (i.e., would Bundle L's fragility re-evaluation find substantively different inputs)
7. Open questions for Bundle L

## END PROMPT
