# Cross-Layer Enrichment Audit — Layer 6 ← Layers 1–5

**Build:** 2026-04-30 · Read-only audit per `cross-layer-enrichment-audit-handover-2026-04-30.md`. No Layer 6 modifications. Goal: surface the full set of enrichment opportunities sitting in L1–L5 that L6 currently underuses, so Phil can decide which bounded re-Phase-3 bundles to commission before Bundle O dispatches.

**Method.** For each layer: read README + llms.txt + headline data, then map each load-bearing finding against L6's SOT JSON country fields and the Specialist Appendix narrative. Score each underuse by Strength × Cost × Knock-on. Bundle P (L4 / Lens 2) is the prior-discussion anchor.

---

## Summary table

| Layer | High-priority opportunities | Medium-priority | Low-priority / scope-boundary |
|---|---|---|---|
| **L1 — AI Exposure** | 2 (regulatory-overlay coverage; UK regulated_score asymmetry) | 2 (exposure-weighted wages; ISCO 3-digit fidelity) | 1 scope-boundary |
| **L2 — Job Market** | 2 (entry-level collapse / Gen Z exclusion; AI/ML +88% as Lens 1 demand-side) | 2 (per-country salary-growth heterogeneity; regulatory demand drivers NIS2/DORA/CSRD) | 1 scope-boundary |
| **L3 — Disruptions** | 1 (5-pattern-type taxonomy as country-level overlay) | 2 (age-50 cliff distributional finding; 9% generational transmission) | 1 scope-boundary (6 diagnostic variables — already absorbed via Bundle K) |
| **L4 — Demographics** | 3 (Bundle P: country-level retirement-offset + Zone A/B/C/D matrix; per-country working-age decline projections; net-migration arithmetic per country) | 2 (four-generational-crisis frame; historical precedents panel) | 1 scope-boundary |
| **L5 — Reskilling** | 2 (per-country A→C rate as Lens 1 absorption refinement; aggregate 7.55M / 450K / 15-year backlog as Class III math anchor) | 2 (six lenses + diagnostic metric "internal transition speed vs external turnover"; reform-velocity composite DE 5 / AT 3 / CH 1) | 1 scope-boundary |
| **TOTAL** | **10 high** | **10 medium** | **5 low / scope-boundary** |

---

## Per-layer detail

### Layer 1 — AI Exposure

Source: `/Users/philippmaul/Documents/projects/european-ai-exposure-map/` — README, `site/llms.txt`, `site/data.json`, `scores.json`, `uk_scores.json`. Load-bearing findings:

1. **Regulatory delta as a country-modulated signal** (avg 1.2 points EU vs 0.5 UK). 40 high-risk AI deployers under EU AI Act Annex III; 125 groups trigger Art 26(7) worker-representation; 31 groups trigger Platform Work Directive.
   - **L6 use: ABSENT.** SOT JSON `lens1_displacement_velocity` per country uses regulated_score in aggregate but does not surface the deployer/Art 26(7)/Platform Work Directive overlay structure. Specialist Appendix mentions "EU AI Act material change to absorption capacity" as a Lens 1 question but the answer is not encoded per-country.
   - **Strength: HIGH** — directly modulates Lens 1 absorption capacity. The 40-deployer × 36-country × Art 26(7)-trigger matrix is a country-specific buffer signal that's load-bearing for the structural-bias debate (does EU regulation actually reduce displacement velocity, or is it regulatory theater?).
   - **Cost: medium** (60–90 min sub-session) — L1 already has the structured overlay; L6 needs a Lens 1 sub-field per country.
   - **Knock-on:** Specialist Appendix §4.1 + §4.5 (squeeze flag mechanics) + Executive §2 + glossary (need entries for Annex III / Art 26(7) / PWD) + One-Pager finding 1 + Bundle N3 Long-Read structural-bias section.
   - **What enrichment would look like:** new SOT JSON field `lens1_regulatory_overlay` per country with `{deployer_count, art26_7_count, pwd_count, regulatory_delta_points}`. Specialist Appendix §4.1 gains a paragraph: "the regulatory-delta gradient (EU 1.2 → UK 0.5) is itself a Lens 1 absorption-capacity input — and the 31-group Platform Work Directive overlay closes the freelance/platform coverage gap (locked spec lines 178–183) earlier in countries that transposed quickly."

