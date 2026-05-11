# Suite Verification Log — 2026-04-29

Verification pass across L1–L5 to confirm what's actually live vs documented. Performed during Layer 6 scoping session.

---

## Method

For each layer:
1. Read local repo state (git log, site/ folder, README, CHANGELOG)
2. Fetch live site URL and verify rendered content
3. Compare local vs live vs build plan vs README claims

## L1 — AI Exposure Map (`ai-exposure.nexalps.com`)

**State:** ✅ Live as v2.4.0. Local matches live.

**Site:** index, analysis, methodology, questions, implications, sources, llms.txt. Risk/Opportunity/Context mode toggle deployed. 199.6M jobs, ~130 ISCO 3-digit groups across 36 countries.

**Issues:**
- `PROJECT-SPEC.md` is wildly stale (says "Status: Concept / Pre-Build" from 2026-03-16; site is at v2.4.0)
- Gostev Capability Floor panel **NOT yet deployed** per occupation (in CHANGELOG implementation backlog from 2026-04-28 ingestion)

**Implication for L6:** Lens 1(c) AI labour load reads exposure scores from the live data. Capability floor sensitivity bound is applied at L6 level (Gostev ~9% floor) since L1 doesn't yet expose it.

## L2 — European Job Market (`job-market.nexalps.com`)

**State:** ✅ Live as v1.0 (commit `e737510`). Local matches live.

**Site:** index, analysis, countries, skills, methodology, sources. 9 role families (Data/AI, Sales, Cybersecurity, SE, Design, BizDev, PM, Growth, Operations). 26 sources.

**Regulatory demand creation analysis status (5 of 7 directives present):**

| Directive | On site? |
|---|---|
| NIS2 | ✅ (160K entities, 424K cybersecurity gap) |
| DORA | ✅ (22K financial entities) |
| EU AI Act | ✅ (78% of orgs plan to hire 1–10 AI governance roles) |
| EAA | ✅ (implementation surge 2025–2026) |
| CSRD | ✅ (declining — 80% scope reduction noted) |
| **Platform Work Directive** | ❌ Missing |
| **Pay Transparency Directive** | ❌ Missing |

**Issues:** Two regulatory directives missing. Both are load-bearing for Lens 1 absorption-capacity (Platform Work directly affects freelance/platform coverage gap; Pay Transparency intersects with AI-driven compensation decisions).

**Implication for L6:** cite the 5 that exist; flag the 2 as scope gaps in Lens 1 absorption-capacity section.

## L3 — Disruptions (`disruptions.nexalps.com`)

**State:** ⚠️ Render gap. Data shipped, HTML not extended.

**Local repo:** Active development. BL-07 verification just landed (Copperbelt, São Paulo ABC, Latrobe Valley) — 3 regional cascade cases verified. Retrofit at v0.3.2. `disruptions-data.json` has all 5 expected new keys (verified 2026-04-29):
- `structured_metrics` ✓ (with sub-keys: schema_version, methodology_note, metric_definitions, high_feasibility_cases, medium_feasibility_cases_note, low_feasibility_cases_note, feasibility_matrix_appendix)
- `spreadsheets_counterfactual` ✓
- `incumbent_vs_cohort_displacement` ✓
- `capability_vs_adoption_gap` ✓
- `institutional_response_scope_statement` ✓

**Live site:**
- `cases.html` — references "20 case studies" but does not name them or show structured metrics
- `findings.html` — does NOT show Spreadsheets Counterfactual, Two Eras of Institutional Response, or Methodological Appendix sections
- Feasibility matrix table not rendered

**Issue:** The 2026-04-14 retrofit work shipped data into JSON but render scripts (`scripts/render-findings.py` or equivalent) were not extended to display the new sections. Estimated fix: ~1 day to extend render scripts.

**Implication for L6:** L6 reads `disruptions-data.json` directly until render gap closes. Structural-bias warning carried in L6 document, not delegated to L3 site. Class IV historical anchors (Copperbelt / São Paulo ABC / Latrobe Valley) cite L3 BL-07 verifications.

## L4 — Demographics (`demographics.nexalps.com`)

**State:** ✅ Live. README stale.

**Site:** index, dach, generations, projections, sources. 270M→236M peak-to-2050; 1M workers lost/yr; 1.34 EU fertility; 8–12M Zone C unfillable jobs; Germany −5.6%/−16.9%. 54 sources.

**Issue:** README labels site "v1.0 (pre-launch)"; site has been live and updated since (commit `be67df2` "Replace 'Coming soon — Reskilling' with full Layer 5 entry"). Phil handling separately.

## L5 — Reskilling (`reskilling.nexalps.com`)

**State:** ✅ Live. Local matches live.

**Site:** index, transitions, lenses, systems, countries, dach, sources. All headline numbers verified: 38.72M / 8.67M / 30.05M / 7.55M / 3.34M / ~450K / 5–9 year speed gap. 8 numbered Python scripts (01–08) for data pipeline. 63 primary sources.

**Issues:** None identified.

---

## Summary issues by priority (input to handover prompt)

**P0 (blocks L6 inputs):**
- L3 render gap (data → HTML rendering not extended) — L6 can work around by reading JSON directly, but L3 site is currently misleading (claims 20 cases without naming them; retrofit findings invisible)

**P1 (load-bearing for L6 lens scoring):**
- L2 Platform Work Directive + Pay Transparency Directive missing
- L1 Gostev Capability Floor panel not yet deployed

**P2 (maintenance / hygiene):**
- L1 PROJECT-SPEC.md stale (months out of date)
- L4 README stale (says pre-launch, site is live) — Phil handling separately
