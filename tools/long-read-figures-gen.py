#!/usr/bin/env python3
"""Render the Long-Read figures as standalone PNGs.

Produces:
  site/exports/long-read/stack-bar-fragility-9-9-15-3-nexalps.png
  site/exports/long-read/reskilling-funnel-nexalps.png
  site/exports/long-read/corridor-columns-nexalps.png   (§2 lead-in)
  site/exports/long-read/scenario-heatmap-nexalps.png   (§5 lead-in)

All four PNGs are embedded into `docs/layer-6-deliverable-long-read.pdf` by
the Long-Read renderer. Corridor + scenario figures mirror Visual Read p3
(`page_corridors`) and p6 (`page_scenarios`) so the Long-Read carries the
same visual language at the same locked sizes; the stack-bar and
reskilling-funnel mirror Visual Read p4 + p5. Numbers are pulled from
`layer-6-deliverable-data.json` (SOT); reskilling-arithmetic constants are
mirrored from `tools/visual-read-pdf-gen.py`.

Architecture (per master decision): inline-copy the v4.1 design tokens and
the small set of canvas drawing helpers from `tools/visual-read-pdf-gen.py`.
A shared `tools/_pdf_style.py` extraction is a follow-up after the suite
stabilises. This script is the second consumer of those helpers; if a third
consumer appears, the shared module should land first.

Rendering pipeline:
  ReportLab canvas → single-page PDF (custom landscape page size, pearl-
  white background) → `pdftoppm -png -r 300` → PNG. We chose this over
  cairosvg (would require an SVG re-implementation of the canvas drawing)
  and `reportlab.graphics.renderPM` (requires `Drawing` objects, not the
  canvas helpers we're inlining). `pdftoppm` is already on the system
  (Homebrew poppler) and produces a clean rasterisation at 300 DPI.

Usage:
  python3 tools/long-read-figures-gen.py
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Shared style module — registers Geist fonts, sets rl_config.invariant=1,
# and exports the v4.1 palette + canvas helpers. Import before any other
# reportlab.* import so the deterministic-build flags are set in time.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _pdf_style import (
    HexColor, Color,
    PEARL_WHITE, PURE_BLACK, PURE_WHITE,
    DEEP_TEAL,
    GRANITE, GRANITE_DARK, GRANITE_LIGHT, GRANITE_LIGHTER,
    HAIRLINE,
    ALPINE_GOLD, ALPINE_RED, CLASS_IV_WINE,
    HEAT_1, HEAT_2, HEAT_3, HEAT_4, HEAT_5, HEAT_6,
    CLS_COLOR, CLS_LABEL,
    REGIME_LABELS, REGIME_ORDER,
    RADIUS_CARD, BAR_H, BAR_RADIUS,
    RESKILLING_COHORT_2035, TRAINING_THROUGHPUT_YR,
    BASELINE_ABSORBED_YR, NET_NEW_YR,
    heat_color, heat_text_color,
    _tracked_text, overline, wrap_lines, page_background,
    draw_paragraph, heading_h2, heading_lede,
    _round_rect_path, draw_card_accent,
    draw_pill, draw_pill_row,
    draw_segmented_bar, draw_simple_bar_row,
    draw_graphic_header, draw_graphic_caption, draw_class_legend,
)

from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas as canvasmod

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO = Path(__file__).resolve().parent.parent
SOT = REPO / "layer-6-deliverable-data.json"
OUT_DIR = REPO / "site" / "exports" / "long-read"
FIG_A_PNG = OUT_DIR / "stack-bar-fragility-9-9-15-3-nexalps.png"
FIG_B_PNG = OUT_DIR / "reskilling-funnel-nexalps.png"
FIG_C_PNG = OUT_DIR / "corridor-columns-nexalps.png"
FIG_D_PNG = OUT_DIR / "scenario-heatmap-nexalps.png"

# Page geometry for the standalone figure PDFs. Landscape near-A5 sizes that
# embed cleanly in the Long-Read at full content-column width. Heights are
# generous so we never clip the legend or caption.
FIG_A_W, FIG_A_H = 200 * mm, 60 * mm    # stack-bar figure (trimmed v4.2.x — content ~50 mm)
FIG_B_W, FIG_B_H = 200 * mm, 80 * mm    # reskilling funnel (trimmed from 110 — content occupies ~75 mm)
FIG_C_W = 240 * mm                       # corridor columns width (height computed dynamically)
FIG_D_W, FIG_D_H = 240 * mm, 200 * mm   # scenario heatmap — 8 rows × 3 cols + legend + note
INNER_PAD_X = 8 * mm
INNER_PAD_Y = 8 * mm

# Output raster resolution. 300 DPI on a 200 mm wide page → ~2362 px wide,
# inside the 1400–2000 px target band the brief specified once you account
# for the page padding; embedded at 100% in the Long-Read PDF it remains
# crisp on screen and print.
PNG_DPI = 300


# ---------------------------------------------------------------------------
# Figure A — Fragility-class stack-bar
# ---------------------------------------------------------------------------


def render_fragility_stack_bar(pdf_path: Path, sot: dict) -> None:
    """Bar 1 (BY COUNT) + Bar 2 (BY SHARE) + legend + cascade footnote.

    Mirrors page_classes Bar 1 + Bar 2 from visual-read-pdf-gen.py at lines
    826–873, scaled to a standalone figure-only canvas.
    """
    page_w, page_h = FIG_A_W, FIG_A_H
    c = canvasmod.Canvas(str(pdf_path), pagesize=(page_w, page_h))
    page_background(c, page_w, page_h)

    content_x = INNER_PAD_X
    content_w = page_w - 2 * INNER_PAD_X
    y = page_h - INNER_PAD_Y

    # ---- Bar 1 — By count (36 markets, 9 / 9 / 15 / 3) -------------------
    fc = sot["fragility_classes"]
    counts = [fc[k]["n_countries"] for k in ["I", "II", "III", "IV"]]
    eyebrow_1 = (
        f"BY COUNT · 36 MARKETS · "
        f"{counts[0]} / {counts[1]} / {counts[2]} / {counts[3]}"
    )
    overline(c, content_x, y, eyebrow_1)
    bar1_y = y - BAR_H - 3 * mm
    inline_1 = [
        (counts[0], CLS_COLOR["I"],   f"{counts[0]} · Class I"),
        (counts[1], CLS_COLOR["II"],  f"{counts[1]} · Class II"),
        (counts[2], CLS_COLOR["III"], f"{counts[2]} · Class III"),
        (counts[3], CLS_COLOR["IV"],  f"{counts[3]} · IV"),
    ]
    draw_segmented_bar(c, content_x, bar1_y, content_w, inline_1)
    y = bar1_y - 8 * mm

    # ---- Bar 2 — By share of working-age population ----------------------
    pae = sot["cross_cutting_findings"]["pan_european_aggregate"]
    eu36 = pae["european_36"]["class_distribution_population_weighted_pct"]
    overline(c, content_x, y, "BY SHARE OF WORKING-AGE POPULATION")
    bar2_y = y - BAR_H - 4 * mm
    inline_2 = [
        (eu36["I"],   CLS_COLOR["I"],   f"{eu36['I']:.1f}% · Class I"),
        (eu36["II"],  CLS_COLOR["II"],  f"{eu36['II']:.1f}% · Class II"),
        (eu36["III"], CLS_COLOR["III"], f"{eu36['III']:.1f}% · Class III"),
        (eu36["IV"],  CLS_COLOR["IV"],  f"{eu36['IV']:.1f}% · Class IV"),
    ]
    draw_segmented_bar(c, content_x, bar2_y, content_w, inline_2)
    y = bar2_y - 9 * mm

    # ---- Legend ----------------------------------------------------------
    draw_class_legend(c, content_x, y, content_w)
    y -= 6 * mm

    # ---- Cascade-pressure footnote --------------------------------------
    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    foot = (
        "Cascade pressure (Class IV) sits at the EU's borders. "
        "Three candidate markets (MK, RS, TR)."
    )
    fy = y
    for line in wrap_lines(foot, "Geist", 9, content_w):
        c.drawString(content_x, fy, line)
        fy -= 12

    c.showPage()
    c.save()


# ---------------------------------------------------------------------------
# Figure B — Reskilling-capacity funnel
# ---------------------------------------------------------------------------


def render_reskilling_funnel(pdf_path: Path) -> None:
    """7.55 M cohort vs 450 K net new — 4-row funnel, identical to Visual
    Read p5's draw_reskilling_arithmetic.
    """
    page_w, page_h = FIG_B_W, FIG_B_H
    c = canvasmod.Canvas(str(pdf_path), pagesize=(page_w, page_h))
    page_background(c, page_w, page_h)

    content_x = INNER_PAD_X
    content_w = page_w - 2 * INNER_PAD_X
    y = page_h - INNER_PAD_Y

    ref = float(RESKILLING_COHORT_2035)
    headline = "7.55 M cohort against 450 K of net new annual capacity"
    cy = draw_graphic_header(
        c, content_x, y, content_w,
        "RESKILLING-CAPACITY ARITHMETIC · EU-27 + UK",
        headline,
    )
    cy -= 0.5 * mm

    cy = draw_simple_bar_row(
        c, content_x, cy, content_w,
        "Cohort needing reskilling by 2035",
        "7.55 M total",
        GRANITE_DARK,
        scale=1.0,
    )
    cy = draw_simple_bar_row(
        c, content_x, cy, content_w,
        "Annual training throughput",
        "3.34 M / yr",
        GRANITE,
        scale=TRAINING_THROUGHPUT_YR / ref,
    )
    cy = draw_simple_bar_row(
        c, content_x, cy, content_w,
        "absorbed by baseline economic churn",
        "2.89 M / yr",
        GRANITE_LIGHTER,
        scale=BASELINE_ABSORBED_YR / ref,
        sub_row=True,
    )
    cy = draw_simple_bar_row(
        c, content_x, cy, content_w,
        "net new capacity for AI transitions",
        "450 K / yr",
        DEEP_TEAL,
        scale=NET_NEW_YR / ref,
        sub_row=True,
        value_color=DEEP_TEAL,
    )
    caption = (
        "~15-year backlog · to clear the 7.55 M cohort at 450 K / yr, "
        "against a 1–3 year AI displacement window. "
        "Response time runs 5–9 years."
    )
    draw_graphic_caption(c, content_x, cy - 2 * mm, content_w, caption)

    c.showPage()
    c.save()


# ---------------------------------------------------------------------------
# Figure C — Three-corridor columns (mirrors Visual Read p3 page_corridors)
# ---------------------------------------------------------------------------


def draw_corridor_column(c, x, y, w, h, key, cor, color):
    """Aligned-rhythm corridor card.

    Y anchors fixed relative to card top so rows line up across all three
    cards (header / label / ratio / big-number / MEMBERS pills / footnote).
    Verbatim port of visual-read-pdf-gen.py draw_corridor_column.
    """
    c.saveState()
    c.setFillColor(HexColor("#FFFFFF"))
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.5)
    c.roundRect(x, y, w, h, RADIUS_CARD, stroke=1, fill=1)
    draw_card_accent(c, x, y, w, h, color, side="top", thickness=6)

    c.setFont("Geist-Bold", 9)
    c.setFillColor(color)
    c.drawString(x + 5 * mm, y + h - 14 * mm, key.upper())

    c.setFillColor(PURE_BLACK)
    c.setFont("Geist-Medium", 12)
    label_lines = wrap_lines(cor["label"], "Geist-Medium", 12, w - 10 * mm)
    ly = y + h - 21 * mm
    for line in label_lines:
        c.drawString(x + 5 * mm, ly, line)
        ly -= 14

    ratio_y = y + h - 45 * mm
    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    c.drawString(x + 5 * mm, ratio_y, f"Ratio {cor['ratio_range']}")

    big_y = y + h - 59 * mm
    c.setFont("Geist-Medium", 30)
    c.setFillColor(color)
    big_str = str(cor["n_countries"])
    c.drawString(x + 5 * mm, big_y, big_str)
    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    c.drawString(
        x + 5 * mm + pdfmetrics.stringWidth(big_str, "Geist-Medium", 30) + 4,
        big_y + 4, "markets",
    )

    members_y = y + h - 71 * mm
    _tracked_text(c, x + 5 * mm, members_y, "MEMBERS",
                  "Geist-Bold", 7.5, GRANITE, 1.2)
    pill_h_9 = 9 + 2.5 * 2 + 1
    pills_y = members_y - 4 - pill_h_9
    draw_pill_row(
        c, x + 5 * mm, pills_y, cor["countries"], w - 10 * mm,
        fill=HexColor("#FFFFFF"), border=color, text_color=color, size=9,
    )
    # Phil-locked 2026-05-13 v4.2.x: interpretation footer removed from each
    # corridor card — the same explanation lives in the surrounding §2 prose.
    c.restoreState()


def _pill_row_count(codes: list[str], max_w: float, size: float = 9,
                    pill_gap: float = 3) -> int:
    """Wrap-fit pill count → row count. Mirrors draw_pill_row's packing."""
    cur_x = 0.0
    rows = 1
    for code in codes:
        w = pdfmetrics.stringWidth(code, "Geist-Medium", size) + 12
        if cur_x + w > max_w:
            cur_x = 0.0
            rows += 1
        cur_x += w + pill_gap
    return rows


