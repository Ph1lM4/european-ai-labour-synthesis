#!/usr/bin/env python3
"""Render the Layer 6 Executive Brief markdown to a Nexalps-styled A4 PDF.

Architecture mirrors tools/long-read-pdf-gen.py (Platypus, story-based) but
adopts the v4.1 design tokens locked in tools/visual-read-pdf-gen.py:

  * 16 pt Geist-Medium H2 (not 22 pt)
  * 12 pt Geist-Medium card-titles / sub-headers
  * 9 pt body / lede / caption / eyebrow (single body size, no 8.5/9.5/10/11)
  * 7.5 pt footer chrome
  * Upright (not italic) 9 pt lede — v4.1 lock
  * 36 pt Geist-LightItalic cover headline
  * 20 pt Geist-LightItalic landing URL on last page
  * Class IV colour = CLASS_IV_WINE #7F1D1D (never gray)
  * Footer: "Part 6 · Executive Brief" · "Nexalps · Part 6 of 7" · "Page N / total"

Tokens are inline-copied (not imported) because visual-read is canvas-direct
and we are Platypus — architectures differ. This is intentional per the
master's architecture decision. Flagged in the post-code review for a
future shared-style-module extraction.

Source:  docs/layer-6-deliverable-document-executive.md
Output:  docs/layer-6-deliverable-executive.pdf
Target:  ~6 pages at 9 pt body / 13 pt leading.

Usage:
  python3 tools/executive-pdf-gen.py
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
    DEEP_TEAL,
    GRANITE, GRANITE_DARK, GRANITE_LIGHT, GRANITE_LIGHTER,
    HAIRLINE,
    ALPINE_GOLD, ALPINE_RED, CLASS_IV_WINE,
    CLS_COLOR,
    RADIUS_CARD,
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
MARKDOWN = REPO / "docs" / "layer-6-deliverable-document-executive.md"
OUTPUT = REPO / "docs" / "layer-6-deliverable-executive.pdf"

# Page setup — match visual-read / long-read margins.
PAGE_W, PAGE_H = A4
MARGIN_LEFT = 25 * mm
MARGIN_RIGHT = 25 * mm
MARGIN_TOP = 25 * mm
MARGIN_BOTTOM = 22 * mm
CONTENT_WIDTH = PAGE_W - MARGIN_LEFT - MARGIN_RIGHT


# ---------------------------------------------------------------------------
# Styles — v4.1 type scale: 9 / 12 / 16 / 20 / 36 pt only.
# ---------------------------------------------------------------------------

def _styles() -> dict[str, ParagraphStyle]:
    base = dict(fontName="Geist", textColor=PURE_BLACK, alignment=TA_LEFT)
    return {
        # H2 — 16 pt Geist-Medium (v4.1 lock; was 22 pt in long-read).
        "h2": ParagraphStyle(
            "h2", **{**base, "fontName": "Geist-Medium"}, fontSize=16,
            leading=20, spaceBefore=7 * mm, spaceAfter=3 * mm,
            keepWithNext=1,
        ),
        # H3 — 12 pt sub-header (v4.1 card-title equivalent).
        "h3": ParagraphStyle(
            "h3", **{**base, "fontName": "Geist-Medium"}, fontSize=12,
            leading=15, spaceBefore=3 * mm, spaceAfter=1.5 * mm,
            keepWithNext=1,
        ),
        # Body — 9 pt / 13 pt leading (executive prose-readability flex).
        "body": ParagraphStyle(
            "body", **base, fontSize=9, leading=13,
            spaceAfter=2.2 * mm,
            allowWidows=0, allowOrphans=0,
        ),
        # Lede — UPRIGHT 9 pt granite (v4.1: not italic).
        "lede": ParagraphStyle(
            "lede", **{**base, "fontName": "Geist", "textColor": GRANITE},
            fontSize=9, leading=13, spaceAfter=3 * mm,
            allowWidows=0, allowOrphans=0,
        ),
        # Bullet — same scale as body. `splitLongWords=1` defensive against
        # rare cases where a bolded em-dashed phrase fails to break. Right
        # indent is set just to keep the wrap width strictly less than the
        # frame width (avoids ReportLab's `rw == aW` edge case which trips
        # a LayoutError on certain single-line paragraphs).
        "bullet": ParagraphStyle(
            "bullet", **base, fontSize=9, leading=13,
            leftIndent=4 * mm, rightIndent=0.5 * mm, bulletIndent=0,
            spaceAfter=1.2 * mm,
            allowWidows=0, allowOrphans=0, splitLongWords=1,
        ),
        # Bold prelude / lead-in headers (the **Foo** lines in the source).
        # Distinct from H2: looks like a paragraph but bolded with bottom air.
        "leadin": ParagraphStyle(
            "leadin", **{**base, "fontName": "Geist-Medium"},
            fontSize=12, leading=15,
            spaceBefore=4 * mm, spaceAfter=2 * mm,
            keepWithNext=1,
        ),
        # Italic standout — 9 pt italic on granite, sets off a punchline line.
        "italic_meta": ParagraphStyle(
            "italic_meta", **{**base, "fontName": "Geist-Italic", "textColor": GRANITE},
            fontSize=9, leading=13, spaceAfter=2 * mm,
        ),
        # Eyebrow — 9 pt Geist-Bold, tracked granite (cover overline + CTA).
        "eyebrow": ParagraphStyle(
            "eyebrow", **{**base, "fontName": "Geist-Bold", "textColor": GRANITE},
            fontSize=9, leading=11, spaceAfter=3 * mm,
        ),
        # Cover headline — 36 pt Geist-LightItalic (v4.1 cover discipline).
        "cover_headline": ParagraphStyle(
            "cover_headline", fontName="Geist-LightItalic",
            fontSize=36, leading=44, textColor=PURE_BLACK,
            alignment=TA_LEFT, spaceBefore=0, spaceAfter=4 * mm,
        ),
        # Cover lede — 9 pt upright (v4.1: not italic).
        "cover_lede": ParagraphStyle(
            "cover_lede", fontName="Geist", fontSize=9, leading=13,
            textColor=GRANITE, alignment=TA_LEFT, spaceAfter=0,
        ),
        # Cover byline — 9 pt Geist-Bold granite, tracked feel.
        "cover_byline": ParagraphStyle(
            "cover_byline", fontName="Geist-Bold", fontSize=9, leading=11,
            textColor=GRANITE, alignment=TA_LEFT,
        ),
        # Table styles (compact, sparse).
        "table_th": ParagraphStyle(
            "table_th", **{**base, "fontName": "Geist-Bold", "textColor": GRANITE},
            fontSize=9, leading=11,
        ),
        "table_td": ParagraphStyle(
            "table_td", **base, fontSize=9, leading=12,
        ),
        # CTA landing — 20 pt Geist-LightItalic teal (v4.1 lock).
        "cta_landing": ParagraphStyle(
            "cta_landing", fontName="Geist-LightItalic", fontSize=20,
            leading=24, textColor=DEEP_TEAL, alignment=TA_LEFT,
            spaceBefore=2 * mm, spaceAfter=4 * mm,
        ),
        # Doc-card title — 12 pt Geist-Medium.
        "card_title": ParagraphStyle(
            "card_title", fontName="Geist-Medium", fontSize=12,
            leading=15, textColor=PURE_BLACK, alignment=TA_LEFT,
            spaceAfter=1 * mm,
        ),
        # Doc-card body — 9 pt granite.
        "card_body": ParagraphStyle(
            "card_body", fontName="Geist", fontSize=9, leading=12,
            textColor=GRANITE, alignment=TA_LEFT, spaceAfter=1 * mm,
        ),
        # Doc-card URL — 9 pt teal.
        "card_url": ParagraphStyle(
            "card_url", fontName="Geist", fontSize=9, leading=12,
            textColor=DEEP_TEAL, alignment=TA_LEFT,
        ),
    }


# ---------------------------------------------------------------------------
# Markdown → flowables (lifted from long-read-pdf-gen.py; trimmed to what
# the executive source actually uses. Inline-copied per master's decision —
# flagged in the Code Review block.)
# ---------------------------------------------------------------------------

INLINE_BOLDITALIC = re.compile(r"\*\*\*(.+?)\*\*\*")
INLINE_BOLD = re.compile(r"\*\*(.+?)\*\*")
INLINE_ITALIC = re.compile(r"(?<!\*)\*([^*]+?)\*(?!\*)")
INLINE_CODE = re.compile(r"`([^`]+?)`")
LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def _inline(text: str) -> str:
    """Convert markdown inline syntax → ReportLab Paragraph mini-language.

    Order matters: ``***x***`` (bold-italic) must be resolved before
    ``**x**`` (bold) so the inner ``*`` isn't picked up as a stray italic
    delimiter and emit mis-nested ``<b><i>...</b></i>`` tags.

    The 🛈 info-circle glyph from the source is preserved as-is (UTF-8).
    """
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = INLINE_BOLDITALIC.sub(r"<b><i>\1</i></b>", text)
    text = INLINE_BOLD.sub(r"<b>\1</b>", text)
    text = INLINE_ITALIC.sub(r"<i>\1</i>", text)
    text = INLINE_CODE.sub(r'<font name="Geist" color="#4A5568">\1</font>', text)
    text = LINK.sub(r'<link href="\2" color="#087569">\1</link>', text)
    return text


def _strip_outer_bold(line: str) -> tuple[bool, str]:
    """If a single line is entirely wrapped in **...** with no other **, treat
    it as a lead-in header (not a body paragraph with bold).

    Returns (is_leadin, payload_without_outer_stars).
    """
    s = line.strip()
    if (
        s.startswith("**")
        and s.endswith("**")
        and s.count("**") == 2
        and len(s) > 4
    ):
        return True, s[2:-2].strip()
    return False, s


IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")


def _image_flowable(path: str, alt: str) -> Image | Paragraph:
    """Embed PNG at full content width; centered. Mirror of the long-read
    helper minus the corridor-map width override (Executive uses the same
    map at full width on the cover, not inline)."""
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


def _block_iter(md: str) -> Iterable[tuple[str, object]]:
    """Yield (kind, payload) blocks: cover_headline, h2, h3, p, leadin, ul,
    hr, italic_meta, image. Trimmed from long-read's iterator — no
    pipe-tables (executive markdown has none)."""
    raw = md.splitlines()
    i = 0
    n = len(raw)

    # First non-empty line: the **bold pseudo-title** doubles as the cover
    # headline. We pull it out and emit a `cover_headline` block so the
    # builder can route it to page 1 with cover-discipline styling.
    while i < n and not raw[i].strip():
        i += 1
    if i < n:
        is_leadin, payload = _strip_outer_bold(raw[i])
        if is_leadin:
            yield ("cover_headline", payload)
            i += 1

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

        if stripped == "<!-- PAGEBREAK -->":
            yield ("pagebreak", None)
            i += 1
            continue

        m = IMAGE.fullmatch(stripped)
        if m:
            yield ("image", (m.group(1), m.group(2)))
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

        # Standalone italic line (e.g. "*The outlier → Italy...*").
        if (
            stripped.startswith("*")
            and not stripped.startswith("**")
            and stripped.endswith("*")
            and stripped.count("*") == 2
        ):
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

        # Lead-in: a single line entirely wrapped in **...** (no other markup).
        # Detected only when the line is on its own (next line is blank or
        # a different block type) — otherwise it's inline bold inside a para.
        if i + 1 < n and not raw[i + 1].strip():
            is_leadin, payload = _strip_outer_bold(stripped)
            if is_leadin:
                yield ("leadin", payload)
                i += 1
                continue

        # Default: paragraph (collect until blank line or block-starting line).
        para_lines = [stripped]
        i += 1
        while i < n and raw[i].strip() and not raw[i].lstrip().startswith(
            ("- ", "## ", "### ", "# ", "|", "!", ">")
        ) and raw[i].strip() != "---":
            para_lines.append(raw[i].strip())
            i += 1
        yield ("p", " ".join(para_lines))


# ---------------------------------------------------------------------------
# Page chrome
# ---------------------------------------------------------------------------

# We need to know the total page count for the footer "Page N / total" form.
# ReportLab Platypus computes this on a two-pass build using `aW` callbacks,
# but a simpler trick is to render once, capture canvas.getPageNumber(),
# then patch the footer text in pass two. We instead use a closure that
# records the final page count in a mutable container.

class _PageCount:
    """Mutable holder for total page count (filled after first pass)."""
    total: int = 0


def _on_cover_page(canvas, doc):
    """Cover page: pearl-white background, no footer."""
    canvas.saveState()
    canvas.setFillColor(PEARL_WHITE)
    canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    canvas.restoreState()


def _make_on_later_pages(page_count: _PageCount):
    def _on_page(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(PEARL_WHITE)
        canvas.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
        # Footer chrome — 7.5 pt Geist granite (v4.1 lock).
        canvas.setFont("Geist", 7.5)
        canvas.setFillColor(GRANITE)
        y = 12 * mm
        canvas.drawString(MARGIN_LEFT, y, "Part 6 · Executive Brief")
        canvas.drawCentredString(PAGE_W / 2, y, "Nexalps · Part 6 of 7")
        total = page_count.total or doc.page
        canvas.drawRightString(
            PAGE_W - MARGIN_RIGHT, y, f"Page {doc.page} / {total}"
        )
        canvas.restoreState()
    return _on_page


# ---------------------------------------------------------------------------
# Last-page CTA (doc ladder, omits self)
# ---------------------------------------------------------------------------

# Mirror visual-read DOC_LADDER but drop the Executive card (we ARE that
# document — no self-link).
DOC_LADDER_OMIT_SELF = [
    ("Visual read · 8 pp",
     "Scan-first version · corridor map · one-page chart per finding.",
     "synthesis.nexalps.com/visual-read"),
    ("Long-read · 14 pp",
     "Specialist appendix in long-form prose · 3,728 words · four graphics.",
     "synthesis.nexalps.com/long-read"),
    ("Specialist document · full",
     "All five lens findings · three corridor sub-clusters · eight scenarios in detail.",
     "synthesis.nexalps.com/specialist"),
]


def _doc_card(title: str, desc: str, url: str, styles: dict) -> Table:
    """3-row card with left teal accent stripe + hairline border."""
    inner = [
        [Paragraph(_inline(title), styles["card_title"])],
        [Paragraph(_inline(desc), styles["card_body"])],
        [Paragraph(_inline(url), styles["card_url"])],
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
    # Outer 2-col table: accent stripe + content. The stripe is a 1-mm wide
    # cell, teal-filled.
    outer = [[Paragraph("&nbsp;", styles["card_body"]), inner_t]]
    t = Table(outer, colWidths=[1.2 * mm, CONTENT_WIDTH - 1.2 * mm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, 0), DEEP_TEAL),
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


def _build_cta(styles: dict) -> list:
    """Document-ladder CTA appended after the source markdown body.

    Mirrors visual-read page 8 — eyebrow, doc cards (self omitted), landing
    URL, cite-as. Page-break before so it always lands cleanly.
    """
    story: list = [PageBreak()]
    story.append(Paragraph("WHERE TO GO NEXT", styles["eyebrow"]))
    story.append(Paragraph("Full read", styles["h2"]))
    story.append(
        Paragraph(
            "This Executive Brief is one render of three. The companion "
            "documents carry the full analysis at progressive depth.",
            styles["lede"],
        )
    )
    story.append(Spacer(1, 3 * mm))
    for title, desc, url in DOC_LADDER_OMIT_SELF:
        story.append(_doc_card(title, desc, url, styles))
        story.append(Spacer(1, 4 * mm))

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("INSPECT THE FULL ANALYSIS AT:", styles["eyebrow"]))
    story.append(Paragraph("synthesis.nexalps.com", styles["cta_landing"]))

    story.append(Spacer(1, 4 * mm))
    story.append(Paragraph("CITE AS", styles["eyebrow"]))
    story.append(
        Paragraph(
            "Maul, P. (2026). Part 6 · European AI Labour Market Synthesis · "
            "Executive Brief. Nexalps.",
            styles["body"],
        )
    )
    return story


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def _build_blocks(md: str, styles: dict) -> list:
    """Walk the block iterator and emit a flowable story.

    Cover page is built from the first **bold pseudo-title** line; everything
    after that flows as body. KeepTogether wraps H2/H3 headings with their
    next paragraph or first bullet.
    """
    blocks = list(_block_iter(md))
    story: list = []
    cover_emitted = False

    i = 0
    n = len(blocks)
    while i < n:
        kind, payload = blocks[i]

        if kind == "cover_headline":
            # Cover — overline + headline + corridor map + byline.
            # No cover lede (Phil-locked 2026-05-15): the prior auto-pulled
            # first sentence of the Prelude was the least interesting reader
            # bait. Cover now reads as headline + visual anchor.
            story.append(Paragraph("EUROPEAN AI LABOUR MARKET SYNTHESIS &middot; EXECUTIVE &middot; FIRST EDITION",
                                   styles["eyebrow"]))
            story.append(Spacer(1, 12 * mm))
            story.append(Paragraph(_inline(payload), styles["cover_headline"]))
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
            story.append(Paragraph("BY PHILIPP MAUL · NEXALPS · MAY 2026",
                                   styles["cover_byline"]))
            story.append(PageBreak())
            cover_emitted = True
            i += 1
            continue

        if kind == "leadin":
            # Lead-in mini-header (used for **Prelude**, **What Survives...**,
            # **The outlier → Italy...**). Wrap with the next paragraph.
            heading = Paragraph(_inline(payload), styles["leadin"])
            j = i + 1
            while j < n and blocks[j][0] in ("hr",):
                j += 1
            if j < n and blocks[j][0] == "p":
                first_para = Paragraph(_inline(blocks[j][1]), styles["body"])
                story.append(KeepTogether([heading, first_para]))
                i = j + 1
                continue
            story.append(heading)
            i += 1
            continue

        if kind == "h2":
            heading = Paragraph(_inline(payload), styles["h2"])
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
            if j < n and blocks[j][0] in ("p", "ul"):
                if blocks[j][0] == "p":
                    first_para = Paragraph(_inline(blocks[j][1]), styles["body"])
                    story.append(KeepTogether([heading, first_para]))
                    i = j + 1
                    continue
                if blocks[j][0] == "ul":
                    bullets = [
                        Paragraph(f"•&nbsp;&nbsp;{_inline(item)}",
                                  styles["bullet"])
                        for item in blocks[j][1]
                    ]
                    story.append(KeepTogether([heading] + bullets[:1]))
                    story.extend(bullets[1:])
                    story.append(Spacer(1, 1 * mm))
                    i = j + 1
                    continue
            story.append(heading)
            i += 1
            continue

        if kind == "p":
            story.append(Paragraph(_inline(payload), styles["body"]))
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

        if kind == "italic_meta":
            story.append(Paragraph(_inline(payload), styles["italic_meta"]))
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

        if kind == "hr":
            story.append(Spacer(1, 2 * mm))
            story.append(HRFlowable(width="100%", thickness=0.4, color=HAIRLINE))
            story.append(Spacer(1, 2 * mm))
            i += 1
            continue

        i += 1
    return story


def _make_story(md: str, styles: dict) -> list:
    """Fresh story per pass — flowables are stateful inside ReportLab
    (Paragraphs cache `_blPara` after first wrap); reusing them across two
    `doc.build` calls produces LayoutErrors on the second pass."""
    story = _build_blocks(md, styles)
    story.extend(_build_cta(styles))
    return story


def build_pdf() -> Path:
    md = MARKDOWN.read_text(encoding="utf-8")

    page_count = _PageCount()
    on_later = _make_on_later_pages(page_count)

    def _new_doc() -> SimpleDocTemplate:
        return SimpleDocTemplate(
            str(OUTPUT),
            pagesize=A4,
            leftMargin=MARGIN_LEFT,
            rightMargin=MARGIN_RIGHT,
            topMargin=MARGIN_TOP,
            bottomMargin=MARGIN_BOTTOM,
            title="European AI Labour Market Synthesis · Executive Brief",
            author="Philipp Maul",
            subject="Part 6 of 7 · Executive Brief",
        )

    # Pass 1: count pages.
    doc1 = _new_doc()
    doc1.build(_make_story(md, _styles()),
               onFirstPage=_on_cover_page, onLaterPages=on_later)
    page_count.total = doc1.page

    # Pass 2: render with the total baked into the footer chrome.
    doc2 = _new_doc()
    doc2.build(_make_story(md, _styles()),
               onFirstPage=_on_cover_page, onLaterPages=on_later)
    return OUTPUT


if __name__ == "__main__":
    out = build_pdf()
    print(f"PDF saved: {out}")
