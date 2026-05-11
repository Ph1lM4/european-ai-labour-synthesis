"""
ESRA-style dot-map generator for Phase 2J corridor map redraw.

Replaces the rastered (square cell) map with circle-based rendering:
  - Web Mercator projection (lon/lat → x/y), restoring Nordic recognisability
    that the prior Lambert equal-area projection squashed.
  - Variable dot radius encoding outline fidelity (NOT data):
      * "full" dots for cells fully inside a country polygon (large)
      * "half"/"edge" dots for cells partially inside (smaller)
    This reproduces the ESRA-style coastline feathering Phil pinned.

Source data:
  Natural Earth 1:50m (CC0) — tools/data/ne_50m_admin_0_countries.geojson
  download URL: https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson

Country centroids (LU/LI/MT force-placed) come directly from Natural Earth
polygon centroids — NOT a separate hardcoded table — so BR-19 fabrication
discipline holds (no second-source synthesis).

Usage: python3 tools/dotmap-gen.py
  → writes site/dotmap-data.json (geometry consumed by findings.html)
  → also embedded into the standalone Nexalps export in
    site/exports/corridor-map-nexalps.svg via dotmap-export.py
"""
import json
import math
from pathlib import Path

from shapely.geometry import Point, shape
from shapely.ops import unary_union
from shapely.prepared import prep

# ---------- Geographic bounds + grid ----------

LON_MIN, LON_MAX = -25.0, 45.0  # Iceland → Eastern Turkey
LAT_MIN, LAT_MAX = 34.0, 72.0   # Cyprus → North Cape

# Dot grid resolution. Higher than rastered map (96×68 → 1938 cells) to
# support variable-radius edge feathering.
#
# ROWS is computed from COLS so the canvas matches true Web Mercator
# aspect ratio at this latitude range (otherwise countries below the
# Nordics get visually squashed because pixels-per-radian on the y axis
# diverges from the x axis). Aspect ratio = mercator_y_span / lon_span,
# evaluated at LAT_MIN/LAT_MAX/LON_MIN/LON_MAX below.
COLS = 140

# Pixel geometry (post-projection canvas size).
CELL_PX = 7
GAP_PX = 1
PITCH = CELL_PX + GAP_PX
MARGIN_PX = 8

# Compute ROWS so the canvas inner area is true-Mercator (square pitch
# in projected radians). lat_span and lon_span are in radians; ROWS is
# the smallest grid count that fits the required inner height at PITCH.
_LON_SPAN_RAD = math.radians(LON_MAX - LON_MIN)
_LAT_SPAN_MERC = math.log(math.tan(math.pi/4 + math.radians(LAT_MAX)/2)) - \
                 math.log(math.tan(math.pi/4 + math.radians(LAT_MIN)/2))
_ASPECT = _LAT_SPAN_MERC / _LON_SPAN_RAD  # height/width
_INNER_W = COLS * PITCH - GAP_PX
_INNER_H_TARGET = _INNER_W * _ASPECT
ROWS = int(round((_INNER_H_TARGET + GAP_PX) / PITCH))

CANVAS_W = COLS * PITCH - GAP_PX + 2 * MARGIN_PX
CANVAS_H = ROWS * PITCH - GAP_PX + 2 * MARGIN_PX

# Dot radii. Variance is for outline fidelity, not data.
R_FULL = 3.4
R_EDGE = 1.7

# ---------- ISO code mapping ----------

EUROSTAT_TO_ISO2 = {"EL": "GR", "UK": "GB"}
ISO2_TO_EUROSTAT = {v: k for k, v in EUROSTAT_TO_ISO2.items()}

TARGETS = ["AT","BA","BE","BG","CH","CY","CZ","DE","DK","EE","EL","ES","FI",
           "FR","HR","HU","IE","IS","IT","LI","LT","LU","LV","MK","MT","NL",
           "NO","PL","PT","RO","RS","SE","SI","SK","TR","UK"]
UKRAINE = "UA"  # Class IV reference panel; rendered separately
NEEDED_ISO2 = {EUROSTAT_TO_ISO2.get(c, c) for c in TARGETS} | {UKRAINE}

# Microstate fallback centroids (lon, lat) — used only when polygon
# sampling produces zero dots at this grid resolution.
MICROSTATE_FORCE = {
    "LI": (9.55, 47.16),
    "MT": (14.45, 35.90),
}

# ---------- Web Mercator projection ----------

