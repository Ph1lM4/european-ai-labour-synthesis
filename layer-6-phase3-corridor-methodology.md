# Layer 6 Phase 3 — Structural-Bias Re-Calibration Methodology (Bundle J)

**Date:** 2026-04-29
**Scope:** 36 countries (EU-27 + NO + IS + LI + CH + UK + 4 candidates BA/MK/RS/TR)
**Source baselines:** `layer-6-phase1-scoring.csv/.json` (Lens 1 ratios), `layer-6-phase2-scoring.csv/.json` (scenario_ratios + Lens 4/5 inputs)
**Outputs:** `layer-6-phase3-corridor-rescaled.csv/.json`
**Phase 1 + Phase 2 source files NOT modified** (locked spec compliance).

---

## 1. Structural-bias adjustment — definition and anchors

Phase 1 findings §3.1 (lines 35–37) flagged that the locked corridor thresholds (C1<1.5, C3≥3.0) inherit a historical-base-rate calibration that **overstates the C1 width and understates the C3 width** under post-1980 reinstatement-effect conditions. Phase 2 carried the warning as a calibration note. Phase 3 (this bundle) applies the adjustment as a single re-scoring pass per Q5 spec lock (`layer-6-lens-framework.md` line 54).

### 1.1 Calibration anchors (BR-19 — anchored, not fabricated)

1. **Phase 1 sub-cluster boundary at 1.20** — Findings §3.1 sub-cluster table: Nordic cluster ends at 1.10 (SE); next cluster (Continental Corporatist FR/BE/NL/LU) starts at 1.59. The 0.49-unit gap between SE 1.10 and FR 1.59 is the largest natural break in the entire 36-country distribution. C1 cap at 1.20 sits inside this gap, captures only the Nordic flexicurity systems, and matches Phase 1 sanity check 3.2 (Nordic cluster 1.00–1.10 → C1 high confidence).
2. **Phase 1 sub-cluster boundary at 2.80** — Findings §3.1 explicitly named the 2.80+ band (PL 2.96, MT 2.91, EE 2.90, HR 2.89, CY 2.89, …) as "plausibly already in Corridor 3 territory under structural-bias adjustment." 13 countries fall into 2.808–2.955 by direct enumeration. C3 floor at 2.80 captures this Phase-1-flagged cluster as the operational realisation of the structural-bias warning.
3. **Autor, Chin, Salomons & Seegmiller (QJE 2024)** — reinstatement effect weakens post-1980; the historical "managed transition" base rate over-states institutional capacity to absorb displacement at any given velocity-to-absorption ratio. This argues for a tighter C1 cap than the 1.50 naive threshold supports. (Source: `disruption-analysis/SKILL.md` Takeaway 22 + handover line 35.)
4. **El-Sahli & Upward (BJIR 2017)** — UK dockworkers NDLS counterfactual: even structurally-managed decline produced lifetime-earnings deficits, supporting a lower C3 floor than the naive 3.0 threshold implies. (Source: `disruption-analysis/SKILL.md` source list.)
5. **Coface/OEM 2026 (Arquié/Duthoit/Subileau)** — `disruption-analysis/SKILL.md` Takeaway 27: 30% of tasks at risk = published anchor for "structural transformation, short of destruction" — the regime that begins around C3 floor below 3.0, distinct from Frey/Osborne 2017 destruction zone (>70%).

### 1.2 New thresholds (locked Phase 3, Bundle J)

| Corridor | Phase 1 (naive) | Phase 3 (re-calibrated) | Mechanism |
|---|---|---|---|
| C1 — Managed Transition | ratio < 1.50 | **ratio < 1.20** | Absorption capacity matches/exceeds displacement |
| C2 — Bifurcated Absorption | 1.50 ≤ ratio < 3.00 | **1.20 ≤ ratio < 2.80** | Displacement exceeds absorption; middle-skill bifurcation softens aggregate impact |
| C3 — Displacement Without Absorption | ratio ≥ 3.00 | **ratio ≥ 2.80** | Velocity overruns reskilling pathway structurally |

**Why theory beats data here.** No natural gap exists in the data at 2.80 (the 2.766 LV → 2.808 CZ transition is +0.042, much smaller than the 1.10→1.59 and 2.96→3.33 natural breaks). The 2.80 floor is **theory-driven** — anchored on Autor 2024 reinstatement-weakness + El-Sahli/Upward counterfactual + Phase 1 sub-cluster-boundary observation. The structural-bias argument explicitly predicts the data will *not* show a natural gap at the corrected threshold: pre-1980-base-rate calibration smears countries that *should* already be in C3 into the upper C2 band. Bundle J accepts this as a feature, not a bug, and surfaces the data-driven alternative below.

