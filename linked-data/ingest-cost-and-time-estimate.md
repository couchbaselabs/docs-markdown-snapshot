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

## Fifth wave the same day (round 9, 33 pages, 2026-08-27) - cloud/ complete

`cloud/guides/` - the last untouched `cloud/` territory, run as 3 batches.
~437,000 tokens for 33 pages (~13,200 tokens/page), roughly $1.30. Five
real-scale waves today, ~357 pages, ~$11 total, one working session, zero
infrastructure issues across all five. This was the one wave expected to
mostly confirm rather than surprise (guide pages wrapping already-documented
statements) - reconciliation effort was correspondingly lighter than rounds
6-8, consistent with the round-7/8 refinement that reconciliation cost tracks
registry surface area touched, not just page count: fewer genuinely new
concepts (4) meant less consolidation work, even though the extraction
batches themselves ran at the usual per-page token rate.

**`cloud/` is now fully covered** - 5 rounds (5 through 9), ~460 pages,
starting from round 2's original 50-page sample. Useful as a real data point
for scale planning: a top-level product directory of this size took 5
distinct waves across roughly one working day once the pipeline was running
at real scale, not the single pass an initial estimate might assume - later
waves kept surfacing genuine new material even in directories a `reconciliation.md`-adjacent
"how much is left" estimate might have called low-yield.

## Scoping `server/` — the next product tree (counted 2026-09-01)

With `cloud/` complete, `server/` is the next and largest product tree. Counting
it properly turned up a correction and a planning technique worth recording.

**Correction: existing `server/` coverage is on a superseded tree.** All 58
`server/` extraction records from rounds 1-2 have `source_version: 7.2` and
`source_path: server/7.2/...`. Those early rounds sampled the 7.2 tree, not
`current`. So `server/current` (1,033 pages, `release/8.0`) began at **zero
coverage**, not 58 pages. 42 of the 58 covered paths do also exist under
`current`, but with different content. Beyond the arithmetic, this matters for
the vocabulary: the project's only server-side terms so far were derived from a
tree two releases behind, which is precisely the setup the "vocabulary from
where a feature is *mentioned* is less reliable than from the feature's own
authoritative page" limit warns about (see `poc/reconciliation.md`). Expect
round 1-2 server concepts to need revision, not just extension, as `current`
gets read.

**`server/current`: 1,033 pages, ~13 waves, ~$32.** At the 71-pages-per-wave
average actually sustained across rounds 5-9 (range 33-115), and the observed
~$0.031/page. Directory-aligned, that's roughly: `n1ql/` 151 (2 waves),
`rest-api/` plus 19 singleton `*-rest-*` dirs 183 (2), `cli/`+`tools/` 138 (2),
`search/`+`fts/`+`vector-search/`+`vector-index/` 115 (1), `learn/` 95 (1),
`manage/` 83 (1), `analytics/`+`backup-restore/`+`metrics-reference/`+
`xdcr-reference/`+misc 87 (1), `eventing/` 66 (1), `install/`+
`getting-started/`+`introduction/`+`tutorials/` 64 (1), `guides/`+`indexes/`+
`javascript-udfs/`+misc 51 (1). Wall-clock at rounds 5-9's demonstrated pace
(5 waves in one working session) is ~3 sessions of extraction, but 4-5 is the
number to plan against: `cloud/` was largely one product's surface, whereas
`server/current` spans `rest-api`, `cli`, server-side `eventing`, `analytics`
and `xdcr` — far more genuinely-new registry surface per wave, and
reconciliation cost tracks registry surface area touched, not page count.

**Diff-gating: a cheap way to order waves by expected yield.** 317 of
`server/current`'s 1,033 pages share a path with an already-extracted `cloud/`
page. Comparing those pairs line-by-line (`difflib`, counting changed lines)
splits them sharply: 109 differ by ≤5 lines — product-name and version-string
churn, near-zero extraction yield — while 117 differ by 6-25 lines (typically
the privilege/prerequisite section, where Capella's Basic/Advanced credential
model diverges from server RBAC) and 91 differ by more than 25. The remaining
716 pages have no `cloud/` counterpart at all. Diff-gated effective workload is
therefore ~924 substantive pages plus a cheap confirm sweep of the 109 trivial
ones — only ~11% off the raw count, so **the ~13-wave estimate stands**. The
real value isn't the saving: it's that waves can be *ordered* highest-yield
first, and that the diffs themselves are the version- and edition-gating
evidence the ontology most lacks. Cost of running the gate is negligible (a
local file comparison, no model calls).

