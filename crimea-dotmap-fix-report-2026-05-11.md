# Crimea Dot-Map Fix — Report

**Date:** 2026-05-11
**Files touched:** `tools/dotmap-gen.py`, `site/dotmap-data.json`, `site/exports/corridor-map-nexalps.svg`, `site/exports/corridor-map-nexalps.png`
**Framing:** UN GA Resolution 68/262 (March 2014) affirms Ukraine's territorial integrity. The dot-map now renders Crimea as part of UA's polygon.

---

## Approach Chosen

**Programmatic merge from the existing Natural Earth source.** No external download.

Discovery: `tools/data/ne_50m_admin_0_countries.geojson` (Natural Earth 1:50m, CC0) assigns Crimea to RU. RU's geometry is a 101-component `MultiPolygon`; component **`poly[100]`** is the Crimea peninsula as a discrete sub-polygon (bbox `(32.51, 44.39, 36.58, 46.22)`, area ≈ 3.10 sq°). Confirmed by point-in-polygon test: Simferopol (34.10°E, 44.95°N), Sevastopol, Yalta, Kerch all return `True` against this sub-polygon and `False` against every UA component.

Implementation in `tools/dotmap-gen.py`:

1. New `_extract_crimea(ru_geom)` helper isolates the RU sub-polygon that contains the Simferopol reference point.
2. `load_geometries()` reads RU alongside UA, extracts Crimea, and runs `shapely.ops.unary_union([ua_geom, crimea_geom])` to produce the merged UA geometry before `prep()`.
3. The merged geometry flows unchanged through `simplify`, `polygon_to_path`, `assign_dots`, and the JSON build — no other code paths modified.

Why this over re-sourcing an older NE release: the Crimea polygon comes from the same checked-in source file (no new dataset, no version-drift risk, no extra moving parts). The Simferopol reference point is a stable, published-coordinate anchor — BR-19 holds (no hand-drawn polygon).

---

## Before / After — UA Geometry

| Metric | Before | After |
|---|---|---|
| UA polygon subpaths | 2 | 2 |
| Subpath 0 (mainland UA) point count | 174 | 186 |
| Subpath 0 x-extent (px) | 761.4 .. 1048.8 | 761.4 .. 1048.8 |
| Subpath 0 y-extent (px) | **711.4 .. 884.6** | **711.4 .. 902.9** |
| Subpath 1 (Zmiinyi/Snake Island) | 5 pts, x 911.3..921.6, y 858.4..863.5 | 5 pts, x 911.3..921.6, y 858.4..863.5 (preserved) |
| UA dot count | 466 | **487** (+21, the Crimea cluster) |
| UA `area_px` (paint-order sort key) | 51,793.4 | 55,392.3 |

**Why y-max landed at 902.9 (not "south of ~920" as the brief hinted):** Cape Sarych — Crimea's southernmost point at 33.78°E, 44.39°N — projects under this Web Mercator configuration to `(947.6, 903.7)` px. The new UA y-max of 902.9 matches Cape Sarych within simplification tolerance (`SIMPLIFY_TOL_DEG = 0.05°`). RO's y-max of 919.7 corresponds to the Danube delta at ~43.6°N, which is geographically further south than Crimea's southernmost cape — so UA correctly does NOT extend below RO, even though both now reach the Black Sea coast.

---

## Schema & Diff Integrity

- `site/dotmap-data.json` schema preserved: `_provenance` / `canvas` / `countries` / `polygons` keys unchanged.
- Canvas dimensions unchanged: `1135 × 1127 px`.
- Country count: 37 (unchanged).
- Polygon count: 37 (unchanged).
- Subpath 1 (5-point Snake Island at x≈916, y≈861) preserved bit-identical — `unary_union` left it as a distinct MultiPolygon component because it has no shared boundary with mainland UA.

### MD5 confirmation — only UA changed

Per-polygon `md5` of the `path` field, before vs after. 36 of 37 hashes are identical; UA is the only delta.

```
diff before vs after:
36c36
< UA  066b1f6516a2ad065913268c99abcb31   (before)
---
> UA  75a0240ab227a32a1bd9a82dea938757   (after)
```

