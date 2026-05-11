# Handover Prompt — Bundle E Session 2: Phase 2 Data Acquisition Continuation (2026-04-29)

Self-contained prompt for a fresh session. Continues Bundle E from session 1.

**Session 1 result:** [`layer-6-phase2-data.json`](layer-6-phase2-data.json) — 4 of 10 tasks landed (Tasks 1, 5, 8, 10 fully populated; coverage 86/396 cells = 21.7%). Bundle D (Phase 2 scoring) remains blocked on session 2 completion.

---

## START PROMPT

Continue Bundle E Phase 2 data acquisition. Session 1 ([`bundle-e-phase2-data-acquisition-handover-2026-04-29.md`](bundle-e-phase2-data-acquisition-handover-2026-04-29.md)) shipped Tasks 1, 5, 8, 10. This session targets Tasks 2, 3, 4, 6, 7, 9 (six remaining). Output: extend the existing `layer-6-phase2-data.json` in place — do NOT regenerate from scratch.

### Read FIRST
- [`layer-6-lens-framework.md`](layer-6-lens-framework.md) — locked spec; do NOT modify
- [`layer-6-fetch-list-2026-04-29.md`](layer-6-fetch-list-2026-04-29.md) — secured + open data items (updated end of session 1 with Munich Re design note + Spain Valencia correction + IISS partial-secure)
- [`layer-6-phase2-data.json`](layer-6-phase2-data.json) — current matrix (read `metadata.session_status` for what session 1 did + outstanding gaps)
- [`layer-6-iiss-military-balance-2025-extracts.md`](layer-6-iiss-military-balance-2025-extracts.md) — Phil-supplied IISS extracts (Task 3 + Lens 5 framing input)
- [`bundle-e-phase2-data-acquisition-handover-2026-04-29.md`](bundle-e-phase2-data-acquisition-handover-2026-04-29.md) — original Bundle E spec (10 tasks)

### Same constraints as session 1
- BR-21 per-cell provenance: `derivation_method` + `uncertainty_band` + `source` + `confidence` (H/M/L/U). NO clean numbers.
- BR-19 no fabrication: cite verbatim, flag null + `data_gap_reason`, never invent.
- Phil does all git commits. Stage outputs; Phil executes.
- Country scope: 36 (EU-27 + NO + IS + LI + CH + UK + BA/MK/RS/TR). LI proxies CH where applicable. Use Eurostat conventions: `EL` for Greece, `UK` for United Kingdom.

### Task 10 corrections from master-session adjudication (2026-04-29)

Two regenerations required for Task 10 (`regime_stability`) cells before any new fetch work:

**(A) IRELAND — replace GDP-based regime reading with modified GNI\*:**
The IE 8.1% aggregate / 6.15% per-capita reading from session 1 is a leprechaun-economics artefact (2015 corporate-tax-domicile reclassification: Apple, Google IP relocations drove +24.6% single-year real growth). Domestic-economy reality is ~2–3%. Replace using CSO Ireland modified GNI\* series.
- **Source:** https://www.cso.ie/en/statistics/economy/grossnationalincomemodified/
- **Set IE confidence = M** (manual artefact-correction applied; document the swap explicitly in `derivation_method`)
- Re-evaluate IE's `regime_secular_stagnation_flag` and `regime_post_growth_empirical_flag` against the corrected series
- Add `note` field: "Modified GNI* substituted for headline GDP per Phil adjudication 2026-04-29 — eliminates 2015 corporate-domicile artefact"

**(B) LUXEMBOURG — add new flag for aggregate-distributional split:**
LU's session-1 reading (1.94% aggregate / −0.12% per-capita) is real but should NOT classify as `growth_baseline`. The aggregate growth is immigration-driven (financial-sector inflow), not productivity. Per-capita is the load-bearing reading for labour economics.
- **Add new flag to the regime_stability schema:** `regime_aggregate_distributional_split` = `true` if aggregate >1.5% AND per-capita <0.5%
- LU is the cleanest current example; apply the flag check to all 36 countries (most will be `false`)
- LU should remain in the dataset with both `regime_secular_stagnation_flag` and `regime_post_growth_empirical_flag` evaluated honestly per existing thresholds, plus the new split-flag set true
- Reference: lens-framework Regime Stability Note (Empirical anchors block) lists LU treatment explicitly

These two regenerations happen first in session 2 (5 minutes; ahead of Tasks 7/4/9/3/2/6 in the sequencing below).

