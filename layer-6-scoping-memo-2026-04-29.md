# Layer 6 Scoping Memo — 2026-04-29

**Session output.** Strategic scoping pass for Layer 6 (Synthesis) of the European AI Labour Market suite. Working session moved from "lens framework spec" to "decision-locked v2 spec." Full updated spec at [`layer-6-lens-framework.md`](layer-6-lens-framework.md).

---

## Starting state

Layer 6 had a lens framework (4 lenses + draft 5 corridors) but no scoping for output format, country-scoring methodology, or how lens findings combine into corridor assignments. Layers 1–5 were live or near-live. L3 retrofit at v0.3.2.

## Decisions locked (2026-04-29)

1. **Output format:** document + site (`synthesis.nexalps.com`). Document anchors analysis; site renders corridor map + 5-trajectory sparkline per country.
2. **Lens 5 added:** Polycrisis Drag (institutional-bandwidth-saturation mechanism). Distinct from Lens 4 (worker-level shock combination). Working name "Multidimensional Chess to the Square Root."
3. **Lens 3 cut as standalone:** folded into Lens 1 as Perez compression footnote.
4. **Country scope:** 36 (EU-27 + EEA + CH + UK) full corridor + Ukraine as Lens 5 reference case (analytical narrative only).
5. **Scenario stack:** 5 scenarios with discipline rule (one mechanism per scenario). Subversions on Scenarios 1, 2, 4. Trajectory Continuation renamed to Muddle Through.
6. **Corridor count:** target 3 (down from 5). Bifurcated folds into scale-tag system; Compounding Crisis folds into Class IV.
7. **Fragility classes:** 4 (Robust / Fragile / Pre-Failure Risk / Currently Failing). III/IV demarcation rule = forecast vs measurement.
8. **Scale tags:** required field per corridor assignment (aggregate / distributional / both).

## Tooze finding

[Chartbook 407 (Sep 2025)](https://adamtooze.substack.com/p/chartbook-407-polycrisis-revisited): Tooze stepped back from "polycrisis" as a general descriptor. Pivoted to personal-agency framing.

[Chartbook 130 (2022, original)](https://adamtooze.substack.com/p/chartbook-130-defining-polycrisis): Tooze never addressed institutional response *bandwidth* as a binding constraint. His mechanism was structural-impersonal feedback loops.

**Implication:** Lens 5's institutional-mechanical mechanism is a third scale of analysis from either Tooze framing. We use the term "polycrisis" because the concurrent-crisis framing is established. We do NOT inherit Tooze's mechanism. Methodology section states this distinction explicitly.

## What's blocking

- Retrofit v0.3 verification (Levinson Ch 7, Bessen banking chapter) — blocks Lens 1 two-horizon spec but NOT Lens 1 v1 (single-horizon)
- L3 render gap — L6 reads `disruptions-data.json` directly until closed
- IISS Military Balance 2025 — paywalled, useful for Lens 5(a) force-structure scoring

## What's unblocked

Phase 1 (Lens 1 + 2 against country data, single-horizon v1) can start today. Phase 2 (Lens 4 + 5 integration) can start in parallel.

## Recommended next session

Continue with the handover prompt at the bottom of `layer-6-handover-prompt-2026-04-29.md`. First step: fix the L1–L5 issues identified in the suite verification log so L6 can read clean data inputs.
