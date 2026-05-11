# Part 6 — European AI Labour Market Synthesis

**Build:** 2026-04-29 · Bundle N composition over Bundle M SOT JSON (schema v1.0). Country scope: 36 (EU-27 + EFTA-4 + UK + 4 candidates). Class IV reference: Ukraine (not corridor-mapped per locked spec line 341). Lenses: 5. Scenarios: 8 (7 routine + S8 conditional). Corridors: 3. Fragility classes: 4.

---

## TL;DR — Five Findings

- **Strict-zero Class I is the structural-bias headline.** Replacing the Phase 1 thresholds (C1 < 1.50, C3 ≥ 3.00) with the theory-anchored 1.20 / 2.80 corridor edges drops Class I to zero under a literal-strict (b) ±0 rule — even spec-anchor Nordics fail strict robustness. The relative-stable rule with the Q1 asymmetric-guard lock (±1 of baseline AND no routine variant reaches C3) restores Class I to 9 (5 Nordics + BE / FR / LU / NL). The published "managed transition" base rate over-states robustness; the corrected reading is that there are no unconditionally robust European labour markets at the 1.20 cap. (See §4.1.)
- **Demographic orthogonality is decisive.** Across 32 scored countries the maximum retirement-offset reading is ~26 % against a locked-spec buffer threshold of 80 %. Zero countries meet `buffer_holds`. Lens 2 is uniformly refuted at scale: demographic load enters Lens 5 polycrisis composite as an independent signal but does not absorb Lens 1 displacement velocity. The "silver-lining ageing" argument fails empirically for all 36 countries. (See §4.2.)
- **The optimism path narrows to Climate Zone-C.** Three countries (AT, LU, TR) are `s2_dependent = TRUE` — among the 7 routine variants S2 (Climate Adaptation Boom) is the *only* scenario that lands them in C1 (Managed Transition). Under post-growth regimes (AT, LU) S2 is also the modal routine variant — the dominant probability mass — and the only genuinely-positive scenario surviving the regime check. Tech-led reinstatement (S1) is materially closed for these countries; only sectoral redirection into climate adaptation reaches C1. (See §4.3.)
- **Averages hide a split in the high-coordination cluster (T34).** The 2-digit Klinger join shows that within OC2 (professionals) teaching weight (0.582) is 3.7× ICT weight (0.157) — a spread that 1-digit averaging concealed. Education / public-administration heavy economies (DK / IS / LU / NO) get pulled up — *EDUCATION / ADMIN LIFT*; ICT-heavy knowledge economies (CH / DE / IE / UK) get pulled down — *FINANCE / TECH DRAG*. Bundle K's "finance/legal underweight" hypothesis was real but smaller than the offsetting ICT overweight. The deliverable presents the high-coord cluster as two distinct archetypes. (See §4.4.)
- **The squeeze cluster is eight worker-protection economies, two distinct mechanisms.** The SOT records eight squeeze-flagged countries (BE, DE, DK, FI, FR, NL, NO, SE) — four Nordic (DK, FI, NO, SE — worker-protection × trade-decoupling, no UK adjacency) and four Continental (BE, DE, FR, NL — worker-protection × UK adjacency × Mode 1 capital-flow vulnerability). LU is explicitly NOT squeeze-flagged in the SOT (asymmetry score 0.6436, binary false). At 2-digit Klinger, BE (drag 0.500) and NL (drag 0.478) sit within the Continental knowledge-economy range and pattern-match neither the *EDUCATION / ADMIN LIFT* nor the *FINANCE / TECH DRAG* archetype — the squeeze is mechanistically independent from coordination-share displacement velocity. Per-country quantification rests on ~40 high-risk Annex III deployer occupations and ~29 PWD post-market duty occupations (Bundle Q). The flag is preserved as an orthogonal capital-flight signal, not a labour-displacement modifier. (See §4.5.)

---

## 1. Why this synthesis exists

European AI labour-market projections circulate in three registers: vendor reports keyed to compute-spend and adoption surveys; macro forecasters working from historical reinstatement base rates; and political communications keyed to ALMP commitments and reskilling envelopes. None of the three takes seriously that (a) the historical reinstatement base rate has weakened (Autor et al. QJE 2024), (b) demographic buffering across Europe is empirically too thin to absorb mid-skill displacement (Lens 2 result here), (c) institutional bandwidth is being contested by concurrent crises (defence, climate, Ukraine, MFF mid-cycle reinforcement), and (d) coordination-share heterogeneity within "high-coord" economies cuts in opposite directions at the 2-digit aggregation level.

This synthesis is a corridor map across all 36 European labour markets, scored under five lenses (displacement velocity, demographic buffer, distributional fold, polycrisis drag, jurisdictional buffering), folded into three corridors (Managed Transition, Partial Absorption, Displacement Without Absorption), bracketed by four fragility classes (Robust, Fragile, Pre-Failure Risk, Currently Failing), and stress-tested against eight scenarios (seven routine variants plus a conditional polycrisis drag). Every country is tagged with regime (growth-baseline, secular-stagnation-warning, post-growth-empirical), scale (aggregate, distributional, both), and a capability-floor breach flag (12 countries). Probabilities are quoted as IPCC AR6 likelihood-scale band ranges, not point estimates.

The audience is senior policy and advisory readers — board members, executive-search principals, lecture-room participants — who need a citable single-document anchor that survives interrogation by a country specialist *and* by a structural-bias critic. Where Phase 1–3 shipped reproducible scoring artefacts (CSVs, JSON, methodology notes), Part 6 ships the result: which corridor, which class, which scenario, with which probability band, under which regime, with what is and is not central to the analysis flagged inline.

---

## 2. Methodology in one page

The 4-SM methodology Minto from `methodology.html` SM 1–4 (Phil-locked 2026-05-08).

### SM 1 — *Five lenses, chosen because earlier parts of the project had already assembled the evidence.*

We went with the five lenses we already collected evidence on in earlier parts of the project: AI exposure, demographics, disruption pathways, reskilling capacity, and careers data. The constraint was not which lenses might exist in theory — it was which ones we could test rigorously today, with European data, across 36 countries.

### SM 2 — *One calibration choice changes the headline.*

This result hinges on one "dial" setting: where we draw the corridor cut-offs. Earlier drafts used cut-offs fitted to past literature (1.50 / 3.00). The published version uses theory-anchored cut-offs (1.20 / 2.80). With the strict rule (no wiggle room), the literature cut-offs produce three "Robust" markets; the theory cut-offs produce zero. That's why we show the choice clearly and keep it reversible: readers can recreate the earlier count from the threshold ladder. We chose the theory anchor because it matches the Lens 1 framework.

### SM 3 — *What we deliberately left open.*

Three known gaps constrain this analysis:

