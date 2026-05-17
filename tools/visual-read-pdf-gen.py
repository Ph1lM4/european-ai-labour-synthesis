#!/usr/bin/env python3
"""Render the Layer 6 Visual Read to a Nexalps-styled A4 PDF.

Eight pages, each one a single canvas composition. ReportLab only — the cover
embeds the Phase 2J corridor map PNG (`site/exports/corridor-map-nexalps.png`),
every other graphic is drawn natively. Every numeric is pulled from
`layer-6-deliverable-data.json` (SOT) or the Phil-locked block in
`site/findings.html` (Italy specifics, which are not in the JSON).

Style locks (per Nexalps tailwind.config.ts):
  * Pearl-white background #F8F9FA, pure-black body text
  * Geist family (300/400/500/600/700) + LightItalic for display
  * Deep-teal-text #087569 accent (WCAG AA on white)
  * Granite-gray #4A5568 secondary
  * A4 portrait, 25 mm margins (160 mm content width)

Pages:
  1. Cover — light-italic headline + real corridor map (Mercator projection)
  2. Five-lens grid — plain-language descriptions
  3. Three corridors — managed / partial / displacement, country pills
  4. Four fragility classes — stack bar 9/9/15/3 + class panels with pills
  5. Reskilling-capacity gap — Sankey diagram + AI/training speed-gap bars
  6. Eight-scenario probability heatmap — neutral grey gradient
  7. Italy callout — overflow-safe layout
  8. CTA — document ladder + cite-as footer

Usage:
  python3 tools/visual-read-pdf-gen.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Shared style module — registers Geist fonts, sets rl_config.invariant=1,
# and exports the v4.1 palette + canvas helpers. Import before any other
# reportlab.* import so the deterministic-build flags are set in time.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _pdf_style import (
    HexColor, Color,
    PEARL_WHITE, PURE_BLACK, PURE_WHITE,
    DEEP_TEAL, DEEP_TEAL_BG,
    GRANITE, GRANITE_DARK, GRANITE_LIGHT, GRANITE_LIGHTER,
    HAIRLINE,
    ALPINE_GOLD, ALPINE_RED, CLASS_IV_WINE, GLACIER_BLUE,
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

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas as canvasmod

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO = Path(__file__).resolve().parent.parent
SOT = REPO / "layer-6-deliverable-data.json"
OUTPUT = REPO / "docs" / "layer-6-deliverable-visual-read.pdf"
CORRIDOR_MAP_PNG = REPO / "site" / "exports" / "corridor-map-nexalps-print.png"

# Page geometry (visual-read-specific A4 portrait, 25 mm margins).
PAGE_W, PAGE_H = A4
M_L = 25 * mm
M_R = 25 * mm
M_T = 25 * mm
M_B = 22 * mm
CONTENT_W = PAGE_W - M_L - M_R
CONTENT_H = PAGE_H - M_T - M_B


# ---------------------------------------------------------------------------
# Footer (page-chrome local to visual-read; not shared)
# ---------------------------------------------------------------------------


def footer(c: canvasmod.Canvas, page_num: int, total: int = 8) -> None:
    c.saveState()
    c.setFont("Geist", 7.5)
    c.setFillColor(GRANITE)
    y = 12 * mm
    c.drawString(M_L, y, "Part 6 · Visual Read")
    c.drawCentredString(PAGE_W / 2, y, "Nexalps · Part 6 of 7")
    c.drawRightString(PAGE_W - M_R, y, f"Page {page_num} / {total}")
    c.restoreState()


# ---------------------------------------------------------------------------
# SOT loader
# ---------------------------------------------------------------------------

def load_sot() -> dict:
    return json.loads(SOT.read_text())


# ---------------------------------------------------------------------------
# Page 1 — Cover with real corridor map
# ---------------------------------------------------------------------------

def page_cover(c: canvasmod.Canvas, sot: dict) -> None:
    page_background(c, PAGE_W, PAGE_H)
    # Cover surface drops the "PART 6 OF 7 ·" prefix (Phil-locked 2026-05-13);
    # Part-6 anchoring remains in the footer chrome and page-8 ladder.
    overline(c, M_L, PAGE_H - M_T, "EUROPEAN AI LABOUR MARKET SYNTHESIS · VISUAL READ · FIRST EDITION")
    headline = "No European labour market is unconditionally safe from AI-driven displacement."
    c.setFont("Geist-LightItalic", 36)
    c.setFillColor(PURE_BLACK)
    y = PAGE_H - M_T - 16 * mm
    for line in wrap_lines(headline, "Geist-LightItalic", 36, CONTENT_W):
        c.drawString(M_L, y, line)
        y -= 44
    y -= 4 * mm
    lede = (
        "36 markets stress-tested across five lenses and eight scenarios. "
        "Nine pass under the softer rule. Under the strict rule, none do."
    )
    y = draw_paragraph(
        c, M_L, y, lede,
        font="Geist", size=9, leading=12,
        max_w=CONTENT_W, color=GRANITE,
    )
    y -= 8 * mm
    # Corridor map (real Mercator projection from Phase 2J export).
    map_top = y
    map_bottom = M_B + 26 * mm
    map_h = map_top - map_bottom
    draw_corridor_map(c, M_L, map_bottom, CONTENT_W, map_h)
    # Byline at bottom
    c.setFont("Geist-Bold", 9)
    c.setFillColor(GRANITE)
    c.drawString(M_L, M_B + 14 * mm, "BY PHILIPP MAUL · NEXALPS · MAY 2026")
    c.showPage()


def draw_corridor_map(c, x, y, w, h):
    """Embed the Phase 2J corridor-map PNG, centered + scaled to fit."""
    if not CORRIDOR_MAP_PNG.exists():
        c.saveState()
        c.setFillColor(HexColor("#FAFBFC"))
        c.setStrokeColor(HAIRLINE)
        c.setLineWidth(0.5)
        c.roundRect(x, y, w, h, 4 * mm, stroke=1, fill=1)
        c.setFont("Geist", 9)
        c.setFillColor(GRANITE)
        c.drawCentredString(x + w / 2, y + h / 2,
                            "Corridor map asset missing — run tools/dotmap-export.py")
        c.restoreState()
        return
    img = ImageReader(str(CORRIDOR_MAP_PNG))
    iw, ih = img.getSize()
    scale = min(w / iw, h / ih)
    dw, dh = iw * scale, ih * scale
    dx = x + (w - dw) / 2
    dy = y + (h - dh) / 2
    c.drawImage(img, dx, dy, width=dw, height=dh, mask="auto")
    # Legend strip below the map — fits within content width.
    legend_y = y - 6 * mm
    _tracked_text(c, x, legend_y, "FRAGILITY CLASS",
                  "Geist-Bold", 7.5, GRANITE, 1.0)
    swatch_x = x + 32 * mm
    item_gap = 5 * mm
    c.setFont("Geist", 7.5)
    for cls in ["I", "II", "III", "IV"]:
        label = f"Class {cls} · {CLS_LABEL[cls]}"
        c.setFillColor(CLS_COLOR[cls])
        c.circle(swatch_x + 2, legend_y + 1.5, 2.2, stroke=0, fill=1)
        c.setFillColor(PURE_BLACK)
        c.drawString(swatch_x + 6.5, legend_y, label)
        swatch_x += pdfmetrics.stringWidth(label, "Geist", 7.5) + 7 + item_gap


# ---------------------------------------------------------------------------
# Page 2 — Five-lens grid (PLAIN LANGUAGE)
# ---------------------------------------------------------------------------

LENSES = [
    ("L1", "Can the country retrain workers fast enough to keep up with AI?",
     "A simple “speed mismatch” score: how fast AI makes jobs disappear versus "
     "how fast people can be retrained and placed into new roles. Values near 1 "
     "mean the training-and-placement system can keep up with displacement. Values "
     "near 3 mean jobs are changing about three times faster than the system can "
     "absorb workers (e.g., Ireland/UK)."),
    ("L2", "Will retirements absorb enough of the displacement?",
     "Testing the “retirement will absorb it” thesis against an ~80% offset bar. "
     "No country clears it. At best, retirements cover only about a quarter "
     "(~26%) of the potentially displaced jobs."),
    ("L3", "Do national averages hide big internal splits?",
     "A country can look “fine” on average while particular regions or worker "
     "groups take much bigger hits. We flag markets where that internal spread "
     "is large enough to change the policy implications."),
    ("L4", "Is the country stretched too thin to support workers through change?",
     "Compounding demands (defence, climate, migration, EU budget pressures) are "
     "consuming the same institutional bandwidth needed to support workers "
     "through the transition. We count active shocks and flag when worker-"
     "protection capacity is being squeezed."),
    ("L5", "Do overlapping pressures push the country past its adaptive capacity?",
     "A composite stress test: “Can the system still cope?” across job families. "
     "Twelve countries breach the floor even at a broad occupational level, and "
     "the true count is likely higher with finer-grained data."),
]

# Page 2 lede + synthesis card prose (Phil-locked 2026-05-13 v4).
PAGE2_LEDE = (
    "Each lens tests a different failure mode. We combine them in two steps: "
    "Lens 1 sets the corridor (a baseline split by displacement speed vs "
    "absorption capacity). The other lenses then determine fragility under "
    "stress across scenarios."
)
PAGE2_LENSES_COMBINE = [
    ("Lens 1 → Corridor (C1 / C2 / C3): ",
     "velocity-to-absorption ratio (next page)."),
    ("Lenses 2, 4, 5 → Fragility class (I / II / III / IV): ",
     "stress-tested robustness across scenarios (page 4)."),
    ("Lens 3: ",
     "flags markets where national averages hide large internal splits "
     "(not shown in this document)."),
]
PAGE2_FINAL_VERDICT = "Final verdict: strict rule 0/36 robust; softer rule 9/36."


def page_lenses(c: canvasmod.Canvas, sot: dict) -> None:
    page_background(c, PAGE_W, PAGE_H)
    overline(c, M_L, PAGE_H - M_T, "WHAT WE TESTED")
    y = heading_h2(c, M_L, PAGE_H - M_T - 8 * mm, "Five diagnostic lenses", CONTENT_W)
    y = heading_lede(c, M_L, y - 4 * mm, PAGE2_LEDE, CONTENT_W)
    grid_top = y - 4 * mm
    col_count = 2
    gap = 5 * mm
    card_w = (CONTENT_W - gap * (col_count - 1)) / col_count
    card_h = 58 * mm
    for i, (num, title, gloss) in enumerate(LENSES):
        col = i % col_count
        row = i // col_count
        cx = M_L + col * (card_w + gap)
        cy = grid_top - (row + 1) * card_h - row * gap
        draw_lens_card(c, cx, cy, card_w, card_h, num, title, gloss)
    sx = M_L + 1 * (card_w + gap)
    sy = grid_top - 3 * card_h - 2 * gap
    draw_lenses_combine_card(c, sx, sy, card_w, card_h)
    # Optional verdict line below the grid if vertical room allows.
    verdict_y = sy - 6 * mm
    if verdict_y > M_B + 14 * mm:
        c.setFont("Geist", 9)
        c.setFillColor(GRANITE)
        c.drawString(M_L, verdict_y, PAGE2_FINAL_VERDICT)
    footer(c, 2)
    c.showPage()


def draw_lens_card(c, x, y, w, h, num, title, gloss):
    c.saveState()
    c.setFillColor(HexColor("#FFFFFF"))
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.5)
    c.roundRect(x, y, w, h, RADIUS_CARD, stroke=1, fill=1)
    draw_card_accent(c, x, y, w, h, DEEP_TEAL, side="left", thickness=4)
    c.setFont("Geist-Bold", 9)
    c.setFillColor(DEEP_TEAL)
    c.drawString(x + 6 * mm, y + h - 7 * mm, num.upper())
    title_y = y + h - 13 * mm
    c.setFont("Geist-Medium", 12)
    c.setFillColor(PURE_BLACK)
    for line in wrap_lines(title, "Geist-Medium", 12, w - 12 * mm):
        c.drawString(x + 6 * mm, title_y, line)
        title_y -= 14
    gloss_y = title_y - 3
    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    for line in wrap_lines(gloss, "Geist", 9, w - 12 * mm):
        c.drawString(x + 6 * mm, gloss_y, line)
        gloss_y -= 11
    c.restoreState()


def draw_lenses_combine_card(c, x, y, w, h):
    """Phil-locked 2026-05-13 v4.1: no bullets; sentences separated by blank lines."""
    c.saveState()
    c.setFillColor(DEEP_TEAL)
    c.setStrokeColor(DEEP_TEAL)
    c.roundRect(x, y, w, h, RADIUS_CARD, stroke=0, fill=1)
    c.setFont("Geist-Bold", 9)
    c.setFillColor(PURE_WHITE)
    c.drawString(x + 6 * mm, y + h - 7 * mm, "HOW THE LENSES COMBINE")
    line_y = y + h - 14 * mm
    body_w = w - 12 * mm
    c.setFont("Geist", 9)
    c.setFillColor(PURE_WHITE)
    for i, (lead, tail) in enumerate(PAGE2_LENSES_COMBINE):
        if i > 0:
            line_y -= 11  # blank-line separator between sentences
        full = lead + tail
        for line in wrap_lines(full, "Geist", 9, body_w):
            c.drawString(x + 6 * mm, line_y, line)
            line_y -= 11
    c.restoreState()


# ---------------------------------------------------------------------------
# Page 3 — Three corridors (aligned Y-heights + country pills)
# ---------------------------------------------------------------------------

def page_corridors(c: canvasmod.Canvas, sot: dict) -> None:
    page_background(c, PAGE_W, PAGE_H)
    overline(c, M_L, PAGE_H - M_T, "HOW THE 36 SPLIT")
    y = heading_h2(c, M_L, PAGE_H - M_T - 8 * mm,
                   "Lens 1 · Velocity-to-absorption ratio", CONTENT_W)
    y = heading_lede(
        c, M_L, y - 4 * mm,
        "Below 1.20 the labour market manages the transition. Above 2.80 it does not. "
        "The middle band is where most of Europe sits. This corridor split is the "
        "baseline segmentation before multi-lens stress-testing.",
    CONTENT_W,
    )
    corridors = sot["corridors"]
    order = ["C1", "C2", "C3"]
    palette = {"C1": DEEP_TEAL, "C2": ALPINE_GOLD, "C3": ALPINE_RED}

    grid_top = y - 4 * mm
    gap = 5 * mm
    col_w = (CONTENT_W - gap * 2) / 3
    col_h = 150 * mm

    for i, key in enumerate(order):
        cx = M_L + i * (col_w + gap)
        cy = grid_top - col_h
        cor = corridors[key]
        draw_corridor_column(c, cx, cy, col_w, col_h, key, cor, palette[key])

    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    example = (
        "Values near 1 mean the training-and-placement system can keep up with "
        "displacement. Values near 3 mean jobs are changing about three times "
        "faster than the system can absorb workers (e.g., Ireland/UK)."
    )
    ey = grid_top - col_h - 6 * mm
    for line in wrap_lines(example, "Geist", 9, CONTENT_W):
        c.drawString(M_L, ey, line)
        ey -= 12
    footer(c, 3)
    c.showPage()


def draw_corridor_column(c, x, y, w, h, key, cor, color):
    """Aligned Y-rhythm: header / label / ratio / big-number / MEMBERS pills / footnote.

    All Y anchors are fixed relative to the card top so that the corresponding row
    sits at the same Y across all three corridor columns.
    """
    c.saveState()
    c.setFillColor(HexColor("#FFFFFF"))
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.5)
    c.roundRect(x, y, w, h, RADIUS_CARD, stroke=1, fill=1)
    draw_card_accent(c, x, y, w, h, color, side="top", thickness=6)
    # Header
    c.setFont("Geist-Bold", 9)
    c.setFillColor(color)
    c.drawString(x + 5 * mm, y + h - 14 * mm, key.upper())
    # Label — locked 12 pt Geist-Medium, wrap to as many lines as needed
    # (Phil-locked 2026-05-13 v4 — no shrink-to-fit).
    c.setFillColor(PURE_BLACK)
    c.setFont("Geist-Medium", 12)
    label_lines = wrap_lines(cor["label"], "Geist-Medium", 12, w - 10 * mm)
    ly = y + h - 21 * mm
    for line in label_lines:
        c.drawString(x + 5 * mm, ly, line)
        ly -= 14
    # Ratio line — FIXED Y across all columns
    ratio_y = y + h - 45 * mm
    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    c.drawString(x + 5 * mm, ratio_y, f"Ratio {cor['ratio_range']}")
    # Big number — FIXED Y across all columns
    big_y = y + h - 59 * mm
    c.setFont("Geist-Medium", 30)
    c.setFillColor(color)
    c.drawString(x + 5 * mm, big_y, str(cor["n_countries"]))
    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    c.drawString(
        x + 5 * mm + pdfmetrics.stringWidth(str(cor["n_countries"]), "Geist-Medium", 30) + 4,
        big_y + 4, "markets",
    )
    # MEMBERS label — FIXED Y across all columns (locked 7.5 pt micro)
    members_y = y + h - 71 * mm
    _tracked_text(c, x + 5 * mm, members_y, "MEMBERS", "Geist-Bold", 7.5, GRANITE, 1.2)
    # Pills below the MEMBERS overline (pills_y is the pill BOTTOM)
    pill_h_9 = 9 + 2.5 * 2 + 1
    pills_y = members_y - 4 - pill_h_9
    draw_pill_row(
        c, x + 5 * mm, pills_y, cor["countries"], w - 10 * mm,
        fill=HexColor("#FFFFFF"), border=color, text_color=color,
        size=9,
    )
    # Interpretation footnote — bottom-aligned (locked 9 pt italic)
    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    interp_lines = wrap_lines(cor["interpretation"], "Geist", 9, w - 10 * mm)
    interp_y = y + 6 * mm + (len(interp_lines) - 1) * 11
    for line in interp_lines:
        c.drawString(x + 5 * mm, interp_y, line)
        interp_y -= 11
    c.restoreState()


# ---------------------------------------------------------------------------
# Page 4 — Four fragility classes (two-bar header + class cards)
# ---------------------------------------------------------------------------

def page_classes(c: canvasmod.Canvas, sot: dict) -> None:
    page_background(c, PAGE_W, PAGE_H)
    # Top eyebrow — routed through overline() to match every other page
    # (Phil-locked 2026-05-13 v4.1): uppercase + 1.5 pt tracking + 8 mm H2 gap.
    overline(c, M_L, PAGE_H - M_T, "Stress test distribution across 36 markets")
    y = heading_h2(c, M_L, PAGE_H - M_T - 8 * mm,
                   "Four fragility classes from stress-testing", CONTENT_W)
    y = heading_lede(
        c, M_L, y - 4 * mm,
        "The corridor sorts on velocity. The class sorts on what happens once you stress-test "
        "the velocity. Three quarters of Europe sits at Class II or worse.",
    CONTENT_W,
    )
    # Stress-test caption (sub-session 13 plain-language note); v4.1 folds in
    # the lens/scenario/regime scope previously carried on the top line.
    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    caption = (
        "Each country is tested against 8 possible futures × 3 economic conditions "
        "(growing / stagnant / no longer growing) using Lenses 2, 4, 5 combined, "
        "to see whether its corridor placement holds."
    )
    cy = y - 4 * mm
    for line in wrap_lines(caption, "Geist", 9, CONTENT_W):
        c.drawString(M_L, cy, line)
        cy -= 12
    y = cy - 3 * mm

    # ---- Bar 1 — By count (36 markets, 9 / 9 / 15 / 3) ---------------------
    fc = sot["fragility_classes"]
    counts = [fc[k]["n_countries"] for k in ["I", "II", "III", "IV"]]
    eyebrow_1 = (
        f"BY COUNT · 36 MARKETS · "
        f"{counts[0]} / {counts[1]} / {counts[2]} / {counts[3]}"
    )
    overline(c, M_L, y, eyebrow_1)
    bar1_y = y - BAR_H - 3 * mm
    inline_1 = [
        (counts[0], CLS_COLOR["I"],   f"{counts[0]} · Class I"),
        (counts[1], CLS_COLOR["II"],  f"{counts[1]} · Class II"),
        (counts[2], CLS_COLOR["III"], f"{counts[2]} · Class III"),
        (counts[3], CLS_COLOR["IV"],  f"{counts[3]} · IV"),
    ]
    draw_segmented_bar(c, M_L, bar1_y, CONTENT_W, inline_1)
    y = bar1_y - 8 * mm

    # ---- Bar 2 — By share of working-age population (36 markets) -----------
    pae = sot["cross_cutting_findings"]["pan_european_aggregate"]
    eu36 = pae["european_36"]["class_distribution_population_weighted_pct"]
    overline(c, M_L, y, "BY SHARE OF WORKING-AGE POPULATION")
    bar2_y = y - BAR_H - 4 * mm
    inline_2 = [
        (eu36["I"],   CLS_COLOR["I"],   f"{eu36['I']:.1f}% · Class I"),
        (eu36["II"],  CLS_COLOR["II"],  f"{eu36['II']:.1f}% · Class II"),
        (eu36["III"], CLS_COLOR["III"], f"{eu36['III']:.1f}% · Class III"),
        (eu36["IV"],  CLS_COLOR["IV"],  f"{eu36['IV']:.1f}% · Class IV"),
    ]
    draw_segmented_bar(c, M_L, bar2_y, CONTENT_W, inline_2)
    y = bar2_y - 9 * mm

    # ---- Legend ------------------------------------------------------------
    draw_class_legend(c, M_L, y, CONTENT_W)
    y -= 6 * mm

    # ---- Cascade-pressure footnote ----------------------------------------
    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    foot = (
        "Cascade pressure (Class IV) sits at the EU's borders. Three candidate markets "
        "(MK, RS, TR)."
    )
    fy = y
    for line in wrap_lines(foot, "Geist", 9, CONTENT_W):
        c.drawString(M_L, fy, line)
        fy -= 12
    y = fy - 2 * mm

    # ---- Four class cards (preserved, compacted to fit underneath) --------
    gap = 4 * mm
    panel_w = (CONTENT_W - gap * 3) / 4
    # Compute panel_h from remaining space above page footer (16mm reserved).
    bottom_reserve = M_B + 8 * mm
    panel_h = max(70 * mm, min(95 * mm, y - bottom_reserve))
    for i, k in enumerate(["I", "II", "III", "IV"]):
        px = M_L + i * (panel_w + gap)
        py = y - panel_h
        draw_class_panel(c, px, py, panel_w, panel_h, k, fc[k])

    footer(c, 4)
    c.showPage()


def draw_class_panel(c, x, y, w, h, key, payload):
    color = CLS_COLOR[key]
    c.saveState()
    c.setFillColor(HexColor("#FFFFFF"))
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.5)
    c.roundRect(x, y, w, h, RADIUS_CARD, stroke=1, fill=1)
    draw_card_accent(c, x, y, w, h, color, side="top", thickness=4)
    # Header — fixed Y
    c.setFont("Geist-Bold", 9)
    c.setFillColor(color)
    c.drawString(x + 4 * mm, y + h - 11 * mm, f"CLASS {key}")
    # Label — fixed Y (locked 12 pt Geist-Medium, wrap; no shrink-to-fit)
    c.setFont("Geist-Medium", 12)
    c.setFillColor(PURE_BLACK)
    label_lines = wrap_lines(CLS_LABEL[key], "Geist-Medium", 12, w - 8 * mm)
    ly = y + h - 17 * mm
    for line in label_lines:
        c.drawString(x + 4 * mm, ly, line)
        ly -= 14
    # Big number — fixed Y (aligned big-number row)
    c.setFont("Geist-Medium", 22)
    c.setFillColor(color)
    c.drawString(x + 4 * mm, y + h - 30 * mm, str(payload["n_countries"]))
    # MEMBERS label — fixed Y (locked 7.5 pt micro)
    members_y = y + h - 40 * mm
    c.setFont("Geist-Bold", 7.5)
    c.setFillColor(GRANITE)
    c.drawString(x + 4 * mm, members_y, "MEMBERS")
    # Pills below the MEMBERS overline (locked 9 pt)
    pill_h_9 = 9 + 2.5 * 2 + 1
    pills_y = members_y - 4 - pill_h_9
    draw_pill_row(
        c, x + 4 * mm, pills_y, payload["countries"], w - 8 * mm,
        fill=HexColor("#FFFFFF"), border=color, text_color=color,
        size=9,
    )
    c.restoreState()


# ---------------------------------------------------------------------------
# Page 5 — Reskilling capacity, baseline-churn decomposition, speed gap
# ---------------------------------------------------------------------------

# Baseline-churn decomposition anchored on
# `european-reskilling-map/scripts/04_net_new_capacity.py`:
#   Job-to-job retraining ~2.46M (Eurostat lfsa_etpgan / lfsi_long_q,
#     training-required share) + Green Deal reskilling 250K (EU Green Deal
#     Social Climate Fund annual) + Demographic replacement 180K (Cedefop
#     Skills Forecast 2025 replacement demand) = 2.89M / yr absorbed.
#   Net new = 3.34M - 2.89M = 450K / yr.
# RESKILLING_COHORT_2035 / TRAINING_THROUGHPUT_YR / BASELINE_ABSORBED_YR /
# NET_NEW_YR are imported from `_pdf_style`.

CHURN_COMPONENTS = [
    # Slate ramp: largest → darkest. No callout — all three are baseline-churn
    # components, none of them is "the good news" being surfaced.
    ("Job-to-job retraining",    2_460_000, GRANITE,         "2.46 M / yr"),
    ("Green Deal reskilling",      250_000, GRANITE_LIGHT,   "250 K / yr"),
    ("Demographic replacement",    180_000, GRANITE_LIGHTER, "180 K / yr"),
]


def page_reskilling(c: canvasmod.Canvas, sot: dict) -> None:
    page_background(c, PAGE_W, PAGE_H)
    # Phil-locked 2026-05-13 v4: eyebrow removed, top line is "How fast can
    # Europe adapt", headline becomes "The reskilling capacity gap".
    overline(c, M_L, PAGE_H - M_T, "HOW FAST CAN EUROPE ADAPT")
    y = heading_h2(c, M_L, PAGE_H - M_T - 8 * mm, "The reskilling capacity gap", CONTENT_W)
    y = heading_lede(
        c, M_L, y - 4 * mm,
        "Europe trains 3.34 million workers a year. Most of that is consumed by baseline churn. "
        "What remains for AI-displacement reskilling is the bottleneck.",
    CONTENT_W,
    )

    # ---- Graphic 1 — Reskilling-capacity arithmetic ----------------------
    y = draw_reskilling_arithmetic(c, M_L, y - 2 * mm, CONTENT_W)
    y -= 4 * mm
    # ---- Graphic 2 — Baseline economic churn decomposition ---------------
    y = draw_baseline_churn(c, M_L, y, CONTENT_W)
    y -= 4 * mm
    # ---- Graphic 3 — AI vs response timeline -----------------------------
    y = draw_speed_gap_bars(c, M_L, y, CONTENT_W)

    footer(c, 5)
    c.showPage()


def draw_reskilling_arithmetic(c, x, y, w) -> float:
    """Graphic 1 — funnel-pattern stacked bars sized vs the 7.55 M cohort.

    Four left-aligned bars, all proportional to the 7.55 M cohort:
      • Cohort (7.55 M) → full width
      • Annual throughput (3.34 M / yr) → 44%
      • — absorbed by baseline churn (2.89 M / yr) → 38%, em-dash sub-row
      • — net new capacity (450 K / yr)   → 6%,  em-dash sub-row, accent
    """
    ref = float(RESKILLING_COHORT_2035)
    headline = "7.55 M cohort against 450 K of net new annual capacity"
    cy = draw_graphic_header(
        c, x, y, w,
        "RESKILLING-CAPACITY ARITHMETIC · EU-27 + UK",
        headline,
    )
    # Long-read funnel palette: slate ramp dark→light for the three context
    # rows, deep-teal as the single callout on the net-new bar. Matches
    # `docs/layer-6-deliverable-long-read.pdf` reskilling-capacity funnel.
    cy -= 0.5 * mm  # H2 → first-bar gap matches inter-graphic vertical rhythm
    cy = draw_simple_bar_row(
        c, x, cy, w,
        "Cohort needing reskilling by 2035",
        "7.55 M total",
        GRANITE_DARK,
        scale=1.0,
    )
    cy = draw_simple_bar_row(
        c, x, cy, w,
        "Annual training throughput",
        "3.34 M / yr",
        GRANITE,
        scale=TRAINING_THROUGHPUT_YR / ref,
    )
    cy = draw_simple_bar_row(
        c, x, cy, w,
        "absorbed by baseline economic churn",
        "2.89 M / yr",
        GRANITE_LIGHTER,
        scale=BASELINE_ABSORBED_YR / ref,
        sub_row=True,
    )
    cy = draw_simple_bar_row(
        c, x, cy, w,
        "net new capacity for AI transitions",
        "450 K / yr",
        DEEP_TEAL,
        scale=NET_NEW_YR / ref,
        sub_row=True,
        value_color=DEEP_TEAL,
    )
    caption = (
        "~15-year backlog · to clear the 7.55 M cohort at 450 K / yr, against a 1–3 year "
        "AI displacement window. Response time runs 5–9 years."
    )
    return draw_graphic_caption(c, x, cy - 2 * mm, w, caption)


def draw_baseline_churn(c, x, y, w) -> float:
    """Graphic 2 — 2.89 M / yr decomposed into 3 components.

    Source: european-reskilling-map/scripts/04_net_new_capacity.py
    (Eurostat lfsa_etpgan job-to-job + EU Green Deal Social Climate Fund +
    Cedefop Skills Forecast 2025 replacement demand).
    """
    ref = float(BASELINE_ABSORBED_YR)
    cy = draw_graphic_header(
        c, x, y, w,
        "BASELINE ECONOMIC CHURN · 2.89 M / YEAR DECOMPOSED",
        "What the 2.89 M absorbs before AI transitions get a turn",
    )
    cy -= 0.5 * mm  # H2 → first-bar gap matches inter-graphic vertical rhythm
    for name, value, color, value_text in CHURN_COMPONENTS:
        cy = draw_simple_bar_row(
            c, x, cy, w,
            name, value_text, color, scale=value / ref,
        )
    caption = (
        "Source: european-reskilling-map Part 5 (Eurostat lfsa_etpgan tenure-under-1yr proxy · "
        "EU Green Deal Social Climate Fund · Cedefop Skills Forecast 2025 replacement demand)."
    )
    return draw_graphic_caption(c, x, cy - 2 * mm, w, caption)


def draw_speed_gap_bars(c, x, y, w) -> float:
    """Graphic 3 — three horizontal bars on a 9-year reference, same style.

    AI window (1–3 yr) · response (5–9 yr) · gap (3–5 yr) — each shown as a
    left-aligned bar whose width is its upper-bound year count over a 9-year
    reference span. The gap bar uses the accent palette (alpine-gold) to read
    as a callout, matching its role in the AI-vs-response narrative.
    """
    ref = 9.0
    cy = draw_graphic_header(
        c, x, y, w,
        "SPEED GAP · AI DISPLACEMENT WINDOW VS TRAINING RESPONSE",
        "AI moves in 1–3 years. Training systems respond in 5–9 years.",
    )
    cy -= 0.5 * mm  # H2 → first-bar gap matches inter-graphic vertical rhythm
    cy = draw_simple_bar_row(
        c, x, cy, w,
        "AI displacement window", "1–3 years", ALPINE_RED, scale=3 / ref,
    )
    cy = draw_simple_bar_row(
        c, x, cy, w,
        "European VET / university response", "5–9 years", GLACIER_BLUE,
        scale=9 / ref,
    )
    cy = draw_simple_bar_row(
        c, x, cy, w,
        "The gap", "3–5 years", ALPINE_GOLD, scale=5 / ref,
        value_color=ALPINE_GOLD,
    )
    caption = (
        "Displaced workers spend 3–5 years in limbo while the training system retools "
        "curricula, accredits new programmes, and runs cohorts through."
    )
    return draw_graphic_caption(c, x, cy - 2 * mm, w, caption)



# ---------------------------------------------------------------------------
# Page 6 — Eight-scenario heatmap (NEUTRAL GRADIENT)
# ---------------------------------------------------------------------------

# REGIME_LABELS / REGIME_ORDER / heat_color / heat_text_color imported from
# `_pdf_style`.


def page_scenarios(c: canvasmod.Canvas, sot: dict) -> None:
    page_background(c, PAGE_W, PAGE_H)
    overline(c, M_L, PAGE_H - M_T, "EIGHT SCENARIOS × THREE REGIMES")
    y = heading_h2(c, M_L, PAGE_H - M_T - 8 * mm, "Probability heatmap", CONTENT_W)
    y = heading_lede(
        c, M_L, y - 4 * mm,
        "The eight scenarios cover the spectrum from reinstatement revival to polycrisis drag. "
        "The likelihood of each shifts with the economic regime. "
        "These scenarios define the stress test used to assign fragility classes.",
    CONTENT_W,
    )
    scenarios = sot["scenarios"]
    sc_keys = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"]
    grid_top = y - 8 * mm
    label_col = 80 * mm
    cell_w = (CONTENT_W - label_col) / 3
    cell_h = 17 * mm
    header_h = 6 * mm  # v4.1: tightened regime-column header → first row gap

    for j, reg in enumerate(REGIME_ORDER):
        hx = M_L + label_col + j * cell_w + cell_w / 2
        label = REGIME_LABELS[reg].upper()
        w_label = pdfmetrics.stringWidth(label, "Geist-Bold", 7.5) + 1.2 * (len(label) - 1)
        _tracked_text(c, hx - w_label / 2, grid_top - 7,
                      label, "Geist-Bold", 7.5, GRANITE, 1.2)

    for i, sk in enumerate(sc_keys):
        sc = scenarios[sk]
        ry = grid_top - header_h - (i + 1) * cell_h
        label_full = sk + " · " + sc["label"]
        # Locked 12 pt Geist-Bold row label; if it doesn't fit the label
        # column, drop the parenthetical (e.g. "(Zone-C)", "Autor 2024…").
        if pdfmetrics.stringWidth(label_full, "Geist-Bold", 12) > label_col - 4 * mm:
            paren = label_full.find("(")
            if paren > 0:
                label_full = label_full[:paren].strip()
        c.setFont("Geist-Bold", 12)
        c.setFillColor(PURE_BLACK)
        # Wrap, don't shrink-to-fit (Phil-locked 2026-05-13 v4).
        wrapped = wrap_lines(label_full, "Geist-Bold", 12, label_col - 4 * mm)
        ly_lbl = ry + cell_h - 6 * mm
        for line in wrapped:
            c.drawString(M_L, ly_lbl, line)
            ly_lbl -= 13
        sub_y = ly_lbl - 1
        c.setFont("Geist", 9)
        c.setFillColor(GRANITE)
        c.drawString(M_L, sub_y, sc.get("spectrum_position", "")[:50])
        pr = sc.get("probability_per_regime") or sc.get("probability_conditional_per_regime", {})
        for j, reg in enumerate(REGIME_ORDER):
            cx = M_L + label_col + j * cell_w
            triple = pr.get(reg, [0, 0, 0])
            mid = triple[1] if len(triple) > 1 else 0
            cell_col = heat_color(mid)
            c.setFillColor(cell_col)
            c.rect(cx + 1, ry + 1, cell_w - 2, cell_h - 2, stroke=0, fill=1)
            # Median + range as a vertically-centred two-line stack. Median
            # (12 pt Geist-Bold) baseline anchored such that the pair sits at
            # the cell's geometric centre; range bracket (7.5 pt Geist) sits
            # directly below the median with a tight ~3.5 pt visible gap
            # (Phil-locked 2026-05-13 v4 — was 14 pt top-aligned, 7 pt).
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

    legend_y = grid_top - header_h - len(sc_keys) * cell_h - 14 * mm
    _draw_heatmap_legend(c, M_L, legend_y, CONTENT_W)

    note_y = legend_y - 12 * mm
    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    for line in wrap_lines(
        "Cell shading darkens as probability rises. Each cell shows the median "
        "probability with the 80% confidence-interval range below. "
        "S1 (reinstatement revival) collapses from 10% in a growth regime to 5% in post-growth. "
        "S2 (climate-adaptation) is the only scenario whose probability rises into post-growth.",
        "Geist", 9, CONTENT_W,
    ):
        c.drawString(M_L, note_y, line)
        note_y -= 12
    footer(c, 6)
    c.showPage()


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


# ---------------------------------------------------------------------------
# Page 7 — Italy callout (overflow-safe)
# ---------------------------------------------------------------------------

ITALY_STATS = [
    ("Net migration · 2025",          "−485,823",   "Only major EU economy with negative migration."),
    ("Working-age decline to 2050",   "−17.5%",     "Projected EUROPOP2023 trajectory."),
    ("Retirement offset",             "25.3%",      "Well below the 80% buffer threshold."),
    ("Fragility class",               "III",        "Pre-Failure Risk."),
    ("Corridor",                      "C3",         "Displacement Without Absorption."),
]


def page_italy(c: canvasmod.Canvas, sot: dict) -> None:
    page_background(c, PAGE_W, PAGE_H)
    overline(c, M_L, PAGE_H - M_T, "THE OUTLIER")
    y = heading_h2(
        c, M_L, PAGE_H - M_T - 8 * mm,
        "Italy · workforce shrinks before AI displaces a single worker",
    CONTENT_W,
    )
    y = heading_lede(
        c, M_L, y - 4 * mm,
        "Italy is the only major European economy with negative net migration in 2025. "
        "The headline finding is sequencing: demographic contraction precedes the AI shock. "
        "An outlier case: Italy is Corridor C3 with Fragility Class III, "
        "driven by pre-AI demographic contraction.",
    CONTENT_W,
    )

    grid_top = y - 6 * mm
    cols = 3
    gap = 5 * mm
    card_w = (CONTENT_W - gap * (cols - 1)) / cols
    card_h = 46 * mm
    for i, (label, value, note) in enumerate(ITALY_STATS):
        col = i % cols
        row = i // cols
        cx = M_L + col * (card_w + gap)
        cy = grid_top - (row + 1) * card_h - row * gap
        draw_italy_card(c, cx, cy, card_w, card_h, label, value, note)

    # Italy synthesis card — v4.1 sizes to fit (was fixed 50 mm). Blank line
    # between the SYNTHESIS header and the body per Phil-locked 2026-05-13 v4.1.
    body = (
        "Italy is the only country in the suite where the labour-supply contraction is "
        "structural and pre-AI. Caregiving, skilled manual, and medical roles already cannot be "
        "filled. AI displacement compounds, rather than triggers, the gap."
    )
    body_lines = wrap_lines(body, "Geist-LightItalic", 12, CONTENT_W - 12 * mm)
    body_leading = 16  # pt
    header_pad_top = 6 * mm  # padding above "SYNTHESIS" eyebrow
    header_to_body = 16 + 6  # 1 blank line + small extra (pt)
    bottom_pad = 6 * mm
    synth_h = (
        header_pad_top
        + 9  # SYNTHESIS eyebrow at 9 pt
        + header_to_body
        + body_leading * len(body_lines)
        + bottom_pad
    )
    synth_y = grid_top - 2 * card_h - gap - synth_h - 6 * mm
    c.saveState()
    c.setFillColor(DEEP_TEAL)
    c.roundRect(M_L, synth_y, CONTENT_W, synth_h, RADIUS_CARD, stroke=0, fill=1)
    c.setFont("Geist-Bold", 9)
    c.setFillColor(PEARL_WHITE)
    header_y = synth_y + synth_h - header_pad_top - 3  # baseline below pad
    c.drawString(M_L + 6 * mm, header_y, "SYNTHESIS")
    c.setFont("Geist-LightItalic", 12)
    by = header_y - header_to_body
    for line in body_lines:
        c.setFillColor(PEARL_WHITE)
        c.drawString(M_L + 6 * mm, by, line)
        by -= body_leading
    c.restoreState()

    footer(c, 7)
    c.showPage()


def draw_italy_card(c, x, y, w, h, label, value, note):
    """Italy stat card — locked 9 pt label / 22 pt value / 9 pt note.

    Per Phil-locked 2026-05-13 v4 Track 4: no shrink-to-fit; label and note
    wrap to a second line when needed. Value stays fixed at 22 pt (its values
    are short enough to fit at the locked column width).
    """
    c.saveState()
    c.setFillColor(HexColor("#FFFFFF"))
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.5)
    c.roundRect(x, y, w, h, RADIUS_CARD, stroke=1, fill=1)
    draw_card_accent(c, x, y, w, h, ALPINE_RED, side="left", thickness=3)
    avail_w = w - 10 * mm
    # Label — locked 9 pt Geist-Bold, wrap (no shrink-to-fit)
    c.setFont("Geist-Bold", 9)
    c.setFillColor(GRANITE)
    label_lines = wrap_lines(label.upper(), "Geist-Bold", 9, avail_w)
    ly = y + h - 8 * mm
    for line in label_lines:
        c.drawString(x + 5 * mm, ly, line)
        ly -= 11
    # Value — locked 22 pt Geist-Medium
    c.setFont("Geist-Medium", 22)
    c.setFillColor(PURE_BLACK)
    c.drawString(x + 5 * mm, y + h - 24 * mm, value)
    # Note — locked 9 pt Geist (wraps naturally to a second line)
    note_lines = wrap_lines(note, "Geist", 9, avail_w)
    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    note_y = y + 4 * mm + (len(note_lines) - 1) * 12
    for line in note_lines:
        c.drawString(x + 5 * mm, note_y, line)
        note_y -= 12
    c.restoreState()


# ---------------------------------------------------------------------------
# Page 8 — CTA
# ---------------------------------------------------------------------------

DOC_LADDER = [
    # Einfache Sprache card removed (Phil-locked 2026-05-13 v4).
    ("Long-read · 14 pp",
     "Specialist appendix in long-form prose · 3,728 words · four graphics.",
     "synthesis.nexalps.com/long-read"),
    ("Executive brief · 6 pp",
     "Decision-maker version · key tables · strict-zero finding upfront.",
     "synthesis.nexalps.com/executive"),
    ("Specialist document · full",
     "All five lens findings · three corridor sub-clusters · eight scenarios in detail.",
     "synthesis.nexalps.com/specialist"),
]


def page_cta(c: canvasmod.Canvas, sot: dict) -> None:
    page_background(c, PAGE_W, PAGE_H)
    overline(c, M_L, PAGE_H - M_T, "WHERE TO GO NEXT")
    y = heading_h2(c, M_L, PAGE_H - M_T - 8 * mm, "Full read", CONTENT_W)
    y = heading_lede(
        c, M_L, y - 4 * mm,
        "This Visual Read is a derivative. Three longer renders carry the full analysis at "
        "progressive depth.",
    CONTENT_W,
    )

    grid_top = y - 6 * mm
    card_h = 28 * mm
    gap = 5 * mm
    n_cards = len(DOC_LADDER)
    for i, (title, desc, url) in enumerate(DOC_LADDER):
        cy = grid_top - (i + 1) * card_h - i * gap
        draw_doc_card(c, M_L, cy, CONTENT_W, card_h, title, desc, url)

    landing_y = grid_top - n_cards * card_h - (n_cards - 1) * gap - 10 * mm
    # Phil-locked 2026-05-13 v4: label replaced "LANDING" → "Inspect the
    # full analysis at:" (kept at 9 pt Geist-Bold for eyebrow rhythm).
    c.setFont("Geist-Bold", 9)
    c.setFillColor(GRANITE)
    c.drawString(M_L, landing_y, "INSPECT THE FULL ANALYSIS AT:")
    c.setFont("Geist-LightItalic", 20)
    c.setFillColor(DEEP_TEAL)
    c.drawString(M_L, landing_y - 10 * mm, "synthesis.nexalps.com")

    cite_y = landing_y - 24 * mm
    c.setFont("Geist-Bold", 9)
    c.setFillColor(GRANITE)
    c.drawString(M_L, cite_y, "CITE AS")
    c.setFont("Geist", 9)
    c.setFillColor(PURE_BLACK)
    cite = ("Maul, P. (2026). Part 6 · European AI Labour Market Synthesis · "
            "Visual Read. Nexalps.")
    cy = cite_y - 5 * mm
    for line in wrap_lines(cite, "Geist", 9, CONTENT_W):
        c.drawString(M_L, cy, line)
        cy -= 12

    footer(c, 8)
    c.showPage()


def draw_doc_card(c, x, y, w, h, title, desc, url):
    c.saveState()
    c.setFillColor(HexColor("#FFFFFF"))
    c.setStrokeColor(HAIRLINE)
    c.setLineWidth(0.5)
    c.roundRect(x, y, w, h, RADIUS_CARD, stroke=1, fill=1)
    draw_card_accent(c, x, y, w, h, DEEP_TEAL, side="left", thickness=4)
    # Locked 12 pt section sub-header (was 14 pt).
    c.setFont("Geist-Medium", 12)
    c.setFillColor(PURE_BLACK)
    c.drawString(x + 6 * mm, y + h - 9 * mm, title)
    # Locked 9 pt body (was 10 pt).
    c.setFont("Geist", 9)
    c.setFillColor(GRANITE)
    c.drawString(x + 6 * mm, y + h - 15 * mm, desc)
    c.setFont("Geist", 9)
    c.setFillColor(DEEP_TEAL)
    c.drawRightString(x + w - 6 * mm, y + 5 * mm, url)
    c.restoreState()


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def build() -> Path:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    sot = load_sot()
    c = canvasmod.Canvas(str(OUTPUT), pagesize=A4)
    c.setTitle("Part 6 · Visual Read · Nexalps")
    c.setAuthor("Philipp Maul")
    c.setSubject("European AI Labour Market Synthesis · Part 6 of 7")
    page_cover(c, sot)
    page_lenses(c, sot)
    page_corridors(c, sot)
    page_classes(c, sot)
    page_reskilling(c, sot)
    page_scenarios(c, sot)
    page_italy(c, sot)
    page_cta(c, sot)
    c.save()
    return OUTPUT


if __name__ == "__main__":
    out = build()
    print(f"Wrote {out} ({out.stat().st_size:,} bytes)")