def mercator_y(lat):
    """Standard Web Mercator y (in radians-equivalent units, unscaled).
    Clamp lat to (-85.05, 85.05) but our range is well inside that."""
    return math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))

_MY_MIN = mercator_y(LAT_MIN)
_MY_MAX = mercator_y(LAT_MAX)

def project(lon, lat):
    """Return canvas (x_px, y_px) for a (lon, lat) point.

    Bounding box (LON_MIN..LON_MAX, LAT_MIN..LAT_MAX) maps onto the inner
    canvas (excluding margin). y axis is flipped (north → low y)."""
    fx = (lon - LON_MIN) / (LON_MAX - LON_MIN)
    fy = 1.0 - (mercator_y(lat) - _MY_MIN) / (_MY_MAX - _MY_MIN)
    inner_w = CANVAS_W - 2 * MARGIN_PX
    inner_h = CANVAS_H - 2 * MARGIN_PX
    return MARGIN_PX + fx * inner_w, MARGIN_PX + fy * inner_h

def unproject_to_lonlat(col, row):
    """Cell (col, row) center → geographic (lon, lat).
    Inverse of the projection at cell-center positions, used for
    point-in-polygon sampling."""
    # Cell center in canvas coords.
    x_px = MARGIN_PX + (col + 0.5) * PITCH - PITCH / 2 + CELL_PX / 2
    y_px = MARGIN_PX + (row + 0.5) * PITCH - PITCH / 2 + CELL_PX / 2
    inner_w = CANVAS_W - 2 * MARGIN_PX
    inner_h = CANVAS_H - 2 * MARGIN_PX
    fx = (x_px - MARGIN_PX) / inner_w
    fy = 1.0 - (y_px - MARGIN_PX) / inner_h  # flip y
    lon = LON_MIN + fx * (LON_MAX - LON_MIN)
    my = _MY_MIN + fy * (_MY_MAX - _MY_MIN)
    lat = math.degrees(2 * math.atan(math.exp(my)) - math.pi / 2)
    return lon, lat

def cell_center_px(col, row):
    """Canvas pixel coordinates of cell (col, row) center."""
    x = MARGIN_PX + col * PITCH + CELL_PX / 2
    y = MARGIN_PX + row * PITCH + CELL_PX / 2
    return x, y

def cell_lonlat(col, row):
    """Cell-center geographic coordinates (matches cell_center_px)."""
    inner_w = CANVAS_W - 2 * MARGIN_PX
    inner_h = CANVAS_H - 2 * MARGIN_PX
    x_px, y_px = cell_center_px(col, row)
    fx = (x_px - MARGIN_PX) / inner_w
    fy = 1.0 - (y_px - MARGIN_PX) / inner_h
    lon = LON_MIN + fx * (LON_MAX - LON_MIN)
    my = _MY_MIN + fy * (_MY_MAX - _MY_MIN)
    lat = math.degrees(2 * math.atan(math.exp(my)) - math.pi / 2)
    return lon, lat

# ---------- Load Natural Earth ----------

def _extract_crimea(ru_geom):
    """Return the RU MultiPolygon sub-component covering the Crimean
    peninsula. Identified as the sub-polygon containing Simferopol
    (34.10°E, 44.95°N), the administrative centre of Crimea.

    Natural Earth's current master assigns Crimea to RU's geometry; UN
    GA Resolution 68/262 (March 2014) affirms Ukraine's territorial
    integrity over Crimea, so this dot-map renders Crimea under UA.
    The Crimea coordinates come from the same NE source file — no
    fabricated polygon."""
    simferopol = Point(34.10, 44.95)
    for poly in ru_geom.geoms:
        if poly.contains(simferopol):
            return poly
    raise SystemExit("Crimea sub-polygon not found in RU geometry")


def load_geometries():
    path = Path(__file__).parent / "data" / "ne_50m_admin_0_countries.geojson"
    with path.open() as f:
        gj = json.load(f)
    geoms = {}
    ua_geom = None
    crimea_geom = None
    for feat in gj["features"]:
        p = feat["properties"]
        iso2 = p.get("ISO_A2_EH") or p.get("ISO_A2")
        if iso2 == "RU":
            crimea_geom = _extract_crimea(shape(feat["geometry"]))
            continue
        if iso2 in NEEDED_ISO2:
            eurostat = ISO2_TO_EUROSTAT.get(iso2, iso2)
            geom = shape(feat["geometry"])
            if eurostat == UKRAINE:
                ua_geom = geom
            else:
                geoms[eurostat] = (geom, prep(geom))
    if ua_geom is None:
        raise SystemExit("UA geometry not found")
    if crimea_geom is None:
        raise SystemExit("RU geometry not found (needed for Crimea extraction)")
    ua_with_crimea = unary_union([ua_geom, crimea_geom])
    geoms[UKRAINE] = (ua_with_crimea, prep(ua_with_crimea))
    expected = set(TARGETS) | {UKRAINE}
    missing = expected - set(geoms)
    if missing:
        raise SystemExit(f"Missing geometries: {missing}")
    return geoms