### Do this in order (fastest → slowest)

#### 1. Task 7 — EEA EUCRA country-level vulnerability (~2.5h, fastest binding constraint)
**Source:** [EEA European Climate Risk Assessment 2024](https://www.eea.europa.eu/en/about/who-we-are/projects-and-cooperation-agreements/european-climate-risk-assessment) — full report.
**Approach:**
- WebFetch the EEA HTML pages (open access, no WAF expected).
- If the assessment aggregates by N/E/S/W region, decompose to country with explicit derivation note in each cell.
- Score 6 sub-dimensions per country, each 0–1 normalised: wildfire / drought / flood / heat-stress on outdoor work / agricultural disruption / infrastructure stress.
**Output key:** `lens5d_eea_vulnerability` (with all 6 sub-fields).
**Coverage expectation:** EU-27 + EEA full; CH likely flagged via Alpine region; UK pre-Brexit data + national supplement; candidates null+flag.

#### 2. Task 4 — Trade-policy decoupling exposure (~3h)
**Sources:**
- Eurostat external-trade datasets via SDMX (use the same TSV-direct-fetch pattern that worked for Tasks 1+10): `ext_lt_intratrd` or `ds-018995` for trade-with-Russia + trade-with-China-strategic-goods share per country.
- EU export-control register: `https://policy.trade.ec.europa.eu/help-exporters-and-importers/exporting-dual-use-items_en`
- Trans-Atlantic export-control alignment: derive from CBAM + AI Act extraterritorial scope per country (mostly aggregate-EU; flag).
**What to compute per country:** composite score 0–1 reflecting share of trade exposed to decoupling pressure. Components: (a) share of imports from RU + CN (sanctions-architecture exposure), (b) share of exports of dual-use goods to non-aligned, (c) presence of strategic-materials China-dependency (nitrocellulose, REE, etc. — see IISS extracts).
**Output key:** `lens5a_trade_decoupling`.
**Reuse from session 1:** [`layer-6-iiss-military-balance-2025-extracts.md`](layer-6-iiss-military-balance-2025-extracts.md) Section E names China nitrocellulose + electronics + armour-steel dependencies as material attestation.

#### 3. Task 9 — National climate-adaptation budgets (~3h)
**Sources:**
- EU Recovery and Resilience Facility (RRF) climate-adaptation pillar per country: [RRF Scoreboard](https://commission.europa.eu/business-economy-euro/economic-recovery/recovery-and-resilience-scoreboard_en) (open, WebFetch-accessible).
- National Climate Adaptation Plans (NAPs): track via [EEA Climate-ADAPT](https://climate-adapt.eea.europa.eu/).
- Cedefop 2025 green-skills training budgets — overlap with Task 2; do them in same session.
**What to extract per country:** climate-adaptation budget % of GDP, per capita, or absolute (whichever is most reliably available; specify which).
**Output key:** `lens5d_adaptation_budget`.
**Coverage expectation:** EU-27 + UK have NAPs; EEA mixed; candidates likely null. Smaller MS without published NAPs → flag, don't fabricate.

#### 4. Task 3 — Geopolitical fragmentation worker-side (~3h, with narrative)
**Two output keys this time:**
- `lens4_geopolitical` — composite score 0–1
- `lens4_geopolitical_narrative` — 1–2 sentence MSC-grounded country framing (added to spec 2026-04-29)

**Sources:**
- **Defence-labour-demand growth:** SIPRI 2025 (already in fetch-list as secured) + IISS Military Balance 2025 extracts (already secured this session — top-15 figures DE/UK/FR/IT/UA/PL with hard USD; PL/EE/LV/LT >3% GDP; ES/IT <2% GDP). For the other 22 countries, use SIPRI 2025 fact-sheet country tables.
- **Supply-chain reshoring:** EU CRMA + NZIA regional allocations. Derive from [Critical Raw Materials Act](https://commission.europa.eu/strategy-and-policy/priorities-2019-2024/european-green-deal/green-deal-industrial-plan/critical-raw-materials-act_en) + Net-Zero Industry Act 40% domestic-manufacturing target allocations.
- **Migration-flow volatility:** Eurostat asylum applications (`migr_asyappctzm`) + first-time residence permits (`migr_resfirst`) per country, 2022–2025 trend. Use SDMX direct-fetch pattern.
- **Munich Security Reports 2024/2025/2026** — narrative-context source for `lens4_geopolitical_narrative`. Inherit MSC Atlanticist-framing caveat: cite, do not adopt uncritically (same discipline as Tooze framing note in lens-framework).

**Composite score:** weighted average of (a)+(b)+(c). Document the weighting choice in the cell's `derivation_method` field.

#### 5. Task 2 — Cedefop 2025 climate worker-side shocks (~4h, possible WAF risk)
**Source:** [Cedefop Skills Forecast](https://www.cedefop.europa.eu/en/tools/skills-forecast) per-country PDFs (~32 files for EU-27 + UK + NO + a few others).
**Approach:**
- Try WebFetch on each country PDF first.
- If Cedefop WAFs WebFetch (Munich Re pattern), flag specifically which countries failed, then ask Phil to download blocked PDFs and supply via Read tool (he did this for Munich Re + IISS 2025; same workflow works here).
**What to extract per country:** (a) green-economy job creation projection by 2035, (b) carbon-sector job displacement projection by 2035, (c) regional energy-cost asymmetry indicator (use NZIA Net-Zero Acceleration Valley assignments as proxy where Cedefop doesn't break this out).
**Output key:** `lens4_climate_shocks`.

#### 6. Task 6 — Klinger ISCO 3-digit coordination-share (~4h, biggest uncertainty)
**Output:** **separate file** `layer-6-klinger-isco-coordination-share.json` (NOT in main JSON; cross-referenced via `lens5c_klinger_coordination` cell).
**Sources:**
- Eurostat LFS occupational data via SDMX (`lfsq_egan22d` or similar, ISCO 2-digit; ISCO 3-digit only available in restricted access).
- ESCO occupation descriptions: API at `https://ec.europa.eu/esco/api/` for ~130 ISCO 3-digit groups.
**What to do:**
- Try ESCO+LFS join first.
- **If insufficient data:** ship the spec-authorized fallback (default 0.4 for management ISCOs / 0.2 for professional / 0.1 for clerical). Document the fallback explicitly in `derivation_method`.
**Output:** per-ISCO 3-digit code, coordination-layer share 0–1 + confidence flag.
**Cross-country:** apply same coefficient across countries (occupation-level, not country-level).

### Verification (same as session 1)
1. BR-21 spot-check 5 random cells across new tasks.
2. `metadata.data_gaps` array updated with new entries; old entries cleared where now populated.
3. Candidate coverage realism: BA/MK/RS/TR likely have data only for Tasks 1, 4 (partial), 5 (IPA III separate), 8, 10. Other tasks flag as gap.
4. JSON validates; all 36 country keys present.
5. No clean numbers anywhere.
6. **Update `metadata.session_status`** with session 2 deltas: tasks_completed, tasks_pending, blockers_encountered.

### Realistic yield expectation
6 tasks × ~3h average = 18h target — multi-day still possible. Minimum-viable session 2 finishes Tasks 7, 4, 9 (the 3 fastest with established WebFetch patterns). Tasks 2, 3, 6 may slip to session 3 if Cedefop WAF or ESCO data resolution blocks.

### When done — report back with
- 6 tasks status (✅ / ⚠️ / ❌)
- Total cells populated vs planned (target after session 2: ~70% of 396 = ~277 cells)
- Top 3 remaining gaps
- Klinger status (default-coefficient fallback shipped vs LFS+ESCO derivation)
- Whether Bundle D (Phase 2 scoring) can now proceed
- Updated `data_gaps` count

### Blockers anticipated
- **Cedefop WAF** (analogous to Munich Re session 1) — if blocks, ask Phil for manual PDF download
- **EEA EUCRA regional aggregation** — if 6 sub-dimensions aren't published per country, decompose with explicit methodology note
- **Eurostat trade-with-China-strategic-goods** — may require multiple SDMX queries combined
- **MSC reports paywall/access** — if blocked, the narrative key ships with `[citation pending direct read]` per BR-19 + a 1-sentence framing derived from the reports' public summaries

### Reuse from session 1
- **Eurostat SDMX TSV-direct-fetch pattern** (memory: `feedback_eurostat_sdmx_pattern.md`) — confirmed reliable for tabular data; do NOT use databrowser SPA URLs.
- **Phil-supplied PDF read pattern** — when WAF blocks WebFetch, ask Phil to drop PDF in `~/Downloads/`; pdftotext extracts cleanly.
- **Build script** — extend `/tmp/build_layer6_phase2_data.py` from session 1 (or rewrite if no longer in /tmp); same INPUT_KEYS dict; same null-cell + pending-cell generators.

## END PROMPT
