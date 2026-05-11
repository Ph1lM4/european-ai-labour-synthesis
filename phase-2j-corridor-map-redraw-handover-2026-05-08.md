# Handover Prompt — Phase 2J: Corridor Map Redraw (ESRA-style Dot Rendering)

Bounded build session. Replaces the existing rastered corridor map (Phase 2A.2, 1938 cells, equal-area, on `site/findings.html`) with an ESRA-style dot-based rendering. **Output mode: live build + iteration.** Two render targets: synthesis-site (ai-project style, dark theme, interactive) + PDF export (Nexalps style, static). ~6–8 h initial build + 2–4 Phil-iteration rounds (Phase 2A.2 history baseline).

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).** This is a substantial code-generation session: SVG geometry, projection math, country-centroid mapping, interactive event handlers, dual-stylesheet rendering.

---

## Research scope

**Corpus + targeted lookup as needed.** Country centroid lat/lon coordinates are likely needed for Mercator-derivative projection — `site/data.json` may or may not carry them; if not, sub-session does a targeted lookup against a stable public source (Natural Earth, Wikipedia ISO-2 → centroid table, or equivalent — single sweep, document source). No open-ended WebSearch beyond that.

---

## Context

Phil flagged 2026-05-08 (post-Bundle-W browser pass) that the existing rastered corridor map (Phase 2A.2, 4 iterations: 222 → 400 → 762 → 1850 → 1938 cells; 96 × 68 grid; Lambert cylindrical equal-area) has two issues for the deliverable surface:

