# Handover Prompt — Bundle O Phase 2E: Sources Audit + Draghi Addition

Bounded research + composition session. **Exhaustive** audit of the current synthesis `sources.html` against `DATA-REGISTRY.md` + every source on each of the 5 sister-layer sources pages. Identifies all sources that inform Layer 6 synthesis (Draghi 2024 confirmed; expected 10–30+ others depending on audit). Adds Tier 1 / Tier 2 source-cards for every relevant addition, adds a "See also" cross-layer footer, updates byline + llms.txt source counts. ~2.5–3.5 h.

**Code task — load `skills/code-craft/SKILL.md` before generating code (CLAUDE.md Rule 3.5).**

---

## Context

The synthesis project's `sources.html` was inherited from Bundle N (Specialist Appendix source-cards) and never explicitly audited across Phase 1A → 2D. The Phase 2D ship-ready audit counted 15 primary sources; Phil's review on 2026-05-07 surfaced that **Draghi 2024 (The Future of European Competitiveness)** is missing. Layer 7 RATIONALE.md cites Draghi as the structural anchor for Tier 1 work, but synthesis itself never references it. Likely other gaps too — this brief audits and fills.

The cross-layer source bridge (sister-layer sources lists) is also unsynced; synthesis is the *synthesis* of L1–L5 and should at minimum link out to those layer sources rather than duplicate or ignore them.

---

## START PROMPT

I need you to audit the current synthesis `sources.html`, identify omissions against `DATA-REGISTRY.md` + 5 sister-layer sources pages, add the Tier 1 / Tier 2 source-cards for the missing items (Draghi 2024 confirmed + any others surfaced), add a cross-layer "See also" footer, and update the byline + llms.txt source-count downstream. Banned-phrase scan on all new copy.

### Read FIRST (absolute paths)

**Synthesis (audit + write target):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/sources.html` — current 15 primary source-cards
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/llms.txt` — source-count reference (currently "15 primary")
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/site/index.html` + `findings.html` + `scenarios.html` + `europe.html` + `methodology.html` + `glossary.html` — 7 pages with the second byline that references "15 primary sources"; needs source-count refresh

**Cross-layer source registries (read for audit):**
- `/Users/philippmaul/Documents/projects/DATA-REGISTRY.md` — project-level dataset registry (179 lines)
- `/Users/philippmaul/Documents/projects/european-ai-exposure-map/site/sources.html` (Layer 1, 662 lines)
- `/Users/philippmaul/Documents/projects/european-careers-map/site/sources.html` (Layer 2, 274 lines)
- `/Users/philippmaul/Documents/projects/european-disruptions-map/site/sources.html` (Layer 3, 351 lines)
- `/Users/philippmaul/Documents/projects/european-demographics-map/site/sources.html` (Layer 4, 354 lines)
- `/Users/philippmaul/Documents/projects/european-reskilling-map/site/sources.html` (Layer 5, 581 lines)

**Layer 7 evidence base (already includes Treichl + Klinger):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-actions/RATIONALE.md` — Tier 1 evidence inputs section (logged 2026-05-06)

### Audit procedure

**Step 1 — Inventory.** Read synthesis `sources.html`. Extract the current 15 primary source-cards with their citation strings, tier assignments, and how-used summaries. Build a working list.

**Step 2 — Cross-reference.** For each sister-layer `sources.html`, scan for sources that:
- Directly inform any of the 5 lenses (L1 displacement velocity, L2 demographic buffer, L3 distributional fold, L4 polycrisis drag, L5 jurisdictional buffering)
- Underpin the corridor-edge thresholds (1.20 / 2.80) or the strict-zero finding
- Anchor any of the 8 scenarios (S1 Reinstatement Revival, S2 Climate Adaptation Boom, S3 Jobs Transform, S4 Muddle Through, S5 Wage Cliff, S6 Reinstatement Failure, S7 Bandwidth Fracture, S8 Polycrisis Drag)
- Provide the population / area / institutional data feeding the per-country fragility-class assignments

Build a candidate-additions list. Each candidate carries: source citation, where it currently lives (which sister-layer sources.html), why it applies to synthesis (explicit lens or finding it informs), proposed tier (1 or 2), proposed how-used summary.

