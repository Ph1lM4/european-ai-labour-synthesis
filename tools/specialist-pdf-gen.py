#!/usr/bin/env python3
"""Render the Part 6 Specialist Appendix markdown to a Nexalps-styled A4 PDF.

Architecture mirrors tools/long-read-pdf-gen.py (ReportLab Platypus, Story-based
composition); design tokens follow tools/visual-read-pdf-gen.py v4.1 (locked
type scale, palette, footer chrome, cover treatment).

Source: docs/layer-6-deliverable-document.md (53 KB Specialist appendix).
Output: docs/layer-6-deliverable-specialist.pdf (depth document; ~30-50 pp).

v4.1 highlights:
  * Type scale locked: 36 / 30 / 22 / 20 (display) · 16 H2 / 12 sub-header /
    9 body, lede, eyebrow / 7.5 footer chrome. 4th-tier micro-anchor uses
    9 pt Geist-Bold (eyebrow style) for ###-equivalent.
  * Lede upright (not italic).
  * Footer 7.5 pt Geist GRANITE; left "Part 6 · Specialist Document",
    center "Nexalps · Part 6 of 7", right "Page N / total".
  * Cover: overline + 36 pt Geist-LightItalic hero + 9 pt upright lede +
    byline. No "PART 6 OF 7" on cover surface (only in footer).
  * Last page: doc ladder (long-read 14 pp / executive brief 6 pp; specialist
    omitted) + landing URL synthesis.nexalps.com at 20 pt Geist-LightItalic.
  * Auto-generated Table of Contents (Platypus TableOfContents flowable),
    pulling H2 entries from the source.
  * Code blocks (fenced ``` blocks) rendered in 9 pt mono-fallback (Geist
    upright, GRANITE_DARK, slight indent + hairline left rule).
  * Pipe tables rendered via Platypus Table; header Geist-Bold GRANITE,
    body Geist 9 pt, hairline borders.

Usage:
  python3 tools/specialist-pdf-gen.py
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
    ALPINE_GOLD, ALPINE_RED, CLASS_IV_WINE, GLACIER_BLUE,
    DOC_VARIANTS, LADDER_URL, doc_ladder_others,
)

from reportlab.lib.enums import TA_LEFT, TA_CENTER
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
from reportlab.platypus.tableofcontents import TableOfContents


# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

REPO = Path(__file__).resolve().parent.parent
MARKDOWN = REPO / "docs" / "layer-6-deliverable-document.md"
OUTPUT = REPO / "docs" / "layer-6-deliverable-specialist.pdf"

# ---------------------------------------------------------------------------
# Page geometry — 25 mm margins (matches visual-read + long-read)
# ---------------------------------------------------------------------------

PAGE_W, PAGE_H = A4
MARGIN_LEFT = 25 * mm
MARGIN_RIGHT = 25 * mm
MARGIN_TOP = 25 * mm
MARGIN_BOTTOM = 22 * mm
CONTENT_WIDTH = PAGE_W - MARGIN_LEFT - MARGIN_RIGHT


# ---------------------------------------------------------------------------
# Styles — v4.1 locked type scale
# ---------------------------------------------------------------------------

def _styles() -> dict[str, ParagraphStyle]:
    base = dict(fontName="Geist", textColor=PURE_BLACK, alignment=TA_LEFT)
    return {
        # Cover
        "cover_overline": ParagraphStyle(
            "cover_overline", fontName="Geist-Bold", fontSize=9,
            leading=12, textColor=GRANITE, alignment=TA_LEFT,
            spaceAfter=4 * mm,
        ),
        "cover_headline": ParagraphStyle(
            "cover_headline", fontName="Geist-LightItalic",
            fontSize=36, leading=44, textColor=PURE_BLACK,
            alignment=TA_LEFT,
        ),
        "cover_lede": ParagraphStyle(
            "cover_lede", fontName="Geist", fontSize=9, leading=13,
            textColor=GRANITE, alignment=TA_LEFT, spaceAfter=4 * mm,
        ),
        "cover_byline": ParagraphStyle(
            "cover_byline", fontName="Geist-Bold", fontSize=9, leading=12,
            textColor=GRANITE, alignment=TA_LEFT,
        ),
        # TOC
        "toc_title": ParagraphStyle(
            "toc_title", fontName="Geist-Medium", fontSize=22,
            leading=28, textColor=PURE_BLACK,
            spaceBefore=0, spaceAfter=6 * mm,
        ),
        # Body hierarchy — v4.1 locked
        "h1": ParagraphStyle(
            "h1", **{**base, "fontName": "Geist-Medium"}, fontSize=22,
            leading=28, spaceBefore=0, spaceAfter=4 * mm,
            keepWithNext=1,
        ),
        "h2": ParagraphStyle(
            "h2", **{**base, "fontName": "Geist-Medium"}, fontSize=16,
            leading=20, spaceBefore=8 * mm, spaceAfter=3 * mm,
            keepWithNext=1,
        ),
        "h3": ParagraphStyle(
            # 12 pt sub-header (third tier)
            "h3", **{**base, "fontName": "Geist-Medium"}, fontSize=12,
            leading=15, spaceBefore=4 * mm, spaceAfter=2 * mm,
            keepWithNext=1,
        ),
        "h4": ParagraphStyle(
            # 4th-tier micro-anchor — 9 pt Geist-Bold (eyebrow style)
            "h4", **{**base, "fontName": "Geist-Bold", "textColor": GRANITE_DARK},
            fontSize=9, leading=12, spaceBefore=3 * mm, spaceAfter=1 * mm,
            keepWithNext=1,
        ),
        "overline": ParagraphStyle(
            "overline", **{**base, "fontName": "Geist-Bold", "textColor": GRANITE},
            fontSize=9, leading=12, spaceAfter=2 * mm,
        ),
        "lede": ParagraphStyle(
            # v4.1 lede is UPRIGHT (not italic)
            "lede", **{**base, "fontName": "Geist", "textColor": GRANITE},
            fontSize=9, leading=13, spaceAfter=3 * mm,
            allowWidows=0, allowOrphans=0,
        ),
        "body": ParagraphStyle(
            # 9 pt body, 13 pt leading for sustained reading over many pages
            "body", **base, fontSize=9, leading=13,
            spaceAfter=2.5 * mm,
            allowWidows=0, allowOrphans=0,
        ),
        "bullet": ParagraphStyle(
            "bullet", **base, fontSize=9, leading=13,
            leftIndent=5 * mm, bulletIndent=0, spaceAfter=1.2 * mm,
            allowWidows=0, allowOrphans=0,
        ),
        "italic_meta": ParagraphStyle(
            "italic_meta", **{**base, "fontName": "Geist-Italic", "textColor": GRANITE},
            fontSize=9, leading=12, spaceAfter=1 * mm,
        ),
        "code_block": ParagraphStyle(
            # Fenced code block — Geist upright, GRANITE_DARK, indented +
            # hairline left rule visually delineates from prose.
            "code_block", fontName="Geist", fontSize=8.5, leading=12,
            textColor=GRANITE_DARK, alignment=TA_LEFT,
            leftIndent=4 * mm, rightIndent=2 * mm,
            spaceBefore=2 * mm, spaceAfter=2 * mm,
            borderColor=HAIRLINE, borderPadding=4,
        ),
        # Table cells
        "table_th": ParagraphStyle(
            "table_th", **{**base, "fontName": "Geist-Bold", "textColor": GRANITE},
            fontSize=8.5, leading=11,
        ),
        "table_td": ParagraphStyle(
            "table_td", **base, fontSize=8.5, leading=11,
        ),
        # Closing-page (ladder)
        "ladder_overline": ParagraphStyle(
            "ladder_overline", fontName="Geist-Bold", fontSize=9,
            leading=12, textColor=GRANITE, alignment=TA_LEFT,
            spaceAfter=4 * mm,
        ),
        "ladder_url": ParagraphStyle(
            "ladder_url", fontName="Geist-LightItalic", fontSize=20,
            leading=26, textColor=PURE_BLACK, alignment=TA_LEFT,
            spaceAfter=8 * mm,
        ),
        "ladder_row": ParagraphStyle(
            "ladder_row", fontName="Geist", fontSize=9, leading=14,
            textColor=GRANITE, alignment=TA_LEFT, spaceAfter=1.5 * mm,
        ),
        # Doc-card meta / title / audience / body — 4-line card to match Executive.
        "card_meta": ParagraphStyle(
            "card_meta", fontName="Geist-Medium", fontSize=9,
            leading=12, textColor=GRANITE, alignment=TA_LEFT,
            spaceAfter=0.5 * mm,
        ),
        "card_title": ParagraphStyle(
            "card_title", fontName="Geist-Medium", fontSize=12,
            leading=15, textColor=PURE_BLACK, alignment=TA_LEFT,
            spaceAfter=1 * mm,
        ),
        "card_audience": ParagraphStyle(
            "card_audience", fontName="Geist-Italic", fontSize=9,
            leading=12, textColor=GRANITE_LIGHT, alignment=TA_LEFT,
            spaceAfter=1 * mm,
        ),
        "card_body": ParagraphStyle(
            "card_body", fontName="Geist", fontSize=9, leading=12,
            textColor=GRANITE, alignment=TA_LEFT, spaceAfter=1 * mm,
        ),
    }


# ---------------------------------------------------------------------------
# Markdown parsing — adapted from long-read-pdf-gen.py
# ---------------------------------------------------------------------------

INLINE_BOLD = re.compile(r"\*\*(.+?)\*\*")
INLINE_ITALIC = re.compile(r"(?<!\*)\*([^*]+?)\*(?!\*)")
INLINE_CODE = re.compile(r"`([^`]+?)`")
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def _image_flowable(path: str, alt: str) -> Image | Paragraph:
    """Embed PNG at full content width; centered. Mirror of the Executive
    helper. Per-image scale overrides are gated by path suffix; none needed
    yet at body width (all four long-read PNGs render cleanly full-width).
    """
    p = (REPO / path).resolve()
    if not p.exists():
        return Paragraph(
            f"<i>[missing graphic: {path}]</i>",
            ParagraphStyle("_missing", fontName="Geist-Italic", fontSize=9),
        )
    img = Image(str(p))
    ratio = img.imageHeight / img.imageWidth
    img.drawWidth = CONTENT_WIDTH
    img.drawHeight = CONTENT_WIDTH * ratio
    img.hAlign = "CENTER"
    return img


def _inline(text: str) -> str:
    """Convert markdown inline to ReportLab Paragraph mini-language."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = INLINE_BOLD.sub(r"<b>\1</b>", text)
    text = INLINE_ITALIC.sub(r"<i>\1</i>", text)
    text = INLINE_CODE.sub(r'<font name="Geist" color="#2D3748">\1</font>', text)
    text = LINK.sub(r'<link href="\2" color="#087569">\1</link>', text)
    return text