---

## 2. PL sentinel test — outcome

| Metric | Value |
|---|---|
| Country | PL (Poland) |
| `lens1_ratio` | 2.955 |
| Phase 1 corridor | 2 |
| Phase 3 (re-calibrated) corridor | **3** |
| Corridor shift | C2 → C3 |
| Phase 1 fragility class | II |
| Phase 3 fragility class | III |
| Sentinel verdict | **PASS** — methodology re-locked |

PL sits 5.5 percentage points above the new C3 floor; the test is unambiguous.

---

## 3. Re-evaluation of Phase 2 fragility classes under new corridors

### 3.1 Methodology

Class precedence carried forward from Phase 2 methodology §4 (locked): **IV → III → I → II**.

- **Class IV (Active Cascade)** — criterion *unchanged*. Inputs (polycrisis, demographic load, AI load, EEA vulnerability, Gini) come from Lens 4/5 and are not affected by Lens 1 corridor re-calibration. Full-data triggers (poly>0.80 AND demo>0.80 AND ai>0.70) remain unmet for any country. Candidate-relaxed criterion (BA/MK/RS/TR + poly≥0.50 OR eea_vuln≥0.60 OR gini≥35) is unchanged.
- **Class III (Pre-Failure Risk)** — `corridor_under_scenario_3 == 3` re-evaluated using Phase 3 thresholds applied to Phase 2 `scenario_ratios`. A country whose ratio under Muddle Through (S3) is ≥2.80 now triggers Class III.
- **Class I (Robust)** — `distinct_corridors_routine_s1_s4b == 1` re-evaluated under Phase 3 thresholds.
- **Class II (Fragile)** — default.

### 3.2 Computational note

Phase 2 stored each country's `scenario_ratios` (raw velocity/absorption ratios per scenario, before threshold mapping). Phase 3 re-maps those ratios under the new thresholds without re-running the velocity/absorption perturbation engine. This keeps the structural-bias pass as a pure threshold change — no change to drag calibration, scenario multipliers, or absorption haircuts.

### 3.3 Class I collapse — load-bearing surfaced finding

**Under naive carryover, all 5 Phase 2 Class I countries (DK, FI, IS, NO, SE) drop to Class II.** This is structural and analogous to the Phase 2 S5-collapse problem.

Mechanism: under the tightened C1 cap (1.20), a Nordic baseline ratio of ~1.05 plus any scenario that increases velocity by >14% (S4a applies ×1.20) pushes the country into rescaled C2. The Phase 2 S4b drag calibration (`drag_mult=0.15`) was tuned against the *old* 1.50 C1 cap — it preserved Nordic Class I status by keeping S4b ratios under 1.5. Under the new 1.20 cap, S4b Nordic ratios land ~1.40 → C2-rescaled, breaking corridor stability.

This is methodologically symmetric to the Phase 2 S5 problem: a stricter mapping makes "stable" empirically un-achievable for any data point. Phase 2 resolved S5 by amending Class I to S1–S4b; Phase 3 cannot use the same pattern (Class I collapse spans S1–S4b inclusive, not just S5).

**Three resolution options surfaced for master-session decision:**

| Option | Definition | Implication |
|---|---|---|
| (a) Accept collapse | Class I = empty under recalibration | Names a structural truth: under structural-bias adjustment, *no European country is fully robust* to routine perturbation. Defensible analytically; politically uncomfortable. |
| (b) Re-define Class I as relative-stable | Class I = `phase3_corridor` retained under all S1–S4b (no shift across the recalibrated boundaries the country sits inside) | Re-introduces 5 Nordic Class I but loses absolute-corridor semantics. Requires per-country baseline-corridor reference. |
| (c) Re-tune S4b drag_mult | Lower `drag_mult` so Nordic S4b ratio stays <1.20 (would need ~0.05 vs current 0.15) | Re-runs Phase 2 with new calibration. Out of Bundle J scope; Phase 2 outputs are locked. |

**Bundle J recommendation:** option (b) — relative-stable. Reason: "Class I = robust" is an institutional-pattern claim, not an absolute-ratio claim. Under the re-calibrated thresholds, "robust" means "Phase 2-stable scenario corridor envelope" rather than "fixed at C1 across scenarios." This preserves the Nordic flexicurity finding (DK/FI/IS/NO/SE remain in C1 under S3 Muddle Through and shift only to C2 under stress, never to C3) while honouring the structural-bias adjustment to the threshold itself.

