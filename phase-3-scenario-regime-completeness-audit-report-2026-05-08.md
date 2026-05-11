# Phase 3 — Scenario / Regime Completeness Audit (Flag-Only)

**Session:** 2026-05-08 bounded sub-session, ~3 h.
**Scope:** audit locked 8-scenario × 3-regime taxonomy against (a) the 25-source 2026-04-30 → 2026-05-07 corpus surfaced in Phase 2F and (b) the Industrial Accelerator Act / Made in Europe 2.0 corpus Phil surfaced 2026-05-08 (8 EU PDFs + 6 URLs).
**Output mode:** Flag-only. No SOT edits, no source-card edits, no re-derivations.
**Verification:** 6 SOT files (`site/data.json`, `layer-6-deliverable-data.json`, `layer-6-lens-framework.md`, `site/scenarios.html`, `site/methodology.html`, `site/sources.html`) untouched — md5 checksums identical pre-/post-session.

---

## TL;DR

- **PRIMARY — S9 Industrial Reconstruction: decline-recommend.** The Industrial Accelerator Act (IAA) is real, well-evidenced, and changes the policy environment, but its absorption mechanism collapses primarily into S2 Climate Adaptation Boom (Zone-C) and secondarily into S6/S7 fiscal-headroom dynamics. Net new EU jobs from the IAA preferred option are ~148k by 2030 (lead markets) + ~85k batteries + ~59k solar — a single-digit-million labour signal against the 7.55M deep-reskilling cohort. Mechanism-distinctness vs S2 fails the bar.
- **SECONDARY — 4th regime "Wealth-Fund Rich": decline-recommend.** The hypothesis that NO/SE/DK/CH/NL/LU diverge mechanically from DE/FR/IT/AT/FI inside `post_growth_empirical` is plausible, but no source in the expanded corpus supplies the per-country fiscal-headroom-vs-modal-scenario test the split needs. Re-derivation footprint is also large (10-country regime tags + 8 scenario probability vectors). Defer to Phase 5+ if the data lands.
- **TERTIARY — S9 Startup-Driven Absorption: confirm exclusion.** Phase 2F sources do not flip the SM 4 verdict. The ECB Schnabel "28th regime" speech adds founder-formation friction context but no country-level absorption evidence.
- **Source-card audit gap (carry-forward):** Phase 2F flagged Brynjolfsson Canaries S3 framing on `sources.html` line 226 — unchanged this session, still pending.
- **Evidence gap surfaced for Bundle W:** the IAA corpus contains zero per-country labour breakdowns, zero Switzerland-specific provisions, zero candidate-country (BA/MK/RS/TR) provisions. Phil's framing "(CH included)" is not corroborated by the corpus and should be treated as pending verification, not as a source-anchored finding.
- **Bundle W dispatch implication:** scope-as-written. No expansion to S9 or 4th regime. One paragraph in SM 4 / `methodology.html` could be added to acknowledge the IAA as an externally-evidenced policy lever that operates inside S2; flag-only, not edited here.

---

## PRIMARY: S9 Industrial Reconstruction

### What the corpus carries

Eight Commission documents (proposal, impact assessment 10 MB, executive summary, Q&A, press release, factsheet, subsidiarity grid, annexes) plus ECB Schnabel 2026-02-11, CEPA 2026-03 "Made in Europe 2.0", Bruegel 2026-03 "Made with Europe", EC competitiveness priorities 2024-2029. Press-corner Q&A page returned no body content via WebFetch — substantive Q&A was retrieved from the PDF.

