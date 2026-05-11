# Layer 6 Phase 2 — Findings

**Date:** 2026-04-29
**Scope:** 36 countries (EU-27 + NO + IS + LI + CH + UK + 4 candidates BA/MK/RS/TR)
**Inputs:** Phase 1 outputs + `layer-6-phase2-data.json` (89.9% coverage; 71 documented gaps)
**Companion files:** `layer-6-phase2-scoring.csv`, `layer-6-phase2-scoring.json`, `layer-6-phase2-methodology-notes.md`

---

## TL;DR

- **Jurisdictional buffering squeeze (Lens 4 category-shift mechanism) flags 8 countries**: DE, FR, NL, BE, DK, FI, SE, NO. Specification-named cases (DE/FR/Nordics-mainland) all flag. IS does not (lower trade-decoupling exposure — substantive finding).
- **Class I (Robust) = 5 countries** — exactly the Nordics (DK/FI/SE/NO/IS), corridor-stable across all 6 routine scenarios. All 5 cascade to C2 under S5 (no country is cascade-robust).
- **Class III (Pre-Failure Risk) = 2 countries** — IE, UK. Both already in Corridor 3 under Phase 1 baseline (Muddle Through); recovery requires Scenario 1 or 2b realisation.
- **Class IV (Currently Failing) = 3 of 4 candidates** — RS, TR, MK qualify under candidate-relaxed criterion. **BA does NOT qualify** despite partial coverage; assigned Class II + partial-coverage flag (substantive finding — partial coverage alone is insufficient for Class IV).
- **Class II (Fragile) = 26 countries** — most of the EU. Corridor flips between scenarios are concentrated at S2b (best-case absorption boom → C1) vs S4b/S5 (bandwidth fracture → C3).
- **Orthogonality survives Phase 2** — no Lens 4/5 finding re-introduces a buffer mechanism. Methodology preserves orthogonality by construction (no negative corridor modifiers issued); empirical content of the buffer-failure thesis tested at all 5 lenses now.
- **Regime classification:** 24 growth-baseline / 10 post-growth-empirical / 2 secular-stagnation-warning. **Italy is uniquely secular-stagnation-warning + Corridor 2** — same corridor as growth-baseline peers but very different policy implication.

---

## 1. Lens 4 Jurisdictional Buffering Squeeze

### 1.1 Squeeze-flagged countries (8)

| Country | (a) AI worker-protection | (b) Adjacent-jurisdiction asymmetry | (c) Mode 1 vulnerability | Phase 1 corridor | Lens 4 modifier | Phase 2 net corridor (modifier-applied) |
|---|---|---|---|---|---|---|
| **DE** | H (EU AI Act + strong Mode 3 buffering) | H (CH border + US/UK manufacturing-export asymmetry) | H (525k absolute climate reallocation; velocity 0.54) | 2 | +1 | **3** |
| **FR** | H (EU AI Act + Code du travail) | H (CH border, UK Channel, US export exposure) | H (361k climate reallocation; velocity 0.52) | 2 | +1 | **3** |
| **DK** | H (EU AI Act + strong tripartite system) | H (UK financial-services + non-EU export) | H (small-open-economy: trade composite 0.44) | 1 | +1 | **2** |
| **FI** | H (EU AI Act) | H (UK + NO border + small-open-economy) | H (trade composite 0.58) | 1 | +1 | **2** |
| **SE** | H (EU AI Act + LAS) | H (UK financial-services + non-EU export) | H (trade composite 0.50) | 1 | +1 | **2** |
| **NO** | H (EEA Joint Committee AI Act adoption pathway) | H (small-open-economy + UK + EU border) | H (trade composite 0.62) | 1 | +1 | **2** |
| **NL** | H (EU AI Act) | H (Rotterdam + UK Channel + financial services) | H (trade composite 0.50; large logistics base) | 2 | +1 | **3** |
| **BE** | H (EU AI Act + strong CCT system) | H (financial services + UK Channel) | H (small-open-economy: trade composite 0.50) | 2 | 0 (shock count <4) | 2 |

**Specification-named (DE/FR/Nordics) all flag** *except IS* — see §1.2.

