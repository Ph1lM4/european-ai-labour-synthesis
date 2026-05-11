# Handover Prompt — Bundle O: Layer 6 Site Build (Phase 4 Track B)

Bounded build session. Static-site v0.1 scaffold for `synthesis.nexalps.com` rendering Layer 6. Mirrors the **v3 Nexalps layer-site design system** (disruptions / reskilling / careers / demographics). Reads from the locked SOT JSON + the post-N2-redrive deliverable surface. Ships 5 pages + Einfache Sprache toggle for first deploy. ~150–210 min.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).**

---

## Context (read this section before the START PROMPT)

This handover supersedes any earlier Bundle O draft. State as of 2026-04-30 evening:

- **SOT JSON enriched** (Bundles P/Q/R) — per-country Lens 2 demographic-buffer object; per-country Lens 1 absorption + regulatory-friction; per-country A→C transition rates; Italy −485,823 net migration; 7.55M / 450K / 15-year capacity gap; 8-country squeeze with two sub-clusters.
- **Deliverable surface locked** (post-N2 redrive + editorial pass + plain-language fixes) — Executive Edition, One-Pager, Einfache EN/DE, Specialist Appendix, glossary TSV (43 entries), Lens framework spec.
- **Corridor C2 renamed** "Bifurcated Absorption" → **"Partial Absorption"** globally.
- **Squeeze cluster locked at 8 countries** (BE, DE, DK, FI, FR, NL, NO, SE) with Nordic + Continental sub-cluster decomposition.
- **"Part 7" public-facing convention** ("Layer 7" is internal master-session vocabulary only).
- **Executive register absorbs Notion-Explain framings:** traffic-light (fragility classes), weather patterns (regimes), what-if futures (scenarios), five simple checks (lenses).

Bundle O renders this state. No re-computation. No content rewrite.

---

## START PROMPT

I need you to build the v0.1 scaffold of `synthesis.nexalps.com` — the public rendering of Layer 6. Mirror the v3 Nexalps layer-site design system (disruptions / reskilling). Render from the locked SOT JSON and the post-N2-redrive deliverable surface. Ship 5 pages + Einfache Sprache toggle for first deploy. Country-detail pages are Bundle O.2 (post-scaffold), out of scope.

This is NOT re-computation or rewrite. All content is locked.

### Read FIRST (absolute paths)

**Canonical inputs (data + deliverable surface):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — SOT JSON (post-Bundles-P/Q/R enrichment, schema v1.0). Every render claim traces to a field. ~250 KB single-file fetch.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document-executive.md` — **Executive Edition** (~2,400 words, Notion-Explain register). Primary content source for `index.html`.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-onepager.md` — McKinsey-style One-Pager (~750 words). Source for downloadable PDF + condensed homepage rendering.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document-einfache-en.md` — Einfache English (B1, ~1,300 words). Source for English Einfache toggle variant of `index.html` + `glossary.html`.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document-einfache-de.md` — Einfache Deutsch (B1, ~1,250 words). Source for German Einfache toggle variant.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document.md` — Specialist Appendix (~6,400 words). Primary content source for `methodology.html`.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-glossary-draft.tsv` — 42 terms with `term \t standard_definition \t einfache_definition`. Primary content source for `glossary.html`.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — locked spec. Reference for sparkline spec (line 418 — 5-trajectory per country 2026–2035), Ukraine line 341, corridor labels (now "Partial Absorption").

**Architecture reference (v3 design system):**
- `/Users/philippmaul/Documents/projects/european-disruptions-map/site/index.html` — **primary architecture reference.** Live at `disruptions.nexalps.com`. Mirror HTML head, font loading, PostHog block, dark-theme CSS variables (`--background: #09090b`, `--foreground: #fafafa`, accent `#f97316`), glassmorphic floating top-nav, mobile burger menu, skip-link + focus-visible accessibility, `404.html` + `og-image.png` + `favicon.svg` + `llms.txt` standard assets, JSON-LD block.
- `/Users/philippmaul/Documents/projects/european-reskilling-map/site/index.html` — secondary v3 reference. Cross-check pattern consistency. If diverged on detail, prefer disruptions (more recent build).
- `/Users/philippmaul/Documents/projects/european-disruptions-map/site/analysis.html`, `findings.html`, `sources.html` — page-template references for analytical / findings / sources content.

