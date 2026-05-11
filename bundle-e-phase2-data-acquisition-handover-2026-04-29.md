# Handover Prompt — Bundle E: Phase 2 Data Acquisition (2026-04-29)

Self-contained prompt for a fresh session. Does not require prior conversation context.

Runs in parallel with Bundle A (L3 fixes) and Bundle B (Phase 1 re-score). Bundle D (Phase 2 scoring) is blocked on Bundle E completion.

---

## START PROMPT

I need you to acquire 9 datasets needed for Layer 6 Phase 2 scoring of the European AI Labour Market suite. Output is one consolidated `layer-6-phase2-data.json` with per-country-per-input matrix that the next session (Phase 2 scoring) reads as canonical input. This session is data acquisition only — does NOT do any scoring or analysis.

Read FIRST:
- `projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — locked spec. Do NOT modify.
- `projects/european-ai-labour-synthesis/layer-6-fetch-list-2026-04-29.md` — secured + open data items
- `projects/european-ai-labour-synthesis/layer-6-phase1-scoring.csv` — Phase 1 country scope (may be 32 or 36 depending on Bundle B status)

Country scope: 36 (EU-27 + NO + IS + LI + CH + UK + 4 candidates BA/MK/RS/TR). Where data isn't available for candidates (which is most of these), flag as `null` with `data_gap_reason`. Where data isn't available for LI (proxy country), flag similarly.

### Constraints

- Per BR-21: every cell ships with `derivation_method` + `uncertainty_band` + `source` + `confidence` flag (H/M/L/U). NO clean numbers.
- Where primary source paywalled or unavailable: log with `data_gap_reason` and propose fallback (e.g., "EUROSTAT proxy" or "estimated from regional aggregate"). NEVER fabricate numbers.
- Per BR-19: cite verbatim where possible; `[citation pending direct read]` where partial.
- Phil does all git commit + push. Stage outputs; Phil executes.

### Output structure (single canonical JSON)

`projects/european-ai-labour-synthesis/layer-6-phase2-data.json`:

```json
{
  "metadata": {
    "fetch_date": "2026-04-29",
    "br21_compliant": true,
    "country_scope": ["AT", "BE", ...],
    "data_gaps": [
      {"country": "BA", "lens": "lens5d_eea_vulnerability", "reason": "EEA EUCRA 2024 covers EU+EEA only; no candidate data"},
      ...
    ]
  },
  "country_data": {
    "DE": {
      "lens4_gini": {
        "value": 31.7,
        "unit": "Gini coefficient (0–100)",
        "derivation_method": "Eurostat ilc_di12 — direct read",
        "uncertainty_band": "±0.5",
        "source": "https://ec.europa.eu/eurostat/databrowser/view/ilc_di12/...",
        "source_year": 2024,
        "confidence": "H"
      },
      "lens4_climate_shocks": { ... },
      ...
    },
    ...
  }
}
```

### The 9 fetch tasks

#### Task 1 (Lens 4) — Gini coefficient per country
**Source:** Eurostat `ilc_di12` (Gini coefficient of equivalised disposable income)
**URL:** https://ec.europa.eu/eurostat/databrowser/view/ilc_di12
**Coverage:** EU-27 + most EEA. Candidates: try Eurostat candidate-country data; fall back to World Bank Gini if unavailable.
**Output key:** `lens4_gini`

#### Task 2 (Lens 4) — Climate transition worker-side shocks per country
**Source:** Cedefop 2025 Skills Forecast country reports (per-country PDFs at https://www.cedefop.europa.eu/en/tools/skills-forecast)
**What to extract:** For each country, identify (a) green-economy job creation projection by 2035, (b) carbon-sector job displacement projection by 2035, (c) regional energy-cost asymmetry indicator (use NZIA Net-Zero Acceleration Valley assignments as proxy)
**Coverage:** EU-27 + UK + Norway typically. Candidates likely no.
**Output key:** `lens4_climate_shocks`

#### Task 3 (Lens 4) — Geopolitical fragmentation worker-side per country
**Sources:**
- Defence-sector labour demand: SIPRI 2025 + ReArm Europe national escape clause activations (17 member states activated as of Feb 2026)
- Supply-chain reshoring: derive from EU Critical Raw Materials Act + Net-Zero Industry Act regional allocations
- Migration flow volatility: Eurostat asylum applications + first-time residence permits per country, 2022–2025 trend
- **Munich Security Reports 2024 + 2025 + 2026** (https://securityconference.org/en/publications/munich-security-report/) — narrative-context source for strategic framing of multi-front conflict + decoupling. NOT direct quantitative input; cited in methodology section for Lens 5(a) interpretation. Inherit caveat: MSC has Atlanticist framing — cite, do not adopt uncritically (same discipline as Tooze framing note).
**What to extract per country:** composite score (0–1) reflecting (a) defence-labour-demand growth rate, (b) supply-chain-reshoring exposure, (c) migration-flow volatility. Plus narrative-frame summary (1–2 sentences per country) drawn from MSC reports where relevant.
**Output key:** `lens4_geopolitical` (composite score) + `lens4_geopolitical_narrative` (MSC-grounded framing per country)

#### Task 4 (Lens 5a) — Trade-policy decoupling exposure per country
**Sources:**
- EU export-control register (https://ec.europa.eu/trade/policy/...)
- Sanctions architecture exposure: trade-with-Russia + trade-with-China-strategic-goods share per country (Eurostat external trade data)
- Trans-Atlantic export-control alignment (CBAM, AI Act extraterritorial effect)
**What to extract per country:** composite score (0–1) reflecting share of trade exposed to decoupling pressure
**Output key:** `lens5a_trade_decoupling`

#### Task 5 (Lens 5a) — EU MFF country-level allocation breakdown
**Sources:**
- EU MFF 2021–2027 country-level allocations (https://commission.europa.eu/strategy-and-policy/eu-budget/long-term-eu-budget/2021-2027_en)
- Mid-term review 2024 €64.6B reinforcement breakdown per country (where Ukraine Facility, migration support, emergency funding land)
- ReArm Europe SAFE €150B loan uptake per country (as of Feb 2026)
**What to extract per country:** (a) MFF allocation share % of GDP, (b) mid-term review reinforcement share, (c) SAFE uptake. Composite as bandwidth-tax proxy.
**Output key:** `lens5a_eu_mff_allocation`

#### Task 6 (Lens 5c) — Klinger coordination-share per ISCO 3-digit
**Note:** Spec already flags this as "if data permits, else flag as Phase 2 refinement."
**Sources:**
- Eurostat LFS occupational data with management/professional/clerical breakdown by ISCO
- ESCO occupation descriptions tagged for coordination-layer share (manual coding may be required for ~130 ISCO 3-digit groups)
**What to extract:** per ISCO 3-digit group, estimated coordination-layer share (0–1). Apply same coefficient across countries (this is occupation-level, not country-level).
**Output:** Separate file `projects/european-ai-labour-synthesis/layer-6-klinger-isco-coordination-share.json`. If insufficient data → ship a partial coverage with explicit gap flags + fallback method note (e.g., "default 0.4 for management ISCOs, 0.2 for professional, 0.1 for clerical").
**Output key:** `lens5c_klinger_coordination` (referenced from main JSON via the separate file)

#### Task 7 (Lens 5d) — EEA EUCRA country-level vulnerability scores
**Source:** EEA European Climate Risk Assessment 2024 — full report at https://www.eea.europa.eu/en/about/who-we-are/projects-and-cooperation-agreements/european-climate-risk-assessment
**What to extract:** Per country (EU+EEA), score on 6 vulnerability sub-dimensions:
- Wildfire risk
- Drought severity
- Flooding exposure
- Heat-stress on outdoor work
- Agricultural disruption
- Infrastructure stress
Each 0–1 normalised. EUCRA 2024 may aggregate by region (N/E/S/W); if so, decompose to country with explicit derivation note.
**Coverage:** EU-27 + EEA. Candidates: not covered; flag.
**Output key:** `lens5d_eea_vulnerability`

#### Task 8 (Lens 5d) — Munich Re per-country 2024 + 2025 disaster losses
**Source:** Munich Re NatCat factsheets — https://www.munichre.com/en/company/media-relations/media-information-and-corporate-news/media-information/2026/natural-disaster-figures-2025.html (2025) + https://www.munichre.com/en/company/media-relations/media-information-and-corporate-news/media-information/2025/natural-disaster-figures-2024.html (2024)
**What to extract per country:** Total losses + insured losses for 2024 + 2025 (USD billions), event types (wildfire/flood/storm/etc.), %GDP impact
**Coverage:** Whatever Munich Re reports per country. EU large economies likely covered; smaller may aggregate.
**Output key:** `lens5d_munichre_losses`

#### Task 9 (Lens 5d) — National climate-adaptation budget allocations per country
**Sources:**
- EU Recovery and Resilience Facility climate-adaptation pillar allocation per country
- National Climate Adaptation Plans (where filed; track via EEA Climate-ADAPT)
- Cedefop 2025 Skills Forecast country reports (Task 2 overlap — green skills training budget)
**What to extract per country:** climate-adaptation budget % of GDP, per capita, or absolute (whichever is most reliably available)
**Coverage:** EU-27 + UK have national plans. EEA mixed. Candidates likely no.
**Output key:** `lens5d_adaptation_budget`

#### Task 10 (Regime Stability) — Real GDP growth per country 2010–2024 (NEW 2026-04-29; partial complete in session 1)

**SESSION 1 COMPLETION NOTE (2026-04-29):** First Bundle E session shipped 36/36 country coverage but flagged Ireland as a `leprechaun_economics_artefact` requiring fix. **Continuation session must regenerate IE entry from CSO modified GNI\* series**, NOT GDP — 2014–2024 GDP includes the 2015 corporate-tax-domicile reclassification (+24.6% real-growth single-year reading inflates 10-year aggregate to 8.1%). Modified GNI* gives ~2–3% for the same period, which is the correct domestic-economy regime reading. CSO Ireland publishes modified GNI* annually; URL: https://www.cso.ie/en/statistics/economy/grossnationalincomemodified/

**Luxembourg note:** LU shows 1.94% aggregate / −0.12% per-capita over 10 years (immigration-driven aggregate growth, no productivity / real-wage progress). Treat LU as `aggregate_distributional_split` flag, NOT `growth_baseline` — per-capita is the load-bearing reading for labour economics. Add this as a separate output field for affected countries.

**Source:** Eurostat `nama_10_gdp` (real GDP growth, chain-linked volumes) + `nama_10_pc` (real per-capita GDP growth)
**URLs:**
- Aggregate: https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp
- Per-capita: https://ec.europa.eu/eurostat/databrowser/view/nama_10_pc
**What to extract per country:**
- 10-year sustained average real GDP growth (aggregate), 2014–2024
- 10-year sustained average real per-capita GDP growth, 2014–2024
- Soft threshold flag: `secular_stagnation` = true if aggregate <1.5% sustained
- Hard threshold flag: `post_growth_empirical` = true if per-capita <1.0% sustained
**Coverage:** EU-27 + EEA + CH + UK reliable. Candidates: try Eurostat candidate-country GDP series; fall back to World Bank WDI.
**Why this matters:** Regime Stability Note in lens framework (added 2026-04-29) classifies countries by regime (growth-baseline vs post-growth). Scenario implications differ by regime per the comparison table in the framework. Phase 2 scoring requires this classification to apply scenario perturbations correctly.
**Output keys:** `regime_aggregate_growth_10y_avg`, `regime_per_capita_growth_10y_avg`, `regime_secular_stagnation_flag` (bool), `regime_post_growth_empirical_flag` (bool)
**Effort:** ~30 min — lightweight Eurostat fetch.

### Sequencing within session

Suggested order — fastest to slowest:
1. Task 1 (Gini) — Eurostat direct, ~30 min
2. Task 8 (Munich Re) — published factsheets, ~45 min
3. Task 7 (EEA EUCRA) — full report read, ~2–3 hours
4. Task 5 (EU MFF allocation) — multiple sources, ~2 hours
5. Task 4 (Trade-policy decoupling) — derived from multiple Eurostat external trade tables, ~3 hours
6. Task 9 (Adaptation budgets) — RRF + national plans, ~3 hours
7. Task 2 (Climate worker-side) — Cedefop country PDFs (up to 32 PDFs), ~4 hours
8. Task 3 (Geopolitical fragmentation) — composite of 3 sources, ~3 hours
9. Task 6 (Klinger coordination-share) — biggest unknown; up to ~4 hours; ship partial if blocked

**Total estimate:** ~22 hours of work, distributed across multiple sub-fetches. Realistic over 2 working days.

### Verification

Before declaring complete:
1. **Per-task BR-21 compliance:** every cell has derivation_method + uncertainty_band + source + confidence. Spot-check 5 random cells.
2. **Data gap log:** the `metadata.data_gaps` array enumerates every (country, input) pair where data wasn't available + reason
3. **Candidate coverage realism:** BA, MK, RS, TR likely have data only for Tasks 1, 4, 5, 8. Other tasks should flag as gap, not fabricate.
4. **JSON validates:** parse the output file; ensure all 36 country keys are present (with gap flags where applicable)
5. **No clean numbers:** every numeric value has explicit derivation + uncertainty. If you see a bare integer or float without context, it's an error.

### When done

Report back with:
- 9 tasks status (✅ complete / ⚠️ partial / ❌ blocked)
- Total cells populated vs total cells planned (36 countries × 9 inputs = 324; expect ~70% coverage realistically)
- Top 3 data gaps that would change Phase 2 scoring quality if surfaced
- Klinger coordination-share status (this is the biggest uncertainty — report whether a defensible approach was found)
- Suggested fallback methods for any blocked tasks
- Whether Bundle D (Phase 2 scoring) can proceed with current coverage or whether one more fetch session is required

## END PROMPT
