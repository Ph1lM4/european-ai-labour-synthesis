# Handover Prompt — Bundle R: Layer 5 Reskilling Math + Country A→C Transition Rates

Bounded enrichment session. Pulls Layer 5 (Reskilling) data into Layer 6 SOT JSON to refine Lens 1 absorption with country-level A→C transition rates, anchor Class III §3 with the 7.55M / 450K backlog math, and surface the BR-22-validated diagnostic metric (internal transition speed vs external turnover). ~50–60 min.

---

## START PROMPT

I need you to enrich Layer 6's Lens 1 absorption + Class III narrative + Lens 5 from Layer 5 (Reskilling) per the cross-layer audit's Bundle R recommendation. Layer 5 carries three load-bearing findings that Layer 6 currently underuses or misses entirely:

1. **Per-country A→C transition rates** (Layer 5 system models) — refines Lens 1 absorption denominator beyond the current institutional-system-tag proxy.
2. **The 7.55M deep-reskilling need / 450K annual throughput / 15-year backlog** — anchors the Class III "reskilling pathway is structurally insufficient" claim from assertion to evidence.
3. **The internal-transition-speed-vs-external-turnover diagnostic metric** (BR-22 external-human-variant validation, 2026-04-15 Stefanie Haslauer thread) — load-bearing for squeeze-flag interpretation; currently absent from Layer 6.

This is enrichment, not re-computation. Layer 5's findings are accepted as canonical inputs.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/cross-layer-enrichment-audit-2026-04-30.md` — **canonical scope.** Read the Layer 5 detail section + Bundle R entry in recommended bundles.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — SOT JSON. Lens 1 absorption fields, Class III sub-cluster narrative, Lens 5 system-model are the modification surface.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — Lens 1 + Lens 5 spec; Class III definition.
- `/Users/philippmaul/Documents/projects/european-reskilling-map/site/reskilling-data.json` — Layer 5 primary site data.
- `/Users/philippmaul/Documents/projects/european-reskilling-map/README.md` — context on the 7.55M/450K/15-year math + Nordic flexicurity 8–12% / Germanic Dual 3–6% / Southern 2–5% transition rates.
- `/Users/philippmaul/Documents/projects/european-reskilling-map/site/lenses.html` — six practitioner-and-research views (Haslauer, Klinger, etc.) — sample for the internal-transition-vs-external-turnover diagnostic.

### Goal — modify SOT JSON Lens 1, §3-equivalent metadata, Lens 5 fields only

**Lens 1 absorption refinement:** add per-country `lens1_a_to_c_transition_rate_pct` capturing the L5 transition rate for the country's institutional-system. Use the Nordic / Continental / Germanic / Southern / CEE bands (8–12% / 5–8% / 3–6% / 2–5% / 1–4% per L5) keyed off the country's `_system_p1` tag. For DE/AT/CH specifically, use the L5 DACH-page granular numbers if available.

**Class III §3 anchor:** add a top-level `cross_cutting_findings.reskilling_capacity_gap` entry with the load-bearing 7.55M / 450K / 15-year math:

```json
"reskilling_capacity_gap": {
  "deep_reskilling_need_eu27_uk_m": 7.55,
  "annual_throughput_m": 0.45,
  "implied_backlog_years": 15,
  "speed_gap_years": "5-9",
  "context": "<short string explaining what this means for Class III countries>",
  "_provenance": {"source_layer": "L5", "source_data": "reskilling-data.json", "bundle": "R"}
}
```

This is the empirical anchor for the Class III "reskilling pathway is structurally insufficient" framing in §4 of the executive doc.

**Lens 5 internal-transition diagnostic:** add per-country `lens5_internal_transition_diagnostic` field where L5 has the data. The BR-22-validated finding is: a country whose internal-transition speed (workers moving zone-to-zone within firms) is materially slower than its external-turnover rate is at higher squeeze risk. Where L5 carries this, lift it; where it doesn't, render `null` + flag for Phase 5+.

Add top-level `metadata.layer_5_enrichment` block recording source paths + ingestion date + Bundle R version.

### Composition rules

1. **Read-only against Layer 5.** No modifications.
2. **Read-only against Layer 6 except specified Lens 1, top-level cross_cutting_findings, Lens 5 sub-fields.** Do not modify country profiles outside the specified fields, do not modify scenarios or fragility-class definitions.
3. **BR-19 no fabrication.** Every transition-rate value traces to L5 system-model bands. The 7.55M / 450K / 15-year numbers traceto reskilling-data.json + Derivation Appendix; quote the appendix reference.
4. **Per-country granularity for DACH** must match L5's DACH-specific numbers (DE 5, AT 3, CH 1 on the reform-velocity composite). For the rest, the system-model bands are acceptable as proxies — flag where L5 has finer data that wasn't lifted.
5. **The internal-transition-vs-external-turnover diagnostic** must be populated where L5 carries the data. If only DACH or a subset has it, populate that subset and flag the gap for the rest.
6. Phil does all git commits.

### Verification (before reporting back)

1. SOT JSON loads round-trip cleanly.
2. All 36 country blocks have a non-null `lens1_a_to_c_transition_rate_pct`.
3. DE / AT / CH have country-specific (not band-proxy) values.
4. `cross_cutting_findings.reskilling_capacity_gap` is present with the 7.55M / 450K / 15-year math.
5. `lens5_internal_transition_diagnostic` populated for at least DACH; gap-flagged for others.
6. `metadata.layer_5_enrichment` block records source paths + ingestion date.
7. No other SOT JSON fields modified (diff against pre-enrichment SOT shows only Lens 1 + Lens 5 + top-level cross-cutting + metadata).

### When done — report back to master session with

1. Per-country transition-rate summary (range, distribution by institutional system).
2. Reskilling capacity gap math: confirmed numbers + the per-country implication for Class III countries.
3. Internal-transition diagnostic coverage (which countries populated, which gap-flagged).
4. Verification checklist (1–7) — pass/fail per item.
5. Knock-on flag list: which Layer 6 outputs need re-derivation (Executive §2 Lens 1 + §3 Class III anchor + §4 + One-Pager + Einfache + glossary).
6. Composition gaps surfaced.

## END PROMPT
