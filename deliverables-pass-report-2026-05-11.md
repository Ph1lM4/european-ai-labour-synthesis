# Deliverables Pass Report — 2026-05-11

Final cleanup batch executed against the synthesis deliverable suite. Italy + Conclusion propagation, locked-copy mirror sweep, Long-Read PDF regen, per-page version-stamp audit, banned-phrase verification.

---

## 1. Italy + Conclusion propagation

| Surface | Italy | Conclusion | Source |
|---|---|---|---|
| `site/findings.html` | Locked (lead + body) | Locked (Forecasts-easy opening + class-by-class + dropping-soon) | SOT |
| `layer-6-deliverable-onepager.md` | **Added** — new "Italy — the outlier" section after Methodology; verbatim mirror | **Added** — new "Conclusion" section before print citation; verbatim mirror | This pass |
| `layer-6-deliverable-document-executive.md` | **Replaced** technical Italy block (Lens 2, §2) with plain-language version; advisory-track register | **Replaced** §6 Closer with plain-language Conclusion ("Forecasts are easy..." opening + class-by-class + dropping-soon); §6 heading renamed `Closer` → `Conclusion` | This pass |
| `layer-6-deliverable-document.md` | Kept technical Italy treatment (Specialist Appendix; per handover) | Kept technical Closer/Conclusion (Specialist Appendix; per handover) | Unchanged |

Italy plain-prose lead (verbatim, single source of truth):
> *"The outlier → Italy, with the workforce shrinking before AI displaces a single worker."*

Italy body (verbatim, plain-language):
> Italy is the only major European economy with negative net migration in 2025 (**−485,823**). It is singled out as an "outlier" because its workforce is already shrinking and is projected to keep shrinking through 2050 (a −17.5% decline in working-age people, plus negative migration). That leaves less capacity to absorb AI-driven disruption, while the usual buffers, retirement (25.3% offset) and migration, are too small or politically constrained. This means there are already too few people to hire for essential jobs like caregiving, skilled manual work, and medical roles, so these labour gaps worsen disruption instead of helping absorb it.

Conclusion verbatim three-paragraph block propagated as written in `site/findings.html` (Forecasts-easy opening → class-by-class action implications → strict-zero + Part 7 dropping-soon close).

## 2. Locked-copy mirror sweep

### Math fix (S1 + S3 combined; growth-baseline vs post-growth)

| File | Pre-pass | Post-pass | Status |
|---|---|---|---|
| `site/index.html` line 241 | 20% → 13% | 20% → 13% | Already correct |
| `site/scenarios.html` lines 282, 341 | 20% → 13% | 20% → 13% | Already correct |
| `layer-6-deliverable-onepager.md` line 33 | 20% → 13% | 20% → 13% | Already correct |
| `layer-6-deliverable-long-read.md` line 104 | **25% → 5%** (wrong) | **20% → 13%** (fixed) | **Fixed this pass** |
| `layer-6-deliverable-document-executive.md` | no hit | no hit | OK |
| `layer-6-deliverable-document.md` | no hit | no hit | OK |

Long-read line 104 rewrite:
- Before: *"The standard tech-led-recovery story collapses from about 25 % probability under growth-baseline (S1 + S3 combined) to about 5 % under post-growth."*
- After: *"The standard tech-led-recovery story (S1 + S3 combined) collapses from about 20 % under growth-baseline to about 13 % under post-growth."*

### "gathered" → "assembled" sync

| File | Pre-pass | Post-pass |
|---|---|---|
| `layer-6-deliverable-long-read.md` line 30 | assembled | assembled (no change; already current) |
| `layer-6-deliverable-onepager.md` line 49 | gathered | **assembled** |
| `layer-6-deliverable-document-executive.md` line 85 | gathered | **assembled** |
| `layer-6-deliverable-document.md` line 31 | gathered | **assembled** |

### Lens 1 ratio explainer (Norway 1.06 / IE-UK 3.33-3.40)

| Surface | State |
|---|---|
| `layer-6-deliverable-long-read.md` line 30 | Has full gloss (1.00 same pace; 2.80 = 2.8× absorption; Norway 1.06; IE-UK 3.33-3.40) |
| `site/methodology.html` line 271 | Has full gloss |
| `layer-6-deliverable-document-executive.md` §2 Lens 1 | **Gloss inserted this pass** — sentence added after "The ratio defines corridor placement": *"A ratio of 1.00 means the two are running at the same pace; 2.80 means displacement is running at 2.8× absorption. Norway 1.06 sits well-absorbed; Ireland and the UK at 3.33–3.40 show displacement materially outpacing absorption."* |
| `layer-6-deliverable-document.md` | Specialist — already carries Lens 1 detail at finer technical grain |

### "The missing European countries" section

