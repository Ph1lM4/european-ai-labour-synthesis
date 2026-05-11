# Handover Prompt — Bundle P: Layer 4 Demographics Enrichment for Lens 2

Bounded enrichment session. Pulls Layer 4 (demographics) data into Layer 6 SOT JSON to replace the single-string Lens 2 rendering with a per-country / per-zone reading. ~75–90 min.

---

## START PROMPT

I need you to enrich Layer 6's Lens 2 from Layer 4 (demographics) per the cross-layer audit's Bundle P recommendation. The current Lens 2 in the SOT JSON is a single-string field ("refuted at scale") because Layer 6's Phase 1 only computed the headline retirement-offset comparison. Layer 4 carries substantially richer granular data that should replace the single-string with a per-country object surfacing Zone A/B/C/D heterogeneity, working-age decline trajectories, and net-migration arithmetic.

This is enrichment, not re-computation. Layer 4's findings are accepted as canonical inputs; Bundle P lifts them into Layer 6's SOT JSON.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/cross-layer-enrichment-audit-2026-04-30.md` — **canonical scope.** Read the Layer 4 detail section + Bundle P entry in recommended bundles. Every enrichment in this session traces back to a finding flagged in the audit.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — SOT JSON, schema v1.0. Lens 2 currently a single-string field (per-country `lens2_demographic_buffer` = "refuted at scale").
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — Lens 2 spec. Confirms the 80% retirement-offset threshold + the orthogonality finding.
- `/Users/philippmaul/Documents/projects/european-demographics-map/site/demographics-data.json` — Layer 4 site data (primary input).
- `/Users/philippmaul/Documents/projects/european-demographics-map/data/eurostat/` — Eurostat extracts (sample as needed for per-country data).
- `/Users/philippmaul/Documents/projects/european-demographics-map/README.md` — context on the AI Substitution Matrix (Zones A/B/C/D), the 8–12M Zone C unfillable positions, and the working-age trajectory.

### Goal — modify SOT JSON Lens 2 fields only

Replace per-country `lens2_demographic_buffer` single-string with a structured object:

```json
"lens2_demographic_buffer": {
  "buffer_holds": false,
  "retirement_offset_pct": <number, country-specific>,
  "working_age_change_pct_to_2050": <number, country-specific>,
  "zone_heterogeneity": {
    "zone_a_clerical": "<short string — AI substitutes; retirement low; compounding mismatch>",
    "zone_c_healthcare_trades": "<short string — AI doesn't substitute; retirement high; negative buffer / unfillable shortage>",
    "headline": "<one-line per country>"
  },
  "net_migration_dependency": "<short string — required net migration to maintain working-age population, where data available>",
  "_provenance": {
    "source_layer": "L4",
    "source_data": "demographics-data.json + Eurostat EUROPOP2023",
    "ingestion_date": "2026-04-30",
    "bundle": "P"
  }
}
```

Add a top-level `cross_cutting_findings.lens2_zone_heterogeneity` entry summarising the A/C compounding-vs-buffering finding (~80 words) for Bundle N3 / Bundle O to render.

Add a top-level `metadata.layer_4_enrichment` block recording: source data path(s), ingestion date, Bundle P version, and the 3–5 highest-impact L4 findings now reflected in the SOT.

### Composition rules

1. **Read-only against Layer 4.** Do not modify any L4 files. All L4 data flows through SOT JSON modifications only.
2. **Read-only against Layer 6 except the specified Lens 2 fields + 2 top-level additions.** Do not modify other lenses, fragility classes, scenarios, country profiles outside the Lens 2 sub-block.
3. **BR-19 no fabrication.** Every numeric value (retirement offset %, working-age change %, net migration arithmetic) traces to a specific L4 file path + field. Where L4 doesn't have country-level data for a specific country, render `null` with `data_gap_reason`.
4. **Preserve the structural-bias headline** ("buffer thesis fails uniformly at 80% threshold"). The enrichment ADDS the variance below that headline; it does not contradict the uniform-refutation finding.
5. **Net-migration arithmetic must be included** — the audit flagged it as wholly absent from L6 despite being load-bearing. If L4 doesn't have country-level net-migration data, document the gap explicitly with a Phase 5+ enhancement candidate flag.
6. Phil does all git commits.

### Verification (before reporting back)

1. SOT JSON loads round-trip cleanly via `json.load()` → `json.dumps()` → `json.load()`.
2. All 36 country blocks have an updated `lens2_demographic_buffer` object (no countries left with the single-string field).
3. `buffer_holds` is `false` for all 36 countries (the uniform-refutation headline holds).
4. At least 30 of 36 countries have a non-null `retirement_offset_pct` (audit-flagged: L4 has country-level data for most; gaps acceptable for the candidate-partial-coverage four).
5. `cross_cutting_findings.lens2_zone_heterogeneity` is present with a single-paragraph summary.
6. `metadata.layer_4_enrichment` block records source paths + ingestion date + bundle version.
7. No other SOT JSON fields modified (diff against pre-enrichment SOT shows only Lens 2 + the two new top-level entries).
8. Total SOT JSON size remains under 250 KB (was 162.7 KB pre-enrichment; L4 lift adds ~50–80 KB).

### When done — report back to master session with

1. Per-country Lens 2 enrichment summary table (country, retirement_offset_pct, working_age_change_pct, zone-A/zone-C headline).
2. Net-migration arithmetic: included or flagged-as-gap? Per-country count.
3. Verification checklist (1–8) — pass/fail per item.
4. Any L4 findings that surfaced during enrichment but didn't fit Lens 2 (likely Bundle U candidates per the audit).
5. Knock-on flag list: which Layer 6 outputs need re-derivation against the enriched Lens 2 (Executive §2 + §4 + §5 + One-Pager finding 2 + Einfache versions + glossary).
6. Composition gaps surfaced (data fields the audit flagged that L4 turned out not to carry).

## END PROMPT
