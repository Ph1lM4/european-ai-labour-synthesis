# Handover Prompt — Bundle F: Cedefop 2025 Skills Forecast Extraction (2026-04-29)

Self-contained prompt for a fresh session. Closes the Lens 4 Task 2 (a)+(b) gap by extracting per-country sectoral growth data from Cedefop 2025 Skills Forecast country PDFs.

---

## START PROMPT

I need you to extract structured sectoral employment data from Cedefop 2025 Skills Forecast country PDFs and update the existing Phase 2 data matrix to close the Lens 4 Task 2 gap. This is a focused extraction session — does NOT do scoring or analysis beyond the documented derivation method.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — locked spec; do NOT modify
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-data.json` — current matrix; extend in place; do NOT regenerate
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-e-phase2-data-acquisition-handover-2026-04-29.md` — Bundle E Task 2 spec (the gap this session closes)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-e-session2-handover-2026-04-29.md` — Bundle E session 2 outputs reference

### Goal

For each of 29 countries (EU-27 + Iceland + Norway), extract from the Cedefop 2025 Skills Forecast country PDF and populate two `lens4_climate_shocks` sub-fields:

- **(a) green-jobs-2035** — projected employment in green-relevant sectors by 2035 (delta vs 2022 baseline)
- **(b) carbon-displacement-2035** — projected employment displacement in carbon-relevant sectors by 2035 (delta vs 2022 baseline)

These are 2035-horizon (vs the existing 2030-horizon NZAV-proxy data already populated by Bundle E session 1). The 2035 data REPLACES the existing 2030-horizon proxy at H-confidence; methodology notes track the derivation.

### Country list and PDF source

URL pattern (verified): `https://www.cedefop.europa.eu/files/skills_forecast_-_{country_lowercase}_2025.pdf`

**Already in `/Users/philippmaul/Downloads/`** (do NOT re-fetch):
- austria, belgium, bulgaria, cyprus, czechia (5 forecasts)
- Croatia: `/Users/philippmaul/Downloads/8163_en.pdf` is the Croatia 2026 SPOTLIGHT (different document — 4-page summary). Use it as supplementary; ALSO fetch the 2025 Forecast at `https://www.cedefop.europa.eu/files/skills_forecast_-_croatia_2025.pdf` for consistency with other countries.

**To fetch via WebFetch** (24 PDFs):

```
denmark, estonia, finland, france, germany, greece, hungary, ireland,
italy, latvia, lithuania, luxembourg, malta, netherlands, poland,
portugal, romania, slovakia, slovenia, spain, sweden, iceland, norway, croatia
```

**Slug edge cases to watch:**
- Greece: `greece` (NOT `el` or `hellas`)
- Czechia: `czechia` (already confirmed; NOT `czech_republic`)
- If any URL 404s, log the country to `data_gaps` array with `reason: "Cedefop URL pattern miss; manual fetch required"`

For each PDF: 12–14 pages, 2.1–2.5MB. Read with pages parameter (max 14 per request). Read full document since data is distributed across §1 (Employment outlook), §3 (Sectoral employment trends), §4 (Job openings by occupational group).

### Extraction methodology — green/carbon sector mapping

The Cedefop reports use 6 broad sectors. Map to green/carbon as follows (lock this mapping and document it explicitly in methodology notes):

**Green-relevant sectors (positive employment from green transition):**
- Primary sector & utilities — sub-sector "electricity, gas, steam & air conditioning supply" (positive — renewables expansion)
- Business & other services — sub-sectors "research & development", "architectural & engineering services" (positive — green skills)
- Construction — sub-sector growth driven by renovation/insulation/renewable installation (positive)
- Manufacturing — sub-sector "electrical equipment" where forecast positive (e.g. heat pumps, batteries, electrolysers)

**Carbon-relevant sectors (negative employment from green transition):**
- Primary sector & utilities — sub-sector "agriculture, forestry & fishing" (often forecast strong decline)
- Primary sector & utilities — sub-sector "mining & quarrying" (fossil fuel extraction)
- Manufacturing — sub-sectors "basic metals", "rubber & non-metallic mineral products", "wood, paper, printing", "food, drink & tobacco" where forecast decline (carbon-intensive subsectors)
- Distribution & transport — sub-sector "transport" where forecast decline (combustion-vehicle-dependent)

