# Handover Prompt — Bundle L: Scenario-Realisation Probability Weighting (Phase 3 Priority 3, Closure)

Self-contained prompt. **Final Phase 3 sub-bundle.** Assigns realisation probabilities to the 6 routine-perturbation scenarios (S1, S2a, S2b, S3, S4a, S4b) + S5 cascade, computes probability-weighted expected corridor per country, and folds in the cluster of findings surfaced across Bundles D / H / I / J / K-2: SE knife-edge, Nordic post-growth context, S2b-only-optimism fragility, BE/NL squeeze-flag extension, capability-floor breach scope expansion. Closes Phase 3.

**Dispatch only after Bundle K-2 reports back.** Bundle K-2 is the final input refinement.

---

## START PROMPT

I need you to execute Phase 3 priority 3: scenario-realisation probability weighting + Phase 3 closure synthesis. This consumes Bundle J (re-calibrated corridors), Bundle K-2 (2-digit Klinger Lens 5(c) signal), and folded findings from Bundles D/H/I to produce the final Phase 3 fragility map.

This is the last sub-bundle of Phase 3. After Bundle L, the master session synthesises Phase 4 (deliverable). Do NOT touch deliverable scoping in this bundle.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — locked spec; Class I now relative-stable (±1 of baseline); see the "Fragility Classes" + "Per-scenario implications under post-growth regime" sections
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-plan-2026-04-29.md` — Phase 3 plan; folded items list
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-corridor-rescaled.csv` + `.json` — Bundle J output (re-calibrated corridors at 1.20/2.80; PL → C3; Class I empty under naive carryover; new class distribution proposed under (b))
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-corridor-methodology.md` + `findings.md` — Bundle J methodology + findings
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-klinger-rescaled.csv` + `.json` — Bundle K-2 output (2-digit Klinger; updated Lens 5(c); refined capability-floor breach scope)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase3-klinger-findings.md` — Bundle K-2 findings (top deltas, breach scope at 2-digit, Class L candidate countries)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-scoring.csv` + `.json` — Bundle D Phase 2 scoring (per-scenario corridors per country; do NOT modify)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-robustness-probe-2026-04-29.md` — Bundle H verdict (SE knife-edge specifics)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-data.json` — Lens 4/5 input data (regime classifications via `regime_stability`)

### Class I locked (b) — relative-stable

Class I = corridor stays within ±1 of baseline across S1–S4b. Class II = swings >±1 (spans 3+ corridors). Cascade behaviour reported separately. Apply this definition uniformly when re-evaluating fragility classes under the re-calibrated Phase 3 corridors. Do NOT re-litigate (a)/(b)/(d) — locked.

### Task 1 — Scenario realisation probabilities

Assign realisation probabilities to S1, S2a, S2b, S3, S4a, S4b (the 6 routine variants) + S5 cascade. Sum to 1.0 across the 6 routine variants (S5 is structurally separate per locked spec; assign its own conditional-probability marker, NOT included in the 1.0 sum).

**Methodology:** defensible methodology, not pulled from thin air. Anchor on:
1. **Locked spec lines 60–104** — the per-scenario implications under growth-baseline vs post-growth regime (table). Use this to constrain probability ranges by regime.
2. **Phase 1 finding** — orthogonality refuted demographic buffer at scale; reinstatement-revival historical-base-rate is structurally biased (Autor 2024). S1 probability should reflect this — not 0, but bounded above by the structural-bias finding.
3. **Bundle D finding** — concentrated S2b-only-optimism (31/36 countries reach C1 only under S2b). S2b probability is the sentinel calibration: too-high = optimistic-by-default; too-low = framework collapses to "everything is C2/C3."
4. **Phase 1/3 structural-bias correction** — under post-growth regime (DE/IT/NO/SE/FI per `regime_stability` flags), S1 probability is materially lower than under growth-baseline.

**Recommended probability frame:**
- Use a **regime-conditional** probability assignment: P(S | regime) where regime ∈ {growth_baseline, secular_stagnation_warning, post_growth_empirical}.
- For each country, look up its regime classification, then apply the regime-conditional probability vector.
- Document the probability vector + the methodological anchors per scenario × regime.

**Sentinel test:** P(S2b | post_growth_empirical) should be the *highest* probability among the 6 routine variants (per spec line 104: "Climate Adaptation Boom 2b becomes the only genuinely-positive scenario that survives the regime check"). If S2b doesn't dominate under post_growth, methodology is wrong.

**Defensibility test:** ranges should be wider than point estimates. Output mid-point + 80% CI per scenario × regime. Bundle L's claim is calibrated probability, not deterministic forecast.

### Task 2 — Probability-weighted expected corridor per country

For each of the 36 countries:
```
P(corridor=k | country) = Σ_{s ∈ S1..S4b} P(s | regime_country) × I(corridor_country_under_s == k)
```

Where `corridor_country_under_s` comes from Bundle D's per-scenario corridor assignment, **mapped to Bundle J's re-calibrated thresholds** (1.20/2.80) — i.e., re-bucket each country's per-scenario lens1_ratio under the new thresholds, then probability-weight.

Output per country:
- `expected_corridor` (probability-weighted; can be fractional, e.g., 2.4)
- `expected_corridor_rounded` (nearest integer; for headline communication)
- `corridor_uncertainty_band` (from the 80% CI on probabilities)
- `dominant_corridor` (the corridor with highest single-scenario probability mass)

### Task 3 — Re-evaluate fragility classes under (b) + re-calibrated corridors

