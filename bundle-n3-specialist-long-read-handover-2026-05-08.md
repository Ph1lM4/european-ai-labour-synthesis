# Handover Prompt — Bundle N3: Specialist Long-Read with Graphics + Nexalps PDF

Bounded composition session. Builds the Specialist Long-Read derivative of the post-Phase-2K Specialist Appendix as a narrative-driven advisory deliverable with graphics. **Two output targets:** markdown long-read source + Nexalps-styled PDF. Audience: advisory-track (Cembra-class engagements, board materials, lecture decks). ~10–12 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).** This is a substantial composition + code-generation session: PDF generator extension, Nexalps graphic exports, ReportLab layout work.

---

## Research scope

**Corpus-only.** All content derives from existing post-Phase-2K state. No external WebSearch. Graphics either (a) re-export from existing site assets in Nexalps style or (b) compose new from data already in `data.json` / `layer-6-deliverable-data.json`.

---

## Context

The Specialist Appendix (`layer-6-deliverable-document.md`, ~305 lines post-Bundle-W) is the technical reference document. The **Long-Read** is a different format — narrative-driven, graphic-rich, designed for sustained advisory-track reading. Same body of work, different audience contract:

| Specialist Appendix | Long-Read |
|---|---|
| Section-by-section data document with provenance | Narrative-driven advisory document with graphics |
| Technical reference (probability tables, source schemas, methodology trail) | Story-driven (the diagnostic, the asymmetry, the capacity gap, the stack) |
| Read selectively for specific facts | Read sustained in one sitting (~2 hr) |
| Synthesis-site style implicitly (markdown for reference) | **Nexalps style for PDF** (consulting deliverable) |

**Style locks (from prior conversations 2026-05-08):**

- **Long-read PDF = Nexalps style.** Pearl-white background `#F8F9FA`, Geist font (300/400/500/600/700), `pure-black` text, `deep-teal-text` `#087569` accent (WCAG-AA on white), `granite-gray` secondary. Light-italic special headlines (300 weight + italic, 80/56/40 px) usable for pull-quotes. 1280 px container or A4-equivalent print-safe. NOT synthesis-site dark theme.
- **Long-read markdown source = Nexalps register**, plain conversational, banned-phrase scan applies. Same Phil-locked register as the rest of the suite (no `load-bearing`, no `structurally`, no `the analysis is built to surface`, no `read` as singular noun, no fragment-then-colon openers).
- **Graphics: each needs a Nexalps-style render.** Corridor map already exported (Phase 2J: `site/exports/corridor-map-nexalps.svg` + `.png`). Other graphics (stack-bar, reskilling funnel, lens-grid, possibly weather-pattern + fragility-class panel) need new Nexalps versions.

**Existing PDF generator infrastructure (per brain memory):** `/Users/philippmaul/Documents/projects/job-scout-agent/generate_pdf.py` uses ReportLab + Geist fonts (font path `projects/job-scout-agent/fonts/`). Generic variant at `generate_pdf_generic.py`. Reuse + extend for the long-read PDF; do not reinvent.

---

## START PROMPT

Build the Specialist Long-Read in three phases: composition (markdown), graphics build (Nexalps exports), PDF assembly (ReportLab). Audience: advisory-track. Nexalps style for the PDF. Plain conversational register throughout.

### Read FIRST (absolute paths)

**Source content (post-Phase-2K state):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document.md` — Specialist Appendix, the canonical content body
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/index.html` — landing-page hero + lede (Phil-locked)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/findings.html` — Italy plain-prose block, scenario stack, reskilling §5 funnel content, Conclusion
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html` — 8-scenario page (S8 Polycrisis Drag prominence)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/europe.html` — pan-European Minto + variation guard
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/methodology.html` — 4-SM Minto v5 (header + 4-paragraph SM 4 just landed)
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — SOT data
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/sources.html` — 59 source-cards

**Nexalps style reference:**
- `/Users/philippmaul/Documents/Other/My projects/Nexalps/nexalps-website/tailwind.config.ts` — color tokens (lines 23–39), type ladder (lines 90–123)
- `/Users/philippmaul/Documents/Other/My projects/Nexalps/nexalps-website/src/index.css` — CSS variables, custom utilities
- Extracted Nexalps style notes in conversation memory: pearl-white `#F8F9FA`, deep-teal-text `#087569` (WCAG-AA), granite-gray `#4A5568`, alpine-gold `#F59E0B`, alpine-red `#C41E3A`. Geist (sans), Arnhem (serif fallback). Desktop type ladder: H1 80 / H2 56 / H3 40 / H4 32 / H5 24 px (medium 500). Body 24/20/16/14. Special light-italic 80/56/40 for pull-quotes.