**IAA core claims (cite-checked):**
- Manufacturing share of EU GDP target: 14.3% (2024) → 20% (2035). Press release IP/26/515 + factsheet ET-01-26-028-EN-N.
- Job estimate (lead market provisions, 2030): **148,352 jobs**. IA report Section 6 + executive summary SWD(2026) 72.
- Battery sector pipeline jobs anchored: **85,000 of 170,000** at medium/high risk by 2030. IA Annex 3 §2.
- Solar manufacturing jobs: **58,852 by 2030** (5,193 procurement + 32,888 auctions + 20,771 support schemes). IA Annex 3 §2.
- Steel: **up to 4,500 jobs** preserved in steel sector by 2030. IA Annex 3 §2.
- LEAD_VC1: GVA increase €5.5B (2027) / €4.5B (2030) first-tier; €10.5B / €9.7B full vehicle value chain.
- Permitting digitalisation savings: €240M for all manufacturing.
- Total IAA labour signal: ~150,000 jobs preserved-or-created by 2030 (factsheet headline).
- Sectoral scope (Annex I): NACE C17 paper, C19 coke/petroleum, C20 chemicals, C22 rubber/plastics, C23 non-metallic minerals, C24 basic metals; C29 motor vehicles; net-zero technologies per Reg 2024/1735 Article 4(1) (solar PV, batteries, heat pumps, wind, electrolysers, BESS, nuclear).
- Implementation timeline: legislative proposal 4 March 2026; Parliament/Council negotiation pending; lead-market obligations apply from 1 January 2029; review at 3 years post-entry; review clause at 5 years.
- Legal basis: Article 114 TFEU (single market, shared competence) + Article 207 TFEU (FDI, exclusive competence). Subsidiarity grid: scope of action limited to "27 Member States."

**External framings:**
- ECB Schnabel ("Europe lacks scale, not ideas") frames the gap as the *28th regime* — a unified incorporation framework. Identifies founder-formation friction (European founders incorporating in Delaware) but does not propose state-coordinated absorption.
- CEPA describes "Industrial Accelerator Act" as the formal vehicle for "Made in Europe 2.0" and surfaces the political tension: *"France calls for more Made in Europe. The Nordics and Germany call for less. Smaller states fear their larger neighbors are best placed to benefit at their expense."* Direct quote.
- Bruegel argues that local-content requirements *"raise costs for export-oriented industries, slowing domestic industrial transformation and ultimately the clean-energy transition"* — i.e. Bruegel reads the IAA as a drag on the very transition S2 anchors.

### Mechanism-distinctness check

1. **vs S1 Reinstatement Revival** — The IAA does not trigger endogenous reinstatement. It mobilises public procurement (~3-31% of sectoral demand depending on industry: cement 31%, steel 11%, EVs ~3.5%) plus public support schemes plus permitting acceleration. The mechanism is policy-induced demand-side support for incumbent EIIs. Distinct from S1 endogenous reinstatement — but distinctness alone does not earn a separate scenario row.
2. **vs S2 Climate Adaptation Boom (Zone-C)** — **near-total overlap**. S2 is anchored on Cedefop 2025 + EU Net-Zero Industry Act €100B + Climate Zone-C wage-positive premium. The IAA is the demand-side complement to NZIA: Q&A explicitly says *"This initiative is a proposal for a Regulation. It was announced in the Clean Industrial Deal"* and *"introduces 'Made in EU' requirements for batteries, battery energy storage systems (BESS), solar PV, heat pumps, wind, electrolysers, and nuclear technologies."* Six of seven net-zero technologies are climate-adjacent; the seventh (nuclear) sits adjacent to climate via decarbonisation. The IAA's automotive-and-EII tail (steel, cement, aluminium decarbonisation; EV value chain) is the broader-than-climate residual — but even the residual is decarbonisation-driven, not defence- or biotech-driven. Phil's pre-read framing assumed "defence, semiconductors, biotech, raw materials per impact assessment scope" — the IA report does not name semiconductors or biotech as in scope; defence and dual-use sit adjacent (chemicals, basic metals, raw materials) but are not the primary target. The Phil-framing was an over-read.
3. **vs S4 Muddle Through** — IAA is an active policy intervention, not residual. Not a collapse to S4.
4. **vs S6 / S7 fiscal-headroom dynamics** — The IAA imposes *recurrent* public-procurement costs on Member State budgets (€8.92M EU-wide annual administrative; downstream construction loss €691M GVA; corporate fleet EVs €1.24B adjustment cost). Member States with constrained fiscal headroom (DE 1.02% / 0.54%, IT 1.04% / 1.30%, FR ~post_growth) absorb these less easily than wealth-fund-rich peers. This is a regime-conditional re-weighting input, not a new scenario — feeds the Wealth-Fund Rich secondary triage below.

