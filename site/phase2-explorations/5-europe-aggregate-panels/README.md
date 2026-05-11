# Problem 5 — Europe aggregate panels

## What the visual must surface

EU-27 is a strict subset of the 36-market scope. The current side-by-side tabular layout reads as a comparison table; it misses (a) the subset-superset structural relationship, (b) the Class IV asymmetry that places the cascade pressure in the ring (EFTA-4 + UK + 4 candidates), and (c) the variation-guard principle: variation IS the read, aggregates are reference points.

## Alternatives

- **A — Subset wrapper.** 36-market panel as outer container; EU-27 panel nested inside it. The 9-country ring between them is labelled where the cascade pressure sits (Class IV: 0 EU-27 markets → 3 in 36-market). A delta strip at the foot summarises the asymmetries. Layout dramatises the subset relationship.
- **B — Primary view + delta strip.** 36-market is the single primary read; a delta strip above it shows what *changes* when you restrict to EU-27. One read, not two. Foregrounds the variation-guard already on the live page (variation IS the answer; the EU-27 "comparison" is itself a restriction-induced delta).

## Trade-offs

| | A — Subset wrapper | B — Delta strip + primary |
|---|---|---|
| Subset relationship | Visual (nested) | Implicit (delta says "what changes when restricted") |
| Variation-guard alignment | Moderate (still shows two panels) | High (one read; deltas reinforce variation-IS-the-answer) |
| Class IV asymmetry | Surfaced via ring label | Surfaced via top delta item |
| Build cost | Moderate (nested panel layout, ring label, mobile collapse needs care) | Minor-to-moderate (delta grid + primary panel reuses existing pattern) |
| Mobile | Tight (nested cards stack but read heavy) | Excellent (delta grid collapses 4→2→1 cols; primary panel single-column) |
| Visual weight | Heavy (two cards nested + ring + deltas = 3 information bands) | Lighter (1 delta strip + 1 primary panel) |
| Storytelling | "Here is the whole; here is the part inside" | "Restricting to EU-27 is itself a transformation; here is its shape" |

## Note

C — Stacked comparison (optional in brief) was skipped: paired comparison density is what the current site already does, so it adds no design-space coverage. A and B bracket the design space.

The two alternatives encode different editorial stances:
- A foregrounds *containment* (EU sits inside Europe).
- B foregrounds *the act of restriction* (the EU view is a transform).

Phil picks based on which stance he wants the page to make.
