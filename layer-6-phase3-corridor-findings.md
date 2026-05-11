# Layer 6 Phase 3 — Structural-Bias Re-Calibration Findings (Bundle J)

**Date:** 2026-04-29
**Scope:** Lens 1 corridor re-calibration + Phase 2 fragility class re-derivation under new corridor mapping. 36 countries.
**Outputs:** `layer-6-phase3-corridor-rescaled.csv/.json` + `layer-6-phase3-corridor-methodology.md` (this file's companion).

---

## TL;DR

1. **PL sentinel test PASS.** Ratio 2.955 → C3-rescaled, Class III. Methodology re-locked at C1<1.20, C3≥2.80.
2. **13 countries shift C2 → C3** (CZ, HU, SI, EL, IT, LT, HR, SK, CY, EE, PT, MT, PL). 0 shift downward. Corridor distribution moves from 5 / 29 / 2 (Phase 1) to **5 / 16 / 15** (Phase 3) — triadic balance achieved.
3. **Class III count grows from 2 → 15** (the 13 corridor-shift countries gain Class III by Muddle Through criterion). Class IV unchanged (TR/RS/MK). **Class I collapses 5 → 0** under naive carryover — surfaced as load-bearing methodology question.
4. **Squeeze-flag BE/NL extension is orthogonal to displacement-corridor recalibration.** Confirmed: keep extension; document as a different signal channel (jurisdictional buffering ≠ displacement velocity).
5. **3-corridor count locked at 1.20 / 2.80** (theory-driven). 4-corridor alternative (split C3 at 3.00 for Liberal Market IE+UK) surfaced for master-session adjudication, not auto-applied.
6. **Bundle J independent of Bundle K — no blocking dependency.** Klinger ISCO join (Bundle K) operates on `ai_labour_load`; corridor recalibration operates on `lens1_ratio` thresholds. Different inputs, no cross-contamination.

---

## 1. PL sentinel test result

| Metric | Value |
|---|---|
| Sentinel country | PL (Poland) |
| `lens1_ratio` | 2.955 |
| Phase 1 corridor (naive thresholds 1.5/3.0) | 2 |
| Phase 3 corridor (recalibrated 1.20/2.80) | **3** |
| Phase 1 fragility class | II |
| Phase 3 fragility class | **III** (gains Pre-Failure Risk under Muddle Through criterion) |
| Verdict | **PASS** — ratio sits 5.5 percentage points above the new C3 floor; unambiguous shift |

PL was named in the locked spec (line 54) as the single Phase 3 sentinel. Methodology survives.

---

## 2. Top corridor shifts (gainers + losers)

**0 countries shift downward.** All 13 shifts are upward (C2 → C3). No country moves C3 → C2 or C2 → C1 under recalibration — orthogonality finding survives by construction (Phase 2 §6 still holds).

**All 13 C2 → C3 shifts (sorted by ratio, highest first):**

| Country | Ratio | Sub-region | Notes |
|---|---|---|---|
| PL | 2.955 | Central/Eastern European | Sentinel — load-bearing case |
| MT | 2.910 | Southern European | small island; sparse-data flag from Phase 1 |
| EE | 2.902 | Central/Eastern European | digital-state; flagged for Nordic-light dual scoring (Phase 1 §4.1) |
| PT | 2.902 | Southern European | demographic decline + fragmented ALMP |
| CY | 2.889 | Southern European | small island; sparse-data flag |
| HR | 2.887 | Central/Eastern European | sharpest_decline tier |
| SK | 2.887 | Central/Eastern European | unassigned-tier proxy |
| LT | 2.869 | Central/Eastern European | sharpest_decline tier |
| IT | 2.840 | Southern European | secular_stagnation_warning regime |
| EL | 2.833 | Southern European | secular_stagnation_warning regime |
| SI | 2.824 | Central/Eastern European | unassigned-tier proxy |
| HU | 2.820 | Central/Eastern European | unassigned-tier proxy |
| CZ | 2.808 | Central/Eastern European | unassigned-tier proxy |

**Pattern:** The 13 shifts split cleanly along the Phase 1 sub-cluster lines — 7 CEE (the entire Central/Eastern European sharpest_decline + unassigned-tier band) + 6 Southern European (most of the cluster minus ES at 2.755 and BG at 2.760, both sitting just below the new floor).

**Countries that *almost* shifted (within 0.04 of new C3 floor):**

| Country | Ratio | Distance to 2.80 |
|---|---|---|
| ES | 2.755 | −0.045 |
| LV | 2.766 | −0.034 |
| BG | 2.760 | −0.040 |
| RS | 2.744 | −0.056 |

These four would shift to C3 under a slightly looser C3 floor (e.g. 2.74). Sensitivity-band recommendation in §7.

---

## 3. Fragility class distribution old → new

| Class | Phase 2 | Phase 3 (naive carryover) | Δ |
|---|---|---|---|
| I — Robust | 5 | **0** | −5 |
| II — Fragile | 26 | 18 | −8 |
| III — Pre-Failure Risk | 2 | 15 | +13 |
| IV — Currently Failing | 3 | 3 | 0 |

### 3.1 Countries that changed class (18 total)

**To Class III (+13):** CY, CZ, EE, EL, HR, HU, IT, LT, MT, PL, PT, SI, SK
- All 13 are the C2→C3 corridor-shift countries; their Muddle Through ratio (= Phase 1 baseline ratio) now lands ≥2.80, triggering Class III.

**Out of Class I (−5):** DK, FI, IS, NO, SE
- All 5 Nordics drop from Class I to Class II under naive carryover.
- Mechanism: under tightened C1 cap (1.20), Nordic baseline ~1.05 plus ×1.20 velocity multiplier under S4a yields ratio ~1.26 → C2-rescaled, breaking corridor-stability criterion.
- This is **methodologically symmetric to the Phase 2 S5 collapse** — a stricter mapping makes "stable" empirically un-achievable, requiring a definition amendment to remain analytically meaningful.

### 3.2 Class I collapse — recommendation

The methodology document (§3.3) surfaces three resolution options. **Bundle J recommends option (b): redefine Class I as relative-stable** — country's Phase 3 corridor under all six routine scenarios stays within ±1 corridor of its Phase 3 baseline corridor. Under this definition, all 5 Nordics return to Class I (they remain in C1 under S3 Muddle Through and only shift to C2 under stress, never to C3).

This preserves the institutional-pattern semantics of Class I ("Nordic flexicurity is robust to routine perturbation") while honouring the structural-bias-adjusted threshold. It does NOT require re-running the Phase 2 scenario stack.

**Master-session decision required before publication.**

---

## 4. Squeeze-flag pattern-extension verdict

**Decision: keep BE/NL extension; document as orthogonal signal.**

| Squeeze-flag country | Phase 1 corridor | Phase 3 corridor | Shifted? |
|---|---|---|---|
| DK | 1 | 1 | No |
| FI | 1 | 1 | No |
| NO | 1 | 1 | No |
| SE | 1 | 1 | No |
| BE | 2 | 2 | No |
| DE | 2 | 2 | No |
| FR | 2 | 2 | No |
| NL | 2 | 2 | No |

All 8 squeeze-flagged countries stay in their Phase 1 corridor. Meanwhile, IT (squeeze=FALSE) shifts to C3 along with 12 other non-squeeze countries.

**Mechanism distinction:** Squeeze flag = high worker protection × adjacent-jurisdiction asymmetry × mode-1 capital-flow vulnerability. Mechanism re-routes risk via capital flight, not via displacement velocity. Structural-bias adjustment = weak-ALMP destination institutions failing to absorb post-1980-base-rate-corrected displacement velocity. The two patterns are mechanistically independent — confirmed by zero correlation between squeeze flag and Phase 3 corridor shift.

BE/NL extension is real pattern extension (high adjacency to UK weak-protection + significant cross-border capital flows) on the *same* mechanism as DE/FR/Nordics. It is not a methodology over-fit. Bundle D extension stands.

---

## 5. SE knife-edge under recalibration

Bundle H found SE was the knife-edge case in Phase 2 — Class I status held but barely (S4b drag composite was the binding constraint).

**Under Phase 3 with naive carryover:** SE (along with all Nordics) drops to Class II — *not* because of S4b knife-edge, but because of S4a-induced exit from C1-rescaled. The Bundle H knife-edge mechanism is now masked by the broader C1-collapse problem. Under recommended option (b) relative-stable Class I redefinition, SE returns to Class I; the original Bundle H knife-edge finding (SE = least-robust Nordic) re-emerges as a within-Class-I confidence band rather than a class-boundary issue.

**Status:** SE knife-edge survives recalibration *conditional* on the Class I redefinition adopted. If option (a) accept collapse is chosen, SE knife-edge becomes moot (no Class I exists). Recommend Bundle H finding be re-stated as a within-corridor-stress band measurement when option (b) is locked.

---

## 6. Corridor count verdict

**Locked: 3 corridors at 1.20 / 2.80** (named criterion: structural-bias adjustment per Phase 1 §3.1 + Autor 2024 + El-Sahli/Upward).

Population stats (mean ± std, range):
- C1: n=5, 1.05 ± 0.03, [1.00, 1.10] — tight Nordic cluster
- C2: n=16, 2.35 ± 0.40, [1.59, 2.77] — broad bifurcated-absorption mid
- C3: n=15, 2.94 ± 0.17, [2.81, 3.40] — tight band, with internal sub-structure (see below)

**C3 sub-corridor analysis (analytical-only, not promoted to 4th corridor):**

| Sub-band | Range | n | Institutional regime |
|---|---|---|---|
| C3-low (structural-bias-adjusted) | 2.81–2.96 | 13 | CEE + Southern weak-ALMP regimes |
| C3-high (Liberal Market) | 3.33–3.40 | 2 (IE, UK) | Liberal Market institutional regime |

A natural-gap analysis on the data shows breaks at 1.10→1.59 (Δ=0.49) and 2.96→3.33 (Δ=0.38), supporting a *data-driven* 3-corridor scheme at 1.20/3.00. The 2.80 floor is a *theory-driven* override per the structural-bias literature. Bundle J accepts the theory over the data on this point, but documents the alternative: 3 corridors at 1.20/3.00 (data-driven) or 4 corridors at 1.20/2.80/3.00 (institutional-regime split) are viable spec amendments. Master session decides.

---

## 7. Open questions for Bundle K + Bundle L

### 7.1 For Bundle K (Klinger ISCO coordination-share join)

1. **Will Klinger weighting move ratios across the new 2.80 floor?** Phase 2 used `ai_labour_load = clip(lens1_displacement_velocity, 0, 1)` as a Phase 3 placeholder (§2.3 methodology note). Klinger join shifts AI labour load by ±0.05–0.15 typically. Under Phase 3 recalibration, several countries sit within 0.05 of the C2/C3 boundary (ES 2.755, LV 2.766, BG 2.760). Klinger join could:
   - Push ES/LV/BG/RS into C3 if coordination-share is high (e.g., for Southern + Eastern European occupational mixes with admin-heavy structures)
   - Pull EE/CZ/HU/SI back into C2 if coordination-share is low (high-routine-execution profiles that Klinger weights down)
   - Bundle K should report which of the 11 close-boundary countries (4 close-from-below, 7 close-from-above within Phase 3 ±0.05 band) shift under the join.
2. **Does Klinger join surface a 4th corridor?** If Liberal Market countries (IE/UK) score on a different coordination-share profile from CEE/Southern (i.e., financialised vs admin-clerical), the 4-corridor recommendation strengthens. If they score similarly (which seems unlikely given UK financialisation), 3-corridor verdict strengthens.
3. **Sentinel re-test under Klinger join.** Master session should re-run PL sentinel after Klinger weighting — does PL stay in C3 once coordination-share is applied? If not, the structural-bias adjustment may need further calibration.

### 7.2 For Bundle L (scenario probability)

1. **Class III gain (2 → 15) reshapes scenario-realisation policy implications.** 13 new Class III countries means 13 countries whose recovery requires Scenario 1 or 2b realisation. Bundle L's scenario-probability layer must explicitly carry per-corridor probability distributions: P(S1 | C3-low) and P(S2b | C3-low) become decision-load-bearing for these 13 countries that were previously Class II.
2. **Post-growth regime × Phase 3 corridor interaction.** DE (post_growth_empirical) stays in C2-rescaled but its policy implication is: in a post-growth regime, Scenario 1 (Reinstatement Revival) is structurally weaker (locked spec line 92–106). For C3-rescaled countries that are also post-growth (IT secular_stagnation_warning, EL secular_stagnation_warning), Bundle L should compute joint probability of escape: P(S1 ∨ S2b | post_growth_regime ∩ C3-rescaled).
3. **Class I redefinition decision affects Bundle L baseline.** If Phase 3 adopts option (b) relative-stable Class I, Bundle L scenario-probability for "robust" countries operates on a different baseline than Phase 2 ran. Bundle L should treat Class I redefinition decision as a precursor lock.

### 7.3 Methodology questions deferred to master session

1. **Class I definition** (option a / b / c — see methodology §3.3).
2. **Final corridor count lock** (3 at 1.20/2.80 vs 3 at 1.20/3.00 vs 4 at 1.20/2.80/3.00).
3. **C3 sub-corridor formalisation** — analytical tag vs schema field.
4. **Sensitivity bands for boundary-adjacent countries** — recommendation: run ES/LV/BG/RS (within 0.05 below new C3 floor) with explicit confidence interval rather than point assignment.
5. **Phase 3 lock vs continued iteration** — Bundle K and Bundle L outputs may surface evidence to revise corridor thresholds again. Master-session governance question: is Bundle J the final structural-bias pass, or does the locked spec's "single re-scoring pass" allow one further calibration after Bundle K/L close?

---

## 8. Verification checklist (per Bundle J handover §Verification)

| # | Check | Result |
|---|---|---|
| 1 | PL (lens1_ratio 2.96) shifts to C3-rescaled | ✅ PASS — `phase3_corridor=3`, sentinel verdict locked |
| 2 | Nordic Class I status preserved or explicitly flagged | ✅ Flagged — all 5 Nordics drop to Class II under naive carryover; option (b) relative-stable redefinition recommended for restoration |
| 3 | IE + UK remain Class III (or shift to Class IV — surface either way) | ✅ Both remain Class III (corridor unchanged at 3; scen3=3 still triggers Class III) |
| 4 | Class IV count: still 3 (TR/RS/MK) | ✅ Confirmed — BA still Class II (poly 0.42 < 0.50; eea 0.583 < 0.60; gini 30.3 < 35) |
| 5 | Corridor count verdict has named criterion | ✅ 3 corridors at 1.20/2.80; criterion = structural-bias adjustment per Phase 1 §3.1 + Autor 2024 + El-Sahli/Upward + Coface/OEM 2026 |
| 6 | 36/36 countries reassigned; no nulls in phase3_corridor | ✅ Confirmed — all 36 rows have phase3_corridor ∈ {1, 2, 3}; CSV row count = 36 |

---

_End findings — see methodology in `layer-6-phase3-corridor-methodology.md`; data in `layer-6-phase3-corridor-rescaled.csv/.json`._