1. **Occupational detail:** capability-floor breach is reported at a coarser job classification (2-digit ISCO) because the finer-grained European Social Survey microdata (3-digit) requires a multi-week application. The count here is a lower bound.
2. **Funding allocation:** the EU's adaptation funding through 2030 is not yet broken down by country. We can see the overall envelope, but not its distribution.
3. **Employer behaviour:** we cannot observe live signals like hiring, retraining launches, or redundancy plans because they sit behind paywalls or in proprietary HR systems.

### SM 4 — *We tested three candidate additions. None held up on its own.*

The EU Industrial Accelerator Act, proposed in March 2026, looked like a candidate ninth scenario. On close inspection, it runs the same absorption pathway as Climate Adaptation Boom: state-coordinated sectoral demand, with workers pivoting into new sectors. The US Inflation Reduction Act, three years post-implementation, confirms the mechanism class.

We also tested whether the wealth-fund-rich economies (Norway, Sweden, Denmark, the Netherlands, with Switzerland adjacent) deserved their own regime. The direction is empirically defensible — pension and sovereign-wealth differences are real — but the per-country threshold did not hold cleanly across all five candidates. Switzerland's central-bank reserves do not behave like Norway's sovereign wealth fund, so the line between "wealth-fund rich" and "post-growth" could not be drawn consistently.

