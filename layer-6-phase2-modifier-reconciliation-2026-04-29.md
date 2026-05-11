# Layer 6 Phase 2 — `lens4_corridor_modifier` Spec/Implementation Reconciliation

**Date:** 2026-04-29
**Trigger:** Bundle H robustness probe §5 surfaced ambiguity between methodology-notes §1.3 ("push C2 → C3" / "push C1 Nordics → C2") and Bundle D engine output (baseline reproduces only if modifier is annotation-only).
**Scope:** Diagnostic + targeted methodology-notes patch. NO re-scoring. NO change to lens-framework, scoring CSV/JSON, or findings.

---

## Verdict: (a) — modifier is annotation-only; methodology-notes wording is loose

**Diagnostic finding: uniform annotation-only across all 11 modifier=+1 countries.** Engine has a single semantic. Spec wording ("push C2 → C3", "push C1 Nordics → C2") implies corridor-shifting, but the engine never shifts. The same §1.3 simultaneously commits to orthogonality preservation, which is consistent with annotation semantics. Loose wording, consistent implementation. Fix is in the methodology-notes file, not the engine.

---

## Diagnostic — squeeze-flag-TRUE countries (8)

| Country | phase1 | shocks | squeeze | modifier | S3 | S3 vs phase1 | Behaviour |
|---|---|---|---|---|---|---|---|
| BE | 2 | 2 | TRUE | +1 | 2 | == | annotation-only |
| DE | 2 | 4 | TRUE | +1 | 2 | == | annotation-only |
| DK | 1 | 4 | TRUE | +1 | 1 | == | annotation-only |
| FI | 1 | 4 | TRUE | +1 | 1 | == | annotation-only |
| FR | 2 | 4 | TRUE | +1 | 2 | == | annotation-only |
| NL | 2 | 3 | TRUE | +1 | 2 | == | annotation-only |
| NO | 1 | 3 | TRUE | **0** | 1 | == | **anomalous (modifier mis-assigned)** |
| SE | 1 | 4 | TRUE | +1 | 1 | == | annotation-only |

**NO anomaly:** squeeze=TRUE AND phase1=1 should fire methodology-notes §1.3 rule 3 → modifier=+1. CSV shows modifier=0. This is a flag-application inconsistency separate from the annotation-vs-shifting question; it does NOT affect the verdict (S3 == phase1 either way under annotation semantics) but should be surfaced to master. Possible engine cause: rule 3 may not have been wired in, or only fires when shocks ≥ some additional condition that isn't in §1.3 wording.

---

## Diagnostic — 4-or-more-shocks countries (rule 2 check)

| Country | phase1 | shocks | squeeze | modifier | S3 | S3 vs phase1 | Behaviour |
|---|---|---|---|---|---|---|---|
| DE | 2 | 4 | TRUE | +1 | 2 | == | annotation-only |
| DK | 1 | 4 | TRUE | +1 | 1 | == | annotation-only |
| EE | 2 | 4 | FALSE | +1 | 2 | == | annotation-only |
| FI | 1 | 4 | TRUE | +1 | 1 | == | annotation-only |
| FR | 2 | 4 | TRUE | +1 | 2 | == | annotation-only |
| LT | 2 | 4 | FALSE | +1 | 2 | == | annotation-only |
| PL | 2 | 4 | FALSE | +1 | 2 | == | annotation-only |
| PT | 2 | 4 | FALSE | +1 | 2 | == | annotation-only |
| SE | 1 | 4 | TRUE | +1 | 1 | == | annotation-only |

All 9 fire rule 2 correctly. All 9 show S3 == phase1.

---

## Aggregate

- 11 countries with `lens4_corridor_modifier = +1` (BE, DE, DK, EE, FI, FR, LT, NL, PL, PT, SE).
- **All 11**: `corridor_under_scenario_3 == phase1_combined_corridor` → **annotation-only**.
- **0** corridor-shifting cases.
- **0** mixed/conditional cases.
- **1** rule-firing anomaly: NO (rule 3 should fire but didn't).

Engine semantics are uniform: modifier annotates a compound-shock signature without re-corridoring. Per-scenario corridor reassignment is driven only by velocity/absorption/drag perturbation, not by the modifier value.

---

## Reasoning for verdict (a)

§1.3 contains two commitments that pull opposite directions in the literal reading:
1. Three "+1 push" rules described in causal-shifting language.
2. The orthogonality-preservation note: *"This preserves the Phase 1 orthogonality finding by construction"* — only meaningful if the modifier does NOT re-corridor (otherwise Lens 4 actively *changes* Phase 1's corridor distribution).

The engine resolves the tension by treating the modifier as annotation. The orthogonality finding (§6) survives only under annotation semantics — under shifting semantics, Lens 4 would re-corridor 11 countries and the §6 conclusion would need substantial rewriting (Nordics out of C1, EE/LT/PL/PT/DE/FR/NL into C3 from squeeze + 4-shock combinations). The orthogonality writeup is already justified for shipping; that commitment is load-bearing.

The cleanest read: the modifier is a **flag**, not a **shift**. The "push C2 → C3" framing was a thinking-out-loud holdover from Retrofit v0.3 Case 1 derivation, not an implementation directive. Annotation semantics preserve the spec's logical commitments while matching the engine.

---

## Methodology-notes §1.3 amendment (applied this session)

Wording in `layer-6-phase2-methodology-notes.md` lines 52–58 replaced. The three "+1" conditions retain identical firing rules but the parenthetical "push" framing is removed; an explicit semantic statement is added: the modifier annotates a compound-shock signature without re-corridoring; per-scenario corridor reassignment is driven only by the perturbation logic in §3.

---

## Outstanding items for master session

1. **Verdict: (a).**
2. **Methodology-notes §1.3 amended in this session: yes.**
3. **Bundle D scoring re-run needed: no.**
4. **NO modifier=0 anomaly:** decide whether to (i) patch CSV/JSON to set NO modifier=+1 (rule 3 retroactively applied — cosmetic since engine is annotation-only), (ii) document as known engine-vs-spec gap and leave, or (iii) trace the engine logic and reconcile in Phase 3. Recommend (ii) — annotation-only semantics mean NO's class assignment is unaffected; the flag is informational.
5. **Phase 3 dispatch readiness:** unblocked. Bundle H probe results remain valid (calibration sweep was against the now-confirmed annotation-only baseline). Phase 3 can proceed with the modifier reinterpreted as a documented compound-shock annotation field.

---

## Constraints honored

- No modification to `layer-6-lens-framework.md`, scoring CSV/JSON, or findings.md.
- No re-run of Bundle D scoring.
- BR-19: every diagnostic claim sourced from CSV column read; NO anomaly flagged rather than silently rationalised.
