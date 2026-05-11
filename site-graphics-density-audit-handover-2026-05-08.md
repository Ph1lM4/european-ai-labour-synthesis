# Handover Prompt — Site Graphics Density Audit (Flag-Only)

Bounded analytical sub-session. Per-page review of all 7 synthesis-site pages (post-Bundle-W state) to identify where graphical elements would lighten text-heavy reading. **Output mode: flag-only.** No SOT edits, no graphics builds, no site code changes. ~3 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).** This is mostly read-and-analyse; code-craft applies only to inline HTML/CSS snippets if surfaced in candidate descriptions.

---

## Research scope

**Corpus-only.** The post-Bundle-W synthesis site at `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/` is the corpus. No external WebSearch beyond reference-style cross-checks against sister layer sites (deployed at ai-exposure / careers-map / disruptions-site / demographics / reskilling-site — accessible via local preview at ports 8092 / 8091 / 3003 / 3847 / 3005 respectively).

---

## Context

Phil ran a browser pass on the synthesis site post-Bundle-W (2026-05-08) and flagged: *"the site is text-heavy. maybe we should review every page and think about where we can add more graphical elements to make it a bit of a lighter read."* Site is structurally clean (Phases 1A → 2I + Bundle W) but visual density is currently text-dominant with corridor map (rastered, 1938 cells), weather-pattern viz (scenarios), shift-bars (S1 + S3), 4-card stats panel (landing), and fragility-class graphic as the existing graphical elements.

**Important style lock:** the synthesis site stays in **ai-project style** (current design language — dark theme, container widths 1200 px, type ladder 10/11/12/13/14/15/16/18/20/22/24/28/36 px). Audit recommendations must respect this — do not recommend a Nexalps-style restyle. PDF deliverables (Bundle N3) handle Nexalps style separately.

**The corridor map is being redrawn separately** (Phase 2J — ESRA-style dot rendering, locked 2026-05-08). Audit can note current corridor map as "to-be-redrawn" but should not propose corridor-map changes in this scope.

---

## START PROMPT

Audit all 7 synthesis-site pages for graphical-element opportunities. Per-page table of candidates with priority. Flag-only. ~3 h.

### Read FIRST (absolute paths)