def render_corridor_columns(pdf_path: Path, sot: dict) -> None:
    """3-column corridor card grid sized to the largest pill cluster + margin.

    Standalone landscape figure mirroring Visual Read p3. Card height is
    computed dynamically from the corridor with the most country pills (C2
    typically) so no row bleeds out of its card (Phil-locked v4.2.x).
    """
    corridors = sot["corridors"]
    order = ["C1", "C2", "C3"]
    palette = {"C1": DEEP_TEAL, "C2": ALPINE_GOLD, "C3": ALPINE_RED}

    # ---- Dynamic card-height pass ----------------------------------------
    # Card-internal anchors are fixed (see draw_corridor_column):
    #   members_y     = card_top − 71 mm
    #   pills_first_y = members_y − 4 pt − pill_h (≈ 5.3 mm)
    #   pill row step = pill_h + line_gap = 15 + 3 = 18 pt ≈ 6.35 mm
    # Card must fit N pill rows + 8 mm bottom margin.
    PILLS_TOP_FROM_CARD_TOP_MM = 71 + (4 / mm) + (15 / mm)  # ≈ 77.7 mm
    PILL_ROW_STEP_MM = 18 / mm                              # ≈ 6.35 mm
    BOTTOM_MARGIN_MM = 8.0

    content_w_probe = FIG_C_W - 2 * INNER_PAD_X
    col_w = (content_w_probe - 2 * 5 * mm) / 3
    pill_max_w = col_w - 10 * mm
    rows_max = max(_pill_row_count(corridors[k]["countries"], pill_max_w)
                   for k in order)
    card_h_mm = (
        PILLS_TOP_FROM_CARD_TOP_MM
        + (rows_max - 1) * PILL_ROW_STEP_MM
        + BOTTOM_MARGIN_MM
    )
    col_h = card_h_mm * mm

    # ---- Canvas height: top stack (overline + h2 + lede + gap) + col_h ---
    # Empirically the top stack consumes ≈ 36 mm; bottom padding ≈ 12 mm.
    page_w = FIG_C_W
    page_h = (36 + card_h_mm + 12) * mm
    c = canvasmod.Canvas(str(pdf_path), pagesize=(page_w, page_h))
    page_background(c, page_w, page_h)

    content_x = INNER_PAD_X
    content_w = page_w - 2 * INNER_PAD_X
    y = page_h - INNER_PAD_Y

    overline(c, content_x, y, "HOW THE 36 SPLIT")
    y = heading_h2(c, content_x, y - 8 * mm,
                   "Lens 1 · Velocity-to-absorption ratio", content_w)
    y = heading_lede(
        c, content_x, y - 4 * mm,
        "Below 1.20 the labour market manages the transition. Above 2.80 it "
        "does not. The middle band is where most of Europe sits. This corridor "
        "split is the baseline segmentation before multi-lens stress-testing.",
        content_w,
    )

    gap = 5 * mm
    grid_top = y - 4 * mm
    for i, key in enumerate(order):
        cx = content_x + i * (col_w + gap)
        cy = grid_top - col_h
        draw_corridor_column(c, cx, cy, col_w, col_h, key,
                             corridors[key], palette[key])

    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    example = (
        "Values near 1 mean the training-and-placement system can keep up "
        "with displacement. Values near 3 mean jobs are changing about three "
        "times faster than the system can absorb workers (e.g., Ireland/UK)."
    )
    ey = grid_top - col_h - 6 * mm
    for line in wrap_lines(example, "Geist", 9, content_w):
        c.drawString(content_x, ey, line)
        ey -= 12

    c.showPage()
    c.save()


