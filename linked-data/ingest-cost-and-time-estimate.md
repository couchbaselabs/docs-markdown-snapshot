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

## Bedrock migration — tooling and cost notes (small trial, 2026-08-27)

The host environment running this pipeline moved from direct Anthropic API
access to Amazon Bedrock, for cost management. Before resuming ontology work
at any real scale, a deliberately small (3-page) trial re-ran the same
extract → reconcile pipeline unchanged, specifically to check two things: does
anything in the tool surface break, and how should the cost figures above be
read differently on Bedrock. See `poc/reconciliation.md`'s round 4 section for
the ontology findings from the same trial — this section covers only
tooling/cost.

**Tool availability: no change observed.** Extraction, validation, and
reconciliation ran identically to prior rounds — subagent dispatch, file
read/write, and the reconciliation script all behaved the same as on direct
API access, with no failures or unusual output. Checked against Bedrock's
documented feature-availability table (a third-party reference, not Couchbase
or Anthropic first-party): the things Bedrock genuinely doesn't support
(Anthropic's server-hosted web-search/web-fetch/code-execution tool *types*,
the Message Batches API, the Files API, the Models API, the MCP connector,
Managed Agents) are all things this pipeline never used in the first place —
it runs entirely on the host harness's own tools (subagent dispatch, file
read/write), not on those Anthropic API surfaces. The two things this pipeline
actually depends on — tool use and prompt caching (used implicitly, via the
running term registry carried forward in each extraction prompt) — are both
fully supported on Bedrock. One caveat worth carrying forward if this is ever
re-verified independently: Bedrock's *legacy* integration path (models Opus
4.6 and earlier) rejects automatic top-level cache_control and requires
explicit breakpoints instead — a constraint on how a caller structures cache
control, not a loss of caching itself, and one this harness's current model
tier isn't affected by.

**Token usage from the trial:** 62,167 tokens across the 3-page batch (one
subagent, sequential-with-registry-reuse-checking) — about 20,700 tokens/page,
noticeably above round 2's ~11,700 tokens/page benchmark. Plausibly a content-
density effect (this batch introduced four new structural concepts with
detailed disambiguation notes, versus round 2's largely single-statement CRUD
pages) rather than a Bedrock effect — a 3-page sample can't separate the two,
and doing so would need a same-content before/after comparison this trial
didn't attempt. Wall-clock: about 10 minutes for the 3-page batch, one agent,
no parallelism attempted at this scale (consistent with round 2/3's finding
that wall-clock scales with concurrency actually used, not page count alone).

**Pricing: confirmed at parity with first-party, for this model.** An initial
automated pricing-page lookup during this trial surfaced rates for Claude 3.5
Sonnet / 3.5 Sonnet v2 (listed under "Public Extended Access") rather than the
current-generation model this pipeline runs — a lookup miss, not a gap in
Bedrock's pricing page. A direct read of the actual page's Claude Sonnet 5 row
(confirmed by a human, 2026-08-27) gives:

| | Input | Output | Batch input | Batch output | Cache write (5m) | Cache write (1h) | Cache read |
|---|---|---|---|---|---|---|---|
| Bedrock, Claude Sonnet 5 | $2.00 /1M | $10.00 /1M | N/A | N/A | $2.50 /1M | $4.00 /1M | $0.20 /1M |

Base input/output pricing is **identical to the first-party intro rate**
already used throughout this document's tables ($2/$10 per 1M) — so every
dollar figure above already applies to Bedrock for this model, no rework
needed. Cache pricing follows the standard Anthropic ratios (write ≈1.25x base
for a 5-minute cache, ≈2x for a 1-hour cache; read ≈0.1x base) rather than
some Bedrock-specific markup — good news given this pipeline's
registry-carry-forward design is exactly the repeated-prefix workload prompt
caching is built for. One thing to watch, not yet resolved: the first-party
$2/$10 rate is explicitly an *introductory* rate "through 2026-08-31" (four
days from this trial) — whether Bedrock's matching rate rises in step after
that date, or is a separate, standing Bedrock rate that happens to currently
equal it, isn't known from this lookup; worth rechecking after that date
rather than assuming it stays at $2/$10 indefinitely.

**Batch inference not yet available for this model.** Both batch columns read
N/A for Claude Sonnet 5 specifically, even though Bedrock's native
batch-inference discount (~50% off on-demand) exists for other models on the
platform, as a mechanism separate from Anthropic's Message Batches API (which
isn't available on Bedrock at all, for any model). Moot for the cost figures
in this document either way — they were always derived from live agentic
token usage, never from a batch call — but worth knowing before treating batch
inference as an available cost lever for a future large-scale run on this
model.

**Bottom line for this section:** the architecture holds up unchanged on
Bedrock, and the migration introduces no cost surprise for Sonnet 5 — pricing
matches the first-party rate this document was already built on. The one open
question is durability of that rate past 2026-08-31, not whether Bedrock costs
more today.

