"""
Rastered-Europe cellMap generator for D-rastered.html (Bundle O Phase 2A.2 v5).

Samples real country polygons from Natural Earth 1:50m (CC0) via point-in-
polygon ray-casting on a Lambert cylindrical equal-area cell grid.

v5 (2026-05-06): switched from equirectangular to Lambert cylindrical
equal-area for the row mapping. Equirectangular over-allocated northern
countries (IS, FI, SE, NO, EE all +30-130% above proportional) because
each cell at high latitude covers less real surface area than an equator
cell. Equal-area projection makes each row represent the same surface
area, restoring proportional cell counts at the cost of a slight vertical
squash for Nordic shapes.

v5 also adds:
  - widen_english_channel(): post-process pass that trims UK eastern-edge
    cells in the Kent/Dover area so the visual gap to BE/FR/NL is ≥ 4 cols.
  - Cyprus 2-cell floor (was 1).

Why 1:50m, not 1:110m: 1:110m drops Greek archipelago cells, Croatian coast
detail, and Sicily/Sardinia separation. 1:50m gives faithful per-country
shape at our 96×68 grid (~0.73° × 0.43° cell, equal-area).

Source data: tools/data/ne_50m_admin_0_countries.geojson
  download URL: https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson
  license: CC0 (public domain)
  not committed: see .gitignore — re-download via the URL above

Usage: `python3 tools/cellmap-gen.py` -> writes /tmp/cellmap.json + prints
ASCII map, per-country counts, sea-gap diagnostics, area proportionality.
"""
import json
import math
from pathlib import Path

# Grid bounds. Covers Iceland → Turkey, Norway → Cyprus.
LON_MIN, LON_MAX = -25.0, 45.0
LAT_MIN, LAT_MAX = 34.0, 72.0
COLS, ROWS = 96, 68

# Pre-compute equal-area projection constants. Each row represents the
# same surface area (∝ Δsin(lat)).
_SIN_MAX = math.sin(math.radians(LAT_MAX))
_SIN_MIN = math.sin(math.radians(LAT_MIN))

# Eurostat code → ISO-A2 (used in Natural Earth ISO_A2_EH field).
EUROSTAT_TO_ISO2 = {"EL": "GR", "UK": "GB"}
ISO2_TO_EUROSTAT = {v: k for k, v in EUROSTAT_TO_ISO2.items()}

TARGETS = ["AT","BA","BE","BG","CH","CY","CZ","DE","DK","EE","EL","ES","FI",
           "FR","HR","HU","IE","IS","IT","LI","LT","LU","LV","MK","MT","NL",
           "NO","PL","PT","RO","RS","SE","SI","SK","TR","UK"]
NEEDED_ISO2 = {EUROSTAT_TO_ISO2.get(c, c) for c in TARGETS}

CLS = {
    "AT":"II","BA":"II","BE":"I","BG":"II","CH":"II","CY":"III","CZ":"III",
    "DE":"II","DK":"I","EE":"III","EL":"III","ES":"II","FI":"I","FR":"I",
    "HR":"III","HU":"III","IE":"III","IS":"I","IT":"III","LI":"II","LT":"III",
    "LU":"I","LV":"II","MK":"IV","MT":"III","NL":"I","NO":"I","PL":"III",
    "PT":"III","RO":"II","RS":"IV","SE":"I","SI":"III","SK":"III","TR":"IV","UK":"III",
}

# Approx land area km² — used to verify proportionality.
AREA_KM2 = {
    "TR":783562, "FR":643801, "ES":505990, "SE":450295, "DE":357022,
    "NO":385207, "FI":338424, "PL":312696, "IT":301340, "UK":243610,
    "RO":238397, "IS":103000, "EL":131957, "BG":110879, "PT":92090,
    "HU":93028, "BA":51197, "AT":83879, "CZ":78865, "IE":70273,
    "LV":64589, "LT":65300, "EE":45227, "DK":42933, "NL":41850,
    "CH":41285, "BE":30528, "MK":25713, "RS":88361, "SK":49035,
    "SI":20273, "HR":56594, "CY":9251, "LU":2586, "MT":316, "LI":160,
}

# Microstates that may end up with 0 cells at this resolution → force-assign
# at centroid (lon, lat). Assigned even if natural sampling gives 0.
MICROSTATE_CENTROIDS = {
    "LU": (6.13, 49.82),
    "LI": (9.55, 47.16),
    "MT": (14.45, 35.90),
    "CY": (33.43, 35.13),  # CY centroid — may already get cells
    "SI": (14.99, 46.15),  # likely gets cells naturally; here as safety
    "AT": (14.55, 47.52),  # safety
}

# ---------- Point-in-polygon (ray casting) ----------

def point_in_ring(x, y, ring):
    """Standard ray-casting. ring is list of [lon, lat] pairs (closed)."""
    inside = False
    n = len(ring)
    j = n - 1
    for i in range(n):
        xi, yi = ring[i][0], ring[i][1]
        xj, yj = ring[j][0], ring[j][1]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi):
            inside = not inside
        j = i
    return inside

