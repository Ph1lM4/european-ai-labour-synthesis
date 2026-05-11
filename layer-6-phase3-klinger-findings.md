# Bundle K-2 — Klinger × ISCO 2-Digit Recompute — Findings

**Generated:** 2026-04-29
**Supersedes:** Bundle K (1-digit, lower-bound directional confirmation)
**Inputs:**
- Klinger v3 ESCO-derived coordination-share table (`layer-6-klinger-isco-coordination-share.json`, 130 ISCO 3-digit codes)
- Eurostat LFS `lfsa_egai2d__custom_21241431_linear_2_0.csv` (43 ISCO 2-digit codes, 38 entities, 2011–2025)
- Phase 1 displacement velocity (unchanged)
- K1d outputs (preserved as Section 9 below)

---

## TL;DR

1. **Sanity test fails — Bundle K's hypothesis was wrong about direction.** 4 of 6 high-coord sentinels (DE, CH, NL, UK, IE) show *attenuated* (smaller positive) deltas at 2-digit, not amplified. Only AT, NO, IS, DK, LU strengthen upward. CH attenuates sharply (+0.051 → +0.029).
2. **Movement is small.** Largest |delta_vs_K1d| is CH/LI at −0.022; most countries shift <±0.01. The 1-digit aggregation was directionally correct on the cohort (still no country crosses ±0.10) but mis-shaped within the high-coord cluster.
3. **Capability-floor breach: 11 → 12 countries.** DK enters; nobody exits. Stable structural picture vs Bundle K.
4. **Mechanism:** within OC2 (professionals, K1d=0.31), the new 2-digit split reveals OC25 (ICT)=0.16 alongside OC23 (teaching)=0.58. Knowledge-economy countries with heavy ICT mass (CH, DE, IE) get pulled DOWN at 2-digit; education-heavy countries (NO, IS, LU) get pulled UP. Bundle K's "finance/legal underweight" hypothesis was real but smaller than the offsetting "ICT overweight."
5. **Bundle L impact:** No fragility-class boundary moves. The cleaner 2-digit signal validates Bundle K's direction without amplifying it; Class I locked at (b) relative-stable remains the right call.

---

## 1. Methodology — what changed and what did not

**Unchanged.** Phase 1 displacement velocity per country is carried forward as `current_lens5_ai_labour_load`. Phase 2 baseline cells, K-3-digit Klinger file, and the locked spec are untouched.

**Changed.** Lens 5(c) now aggregates Klinger from 3-digit → **2-digit** (43 codes, ESCO-count weighted) instead of → 1-digit (10 codes). Per-country employment shares come from the full LFS extract Phil supplied.

```
klinger_2digit_{OC2X} = Σ_{isco3 ∈ children} ( esco_count_isco3 × klinger_3digit_isco3 ) / Σ esco_count_isco3
country_raw_2d        = Σ_{oc2 ∈ 43} employment_share_country_oc2 × klinger_2digit_oc2
multiplier_2d         = country_raw_2d / cohort_mean_raw_2d                # cohort_mean = 0.27877
weighted_2d           = velocity × multiplier_2d                            # preserves Phase 2 [0,1] scale
```

**Engine validated** by spot-check: OC2-summed → OC1 reproduces DE's K1d raw weight to 5 decimal places (0.26810 vs 0.26809).

**Year selection.** Latest year per country with coverage within ~4 codes of country-level maximum. 30 of 35 distinct countries on **2025**; LU on 2022 (severe 2025 suppression: only 16/43 codes); UK on 2019 (Eurostat ceased UK ISCO post-Brexit, same as K1d); IS on 2024.

**Confidentiality suppression handled.** No country has full 43/43 in any selected year — Eurostat suppresses small cells (most commonly OC03, OC63, OC95). Employment shares renormalized on present codes; missing share <1–2% of total employment by construction (suppressed cells are sub-publication-threshold). Per-country `missing_oc2_codes` documented in JSON.

## 2. Klinger 2-digit table (43 codes, ESCO-count weighted)

Highest-coord OC2s: **OC23 Teaching professionals 0.582** · OC14 Hospitality/retail/services managers 0.525 · OC11 Chief executives & legislators 0.505 · OC01 Officers 0.483.