# ---------------------------------------------------------------------------
# Figure D — Scenario × regime heatmap (mirrors Visual Read p6 page_scenarios)
# ---------------------------------------------------------------------------


def _draw_heatmap_legend(c, x, y, w):
    """Discrete 6-band swatch legend (Phil-locked 2026-05-13 v4)."""
    bands = [
        (HEAT_1, "0–10%"),
        (HEAT_2, "11–15%"),
        (HEAT_3, "16–20%"),
        (HEAT_4, "21–25%"),
        (HEAT_5, "26–30%"),
        (HEAT_6, "31%+"),
    ]
    swatch_w = 12 * mm
    swatch_h = 4 * mm
    gap = 2 * mm
    cur_x = x
    for color, label in bands:
        c.setFillColor(color)
        c.rect(cur_x, y, swatch_w, swatch_h, stroke=0, fill=1)
        c.setFont("Geist", 7.5)
        c.setFillColor(GRANITE)
        c.drawCentredString(cur_x + swatch_w / 2, y - 9, label)
        cur_x += swatch_w + gap
    c.setFont("Geist-Bold", 7.5)
    c.setFillColor(GRANITE)
    c.drawString(cur_x + 4 * mm, y + 1,
                 "Lighter = lower · darker = higher probability.")


def render_scenario_heatmap(pdf_path: Path, sot: dict) -> None:
    """8 × 3 probability heatmap + legend + interpretation note.

    Standalone landscape figure mirroring Visual Read p6.
    """
    page_w, page_h = FIG_D_W, FIG_D_H
    c = canvasmod.Canvas(str(pdf_path), pagesize=(page_w, page_h))
    page_background(c, page_w, page_h)

    content_x = INNER_PAD_X
    content_w = page_w - 2 * INNER_PAD_X
    y = page_h - INNER_PAD_Y

    overline(c, content_x, y, "EIGHT SCENARIOS × THREE REGIMES")
    y = heading_h2(c, content_x, y - 8 * mm,
                   "Probability heatmap", content_w)
    y = heading_lede(
        c, content_x, y - 4 * mm,
        "The eight scenarios cover the spectrum from reinstatement revival to "
        "polycrisis drag. The likelihood of each shifts with the economic "
        "regime. These scenarios define the stress test used to assign "
        "fragility classes.",
        content_w,
    )

    scenarios = sot["scenarios"]
    sc_keys = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"]
    label_col = 80 * mm
    cell_w = (content_w - label_col) / 3
    cell_h = 16 * mm
    header_h = 6 * mm
    grid_top = y - 8 * mm

    for j, reg in enumerate(REGIME_ORDER):
        hx = content_x + label_col + j * cell_w + cell_w / 2
        label = REGIME_LABELS[reg].upper()
        w_label = pdfmetrics.stringWidth(label, "Geist-Bold", 7.5) \
            + 1.2 * (len(label) - 1)
        _tracked_text(c, hx - w_label / 2, grid_top - 7,
                      label, "Geist-Bold", 7.5, GRANITE, 1.2)

    for i, sk in enumerate(sc_keys):
        sc = scenarios[sk]
        ry = grid_top - header_h - (i + 1) * cell_h
        label_full = sk + " · " + sc["label"]
        if pdfmetrics.stringWidth(label_full, "Geist-Bold", 12) \
                > label_col - 4 * mm:
            paren = label_full.find("(")
            if paren > 0:
                label_full = label_full[:paren].strip()
        c.setFont("Geist-Bold", 12)
        c.setFillColor(PURE_BLACK)
        wrapped = wrap_lines(label_full, "Geist-Bold", 12, label_col - 4 * mm)
        ly_lbl = ry + cell_h - 6 * mm
        for line in wrapped:
            c.drawString(content_x, ly_lbl, line)
            ly_lbl -= 13
        sub_y = ly_lbl - 1
        c.setFont("Geist", 9)
        c.setFillColor(GRANITE)
        c.drawString(content_x, sub_y,
                     sc.get("spectrum_position", "")[:50])
        pr = sc.get("probability_per_regime") \
            or sc.get("probability_conditional_per_regime", {})
        for j, reg in enumerate(REGIME_ORDER):
            cx = content_x + label_col + j * cell_w
            triple = pr.get(reg, [0, 0, 0])
            mid = triple[1] if len(triple) > 1 else 0
            c.setFillColor(heat_color(mid))
            c.rect(cx + 1, ry + 1, cell_w - 2, cell_h - 2, stroke=0, fill=1)
            text_col = heat_text_color(mid)
            median_size = 12
            range_size = 7.5
            gap = 3.5
            block_h = median_size + gap + range_size
            cell_cx = cx + cell_w / 2
            cell_cy = ry + (cell_h - 2) / 2 + 1
            median_baseline = cell_cy + block_h / 2 - median_size
            range_baseline = median_baseline - gap - range_size
            c.setFont("Geist-Bold", median_size)
            c.setFillColor(text_col)
            c.drawCentredString(cell_cx, median_baseline, f"{mid*100:.0f}%")
            c.setFont("Geist", range_size)
            c.setFillColor(text_col)
            c.drawCentredString(
                cell_cx, range_baseline,
                f"[{triple[0]*100:.0f}–{triple[2]*100:.0f}]",
            )

    legend_y = grid_top - header_h - len(sc_keys) * cell_h - 12 * mm
    _draw_heatmap_legend(c, content_x, legend_y, content_w)

    note_y = legend_y - 12 * mm
    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    for line in wrap_lines(
        "Cell shading darkens as probability rises. Each cell shows the "
        "median probability with the 80% confidence-interval range below. "
        "S1 (reinstatement revival) collapses from 10% in a growth regime "
        "to 5% in post-growth. S2 (climate-adaptation) is the only scenario "
        "whose probability rises into post-growth.",
        "Geist", 9, content_w,
    ):
        c.drawString(content_x, note_y, line)
        note_y -= 12

    c.showPage()
    c.save()