# ---------- Dot assignment ----------

def classify_cell(lon, lat, geom_prep, geom):
    """Sample 5 sub-points (center + 4 quarter offsets) at a cell.
    Returns (in_count, total) where total=5.

    in_count == 5 → "full" dot (large), 1..4 → "edge" (small),
    0 → not in country."""
    half = 0.5  # cell extent in degrees, scaled by sub-offset
    # Sub-point offsets in canvas-px space, projected back to lon/lat.
    offsets_px = [
        (0, 0),
        (-CELL_PX / 3, -CELL_PX / 3),
        (CELL_PX / 3, -CELL_PX / 3),
        (-CELL_PX / 3, CELL_PX / 3),
        (CELL_PX / 3, CELL_PX / 3),
    ]
    inner_w = CANVAS_W - 2 * MARGIN_PX
    inner_h = CANVAS_H - 2 * MARGIN_PX
    # Project center to canvas px first.
    cx_px, cy_px = project(lon, lat)
    inside = 0
    for dx, dy in offsets_px:
        x_px = cx_px + dx
        y_px = cy_px + dy
        fx = (x_px - MARGIN_PX) / inner_w
        fy = 1.0 - (y_px - MARGIN_PX) / inner_h
        slo = LON_MIN + fx * (LON_MAX - LON_MIN)
        smy = _MY_MIN + fy * (_MY_MAX - _MY_MIN)
        slat = math.degrees(2 * math.atan(math.exp(smy)) - math.pi / 2)
        if geom_prep.contains(Point(slo, slat)):
            inside += 1
    return inside

def assign_dots(geoms):
    """For each cell, find which country's polygon it sits in (most
    sub-samples in). Returns {code: [(col, row, fullness), ...]}."""
    dots = {code: [] for code in (TARGETS + [UKRAINE])}
    # Iterate cells, find best country.
    for col in range(COLS):
        for row in range(ROWS):
            lon, lat = cell_lonlat(col, row)
            best_code = None
            best_fill = 0
            for code, (geom, prep_geom) in geoms.items():
                # Quick reject via bounds.
                minx, miny, maxx, maxy = geom.bounds
                if not (minx - 0.3 <= lon <= maxx + 0.3 and miny - 0.3 <= lat <= maxy + 0.3):
                    continue
                fill = classify_cell(lon, lat, prep_geom, geom)
                if fill > best_fill:
                    best_fill = fill
                    best_code = code
                    if fill == 5:
                        break
            if best_code and best_fill > 0:
                dots[best_code].append((col, row, best_fill))
    return dots

def force_microstates(dots, geoms):
    """For any country with 0 dots, force-place 1 dot at fallback centroid."""
    for code, (lon, lat) in MICROSTATE_FORCE.items():
        if not dots[code]:
            x_px, y_px = project(lon, lat)
            col = int((x_px - MARGIN_PX) / PITCH)
            row = int((y_px - MARGIN_PX) / PITCH)
            col = max(0, min(COLS - 1, col))
            row = max(0, min(ROWS - 1, row))
            # Steal the cell from another country if needed.
            for other in dots:
                if other == code:
                    continue
                dots[other] = [(c, r, f) for (c, r, f) in dots[other] if (c, r) != (col, row)]
            dots[code].append((col, row, 5))
    return dots

# ---------- Output ----------

def cell_to_xy(col, row):
    """Cell index → SVG cx/cy (center of dot)."""
    cx, cy = cell_center_px(col, row)
    return round(cx, 2), round(cy, 2)

# ---------- Polygon hit-area paths ----------

# Simplification tolerance in degrees (~5 km at this latitude). Hit-area
# precision needs only ~1 px on the ~1135 px canvas; this collapses
# Natural Earth 1:50m vertex counts roughly 5-10x with no visible loss.
SIMPLIFY_TOL_DEG = 0.05

