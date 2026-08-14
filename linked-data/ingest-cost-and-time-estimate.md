# Linked-data ingest — time & cost estimate

Reference document for a future business case. Summarizes a back-of-envelope
projection made before any large-scale extraction had been run, then reconciles
it against real data from a 100-page extraction actually carried out (see
`poc/reconciliation.md` for the ontology findings from that run — this document
covers only time and cost).

## Scope options

Four candidate scopes, based on the actual file counts in this docs snapshot:

| Scope | Pages | Basis |
|---|---|---|
| Initial POC | 100 | The original proof-of-concept sample size |
| `server/current` + `cloud` | ~1,500 | The realistic "cover the current docs surface" next step |
| Everything, every product, latest version only | 3,919 | One page per product per topic, skipping superseded version trees |
| Everything, every product, every version | 12,369 | The absolute ceiling — the whole snapshot, every version of every product |

## Projected figures (made before any large run)

**Machine time** assumed strictly sequential processing (one page waits for the
last to finish, to keep a shared term registry consistent), at roughly 20–60
seconds per page. **Human review time** assumed a 20% flag rate (one item needing
a judgment call per five pages, based on a 5-page hand-run) at a few minutes each.

| Scope | Pages | Sequential machine time | Human review time (20% flag rate) |
|---|---|---|---|
| POC | 100 | ~1.5–2 hours | ~1–2 hours |
| `server/current` + `cloud` | ~1,500 | ~1 day, unattended | ~2–4 days, spread out |
| Latest version only | 3,919 | ~1.8 days, unattended | ~1.3 weeks, spread out |
| Everything, every version | 12,369 | ~1 week, unattended | ~3–5 weeks, spread out |

**Token cost** assumed a single structured-output API call per page (~3,000 input
tokens for page content + running registry, ~400 output tokens for the extracted
JSON record), at list pricing current as of 2026-08-07 (Claude Sonnet 5's
introductory rate runs through 2026-08-31; Claude Fable 5 is Anthropic's most
capable, most expensive model; Claude Haiku 4.5 is the cheapest plausibly-adequate
tier):

| Model | Rate ($/1M in / out) | $/page | 100 pages | 1,500 pages | 3,919 pages | 12,369 pages |
|---|---|---|---|---|---|---|
| Claude Sonnet 5 (intro) | $2 / $10 | $0.010 | $1.00 | $15.00 | $39.19 | $123.69 |
| Claude Fable 5 | $10 / $50 | $0.050 | $5.00 | $75.00 | $195.95 | $618.45 |
| Claude Haiku 4.5 | $1 / $5 | $0.005 | $0.50 | $7.50 | $19.60 | $61.85 |

Headline conclusion at the time: compute cost is a non-issue at every scale
considered (low hundreds of dollars even at the extreme), and model-tier choice
should be driven by extraction quality, not price.

## What actually happened on the 100-page run

The 100-page batch (50 `server/`, 50 `cloud/`) was extracted as **10 parallel
subagents**, each handling 10 pages, rather than one sequential call per page —
a materially different execution architecture from the one assumed above. Real
figures, aggregated from the run's own usage reporting:

- **Wall-clock time: under one hour**, not the ~1.5–2 hours projected for
  sequential processing at this scale. The 9 batches that completed on the first
  attempt all finished within about 14 minutes of each other (they ran
  concurrently, so total time is set by the slowest one, not the sum). One batch
  hit a session usage limit partway through and needed a second, sequential pass
  to finish its remaining pages, adding about 35 minutes — still well under the
  original estimate. Parallelism, when actually used, delivered the speedup the
  original estimate treated as optional.
- **Token consumption per page ran ~3.4x higher than assumed.** Total usage
  across the logged batches was ~1,134,000 tokens for 97 pages (one partial
  batch's early pages weren't separately logged before it hit the session
  limit) — about 11,700 tokens/page, versus the 3,400 tokens/page (3,000 in + 400
  out) the original single-call estimate assumed. The gap is architectural, not
  a pricing error: each page involved multiple tool calls (read the source page,
  check sibling files and the running registry for reuse, write the output,
  validate it) rather than one prompt-completion round trip. Agentic extraction
  costs more per page than a single structured-output call would, in exchange
  for the cross-checking a single call can't do on its own.
- **Human review load came in lighter than assumed.** The 100-page run produced
  8 new `docs-issues/` entries — an 8% flag rate, versus the 20% assumed from the
  original 5-page sample. Combined with the original 8-page batch (4 issues, a
  higher rate on a much smaller sample), the two-round total is 12 issues across
  108 pages (~11%). Still a small sample to generalize from, but directionally
  reassuring: the original human-review estimates were, if anything, pessimistic.

## Revised figures

Applying the observed ~3.4x token multiplier to the cost table (holding the
blended $/token rate constant, since the shift is in *token volume* per page, not
model pricing):

| Scope | Pages | Sonnet 5 (agentic, ~3.4x) | Fable 5 (agentic) | Haiku 4.5 (agentic) |
|---|---|---|---|---|
| POC | 100 | ~$3 | ~$17 | ~$2 |
| `server/current` + `cloud` | 1,500 | ~$51 | ~$255 | ~$26 |
| Latest version only | 3,919 | ~$133 | ~$666 | ~$67 |
| Everything, every version | 12,369 | ~$421 | ~$2,100 | ~$210 |

Applying the observed ~11% flag rate to the human-review-time table (roughly
halving the original figures, at the same few-minutes-per-item rate):

| Scope | Pages | Human review time (~11% flag rate) |
|---|---|---|
| POC | 100 | ~30–60 minutes |
| `server/current` + `cloud` | 1,500 | ~1–2 days, spread out |
| Latest version only | 3,919 | ~3–4 days, spread out |
| Everything, every version | 12,369 | ~1.5–2.5 weeks, spread out |

Machine time, if run with similar (10-way) parallelism rather than strictly
sequentially, would also compress well below the original "sequential, unattended"
figures — roughly in proportion to the concurrency actually used, up to whatever
ceiling API rate limits or budget impose at higher concurrency.

## Bottom line

The practical conclusion is unchanged, and if anything strengthened: **even the
most expensive model, at the most extreme scope, applying the real-world token
multiplier, comes to roughly $2,100 and well under a week of wall-clock time.**
Compute and machine time are not the constraint at any scope considered here. The
one number that matters most for planning purposes is human review time, and the
two real data points collected so far (11 issues logged across 108 pages) suggest
the original estimate for that was conservative rather than optimistic.

**The more consequential finding from actually running this at scale wasn't about
money or time at all** — it's that the extraction *architecture* (a single
structured-output call per page vs. a multi-tool-call agent that can read
context, check for reuse, and self-correct) is a bigger cost driver than the
*model tier* choice: the gap between "Sonnet 5, single call" and "Sonnet 5,
agentic" (~3.4x) is comparable in size to the gap between Sonnet 5 and Fable 5 at
a fixed architecture. Both are worth deciding deliberately; neither should be
assumed.

## What this document does not cover

- The one-time cost of designing the extraction schema, the reconciliation
  method, and the promotion rules — the work already done in `poc/` to get to a
  vocabulary worth running at scale. That effort doesn't repeat per page and
  isn't captured in a per-page rate.
- Any cost associated with acting on `docs-issues/` findings (content fixes,
  SME time beyond the review-time figures above).
- The cost of the JSON-LD drafting step, or of building an actual publishing
  pipeline — both still open per `poc/README.md`.
