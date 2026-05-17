#!/usr/bin/env python3
"""Render the Layer 6 Specialist Long-Read markdown to a Nexalps-styled A4 PDF.

Extends the patterns in projects/job-scout-agent/generate_pdf_generic.py:
  * Geist font family registration (300/400/500/600/700)
  * ReportLab Platypus story-based composition

Style: Nexalps consulting deliverable.
  * Pearl-white background #F8F9FA, pure-black text
  * Deep-teal-text #087569 accent (WCAG-AA on white)
  * Granite-gray #4A5568 secondary
  * A4 portrait, 25 mm margins (160 mm content width)

Source: layer-6-deliverable-long-read.md (sibling to repo root).
Graphics: site/exports/long-read/*.png (PNG embed, SVG kept for site).
Output:  layer-6-deliverable-long-read.pdf at repo root.

v2 changes (2026-05-08):
  * Cover page handler — <!-- COVER: ... --> marker emits light-italic giant
    headline on pearl-white, content begins page 2.
  * Pull-quote parser — `> ...` blockquote lines render in Geist-LightItalic
    pullquote style.
  * Margins reduced to 25 mm × 25 mm (160 mm content width).
  * KeepTogether wrapping for heading+first-paragraph, image+caption,
    pull-quote+surrounding-paragraph.
  * Sources table column widths weighted 40/60 for 2-col Source/How-informs
    tables.
  * Orphan/widow control on body Paragraphs.

Usage:
  python3 tools/long-read-pdf-gen.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Iterable

# Shared style module — registers Geist fonts, sets rl_config.invariant=1,
# and exports the v4.1 palette. Import before any other reportlab.* import
# so the deterministic-build flags are set in time.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _pdf_style import (
    HexColor,
    PEARL_WHITE, PURE_BLACK,
    DEEP_TEAL, DEEP_TEAL_BG,
    GRANITE, GRANITE_DARK, GRANITE_LIGHT, GRANITE_LIGHTER,
    HAIRLINE,
    ALPINE_GOLD, ALPINE_RED, GLACIER_BLUE, CLASS_IV_WINE,
    HEAT_1, HEAT_2, HEAT_3, HEAT_4, HEAT_5, HEAT_6,
    CLS_COLOR, CLS_LABEL,
)

from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    Image,
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


REPO = Path(__file__).resolve().parent.parent
MARKDOWN = REPO / "docs" / "layer-6-deliverable-long-read.md"
GRAPHICS = REPO / "site" / "exports" / "long-read"
OUTPUT = REPO / "docs" / "layer-6-deliverable-long-read.pdf"

# Image source that pins the fragility-class legend below it in the Long-Read.
CORRIDOR_MAP_SRC_SUFFIX = "corridor-map-nexalps.png"

# Page setup — 25 mm margins per Bundle N3 v2 spec (content 160 mm).
PAGE_W, PAGE_H = A4
MARGIN_LEFT = 25 * mm
MARGIN_RIGHT = 25 * mm
MARGIN_TOP = 25 * mm
MARGIN_BOTTOM = 22 * mm
CONTENT_WIDTH = PAGE_W - MARGIN_LEFT - MARGIN_RIGHT

# ---------------------------------------------------------------------------
# Styles
# ---------------------------------------------------------------------------

def _styles() -> dict[str, ParagraphStyle]:
    """v4.1 type scale — locked sizes: 36 / 30 / 22 / 20 / 16 / 12 / 9 / 7.5 pt.

    Eliminated (FORBIDDEN): 7, 8, 8.5, 9.5, 10, 11, 14 pt.
    Long-Read prose leading on 9pt body sits at 13pt (readability flex from 12).
    Italic-to-upright flip applied: lede + italic_meta (caption) move from
    Geist-Italic / Geist-Light to upright Geist. Pull-quotes keep Geist-LightItalic
    as the reserved prose-callout exception.
    """
    base = dict(fontName="Geist", textColor=PURE_BLACK, alignment=TA_LEFT)
    return {
        # H2: locked 16 pt Geist-Medium (was 22 pt in pre-v4.1)
        "h2": ParagraphStyle(
            "h2", **{**base, "fontName": "Geist-Medium"}, fontSize=16,
            leading=20, spaceBefore=9 * mm, spaceAfter=3 * mm,
            keepWithNext=1,
        ),
        # H3 / sub-header: locked 12 pt Geist-Medium
        "h3": ParagraphStyle(
            "h3", **{**base, "fontName": "Geist-Medium"}, fontSize=12,
            leading=16, spaceBefore=4 * mm, spaceAfter=2 * mm,
            keepWithNext=1,
        ),
        # Eyebrow / overline: 9 pt Geist-Bold
        "overline": ParagraphStyle(
            "overline", **{**base, "fontName": "Geist-Bold", "textColor": GRANITE},
            fontSize=9, leading=11, spaceAfter=2 * mm,
        ),
        # Lede: v4.1 flipped from Geist-Italic to upright Geist; bumped to
        # 10 pt 2026-05-13 v4.2 (Phil-locked Long-Read readability call).
        "lede": ParagraphStyle(
            "lede", **{**base, "fontName": "Geist", "textColor": GRANITE},
            fontSize=10, leading=14, spaceAfter=3 * mm,
            allowWidows=0, allowOrphans=0,
        ),
        # Body: 10 pt; leading 14 (Phil-locked Long-Read 2026-05-13 v4.2 —
        # re-opens 10 pt for Long-Read prose; Visual Read stays at 9 pt).
        "body": ParagraphStyle(
            "body", **base, fontSize=10, leading=14,
            spaceAfter=2.5 * mm,
            allowWidows=0, allowOrphans=0,
        ),
        # Body intro: identical to body but with keepWithNext=1 — applied to
        # paragraphs that immediately precede a leadin so the intro sentence
        # never orphans at the bottom of a page while its leadin lands on the
        # next (Phil-locked v4.2.2).
        "body_intro": ParagraphStyle(
            "body_intro", **base, fontSize=10, leading=14,
            spaceAfter=2.5 * mm, keepWithNext=1,
            allowWidows=0, allowOrphans=0,
        ),
        # Lead-in: bold mini-header (single-line `**Bold**` markdown blocks).
        # 10 pt Geist-Bold; spaceBefore ≫ spaceAfter so it visually binds to
        # the body that follows, not the content above (Phil-locked v4.2).
        "leadin": ParagraphStyle(
            "leadin",
            **{**base, "fontName": "Geist-Bold", "textColor": PURE_BLACK},
            fontSize=10, leading=14, spaceBefore=6 * mm, spaceAfter=1.5 * mm,
            keepWithNext=1,
        ),
        # Body lead-in: regular paragraph that opens with `**Word.**` or
        # `**Word:**` — a section-end summary marker (e.g. "**Synthesis.**").
        # Same look as body but with generous spaceBefore so it doesn't crowd
        # the previous block (Phil-locked v4.2).
        "body_leadin": ParagraphStyle(
            "body_leadin", **base, fontSize=10, leading=14,
            spaceBefore=6 * mm, spaceAfter=2.5 * mm,
            allowWidows=0, allowOrphans=0,
        ),
        # Byline: 9 pt
        "byline": ParagraphStyle(
            "byline", **{**base, "textColor": GRANITE},
            fontSize=9, leading=12, spaceAfter=1 * mm,
        ),
        # Bullet: 10 pt (matches body — Phil-locked v4.2)
        "bullet": ParagraphStyle(
            "bullet", **base, fontSize=10, leading=14,
            leftIndent=5 * mm, bulletIndent=0, spaceAfter=1 * mm,
        ),
        # Caption: v4.1 flipped from Geist-Italic to upright Geist, 9 pt.
        # Style name kept ("italic_meta") to avoid downstream rename churn —
        # but inline-italic <i>...</i> wrappers around captions in the builder
        # are also stripped (see _build_blocks) so the upright rule holds.
        "italic_meta": ParagraphStyle(
            "italic_meta", **{**base, "fontName": "Geist", "textColor": GRANITE},
            fontSize=9, leading=12, spaceAfter=1 * mm,
        ),
        # Pull-quote: reserved prose-callout — Geist-LightItalic exception.
        # Size stays in display range (20 pt sits on 36/30/22/20 ladder).
        "pullquote": ParagraphStyle(
            "pullquote",
            **{**base, "fontName": "Geist-LightItalic", "textColor": DEEP_TEAL},
            fontSize=20, leading=26, spaceBefore=4 * mm, spaceAfter=4 * mm,
            leftIndent=10 * mm, rightIndent=10 * mm,
        ),
        # Table header: 10 pt Geist-Bold (Phil-locked v4.2 — matches body)
        "table_th": ParagraphStyle(
            "table_th", **{**base, "fontName": "Geist-Bold", "textColor": GRANITE},
            fontSize=10, leading=13,
        ),
        # Table body: 10 pt (Phil-locked v4.2 — matches body)
        "table_td": ParagraphStyle(
            "table_td", **base, fontSize=10, leading=13,
        ),
        # Display-value cell: 12 pt Geist-Medium (was 14 pt)
        "table_td_bold": ParagraphStyle(
            "table_td_bold", **{**base, "fontName": "Geist-Medium"},
            fontSize=12, leading=15,
        ),
        # Compact sources-table body: 10 pt (Phil-locked v4.2 — matches body)
        "table_td_small": ParagraphStyle(
            "table_td_small", **base, fontSize=10, leading=13,
        ),
        # Section number: 9 pt Geist-Bold teal
        "section_num": ParagraphStyle(
            "section_num", **{**base, "fontName": "Geist-Bold", "textColor": DEEP_TEAL},
            fontSize=9, leading=11, spaceAfter=1 * mm,
        ),
        # Title (H1 — page-2 doc title): 22 pt Geist-Medium (display range)
        "title": ParagraphStyle(
            "title", **{**base, "fontName": "Geist-Medium"}, fontSize=22,
            leading=26, spaceBefore=4 * mm, spaceAfter=4 * mm,
            keepWithNext=1,
        ),
        # Cover headline: 36 pt Geist-LightItalic (top of display ladder)
        "cover_headline": ParagraphStyle(
            "cover_headline", fontName="Geist-LightItalic",
            fontSize=36, leading=44, textColor=PURE_BLACK,
            alignment=TA_LEFT, spaceBefore=0, spaceAfter=0,
        ),
        # Cover overline: 9 pt Geist-Bold
        "cover_overline": ParagraphStyle(
            "cover_overline", fontName="Geist-Bold", fontSize=9,
            leading=11, textColor=GRANITE, alignment=TA_LEFT,
            spaceAfter=4 * mm,
        ),
    }


# ---------------------------------------------------------------------------
# Markdown → flowables (intentionally minimal, tuned to this document)
# ---------------------------------------------------------------------------

INLINE_BOLD = re.compile(r"\*\*(.+?)\*\*")
INLINE_ITALIC = re.compile(r"(?<!\*)\*([^*]+?)\*(?!\*)")
INLINE_CODE = re.compile(r"`([^`]+?)`")
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
COVER_MARKER = re.compile(r"<!--\s*COVER:\s*(.+?)\s*-->", re.DOTALL)


def _inline(text: str) -> str:
    """Convert markdown inline to ReportLab Paragraph mini-language."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = INLINE_BOLD.sub(r"<b>\1</b>", text)
    text = INLINE_ITALIC.sub(r"<i>\1</i>", text)
    text = INLINE_CODE.sub(r'<font name="Geist" color="#4A5568">\1</font>', text)
    text = LINK.sub(r'<link href="\2" color="#087569">\1</link>', text)
    return text