def _escape_code(text: str) -> str:
    """Escape XML-special chars for the Paragraph mini-language; preserve
    whitespace via <br/> + non-breaking-space substitution."""
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    # Preserve leading indent: every line keeps its leading spaces converted
    # to non-breaking spaces so the Paragraph wrapper renders them.
    lines = []
    for line in text.splitlines():
        # Count leading spaces, swap for &nbsp;
        stripped = line.lstrip(" ")
        indent = len(line) - len(stripped)
        lines.append("&nbsp;" * indent + stripped)
    return "<br/>".join(lines)


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
    """Yield (kind, payload) blocks.

    Kinds: h1, h2, h3, h4, p, ul, hr, table, code, italic_meta."""
    raw = md.splitlines()
    i = 0
    n = len(raw)
    while i < n:
        line = raw[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # Fenced code block
        if stripped.startswith("```"):
            code_lines = []
            i += 1
            while i < n and not raw[i].lstrip().startswith("```"):
                code_lines.append(raw[i])
                i += 1
            i += 1  # consume closing fence
            yield ("code", "\n".join(code_lines))
            continue

        if stripped == "---":
            yield ("hr", None)
            i += 1
            continue

        if stripped == "<!-- PAGEBREAK -->":
            yield ("pagebreak", None)
            i += 1
            continue

        m = IMAGE.fullmatch(stripped)
        if m:
            yield ("image", (m.group(1), m.group(2)))
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

        if stripped.startswith("#### "):
            yield ("h4", stripped[5:].strip())
            i += 1
            continue

        # Pipe table (header row + separator)
        if stripped.startswith("|") and i + 1 < n and "---" in raw[i + 1]:
            rows, used = _split_table(raw[i:])
            yield ("table", rows)
            i += used
            continue

        # Italic-only single-line meta block — wrapped in *...*
        if (
            stripped.startswith("*")
            and stripped.endswith("*")
            and stripped.count("*") == 2
            and not stripped.startswith("**")
        ):
            yield ("italic_meta", stripped[1:-1])
            i += 1
            continue

        # Bullet list (contiguous - lines)
        if stripped.startswith("- "):
            items = []
            while i < n and raw[i].lstrip().startswith("- "):
                # Allow continuation lines (indented under a bullet)
                item_lines = [raw[i].lstrip()[2:].rstrip()]
                i += 1
                while i < n and raw[i].startswith(("  ", "\t")) and not raw[i].lstrip().startswith("- "):
                    item_lines.append(raw[i].strip())
                    i += 1
                items.append(" ".join(item_lines))
            yield ("ul", items)
            continue

        # Default: paragraph (collect until blank/structural break)
        para_lines = [stripped]
        i += 1
        while (
            i < n
            and raw[i].strip()
            and not raw[i].lstrip().startswith(
                ("- ", "## ", "### ", "#### ", "# ", "|", ">", "```")
            )
            and raw[i].strip() != "---"
        ):
            para_lines.append(raw[i].strip())
            i += 1
        yield ("p", " ".join(para_lines))


# ---------------------------------------------------------------------------
# Table rendering
# ---------------------------------------------------------------------------

def _table_flowable(rows: list[list[str]], styles: dict) -> Table:
    """Markdown pipe-table -> ReportLab Table.

    Header row Geist-Bold GRANITE; body Geist 8.5 pt; hairline row separators.
    Column widths even by default; squeeze-cluster table (2-col-or-3-col with
    Class IV semantics) lets first column be narrower for code labels.
    """
    header = rows[0]
    body = rows[2:]  # skip the separator row
    n_cols = len(header)

    data = [[Paragraph(_inline(c), styles["table_th"]) for c in header]]
    for r in body:
        # Pad short rows so the grid doesn't go ragged
        while len(r) < n_cols:
            r.append("")
        data.append([Paragraph(_inline(c), styles["table_td"]) for c in r[:n_cols]])

    # Heuristic column widths
    if n_cols == 2:
        col_w = [CONTENT_WIDTH * 0.35, CONTENT_WIDTH * 0.65]
    elif n_cols == 3:
        col_w = [CONTENT_WIDTH * 0.22, CONTENT_WIDTH * 0.28, CONTENT_WIDTH * 0.50]
    elif n_cols == 5:
        # Corridor table: Corridor | Label | Ratio | n | Countries
        col_w = [
            CONTENT_WIDTH * 0.10,
            CONTENT_WIDTH * 0.24,
            CONTENT_WIDTH * 0.16,
            CONTENT_WIDTH * 0.06,
            CONTENT_WIDTH * 0.44,
        ]
    elif n_cols == 9:
        # Scenario probability stack: Regime + S1-S7 + S8 conditional
        col_w = [CONTENT_WIDTH * 0.24] + [CONTENT_WIDTH * 0.095] * 8
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
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return t


# ---------------------------------------------------------------------------
# Page chrome — cover, body footer, closing page
# ---------------------------------------------------------------------------

def _page_background(canvas) -> None:
    canvas.setFillColor(PEARL_WHITE)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)


