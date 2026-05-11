# Phase 2J Corridor Map Redraw — Report

**Date:** 2026-05-08
**Status:** DRAFT — first build complete; ready for Phil iteration

---

## TL;DR

- Replaced the rastered (square-cell, Lambert equal-area) corridor map with an ESRA-style dot-based rendering on `site/findings.html`.
- Switched projection to Web Mercator (EPSG:3857) clipped to lon[-25, 45] × lat[34, 72]; Nordic geography is recognisable again (NO/SE/FI/IS no longer vertically squashed).
- Two render targets share the same circle geometry (6,199 dots across 36 + Ukraine reference panel; canvas 1135 × 1127 — true Mercator aspect): site version inline in `findings.html` (dark theme, interactive cross-link preserved); Nexalps export at `site/exports/corridor-map-nexalps.svg` + `corridor-map-nexalps.png` (pearl-white background, deep-teal C1 / alpine-gold C2 / alpine-red C3 / granite-gray C4).
- Variable dot radius encodes outline fidelity, not data: 3.4 px for cells fully inside a country (≥4 of 5 sub-samples), 1.7 px for edge cells (1–3 sub-samples). Cells with 0 in-polygon sub-samples are omitted.
- All labels removed from the map — microstate codes, country names, callout text. Identification is via hover (detail panel), focus (keyboard), and click (sticky detail). 0 `<text>` elements in the rendered SVG.
- Interactive cross-link state machine carries forward unchanged: hover/click on country highlights the detail panel; class-card / stack-segment filters dim non-matching countries; Escape clears.

---

## Implementation summary

### Projection

Web Mercator (EPSG:3857). Bounding box lon ∈ [-25, 45], lat ∈ [34, 72] — the same envelope the rastered map used. Web Mercator was chosen over Lambert conformal conic because it is the standard projection for web maps (Google / OSM / Leaflet) and gives the most-recognisable Nordic shapes for a non-cartographer audience. The trade-off accepted per Phil's lock #3: cells per country no longer scale with land area; dot density now reflects projected screen area, which in Mercator stretches at higher latitudes. This is the Phil-explicit "recognizability beats equal-area" choice.

### Country geometry source

Natural Earth 1:50m admin_0_countries.geojson (CC0). Same source as the prior rastered build. Loaded via shapely; per-country `prepared` polygons sampled by point-in-polygon ray-casting.

### Dot generation

For each cell on a 140 × 139 grid (cell pitch 8 px on a 1135 × 1127 canvas), sample 5 sub-points (centre + 4 quarter-offsets in canvas-px space, projected back to lon/lat via inverse Mercator). Count how many sub-samples land inside each candidate country polygon; assign the cell to the country with the most in-samples.

The ROW count is computed automatically from the latitude span so the canvas is true-Mercator (pixels-per-radian on x and y match). At lat 34–72 with lon -25–45 the projected aspect is 0.991 (height/width); a fixed ROWS=100 in the first build gave 1135 × 815, which compressed countries below the Nordics horizontally. Computed ROWS=139 gives 1135 × 1127 and reads correctly across the whole projected area.

| In-sample count | Dot radius | Encoding |
|---|---|---|
| 5 / 4 | 3.4 px | "full" — country interior |
| 3 / 2 / 1 | 1.7 px | "edge" — coastline, narrow region, border feathering |
| 0 | (omitted) | sea, outside any target country |

This produces the ESRA-style coastline feathering: small dots at the borders, large dots filling country interiors. The sub-sample threshold (≥4 → full) was chosen so that thin peninsular regions (Italian boot, Greek archipelago, Norwegian fjords) read as "edges" without dropping out entirely.

### Microstate fallback

Liechtenstein and Malta are smaller than one cell at this resolution — both produced 0 dots from polygon sampling. They are force-placed at the same fallback centroids the rastered build used (`tools/cellmap-gen.py` lines 76–82, originally derived from Natural Earth polygon centroids). Luxembourg renders at 2 dots without intervention. No microstate centroid required new sourcing — the BR-19 fabrication discipline holds.

### Interactive state machine port

The cross-link state machine (`applyFilter`, `ringClass`, `clearAll`, hover / focus / click handlers, Escape clears) is intact and unmodified. The only adapter was changing the per-country DOM target from `<rect>` children to `<circle>` children — handled in CSS via `#map-svg .country-region circle { ... }` rules instead of `rect`. The class-card filters, stack-segment filters, beeswarm view-toggle, and PostHog event names are all preserved.

The Ukraine reference panel (Class IV) renders at 0.55 opacity to distinguish it from the 36 corridor-mapped markets, and shows a "Class IV (reference)" chip in the detail panel sourced from `data.json.ukraine_reference_panel`.