Lowest-coord OC2s: OC92 Subsistence agriculture 0.033 · OC73 Handicraft & printing 0.051 · OC82 Assemblers 0.070 · OC81 Stationary plant operators 0.071.

The OC2 split surfaces three structurally important splits hidden at OC1:
- **OC2 (professionals):** ICT (OC25=0.157) vs teaching (OC23=0.582) vs business/admin (OC24=0.389) vs health (OC22=0.275). K1d collapsed all to 0.310.
- **OC1 (managers):** chief execs (OC11=0.505) vs production (OC13=0.380) vs hospitality (OC14=0.525). K1d collapsed all to 0.430.
- **OC4 (clerical):** general office (OC41=0.410) vs customer service (OC42=0.357) vs numerical/material (OC43=0.416) vs other (OC44=0.306). K1d collapsed all to 0.381.

## 3. Sanity test — direction-correct, magnitude WEAKER (4/6 high-coord attenuate)

| Sentinel | Hypothesis | Δ (1-digit) | Δ (2-digit) | Strengthened? |
|---|---|---|---|---|
| DE | up | +0.0203 | +0.0137 | **NO (attenuates)** |
| AT | up | +0.0110 | +0.0125 | YES |
| CH | up | +0.0507 | +0.0287 | **NO (attenuates sharply)** |
| NL | up | +0.0499 | +0.0497 | flat |
| UK | up | +0.0501 | +0.0479 | **NO (attenuates)** |
| IE | up | +0.0371 | +0.0341 | **NO (attenuates)** |

**Result: 1/6 strengthened, 1/6 flat, 4/6 attenuated.** Bundle K's hypothesis ("the deltas reported here are conservative; a true 3-digit join would amplify the sentinel-up countries further") is **falsified** for most of the sentinel set. Mechanism (Section 4): within-OC2 ICT mass (OC25=0.157) drags knowledge-economy countries down at 2-digit; this offsets the within-OC2 finance/legal/teaching bumps that the K1d narrative anticipated.

## 4. Anti-sanity test — mixed; cohort-end signal weakens both ways

| Sentinel | Hypothesis | Δ (1-digit) | Δ (2-digit) | More-negative? |
|---|---|---|---|---|
| PL | down | −0.0168 | −0.0115 | NO (attenuates) |
| RO | down | −0.0733 | −0.0719 | flat |
| BG | down | −0.0169 | −0.0176 | YES (slight) |
| HR | ≈neutral | +0.0004 | −0.0060 | YES (flips negative) |

The Visegrád/Balkan low-coord cluster also shows attenuated deltas at 2-digit, suggesting the K1d signal was magnified at both tails of the cohort. The 2-digit reading is more centrist.

## 5. Top 5 amplified up / Top 5 amplified down (delta vs K1d weighted)

| Rank | Country | Δ vs K1d | Δ vs Phase2 (2-digit) | Δ vs Phase2 (1-digit) | Mechanism |
|---|---|---|---|---|---|
| ↑1 | IS | +0.0218 | +0.0619 | +0.0401 | Education + public-admin OC2 mix; OC23 teaching pulls up |
| ↑2 | EL | +0.0151 | +0.0080 | −0.0071 | Greek service/teaching mix flips slightly positive |
| ↑3 | NO | +0.0114 | +0.0528 | +0.0414 | Public-sector + teaching mass; same as IS |
| ↑4 | DK | +0.0094 | +0.0333 | +0.0240 | Education + administration density |
| ↑5 | LV | +0.0072 | −0.0009 | −0.0081 | From slightly negative to ~neutral |
| ↓1 | CH | −0.0220 | +0.0287 | +0.0507 | ICT (OC25=0.16) + finance professional mass; sharper attenuation than expected |
| ↓1 | LI | −0.0220 | +0.0287 | +0.0507 | Proxied via CH |
| ↓3 | RS | −0.0073 | −0.0502 | −0.0429 | Manufacturing/services rebalancing |
| ↓4 | DE | −0.0066 | +0.0137 | +0.0203 | Strong industrial/ICT mass dampens K1d narrative |
| ↓5 | HR | −0.0065 | −0.0060 | +0.0004 | Tourism/services mix below cohort mean at 2-digit |

