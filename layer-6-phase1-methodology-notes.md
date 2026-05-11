# Layer 6 Phase 1 — Methodology Notes

_Generated 2026-04-29 alongside `layer-6-phase1-scoring.csv` and `layer-6-phase1-scoring.json`._
_Spec: `layer-6-lens-framework.md` (locked 2026-04-29). Lenses applied: 1 + 2. Lenses 4 + 5 deferred to Phase 2. Fragility classes (I–IV) deferred to Phase 3._

---

## 1. Scope (32 countries)

EU-27 + NO + IS + LI + CH + UK = **32**.

The locked spec line 18 reads "36 (EU-27 + EEA + CH + UK)" but the enumeration sums to 32 (27 + 3 EEA EFTA states + CH + UK). This is the count repeated in the user prompt verification step. Phase 1 outputs use **32**. Reconciliation candidates Phil should adjudicate before Phase 2:

- Treat "36" as a typo for "32" (most likely — see math).
- Add accession candidates (BA, MK, RS, TR) — they are present in L1 employment data but not in L4 / L5.
- Add microstates (AD, SM, MC, VA) — no data in any layer; would all be very-low-confidence proxies.

ISO codes use Eurostat convention (`EL` for Greece, `UK` rather than `GB`) to match L1 source.

**Caveats surfaced during Bundle E session 1 (2026-04-29) for Phase 2 regime classification:**
- **IE leprechaun-economics artefact** — Eurostat tec00115 records IE 2015 real GDP growth at +24.6% from corporate-tax-domicile reclassification, not real-economy expansion. Inflates IE 10-yr aggregate avg to 8.1% (highest in scope). For Phase 2 regime-stability classification, supplement with CSO modified GNI* national accounts before treating IE as a growth-baseline outlier. Flagged in `regime_stability` cell `note` field of `layer-6-phase2-data.json`.
- **LU divergent regime signal** — aggregate growth 1.94% but per-capita CAGR −0.12% over 2014-2024. Aggregate-vs-distributional axis applies: aggregate growth is immigration-driven, not productivity-driven. Phase 2 regime classification should not treat LU as a growth-baseline economy despite passing the secular_stagnation threshold.
- **BA per-capita series-break** — Eurostat sdg_08_10 returns anomalous "0/10" values for Bosnia-Herzegovina; aggregate-only `regime_stability` reading. WB WDI per-capita is the fallback if needed in Phase 2.

---

## 2. Lens 1 — Displacement Velocity / Absorption Capacity

### 2.1 Displacement velocity

For each country, **employment-weighted average technical exposure score** across 125 ISCO 3-digit occupations from L1 (`european-ai-exposure-map/site/data.json` → `treemap`). Per-occupation `technical_score` ranges empirically 1.5–9.5 across the dataset. Per-country employment from `emp` field on each ISCO 3-digit node.

Weighted formula:

```
tech_avg = Σ(emp_isco × technical_score_isco) / Σ(emp_isco)
exposure_idx = (tech_avg − 1.5) / (9.5 − 1.5)   # normalised to [0, 1]
```

Range across 32 countries: **0.431 (RO) → 0.620 (LU)** — a relatively compressed range. The compression is itself a finding: most corridor differentiation in Phase 1 comes from the absorption side, not the exposure side.

**Klinger coordination-share weighting (spec line 411-436): NOT applied in Phase 1.** L1 data does not contain a coordination/decision/execution decomposition per ISCO 3-digit code. Flagged as Phase 2 enrichment.

**Gostev sensitivity floor (~9% Q1 2026 capability lower bound): noise band only.** All country `exposure_idx` values fall in 0.43–0.62, well above the 0.09 floor. Floor would matter for occupation-level sub-analysis (Phase 2) where individual ISCO codes can score below 0.10.

**Liechtenstein:** L1 has no employment data for LI. Used CH (Germanic Dual peer, microstate adjacency, similar wage profile) as donor. `l1_proxy: true` flagged in JSON output.

### 2.2 Absorption capacity

Per-country cross-zone Zone A→C transition rate from the **L5 system model (per user spec, NOT raw L5 data)**:

| System | Rate (low–high %/yr) | Midpoint | Countries (Phase 1 assignments) |
|---|---|---|---|
| Nordic flexicurity | 8 – 12 | 10.0 | DK, SE, FI, NO, IS |
| Germanic Dual | 3 – 6 | 4.5 | DE, AT, CH, LI |
| Continental Corporatist | 5 – 8 | 6.5 | FR, NL, BE, LU |
| Liberal Market | 2.8 – 3.6 | 3.2 | UK, IE |
| Southern European | 2 – 5 | 3.5 | IT, ES, PT, EL, MT, CY |
| Central/Eastern European | 2 – 5 | 3.5 | PL, CZ, HU, RO, BG, HR, SI, SK, EE, LV, LT |