A third test asked whether startup-driven absorption (Europe's gap relative to the US in venture-scale firm formation) warranted its own scenario. ECB analyses document the gap clearly, and examples from other regions suggest the mechanism is possible. But each existing scenario in this taxonomy rests on something concrete — Cedefop's per-country employment projections, the Net-Zero Industry Act's committed €100 billion, the IRA's three years of realised data — and startup-driven absorption in Europe has no equivalent anchor yet. Without a comparable anchor, it cannot be probability-weighted alongside the others.

The three rejections rest on different reasoning, but the takeaway is the same. Going forward, more than one of these mechanisms likely has to work at the same time — climate-led sectoral pivot, industrial-policy demand, wealth-fund buffering, startup formation, and the within-occupation reshape already in the taxonomy. The next part looks at what happens when several of those forces work together, and what that would cost.

### Specialist data anchors (deferred from the within-section Minto)

**Scope.** 36 countries: EU-27 + EFTA-4 (CH, IS, LI, NO) + UK + 4 candidate-partial-coverage (BA, MK, RS, TR). Ukraine carried as Class IV reference panel only — institutional bandwidth saturated, capability floor breached by definition; corridor classification (C1 / C2 / C3) does not apply.

**Five lenses (specialist detail).** Lens 1 — displacement velocity vs absorption capacity, the corridor-defining ratio; absorption decomposed via Bundle R into a Zone-A-to-Zone-C transition rate keyed off `_system_p1` — Nordic flexicurity 9.9 % derived central, Continental Corporatist 6.9 %, Germanic Dual 7.9 % derived against a 3–6 % headline band, Liberal Market 3.2 % derived against a 5–8 % headline, Southern European 4.8 %, Central/Eastern European 3.3 %, candidate-baseline 3.5 %; plus a regulated-absorption-friction score from Bundle Q ranging 0.46 to 0.68. Lens 2 — demographic buffer test against an 80 % retirement-offset threshold; per-country `lens2_demographic_buffer` object enriched via Bundle P now carries retirement_offset_pct, working_age_change_pct_to_2050, country-divergence tier, and zone heterogeneity. Lens 3 — folded into scale-tag (aggregate / distributional / both) rather than carried as a separate dimension. Lens 4 — compounding-crisis shock count + jurisdictional-buffering squeeze flag; squeeze_flag upgraded boolean→object via Bundle Q with per-country asymmetry_score and AI-Act overlay counts: Annex III high-risk deployer ~40, Art 26(7) deployer obligations ~121–124 universal-scope, PWD post-market duties ~29–31; Annex III + PWD carry the diagnostic weight, Art 26(7) relegated to footnote because its universal scope collapses to country employment-coverage rather than a differentiated overlay. Lens 5 — polycrisis drag composite at 2-digit ESCO-weighted ISCO with Klinger coordination-share weighting and a capability-floor breach test; plus Bundle R `lens5_internal_transition_diagnostic` schema carrying the firm-level internal-transition-vs-external-turnover framework as interpretive lens (country-level data null with framework citation, Phase 5+ acquisition pointer).

**Three corridors.** C1 — Managed Transition (Lens 1 ratio < 1.20). C2 — Partial Absorption (1.20–2.80). C3 — Displacement Without Absorption (≥ 2.80). Thresholds locked in Bundle J (Phase 3) replace the Phase 1 anchors (1.50 / 3.00) with theory-anchored values: Phase 1 sub-cluster boundaries (Nordic ends at 1.10, next cluster starts at 1.59); Autor et al. QJE 2024 weakening reinstatement; El-Sahli & Upward 2017 NDLS structural lifetime-earnings deficits. C2 carries four within-corridor sub-clusters (Continental Corporatist; Germanic Dual; Southern European; Central / Eastern European-in-C2). C3 carries two within-corridor sub-clusters (Liberal Market high; CEE / Mediterranean weak-ALMP).

**Eight scenarios.** Seven routine variants — **S1** Reinstatement Revival, **S2** Climate Adaptation Boom (Zone-C), **S3** Jobs Transform, **S4** Muddle Through, **S5** Wage Cliff, **S6** Reinstatement Failure (Autor 2024 weakening), **S7** Bandwidth Fracture — plus one conditional, **S8** Polycrisis Drag, carried orthogonally to the routine grid. The S2 mechanism is conditional on works-council mediation and procurement-attached social conditionalities (ETUC; IndustriAll Europe). Probability vectors quoted per regime with 80 % CI bands aligned to IPCC AR6 likelihood scale.

**Four fragility classes.** Class I — Robust: ±1 of baseline AND no routine variant reaches C3 (Q1 asymmetric-guard lock 2026-04-29). Class II — Fragile: baseline stable, but routine variant lands in C3 (typically S6 / S7). Class III — Pre-Failure Risk: S4 baseline lands in C3 post-rescaling. Class IV — Currently Failing: candidate-partial-coverage with extreme Lens 5 readings (Ukraine reference panel calibrates upper bound).

**Three regimes.** growth_baseline (24 countries, including 4 candidates); secular_stagnation_warning (EL, IT); post_growth_empirical (10 countries: AT, CH, DE, FI, FR, LI, LU, NO, SE, UK). Regime is scenario-conditional, not country-static: identical corridor assignments imply different scenario-mass distributions across regimes (locked spec line 108).

**Read-only build.** Every claim in §3–§7 below traces to a field in `layer-6-deliverable-data.json` (schema v1.0, locked Bundle M; S2 mechanism-string additive landed Bundle W Phase 1, 2026-05-08). The methodological appendix (§8) renders the threshold-locking ladder, the 3-stage Class I rule trail, the capability-floor breach scope ceiling, the MFF per-country allocation gap, and the candidate-country C2 sub-cluster routing convention. Provenance per field is preserved in the JSON `_provenance` sibling block; this document quotes source bundle + source field where the underlying mechanism is named.

---

## 3. The 36-country corridor map

| Corridor | Label | Ratio range | n | Countries |
|---|---|---|---|---|
| **C1** | Managed Transition | < 1.20 | 5 | DK, FI, IS, NO, SE |
| **C2** | Partial Absorption | 1.20–2.80 | 16 | AT, BA, BE, BG, CH, DE, ES, FR, LI, LU, LV, MK, NL, RO, RS, TR |
| **C3** | Displacement Without Absorption | ≥ 2.80 | 15 | CY, CZ, EE, EL, HR, HU, IE, IT, LT, MT, PL, PT, SI, SK, UK |

**Corridor-1 read.** The five Nordic labour markets cluster at the lower end of the Lens 1 ratio (Norway 1.057 illustrative). Displacement velocity is well-absorbed by ALMP capacity; reinstatement effects remain intact under historical-base-rate calibration. The corridor is narrower than the historical literature suggests once the 1.20 cap is applied — the next sub-cluster begins at 1.59, leaving an empirically empty band. C1 is also the tightest fragility-class match: every C1 country is also a Class I country.

**Corridor-2 read.** Sixteen countries with partial absorption: ALMP partially absorbs mid-skill displacement; sectoral and regional reabsorption is uneven; high-skill augmented; low-skill (manual) unaffected. Four within-corridor sub-clusters: Continental Corporatist (BE, FR, LU, NL — three of which carry the squeeze flag); Germanic Dual (AT, CH, DE, LI — all post-growth or post-growth-proxied, three carry the breach flag); Southern European in C2 (ES alone — just below the C3 floor); Central / Eastern European in C2 (BA, BG, LV, MK, RO, RS, TR — see §8.5 on candidate routing). The C2 sub-clusters are analytical tags, not a 4th corridor (Phase 4 plan Q3 lock).

**Corridor-3 read.** Fifteen countries where displacement velocity exceeds absorption capacity and reskilling pathway is materially insufficient. Two within-corridor sub-clusters: Liberal Market high (IE, UK at ratio 3.33–3.40 — weak ALMP plus high knowledge-economy concentration); CEE / Mediterranean weak-ALMP (the remaining 13, ratio 2.81–2.96 — pulled in by the structural-bias-corrected 2.80 floor). El-Sahli & Upward 2017 supplies the empirical anchor for structural lifetime-earnings deficits in this corridor.

**Regime overlay.** All five C1 countries are split across regimes: DK and IS sit in growth_baseline (S1 reinstatement still serves as recovery channel); FI, NO, SE sit in post_growth_empirical (S1 materially weaker, recovery path runs through S2). Class I under post-growth is a stronger claim than Class I under growth-baseline — robust to routine perturbation under a regime where the historical reinstatement mechanism is itself attenuated.

**Cross-tab — corridor × class.** All 5 C1 countries are Class I. Of 16 C2 countries: 4 are Class I (BE, FR, LU, NL — all squeeze-flagged Continental Corporatist), 9 are Class II (AT, BA, BG, CH, DE, ES, LI, LV, RO), 3 are Class IV (MK, RS, TR). All 15 C3 countries are Class III. Class IV does not arise in C1 or C3 in the routine routine-variant grid; its three members all sit at C2 baseline because their candidate-partial-coverage readings do not push the Lens 1 ratio into C3 directly — the cascade signal arrives via Lens 4 / Lens 5 extremes.

---

## 4. The five folded findings

### 4.1 Structural-bias validation

The strongest validation of the structural-bias warning embedded in the framework arrived not as a confirmation of any positive prediction but as a *strict-zero* result on the Class I count. Bundle J replaced the Phase 1 thresholds (C1 < 1.50, C3 ≥ 3.00) with the theory-anchored 1.20 / 2.80 pair. Three independent anchors converged on the new values: Phase 1 sub-cluster boundaries (Nordic cluster ends at 1.10, the next cluster begins at 1.59 — the 1.20 cap sits inside the empirically empty band); Autor et al. QJE 2024 documenting reinstatement weakening; El-Sahli & Upward 2017 NDLS evidence on structural lifetime-earnings deficits in C3.

Under the literal-strict (b) ±0 rule applied to the new thresholds, Class I dropped to 0. Even the spec-anchor Nordics failed strict robustness. The fix was the relative-stable rule with the Q1 asymmetric-guard lock (Bundle L, 2026-04-29): Class I = ±1 of baseline AND no routine variant reaches C3. Class I restored to 9 — 5 Nordics plus BE / FR / LU / NL Continental Corporatist squeeze. Naive carryover of the same relative-stable rule without the asymmetric guard had returned 16; the guard removed CH, DE, LI, BG, ES, LV, RO because their C2 baseline reaches C3 under S6 / S7 — semantically inconsistent with "Robust." The strict-zero finding survives in the methodology trail not as a failed test but as the structural-bias headline: published "managed transition" base rates over-state robustness; the corrected reading is that there are no unconditionally robust European labour markets at the 1.20 cap, only conditionally robust ones (relative-stable, C3-guarded).

### 4.2 Demographic orthogonality

Lens 2 — the demographic-buffer thesis — was tested against the locked-spec threshold: a country `buffer_holds` if the retirement-offset (annual cohort exit through retirement as a share of AI-displaceable employment) exceeds 80 %. Across the 32 scored countries, the maximum reading observed is approximately 26 % (Greece, Croatia, Bulgaria, Lithuania, Latvia, Malta cluster). Zero countries meet the threshold. The 4 candidate-partial-coverage countries (BA, MK, RS, TR) are restated under L1-only treatment and not re-tested.

The implication is operational: demographic load enters Lens 5 polycrisis composite as an independent signal — old-age dependency, ALMP-relevant exit rates — but does not buffer Lens 1 displacement velocity at any meaningful share. The "silver-lining" ageing argument fails empirically for all 36 countries. Retirement attrition does not absorb the AI-displaceable cohort. This is a uniform refutation across regimes: growth-baseline, secular-stagnation-warning, post-growth-empirical countries all fail the buffer test by roughly the same margin. Lens 2 is therefore rendered as a single-string field in the SOT JSON ("refuted at scale") rather than a country-by-country object — the content is uniform.

The orthogonality finding is the central rebuttal to the most common public-discourse counter-argument: "Europe's older population will absorb the displacement." It does not. The buffer thesis is decisively refuted at 32-country scope — under the threshold the spec itself locked.

**Italy — the workforce shrinks before AI displaces a single worker.**

Italy is the only major European economy with negative net migration in 2025. Institutional ageing has crossed from buffer-deficit into accelerating decline — the workforce is contracting on its own, before AI substitutes for any task. Working-age population trajectory: −17.5% to 2050 (sharpest-decline tier). Retirement offset 25.3%, well below the 80% buffer threshold. Migration-dependence is acute but politically constrained, while unfillable shortages in care, trades, and healthcare amplify rather than absorb displacement. Italy sits in Class III, secular-stagnation regime, with the parallel-cascade scenario carrying a 0.10 conditional weight. Net migration 2025: **−485,823**.

### 4.3 The optimism path narrows to Climate Zone-C (s2-dependent)

Three countries — AT, LU, TR — are `s2_dependent = TRUE`. Among the 7 routine-perturbation variants, S2 (Climate Adaptation Boom) is the *only* scenario that lands them in C1 (Managed Transition); all six other routine scenarios produce C2 or C3. The framing is central: **the optimism path narrows to Climate Zone-C.** The wage-positive premium documented by Cedefop 2025 country-level employment projections plus the EU Net-Zero Industry Act €100 B clean-manufacturing envelope is the only mechanism strong enough to pull these three countries into C1.

Under the post-growth regime probability vector (AT, LU), S2 also dominates as the modal routine variant — the highest probability mass of any of the seven routine scenarios and the sentinel that PASSED in Bundle L (locked spec line 104: "Climate Adaptation Boom 2b becomes the only genuinely-positive scenario that survives the regime check"). The numerical band sits in §6 below; the narrative implication is the same. For TR (growth-baseline, Class IV partial-coverage), S2 mass is lower but the structural argument is identical: tech-led S1 reinstatement is closed; sectoral redirection into climate adaptation is the only routine path to C1.

This pairs with the structural-bias warning surfaced in §4.1. Published transition narratives that assume tech-led S1 reinstatement miss that, for AT / LU / TR, the tech-led path is not in the consideration set. The advisory implication is sharp: portfolio bets keyed to "Austria recovers via reinstatement" or "Luxembourg's financial-sector adaptation continues at trend" are mis-specified — the routine-variant grid says these countries reach C1 only through climate-adaptation-driven sectoral redirection, with all other routes producing C2 or worse.

### 4.4 High-coord archetype split (T34: averages hide a split)

Bundle K-2 ran the 2-digit ESCO-weighted Klinger coordination-share join and surfaced what 1-digit averaging had concealed. Within OC2 (professionals), OC23 (teaching) carries a Klinger coordination-share weight of 0.582 against OC25 (ICT) at 0.157 — a 3.7× spread inside a single 1-digit aggregate. Knowledge-economy countries with heavy ICT mass (CH, DE, IE, UK) get pulled DOWN at 2-digit; education and public-administration heavy economies (NO, IS, DK, LU) get pulled UP. The single 1-digit average had presented these eight countries as a single high-coordination cluster. The 2-digit decomposition splits them into two archetypes that move in opposite directions: **EDUCATION / ADMIN LIFT** (DK, IS, LU, NO) versus **FINANCE / TECH DRAG** (CH, DE, IE, UK). Bundle K's prior "finance/legal underweight" hypothesis was real but smaller than the offsetting ICT overweight that 1-digit aggregation had hidden.

This is the in-suite manifestation of **Takeaway #34** (`disruption-analysis` skill): *aggregation hides archetype bifurcation; the level at which a coordination signal is computed determines whether it acts as a lift or a drag on labour-market resilience*. T34 was abstracted from prior empirical episodes (the dual-baseline-scoring candidate, the bifurcated-lag classification work in Bundle K-2's parent project). Part 6 is its first end-to-end application as a deliverable-shaping decision: the high-coord cluster is *not* presented as a single archetype in the country profile section. Two archetypes ship.

The pedagogical depth this earns the document is not decorative. T34 is the reason a senior advisory reader cannot reduce the deliverable to "Nordics good, southern Europe bad" — the split inside the high-coord cluster fractures that reduction at the level where AI displacement actually cuts, and the 12-country capability-floor breach list (BE, CH, DE, DK, IE, IS, LI, LU, NL, NO, SE, UK — see §8.3) is precisely the population where this split matters most.

### 4.5 Squeeze-flag — eight worker-protection economies, two distinct mechanisms

The squeeze flag is borne by eight countries in the SOT JSON, not five: **BE, DE, DK, FI, FR, NL, NO, SE.** An earlier Specialist Appendix narrative had named only five (BE / DE / FR / LU / NL). That narrative drifted from the SOT data, which records the eight-country pattern Phase 2 methodology had computed. **Path 1 lock (2026-04-30): trust SOT, present the eight-country headline, and decompose the cluster into the two mechanistically distinct sub-clusters the data supports.**

| Squeeze sub-cluster | Countries | Mechanism |
|---|---|---|
| **Nordic** | DK, FI, NO, SE | Worker-protection plus trade-decoupling exposure (no UK adjacency); squeeze arrives via decoupling, not via cross-border capital flight |
| **Continental** | BE, DE, FR, NL | Worker-protection plus UK adjacency plus Mode 1 capital-flow vulnerability — the canonical jurisdictional-buffering profile |
| **LU correction** | (LU is NOT squeeze-flagged) | LU's `squeeze_flag.binary = false` in the SOT (asymmetry score 0.6436); the earlier narrative had wrongly grouped LU with the Continental sub-cluster. LU's Class I status rests on its standalone Continental Corporatist profile + S2-dependent optimism path (§4.3), not on any squeeze designation. |

This resolves the Phase 2 open question — *is the squeeze pattern a genuine institutional finding or a methodology over-fit?* — in favour of the genuine-finding reading: the pattern decomposes cleanly into two sub-clusters with mechanistically distinct generators (decoupling-driven Nordic, UK-adjacency-driven Continental) rather than collapsing under interrogation. The Bundle K-2 Lens 5(c) coordination-share test had asked whether BE and NL pattern-match the *EDUCATION / ADMIN LIFT* (LU, NO, IS, DK) or *FINANCE / TECH DRAG* (CH, DE, IE, UK) archetype. The answer remains no — BE drag composite 0.500, NL 0.478 sit within the Continental knowledge-economy mid-range and pattern-match neither archetype cleanly.

The squeeze flag is therefore not a coordination-share signal — it is preserved as an orthogonal capital-flight signal driven by jurisdictional buffering. Quantification rests on per-country counts of approximately 40 high-risk Annex III deployer occupations and approximately 29 PWD post-market duty occupations, plus an asymmetry score that ranges 0.6333–0.6650 across the 36 markets (a tight 0.03 span — the asymmetry score is a weak per-country differentiator on its own; the Lens 1 regulated-absorption-friction score, range 0.46–0.68, is the stronger signal Bundle Q surfaced).

This is a finding that does not change a corridor assignment but changes an advisory recommendation. A board reader looking at one of the eight squeeze-flagged countries and asking "is the squeeze flag a signal of imminent labour-market displacement?" gets the answer "no — it is a signal of capital-flight risk (Continental sub-cluster) or trade-decoupling exposure (Nordic sub-cluster), mechanistically independent from displacement velocity." Two distinct mechanisms warrant two distinct mitigations; conflating them under a single "squeeze" headline would mis-allocate institutional response capacity.

---

## 5. Fragility-class country profiles

Each profile: name + corridor + scale tag + the SOT one-liner, with a sentence of mechanism. Countries clustered by class; alphabetical by code within class.

### 5.1 Class I — Robust (relative-stable, C3-guarded) — 9 countries

- **BE — Belgium** (C2, both): *Squeeze-flag Class I; Mode 1 vulnerability + capital-flight risk; both scales.* Continental Corporatist sub-cluster; reaches C1 under {S1, S5, S2}; breach flag carried.
- **DK — Denmark** (C1, both): *Nordic Class I + breach (DK marginal entry at 2-digit); Bundle K-2 effect; squeeze-flag Nordic sub-cluster (worker-protection × trade-decoupling).* Highest composite drag among breach Nordics (0.555); growth-baseline S1 still serves as recovery channel.
- **FI — Finland** (C1, both): *Nordic Class I + post-growth; squeeze-flag Nordic sub-cluster.* Recovery path runs through S2 under post-growth; not in 2-digit breach list (drag 0.535).
- **FR — France** (C2, both): *Squeeze-flag Class I; post-growth; Continental Corporatist.* Reaches C1 under {S1, S5, S2}; cascade priority high under post-growth fiscal-headroom contraction.
- **IS — Iceland** (C1, both): *Nordic Class I + breach + small island; cascade priority medium.* Knowledge-economy ICT mass plus 2-digit confidentiality suppression caveat (36/43 codes coverage).
- **LU — Luxembourg** (C2, both): *Post-growth + breach + S2-dependent; aggregate-distributional split.* The s2-dependent profile (§4.3) overlaps with Class I status: rest stable C2, S2 is sole C1 path.
- **NL — Netherlands** (C2, both): *Squeeze-flag Class I; Mode 1 vulnerability + breach; medium S8 priority.* Reaches C1 under {S1, S5, S2}; squeeze profile is orthogonal jurisdictional buffering (§4.5).
- **NO — Norway** (C1, both): *Nordic Class I + post-growth + breach; squeeze-flag Nordic sub-cluster; cascade priority high (post-growth fiscal headroom).* Sovereign-wealth fiscal headroom intact; S2 natural fit (offshore wind, maritime decarbonisation).
- **SE — Sweden** (C1, both): *Nordic Class I knife-edge + post-growth + breach; squeeze-flag Nordic sub-cluster; class_i_confidence=medium.* Bundle H S7 ≥ 0.20 knife-edge resolves to within-Class-I sensitivity band; SE entered breach at 2-digit (highest Klinger weighted among breach Nordics, 0.590).

### 5.2 Class II — Fragile — 9 countries

- **AT — Austria** (C2, aggregate): *Post-growth + S2-dependent: optimism path runs through climate Zone-C wage premium; S7 cascade reaches C3.* Among the 9 countries reclassified out of Class I by the Q1 asymmetric-guard lock indirectly — AT was Class II before; the same logic guards it from drifting up.
- **BA — Bosnia and Herzegovina** (C2, aggregate): *Partial-coverage Class II preserved (no extreme readings); CEE growth-baseline.* Routed to `central_eastern_european_in_c2` per Bundle M (§8.5).
- **BG — Bulgaria** (C2, aggregate): *Growth-baseline C2 reaching C3 only under S6/S7 stress; aggregate.* Reclassified I → II under Q1 asymmetric-guard lock — its C2 baseline reaches C3 under S6 / S7, semantically inconsistent with "Robust."
- **CH — Switzerland** (C2, aggregate): *Post-growth + breach + Continental knowledge-economy; reaches C3 under S6/S7.* Reclassified I → II under Q1 asymmetric-guard. *FINANCE / TECH DRAG* archetype (§4.4) — ICT mass overweights.
- **DE — Germany** (C2, both): *Post-growth + breach + squeeze flag; Europe's largest economy in S4 vulnerability.* Reclassified I → II under Q1 asymmetric-guard. The combined post-growth, breach, and squeeze-flag profile makes DE the highest-bandwidth case in Class II.
- **ES — Spain** (C2, aggregate): *Growth-baseline C2 (just below C3 floor); reaches C3 under S6/S7.* Reclassified I → II under Q1 asymmetric-guard. Southern-European-in-C2 sub-cluster; the only C2 country in that sub-cluster.
- **LI — Liechtenstein** (C2, aggregate): *Post-growth + breach proxied via CH; tiny economy, low cascade priority.* Reclassified I → II under Q1 asymmetric-guard. Breach is proxied via CH per Bundle K-2 routing.
- **LV — Latvia** (C2, aggregate): *Growth-baseline C2 (close to C3 floor); reaches C3 under S6/S7 stress.* Reclassified I → II under Q1 asymmetric-guard. Demographic decline + ALMP capacity strain.
- **RO — Romania** (C2, aggregate): *Growth-baseline C2; reaches C3 under S6/S7; lowest Klinger weighting at 2-digit.* Reclassified I → II under Q1 asymmetric-guard. Lowest 2-digit Klinger weighted score in the C2 cluster.

### 5.3 Class III — Pre-Failure Risk — 15 countries

**Capacity-side anchor (Bundle R, 2026-04-30).** The Class III "reskilling pathway is materially insufficient" framing rests on a central capacity calculation. Across EU-27 plus the United Kingdom, the deep-reskilling cohort by 2035 is approximately **7.55 M workers** (Bundle R `cross_cutting_findings.reskilling_capacity_gap.deep_reskilling_need_eu27_uk_m`). Annual training-system throughput across all channels — university adult learning, VET apprenticeships, corporate L&D, government ALMP, bootcamps, microcredentials — is approximately 3.34 M per year, but ~2.89 M of that is consumed by baseline economic churn (Eurostat lfsa_etpgan tenure-under-1yr proxy), leaving approximately **450 K of net new annual capacity** available for AI transitions. Divided into the 7.55 M cohort, the implied backlog is **15 years**. The AI-vs-system speed gap runs **5–9 years**: AI disrupts in 1–3 years; European VET and university systems respond in 5–9 years for clerical, customer-service, writers/translators, and similar Zone A occupations. Even allocating disproportionately to Class III absorbs only marginal share of the deficit without channel expansion. This is the quantitative spine of the Class III diagnosis below; it bites independent of which routine scenario realises.

- **CY — Cyprus** (C3, distributional): *Class III by Muddle Through; distributional.* CEE / Mediterranean weak-ALMP sub-cluster.
- **CZ — Czechia** (C3, distributional): *Class III by Muddle Through; CEE weak-ALMP regime.* Ratio in 2.81–2.96 band; structural-bias-corrected entry.
- **EE — Estonia** (C3, distributional): *Class III; digital-state but caught by structural-bias adjustment.* Digital-state branding does not insulate against the 2.80 floor.
- **EL — Greece** (C3, distributional): *Secular stagnation + Class III; both scales.* Secular-stagnation regime; S8 conditional probability rises to 0.10.
- **HR — Croatia** (C3, distributional): *Class III CEE; sharpest_decline tier.* Demographic-decline sharp-tier; growth-baseline regime.
- **HU — Hungary** (C3, distributional): *Class III CEE; unassigned-tier proxy.* Phase 2 unassigned-tier proxy; growth-baseline.
- **IE — Ireland** (C3, both): *Liberal Market Class III + breach + S8 high-priority; expected_corridor near C3.* Liberal Market high sub-cluster (ratio 3.33–3.40); knowledge-economy concentration plus weak ALMP.
- **IT — Italy** (C3, distributional): *Secular stagnation + Class III + post-growth aggregate; both scales.* Secular-stagnation regime; S8 conditional 0.10.
- **LT — Lithuania** (C3, distributional): *Class III CEE; sharpest_decline tier.* Demographic-decline sharp-tier; structural-bias-corrected entry.
- **MT — Malta** (C3, distributional): *Class III sparse-data island; small but post-recalibration C3.* Sparse-data island flagged; post-recalibration entry.
- **PL — Poland** (C3, distributional): *Sentinel Class III; structural-bias adjustment locked.* Sentinel — confirms the structural-bias correction landed in the right place.
- **PT — Portugal** (C3, distributional): *Class III; demographic decline + fragmented ALMP.* Demographic decline plus fragmented ALMP capacity.
- **SI — Slovenia** (C3, distributional): *Class III CEE; unassigned-tier proxy.* Phase 2 unassigned-tier proxy; growth-baseline.
- **SK — Slovakia** (C3, distributional): *Class III CEE; unassigned-tier proxy.* Phase 2 unassigned-tier proxy; growth-baseline.
- **UK — United Kingdom** (C3, both): *Liberal Market Class III + breach + post-growth + S8 high-priority.* Liberal Market high sub-cluster; the post-growth-regime member of the IE / UK pair, raising S8 conditional to 0.15.

### 5.4 Class IV — Currently Failing — 3 countries

- **MK — North Macedonia** (C2, distributional): *Candidate-partial-coverage Class IV; vuln 0.62.* Routed to `central_eastern_european_in_c2` for sub-cluster purposes (§8.5); EEA-vulnerability reading 0.62.
- **RS — Serbia** (C2, distributional): *Candidate-partial-coverage Class IV; poly 0.55, eea_vuln 0.60.* Polycrisis composite 0.55, EEA-vulnerability 0.60; the median of the three Class IV readings.
- **TR — Turkey** (C2, distributional): *Candidate-partial-coverage Class IV; poly 0.67, eea_vuln 0.75, gini 44.8.* Highest Class IV polycrisis reading (0.67); also s2-dependent (§4.3) — the climate-Zone-C optimism path is the only route to C1.

Ukraine carried separately as Class IV reference panel — see §7.

---

## 6. Scenario probability stack

Probabilities are quoted as IPCC AR6 likelihood-scale band ranges per regime, with the 80 % CI from the structured-elicitation methodology (Cooke 1991-style, anchored per scenario × regime in the SOT JSON `methodology_anchors` block). Seven routine variants sum to 1.0 per regime; S8 is conditional and orthogonal.

| Regime | S1 | S2 | S3 | S4 | S5 | S6 | S7 | (S8 cond.) |
|---|---|---|---|---|---|---|---|---|
| growth_baseline | 0.10 [0.05–0.15] | 0.20 [0.15–0.25] | 0.10 [0.05–0.15] | 0.25 [0.20–0.30] | 0.15 [0.10–0.20] | 0.12 [0.07–0.17] | 0.08 [0.03–0.13] | 0.05 |
| secular_stagnation_warning | 0.07 [0.04–0.12] | 0.25 [0.20–0.30] | 0.05 [0.02–0.10] | 0.23 [0.18–0.28] | 0.15 [0.10–0.20] | 0.13 [0.08–0.18] | 0.12 [0.07–0.17] | 0.10 |
| **post_growth_empirical** | **0.05** [0.02–0.10] | **0.30** [0.25–0.35] | 0.08 [0.03–0.13] | 0.22 [0.17–0.27] | 0.13 [0.08–0.18] | 0.13 [0.08–0.18] | 0.09 [0.04–0.14] | **0.15** |

Routine sums (S1–S7) per regime: 1.00 / 1.00 / 1.00. S8 is conditional and orthogonal. Cells quote the central probability with the 80 % CI band in brackets, drawn from `layer-6-deliverable-data.json scenarios.{Sx}.probability_per_regime`.

Anchors: S1 is bounded above by demographic-buffer orthogonality (§4.2) plus Autor 2024 weakening reinstatement; under post-growth, S1 mechanism requires expanding output (locked spec line 92–94) so probability drops to 0.05. S2 strengthens under post-growth (line 96, 104) — sectoral redirection within flat aggregate, the only genuinely-positive scenario surviving the regime check, conditional on works-council mediation and procurement-attached social conditionalities (ETUC; IndustriAll Europe); probability rises to 0.30, dominant. S3 Jobs Transform — within-occupation task augmentation rather than between-occupation displacement (Brynjolfsson Li Raymond 2023 anchor) — sits at 0.10 in growth-baseline, falls under stagnation, and modest in post-growth. S4 baseline anchors at ~0.25 across regimes with a small downshift under post-growth as S2 / S6 / S7 absorb mass. S6 / S7 rise under stagnation and post-growth (lines 98-99) because fiscal headroom for institutions shrinks and bandwidth-saturation thresholds drop. S8 is conditional — Ukraine is the empirical anchor — and rises with regime severity (g = 0.05 → s = 0.10 → p = 0.15).

The sentinel test (S2 modal under post-growth) PASSED: P(S2 | post-growth) = 0.30 exceeds P(S4 | post-growth) = 0.22. Per-country distribution sentences in §5 quote the 80 % corridor-mass range, not point estimates, in band language — `Likely`, `More likely than not`, `About as likely as not` — per the IPCC AR6 likelihood scale.

The 36-country distribution sentences in the SOT JSON quote both the dominant corridor and the routine-variant mass range in the country's regime. Reading example: NO under post-growth — "Likely in C1 (Managed Transition) with ~46–99 % routine-variant mass under post-growth-empirical." The lower bound 46 % reflects the asymmetric-guard's tightest binding under S6 / S7 stress; the upper 99 % reflects the case where S2 dominates and S1 / S3 / S4 / S5 also resolve to C1.

---

## 7. Ukraine reference panel

Ukraine is the empirical Class IV anchor and is **not corridor-mapped per locked spec line 341.** The Layer 1 / 4 / 5 backporting required for corridor-map participation would consume 2–3 weeks of fetch-and-score work; the analytical value of that work is dominated by the panel role Ukraine already serves.

`lens5_inputs_at_maxima`: military expenditure 40 % GDP (SIPRI 2025: USD 84.1 bn 2024); demographic collapse from refugee outflow plus war casualties; reskilling infrastructure war-damaged. The function is to calibrate the upper bound of the Lens 5 polycrisis composite without forcing Ukraine through a corridor classification that does not apply — institutional bandwidth is saturated by definition; capability floor is breached by definition; corridor C1 / C2 / C3 distinctions are operationally moot in this state.

The 36-country corridor narrative therefore treats Ukraine as a reference panel: cited (Bundle G IISS extracts; Bundle D handover; locked spec §line 341), tagged `not_corridor_mapped = true`, and used to anchor the Class IV "Currently Failing" rule. The three corridor-mapped Class IV countries (MK, RS, TR) sit below the Ukraine ceiling on Lens 5 readings, which is the reason the rule produces three rather than zero or thirty.

---

## 8. Methodological appendix

### 8.1 Threshold-locking ladder (Phase 1 → Phase 3)

Phase 1 fitted the corridor edges to historical literature: C1 < 1.50, C3 ≥ 3.00. Phase 3 Bundle J replaced these with the theory-anchored 1.20 / 2.80 pair, anchored on three independent sources: (i) Phase 1 sub-cluster boundaries — Nordic cluster ends at 1.10 and the next cluster begins at 1.59, leaving an empirically empty band where the Phase 1 cap had floated; (ii) Autor et al. QJE 2024 documenting reinstatement-effect weakening, which lowers the historical-base-rate-derived ceiling on "managed transition"; (iii) El-Sahli & Upward 2017 NDLS evidence on structural lifetime-earnings deficits among displaced workers in C3-equivalent regimes. The result: Class I count under literal-strict (b) ±0 rule dropped to 0 — even spec-anchor Nordics failed strict robustness — making the strict-zero finding the structural-bias headline (§4.1).

### 8.2 Class I rule trail (3-stage: S8-orthogonal → relative-stable → asymmetric-guard)

The Class I rule passed through three stages, each with an empirical trigger:

```
Stage 1 — Phase 2 S8-orthogonal
  Rule:    Class I scope restricted to S1–S7; S8 cascade carried as orthogonal conditional.
  Trigger: Lens 5 cascade dynamics are mechanistically distinct from routine-variant displacement velocity;
           folding S8 into the perturbation grid would conflate two failure modes.

Stage 2 — Phase 3 Bundle J relative-stable
  Rule:    Class I = ±1 of baseline; max|scenario − baseline| ≤ 1 across S1–S7.
  Trigger: Bundle J literal-strict ±0 returned Class I = 0 under the new 1.20 / 2.80 thresholds.
           Strict-stable rule was restored to its draft-spec sense (relative stability across
           the perturbation grid, not absolute identity).

Stage 3 — Phase 3 Bundle L Q1 asymmetric-guard 2026-04-29
  Rule:    Class I = ±1 of baseline AND no routine variant assigns the country to C3.
  Trigger: Bundle L Q1 lock — naive carryover of the Stage 2 rule produced Class I = 16
           including 7 countries (CH, DE, LI, BG, ES, LV, RO) whose C2 baseline reaches C3
           under S6 / S7. Semantically inconsistent with "Robust"; the asymmetric guard
           preserves institutional-pattern semantics. Aligns with locked-spec line 387
           original expectation (5 Nordics + NL; CH falls out as expected under
           structural-bias-corrected thresholds).
```

The strict-zero finding from Stage 2 is preserved in the methodology trail as the structural-bias validation headline (§4.1), not deleted by Stage 3's restoration of Class I to 9.

### 8.3 Capability-floor breach scope ceiling (12 countries / 2-digit)

The capability-floor breach final scope is **12 countries**: BE, CH, DE, DK, IE, IS, LI, LU, NL, NO, SE, UK. DK is the marginal entrant at 2-digit. The trajectory was: Phase 2 baseline = 3 countries → Bundle K 1-digit = 11 → Bundle K-2 2-digit = 12. Cascade priority distribution: HIGH = 7, MEDIUM = 4, LOW = 1.

The scope ceiling is the ISCO 2-digit limit — Bundle K-2 ESCO-count-weighted 3-digit-to-2-digit aggregation. The 3-digit ESS microdata path requires a multi-week Eurostat application, flagged as a Phase 5+ enhancement candidate in the Phase 4 plan Q5 lock. Readers should note that the DK marginal entry is sensitive to the 3-digit ceiling: at 3-digit, DK's breach status would resolve cleanly, and the 12-country list could expand by 1–2 more entrants in the Continental knowledge-economy band. The 12-country read should be treated as a lower bound at the 2-digit aggregation level.

### 8.4 MFF per-country allocation gap

The SOT JSON field `lens5a_eu_mff_allocation` per-country share is **null** — by design. The €64.6 B MFF mid-cycle reinforcement (Ukraine €50 B + migration €2 B + emergency €1.5 B + STEP and other components) is not disaggregated per Member State in publicly available Council documentation. The reinforcement is a bandwidth-allocation proxy at the EU aggregate level — its existence *is* the concurrent-crisis tax on regular spending priorities, which is the political-economy signal Lens 5 captures. The site Lens 5 panel therefore renders aggregate only. **This is a known gap, not an error.** Phase 5+ candidate enrichment via national contribution / rebate analysis is flagged in the Phase 4 plan.

### 8.5 Candidate-country C2 sub-cluster routing (BA / MK / RS / TR)

The four candidate-partial-coverage countries — Bosnia and Herzegovina, North Macedonia, Serbia, Turkey — sit at C2 baseline but lack the Phase 1 institutional-system tags assigned to confirmed EU / EFTA / UK cases. For C2 sub-cluster purposes they are routed to `central_eastern_european_in_c2` alongside BG, LV, RO. The provenance is preserved in the SOT JSON with `_system_p1: candidate-baseline (CEE+SE weighted avg)` — explicitly flagging that the institutional-similarity proxy is a weighted average over CEE plus Southern European cases, not a direct institutional-system match.

Readers should not conflate candidate-baseline-proxied sub-clustering with confirmed institutional similarity. The routing is an analytical convention: for C2 sub-cluster purposes BA / MK / RS / TR are tagged `central_eastern_european_in_c2`; the underlying institutional-system tag is a CEE+SE weighted-average proxy. MK and RS additionally carry the Class IV currently-failing flag (§5.4); TR is both Class IV and `s2_dependent` (§4.3 / §5.4). The convention is preserved inside the SOT JSON country block and surfaced here so downstream readers do not over-interpret the cluster assignment as a confirmed institutional finding.

### 8.6 Phase 5+ enhancement candidates

(1) ESS microdata 3-digit ESCO breach scope expansion (multi-week Eurostat application); (2) MFF per-country allocation via national contribution / rebate analysis; (3) Layer 1 / 4 / 5 backporting for Ukraine to enable corridor-map participation under a wartime-economy variant. None block the Phase 4 deliverable surface.

---

## 9. Sources and provenance

**Source bundles** compiled in the SOT JSON `metadata.source_bundles`: Phase 1 (lens 1/2 scoring); Bundle B (4-country candidate appendix); Bundle D (Phase 2 lens 4/5 scoring); Bundle H (drag-multiplier robustness probe); Bundle I (corridor modifier reconciliation); Bundle J (structural-bias recalibration, 1.20 / 2.80); Bundle K-2 (Klinger ISCO 2-digit + breach scope); Bundle L (scenario-realisation probability + Phase 3 closure); Bundle M (deliverable SOT JSON composition); Bundle V (scenario reframe: 8 scenarios + S3 Jobs Transform); Bundle W (Phase 3 + 3.5 + deliverable propagation, including the S2 mechanism-string additive on works-council mediation and procurement-attached social conditionalities).

**Per-field provenance** is preserved in the SOT JSON `_provenance` sibling block per country — including `fragility_class` (Bundle L), `phase3_corridor` (Bundle J), `expected_corridor` (Bundle L), `lens5_composite_drag_2digit` (Bundle K-2 via Bundle L), `klinger_weighted_2digit` (Bundle K-2), `squeeze_flag` and `lens4_shock_count` (Bundle D / Phase 2), `breach_flag` (Bundle K-2), `s2_dependent` (Bundle L), `scenario_distribution_language` (Bundle M composed from Bundle L scen_corr × Bundle L probability_vectors). Schema v1.0 of the SOT JSON locked Bundle M, 2026-04-29; mechanism-string additive landed Bundle W Phase 1, 2026-05-08.

**Primary sources — 59 total (41 Tier 1 + 18 Tier 2).** The canonical list mirrors `site/sources.html` and `site/llms.txt`:

**Tier 1 (41).** Autor, Chin, Salomons & Seegmiller 2024 (QJE); El-Sahli & Upward 2017; Cedefop 2025 (European Skills and Jobs Survey + Skills Forecast); EU Net-Zero Industry Act + Clean Industrial Deal 2025; EEA European Climate Risk Assessment 2024; Munich Re NatCat 2025; IISS Military Balance 2025; SIPRI Trends in World Military Expenditure 2025; EU MFF Mid-Term Review 2024; NATO Hague Summit Declaration 2025 / ReArm Europe / Readiness 2030; Eurostat EUROPOP2023 + lfsa_etpgan; **Mario Draghi 2024** (Future of European Competitiveness); Anthropic Economic Index (Handa et al. 2025); Massenkoff & McCrory 2026; Microsoft Working with AI (Tomlinson et al. 2025); OpenAI GPTs are GPTs (Eloundou et al. 2023); Eurostat isoc_eb_ai (Enterprise AI adoption); Eurostat isoc_sks_itspt (ICT specialists); Eurostat lfsa_egai2d (Employment by ISCO 2-digit); OECD EPL Database; Brynjolfsson, Chandar & Chen 2025 (Canaries in the Coal Mine); **Brynjolfsson, Li & Raymond 2023** (Generative AI at Work, NBER WP 31161); Acemoglu & Restrepo 2020 (Robots and Jobs); Acemoglu & Restrepo 2019 (Automation and New Tasks); Feigenbaum & Gross 2024 (Telephone Operation, QJE); Card, Kluve & Weber 2018 (ALMP meta-analysis); Dauth, Findeisen, Südekum & Wößner 2021 (German Robots, JEEA); Jacobson, LaLonde & Sullivan 1993 (Earnings Losses); European Commission 2024 Ageing Report; OECD Old-age dependency ratio; UN Population Division WPP 2024; IMF WEO 2026; OECD Economic Surveys EU 2025; Bertheau et al. 2022 (IZA DP 15033); OECD SOCX ALMP; Eurostat trng_aes_100 (Adult Education Survey); Eurostat older-worker employment rate 55–64; **ILO 2025** (Generative AI Occupational Exposure Index — reclassified Tier 1 Phase 2F); **Rhodium / MIT Clean Investment Monitor (IRA tracker)** (Bundle W Phase 3.5); **Bistline et al. 2024 (NBER WP 32168 / Brookings)** (Bundle W Phase 3.5); **OECD Pension Markets in Focus 2025** (Bundle W Phase 3.5).

**Tier 2 (18).** Klinger 2-digit ISCO coordination-share weighting; Tooze (Chartbook 130 + 407, framing-vs-mechanism distinction the Lens 5 spec deliberately separates from); Cooke 1991 expert-elicitation framework; IPCC AR6 likelihood scale; EU AI Act (Regulation 2024/1689); Hall & Soskice 2001 (Varieties of Capitalism); Acemoglu & Johnson 2023 (Power and Progress); Brynjolfsson, Rock & Syverson 2021 (Productivity J-Curve); Frey 2019 (Technology Trap); Feigenbaum & Gross 2025 (AT&T, Management Science); Autor, Dorn & Hanson 2013 (China Syndrome); Bruegel 2025 (Demographic Divide); OECD Pensions at a Glance 2023; Allianz Research 2024 (Migration matters); European Parliament 2025 (Displaced Ukrainians); EURES / European Labour Authority 2024 (Labour Shortages and Surpluses); **ETUC 2026-03-04 press release (Industrial Accelerator Act)** (Bundle W Phase 3.5); **IndustriAll Europe 2026 Article 1450 (Made in Europe 2.0)** (Bundle W Phase 3.5).

Full source-cards with brief + "How informs" line and live links: see [synthesis.nexalps.com/sources.html](https://synthesis.nexalps.com/sources.html).