# ---------------------------------------------------------------------------
# PDF → PNG rasterisation
# ---------------------------------------------------------------------------


def pdf_to_png(pdf_path: Path, png_path: Path, dpi: int = PNG_DPI) -> None:
    """Use Homebrew poppler's `pdftoppm` to rasterise the single-page PDF.

    `pdftoppm` writes `<prefix>-1.png` (one-indexed). We write to a temp dir
    and move into place to keep the output path stable.
    """
    pdftoppm = shutil.which("pdftoppm")
    if pdftoppm is None:
        raise RuntimeError(
            "pdftoppm not found on PATH — install Homebrew poppler "
            "(`brew install poppler`)."
        )
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        prefix = tmp_path / "page"
        subprocess.run(
            [pdftoppm, "-png", "-r", str(dpi), str(pdf_path), str(prefix)],
            check=True,
        )
        # pdftoppm uses `<prefix>-1.png` for a single-page doc, but some
        # versions emit `<prefix>.png` when there's only one page. Cover both.
        candidates = [tmp_path / "page-1.png", tmp_path / "page.png"]
        produced = next((p for p in candidates if p.exists()), None)
        if produced is None:
            listed = sorted(p.name for p in tmp_path.iterdir())
            raise RuntimeError(
                f"pdftoppm produced no PNG; tmp dir contains: {listed}"
            )
        png_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(produced), str(png_path))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    sot = json.loads(SOT.read_text())

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        fig_a_pdf = tmp_path / "fig-a.pdf"
        fig_b_pdf = tmp_path / "fig-b.pdf"
        fig_c_pdf = tmp_path / "fig-c.pdf"
        fig_d_pdf = tmp_path / "fig-d.pdf"

        render_fragility_stack_bar(fig_a_pdf, sot)
        render_reskilling_funnel(fig_b_pdf)
        render_corridor_columns(fig_c_pdf, sot)
        render_scenario_heatmap(fig_d_pdf, sot)

        pdf_to_png(fig_a_pdf, FIG_A_PNG)
        pdf_to_png(fig_b_pdf, FIG_B_PNG)
        pdf_to_png(fig_c_pdf, FIG_C_PNG)
        pdf_to_png(fig_d_pdf, FIG_D_PNG)

    for path in (FIG_A_PNG, FIG_B_PNG, FIG_C_PNG, FIG_D_PNG):
        size_kb = path.stat().st_size / 1024
        print(f"Written {path.relative_to(REPO)} ({size_kb:,.1f} KB)")


if __name__ == "__main__":
    main()