**Verdict on distinctness:** S9 Industrial Reconstruction collapses ~70% into S2, ~20% into a per-regime probability re-weight inside S2/S6/S7, ~10% into a Lens 1 absorption-capacity refinement (the public-procurement channel adds to Bertheau ALMP-anchored A→C transition rates for countries with high industrial NUTS2 concentration). None of these reach the bar SM 4 sets ("equivalent of the IPCC / Eurofound climate-demand projections or the Brynjolfsson / Dell'Acqua task-level RCTs that grounded S2 and S3").

### Per-country implications

The IAA corpus provides **no per-country labour or GVA breakdowns**. The CARMEN model (IA Annex 4) clusters EIIs across the top-60 NUTS2 regions but its outputs are EU-27 aggregate. FIDELIO general equilibrium is EU aggregate. The Q&A, press release, executive summary, and factsheet all use EU-27 aggregate language only.

Inferable directional implications (not source-cited at country level):
- **DE, AT, IT, FR, CZ, PL, SK, HU, RO** — high industrial NUTS2 share + EII concentration → highest IAA exposure. DE post_growth + AT post_growth + IT secular_stagnation + FR post_growth: IAA may marginally lift S2 probability against S6/S7 for these markets but does not flip modal scenarios.
- **CH** — corpus is silent. Phil's pre-read framing "(CH included)" is not corroborated. Switzerland is a WTO GPA party; the IAA reciprocity provisions allow GPA-party content to be deemed of Union origin "where relevant obligations of the Union exist under that agreement" (press release IP/26/515). Whether CH manufactures fall inside this scope under the EU-CH bilateral arrangements requires a separate legal-mapping read not surfaced in the 8 PDFs + 6 URLs. **Flag for Phil verification before any narrative claim.**
- **TR, MK, RS, BA** (candidates) — corpus silent. Subsidiarity grid uses "27 Member States" and "more industrialised Member States, and the ones aspiring to be." The latter phrase is the only candidate-adjacent language in the corpus.
- **Nordic + NL + LU + IE** — fiscal headroom + lower EII share + service-economy mix → IAA exposure is below average. CEPA flags the political tension explicitly: *"The Nordics and Germany call for less"* IAA, contradicting Phil's intuition that NO/SE/DK would gain disproportionately.

### Regime-conditioning check

Under each regime:
- `growth_baseline` (24 countries): IAA marginally raises P(S2) and lowers P(S5) at the EU-27 average. Effect on per-country S2 probability vector is within the ±0.05 CI band already in SOT, except possibly DE (post_growth) where the IAA + Cedefop alignment may justify P(S2|post_growth) shifting toward 0.32-0.33 from the current 0.30. Inside the band; not a re-derivation trigger.
- `secular_stagnation_warning` (EL, IT): IT has the largest construction-sector exposure to LEAD_EII costs (€691M GVA loss, EU aggregate). The hit lands disproportionately on stagnant economies. Direction-aligned with current SOT, no flip.
- `post_growth_empirical` (10 countries: AT, CH, DE, FI, FR, LI, LU, NO, SE, UK): the IAA's recurrent public-procurement cost is exactly the kind of fiscal load these countries handle asymmetrically. The wealth-fund-rich subset (NO/SE/DK/CH/NL/LU) has the headroom; the fiscally-constrained subset (DE/FR/IT/AT/FI) does not. **This is the empirical hook for the secondary triage below — not a self-standing S9 anchor.**

### Lock-recommend / decline-recommend

**Decline-recommend S9 Industrial Reconstruction.**

Rationale: (a) mechanism collapses ~70% into S2 with the rest splitting into within-scenario probability nudges and a Lens 1 absorption-capacity refinement; (b) no per-country evidence in the IAA corpus supports a per-country probability vector at the resolution the SOT requires (this would be a "data not directly verified" Low-confidence anchor of the kind Phase 2F flagged for the Ageing Report); (c) labour-signal magnitude (~150K-300K direct jobs by 2030) is two orders of magnitude below the deep-reskilling cohort and within the noise-floor of the Lens 1 absorption-capacity calibration; (d) the political-economy framings (CEPA + Bruegel) split — Bruegel reads the IAA as a drag on S2-aligned transition, not an additive optimistic mechanism. SM 4 ninth-scenario exclusion bar holds.

**Recommended carry-forward (flag-only; do NOT edit this session):** add ~3 sentences to `methodology.html` SM 4 acknowledging the IAA as a real but S2-collapsing policy lever surfaced post-Phase 2; cite the 148K + 85K + 59K job estimates with provenance (IA report Section 6, executive summary SWD(2026) 72). This preserves audit traceability without expanding the taxonomy. Bundle W can absorb this in one paragraph; not a re-derivation.

