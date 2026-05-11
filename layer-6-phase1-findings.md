# Layer 6 Phase 1 — First-Pass Findings

_Generated 2026-04-29. Lens 1 + Lens 2 only. Lens 4 + Lens 5 = Phase 2. Fragility classes = Phase 3._

---

## TL;DR

1. **Structural orthogonality holds — strongly.** Demographic shortage and AI displacement do **not** overlap at country level in this dataset. Maximum retirement offset (% of high-exposure roles absorbed by retirement by 2035) is ~26 %; the spec threshold for "buffer holds" is 80 %. **No country in the 32-country EU+EEA+CH+UK scope comes within 50 percentage points of the threshold.** Per spec line 113–114, this is "arguably the single most important finding in the entire project." First-pass result: refuted, decisively. _Caveat: the 4 candidate countries (BA, MK, RS, TR) carry no L4 demographic data; orthogonality is restated for the 32, not re-tested for the 36._
2. **Lens 2 produces zero corridor shifts.** Combined corridor v1 = Lens 1 corridor for all 32 countries with full lens coverage. Candidate countries (BA, MK, RS, TR) have `combined_corridor_v1` = `lens1_corridor` by construction (no Lens 2 modifier possible). Demographic overlay is structurally suppressed.
3. **Lens 1 distribution is bimodal-with-large-middle, not triadic.** Across 36 countries: 5 Corridor 1 (Nordics), 2 Corridor 3 (Liberal Market: UK, IE), **29 Corridor 2** (25 from the original 32 + 4 candidates BA/MK/RS/TR). C2 contains four sub-clusters separated by L5 system, ranging 1.59 (FR) → 2.96 (PL); candidates land 2.39 (TR) – 2.74 (RS).
4. **Most corridor differentiation is absorption-side, not exposure-side.** Country `tech_avg` exposure ranges 4.85 (TR — new minimum, below RO 4.95) – 6.46 (LU, ~33 % relative span); absorption rates range 0.16–0.50 (~3× relative span). Phase 2 with Klinger coordination-share weighting will likely amplify exposure-side variance.
5. **Confidence is concentrated.** Only 6 countries are high-confidence (DE, AT, CH, FR, IT, ES — all DACH+Latin). 24 low-confidence countries depend on tier-based proxies for L4 and L5. **4 countries (BA, MK, RS, TR) carry the new `partial-coverage` flag** — Lens 1 directly scored, Lens 2 not applicable.

---

## 1. Distribution under Lens 1 alone

| Corridor | n | Countries | Ratio range |
|---|---|---|---|
| 1 — Managed Transition | 5 | DK, FI, IS, NO, SE | 1.00 – 1.10 |
| 2 — Bifurcated Absorption | 29 | AT, BE, BG, CY, CZ, DE, EE, EL, ES, FR, HR, HU, IT, LI, LT, LU, LV, MT, NL, PL, PT, RO, SI, SK, CH; **+ candidates BA, MK, RS, TR** | 1.59 – 2.96 (full-coverage) / 2.39 – 2.74 (candidates) |
| 3 — Displacement Without Absorption | 2 | IE, UK | 3.33 – 3.40 |

### Sub-clusters within C2

| Sub-cluster (L5 system) | Ratio range | Countries |
|---|---|---|
| Continental Corporatist (near C1 boundary) | 1.59 – 1.91 | FR, BE, NL, LU |
| Germanic Dual (mid-C2) | 2.31 – 2.43 | AT, DE, CH, LI |
| Romania (low-exposure outlier) | 2.46 | RO |
| Southern European (near C3 boundary) | 2.75 – 2.91 | ES, IT, EL, PT, MT, CY |
| Central/Eastern European (near C3 boundary) | 2.77 – 2.96 | LV, BG, HU, CZ, SI, SK, LT, HR, EE, PL |

**Observation:** the Continental Corporatist countries sit just above the C1 cutoff. Under any modest re-calibration (e.g. extending the absorption window from 5 to 6 years), FR/BE/NL/LU would migrate to C1. This is a real cluster-on-the-boundary, not noise.