**DO NOT mirror:**
- `/Users/philippmaul/Documents/projects/european-ai-exposure-map/site/` — v1 pattern (oldest, thinnest, overdue for retrofit; do not propagate).
- `/Users/philippmaul/Documents/Other/My projects/Nexalps/nexalps-website/` — React/Vite parent site at `nexalps.com`. Layer subdomains use the lighter v3 toolchain.

Skim the disruptions-map site folder end-to-end before writing — copy CSS variable definitions, navigation HTML, font loading, PostHog block, `_redirects` / `robots.txt` / `sitemap.xml` / `llms.txt` patterns. Treat v3 as locked architecture; do not invent new patterns.

### Output folder

`/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/` — total folder budget < 600 KB excluding `data.json` copy.

```
site/
├── index.html               # Headline + corridor map + class panel + 5 findings (Executive register)
├── scenarios.html           # Spectrum + sparkline + scenario toggle + probability table
├── methodology.html         # Specialist gateway — methodology + amendments + appendix
├── sources.html             # Provenance + source bundles + license
├── glossary.html            # 42-term glossary, supports Einfache toggle
├── data.json                # Copy of layer-6-deliverable-data.json (or symlink)
├── glossary.tsv             # Copy of layer-6-glossary-draft.tsv (consumed by glossary.html)
├── 404.html                 # v3 standard
├── favicon.svg              # v3 standard
├── og-image.png             # 1200x630 social preview
├── _redirects               # Netlify redirects (mirror disruptions pattern)
├── robots.txt               # Mirror disruptions
├── sitemap.xml              # 5-page sitemap
└── llms.txt                 # Mirror disruptions pattern
```

### Page-by-page spec

#### index.html — Executive register, traffic-light corridor map, 5 findings

**Headline visual:** 36-country grid colour-coded by fragility class (traffic-light: I=green, II=amber, III=orange-red, IV=deep red). Tooltip on hover/tap shows country code + name + corridor + class + scale_tag + narrative_one_liner. Pair colour-coding with hatch/pattern or text label for colour-blind accessibility.

**Sections (top-to-bottom):**
1. **Header.** Title: "Europe's AI Labour Map Experiment — What Survives the Stress Test" (matches Executive doc title). Sub-title: "36 European labour markets, scored across five lenses, stress-tested under seven scenarios." Nav links: Index / Scenarios / Methodology / Sources / Glossary. Einfache Sprache toggle in nav (see below).
2. **Prelude paragraph** (≤300 words): render Executive §Prelude verbatim.
3. **Headline finding** (Executive §What Survives, ≤500 words): the 9-country resilient set, the strict-vs-softer rule, the "no unconditionally safe European labour market" closer, the silver-lining paragraph.
4. **Corridor map** (the 36-country grid, central visual).
5. **Fragility-class panel** — 4 cards (I/II/III/IV) with count + label + 1-line rule + country list. Source: SOT `fragility_classes`.
6. **Five folded findings** as cards or accordion. Use Executive §4 (or One-Pager 5-finding slate as compact alt) for the body. Each card ~80 words. Reference §4 Class III for the 7.55M / 450K / 15-year capacity gap math; reference §4 squeeze paragraph for the 8-country two-sub-cluster decomposition.
7. **Italy callout** (load-bearing finding): the −485,823 net migration finding deserves a visually distinct callout in or near the Lens 2 finding card. Source: SOT `countries.IT.lens_findings.lens2_demographic_buffer.net_migration_dependency`.
8. **Closer** (Executive §6): brief, with Part 7 teaser.
9. **Footer:** "Built by Philipp Maul / Nexalps. License: CC-BY-4.0 (data) + MIT (code). Last updated 2026-04-30." Cite-as line: `Maul, P. (2026). Layer 6 — European AI Labour Market Synthesis. Nexalps. https://synthesis.nexalps.com/`.