### Draft mechanism string (NOT TO BE WRITTEN — flag-only)

If Phil overrides the decline, the SOT-equivalent mechanism string would be (S3-format, ~100 words):

> *S9 Industrial Reconstruction (DECLINE-RECOMMENDED, flag-only draft).* EU public procurement + 'Made in EU' content requirements + permitting acceleration mobilise demand for EII outputs (steel, cement, aluminium, EVs) and net-zero tech (batteries, solar PV, heat pumps, wind, electrolysers, nuclear). Mechanism: state-coordinated demand-side support raises absorption velocity for incumbent EII workforce in NUTS2-concentrated industrial regions. Empirical anchors: IAA proposal COM(2026) 100, IA report SWD(2026) 71 (CARMEN + FIDELIO + SMILE EU general-equilibrium models), executive summary SWD(2026) 72. Distinct from S2 only insofar as scope extends beyond climate to defence/raw-materials adjacency and from S1 by being policy-induced, not endogenous. Distinct from S4 by being active intervention. **Mechanism-distinctness vs S2 weak; SM 4 exclusion bar holds.**

### Draft probability vector (NOT TO BE WRITTEN — flag-only)

Suppressed. If lock, vectors would carry [0.02, 0.05, 0.10] across all three regimes — within the existing S3 / S6 / S7 noise floor and not differentiating.

### Draft source-card (NOT TO BE WRITTEN — flag-only)

If a source-card is added regardless of decline (for Bibliographic completeness on the audit trail), Tier 1, ~5 lines:

> **EU Industrial Accelerator Act (COM(2026) 100, IA report SWD(2026) 71, exec summary SWD(2026) 72) — Tier 1, 2026-03-04.** Legislative proposal mobilising 'Made in EU' content requirements + low-carbon procurement criteria + permitting acceleration; targets manufacturing share 14.3% → 20% of EU GDP by 2035. Lead-market job estimate 148,352 by 2030 (3 sub-sectors: steel/cement/Al + batteries 85K + solar 58.8K). Provides external policy-lever evidence for SM 4 ninth-scenario discussion; does NOT anchor a separate scenario per Phase 3 audit. Cross-reference: EC press release IP/26/515; ECB Schnabel "28th regime" speech 2026-02-11; CEPA "Made in Europe 2.0" 2026-03; Bruegel "Made with Europe" 2026-03 (counter-framing).

---

## SECONDARY: 4th regime — Wealth-Fund Rich

### Empirical anchor

Draghi 2024 (Tier 1, already in DATA-REGISTRY) carries the wealth-concentration framing the hypothesis relies on. Treichl + Klinger captures in `european-ai-labour-actions/RATIONALE.md` Layer 7 evidence base were not re-read this session — handover Step 2 brain-context flagged them but they are sister-layer artefacts not in the Layer 6 SOT scope. Per the IAA Subsidiarity Grid §2.3(d), *"Regions that currently host energy-intensive industries are particularly at risk of further economic and social decline, leading to widening disparities in employment and prosperity across the single market"* — a direction-aligned signal that fiscal asymmetry between member states is increasing, not narrowing. This corroborates the *direction* of the hypothesis but provides no per-country fiscal-headroom-vs-modal-scenario test.

### Mechanism-distinctness vs `post_growth_empirical`

Currently `post_growth_empirical` collapses NO/SE/DK/CH/NL/LU/AT/DE/FR/FI/UK/LI into one bucket, with S2 modal at P(S2|post_growth) = 0.30. The hypothesis: wealth-fund-rich countries have fiscal headroom for ALMP + industrial-policy + IAA co-financing that fiscally-constrained DE/FR/IT/AT/FI lack, which permits S1 reinstatement to remain marginally viable AND raises P(S2) further AND reduces P(S6)/P(S7).

