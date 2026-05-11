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
from pathlib import Path
from typing import Iterable

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
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
MARKDOWN = REPO / "layer-6-deliverable-long-read.md"
GRAPHICS = REPO / "site" / "exports" / "long-read"
OUTPUT = REPO / "layer-6-deliverable-long-read.pdf"

# Font registration — reuse the Geist installation in job-scout-agent.
FONT_DIR = (
    Path("/Users/philippmaul/Documents/projects/job-scout-agent")
    / "fonts"
    / "geist-font-1.8.0"
    / "fonts"
    / "Geist"
    / "ttf"
)
_FONT_FILES = {
    "Geist-Light": "Geist-Light.ttf",
    "Geist-LightItalic": "Geist-LightItalic.ttf",
    "Geist": "Geist-Regular.ttf",
    "Geist-Italic": "Geist-Italic.ttf",
    "Geist-Medium": "Geist-Medium.ttf",
    "Geist-MediumItalic": "Geist-MediumItalic.ttf",
    "Geist-SemiBold": "Geist-SemiBold.ttf",
    "Geist-Bold": "Geist-Bold.ttf",
    "Geist-BoldItalic": "Geist-BoldItalic.ttf",
}
for _name, _file in _FONT_FILES.items():
    pdfmetrics.registerFont(TTFont(_name, str(FONT_DIR / _file)))

registerFontFamily(
    "Geist",
    normal="Geist",
    bold="Geist-Bold",
    italic="Geist-Italic",
    boldItalic="Geist-BoldItalic",
)

