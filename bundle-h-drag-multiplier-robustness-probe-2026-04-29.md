# Handover Prompt — Bundle H: S4b/S5 Drag-Multiplier Robustness Probe (2026-04-29)

Bounded probe to verify whether Bundle D's Nordic Class I result is robust to the calibration of the velocity-amplification drag multipliers, or whether it sits at a knife-edge that fell out of the calibration loop. Should take ~30–45 minutes.

---

## START PROMPT

I need you to run a focused robustness probe on the Bundle D (Phase 2 scoring) S4b/S5 velocity-amplification drag multipliers. Bundle D set them at S4b = 0.15 and S5 = 0.30 (Interpretation B, velocity-amplification rather than absorption-haircut), explicitly calibrated so the Nordic Class I expectation holds. The master session flagged this as calibration-to-sanity-test smell and wants to know whether the result is load-bearing across a multiplier range, or knife-edge.

This is not a re-scoring session. It re-runs the existing scoring engine with a multiplier sweep and reports class-stability. Do NOT modify any locked spec, methodology notes, or findings files.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-scoring.json` — current Phase 2 scoring (baseline result at S4b=0.15, S5=0.30)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-methodology-notes.md` — Bundle D methodology, including drag-multiplier definitions and the Nordic Class I calibration justification
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-data.json` — Phase 2 input data (do NOT modify)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase1-scoring.json` — Phase 1 baseline corridors

### Goal

Re-run Phase 2 fragility class assignment across a 3×3 multiplier grid and report Nordic Class I stability + class-distribution shifts. Class I uses the **amended definition** (master session 2026-04-29 lock): stable across S1, S2a, S2b, S3, S4a, S4b only — S5 cascade reported separately as `cascade_corridor`, orthogonal to Class I.

### Multiplier sweep

| S4b multiplier | S5 multiplier | Label |
|---|---|---|
| 0.10 | 0.20 | low-low |
| 0.10 | 0.30 | low-mid |
| 0.10 | 0.40 | low-high |
| 0.15 | 0.20 | mid-low |
| 0.15 | 0.30 | **baseline (Bundle D)** |
| 0.15 | 0.40 | mid-high |
| 0.20 | 0.20 | high-low |
| 0.20 | 0.30 | high-mid |
| 0.20 | 0.40 | high-high |

S4b range = ±33% of baseline (0.10–0.20). S5 range = ±33% of baseline (0.20–0.40). 9 grid points total.

### Method

1. Reconstruct the Bundle D scoring engine from `layer-6-phase2-methodology-notes.md`. The engine should:
   - Apply S4b drag as velocity amplification × multiplier (Interp B per Bundle D lock)
   - Recompute lens1_ratio under perturbation
   - Reassign corridor under each scenario
   - Reassign Class I/II/III/IV per the amended definition
2. Run the engine 9 times across the grid.
3. For each grid point, record the full class assignment for all 36 countries.

### Required outputs (in order of priority)

1. **Nordic Class I stability matrix (the load-bearing question):**

   ```
                S5=0.20  S5=0.30  S5=0.40
   S4b=0.10:    [DK,FI,...]  [...]    [...]
   S4b=0.15:    [...]    [DK,FI,IS,NO,SE]  [...]
   S4b=0.20:    [...]    [...]    [...]
   ```

   For each of the 5 Nordics (DK, FI, IS, NO, SE), report which of the 9 grid points the country holds Class I. Compute:
   - **Stability count per country** (out of 9 grid points)
   - **Knife-edge flag** = TRUE if country holds Class I at baseline but drops out at any of the 8 adjacent points; FALSE if stable across all 9
   - **Worst-multiplier-pair-where-still-Class-I** per country

2. **Class distribution shift table** — at each grid point, report the count {I: n, II: n, III: n, IV: n}. Surface the largest deviation from the Bundle D baseline.

3. **Spillover findings** — beyond Nordics, which countries flip class anywhere in the grid? Report each country's class trajectory (e.g., "AT: II at baseline, II at 7/9, III at 2 high-multiplier points"). Focus on the squeeze-flag-TRUE countries (BE, DE, DK, FI, FR, NL, NO, SE) since they're the most-perturbed by Lens 4 changes.

4. **Verdict on Decision 4** — one of three:
   - **LOAD-BEARING**: Nordic Class I holds across all 9 grid points. Calibration was conservative; result is robust. Recommend lock.
   - **KNIFE-EDGE**: Nordic Class I holds only at baseline or 1–2 adjacent points; falls apart elsewhere. Recommend: surface as known fragility in Phase 3; consider absorption-haircut Interpretation A as alternative.
   - **MIXED**: Some Nordics stable, others knife-edge. Recommend per-country Class I confidence flag.

### Constraints

- Do NOT modify any of: layer-6-lens-framework.md, layer-6-phase2-scoring.csv/.json, layer-6-phase2-methodology-notes.md, layer-6-phase2-findings.md, layer-6-phase2-data.json
- Do NOT re-run any data-acquisition or re-fetch sources
- Do NOT recommend Phase 3 changes beyond what the verdict already implies
- Output goes to a NEW file: `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-robustness-probe-2026-04-29.md` — keep it under 250 lines
- Optionally output raw grid data as `layer-6-phase2-robustness-probe-2026-04-29.csv` (9 rows × 36+1 columns: multiplier-pair-label + per-country class) for inspection
- BR-19: no fabrication. If the engine reconstruction surfaces an ambiguity in methodology-notes (e.g., does drag apply pre- or post-Lens-4-modifier?), flag it and stop — do NOT guess.

### Verification

- Baseline grid point (S4b=0.15, S5=0.30) must reproduce Bundle D exactly (5/26/2/3 distribution; Nordics = Class I; IE/UK = Class III; MK/RS/TR = Class IV; BA = Class II).
- If baseline reproduction fails, the engine reconstruction is wrong — report and stop, do NOT ship the sweep.

### When done — report back to master session with

1. Verdict (LOAD-BEARING / KNIFE-EDGE / MIXED)
2. The 5×9 Nordic stability matrix
3. Largest class-distribution deviation from baseline + which grid point produces it
4. Any methodology ambiguity surfaced during engine reconstruction
5. One-line recommendation for Phase 3 (lock the calibration, sensitivity-flag, or interpret-A retest)

## END PROMPT