## First real-scale wave on Bedrock (round 5, 115 pages, 2026-08-27)

The wave-chunked plan's first real (non-trial) wave: completing `cloud/n1ql/`
(115 pages, 10 parallel batches of ~12 pages each) rather than the 3-page
round 4 trial. Real numbers, for comparison against the wave-sizing estimates
above:

- **Token usage: ~1.5M tokens for 115 pages (~13,000 tokens/page)** — close to
  round 2's original ~11,700 tokens/page benchmark, not round 4's ~20,700.
  Round 4's higher rate now reads like a content-density artifact of that
  specific 3-page batch (dense, novel transaction concepts), not a Bedrock
  effect or a new baseline — this wave's 115-page sample is far more reliable
  evidence either way.
- **Cost: roughly $4-5**, using the same blended-rate method as the rest of
  this document — under the ~$4-7/wave estimate from the wave-sizing plan, and
  under the $7 approved for this run.
- **Wall-clock: all 10 batches completed within the same working session**,
  comfortably inside the "single sitting" framing from the wave-sizing plan;
  exact per-batch timing wasn't tracked precisely enough to refine the
  earlier 45-minute-to-2-hour estimate, but nothing suggests it needs revising
  up or down.
- **No batch hit a session/usage-limit interruption** this time (round 2's
  100-page run had one). Good news, but n=1 at this scale under Bedrock —
  not yet enough to conclude interruptions are rarer here than on direct API
  access.

Net effect on the wave-sizing plan: no changes needed. Cost and architecture
both held at the scale actually tried; the main new information is
qualitative (see `poc/reconciliation.md` round 5) rather than a correction to
any number in this document.

## Second wave the same day (round 6, 89 pages, 2026-08-27)

Run back-to-back with round 5 in the same working session, closing out the
rest of `cloud/`'s smaller directories. ~1.05M tokens for 89 pages (~11,800
tokens/page - matching round 2's original benchmark again, not round 4's
outlier), roughly $3. Both real-scale waves this session landed close to
round 2's per-page rate, which is now the more reliable number to plan
against than round 4's single dense 3-page sample. No tool or session-limit
issues in either wave. Confirms two wave-sized rounds comfortably fit in one
"couple of hours" working session, at least at this concurrency (8-10 batches)
and this page-count (89-115) - useful data for pacing the remaining
~3,900-page corpus if this moves past POC.

## Third wave the same day (round 7, 53 pages, 2026-08-27)

Also fit comfortably in the same session (6 parallel batches, `cloud/clusters/`).
~714,000 tokens for 53 pages (~13,500 tokens/page - a touch above rounds 5/6
but still the same order of magnitude, consistent with a denser wave rather
than a cost regression), roughly $2. Three real-scale waves, ~257 pages,
~$8 total, one working session, no infrastructure issues across any of them.
The pattern holding across all three: page-count and wave count are not the
bottleneck at this scale - reconciliation effort (working through what each
wave's richer findings imply for the registry) took noticeably longer,
proportionally, for round 7 than for round 6 despite round 7 covering fewer
pages, because of how much this wave's findings touched already-promoted
concepts rather than only adding new ones. Worth factoring into pacing
estimates: a wave's reconciliation cost tracks how much it *revises* the
existing registry, not just how many new pages it reads.

## Fourth wave the same day (round 8, 67 pages, 2026-08-27)

`cloud/eventing/` - genuinely new territory (no prior round had touched it),
run as 7 batches (3 conceptual, 4 covering ~40 thin JS-handler code samples).
~735,000 tokens for 67 pages (~11,000 tokens/page, right in this session's
usual range), roughly $2. Four real-scale waves today, ~324 pages, ~$10
total, still one working session, still zero infrastructure issues. Despite
being a "new feature, no new structure" round - the kind that might be
expected to reconcile quickly, since less registry surgery was needed than
rounds 6/7 - reconciliation still took real effort, because a brand-new
namespace (`eventing:`) with ~20+ minted concepts still needs the same
per-concept scrutiny (duplicate-mint consolidation across the 7 concurrent
batches, deciding what clears the promotion bar) as a round that revises
existing concepts. Refines the round-7 note: reconciliation cost tracks
registry *surface area touched*, whether that's revision or fresh territory,
not just page count or "was there a headline surprise."

## What this document does not cover

- The one-time cost of designing the extraction schema, the reconciliation
  method, and the promotion rules — the work already done in `poc/` to get to a
  vocabulary worth running at scale. That effort doesn't repeat per page and
  isn't captured in a per-page rate.
- Any cost associated with acting on `docs-issues/` findings (content fixes,
  SME time beyond the review-time figures above).
- The cost of the JSON-LD drafting step, or of building an actual publishing
  pipeline — both still open per `poc/README.md`.
