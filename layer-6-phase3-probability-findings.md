# Bundle L — Scenario-Realisation Probability Weighting + Phase 3 Closure

**Date:** 2026-04-29
**Inputs:** Bundle J (corridors rescaled 1.20/2.80) + Bundle K-2 (2-digit Klinger Lens 5c, breach scope expansion) + Phase 1/2 lens 4/5 inputs + locked spec.
**Outputs:** `layer-6-phase3-scenario-probability.csv/.json` + this file.
**Phase 3 status: CLOSED.**

---

## TL;DR

1. **Probability vectors locked per regime.** S2b dominates under post-growth (P=0.30, highest of 6 routine variants — sentinel PASSED). All probabilities sum to 1.0 across the 6 routine variants per regime. S5 carried as conditional marker (g=0.05, s=0.10, p=0.15).
2. **Final fragility class distribution: I=9, II=9, III=15, IV=3** (locked 2026-04-29 per Q1 asymmetric-guard clarification). 5 Nordics + 4 Continental squeeze (BE/FR/NL/LU) Class I. Asymmetric guard added to (b) relative-stable rule: "no routine variant assigns the country to C3." 7 countries reclassified I→II (CH, DE, LI, BG, ES, LV, RO) — their C2 baseline reaches C3 under S4a/S4b, semantically inconsistent with "Robust." Aligns with spec line 387 original intent (5 Nordics + NL; CH falls out under structural-bias-corrected thresholds — that's the Phase 3 correction working as intended).
3. **3 countries are S2b-dependent for any C1 outcome:** AT, LU, TR. Their optimism path runs entirely through climate Zone-C wage premium.
4. **Capability-floor breach final scope: 12 countries** (Bundle K-2 unchanged). DK marginal entry. s5_cascade_priority distribution: HIGH=7, MEDIUM=4, LOW=1.
5. **BE/NL squeeze-flag extension verdict: orthogonal signal confirmed** (capital-flight Mode 1 mechanism, not displacement velocity). No false-positive evidence at 2-digit Klinger.
6. **SE class_i_confidence = MEDIUM.** Bundle H S4b ≥ 0.20 knife-edge survives as within-Class-I sensitivity band, not class boundary; SE entered breach list at 2-digit.
7. **Phase 3 deliverable surface locked.** 36 rows × 26 columns scenario-probability table ships as Phase 4 input.

---

## 1. Probability table (regime × scenario, 80% CIs)

Methodology: Cooke-1991-style structured expert elicitation; ranges align with IPCC AR6 likelihood scale. Anchors per scenario × regime documented in JSON metadata block (`methodology_anchors`).

| Regime | S1 | S2a | S2b | S3 | S4a | S4b | (S5 cond) |
|---|---|---|---|---|---|---|---|
| growth_baseline | 0.10 [0.05–0.18] | 0.15 [0.08–0.22] | 0.20 [0.10–0.28] | 0.30 [0.22–0.40] | 0.15 [0.08–0.22] | 0.10 [0.05–0.18] | 0.05 |
| secular_stagnation_warning | 0.07 [0.03–0.13] | 0.13 [0.07–0.20] | 0.25 [0.15–0.33] | 0.28 [0.20–0.38] | 0.15 [0.08–0.22] | 0.12 [0.06–0.20] | 0.10 |
| **post_growth_empirical** | **0.05** [0.02–0.10] | 0.12 [0.06–0.18] | **0.30** [0.20–0.38] | 0.25 [0.18–0.33] | 0.15 [0.08–0.22] | 0.13 [0.07–0.20] | **0.15** |

**Anchors (load-bearing):**
- **S1 bounded above** by Phase 1 demographic-buffer orthogonality + Autor 2024 weakening reinstatement; under post-growth, S1 mechanism requires expanding output (locked spec line 92–94) → P drops to 0.05.
- **S2b strengthens under post-growth** (line 96, 104): sectoral redirection within flat aggregate; only genuinely-positive scenario surviving the regime check. P rises to 0.30 — dominant.
- **S3 baseline** anchor at ~0.30 across regimes; small downshift under post-growth as S2b/S4 absorb mass.
- **S4a/S4b rise under post-growth** (lines 98-99): fiscal headroom for institutions shrinks; threshold to bandwidth saturation lower.
- **S5 conditional**: Ukraine empirical anchor; P rises with regime severity (g=0.05 → s=0.10 → p=0.15).

## 2. Sentinel test — S2b dominance under post-growth

**PASSED.** P(S2b | post_growth_empirical) = 0.30, exceeds next-highest P(S3 | post_growth) = 0.25.

Verification chain (locked spec line 104): "Climate Adaptation Boom 2b becomes the only genuinely-positive scenario that survives the regime check." Probability frame respects this constraint: S2b is the modal scenario for any post-growth country, and it is the *only* path generating C1 outcomes for AT/LU/TR (s2b_dependent = TRUE).

## 3. Final fragility map (TL;DR)

| Class | n | Countries | Headline read |
|---|---|---|---|
| **I — Robust (relative-stable, C3-guarded)** | 9 | DK, FI, IS, NO, SE *(Nordic anchor, conf=high)*; BE, FR, NL, LU *(Continental Corporatist + squeeze-flag, conf=medium)* | Q1 asymmetric-guard lock 2026-04-29: ±1 of baseline AND no routine variant reaches C3 |
| **II — Fragile** | 9 | AT *(distinct=3 corridors)*, BA *(partial-coverage preserved)*; CH, DE, LI, BG, ES, LV, RO *(reclassified from Class I per Q1 asymmetric-guard: their C2 baseline reaches C3 under S4a/S4b)* | Q1 lock surfaces the structural-bias-corrected reading: 7 countries with C2-to-C3 perturbation paths fail Class I robustness criterion |
| **III — Pre-Failure Risk** | 15 | CY, CZ, EE, EL, HR, HU, IE, IT, LT, MT, PL, PT, SI, SK, UK | S3 lands C3-rescaled |
| **IV — Active Cascade** | 3 | MK, RS, TR | Candidate-partial-coverage with extreme readings |

**Class distribution comparison:**
- Phase 2 (Bundle D, strict-stable): 5 / 26 / 2 / 3
- Bundle J naive carryover (option a): 0 / 18 / 15 / 3
- **Phase 3 final under (b) + Bundle K-2 + Q1 asymmetric-guard lock: 9 / 9 / 15 / 3**

**Sentinels (all PASS):**
- 5 Nordics (DK/FI/IS/NO/SE) Class I confirmed under (b) + Bundle K-2 ✓
- PL Class III confirmed ✓
- TR/RS/MK Class IV confirmed; BA Class II preserved ✓
- All `expected_corridor` ≤ 3 ✓
- All 36 rows have `scale_tag` ✓

**Q1 asymmetric-guard lock (applied 2026-04-29):** Class I = ±1 of baseline AND no routine variant assigns the country to C3. 7 countries reclassified I→II (CH, DE, LI, BG, ES, LV, RO) because their C2 baseline reaches C3 under S4a/S4b — semantically inconsistent with "Robust." Final Class I = 9 (5 Nordics + 4 Continental squeeze). The asymmetric guard preserves institutional-pattern semantics: "Robust" is a claim about resilience to displacement-without-absorption (C3); a country that reaches C3 in *any* routine variant is not analytically robust regardless of average behaviour. Aligns with spec line 387 original expectation (5 Nordics + NL/CH; CH falls out as expected under structural-bias-corrected thresholds — Phase 3 correction working as intended). The strict-zero finding from Bundle J (no Class I under literal-strict ±0) remains preserved as structural-bias validation in methodology-notes.

## 4. Folded findings synthesis (5 paragraphs)

### (a) SE knife-edge verdict — `class_i_confidence` = MEDIUM

SE passes the (b) relative-stable rule (scens [1,1,1,1,2,2], baseline 1, max deviation 1) and retains Class I in the Phase 3 final map. Bundle H's S4b ≥ 0.20 knife-edge finding is now reframed as a **within-Class-I sensitivity band**, not a class-boundary issue: SE's S4b composite drag value sits above the 9/9 grid-load-bearing thresholds DK/FI/IS/NO clear, but does not push SE to C3 in any routine variant. Bundle K-2 added a complication: SE entered the capability-floor-breach list at 2-digit (klinger_weighted_2digit = 0.590, drag composite 0.511 — highest among breach Nordics). The breach is a Lens 5(c) signal, not a Lens 1 displacement-velocity signal, so it does not break Class I per the spec, but it raises the conditional cascade priority. **Confidence MEDIUM** captures: (1) (b) rule passes, (2) Bundle H knife-edge resolves to sensitivity band, (3) breach entry signals coordination-layer exposure under post-growth fiscal-headroom shrinkage.

### (b) Nordic post-growth annotations

Three Nordics are post_growth_empirical (NO, SE, FI); two are growth_baseline (DK, IS).

- **DK (Class I under growth_baseline)** — structural read: managed transition with growing output denominator; reinstatement mechanism (S1) intact; Mode 3 fiscal buffering credible. Cascade priority HIGH despite Class I because composite drag 0.555 is highest among breach Nordics (DK marginal breach entrant at 2-digit).
- **FI (Class I under post_growth_empirical)** — structural read: S1 mechanism structurally weaker (line 92-94); recovery path runs through S2b (Cleantech / climate Zone-C). Not in breach list (drag 0.535 below 0.55 threshold at 2-digit).
- **IS (Class I under growth_baseline)** — structural read: small open economy + breach entry (knowledge-economy ICT mass) + 2-digit confidentiality suppression caveat (36/43 codes). Cascade priority MEDIUM.
- **NO (Class I under post_growth_empirical)** — structural read: S1 weaker but sovereign-wealth fiscal headroom intact; S2b natural fit (offshore wind + maritime decarbonisation). Cascade priority HIGH.
- **SE (Class I under post_growth_empirical)** — see §4(a). Cascade priority HIGH.

Per locked spec line 108: "the same corridor assignment carries different implications depending on which regime the country occupies." Class I under post-growth (FI/NO/SE) means *robust to routine perturbation under a regime where S1 is structurally weakened* — a stronger claim than Class I under growth-baseline (DK/IS), where S1 still serves as recovery channel.

### (c) S2b-only-optimism — country count + list

**3 countries are `s2b_dependent = TRUE`**: AT, LU, TR.

For each: among the 6 routine variants, S2b is the *only* scenario that lands the country in C1; all other scenarios produce C2 or C3.

- **AT** (post_growth, Class II): scens [2,2,1,2,2,3] — S2b is sole C1 path; S4b reaches C3.
- **LU** (post_growth, Class I, breach): scens [2,2,1,2,2,2] — S2b is sole C1 path; rest stable C2.
- **TR** (growth_baseline, Class IV partial-coverage): scens [2,2,1,2,3,3] — S2b is sole C1 path; S4a/S4b reach C3.

**Other 33 countries are not `s2b_dependent`:**
- 5 Nordics + BE/FR/NL: have multiple paths to C1 (S1, S2a, S2b all = 1).
- The remaining 25 countries do not reach C1 under any routine scenario.

This is a more honest read than Bundle D's "31/36 reach C1 only under S2b" framing — under structural-bias-adjusted thresholds, only 3 countries have S2b as their *exclusive* C1 path, and only 8 countries (5 Nordics + BE/FR/NL/AT/LU/TR) reach C1 at all under any routine variant.

### (d) BE/NL squeeze-flag extension verdict — orthogonal signal CONFIRMED

Bundle K-2 Lens 5(c) test: do BE/NL show the high-coord pulse expected of squeeze-flagged countries (i.e., pattern-match the EDUCATION/ADMIN LIFT archetype LU/NO/IS, or the FINANCE/TECH DRAG archetype CH/DE)?

| Country | klinger_weighted_2digit | composite_drag_2digit | breach | archetype |
|---|---|---|---|---|
| BE | 0.580 | 0.500 | TRUE | between archetypes — moderate ICT + moderate teaching |
| NL | 0.600 | 0.478 | TRUE | between archetypes — moderate ICT + moderate teaching |
| LU (anchor) | 0.690 | 0.426 | TRUE | EDUCATION/ADMIN LIFT |
| CH (anchor) | 0.576 | 0.407 | TRUE | FINANCE/TECH DRAG (attenuates at 2-digit) |
| DE (anchor) | 0.555 | 0.554 | TRUE | FINANCE/TECH DRAG |

**Verdict: orthogonal signal CONFIRMED.** BE/NL pattern-match neither archetype cleanly — they sit between the LU lift (heavy education/admin) and the CH/DE drag (heavy ICT/finance). Their squeeze-flag profile is driven by the Mode 1 jurisdictional-buffering mechanism (high worker protection × adjacent-jurisdiction asymmetry to UK weak-protection × Mode 1 capital-flow vulnerability), which is **mechanistically independent from coordination-share displacement velocity**. Bundle J's pre-K2 finding (squeeze flag operates on capital-flight, not displacement) is corroborated at 2-digit Klinger granularity. **Action: keep BE/NL extension; orthogonal-signal classification preserved in schema.** Not an over-fit.

### (e) Capability-floor breach final scope + s5_cascade_priority

**Final breach count: 12 countries** (Bundle K-2 2-digit, unchanged for Bundle L). Trajectory: Phase 2 baseline (3) → Bundle K 1-digit (11) → Bundle K-2 2-digit (**12**, DK marginal entry).

| Country | composite_drag_2d | s5_cascade_priority | Notes |
|---|---|---|---|
| DK | 0.555 | HIGH | Marginal breach entrant; growth_baseline but highest composite drag among breach |
| DE | 0.554 | HIGH | Post-growth + squeeze + largest EU economy |
| SE | 0.511 | HIGH | Post-growth + squeeze + breach + Bundle H knife-edge |
| NO | 0.507 | HIGH | Post-growth + breach |
| BE | 0.500 | HIGH | Squeeze + Mode 1 + breach |
| UK | 0.489 | HIGH | Liberal Market + post-growth + baseline C3 |
| IE | 0.406 | HIGH | Liberal Market + baseline C3 + leprechaun-economics caveat |
| NL | 0.478 | MEDIUM | Squeeze + breach but lower drag |
| LU | 0.426 | MEDIUM | Aggregate-distributional split + breach |
| IS | 0.437 | MEDIUM | Small island + 2-digit suppression caveat |
| CH | 0.407 | MEDIUM | Post-growth but tight-band budget headroom |
| LI | 0.332 | LOW | Tiny proxied-via-CH economy |

**Cascade-priority distribution:** HIGH=7, MEDIUM=4, LOW=1 (12 breach total). Class IV countries (TR, RS, MK) are tagged `active_cascade` (already cascading per Lens 5 measurement; not breach-flagged).

## 5. Phase 3 closure summary

### What's locked

1. **Corridor thresholds:** 1.20 / 2.80 (Bundle J theory-driven, Autor 2024 + El-Sahli/Upward + Phase 1 sub-cluster boundaries).
2. **Lens 5(c) Klinger weighting:** 2-digit ESCO-weighted (Bundle K-2 supersedes K1d). Capability-floor breach 12 countries.
3. **Class I rule (operational, locked):** ±1 of baseline across S1–S4b AND no routine variant reaches C3 → 9 Class I (Q1 asymmetric-guard lock 2026-04-29). Class III/IV unchanged from Bundle J/D.
4. **Per-country scale tags:** assigned per spec line 48 (aggregate-only assignments declare matched distributional reading).
5. **Probability vectors per regime:** locked (Cooke 1991 elicitation; sentinel S2b-dominance under post-growth PASSED).
6. **S2b-dependent country list:** AT, LU, TR.
7. **BE/NL squeeze-flag extension:** orthogonal signal — not over-fit.
8. **SE class_i_confidence:** MEDIUM.

### Phase 4 open questions

1. **Class I rule final lock** — ✅ RESOLVED 2026-04-29: asymmetric-guard adopted (±1 AND no routine variant reaches C3). 7 countries reclassified I→II. Final distribution 9/9/15/3. See §3 above for the locked Class I list.
2. **Probability vectors — sensitivity bands.** Current point estimates carry 80% CIs; Phase 4 deliverable should propagate uncertainty into corridor-distribution language ("likely in C2 with 60-70% mass" rather than "expected_corridor = 2.28"). Whether to publish CIs or only point estimates is a comms-vs-rigor tradeoff.
3. **C3 sub-corridor split (Liberal Market vs CEE/Mediterranean weak-ALMP).** Bundle J surfaced as analytical-only tag; Phase 4 must decide if this is a within-corridor flag or a 4th corridor in the deliverable.
4. **Lecture/site rendering of `s2b_dependent`.** AT/LU/TR are the load-bearing "optimism path narrows to climate Zone-C" callouts; deliverable should foreground these as the single-path-fragility cluster.
5. **Breach scope policy implication.** 12 breach countries is the operational ceiling of Bundle K-2 scope; whether Phase 4 commissions a 3-digit Eurostat microdata application (resolves OC25 ICT internal heterogeneity, would re-shift scores again) or accepts 2-digit as the published granularity.
6. **Ukraine reference case integration.** Currently cited as Class IV anchor but not corridor-mapped. Phase 4 deliverable must decide whether to render as a separate panel or fold into Class IV narrative section.

### Verification (all PASSED)

| # | Check | Result |
|---|---|---|
| 1 | S2b dominance under post-growth | ✅ P(S2b\|p)=0.30 > all others |
| 2 | Probabilities sum to 1.0 across 6 routine variants per regime | ✅ all 3 regimes |
| 3 | 5 Nordics Class I under (b) + K-2 | ✅ DK/FI/IS/NO/SE |
| 4 | PL Class III preserved | ✅ |
| 5 | TR/RS/MK Class IV preserved; BA Class II preserved | ✅ |
| 6 | No country has expected_corridor > 3 | ✅ max=2.55 |
| 7 | All 36 rows have scale_tag | ✅ |

### What ships to Phase 4

- **`layer-6-phase3-scenario-probability.csv`** — 36 rows × 26 columns (deliverable-ready).
- **`layer-6-phase3-scenario-probability.json`** — same data + metadata block (probability vectors, methodology anchors, sentinel-test results, class-distribution comparison).
- **This file** — Phase 3 closure documentation.

### What does NOT ship from Phase 3 (deferred to Phase 4 master session)

- Site/document deliverable scoping (per handover: "Do NOT touch deliverable scoping in this bundle").
- 4th-corridor adjudication (data-driven 1.20/3.00 vs theory-driven 1.20/2.80 vs split 1.20/2.80/3.00).
- C3 sub-corridor formalisation.
- Class I rule final lock (literal vs asymmetric — see Phase 4 question 1).
- 3-digit Klinger microdata application.

---

_End findings — outputs in `layer-6-phase3-scenario-probability.csv/.json`. Phase 3 closed; Phase 4 (deliverable build) opens with the questions above._
