# Handover Prompt — Cross-Layer Enrichment Audit (Layer 6 ← Layers 1–5)

Bounded read-only audit. Identifies data + findings sitting in Layers 1–5 that Layer 6 currently underuses or doesn't surface. Output is a structured priority-ranked report; no Layer 6 modifications. ~60–90 min.

---

## Context

Layer 6 (European AI Labour Market Synthesis) is mid-Phase-4 — Bundle M (SOT JSON) and Bundle N (Specialist Appendix) shipped; Bundle N2 (Executive + One-Pager + Einfache) ran in parallel and has been through editorial review; Bundle N3 (Long-Read) and Bundle O (site) are queued.

During the editorial review, two enrichment opportunities surfaced from Layer 4 (demographics): granular country-level retirement-offset data + Zone A/B/C/D substitution matrix that would replace Layer 6's current single-string Lens 2 rendering with a richer per-country / per-zone reading. Before committing to a bounded re-Phase-3 round (Bundle P) for Layer 4 enrichment, Phil wants a **systematic audit across all 5 evidence layers** to surface every comparable enrichment opportunity, not just the one that surfaced reactively.

---

## START PROMPT

I need you to audit all 5 evidence layers of the European AI Labour Market suite (Layers 1–5) for data + findings that Layer 6 (Synthesis) currently underuses or doesn't surface. Read-only — no Layer 6 modifications. Output is a priority-ranked report that informs whether to commission additional bounded re-Phase-3 rounds before Layer 6 ships fully.

### Read FIRST (absolute paths)