**Discrepancy with L5 raw data.** L5 (`reskilling-data.json` → `systems`) reports Liberal Market rate as **5–8%** — closer to Continental Corporatist than to the user-spec 2.8–3.6%. User spec value used here per session instruction; flag to reconcile with Phil before Phase 2 (likely deliberate downward calibration: ALMP-spend-as-share-of-GDP for UK is 0.03%, vs 0.9% for Continental Corporatist, so 2.8–3.6% is more consistent with funding-side reality than the L5 headline range).

**Country assignments outside L5 raw lists** (Phase 1 first-pass, all flagged in methodology):

- IS → Nordic flexicurity (cultural + institutional peer to DK/SE/FI/NO; not in L5 list).
- LI → Germanic Dual (CH-adjacent microstate; uses CH labour-market institutions; not in L5 list).
- LU → Continental Corporatist (small-economy fiscal-services profile, Continental peer group).
- BG, HR, SI, SK, EE, LV, LT → Central/Eastern European extension. EE often categorised as Nordic-style on digital infrastructure and ALMP intensity but funding/scale closer to CEE; flagged as borderline for Phase 2 review.
- MT, CY → Southern European (Mediterranean labour-market institutions; small-island modifier not yet applied).

### 2.3 Time-horizon adjustment

Spec: "AI 1–3yr, reskilling 5–9yr → use 5x speed-gap coefficient from L5." Implementation:

```
absorption_idx = (rate_midpoint_pct / 100) × 5      # 5-yr cumulative absorption window
```

So Nordic 10%/yr → 0.50 cumulative over 5 years. Germanic 4.5%/yr → 0.225. Liberal 3.2%/yr → 0.16. The 5-year horizon is the *reskilling* lower bound; AI displacement happens faster, but the ratio compares displacement potential against the absorption window the system can plausibly deliver against.

### 2.4 Ratio + corridor thresholds

```
ratio = exposure_idx / absorption_idx
```

Spec thresholds (first-pass anchors, **not validated**):

| Ratio | Corridor | Mechanism |
|---|---|---|
| < 1.5 | 1 — Managed Transition | Absorption capacity matches/exceeds displacement |
| 1.5 – 3.0 | 2 — Bifurcated Absorption | Displacement exceeds absorption but middle-skill bifurcation softens aggregate impact |
| > 3.0 | 3 — Displacement Without Absorption | Velocity overruns reskilling pathway structurally |

**Corridor 2 bifurcation criterion not applied in Phase 1.** Spec says "1.5–3 AND middle-skill share > 60%" for C2. Phase 1 used `1.5 ≤ ratio ≤ 3.0 → C2` as default; the middle-skill-share gate requires per-country labour-force-by-skill-tier data (not in L1). Phase 2 enrichment.

**Calibration note (NOT a footnote — applied as a flag):** per spec lines 355–362, Corridor 1 is narrower than historical base rates suggest; Corridor 3 is broader. Several Phase 1 countries near the C2/C3 boundary (PL 2.96, MT 2.91, EE 2.90, HR 2.89, CY 2.89) are plausibly already C3 under structural-bias adjustment. Phase 3 validation will re-test thresholds against historical base rates.

---

## 3. Lens 2 — Demographic Buffer or Accelerant

### 3.1 Demographic load (annual working-age shrinkage rate, 2025–2035)

L4 (`demographics-data.json` → `projections.working_age`) provides **8 direct entries** (EU27, DE, AT, CH, FR, IT, ES, NL). For each:

```
y2035_interp = (y2030 + y2040) / 2                    # linear midpoint
load = (y2035_interp / y2025)^(1/10) − 1              # CAGR, decimal
```

Direct values (decimal/yr): DE −0.00704, AT −0.00377, CH **+0.00185** (positive), FR −0.00270, IT −0.00681, ES −0.00193, NL −0.00185.

For the **24 countries without direct projections**, two-tier proxy:

(a) `country_divergence` tier proxy (L4 lists 19 countries across three tiers):

| Tier | Annual rate proxy | Anchor logic |
|---|---|---|
| sharpest_decline | −0.85 % | Anchored on IT direct (−0.68 %) + LV/LT/BG cluster (worse, ~ −1.0 %) |
| moderate_decline | −0.50 % | DE direct (−0.70 %) + AT direct (−0.38 %) cluster |
| relative_resilience | −0.20 % | FR direct (−0.27 %) + IE/SE pattern (Eurostat 2024 baseline) |