The CSV/JSON output ships the **naive carryover** (option a). Master-session adjudicates whether to re-derive under (b) or (c) before publication.

### 3.4 Class IV unchanged

3 candidates remain Class IV (TR/RS/MK) under Phase 3 — Lens 4/5 inputs unaffected. BA remains Class II (poly 0.42, eea 0.583, gini 30.3 — all under candidate triggers). Phase 2 §4.4 BA finding survives Phase 3 unchanged.

### 3.5 Class III gain

13 countries gain Class III (Pre-Failure Risk) under Phase 3 because their Muddle Through ratio (= Phase 1 baseline ratio) is now ≥2.80: CY, CZ, EE, EL, HR, HU, IT, LT, MT, PL, PT, SI, SK. IE + UK retain Class III (Phase 2 baseline, ratios well above new floor).

---

## 4. Corridor count verdict — 3 corridors at 1.20 / 2.80

### 4.1 Population statistics under recalibration

| Corridor | n | Mean ratio | Std | Range |
|---|---|---|---|---|
| C1 — Managed Transition | 5 | 1.047 | 0.033 | 1.004 – 1.101 |
| C2 — Bifurcated Absorption | 16 | 2.346 | 0.395 | 1.592 – 2.766 |
| C3 — Displacement Without Absorption | 15 | 2.937 | 0.172 | 2.808 – 3.397 |

Total 36/36. Triadic balance (5/16/15) replaces Phase 1's bimodal-with-large-middle (5/29/2).

### 4.2 Sub-corridor analysis within C3

C3 splits into two qualitatively distinct sub-clusters:

| Sub-band | Range | n | Countries | Institutional regime |
|---|---|---|---|---|
| **C3 low** (structural-bias-adjusted) | 2.808 – 2.955 | 13 | CZ, HU, SI, EL, IT, LT, HR, SK, CY, EE, PT, MT, PL | CEE + Southern European weak-ALMP regimes brought into C3 by structural-bias adjustment |
| **C3 high** (Liberal Market) | 3.330 – 3.397 | 2 | IE, UK | Liberal Market institutional regime — no demographic-buffer infrastructure; Phase 2 Class III Pre-Failure Risk |

**Natural-gap evidence in the data** (sorted ratio differentials):
- 1.10 (SE) → 1.59 (FR): **Δ = 0.491** — major break, supports C1 cap near 1.20
- 2.96 (PL) → 3.33 (IE): **Δ = 0.375** — major break, supports a separator at 3.00
- 2.766 (LV) → 2.808 (CZ): Δ = 0.042 — *no* natural break at 2.80

This means the data alone supports a 3-corridor scheme **at 1.20 / 3.00** (preserving the naive C3 floor for Liberal Market only). The 2.80 floor is a *theory-driven* override.

### 4.3 Verdict

**Recommendation: 3 corridors at 1.20 / 2.80 (current Bundle J output).** Reasoning:

1. **The structural-bias adjustment is the load-bearing reason this re-calibration exists.** Holding 3.00 to honour data-driven gaps would defeat the bundle's purpose: the entire pre-Phase-3 argument was that the data is contaminated by historical-base-rate over-calibration; the absence of a natural gap at the corrected threshold is *expected*, not falsifying.
2. **Sub-corridor sub-structure is documented but not promoted to a 4th corridor.** A C3-low / C3-high tag is a within-corridor analytical sub-axis (institutional-regime classifier), not a separate corridor. Promoting the split to a 4th corridor would require a *decision-relevant difference* that the current scenario stack does not capture: under Phase 2 Muddle Through (S3), both sub-bands map to C3 with similar implications. The institutional difference between Liberal Market and weak-ALMP CEE/Southern matters at the *recovery-pathway* layer (S1 / S2b realisation), not the corridor-assignment layer.
3. **Master-session reversal pathway is open.** The locked spec (line 40) said "3 corridors target after consolidation; validation runs against L1–L5 data." Phase 3 has discretion to reverse. Bundle J does not exercise that discretion but documents the alternative for master-session adjudication.

**Alternatives surfaced (not locked):**
- **3 corridors at 1.20 / 3.00** — data-driven; preserves naive C3 = Liberal Market only; structural-bias adjustment becomes a within-C2 sub-tag rather than a corridor shift.
- **4 corridors at 1.20 / 2.80 / 3.00** — splits C3 into "Structural-bias-adjusted displacement risk" (n=13) vs "Liberal Market structural displacement" (n=2). Defensible if the institutional-regime distinction proves load-bearing for Phase 3 fragility classes or Layer 7 prescriptions; current scenario stack does not surface it as decision-relevant.