**Layer 6 (anchor — what's already there):**
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-data.json` — SOT JSON (162.7 KB, schema v1.0). The canonical record of what Layer 6 carries.
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-lens-framework.md` — locked spec. Lens definitions are the lookup for "what Layer 6 was supposed to test."
- `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/layer-6-deliverable-document.md` — Specialist Appendix. Carries the load-bearing findings + caveats + §5 honest limits. The §5 paragraph names known underuse points.

**Layers 1–5 (sources to audit):**
- L1 — `/Users/philippmaul/Documents/projects/european-ai-exposure-map/` (capability floor / AI exposure)
- L2 — `/Users/philippmaul/Documents/projects/european-careers-map/` (job market — current employment / wage / skills)
- L3 — `/Users/philippmaul/Documents/projects/european-disruptions-map/` (historical analogues — 580 years)
- L4 — `/Users/philippmaul/Documents/projects/european-demographics-map/` (demographics / retirement / Zone matrix)
- L5 — `/Users/philippmaul/Documents/projects/european-reskilling-map/` (ALMP / transitions / country systems)

For each layer: README.md, primary data file (`*-data.json`), and llms.txt (machine-readable project summary). If a finding looks load-bearing for Layer 6 enrichment, sample the relevant source file in the layer's `data/` subfolder.

### Audit method

For each of the 5 layers:

1. **Inventory the layer's load-bearing findings** — read README + llms.txt + skim primary data file. List 5–10 findings that are central to the layer.
2. **Map findings against Layer 6's lenses + sections** — for each finding, ask: does Layer 6 already use this? Where? Is the use full-fidelity, lossy, or absent?
   - Full-fidelity: Layer 6 surfaces the finding at its native granularity.
   - Lossy: Layer 6 surfaces a compressed version (e.g. single-string Lens 2 rendering when L4 has per-country/per-zone variation).
   - Absent: Layer 6 doesn't surface the finding at all.
3. **For each lossy or absent finding, score the enrichment opportunity** along three axes:
   - **Strength** — how load-bearing the finding is for Layer 6's narrative (high / medium / low)
   - **Cost** — rough estimate of sub-session work to integrate (small <30 min / medium 30–90 min / large >90 min)
   - **Knock-on** — how many downstream files would update if Layer 6 absorbs the finding (Executive / One-Pager / Einfache / Specialist Appendix / Bundle N3 / Bundle O / glossary)
4. **Flag scope-boundary cases** — findings that look enrichment-worthy but actually belong in Layer 7 (Actions) or a different layer's home, not Layer 6 (Synthesis).

### Goal — output `cross-layer-enrichment-audit-2026-04-30.md`

A single structured report at `/Users/philippmaul/Documents/projects/european-ai-labour-synthesis/cross-layer-enrichment-audit-2026-04-30.md` with these sections:

```
# Cross-Layer Enrichment Audit — Layer 6 ← Layers 1–5

## Summary table
| Layer | High-priority opportunities | Medium-priority | Low-priority / scope-boundary |

## Per-layer detail
### Layer 1 — AI Exposure
- Finding 1: [name]
  - Layer 6 use: full / lossy / absent
  - Strength × Cost × Knock-on
  - What enrichment would look like
- Finding 2 ...

### Layer 2 — Job Market
... (same structure)

### Layer 3 — Disruptions
... (same structure)

### Layer 4 — Demographics
- Finding 1: country-level working-age decline projections (EUROPOP2023)
  - Layer 6 use: ABSENT
  - Strength: HIGH (Lens 2 sharper read; underused)
  - Cost: medium (60-90 min sub-session)
  - Knock-on: Executive §2 + Specialist Appendix + One-Pager finding 2 + glossary + §5 limits
  - What enrichment would look like: replace single-string Lens 2 rendering with per-country + Zone A/B/C/D heterogeneity
- ... (other L4 findings)

### Layer 5 — Reskilling
... (same structure)

## Recommended bundles (priority-ranked)
| Bundle | Layer | Scope | Estimated cost | Recommendation |
| Bundle P | L4 | Lens 2 demographic enrichment | ~90 min | RECOMMEND — already discussed |
| Bundle Q | L? | ... | ... | ... |
| Bundle R | L? | ... | ... | ... |

## Scope-boundary cases (NOT for Layer 6)
- Finding X (Layer Y): belongs in Layer 7 because [reason]
- Finding Z (Layer Y): belongs in [other layer] because [reason]

## Not-worth-the-cost flags
- Findings where the enrichment cost outweighs the strength.

## Honest limits of this audit
- Time-bounded read; does not deeply inspect every L1–L5 source file.
- Strength scoring is the auditor's judgment, not Phil's.
- Final go/no-go on each bundle is Phil's, not the audit's.
```

### Constraints

- **READ-ONLY across the board.** Do not modify any Layer 1–5 files. Do not modify Layer 6 SOT JSON, Specialist Appendix, or any executive/one-pager/einfache/glossary files.
- **No write outside the audit report.** The single output is `cross-layer-enrichment-audit-2026-04-30.md` at the path specified.
- **Do not commit.** Phil does all git commits.
- **Prioritise breadth over depth.** Goal is to surface the full set of enrichment opportunities, not deeply analyse any single one. Phil chooses which to commission as bundles after reading the audit.
- **No fabrication (BR-19).** Every finding cited from Layers 1–5 must trace to a specific file path + section/heading in the source layer.
- **Scope-discipline:** if a finding looks enrichment-worthy but actually belongs in Layer 7 (Actions), flag it in the scope-boundary section, don't include it in the recommended bundles.
- **Don't re-design Layer 6.** The audit identifies what's underused; it doesn't propose architectural changes to lens definitions or scenario taxonomy.

### Verification (before reporting back)

1. Audit report exists at the specified path with all required sections.
2. Each of the 5 layers has at least 3 findings inventoried.
3. Each enrichment opportunity has all three axes scored (Strength × Cost × Knock-on).
4. Bundle P (Layer 4 / Lens 2) is one of the recommendations — sanity check on prior-discussion alignment.
5. At least one scope-boundary case is flagged (if none surface, that's also a valid finding — note it explicitly).
6. Recommended bundles are priority-ranked, not just enumerated.

### When done — report back to master session with

1. Total enrichment opportunities surfaced per layer (count).
2. Top 3 highest-priority bundles by your scoring.
3. Any surprises — opportunities that surfaced unexpectedly or didn't land where expected.
4. Layer-level read: which layer is most underused by Layer 6, which is best integrated.
5. Recommendation: bundles to commission before Bundle O dispatches vs bundles to defer to Phase 5+ post-O candidate work.
6. Any candidate brain captures (cross-layer integration patterns, T35-adjacent observations).

## END PROMPT