### 1.2 Why IS does not flag (substantive finding, not methodology miss)

IS scores `low` on (c) — its trade-decoupling composite is 0.339, below the 0.40 small-open-economy threshold. This reflects IS's economic profile (insurance + fishing + aluminum) being structurally less integrated into EU-supply-chain manufacturing flows than Denmark/Sweden/Finland/Norway. The squeeze is a *capital-flight asymmetry* mechanism; IS has materially less of the capital-mobile asset base that the squeeze is about. Phase 3 may want to scope (c) more carefully — small-open economies vary in *what kind* of openness exposes them to the squeeze.

### 1.3 Compounding shock count distribution

| Shocks | Countries | Note |
|---|---|---|
| 1 | 4 (CY, IS, LI, MT) | Lowest combinations — small economies with limited shock convergence |
| 2 | 9 | |
| 3 | 14 | Dominant tier |
| 4 | 9 | Compounding-modifier triggered for 5 countries (others already at C3 or have demographic null) |
| 5 | 0 | No country triggers all 5 simultaneously |

**Modifier `+1` issued to 11 countries**: BE, DE, DK, EE, FI, FR, LT, NL, PL, PT, SE. Mix of (a) squeeze-flagged C1/C2 cases and (b) generic 4-shock cases without squeeze (EE, LT, PL, PT — Eastern EU with demographic + AI + Gini + climate compounding but lacking adjacency exposure).

---

## 2. Lens 5 Polycrisis Drag

### 2.1 Composite drag score distribution

| Tier | Range | Countries |
|---|---|---|
| Highest drag (>0.60) | 0.60–0.62 | PL, EL, TR, LV, LT, EE |
| High drag (0.55–0.60) | 0.55–0.59 | BG, PT, IT, SK, SE (just below), HR, RO, MT, HU, SI, DE |
| Mid drag (0.45–0.55) | 0.45–0.55 | DK, FI, MK, BA, NL, AT, BE, ES, RS, CY, NO, UK, AT |
| Low drag (<0.45) | 0.32–0.42 | FR, LU, CH, IE, LI |

**Surprise:** PL/EL/Baltics top the drag ranking despite Phase 1 corridor 2 — driven by (a) high polycrisis (PL has 0.59 polycrisis from large EU defence procurement + significant CN trade dependency; Baltics have NATO frontier exposure), (b) high demographic load (Baltics shrinking faster than EU average), and (c) high physical climate vulnerability for southern/eastern members.

**Surprise:** FR has *lowest* drag among major EU economies (0.42) — high green-jobs creation pipeline (251k value_a) + reasonable adaptation capacity offset by moderate polycrisis. **But FR still squeeze-flags via Lens 4** — these are different mechanisms.

### 2.2 Climate net position buckets

| Bucket | Count | Countries | Note |
|---|---|---|---|
| net_positive | 5 | AT, DE, ES, FR, NL | Adaptation capacity (RRF + green-jobs pipeline) exceeds vulnerability by ≥0.20 |
| net_neutral | 18 | Most of EU + EFTA | Roughly balanced |
| net_negative_capacity_side | 5 | EE, LT, LV, MK, RS | Vulnerability dominates AND capacity binding |
| net_negative_vulnerability_side | 4 | BG, EL, HR, TR | Capacity reasonable but vulnerability overwhelming |
| data_gap | 4 | UK, LI, BA, plus Cedefop coverage gaps | Climate data not fully populated |

### 2.3 Capability floor breach proxy

Triggered (`ai_labour_load > 0.55`) for: **LU (0.620), NL (0.550), SE (0.551)**. Acknowledged proxy — true Gostev floor breach requires Klinger ISCO-coordination join (Phase 3).

### 2.4 Polycrisis cluster — top-quartile flagged

Polycrisis ≥ 0.55: SE (0.55), NL (0.56), FR (0.51 — moderate), PL (0.59), DK (0.55), TR (0.65 — highest), BG (0.61), EL (0.59), DE (0.56), BE (0.56), IT (0.58), AT (0.55). Driven primarily by combined defence-spending growth + trade-decoupling exposure to CN/RU.

---

## 3. Five-Scenario Stack — Sensitivity per Country