`site/methodology.html` 224–229 documents AL/ME/MD/XK/BY data-coverage exclusion. The Executive Edition's §5 already covers the candidate-coverage scope (BA/MK/RS/TR sub-cluster) — adding the AL/ME/MD/XK/BY detail would be net-additive beyond "today's locked-copy mirror sweep" and would dilute the §5 limits frame. **Deferred for Phil's call.** Same call for `layer-6-deliverable-document.md`. No edit this pass.

## 3. Long-Read PDF regeneration

```
$ python3 tools/long-read-pdf-gen.py
PDF saved: /Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-long-read.pdf
```

Output file: `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-long-read.pdf`
- Size: 1,786,549 bytes
- Timestamp: 2026-05-11 17:21
- Source `.md` carries: cite-as "Part 6" (line 30) ✓ · "Currently Failing" rename throughout ✓ · Lens 1 ratio gloss with Norway 1.06 + IE-UK 3.33-3.40 (line 30) ✓ · S1+S3 math 20% → 13% (line 104) ✓

## 4. Per-page version-stamp audit

| File | Pre-pass | Post-pass | Reason |
|---|---|---|---|
| `site/methodology.html` line 198 | 2026-05-11 | 2026-05-11 | Already current (no edit needed) |
| `site/sources.html` line 189 | 2026-05-11 | 2026-05-11 | Already current (no edit needed) |
| `site/glossary.html` line 171 | 2026-05-07 | **2026-05-11** | Bumped — page edited today ("Currently Failing" definition addition) |

## 5. Verification

### md5 — pre/post pass

| File | md5 pre-pass (session start) | md5 post-pass | Δ |
|---|---|---|---|
| `site/data.json` | `c8bebd1107552c89c7bca3f5f7f7c43b` | `c8bebd1107552c89c7bca3f5f7f7c43b` | **UNCHANGED** ✓ |
| `layer-6-deliverable-data.json` | `04c64b4292d929894d69d96549ee065f` | `04c64b4292d929894d69d96549ee065f` | **UNCHANGED** ✓ |
| `layer-6-deliverable-onepager.md` | `9ed9ed3ad472525847091ed317df2add` | `5e8cffaeeab9a62ddbbfc57ec029cf15` | changed (expected) |
| `layer-6-deliverable-document-executive.md` | `511e5061c754923c81dccb337fce7a31` | `3d94058b57f29f31bc9d18c44e81582c` | changed (expected) |
| `layer-6-deliverable-document.md` | `567a07ff83dca1ea192e1d1a8c7cd27a` | `f596ec8a381314af2b00b3a35f915279` | changed (expected) |
| `layer-6-deliverable-long-read.md` | `d12866d42932722faccc2a8e13016347` | `9ad49b3871e0ba007be88a0c5660d4ad` | changed (expected) |

Both data files md5 UNCHANGED ✓.

### Banned-phrase scan across deliverables

`stretched institutions | capability floor | stalled economy | stopped growing | bounding | bounded` →

| File | Hits | Notes |
|---|---|---|
| `layer-6-deliverable-onepager.md` | 0 | clean ✓ |
| `layer-6-deliverable-document-executive.md` | 1 — *"capability-floor breach scope is bounded above by the 2-digit ISCO ceiling"* (§5 line 81) | **Flag** — Executive is advisory-track register; this is technical-precision phrasing. Two ways out: (a) rewrite to plain-language ("capped at the 2-digit ISCO ceiling"); (b) leave as methodological-precision exception. Not auto-edited — Phil call. |
| `layer-6-deliverable-document.md` | 3 (lines 59, 219, 231) | Specialist appendix; technical language allowed per handover lock. No action. |
| `layer-6-deliverable-long-read.md` | 1 — *"economies have stopped growing in the conventional sense"* (line 62) | **Flag** — long-read mirrors `site/europe.html` line 221 which still carries the same phrasing. Site-side sweep is incomplete here; not a deliverable-vs-site divergence. Either fix both or leave both. Phil call. |

### "Layer 6" grep across deliverables

| File | Hits | Notes |
|---|---|---|
| `layer-6-deliverable-onepager.md` | 0 | ✓ |
| `layer-6-deliverable-document-executive.md` | 0 | ✓ |
| `layer-6-deliverable-document.md` | 3 (lines 1, 23, 127) | line 1 is the document title; lines 23 + 127 are historical/methodological references. Per handover note "Specialist Appendix keeps the technical version" — `Layer 6` as the internal/technical name is intentional. Title rename (line 1 → `Part 6`) deferred for Phil's call. |
| `layer-6-deliverable-long-read.md` | 0 | ✓ |

## Summary