# Total page count is resolved on first build pass; closure pattern lets the
# footer draw "Page N / total" instead of "Page N".
class _PageCount:
    total: int = 0


def _on_cover_page(canvas, doc) -> None:
    """Cover page: pearl-white only, no footer chrome."""
    canvas.saveState()
    _page_background(canvas)
    canvas.restoreState()


def _on_later_page(canvas, doc) -> None:
    """All non-cover pages: pearl-white + v4.1 footer chrome."""
    canvas.saveState()
    _page_background(canvas)
    canvas.setFont("Geist", 7.5)
    canvas.setFillColor(GRANITE)
    y = 12 * mm
    canvas.drawString(MARGIN_LEFT, y, "Part 6 · Specialist Document")
    canvas.drawCentredString(PAGE_W / 2, y, "Nexalps · Part 6 of 7")
    total = _PageCount.total or doc.page
    canvas.drawRightString(
        PAGE_W - MARGIN_RIGHT, y, f"Page {doc.page} / {total}"
    )
    canvas.restoreState()


# ---------------------------------------------------------------------------
# Build the Story
# ---------------------------------------------------------------------------

class _TocDoc(SimpleDocTemplate):
    """SimpleDocTemplate variant that calls notify() on H2 headings so the
    TableOfContents flowable can collect them. Standard Platypus pattern."""

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        style_name = flowable.style.name
        if style_name == "h2":
            text = flowable.getPlainText()
            self.notify("TOCEntry", (0, text, self.page))


