# Problem 4 — Weather-pattern viz

## What the visual must surface

Three regimes (growth / secular stagnation / post-growth) reshape scenario probabilities. The dramatic shift: tech-led S1 drops from ~25% under growth to ~5% under post-growth; S2 Climate Adaptation Boom rises 22% → 30%. 38.5% of EU-27 working-age population lives under post-growth — this isn't a corner case. Regime is country-level and stable on a multi-year horizon, not a scenario in itself.

The current 3-card text panel reads as a glossary entry. It misses the probability-shift drama and the population callout.

## Alternatives

- **A — Probability-shift bars (small multiples).** Three cards, each shows the seven routine scenarios as horizontal bars sorted by probability. The same scenario appears in different rank positions across the three regimes — the rank inversion *is* the data. Includes the population-share callout and a shift summary sentence below the grid.
- **B — Weather-icon cards.** Keeps the existing 3-card layout. Adds a single inline-SVG icon per regime (sun / partly-cloudy / overcast), the modal routine variant as a pull-quote inside the card, plus the population share. Decorative icons are an aesthetic upgrade; the data is in the modal scenario and population share.

## Trade-offs

| | A — Probability-shift bars | B — Icon cards |
|---|---|---|
| Surfaces the shift | Yes (rank inversion is the visual) | No (modal scenario surfaced; shift remains implicit) |
| Population callout | Yes (per-regime, both EU-27 and 36) | Yes (per-regime, both EU-27 and 36) |
| Build cost | Moderate (sorted bars, scaled widths) | Minor (existing 3-card structure + 3 icons + pull-quote) |
| Mobile | Good (cards stack; bars compress) | Excellent (no chart logic) |
| Editorial register | Storytelling (the shift is the story) | Glossary-with-aesthetic (still slightly dictionary-flavoured) |
| Risk | Three-way visual comparison demands more reader effort | Doesn't earn the Problem-4 brief: shift remains untold |

## Note

C — Sankey/flow diagram (optional in brief) is skipped: A and B bracket the design space adequately. A Sankey would visualise the shift more dramatically than A but at heavy build cost and chart-literacy cost; A delivers ~80% of the same story at a fraction of the build effort.