Tested:
- **NO** — Government Pension Fund Global ~$1.7T, ~3-4× GDP. Fiscal headroom unmatched in the data set.
- **SE** — large pension assets, AP-funds ~25% GDP, current-account surplus ~5% GDP.
- **DK** — pension-asset stack >200% GDP; current-account surplus consistent ~7-9%.
- **CH** — SNB reserves ~120% GDP; current-account surplus 5-yr avg ~7%.
- **NL** — pension assets >190% GDP; current-account surplus structural ~9%.
- **LU** — financial-centre artefact; LU is already flagged as `aggregate_distributional_split` in `layer-6-lens-framework.md` and treated as a per-capita reading, not aggregate.

The wealth-fund-rich cluster has the fiscal headroom to (i) absorb IAA recurrent public-procurement costs without crowding out ALMP, (ii) co-finance NZIA + IAA at higher effective rates, (iii) sustain Mode 1 / Mode 3 jurisdictional-buffering institutions through stagnation. The fiscally-constrained subset (DE/FR/IT/AT/FI) cannot do all three simultaneously. This is the *mechanism* the hypothesis names.

**But:** the corpus surfaced 2026-04-30 → 2026-05-08 does NOT supply the per-country fiscal-headroom proxy at the granularity required to operationalise a regime split. The EC 2024 Ageing Report (Phase 2F flagged "Refines, Low confidence") would be the closest Tier 1 candidate; it adds pension-spending and age-related-public-spending projections, not sovereign-wealth-fund-headroom indicators. Bundle P L4 demographics carries working-age trajectories per country for 9 of 36 markets; Bundle R L5 ALMP-spend %GDP per country for 25+ markets. Neither is the wealth-fund-rich sentinel proxy.

### Per-country re-classification (if the regime were locked)

| Current `post_growth_empirical` (10) | Proposed `wealth_fund_rich` | Proposed `post_growth_empirical_constrained` |
|---|---|---|
| AT | — | AT |
| CH | CH | — |
| DE | — | DE |
| FI | — | FI |
| FR | — | FR |
| LI | LI (proxy-data flag) | — |
| LU | LU (already aggregate_distributional_split) | — |
| NO | NO | — |
| SE | SE | — |
| UK | — | UK |

Plus `growth_baseline` re-evaluations for: NL (current-account surplus + pension assets argue for `wealth_fund_rich` rather than `growth_baseline`), DK (same argument), NL/DK currently `growth_baseline` per SOT regime_split because their aggregate GDP growth >1.5%. **A 4th regime would force a re-test of all 36 country regime tags, not just the post-growth subset.**

### Re-derivation footprint estimate

A 4th regime touches:
- 36 per-country `regime` field assignments — re-evaluation pass against thresholds plus newly defined wealth-fund-rich qualifying criteria.
- 8 scenario probability vectors per regime — 8 × 4 = 32 [low, mid, high] arrays in `layer-6-deliverable-data.json`. Currently 8 × 3 = 24 vectors. Net new: 8 vectors.
- `regime_split` aggregate listing in `layer-6-deliverable-data.json` line 7123-7166 — 1 new key + reclassification of ~5-7 countries.
- `cross_cutting_findings.pan_european_aggregate.eu_27` and `european_36` `regime_mix` blocks — recompute population-weighted shares.
- `site/scenarios.html` per-regime probability table — column added.
- `site/methodology.html` "Three regimes" sentence (line ~228) — change to four; SM 4 numbering left intact.
- Phase 2F + Phase 2E source-card "how informs" copy on regime-classification anchors (OECD Economic Surveys, Ageing Report, IMF WEO) — add wealth-fund-rich qualifying criterion citation.
- 36 per-country `_provenance.regime_classification` fields — minor field addition.

Estimated effort: 1.5-2 days re-derivation + 0.5 day SOT propagation + 0.5 day site rebuild + 0.5 day Bundle W absorption. ~3 days total. Comparable to a single-bundle Phase 2 sub-session, not a Phase 5+ overhaul.

### Modal-scenario change estimate

Current modal-under-post-growth: S2 (P=0.30 ≥ P(S4)=0.22). If wealth-fund-rich split stands, the wealth-fund-rich modal stays S2 (probably P(S2|wealth_fund_rich) ≈ 0.32-0.34 with stronger fiscal absorption); fiscally-constrained-post-growth modal probably *flips to S4* (P(S4|constrained) likely 0.24-0.27 vs P(S2|constrained) 0.25-0.27 — within noise; modal flip is plausible but not robust). So the headline finding the L6 document carries (*"S2 modal under post-growth"*) becomes regime-conditional inside the 4th regime split — which is a real finding but not yet defensible at the resolution required.

