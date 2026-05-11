# Handover Prompt — Bundle Q: Layer 1 Regulatory Overlay for Lens 1 + Lens 4

Bounded enrichment session. Pulls Layer 1 (AI Exposure) regulatory-overlay data into Layer 6 SOT JSON to quantify the squeeze flag (currently binary) and add EU/UK regulated-score asymmetry to Lens 1 absorption. ~50–60 min.

---

## START PROMPT

I need you to enrich Layer 6's Lens 1 + Lens 4 from Layer 1 (AI Exposure) per the cross-layer audit's Bundle Q recommendation. Layer 1 carries two regulatory-overlay structures that Layer 6 currently doesn't surface: (a) per-country AI Act material-change counts (40-deployer × Art 26(7) × PWD), and (b) EU/UK regulated-score asymmetry that quantifies the squeeze flag. The squeeze flag is currently a binary in Layer 6; Layer 1 has the data to make it quantitative.

This is enrichment, not re-computation. Layer 1's regulatory-overlay structure is accepted as a canonical input.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/cross-layer-enrichment-audit-2026-04-30.md` — **canonical scope.** Read the Layer 1 detail section + Bundle Q entry in recommended bundles.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — SOT JSON. Lens 1 absorption denominator + Lens 4 squeeze-flag binary fields are the modification surface.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — Lens 1 + Lens 4 spec.
- `/Users/philippmaul/Documents/projects/european-ai-exposure-map/scores.json` — Layer 1 primary scoring file (technical exposure + regulated exposure).
- `/Users/philippmaul/Documents/projects/european-ai-exposure-map/uk_scores.json` — UK-specific scores under lighter regulation.
- `/Users/philippmaul/Documents/projects/european-ai-exposure-map/site/data.json` — Layer 1 site data; carries the country-occupation-regulated trifecta.
- `/Users/philippmaul/Documents/projects/european-ai-exposure-map/README.md` — context on technical-vs-regulated scoring + EU AI Act overlay (Annex III / Art 26(7) / PWD).

### Goal — modify SOT JSON Lens 1 + Lens 4 fields only

**Lens 1 enrichment:** add a per-country `lens1_regulated_absorption_pct` field capturing the EU/UK regulated-score asymmetry. For each country, what fraction of its high-exposure occupations are regulated (and therefore have absorption-friction from EU AI Act)? UK as the baseline (lighter regulation); EU-27 + EFTA above the UK baseline by varying margins.

**Lens 4 squeeze-flag quantification:** convert per-country `squeeze_flag` from boolean to structured:

```json
"squeeze_flag": {
  "binary": true,
  "asymmetry_score": <number 0.0–1.0, EU_regulated_score / UK_regulated_score>,
  "ai_act_overlay_count": {
    "annex_iii_high_risk": <int>,
    "art_26_7_deployer_obligations": <int>,
    "pwd_post_market_duties": <int>
  },
  "_provenance": {"source_layer": "L1", "source_data": "scores.json + uk_scores.json", "bundle": "Q"}
}
```

For the 5 currently-flagged squeeze countries (BE, DE, FR, LU, NL): these get full quantification. For non-squeeze countries: `binary: false` + `asymmetry_score: <number>` only (the regulatory-asymmetry score is informative across all countries even when it doesn't trip the binary squeeze threshold).

Add a top-level `cross_cutting_findings.regulatory_asymmetry` entry summarising the EU/UK divergence finding (~60 words).

Add a top-level `metadata.layer_1_enrichment` block recording source paths + ingestion date + Bundle Q version.

### Composition rules

1. **Read-only against Layer 1.** No modifications.
2. **Read-only against Layer 6 except the specified Lens 1 + Lens 4 fields + 2 top-level additions.** Do not modify other lenses, country profiles outside the specified sub-blocks.
3. **BR-19 no fabrication.** Every count (Annex III / Art 26(7) / PWD) traces to a specific L1 file path. If L1 doesn't have a count for a country at the per-country level, render `null` with `data_gap_reason`.
4. **Preserve the existing squeeze-flag set** (BE, DE, FR, LU, NL). Bundle Q quantifies; it does not re-classify.
5. **EU/UK asymmetry score must be calculated** for all 36 countries, not just squeeze-flagged ones. The asymmetry is a Lens-1-wide signal; it informs the regulatory-friction component of absorption capacity beyond just squeeze.
6. Phil does all git commits.

### Verification (before reporting back)

1. SOT JSON loads round-trip cleanly.
2. All 36 country blocks have a non-null `lens1_regulated_absorption_pct` and a non-null `squeeze_flag.asymmetry_score`.
3. The 5 currently-squeeze-flagged countries (BE, DE, FR, LU, NL) have `squeeze_flag.binary: true`; all others have `false`. (Bundle Q does not re-classify.)
4. At least 4 of 5 squeeze countries have non-null `ai_act_overlay_count` sub-fields.
5. `cross_cutting_findings.regulatory_asymmetry` is present with a single-paragraph summary.
6. `metadata.layer_1_enrichment` block records source paths + ingestion date.
7. No other SOT JSON fields modified (diff against pre-enrichment SOT shows only Lens 1 + Lens 4 + the two new top-level entries).

### When done — report back to master session with

1. Per-country `asymmetry_score` summary (range, distribution, top 5 + bottom 5).
2. AI Act overlay counts for the 5 squeeze countries (filled vs gap-flagged).
3. Verification checklist (1–7) — pass/fail per item.
4. Knock-on flag list: which Layer 6 outputs need re-derivation against the enriched Lens 1 + Lens 4 (Executive §2 Lens 4 + One-Pager finding-on-squeeze + Einfache versions + glossary entry for AI-Act-overlay).
5. Composition gaps surfaced.

## END PROMPT