**Existing graphics (re-export targets):**
- `site/exports/corridor-map-nexalps.svg` + `.png` — already Nexalps-styled (Phase 2J)
- `site/findings.html` §2 stack-bar — needs Nexalps re-render
- `site/findings.html` §5 reskilling funnel — needs Nexalps re-render
- `site/methodology.html` lens-grid — needs Nexalps re-render

**PDF generator:**
- `/Users/philippmaul/Documents/projects/job-scout-agent/generate_pdf.py` — ReportLab base + Geist fonts (fonts at `projects/job-scout-agent/fonts/`)
- `/Users/philippmaul/Documents/projects/job-scout-agent/generate_pdf_generic.py` — generic variant; closer starting point for the long-read

### Three phases

#### Phase 1 — Long-read markdown composition (~4–5 h)

Compose `layer-6-deliverable-long-read.md` (~3,500–5,000 words). Narrative arc:

1. **Hero + lede** — Phil-locked landing headline + 4-card stats panel ("36 markets / 9 Class I robust / 12 capability-floor breach / 15-year reskilling gap")
2. **The diagnostic** (~600 words) — five lenses, why these five, what the test is. Plain conversational. Cites Cedefop / Eurostat / Klinger / Autor 2024 inline.
3. **The 36-country corridor map** (graphic + ~400 words) — embed Nexalps corridor map; explain three corridors + Mercator + dot-encoding-fidelity caveat. Italy plain-prose block lands here as a worked example.
4. **The asymmetry** (~600 words) — count vs population-weighted: 9/9/15/3 by count, but population-weighted shifts the picture (Class I = 25.6% EU-27 working-age; Class IV = 15.7% of 36-market). Embed stack-bar graphic.
5. **The reskilling-capacity gap** (graphic + ~500 words) — embed funnel graphic; explain 7.55 M cohort vs 450 K net new vs 1–3 yr displacement window vs 5–9 yr response time. Why it doesn't add up.
6. **The eight-scenario stack** (~700 words) — S1 → S8 with Polycrisis Drag as the conditional-orthogonal carrier. P(S2 | post-growth) modal finding. Wage Cliff (S5) holds 0.13–0.15 across regimes. Cascade conditional 0.05/0.10/0.15.
7. **What we tested and excluded** (~400 words) — methodology SM 4 v5 summary (three candidate additions, none held alone, mix is the answer). Hand-off to Part 7.
8. **Conclusion** (~250 words) — Phil-locked Layer 7 closer.

Embedded graphics: 4–5 Nexalps SVG/PNG inserted via standard markdown `![]()` references. Phase 2 builds them.

**Register lock — same as Specialist Appendix.** Plain conversational; Phil-locked verbatim where applicable (hero, lede, Italy block, methodology SMs, Polycrisis Drag prominence, scenarios phrasing, Conclusion). Banned-phrase scan against Tier 1/2/3 reference at every section boundary.

#### Phase 2 — Nexalps graphics build (~3–4 h)

Re-render the existing site graphics in Nexalps style. **Two-layer thinking** (per `feedback_layer_site_graphic_port_idiom.md` n=2 refinement): port the chart-box container, pick internals to match the story.

| Graphic | Source | Nexalps target | Internals |
|---|---|---|---|
| Corridor map | `site/exports/corridor-map-nexalps.svg` | already done (Phase 2J) | static SVG |
| 9/9/15/3 stack-bar | `site/findings.html` §2 | new SVG export, pearl-white bg, teal/gold/red/granite by class | static SVG (4 segments, flex weights) |
| Reskilling funnel | `site/findings.html` §5 | new SVG export, monochrome greys + deep-teal-text accent on net-new | static SVG (4 proportional bars + tip-label + callout) |
| Five-lens card-grid | `site/methodology.html` §1 | new layout, 5 cards pearl-white with `--ring-equivalent` left border in deep-teal | static SVG or directly in PDF as ReportLab Frame layout |
| (Optional) Scenario weather-pattern | `site/scenarios.html` | only if narrative needs it; defer if scope tight | TBD |

Output to `site/exports/long-read/`:
- `corridor-map-nexalps.svg` (existing, copy or symlink)
- `stack-bar-fragility-9-9-15-3-nexalps.svg`
- `reskilling-funnel-nexalps.svg`
- `lens-grid-nexalps.svg` (or skip if PDF renders directly via ReportLab)
- PNG fallbacks for each (2400 px wide, 2x DPR-equivalent for print)

#### Phase 3 — PDF generation + assembly (~3 h)

Extend `projects/job-scout-agent/generate_pdf_generic.py` into a long-read-specific generator at `tools/long-read-pdf-gen.py`:

1. **Page setup** — A4 portrait, 50 mm margins, pearl-white background, Geist font registered (300/400/500/600/700 weights from `projects/job-scout-agent/fonts/`)
2. **Style sheets** — H1 (40 / 0.95 line-height, medium 500, -1.2px tracking), H2 (28 / 1.1, medium), H3 (20 / 1.2, medium), body (11 pt / 1.55, regular), pull-quote (16 pt / 1.3, light 300 italic — the Nexalps signature move), overline (9 pt bold uppercase 2 px tracking)
3. **Image embedding** — SVG via `svg2rlg` (reportlab-graphics ext) or pre-rendered PNG fallback if SVG fails. Width 100% of content area (~110 mm) for in-flow; 80% for figure-style.
4. **Markdown → PDF pipeline** — read `layer-6-deliverable-long-read.md`, parse via `markdown` lib, emit ReportLab Story elements section-by-section.
5. **Output** — `layer-6-deliverable-long-read.pdf` (target ~12–18 pages).

### Discipline (carry forward)

- **Style lock — long-read PDF in Nexalps; markdown source register matches the Phil-locked rest-of-suite voice.** No synthesis-site dark theme on the PDF; no Nexalps-restyle in the markdown source (markdown is render-target-agnostic).
- **Banned-phrase scan on own draft + commit messages.** Tier 1/2/3 reference: `skills/linkedin-playbook/references/banned-phrases.md`. Run grep at every Phase boundary.
- **BR-19 fabrication discipline** — every numeric, every citation, every per-country claim traces to `layer-6-deliverable-data.json` SOT, the post-Bundle-W Specialist Appendix, or the 59-source bibliography. Do not invent numerics for narrative flow.
- **Audit-at-class** — when composing a section that summarises N lenses / regimes / scenarios, audit the SOT for completeness; do not compress past structural fidelity.
- **Counterfactual-corpus hardening light** — composition is corpus-only, but cross-check claims against existing site state (post-Phase-2K) at each section boundary.
- **Two-layer thinking on graphics** (per `feedback_layer_site_graphic_port_idiom.md`) — port chart-box container, pick internals to match story.
- **Time budget: 10–12 h.** Phase 1 composition is the largest; if it stretches, surface scoping issue rather than compressing the methodology / scenarios sections.

### Verification (before reporting back)

1. **Markdown source clean** — long-read renders to valid markdown; banned-phrase grep returns 0 hits; word count between 3,500–5,000.
2. **Graphics exported** — each required SVG / PNG in `site/exports/long-read/` (4–5 files); pearl-white bg confirmed; Nexalps palette confirmed via inline `<style>` audit.
3. **PDF assembled** — `layer-6-deliverable-long-read.pdf` exists; 12–18 pages; Geist rendering confirmed; image embedding works at sufficient resolution; pull-quotes use light-italic where applicable.
4. **md5 audit** — Specialist Appendix `.md` + `site/data.json` + `layer-6-deliverable-data.json` UNCHANGED (long-read does not edit the SOT or canonical reference document).
5. **Visual sanity** — first 2 pages + corridor-map page + reskilling-funnel page + methodology + conclusion: take screenshot or PDF page render for Phil sanity-check.

### Report-back format

Single markdown file: `bundle-n3-specialist-long-read-report-2026-05-08.md`. Same directory.

1. **TL;DR** (5–7 bullets)
2. **Phase 1 audit** — section-by-section word count + key Phil-locked anchors lifted verbatim + banned-phrase scan
3. **Phase 2 audit** — each Nexalps graphic with palette confirmation + dimensions + size
4. **Phase 3 audit** — PDF generator changes, page count, file size, font-registration confirmation
5. **Verification checklist (1–5)** — pass/fail per item
6. **Phil-iteration handoff** — flag the 3–5 things you're least sure about (register tone in section X, pull-quote selection, graphic placement, page-break landing)
7. **Brain capture candidates** (if any surfaced; do not auto-write — surface for Phil per Rule 12)

---

## Out of scope

- IA changes to existing site files (long-read is a new derivative; site is unchanged)
- New SOT data — long-read consumes existing data
- Re-deriving any Phase 1–3 outputs (probabilities, classifications, regime tags)
- Brain skill enrichment — capture candidates surface for Phil per Rule 12
- Deploy v1 — Phil handles git after report-back

---

*This brief is the dispatch prompt for Bundle N3. Sub-session composes the long-read markdown, builds Nexalps graphics, assembles the PDF, all in one focused session. ~10–12 h. Output: long-read .md + .pdf + 4–5 Nexalps graphic exports + report.*