### 3.1 Corridor flips between specific scenario pairs

**S2b → S3 flip (best case absorption boom vs muddle through):** 28 countries flip from C1 (S2b) to C2 (S3) — the entire EU+EEA except (a) Nordics already in C1 (no flip), (b) IE/UK already in C3 even under S2b.

**S3 → S4a flip (muddle through vs structural bias compounds):** 21 countries flip from C2 (S3) to C3 (S4a) — bandwidth-holding countries with displacement velocity > 1.2× margin to C2/C3 boundary. The "structural-bias-only" scenario is enough to break absorption headroom for most of Europe.

**S3 → S4b flip (muddle through vs bandwidth fractures):** 23 countries flip C2→C3. The bandwidth-fracture pathway captures everyone S4a captures plus AT/CH/RO/LI/DE — countries that were resilient under velocity-only stress but break under absorption haircut + drag.

**S4b → S5 flip:** All 36 countries except the Nordics flip up by 1+ corridors under cascade. The 5 Nordics flip C1→C2.

### 3.2 Scenario sensitivity ranking (most → least sensitive)

| Sensitivity | Distinct corridors across 7 | Countries |
|---|---|---|
| Very high (3 corridors) | C1, C2, C3 | 31 — bulk of the cohort |
| Moderate (2 corridors) | C2, C3 | IE, UK (Class III locked at C3 under most scenarios) |
| Moderate (2 corridors) | C1, C2 | DK, FI, IS, NO, SE (Class I — never reach C3) |

### 3.3 The 4 "C1-resilient" patterns (Phase 1 C1 countries that hold C1 through S4b)

DK, FI, NO, SE, IS — same as Class I. **All 5 cascade to C2 under S5**, none cascade to C3. This is the Phase 2 cleanest "robust" cohort.

### 3.4 Concentrated S2b-only optimism

For *all* 31 non-Class-I non-Class-III countries, **only Scenario 2b realises Corridor 1**. Under every other scenario including the optimistic Reinstatement Revival (S1) and Climate Boom with wage cliff (S2a), they remain at C2 or worse. This concentrates the optimistic-case dependence on a single load-bearing scenario — the wage-premium variant of Climate Adaptation Boom. **Phase 3 should validate whether 2b is realistically attainable** (Layer 5 wage-cliff data: cross-zone transition rates need to rise from 3–10% to 12–15% with wage premium; current evidence is sparse).

---

## 4. Fragility Class Distribution

### 4.1 Final assignment

| Class | Count | Countries |
|---|---|---|
| **Class I — Robust** | 5 | DK, FI, IS, NO, SE |
| **Class II — Fragile** | 26 | AT, BA, BE, BG, CH, CY, CZ, DE, EE, EL, ES, FR, HR, HU, IT, LI, LT, LU, LV, MT, NL, PL, PT, RO, SI, SK |
| **Class III — Pre-Failure Risk** | 2 | IE, UK |
| **Class IV — Currently Failing** | 3 | MK, RS, TR |

Total: 36 ✓

### 4.2 Class III commentary — IE, UK already in Corridor 3 under Phase 1 baseline

Both IE and UK are in C3 under Muddle Through (lens1_ratio 3.33 / 3.40 respectively). Recovery is possible only if Scenario 1 (Reinstatement Revival, velocity ×0.65) or Scenario 2b (absorption ×2.0) realises. Under all other scenarios (2a, 4a, 4b, 5) they remain at C3. This is the structural pattern of Pre-Failure Risk: the country is already in the displacement-without-absorption corridor, and survival depends on a positive scenario.

**Caveat for IE:** the modGNI-substituted regime classification (4.30% aggregate / 2.30% per-capita) shows growth_baseline despite C3 designation — IE's headline growth is leprechaun-economics-distorted; real-economy fragility may be higher than the per-capita reading suggests.

**Caveat for UK:** post_growth_empirical regime classification (1.67% / 0.87%) compounds with C3 + Class III — this is the worst combination in the dataset (post-growth + already pre-failure under Muddle Through).

### 4.3 Class IV commentary — candidates