For each country, re-evaluate Class I/II/III/IV using:
- Bundle J's re-calibrated corridors (1.20/2.80)
- Bundle K-2's updated Lens 5(c) (capability-floor breach scope at 2-digit)
- Class I = relative-stable (±1 baseline) across S1–S4b
- Class III = under S3 (Muddle Through) lands in C3-rescaled
- Class IV = Lens 5 inputs at maxima OR partial-coverage candidate with ≥1 extreme reading (Bundle D's BA exception preserved)

**Verify:** Bundle J's prediction (5 Nordics in Class I under (b)) should hold. If a Nordic falls out, surface — could be a Bundle K-2 effect (capability-floor breach pulled them into more variant corridors).

### Task 4 — Folded findings synthesis

For each folded item, produce a deliverable-ready paragraph:

**(a) SE knife-edge** — Bundle H found SE drops Class I at S4b ≥ 0.20. Under (b)'s relative-stable definition, does SE survive Class I? Add a `class_i_confidence` flag to SE specifically (low/medium/high) with rationale.

**(b) Nordic post-growth (NO/SE/FI also `post_growth_empirical`)** — Class I status under post-growth carries different policy implications than Class I under growth-baseline. Per spec line 108: "the same corridor assignment carries different implications depending on which regime the country occupies." Produce a 2-line annotation per Nordic country: "Class I under [regime]; structural read: …"

**(c) S2b-only-optimism** — quantify per country: how many of the 6 routine variants land that country in C1 vs C2 vs C3? If S2b is the only path to C1, flag the country as `s2b_dependent` = TRUE. Country count + list.

**(d) BE/NL squeeze-flag extension** — Bundle J found BE/NL squeeze flag survives recalibration but BE/NL did NOT shift to C3 like other re-calibration shifts. Confirm: is BE/NL squeeze flag an *orthogonal signal* (jurisdictional buffering, not displacement velocity) or a *false positive* (over-fit)? Apply Bundle K-2's Lens 5(c) to test: do BE/NL show the high-coord pulse expected of squeeze-flagged countries? If yes → orthogonal signal confirmed. If no → over-fit candidate.

**(e) Capability-floor breach scope expansion (Bundle K-2)** — final count of breach-flagged countries (was 11 at 1-digit; possibly more at 2-digit). For each breach country, mark `s5_cascade_priority` = high/medium/low based on Lens 5 composite drag + breach magnitude.

### Task 5 — Phase 3 final fragility map

Produce the deliverable-ready output: 36 rows × {country, expected_corridor, dominant_corridor, fragility_class, class_i_confidence (where relevant), regime, s2b_dependent, breach_flag, scale_tag, narrative_one_liner}.

Where `scale_tag` per spec is one of: aggregate / distributional / both. Apply the scale-tag rule from spec line 48: aggregate-only assignments must declare matched distributional reading.

### Required outputs

1. **`layer-6-phase3-scenario-probability.csv`** — 36 rows × ~18 columns
2. **`layer-6-phase3-scenario-probability.json`** — same data structured + metadata block:
   - Probability vector per regime + 80% CIs
   - Methodology anchors per scenario × regime
   - Sentinel-test result (S2b dominance under post-growth)
   - Class distribution comparison: Phase 2 (5/26/2/3) → Bundle J naive carryover (0/?/15/3) → Phase 3 final (under (b) + Bundle K-2)
3. **`layer-6-phase3-probability-findings.md`** — under 300 lines:
   - Probability table + regime breakdown
   - Sentinel test (S2b under post-growth)
   - Final fragility map TL;DR (corridor-by-class country count)
   - Folded findings synthesis (5 paragraphs, one per folded item)
   - SE confidence flag rationale
   - Nordic post-growth annotations
   - S2b-dependent countries list + count
   - BE/NL extension verdict (orthogonal vs over-fit)
   - Capability-floor breach final count + s5_cascade_priority distribution
   - **Phase 3 closure summary** — what's locked, what's open for Phase 4 (deliverable building)

### Constraints

- BR-19: probability assignments must cite methodology anchors. No bare numbers. If anchor is "expert elicitation," cite the elicitation framework (e.g., Cooke 1991 classical model, IPCC AR6 likelihood scale).
- BR-21: per-country provenance — `derivation_method` documents probability vector + regime + per-scenario mapping
- Do NOT modify locked spec, Phase 1/2 outputs, Bundle J or K-2 outputs
- Phil does all git commits

### Verification

Before declaring complete:
1. **S2b dominance sentinel** — P(S2b | post_growth_empirical) is highest among 6 routine variants. If not, methodology is wrong.
2. **Probabilities sum to 1.0** across 6 routine variants per regime (within rounding).
3. **5 Nordics Class I confirmed** under (b)'s relative-stable definition + Bundle K-2 inputs.
4. **PL Class III confirmed** (Bundle J sentinel preserved).
5. **TR/RS/MK Class IV confirmed** (Bundle D's candidate-Class-IV result preserved); BA stays Class II.
6. **No country has expected_corridor > 3** (corridors bounded 1–3 per spec).
7. **No country lacks scale_tag** — required field per spec.

### When done — report back to master session with

1. Probability table (regime × scenario; with CIs)
2. Final class distribution (Phase 3 lock)
3. SE class_i_confidence verdict
4. S2b-dependent country count + list
5. BE/NL extension verdict (orthogonal/over-fit)
6. Capability-floor breach final scope (vs Bundle K-2's 1-digit count)
7. Sentinel tests passed
8. **Phase 3 closure status** — what's ready for Phase 4 (deliverable scoping)
9. Open questions for Phase 4

## END PROMPT