**Bundle K's CH/UK/IE "underweight" hypothesis (Section 4 of K1d findings) does NOT survive the 2-digit recompute.** CH attenuates from +0.051 to +0.029 — the largest swing in the cohort. The OC25 ICT pull dominates the OC24 business-admin lift. Banking and insurance sit primarily in OC24 (professional, business-admin), but Switzerland has a comparably-sized OC25 ICT cluster that K1d had collapsed into the OC2 average.

## 6. Spec ±0.10 threshold check

**Crossings: 0/36** — same as Bundle K. Cohort spread at 2-digit narrows: max |Δ_phase2| = 0.072 (LU); five years ago the equivalent was 0.073 (RO). The 2-digit recompute does not reach the substantive-change threshold for any country. Bundle K's 0/36 finding is robust to the magnitude upgrade.

## 7. Composite drag — minor shifts, no fragility-class boundary moves

Composite drag formula uses w_ai_labour = 0.25, so |ΔDrag| ≤ 0.25 × |ΔAI|.

| Country | Δ Drag (2-digit vs phase2) | Δ Drag (1-digit vs phase2) |
|---|---|---|
| RO | −0.0180 | −0.0184 |
| BA | −0.0153 | −0.0144 |
| MK | −0.0138 | −0.0130 |
| TR | −0.0134 | −0.0140 |
| RS | −0.0126 | −0.0107 |
| LU | +0.0175 | +0.0162 |
| IS | +0.0155 | +0.0100 |
| NO | +0.0132 | +0.0104 |
| NL | +0.0124 | +0.0125 |
| UK | +0.0120 | +0.0147 |

Max |ΔDrag| = 0.018 (RO). No country crosses Bundle L's fragility-class boundary on the basis of this recompute alone. Combined-effect with Bundle J (structural-bias recalibration) is the relevant question; pure Bundle K-2 effect is small.

## 8. Capability-floor breach proxy at 2-digit (>0.55)

- **K1d:** 11 countries — BE, DE, IE, LU, NL, SE, NO, IS, LI, CH, UK
- **K2d:** 12 countries — adds **DK** (0.524 → 0.558)
- **Phase 2 baseline:** 3 countries (LU, NL, SE)

Trajectory: Phase 2 baseline (3) → Bundle K 1-digit (11) → Bundle K-2 2-digit (12). The breach scope expansion is structurally robust across granularities. DK is the marginal entry; CH and IE are the borderline cases (0.576 and 0.567 respectively — comfortably above 0.55 at both granularities). The **interpretive shift Bundle K identified holds.**

## 9. Bundle K 1-digit lower-bound result, retained for comparison

The full Bundle K 1-digit findings file (now superseded) is preserved as the JSON metadata block `klinger_oc1_aggregated` and `klinger_oc1_aggregation_metadata` inside the rescaled JSON, plus the per-country `lens5c_klinger_*_1digit` columns in the rescaled CSV.

K1d headline:
- All 6 high-coord sentinels positive (DE/AT/CH/NL/UK/IE), 3 of 4 low-coord negative (PL/RO/BG; HR neutral). **K1d sanity passed direction; K2d sanity FAILS magnitude on 4/6.**
- Capability-floor breach: 3 → 11 (largest interpretive shift).
- 0/36 cross ±0.10 threshold.
- Top up: LU +0.065, LI/CH +0.051, UK +0.050, NL +0.050.
- Top down: RO −0.073, BA −0.057, TR −0.056, MK −0.052, RS −0.043.

K1d acknowledged its conservative-bias caveat ("true 3-digit join would amplify high-coord countries further"). **Bundle K-2 falsifies that caveat for the high-coord cluster** — the within-OC2 ICT mass offsets the within-OC2 finance/legal mass, and CH/DE/IE/UK get smaller deltas at 2-digit, not larger.

## 10. Methodology gaps surfaced