- **Files edited:** `layer-6-deliverable-onepager.md` (Italy + Conclusion + assembled), `layer-6-deliverable-document-executive.md` (Italy + Conclusion + assembled + Lens 1 gloss + §6 heading), `layer-6-deliverable-document.md` (assembled), `layer-6-deliverable-long-read.md` (math fix), `site/glossary.html` (version stamp).
- **PDF regenerated:** `layer-6-deliverable-long-read.pdf` (1.79 MB, 17:21).
- **Data files unchanged:** both `data.json` files match pre-pass md5.
- **Open items for Phil:** (1) "bounded above" in Executive §5 line 81 — rewrite or keep as precision; (2) "stopped growing" in long-read line 62 — mirrors site/europe.html; (3) `Layer 6` title at main-document line 1 — rename to `Part 6` or keep as technical internal; (4) "missing European countries" section propagation to Executive + main document — deferred as net-additive content beyond mirror sweep.
- **Deploy-readiness:** the deliverable suite is internally consistent with the site SOT on the locked elements from 2026-05-09 + 2026-05-11. Phil handles git + deploy.

---

## Addendum — Phil follow-ups applied (2026-05-11, post-report)

| # | Open item | Phil decision | Action taken |
|---|---|---|---|
| 1 | Executive §5 line 81 `bounded above` | rewrite | `bounded above by` → `capped at` (plain-language; same meaning) |
| 2 | Long-read line 62 `stopped growing` | good (leave) | No change; mirrors `site/europe.html` line 221 |
| 3 | Main-document `Layer 6` title | rename | line 1 title: `Layer 6` → `Part 6`; line 23 body: `Layer 6 ships the result` → `Part 6 ships the result`; line 127 body: `Layer 6 is its first end-to-end application` → `Part 6 is its first end-to-end application` |
| 4 | Missing-countries section propagation | deferred is fine | No change |

Post-addendum md5:
- `layer-6-deliverable-document-executive.md` = `fbc305fa114fea1af70db96d2b225d60`
- `layer-6-deliverable-document.md` = `2e4a1bf9cfbd216897b15fb722022b34`

Note: `layer-6-deliverable-document.md` line 219 retains `bounded above by demographic-buffer orthogonality` — specialist technical content, kept per handover lock ("Specialist Appendix keeps the technical version"). Phil's "rewrite" decision applied only to the Executive Edition where advisory-track plain-language is the register.

## Addendum 2 — Missing-countries section propagation (2026-05-11)

Phil reversed the earlier "deferred" call on item (4): add the missing-countries scope note to long-read + executive methodology sections; skip main document (already technical-detailed in its scope subsection).

| File | Insertion point | Action |
|---|---|---|
| `layer-6-deliverable-long-read.md` | §6 scope/constraints block, after the "three known gaps" paragraph | **Added** — new paragraph: AL/ME/MD (EU candidates, data-coverage gap), XK (partial recognition + SAA, same gap), BY (sanctions + no integration path) + reopens "when coverage improves, they can be added without changing the methodology" |
| `layer-6-deliverable-document-executive.md` | §5 limits, after the "five honest limits" paragraph | **Added** — same content, register-matched to the rest of §5 |
| `layer-6-deliverable-document.md` (specialist) | n/a | **Skipped** per Phil — line 59 already documents the 36-country scope at finer technical grain |

Long-Read PDF regenerated to absorb the change:
- File: `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-long-read.pdf`
- Size: 1,787,959 bytes (+1,410 vs prior pass)
- Timestamp: 2026-05-11 17:28

Post-Addendum-2 md5:
- `layer-6-deliverable-long-read.md` = `b0a08497c6ac715b9a74c7cca5865da2`
- `layer-6-deliverable-document-executive.md` = `2d880fe90d973a98181ced5a207c6be1`

---

⚠️ Code Review Summary (code-craft rubric)
- Names: pass — no code identifiers introduced
- Nesting depth: n/a (markdown edits + 1 single-line HTML edit + 1 Python script execution, no code authored)
- Hidden dependencies / side effects: PDF generator wrote `layer-6-deliverable-long-read.pdf`; both `data.json` md5s unchanged (verified)
- Duplication: knowledge-level mirroring is intentional (One-Pager + Executive mirror findings.html locked copy)
- Local-style match: pass — Markdown headings + advisory-track register align with surrounding sections; HTML edit matches sibling `byline` patterns
- Honest signatures: n/a (no code authored this pass)
- Things I chose NOT to add (YAGNI): (a) missing-countries section in Executive + main document (out of scope for mirror sweep); (b) `Layer 6 → Part 6` rename in main document title (handover scoped to One-Pager + Long-Read only); (c) automated rewrite of "bounded" + "stopped growing" banned-phrase hits (Phil call); (d) no helper script to verify md5 / PDF — direct shell commands sufficient
- Uncertainty / assumptions a human should verify: PDF visual output (cite-as "Part 6", "Currently Failing", Lens 1 gloss render correctly across page-breaks); Executive §6 heading rename (`Closer` → `Conclusion`) consistent with Phil's TOC/navigation intent for the Executive Edition; banned-phrase flags above