def _build_cover(styles: dict) -> list:
    """Cover page flowables. Match Executive v4.1 cover treatment:
    overline + 36 pt headline + 100 mm corridor map + byline. No cover
    lede (Phil-locked 2026-05-15 across the suite): the prior auto-pulled
    first sentence was the least interesting reader bait. The visual anchor
    carries the cover instead.
    """
    story = []
    story.append(Spacer(1, 0 * mm))
    story.append(
        Paragraph("EUROPEAN AI LABOUR MARKET SYNTHESIS &middot; SPECIALIST &middot; FIRST EDITION", styles["cover_overline"])
    )
    story.append(Spacer(1, 12 * mm))
    headline = (
        "Specialist appendix: thresholds, rule trail, "
        "per-country class assignments."
    )
    story.append(Paragraph(headline, styles["cover_headline"]))
    # Corridor map: 100 mm wide, centered (mirror Executive).
    cover_map = _image_flowable(
        "site/exports/corridor-map-nexalps.png",
        "36-country corridor map",
    )
    if isinstance(cover_map, Image):
        cover_w = 100 * mm
        ratio = cover_map.drawHeight / cover_map.drawWidth
        cover_map.drawWidth = cover_w
        cover_map.drawHeight = cover_w * ratio
        cover_map.hAlign = "CENTER"
    story.append(Spacer(1, 14 * mm))
    story.append(cover_map)
    story.append(Spacer(1, 14 * mm))
    story.append(
        Paragraph("BY PHILIPP MAUL · NEXALPS · MAY 2026", styles["cover_byline"])
    )
    story.append(PageBreak())
    return story