**Calibration-adjusted reading.** Per spec lines 355–362, Corridor 1 is narrower than historical base rates suggest; Corridor 3 broader. Under structural-bias adjustment, the **10 countries with ratio ≥ 2.80** (PL 2.96, MT 2.91, HR 2.89, CY 2.89, EE 2.90, LT 2.87, IT 2.84, EL 2.83, HU 2.82, CZ 2.81, SI 2.82, SK 2.89) are plausibly already in Corridor 3 territory. Phase 3 validation should re-test thresholds.

## 2. Demographic buffer thesis: structurally refuted

Per L5 `reskilling_gap.by_country` direct data (7 countries), retirement_2035 covers a uniform **20–25 %** of high-exposure roles. EU27 aggregate: 22.4 %. Spec threshold for "buffer holds": **≥ 80 %**. Spec threshold for "buffer fails": **< 50 %**.

| Country | Retirement offset (direct) | Buffer status |
|---|---|---|
| DE | 24.6 % | fails |
| AT | 21.6 % | fails |
| CH | 23.4 % | fails |
| FR | 21.0 % | fails |
| IT | 25.3 % | fails |
| ES | 23.3 % | fails |
| UK | 21.4 % | fails |
| EU27 aggregate | 22.4 % | fails |
| Tier-proxied (sharpest_decline) | 26.4 % | fails |
| Tier-proxied (relative_resilience) | 20.4 % | fails |

**32 / 32 countries fall in `buffer_fails`.** No country meets `buffer_holds`. The default narrative — "demographic decline softens AI's blow" — does not hold for any country in the EU-27 + EFTA + UK scope under this dataset.

### Why orthogonality holds

Two structural reasons, both visible in L5 transitions data:

1. **High-exposure roles** (admin, clerical, customer service, business support) are concentrated in working-age cohorts that are **not retiring at sufficient scale**. Boomer retirement absorbs ~20–25 % of high-exposure stock by 2035; the remaining 75–80 % is Gen X + Millennials, who must transition or be displaced.
2. **Demographic shortage roles** (Zone C: care, healthcare, trades, infrastructure) require skills_distance 5–8 / 10 from displaced cohorts, mandatory certifications 3–36 months, and wage cuts 12–33 %. The transition is not free, not automatic, and not desired by displaced workers under current wage structures (per L5 wage-cliff documentation).

This supports the spec's structural-bias finding (lines 355–362, 440): the "managed transition" corridor is narrower than historical calibration suggests precisely because reinstatement and demographic-buffer mechanisms are weaker than prior-disruption analogues imply.

## 3. Sanity checks

### 3.1 Hand-checked countries (DE, FR, IT, ES, PL)

| ISO | tech_avg | System | Rate mid (%/yr) | Ratio | Lens 1 corridor | Combined v1 | Confidence | Sanity |
|---|---|---|---|---|---|---|---|---|
| DE | 5.83 | Germanic Dual | 4.5 | 2.41 | 2 | 2 | high | ✅ Bifurcated absorption — Beruf system slow-but-deep; corridor matches Klinger middle-management-compression hypothesis |
| FR | 5.64 | Continental Corporatist | 6.5 | 1.59 | 2 | 2 | high | ✅ Just above C1 — CPF + sectoral funds give moderate absorption; C2 with C1-boundary annotation defensible |
| IT | 5.48 | Southern European | 3.5 | 2.84 | 2 | 2 | high | ✅ Near C3 — fragmented ALMP, insider/outsider rigidity, demographic crash; "structural-bias-adjusted" reading puts IT in C3 |
| ES | 5.36 | Southern European | 3.5 | 2.75 | 2 | 2 | high | ✅ Spain's 46% adult learning is best-in-South but ALMP fragmentation persists; C2 with C3-boundary annotation |
| PL | 5.64 | Central/Eastern European | 3.5 | 2.96 | 2 | 2 | low | ⚠️ At the edge of C3. EU cohesion funding plus demographic drain via emigration. Structural-bias-adjusted reading places PL in C3. Confidence "low" because L4 + L5 are both tier-proxied. |