# Nexalps palette
PEARL_WHITE = HexColor("#F8F9FA")
PURE_BLACK = HexColor("#000000")
DEEP_TEAL = HexColor("#087569")
GRANITE = HexColor("#4A5568")
HAIRLINE = HexColor("#CBD5E0")

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
    base = dict(fontName="Geist", textColor=PURE_BLACK, alignment=TA_LEFT)
    return {
        "h2": ParagraphStyle(
            "h2", **{**base, "fontName": "Geist-Medium"}, fontSize=22,
            leading=28, spaceBefore=10 * mm, spaceAfter=4 * mm,
            keepWithNext=1,
        ),
        "h3": ParagraphStyle(
            "h3", **{**base, "fontName": "Geist-Medium"}, fontSize=14,
            leading=18, spaceBefore=4 * mm, spaceAfter=2 * mm,
            keepWithNext=1,
        ),
        "overline": ParagraphStyle(
            "overline", **{**base, "fontName": "Geist-Bold", "textColor": GRANITE},
            fontSize=8, leading=10, spaceAfter=2 * mm,
        ),
        "lede": ParagraphStyle(
            "lede", **{**base, "fontName": "Geist-Light", "textColor": GRANITE},
            fontSize=14, leading=20, spaceAfter=3 * mm,
            allowWidows=0, allowOrphans=0,
        ),
        "body": ParagraphStyle(
            "body", **base, fontSize=10.5, leading=15,
            spaceAfter=2.5 * mm,
            allowWidows=0, allowOrphans=0,
        ),
        "byline": ParagraphStyle(
            "byline", **{**base, "textColor": GRANITE},
            fontSize=9, leading=12, spaceAfter=1 * mm,
        ),
        "bullet": ParagraphStyle(
            "bullet", **base, fontSize=10.5, leading=15,
            leftIndent=5 * mm, bulletIndent=0, spaceAfter=1 * mm,
        ),
        "italic_meta": ParagraphStyle(
            "italic_meta", **{**base, "fontName": "Geist-Italic", "textColor": GRANITE},
            fontSize=9, leading=12, spaceAfter=1 * mm,
        ),
        "pullquote": ParagraphStyle(
            "pullquote",
            **{**base, "fontName": "Geist-LightItalic", "textColor": DEEP_TEAL},
            fontSize=16, leading=24, spaceBefore=4 * mm, spaceAfter=4 * mm,
            leftIndent=10 * mm, rightIndent=10 * mm,
        ),
        "table_th": ParagraphStyle(
            "table_th", **{**base, "fontName": "Geist-Bold", "textColor": GRANITE},
            fontSize=8, leading=10,
        ),
        "table_td": ParagraphStyle(
            "table_td", **base, fontSize=10, leading=13,
        ),
        "table_td_bold": ParagraphStyle(
            "table_td_bold", **{**base, "fontName": "Geist-Bold"},
            fontSize=14, leading=18,
        ),
        "table_td_small": ParagraphStyle(
            "table_td_small", **base, fontSize=8.5, leading=11,
        ),
        "section_num": ParagraphStyle(
            "section_num", **{**base, "fontName": "Geist-Bold", "textColor": DEEP_TEAL},
            fontSize=10, leading=12, spaceAfter=1 * mm,
        ),
        "title": ParagraphStyle(
            "title", **{**base, "fontName": "Geist-Medium"}, fontSize=26,
            leading=30, spaceBefore=4 * mm, spaceAfter=4 * mm,
            keepWithNext=1,
        ),
        "cover_headline": ParagraphStyle(
            "cover_headline", fontName="Geist-LightItalic",
            fontSize=44, leading=56, textColor=PURE_BLACK,
            alignment=TA_LEFT, spaceBefore=0, spaceAfter=0,
        ),
        "cover_overline": ParagraphStyle(
            "cover_overline", fontName="Geist-Bold", fontSize=10,
            leading=12, textColor=GRANITE, alignment=TA_LEFT,
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
        yield ("p", " ".join(para_lines))


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def _on_page(canvas, doc):
    """Draw pearl-white page background and footer."""
    canvas.saveState()
    canvas.setFillColor(PEARL_WHITE)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    # Footer
    canvas.setFont("Geist", 8)
    canvas.setFillColor(GRANITE)
    y = 12 * mm
    canvas.drawString(MARGIN_LEFT, y, "Layer 6 — Long Read")
    canvas.drawCentredString(PAGE_W / 2, y, "Nexalps · Part 6 of 7")
    canvas.drawRightString(PAGE_W - MARGIN_RIGHT, y, f"Page {doc.page}")
    canvas.restoreState()


def _on_cover_page(canvas, doc):
    """Cover page: pearl-white only, no footer."""
    canvas.saveState()
    canvas.setFillColor(PEARL_WHITE)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canvas.restoreState()


def _image_flowable(path: str, alt: str) -> Image | Paragraph:
    """Embed PNG (preferred over SVG for ReportLab without svglib)."""
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
    img.drawWidth = CONTENT_WIDTH
    img.drawHeight = CONTENT_WIDTH * ratio
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
                    "Layer 6 · European AI Labour Market Synthesis",
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
            # Heading + first paragraph → KeepTogether.
            heading = Paragraph(_inline(payload), styles["h2"])
            # Look ahead for next paragraph or image to group with.
            group = [heading]
            j = i + 1
            while j < n and blocks[j][0] in ("hr", "italic_meta"):
                j += 1
            if j < n and blocks[j][0] in ("p", "image"):
                next_kind, next_payload = blocks[j]
                if next_kind == "image":
                    img = _image_flowable(next_payload[1], next_payload[0])
                    cap = Paragraph(
                        f"<i>{_inline(next_payload[0])}</i>" if next_payload[0] else "&nbsp;",
                        styles["italic_meta"],
                    )
                    group.extend([Spacer(1, 2 * mm), img, cap, Spacer(1, 2 * mm)])
                    story.append(KeepTogether(group))
                    i = j + 1
                    continue
                else:
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
                    tbl = _table_flowable(blocks[j][1], styles)
                    story.append(KeepTogether([heading, tbl]))
                    story.append(Spacer(1, 3 * mm))
                    i = j + 1
                    continue
            story.append(heading)
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

        if kind == "image":
            alt, src = payload
            img = _image_flowable(src, alt)
            cap = Paragraph(
                f"<i>{_inline(alt)}</i>" if alt else "&nbsp;",
                styles["italic_meta"],
            )
            # Image + caption stay together.
            story.append(Spacer(1, 2 * mm))
            story.append(KeepTogether([img, cap]))
            story.append(Spacer(1, 2 * mm))
            i += 1
            continue

        if kind == "italic_meta":
            story.append(Paragraph(_inline(payload), styles["italic_meta"]))
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
    md = MARKDOWN.read_text(encoding="utf-8")
    styles = _styles()

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=MARGIN_LEFT,
        rightMargin=MARGIN_RIGHT,
        topMargin=MARGIN_TOP,
        bottomMargin=MARGIN_BOTTOM,
        title="European AI Labour Market Synthesis — Long Read",
        author="Philipp Maul",
        subject="Layer 6 Specialist Long-Read",
    )

    story = _build_blocks(md, styles)

    # First page = cover (no footer); subsequent pages get the footer.
    doc.build(story, onFirstPage=_on_cover_page, onLaterPages=_on_page)
    return OUTPUT


if __name__ == "__main__":
    out = build_pdf()
    print(f"PDF saved: {out}")