**Retrospective after wave 1 (round 10): the ordering works, the magnitude
misleads.** Selecting the 38 wave-1 pages by diff size did put genuinely
divergent content first — the gate did its job. But **raw changed-line counts
systematically overstate extraction yield**, because re-rendered example blocks
dominate the diff: an identical statement whose sample query output was
regenerated can show 30+ changed lines and contain not one new fact, while a
6-line diff confined to a Prerequisites section can be the most load-bearing
page in the wave. Two corrections for the remaining ~12 waves:

1. Treat the changed-line count as a *sort key only*, never as a yield
   estimate. Do not budget wave cost from it.
2. Prefer diffing with example/output blocks stripped (fenced code, `----`
   listing blocks) before counting. The signal lives in prose, tables and
   admonitions; the noise lives in the samples.

This also means the 109/117/91 buckets above are softer than they look: the
"≥25 lines" bucket is not reliably the highest-yield one. The ~13-wave estimate
is unaffected — it was never derived from the bucket sizes.

**The older version trees are much cheaper than a naive 3x.** Same technique
applied across trees: of 7.6's 953 paths shared with `current`, **581 differ by
≤5 lines**, leaving 372 substantive plus 20 pages existing only in 7.6 — about
392 pages, ~6 waves. For 7.2: 492 substantive plus 153 pages existing only in
7.2, about 645 pages, ~9 waves. All three server trees therefore come to ~28
waves and ~$60 diff-gated, versus ~42 waves naively.

**Version-gate attrition is real but mostly deliberate — so recommend one
previous version, not the full history.** Measured across the corpus:
`server/current` contains 165 "version X and later" gate statements, spread over
only 129 of its 1,033 pages. Ingesting 7.2 would recover 23 gate statements that
`current` has lost (skewed old: 6.5 ×6, 7.0 ×4, 5.5); 7.6 would recover 20
(7.6.2 ×8). Conversely `current` carries 82 gates that 7.2 never had. The
clearest single case is `n1ql/n1ql-language-reference/createindex.md`, whose
gates by tree are 7.2 → {6.5, 7.0}, 7.6 → {7.6}, 8.0 → {7.6, 8.0}: no single
tree holds the full history.

The tempting conclusion — ingest everything, since only the union is complete —
is wrong, and the reason is editorial rather than technical. Per the docs team:
as support for a version is dropped, the team stops documenting it, and
retroactively updating superseded trees has often not been resourced, so changes
land only on the latest version. The attrition is therefore **intentional
pruning of facts about out-of-support versions**, not accidental data loss. That
reframes the value of each tree: it tracks whether the version is *still
supported*, not how old the tree is. The 23 gates recoverable from 7.2 describe
versions largely out of support (5.5, 6.5, 7.0) and are close to worthless for
answering a live support question; 7.6's 20 recovered gates describe a version
still in support and are worth having.

**Recommendation: ingest `server/current` plus one previous version (7.6), and
skip 7.2** unless a specific question demands it. That is ~19 waves and ~$40,
against ~28 waves for all three. Revisit only if a concrete use case needs
deep history — the 153 pages that exist only in 7.2 remain the richest seam for
"what was removed", but removal of an out-of-support feature is rarely the
question anyone actually asks.

## The real running total (rounds 1-24): extraction was never the cost driver

This document tracked real per-round cost meticulously through round 9 (~$11
total across ~357 `cloud/` pages) and then stopped — rounds 10-24 read a
further ~488 pages (`server/` waves 1 through the REST reference layer,
`poc/reconciliation.md` rounds 10-24) with no matching entry here. That gap
is itself the first finding: **this document's cost model only ever measured
extraction**, and extraction is not what the real bill turned out to be
dominated by.

**Checked against the two cleanest rounds available (22 and 23, both
stall-free, both cleanly logged): extraction cost held at the established
rate, not blown out.** Round 22 (`search/`, 54 pages): 760,152 tokens total,
~14,077 tokens/page. Round 23 (`fts/`, 45 pages): 671,673 tokens,
~14,926 tokens/page. Both sit close to — slightly above, not multiples above
— the ~11,000-13,500 tokens/page range rounds 5-9 established as the agentic
extraction baseline. Extrapolating that same rate across the ~488 pages read
in rounds 10-24, at this document's own blended-rate method (~$0.03-0.04 per
page, per rounds 5-9's own real figures), extraction across that whole
stretch comes to roughly **$15-25** — even generously doubled for retry/stall
overhead (rounds 21 and 24 both lost batches to stalls and needed relaunches),
call it **$30-50**. Nowhere near the reported $300+.