All five "feel right" — methodology is producing intuitively-correct ordinal rankings.

### 3.2 Nordic cluster (DK, FI, IS, NO, SE)

| ISO | Ratio | Lens 1 corridor |
|---|---|---|
| FI | 1.00 | 1 |
| IS | 1.02 | 1 |
| DK | 1.05 | 1 |
| NO | 1.06 | 1 |
| SE | 1.10 | 1 |

✅ All Nordic countries cluster Corridor 1 — high confidence on ordinal placement (low confidence on absolute ratio for IS, NO, SE due to L4 / L5 data sparsity). Spec sanity check passes.

### 3.3 Scope verification

- **36 country rows in CSV ✅** (32 original + 4 candidates appended via Bundle B re-score 2026-04-29)
- Ukraine NOT in output ✅ (Phase 2 reference case only per spec)
- LI included with proxy flag ✅
- Western Balkans accession candidates (BA, MK, RS) and TR **included with `partial-coverage` flag** ✅ — Lens 1 only

**Spec discrepancy resolved:** spec line 18 was correct at 36; original Phase 1 inadvertently dropped the 4 candidates. Bundle B (this update) reconciles. See methodology notes §8.

## 4. Open questions for Phase 2

### 4.1 Material methodology decisions

1. **Liberal Market transition rate.** User spec says 2.8–3.6 %/yr; L5 raw says 5–8 %/yr. Difference is material — under L5 raw, UK and IE shift from C3 (ratio 3.40 / 3.33) to C2 (ratio ~1.7) — corridor changes for the only Phase 1 C3 countries. Phil to adjudicate: lower rate is consistent with UK ALMP-spend-as-share-of-GDP (0.03 % vs Continental 0.9 %) and supports "Liberal Market = sink-or-swim, low absorption infrastructure." Higher rate captures UK's faster bootcamp/short-course agility. Likely answer: keep 2.8–3.6 % but flag UK + IE as Class II "Fragile" in Phase 3 (corridor flips between scenarios).
2. **Estonia.** Currently CEE (rate 3.5 %/yr) → ratio 2.90 → C2-near-boundary. EE digital-state + e-Residency suggest Nordic-pattern absorption infrastructure (rate would be 10 %/yr → ratio 1.04 → C1). Funding-side reality is CEE. Genuine ambiguity — flag for Phase 2 dual scoring.
3. **Romania (RO) outlier.** RO has the lowest country `tech_avg` in the entire dataset (4.95) — significantly below the 5.36–5.91 cluster of all other CEE+Southern countries. Implication: ratio 2.46 places RO closer to Germanic Dual than to its CEE peers. Suspect data quality (RO ISCO employment distribution may underweight high-exposure occupations) — verify in Phase 2 with Eurostat 2024 LFS cross-check.
4. **C2 bifurcation gate not applied.** Spec defines C2 as "ratio 1.5–3 AND middle-skill share > 60%." Phase 1 used only the ratio gate. Strict gate application requires per-country labour-force-by-skill-tier data — Phase 2.
5. **Climate net position (Phase 2 input)** — already pre-mapped in spec line 229–235. Will move 6 Mediterranean countries (ES, PT, IT, EL, MT, CY) toward worse outcomes and 7 northern countries (DK, NO, FI, SE, CH, NL, EE) toward partial offset. Will be folded into Lens 5 scoring.

### 4.2 Data gaps blocking Phase 2