**Neutral / excluded:**
- Non-marketed services (health, education, public admin) — not climate-mode-determined
- Distribution & transport wholesale & retail — not climate-mode-determined
- Construction non-renovation — not climate-mode-determined

### Per-country extraction per PDF — required outputs

For each country, populate this structure under `country_data.{ISO}.lens4_climate_shocks`:

```json
"lens4_climate_shocks": {
  "value_a_green_jobs_2035": {
    "value": <number, in thousands of jobs delta 2022→2035>,
    "unit": "thousand jobs (delta)",
    "derivation_method": "Cedefop 2025 Skills Forecast country report. Sum of growth rates × 2022 employment shares for green-relevant sub-sectors per documented green/carbon mapping. Sub-sectors counted: [list with % shares + growth rates from PDF]",
    "uncertainty_band": "±20% (sub-sector growth rates from broad-sector trajectories; share weights from §3 narrative + figures)",
    "source": "https://www.cedefop.europa.eu/files/skills_forecast_-_{slug}_2025.pdf §3 Sectoral employment trends + §6 Demand for and supply of skills",
    "source_year": 2025,
    "confidence": "H"
  },
  "value_b_carbon_displacement_2035": {
    "value": <number, in thousands of jobs delta 2022→2035>,
    "unit": "thousand jobs (delta, negative)",
    "derivation_method": "Cedefop 2025 Skills Forecast country report. Sum of decline rates × 2022 employment shares for carbon-relevant sub-sectors per documented green/carbon mapping. Sub-sectors counted: [list with % shares + decline rates from PDF]",
    "uncertainty_band": "±20%",
    "source": "https://www.cedefop.europa.eu/files/skills_forecast_-_{slug}_2025.pdf §3 Sectoral employment trends",
    "source_year": 2025,
    "confidence": "H"
  },
  "value_c_regional_energy_cost_asymmetry": <retain existing NZAV proxy from Bundle E session 1>
}
```

**Update `confidence` from `M` to `H` for the 27 EU MS + IS + NO once both (a) and (b) are populated.** For the 4 candidates (BA/MK/RS/TR) and Switzerland and UK and Liechtenstein, leave as `null` with `data_gap_reason: "Cedefop 2025 country reports cover EU-27 + Iceland + Norway only"`.

### Constraints

- Per BR-21: every cell ships with `derivation_method` + `uncertainty_band` + `source` + `confidence`. NO clean numbers.
- Per BR-19: extract verbatim where the PDF gives explicit percentages; flag with `[derived from broad-sector + sub-sector commentary; no explicit point estimate in source]` where derivation involves sub-sector inference.
- Where the PDF narrative is ambiguous about a sub-sector's direction, flag with confidence M not H, and document the ambiguity in `derivation_method`.
- Phil does all git commits (synthesis project not a git repo per session 1 — no git operations needed).
- Maximum 14 pages per Read tool call (PDFs are 12–14 pages — read full).
- Update `layer-6-phase2-data.json` `metadata.session_status` field with this session's progress + cell coverage delta.

### Verification

Before declaring complete:
1. **Sanity-check Germany** — the existing 2030-horizon NZAV proxy showed DE green-jobs −22,976 (CONTRACTION while peers expand). The 2035-horizon Cedefop figure should either confirm or refute this. If confirmed: DE compounder finding strengthens. If refuted: methodology document the discrepancy + possibly retain 2030-horizon NZAV reading as the load-bearing metric (since 2030 is closer to current decision horizon).
2. **Sanity-check Spain** — existing data showed ES green-jobs +49k. Verify against Cedefop 2035 figure.
3. **Cross-country consistency** — derivation method applied identically across all 29 countries; no country gets a different mapping rule.
4. **Top-3 vs bottom-3** — report which 3 countries have the largest positive green-jobs delta and which 3 have the largest carbon-displacement.
5. **Coverage check** — 29 countries with full (a)+(b) at H-confidence; remaining 7 (CH, UK, LI, BA, MK, RS, TR) flagged null with documented gap reason.

### When done

Report back with:
- 29/29 countries populated at H-confidence (or flag which 404'd / had data ambiguity)
- DE compounder reading after 2035-horizon swap: confirmed / refuted / ambiguous
- Top-3 green-jobs creators + top-3 carbon-jobs displacers
- Updated cell coverage delta (89.9% → expected ~95%)
- Whether Bundle D Phase 2 scoring can now proceed at strengthened confidence

## END PROMPT
