# Handover Prompt — Bundle J: Structural-Bias Re-Calibration + Corridor Count Validation (Phase 3 Priority 1)

Self-contained prompt for a fresh session. Applies the structural-bias adjustment that Phase 1 + 2 deferred to Phase 3, with PL as sentinel test. Re-validates whether 3 corridors is the right count or whether the re-calibrated data warrants 2 or 4. Independent of Bundle K (can run in parallel).

---

## START PROMPT

I need you to execute Phase 3 priority 1: apply the structural-bias re-calibration to Lens 1 corridor thresholds and re-validate the 3-corridor decision against the re-calibrated data. This is the work the Phase 1 findings flagged for Phase 3 (lines 35–37: "10 countries with ratio ≥ 2.80 are plausibly already in Corridor 3 territory").

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — locked spec; section "Structural-bias re-calibration (Q5 lock)" line 54: "Apply once in Phase 3, after Lens 4 + Lens 5 + scenario stack outputs exist. Phase 2 keeps the warning as a calibration note only. Single re-scoring pass avoids compounding adjustments. PL at 2.96 is the sentinel test case — must shift to C3 under re-calibration or methodology is wrong."
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase1-scoring.csv` + `.json` — Phase 1 corridor assignments (36 countries)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase1-findings.md` §3 + §3.1 — sub-cluster table on lines 27–35; structural-bias note on lines 35–37
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-scoring.csv` + `.json` — Phase 2 fragility classes + scenario corridors (you'll re-evaluate these under new corridor boundaries)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase1-methodology-notes.md` — original Lens 1 corridor threshold definitions

Do NOT modify the locked spec, Phase 1 outputs, or Phase 2 outputs. Bundle J produces its own Phase 3 output files.

### Task 1 — Calibrate the structural-bias adjustment

The Phase 1 finding (line 35–37) was that historical-base-rate calibration **overstates** the C1 width and **understates** C3 width. The current thresholds are:
- C1: ratio < 1.5 (Managed Transition)
- C2: 1.5 ≤ ratio < 3.0 (Bifurcated Absorption)
- C3: ratio ≥ 3.0 (Displacement Without Absorption)

The structural-bias adjustment must:
1. **Tighten C1** (narrower window — fewer countries qualify as "managed")
2. **Widen C3** (broader window — more countries fall into displacement-without-absorption)
3. Be principled, not arbitrary

Recommended approach (sanity-check before locking):
- Read `disruption-analysis/SKILL.md` (in second-brain `skills/`) v0.5.x for the structural-bias framing if needed for context
- Calibrate against the Autor 2024 reinstatement-weakness finding + El-Sahli/Upward counterfactual (these are the named Phase 1 anchors)
- Propose new thresholds, e.g.:
  - C1 cap → 1.20 (was 1.50) — only Nordics + Iceland survive as truly managed
  - C3 floor → 2.80 (was 3.00) — captures the 10 Phase 1 sub-cluster countries flagged as boundary cases
- Document the calibration anchor: WHY 2.80 and 1.20 specifically? If the answer is "matches the Phase 1 sub-cluster boundary," that's defensible — surface it.

### Task 2 — Apply to all 36 countries + run sentinel test

For each country:
1. Read `lens1_ratio` from Phase 1 scoring
2. Apply new C1/C2/C3 thresholds
3. Record old corridor, new corridor, shift direction
4. **Sentinel test:** PL (ratio 2.96) MUST shift C2 → C3. If PL stays in C2, the threshold is wrong — adjust C3 floor downward and re-run.

Spot-check expected shifts:
- DE (ratio 2.41): likely stays C2
- IT (2.84): likely shifts C2 → C3
- ES (2.75): likely stays C2 (just below new C3 floor)
- FR (1.59): likely shifts C2 → C2 still, or could drop to C1 boundary
- LU/BE (~1.59-1.91 sub-cluster): test sensitivity — under tighter C1, do they stay C2?

### Task 3 — Re-evaluate Phase 2 fragility classes under new corridors

Phase 2 fragility class assignment used Phase 1 corridors as baseline. With new corridor boundaries, some Class assignments will change. Re-run the Class I/II/III/IV logic from `layer-6-phase2-methodology-notes.md` (using the **amended** Class I = stable across S1, S2a, S2b, S3, S4a, S4b — six routine-perturbation variants) but with the new corridor mapping.