2. **UK regulated_score as separate scoring track** (uk_regulated_score, 0.5 regulatory delta vs EU's 1.2).
   - **L6 use: LOSSY.** UK appears in C3 (Liberal Market high, ratio 3.33–3.40), and "weak ALMP plus high knowledge-economy concentration" is cited (§3 Corridor-3 read), but the UK-specific regulatory-friction asymmetry (DSIT pro-innovation framework vs EU AI Act) is not itself encoded as a Lens 1 modifier for UK. The Lens 1 ratio uses regulated_score for EU and uk_regulated_score for UK, but the *asymmetry between them* — which is itself Lens 4 jurisdictional-buffering input — is not surfaced.
   - **Strength: HIGH** — directly relevant to Lens 4 squeeze-flag reasoning (BE/NL adjacency to UK weak-protection; locked spec lines 271–289). Currently the squeeze flag is a binary; the L1 UK delta gives it quantitative shape.
   - **Cost: small** (<30 min) — the data exists; L6 needs to expose `eu_uk_regulated_delta` per country in Lens 4.
   - **Knock-on:** Specialist Appendix §4.5 (BE/NL squeeze finding) + Executive §3 + glossary.
   - **What enrichment would look like:** Lens 4 squeeze-flag block gains a numeric `regulatory_asymmetry_to_uk` field; §4.5 paragraph quantifies the squeeze rather than asserting it.

3. **Exposure-weighted wages** (~€4.7T technical vs ~€3.7T regulated; the €1T regulatory wedge).
   - **L6 use: ABSENT.** Layer 6 corridor map quotes counts and ratios; nowhere does it monetise the wage stock at risk per country.
   - **Strength: MEDIUM** — powerful headline for executive/board readers; not load-bearing for the corridor-class methodology but high-impact for distribution.
   - **Cost: small** (<30 min).
   - **Knock-on:** Executive §1 (could anchor the "why this synthesis exists" paragraph) + One-Pager headline + Einfache versions.
   - **What enrichment would look like:** SOT JSON `wage_at_risk_eur` per country; Executive opens with "€X trillion of wage stock sits inside the C2/C3 corridor at the regulated_score threshold."

4. **ISCO 3-digit fidelity** (~130 groups). L6 currently runs Klinger join at 2-digit (Bundle K-2) with the explicit ceiling that 3-digit ESS microdata requires multi-week Eurostat application (§8.3, §8.6).
   - **L6 use: LOSSY.** The 12-country breach scope is explicitly flagged as a "lower bound at the 2-digit aggregation level" and Phase 5+ enhancement candidate. L1 itself has the 3-digit data already.
   - **Strength: MEDIUM** — would tighten the breach list and possibly add 1–2 entrants in the Continental knowledge-economy band (DK marginal entry would resolve cleanly).
   - **Cost: large** (>90 min) — requires re-running Bundle K-2 logic at 3-digit; possibly multi-week if ESS microdata is needed for the employment side. L6's current rate-limiter is the employment-distribution side, not the L1 side.
   - **Knock-on:** Specialist Appendix §8.3 + §4.4 + §5.1 (DK entry) + breach-flag fields throughout SOT JSON.
   - **What enrichment would look like:** Phase 5+ candidate, not Bundle Q-tier. Already in plan.

**Scope-boundary case:** L1's Adoption-survey data (`data/adoption/`) — sits in L1 because adoption is a separate construct from exposure; should not migrate into L6 as a separate input. Adoption modulates the velocity (timing) of how exposure becomes displacement; if needed, this belongs in **Layer 7** (Actions / Futureproof) where the prescriptive question is "given this adoption rate, what action?" — not in L6 (Synthesis).

### Layer 2 — Job Market

Source: `/Users/philippmaul/Documents/projects/european-careers-map/` — README, `site/llms.txt`, `site/job-market-data.json`. Load-bearing findings:

1. **Entry-level (P1/P2) hiring collapsed 73.4%; AI/ML +88% YoY; SDR-to-AE promotions halved 34→16%.**
   - **L6 use: LOSSY.** §1 mentions "P1/P2 hiring collapsed 73.4%" once in framing. But this is a *structural Gen Z exclusion finding* that should appear in Lens 4 (compounding shocks: AI displacement + generational labour-market entry collapse) and Lens 5 (institutional bandwidth: youth unemployment 15.1% per L4 generations.html competes for the same ALMP envelope). It's mentioned but not lens-encoded.
   - **Strength: HIGH** — distributional finding that the corridor framework currently aggregates away. Class III countries with high youth-unemployment carry a different cohort-incidence profile than Class III countries without.
   - **Cost: medium** (30–90 min) — needs per-country entry-level hiring data join to a Lens 4 sub-field.
   - **Knock-on:** Specialist Appendix §4.1 (structural-bias) + §4.5 + new sub-section under Lens 4; Executive §3; One-Pager finding 5; Einfache (cohort-impact paragraph).
   - **What enrichment would look like:** new Lens 4 sub-field `cohort_incidence` with `{entry_level_decline_pct, youth_unemployment_pct, ai_premium_pct}` per country.

2. **AI/ML specialist hiring +88% YoY; 12% IC salary premium; foundation-model companies grew employment 92% YoY; 50% increase in distinct AI/ML titles.**
   - **L6 use: ABSENT.** The Lens 1 absorption-capacity variable currently reads ALMP capacity. It does *not* read the demand-side data for AI/D-Zone roles — i.e., the Zone-D pull from L4 plus the L2 hiring growth on AI/ML titles. The orthogonality of "AI displaces" (Lens 1 numerator) and "AI creates demand" (Zone D, currently in L4 only) is asymmetric: L6 prices in the displacement, not the absorption-via-Zone-D component.
   - **Strength: HIGH** — directly affects the S1 Reinstatement Revival probability vector (locked spec line 92–94 says S1 requires growth-dependent new-work creation; L2 AI/ML growth IS that new-work creation, observable). If AI/ML growth is empirically holding at +88%, S1 may be stronger than the current 0.05–0.10 probability band suggests under post-growth.
   - **Cost: medium** (30–90 min) — refines S1 probability vector per regime; needs per-country AI/ML hiring rate join.
   - **Knock-on:** §6 scenario probability table (S1 vector revision per regime) + §4.3 (s2b-dependent finding may need re-test against revised S1 probabilities) + Executive §2.
   - **What enrichment would look like:** S1 probability band re-calibrated against L2 AI/ML hiring rate per country; per-country `s1_demand_side_anchor` SOT field.

3. **Per-country salary-growth heterogeneity** (NL 6.3%, DE/UK 5.0%, FR 3.9%, ES 4.0%, SE 4.1%; near-zero in Operations Sweden 0.2%).
   - **L6 use: ABSENT.** Country-level corridor map does not surface wage growth heterogeneity. Salary growth is a Lens 1 absorption-capacity signal (where wages are growing, displaced workers can move; where they're flat, they can't).
   - **Strength: MEDIUM** — useful as a cross-check on Lens 1 absorption ratios; correlations with the corridor map could surface anomalies (e.g., NL is C2 squeeze-flag yet has highest salary growth — what does that imply for the squeeze mechanism?).
   - **Cost: small** (<30 min).
   - **Knock-on:** Specialist Appendix §4.5 + §3 corridor reads + countries.html drilldown (Bundle O).
   - **What enrichment would look like:** SOT JSON `salary_growth_yoy` per country (where data exists); §4.5 cross-checks BE/NL salary trajectory against the squeeze hypothesis.

4. **Regulatory demand drivers: NIS2 (160K entities), DORA (22K firms), EU AI Act, EAA, CSRD.** 78% plan to hire 1–10 AI governance professionals.
   - **L6 use: ABSENT.** L6 mentions EU AI Act in passing but does not encode the *demand-side regulatory-induced hiring* as Lens 1 absorption capacity. NIS2 + DORA together create a quantifiable cybersecurity demand pull (424K European gap — also in L2).
   - **Strength: MEDIUM** — modulates Lens 1 absorption, particularly for the s2b-dependent countries and the C2 sub-clusters.
   - **Cost: medium** (30–90 min).
   - **Knock-on:** §3 corridor reads + §4.3 (optimism path could broaden — not just Climate Zone-C, also Cyber Zone-D under regulatory demand pull) + Executive §3.
   - **What enrichment would look like:** Lens 1 absorption capacity gains a `regulatory_demand_pull` component; cybersecurity 424K gap quoted as parallel optimism path alongside S2b.

**Scope-boundary case:** Tooling adoption rates (GitHub Copilot 35.6%) — sits in L2 because it's a hiring-side observation; the prescriptive question "should firms mandate Copilot" belongs in **Layer 7** (Actions), not L6.

### Layer 3 — Disruptions

Source: `/Users/philippmaul/Documents/projects/european-disruptions-map/` — README, `site/llms.txt`, `site/disruptions-data.json`, `retrofit-lag-reconstruction.md`. Load-bearing findings:

1. **5 disruption pattern types** (Type 1 Demand Creation, Type 2 Transformation+Expansion, Type 3 Absorption, Type 4 Restructuring, Type 5 Elimination). 6 diagnostic variables predict pattern.
   - **L6 use: LOSSY.** L6 uses the 3-corridor structure (Managed Transition / Bifurcated / Displacement) which is mechanistically related but not isomorphic to the L3 pattern taxonomy. A country can be "Managed Transition" overall while specific occupation clusters within it follow Type 5 elimination paths. The L3 pattern types are not surfaced as country-level overlays.
   - **Strength: HIGH** — directly addresses the §4.4 T34 "aggregation hides bifurcation" finding from a different angle. A C2 country's Lens 4 sub-cluster could be tagged with the dominant L3 pattern type for its largest at-risk ISCO group.
   - **Cost: medium** (30–90 min) — requires joining L3 case-to-ISCO mappings (containerisation→ISCO 933, etc.) onto L1's per-country employment distribution.
   - **Knock-on:** Specialist Appendix §4.4 (high-coord archetype split — finance/tech drag may pattern-match Type 5 elimination at task level via the sub-role task displacement angle, locked spec lines 185–188) + Bundle N3 Long-Read + countries.html drilldowns.
   - **What enrichment would look like:** SOT JSON `dominant_l3_pattern_type` per country (or per-country-cluster) with citation back to the calibrating case.

2. **Age-50 cliff: reemployment probability halved, earnings loss doubled.**
   - **L6 use: ABSENT.** L6 demographic findings are aggregate (working-age decline, dependency ratios). The age-50 cliff is a distributional finding that re-frames the Lens 2 orthogonality result: "demographic buffer fails *and* the displaced cohort has age-stratified absorption probability." Currently §4.2 reads as a flat refutation; the age-50 cliff would deepen it.
   - **Strength: MEDIUM** — high-impact for the Specialist Appendix audience (executive search principals especially); not load-bearing for corridor assignment.
   - **Cost: small** (<30 min) — primarily narrative; the L3 data is already cited.
   - **Knock-on:** Specialist Appendix §4.2 (orthogonality finding gains an age-cohort layer) + glossary + Bundle N3.
   - **What enrichment would look like:** §4.2 closing paragraph: "the orthogonality finding compounds with the age-50 cliff (L3): the 26% maximum retirement-offset is itself biased toward older cohorts whose displacement-to-reemployment penalty is itself worst — the buffer thesis fails on cohort dimension as well as scale."

3. **9% generational earnings transmission; 30–50 year geographic scarring (Rust Belt / UK coalfields).**
   - **L6 use: PARTIALLY (LOSSY).** Class IV historical anchors (Copperbelt, ABC, Latrobe) cite geographic scarring (locked spec line 390 / §5.4 references). 9% generational transmission is *not* in the document — it's the multi-generational angle of Class III "pre-failure risk" that the current taxonomy doesn't carry.
   - **Strength: MEDIUM** — distributional / temporal-horizon finding that reframes Class III stakes for advisory readers ("pre-failure risk isn't a single-decade story").
   - **Cost: small** (<30 min) — primarily narrative.
   - **Knock-on:** Specialist Appendix §5.3 (Class III block) + §5.4 + Executive §3.
   - **What enrichment would look like:** §5.3 opener gains a sentence: "Class III countries face not a single-decade scarring horizon but a 30–50 year geographic-cohort scar with 9% generational earnings transmission documented in the L3 case bank."

4. **6 diagnostic variables predict pattern (capital intensity × skill specificity × institutional buffering × task substitutability × adjacency × density).**
   - **L6 use: PARTIALLY ABSORBED.** The retrofit-lag-reconstruction document already feeds these variables into Lens 1's lag specification (per locked spec Open Question 3 RESOLVED 2026-04-14). Bundle K Klinger join uses coordination-share — adjacent to but not identical to the 6 variables.
   - **Strength: LOW–MEDIUM** — already largely operationalised.
   - **Cost: medium** if pursued; likely **not worth the cost**.

**Scope-boundary case:** ECB SAFE / ifo "AI is currently a net hiring driver" — empirical observation belongs in L2 (job market state) or L1 (exposure timing); L6 cites it implicitly via the regime-stability note but the headline-counterfactual framing belongs upstream, not as an L6 lens enrichment.

### Layer 4 — Demographics

Source: `/Users/philippmaul/Documents/projects/european-demographics-map/` — README, `site/llms.txt`, `site/demographics-data.json`. Load-bearing findings:

1. **Country-level retirement-offset data + Zone A/B/C/D substitution matrix.** 8–12M Zone C gap by 2030; AI substitutes 5–15% of Zone C tasks; 60–80% of Zone A tasks.
   - **L6 use: LOSSY.** SOT JSON Lens 2 field is the single string "refuted at scale (retirement_offset < 80% threshold)" per locked spec (§4.2: "rendered as a single-string field … rather than a country-by-country object — the content is uniform"). The 80% threshold is correctly refuted at scale but the *per-country, per-zone variation under it* is wholly suppressed. L4 has Zone-by-zone retirement gap (~3.5M Zone A / ~5M Zone B / ~12M Zone C / ~0.25M Zone D) that L6 does not surface.
   - **Strength: HIGH** — Bundle P anchor case. The Lens 2 single-string render is the most visible underuse in the entire deliverable. Per-country / per-zone reading would replace a flat "uniformly refuted" with a richer "refuted at aggregate; Zone C gap is the binding constraint; demographic load enters Lens 5 with country-specific shape."
   - **Cost: medium** (60–90 min sub-session) — Phil already discussed.
   - **Knock-on:** Executive §2 + Specialist Appendix §4.2 + One-Pager finding 2 + glossary + §5 limits + Einfache versions.
   - **What enrichment would look like:** SOT JSON `lens2_demographic_buffer` becomes a per-country object with `{retirement_offset_pct, zone_a_gap_M, zone_b_gap_M, zone_c_gap_M, zone_d_gap_M, working_age_decline_2050_pct}`. §4.2 narrative gains a "Zone C is the binding constraint" paragraph; the orthogonality finding sharpens rather than softens.

2. **Per-country working-age decline projections (EUROPOP2023): IT −17.5%, ES −12.9%, DE −12.0% by 2050; BG −29%, LV −28%; FR / IE outliers.**
   - **L6 use: ABSENT.** Country corridor classifications make no reference to per-country working-age decline trajectories. This is the timing variable for when the demographic load binds for each country. DE's classification as "Class II Fragile + post-growth + breach + squeeze" should compound with "−12% working-age by 2050" — but doesn't, in the SOT.
   - **Strength: HIGH** — feeds Lens 5(b) demographic-load composite which is currently a single score per country; the underlying time-series is suppressed. Critical for the s2b-dependent finding (§4.3) — AT/LU/TR are in different demographic-trajectory positions.
   - **Cost: medium** (60–90 min) — likely Bundle P sub-component.
   - **Knock-on:** §4.2 + §5 country profiles (every Class II/III/IV country gets a one-line demographic-trajectory tag) + glossary + §6 scenario probability table (S5 conditional probability scales with demographic load).
   - **What enrichment would look like:** SOT JSON `demographic_decline_trajectory` per country as `{working_age_2025_M, working_age_2050_M, decline_pct, peak_year}`.

3. **Net-migration arithmetic per country: DE needs 400K net migrants/year; 2024 net EU migration turned negative; without migration EU pop −60M by 2050.**
   - **L6 use: ABSENT.** L6 is silent on migration despite migration being the single largest variable for the demographic-load composite in Lens 5(b). The 4 candidate countries (BA/MK/RS/TR) plus Class IV-flagged are all migration-relevant in different directions.
   - **Strength: HIGH** — directly relevant to the s2b-dependent finding (climate Zone-C demand depends on Zone-C labour availability, which depends on migration policy) and the squeeze flag (BE/NL/FR/LU adjacency to UK is also a migration-policy adjacency).
   - **Cost: medium** (60–90 min) — Bundle P sub-component.
   - **Knock-on:** §4.3 + §4.5 + §5 + §6 (migration restrictiveness modulates S2b feasibility).
   - **What enrichment would look like:** SOT JSON `net_migration_2024` per country + `migration_political_constraint_flag` (proxy from L4 generations.html political constraints).

4. **Four generational crises: Boomer knowledge exodus (29% have transfer plans); Gen X frozen middle (12% L&D plan); Millennials max exposure / max adapt; Gen Z structurally excluded (−73%, 15.1% youth unemployment).**
   - **L6 use: ABSENT.** Generational stratification is not in any L6 lens. Cross-references both with L2 entry-level collapse and L3 age-50 cliff — three independent layers carry related distributional findings that L6 does not synthesise.
   - **Strength: MEDIUM** — distributional re-read of corridor assignments by cohort.
   - **Cost: medium** (30–90 min).
   - **Knock-on:** Specialist Appendix new sub-section under Lens 4 + Executive §3 + Bundle N3.
   - **What enrichment would look like:** Lens 4 sub-cluster `generational_incidence` per country with cohort-specific corridor reads.

5. **Historical precedents panel (Japan / China / Baltic / France / Black Death) for workforce-shrinkage recovery.**
   - **L6 use: ABSENT.** Class IV anchors (§5.4) cite Copperbelt/ABC/Latrobe for industrial-displacement scarring. The L4 demographic-shrinkage panel (Japan 30 years GDP stagnation, France 100-year recovery, Black Death structural-reorganisation-not-managed) is a parallel anchor set that L6 does not draw on. Particularly relevant for the post-growth regime block (DE/IT analogous to Japan).
   - **Strength: MEDIUM** — narrative depth for the §1 framing and the Regime Stability Note.
   - **Cost: small** (<30 min) — primarily narrative.
   - **Knock-on:** §1 + Specialist Appendix Regime Stability Note (currently in lens-framework.md, not yet in the deliverable document).
   - **What enrichment would look like:** Regime Stability Note section gains a "Japan as DE/IT analogue" anchor paragraph.

**Scope-boundary case:** L4 fertility data (TFR 1.34) — relevant to L4's structural thesis but not load-bearing for L6's 10-year horizon corridor map. Belongs in L4, not L6.

### Layer 5 — Reskilling

Source: `/Users/philippmaul/Documents/projects/european-reskilling-map/` — README, `site/llms.txt`, `site/reskilling-data.json`. Load-bearing findings:

1. **Per-country A→C transition rates by system model: Nordic 8–12%, Germanic Dual 3–6%, Continental 5–8%, Liberal 2.8–3.6% (UK), Southern 2–5%, CEE 2–5%.**
   - **L6 use: PARTIALLY (LOSSY).** Locked spec uses 6 system models for C2 sub-clusters; the *transition rate range* is referenced in spec (§4.3 "Layer 5 bounding constraint on Scenario 2") but not encoded per country in SOT JSON. The range 5–10% baseline → 12–15% required for S2b feasibility is the bounding constraint but per-country position within the range is not surfaced.
   - **Strength: HIGH** — directly modulates Lens 1 absorption capacity per country and the S2b probability per regime. UK at 2.8–3.6% is below the C2 sub-cluster average; that's a Lens 1 sharpening signal that the C3 classification of UK already captures aggregately but not at this granularity.
   - **Cost: medium** (30–90 min).
   - **Knock-on:** §3 corridor reads + §4.3 s2b-dependent finding (refines the AT/LU/TR triad — what's their A→C rate baseline?) + §5 country profiles + Executive §2.
   - **What enrichment would look like:** SOT JSON `lens1_a_to_c_rate` per country; §4.3 quantifies the s2b-dependent triad's distance from the 12–15% threshold.

2. **Aggregate scale: 7.55M deep reskilling need / 30.05M net 2035 / 3.34M throughput already saturated / 450K net new / 15+ year backlog clearance.**
   - **L6 use: ABSENT.** Class III corridor classification (15 countries) is the scaling result but the underlying L5 aggregate math (450K vs 7.55M = 16.7-year backlog) is not in the deliverable as the load-bearing math. This is the *quantitative anchor* for "structurally insufficient reskilling pathway" (§3 Corridor 3 read) but the document narrates it qualitatively.
   - **Strength: HIGH** — Class III math anchor. Without the 15+ year backlog quoted explicitly, "structurally insufficient" reads as assertion not evidence. With it, it's load-bearing.
   - **Cost: small** (<30 min) — primarily narrative integration; the L5 numbers are stable.
   - **Knock-on:** §3 Corridor-3 read + §4.1 (structural-bias) + Executive §1 + One-Pager finding 4.
   - **What enrichment would look like:** §3 Corridor-3 read paragraph adds: "the structural-insufficiency claim is anchored in L5: 7.55M deep-reskilling need by 2035 against 450K/year net throughput = 16.7-year backlog at current capacity, with no mechanism in the C2/C3 sub-cluster system models to close the gap."

3. **Six lenses in L5 (Haslauer, Klinger, Ronacher/Poncela Cubeiro, Weber GAAP/SBC, Andreessen, Poncela Cubeiro native-cohort) and the diagnostic metric "internal transition speed vs external turnover."**
   - **L6 use: PARTIALLY (LOSSY).** Klinger is heavily used (Bundle K, K-2). The other five lenses and the diagnostic metric (which is the BR-22 external-human variant validation finding from 2026-04-15) are absent. The L5 self-honest heat-map of which lens finds support where in the data is exactly the kind of structural-bias-aware artefact L6 should be drawing from.
   - **Strength: MEDIUM** — depth-additive rather than corridor-changing; relevant for Bundle N3 Long-Read.
   - **Cost: medium** (30–90 min).
   - **Knock-on:** Specialist Appendix new methodology sub-section + Bundle N3 + lenses.html (Bundle O).
   - **What enrichment would look like:** Specialist Appendix gains a "L5 lens cross-check" appendix; the diagnostic metric (internal transition speed vs external turnover) is encoded as a validation field per country where L5 has data.

4. **Reform-velocity composite (DE 5, AT 3, CH 1) and Germanic Dual hysteresis (24-month minimum; 3–5 year Ausbildungsordnung reform cycle).**
   - **L6 use: PARTIALLY (LOSSY).** AT/CH/DE all appear in Class II Fragile and the Germanic Dual sub-cluster; the *reform velocity differential* between them is not encoded (DE more reformable than CH per L5). This matters for Lens 5 institutional bandwidth.
   - **Strength: MEDIUM** — DACH-specific advisory finding; directly relevant to client positioning per locked spec Site Specification (`/dach.html`).
   - **Cost: small** (<30 min).
   - **Knock-on:** §5 country profiles for AT/CH/DE/LI + dach.html (Bundle O).
   - **What enrichment would look like:** SOT JSON `reform_velocity_score` per country (where L5 has it); DACH section gains a comparative read.

5. **Speed gap: AI disrupts in 1–3 years; systems respond in 5–9 years; 3–5 year structural lag for admin/customer-service/writers/translators.**
   - **L6 use: PARTIALLY.** Locked spec line 244 mentions Perez compression 4–5x and the political-vs-template decomposition. L5's specific 1–3y vs 5–9y reads as a parallel finding but is not lens-encoded.
   - **Strength: MEDIUM** — feeds Lens 1 lag specification (already partially done via L3 retrofit).
   - **Cost: small** (<30 min).
   - **Knock-on:** §2 methodology + glossary.

**Scope-boundary case:** L5 Singapore SkillsFuture benchmark (555K learners, 64% career-advancement) — comparator data belongs in L5 or L7 (Actions: "what would it take for Europe to match Singapore?"), not in L6 corridor narrative.

---

## Recommended bundles (priority-ranked)

| Bundle | Layer | Scope | Estimated cost | Recommendation | Sequence |
|---|---|---|---|---|---|
| **Bundle P** | L4 | Lens 2 demographic enrichment: per-country retirement-offset + Zone A/B/C/D substitution matrix + per-country working-age-decline trajectory + net-migration arithmetic. (Bundles L4-1 + L4-2 + L4-3 in the per-layer table; recommend single combined sub-session.) | ~90 min | **STRONG RECOMMEND** — already discussed, anchor case, replaces single-string Lens 2 with per-country object, knock-on across Executive / One-Pager / Einfache / Specialist Appendix / Bundle N3 / glossary. Highest knock-on density of any opportunity in the audit. | **Before Bundle O dispatches.** |
| **Bundle Q** | L1 | Lens 1 regulatory overlay: encode 40-deployer × Art 26(7) × PWD per-country counts + EU/UK regulated-score asymmetry as Lens 4 squeeze-flag quantification. | ~60 min | **RECOMMEND** — feeds two findings simultaneously (Lens 1 absorption + Lens 4 squeeze). Closes "EU AI Act material change to absorption capacity" as an answered question in §4.1. | **Before Bundle O dispatches** if Bundle P stays under budget; otherwise after. |
| **Bundle R** | L5 | Per-country A→C transition rate as Lens 1 absorption refinement + aggregate 7.55M/450K/15-year-backlog math as Class III §3 anchor + reform-velocity score for DACH. | ~60 min | **RECOMMEND** — sharpens Class III "structural insufficiency" from assertion to anchored evidence and refines AT/LU/TR s2b-dependent finding. | **Before Bundle O dispatches** if budget allows; high knock-on for `dach.html` and Specialist Appendix §3 / §4.3. |
| **Bundle S** | L2 | Entry-level collapse / Gen Z exclusion as Lens 4 cohort_incidence sub-field + AI/ML +88% as S1 demand-side anchor + per-country salary-growth heterogeneity. | ~75 min | **DEFER to Phase 5+** — distributional findings, depth-additive but not corridor-changing. Reasonable post-Bundle-O candidate. | Phase 5+. |
| **Bundle T** | L3 | 5-pattern-type taxonomy as country-cluster overlay + age-50 cliff distributional finding + 9% generational transmission for Class III. | ~75 min | **DEFER to Phase 5+** — Bundle N3 Long-Read enhancement; not load-bearing for the corridor map itself. | Phase 5+ (Bundle N3 enrichment). |
| **Bundle U** | L4 | Generational crises stratification + historical precedents panel (Japan/Black Death) for Regime Stability Note. | ~45 min | **DEFER to Phase 5+** — narrative depth; high-impact for Bundle N3 but not for SOT or Specialist Appendix structural integrity. | Phase 5+ (Bundle N3 enrichment). |
| **Bundle V** | L5 | Six-lens cross-check + diagnostic metric (internal transition speed vs external turnover). | ~45 min | **DEFER to Phase 5+** — methodology depth; useful for `lenses.html` (Bundle O) but the page can ship without it. | Phase 5+ or merge into Bundle O if Bundle O has slack. |
| **Bundle W** | L1 | ISCO 3-digit fidelity + ESS microdata application for breach scope. | multi-week | **DEFER (long-term Phase 5+)** — already flagged in §8.6 as enhancement candidate. | Long-term. |
| **Bundle X** | L1 | Exposure-weighted wages (€4.7T tech / €3.7T regulated). | <30 min | **DEFER OR FOLD INTO BUNDLE Q** — narrative anchor for Executive §1 only; small enough to fold into Bundle Q if pursued. | Bundle Q rider. |

**Pre-Bundle-O priority:** Bundle P (anchor) + Bundle Q (regulatory) + Bundle R (reskilling math). Combined ~210 min if run sequentially; ~150 min if Phil parallelises P with Q/R since they touch different SOT sub-fields.

---

## Scope-boundary cases (NOT for Layer 6)

- **L1 adoption-survey data** — adoption rate is a Layer 7 (Actions) input ("given this adoption rate, what action?"), not an L6 (Synthesis) lens.
- **L2 tooling-adoption rates (GitHub Copilot 35.6%)** — hiring-side observation; prescriptive use ("should firms mandate Copilot?") belongs in L7.
- **L3 ECB SAFE / ifo "AI is currently a net hiring driver"** — empirical observation belongs upstream in L1 (timing) or L2 (current state); L6 already cites it implicitly in the Regime Stability Note framing, no enrichment needed.
- **L4 fertility data (TFR 1.34)** — relevant to L4's own structural thesis but not load-bearing for L6's 10-year corridor horizon.
- **L5 Singapore SkillsFuture benchmark** — comparator belongs in L5 itself or in L7 ("what would it take for Europe to match Singapore?"); not an L6 lens enrichment.

---

## Not-worth-the-cost flags

- **L3's 6 diagnostic variables.** Already largely operationalised through the retrofit-lag-reconstruction document (locked spec Open Question 3 RESOLVED 2026-04-14) and Bundle K Klinger join. Re-running would mostly duplicate work.
- **L1 ISCO 3-digit breach scope expansion.** Already correctly flagged as Phase 5+ enhancement (§8.6); the cost (multi-week ESS application) outweighs the marginal scope refinement (1–2 additional Continental knowledge-economy entrants). The 12-country lower-bound caveat in §8.3 is the right disposition.

---

## Honest limits of this audit

- **Time-bounded read.** Approximately 75 minutes of read-only inspection across 5 layers + L6 anchor. Did not deeply inspect every L1–L5 source file; sampled READMEs + llms.txt + selected data files and prose documents. Strength scoring is the auditor's judgment based on the L6 deliverable structure as observed in the SOT JSON country object schema and the Specialist Appendix narrative — not on a full traverse of every L1–L5 data field.
- **Strength scoring is auditor judgment, not Phil's.** Findings tagged HIGH could land MEDIUM after Phil applies advisory/board-positioning weighting that the audit does not have full visibility into. Bundle Q (regulatory overlay) in particular: its strategic value depends on whether the L6 audience prioritises the EU AI Act story; if not, it slides to MEDIUM.
- **Final go/no-go on each bundle is Phil's, not the audit's.** The audit surfaces the menu; Phil picks the dishes.
- **No L6 modifications were made.** Read-only constraint observed. Single output is this audit report.
- **No primary-source verification.** Findings are cited to layer files; the audit does not re-verify the underlying primary sources behind those layer files. BR-19 applies at the layer-file level, not the primary-source level.
- **Cross-layer interaction surface not exhaustively mapped.** Findings that emerge from *interactions* between two L1–L5 layers (e.g., L2 entry-level collapse × L4 Gen Z structural exclusion × L3 age-50 cliff = three-layer cohort-stratified distributional read) are partially flagged but not exhaustively enumerated; a deeper interaction audit would be a separate sub-session.

---

**Audit complete.** 25 enrichment opportunities surfaced (10 high / 10 medium / 5 low+scope-boundary). Bundle P confirmed as priority. Recommended pre-Bundle-O work: P + Q + R.