**SEO + structured data:**
- `<title>European AI Labour Market Synthesis | Nexalps</title>`
- Meta description ≤155 chars; canonical to `https://synthesis.nexalps.com/`.
- Open Graph + Twitter Card mirroring exposure-map / disruptions.
- JSON-LD `@type: Dataset` block with creator, license (CC-BY-4.0), spatialCoverage, keywords. Mirror exposure-map exactly; update title/description.

#### scenarios.html — spectrum framing + sparkline + probability table

**Headline visual:** 5-line trajectory sparkline per country (locked spec line 418 — one line per S1/S2a/S2b/S3/S4a/S4b, x-axis 2026–2035, y-axis corridor 1–3). Country selector + scenario-emphasis toggle (highlight one trajectory at a time, fade others).

**Sections:**
1. **Header + nav + Einfache toggle.**
2. **Spectrum framing** (Executive §3 ¶1 verbatim): the 7 scenarios as 5 spectrum positions (uber-optimistic / optimistic / middle / pessimistic / pessimistic) + S5 sitting outside. Include the framing-assumption disclaimer.
3. **Three weather patterns panel** (Executive §3 ¶2): growth-baseline / secular-stagnation / post-growth-empirical. Country list per pattern.
4. **Sparkline visual** (D3-rendered).
5. **Probability table:** regime × scenario, mid-points + 80% CI. Source: SOT `scenarios.{S}.probability_per_regime`.
6. **Capacity-side anchor** (Executive §3 ¶4 + §4 Class III math): 7.55M deep-reskilling need / ~450K annual net new / 15-year backlog / 5–9-year speed gap. Visual treatment: callout card or sidebar.
7. **s2b-dependent callout** (Q4 load-bearing): "The optimism path narrows to Climate Zone-C. Three countries — AT, LU, TR — reach Corridor 1 only under S2b." Use Executive §4 phrasing.
8. **Capability-floor breach panel:** 12-country list (BE, CH, DE, DK, IE, IS, LI, LU, NL, NO, SE, UK) + map highlight. Source: SOT `cross_cutting_findings.capability_floor_breach`.
9. **Squeeze cluster panel** (Executive §4 squeeze paragraph): 8 countries with Nordic + Continental sub-cluster decomposition. Source: SOT `cross_cutting_findings.regulatory_asymmetry` + per-country `squeeze_flag` objects. Annex III + PWD count as supporting numerics.

#### methodology.html — Specialist gateway

Plain-text page; no interactive visuals beyond the amendments-trail code-fence. Renders the Specialist Appendix §2 (Methodology) + §8 (Methodological Appendix) at full fidelity. Source: `layer-6-deliverable-document.md` §2 + §8 + spec `metadata.amendments_trail` + `metadata.Q_decisions_baked_in` + `metadata.schema_deviations_from_draft`.

**Sections:**
1. Header + nav + Einfache toggle (Einfache version is "Coming soon" stub for v0.1 per scope below).
2. Methodology overview (Executive §2 + Specialist §2 hybrid, ~600 words).
3. Amendments trail (3-stage Class I rule ladder, code-fence rendered).
4. Threshold-locking ladder (Phase 1 → Phase 3, table).
5. Capability-floor breach scope ceiling.
6. MFF per-country gap callout.
7. Candidate-country C2 sub-cluster routing callout.
8. Phase 5+ enhancement candidates list (from `metadata.layer_4_enrichment.composition_gaps_surfaced` and equivalents).

#### sources.html — provenance + license

