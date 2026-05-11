# Layer 6 Phase 3 Plan — 2026-04-29

Master-session plan for Phase 3 dispatch. Scopes 3 sub-bundles with dependencies + folded findings from Bundles D, H, I.

---

## Phase 3 scope (locked)

Phase 3 closes Layer 6 by validating two structural decisions left as warnings in Phase 2 (corridor count + structural-bias re-calibration), upgrading one deferred input (Klinger ISCO join), and adding scenario-realisation probability so the corridor map carries operational weight rather than uniform-likelihood scenario stacking.

### 4 priorities

| # | Priority | Bundle | Depends on |
|---|---|---|---|
| 1 | Structural-bias re-calibration + corridor count validation | **J** | none |
| 2 | Klinger × ISCO-3-digit join for Lens 5(c) | **K** | none (parallel with J) |
| 3 | Scenario-realisation probability weighting | **L** | J + K |
| 4 | Synthesis + Phase 4 readiness check | (master session) | J + K + L |

### Folded items (from Bundles D / H / I)

- **Bundle H finding — SE knife-edge:** SE drops Class I → II at S4b ≥ 0.20. Folded into Bundle L (probability weighting): if S4b high-multiplier scenarios carry meaningful realisation probability, SE Class I confidence flag becomes load-bearing.
- **Bundle D finding — Nordic post-growth (NO/SE/FI also `post_growth_empirical`):** Folded into Bundle L. Class I status under post-growth carries different policy implications than Class I under growth-baseline; probability weighting must surface this asymmetry.
- **Bundle D finding — concentrated S2b-only optimism:** 31 of 36 countries reach C1 only under wage-premium climate boom. Bundle L's probability assignment for S2b is the sentinel calibration question — if S2b probability is low (<0.15), the optimistic corridor map is fragile by construction.
- **Bundle D finding — BE/NL squeeze-flag pattern extension beyond spec-named DE/FR/Nordics:** Folded into Bundle J (corridor count). If BE/NL's compound-shock signature shifts them to C3 under re-cal, this validates the pattern extension; if not, the squeeze-flag extension is decorative.
- **Bundle I patch — NO rule-3 retroactive +1:** No Phase 3 implication; annotation-only.

---

## Bundle dependencies

```
   ┌──────────────┐      ┌──────────────┐
   │ Bundle J     │      │ Bundle K     │
   │ Structural   │      │ Klinger ISCO │
   │ bias + count │      │ join → L5(c) │
   └──────┬───────┘      └──────┬───────┘
          │                     │
          └─────────┬───────────┘
                    ▼
            ┌──────────────┐
            │ Bundle L     │
            │ Scenario     │
            │ probability  │
            └──────┬───────┘
                   ▼
            ┌──────────────┐
            │ Synthesis    │
            │ (master)     │
            └──────────────┘
```

J and K can run in parallel — they touch different methodology layers and produce independent outputs. L waits for both.

---

## Bundle J — Structural-bias re-calibration + corridor count

**Handover:** [`bundle-j-structural-bias-recal-handover-2026-04-29.md`](bundle-j-structural-bias-recal-handover-2026-04-29.md)

**Goal:** Apply the structural-bias adjustment that Phase 1 + 2 deferred to Phase 3. Verify PL (lens1_ratio 2.96) shifts to C3 — sentinel test per spec line 54. Re-evaluate whether 3 corridors is the right count or if the data warrants 2 or 4.

**Output files:** `layer-6-phase3-corridor-rescaled.csv/.json`, `layer-6-phase3-corridor-findings.md`, `layer-6-phase3-corridor-methodology.md`

**Sentinel:** PL must shift C2 → C3. If it doesn't, methodology is wrong.

---

## Bundle K — Klinger × ISCO-3-digit join for Lens 5(c)

**Handover:** [`bundle-k-klinger-isco-join-handover-2026-04-29.md`](bundle-k-klinger-isco-join-handover-2026-04-29.md)

**Goal:** Lens 5(c) currently uses Phase 1 velocity directly (Bundle D Decision 5 deferred Klinger weighting). Join the Klinger ISCO 3-digit coordination-share data (130 codes, 125 at M-confidence from `layer-6-klinger-isco-coordination-share.json`) with per-country Eurostat LFS occupation-employment shares, recompute Lens 5(c) as employment-weighted Klinger × velocity, and report which countries shift substantively.

**Output files:** `layer-6-phase3-klinger-rescaled.csv/.json`, `layer-6-phase3-klinger-findings.md`

**Sentinel:** Countries with high coordination-layer occupation density (DE/AT — strong Beruf system + management depth; UK/IE — knowledge-services concentration) should show meaningfully different Lens 5(c) under Klinger weighting vs uniform-velocity proxy.

---

## Bundle L — Scenario-realisation probability weighting

**Handover:** *To be written after J + K complete.* Inputs are J's re-calibrated corridors + K's re-weighted Lens 5(c) + folded findings (SE knife-edge, Nordic post-growth, BE/NL squeeze).

**Goal:** Assign realisation probabilities to S1, S2a, S2b, S3, S4a, S4b, S5 — using a defensible methodology (e.g., expert-elicitation-anchored ranges + scenario-discipline-rule constraint). Produce probability-weighted expected corridor per country. Flag SE under post-growth Nordic context. Surface S2b-only-optimism fragility.

**Output files:** `layer-6-phase3-scenario-probability.csv/.json`, `layer-6-phase3-probability-findings.md`

---

## Phase 4 readiness check (post-Phase-3, master session)

Once L is complete, the master session synthesises:

1. Final corridor map (3 / 2 / 4 — whichever J validates) with probability-weighted corridor + fragility class + scale tag per country
2. Lens-by-lens findings document
3. Site-renderable data structure for `synthesis.nexalps.com`
4. Document-anchor structure for the Layer 6 deliverable

Phase 4 = building the document + site. Out of scope for this plan.

---

## Tracking

| Bundle | Handover written | Dispatched | Complete |
|---|---|---|---|
| J | ✅ 2026-04-29 | ⏸ | ⏸ |
| K | ✅ 2026-04-29 | ⏸ | ⏸ |
| L | ⏸ (post-J+K) | ⏸ | ⏸ |
| Synthesis | n/a | n/a | ⏸ |
