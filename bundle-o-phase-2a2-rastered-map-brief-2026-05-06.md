# Design-Exploration Brief — Bundle O Phase 2A.2: Rastered Corridor Map

Bounded design-exploration session. Produces a single high-fidelity standalone mockup of the rastered corridor map (Problem 1 in the Phase 2A taxonomy) replacing all three prior P1 alternatives. Carries the full P3 cross-link interaction (hover-highlight + click-filter) baked in, plus a beeswarm view toggle. Output is one HTML mockup in `site/phase2-explorations/1-corridor-map/D-rastered.html` + a short README addendum. No edits to live site. Phil reviews, locks final visual tweaks; Phase 2B integrates into `findings.html` §3. ~60–90 min.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).**

---

## Context

Phase 2A complete (12 mockups, 5 problems). Phil locked all 5 directions but rejected the original P1 candidates: the tile cartogram (A) reads as a heatmap not a map; the beeswarm (B) loses geography; the sortable list (C) is too utilitarian. Phil's reference: the European demographics layer-site map (real country shapes, choropleth fills, dark theme) but **more abstract** — the iStock-style dotted/rastered Europe where countries appear as clusters of dots, not as outlined shapes.

This mini-exploration produces one mockup of that direction. Phase 2B then integrates the locked mockup into `findings.html` §3 and wires it to the §4 fragility-class panel for cross-linking.

---

## START PROMPT

I need you to produce a single high-fidelity mockup of a rastered corridor map of 36 European labour markets. Each country renders as a cluster of small coloured dots arranged on a coarse Europe-shaped grid; dot colour = the country's fragility class. Hover (desktop) / tap (mobile) reveals a country detail panel. Click-filter from a fragility-class card dims non-matching dots to ~30% opacity. A toggle button switches view to the existing `B-beeswarm.html`.

This is exploration only. Do not modify any live-site file. Output is one new HTML file + a short README addendum. Phil reviews; Phase 2B (separate sub-session) integrates into the live site.

### Read FIRST (absolute paths)

- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/data.json` — SOT. Per-country fields used: `code` (ISO-2), `name`, `class` (I/II/III/IV), `baseline_corridor`, `narrative_one_liner`, `regime_tag`, `scenario_distribution_language` (or equivalent one-line read).
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/phase2-explorations/1-corridor-map/A-geographic.html` — prior tile cartogram (reference for colour tokens, focusable-element pattern, country-detail panel structure).
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/phase2-explorations/1-corridor-map/B-beeswarm.html` — beeswarm view (the toggle target).
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/phase2-explorations/3-cross-linking/A-hover-highlight.html` + `B-click-filter.html` — interaction patterns to absorb into the new map.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/findings.html` — register reference (Italy callout structure for hover-panel layout; fragility-class panel for class-colour mapping).

### Design parameters

**Grid.** Coarse cell grid covering Europe + EFTA + UK + 4 candidates. Recommended target: ~30 cols × 25 rows (≈ 750 cells). Density scales with country area (larger countries = more cells; LU/MT/LI render as 1–2 cells with a callout label nearby). The grid does not need to be photorealistic; the iStock reference is the aesthetic anchor (Phil-approved direction).

**Country-to-cell mapping.** Two acceptable approaches:

1. **Precomputed cellMap (preferred).** Use a one-shot Python or Node script to sample a low-res European GeoJSON (Natural Earth 1:50m or 1:110m, CC0) at fixed grid resolution; output a `{ "AT": [[col,row], ...], "BE": [...], ... }` JSON. Bake the result inline into the mockup file. Total inline data ≤ 20 KB.
2. **Hand-authored cellMap.** At coarser resolution (~20×16 = 320 cells), a hand-authored cellMap is feasible. Document the resolution choice in the README.

Either is acceptable; pick whichever produces a recognisable Europe at the specified resolution.

**Cell rendering.** Each cell is either a dot (filled) or empty (water/non-Europe). Recommended cell size: 10–14 px square at desktop; cell gap 2–4 px. Dots render as either:
- CSS-grid `<div>` cells with `border-radius:50%` (if circular)
- CSS-grid `<div>` cells with `border-radius:2px` (if square — closer to iStock reference)

Pick one consistent treatment. Do not mix.

**Colour fills.** Use existing fragility-class tokens:
- Class I = `--class-i` (green)
- Class II = `--class-ii` (amber-light)
- Class III = `--class-iii` (amber)
- Class IV = `--class-iv` (red)
- "No data" or non-coverage = `--card-border` (neutral grey)

Each country's cells share its class colour. Do not add new tokens.

**Country region as focusable unit.** Each country is one keyboard-focusable element (`<button class="country-region" data-code="..." data-class="..." aria-label="...">`) wrapping its cells. Cells inside a country region are not individually focusable (would produce 750 tab stops). Tabbing moves country-by-country in a sensible order (geographic L→R, T→B is fine).

**Hover / tap detail panel.** A fixed-position panel (top-right desktop / bottom-of-map mobile) surfaces the focused country's:
- Name
- Class chip (coloured + label)
- Baseline corridor (C1/C2/C3)
- One-line mechanism (from `narrative_one_liner` or `scenario_distribution_language`)
- Regime tag

Panel collapses when no country is focused.

**Toggle button.** Top-right of the map: `Map view ↔ Beeswarm view`. Clicking switches the body-render from rastered map to beeswarm. Either inline both views in the same mockup with display-toggle, or load `B-beeswarm.html` in an iframe — pick the cleaner option.

**Click-filter (P3 absorbed).** Below the map, embed a stripped-down version of the fragility-class panel (4 class cards) so cross-link interaction is demonstrable. Clicking a class card:
- Dims all non-matching country regions to 30% opacity
- Adds a badge: *"Showing Class N — n countries"* with a clear (×) button
- Esc clears
- A second click on the same class card also clears

Hover on a class card: temporarily highlights matching countries with a 2 px ring; hover ends, ring disappears. Hover and click states do not collide (transient ≠ sticky).

**Mobile (≤900 px).**
- Map fills container; cell size scales down to 7–9 px
- Detail panel collapses below map (not floating)
- Toggle and class-card row stack vertically
- Tap replaces hover; first tap = sticky-show panel; second tap on same country = clear; tap empty area = clear
- Class cards remain tappable for filter

### Reference inputs

Two visual anchors:
1. **iStock dotted Europe** (Phil-supplied) — overall aesthetic: countries as dot clusters, dark borders absent, Europe-shape readable from dots alone.
2. **`demographics.nexalps.com` overview map section 1** — portfolio house style: dark theme, class-chip legend strip below, simple title above, no chrome around the map. The new mockup matches this house style for portfolio coherence.

The new mockup is *more abstract* than the demographics choropleth (no country borders) but still in the same dark-theme/legend-strip layout.

### Constraints

- **No live-site edits.** Output goes only to `site/phase2-explorations/1-corridor-map/D-rastered.html` + an updated `site/phase2-explorations/1-corridor-map/README.md`.
- **Existing CSS tokens only.** No new colour / spacing / radius tokens.
- **No external libraries.** Inline SVG / CSS only. No D3, no Leaflet, no Mapbox. If a precomputed cellMap is used, the GeoJSON sampling happens offline; the mockup ships with the cellMap already baked in (no runtime GeoJSON dependency).
- **No new copy.** All labels, hover-panel content, and class-chip text taken from `data.json` or existing live-site labels.
- **Mobile responsive at 900 px breakpoint.** Test at 375 / 768 / 1280 widths.
- **Accessibility.** Every country region keyboard-focusable; class colours supplemented by labels in the hover panel + class chip text; Esc clears state; hover-only signals never the sole indicator.
- **No emoji.**
- **No PostHog tracking** (Phase 2B reapplies).
- **Phil does all git commits.**

### Verification (before reporting back)

1. `D-rastered.html` opens cleanly via the running preview server; no console errors on load.
2. All 36 European labour markets render as distinct country regions with their correct fragility-class colour fill (verify against `data.json` per-country `class` field).
3. Tabbing reaches every country region in a sensible order; tab count = 36 (or 37 if including the toggle button).
4. Hover desktop / tap mobile reveals the detail panel with the correct country data.
5. Class-card click dims non-matching regions to 30% opacity; badge shows correct country count for the active class; clear button + Esc both clear.
6. Hover on class card adds 2 px ring on matching regions; hover end removes it; hover + click states do not collide.
7. Toggle button switches between rastered map and beeswarm view; switching back returns to the rastered map without state loss.
8. Mobile (375 px width): map fits without horizontal scroll, cells scale down, detail panel collapses below map, class cards stack vertically.
9. Inline cellMap JSON ≤ 20 KB (or hand-authored alternative is documented in README with resolution tradeoff).
10. Live site files (`findings.html`, `scenarios.html`, `europe.html`, etc.) untouched — `git status` shows only the new mockup + README addendum.

### When done — report back to master session with

1. File path of the new mockup + brief description of cellMap approach (precomputed vs hand-authored; resolution; total cells; non-empty cells).
2. Verification checklist (1–10) — pass/fail per item.
3. Static screenshot or rendered-HTML preview proof of the desktop view + the mobile view + a click-filter active state.
4. Any constraint violations or design decisions that needed flagging (cell-size / grid-resolution tradeoffs; country-region tab order; LU/MT/LI callout treatment).
5. Cross-problem readiness for Phase 2B — confirm the country-region API (`data-code` + `data-class` + class-card-event listener pattern) is stable enough to wire into `findings.html` §3 without redesign.
6. Phase 2B build-cost estimate revision for Problem 1 — recheck the prior 3–4 h estimate against the actual rastered-map work; flag if higher.
7. Any candidate brain captures (likely none).

## END PROMPT
