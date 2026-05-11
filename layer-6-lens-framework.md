# Layer 6: Synthesis — Lens Framework

_Working document. Communication structure (Minto/message map) deliberately deferred until lenses have been run and findings emerge._

---

## Locked Decisions (2026-04-29 scoping session)

**Output format:** Document + site. Document anchors analysis; site renders corridor map per scenario toggle plus 5-trajectory sparkline per country as headline visual.

**Lenses (final):**
1. **Lens 1 — Displacement Velocity × Absorption Capacity** (worker / occupation-level, single jurisdiction)
2. **Lens 2 — Demographic Buffer or Accelerant**
3. **Lens 3 — _folded into Lens 1 as Perez compression footnote_** (decision: did not earn standalone status; macro-level framing only, no country differentiation)
4. **Lens 4 — Compounding Shocks Exposure** (worker-level shock combination + jurisdictional buffering asymmetry)
5. **Lens 5 — Polycrisis Drag** _(NEW)_ — institutional-level concurrent-crisis bandwidth competition. Working name: "Multidimensional Chess to the Square Root."

**Country scope:** **36 countries** (locked 2026-04-29 after Phase 1 review):
- EU-27 (27)
- EEA non-EU: NO, IS, LI (3) — LI carried with proxy-data flag
- CH (1)
- UK (1)
- **Candidates: BA, MK, RS, TR (4)** — present in L1 data; Lens 1 only + Lens 5 reference case (no L2/L4/L5 coverage); flagged "candidate-status partial-coverage"

**Ukraine added as Lens 5 reference case** (analytical narrative only, alongside the 4 candidates as the worst-case reference; not in corridor map).

The original "36" claim was correct; Phase 1 inadvertently dropped the 4 candidates and produced 32. Phase 1 outputs to be regenerated with candidates added (Bundle B).

**Scenario stack** (pre-Bundle V, preserved for historical record): 5 scenarios with discipline rule (one load-bearing mechanism per scenario):
1. **Reinstatement Revival** — augmentation effects strengthen; new-work creation reverts to *or exceeds* historical base rate
2. **Climate Adaptation Boom** — Zone C demand surge from climate adaptation absorbs displaced Zone A workers
   - 2a: transition with current wage cliff (−25% to −40%)
   - 2b: transition wage-neutral or wage-positive (climate-Zone-C commands premium)
3. **Muddle Through** — current parameters persist; baseline (renamed from "Trajectory Continuation" — "trajectory" is a trigger word and applies to all scenarios)
4. **Structural Bias Compounds**
   - 4a: reinstatement weakens, institutional bandwidth holds
   - 4b: reinstatement holds, institutional bandwidth fractures
5. **Cascading Institutional Failure** — concurrent crises saturate bandwidth; capability floor breached; reskilling capacity overrun. Empirical anchor: Ukraine.

> **Bundle V update (2026-04-30):** Scenario stack expanded from 5 with subversions to 8 linear codes S1–S8. Old S2a (Wage Cliff) split into S5 (Wage Cliff, mid-skill compression) + S3 NEW (Jobs Transform, within-occupation reshape). Renumbering map: S1→S1, S2b→S2, NEW→S3, old-S3→S4, S2a→S5, S4a→S6, S4b→S7, S5_cascade→S8. See Scenario Stack section below for the canonical definition.

**Corridors (target after consolidation):** 3 corridors + fragility class + scale tag, not 5. Validation test runs against L1–L5 data; corridors that fail the test are cut.

**Fragility classes (per country, across scenario stack):**
- **Class I — Robust (relative-stable, C3-guarded):** corridor stays **within ±1 of baseline** across the seven routine-perturbation variants (S1, S2, S3, S4, S5, S6, S7) **AND no routine variant assigns the country to C3** (the displacement-without-absorption corridor). Cascade behaviour under S8 reported separately as `cascade_corridor` and is **orthogonal** to Class I status — parallel to the III/IV observability rule (Class IV is a *measurement* of cascade-already-happening, not a forecast under a cascade *scenario*). [**Amended/clarified three times in 2026-04-29 Phase 2/Phase 3.** Stage 1 (Phase 2): original spec said "stable across all 5 scenarios"; S5 by construction breaks corridors for nearly all countries, making it degenerate — restricted scope to S1–S4b. Stage 2 (Phase 3 Bundle J): under structural-bias-corrected thresholds (C1 < 1.20, C3 ≥ 2.80), strict-stable Class I = 0 because the tightened C1 cap means S4a velocity multiplier exits C1 even for Nordics. Relaxed to relative-stable (±1 of baseline) — the strict-zero finding preserved as **structural-bias validation** in methodology-notes: even spec-anchor countries fail strict robustness under tight C1, exactly as the structural-bias warning predicted. Stage 3 (Phase 3 Bundle L clarification): mechanical application of Stage 2's ±1 rule produced 16 Class I including 7 C2-baseline countries (CH/DE/LI/BG/ES/LV/RO) whose perturbation paths touch C3 — semantically inconsistent with "Robust." C3-guard added: a country whose routine-variant path includes C3 cannot be Class I regardless of ±1 spread. Final Class I count: 9 (5 Nordics + 4 Continental squeeze BE/FR/NL/LU); aligns more closely with original spec line 387 expectation (5 Nordics + NL/CH; CH falls out because Phase 3 thresholds correctly surface its C3 path under perturbation — that's the structural-bias correction working as intended).]
- **Class II — Fragile:** corridor swings by **>±1 of baseline** across routine-perturbation variants (i.e., spans 3+ corridors)
- **Class III — Pre-Failure Risk:** under Muddle Through (S4), lands in Corridor 3; recovery possible only if S1 (Reinstatement Revival), S2 (Climate Adaptation Boom), or S3 (Jobs Transform) realises [2026-04-29: original "Corridor 5" was leftover from pre-consolidation 5-corridor scheme; consolidated to 3. 2026-04-30 Bundle V: S3 Jobs Transform added as third recovery path]
- **Class IV — Currently Failing:** Lens 5 inputs already at maxima; cascade is happening *now* (measured), not predicted (forecasted). Recovery requires regime change, not scenario realisation. Anchors: Ukraine (contemporary); Copperbelt 1991–2001 (−66% ZCCM employment), São Paulo ABC 1989–1999 (−48% industrial jobs), Latrobe Valley (+0.8pp SA4 unemployment gap, persistent 30+ years) as historical analogues.

**Scale tags (per corridor assignment):** aggregate / distributional / both. Required field. Aggregate-only assignments must declare matched distributional reading.