**Synthesis-site pages (in audit order):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/index.html` — landing
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/findings.html` — Findings drill-down (carries Italy block, scenarios stack, etc.)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html` — 8-scenario page (carries weather-pattern viz, S8 Polycrisis Drag block)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/europe.html` — pan-European aggregates (3 SMs, 2 panels EU-27 / 36-market)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/methodology.html` — 4-SM Minto methodology (SM 4 v5 just landed)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/sources.html` — 59 source-cards
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/glossary.html` — term glossary

**Reference (sister layer sites for graphics-pattern reuse — accessible via local preview):**
- `ai-exposure` port 8092 — ai-exposure.nexalps.com
- `careers-map` port 8091 — career flow diagrams
- `disruptions-site` port 3003 — disruption-pathway visuals
- `demographics` port 3847 — D3 sankey migration flows, demographic projections
- `reskilling-site` port 3005 — reskilling capacity visuals

**Inspection approach:**

1. Load preview tools via ToolSearch: `mcp__Claude_Preview__preview_start`, `preview_eval`, `preview_inspect`, `preview_snapshot`, `preview_screenshot`.
2. Start `synthesis-site` preview server (port 3006). Confirm running.
3. For each of the 7 pages: navigate, full-page snapshot, identify text-dense regions (long unbroken paragraphs, dense lists without visual break, repeated numeric callouts that could become charts, stat sequences, comparisons buried in prose).
4. For sister-layer sites: cross-reference any graphics that handle the same pattern type and could port to the synthesis site.

### Output structure (target ~80–120 lines, flag-only report)

Single markdown file: `site-graphics-density-audit-report-2026-05-08.md`. Same directory.

1. **TL;DR** (5–7 bullets): top priorities across pages, total candidate count, reusable-vs-port-vs-new split, any cross-page graphics that would serve multiple surfaces
2. **Per-page table** (one section per page; 7 sections total): each candidate as a row with columns:
   - **Location** — section / line range / sub-element on the page
   - **Density signal** — what's text-heavy (long paragraph / dense list / numeric prose / comparison-buried-in-text / etc.)
   - **Proposed graphic** — what visualization would lighten it (small inline chart / icon row / pull-quote with stat / comparison bars / mini-table-as-graphic / etc.)
   - **Source** — reusable existing site graphic / portable from sister layer (name which) / new build needed
   - **Priority** — high / medium / low
3. **Cross-page candidates**: graphics that would serve 2+ pages (e.g., a fragility-class legend graphic that lands on findings + scenarios + europe; or a corridor-class color key reused everywhere)
4. **Top 5–8 priority shortlist** — your recommended subset for first-pass build, sized roughly by impact-vs-effort
5. **Out-of-scope flags**: any candidate that crosses into N3 territory (PDF graphics) or Phase 2J territory (corridor map) — flag for awareness, do not include in shortlist
6. **Brain capture candidates** (if any surfaced; do not auto-write — surface for Phil per Rule 12)

### Discipline (carry forward)

- **Style lock — ai-project style only.** Audit operates within the synthesis site's current design language. No "Nexalps restyle" recommendations. No tone shift away from advisory + policy audience.
- **Banned-phrase scan on own draft before surfacing.** Tier 1/2/3 reference: `skills/linkedin-playbook/references/banned-phrases.md`. Grep for: `load-bearing`, `structurally`, `structural asymmetry`, `the analysis is built to surface`, `read` as singular noun, fragment-then-colon openers.
- **BR-19 fabrication discipline.** Cite from the actual page state, not generalised assumptions. If a sister-layer site is referenced as "has this graphic," verify by inspecting the live site at the local preview port.
- **Audit-at-class** (per `feedback_audit_at_class_at_phase_boundaries.md`). Per-page candidates in a systematic table; categorise every row.
- **Counterfactual-corpus hardening light variant** (per `feedback_counterfactual_corpus_hardening.md`, captured 2026-05-08): briefly cross-check against 1-2 sister-layer sites for graphics-pattern reuse — counter-vantage check on "what's the strongest graphical language for this content type in the layer-site portfolio."
- **No SOT edits.** Verify md5 checksums on the 7 page files + `site/data.json` are identical pre-/post-session. The synthesis-site preview can refresh on edits but the audit doesn't make any.
- **Time budget: 3 h.** If a page balloons (sources page audit, in particular — 59 source-cards), surface the scoping issue and stop at the budget. Audit completeness > per-page exhaustion.
- **Honest deviation reporting.** If a sister-layer site has nothing applicable, say so. Do not pad to hit a "graphics-portable from X" claim per page.

### Verification (close with this)

```
md5 site/index.html site/findings.html site/scenarios.html site/europe.html \
    site/methodology.html site/sources.html site/glossary.html site/data.json
```

Match to pre-session run. Flag any drift (should be zero).

### Report-back format

Single markdown file as above. Phil reviews → master uses priority shortlist to inform N3 graphics scope + any direct-build candidates that don't need PDF parity → dispatch downstream as appropriate.

---

## Out of scope

- Any code changes to site files (audit is flag-only; subsequent build phases handle changes)
- Corridor map redesign — that's Phase 2J (locked 2026-05-08, separate dispatch)
- PDF / N3 graphics scope — those are PDF-only graphics in Nexalps style
- Brain skill enrichment — capture candidates surface for Phil per Rule 12
- New page additions / IA changes — those are Phase 1B-class and require explicit Phil approval

---

*This brief is the dispatch prompt for the site graphics density audit. Sub-session inspects all 7 pages via preview, builds per-page candidate table, surfaces priority shortlist. Phil reviews → priorities feed N3 graphics scope + any direct-site builds.*
