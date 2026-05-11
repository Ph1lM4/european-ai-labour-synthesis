# Problem 3 — §3 ↔ §4 cross-linking

## What the interaction must surface

Every country lives in both a corridor (§3) and a class (§4). The current site shows two independent blocks. The reader has to mentally reconstruct the relationship. The interaction makes the relationship visible without forcing a Sankey or other heavy chart.

## Alternatives

- **A — Bidirectional hover-highlight.** Hover a country tile → its class card lights up with the orange ring. Hover a class card → that class's countries get the orange outline. Always-on, no clicks, no learnable affordance. Discoverable on desktop; on touch, tap acts as hover.
- **B — Click to filter.** Click a class card → the country grid dims everything except that class (30% opacity, slight grayscale). Persistent filter badge with a clear button. Works on touch; intent-driven; supports "I want to focus on Class III for a paragraph."

## Recommended pattern: A + B coexist

Hover-highlight is the discovery layer (no learning required, fires on any pointer movement). Click-filter is the persistence layer (works on touch, useful for sustained reading). The two patterns are not in conflict: hover sets a transient highlight; click sets a sticky filter that hover doesn't override.

The combined behaviour:
- Hover a tile → its class card highlights (transient)
- Hover a class card → its tiles highlight (transient)
- Click a class card → tiles dim except that class (sticky)
- Click again or Esc → filter clears
- Tap (touch device) acts as click

Phase 2B can build both behaviours in one pass. Estimated additional cost over either alternative alone: ~30 min (a single state machine handling transient vs sticky highlight).

## Trade-offs

| | A — Hover-highlight | B — Click-filter | A + B combined |
|---|---|---|---|
| Discoverability | Excellent | Lower (no affordance hint) | Excellent (hover teaches the relation; click reinforces) |
| Touch device | OK (tap as hover) | Excellent | Excellent |
| Persistent filter | No | Yes | Yes |
| Build cost | Minor | Moderate | Moderate (one pass for both) |
| Constraint on Problem 1 | Country tile must be a button with `data-class` | Same | Same |

## Constraint propagated to Problem 1

Whichever Problem 1 alternative Phil locks must support the cross-link hooks: each country element needs a `data-code` and `data-class` attribute and must be a button or focusable element. All three Problem 1 alternatives (A geographic, B beeswarm, C list) already meet this constraint.