def _ring_to_subpath(coords):
    """Project a closed ring (lon,lat tuples) to an SVG 'M x,y L x,y Z' subpath."""
    pts = []
    for lon, lat in coords:
        x, y = project(lon, lat)
        pts.append(f"{round(x,1)},{round(y,1)}")
    if not pts:
        return ""
    return "M" + pts[0] + "L" + "L".join(pts[1:]) + "Z"

def polygon_to_path(geom):
    """Project a (Multi)Polygon to a compound SVG 'd' string covering all
    exterior rings. Holes are dropped — hit-area is filled, not stroked,
    and pointer-events on a polygon with holes still capture the whole
    enclosing shape under fill='transparent' + pointer-events='all'."""
    simplified = geom.simplify(SIMPLIFY_TOL_DEG, preserve_topology=True)
    parts = []
    if simplified.geom_type == "Polygon":
        polys = [simplified]
    elif simplified.geom_type == "MultiPolygon":
        polys = list(simplified.geoms)
    else:
        return ""
    for poly in polys:
        if poly.is_empty:
            continue
        ring = list(poly.exterior.coords)
        sub = _ring_to_subpath(ring)
        if sub:
            parts.append(sub)
    return "".join(parts)

def polygon_area_px(geom):
    """Approximate projected area in pixel² for paint-order sort.
    Uses bounding-box of the projected polygon as a cheap proxy."""
    minx, miny, maxx, maxy = geom.bounds
    x1, y1 = project(minx, miny)
    x2, y2 = project(maxx, maxy)
    return abs((x2 - x1) * (y2 - y1))

def build_output(dots, geoms):
    countries = {}
    polygons = {}
    for code, cells in dots.items():
        out_dots = []
        for (col, row, fullness) in sorted(cells):
            cx, cy = cell_to_xy(col, row)
            r = R_FULL if fullness >= 4 else R_EDGE
            # Encode fullness for runtime if needed: 'f' or 'e'.
            kind = "f" if fullness >= 4 else "e"
            out_dots.append([cx, cy, r, kind])
        countries[code] = out_dots
        if code in geoms:
            geom, _ = geoms[code]
            polygons[code] = {
                "path": polygon_to_path(geom),
                "area_px": round(polygon_area_px(geom), 1),
            }
    return {
        "_provenance": {
            "source": "Natural Earth 1:50m admin_0_countries.geojson (CC0)",
            "url": "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson",
            "projection": "Web Mercator (EPSG:3857) clipped to lon[-25,45] lat[34,72]",
            "grid": f"{COLS}×{ROWS} cells, pitch {PITCH}px, cell {CELL_PX}px",
            "radii": {"full": R_FULL, "edge": R_EDGE},
            "canvas": [CANVAS_W, CANVAS_H],
            "fullness_threshold": "5-sample sub-grid; ≥4 in-polygon → 'f' (R={}px), 1..3 → 'e' (R={}px), 0 → omitted".format(R_FULL, R_EDGE),
            "microstate_fallback_centroids": MICROSTATE_FORCE,
            "polygons": (
                f"per-country projected SVG paths for hit-area overlays; "
                f"simplified at {SIMPLIFY_TOL_DEG}° tolerance; holes dropped; "
                f"area_px (projected bbox) is a paint-order sort key — render largest first so microstates stack on top."
            ),
        },
        "canvas": {"width": CANVAS_W, "height": CANVAS_H},
        "countries": countries,
        "polygons": polygons,
    }

def main():
    print(f"Loading Natural Earth, sampling {COLS}×{ROWS} grid via Web Mercator...")
    geoms = load_geometries()
    dots = assign_dots(geoms)
    dots = force_microstates(dots, geoms)

    total = sum(len(v) for v in dots.values())
    by_country = sorted(((code, len(v)) for code, v in dots.items()), key=lambda kv: -kv[1])
    print()
    print(f"Canvas: {CANVAS_W} × {CANVAS_H} px")
    print(f"Total dots: {total}")
    print(f"Microstates ≤ 3 dots:")
    for code, n in by_country:
        if n <= 3:
            print(f"  {code}: {n}")
    print()
    print("Per-country counts (sorted desc):")
    for code, n in by_country:
        print(f"  {code:3} {n:>5}")

    out = build_output(dots, geoms)
    out_path = Path(__file__).parent.parent / "site" / "dotmap-data.json"
    with out_path.open("w") as f:
        json.dump(out, f, separators=(",", ":"))
    size = out_path.stat().st_size
    print(f"\nWritten {out_path} ({size:,} bytes)")

if __name__ == "__main__":
    main()