**Step 3 — Confirm Draghi 2024.** Add as Tier 1 regardless of audit:

> **Mario Draghi, *The Future of European Competitiveness* (Sept 2024).** Strategic anchor for the European competitiveness diagnosis. Direct overlap with Lens 5 (institutional adaptive capacity) — Draghi's whole thesis is the institutional-capacity gap; this is the closest external echo of Lens 5's analytical surface. Productivity-gap framing supports the strict-zero finding (Europe's capacity to absorb structural shocks has degraded versus the US over 20 years). Bridges to Layer 7's Tier 1 framing. URL: `https://commission.europa.eu/topics/strengthening-european-competitiveness/eu-competitiveness-looking-ahead_en`

**Step 4 — Treichl + Klinger LinkedIn posts (Phil-decision flag).** These are already in Layer 7 RATIONALE.md as Tier 1 evidence inputs. Two options:
- (a) Cross-reference from synthesis sources as Tier 2 ("see also: Layer 7 evidence base") — preserves the Layer 6 / 7 separation
- (b) Add as Tier 2 source-cards directly in synthesis sources.html — more discoverable but duplicates Layer 7's evidence

Sub-session picks (a) by default; flags (b) for Phil reconsideration if the audit surfaces strong reason. Surface the choice in report-back.

**Step 5 — Exhaustive audit; no cap.** Every source on each of the 5 sister-layer `sources.html` files gets reviewed individually for synthesis-relevance. For each source ask:
- Does it inform any of the 5 lenses (Lens 1 displacement velocity, Lens 2 demographic buffer, Lens 3 distributional fold, Lens 4 polycrisis drag, Lens 5 jurisdictional buffering)?
- Does it underpin any of the 8 scenarios (S1–S8) or any corridor-edge / fragility-class threshold?
- Does it provide population, area, ALMP, regulatory, or institutional data feeding per-country reads?
- Is it cited (even implicitly) in the synthesis findings prose?

If yes to any: add as Tier 1 (direct empirical input) or Tier 2 (analytical / contextual / strategic). If a source applies to multiple lenses or scenarios, name all in the "how informs" copy.

**Tier assignment principles:**
- Tier 1: direct empirical input to the corridor scoring, regime classification, fragility-class assignment, scenario-probability vectors, or capability-floor breach scope (e.g., Eurostat EUROPOP, Cedefop projections, Autor 2024, ESCO, OECD EPL, Anthropic Economic Index)
- Tier 2: analytical / strategic / contextual anchors that inform interpretation but don't feed numbers (e.g., Draghi 2024, IPCC AR6 likelihood-scale, ECRA, named expert posts/papers that frame mechanisms)

Surface the full audit list in report-back, organised by sister-layer-source-of-origin + tier assignment + how-informs reasoning. No artificial cap — if the audit surfaces 30+ relevant additions, ship 30+. Final source count after audit will likely jump from 15 → 30-50 range; this is expected scope-correction, not over-inclusion.

**Step 6 — "See also" cross-layer footer.** Add a new section to `sources.html` titled *"Sister-layer source bases"* (or similar) with 5 link cards, one per sister layer:

| Layer | Page name | URL | One-line scope |
|---|---|---|---|
| Layer 1 — AI Exposure | AI Exposure Map sources | `https://ai-exposure.nexalps.com/sources.html` | AI exposure indices, occupation taxonomies, productivity studies |
| Layer 2 — Job Market | Job Market sources | `https://job-market.nexalps.com/sources.html` | European job-posting datasets, wage indices, employer behaviour |
| Layer 3 — Disruptions | Historical Disruptions sources | `https://disruptions.nexalps.com/sources.html` | 580 years of technology disruption case base, ATM/forklift/spreadsheet anchors |
| Layer 4 — Demographics | Demographics sources | `https://demographics.nexalps.com/sources.html` | Eurostat EUROPOP, working-age trajectories, retirement-offset data |
| Layer 5 — Reskilling | Reskilling Capacity sources | `https://reskilling.nexalps.com/sources.html` | ALMP datasets, training throughput, transition-velocity literature |

Source the one-line scopes from the actual landing/intro of each sister-layer sources.html (not invented). Use existing card styling.

### Composition

For each new source-card:
- Use the existing card markup pattern from `sources.html` (sub-session reads + matches)
- Tier label: visible per existing convention
- Citation: full bibliographic / URL form
- "Used by" / "How it informs": 2–3 sentences naming the specific lens / scenario / finding it underpins
- No banned phrases (`load-bearing`, `structurally`, `the analysis is built to surface`, `read` as singular noun for analysis)

### Downstream updates

After source additions:

**1. Update second byline on all 7 pages.** Current text (Phase 2D-locked):

> *Based on [15 primary sources](sources.html) including Autor 2024 (QJE), Cedefop 2025, the EU Net-Zero Industry Act, the European Climate Risk Assessment, and Eurostat EUROPOP2023.*

Update the count + add Draghi to the named-five if it ranks higher than one of the existing names by analytical leverage. Sub-session decides whether Draghi displaces (recommend: replace EU Net-Zero Industry Act with Draghi, since Draghi is the higher-tier strategic anchor). Surface the new byline text in report-back; Phil locks at next turn.

**2. Update `llms.txt` "Sources (N primary)" line.** Match the new count + add Draghi to the comma-separated source-name list.

**3. Update sources.html intro / preamble** (if it states "15 primary sources" or similar) to match the new count.

**4. Update JSON-LD on sources.html** (Article schema) — refresh `dateModified` to `2026-05-07`. If the JSON-LD references source count, refresh.

### Constraints

- **No new design tokens.** Use existing source-card / tier-pill styling.
- **No external libraries.**
- **`data.json` + `layer-6-deliverable-data.json` unchanged.**
- **Phase 1B / 2B / 2C / 2D IA preserved.**
- **No emoji.**
- **Banned-phrase scan applies to all new source-card copy** (per the brain rule landed 2026-05-06).
- **Phil does all git commits.**

### Verification (before reporting back)

1. Draghi 2024 added as Tier 1 in `sources.html`, with full citation + "how informs" copy + URL.
2. All Tier 1 / Tier 2 additions per the exhaustive audit. No cap. Each addition has full citation + URL + tier label + 2–3 sentence "how informs" copy naming the specific lens / scenario / finding it underpins.
3. "See also" cross-layer footer added with 5 link cards (one per sister layer) + sourced one-line scopes.
4. Updated source count on `sources.html`, all 7 page bylines, `llms.txt`, and any JSON-LD references.
5. Banned-phrase grep clean across all new copy.
6. Pre-existing source-cards untouched (no rewrites of inherited content beyond the count delta).
7. Live-site files outside `sources.html`, `llms.txt`, and the 7 pages' bylines are untouched (`git status` should show edits to those files only).
8. Sources.html still parses; JSON-LD valid.

### When done — report back to master session with

1. **Full audit table** — every source from each of the 5 sister-layer `sources.html` files, with synthesis-relevance verdict (include / exclude / already-present), proposed tier, and how-informs reasoning. Organised by sister-layer-source-of-origin. Counts at end: total reviewed / total added / total excluded with rationale.
2. **Final additions list** — Draghi 2024 + all other additions surfaced by the audit, with full citation + URL + tier + "how informs" per source.
3. **Treichl + Klinger decision** — option (a) or (b), with reasoning.
4. **Updated source count** — new total + the diff (was 15 + N additions = X total).
5. **Proposed updated byline text** — with Draghi included; surface for Phil lock at next turn.
6. **Updated `llms.txt` "Sources" line.**
7. **Cross-layer footer audit** — scope strings sourced from each sister-layer's actual sources.html intro (no invention).
8. **Banned-phrase grep audit** — confirm 0 hits in all new copy.
9. **Bundle W readiness** — anything new this session that Bundle W deliverable-doc updates need to absorb (likely: same source additions need to propagate to `layer-6-deliverable-document.md` + executive doc + appendix).
10. **Any candidate brain captures** — pattern observation: process-level rule for sources audits at phase boundaries (similar in family to the banned-phrase-propagation rule already landed 2026-05-06).

## END PROMPT