def _split_table(lines: list[str]) -> tuple[list[list[str]], int]:
    """Pull a contiguous markdown pipe-table starting at lines[0]."""
    rows = []
    consumed = 0
    while consumed < len(lines) and lines[consumed].lstrip().startswith("|"):
        rows.append(
            [c.strip() for c in lines[consumed].strip().strip("|").split("|")]
        )
        consumed += 1
    return rows, consumed


def _block_iter(md: str) -> Iterable[tuple[str, object]]:
    """Yield (kind, payload) blocks: cover, h1, h2, h3, p, ul, hr, image,
    table, pullquote, italic_meta."""
    # Strip & yield cover marker first
    cover_match = COVER_MARKER.search(md)
    if cover_match:
        yield ("cover", cover_match.group(1).strip())
        # Remove the marker (and one trailing blank line) from the body to parse.
        md = md.replace(cover_match.group(0), "", 1).lstrip("\n")

    raw = md.splitlines()
    i = 0
    n = len(raw)
    while i < n:
        line = raw[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped == "---":
            yield ("hr", None)
            i += 1
            continue

        # Explicit page-break marker (Phil-locked v4.2.x).
        if stripped == "<!-- PAGEBREAK -->":
            yield ("pagebreak", None)
            i += 1
            continue

        if stripped.startswith("# "):
            yield ("h1", stripped[2:].strip())
            i += 1
            continue

        if stripped.startswith("## "):
            yield ("h2", stripped[3:].strip())
            i += 1
            continue

        if stripped.startswith("### "):
            yield ("h3", stripped[4:].strip())
            i += 1
            continue

        # Image block (line is a single image).
        m = IMAGE.fullmatch(stripped)
        if m:
            yield ("image", (m.group(1), m.group(2)))
            i += 1
            continue

        # Pipe table (header row starts with '|').
        if stripped.startswith("|") and i + 1 < n and "---" in raw[i + 1]:
            rows, used = _split_table(raw[i:])
            yield ("table", rows)
            i += used
            continue

        # Pull-quote (blockquote `> ...` — single or multi-line).
        if stripped.startswith("> "):
            quote_lines = []
            while i < n and raw[i].lstrip().startswith("> "):
                quote_lines.append(raw[i].lstrip()[2:].strip())
                i += 1
            yield ("pullquote", " ".join(quote_lines))
            continue

        # Bold-only single-line block → lead-in mini-header (Phil-locked v4.2).
        # Matches `**…**` on its own line, e.g. lens headlines.
        if (
            stripped.startswith("**")
            and stripped.endswith("**")
            and stripped.count("**") == 2
            and len(stripped) > 4
        ):
            yield ("leadin", stripped[2:-2])
            i += 1
            continue

        # Italic-only single-line block → meta caption.
        if stripped.startswith("*") and stripped.endswith("*") and stripped.count("*") == 2:
            yield ("italic_meta", stripped[1:-1])
            i += 1
            continue

        # Bullet list (- ... contiguous).
        if stripped.startswith("- "):
            items = []
            while i < n and raw[i].lstrip().startswith("- "):
                items.append(raw[i].lstrip()[2:].strip())
                i += 1
            yield ("ul", items)
            continue

        # Default: paragraph (collect until blank line).
        para_lines = [stripped]
        i += 1
        while i < n and raw[i].strip() and not raw[i].lstrip().startswith(
            ("- ", "## ", "### ", "# ", "|", "!", ">")
        ) and raw[i].strip() != "---":
            para_lines.append(raw[i].strip())
            i += 1
        para = " ".join(para_lines)
        # body_leadin: paragraph starts with `**Word.**` or `**Word:**` —
        # a short bold prefix ending in period/colon (section-end summary
        # markers like "**Synthesis.**" or "**Build:**"). Distinct from
        # `**S1 Reinstatement Revival**` where the bold has no trailing
        # punctuation (those render as regular p with inline bold).
        if para.startswith("**"):
            close = para.find("**", 2)
            if 0 < close and close - 2 <= 30 and para[close - 1] in ".:":
                yield ("body_leadin", para)
                continue
        yield ("p", para)


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

# Total page count is filled in by the second pass (see build_pdf). The first
# build pass uses a placeholder so flowable pagination matches; the second pass
# uses the real count so the footer reads "Page N / total".
_TOTAL_PAGES: int | None = None


def _on_page(canvas, doc):
    """Draw pearl-white page background and v4.1 footer chrome.

    Footer: 7.5 pt Geist GRANITE — left "Part 6 · Long Read",
    center "Nexalps · Part 6 of 7", right "Page N / total".
    Vocabulary lock: "Part 6" (not "Layer 6").
    """
    canvas.saveState()
    canvas.setFillColor(PEARL_WHITE)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    # Footer — 7.5 pt micro-chrome
    canvas.setFont("Geist", 7.5)
    canvas.setFillColor(GRANITE)
    y = 12 * mm
    total = _TOTAL_PAGES if _TOTAL_PAGES is not None else doc.page
    canvas.drawString(MARGIN_LEFT, y, "Part 6 · Long Read")
    canvas.drawCentredString(PAGE_W / 2, y, "Nexalps · Part 6 of 7")
    canvas.drawRightString(PAGE_W - MARGIN_RIGHT, y, f"Page {doc.page} / {total}")
    canvas.restoreState()


def _on_cover_page(canvas, doc):
    """Cover page: pearl-white only, no footer."""
    canvas.saveState()
    canvas.setFillColor(PEARL_WHITE)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canvas.restoreState()


def _image_flowable(path: str, alt: str) -> Image | Paragraph:
    """Embed PNG (preferred over SVG for ReportLab without svglib).

    The dot-map (corridor-map-nexalps.png) renders near-square; at full content
    width it dominates the page. Phil-locked v4.2.x: render the dot-map at 70 %
    of content width so the map + class legend + caption fit one page together.
    """
    p = (REPO / path).resolve()
    if not p.exists():
        if p.suffix.lower() == ".svg":
            png = p.with_suffix(".png")
            if png.exists():
                p = png
    if not p.exists():
        return Paragraph(f"<i>[missing graphic: {path}]</i>", _styles()["italic_meta"])
    img = Image(str(p))
    ratio = img.imageHeight / img.imageWidth
    draw_w = (
        CONTENT_WIDTH * 0.70
        if path.endswith(CORRIDOR_MAP_SRC_SUFFIX)
        else CONTENT_WIDTH
    )
    img.drawWidth = draw_w
    img.drawHeight = draw_w * ratio
    img.hAlign = "CENTER"
    return img


def _table_flowable(rows: list[list[str]], styles: dict) -> Table:
    """Markdown pipe-table → ReportLab Table.

    Header heuristics:
      * 4-column at-a-glance (Markets/Class I/Breach/Reskilling) → equal cols,
        bold-numeric heuristic on second body row.
      * 2-column Source / How informs → 40/60 weighted, smaller body cell.
    """
    header = rows[0]
    body = rows[2:]
    n_cols = len(header)

    is_sources_table = (
        n_cols == 2
        and len(header) == 2
        and "Source" in header[0]
    )
    is_at_a_glance = n_cols == 4 and "Markets scored" in header[0]

    cell_style_th = styles["table_th"]
    cell_style_td = styles["table_td_small"] if is_sources_table else styles["table_td"]
    cell_style_td_bold = styles["table_td_bold"]

    data = [[Paragraph(_inline(c), cell_style_th) for c in header]]
    for r in body:
        is_numeric_row = all(len(c) <= 32 for c in r) and any(
            re.match(r"^\*\*[\d,. M%kK]+\*\*$", c) for c in r
        )
        s = cell_style_td_bold if is_numeric_row else cell_style_td
        data.append([Paragraph(_inline(c), s) for c in r])

    if is_sources_table:
        col_w = [CONTENT_WIDTH * 0.4, CONTENT_WIDTH * 0.6]
    elif is_at_a_glance:
        # Wider 2nd/3rd cells so "Countries below adaptive-capacity floor"
        # and "Strict rule: 0." don't break mid-word.
        col_w = [
            CONTENT_WIDTH * 0.22,
            CONTENT_WIDTH * 0.22,
            CONTENT_WIDTH * 0.34,
            CONTENT_WIDTH * 0.22,
        ]
    else:
        col_w = [CONTENT_WIDTH / n_cols] * n_cols

    t = Table(data, colWidths=col_w, repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), PEARL_WHITE),
                ("LINEBELOW", (0, 0), (-1, 0), 0.6, GRANITE),
                ("LINEBELOW", (0, 1), (-1, -2), 0.3, HAIRLINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return t


def _class_legend_flowable(styles: dict) -> Table:
    """4-cell horizontal legend matching v4.1 dot-map style.

    Each cell: filled circle (CLS_COLOR) + "Class X — Label". Rendered as a
    1-row Table with 4 equal columns so the items align across the page width.
    The bullet uses an inline `<font color="...">●</font>` because the
    italic_meta Paragraph style already supplies the 9-pt Geist body label.
    """
    cells = []
    for cls in ["I", "II", "III", "IV"]:
        swatch_hex = CLS_COLOR[cls].hexval()[2:]  # strip "0x" → "rrggbb"
        cell_html = (
            f'<font color="#{swatch_hex}">&#9679;</font>&nbsp;&nbsp;'
            f'Class {cls} · {CLS_LABEL[cls]}'
        )
        cells.append(Paragraph(cell_html, styles["italic_meta"]))
    col_w = [CONTENT_WIDTH / 4] * 4
    t = Table([cells], colWidths=col_w)
    t.setStyle(
        TableStyle(
            [
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ]
        )
    )
    return t


def _build_blocks(md: str, styles: dict) -> list:
    """Build flowables with KeepTogether grouping for headings + first paragraph,
    images + captions, and pull-quote + adjacent paragraph."""
    blocks = list(_block_iter(md))
    story: list = []
    saw_first_h2 = False  # H2 = top-level after refactor
    saw_title = False

    pending_heading = None  # (kind, paragraph) — wait for next paragraph to group

    def flush_pending(s: list):
        if pending_heading is not None:
            s.append(pending_heading)
        return None

    i = 0
    n = len(blocks)
    while i < n:
        kind, payload = blocks[i]

        if kind == "cover":
            # Cover-only page: light-italic giant headline, no footer.
            cover_text = payload
            story.append(
                Paragraph(
                    "Part 6 · European AI Labour Market Synthesis · Long-Read · First Edition",
                    styles["cover_overline"],
                )
            )
            story.append(Spacer(1, 60 * mm))
            story.append(Paragraph(_inline(cover_text), styles["cover_headline"]))
            story.append(PageBreak())
            i += 1
            continue

        if kind == "h1":
            story.append(Paragraph(_inline(payload), styles["title"]))
            saw_title = True
            i += 1
            continue

        if kind == "h2":
            # Heading + first paragraph (or image) → KeepTogether.
            heading = Paragraph(_inline(payload), styles["h2"])
            group = [heading]
            j = i + 1
            while j < n and blocks[j][0] in ("hr", "italic_meta"):
                j += 1
            if j < n and blocks[j][0] in ("p", "image"):
                next_kind, next_payload = blocks[j]
                if next_kind == "image":
                    img = _image_flowable(next_payload[1], next_payload[0])
                    cap = Paragraph(
                        _inline(next_payload[0]) if next_payload[0] else "&nbsp;",
                        styles["italic_meta"],
                    )
                    group.extend([Spacer(1, 2 * mm), img, cap, Spacer(1, 2 * mm)])
                    story.append(KeepTogether(group))
                    i = j + 1
                    continue
                first_para = Paragraph(_inline(next_payload), styles["body"])
                group.append(first_para)
                story.append(KeepTogether(group))
                i = j + 1
                continue
            story.append(heading)
            i += 1
            continue

        if kind == "h3":
            heading = Paragraph(_inline(payload), styles["h3"])
            j = i + 1
            while j < n and blocks[j][0] in ("hr", "italic_meta"):
                j += 1
            if j < n and blocks[j][0] in ("p", "table"):
                if blocks[j][0] == "p":
                    first_para = Paragraph(_inline(blocks[j][1]), styles["body"])
                    story.append(KeepTogether([heading, first_para]))
                    i = j + 1
                    continue
                if blocks[j][0] == "table":
                    # v4.2.x: emit H3 with keepWithNext OFF so a splittable
                    # table (e.g. Tier 1's 41 rows) lands on the same page as
                    # its heading rather than pushing both to the next page.
                    # The table splits naturally across pages from there.
                    h3_inline = ParagraphStyle(
                        "_h3_inline", parent=styles["h3"], keepWithNext=0,
                    )
                    tbl = _table_flowable(blocks[j][1], styles)
                    story.append(Paragraph(_inline(payload), h3_inline))
                    story.append(tbl)
                    story.append(Spacer(1, 3 * mm))
                    i = j + 1
                    continue
            story.append(heading)
            i += 1
            continue

        if kind == "p":
            # If the next block is a leadin, glue the intro paragraph to it
            # via keepWithNext — prevents the intro from orphaning when its
            # following section header lands on the next page.
            style_key = (
                "body_intro"
                if i + 1 < n and blocks[i + 1][0] == "leadin"
                else "body"
            )
            story.append(Paragraph(_inline(payload), styles[style_key]))
            i += 1
            continue

        if kind == "leadin":
            story.append(Paragraph(_inline(payload), styles["leadin"]))
            i += 1
            continue

        if kind == "body_leadin":
            story.append(Paragraph(_inline(payload), styles["body_leadin"]))
            i += 1
            continue

        if kind == "ul":
            for item in payload:
                story.append(
                    Paragraph(f"•&nbsp;&nbsp;{_inline(item)}", styles["bullet"])
                )
            story.append(Spacer(1, 1 * mm))
            i += 1
            continue

        if kind == "image":
            alt, src = payload
            img = _image_flowable(src, alt)
            cap = Paragraph(
                _inline(alt) if alt else "&nbsp;",
                styles["italic_meta"],
            )
            story.append(Spacer(1, 2 * mm))
            group = [img, cap]
            if src.endswith(CORRIDOR_MAP_SRC_SUFFIX):
                group.append(Spacer(1, 1.5 * mm))
                group.append(_class_legend_flowable(styles))
            story.append(KeepTogether(group))
            story.append(Spacer(1, 2 * mm))
            i += 1
            continue

        if kind == "italic_meta":
            story.append(Paragraph(_inline(payload), styles["italic_meta"]))
            i += 1
            continue

        if kind == "pagebreak":
            story.append(PageBreak())
            i += 1
            continue

        if kind == "hr":
            story.append(Spacer(1, 2 * mm))
            story.append(HRFlowable(width="100%", thickness=0.4, color=HAIRLINE))
            story.append(Spacer(1, 2 * mm))
            i += 1
            continue

        if kind == "pullquote":
            # Strip any surrounding quote characters the markdown source
            # already includes — the pullquote style adds visual emphasis,
            # and markdown convention varies on whether to quote inside `>`.
            quote_text = payload.strip()
            if (quote_text.startswith('"') and quote_text.endswith('"')) or (
                quote_text.startswith("“") and quote_text.endswith("”")
            ):
                quote_text = quote_text[1:-1].strip()
            # Anchor pull-quote to the previous paragraph if possible.
            quote = Paragraph(f'"{_inline(quote_text)}"', styles["pullquote"])
            # Pull last body paragraph from story to KeepTogether with the quote.
            anchor = None
            for k in range(len(story) - 1, -1, -1):
                if isinstance(story[k], Paragraph) and story[k].style.name in ("body", "lede"):
                    anchor = story.pop(k)
                    # also remove a trailing Spacer if present right after
                    break
            if anchor is not None:
                story.append(KeepTogether([anchor, quote]))
            else:
                story.append(quote)
            i += 1
            continue

        if kind == "table":
            tbl = _table_flowable(payload, styles)
            story.append(tbl)
            story.append(Spacer(1, 3 * mm))
            i += 1
            continue

        i += 1
    return story


def build_pdf() -> Path:
    """Two-pass build so the footer can show 'Page N / total'.

    Pass 1: build to /dev/null-equivalent (BytesIO would also work, but
    SimpleDocTemplate writes to a path) just to count pages. We use a
    sibling tmp file in the same dir so atomic-write semantics still hold
    if Phil's running this on a synced volume.
    Pass 2: rebuild to the real path with _TOTAL_PAGES set.
    """
    global _TOTAL_PAGES
    md = MARKDOWN.read_text(encoding="utf-8")

    # Pass 1 — count pages.
    _TOTAL_PAGES = None
    tmp_path = OUTPUT.with_suffix(".tmp.pdf")
    doc1 = SimpleDocTemplate(
        str(tmp_path), pagesize=A4,
        leftMargin=MARGIN_LEFT, rightMargin=MARGIN_RIGHT,
        topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
        title="European AI Labour Market Synthesis · Long Read",
        author="Philipp Maul",
        subject="Part 6 Specialist Long-Read",
    )
    story1 = _build_blocks(md, _styles())
    doc1.build(story1, onFirstPage=_on_cover_page, onLaterPages=_on_page)
    _TOTAL_PAGES = doc1.page
    if tmp_path.exists():
        tmp_path.unlink()

    # Pass 2 — render with total known.
    doc2 = SimpleDocTemplate(
        str(OUTPUT), pagesize=A4,
        leftMargin=MARGIN_LEFT, rightMargin=MARGIN_RIGHT,
        topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
        title="European AI Labour Market Synthesis · Long Read",
        author="Philipp Maul",
        subject="Part 6 Specialist Long-Read",
    )
    story2 = _build_blocks(md, _styles())
    doc2.build(story2, onFirstPage=_on_cover_page, onLaterPages=_on_page)
    return OUTPUT


if __name__ == "__main__":
    out = build_pdf()
    print(f"PDF saved: {out}")