1. **Nordic geography squashed** by equal-area projection — recognizability suffers
2. **Style direction shift** — Phil pinned ESRA reference (https://framerusercontent.com/images/ggXVwXnhZVcm3Up0jplnwE515As.png + https://www.studentrobotics.eu/) — geometric dot-based rendering with variable dot sizes for outline fidelity

**The 5 redraw locks (Phil 2026-05-08):**

| # | Lock | Detail |
|---|---|---|
| 1 | **Tile shape** | Dots (circles), ESRA-style — NOT square cells |
| 2 | **Size variance** | Mix of larger + smaller dots — small fills coastlines / narrow regions; large defines country body. Variance encodes outline fidelity, NOT data. |
| 3 | **Nordic geography** | "Displayed more real" — switch to Mercator-derivative projection (Web Mercator or equivalent); recognizability beats equal-area |
| 4 | **Labels on map** | REMOVED — microstate labels + any country codes / names. Map is unlabelled. Identification via interaction (hover tooltip / click cross-link). |
| 5 | **Interactive cross-link** | PRESERVED — existing state machine (clicks highlight scenarios / fragility classes; P3 absorbed into P1 per Phase 2A.2 lock) carries forward in the SVG-based redesign |

**Two render targets** (locked architectural decision 2026-05-08):

- **Site version** (ai-project style, dark theme, interactive): replaces rastered map in `site/findings.html` and anywhere else it's referenced. Coloring follows synthesis-site current palette (preserve corridor-class color encoding in dark theme).
- **PDF version** (Nexalps style, static): pearl-white background `#F8F9FA`, deep-teal `#087569` C1 / alpine-gold `#F59E0B` C2 / alpine-red `#C41E3A` C3 / granite-gray `#4A5568` C4 reference. Geist font. SVG primary, PNG fallback. No interactivity.

Both render from the same SVG geometry; theme/style applied via CSS variables or stylesheet swap.

---

## START PROMPT

Replace the existing rastered corridor map with an ESRA-style dot-based rendering. Two render targets (site + PDF) sharing the same SVG geometry with theme-swap. Preserve interactive cross-link layer on the site. Iterate to Phil-lock.

### Read FIRST (absolute paths)

**Existing implementation (read for current state):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/findings.html` — locate the existing rastered-map block + interactive cross-link state machine
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/europe.html` — check whether map is referenced here too
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/scenarios.html` — same check
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/data.json` — country list, corridor-class assignments, fragility-class assignments. **Check whether lat/lon centroids are present** — if not, flag and add via targeted lookup
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/bundle-o-phase-2a2-rastered-map-brief-2026-05-06.md` — original Phase 2A.2 brief (constraints, naming conventions, what was tried)

**Nexalps style reference (PDF target):**
- `/Users/philippmaul/Documents/Other/My projects/Nexalps/nexalps-website/tailwind.config.ts` — exact color tokens (lines 23–39), type ladder (lines 90–123)
- `/Users/philippmaul/Documents/Other/My projects/Nexalps/nexalps-website/src/index.css` — CSS variables, custom utilities

**ESRA reference (visual style anchor):**
- https://framerusercontent.com/images/ggXVwXnhZVcm3Up0jplnwE515As.png — the corridor-style dot map Phil pinned
- https://www.studentrobotics.eu/ — page context

**Sister-layer site for graphics-pattern reuse (if any layer-site already has a dot-based map):**
- demographics (port 3847) — has D3 sankey + projection visuals; check if any base mapping exists

### Country coverage scope

36 countries (post-V/X locks):
- EU-27: AT, BE, BG, HR, CY, CZ, DK, EE, FI, FR, DE, EL, HU, IE, IT, LV, LT, LU, MT, NL, PL, PT, RO, SK, SI, ES, SE
- EFTA-4: CH, IS, LI, NO
- UK
- Candidate-partial: BA, MK, RS, TR

Plus Ukraine (Class IV reference panel — render but optionally distinguish).

### Build sequence

1. **Inspect existing rastered-map implementation** — read findings.html block; identify interactive state machine API (event handlers, highlight functions, scenario / fragility-class binding).
2. **Acquire country centroids** — check `data.json` first; if absent, targeted lookup (Natural Earth ISO-2 centroid table or equivalent). Document source in `_provenance` field.
3. **Choose Mercator-derivative projection** — Web Mercator standard (EPSG:3857) is fine; for narrower-Europe focus, custom Lambert conformal conic centered on Europe is also defensible. Pick one, document choice.
4. **Compute dot grid** — for each country, generate set of dots that approximate country shape:
   - Large dots (~8–10 px @ desktop, scale-down for mobile) for country interior
   - Small dots (~3–4 px) for narrow regions / coastlines / outline fidelity
   - Approach: country polygons → uniform grid sampling → adaptive density at borders
5. **Render SVG geometry** — `<circle>` per dot with `cx`, `cy`, `r`, `data-country` (ISO-2), `data-corridor-class`, `data-fragility-class`, `class="dot"`
6. **Apply two stylesheets:**
   - Site version: synthesis-site dark theme. Preserve existing corridor-class color encoding (read what's currently used in findings.html — likely CSS classes like `.c1`, `.c2`, `.c3`, `.c4` or similar).
   - PDF version: Nexalps palette per the locked color map (teal/gold/red/granite). Class hierarchy: `.dot[data-corridor-class="C1"] { fill: var(--nexalps-deep-teal-text); }` etc.
7. **Wire interactive state machine on site version** — port existing event handlers; ensure clicks on any country's dot-cluster highlight scenarios / fragility classes per Phase 2A.2 lock (P3 absorbed into P1).
8. **Remove labels** — strip microstate labels + country codes from the rendered SVG. Identification via hover tooltip + click cross-link only.
9. **Export pipeline** — site version inline in `findings.html`. PDF version as standalone `.svg` file (path: `site/exports/corridor-map-nexalps.svg`) + PNG fallback (`site/exports/corridor-map-nexalps.png`, ~2400 × 1600 @ 2x).
10. **Iterate to Phil-lock** — first build → Phil review → 2–4 iteration rounds expected (Phase 2A.2 baseline).

### Discipline (carry forward)

- **Style lock — site stays in ai-project style.** Site version uses synthesis-site current dark-theme palette + container conventions. NO Nexalps restyle on the site.
- **Two render targets share geometry, differ in style only.** Same SVG `<circle>` set; CSS classes / variables swap palette. Avoid divergent geometry between site + PDF.
- **No labels on map** — both versions. Microstates identified via tooltip (site) or legend (PDF). Country codes / names do not render on the map.
- **Banned-phrase scan on own draft + commit messages.** Tier 1/2/3 reference: `skills/linkedin-playbook/references/banned-phrases.md`.
- **BR-19 fabrication discipline** — country centroids are real coordinates from a verified source; do not infer / approximate. Flag any country where canonical centroid is ambiguous (e.g., overseas territories, Russia-Asia split).
- **Audit-at-class** (per `feedback_audit_at_class_at_phase_boundaries.md`) — when a rendering issue appears at one country (e.g., Iceland dot density wrong), audit all 36 countries against the same metric, not just spot-fix Iceland.
- **Counterfactual-corpus hardening light variant** (per `feedback_counterfactual_corpus_hardening.md`) — cross-check the Mercator-derivative output against Phil's ESRA reference image for visual fidelity before locking the projection.
- **Time budget: 6–8 h initial build.** If projection / centroid acquisition / dot-density tuning balloons, surface scoping issue and stop at the budget. Iterate from there.
- **Phil iterates on visual** — surface first build as DRAFT, expect 2–4 review rounds before lock. Phase 2A.2 history: 4 iterations from 222 → 400 → 762 → 1850 → 1938 cells. Same iteration shape expected.

### Verification (before reporting back)

1. **Site version live in `findings.html`** — replaces existing rastered map; interactive cross-link works (click highlights scenarios / fragility classes per Phase 2A.2 lock).
2. **PDF version exported** — `site/exports/corridor-map-nexalps.svg` + `corridor-map-nexalps.png` (2400 × 1600 @ 2x); pearl-white background; teal/gold/red/granite palette; Geist labels (none on map; legend uses Geist if present).
3. **Both versions share geometry** — same `<circle>` set; diff is CSS only. Confirm via `<circle>` count + `cx`/`cy`/`r` parity check.
4. **No labels on map** — grep the SVG output for any `<text>` element overlapping country dot regions; should be zero.
5. **Country coverage complete** — 36 countries + Ukraine reference panel rendered; spot-check via DOM query for `[data-country="XX"]` for each ISO-2.
6. **Nordic geography improved** — visual check: NO/SE/FI/DK/IS recognisable in Mercator-derivative; not vertically squashed.
7. **No labels** — final visual audit.
8. **md5 audit** — `site/data.json` unchanged unless centroids added (in which case flag the targeted addition + provenance). Other site files: `findings.html` changes (map block replaced); `europe.html` and `scenarios.html` change only if they referenced the rastered map.
9. **Banned-phrase grep** on commit messages + any prose surfaces touched.

### Report-back format

Single markdown file: `phase-2j-corridor-map-redraw-report-2026-05-08.md`. Same directory.

1. **TL;DR** (5–7 bullets): build state, projection chosen, centroid source, dot-count, Phil-iteration readiness
2. **Implementation summary** — projection / centroids / dot-density approach / interactive state machine porting
3. **Site version live audit** — screenshot or preview-snapshot of the new map in `findings.html`; interactive verification (click country, confirm cross-link fires)
4. **PDF version export audit** — screenshot of SVG + PNG; Nexalps palette confirmation; legend (if any) using Geist
5. **Country coverage check** — 36 + UA confirmed; per-country dot count for sanity
6. **Verification checklist (1–9)** — pass/fail per item
7. **Phil-iteration handoff** — flag the 2–3 things you're least sure about for first review (e.g., Nordic dot density, color contrast for C1 in dark theme, projection edge handling for TR)
8. **Brain capture candidates** — likely none unless the dual-render target pattern surfaces something portfolio-wide

---

## Out of scope

- Other site graphics density changes — that's the parallel Site Graphics Density Audit (different sub-session)
- N3 PDF composition — N3 absorbs the corridor map PDF export, doesn't redo the geometry
- IA changes / new pages
- Brain skill enrichment — capture candidates surface for Phil per Rule 12

---

*This brief is the dispatch prompt for the Phase 2J corridor map redraw. Sub-session builds the new map (two render targets, shared geometry), surfaces first iteration to Phil, expects 2–4 Phil-iteration rounds before lock. Output: live site + SVG/PNG exports for N3.*