def point_in_polygon(x, y, polygon):
    """polygon = [outer_ring, hole1, hole2, ...]. Inside outer minus holes."""
    if not point_in_ring(x, y, polygon[0]):
        return False
    for hole in polygon[1:]:
        if point_in_ring(x, y, hole):
            return False
    return True

def point_in_geometry(x, y, geom):
    """Handle Polygon and MultiPolygon."""
    t = geom["type"]
    if t == "Polygon":
        return point_in_polygon(x, y, geom["coordinates"])
    if t == "MultiPolygon":
        for poly in geom["coordinates"]:
            if point_in_polygon(x, y, poly):
                return True
        return False
    return False

def bbox_of(geom):
    """Compute lon/lat bbox to short-circuit point-in-poly."""
    coords = []
    if geom["type"] == "Polygon":
        for ring in geom["coordinates"]:
            coords.extend(ring)
    elif geom["type"] == "MultiPolygon":
        for poly in geom["coordinates"]:
            for ring in poly:
                coords.extend(ring)
    xs = [c[0] for c in coords]
    ys = [c[1] for c in coords]
    return (min(xs), min(ys), max(xs), max(ys))

# ---------- Load + filter Natural Earth ----------

def load_geometries():
    path = Path(__file__).parent / "data" / "ne_50m_admin_0_countries.geojson"
    with path.open() as f:
        gj = json.load(f)
    geoms = {}
    for feat in gj["features"]:
        p = feat["properties"]
        iso2 = p.get("ISO_A2_EH") or p.get("ISO_A2")
        if iso2 in NEEDED_ISO2:
            eurostat = ISO2_TO_EUROSTAT.get(iso2, iso2)
            geoms[eurostat] = (feat["geometry"], bbox_of(feat["geometry"]))
    missing = set(TARGETS) - set(geoms)
    if missing:
        raise SystemExit(f"Missing geometries: {missing}")
    return geoms

# ---------- Sample grid ----------

def cell_lonlat(col, row):
    """Lambert cylindrical equal-area: rows are linear in sin(lat).
    Each row represents the same surface-area band on the globe.
    Lon is still equirectangular (no longitude distortion at this scope).
    """
    lon = LON_MIN + (col + 0.5) / COLS * (LON_MAX - LON_MIN)
    sin_lat = _SIN_MAX - (row + 0.5) / ROWS * (_SIN_MAX - _SIN_MIN)
    lat = math.degrees(math.asin(sin_lat))
    return lon, lat

def lonlat_to_cell(lon, lat):
    """Inverse of cell_lonlat — used for microstate forced placement."""
    col = int((lon - LON_MIN) / (LON_MAX - LON_MIN) * COLS)
    sin_lat = math.sin(math.radians(lat))
    row = int((_SIN_MAX - sin_lat) / (_SIN_MAX - _SIN_MIN) * ROWS)
    col = max(0, min(COLS - 1, col))
    row = max(0, min(ROWS - 1, row))
    return col, row

def assign(geoms):
    cellmap = {code: [] for code in TARGETS}
    for col in range(COLS):
        for row in range(ROWS):
            lon, lat = cell_lonlat(col, row)
            for code, (geom, bbox) in geoms.items():
                if not (bbox[0] <= lon <= bbox[2] and bbox[1] <= lat <= bbox[3]):
                    continue
                if point_in_geometry(lon, lat, geom):
                    cellmap[code].append((col, row))
                    break
    return cellmap

def force_microstates(cellmap):
    """For any country with 0 cells, force-assign 1 cell at its centroid.
    CY gets a 2-cell floor (was 1) since at 96×68 grid CY's island maps to
    a single cell which is too small relative to its 9k km² area.
    """
    for code, (lon, lat) in MICROSTATE_CENTROIDS.items():
        if not cellmap[code]:
            col, row = lonlat_to_cell(lon, lat)
            for other in cellmap:
                if other != code and (col, row) in cellmap[other]:
                    cellmap[other].remove((col, row))
            cellmap[code].append((col, row))
    # CY-specific: ensure ≥ 2 cells. Add a horizontal neighbour.
    if len(cellmap["CY"]) < 2:
        col, row = cellmap["CY"][0]
        for dc in (1, -1):
            cand = (col + dc, row)
            if 0 <= cand[0] < COLS and not any(cand in cellmap[k] for k in cellmap):
                cellmap["CY"].append(cand)
                break
    return cellmap