(b) **Outside-tier proxies** (12 countries not in any L4 tier — manual assignment):

| ISO | Rate | Rationale |
|---|---|---|
| CH | +0.18 % | L4 direct |
| NO | −0.20 % | Nordic resilience peer |
| IS | −0.10 % | Small + relatively young population |
| LI | +0.15 % | CH proxy |
| LU | −0.10 % | Immigration-buffered, very low decline |
| EE | −0.80 % | Baltic, near-sharpest |
| CZ | −0.60 % | CEE moderate-sharp |
| HU | −0.70 % | CEE moderate-sharp |
| SK | −0.70 % | CEE moderate-sharp |
| SI | −0.70 % | CEE moderate-sharp |
| CY | −0.40 % | Med small-island, immigration buffer |
| UK | −0.30 % | Moderate (ONS 2023 baseline) |

`demographic_load_src` field in JSON output records which source applied per country.

### 3.2 Retirement offset (% of high-exposure roles absorbed by retirement by 2035)

L5 (`reskilling-data.json` → `reskilling_gap.by_country`) provides **7 direct entries** (DE, FR, IT, ES, UK, AT, CH). Computation:

```
retirement_offset = retirement_2035 / high_exposure
```

Direct values: DE 24.6 %, FR 21.0 %, IT 25.3 %, ES 23.3 %, UK 21.4 %, AT 21.6 %, CH 23.4 %. EU27 aggregate: **22.4 %** (8.67M / 38.72M).

For the **25 countries without direct data**, EU27 baseline ± country-divergence tier modifier:

| Tier | Modifier | Result |
|---|---|---|
| sharpest_decline | +4 pp | 26.4 % (older population) |
| moderate_decline | +1 pp | 23.4 % |
| relative_resilience | −2 pp | 20.4 % |
| outside any tier | 0 | 22.4 % |

`retirement_offset_src` field in JSON output records source.

### 3.3 Occupation overlap score

The non-obvious hypothesis (spec line 113–114): does demographic shortage (mostly Zone C — care, healthcare, trades, infrastructure) overlap with displaced occupations (mostly Zone A — admin, clerical, business support, customer service)?

L5 `transitions.a_to_c` documents the actual overlap structure:

- Admin → Care assistant: skills_distance 6/10, training 3–12 mo, wage cut −33% (DE) / −20% (FR) / −12% (UK) — feasibility "moderate"
- Customer service → Care assistant: skills_distance 5/10, training 3–12 mo, wage cut −25% (DE) — feasibility "moderate-high"
- Admin → Registered nurse: skills_distance 8/10, training 24–36 mo, wage cut −17% (DE) — feasibility "low"
- Business admin → Electrician: skills_distance 8/10, training 12–24 mo, wage cut −28% (DE) — feasibility "low"

Overlap is structurally constrained: high skills distance, mandatory certifications, substantial wage cuts. Phase 1 uses **system-level base values** (per-country occupation × age data not available):

| System | Overlap base | Logic |
|---|---|---|
| Nordic flexicurity | 0.40 | Strong activation + individual learning accounts → highest practical overlap |
| Continental Corporatist | 0.25 | Training accessible but skewed to advantaged cohorts |
| Liberal Market | 0.25 | Market-driven transitions, no protection bridge |
| Germanic Dual | 0.20 | Beruf system rigid; lateral moves blocked |
| Southern European | 0.20 | Insider/outsider rigidity → displaced → LTU |
| Central/Eastern European | 0.20 | Low ALMP funding |

Range 0.20–0.40 across 32 countries. **Phase 2 enrichment:** per-country occupation × age × shortage-sector data (Cedefop 2025 country reports + EURES vacancy data).

### 3.4 Lens 2 modifier rules

Spec:

```
retirement_offset ≥ 80% AND overlap > 0      → buffer holds → shift toward Corridor 1
retirement_offset < 50% OR  overlap = 0      → buffer fails → stay or shift to Corridor 3
intermediate                                  → no modifier
```

**Empirical result:** 32 / 32 countries fall in `buffer_fails`. Maximum retirement offset across the dataset is 26.4 % (sharpest_decline tier proxy). No country comes within 50 percentage points of the `buffer_holds` threshold. **The buffer thesis is structurally refuted by this dataset** (see findings document).