def _build_toc(styles: dict) -> list:
    """Table of contents page."""
    story = []
    story.append(Paragraph("Contents", styles["toc_title"]))
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "toc_entry", fontName="Geist", fontSize=10, leading=15,
            leftIndent=0, firstLineIndent=0,
            textColor=PURE_BLACK, spaceAfter=2,
        ),
    ]
    story.append(toc)
    story.append(PageBreak())
    return story


def _build_blocks(md: str, styles: dict) -> list:
    """Convert the markdown body into flowables with KeepTogether grouping
    for heading + first paragraph and table + heading."""
    blocks = list(_block_iter(md))
    story: list = []

    i = 0
    n = len(blocks)
    while i < n:
        kind, payload = blocks[i]

        if kind == "h1":
            story.append(Paragraph(_inline(payload), styles["h1"]))
            i += 1
            continue

        if kind == "h2":
            heading = Paragraph(_inline(payload), styles["h2"])
            # Try to keep with the next paragraph or table
            j = i + 1
            while j < n and blocks[j][0] in ("hr", "italic_meta"):
                j += 1
            if j < n and blocks[j][0] == "p":
                first_para = Paragraph(_inline(blocks[j][1]), styles["body"])
                story.append(KeepTogether([heading, first_para]))
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
                    tbl = _table_flowable(blocks[j][1], styles)
                    story.append(KeepTogether([heading, tbl]))
                    story.append(Spacer(1, 2 * mm))
                    i = j + 1
                    continue
            story.append(heading)
            i += 1
            continue

        if kind == "h4":
            story.append(Paragraph(_inline(payload), styles["h4"]))
            i += 1
            continue

        if kind == "p":
            story.append(Paragraph(_inline(payload), styles["body"]))
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

        if kind == "italic_meta":
            story.append(Paragraph(_inline(payload), styles["italic_meta"]))
            i += 1
            continue

        if kind == "pagebreak":
            story.append(PageBreak())
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
            story.append(KeepTogether([img, cap]))
            story.append(Spacer(1, 2 * mm))
            i += 1
            continue

        if kind == "hr":
            story.append(Spacer(1, 2 * mm))
            story.append(HRFlowable(width="100%", thickness=0.4, color=HAIRLINE))
            story.append(Spacer(1, 2 * mm))
            i += 1
            continue

        if kind == "code":
            code_html = _escape_code(payload)
            story.append(
                KeepTogether(
                    Paragraph(code_html, styles["code_block"])
                )
            )
            i += 1
            continue

        if kind == "table":
            tbl = _table_flowable(payload, styles)
            story.append(tbl)
            story.append(Spacer(1, 2.5 * mm))
            i += 1
            continue

        i += 1
    return story


