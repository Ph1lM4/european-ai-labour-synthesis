# Handover Prompt — Bundle I: lens4_corridor_modifier Spec/Implementation Reconciliation (2026-04-29)

Bounded reconciliation pass to resolve the load-bearing ambiguity surfaced by Bundle H §5: methodology-notes §1.3 specifies `lens4_corridor_modifier = +1` for squeeze-flagged C1 countries (which would push DK/FI/NO/SE → C2 and collapse the Nordic Class I result), but the Bundle D engine reproduces the baseline only when the modifier is treated as annotation-only.

This is the single load-bearing item between Phase 2 and Phase 3 dispatch. Should take ~20–40 minutes — diagnostic, then a small targeted fix.

---

## START PROMPT

I need you to reconcile a methodology-spec vs implementation mismatch in Bundle D Phase 2 scoring. The mismatch is centred on `lens4_corridor_modifier`. Bundle H robustness probe (file: `layer-6-phase2-robustness-probe-2026-04-29.md` §5) flagged that the engine reproduces baseline only if the modifier is treated as annotation; methodology-notes §1.3 describes it as corridor-shifting. Resolve the ambiguity.

This is NOT a re-scoring session unless the resolution requires it. Diagnose first, then patch the smaller artefact.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-methodology-notes.md` §1.3 (lines 52–58) — the canonical modifier spec
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-scoring.csv` — particularly columns `lens4_corridor_modifier`, `phase1_combined_corridor`, `corridor_under_scenario_1` … `corridor_under_scenario_5`
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-scoring.json` — same data + metadata block
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-robustness-probe-2026-04-29.md` §5 — the probe's framing of the ambiguity
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — locked spec, Class I + corridor definitions (do NOT modify)

### The exact ambiguity

Methodology-notes §1.3 specifies three +1 conditions:
1. `+1` if squeeze-flag=TRUE AND Phase 1 corridor = 2 (push C2 → C3)
2. `+1` if compounding-shock-count ≥ 4 AND Phase 1 corridor < 3 (generic push)
3. `+1` if squeeze-flag=TRUE AND Phase 1 corridor = 1 (push C1 Nordics → C2)

Bundle D output: DK/FI/NO/SE have `phase1_combined_corridor=1`, are squeeze-flag=TRUE, AND their per-scenario corridors all equal 1 (or scenario-perturbation outputs of 1). If §1.3 rule 3 had been *applied to per-scenario corridors*, their baseline corridor would be 2, and Class I evaluation would proceed from C2 baseline — likely changing the Nordic Class I count.

### Your diagnostic task

For each of the 36 countries:
1. Read `lens4_corridor_modifier` and `phase1_combined_corridor` from the CSV.
2. For each scenario column (1, 2a, 2b, 3, 4a, 4b, 5), check whether the corridor reflects modifier application or not.
3. Concretely: for any country where `lens4_corridor_modifier = +1`, is `corridor_under_scenario_3 == phase1_combined_corridor + 1` (modifier applied) or `corridor_under_scenario_3 == phase1_combined_corridor` (modifier annotation-only)?
   - Note: Scenario 3 = Muddle Through = Phase 1 baseline by spec. So this is the cleanest test point.
4. Tally: how many countries with modifier=+1 show modifier-applied vs annotation-only behaviour under S3?
5. If the behaviour is uniform across all +1 countries, the engine has a single semantic. If mixed, the engine has conditional logic — surface the pattern.

### Determine resolution among (a) / (b) / (c)

**(a) Methodology-notes are wrong; modifier is annotation-only.**
Evidence for: engine consistently applies annotation-only across all +1 countries; Class I result depends on this reading; the spec preserved the orthogonality finding by treating +1 as a documented-but-non-corridor-shifting flag (see §1.3 note "Negative modifiers explicitly excluded… preserves the Phase 1 orthogonality finding").
Fix: amend methodology-notes §1.3 wording to remove "push C2 → C3" and "push C1 Nordics → C2" framing; replace with "annotates the country as having compound-shock signature without re-corridoring; corridor reassignment driven only by per-scenario perturbation logic."

**(b) Engine is wrong; modifier should shift corridors.**
Evidence for: §1.3 wording is unambiguous about pushing corridors; the orthogonality finding is preserved at *Phase 1*, not Phase 2 (Phase 2 *is* where Lens 4 surfaces the squeeze mechanism). If +1 means +1, it means +1.
Fix: re-run Bundle D scoring with modifier applied to baseline corridor before per-scenario perturbation. Class distribution will change; Nordic Class I result may not survive. This invalidates Bundle H probe results too (calibration sweep ran against the annotation-only baseline).

**(c) Modifier is conditional** (e.g., applied to some scenarios but not others, or applied only when Lens 5 also signals).
Evidence for: only if the diagnostic finds mixed behaviour in step 4 above. Surface the pattern; document.
Fix: spec amendment + methodology-notes reconciliation; no re-run unless conditional logic was implemented inconsistently.

### Recommended verdict structure

Lead with the diagnostic finding (uniform vs mixed). Then:
- If uniform annotation-only AND the orthogonality finding is what the spec was really protecting → recommend (a). This is the most likely outcome and the cleanest fix.
- If uniform corridor-shifting expected by spec but engine doesn't deliver → recommend (b) ONLY if Phil should accept a Bundle D re-run.
- If mixed → recommend (c) with explicit conditional rule.

Master session strongly suspects (a) is correct: the methodology-notes §1.3 also contains the line *"This preserves the Phase 1 orthogonality finding by construction"* — which is consistent with annotation semantics (don't re-corridor; just flag). Spec wording is loose ("push") but the logical commitment is to orthogonality preservation.

### Required outputs

1. **Diagnostic table:** for each of the squeeze-flag-TRUE countries (BE, DE, DK, FI, FR, NL, NO, SE — 8 countries), report:
   - phase1_combined_corridor
   - lens4_corridor_modifier
   - corridor_under_scenario_3 (the cleanest test point)
   - "applied" / "annotation-only" / "anomalous"
2. Same for the 4-or-more-shocks countries (run modifier-condition-2 check)
3. Verdict: (a), (b), or (c) with one-paragraph reasoning
4. **If (a):** write the methodology-notes §1.3 amendment text. Apply the edit to `layer-6-phase2-methodology-notes.md`. Do NOT re-run scoring.
5. **If (b) or (c):** stop and report back to master session. Do NOT re-run scoring autonomously — Phil decides.

### Constraints

- Do NOT modify `layer-6-lens-framework.md`, scoring CSV/JSON, or findings.md
- Do NOT re-run Bundle D scoring without master-session approval
- BR-19 no fabrication: read what's there; flag mismatches; don't invent reconciliation logic
- Output verdict + diagnostic to a NEW file: `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-modifier-reconciliation-2026-04-29.md` — under 150 lines

### When done — report back to master session with

1. Verdict: (a) / (b) / (c)
2. The 8-country squeeze-flag diagnostic table
3. Whether methodology-notes §1.3 was amended in this session (yes if (a); no if (b)/(c))
4. Whether Bundle D scoring needs re-run (yes if (b); maybe if (c); no if (a))
5. One-line implication for Phase 3 dispatch readiness

## END PROMPT