Plain-text page. Renders Specialist Appendix §9 + the source bundle list from `metadata.source_bundles` + a per-bundle short description. Includes license block (data: CC-BY-4.0, code: MIT) and contact (LinkedIn). External sources cited (Autor 2024, El-Sahli & Upward 2017, Cedefop 2025, EU Net-Zero Industry Act, EEA ECRA 2024, Munich Re NatCat 2025, IISS Military Balance 2025, SIPRI 2025, EU MFF Mid-Term Review 2024, NATO Hague June 2025, ReArm Europe).

#### glossary.html — 42-term reference, Einfache toggle support

Renders `glossary.tsv` as a searchable / filterable list. Each term: name + standard definition. Einfache toggle swaps the standard definition for the Einfache definition column. Search/filter input at top. Letter-jump anchors (A–Z) for navigation.

**Sections:**
1. Header + nav + Einfache toggle (this page is one of the two that ship with full Einfache support in v0.1).
2. Search input + letter-jump anchors.
3. Term list (alphabetical).
4. "Suggest a term" footer pointing to LinkedIn.

### Einfache Sprache toggle — v0.1 scope

**Toggle UI:** persistent button in nav labelled "Einfache Sprache" / "Standard." Click toggles + saves preference to `localStorage` key `synthesis-nexalps-language-mode` (values: `"standard"` or `"einfache"`).

**Implementation pattern:**
- All toggle-aware text wrapped in two parallel DOM nodes: `<div data-lang="standard">...</div>` + `<div data-lang="einfache" hidden>...</div>` (or equivalent CSS-controlled visibility).
- Toggle script reads localStorage on page load + applies state; toggle button click flips state + dispatches a custom event for any D3-rendered components that need to re-render captions.
- Visualisations themselves don't change between modes; only captions, tooltip copy, and surrounding prose.

**v0.1 Einfache coverage:**
- `index.html` — full Einfache version (consume `layer-6-deliverable-document-einfache-en.md` for English; `-de.md` for German).
- `glossary.html` — full Einfache version (consume `einfache_definition` column from glossary TSV).
- `scenarios.html` / `methodology.html` / `sources.html` — **"Coming soon" stub** when toggled to Einfache. Display: heading + brief paragraph in B1 ("This page is being prepared in Einfache Sprache. The standard version is available; click 'Standard' to read it.") + back-to-toggle button. These ship in Bundle O.2.

**Language sub-toggle:** when Einfache mode is active on `index.html` or `glossary.html`, surface a second toggle for EN ↔ DE. Persistent in `localStorage` key `synthesis-nexalps-einfache-language` (values: `"en"` or `"de"`).

**Status banner:** Einfache pages display a small banner at the top: *"Erstentwurf — vor Veröffentlichung muss eine Einfache-Sprache-Fachperson den Text prüfen. / First draft. Before public release this text needs review by a certified Einfache-Sprache editor."* This is the locked status header from the Einfache files. It must not be removed.

### Visual + interaction rules

- **Font:** Geist 400/500/600/700 (mirror v3 layer-site font import).
- **Theme:** dark, matching v3. Copy CSS variable definitions verbatim from disruptions-map (see prior handover for exact tokens; `--background: #09090b` / `--foreground: #fafafa` / accent `#f97316` / radii / Geist font / 150ms cubic-bezier transition).
- **Class-colour overlay** (data-encoding only, not chrome): I=#22c55e, II=#f59e0b, III=#ef4444, IV=#7f1d1d. Pair with hatch pattern + text label for accessibility.
- **Navigation:** glassmorphic floating top-nav (mirror disruptions `.site-nav`), mobile burger menu, skip-link, `:focus-visible` tokens.
- **D3 v7** from `https://d3js.org/d3.v7.min.js`.
- **Mobile:** legible at 375px width. Sparkline degrades to single-country view. Corridor grid wraps to 4-wide on narrow viewports.
- **Accessibility:** skip-link, alt text on all visuals, tooltips keyboard-accessible, class colour-coding paired with hatch + label.
- **No emoji** in copy or UI (🛈 tooltip markers from the Executive doc map to UI affordances, not display glyphs — render as info icons).
- **PostHog config:** reuse exact block + project token (`phc_bjax6jdRxYJAaExodvALjRru8AQzUSbYFNlWlXiJM8A`, EU host `https://eu.i.posthog.com`, `person_profiles: 'identified_only'`) from disruptions-map. Do NOT generate a new token — Phil has scheduled a portfolio-wide PostHog audit + cookie-banner review post-Bundle-O ship; consistency required.

