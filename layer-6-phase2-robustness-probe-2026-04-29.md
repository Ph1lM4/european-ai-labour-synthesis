# Layer 6 Phase 2 — S4b/S5 Drag-Multiplier Robustness Probe

**Date:** 2026-04-29
**Scope:** Bundle H bounded probe. Re-runs Bundle D scoring engine across a 3×3 multiplier grid (S4b ∈ {0.10, 0.15, 0.20} × S5 ∈ {0.20, 0.30, 0.40}). Reports Nordic Class I stability, class-distribution shifts, and spillover effects. **No Phase 2 file modified.**
**Engine reconstruction:** Baseline grid point (S4b=0.15, S5=0.30) reproduces Bundle D exactly — 5/26/2/3 distribution; Nordics = Class I; IE/UK = Class III; MK/RS/TR = Class IV; BA = Class II. **0 mismatches across 36 countries.** Engine validated.

---

## VERDICT: **MIXED** — recommend per-country Class I confidence flag

- **4 of 5 Nordics (DK, FI, IS, NO)** hold Class I across **all 9 grid points** → load-bearing.
- **SE is knife-edge:** holds Class I at 6/9 grid points; drops to Class II whenever S4b ≥ 0.20 (independent of S5).
- **S5 multiplier is non-load-bearing for class assignment** under the amended Class I definition (S5 excluded from routine-stability check). The 9-grid collapses to 3 effective rows for Class I; S5 only moves cascade_corridor.
- **No other country flips class anywhere in the 3×3 grid.** Class III (IE, UK), Class IV (MK, RS, TR), and Class II (26 countries) are fully robust to drag calibration in this range.

**One-line Phase 3 recommendation:** Lock S4b=0.15 with documented ±33% boundary; flag SE with per-country knife-edge note (loses Class I at S4b≥0.20); S5 calibration irrelevant for class assignment, retain only as cascade_corridor input.

---

## 1. Nordic Class I Stability Matrix

|              | S5=0.20            | S5=0.30 (baseline) | S5=0.40            |
|--------------|--------------------|--------------------|--------------------|
| **S4b=0.10** | DK, FI, IS, NO, SE | DK, FI, IS, NO, SE | DK, FI, IS, NO, SE |
| **S4b=0.15** | DK, FI, IS, NO, SE | **DK, FI, IS, NO, SE** (Bundle D) | DK, FI, IS, NO, SE |
| **S4b=0.20** | DK, FI, IS, NO     | DK, FI, IS, NO     | DK, FI, IS, NO     |

### Per-country stability counts

| Country | Class I holds at | Knife-edge flag | Worst (s4b, s5) where still Class I |
|---------|------------------|-----------------|-------------------------------------|
| DK      | 9/9              | FALSE           | (0.20, 0.40)                        |
| FI      | 9/9              | FALSE           | (0.20, 0.40)                        |
| IS      | 9/9              | FALSE           | (0.20, 0.40)                        |
| NO      | 9/9              | FALSE           | (0.20, 0.40)                        |
| **SE**  | **6/9**          | **TRUE**        | (0.15, 0.40) — drops at S4b=0.20    |

SE knife-edge mechanism: SE has the highest lens1_ratio among Nordics (1.101) and a near-Nordic-median composite_drag (0.501). At S4b=0.20, the perturbed S4b ratio = 1.101 × 1.0 × (1 + 0.20 × 0.501) / 0.8 = 1.514, just over the C1/C2 boundary at 1.5. DK (1.049 × ... = 1.443) and FI (1.004 × ... = 1.382) and NO (1.057 × ... = 1.452) and IS (1.025 × ... = 1.388) all stay below 1.5 even at S4b=0.20.

**This matches the sensitivity audit pre-recorded in `layer-6-phase2-methodology-notes.md` §7:** *"S4b drag_mult = 0.15 — At 0.20: SE drops out of Class I; at 0.25: all Nordics drop. Highly sensitive — Class I count is brittle to drag calibration."* The probe confirms the audit's call empirically.

---

## 2. Class Distribution Shift Table

| Grid point          | I  | II | III | IV | Δ vs baseline |
|---------------------|----|----|-----|----|--------------|
| S4b=0.10, S5=0.20   | 5  | 26 | 2   | 3  | 0            |
| S4b=0.10, S5=0.30   | 5  | 26 | 2   | 3  | 0            |
| S4b=0.10, S5=0.40   | 5  | 26 | 2   | 3  | 0            |
| S4b=0.15, S5=0.20   | 5  | 26 | 2   | 3  | 0            |
| **S4b=0.15, S5=0.30 (baseline)** | **5** | **26** | **2** | **3** | — |
| S4b=0.15, S5=0.40   | 5  | 26 | 2   | 3  | 0            |
| S4b=0.20, S5=0.20   | 4  | 27 | 2   | 3  | 2            |
| S4b=0.20, S5=0.30   | 4  | 27 | 2   | 3  | 2            |
| S4b=0.20, S5=0.40   | 4  | 27 | 2   | 3  | 2            |

**Largest deviation:** any of the three S4b=0.20 points; total class-count delta = 2 (one country shifts I→II). The deviation is wholly accounted for by SE.

**Key observation:** S5 multiplier produces **zero** class-distribution change across any (s4b, s5) pair. This is by construction under the amended Class I definition — S5 corridor is not part of the routine-stability check and Class III is determined by S3 (drag-free).