Track:
- Countries that change class (e.g., a country in C3-rescaled now satisfies Class III under Muddle Through where it didn't before)
- Class distribution: was 5/26/2/3 — what's the new distribution?
- Whether SE knife-edge (Bundle H finding) changes under new corridors

### Task 4 — Validate corridor count: 3, 2, or 4?

After re-calibration, ask:
1. **Are the 3 corridors well-separated?** Compute population stats per corridor (mean ratio, std, min, max).
2. **Does any corridor have natural sub-structure?** If C3-rescaled splits cleanly into "displacement, recoverable" (e.g., 2.80–3.20) vs "displacement, structural" (>3.20), that's a 4-corridor case.
3. **Could C1 + C2 collapse?** Under tight C1, if only Nordics + IS qualify, it might be that "managed transition" is really an outlier category, and the data wants 2 corridors: managed-outlier vs everything else. Test against the Lens 4/5 readings — do C1 and C2 countries differ in compound-shock profiles or only in absorption rate?

Recommend one of:
- **3 corridors locked** (current spec — Phase 1 + 2 + 3 alignment)
- **2 corridors recommended** (with rationale; spec amendment needed)
- **4 corridors recommended** (with split criterion + rationale)

This is the sub-bundle's load-bearing decision. The spec said "3 corridors target after consolidation"; Phase 3 has discretion to reverse only with strong evidence.

### Task 5 — Squeeze-flag pattern-extension audit

Bundle D extended squeeze-flag firing beyond spec-named DE/FR/Nordics to include BE/NL. Master session flagged this as "real pattern extension or methodology over-fit?" Under re-calibration:
- If BE/NL shift to C3-rescaled along with PL/IT/etc., the squeeze flag's signal correlates with the structural-bias finding → validates extension
- If BE/NL stay in C2-rescaled while PL/IT shift to C3, squeeze flag captures something different (jurisdictional buffering specifically, not displacement velocity) → keep extension but document as orthogonal signal

Report which it is.

### Required outputs

1. **`layer-6-phase3-corridor-rescaled.csv`** — 36 rows × ~12 columns:
   - country_code, country_name, lens1_ratio, phase1_corridor, phase3_corridor, corridor_shift, phase1_fragility_class, phase3_fragility_class, fragility_class_shift, squeeze_flag, post_recal_squeeze_alignment, notes
2. **`layer-6-phase3-corridor-rescaled.json`** — same data, structured, plus a `metadata` block with:
   - new threshold values + calibration rationale
   - corridor count verdict + rationale
   - sentinel test result (PL shift confirmed/refuted)
   - class distribution old → new
3. **`layer-6-phase3-corridor-methodology.md`** — under 200 lines:
   - structural-bias adjustment definition + calibration anchors
   - new corridor thresholds + rationale
   - corridor count verdict (with sub-corridor analysis if applicable)
   - methodology for re-evaluating fragility classes under new corridors
   - squeeze-flag pattern-extension verdict
4. **`layer-6-phase3-corridor-findings.md`** — under 200 lines:
   - PL sentinel test result
   - Top corridor shifts (gainers + losers)
   - New class distribution + which countries changed class
   - Squeeze-flag extension verdict
   - Open questions for Bundle K + L

### Constraints

- BR-19: don't fabricate calibration anchors. If 2.80 / 1.20 thresholds aren't well-justified by the named anchors (Autor 2024, El-Sahli/Upward, Phase 1 sub-cluster boundaries), surface that as a methodology gap and propose a defensible alternative.
- BR-21: per-country provenance in CSV/JSON. derivation_method explicit for any inferred class change.
- Do NOT modify the locked spec (`layer-6-lens-framework.md`). If Phase 3 finds the spec needs amendment (e.g., 3 → 2 corridors), surface as recommendation; master session decides.
- Do NOT touch Phase 1 or Phase 2 output files.
- Phil does all git commits.

### Verification

Before declaring complete:
1. PL (lens1_ratio 2.96) shifts to C3-rescaled. If not, threshold is wrong.
2. Nordic Class I status preserved or explicitly flagged for change. (Bundle H found DK/FI/IS/NO are robust; SE is knife-edge.)
3. IE + UK remain Class III (or shift Class IV — surface either way).
4. Class IV count: still 3 (TR/RS/MK), or any candidate moves out → audit per Bundle D's BA → Class II logic.
5. Corridor count verdict has named criterion (not "feels right").
6. Cell count check: 36/36 countries reassigned; no nulls in phase3_corridor.

### When done — report back to master session with

1. PL sentinel test result (pass/fail) + threshold values locked
2. New corridor boundaries + rationale
3. Corridor count verdict (3 / 2 / 4) + rationale
4. Class distribution old (5/26/2/3) → new (?/?/?/?)
5. Top 5 corridor shifts (which countries moved + magnitude)
6. Squeeze-flag pattern-extension verdict (BE/NL real or decorative)
7. Whether SE knife-edge survives re-calibration unchanged
8. Open questions for Bundle K (Klinger join) + L (scenario probability)

## END PROMPT