---

## 5. Squeeze-flag pattern-extension audit

Phase 2 (Bundle D) extended `lens4_jurisdictional_buffering_squeeze_flag = TRUE` beyond spec-named DE/FR/Nordics to include BE and NL. Master session flagged: real pattern extension or methodology over-fit?

### 5.1 Post-recalibration alignment

| Country | Phase 1 corr | Phase 3 corr | Shift | Squeeze flag | Alignment |
|---|---|---|---|---|---|
| DK | 1 | 1 | 0 | TRUE | squeeze_flag_orthogonal |
| FI | 1 | 1 | 0 | TRUE | squeeze_flag_orthogonal |
| NO | 1 | 1 | 0 | TRUE | squeeze_flag_orthogonal |
| SE | 1 | 1 | 0 | TRUE | squeeze_flag_orthogonal |
| BE | 2 | 2 | 0 | TRUE | squeeze_flag_orthogonal |
| DE | 2 | 2 | 0 | TRUE | squeeze_flag_orthogonal |
| FR | 2 | 2 | 0 | TRUE | squeeze_flag_orthogonal |
| NL | 2 | 2 | 0 | TRUE | squeeze_flag_orthogonal |

### 5.2 Verdict

**Squeeze flag captures something different — keep BE/NL extension; document as orthogonal signal.**

Per Bundle J handover Task 5 second clause: "If BE/NL stay in C2-rescaled while PL/IT shift to C3, squeeze flag captures something different (jurisdictional buffering specifically, not displacement velocity) → keep extension but document as orthogonal signal."

Both BE and NL stay in C2-rescaled. Meanwhile, IT (squeeze=FALSE) shifts C2→C3 along with 12 other countries. The squeeze flag identifies countries with *high worker protection + adjacent-jurisdiction asymmetry exposure + mode-1 vulnerability* — a buffering-mechanism signal that re-routes risk through capital-flow channels, not through displacement velocity. BE/NL extension has the same institutional mechanism as DE/FR/Nordics (high adjacency to UK weak-protection + significant cross-border capital flows). The structural-bias finding operates on *displacement-velocity* mechanics (weak ALMP at the destination), and the two patterns are mechanistically independent.

**Status:** BE/NL extension retained. `lens4_jurisdictional_buffering_squeeze_flag` is documented as an orthogonal-to-displacement-corridor signal in the methodology hierarchy. Annotation-only semantics (Phase 2 §1.3 reconciliation) preserved.

---

## 6. Constraints honoured

- **BR-19 (no fabrication):** Calibration anchors are all named primary sources (Phase 1 §3.1 sub-cluster table; Autor 2024 QJE; El-Sahli/Upward 2017 BJIR; Coface/OEM 2026). The 2.80 floor is *theory-driven*, not data-fitted; this is surfaced explicitly in §1.2.
- **BR-21 (per-country provenance):** Each country row carries `lens1_ratio` (Phase 1 source), `phase1_corridor`, `phase3_corridor`, `corridor_shift`, all 7 scenario corridors under recalibration, fragility class change, and squeeze-flag alignment. `class_iv_reason_new` records the trigger predicate for any candidate Class IV.
- **No modification of locked spec or Phase 1/2 outputs.** Phase 3 outputs are written to new files. Phase 2 `scenario_ratios` are read-only inputs; Phase 2 corridor labels (`corridor_under_scenario_*`) are not overwritten.
- **Phil does all git commits.** No git operations performed.

---

## 7. Open methodology questions deferred to master session

1. **Class I definition under Phase 3 thresholds** — adopt option (b) relative-stable, option (a) accept collapse, or re-tune S4b drag (option c)?
2. **Corridor count final lock** — confirm 3 at 1.20/2.80, or revise to 3 at 1.20/3.00 or 4 at 1.20/2.80/3.00?
3. **Phase 2 re-write requirement** — if option (c) is chosen for Class I, Phase 2 scenario stack must be re-run with new drag calibration. If option (b) is chosen, Phase 2 outputs survive unchanged with Phase 3 fragility-class amendments.
4. **C3 sub-corridor formalisation** — promote C3 low/high split to a within-corridor tag in the schema, or hold as analytical-only documentation?

---

_End methodology — outputs in `layer-6-phase3-corridor-rescaled.csv/.json`; findings in `layer-6-phase3-corridor-findings.md`._
