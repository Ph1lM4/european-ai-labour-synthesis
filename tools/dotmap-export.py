"""
Phase 2J — Nexalps PDF-target export.

Reads dotmap geometry + per-country fragility class, writes:
  site/exports/corridor-map-nexalps.svg  (standalone, Nexalps palette,
    pearl-white #F8F9FA, deep-teal C1 / alpine-gold C2 / alpine-red C3 /
    granite-gray C4, no labels, no interactivity)
  site/exports/corridor-map-nexalps.png  (2400 × ~1722 raster fallback;
    height computed to preserve aspect ratio of the SVG canvas)

Source data: tools/dotmap-gen.py output (site/dotmap-data.json) +
site/data.json (fragility_class per country).

UA Class IV reference panel rendered with the same fragility palette. All
labels / country codes deliberately omitted per Phase 2J lock #4.
"""
import json
import os
from pathlib import Path

ROOT = Path(__file__).parent.parent
SITE = ROOT / "site"
OUT_DIR = SITE / "exports"
OUT_DIR.mkdir(exist_ok=True)

# Nexalps palette (tailwind.config.ts, lines 23–39).
NEX = {
    "bg": "#F8F9FA",
    "C1": "#087569",  # deep-teal-text — Class I (Robust)
    "C2": "#F59E0B",  # alpine-gold — Class II (Fragile)
    "C3": "#C41E3A",  # alpine-red — Class III (Pre-Failure Risk)
    "C4": "#4A5568",  # granite-gray — Class IV (Active Cascade)
}
CLS_TO_NEX = {"I": "C1", "II": "C2", "III": "C3", "IV": "C4"}

# Ukraine is Class IV reference panel (data.json.ukraine_reference_panel).
UA_CLASS = "IV"


def load_inputs():
    dotmap = json.loads((SITE / "dotmap-data.json").read_text())
    data = json.loads((SITE / "data.json").read_text())
    cls = {code: c.get("fragility_class") for code, c in data["countries"].items()}
    cls["UA"] = UA_CLASS
    return dotmap, cls


def build_svg(dotmap, cls_map):
    canvas = dotmap["canvas"]
    W, H = canvas["width"], canvas["height"]
    parts = []
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" font-family="Geist, system-ui, -apple-system, sans-serif" '
        f'role="img" aria-label="Corridor map of 36 European labour markets plus Ukraine reference panel; dot colour encodes fragility class.">'
    )
    parts.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="{NEX["bg"]}"/>')
    parts.append("<style>")
    parts.append(".dot-c1{fill:" + NEX["C1"] + "}")
    parts.append(".dot-c2{fill:" + NEX["C2"] + "}")
    parts.append(".dot-c3{fill:" + NEX["C3"] + "}")
    parts.append(".dot-c4{fill:" + NEX["C4"] + "}")
    parts.append("</style>")

    for code in sorted(dotmap["countries"].keys()):
        dots = dotmap["countries"][code]
        if not dots:
            continue
        cls = cls_map.get(code)
        if not cls:
            continue
        nex = CLS_TO_NEX[cls]
        parts.append(
            f'<g class="country-region dot-{nex.lower()}" data-country="{code}" '
            f'data-corridor-class="{nex}" data-fragility-class="{cls}">'
        )
        for cx, cy, r, _kind in dots:
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}"/>')
        parts.append("</g>")

    parts.append("</svg>")
    return "".join(parts)


def render_png(svg_text, png_path, target_w=2400):
    # Set DYLD path so cairocffi finds homebrew cairo.
    cellar = "/opt/homebrew/Cellar/cairo"
    versions = sorted(os.listdir(cellar)) if os.path.isdir(cellar) else []
    if versions:
        os.environ.setdefault(
            "DYLD_LIBRARY_PATH",
            f"{cellar}/{versions[-1]}/lib:" + os.environ.get("DYLD_LIBRARY_PATH", ""),
        )
    import cairosvg  # local import after env

    cairosvg.svg2png(
        bytestring=svg_text.encode("utf-8"),
        write_to=str(png_path),
        output_width=target_w,
    )


def main():
    dotmap, cls_map = load_inputs()
    svg_text = build_svg(dotmap, cls_map)
    svg_path = OUT_DIR / "corridor-map-nexalps.svg"
    svg_path.write_text(svg_text)
    print(f"Written {svg_path} ({svg_path.stat().st_size:,} bytes)")

    png_path = OUT_DIR / "corridor-map-nexalps.png"
    render_png(svg_text, png_path, target_w=2400)
    print(f"Written {png_path} ({png_path.stat().st_size:,} bytes)")

    # Coverage check.
    countries_with_dots = sum(1 for v in dotmap["countries"].values() if v)
    countries_classed = sum(1 for code in dotmap["countries"] if cls_map.get(code))
    print(f"Coverage: {countries_with_dots} countries rendered, {countries_classed} classed")


if __name__ == "__main__":
    main()
