# Handover Prompt — Bundle G: MSC Narrative Closure (13 Below-Threshold Countries) + Phase 2 Metadata Follow-up (2026-04-29)

Self-contained prompt for a fresh session. Closes the `lens4_geopolitical_narrative` gap for the 13 countries that fell below the keyword-score threshold during Bundle E session 2's MSC ingestion, and refreshes the now-stale `top_3_remaining_gaps_for_bundle_d` field. Last task before Bundle D Phase-2 scoring.

---

## START PROMPT

I need you to (1) close the `lens4_geopolitical_narrative` gap for 13 below-threshold countries by re-processing the Munich Security Report PDFs that are already on disk, and (2) refresh stale entries in the Phase 2 data file's `metadata.session_status.top_3_remaining_gaps_for_bundle_d` array. Both tasks update the same file in place. No fetching needed — all source PDFs are local.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — locked spec; do NOT modify
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-phase2-data.json` — current matrix; extend in place; do NOT regenerate
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-e-session2-handover-2026-04-29.md` — original Task 3 narrative spec for output structure reference
- The 23 already-populated `lens4_geopolitical_narrative` cells in the JSON — read 3–4 (e.g. DE, FR, IT, PL) to understand the verbatim-citation style + provenance fields used; **match that style exactly**.

### Country scope — 13 below-threshold countries

Each currently has `lens4_geopolitical_narrative.value` starting with "Country narrative — direct MSC text not retrieved (country mentioned 0-1 times in MSC 2024-2026 reports; below threshold)" at L-confidence:

```
BE, CY, EL, ES, IE, LT, LU, LV, MT, SK, LI, BA, MK
```

These are the 4 EFTA/non-EU edges (LI, BA, MK + EL is EU but Greek-letter ISO) plus 9 EU member states that the prior keyword-score pass scored too low.

### Source PDFs (all on disk in `/Users/philippmaul/Downloads/`)

Full reports (use these as primary):
- `Under_Destruction–Munich_Security_Report_2026.pdf` — MSR 2026 full
- `Multipolarization_–_Munich_Security_Report_2025.pdf` — MSR 2025 full
- `MSR2024_MSI_mitCover_final_240507_DIGITAL.pdf` — MSR 2024 full