- **Country-level retirement_2035 / high_exposure** for 25 countries (currently EU27 baseline + tier modifier).
- **Country-level working_age 2025 / 2030 / 2040 / 2050** for 24 countries (currently tier proxy or hand-assigned).
- **Klinger coordination-share** per ISCO 3-digit (need Klinger's coordination/decision/execution decomposition, not just headline exposure).
- **Occupation × age × country** matrix for true overlap scoring (currently using system-level base + uniform per-country logic).
- **L3 task → employment lag retrofit** (containers, ATMs, CAD, DTP) for Lens 1 lag specification — feeds Phase 2.

### 4.3 Findings to test in Phase 2

- **Aggregate-distributional split (spec line 438+).** Current Phase 1 corridor labels collapse aggregate and distributional. Under Lens 4 (compounding shocks) and Lens 5 (polycrisis drag), aggregate-OK / distributional-bad combinations should appear — predictably for DE (regional-economy capital-outflow risk per Lens 4 jurisdictional-buffering finding), for ES/IT (Mediterranean physical climate vulnerability), for PL (Eastern European concurrent-crisis exposure).
- **Jurisdictional-buffering squeeze (spec line 169–187).** DE + FR + Nordics — strong AI worker protection + adjacent UK/US asymmetry + high-value export dependence. Lens 4 should reclassify some of these from current Lens 1+2 corridor to a new "buffering-squeeze" pattern.
- **Class IV anchor** (Ukraine) — out of corridor scope but feeds Lens 5 reference case for Phase 2 + fragility class assignment Phase 3.

---

## 5. Methodology decisions Phil should review before Phase 2 starts

1. Spec country count (36 vs 32) reconciliation.
2. Liberal Market transition rate (2.8–3.6 % vs L5 raw 5–8 %).
3. Estonia classification (CEE vs Nordic-light dual scoring).
4. C2 bifurcation gate — apply strictly in Phase 2, or treat as Phase 3 corridor-validation criterion?
5. Threshold re-calibration timing — apply structural-bias adjustment during Phase 2 or hold until Phase 3 validation step?
6. Liechtenstein — keep with proxy flag or drop?

---

## 6. Phase 1 closes with

- 4 output files written (CSV, JSON, methodology, this findings doc).
- 5/5 hand-checked countries pass intuitive-ranking sanity check.
- Nordic cluster verified Corridor 1.
- Ukraine correctly excluded.
- Spec-scope discrepancy (36 vs 32) flagged.
- Buffer-thesis hypothesis result: **refuted** — strongest single finding of Phase 1, surfaced for Phase 2 / synthesis foregrounding.

---

**Next action requested of Phil:** review section 5 above; adjudicate the 5 outstanding methodology decisions (item 1, country count, was resolved by Bundle B 2026-04-29) before Phase 2 begins. Phase 2 (Lens 4 + Lens 5 scoring) blocks on items 2 and 5 specifically.

---

## 7. Candidate Country Findings (added 2026-04-29, Bundle B re-score)

### 7.1 Lens 1 readings

| ISO | Country | tech_avg | exposure_idx | absorption_idx | ratio | Lens 1 corridor | combined v1 | confidence | total emp (L1) |
|---|---|---|---|---|---|---|---|---|---|
| TR | Turkey                  | 4.85 | 0.4190 | 0.175 | 2.394 | 2 | 2 | partial-coverage | 31,470,300 |
| BA | Bosnia and Herzegovina  | 5.08 | 0.4477 | 0.175 | 2.558 | 2 | 2 | partial-coverage |  1,215,400 |
| MK | North Macedonia         | 5.21 | 0.4634 | 0.175 | 2.648 | 2 | 2 | partial-coverage |    684,600 |
| RS | Serbia                  | 5.34 | 0.4802 | 0.175 | 2.744 | 2 | 2 | partial-coverage |  2,747,200 |

**All 4 candidates land in Corridor 2 (Bifurcated Absorption).** Ratios cluster 2.39–2.74 — squarely within C2, well below the C2/C3 boundary cluster of PL/MT/EE/HR/CY at 2.89–2.96. Candidates do not become Phase 3 sentinels under the existing thresholds.

### 7.2 TR exposure-side observation

**Turkey is the new minimum-exposure country in the dataset** (`tech_avg` 4.85), edging below the prior minimum RO 4.95. Implication: TR's relatively low ratio (2.39) is exposure-side, not absorption-side. The country has a less-AI-exposed occupational mix than even Romania — driven by larger agricultural and physical-trades shares in the L1 ISCO-3 employment distribution. This is intuitive for an Eastern-Mediterranean / Anatolian labour-market profile and provides directional sanity for the candidate-baseline absorption proxy: if absorption were over-stated in the proxy, TR would still land in C2 simply because its exposure is structurally lower.

### 7.3 Defensibility of corridor assignments

**TR — defensible at C2.** Eastern-Mediterranean labour-market characteristics (large informal sector ~28%, fragmented ALMP, insider/outsider rigidity in the formal sector, growing working-age population through ~2035–2040) match the Bifurcated Absorption mechanism: the formal-sector half of the labour market behaves like Southern European institutional patterns (slow but partial absorption via informal-sector relief valve and demographic inflow), while displaced workers in the informal-formal interface fall through. C2 is the right corridor; the open question is whether TR should be flagged for distributional-fragility scoring in Phase 3.

**BA, MK, RS — defensible at C2 with proxy-uncertainty caveat.** All three sit in the high-C2 band (2.56–2.74), one structural-bias re-calibration step away from C3. Western Balkans ALMP funding is below the CEE floor (Western Balkans Labour Market Trends 2024: <0.2% of GDP vs CEE 0.3–0.6%), suggesting absorption is over-stated by the candidate-baseline proxy. Under a hypothetical 4th-tier proxy ("pre-accession" 2.0–2.5%/yr → absorption_idx 0.10–0.125), all three would shift to C3. Phase 2 should consider this tier if Western Balkans become an analytical thread rather than a coverage line.

### 7.4 Orthogonality finding does NOT extend to candidates

The buffer-thesis-refuted finding rests on retirement-offset evidence that does not exist for BA/MK/RS/TR (no L4 demographic projections, no L5 reskilling-system country classification). The 32-country result stands; **the 36-country statement is "32 with full lens coverage refute the buffer thesis; 4 candidates carry no demographic data, finding not re-tested for them."** Document this caveat in the synthesis writeup — do not implicitly extend the orthogonality claim to candidates.

### 7.5 Data gaps surfaced

1. **L4 demographic projections** for BA/MK/RS/TR — Eurostat projections cover EU-27; UNDESA WPP 2024 has Western Balkans + Turkey but on different age-cohort definitions. Phase 2 enrichment if candidates become substantive.
2. **L5 system classification** for Western Balkans + Turkey — none of the six existing systems fits cleanly. Pre-accession EU candidates pull toward CEE conventions in formal-sector institutions but lack the funding floor; TR has its own Eastern-Mediterranean profile distinct from SE.
3. **Informal-sector data** — TÜİK / Western Balkans labour-force surveys report informality but do not align to the ISCO 3-digit employment structure used in L1. Phase 2 needs informality-by-occupation overlays to refine candidate absorption.
4. **ALMP spend as share of GDP** — confirmed below CEE floor for BA/MK/RS via Western Balkans Labour Market Trends 2024; needs verification for TR (likely also low but data sparser). Material to whether candidate-baseline 3.5%/yr proxy holds.

### 7.6 Phase 2 / Phase 3 implications

- **Phase 2 candidate cluster scoping** — decide whether to deepen (add 4th proxy tier, ingest UNDESA / Cedefop candidate-country data, score Lens 4 partial) or hold at L1-only. Recommend deepening only if synthesis narrative requires candidate corridor confidence comparable to EU-27.
- **Phase 3 fragility classes** — candidates cannot be assigned Class I (corridor stable across scenarios) without scenario-stack scoring. Default treatment: candidates carry "fragility class N/A — insufficient lens coverage" until Phase 2 closes the gap or the candidates are de-scoped from corridor-mapping into reference-case-only narrative (parallel to Ukraine).
- **Sentinel preservation** — PL at 2.96 remains the single Phase 3 sentinel for structural-bias re-calibration; candidates do not displace it.
