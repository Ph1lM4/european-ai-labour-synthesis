# Handover Prompt — Bundle D: Layer 6 Phase 2 Scoring (Lens 4 + Lens 5 + Scenario Stack + First-Pass Fragility Classes)

Self-contained prompt for a fresh session. Dispatch only AFTER Bundle A (L3 fixes), Bundle B (Phase 1 re-score with candidates), AND Bundle E (Phase 2 data acquisition) have completed.

---

## START PROMPT

I need you to execute **Layer 6 Phase 2** of the European AI Labour Market suite — adding Lens 4 (Compounding Shocks), Lens 5 (Polycrisis Drag), the 5-scenario stack, and first-pass fragility class assignments to the Phase 1 country scoring. Phase 3 (corridor reduction validation, structural-bias re-calibration) is the next session — do NOT do those.

Read FIRST:
- `projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — locked spec. Do NOT modify.
- `projects/european-ai-labour-synthesis/layer-6-phase1-scoring.csv` + `.json` — Phase 1 outputs (36 countries after Bundle B re-score)
- `projects/european-ai-labour-synthesis/layer-6-phase1-findings.md` — Phase 1 findings, especially the orthogonality finding (treat as confirmed baseline)
- `projects/european-ai-labour-synthesis/layer-6-phase1-methodology-notes.md` — methodology decisions locked in Phase 1

Country scope: 36 (EU-27 + NO + IS + LI + CH + UK + 4 candidates BA/MK/RS/TR). Ukraine + Russia are reference cases for Class IV "Active Cascade" anchoring, NOT corridor-mapped.

### Goal

Produce a Phase 2 scoring tensor: country × lens × scenario, plus first-pass fragility class assignments.

### Lens 4 scoring (Compounding Shocks Exposure)

Per the locked spec, Lens 4 measures worker-level shock combination + jurisdictional buffering asymmetry. Inputs:
- AI exposure (from L1)
- Climate transition shocks (worker-side: which occupations face green-economy displacement OR creation)
- Demographic shortage interaction
- Wealth concentration (proxy: Gini coefficient or wealth share of top 10%)
- Geopolitical fragmentation (worker-side: which countries face supply-chain reshoring + defence-sector labour demand shifts + migration flow volatility)
- **Jurisdictional buffering asymmetry** (key finding from retrofit v0.3 Case 1): EU strong worker protection vs UK/US weak protection → AI capital deployment relocates rather than slows. Score per country: (a) AI worker-protection stance, (b) adjacent-jurisdiction asymmetry exposure, (c) Mode 1 regional-economy vulnerability.

For each country, output:
- `lens4_compounding_shock_count` (how many of 5 inputs are at significant levels)
- `lens4_jurisdictional_buffering_squeeze_flag` (boolean — high on (a) AND (b) AND (c))
- `lens4_corridor_modifier` (does Lens 4 shift this country to a different corridor than Lens 1+2 alone? +/-/0)

**Phase 2 candidates are most likely jurisdictional-buffering-squeeze cases.** Specifically flag DE, FR, Nordics per spec.

### Lens 5 scoring (Polycrisis Drag)

4 inputs per the locked spec, each scored per country:

**(a) Polycrisis cluster** (decoupling + multi-front conflict + climate fragmentation):
- SIPRI 2025 military expenditure as % GDP
- NATO Hague 5%-by-2035 trajectory exposure
- Trade-policy decoupling exposure (export controls + sanctions architecture)
- Score: 0–1 normalised composite

**(b) Demographic load** — from L4 demographics-data.json: working-age shrinkage rate per country, dependency ratio shift, retirement-cohort size relative to entrant cohort. Candidates have no L4 data → `null` + flag.

**(c) AI labour load** — from L1 data.json: employment-weighted exposure × Klinger coordination-share weighting (if data permits, else flag) × Gostev capability-floor sensitivity bound (~9% Q1 2026).

**(d) Net climate position** (signed score per country) — adaptation capacity − physical vulnerability:
- Physical Vulnerability: wildfire risk + drought severity + flooding exposure + heat stress on outdoor work + agricultural disruption + infrastructure stress (use EEA EUCRA 2024 + Munich Re 2025 country breakdowns)
- Adaptation Capacity: climate-adaptation budget allocation + workforce trainable for Zone C climate work (use Cedefop 2025 country reports) + existing Zone C labour market depth (from L5) + institutional speed
- Score: signed (-1 to +1), with category buckets (net-positive / net-neutral / net-negative-capacity-side / net-negative-vulnerability-side)

Per-country output:
- `lens5_polycrisis_cluster_score` (0–1)
- `lens5_demographic_load` (0–1; null for candidates)
- `lens5_ai_labour_load` (0–1)
- `lens5_climate_net_position` (-1 to +1)
- `lens5_composite_drag_score` (weighted aggregate, methodology documented)

### 5-Scenario Stack scoring

For each country × each of the 5 scenarios, compute the corridor that country lands in under that scenario:

| Scenario | Mechanism | How to compute corridor under this scenario |
|---|---|---|
| **1 — Reinstatement Revival** | Augmentation effects strengthen; new-work creation reverts to or exceeds historical base rate | Reduce displacement velocity (Lens 1) by 30–50%; recompute ratio + corridor |
| **2a — Climate Adaptation Boom (with wage cliff)** | Zone C demand surge absorbs Zone A workers at current wage cliff (−25% to −40%) | Increase absorption capacity (Lens 1) by 50%; recompute |
| **2b — Climate Adaptation Boom (wage-neutral or positive)** | Climate-Zone-C work commands premium → cross-zone transition rate doubles | Increase absorption capacity by 100%; recompute |
| **3 — Muddle Through** | Current parameters persist | Phase 1 corridor (no change) |
| **4a — Structural Bias Compounds (reinstatement weakens)** | Reinstatement weakens further; bandwidth holds | Increase displacement velocity by 20%; same absorption; recompute |
| **4b — Structural Bias Compounds (bandwidth fractures)** | Bandwidth fractures; reinstatement holds | Apply Lens 5 Polycrisis Drag at 1.5x; reduce absorption by 20%; recompute |
| **5 — Cascading Institutional Failure** | Concurrent crises saturate bandwidth; capability floor breached | Apply Lens 5 at 2x; reduce absorption to 50% of Phase 1 value; capability floor breach |

Note: Scenario 4 has 2 subversions but Phase 1 modeled it as one. Output BOTH 4a and 4b per country.

Per-country output (8 corridor assignments per country: 5 scenarios + 2 subversions on 4 + 1 subversion on 2):
- `corridor_under_scenario_1`
- `corridor_under_scenario_2a`
- `corridor_under_scenario_2b`
- `corridor_under_scenario_3` (= Phase 1 baseline)
- `corridor_under_scenario_4a`
- `corridor_under_scenario_4b`
- `corridor_under_scenario_5`

### First-Pass Fragility Classes

For each country, assign Class I–IV based on cross-scenario stability:
- **Class I (Robust):** corridor stable across all 7 scenario variants (1, 2a, 2b, 3, 4a, 4b, 5)
- **Class II (Fragile):** corridor flips between scenarios (multiple distinct corridor assignments across the 7)
- **Class III (Pre-Failure Risk):** under Scenario 3 (Muddle Through), lands in Corridor 3 (Displacement Without Absorption); recovery possible only if Scenario 1 or 2b realises
- **Class IV (Active Cascade):** Lens 5 inputs already at maxima (e.g., polycrisis cluster score >0.8 + demographic load >0.8 + AI labour load >0.7 simultaneously); cascade is happening NOW, not predicted. Anchors: Ukraine + Russia (reference cases). For 36-country corridor map, candidates are most likely Class IV candidates if their Lens 5 readings are extreme.

Output: `phase2_fragility_class` (I / II / III / IV) per country.

### Regime Stability classification (added 2026-04-29)

Read `regime_*` fields from Bundle E Task 10 output. Per country, output:
- `regime_classification` — one of: `growth_baseline` (aggregate ≥1.5%), `secular_stagnation_warning` (aggregate <1.5% but per-capita ≥1.0%), `post_growth_empirical` (per-capita <1.0%)

For each country, when reporting scenario corridor assignments, include the regime classification. The same corridor carries different policy implications depending on regime per the comparison table in `layer-6-lens-framework.md` Regime Stability Note section. Do NOT re-score scenarios under post-growth in Phase 2 — that's Phase 3 scenario-realisation-probability adjustment. Phase 2 just classifies + flags.

**Sentinel test:** Italy + Germany should land in `secular_stagnation_warning` or `post_growth_empirical`. Nordics should land in `growth_baseline`. Japan-anchor reference: Japan would be `post_growth_empirical` if scored.

### Outputs

Update (NOT replace) Phase 1 output files into Phase 2:
- `projects/european-ai-labour-synthesis/layer-6-phase2-scoring.csv` — 36 rows + new columns for Lens 4 + Lens 5 + 7 scenario corridors + fragility class
- `projects/european-ai-labour-synthesis/layer-6-phase2-scoring.json` — same data, JSON-structured
- `projects/european-ai-labour-synthesis/layer-6-phase2-methodology-notes.md` — Lens 4 + Lens 5 scoring rubrics, scenario perturbation methodology, fragility class assignment rules, threshold sensitivity audit
- `projects/european-ai-labour-synthesis/layer-6-phase2-findings.md` — first-pass observations:
  - Which countries shift corridor under Lens 4 (jurisdictional-buffering-squeeze cases)
  - Which countries land in Class IV (Active Cascade) under Phase 2 alone
  - Which countries are Class I (Robust) — likely Nordics
  - Which countries are Class III (Pre-Failure Risk) — under Muddle Through, in Corridor 3
  - 4-candidate countries' fragility class (likely Class IV given partial coverage)
  - Open questions for Phase 3

### Constraints

- Do NOT modify `projects/european-ai-labour-synthesis/layer-6-lens-framework.md` (locked spec)
- Do NOT apply structural-bias re-calibration (Phase 3 lock per Q5)
- Do NOT reduce corridors below 3 — Phase 3
- Do NOT touch any layer repo
- **Read all Lens 4 + Lens 5 inputs from `projects/european-ai-labour-synthesis/layer-6-phase2-data.json`** (produced by Bundle E). Do NOT re-fetch primary sources during scoring. If a cell is missing or flagged as data-gap in that file, propagate the gap into the scoring output (use null + reason); do NOT fabricate.
- Per BR-21: every derived metric ships with derivation_method + uncertainty_band fields
- Phil does all git commit + push. Stage outputs; Phil executes.

### Verification

Before declaring Phase 2 complete:
1. Sanity-check the jurisdictional-buffering-squeeze finding: DE, FR, Nordics should flag for high (a) + (b) + (c). If they don't, methodology is wrong.
2. Sanity-check Class IV: candidates (BA, MK, RS, TR) should likely be Class IV given partial coverage + likely high polycrisis cluster scores. Ukraine reference case validates the class definition.
3. Sanity-check Class I: Nordics (DK, NO, SE, FI, IS) should be Class I (corridor stable across scenarios). If not, the scenario perturbation magnitudes are wrong.
4. Verify orthogonality finding from Phase 1 still holds after Phase 2 — Lens 4 + 5 should NOT re-introduce a buffer mechanism for any country.

### When done

Report back with:
- 4 output files shipped
- Lens 4 jurisdictional-buffering-squeeze countries (expected: DE, FR, Nordics; report actuals)
- Class I / II / III / IV distribution
- Scenario sensitivity per country (which countries flip corridor between which scenarios)
- Whether orthogonality finding survives Phase 2
- Open questions for Phase 3 (corridor reduction validation + structural-bias re-calibration)
- Methodology decisions needing Phil's review before Phase 3 starts

## END PROMPT