`buffer_fails` rule says "stay OR shift to 3" — Phase 1 uses **stay** (don't auto-promote everyone to C3) until per-country evidence supports a structural shift. Combined corridor v1 = Lens 1 corridor for all 32 countries.

---

## 4. Confidence flag

Per-country data-density count:

- L1 employment-weighted exposure: direct for 31/32 (LI proxied from CH).
- L2 demographic load: direct for 7/32 (EU27, DE, AT, CH, FR, IT, ES, NL — minus EU27 = 7), tier proxy for 19, outside-tier proxy for 6.
- L2 retirement offset: direct for 7/32 (DE, FR, IT, ES, UK, AT, CH), EU27-baseline-with-tier-modifier for 25.

Rule:

```
0 proxies → high
1 proxy   → medium
2+ proxies → low
MT, CY, LU, IS, LI flagged ≥2 regardless (sparse-data per spec).
```

Distribution: 6 high (DE, AT, CH, FR, IT, ES), 2 medium (NL, UK), 24 low.

---

## 5. Decisions needing Phil's review before Phase 2

1. **Country count — 36 vs 32.** Spec says 36; arithmetic = 32. Reconcile.
2. **Liberal Market transition rate — 2.8–3.6 % (user spec) vs 5–8 % (L5 raw).** Material to UK + IE corridor assignment (currently both C3; would shift to C2 under L5 raw).
3. **Estonia system assignment — CEE vs Nordic-light.** EE digital-state institutions are Nordic-pattern; ALMP funding is CEE-pattern. Currently CEE; rate-low 2.0% may understate.
4. **Liechtenstein** — keep as CH-proxy or drop entirely? Adds noise without adding signal.
5. **Corridor 2 bifurcation gate** — Phase 1 ignores the "middle-skill share > 60%" criterion. If applied strictly, several C2 countries may demote to C3. Defer to Phase 2 with labour-force-skill-tier data?
6. **Structural-bias warning** — Phase 1 documents this as calibration note; Phase 3 validation. Phil to confirm timing.

---

## 6. Excluded / deferred (per session scope)

- **Lens 4 (Compounding Shocks)** — Phase 2.
- **Lens 5 (Polycrisis Drag)** — Phase 2.
- **Fragility classes I–IV** — Phase 3 (requires full scenario stack).
- **Scale tags (aggregate / distributional / both)** — Phase 3.
- **Klinger coordination-share weighting** — Phase 2.
- **Task → employment lag retrofit** (containers, ATMs, CAD, DTP from L3) — Phase 2.
- **Site build (synthesis.nexalps.com)** — Phase 5.
- **Synthesis document draft** — Phase 4.

---

## 7. File integrity

```
projects/layer-6-phase1-scoring.csv         36 rows + header (32 original + 4 candidates appended 2026-04-29)
projects/layer-6-phase1-scoring.json        meta + 36 rows with traceability fields
projects/layer-6-phase1-methodology-notes.md (this file)
projects/layer-6-phase1-findings.md         first-pass observations
```

Reproducibility: `python3` script archived at `/tmp/layer6_phase1.py` during this session — re-run produces byte-identical CSV/JSON given current input data files. Bundle B candidate-row append is reproducible from L1 `data.json` + the candidate-baseline absorption proxy documented in §8 below.

---

## 8. Candidate Country Treatment (added 2026-04-29, Bundle B re-score)

### 8.1 Scope reconciliation

The locked spec (`layer-6-lens-framework.md`, line 18) was correct: country scope is **36** = EU-27 (27) + EEA non-EU (NO, IS, LI = 3) + CH (1) + UK (1) + **candidates (BA, MK, RS, TR = 4)**. The original Phase 1 session inadvertently dropped the 4 candidates and produced 32; Bundle B (this update) appends the 4 candidate rows. The reconciliation question raised in §1 above ("treat 36 as a typo for 32") is now resolved — 36 is the correct count, and the 4 candidates are the missing rows.

### 8.2 Coverage profile of candidates

Candidates have **L1 employment-weighted exposure data** (treemap with `emp` field for all four ISO codes confirmed in `european-ai-exposure-map/site/data.json`). They lack **L4 demographic projections** (`demographics-data.json` covers EU-27 + CH + UK only) and **L5 reskilling-system data** (`reskilling-data.json → systems` does not classify Western Balkans / Turkey institutional patterns). Phase 1 candidate rows therefore carry **Lens 1 only**; Lens 2 fields are null.

### 8.3 Lens 1 displacement velocity (candidates)

Identical methodology to §2.1 — employment-weighted technical exposure across the 125 ISCO 3-digit occupations, normalised to [0, 1] via `(tech_avg − 1.5) / 8.0`. L1 emp coverage is sufficient for all four candidates (BA 1.22M, MK 0.68M, RS 2.75M, TR 31.47M total employed across the 125 ISCO 3-digit nodes, vs e.g. RO 7.77M / DE 40.55M for context).

### 8.4 Absorption capacity proxy — candidate-baseline

Candidates do not map cleanly to any of the six L5 systems (Nordic flexicurity, Germanic Dual, Continental Corporatist, Liberal Market, Southern European, CEE). Per spec line 23 + handover: use **weighted average of CEE rate (2–5%/yr) and Southern European rate (2–5%/yr)**, since Western Balkans + Turkey have institutional patterns most similar to those two clusters (low ALMP funding, fragmented activation infrastructure, insider/outsider rigidity, large informal sector, EU pre-accession alignment in BA/MK/RS/TR pulling toward CEE/SE conventions but without the funding floor).

The two source ranges are identical (both 2–5%/yr, midpoint 3.5%/yr), so the weighted average collapses to **3.5%/yr regardless of weights** — a structural feature, not a coincidence. Applying the §2.3 5-year horizon coefficient gives:

```
candidate_baseline_rate     = 3.5%/yr  (weighted avg of CEE 3.5 + SE 3.5)
absorption_idx_candidate    = 0.035 × 5 = 0.175
```

This is numerically identical to the absorption value used for all CEE and Southern European countries already in the dataset (PL, CZ, HU, RO, BG, HR, SI, SK, EE, LV, LT, IT, ES, PT, EL, MT, CY) — by construction, not by accident.

**Defensibility note.** The proxy is conservative-by-anchor (matches the closest peer clusters) but does not capture three real differences that Phase 2 enrichment should address:

1. **TR informal-sector share is materially higher** than any CEE/SE country (TÜİK 2024: ~28% vs CEE peers <15%). High informality compresses formal-sector absorption capacity below the 3.5% midpoint — proxy may overstate TR absorption.
2. **BA/MK/RS ALMP spend as share of GDP is below CEE floor** (Western Balkans Labour Market Trends 2024 reports <0.2% vs CEE 0.3–0.6%). Funding-side reality below proxy.
3. **TR working-age population is still growing** (TR demographic transition ~2035–2040), unlike SE/CEE shrinkage. Lens 2 absent for candidates means this signal is unscored — but it cuts the other way (more young entrants = more transition pressure absorbed by labour-force inflow rather than reskilling, but only if jobs exist for them).

Net direction of unmodelled error: candidate `absorption_idx` of 0.175 is plausibly an upper bound for TR (informality + funding gap), roughly correct for RS, and slightly optimistic for BA/MK (lowest ALMP funding). Phase 2 enrichment with a fourth proxy tier ("pre-accession" = ~2.0–2.5%/yr) should be considered if Western Balkans / Turkey become a substantive analytical thread rather than a coverage line.

### 8.5 Lens 2 — N/A for candidates

`lens2_demographic_load`, `lens2_retirement_offset`, `lens2_overlap_score`, `_lens2_modifier` are all null/empty for the 4 candidate rows. **Combined corridor v1 = Lens 1 corridor** (no Lens 2 modifier possible). The orthogonality finding (§3.4 + headline finding in spec) does not apply to candidates in the same way — there is no demographic projection to evaluate against retirement-offset thresholds. Findings document carries the caveat explicitly.

### 8.6 Confidence flag — `partial-coverage` (new value)

The existing high / medium / low scale tracks **proxy-density within full lens coverage** (0 / 1 / 2+ proxies across L4 + L5). Candidates lack the underlying lenses entirely, so a per-proxy count is not the right axis. New flag value: **`partial-coverage`** — distinct from low. Reads as: "Lens 1 directly scored; Lens 2 not applicable; corridor assignment is provisional pending Phase 2 candidate-cluster scoping."

### 8.7 Sentinel preservation

PL at 2.96 remains the Phase 3 sentinel test case for structural-bias re-calibration (§2.4 calibration note unchanged). Candidate ratios (TR 2.39, BA 2.56, MK 2.65, RS 2.74) sit below the C2/C3 boundary cluster (PL/MT/EE/HR/CY 2.89–2.96) and are not candidate sentinels — TR's lower ratio is exposure-side (lowest `tech_avg` in the dataset, 4.85, even below RO at 4.95), not absorption-side relief.

### 8.8 Reproducibility (Bundle B)

Inputs: `european-ai-exposure-map/site/data.json` treemap (125 ISCO 3-digit leaves with `emp` per country and `technical_score` per occupation). Outputs: 4 appended rows in `layer-6-phase1-scoring.csv` (rows 34–37) and 4 appended entries in `layer-6-phase1-scoring.json → rows`. Existing 32 rows byte-identical to original (verified during write). `meta.scope_count` updated 32 → 36; `meta.updated = 2026-04-29`.