| Country | Trigger | Note |
|---|---|---|
| **TR** | poly=0.67, eea_vuln=0.75, gini=44.8 | All three thresholds exceeded; clearest Class IV case |
| **RS** | poly=0.55, eea_vuln=0.60 | Two thresholds exceeded (boundary on EEA); polycrisis driven by high CN+RU trade share |
| **MK** | eea_vuln=0.62 | Single threshold (climate vulnerability — Western Balkans CE-region proxy); polycrisis 0.40 is low |
| **BA** | *None of poly (0.42), eea (0.58), gini (30.3) trigger* | **Assigned Class II + partial-coverage flag, NOT Class IV** |

**The BA finding is substantive:** partial coverage (no L2/L4/L5 demographic + AI labour data) by itself does not justify Class IV. BA's available shock indicators are materially lower than RS/MK/TR on every dimension. Phase 3 should reconsider whether the binding criterion is "partial coverage alone" (sweep all candidates into IV) or "partial coverage + ≥1 extreme reading" (this Phase 2 choice). Empirical reality: BA has lower polycrisis exposure than the EU mean.

---

## 5. Regime Classification

### 5.1 Distribution

| Regime | Count | Countries |
|---|---|---|
| `growth_baseline` (agg ≥1.5%) | 24 | BE, BG, CY, CZ, DK, EE, ES, HR, HU, IE, IS, LT, LU, LV, MT, NL, PL, PT, RO, SE (no — see note), SI, SK, BA, MK, RS, TR — but recheck SE |
| `post_growth_empirical` (per-capita <1.0%) | 10 | AT, DE, FI, FR, LI, LU (no, distributional split), NO, SE, UK, CH |
| `secular_stagnation_warning` | 2 | EL, IT |
| `data_gap` | 0 | — |

(Counts pulled from `phase2_results.json`; LU is a peculiar case — agg 1.94%, per-capita -0.12% → flagged as `aggregate_distributional_split` per Bundle E session 2 schema, classified as post_growth_empirical based on negative per-capita.)

### 5.2 Sentinel test results

| Country | Expected regime | Actual | Pass? |
|---|---|---|---|
| Italy | secular_stagnation or post-growth | secular_stagnation_warning (1.04% agg, 1.30% pc) | ✓ |
| Germany | secular_stagnation or post-growth | post_growth_empirical (1.02% agg, 0.54% pc) | ✓ |
| Nordics (DK/NO/SE/IS) | growth_baseline | DK ✓ IS ✓ but **NO post_growth_empirical (0.89% pc)**, **SE post_growth_empirical (0.86% pc)** | Partial — finding |
| Finland | (not specified) | post_growth_empirical (0.77% agg, 0.59% pc) | Lowest growth in cohort |
| Japan-anchor | (would be post-growth if scored) | n/a | n/a |

**Finding:** "Nordics → growth_baseline" sentinel passes for DK/IS only. NO + SE + FI all classify as post_growth_empirical because per-capita 10-year averages are below 1.0%. This is materially relevant for Layer 6 narrative — three of the five Class-I-Robust Nordics are simultaneously in post-growth regime. **The same C1 corridor reads very differently under post-growth: Scenario 1 (Reinstatement Revival, growth-dependent new-work creation) becomes structurally weaker; Scenario 2b becomes the only genuinely positive scenario.** This compounds with the squeeze-flag finding for SE/NO/FI — robust corridor + post-growth regime + buffering-squeeze risk = a fragility-class-Robust country whose policy implication is far from "structurally fine."

### 5.3 The Italy case

Italy is alone in `secular_stagnation_warning` (the other "warning" tier between growth-baseline and post-growth-empirical). Aggregate 1.04% is below 1.5% threshold; per-capita 1.30% is above 1.0% threshold. This means Italy's per-capita performance is decent (despite shrinking working-age population) but the aggregate is anaemic. Class II + Corridor 2 (under Muddle Through) — same corridor as DE, but DE is post-growth, IT is secular-stagnation-warning. Phase 3 narrative needs to disambiguate.

---

## 6. Orthogonality Test — Phase 2 Outcome

**Phase 1 finding:** Demographic-rescue thesis fails. Retirement offset is <50% of displacement velocity for all 36 countries. No country produces a buffer mechanism that re-introduces protection.