Executive summaries (cross-reference, NOT primary unless full text doesn't mention country):
- `MSR_2026_ExecutiveSummary_en.pdf`
- `MSR_2025_ExecutiveSummary_de_01.pdf` (German — only if EN summary unavailable)
- `MSR_2024_ExecutiveSummary_en_final.pdf`

Errata (apply if cited passage falls in errata-touched range):
- `MunichSecurityReport2024_Errata.pdf`
- `Munich_Security_Report_2026_Errata.pdf`

Use `pdftotext -layout` for extraction (matches the workflow Bundle E session 2 used).

### Methodology — relaxed threshold

Bundle E session 2 used keyword-score thresholding that excluded these 13. Lower the bar for THIS pass:

1. **Country-name presence is sufficient** — if the country is mentioned by name (or canonical adjective: "Greek", "Spanish", "Belgian", "Latvian", "Lithuanian", "Maltese", "Cypriot", "Slovak", "Irish", "Luxembourgish", "Liechtenstein", "Bosnian", "Macedonian"/"North Macedonian"), capture the surrounding sentence(s) verbatim. Do not require additional strategic-keyword co-occurrence.
2. **Capture up to 2 verbatim sentences** per country, ideally one from the most recent report that mentions it (MSR 2026 > 2025 > 2024). If a country appears in multiple reports, prefer the most security-policy-relevant passage and cite the report-year.
3. **Citation format must match existing cells.** Look at DE / FR / IT cells for the canonical format. Each value string should embed report-year + verbatim quote, e.g. `MSC 2026: "<quote>" | MSC 2025: "<quote>"`.
4. **If a country is genuinely 0-mention across all 3 reports**, ship a structural-absence note instead of a quote: `"<ISO>: Not named in MSC 2024, 2025, or 2026 reports. Structurally absent from MSC framing — interpret as low Atlanticist-frame salience, not data gap."` Set confidence to `M` (the structural absence is itself an informative finding).
5. **Do NOT paraphrase or summarise.** Verbatim only — same BR-19 discipline that produced the 23 H/M-confidence cells.

### Output schema (per cell)

Update `country_data.{ISO}.lens4_geopolitical_narrative` to:

```json
{
  "value": "<verbatim citation string formatted per existing cells>",
  "unit": "narrative text",
  "derivation_method": "Bundle G re-pass with country-name-only matching (relaxed from Bundle E session 2 keyword-score threshold). Direct read of MSR {2024|2025|2026}.pdf via pdftotext -layout. Sentences extracted around named-mention sites; verbatim — no paraphrase.",
  "uncertainty_band": "verbatim citation; no estimation",
  "source": "Munich Security Report {year}, p. {page} | <repeat per cited year>",
  "source_year": <most-recent-year-cited>,
  "confidence": "M"
}
```

Confidence = `M` (not H) reflects: (a) the country was below the original strategic-keyword threshold, so its MSC framing is shallow; (b) verbatim quote is reliable but salience is low.

For "structurally absent" countries, follow the rule in methodology step 4 — confidence still `M`, derivation_method documents the absence.

### Sub-task — Metadata follow-up

After all 13 cells are updated, refresh `metadata.session_status` in the same JSON:

1. **Replace `top_3_remaining_gaps_for_bundle_d`** — current entries are stale (RRF gap was resolved by Phil-supplied Sectoral Data; Cedefop a+b were resolved by Bundle F). New top-3:
   ```json
   [
     "Munich Re per-country event coverage — 22/36 null by Munich Re top-3-Europe-only publication policy. Could close ~10-15 via Aon Catastrophe Insight + Swiss Re sigma; deferred — sparse-by-design propagates to Bundle D as documented uncertainty.",
     "EU MFF SAFE allocation table for 14 unnamed countries + midterm-review per-country shares — awaiting Commission publication. Ranges retained at L-confidence; Bundle D propagates as wide uncertainty band.",
     "Klinger M→H validation against Eurostat LFS occupation-level employment shares — 125 cells at M-confidence; lift deferred until Bundle D scoring shows whether Klinger weighting is sensitive."
   ]
   ```

2. **Add a `bundle_g_deltas` block** to `session_status`:
   ```json
   {
     "session_label": "Bundle G (2026-04-29) — MSC narrative closure for 13 below-threshold countries + metadata follow-up",
     "narrative_cells_lifted_L_to_M": <count>,
     "structural_absence_findings": [<list of ISOs with 0 MSC mentions across all 3 reports>],
     "msc_reports_re_processed": ["MSR2024 full", "MSR2025 full", "MSR2026 full"],
     "method": "Country-name-only matching (relaxed from keyword-score threshold)"
   }
   ```

3. **Increment `session_status.session_label`** to `"Bundle G final (2026-04-29) — narrative + metadata follow-up; Phase 2 inputs locked for Bundle D"`.

4. **Recompute coverage**: `lens4_geopolitical_narrative` H-conf goes from 0 → likely 0 (still M for the 13); but full-cell-with-real-content count updates. Refresh `cells_populated_estimate` if any sub-cell completeness change occurred.

5. **Update `data_gaps`**: remove any entries where `lens == "lens4_geopolitical_narrative"` AND the cell now has substantive content (verbatim or structural-absence). For genuine `null` entries (none expected after this pass), retain.

### Constraints

- BR-19 no fabrication: verbatim only. If a country isn't in the PDFs, document the absence — do not invent.
- BR-21 per-cell provenance: every cell ships with the 5 provenance fields exactly as in the existing 23 cells.
- Phil does all git commits (synthesis project not under git; no git operations needed).
- Do NOT modify `layer-6-lens-framework.md`.
- Do NOT touch any of the other 35 cells in `lens4_geopolitical_narrative` that already have verbatim citations.
- Master session reminder: Phil is treating the calling session as the orchestrator. Report back to it via the structured "When done" block; do not start Bundle D from this session.

### Verification

Before declaring complete:
1. Re-load `layer-6-phase2-data.json`; spot-check 3 of 13 cells and confirm verbatim format matches DE/FR/IT pattern.
2. Confirm no cell has paraphrased content — every quoted passage should be findable verbatim in the source PDF.
3. Confirm structural-absence cells (if any) carry the M-confidence + the explicit "interpret as low Atlanticist-frame salience" framing.
4. JSON validates; all 36 country keys still present; no schema drift.
5. `tasks_pending` still empty; `top_3_remaining_gaps_for_bundle_d` refreshed; `bundle_g_deltas` block present.

### When done — report back to master session with

- 13/13 cells lifted from L→M confidence (or N/M if any were structurally absent — list ISOs)
- Top-3 most-cited passages by report-year (which countries appear most prominently in MSC 2024 / 2025 / 2026)
- Any country flagged as "structurally absent" across all 3 reports
- Confirmation that `top_3_remaining_gaps_for_bundle_d` is refreshed
- Bundle D blocking status: confirmed unblocked / new blocker discovered

### Anticipated outcomes

- BE, ES, IE, EL likely have 1–2 verbatim citations available (medium-economy EU members; appear in NATO / migration / energy contexts)
- LU, MT, CY likely structurally-absent or 1 mention each
- BA, MK likely have Western-Balkans-cluster citations (Bundle G should capture cluster-level mentions and attribute to BA / MK with explicit "named within Western Balkans cluster of: ..." framing)
- LI almost certainly structurally absent; document the finding and proxy-flag CH treatment
- LT, LV, SK have likely 2–3 mentions each in NATO eastern-flank context

## END PROMPT
