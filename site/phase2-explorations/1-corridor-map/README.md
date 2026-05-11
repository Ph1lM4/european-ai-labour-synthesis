# Problem 1 — Corridor map

## What the visual must surface

36 European labour markets distributed across three corridors and four fragility classes, with country-level mechanism reachable on hover/tap. The current 4×9 colour-coded grid loses the geographic clustering story (Nordics-as-a-block, Balkans-as-a-block); the alternatives below restore narrative, continuous variation, or country-level mechanism as the primary read.

## Alternatives

- **A — Geographic tile cartogram.** Each country = an equal-sized tile placed in approximate geographic position. Clusters become visually obvious (Nordic green block top-right, Balkan red block bottom-right, Continental amber band centre).
- **B — Beeswarm on Lens 1 ratio.** Continuous-axis dot chart with corridor edges (1.20 / 2.80) marked. Reveals the corridor-edge correction story directly and makes the "no robust under strict rule" finding visible.
- **C — Sortable / filterable list.** Country-level mechanism is the primary read, not a hover secondary. Sort by class / alphabet / ratio; filter by class. Highest accessibility and works on touch.
- **D — Rastered corridor map.** Each country = a cluster of small coloured dots arranged on a coarse 32×22 Europe-shaped grid; dot colour = fragility class. Geographic clusters read at a glance (Iberia green-shaded block, Balkans red cluster with two cascade-class flecks, Nordics green vertical band, Italy boot in red), country borders not drawn — clusters carry the geography. Hover/focus surfaces the country detail panel; click a fragility-class card dims non-matching dots to ~30 % opacity. Toggle button switches view to B-beeswarm.html via iframe. Replaces A/B/C as the locked Problem 1 direction (Phil-rejected A as heatmap, B as geography-loss, C as utilitarian).

## Trade-offs

| | A — Geographic | B — Beeswarm | C — Sortable list |
|---|---|---|---|
| Story clarity | Highest (cluster shape) | High (continuous variation) | Lower (no spatial story) |
| Accessibility | Moderate (button labels carry data) | Moderate (focus-able dots) | Highest (table-like, no hover required) |
| Mobile | Good (collapses to 7-col / 6-col grid) | OK at 375w (vertical stack) | Excellent (drops Lens-1 column) |
| Build cost | Moderate (cartogram positions hand-coded) | Moderate (collision avoidance + axis) | Minor (HTML table + sort/filter JS) |
| Cross-link compatibility | Excellent (tile = button, easy hover/click hooks) | Good (circle = focusable element) | Excellent (row = button) |
| Editorial register fit | "Here is Europe" — yes | Requires "Lens 1 ratio" vocabulary | Reads as a reference table, not a story |

## Notes on geographic positions in A

Tile positions are geographic-approximate (Iberia bottom-left, Nordics top-right, Balkans bottom-right). They are not topologically accurate — the goal is cluster legibility, not cartographic precision. Phil reviews positions at lock time; reposition is a single object literal in the script.

## D — Rastered map: cellMap approach & API

**Approach:** hand-authored ellipse generator at 32×22 grid (704 max cells; 222 active). Each country defined by `(cx, cy, rx, ry, priority)` ellipse; cells assigned to nearest country whose normalised ellipse-distance is smallest below a `1.15` cap. Empty countries (collisions or wholly excluded) force-assigned to centroid. Generator script lives at `/tmp/cellmap-gen.py` (not shipped); the resulting `CELL_MAP` JSON is baked inline into `D-rastered.html` (1.86 KB, well below 20 KB cap). No runtime GeoJSON dependency.

**Resolution tradeoff:** 32×22 chosen over the brief's recommended ~30×25 (~750 cells) because the iStock-dotted aesthetic is recognisable at lower density and hand-authoring a precomputed sample of Natural Earth at higher resolution exceeds the bounded-session budget. 222 cells averages ~6 per country — large countries (FR, UK, NO, FI, TR, IT) get 12–23 cells; small countries (LU, LI, MT) get 1 with a micro-callout label. Iterating to ~400–500 cells is straightforward (boost the ellipse `r*` values uniformly) without touching the country-region API.

**Country-region API for Phase 2B integration.** Each country renders as one SVG `<g class="country-region" data-code data-class tabindex="0" role="button" aria-label="...">` wrapping its `<rect>` cells. Stable contract for `findings.html` §3 ↔ §4 wiring:
- `data-code` (ISO-2) and `data-class` (I/II/III/IV) attributes on every region
- `.dimmed` toggles 30 % opacity on cell rects
- `.ringed` toggles a 1.2 px orange stroke for transient class-card hover
- `.active` toggles a white-ish stroke for the focused/hovered country
- Class-card click pattern: `applyFilter(cls)` writes `.dimmed` to non-matching regions + sets `aria-pressed` on cards + shows the filter badge bar
- Esc and the clear button both call `applyFilter(null)`

This API is identical in shape to the prior P3 cross-link mockups (`3-cross-linking/A-hover-highlight.html`, `B-click-filter.html`), so a Phase 2B integration into `findings.html` §3 needs no redesign — just port the SVG render block, the inline `CELL_MAP`, and reuse the existing class-card panel that already lives in §4.

**Tab order.** Country regions tab geographically L→R, T→B by centroid binned into row-bands of 3. 36 country tab stops + view-toggle + clear-btn + 4 class cards = 42 total focusable elements.

**View toggle.** Inline iframe of `B-beeswarm.html` rather than embedded SVG copy — simpler and avoids state-loss (iframe persists across toggles). The iframe is `loading="lazy"` to avoid the initial fetch penalty.