### Constraints

- **Read-only** against the SOT JSON, deliverable docs, glossary TSV, locked spec, v3 site references.
- **No emoji** in body or UI (info-icon SVGs replace 🛈 markers in the Executive doc).
- **No build step** — pure static HTML + vanilla JS + D3. No bundler, framework, transpilation.
- **No external trackers** beyond PostHog.
- **No new external dependencies** (D3 + Geist via CDN are existing; flag any others before adding).
- **Phil does all git commits.**
- **"Part 7" globally** — 0 instances of "Layer 7" in any rendered page.
- **"Partial Absorption" globally** — 0 instances of "Bifurcated Absorption" in any rendered page.
- **Squeeze cluster = 8 countries** (BE, DE, DK, FI, FR, NL, NO, SE) with two sub-clusters; LU explicitly NOT squeeze (where surfaced).

### Verification (run before reporting back)

1. `data.json` is byte-identical to `../layer-6-deliverable-data.json` (or symlinked).
2. All 5 pages parse as valid HTML5.
3. Each page does its `fetch('./data.json')` (where applicable) and renders without console errors against a static-served folder.
4. **Class distribution rendered on `index.html` = 9 / 9 / 15 / 3.**
5. **AT, LU, TR named together in s2b-dependent callout** on `scenarios.html`.
6. **Capability-floor breach list** has exactly 12 countries on `scenarios.html`.
7. **Squeeze cluster panel** lists exactly 8 countries (BE, DE, DK, FI, FR, NL, NO, SE) with two sub-clusters labelled.
8. **Italy callout** renders on `index.html` showing the −485,823 net migration finding.
9. **Amendments trail** on `methodology.html` shows all 3 stages (S5-orthogonal → relative-stable → asymmetric-guard).
10. JSON-LD block on `index.html` validates as structured data.
11. PostHog config mirrors disruptions exactly (same project token).
12. **No emoji in any HTML body.**
13. **0 "Layer 7"** anywhere in the site (only "Part 7").
14. **0 "Bifurcated Absorption"** anywhere (only "Partial Absorption").
15. Mobile layout: all 5 pages render legibly at 375px viewport width.
16. Einfache toggle persists across pages via `localStorage`; functional on `index.html` + `glossary.html`; "Coming soon" stub on the other 3.
17. Einfache status banner present + visible on Einfache-mode pages.
18. EN ↔ DE sub-toggle functional in Einfache mode on `index.html` and `glossary.html`.
19. Total site folder size (excluding `data.json`) < 600 KB.
20. `_redirects`, `robots.txt`, `sitemap.xml`, `llms.txt`, `404.html`, `favicon.svg`, `og-image.png` all present and structurally mirror disruptions-map equivalents.

### When done — report back to master session with

1. Pages shipped + line counts per page.
2. Verification checklist (1–20) — pass/fail per item.
3. Rendering gaps surfaced (places where SOT JSON or deliverable docs didn't carry a visual-needed field — e.g. country-coordinate data for choropleth; confirm fallback used).
4. PostHog config decision: reused disruptions token confirmed.
5. Deployment readiness: is the folder Netlify-deploy-ready as-is, or do DNS / build-settings tweaks need flagging?
6. Mobile-render description (per page at 375px viewport).
7. Einfache toggle functional verification (localStorage persistence + sub-toggle EN/DE + stub display on non-supported pages).
8. Any candidate brain captures (cross-layer-site rendering patterns, code-craft observations, BR triggers fired).
9. Recommended next step: dispatch Bundle N3 (Long-Read with graphics) immediately or pause for Phil deployment to live site first?

## END PROMPT