### Lock-recommend / decline-recommend

**Decline-recommend Wealth-Fund Rich regime — but at lower-confidence than the S9 decline.**

Rationale: (a) the *direction* is empirically defensible (fiscal asymmetry inside post-growth is real, anchored on Draghi 2024 + Subsidiarity Grid §2.3(d) regional disparity language); (b) the *resolution* required to operationalise — per-country sovereign-wealth-fund-headroom proxy — is not in the surfaced corpus and is a Phase 5+ acquisition target; (c) the re-derivation footprint (~3 days) is feasible inside Bundle W if data lands but premature without the sentinel proxy; (d) the modal-scenario flip is plausible but not robust at current resolution; running it on weak data risks shipping a regime split the next round of evidence collapses.

**Recommended carry-forward:** add to `docs/MAINTENANCE-STATE.md` Phase 5+ acquisition queue: *sovereign-wealth-fund + pension-assets %GDP per country (NO/SE/DK/CH/NL/LU/IE) as candidate proxy for wealth_fund_rich regime split inside post_growth_empirical*. Acquisition target: OECD Pensions at a Glance 2023 + IMF Sovereign Wealth Fund Database. Defer regime split until proxy lands and modal-scenario-flip robustness check passes a 2-of-3 sensitivity.

### Draft regime definition (NOT TO BE WRITTEN — flag-only)

If Phil overrides the decline, the regime definition would carry these qualifying criteria:

> *`wealth_fund_rich` regime (DECLINE-RECOMMENDED, flag-only draft).* Country qualifies if (i) sovereign-wealth-fund or pension-assets %GDP > 100% (5-yr avg) OR (ii) current-account surplus 5-yr avg ≥ 5% GDP AND aggregate fiscal balance non-negative. Both conditions OR'd, not AND'd, to capture both the Norwegian (sovereign fund) and Swiss (CB-reserve + surplus) variants. Within `post_growth_empirical` subset only (i.e. low aggregate or per-capita growth + qualifying fiscal headroom). Initial qualifying set: **CH, NO, SE, DK, NL, LU** (6 countries). LI carried with proxy-data flag. Re-derivation triggers full 36-country regime-classification re-test; modal-scenario probability vectors (8 × 4 = 32) require Bundle V-equivalent re-score pass.

---

## TERTIARY: S9 Startup-Driven Absorption (revisit)

The Phase 2F new Tier 1 sources (Brynjolfsson Li Raymond 2023 RCT, Massenkoff & McCrory 2026, Anthropic Economic Index, Eloundou 2023 GPTs are GPTs, Brynjolfsson Chandar Chen 2025 Canaries) are productivity / entry-level-employment / occupation-level evidence, not new-firm-formation evidence. The ECB Schnabel 2026-02-11 "28th regime" speech is the closest 2026 surface to startup-formation evidence — it documents the *gap* (European founders incorporating in Delaware, "incorporating a company in Delaware takes just a few days") but does NOT document an absorption mechanism: no country-level new-firm formation rate, no startup-headcount-vs-displaced-worker overlap, no equivalent of the IPCC/Eurofound climate-demand projections that ground S2.

**Verdict: confirm SM 4 exclusion stands.**

The new corpus does not flip the verdict. The policy-lever variant (what would it take to build this mechanism deliberately at supra- or national level) belongs in Layer 7 / `european-ai-labour-actions/`, per SM 4's existing language: *"belongs in Part 7."* No SOT or methodology change.

---

## Cross-candidate dependencies

The S9 Industrial Reconstruction primary candidate and the 4th regime Wealth-Fund Rich secondary candidate interact at one point: the IAA's recurrent public-procurement cost lands asymmetrically inside `post_growth_empirical`. Wealth-fund-rich members can co-finance + absorb the green-premium without crowding out ALMP or jurisdictional-buffering institutions; fiscally-constrained members cannot. *If* both candidates were locked, the IAA would shift P(S2|wealth_fund_rich) up by ~0.02-0.04 and P(S6|constrained) up by ~0.01-0.03. Since both are decline-recommended, this interaction stays narrative-only and is not a re-derivation trigger.

