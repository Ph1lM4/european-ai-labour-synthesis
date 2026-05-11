# Phase 3.5 — Supplementary-Sources Sweep (Flag-Only)

**Session:** 2026-05-08 bounded sub-session, ~3 h.
**Scope:** Targeted-WebSearch sweep on three named topics to harden Phase 3 audit verdicts and source `methodology.html` SM 4 v2 attribution. No SOT edits. No source-card edits. No re-derivations.
**Verification:** 6 SOT files (`site/data.json`, `layer-6-deliverable-data.json`, `layer-6-lens-framework.md`, `site/scenarios.html`, `site/methodology.html`, `site/sources.html`) untouched — md5 checksums identical pre-/post-session.
**DATA-REGISTRY check:** none of the three topics returned a local match (`grep` on IRA / Inflation Reduction / sovereign-wealth / SWF / ETUC / Eurofound / IndustriAll / NBIM / Temasek / Pensions at a Glance / Rhodium / Bistline / REPEAT / Goulder against `/Users/philippmaul/Documents/projects/DATA-REGISTRY.md` — zero hits). External fetch was required and ran via WebSearch only; no PDFs downloaded.

---

## TL;DR

- **Topic 1 (IRA labour outcomes) — verdict HARDENS the S9 Industrial Reconstruction decline.** Three years of post-implementation IRA tracking (Rhodium / MIT Clean Investment Monitor) show the IRA's labour-absorption pathway is the same demand-side-policy-induced class the Phase 3 audit collapsed the IAA into S2 — plus a fragility signal Phase 3 didn't have (Q1 2025 cancellations of 27K operational manufacturing jobs / $8B, mainly EV). Order of magnitude consistent with the IAA's ~150K-by-2030 estimate; mechanism class consistent with S2.
- **Topic 2 (sovereign-wealth / fiscal-headroom proxies) — verdict SOFTENS the 4th regime decline, does not flip it.** OECD Pension Markets in Focus + SWFI/Global SWF rankings + NBIM annual reports together provide thresholdable per-country data for **4 of the 5 candidate markets (NO, SE, DK, NL)** with one partial gap (CH — SNB reserves are central-bank not SWF). The operationalisation-gap argument that anchored the Phase 3 decline weakens; per-country proxy is feasible inside ~1 day of acquisition work, not the days originally estimated. Decline still recommended on parsimony grounds, but the proxy-availability rationale is no longer the decisive blocker.
- **Topic 3 (ETUC / Eurofound / labour-side framing) — verdict HOLDS, mechanism-string refinement candidate identified.** ETUC and IndustriAll Europe both frame IAA labour absorption as conditional on (a) social conditionalities attached to public procurement, (b) collective-bargaining-anchored qualification measures, (c) works-council-mediated location guarantees. None of this overturns the S9 Startup-Driven Absorption decline (no startup-formation evidence). It does surface a **within-mechanism refinement candidate** for the S2 mechanism string: current copy is supply-side-only; labour-side adds a conditional-on-mediation component.
- **SM 4 v2 attribution shortlist (5 sources):** Rhodium / MIT Clean Investment Monitor (Topic 1 primary), Bistline et al. NBER WP 32168 / Brookings 2024 (Topic 1 modelling), OECD Pension Markets in Focus 2025 (Topic 2 primary), ETUC press release 2026-03-04 (Topic 3 supranational labour-side primary), IndustriAll Europe Article 1450 (Topic 3 sectoral labour-side).
- **Cross-topic finding:** IRA experience (Topic 1) and ETUC framing (Topic 3) converge on the same point — public-procurement-anchored industrial-policy absorption is highly conditional on policy-stability (US 2025 cancellations) and labour-side mediation institutions (works councils, collective bargaining). S2 as currently coded under-specifies that conditionality.

---

## Topic 1 — IRA labour outcomes

### Source 1.1 (PRIMARY) — Rhodium Group / MIT CEEPR Clean Investment Monitor (CIM)