**So the $300+ real spend is coming from something this document's model
never counted at all: the coordinator session itself, not the extraction
batches it dispatches.** Two components, neither driven by page count:

- **Reconciliation-phase token usage, scaling with round count and running
  session length, not pages read.** Every round after extraction returns, one
  continuous coordinator session reads every batch's report, runs analysis
  scripts, writes dozens of promoted concept/relation records with
  evidence-backed notes, and writes a 100-200+ line `reconciliation.md`
  section plus a matching `README.md` update — every round, inside one
  session whose own conversation history keeps growing. Prompt caching offsets
  some of this, but the *reasoning* work (reading extraction files, deciding
  what crosses the promotion bar, drafting the write-up) is genuinely
  proportional to round count and accumulated context, not to how many pages
  that round happened to read. A round that reads 18 pages (round 24) but pays
  down a 43-item cross-corpus backlog and writes docs-issues can cost more in
  coordinator tokens than a round that reads 3x as many pages and finds little
  to reconcile.
- **Retry/stall overhead, which burns tokens for zero yield and is invisible
  in any "tokens per page extracted" metric.** Round 21 lost two batches to
  stalls, each needing a second attempt. Round 24 lost all five original
  batches to a simultaneous infrastructure stall and needed full relaunches.
  Every stalled attempt consumes tokens before failing; none of it shows up in
  a metric measured only on the batches that eventually succeeded.

**The practical framing for a business case: this $300+ figure describes how
this POC was actually run — one long, exploratory, ever-growing coordinator
session across 24 rounds — not a property of the extraction+reconciliation
architecture at production scale.** A production run would not keep one
continuous session accumulating context across dozens of rounds; it would
scope reconciliation to a bounded unit of work (per wave, per product tree)
and start each one fresh, the same way extraction already runs as isolated,
stateless subagent batches rather than one long-running process. The
$0.03-0.04/page extraction figure this document has tracked since round 5
still holds and is still the right number for *that* line item — it just was
never the whole bill, because this POC's reconciliation work was never priced
as its own line item at all.

**Also worth stating plainly, since it changes how the $133 "latest version
only" projection should be read**: that figure prices 3,919 pages. This
project has read 845 — about 22% of that scope — and reportedly already spent
more than twice $133 getting there, almost entirely outside the thing the
$133 figure prices. Comparing the two numbers directly, without this
context, understates the real cost of running a project this way by a wide
margin; comparing extraction-to-extraction, the two numbers are actually
consistent.

**Recommendation for future cost tracking: split "extraction cost" and
"coordination/reconciliation cost" into two separate line items, and re-scope
reconciliation sessions before pricing a production run.** Extraction is
page-count-driven, small, and already well-modeled above. Reconciliation, as
actually run in this POC, is round-count-and-session-length-driven and has
never been priced at all — the single biggest open number in this whole
document. If a future business case needs a defensible reconciliation-cost
figure, the right next step is either (a) instrumenting per-round coordinator
token usage going forward so it can be measured directly, the way extraction
already is, or (b) re-running one wave's reconciliation in a fresh, bounded
session and pricing that in isolation, rather than continuing to infer it
from the difference between a running total and an extraction-only estimate.

## What this document does not cover

- The one-time cost of designing the extraction schema, the reconciliation
  method, and the promotion rules — the work already done in `poc/` to get to a
  vocabulary worth running at scale. That effort doesn't repeat per page and
  isn't captured in a per-page rate.
- Any cost associated with acting on `docs-issues/` findings (content fixes,
  SME time beyond the review-time figures above).
- The cost of the JSON-LD drafting step, or of building an actual publishing
  pipeline — both still open per `poc/README.md`.
- **A priced figure for coordinator/reconciliation session cost.** The section
  above names this as the dominant real cost observed so far and explains why
  it isn't in any table in this document, but it stops at a rough bound
  (~$250-280 of the reported $300+ Sonnet spend, by elimination), not a
  measured number. Treat every dollar figure elsewhere in this document as an
  extraction-only estimate until that gap is closed.