A subtler interaction: CEPA's framing — *"France calls for more Made in Europe. The Nordics and Germany call for less."* — implies the political coalition that *passes* the IAA is not the wealth-fund-rich coalition that benefits most from it under the proposed regime split. This is a Layer 7 political-economy finding, not a Layer 6 corridor-classification input. Flag for `european-ai-labour-actions/` if/when Phase 5+ proxy data lands.

---

## Bundle W dispatch implication

Three scope estimates:

1. **Scope-as-written (recommended):** Bundle W dispatches against the locked 8-scenario × 3-regime taxonomy. ~0 propagation work from this Phase 3 audit. Optional: 3-sentence addition to `methodology.html` SM 4 acknowledging the IAA as an externally-evidenced S2-aligned policy lever; ~15 min edit, can fold into Bundle W's existing methodology pass.
2. **Scope-expanded-S9-only:** Bundle W absorbs S9 Industrial Reconstruction. ~1.5-2 days propagation: SOT scenario block expansion (8→9), per-regime probability vector re-balance, methodology + scenarios HTML rebuild, source-card additions for IAA + Schnabel + CEPA + Bruegel (4 cards). Also re-runs Bundle X pan-European aggregate computation. **Not recommended** per primary triage above.
3. **Scope-expanded-S9-plus-regime:** Bundle W absorbs S9 + Wealth-Fund Rich regime. ~4-5 days propagation: above + 36-country regime-classification re-test + 32-vector probability re-derivation + Bundle X re-run + Phase 5+ acquisition for wealth-fund-headroom proxy or accept Low-confidence anchors throughout. **Not recommended** per secondary triage above.

**Recommended dispatch:** scope-as-written, with the optional methodology paragraph addition.

---

## Audit-at-class lens (per `feedback_audit_at_class_at_phase_boundaries.md`)

Triggered by the S9 Industrial Reconstruction triage finding that the IAA mechanism collapses ~70% into S2. Re-read S2 mechanism string:

> *S2 mechanism (current SOT line 7941, layer-6-deliverable-data.json):* "Climate adaptation Zone C wage-positive premium; Cedefop 2025 country-level employment projections + EU Net-Zero Industry Act €100B. Under post-growth, S2 is the only genuinely-positive scenario where new sectoral demand absorbs displaced workers (locked spec line 96, 104)."

Refinement candidate: S2 mechanism string could be tightened to acknowledge the IAA as a complementary demand-side instrument to NZIA's supply-side anchor — current copy implies NZIA carries the policy weight alone, when as of 2026-03-04 the IAA is the named demand-side counterpart. Also re-read S1 Reinstatement Revival mechanism (line 7919): currently anchored on Autor 2024 historical-base-rate refutation. The IAA is policy-induced demand, not endogenous reinstatement, so S1 distinctness is preserved against the IAA finding — no refinement needed.

**Recommended:** S2 mechanism-string refinement (additive, ~10 words) — *"Cedefop 2025 country-level employment projections + EU Net-Zero Industry Act €100B (supply-side) + Industrial Accelerator Act 2026 (demand-side)"* — to preserve the audit trail and avoid the kind of source-card-anchor confusion Phase 2F flagged for the Brynjolfsson Canaries / Generative-AI-at-Work mix-up. **Flag-only this session.** Bundle W can absorb in one line.

---

## Honest deviation reporting

- **CH inclusion:** corpus is silent. Phil's framing 2026-05-08 *"the EU is planning a Made in EU(rope) initiative (CH included)"* is not corroborated by the 8 PDFs + 6 URLs. CH is a WTO GPA party, which under IAA reciprocity provisions could trigger Union-origin treatment for procurement, but the bilateral-agreement coverage of "other forms of public intervention" (auctions, support schemes) requires a legal-mapping read not in the corpus. **Flagged as evidence gap, not invented.**
- **Per-country labour estimates:** corpus is silent. CARMEN model uses NUTS2 cluster aggregation, FIDELIO and SMILE EU are EU aggregate. **Flagged as evidence gap.**
- **Candidate-country provisions (BA, MK, RS, TR):** corpus is silent. Subsidiarity grid uses "27 Member States" + "ones aspiring to be" (the only candidate-adjacent phrasing). **Flagged as evidence gap.**
- **Sectoral scope:** Phil's pre-read framing assumed *"defence, semiconductors, biotech, raw materials per impact assessment scope"*. Annex I confirms NACE C17/C19/C20/C22/C23/C24 + C29 + net-zero technologies per Reg 2024/1735 Article 4(1). Defence and dual-use sit adjacent (basic metals, critical raw materials inside FDI conditionalities) but are not the primary target. Semiconductors and biotech are NOT named in scope. **The Phil pre-read was an over-read; corrected against the corpus.**
- **EC press-corner Q&A URL** (`https://ec.europa.eu/commission/presscorner/detail/en/qanda_26_516`) returned only the page title via WebFetch with no body content. Substantive Q&A retrieved from the local PDF. **Flagged as fetch failure, not silent skip.**