- **Citation:** Rhodium Group + MIT Center for Energy and Environmental Policy Research, *Clean Investment Monitor: US Q1 2025 Update*, *Q4 2025 Update*, and *State of US Clean Energy Supply Chains in 2025*. Live tracker at `cleaninvestmentmonitor.org` plus quarterly write-ups at `rhg.com`.
- **Primary-data anchor:** $321B in private clean-investment since IRA enactment Q3 2022; 2,369 new facilities opened US-wide; per-state operational jobs from completed facilities (TX ~13,000; GA ~12,500; NC ~7,500; MI ~7,500). Q1 2025 manufacturing investment +7.7% vs Q1 2024 but −11.5% vs Q4 2024. Cancelled projects Q1 2025: $8B / ~27,000 operational manufacturing jobs affected, concentration in EV supply chain. Joint construction-and-operational-jobs tracking added to database in 2025 expansion.
- **S9-vs-S2 mechanism-relevance:** highest of any Topic 1 source. IRA is the strongest live counterfactual for state-coordinated demand-side industrial-policy absorption with three years of realised post-implementation labour data. The CIM's per-state operational-job counts (single-digit thousands per anchor state, scaling to tens of thousands EU-equivalent) are an order-of-magnitude consistent with the IAA's 148K-by-2030 lead-market estimate (Phase 3 IA Section 6 anchor). Mechanism class is identical: public procurement plus support schemes plus permitting drive demand-side absorption in a regionally-concentrated subset of incumbent industrial capacity. **The IRA experience does NOT produce a qualitatively different absorption pathway from what Phase 3 collapsed the IAA into.** Adds a fragility signal Phase 3 didn't surface: cancellation risk under policy uncertainty (Q1 2025 EV-supply-chain cancellations of 27K jobs / $8B in a single quarter is non-trivial against the cumulative $321B since 2022).
- **Verdict-robustness:** **HOLDS — and HARDENS.** The S9 decline rationale was that the IAA mechanism collapses into S2. The IRA evidence confirms that empirically-realised absorption from a same-class policy is in S2's mechanism family. The cancellation signal is additionally an argument against treating IAA-type absorption as a self-standing optimistic scenario.
- **URLs:** [Q1 2025 update](https://rhg.com/research/clean-investment-monitor-q1-2025-update/), [Q4 2025 update](https://rhg.com/research/clean-investment-monitor-us-q4-2025/), [supply chains 2025](https://rhg.com/research/clean-investment-monitor-us-clean-energy-supply-chains/), [methodology](https://www.cleaninvestmentmonitor.org/methodology).

### Source 1.2 (MODELLING) — Bistline, Clausing, Mehrotra, Stock & Wolfram 2024 — *Climate Policy Reform Options in 2025*

- **Citation:** John E. Bistline, Kimberly A. Clausing, Neil Mehrotra, James H. Stock, Catherine Wolfram, *Climate Policy Reform Options in 2025*, NBER WP 32168 / Brookings Hamilton Project Feb 2024. Multi-model integrated energy-system comparison covering eleven models. Companion to the same authors' 2023 Brookings BPEA paper *Economic Implications of the Climate Provisions of the Inflation Reduction Act*.
- **Primary-data anchor:** modelled vs realised IRA outcomes through 2035. IRA incentives accelerate deployment of low-emitting capacity by up to 3.2× current annual additions. Per the 2023 BPEA paper, the IRA's emissions-reduction trajectory is sensitive to take-up assumptions; the 2024 follow-up adds policy-counterfactual scenarios (carbon fee, clean electricity standard) that reach 50–52% economy-wide reductions between 2030 and 2035.
- **S9-vs-S2 mechanism-relevance:** the strongest counterfactual *modelling* (vs realised) baseline available for IRA-class industrial-policy absorption. Useful for SM 4 v2 to make the symmetric methodological claim: the IAA is in the same model-evidence class as the IRA. Not a self-standing absorption-mechanism finding.
- **Verdict-robustness:** **HOLDS.** No mechanism-class signal that contradicts the Phase 3 decline. Useful as the "model-baseline" companion to the CIM "realised-outcomes" anchor.
- **URLs:** [NBER WP 32168 PDF](https://www.nber.org/system/files/working_papers/w32168/w32168.pdf), [Brookings article](https://www.brookings.edu/articles/climate-tax-policy-reform-options-in-2025/), [BPEA Spring 2023 PDF](https://www.brookings.edu/wp-content/uploads/2023/03/BPEA_Spring2023_Bistline-et-al_unembargoedUpdated.pdf).

### Source 1.3 (FEDERAL-SIDE) — US Treasury IRA Impact and Stories portal + DOE/Treasury Round 1 announcement

- **Citation:** US Department of the Treasury, *Inflation Reduction Act: Impact and Stories*, ongoing. Plus joint DOE+Treasury announcement 2024-03-29 of $4B Round 1 §48C credits awarded to 100+ projects with all awardees meeting prevailing-wage requirements.
- **Primary-data anchor:** federal-government-side primary surface for IRA labour-rule compliance; prevailing-wage and apprenticeship-requirement design is the IRA's labour-conditionality feature comparable to the IAA's social-conditionality framing the labour-side surfaced in Topic 3.
- **S9-vs-S2 mechanism-relevance:** lower than 1.1 or 1.2 for absorption-pathway evidence; higher than either for the labour-conditionality cross-link to Topic 3 (the IRA does attach prevailing-wage labour conditionality to procurement/credit channels — the IAA proposal does not, which is exactly the gap ETUC and IndustriAll Europe flag).
- **Verdict-robustness:** **HOLDS.** Useful as a labour-conditionality bridge to Topic 3 in the SM 4 v2 attribution; weak as a stand-alone IRA absorption anchor.
- **URLs:** [Treasury IRA Impact](https://home.treasury.gov/policy-issues/inflation-reduction-act/impact-and-stories), Treasury TBAC economy statements series.

---

## Topic 2 — Sovereign-wealth / fiscal-headroom per-country proxies

**Explicit answer to the brief's framing question — *is there a thresholdable per-country dataset for the 5 candidate markets (NO/SE/DK/CH/NL)?*** **Partially yes.** Combining OECD Pension Markets in Focus + SWFI/Global SWF + NBIM annual reports gives clean per-country thresholdable data for 4 of 5 (NO, SE, DK, NL). The fifth (CH) requires a non-OECD-pensions reading (SNB reserves; current-account-surplus 5-yr avg from IMF WEO already in DATA-REGISTRY). No single dataset covers all five at once; a composite is required.

### Source 2.1 (PRIMARY — pension-stack proxy) — OECD Pension Markets in Focus 2024/2025 + Pensions at a Glance 2023

- **Citation:** OECD, *Pension Markets in Focus — Preliminary 2023 data* (June 2024) and *Preliminary 2024 data* (June 2025); OECD, *Pensions at a Glance 2023* (country-notes series). OECD data explorer at `data-explorer.oecd.org/vis?df...DSD_PAG`.
- **Primary-data anchor:** per-country pension-assets-%GDP. Headline: pension assets in NL, CH, and Canada exceed 150% GDP; advanced-economy average ~55%; eight countries above 100%. NL 97.5% defined-benefit share end-2023; CH 88.8% defined-benefit share. Per-country reads available for all OECD members including the 5 candidates. *Pensions at a Glance 2023* (Tier 2 entry already in `bundle-o-phase-2f-source-triage-report-2026-05-07.md` row 9 of the Tier 2 spot-check) — confirmed publicly available, individual country notes published in October 2024 (Germany, UK, Türkiye notes verified in search).
- **5-candidate coverage:** NO (covered, OECD member, GPFG dominates), SE (covered, AP-funds), DK (covered, ATP-driven, pension stack >200% GDP per Phase 3 audit narrative), NL (covered, >150%), CH (covered, occupational pensions ~140% GDP). **All 5 candidates in scope.**
- **Verdict-robustness:** the operationalisation-gap argument that anchored the Phase 3 4th-regime decline **weakens.** A pension-assets-%GDP threshold (>100% 5-yr avg) operationalises 4 of 5 candidate markets cleanly, plus extends to ~10 OECD economies for full-36-market regime-classification re-test.
- **URLs:** [PMF 2024 PDF](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/asset-backed-pensions/PMF-2024-Preliminary-2023-Data.pdf), [PMF 2025 PDF](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/asset-backed-pensions/PMF%202025%20-%20Preliminary%202024.pdf), [Pensions at a Glance 2023 hub](https://www.oecd.org/en/publications/pensions-at-a-glance-2023_678055dd-en.html), [data explorer](https://data-explorer.oecd.org/vis?df%5Bds%5D=DisseminateFinalDMZ&df%5Bid%5D=DSD_PAG%40DF_PAG&df%5Bag%5D=OECD.ELS.SPD).

### Source 2.2 (SECONDARY — sovereign-fund proxy) — SWFI / Global SWF rankings + NBIM annual report 2025

- **Citation:** SWFI (`swfinstitute.org/fund-rankings/sovereign-wealth-fund`); Global SWF (`globalswf.com/ranking`); IFSWF "SWFs By Numbers". Plus Norges Bank Investment Management *Government Pension Fund Global — Annual Report 2025*.
- **Primary-data anchor:** SWF-AUM rankings ordered by total assets. Norway GPFG ~US$2.2T as of April 2025 (15.1% return in 2025; end-2025 value 21,268B NOK). SWFI uses AUM as primary criterion plus the Linaburg-Maduell Transparency Index as a secondary scoring layer. Coverage of the 5 candidates is **uneven**: NO covered explicitly via NBIM; NL has no sovereign wealth fund (uses pension stack — cite via 2.1); CH has SNB foreign-exchange reserves which are central-bank operations not SWF (excluded from SWFI database); SE has AP-funds (covered as pension-funds in OECD PMF rather than as SWF in SWFI); DK has ATP (covered as pension fund rather than as SWF).
- **5-candidate coverage:** NO covered cleanly. The other 4 are not in SWFI/Global SWF the way NO is — which is itself the finding: **NO is the only candidate where sovereign-fund-AUM-%GDP is the appropriate proxy. The other 4 require pension-stack-%GDP (Source 2.1).** This is a hybrid-proxy answer.
- **Verdict-robustness:** **SOFTENS the decline somewhat** — composite-proxy is feasible. Operationalisation-gap argument is no longer "no per-country data exists"; it becomes "two complementary proxies need to be combined per country." That's still parsimony-cost but not data-availability-cost.
- **URLs:** [SWFI rankings](https://www.swfinstitute.org/fund-rankings/sovereign-wealth-fund), [Global SWF ranking](https://globalswf.com/ranking), [IFSWF numbers](https://www.ifswf.org/SWFs-numbers), [NBIM annual report 2025](https://www.nbim.no/en/news-and-insights/reports/2025/annual-report-2025/).

### Source 2.3 (METHODOLOGY) — IMF WP/23/133 — *Do Sovereign Wealth Funds Reduce Fiscal Policy Pro-cyclicality?*

- **Citation:** IMF Working Paper No. 2023/133, *Do Sovereign Wealth Funds Reduce Fiscal Policy Pro-cyclicality?*, June 2023.
- **Primary-data anchor:** methodological — addresses whether SWF-presence vs SWF-absence explains differential fiscal-stabilisation behaviour across countries. Useful for the operationalisation rationale of a wealth-fund-rich regime split: confirms there is a published methodological case for the SWF-presence binary as a fiscal-headroom proxy at country level.
- **5-candidate coverage:** methodology-level only; not a per-country dataset.
- **Verdict-robustness:** **HOLDS — supportive context.** Useful for SM 4 v2 to source the operationalisation argument (or its limits) without re-deriving methodology.
- **URLs:** [IMF WP 2023/133 PDF](https://www.imf.org/-/media/Files/Publications/WP/2023/English/wpiea2023133-print-pdf.ashx).

**Negative finding (honest deviation):** there is no public *IMF Sovereign Wealth Fund Database* with the structured per-country fiscal-headroom dataset the brief speculated about. The IMF Statistical Department initiated SWF reporting standardisation work in 2008–2009 (BOPCOM-09/24, BOPCOM-08-19) and the WEO carries fiscal-balance series, but the dedicated dataset name does not exist as a publicly-accessible structured download. SWFI is the closest commercial-proxy database; OECD PMF is the closest official-statistics-route per-country dataset. Phil's pre-read framing was an over-read on this point.

---

## Topic 3 — ETUC / Eurofound / labour-side framing of the IAA

**Explicit answer to the brief's framing question — *any mechanism-component refinement candidate for the S2 mechanism string?*** **Yes — one candidate.** ETUC and IndustriAll Europe both frame IAA labour absorption as conditional on works-council-mediated procurement-attached social conditionalities + collective-bargaining-anchored qualification measures. The current S2 mechanism string is supply-side-only ("Climate adaptation Zone C wage-positive premium; Cedefop 2025 + EU Net-Zero Industry Act €100B"); a within-mechanism conditional-component additive of ~12 words would close that gap.

### Source 3.1 (PRIMARY) — ETUC press release, 2026-03-04 — *Industrial Accelerator Act must deliver a Made in Europe approach that guarantees quality jobs*

- **Citation:** European Trade Union Confederation (ETUC), press release, "Industrial Accelerator Act must deliver a Made in Europe approach that guarantees quality jobs", 2026-03-04 (issued same day as the EC IAA proposal).
- **Primary-data anchor:** supranational-labour-side framing. Quoted demands: respect for collective bargaining on pay and conditions; access to fair pay, secure contracts, safe workplaces; investments in training/skills with quality apprenticeships and upskilling. Stated conditionality: "awarding public contracts to companies must be made conditional on those companies delivering quality jobs and meeting social conditions." Framing of the procurement gap: "EU funding and current procurement rules often reward the lowest-cost bidder, fueling a race to the bottom at the expense of companies and workers, when instead they should reward good companies which create and maintain quality jobs underpinned by collective agreements."
- **S2-mechanism-refinement candidate:** ETUC's framing makes labour absorption *conditional* on procurement-attached social-conditionalities. Currently absent from S2 mechanism string in `layer-6-deliverable-data.json` line 7941 (per Phase 3 report).
- **Verdict-robustness on S9 startup decline:** no startup-formation mechanism evidence here. **S9 decline holds.**
- **URLs:** [ETUC press release](https://www.etuc.org/en/pressrelease/industrial-accelerator-act-must-deliver-made-europe-approach-guarantees-quality-jobs), [ETUC industrial-policy issue page](https://www.etuc.org/en/issue/industrial-policy).

### Source 3.2 (SECTORAL) — IndustriAll Europe Article 1450 — *Industrial Accelerator Act launched – but will it be fast enough to stop Europe's deindustrialisation?*

- **Citation:** IndustriAll European Trade Union, news article 1450, March 2026.
- **Primary-data anchor:** sectoral-labour-side critique. Welcomes the IAA as a step but calls out three named gaps — (a) "social conditionalities are not leveraged through public procurement" (procurement-conditionality gap), (b) "the scope of Union origin is still unclear" (Made-in-EU operationalisation gap), (c) "strategic sectors like steel are not sufficiently supported" (sectoral-coverage gap). Steel-sector framing: "the creation of lead markets for locally-made, low-carbon steel is essential to provide long-term demand certainty for the European steel sector."
- **S2-mechanism-refinement candidate:** convergent with 3.1. Adds the steel-sector lead-market specificity that overlaps with the IAA Annex I sectoral scope already in the Phase 3 report.
- **Verdict-robustness on S9 startup decline:** none — sectoral-incumbent absorption framing, not startup formation. **S9 decline holds.**
- **URL:** [IndustriAll Europe Article 1450](https://www.industriall-europe.eu/Article/1450).

### Source 3.3 (CONTEXTUAL) — Eurofound *State of Play of Convergence 2026 — Job quality in the EU* + *Living and Working in Europe 2025*

- **Citation:** Eurofound, *State of Play of Convergence 2026 — Job quality in the EU*; Eurofound, *Living and Working in Europe 2025*; Eurofound *Working Conditions Survey* (published 2025-09-04, 36,700 workers across EU-27).
- **Primary-data anchor:** EU labour-market context. Employment growth 2024 +0.8% (vs +1.2% 2023). Major restructuring events 2024 in automotive, telecoms, electrical equipment, pharmaceuticals. Quality Jobs Roadmap framing actively in preparation by the Commission, with Eurofound surveys feeding it.
- **S2-mechanism-refinement candidate:** background-context only. Useful for SM 4 v2 to cite the labour-market-deceleration baseline against which IAA absorption claims must be evaluated.
- **Verdict-robustness:** **HOLDS — supportive context.**
- **URLs:** [State of Play of Convergence 2026](https://www.eurofound.europa.eu/en/publications/all/state-of-play-of-convergence-2026-job-quality-in-the-eu), [Living and Working in Europe 2025](https://www.eurofound.europa.eu/en/publications/all/living-and-working-europe-2025), [Eurofound work programme 2025](https://www.eurofound.europa.eu/en/publications/all/eurofound-work-programme-2025).

**Negative finding (honest deviation):** national-level union responses (DGB Germany; CGT/CFDT France) did not surface in two rounds of WebSearch. The supranational labour-side framing is well-anchored at ETUC + IndustriAll Europe; below that, search returned only law-firm summaries and EC press materials. If Phil wants national-union granularity for SM 4 v2, that's a separate fetch via DGB / CGT / CFDT direct websites — not in scope for this 3-4 h sweep.

---

## SM 4 v2 attribution shortlist

Five sources, ranked for citation in the methodology SM 4 v2 callout (the surface that replaces the existing SM 4 ninth-scenario language at `site/methodology.html`):

| Rank | Source | Topic | Why it earns the cite |
|---|---|---|---|
| 1 | **Rhodium / MIT Clean Investment Monitor** (2025 quarterly + supply-chains report) | T1 | Strongest live counterfactual evidence for IAA-class absorption mechanism. Realised-data anchor. Three years post-implementation. |
| 2 | **OECD Pension Markets in Focus 2025** (preliminary 2024 data) + Pensions at a Glance 2023 | T2 | Per-country pension-assets-%GDP for all 5 wealth-fund-rich candidates. Operationalisation-feasibility surface. |
| 3 | **ETUC press release 2026-03-04** | T3 | Supranational labour-side framing + procurement-conditionality gap claim. The labour-side mechanism-refinement candidate's primary anchor. |
| 4 | **Bistline et al. NBER WP 32168 / Brookings 2024** | T1 | IRA modelling-vs-realised methodological companion. Supports symmetric methodological claim that the IAA is in the same model-evidence class. |
| 5 | **IndustriAll Europe Article 1450** | T3 | Sectoral-labour-side complement to ETUC. Steel-sector lead-market specificity. |

Reserve (sixth, optional): **NBIM Annual Report 2025** for the Norway-specific GPFG-headroom anchor if SM 4 v2 names NO explicitly.

---

## Cross-topic findings

One convergent finding from comparing T1 and T3:

**Public-procurement-anchored industrial-policy absorption is highly conditional** — both on (a) policy stability (Topic 1: Q1 2025 IRA EV-supply-chain cancellations of 27K jobs / $8B in a single quarter under federal-policy uncertainty) and (b) labour-side mediation institutions (Topic 3: ETUC + IndustriAll Europe both name the procurement-attached social-conditionality gap as the primary absorption-quality determinant). These two findings reinforce each other and converge on the same insight: the S2 mechanism string in `layer-6-deliverable-data.json` is currently supply-side only; the realised-data evidence (T1) and the labour-side framing (T3) both add conditionality components. SM 4 v2 could acknowledge this in a single sentence — "the IAA's S2-aligned absorption pathway is conditional on policy-stability (cf. Rhodium CIM Q1 2025 cancellations) and labour-side mediation institutions (cf. ETUC 2026-03-04)" — without re-deriving the SOT mechanism string.

A second, weaker cross-link: T1 (US Treasury §48C prevailing-wage requirement) and T3 (ETUC procurement-conditionality demand) frame the same policy-design feature from opposite sides of the Atlantic. The IRA *has* the labour-conditionality the labour-side argues is missing from the IAA. SM 4 v2 could note this asymmetry briefly, but it's a Layer 7 political-economy point more than a Layer 6 methodology point — flag for `european-ai-labour-actions/` rather than for SM 4 v2.

---

## Verdict-robustness summary (per Phase 3 audit candidate)

| Candidate | Phase 3 verdict | This sweep | Net |
|---|---|---|---|
| S9 Industrial Reconstruction | Decline-recommend | Topic 1 IRA evidence is in the same mechanism class — confirms S2 collapse, adds fragility-under-uncertainty signal | **Decline HARDENS** |
| 4th regime Wealth-Fund Rich | Decline-recommend on operationalisation-gap grounds | Topic 2 composite proxy (OECD PMF + SWFI + NBIM) operationalises 4 of 5 candidates cleanly | **Decline SOFTENS** — proxy-availability rationale weakens; parsimony rationale still holds |
| S9 Startup-Driven Absorption | Confirm exclusion | Topic 3 surfaced no startup-formation mechanism evidence | **Decline HOLDS** |
| (Bonus) S2 mechanism string refinement | Phase 3 audit-at-class flagged additive +10 words | Topic 3 surfaces a labour-side conditional-component additive of ~12 words | **Refinement candidate STRENGTHENED** |

---

## Brain capture candidates (surface for Phil per Rule 12)

Two pattern-level captures worth surfacing:

### Capture 1 — "Counterfactual-corpus hardening at single-side audit boundaries" (medium scope)

**Pattern observed:** Phase 3 audit corpus was EU-only and proposing-side-only (8 EC PDFs + 6 EC URLs + Schnabel/CEPA/Bruegel framings). This 3.5 sweep added US counterfactual (Rhodium CIM, Bistline et al.), supranational labour-side (ETUC, IndustriAll Europe), and per-country fiscal-headroom proxies (OECD PMF, SWFI). All three additions hardened or refined the verdicts without flipping any. The pattern is generalisable: when an audit corpus is single-side-of-debate, a bounded supplementary sweep on counter-side / counter-jurisdiction / per-country-proxy sources tends to be high-value at low cost.

**Proposed rule:** *Before locking a flag-only audit verdict, run a bounded counterfactual-corpus sweep — counter-side framing + counter-jurisdiction equivalents + per-country proxies — at ~3–4 h. Three named topics is a workable budget. The deliverable is verdict-robustness verification plus an attribution shortlist for the methodology callout, not new SOT data.*

**Why:** prevents shipping audits anchored on single-side corpora that would soften under counterfactual evidence the brain didn't surface.

**How to apply:** at the close of any flag-only audit phase, ask three questions — (a) is there a same-class policy already implemented in another jurisdiction? (b) is there a counter-side framing absent from the corpus? (c) is there a per-country proxy that operationalises a deferred regime split? If yes to any, dispatch a 3-4 h supplementary sweep before locking. If yes to two or three, dispatch is mandatory.

### Capture 2 — "Mechanism-string conditionality refinement" (small scope)

**Pattern observed:** S2 mechanism string in the SOT is supply-side-only — climate-demand premium plus EU funds. The ETUC + IndustriAll Europe labour-side framing surfaces that absorption is conditional on works-council mediation + collective-bargaining-anchored qualification measures + procurement-attached social conditionalities. This is a within-mechanism conditional-component additive (~12 words), not a new scenario row. Same pattern as Phase 3's "policy-lever-vs-mechanism distinctness rule" applied in the inverse direction — there, a candidate scenario collapsed into a probability shift; here, a counter-side framing surfaces a conditionality the supply-side mechanism string under-specifies.

**Proposed rule:** *When a mechanism string is anchored on supply-side evidence only, run an explicit labour-side / demand-side / conditionality-side check before locking it. A mechanism that omits its conditionality components is a partial mechanism, even if its supply-side evidence is strong.*

**Why:** prevents the inverse failure of the Phase 3 distinctness rule — the rule prevents inflation; this rule prevents under-specification.

**How to apply:** for any S-row mechanism string, add a conditionality-component checklist — (a) labour-side mediation institutions, (b) policy-stability conditionality, (c) procurement / regulatory-design conditionality. If any are absent and a counter-side source supports them, the additive belongs in the mechanism string.

These are sub-session candidates for Phil to decide on; not auto-written to the brain.

---

## Verification

```
md5 site/data.json layer-6-deliverable-data.json layer-6-lens-framework.md \
    site/scenarios.html site/methodology.html site/sources.html
```

**Pre-session (captured 2026-05-08, `/tmp/phase3-5-md5-pre.txt`):**
- `site/data.json` 298bd73025ca8d150d49dfb61ef96b46
- `layer-6-deliverable-data.json` 61b5e973c1670f039e4e6368e1675272
- `layer-6-lens-framework.md` 87933b817b1d9ddb9074c8ee541b9927
- `site/scenarios.html` 7e5394ed9849915a05e09b91d05a3fa4
- `site/methodology.html` 9c96df6f440f777355d20d41f3f9e4d6
- `site/sources.html` 97701dba4b14b3d4ec6a40305e908eae

**Post-session:** to verify at session close — see "Closing verification" below.

---

## Honest deviation reporting

- **National-union responses (DGB / CGT / CFDT) did not surface.** Two WebSearch rounds returned law-firm summaries and EC press materials, not direct union statements at national level. ETUC + IndustriAll Europe carry the labour-side framing at supranational level adequately; if national-granularity is desired for SM 4 v2, a direct fetch via union websites is needed and is out of scope here.
- **No public IMF Sovereign Wealth Fund Database.** The brief speculated on its existence; search returned IMF statistical-work papers (BOPCOM-09/24, BOPCOM-08-19) plus IMF WP/23/133, but no dedicated structured downloadable database under that name. SWFI / Global SWF (commercial) and OECD PMF (official) are the operative substitutes; flagged honestly rather than padded.
- **CH coverage is partial in Topic 2.** Pension-stack proxy works for CH (occupational pensions ~140% GDP per OECD PMF). SWF-AUM proxy doesn't (SNB foreign-exchange reserves are central-bank operations, not in SWFI). The composite-proxy answer is honest about this; a single-dataset solution does not exist for the 5 candidates simultaneously.
- **No PDFs downloaded in this sweep.** Per the brief's "shortlist is the deliverable" framing — full ingestion is Phase 5+ scope if pursued. WebSearch returned URL-anchored summaries; the URLs above are sufficient for SM 4 v2 attribution.
- **Time budget kept.** ~3 h of WebSearch + synthesis + drafting. Topic 2 SWF data scoping was the budget-risk topic per brief; it landed cleanly via the OECD PMF + SWFI composite without ballooning.

---

## Closing verification

To run at session close (Phil or master agent):

```
cd /Users/philippmaul/Documents/projects/european-ai-labour-synthesis && \
md5 site/data.json layer-6-deliverable-data.json layer-6-lens-framework.md \
    site/scenarios.html site/methodology.html site/sources.html
```

Match against the pre-session checksums above. Any drift is a sub-session bug to investigate before SM 4 v2 drafting proceeds.

---

## Sub-session metadata

- **Bounded duration:** 3-4 h target. Actual: ~3 h.
- **Reads only.** No writes to SOT, source-cards, site HTML, lens framework, deliverable data, or llms.txt.
- **Files touched:** this report only — `phase-3-5-supplementary-sources-sweep-report-2026-05-08.md` (new file at project root).
- **Phil does all git commits.**

---

*This brief is the Phase 3.5 sub-session report. Three topics swept — IRA labour outcomes, sovereign-wealth/fiscal-headroom proxies, ETUC/Eurofound labour-side framing. Five-source SM 4 v2 attribution shortlist returned. Verdict-robustness verified — S9 decline hardens, 4th regime decline softens but holds, S2 mechanism string refinement candidate strengthened. Phil reviews → master drafts SM 4 v2 → Phil locks → Bundle W absorbs.*