---

## 3. Spillover Findings

Beyond Nordics, **no country flips class anywhere in the grid.** All squeeze-flag-TRUE countries other than the Nordics (BE, DE, FR, NL) hold Class II across all 9 grid points. Their per-scenario corridors do shift (e.g., DE moves from S4b=C2 at low multipliers to S4b=C3 at higher multipliers), but the routine-stability count remains ≥2 distinct corridors regardless, keeping them in Class II throughout.

**Trajectories of the squeeze-flagged set (BE, DE, DK, FI, FR, NL, NO, SE):**

| Country | Trajectory across 9 grid points |
|---------|----------------------------------|
| DK      | I at 9/9                          |
| FI      | I at 9/9                          |
| NO      | I at 9/9                          |
| SE      | I at 6/9; II at 3/9 (all S4b=0.20)|
| BE      | II at 9/9                         |
| DE      | II at 9/9                         |
| FR      | II at 9/9                         |
| NL      | II at 9/9                         |

The Lens-4 squeeze flag (capital-flight asymmetry) does not interact with S4b drag calibration to produce additional spillover. The squeeze-flag set is corridor-stable in class outcome across the tested range.

---

## 4. Cascade Corridor (S5) — orthogonal to Class I

Cascade corridor for all 5 Nordics is uniformly **C2 across all 9 grid points.** Even at the most extreme tested calibration (S4b=0.20, S5=0.40), no Nordic reaches C3 under cascade — and even at the least extreme (S4b=0.10, S5=0.20), no Nordic stays at C1 under cascade. The Nordic cascade behaviour is robust to S5 multiplier in this ±33% range.

This means:
- The methodology-notes claim that *"S5 universally degrades corridors for all but trivially-positioned cases"* (line 162) holds across the tested S5 range.
- The structural finding that Nordic ratios under S5 sit roughly in the middle of C2 (not borderline C1 or borderline C3) is calibration-independent — it is a property of the underlying baseline ratios (≈1.0–1.1) combined with absorption-halving.
- Phase 3 retest of cascade-corridor stability under the alternative absorption-haircut interpretation (Interp A) is still warranted for separate reasons (the velocity-vs-absorption split affects which mechanism is empirically validated), but **the direction of the cascade verdict for Nordics — uniform C2 — is not at risk from S5 multiplier choice in the tested band.**

---

## 5. Methodology Ambiguity Surfaced During Engine Reconstruction

**Resolved (no blocker):** Per `layer-6-phase2-methodology-notes.md` §3, the per-scenario ratio is computed as `velocity_new = lens1_ratio × velocity_mult × (1 + drag_mult × composite_drag)`, divided by `absorption_new`. The `lens4_corridor_modifier` (a `+1` flag for squeeze-flagged countries) is documented as a Phase-1-corridor adjustment but does **not** appear to be folded into the per-scenario corridor calculation in the locked scoring JSON. Engine reproduction confirmed: e.g., DK has `lens4_corridor_modifier = +1` and `lens4_jurisdictional_buffering_squeeze_flag = TRUE`, but `corridor_under_scenario_3 = 1` — i.e., the modifier is recorded as a flag for downstream interpretation but does not shift per-scenario corridors. The probe replicates this behaviour, and baseline reproduction is exact. **No methodology guess was required.**

This is worth flagging to the master session as a **documentation-vs-implementation observation** (not a probe blocker): methodology-notes §1.3 describes the `lens4_corridor_modifier` as a corridor-shifting input ("squeeze pushes C1 Nordics → C2"), but the locked Phase 2 scoring engine appears to treat it as an annotation. If the intended behaviour was for the squeeze flag to push DK/FI/SE Phase 1 corridor from C1→C2, then DK/FI/SE would not be eligible for Class I in the first place (their S3 corridor would be 2 not 1). The Nordic Class I result is contingent on the modifier being recorded but not applied to per-scenario corridors. Phase 3 should reconcile this if it represents a spec-vs-implementation drift.

---

## 6. Recommendation Summary

1. **Lock S4b=0.15** with the documented ±33% boundary (0.10–0.20). Within this band, 4 of 5 Nordics are robust; SE is knife-edge at the upper bound only.
2. **Flag SE specifically** with a per-country Class I knife-edge note: *"SE Class I holds at S4b≤0.15; drops to Class II at S4b=0.20."* This converts a brittleness from hidden to visible.
3. **De-emphasise S5 multiplier sensitivity for class assignment.** Under the amended Class I definition, S5 multiplier has zero effect on class outcomes for any of 36 countries in the tested band. S5 calibration matters only for cascade_corridor magnitude — and even there, all Nordics are uniformly C2.
4. **Retain Phase 3 task: Interp A vs Interp B test.** The probe does not address the velocity-amplification (Interp B) vs absorption-haircut (Interp A) split — that is a separate sensitivity question. Phase 3 should still execute it.
5. **Reconcile lens4_corridor_modifier semantics in Phase 3** (per §5 above): is it a corridor-shifting input or an annotation? If the former, baseline Nordic Class I would not survive — which would be a much larger finding than this probe is scoped to address.

---

## Files

- `layer-6-phase2-robustness-probe-2026-04-29.md` (this file)
- `layer-6-phase2-robustness-probe-2026-04-29.csv` — 9 rows × 41 columns: multiplier-pair label + per-country class for all 36 countries + nordic_class_I_count + per-class totals

No locked file modified.