def widen_english_channel(cellmap, min_gap=4):
    """Trim UK eastern-edge cells in rows where UK ↔ {BE, FR, NL} gap < min_gap.
    Only applies south of lat ~55 N (Scotland is too far north for any
    continental neighbour to define a gap).
    """
    # Equal-area row for lat 55 N (north of Newcastle)
    lat55_row = int((_SIN_MAX - math.sin(math.radians(55))) / (_SIN_MAX - _SIN_MIN) * ROWS)
    cont_cells = set()
    for k in ("BE", "FR", "NL"):
        cont_cells |= set(cellmap[k])
    cont_by_row = {}
    for (c, r) in cont_cells:
        cont_by_row.setdefault(r, []).append(c)

    uk = list(cellmap["UK"])
    rows = sorted({r for (_, r) in uk if r >= lat55_row})
    trimmed = 0
    for r in rows:
        cols_in_row = sorted(c for (c, rr) in uk if rr == r)
        if not cols_in_row or r not in cont_by_row:
            continue
        cont_min = min(cont_by_row[r])
        # Trim from the east until gap >= min_gap
        while cols_in_row and (cont_min - cols_in_row[-1] - 1) < min_gap:
            uk.remove((cols_in_row[-1], r))
            cols_in_row.pop()
            trimmed += 1
    cellmap["UK"] = uk
    return trimmed

# ---------- Diagnostics ----------

def render_ascii(cellmap):
    grid = [["." for _ in range(COLS)] for _ in range(ROWS)]
    for code, cells in cellmap.items():
        for (col, row) in cells:
            grid[row][col] = code[:1]
    print("    " + "".join(f"{c%10}" for c in range(COLS)))
    for r, row in enumerate(grid):
        print(f"{r:2}  " + "".join(row))

def check_seas(cellmap):
    """Per-row gap between (UK east) ↔ (NL/DE/DK west) and (SE east) ↔ Baltics west."""
    def min_gap_per_row(set_a, set_b):
        rows_a = {r for (_, r) in set_a}
        rows_b = {r for (_, r) in set_b}
        common = rows_a & rows_b
        if not common:
            return 99
        return min(
            min(c for (c, rr) in set_b if rr == r)
            - max(c for (c, rr) in set_a if rr == r)
            - 1
            for r in common
        )
    uk = set(cellmap["UK"])
    cont = set().union(*(set(cellmap[k]) for k in ("NL", "DE", "DK", "BE")))
    se = set(cellmap["SE"])
    balt = set().union(*(set(cellmap[k]) for k in ("EE", "LV", "LT")))
    return min_gap_per_row(uk, cont), min_gap_per_row(se, balt)

def proportionality_report(cellmap, total):
    """Compute cells/1000km² per country and z-score vs the median ratio."""
    ratios = {code: len(cells) / (AREA_KM2[code] / 1000)
              for code, cells in cellmap.items() if len(cells) > 0}
    sorted_ratios = sorted(ratios.values())
    median = sorted_ratios[len(sorted_ratios)//2]
    rows = []
    for code in sorted(TARGETS):
        n = len(cellmap[code])
        area = AREA_KM2[code]
        ratio = n / (area / 1000) if area else 0
        deviation = (ratio - median) / median * 100 if median else 0
        flag = "" if abs(deviation) <= 25 else (" ⚠" if abs(deviation) <= 50 else " ⚠⚠")
        rows.append((code, n, area, ratio, deviation, flag))
    return median, rows

# ---------- Main ----------

if __name__ == "__main__":
    print(f"Loading Natural Earth 1:50m, sampling {COLS}×{ROWS} grid...")
    geoms = load_geometries()
    cellmap = assign(geoms)
    cellmap = force_microstates(cellmap)
    trimmed = widen_english_channel(cellmap, min_gap=4)
    print(f"English Channel widening: trimmed {trimmed} UK cells in Kent/SE England")

    total = sum(len(v) for v in cellmap.values())
    empty = [c for c, v in cellmap.items() if not v]

    print()
    render_ascii(cellmap)
    print()
    print(f"Total cells: {total}")
    print(f"Empty countries: {empty}")
    ns, bs = check_seas(cellmap)
    print(f"North Sea gap (UK ↔ NL/DE/DK/BE): {ns} cols (target ≥ 4)")
    print(f"Baltic Sea gap (SE ↔ EE/LV/LT): {bs} cols (target ≥ 3)")

    print("\nPer-country counts (sorted by cells desc):")
    for code, cells in sorted(cellmap.items(), key=lambda kv: -len(kv[1])):
        print(f"  {code}: {len(cells):>4} cells   class {CLS[code]:<3}   area {AREA_KM2[code]:>7,} km²")

    print("\nProportionality vs median cells/1000km²:")
    median, rows = proportionality_report(cellmap, total)
    print(f"  Median ratio: {median:.4f} cells/km²")
    print(f"  {'code':<5} {'cells':>6} {'area':>9} {'ratio':>7} {'dev_%':>7}  flag")
    for code, n, area, ratio, dev, flag in rows:
        print(f"  {code:<5} {n:>6} {area:>9,} {ratio:>7.4f} {dev:>+7.1f}{flag}")

    out = {code: [list(p) for p in sorted(cellmap[code])] for code in sorted(cellmap)}
    js = json.dumps(out, separators=(',', ':'))
    print(f"\nJSON byte size: {len(js)} (target ≤ 30720)")
    with open("/tmp/cellmap.json", "w") as f:
        f.write(js)
    print("Written /tmp/cellmap.json")
