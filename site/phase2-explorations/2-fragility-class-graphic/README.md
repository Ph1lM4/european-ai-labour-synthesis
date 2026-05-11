# Problem 2 — Fragility-class graphic

## What the visual must surface

The 9 / 9 / 15 / 3 distribution across Classes I / II / III / IV; the population-weighted distribution that diverges from country count (EU-27 Class I = 25.6% of pop on 7 markets; 36-market Class IV = 15.7% pop on 3 markets); the rule that places countries in each class; and the qualitative break at Class IV (cascade is not "worse Class III"). The current 4-card panel reads as enumeration and misses all of the above.

## Alternatives

- **A — Distribution funnel.** Four horizontal bars, widths proportional to country count. Class III bar is the widest (15) and the visual punchline. Class IV is visually separated below a dashed divider because the cascade is qualitatively distinct, not the linear extension of "worse."
- **B — Population-weighted stack.** Two horizontal stacked bars (EU-27 + 36-market), each segment width = % of working-age population in that class. Reveals the count-vs-population asymmetry and the Class IV asymmetry between EU-27 (0 markets) and 36-market (3 markets, 15.7% of pop) directly.
- **C — Corridor → Class Sankey.** Left side: baseline corridor (C1 / C2 / C3). Right side: class (I / II / III / IV). Ribbon thickness = country count. Surfaces the relational rule: Class III markets are already in C3 baseline; Class II markets are stable in C1 / C2 baseline but fracture; Class IV markets are baseline-C2 candidates with extreme Lens 5 readings.

## Trade-offs

| | A — Funnel | B — Pop stack | C — Sankey |
|---|---|---|---|
| Distribution legibility | High (count visible) | High (population visible) | Moderate (relation visible, count secondary) |
| Population weighting | No | Yes (the differentiating feature) | No |
| Rule visible | Yes (rule in bar) | No (rules omitted for compactness) | Yes (visible from corridor → class flow) |
| Class IV separation | Explicit (dashed divider) | Implicit (small segment) | Implicit (small ribbon) |
| Mobile | Excellent (bars stack) | Good | Tight at 375w (svg compresses) |
| Build cost | Minor (CSS bars) | Minor-to-moderate (data binding) | Heavy (Sankey layout maths) |
| Editorial register fit | Storytelling-aligned | Storytelling-aligned | Methodology-paper-leaning |

## Note

Alternative B is the only option that ties to the Bundle X aggregate panels already on `europe.html`. If Phil locks Problem 5 around delta-strip primary-view (which highlights the EU-27 / 36 asymmetry), B reinforces the same story and the two views become a coherent pair. If Phil prefers a country-count-first reading, A wins.