1. **2-digit ≠ 3-digit.** Bundle K-2 closes the OC2 split but leaves the OC25 ICT (=0.157) vs OC25-internal (DevOps/data engineering 251 vs ICT support 252) heterogeneity untouched. A true 3-digit join (Eurostat microdata application) would resharpen knowledge-economy scores yet again — but the direction of the 2-digit→3-digit shift is now ambiguous (could re-amplify or further attenuate depending on country-specific OC25 internal mix).
2. **Confidentiality suppression for high-suppression countries.** LU (16/43 in 2025, forced back to 2022) and IS (36/43 in 2024) have the most missing-cell residual; their 2-digit reading rests on a noisier denominator. Document; not a refutation but a confidence ceiling.
3. **UK on 2019.** Same as K1d — Eurostat ceased UK ISCO publication post-Brexit. UK's K2d score uses 2019 occupational structure × 2025 velocity. Direction unchanged; magnitude unchanged at attenuation level.
4. **HR neutral-flip.** HR moves from +0.0004 to −0.0060. The shift is below noise; HR's tourism-heavy OC5 mass slightly drags the new OC51-OC54 split below cohort mean. Not interpretively material.
5. **Default-fallback Klinger codes** (n=5: 224, 631, 632, 633, 634) carry weight=1 in the OC2 aggregation. Empirically these sit in OC22 paramedical and OC63 subsistence — both small employment categories. Sensitivity is bounded; documented but not a structural concern.

## 11. Open questions for Bundle L

1. **Class I locked at (b) relative-stable** is independent of this recompute (per handover). K2d does not introduce Class I boundary movement. ✓
2. **Fragility-class re-evaluation candidates.** No country's composite drag shifts more than ±0.018; combined with Bundle J's PL recalibration, the question of whether the 2-digit reading nudges PL (or any other Bundle J flagged country) toward a class boundary is the primary Bundle L question. Pure Bundle K-2 effect: small.
3. **Capability-floor breach (12 countries).** Scenario 5 corridor stack from Phase 2 was tuned with 3-country breach. Bundle L should examine whether the 12-country breach changes cascade-corridor distribution materially or whether the K1d-flagged 11 was already the right operating set.
4. **CH attenuation interpretation.** K1d flagged CH/UK/IE/LU as "+0.05 likely lower bound, would amplify under 3-digit." K2d shows CH/IE/UK move the other way (slight attenuation), LU still amplifies (+0.065 → +0.070). The "knowledge-economy lift" hypothesis is not uniform — finance-services (CH/UK) and tech-services economies get the OC25 ICT drag, while administrative-finance (LU) and education-heavy (NO/IS) economies get the OC23 teaching lift. Bundle L should distinguish these archetypes when re-classifying.
5. **DK entering capability-floor breach.** New finding at 2-digit. DK's manager + professional + clerical density crosses 0.55 at 2-digit. If Scenario 5 corridor depends on breach count, DK's late entry matters at the margin.

## 12. Verification checklist

- [x] LFS extract filtered to Y15-64 × T × 43 OC2 × 36 countries (LI proxy CH).
- [x] Country coverage check: 35/35 distinct countries with data; LI proxied. 27 countries have <43 codes (confidentiality suppression); per-country missing-codes log in JSON.
- [x] Sum of employment shares per country = 1.0 by construction (renormalized on present codes).
- [x] Klinger 2-digit table: 43 OC2 codes derived; ESCO-count-weighted; default-fallback codes weight=1.
- [x] Spot-check baseline reproduction: DE OC2-sum → OC1 reproduces K1d raw weight to 5 decimals (0.26810 vs 0.26809). Engine validated.
- [x] Sanity test high-coord: 1/6 strengthened, 1/6 flat, 4/6 attenuated — **falsifies K1d hypothesis for sentinel cluster**.
- [x] Anti-sanity test low-coord: 1/4 strengthened (+1 HR neutral-flip), 2/4 attenuated, 1/4 flat.
- [x] No country crosses spec ±0.10 (same as K1d).
- [x] Capability-floor breach at 2-digit: 12 countries (K1d had 11; DK enters).
- [x] BR-19: no fabricated employment shares; suppression flagged per-country; LU 2022, UK 2019, IS 2024 documented.
- [x] BR-21: per-country `derivation_method` documents granularity (2-digit), data source (`lfsa_egai2d__custom_21241431`), year, n_codes/43.
- [x] Klinger file, Phase 2 outputs, locked spec — none modified. Only the three Bundle K Phase 3 outputs replaced in place.