All other 36 polygon paths byte-identical.

---

## Browser Render Confirmation

Loaded `http://localhost:3006/findings.html` in the preview harness. Dot-map SVG renders 37 country groups via `[data-code]`. UA group inspection:

| Property | Value |
|---|---|
| `aria-label` | `Ukraine, UA. Class IV. 487 dots.` |
| `<circle>` count inside UA group | 487 |
| Dot x-range | 771.5 .. 1043.5 |
| Dot y-range | 715.5 .. 899.5 |
| Dots with y > 890 (Crimea region) | 8 |
| Dots with y > 895 (southern Crimea) | 2 |

Visual: the screenshot shows a clearly-shaped Crimean peninsula in Class IV dark-red (granite-gray dimmed to reduced opacity per the geo-note) attached to UA's southern coast, between the Sea of Azov bulge and the Black Sea. Reduced-opacity Class IV styling preserved.

**Screenshot reference:** captured in-session via `preview_screenshot` against `findings.html` on `localhost:3006`. The bottom-right of UA's coloured-dot cluster now contains the Crimea protrusion; pre-fix the cluster terminated at the Sea of Azov coast.

---

## Files Modified

- `tools/dotmap-gen.py` — added `from shapely.ops import unary_union`; added `_extract_crimea` helper; modified `load_geometries` to merge Crimea into UA before `prep()`. ~25 lines added.
- `site/dotmap-data.json` — regenerated (193,166 bytes; UA path + UA dot list changed; rest byte-identical).
- `site/exports/corridor-map-nexalps.svg` — regenerated from new JSON (247,647 bytes).
- `site/exports/corridor-map-nexalps.png` — regenerated (1,354,681 bytes).

`site/data.json` (SOT) **not touched** — UA's labour-market data remains the existing reference panel; this fix is geometric only.

---

## ⚠️ Code Review Summary (code-craft rubric)

- **Names:** pass — `_extract_crimea`, `ua_geom`, `crimea_geom`, `ua_with_crimea` are full-word and intent-naming; underscore prefix on the helper signals module-private per existing module style.
- **Nesting depth:** max 2 levels in the modified function; early `continue` and explicit `raise SystemExit` for the two missing-source cases, matching the existing `missing → SystemExit` pattern.
- **Hidden dependencies / side effects:** none. `unary_union` is pure; `prep` is rebuilt for the merged geometry; no global state mutated.
- **Duplication:** none. Crimea extraction lives in one helper; the merge happens once at load time.
- **Local-style match:** matches existing module style (4-space, type-hint-free, `SystemExit` for invariants, comment density on rationale-bearing lines only).
- **Honest signatures:** `_extract_crimea` raises if Crimea sub-polygon not found; `load_geometries` raises if UA or RU missing. No silent fallback.
- **Things I chose NOT to add (YAGNI):** no CLI flag for "merge Crimea on/off", no fallback for older NE releases, no general-purpose disputed-territories merger, no automated detection of which RU sub-polygon is Crimea by area heuristic (the Simferopol point-in-polygon test is the cheapest and most legible identifier).
- **Uncertainty / assumptions a human should verify:**
  - The Simferopol coordinate (34.10°E, 44.95°N) is treated as a stable, published landmark; if NE ever splits Crimea into multiple sub-polygons (e.g., separating the Kerch peninsula), the current single-poly extraction would miss the additional piece. Currently a single contiguous sub-polygon in `ne_50m_admin_0_countries.geojson`.
  - The merge assumes UA mainland and Crimea share a common border along the Perekop isthmus in NE's geometry; the resulting `unary_union` produces a connected `Polygon` if so, else a `MultiPolygon`. Either case is handled correctly by the existing `polygon_to_path` function (Polygon vs MultiPolygon branch). Output ended up as MultiPolygon (Crimea + mainland came out as one component; Snake Island remained the second component).
  - Phil should re-render `findings.html` in his own browser to confirm the Crimean peninsula is visually unmistakable at his target viewing size.