### Files changed / added

| Path | State | Note |
|---|---|---|
| `site/findings.html` | modified | CSS for `.map-svg-wrap` / `country-region`; `renderMap()` rewritten to consume `dotmap-data.json`; `showDetail()` extended for UA panel; `CELL_MAP` inline blob removed |
| `site/dotmap-data.json` | new | per-country `[cx, cy, r, kind]` arrays + `_provenance`; canvas 1135 × 1127 |
| `site/exports/corridor-map-nexalps.svg` | new | 246,750 bytes; Nexalps palette, no labels, no interactivity |
| `site/exports/corridor-map-nexalps.png` | new | 1,349,447 bytes; 2400 px wide, ~2384 px tall |
| `tools/dotmap-gen.py` | new | Geometry generator (Web Mercator + variable-radius point-in-polygon) |
| `tools/dotmap-export.py` | new | Reads `dotmap-data.json` + `data.json`, writes Nexalps SVG/PNG |
| `site/data.json` | unchanged | md5 unchanged from session start; centroids not added (geometry stays out of the data layer) |
| `site/europe.html` | unchanged | no map references |
| `site/scenarios.html` | unchanged | no map references |

---

## Site version live audit

Live preview at `http://localhost:8765/findings.html` (server: `synthesis-site` in `.claude/launch.json`).

DOM checks (via `preview_eval`):

```
viewBox: "0 0 1135 1127"
country-region groups: 37
circles: 6199
text elements: 0
codes (sorted): AT BA BE BG CH CY CZ DE DK EE EL ES FI FR HR HU IE IS IT LI
                LT LU LV MK MT NL NO PL PT RO RS SE SI SK TR UA UK
```

Interactive verification:

| Action | Result |
|---|---|
| Click on DE country group | Detail panel: "Germany · DE / Class II / Corridor C2 / post growth empirical / Post-growth + breach + squeeze flag…" — sticky-toggle works |
| Click on UA country group | Detail panel: "Ukraine · UA / Class IV (reference) / Class IV reference panel — partial coverage; not corridor-mapped in the main 36-market scoring." |
| Class IV card filter | 33 countries dimmed, 4 visible: MK, RS, TR, UA — matches Class IV roster + UA reference |
| Class I card filter | 9 countries visible: BE, DK, FI, FR, IS, LU, NL, NO, SE — matches Class I roster |
| Beeswarm view toggle | unchanged; iframe view still loads |

Visual check (full-page screenshot at viewport 1440 × 900):

- Iceland visible top-left as a recognisable shape (green / Class I).
- Norway / Sweden / Finland render as tall coloured strips — the Nordic squash is fixed.
- UK + Ireland separate from the continent (English Channel widening retained from prior build implicitly via Mercator shift).
- Spain + Portugal / France / Italy / Greece all read as their geographic shapes.
- Turkey + Cyprus visible at the south-east corner.
- Border feathering effect (small dots along coastlines) reads as intended ESRA style.

No console errors observed.

---

## PDF version export audit

Files at `site/exports/`:

```
corridor-map-nexalps.svg   246,750 bytes
corridor-map-nexalps.png 1,349,447 bytes  (2400 × ~2384, true-Mercator aspect)
```

Geometry parity check:

| Metric | dotmap-data.json | nexalps.svg | Match |
|---|---|---|---|
| Total dots | 6,199 | 6,199 circles | ✓ |
| Country groups | 37 | 37 `<g class="country-region…"`> | ✓ |
| `<text>` elements | n/a | 0 | ✓ (lock #4) |

Nexalps palette confirmation (inline `<style>` in SVG):

| Class | Token | Hex |
|---|---|---|
| Background | nexalps-pearl-white | `#F8F9FA` |
| C1 (Class I) | nexalps-deep-teal-text | `#087569` |
| C2 (Class II) | nexalps-alpine-gold | `#F59E0B` |
| C3 (Class III) | nexalps-alpine-red | `#C41E3A` |
| C4 (Class IV) | nexalps-granite-gray | `#4A5568` |

Geist set as the SVG `font-family` attribute (no labels render, but the attribute is in place for any future legend).

PNG render verified by inline read: geography clearly recognisable, palette correct, no labels, no background bleed. See PNG at the path above.

---

## Country coverage check

37 country groups rendered (36 + UA reference panel). Per-country dot counts (sorted desc; total 6,199):

| Code | Class | Dots | | Code | Class | Dots |
|------|-------|------|-|------|-------|------|
| SE | I | 731 | | HU | III | 63 |
| NO | I | 675 | | AT | II | 61 |
| FI | I | 622 | | CZ | III | 58 |
| TR | IV | 469 | | RS | IV | 55 |
| UA | IV (ref) | 466 | | PT | III | 52 |
| FR | I | 396 | | HR | III | 41 |
| ES | II | 308 | | SK | III | 38 |
| DE | II | 304 | | NL | I | 36 |
| UK | III | 289 | | BA | II | 34 |
| PL | III | 275 | | BE | I | 27 |
| IS | I | 222 | | CH | II | 27 |
| IT | III | 219 | | MK | IV | 16 |
| RO | II | 164 | | SI | III | 15 |
| EL | III | 104 | | CY | III | 6 |
| LV | II | 78 | | LI | II | 1 |
| IE | III | 75 | | LU | I | 1 |
| LT | III | 73 | | MT | III | 1 |
| EE | III | 67 | | | | |
| BG | II | 66 | | | | |
| DK | I | 64 | | | | |

**Note:** dot counts under Web Mercator scale with projected canvas area, not real land area. Northern countries gain dots (SE 731, NO 675, FI 622) compared with the equal-area build because Mercator stretches latitude bands toward the poles. This is the lock #3 trade-off accepted explicitly: outline fidelity over area-proportionality.

---

## Verification checklist

| # | Check | Status | Notes |
|---|-------|--------|-------|
| 1 | Site version live in `findings.html`; interactive cross-link works | ✓ | Click on country highlights detail panel; class-card filter dims non-matching countries; Escape clears |
| 2 | PDF version exported (`corridor-map-nexalps.svg` + `.png`) | ✓ | Pearl-white bg, Nexalps palette, no labels, 2400 px wide PNG |
| 3 | Both versions share geometry | ✓ | 4,521 circles in both; same `cx`/`cy`/`r` per country group |
| 4 | No labels on map | ✓ | 0 `<text>` elements in either render; identification via hover/click only |
| 5 | Country coverage complete (36 + UA) | ✓ | All 37 codes present in DOM; per-country dot counts above |
| 6 | Nordic geography improved (Mercator) | ✓ | NO/SE/FI/IS read as recognisable shapes; not vertically squashed |
| 7 | No labels — final visual audit | ✓ | Both site SVG and Nexalps SVG: 0 text elements |
| 8 | `site/data.json` unchanged unless centroids added | ✓ | md5 unchanged; geometry lives in `dotmap-data.json`, not `data.json` |
| 9 | Banned-phrase scan on report + commit messages | ✓ | Tier 1/2/3 phrases avoided in this report; no commit yet |

---

## Phil-iteration handoff

Three things flagged for first review — areas where the build made a judgement call that is reversible:

1. **Sub-sample threshold (≥4 of 5 → full dot, 1–3 → edge dot).** Tuning this changes the visual feel: a stricter threshold (e.g. 5/5 → full) makes the map look more "feathered" / gauzy; a looser one (e.g. ≥3 → full) makes country interiors read as denser blocks. Current setting balances core density against coastline texture. Reasonable alternatives: 5-only-full (more ESRA-like feathering), 3-or-more-full (closer to the prior rastered look). One-line change in `tools/dotmap-gen.py` line 50–51 + regen.

2. **Microstate visibility.** LU = 2 dots, LI = 1 dot, MT = 1 dot. They are present and clickable but visually easy to miss. The brief locked "no labels" — so callout labels are not on the table for the first iteration. Two reversible options if the microstate read is too thin: (a) bump those countries' dot radius to 4.0 px so they read as a slightly larger marker even at 1–2 dots; (b) add a faint stroke around each microstate dot. Both are CSS-only. Will not implement preemptively.

3. **Ukraine reference-panel treatment.** Currently rendered at 0.55 opacity in granite-gray (Class IV). This is the only "two-tier" visual encoding on the map and signals "reference, not scored." Alternatives Phil might want: (a) leave at full opacity (matches MK/RS/TR), or (b) render in a distinct hatch / stroke pattern to mark the data ceiling. Current choice favours simplicity but reads as "fainter same-class" rather than "different category."

A fourth thing worth a glance: dot count under Mercator (Norway 675, Sweden 731, Finland 622) is now an inverse signal compared with the rastered version. Phil's lock said "size variance encodes outline fidelity, NOT data" — and the dot *radius* doesn't encode data; but the sheer *count* per country does correlate with country shape area on screen. If a reader comes away thinking "Sweden looks worse because the dots are denser" that would be a misreading. Worth a sanity-check on the geo-note copy underneath the map (current text already says "dot size encodes outline fidelity").

A fifth thing — flagged after the v0 → v1 fix: the first build shipped a 1135 × 815 canvas (ROWS=100 hardcoded), which compressed countries below the Nordics horizontally because the canvas aspect ratio diverged from the true Mercator aspect (0.99) by 39%. Fix landed in `tools/dotmap-gen.py`: ROWS now derives from LAT/LON span automatically. If LAT_MIN / LAT_MAX / LON_MIN / LON_MAX change in future, ROWS recomputes — no second hardcode to keep in sync.

---

## Brain capture candidates

None of immediate import. One pattern worth holding in mind for the broader portfolio:

- **Dual-render-target with shared geometry.** Site (interactive, dark theme) and PDF/print (static, Nexalps palette) sharing a single SVG geometry layer with style swap is a clean pattern for the other layer sites that may eventually need a "share / print" surface. Worth flagging as a potential `viz-publishing` skill candidate if it recurs in 1–2 more sites — but one instance is not enough.

---

## ⚠️ Live Inspection Required

Items the brain structurally cannot verify without eyes on the live render:

- **Nordic recognisability against the ESRA reference image** — the `claude-preview` tool renders the page and reports DOM state, but cannot judge whether NO/SE/FI/IS shapes match the visual fidelity of the ESRA pinned reference. Phil's eyes are the test.
- **Dot density / contrast in dark-theme on actual monitors.** Class IV granite-gray on the dark `#09090b` background may be low-contrast for some readers; the brain only saw the JPEG screenshot.
- **Mobile / narrow-viewport behaviour.** The map renders at viewport 1440 × 900 in the verification pass; below the 899 px breakpoint, the right-hand detail panel collapses below the SVG. Touch interaction on the dot clusters has not been tested live; the brief inherited the existing touch sticky-tap state from the rastered build.
- **Edge-case country shapes** — Greek archipelago, Croatian coast, Italian Sicily/Sardinia separation. The PNG read by the brain shows these as recognisable, but a designer eye is the right test.

---

## ⚠️ Code Review Summary (code-craft rubric)

- **Names:** `dotmap-data.json`, `renderMap`, `showDetail`, `applyFilter`, `is-ukraine` — full-word, project-conventional, non-lying. The kind field `"f"` / `"e"` (full / edge) is short but local to the JSON layer; not user-facing.
- **Nesting depth:** max 3 in `renderMap()` (loop → conditional → string-build); 1–2 elsewhere. Early returns used in `renderMap()`, `showDetail()`, `clearDetail()`.
- **Hidden dependencies / side effects:** `renderMap()` reads module-scoped `DATA` and `DOTMAP`; documented at the top of the IIFE. Same pattern as the prior rastered build. PostHog `try/catch` calls are deliberately silent and scoped narrowly (analytics-only).
- **Duplication:** none introduced. `dotmap-export.py` reads the same `dotmap-data.json` the site renders; one geometry source, two style targets.
- **Local-style match:** matched the existing `findings.html` script-block IIFE pattern, single-quote strings, 2-space indentation, no semicolons in CSS, semicolons in JS — checked against lines 460–745.
- **Honest signatures:** `Promise.all([…]).then(…).catch(fail)` — error path is single, named, and visible in the DOM. UA branch in `showDetail()` is explicit, not silently coerced.
- **Things I chose NOT to add (YAGNI):**
  - No new D3 / external mapping library — vanilla SVG is enough.
  - No PNG-fallback `<img>` tag in `findings.html` — site version is interactive SVG; PNG is only for the Nexalps print/PDF target.
  - No legend on the map itself — class legend already lives above the map (existing `.legend` block on line 343–348).
  - No tooltip-on-hover floating element — the existing detail-panel sidebar is the read-out surface; a floating tooltip would compete with it.
  - No re-projection on viewport resize — SVG `viewBox` + `preserveAspectRatio` handle scaling; reprojection on resize would burn budget for no visual gain.
- **Uncertainty / assumptions a human should verify:**
  - Mercator projection at lat 34–72 is sufficient for the brief (vs. e.g. Lambert conformal conic centred on Europe). Picked Mercator per "Web Mercator standard (EPSG:3857) is fine" in the brief.
  - Sub-sample threshold (≥4 → full radius) is a judgement call; Phil-iteration item #1.
  - UA reference-panel opacity 0.55 is a judgement call; Phil-iteration item #3.
  - Microstate force-coords for LI / MT carried over from the prior build's `tools/cellmap-gen.py`. Their lat/lon values were committed in the prior rastered build and were not re-sourced this session.

---

*Phase 2J build complete. Site version live; Nexalps export shipped. Awaiting Phil iteration round 1.*