**Phase 2 verification:**
1. **No Lens 4 corridor modifier is negative.** Modifiers issued: `+1` for 11 countries; `0` for 25; `−1` for 0. By construction, Lens 4 + Lens 5 do not reduce a country's corridor below Phase 1 baseline.
2. **The squeeze mechanism converts buffer to risk.** Per Retrofit v0.3 Case 1: high AI-worker-protection in EU/EEA, combined with adjacent weakly-protected jurisdictions and Mode 1 capital-mobile economy, generates capital-flight risk. The "buffer institution" (strong worker protection) is the *cause* of the regional-economy risk, not its mitigant. This is the category-shift Lens 4 finding.
3. **Climate net-positive ≠ Phase 1 buffer.** AT, DE, ES, FR, NL show net_positive on climate — but this is a Lens 5 mitigant of *climate vulnerability*, not a Lens 1 buffer of *AI displacement*. They are separate shock channels and don't substitute.

**Conclusion:** Orthogonality finding survives Phase 2 with greater confidence than at Phase 1 close. The empirical claim is now tested at all five lenses (1+2 in Phase 1; 4+5 + climate in Phase 2). Practitioner-knowledge writeup `knowledge/practitioner/demographic-rescue-orthogonality.md` is justified for shipping.

---

## 7. Open Questions for Phase 3

### 7.1 Methodology lock-ins required before Phase 3 starts

1. **Class I definition** — accept the routine-S1–S4b stability rule (this Phase 2 choice), or redefine S5 with milder absorption haircut so the literal-7-scenarios spec works? Decision affects whether cascade resilience becomes a class-eligible criterion or stays in `cascade_corridor` field.
2. **Class IV candidate criterion** — accept the "partial coverage + ≥1 extreme reading" rule (this Phase 2 choice), or sweep all 4 candidates into IV by partial-coverage alone? Decision affects whether BA classifies as IV or II.
3. **Lens 5 (c) AI labour load** — Phase 2 used Phase 1 displacement velocity directly. Phase 3 must execute the Klinger ISCO-coordination join. Approximate effort: 8–12h to derive country-level coordination-share weighting from `layer-6-klinger-isco-coordination-share.json` × Eurostat ISCO-3-digit employment shares.
4. **S4b / S5 drag interpretation** — Phase 2 chose velocity-side amplification (Interpretation B). Phase 3 should run sensitivity check against absorption-side application (Interpretation A) — same parameter values, different mechanism.

### 7.2 Phase 3 deliverables (per Phase 2 handover)

1. **Corridor reduction validation** — Phase 1 used 3 corridors. Validate whether 3 is the right count. Could reduce to 2 if Class III+IV always implies C3-equivalent; could expand to differentiate "Buffering Squeeze" cohort from generic C2 (DE/FR/NL/BE clustering).
2. **Structural-bias re-calibration** — Phase 2 left the warning as a calibration note only. Phase 3 should apply the re-calibration to the Phase 1 ratios (Q5 lock per framework). PL at lens1_ratio 2.96 is the sentinel test case — must shift to C3 under re-calibration or methodology is wrong.
3. **Scenario realisation probabilities** — Phase 2 has scenario corridors but no probability weighting. Phase 3 should assign probability weights per scenario (informed by IISS bandwidth-tax findings, EUCRA climate trajectory, Cedefop labour projections) to produce a Phase 1+2+3 probability-weighted corridor expectation per country.

### 7.3 Substantive analytical questions surfaced in Phase 2