**Tooze framing note:** "Polycrisis Drag" uses the term "polycrisis" despite Adam Tooze stepping back from it as a general descriptor in [Chartbook 407 (Sep 2025)](https://adamtooze.substack.com/p/chartbook-407-polycrisis-revisited). Tooze 2022 framing was structural-impersonal (feedback loops, amplification, unboundedness); Tooze 2025 pivoted to personal-agency framing (Trump, Netanyahu, MAGA as named actors). Lens 5's mechanism is institutional-mechanical (concurrent crises consume the same finite institutional response budget) — different scale of analysis from either Tooze framing. We use the term, not his mechanism. Methodology section states this distinction explicitly.

**L3 read pattern:** L6 reads `european-disruptions-map/site/disruptions-data.json` directly (the structured truth). L3 render gap was closed by Track 1 fix session 2026-04-29; v0.2 quality fixes pending (Bundle A) before L3 site can be cited as canonical render.

**Structural-bias re-calibration (Q5 lock):** Apply once in Phase 3, after Lens 4 + Lens 5 + scenario stack outputs exist. Phase 2 keeps the warning as a calibration note only. Single re-scoring pass avoids compounding adjustments. PL at 2.96 is the sentinel test case — must shift to C3 under re-calibration or methodology is wrong.

---

## Regime Stability Note (added 2026-04-29) — The Growth Assumption Is Itself Contested

All scenarios in this framework (post-Bundle V: S1–S8) assume a **base regime continuation**: classical labour-economics machinery (Autor reinstatement, Card/Kluve/Weber ALMP effectiveness, S1 Reinstatement Revival) all assume an *expanding output denominator*. Displaced workers find new work because the economy is growing. This assumption is contested.

**Empirical anchor for the post-growth question:**
- EU real GDP growth: ~1.4% average 2010–2024 (Eurostat)
- Japan: ~0% aggregate, ~0.7% per-capita 1990–2024 — empirically in post-growth regime by data
- Italy: real per-capita GDP roughly flat since 1999
- Germany: −0.3% real growth 2024; secular trend below 1% post-2008

The growth assumption may already be empirically wrong for large parts of Europe. **This is a structural-bias compounder beyond the Autor 2024 / El-Sahli/Upward warnings already in the framework.**

### Three definitions of "post-growth" (do not conflate)

| Tradition | Claim type | Use in this framework |
|---|---|---|
| **Secular stagnation** (Gordon, Summers, Eichengreen) | Empirical — growth structurally slow due to demographic + productivity reasons | **Yes — analytical input** |
| **Normative degrowth** (Jackson, Hickel, Kallis) | Normative — growth *should* be abandoned for ecological reasons | **No — out of scope (values claim)** |
| **Post-Keynesian regime shift** (Mazzucato, Susskind) | Transitional — growth is reorganising via AI/sustainability transition; different growth, not no growth | **No — possibility, not baseline** |

For Layer 6 analytical machinery, only **secular stagnation (empirical)** belongs. Normative degrowth is a different document. Post-Keynesian transition is a possibility, not a baseline.

### Threshold (locked 2026-04-29)

**Two-tier classification per country, 10-year sustained average:**
- **Soft (warning) threshold:** real GDP growth <1.5% aggregate sustained → "secular stagnation territory" (matches academic mainstream: Summers/Gordon/IMF/ECB/OECD)
- **Hard (post-growth) threshold:** real per-capita GDP growth <1.0% sustained → "post-growth empirically" (matches conservative anchor; Japan reference 0.7% per-capita 1990–2024)

Per-capita preferred for the hard threshold because aggregate growth includes demographic effects and demographic shrinkage is already in Lens 2 / Lens 5(b). Per-capita isolates the labour-economics question.

### Per-scenario implications under post-growth regime

The two regimes (growth-baseline vs post-growth) reshape every scenario's mechanism. This is the load-bearing comparison (S1–S8 spectrum order, post-Bundle V):

| Scenario | Under Growth-Baseline Regime | Under Post-Growth Regime |
|---|---|---|
| **S1. Reinstatement Revival** | Augmentation effects strengthen; new-work creation reverts to *or exceeds* historical base rate | Mechanism *requires* growing output for new-work creation; **structurally weaker; probability shrinks**. Reinstatement under flat aggregate is mathematically constrained |
| **S2. Climate Adaptation Boom (Zone-C, wage-positive)** | Climate Zone-C work commands premium; cross-zone transition rate ~12–15%; wage-neutral or wage-positive | **Strengthens — the only sectoral-redirection scenario that doesn't depend on output expansion.** New sectoral demand absorbs displaced workers |
| **S3. Jobs Transform** *(NEW, Bundle V)* | Within-occupation reshape; AI substitutes for routine sub-tasks; wages stable or up; seniority-tier compression (Nielsen forklift, T31). Empirical anchors: Brynjolfsson OpenAI RCT, BCG +40%/-19pp (Dell'Acqua), ATM/Spreadsheets historical | Viable in flat aggregate — mechanism is *within*-occupation, not cross-occupation. Bounded by within-firm transition infrastructure + human-capital intensity. **Subordinate to S2 in post-growth** because steady-state occupation reshape doesn't generate the new sectoral demand S2 supplies |
| **S4. Muddle Through** | Current parameters persist; baseline | Same — no change |
| **S5. Wage Cliff** | Mid-skill wage compression; AI substitutes for mid-skill labour; transition at current −25% to −40% wage cliff. Bounded by Layer 5 reality | Sectoral redirection logic still operates; wage compression load-bearing finding holds — **moderate-to-high probability under stress regimes** |
| **S6. Reinstatement Failure** *(was 4a)* | Autor 2024 trend continues; bandwidth holds | Worsens — buffer institutions need growth-dependent fiscal capacity. Mode 3 (income-floor) buffering hardest hit |
| **S7. Bandwidth Fracture** *(was 4b)* | Lens 5 dominates; reinstatement intact | Worsens — fiscal headroom for institutions shrinks under post-growth; bandwidth-saturation arrives faster |
| **S8. Polycrisis Drag** *(conditional, orthogonal)* | Concurrent crises saturate bandwidth; capability floor breached | **More likely** — institutional response capacity has lower fiscal headroom; threshold to cascade is lower |

### The load-bearing finding this surfaces

**Under post-growth regime, Climate Adaptation Boom (S2) becomes the modal genuinely-positive scenario.** Reinstatement Revival (S1) relies on growth-dependent new-work creation. S2 is sectoral redirection — works whether the aggregate economy grows or not. Jobs Transform (S3) is viable but subordinate to S2 in post-growth because within-occupation reshape doesn't produce new sectoral demand.

Probability re-score (Bundle V, 2026-04-30) preserves: **P(S2 | post_growth) = 0.30 ≥ P(S4 | post_growth) = 0.22** (S2 modal); S5 (Wage Cliff) holds 0.13–0.15 across stress regimes; S8 cascade conditional 0.05/0.10/0.15 unchanged. See `layer-6-deliverable-data.json` `scenarios.*` and `metadata.bundle_v_scenario_reframe`.

**Policy implication:** if Europe is in post-growth regime, the dominant optimistic path is *aggressive climate-adaptation Zone C investment with wage premiums sufficient to draw Zone A workers across* (S2). The secondary optimistic path is *within-firm transition infrastructure that lets occupations reshape under stable wages* (S3). Anything less defaults to S4 Muddle Through or S5–S7 pessimistic.

**Country implication:** the regime check splits the 36 countries into two interpretive groups. Countries above the soft threshold (1.5% real GDP) read scenarios under growth-baseline. Countries below the hard threshold (1.0% per-capita) read scenarios under post-growth. The same corridor assignment carries different implications depending on which regime the country occupies.

### Empirical anchors (Bundle E partial, 2026-04-29)

Bundle E Task 10 produced 36/36 country regime classification (32 H, 3 M, 1 L confidence). Notable readings:

- **Germany: 1.02% aggregate / 0.54% per-capita → both flags true (secular stagnation AND post-growth empirical).** Europe's largest economy is empirically in post-growth regime. Scenario 1 (Reinstatement Revival) becomes structurally weaker for the country anchoring EU industrial-policy assumptions; Scenario 2b becomes the only genuinely-positive path for DE. Compounds with Lens 5 jurisdictional-buffering-squeeze hypothesis (DE has weak post-growth fiscal headroom AND high adjacent-jurisdiction asymmetry exposure to US/UK weaker buffering).
- **Italy: 1.04% aggregate / 1.30% per-capita → stagnation only (demographic decline saves per-capita).** Aggregate is post-growth; per-capita above hard threshold because population shrinkage is doing the work. Lens 2 demographic load × Lens 5(b) demographic load interact directly — IT's per-capita "OK" reading is a denominator effect, not productivity recovery.
- **UK: 1.67% aggregate / 0.87% per-capita → post-growth only.** Above 1.5% aggregate but per-capita under threshold. (Eurostat truncates UK at 2019 post-Brexit; uses WB WDI fallback.)
- **Luxembourg: 1.94% aggregate / −0.12% per-capita → aggregate-distributional split.** Aggregate growth driven entirely by immigration flow; no productivity or real-wage progress for residents. Cleanest empirical anchor for the aggregate-vs-distributional scale axis (`docs/CONCEPT-BRIDGES.md`) yet observed in this dataset. Per-capita is the load-bearing reading for labour economics; treat LU as `aggregate_distributional_split` flag, not `growth_baseline`.
- **Ireland: 8.1% aggregate / 6.15% per-capita → leprechaun-economics artefact.** 2015 corporate-tax-domicile reclassification (Apple, Google IP relocations) drove +24.6% real-growth single-year reading; inflates 10-year aggregate. **Use modified GNI\* (CSO Ireland series) for IE regime classification** — domestic-economy reading is roughly 2–3%, not 8.1%. Without this fix, IE incorrectly reads as robust-growth-baseline.
- **Poland: 3.72% / 3.81% → robust growth-baseline.** Cleanest CEE growth-baseline reading.
- **Nordic cluster (DK, NO, SE, FI, IS):** all expected `growth_baseline` per regime classification (final readings pending Bundle E completion).

**The DE finding is potentially the second L6 document headline alongside the orthogonality finding** — Europe's largest economy is empirically in post-growth regime, which compounds the structural-bias warning the framework already carries.

### Post-globalization is not a new variable

Lens 5(a) polycrisis cluster already operationalises post-globalization via its decoupling input (industrial-bloc competition replacing global cooperation). The Regime Stability Note adds **post-growth** as a separate axis from post-globalization — they're related but distinct mechanisms. A country can be post-globalization without being post-growth (e.g., US under reshoring) or post-growth without being fully post-globalization (e.g., Italy).

---

## Headline Finding (Phase 1, 2026-04-29) — Demographic Buffer Thesis Empirically Refuted

The spec's own non-obvious hypothesis from Lens 2: *"If the data shows displacement and shortage are structurally orthogonal — that's arguably the single most important finding in the entire project."* **Phase 1 confirms it.**

- 32 of 32 scored countries fall in `buffer_fails`
- Maximum observed retirement offset: ~26%
- Spec threshold for buffer-holds: 80%
- Even at 50% threshold, no country qualifies — finding is robust to threshold relaxation

**Implication:** "Demographic decline rescues us from AI displacement" is empirically dead across Europe. The retirement cohort is too small relative to the displaced cohort, AND the occupation overlap between displaced workers and demographic-shortage roles is structurally weak.

**This becomes the L6 document headline, not a footnote.** All downstream lens scoring (Phase 2 onwards) treats buffer-failure as a baseline assumption rather than a hypothesis to test. Practitioner-knowledge writeup (`knowledge/practitioner/demographic-rescue-orthogonality.md`) ships post-Phase 2 if Lens 4 + 5 don't surface a country-specific buffer mechanism that re-introduces the thesis.

**Threshold sensitivity audit** documented in Phase 2 methodology: max observed offset 26% means even at half the spec threshold, no country comes close. The finding is not a calibration artefact.

**Caveat — overlap score is coarse proxy:** Phase 1's `lens2_overlap_score` shows only 3 distinct values (0.2 / 0.25 / 0.4), assigned by system-model tier rather than country-specific occupation × age × shortage-sector data. The orthogonality finding does NOT depend on overlap precision — it depends on the retirement-offset ceiling. Even if every country had perfect overlap, the cohort-size mismatch alone breaks the buffer thesis. This robustness is documented; do not soften the finding.

---

## SCQA Entry Point (stable)

**Situation:** AI is the first general-purpose technology to hit virtually every occupation group simultaneously, arriving into a European labor market already contracting from demographic decline.

**Complication:** Unlike prior disruptions — which were sector-specific and absorbed over decades — AI displacement is broad, fast, and compounding with at least three other structural forces. Europe's institutional response architecture was built for single-sector, slow-moving shocks.

**Question:** Under which conditions does AI-driven displacement outpace Europe's capacity to absorb it — and which countries and occupation groups enter which scenario corridor?

**Answer:** _Deferred. Let the lenses produce findings first. Do not pre-fit to a triad or any other count._

---

## Lens 1: Displacement Velocity × Absorption Capacity

### What it asks
For a given country or occupation cluster: how fast does AI displace, and how fast can the system absorb displaced workers? The *ratio* between these two rates is the primary diagnostic variable.

### Feeds from
- **Layer 1** (AI exposure scores) → displacement potential per ISCO 3-digit group
- **Layer 2** (current European job market) → current labor market slack, vacancy rates, sectoral demand
- **Layer 3** (historic disruptions) → empirical displacement speed benchmarks from prior GPTs
- **Layer 5** (reskilling feasibility) → absorption rate ceiling (~10–20% meaningful reskilling within 5 years)

### Institutional readiness as sub-dimension
Absorption capacity is not just labor market mechanics — it includes institutional response speed (policy, regulation, retraining infrastructure). This is diagnostic, not prescriptive: how *prepared* is the system now, not what it *should* do.

Calibration from Layer 3: what was the typical institutional response lag in prior disruptions (years between first displacement and first meaningful policy response)?

### Coverage gap as scope constraint
Lens 1 measures absorption capacity for workers inside the institutional perimeter. For workers outside that perimeter (freelance, platform-based, cross-border remote), the gap is not "low capacity" but **visible-but-uninterpretable** — data exists in tax and platform records, but the institutional reading capacity to interpret it as displacement does not. This decomposes into two bottlenecks with different closure timelines:

- **Categorisation bottleneck** (closes ~2030): legislation + platform reporting mandates via EU Platform Work Directive and national transposition. Tax records start distinguishing "thriving self-employed IT services" from "displaced self-employed IT services."
- **Event trigger bottleneck** (closes ~2040+): no administrative moment fires when a freelancer stops getting contract renewals. Requires new infrastructure + platform disclosure + cross-jurisdictional cooperation.

Layer 6 treats these as separate inputs to Lens 1, not bundled under "coverage gap reduces." Historical precedent (pre-Bismarck 1760–1880): coverage gaps close through institutional invention, not extension. But compression (~4–5x vs Bismarck baseline, see Lens 3) implies shorter closure than historical precedent alone suggests.

### Sub-role task displacement: separate measurement category
Sub-role task displacement (employed workers whose task mix has hollowed while their employment status has not changed) is invisible to employment-granularity measurement. A software engineer reviewing AI-generated code instead of writing it is 100% employed in statistics while doing perhaps 60% of the 2024 value-add. No institutional sensor fires because no role-level event exists.

This is distinct from the freelance/platform coverage gap — it is invisibility *inside* the institutional perimeter, not outside it. Lens 1 measured at employment granularity is systematically late for this displacement category. Design implication: leading-indicator measurement at task level (productivity per worker, hiring intensity against output, wage stagnation within preserved roles) with stated lag to employment-level effects. The task→employment lag retrofit in Layer 3 (containers, ATMs, CAD, DTP) is the empirical foundation for specifying that lag — and since lag varies ~10x across historical cases, it is almost certainly a parametric function of capital intensity × skill specificity × institutional buffering × task substitutability, not a constant.

### Key analytical questions
- At what displacement-to-absorption ratio do historical disruptions produce structural unemployment vs. managed transition?
- Which ISCO groups and countries sit above that threshold under current AI adoption trajectories?
- Does the EU AI Act materially change absorption capacity, or is it regulatory theater relative to displacement speed?

### What a finding might look like
_"In X of 36 countries, projected displacement velocity exceeds demonstrated absorption capacity by >Nx, placing them in [corridor]. Only Y countries show absorption infrastructure capable of matching displacement speed at current trajectories."_

### Schema additions (Bundle Q + Bundle R, 2026-04-30)

Two per-country sub-fields formalise the absorption-capacity reading and resolve the Phase 2 "asymmetry score is too tight to differentiate" critique:

- `lens1_a_to_c_transition_rate_pct` — keyed off `_system_p1` institutional cluster. Schema:
  ```
  {
    band_low_pct, band_high_pct, central_derived_pct,
    system_p1_match, delta_central_vs_mid_pp, source_alignment,
    country_specific (bool), reform_velocity_composite_0_10,
    reform_velocity_decomposition: { veto_player_factor_0_5, recent_reform_factor_0_5, rationale },
    time_to_first_graduate_yr (DACH), public_cost_per_transition_eur_k (DACH),
    dach_time_cost_note,
    _provenance: { source_layer: "L5", source_data: [...], bundle: "R" }
  }
  ```
  System-level central derived rates (Bertheau IZA DP 15033 anchor, plus reform-velocity composite for country-specific resolution): Nordic flexicurity 9.9 % derived (8–12 % headline band); Continental Corporatist 6.9 % (5–8 %); Germanic Dual 7.9 % derived against 3–6 % headline (Δ = +3.4pp; reform-velocity composite is country-specific — DE rv=5, AT rv=3, CH rv=1); Liberal Market 3.2 % derived against 5–8 % headline (Δ = −3.3pp — derived is canonical); Southern European 4.8 %; Central/Eastern European 3.3 %; candidate-baseline 3.5 %.
- `lens1_regulated_absorption_pct` — country-specific regulated-absorption-friction score derived from Layer 1 EU vs UK regulatory dual-scoring. Range 0.46 (BA) to 0.68 (IS). Schema: `float`. Provenance: `{ source_layer: "L1", source_data: "scores.json + uk_scores.json + site/data.json", bundle: "Q" }`. Stronger per-country differentiator than the squeeze-flag asymmetry score (range 0.6333–0.6650, span 0.0317).

Per Bundle Q, top-level `cross_cutting_findings.regulatory_asymmetry` carries the cross-country narrative: the eight squeeze-flagged Lens 4 countries sit at the top of the regulated-absorption-friction distribution — high-exposure occupations are also the most regulated, compounding the squeeze the binary flag identifies.

### Schema addition (Bundle X, 2026-04-30) — `cross_cutting_findings.pan_european_aggregate`

Per Bundle X, top-level `cross_cutting_findings.pan_european_aggregate` carries the pan-European read in two parallel sub-blocks: `eu_27` (the EU as political entity) and `european_36` (full Layer 6 scope — EU-27 + EFTA-4 + UK + 4 candidates). Both sub-blocks expose the same fields: `weighted_lens1_ratio`, `headline_corridor` + `headline_corridor_distribution` (count + population-weighted percentage), `class_distribution` (count + population-weighted percentage), `regime_mix` (count + population-weighted percentage), `weighted_scenario_probability` (S1–S8 [low, mid, high] vectors), `modal_scenario_under_post_growth_subset`, `capability_floor_breach_count` + subset list, `squeeze_cluster_count` + subset list, plus `country_population_weights` (per-country working-age 2024 weight share) and `_provenance`. Weighting uses UN PPP2024 working-age (20–64) population, 2024 baseline, median variant — covers all 36 markets consistently, avoiding country-count fallback. **Variation guard mandatory:** every aggregate scalar surfaces alongside the distribution it summarises (corridor + class + regime distributions). A standalone aggregate corridor figure dilutes the structural-bias finding; the 36-market variation IS the analytical surface. Phase 1B `europe.html` reads from this block; Bundle W reframes deliverable docs around it.

---

## Lens 2: Demographic Buffer or Accelerant

### What it asks
Does Europe's demographic decline offset AI displacement (fewer workers needed anyway) or compound it (displaced workers are the wrong workers for the gaps)?

### Feeds from
- **Layer 4** (European demographics) → 8–12M Zone C workforce gap by 2030, country-level age structure
- **Layer 1** (AI exposure) → which occupation groups face displacement
- **Layer 2** (current market) → where shortages already exist

### Key analytical questions
- Is there meaningful overlap between AI-displaced occupation groups and demographic-shortage occupation groups? Or is the mismatch structural?
- Country-level: where does demographic decline create genuine absorption space for AI-displaced workers, and where does it just mean two simultaneous crises?
- Does the "demographic rescue" narrative hold empirically for any country, or is it a comforting fiction?

### The non-obvious hypothesis to test
The default assumption is that demographic decline softens AI's blow. If the data shows this is wrong — that displacement and shortage are structurally orthogonal — that's arguably the single most important finding in the entire project.

### What a finding might look like
_"In X of 36 countries, >Y% of AI-displaced workers are in occupation groups with no structural pathway to demographic-shortage roles. The demographic buffer thesis holds only in Z countries where [specific conditions]."_

---

## Lens 3: Perez Phase Positioning (Framing Lens)

### What it asks
Where is AI on the installation→deployment curve, and has the institutional "turning point" crisis happened yet?

### Important constraint
This lens operates at macro level. It does not differentiate countries or occupation groups. Its function is **temporal framing** — preventing Lenses 1, 2, and 4 from being read as static snapshots. It tells you where we are in the cycle, not who gets hit.

### Feeds from
- **Layer 3** (historic disruptions) → pattern-matching prior GPTs to Perez's five revolutions
- External: Perez's own framework (installation: irruption → frenzy → bubble → crash → turning point → deployment: synergy → maturity)

### Key analytical questions
- Is AI still in the frenzy/bubble phase of installation? If so, the institutional reset that enables broad-based deployment hasn't happened yet — and current policy inadequacy is *expected* within the model, not an anomaly.
- What would the "turning point" look like for AI? Financial crisis? Regulatory crisis? Political crisis triggered by displacement?
- Does the Perez model predict a deployment phase that *eventually* produces broad prosperity — and if so, how long is "eventually" relative to the demographic timeline from Lens 2?

### Honest limitation
Perez gives you narrative coherence and temporal orientation. It does not give you numbers, country-level differentiation, or falsifiable predictions. If this lens doesn't earn its place by genuinely reframing what the other lenses show, cut it. Don't keep it for intellectual decoration.

### Calibration footnote: phase duration compression
Perez's original cycle durations were calibrated to pre-acceleration institutional response baselines. Institutional response has compressed ~4–5x since Bismarck (Platform Work Directive 2024 arrived ~9–11 years after platform displacement became politically visible, vs ~40–50 years for Bismarck social insurance after industrial displacement became visible). Compression decomposes into ~2–3x faster political/information cycles (pessimistic: institutions getting yelled at sooner) + ~1.5–2x genuine template-response capacity built over a century of labour law (optimistic: institutions have adaptable templates to extend). Both mechanisms are real. Implication: Perez phase durations for the AI cycle should be scaled ~4–5x shorter than the historical baseline — but don't treat this as a clean multiplier. The compression is itself uncertain, and dominant mechanism (political vs template) is debated.

### What a finding might look like
_"Perez's model suggests we are in [phase], which historically precedes [event]. This implies current institutional responses are pre-turning-point and structurally insufficient — not because policymakers are incompetent, but because the institutional reset hasn't been triggered yet. The critical question is whether the turning point arrives before or after demographic decline hits its steepest gradient (Layer 4: [year range])."_

---

## Lens 4: Compounding Shocks Exposure

### What it asks
AI displacement is not arriving in isolation. Climate transition, wealth concentration, geopolitical fragmentation, and pandemic risk interact with it. Under which combinations do outcomes change category, not just degree?

### Feeds from
- All prior layers as baseline
- External: climate transition job displacement projections, inequality data, geopolitical risk indicators

### Key analytical questions
- Which countries face 2+ simultaneous structural shocks (AI displacement + green transition + demographic decline)? Are there countries facing 3+?
- Is there a compounding threshold where the interaction between shocks changes the outcome qualitatively (i.e., not "worse version of the same corridor" but "different corridor entirely")?
- Which shock combinations are most dangerous? Hypothesis: AI displacement + wealth concentration is more dangerous than AI displacement + climate transition, because the latter creates new jobs while the former reduces demand.

### The novel contribution
Most AI-and-labor research treats AI as an isolated variable. Your differentiation is explicitly modeling the interaction effects. If this lens doesn't produce findings that change the corridor assignment from what Lenses 1+2 alone would produce, it's not doing enough work.

### What a finding might look like
_"X countries that appear in the 'managed transition' corridor under Lenses 1+2 shift to 'displacement without absorption' when compounding shocks are modeled. The primary driver is [specific interaction]. Conversely, Y countries appear more resilient than single-lens analysis suggests because [reason]."_

### Jurisdictional-buffering asymmetry as a compounding-shock generator (2026-04-14, Retrofit v0.3 Case 1 finding)

The retrofit v0.3 produced a finding that belongs directly in Lens 4 rather than in Lens 1 or 2: **asymmetric institutional buffering across jurisdictions is itself a compounding-shock generator**, not merely a mitigation.

Historical precedent (UK containerisation, 1968–1970): TGWU's 27-month container ban at Tilbury (strong worker protection inside the NDLS perimeter) did not slow containerisation — it rerouted $60M of capital investment to Rotterdam's European Container Terminus, and allowed Felixstowe (TGWU-uncovered) to rise from zero to 9th-largest containerport globally in 3 years. By 1975 London had been overtaken by Antwerp, Hamburg, and Le Havre (*Fairplay* magazine). Mode 1 buffering protected the incumbent worker inside the perimeter; the UK regional economy lost the capital investment to jurisdictional competitors.

**Direct AI/EU application:** If the EU imposes strong AI-era worker protection and the US/UK do not, AI capital deployment is likely to relocate to US/UK firms and jurisdictions, not slow globally. Incumbent EU workers inside the protection perimeter experience Mode 1 benefits; the EU regional economy experiences the Rotterdam/Felixstowe outcome at continental scale — loss of AI capital formation to competitors. Historical Mode 1 record shows the worker-level benefit real; the regional-economy outcome potentially catastrophic on a 10–15 year horizon.

**Why this belongs in Lens 4, not Lens 1:**
- Lens 1 measures displacement velocity within a jurisdiction
- Lens 4 measures how shocks combine across dimensions

Jurisdictional-buffering asymmetry combines AI displacement exposure with jurisdictional-competition pressure. Under symmetric buffering, both dimensions are held. Under asymmetric buffering (e.g., EU strong / US weak), the protected jurisdiction faces displacement compounded by capital-outflow risk. This is a category shift, not a degree shift — Corridor 1 (managed transition) countries may appear in Lens 1+2 analysis but reclassify to a new "jurisdictional-buffering squeeze" pattern under Lens 4.

**Scoping question for Lens 4 output:** for each of the 36 countries, score (a) AI worker-protection stance (strong/weak), (b) adjacent-jurisdiction-asymmetry exposure (dependency on capital/labour flows to less-protected jurisdictions), (c) Mode 1 regional-economy vulnerability. Countries scoring high on (a) AND high on (b) AND high on (c) are candidates for the jurisdictional-buffering-squeeze category. Specifically flag: Germany (strong Mode 3 buffering tradition + adjacent UK/US asymmetry + high-value manufacturing export dependence), France (similar profile, smaller buffer), Nordics (strong protection + small-open-economy vulnerability).

This finding partially undermines the "EU institutional advantage" narrative that has been assumed in prior Layer 6 corridor calibration. The advantage is real for incumbent workers but conditional at the regional-economy level — needs to be scoped explicitly before use.

— Synthesis: Levinson (2016) × El-Sahli & Upward (BJIR 2017) via retrofit v0.3 Case 1.

---

## Lens 5: Polycrisis Drag (NEW — 2026-04-29)

### What it asks
When AI labour disruption arrives into a world with 5–7 concurrent civilizational-scale crises consuming the same finite institutional response budget, does response capacity for AI displacement saturate, fracture, or hold? This is a different question from Lens 4 (which asks how shocks combine *for the worker*). Lens 5 asks how concurrent crises compete *for institutional response bandwidth*.

### Mechanism (and why it's distinct from Tooze)
Tooze's 2022 polycrisis framing addresses **structural-impersonal feedback loops** between crises (escalatory interaction, amplification, unboundedness — see [Chartbook 130](https://adamtooze.substack.com/p/chartbook-130-defining-polycrisis)). His 2025 pivot in [Chartbook 407](https://adamtooze.substack.com/p/chartbook-407-polycrisis-revisited) addresses **personal-agency** framing (named actors as the analytical unit). Neither addresses institutional response *capacity* as a binding constraint. Lens 5's mechanism — concurrent crises consume the same finite institutional response budget — is institutional-mechanical, a third scale of analysis. We use the label "polycrisis" because the concurrent-crisis framing is established; we do NOT inherit Tooze's mechanism and state this distinction explicitly in methodology.

### Inputs (4)

**(a) Polycrisis cluster** — one compound force, not three:
- Decoupling / de-globalization (industrial-bloc competition replaces global cooperation)
- Multi-front sub-threshold conflict (kinetic + economic + cyber + space; "World War 3 looks different")
- Climate fragmentation (climate as policy-bloc battleground, not cooperation domain)

These are causally linked (decoupling drives multi-front conflict by removing economic interdependence as deterrent; multi-front conflict drives further decoupling via sanctions architecture; both replace global climate cooperation with bloc-level industrial policy). Treating them as one cluster is more honest about the generator function.

Per-country score: SIPRI 2025 military-expenditure %GDP; NATO Hague 5%-by-2035 trajectory exposure; ReArm Europe national escape clause activation; trade-policy decoupling exposure (export controls + sanctions architecture).

**(b) Demographic load** — Layer 4 working-age population shrinkage rate per country, dependency ratio shift, retirement-cohort size relative to entrant cohort.

**(c) AI labour load** — Layer 1 exposure score per country × ISCO group, modulated by Klinger coordination-share weighting and Gostev capability floor (~9% Q1 2026 sensitivity bound).

**(d) Net climate position** (signed score per country) — adaptation capacity − physical vulnerability:

```
Physical Vulnerability = wildfire risk + drought severity + flooding exposure
                       + heat-stress on outdoor work + agricultural disruption
                       + infrastructure stress

Adaptation Capacity   = climate-adaptation budget allocation
                       + workforce trainable for Zone C climate work
                       + existing Zone C labour market depth (from L5)
                       + institutional speed (planning permission, public works)
```

Three country categories:

| Category | Countries (preliminary) | Lens 5 implication |
|---|---|---|
| **Net positive** | DK, NO, FI, SE, CH, NL, EE | Climate generates Zone C demand faster than displacement; partial offset to AI labour load |
| **Net neutral** | DE, AT, FR, BE, IE, UK, LU, IS | Climate is a wash |
| **Net negative — capacity-side** (Eastern + Baltic) | LV, LT, PL, CZ, SK, HU, RO, BG, HR, SI | Vulnerability medium, adaptation budgets constrained. Baltics: Russian-border polycrisis exposure compounds — worst-case Lens 5 readings in EU-27 |
| **Net negative — vulnerability-side** (Mediterranean) | ES, PT, IT, GR, MT, CY | High vulnerability outpacing capacity. Spain 2025: 400,000 hectares burned, 5x annual average ([Munich Re 2025](https://www.munichre.com/en/company/media-relations/media-information-and-corporate-news/media-information/2026/natural-disaster-figures-2025.html)) |

Country categorisation is preliminary; final weights pending Phase 2 scoring with Cedefop 2025 country reports + EEA EUCRA 2024 + Munich Re country breakdowns.

### Ukraine reference case
Not in 36-country corridor scope (would require backporting Layer 1 / 4 / 5 data — 2–3 weeks). Used as analytical anchor for Class IV "Currently Failing" — empirically the worst Lens 5 reading available (military expenditure 40% GDP per [SIPRI 2025](https://www.sipri.org/publications/2026/sipri-fact-sheets/trends-world-military-expenditure-2025); demographic collapse from refugee outflow + casualties; reskilling infrastructure war-damaged). Cited; not corridor-mapped.

### Sources secured (2026-04-29)
- [SIPRI Trends in World Military Expenditure 2025](https://www.sipri.org/publications/2026/sipri-fact-sheets/trends-world-military-expenditure-2025) — 29 European NATO members $559B combined; Germany $114B (2.3% GDP); Spain $40.2B; Ukraine $84.1B (40% GDP); Russia 7.5% GDP
- [NATO Hague Summit Declaration June 2025](https://www.nato.int/en/about-us/official-texts-and-resources/official-texts/2025/06/25/the-hague-summit-declaration) — 5% GDP by 2035 (3.5% core + 1.5% security-related); Spain excluded; 2029 review
- [ReArm Europe / Readiness 2030](https://www.consilium.europa.eu/en/policies/european-defence-readiness/) — €800B target, €150B SAFE loan, national escape clause activated for 17 member states (Feb 2026)
- [EU MFF Mid-Term Review 2024](https://www.consilium.europa.eu/en/policies/eu-long-term-budget/timeline-mid-term-revision-of-the-long-term-budget-2021-2027/) — €64.6B reinforcement (Ukraine €50B + migration €2B + emergency €1.5B); next MFF 2028–2034 proposal July 2025 with competitiveness/resilience/defence focus. **Bandwidth-allocation proxy: a €64.6B mid-cycle reinforcement IS the concurrent-crisis tax on regular spending priorities.**
- [EEA European Climate Risk Assessment 2024](https://www.eea.europa.eu/en/about/who-we-are/projects-and-cooperation-agreements/european-climate-risk-assessment) — 36 climate risks, 8 particularly urgent; agriculture/food most-affected sector 2025
- [Munich Re NatCat 2025 Europe](https://www.munichre.com/en/company/media-relations/media-information-and-corporate-news/media-information/2026/natural-disaster-figures-2025.html) — Spain wildfires 400,000 hectares (5x average); 2024 Valencia floods anchor
- [Cedefop 2025 Skills Forecast](https://www.cedefop.europa.eu/en/tools/skills-forecast) — country-level employment projections to 2035 by sector. Coal mining largest decrease; electricity jobs increase; engineering + administration increase. Direct input for net-climate-position adaptation-capacity scoring
- [Net-Zero Industry Act + Clean Industrial Deal Feb 2025](https://commission.europa.eu/topics/competitiveness/green-deal-industrial-plan/net-zero-industry-act_en) — €100B clean manufacturing; 40% strategic manufacturing capacity target by 2030
- [Tooze Chartbook 130 (2022, original definition)](https://adamtooze.substack.com/p/chartbook-130-defining-polycrisis) — parallel framing only; does not address institutional bandwidth
- [Tooze Chartbook 407 (2025, retraction)](https://adamtooze.substack.com/p/chartbook-407-polycrisis-revisited) — pivot to personal-agency framing; "polycrisis no longer seems so apt"
- **IISS Military Balance 2025** — three chapters secured 2026-04-29 (launch remarks + Defence Spending and Procurement Trends + Russia and Eurasia). Verbatim extracts in [`layer-6-iiss-military-balance-2025-extracts.md`](layer-6-iiss-military-balance-2025-extracts.md). Direct external attestation of bandwidth-tax mechanism from IISS analysts: Giegerich ("the major concern in Europe is the sustainability of current defense spending increases at a time of significant fiscal pressures across the continent") + McGerty ("potentially elements of social care or pensions are going to have to be impacted to continue to fund defense"). Independent confirmation of the Lens 5(a) institutional-bandwidth-competition mechanism without going through Tooze. Plus: top-15 defence-spending USD figures (DE 86.0, UK 81.1, FR 64.0, IT 35.2, UA 28.4, PL 28.4); European procurement contracts (KR $18.03bn, IL $6.85bn+, BR $4.18bn); nitrocellulose China-dependency (direct Task 4 input); Anduril Arsenal-2 abroad-optionality (Lens 4 jurisdictional-buffering input).

### Open data fetches
- IISS *Military Balance 2025* — **PARTIALLY SECURED 2026-04-29** (3 chapters via Phil-supplied PDFs). Full Military Balance plus database remains paywalled for force-structure tables.
- Tooze *Shutdown* (2021) Ch on COVID institutional response — closest adjacent literature
- Freedman *Command* (2022) — bandwidth saturation in crisis decision-making
- Lieven essays at Quincy Institute — no specific polycrisis essay located, parallel framing only
- Cedefop 2025 country-report PDFs at country granularity

### Schema addition (Bundle R, 2026-04-30) — `lens5_internal_transition_diagnostic`

A firm-level interpretive lens added to Lens 5 alongside the existing country-level polycrisis composite. The diagnostic answers a question Lens 5's aggregate readings cannot: when two firms with identical reskilling-programme participation produce opposite ROIs, why? Per-country schema:

```
{
  value: null,
  acquisition_status: "L5-framework-only; no country-level data; Phase 5+ acquisition target",
  framework_citation: "L5 lenses.html §4 'Candidate diagnostic metric — internal transition speed vs external turnover'",
  operational_definition: "internal transition speed = elapsed time from capability formation
    (training completion / certification) to internal role change using that capability;
    external turnover = rate at which newly-capable workers leave the firm before internal translation.
    Where external turnover materially exceeds internal transition speed,
    transition architecture is broken (firm pays to produce capability; market captures it).",
  br_22_provenance: { validation_event: "Stefanie Haslauer LinkedIn thread, 2026-04-15",
                      validation_pattern: "BR-22 external-human variant (5-round adversarial pushback)",
                      outcome: "Metric crystallised at round 5 as testable diagnostic" },
  layer_5_acquisition_status: "framework-only; country-level data is Phase 5+ acquisition target",
  layer_6_application_note: "Use as squeeze-flag interpretive lens for Class III countries even
    where country-level data is absent; carry as caveat in §4 reskilling-pathway framing",
  _provenance: { source_layer: "L5", bundle: "R", ingestion_date: "2026-04-30" }
}
```

Per Bundle R, top-level `cross_cutting_findings.internal_transition_diagnostic_framework` carries the country-agnostic framework. All 36 countries surface `value: null` with the framework citation and Phase 5+ acquisition pointer; the diagnostic is interpretive rather than load-bearing in the current corridor map. Layer 6 application: use as a squeeze-flag interpretive lens — the metric explains why programme-design comparisons in §3 explain less variance than they appear to, and why aggregate reskilling KPIs (completion rates, participation %) miss the binding constraint on reskilling ROI.

---

## Scenario Stack (8 scenarios, S1–S8 spectrum order, with discipline rule)

**Discipline rule:** each scenario declares ONE load-bearing mechanism. If two scenarios share a mechanism they collapse into one. This stops scenarios from drifting into mood-narrative territory and keeps them falsifiable.

**Bundle V (2026-04-30) renumbering:** the prior 5-scenario stack with subversions (S1, S2a/S2b, S3, S4a/S4b, S5_cascade) is retired. Bundle V splits old S2a (Wage Cliff) — which conflated mid-skill wage compression with within-occupation reshape — by promoting the within-occupation reading to a separate scenario (S3 Jobs Transform) and renumbering the full set linearly in spectrum order.

| # | Scenario | Spectrum position | Load-bearing mechanism | Counterfactual it tests | Old code |
|---|---|---|---|---|---|
| **S1** | **Reinstatement Revival** | uber-optimistic | Augmentation effects strengthen; new-work creation reverts to *or exceeds* historical base rate | Autor 2024 weakening trend reverses | S1 |
| **S2** | **Climate Adaptation Boom (Zone-C)** | optimistic | Zone C demand surge from climate adaptation absorbs displaced Zone A workers; new sectoral demand at premium wages | Climate-adaptation Zone C wages exceed displaced Zone A wages; cross-zone transition rate ~12–15% | S2b |
| **S3** | **Jobs Transform** *(NEW)* | slightly optimistic | AI substitutes for routine sub-tasks within existing occupations; wages stable or up; jobs reshape (within-occupation reinstatement) rather than cross-occupation creation | Brynjolfsson OpenAI RCT 2025 + Dell'Acqua HBS WP 24-013 (BCG consultants +40% within-frontier / -19pp out-of-frontier) + Nielsen forklift / seniority-tier T31; historical: ATM/teller (Bessen), Spreadsheets (Levy) | NEW |
| **S4** | **Muddle Through** | middle (baseline) | Current parameters persist; outcomes neither recover nor cascade | Baseline — no regime change | S3 |
| **S5** | **Wage Cliff** | slightly pessimistic | AI substitutes for mid-skill labour; cross-zone transition under current −25% to −40% wage cliff; fewer or lower-paid reinstatement jobs | Layer 5 wage-cliff + certification-wall reality holds; transition rate stays at 3–10%, doesn't double | S2a |
| **S6** | **Reinstatement Failure** | pessimistic | Autor 2024 reinstatement weakening + Lens 5 inputs hold | Autor 2024 trend continues, Lens 5 inputs hold; cross-occupation reinstatement under-supplies new work | S4a |
| **S7** | **Bandwidth Fracture** | pessimistic | Lens 5 dominates; bandwidth fractures; reskilling supply-side intact but coordinative capacity overrun | Lens 5 inputs dominate while reinstatement supply-side holds | S4b |
| **S8** | **Polycrisis Drag** *(conditional, orthogonal)* | parallel cascade | Concurrent crises saturate bandwidth; capability floor breached; reskilling capacity overrun | Lens 5 inputs all max; Zone A→C drops below 2%. Empirical anchor: Ukraine | S5_cascade |

**S3 distinct from S2.** S2 (Climate Adaptation Boom) requires *new sectoral demand* — Zone C climate work absorbs displaced Zone A workers. S3 (Jobs Transform) reshapes *existing occupations* without sectoral redirection — workers stay in their occupation, sub-task mix changes. S2 is cross-occupation reinstatement; S3 is within-occupation reinstatement. They can co-realise but operate on different mechanisms.

**S3 distinct from S5.** S5 (Wage Cliff) features mid-skill wage compression as the load-bearing mechanism. S3 (Jobs Transform) features wage stability or modest rise. The empirical question is which dominates per country: wage compression vs within-occupation reshape under stable wages. Determined by within-firm transition infrastructure, human-capital intensity, sector mix favouring cognitive-social complementarity (Deming).

**Layer 5 bounding constraint on S2.** Climate Adaptation Boom is feasible only if Zone A→C cross-zone transition rates rise from current 3–10% to 12–15%. Layer 5 documents wage cliff −25% to −40%, certification walls 12–42 months, 6 years unemployment before reservation wages collapse. S2 requires climate-adaptation Zone C work to command a wage premium that closes or reverses the cliff. The optimistic scenarios are bounded by Layer 5 reality, not narrative.

---

## Fragility Classes (4 — country-level, across scenario stack)

Each country gets a corridor assignment (3 corridors, see below) PLUS a fragility class (I–IV) PLUS a scale tag (aggregate / distributional / both).

| Class | What it means | Recovery path | Empirical anchor |
|---|---|---|---|
| **I — Robust (relative-stable, C3-guarded)** | Corridor stays within ±1 of baseline across the seven routine-perturbation variants (S1, S2, S3, S4, S5, S6, S7) AND no routine variant assigns the country to C3; cascade behaviour under S8 reported as `cascade_corridor` (orthogonal) | (none needed for routine perturbation; cascade-readiness still informative) | **Phase 3 final (Bundle L, 2026-04-29):** 9 countries — 5 Nordics (DK/FI/IS/NO/SE) + 4 Continental squeeze (BE/FR/NL/LU). NL did confirm under final lock (squeeze-flag profile + ±1 perturbation + no C3 path); CH did NOT confirm (C3 path under S4a/S4b — structural-bias correction working as intended) |
| **II — Fragile** | Corridor swings >±1 of baseline across routine-perturbation variants (spans 3+ corridors) | Depends which scenario realises | Probable: most EU-27 |
| **III — Pre-Failure Risk** | Under Muddle Through (S4), lands in Corridor 3 | Possible only if S1, S2, or S3 realises (S3 added Bundle V 2026-04-30) | **Phase 2 result:** IE, UK |
| **IV — Currently Failing** | Lens 5 inputs already at maxima; cascade is happening *now* (measured), not predicted (forecasted) | Requires regime change — institutional re-architecture, ceasefire, capital re-stabilisation. NOT scenario realisation | **Contemporary anchor:** Ukraine (military expenditure 40% GDP, infrastructure war-damaged, demographic collapse). **Historical anchors:** Copperbelt 1991–2001 (−66% ZCCM employment, Fraser & Lungu 2007); São Paulo ABC 1989–1999 (−48% industrial jobs, Ramalho et al 2009); Latrobe Valley (+0.8pp SA4 unemployment gap persistent 30+ years, Burke/Best/Jotzo 2018) |

**III/IV demarcation rule:** Class III is a forecast (under current trajectory the country lands in Corridor 5). Class IV is a measurement (it's happening — multiple Lens 5 inputs already at empirical maxima). The line is observability, not severity. This stops Class IV from becoming a rhetorical category.

**Fragility class is itself a finding.** A country in Class I under any corridor is structurally robust regardless of which scenario realises — a different finding from a country in Class II Corridor 1 (which depends on positive-scenario realisation). The class system is the operationalisation of the structural-bias warning already in this framework: historical calibration overstates protective power of buffering institutions; Class III countries under historical-base-rate calibration may be more fragile than the calibration suggests.

---

## Corridors (consolidated to 3 from draft 5)

Validation test (4 criteria each corridor must satisfy) runs against L1–L5 data in Phase 2. Probable consolidation (pending validation):

| # | Corridor | Mechanism (distinct from severity) | Pre-validation status |
|---|---|---|---|
| 1 | **Managed Transition** | Displacement absorbed by absorption capacity + demographic buffer; reinstatement effects sufficient | Narrower than historical base rate suggests (structural bias) |
| 2 | **Partial Absorption** | Mid-skill displacement; high-skill augmented; low-skill unaffected (manual). Aggregate-vs-distributional split is structural, not transient | Folds in former Corridor 3 ("bifurcated labor market") as a distributional descriptor across other corridors via scale-tag system |
| 3 | **Displacement Without Absorption** | Velocity exceeds absorption capacity; reskilling pathway structurally insufficient. Polycrisis Drag (S8) is the terminal state of this corridor | Wider than historical base rate suggests (structural bias) |

**Cut from draft set:**
- **Demographic Rescue** (former Corridor 4) — fails structural-bias test; reinstatement mechanisms it depends on are weaker now than in historical analogues. Folds into Lens 2 finding ("rescue thesis holds only in Z countries where [conditions]"), not a standalone corridor.
- **Compounding Crisis** (former Corridor 5) — S8 (Polycrisis Drag, was Cascading Institutional Failure pre-Bundle V) does this work better as a scenario than as a corridor. Folds into Class IV "Currently Failing" + scenario stack.

**Scale tag (required field per assignment):** aggregate / distributional / both. Aggregate-only assignments must declare matched distributional reading.

---

## Site Specification (synthesis.nexalps.com — Layer 6 deliverable)

**Headline visual:** 5-line trajectory sparkline per country (one trajectory per scenario, 2026–2035 horizon). Country selector + scenario toggle + fragility-class indicator.

**Page structure:**
- `/` (overview) — corridor map across 36 countries with scenario toggle
- `/lenses.html` — 4 lenses + folded Lens 3 explanation
- `/lens5.html` — Polycrisis Drag standalone (deepest content, most novel)
- `/scenarios.html` — 5-scenario stack with discipline rule + bounding constraints
- `/fragility.html` — 4-class system with III/IV demarcation rule + Class IV anchors
- `/countries.html` — per-country drill-down (corridor + class + 5 trajectories + Lens 5 inputs scored)
- `/dach.html` — DACH-specific depth for client positioning (mirrors L4/L5 pattern)
- `/methodology.html` — Tooze-distinction note; structural-bias warning surfaced; lens scoring rubrics
- `/sources.html` — bibliography
- `/llms.txt` — machine-readable summary

**Document deliverable:** 15–25k word synthesis paper, document-first then site renders the corridor map + key tables. SCQA → corridor findings → country detail → structural-bias section → fragility classes → Layer 7 handoff. Defer Minto/message map until findings exist (framework discipline — don't pre-fit to a triad).

**L3 read pattern:** site reads `european-disruptions-map/site/disruptions-data.json` directly until L3's render gap is closed (data shipped, HTML render not extended). Verified 2026-04-29: all 5 expected keys present (`structured_metrics`, `spreadsheets_counterfactual`, `incumbent_vs_cohort_displacement`, `capability_vs_adoption_gap`, `institutional_response_scope_statement`).

---

## Scenario Corridors (output of combined lenses)

_Original v1 draft below — superseded by Locked Decisions block at top + Scenario Stack + Fragility Classes + Corridors sections above. Retained for reference._

_To be defined after lenses are run. Initial candidates below — but these must earn their place through non-obvious findings, not 2×2 matrix logic._

### Draft corridors (to validate or discard)
1. **Managed transition** — displacement is real but absorption capacity matches or exceeds it; demographic decline provides genuine buffer
2. **Displacement without absorption** — displacement velocity exceeds absorption capacity; reskilling pathway structurally insufficient
3. **Bifurcated labor market** — high-skill workers augmented, mid-skill workers displaced, low-skill workers unaffected (too manual); society splits
4. **Demographic rescue** — AI displacement is absorbed by demographic decline before institutional response is needed
5. **Compounding crisis** — multiple simultaneous shocks push beyond any single-variable corridor

### Corridor validation test
Each corridor must satisfy ALL of:
- [ ] At least one country empirically maps to it based on Layers 1–5 data
- [ ] It is distinguishable from other corridors in mechanism, not just severity
- [ ] It produces at least one non-obvious or counterintuitive implication
- [ ] It is not trivially predictable from a 2×2 matrix of "high/low displacement × high/low absorption"

### Structural bias in the corridor calibration (2026-04-14, Layer 3 finding)
All historical cases that calibrate these corridors — accountants, telephone operators, dockworkers, and the rest — played out in an era when reinstatement effects (new-work creation, augmentation-driven demand expansion) were structurally stronger than they are now. Autor/Chin/Salomons/Seegmiller (QJE 2024) document that automation's demand-eroding effects have intensified over the last four decades while augmentation's demand-increasing effects have not. Applying historical lag estimates, adjacency findings, or corridor assignments to AI without discounting for this weakening-reinstatement trend systematically UNDERESTIMATES displacement severity.

**Implication for this framework:** the "managed transition" corridor is narrower than historical calibration alone suggests. Corridors 1 (managed transition) and 4 (demographic rescue) both depend on reinstatement mechanisms that are weaker in 2026 than they were in 1985. Corridor 2 (displacement without absorption) is correspondingly broader than historical base rates imply. The corridors themselves are not as wide as they used to be — and the project must state this explicitly rather than implicitly assuming historical-base-rate widths.

This is not a caveat. It is a structural bias in the entire Layer 6 calibration methodology and must be surfaced in the final output, not buried.

**Second structural-optimism mechanism — counterfactual selection bias (2026-04-14, Retrofit v0.3 Case 1 finding):** El-Sahli & Upward (2015) show that UK dockworkers fared "no worse" than matched unskilled men over 1971–2011. But Nickell & Bell (1995) document that UK unskilled men overall had extremely poor 1980s–90s labour-market outcomes. "No worse than controls" here means *"dragged down with the rest of the unskilled male workforce"* — not *"insulated from the shock."* Historical institutional buffering looks effective because the counterfactual cohort is itself in structural decline; against a healthier counterfactual, buffered outcomes would look materially worse. Same direction as the weakening-reinstatement bias: both mechanisms cause historical calibration to overstate the true protective power of buffering institutions. Corridor 1 (managed transition) is even narrower than the reinstatement-adjusted estimate suggests.

---

## Layer 7 Interface

Layer 7 (Futureproof) receives the corridor assignments and asks: **given your corridor, what do you do?**

Institutional readiness appears here as the *prescriptive* variable:
- If Lens 1 shows you're in corridor X, and your institutional readiness is Y, then action Z
- If the combination of Lens 1 + Lens 2 + Lens 4 shifts you from corridor A to corridor B, then the action set changes to...

This is where the message map / Minto structure likely belongs — the communication of actionable findings, not the analytical framework itself.

---

## Open Questions

1. ~~**Perez — keep or cut?**~~ **RESOLVED 2026-04-29:** Folded into Lens 1 as compression footnote. Did not earn standalone status; macro-level only, no country differentiation.

2. ~~**Corridor count.**~~ **RESOLVED 2026-04-29:** Target 3 corridors + fragility classes (4) + scale tags (3 values). Bifurcated and Compounding Crisis cut from draft as standalone corridors; folded into scale-tag system + Class IV "Currently Failing" respectively.

3. **Cross-case metrics for Layer 3.** ~~Run the feasibility audit…~~ **RESOLVED 2026-04-14.** Feasibility audit completed across 20 disruptions × 5 metrics. Result: 7 high-feasibility cases, 8 medium, 5 low. 75% of cases are workable — clean pass with tail exclusions, not a marginal pass. Addition proceeds with scope matched to data density: quantitative backbone on 7 cases, per-cell confidence flags on 8 medium cases, narrative-only treatment of 5 low cases. Feasibility matrix published as methodological appendix. Metric (e) peak annual displacement rate ships with explicit `derivation_method` and `uncertainty_band` fields per BR-21, not clean numbers. Task→employment lag retrofit on 4 best-documented cases (containers, ATMs, CAD, DTP) is the Layer 3 archival task that feeds Lens 1's lag specification.

4. **Communication structure.** Defer until findings exist. Let the Minto pyramid, message map, or SCQA structure emerge from what the lenses actually produce. Don't pre-fit.

---

## Framing Inputs

### Inertia as absorption-rate modulator (Jaffer, Module 4)

> "Inertia is the most underestimated force — the 10x better threshold exists because of inertia. 'I've always done it this way' is more powerful than any feature. Positioning must amplify identity, not threaten it: 'Be a better lawyer with AI' not 'Replace lawyers with AI.'"

**Why this matters for Layer 6:**

Inertia is the missing variable between AI *exposure* (Layer 1) and AI *displacement* (Lens 1). High exposure scores predict displacement only in the absence of identity-preserving adoption paths. Where positioning amplifies professional identity ("be a better lawyer"), adoption is faster but displacement is slower — the worker absorbs AI rather than being absorbed by it. Where positioning threatens identity ("replace lawyers"), adoption is slower AND displacement sharper when it eventually breaks through.

**Implications to test:**
- The 10x-better threshold may explain why some high-exposure roles show little actual displacement (inertia barrier absorbs the first-order shock).
- Corridor assignment may depend on positioning-path availability, not just displacement/absorption ratios. A profession with strong identity-amplifying AI positioning (lawyers, doctors, accountants) may land in Corridor 1 even at high exposure; a profession without that positioning (entry-level clerical, content moderation) may land in Corridor 2 even at lower exposure.
- Layer 7 prescription must distinguish between "reduce exposure" (rarely feasible) and "build identity-amplifying positioning" (often feasible and high-leverage).

**Cross-references:**
- `knowledge/practitioner/middle-hollowing-bifurcation.md` — bifurcation concentrates at the pole that can't identity-amplify (generalist middle knowledge work)
- `knowledge/practitioner/transition-architecture-metric.md` — inertia inside firms shows up as slow internal transition speed even when external demand is clear

**Source:** `skills/ai-product-strategy` Takeaway #8 (Jaffer, Module 4). Related: Takeaway #7 (Action = Drive minus Resistance, where Inertia is one of three Resistance components).

### Functional-layer exposure decomposition (Klinger three-layer, Apr 2026)

Default narrative says the execution layer (ICs, juniors, production workers) is cut first. Andreas Klinger's 2026-04-21 inversion: in good organisations, decisions happen at every layer close to the problem. What AI compresses is the **coordination layer** — translation, synthesis, tacit-knowledge transmission, onboarding, handoff management. Middle management is the exposed seam, not execution.

Three functional layers per org or role:

1. **Decision** — judgment, portfolio calls, escalation, taste. Robust. LLMs lack time-sense, taste, accountability.
2. **Coordination** — translation, synthesis, onboarding, meeting-running, handoff management. Most exposed. This is the function middle management sits on.
3. **Execution** — doing the work. Reshaped, not removed. Productivity multiplies.

**Why this matters for Layer 6:**

Lens 1's absorption-capacity variable is currently read at firm-level or occupation-level. The Klinger decomposition implies a sub-dimension: two roles at the same ISCO 3-digit code can have very different coordination-layer shares, and therefore different Lens 1 readings. An ISCO group dominated by coordination-layer roles (classic middle-management work) sits closer to the displacement regime than the same group's headline exposure score would suggest. An ISCO group dominated by decision-layer work (portfolio managers, principals, senior technical leads) sits further from it.

**Implications to test:**
- Occupation-level exposure scores should be re-read with a coordination-share weighting. ISCO groups with high coordination-share + high exposure are the priority Lens 1 candidates.
- Corridor assignment may depend on the country-level mix of decision-heavy vs coordination-heavy roles inside an ISCO group — not just the exposure headline. Countries with flatter middle-management layers (culturally or structurally) may absorb AI displacement differently than countries with larger middle-management layers.
- Layer 7 prescription should distinguish between "retrain execution-layer workers" (current default) and "restructure coordination-layer work" (the Klinger implication). These are different interventions with different cost curves.

**Cross-references:**
- `knowledge/practitioner/klinger-three-layer-exposure.md` — full frame + limits
- `knowledge/practitioner/middle-hollowing-bifurcation.md` — distributional outcome of the functional-layer compression
- `knowledge/practitioner/contemporary-claims-registry.md` — Source 1 testable claims
- `knowledge/practitioner/transition-architecture-metric.md` — coordination layer compressing faster than internal transition can rebuild it is the mechanism behind the transition-architecture failure

**Source:** Andreas Klinger, "Who is getting fired and why?" (Substack + YouTube, 2026-04-21). Operator/investor perspective (Remote First Capital); structural observation, not empirical claim. Limits: assumes coordination and execution are cleanly separable (in some roles they're entangled); thin-sourced IKEA example; knowledge-worker focused.

### Aggregate-vs-distributional scale axis (Andreessen × Class C, Apr 2026)

Every disruption claim operates at a scale of analysis. Maximalist-optimistic claims typically operate at aggregate long-run (Andreessen's "lump of labour fallacy," 99% consumer surplus framing — true for electricity, internet, smartphones at 50-year horizons). Pessimistic claims typically operate at distributional medium-run (Class C scarring evidence — Gelsenkirchen, Latrobe, Copperbelt — 30-50 year regional wage suppression, generational stickiness). **Both can be simultaneously true.** Most apparent disagreements between optimists and pessimists are scale-mismatch, not factual disagreement.

**Why this matters for Layer 6:**

The corridor assignments currently collapse aggregate and distributional outcomes into a single label. A country in "managed transition" at aggregate scale may host "Gelsenkirchen-shape scarring" at regional or cohort scale. These are different empirical realities that demand different policy responses, and the current corridor labels hide that distinction.

**Candidate implementation:**
- Every corridor assignment ships with a **scale tag** (aggregate / distributional / both) and an explicit annotation when the two scales disagree.
- Lens 4 (compounding shocks) is the natural home for this framing — aggregate-gains + distributional-costs is itself a compounding pattern. May fold into Lens 4 rather than standing alone as Lens 5.
- The corridor validation test in the Scenario Corridors section should add a fifth criterion: "Does this corridor describe aggregate outcome, distributional outcome, or both? If aggregate only, what is the matched distributional reading?"

**Cross-references:**
- `docs/CONCEPT-BRIDGES.md` — aggregate-vs-distributional scale axis as cross-domain primitive
- `knowledge/practitioner/contemporary-claims-registry.md` Section 3 (Andreessen claims with scale tags)
- `knowledge/lecture-kits/ai-labour-reskilling.md` Section 1 (scale-mismatch diagnostic)

**Source:** Surfaced during Andreessen 20VC cross-check × Phil's Layer 3 Class C data (2026-04-21 ingestion session). Held as methodology candidate pending one more application before promotion to skill takeaway.