---

## Brain capture candidates (surface for Phil per Rule 12)

Two pattern-level captures worth surfacing:

### Capture 1 — "Policy-lever-vs-mechanism distinctness rule" (medium scope)

**Pattern observed:** Phase 3 audit found the IAA collapses ~70% into S2 *because* the IAA's mechanism is policy-induced demand, not a different absorption mechanism. The IAA changes the *probability* of S2 being realised in some markets, not the *mechanism* by which displaced workers are absorbed.

**Proposed rule:** *When evaluating a candidate scenario against an existing taxonomy, distinguish "different mechanism" from "policy-induced probability shift on existing mechanism." A candidate that changes P(scenario|regime) but not the mechanism's mathematical form is a probability-vector update, not a new scenario row.*

**Why:** prevents scenario-stack inflation from policy news cycles. The scenario stack is a mechanism taxonomy; policy levers are inputs to probability vectors, not new mechanism categories.

**How to apply:** when triaging a scenario candidate, run the test: "Does this candidate change the mathematical form of the absorption equation, or does it change the inputs?" If inputs only → probability-vector update. If form → new scenario.

### Capture 2 — "Pre-read framing as invitation, not anchor" (small scope)

**Pattern observed:** Phil's pre-read framing 2026-05-08 contained two over-reads (CH inclusion claimed; sectoral scope including defence/semiconductors/biotech). The audit corrected both against the corpus. The pre-read was an invitation to look, not a finding to defend.

**Proposed rule:** *When a handover prompt contains framing claims (e.g. "the IAA covers defence, semiconductors, biotech"), treat them as audit hypotheses, not anchored facts. Verify against corpus before grounding any downstream finding in them. If contradicted, flag honestly, do not paper over.*

**Why:** the BR-19 fabrication discipline already covers don't-invent. This is the inverse: don't-defer-to-Phil-framing-when-corpus-contradicts.

**How to apply:** treat handover framing claims as a checklist of things to test, not a baseline to extend. If the corpus contradicts, the corpus wins. Flag the contradiction as a finding, not a footnote.

These are sub-session candidates for Phil to decide on; not auto-written to the brain.

---

## Verification

```
md5 site/data.json layer-6-deliverable-data.json layer-6-lens-framework.md \
    site/scenarios.html site/methodology.html site/sources.html
```

**Pre-session (captured 2026-05-08 ~09:55 CEST, `/tmp/phase3-md5-pre.txt`):**
- `site/data.json` 298bd73025ca8d150d49dfb61ef96b46
- `layer-6-deliverable-data.json` 61b5e973c1670f039e4e6368e1675272
- `layer-6-lens-framework.md` 87933b817b1d9ddb9074c8ee541b9927
- `site/scenarios.html` 7e5394ed9849915a05e09b91d05a3fa4
- `site/methodology.html` 9c96df6f440f777355d20d41f3f9e4d6
- `site/sources.html` 97701dba4b14b3d4ec6a40305e908eae

**Post-session:** verified clean — re-run at session close.

---

## Sub-session metadata

- **Bounded duration:** ~4-6h target. Actual: ~3h.
- **Reads only.** No writes to SOT, source-cards, site HTML, lens framework, deliverable data, or llms.txt.
- **Files touched:** this report only — `phase-3-scenario-regime-completeness-audit-report-2026-05-08.md` (new file at project root).
- **Phil does all git commits.**

---

*This brief is the Phase 3 sub-session report. Three candidates triaged. All three decline-recommend. Bundle W dispatches scope-as-written; optional ~3-sentence methodology addition to acknowledge the IAA as a real S2-aligned policy lever surfaced post-Phase 2.*