def _doc_card(variant: dict, styles: dict) -> Table:
    """4-row card: meta, header, audience (italic), oneliner.
    Left edge stripe uses per-deliverable colour (matches resources.html)."""
    inner = [
        [Paragraph(variant["meta"], styles["card_meta"])],
        [Paragraph(variant["header"], styles["card_title"])],
        [Paragraph(variant["audience"], styles["card_audience"])],
        [Paragraph(variant["oneliner"], styles["card_body"])],
    ]
    inner_t = Table(inner, colWidths=[CONTENT_WIDTH - 8 * mm])
    inner_t.setStyle(
        TableStyle(
            [
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    outer = [[Paragraph("&nbsp;", styles["card_body"]), inner_t]]
    t = Table(outer, colWidths=[1.5 * mm, CONTENT_WIDTH - 1.5 * mm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), variant["color"]),
                ("BACKGROUND", (1, 0), (1, 0), HexColor("#FFFFFF")),
                ("BOX", (0, 0), (-1, -1), 0.5, HAIRLINE),
                ("LEFTPADDING", (0, 0), (0, 0), 0),
                ("RIGHTPADDING", (0, 0), (0, 0), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 4 * mm),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4 * mm),
                ("LEFTPADDING", (1, 0), (1, 0), 5 * mm),
                ("RIGHTPADDING", (1, 0), (1, 0), 5 * mm),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]
        )
    )
    return t


def _build_closing_page(styles: dict) -> list:
    """Last-page document ladder + landing URL."""
    story = []
    story.append(PageBreak())
    story.append(Spacer(1, 20 * mm))
    story.append(Paragraph("WHERE TO GO NEXT", styles["ladder_overline"]))
    story.append(Paragraph("Full read", styles["h2"]))
    story.append(
        Paragraph(
            "This Specialist Appendix is one of four renders. The companion "
            "documents carry the analysis at progressive depth.",
            styles["body"],
        )
    )
    story.append(Spacer(1, 4 * mm))
    for slug, variant in doc_ladder_others("specialist"):
        story.append(_doc_card(variant, styles))
        story.append(Spacer(1, 4 * mm))
    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("ALL FOUR AT:", styles["ladder_overline"]))
    story.append(Paragraph(LADDER_URL, styles["ladder_url"]))
    return story


# ---------------------------------------------------------------------------
# Build entry point
# ---------------------------------------------------------------------------

def build_pdf() -> Path:
    md = MARKDOWN.read_text(encoding="utf-8")
    styles = _styles()

    # Two-pass build is the canonical Platypus pattern for accurate page
    # numbers and TOC entries. SimpleDocTemplate.multiBuild handles it.
    doc = _TocDoc(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=MARGIN_LEFT,
        rightMargin=MARGIN_RIGHT,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM,
        title="European AI Labour Market Synthesis · Specialist Appendix",
        author="Philipp Maul",
        subject="Part 6 Specialist Document",
    )

    story: list = []
    story.extend(_build_cover(styles))
    story.extend(_build_toc(styles))
    story.extend(_build_blocks(md, styles))
    story.extend(_build_closing_page(styles))

    # First pass: count pages so the footer can render "Page N / total".
    doc.multiBuild(
        story,
        onFirstPage=_on_cover_page,
        onLaterPages=_on_later_page,
    )
    total = doc.page
    # Second pass with total page count baked in — only needed if total differs.
    if _PageCount.total != total:
        _PageCount.total = total
        # Re-create the doc and rebuild so the footer renders accurately on
        # every page (multiBuild already ran the TOC pass).
        doc2 = _TocDoc(
            str(OUTPUT),
            pagesize=A4,
            leftMargin=MARGIN_LEFT,
            rightMargin=MARGIN_RIGHT,
            topMargin=MARGIN_TOP,
            bottomMargin=MARGIN_BOTTOM,
            title="European AI Labour Market Synthesis · Specialist Appendix",
            author="Philipp Maul",
            subject="Part 6 Specialist Document",
        )
        story2: list = []
        story2.extend(_build_cover(styles))
        story2.extend(_build_toc(styles))
        story2.extend(_build_blocks(md, styles))
        story2.extend(_build_closing_page(styles))
        doc2.multiBuild(
            story2,
            onFirstPage=_on_cover_page,
            onLaterPages=_on_later_page,
        )
    return OUTPUT


if __name__ == "__main__":
    out = build_pdf()
    print(f"PDF saved: {out}")