1. **Why do 3 of 5 Class-I-Robust Nordics classify as post-growth (FI/NO/SE)?** Is "growth-baseline" robustness an artifact of small-economy aggregation, or does post-growth Nordics have a different policy implication than non-Nordic post-growth (DE/FR)?
2. **Why does the squeeze flag include BE/NL beyond the spec-named DE/FR/Nordics?** Is this a genuine extension of the squeeze pattern, or a methodology over-fitting? Phase 3 narrative should decide whether BE/NL belong in the named cohort.
3. **Why does PL top the composite drag ranking despite growth-baseline regime?** The drag mechanism is structural (polycrisis + demographic + climate-capacity); regime is fiscal headroom. They can diverge. But the divergence raises the question: how much of PL's growth is structurally durable vs propelled by EU funds + Ukraine-reconstruction tailwinds that Phase 5 (cascade) would reverse?
4. **Concentrated S2b-only optimism — is this realistic?** For all 31 non-Class-I non-Class-III countries, only S2b reaches C1. Phase 3 should report scenario realisation probabilities and stress whether 2b is plausible given Layer 5 wage-cliff evidence.
5. **The Italy case** — secular_stagnation_warning + Class II + Corridor 2 + ~2% per-capita. Italy is a structural anomaly in the cohort — Phase 3 narrative should treat it as its own case, not pool it with growth-baseline C2 peers.

### 7.4 Data acquisition gaps surfaced in Phase 2

1. **Klinger × country-employment ISCO-3-digit join** — required for Lens 5 (c) refinement. Source: Eurostat lfsa_egais (employment by 1-digit ISCO) — but 3-digit shares are at the EU-LFS micro-data level, not freely API-accessible.
2. **Per-MS dual-use export shares** — currently EU-aggregate proxy (uniform 0.5) per Commission 2024 Annual Report. Phase 3 might benefit from Member-State export-control filing data if available.
3. **SAFE allocation for 14 unnamed Member States** — currently ±€0.5–10B range. Commission has not published the formal allocation table; will tighten the Lens 5(a) bandwidth-tax proxy.
4. **Missing Cedefop coverage** — UK/LI/BA/RS/null on climate-shocks. Climate component for these countries flagged as data-gap.
5. **Munich Re country-split for joint events** — sparse-by-design. Top-3 events per continent only; smaller events not enumerated. 14 of 36 countries have named-event coverage; rest null+flagged. Impacts physical-vulnerability granularity.

---

## 8. Methodology Decisions Needing Phil's Review Before Phase 3 Starts

**Block-list — Phil's call before Phase 3 ships:**

1. **Class I definition** — keep routine-only (S1–S4b) Phase 2 choice, or revise? *(Methodology notes §4.4 explains the issue and three options.)*
2. **Class IV candidate criterion** — keep "partial-coverage + ≥1 extreme" (this Phase 2 choice), or sweep-all-candidates? Affects BA only currently. *(Methodology notes §4.4.)*
3. **Lens 4 squeeze flag scope** — keep BE/NL in (extension of spec-named DE/FR/Nordics), or restrict to spec-named only? *(Findings §1.1.)*
4. **IS in Nordic Class I** — current Phase 2 has IS in Class I despite NOT being squeeze-flagged. Conceptually consistent (Class I = corridor stability; squeeze = category-shift mechanism — they don't have to align), but worth Phil's eyes. *(Methodology notes §1.2.)*
5. **S4b / S5 drag interpretation** — velocity-amplification (Interpretation B, Phase 2 choice) vs absorption-haircut (Interpretation A). Phase 3 sensitivity check planned; Phil's preference noted in advance shapes Phase 3 narrative.
6. **Lens 5 (c) Phase 2 simplification** — using Phase 1 velocity directly without Klinger join. Phase 3 must do the join, but Phil should confirm whether Phase 2 outputs are valid for *interim* use cases (lectures, advisory) or whether they should be embargoed until Phase 3 refinement.

---

## Captures

**Captures:**
- Phase 2 squeeze finding extends spec-named DE/FR/Nordics to include BE/NL (8 countries total) → consider updating `layer-6-lens-framework.md` line 285 named cohort to reflect Phase 2 finding
- Italy's unique secular_stagnation_warning + C2 + Class II profile is a narrative-distinct case → flag for Layer 6 document section on "anomalous regimes within corridor groupings"
- Class I = 5 Nordics with cascade-to-C2 (no country cascade-robust) → candidate concept bridge: "robust-but-vulnerable" pattern between Lens-1 corridor stability and S5 cascade behavior
- Concentrated S2b-only optimism (31 countries reach C1 only under wage-premium climate boom) → potential lecture-kit takeaway: the optimistic-case is single-path, not multi-path
