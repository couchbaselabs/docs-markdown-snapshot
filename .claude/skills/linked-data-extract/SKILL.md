---
name: linked-data-extract
description: Dispatch parallel subagents to extract candidate ontology concepts/relations from a new batch of Couchbase docs pages into linked-data/poc/extractions/. Use when extending or stress-testing the linked-data POC with a new set of pages (a new product, component, or scale round). Phase 1 of 2 - see the linked-data-reconcile skill for phase 2.
---

# Linked-data extraction batch

Phase 1 of the linked-data POC pipeline (extraction → reconciliation - see the
`linked-data-reconcile` skill for phase 2). Produces one pass-1 JSON record per
source page under `linked-data/poc/extractions/`, using parallel subagents. This
process has been run three times (8 pages by hand, 100 pages across `server/`+
`cloud/`, 37 pages across Couchbase Lite/Sync Gateway/Java SDK) - see
`linked-data/poc/reconciliation.md` for what each round found, and
`linked-data/README.md` / `linked-data/poc/README.md` for the current state of
the ontology this process has produced.

## 1. Decide scope

- How many pages, from which product/component/directory tree.
- What is this round testing? Every round so far has had a specific hypothesis
  worth stating up front (e.g. "does the vocabulary survive a different
  deployment model of the same product", "does it survive a genuinely different
  product family", "build density in an already-covered area"). Write the
  hypothesis down - it becomes the framing paragraph in every agent's prompt and
  shapes which pages you pick.
- Deliberately load some of the selection toward areas likely to break current
  assumptions, not just areas likely to confirm them. A round that only
  confirms the vocabulary teaches you less than one that stresses it - the most
  valuable rounds so far were the ones deliberately aimed at a product's own
  security/access-control surface, since that's where every structural
  difference between products has shown up.
- Batch size: ~10-15 pages per agent keeps prompts and output manageable. Group
  pages by theme (same component, same statement family) so one agent's report
  is coherent, not scattered across unrelated topics.

## 2. Build the current registry fresh - do not reuse a memorized or previously-written table

Before drafting any agent prompt, regenerate the registry from the actual
current state of the repo - it only grows, and a stale table causes agents to
re-mint things that are already promoted (this has happened: `requiresMinVersionFor`
was independently re-minted by a later round after being consolidated into
`availableSince` in an earlier one, precisely because the later round's agents
were only given the promoted predicate *names*, not the full design history).

```bash
find linked-data/poc/concepts -name '*.json' -print -exec cat {} \;
find linked-data/poc/relations -name '*.json' -print -exec cat {} \;
```

From that output, build two short tables for the agent prompts:

- **Concepts**: shorthand and real IRI, label, one-line meaning, and any note
  about what it must NOT be confused with or reused for (the registry has
  accumulated same-word-different-thing collisions - e.g. three unrelated
  things are all called "role" across different products - carry those
  warnings forward into new prompts).
- **Relations**: name, one-line shape ("subject = X; object = Y; means Z"), and
  domain/range notes.

## 3. The extraction schema (give this to every agent, verbatim)

```json
{
  "page_id": "<product>/<path-without-extension>",
  "source_version": "<version string, or the product's own name if version-less>",
  "source_path": "<the real source path you read>",
  "concepts": [
    { "candidate_id": "<namespace>:<kebab-case>", "label": "...", "reused_or_minted": "reused | minted - reason" }
  ],
  "relations": [
    { "subject": "...", "predicate": "...", "object": "...", "reused_or_minted_predicate": "...", "evidence": "<direct quote from the page - required, every time>" }
  ],
  "notable_absence": { "predicate": "...", "finding": "..." },
  "cross_component_finding": "...",
  "cross_product_finding": "..."
}
```

Rules to state explicitly in every prompt:

- Every relation needs a direct-quote `evidence` field. No inference without
  textual evidence.
- Structural Markdown links (`[text](file.md)`) become `"predicate": "seeAlso"`
  - a reused standard term (`rdfs:seeAlso`), never minted.
- Thin/reference pages can have empty `concepts`/`relations` arrays - don't force
  content that isn't there.
- Reuse a concept id from the registry when the underlying thing is genuinely
  the same (e.g. the same SQL++ statement documented on two products) - note the
  cross-reuse in `reused_or_minted`. Don't force a reuse that isn't really there;
  when in doubt, mint and flag the judgment call in a finding field. Agents have
  correctly *rejected* a coordinator's suggested reuse after checking the actual
  page content - that's the desired behavior, not something to discourage.
- Mint a new predicate/concept whenever nothing in the registry fits - this is
  expected and desired, not a failure. Name predicates as camelCase verb
  phrases (`grantsChannelAccess`), concepts as `namespace:kebab-case`
  (`sgw:channel`).
- `notable_absence` / `cross_component_finding` / `cross_product_finding` are
  for things noticed that aren't ontology relations at all (missing docs,
  content duplication, unadapted copy, internal contradictions, empty stub
  pages). Use them liberally - they cost nothing and the reconciliation phase
  decides what to do with them.
- Extraction only. Agents must not write to `concepts/`, `relations/`, or
  `docs-issues/` - only to `extractions/`.
- Output path: mirror the source path under `linked-data/poc/extractions/`,
  dropping any version segment the source path has (e.g. `server/7.2/...` →
  `extractions/server/...`; `couchbase-lite/current/...` →
  `extractions/couchbase-lite/...`).
- Tell every agent explicitly: don't try to reconcile against other batches,
  don't guess what a sibling agent running concurrently might be doing. A
  coordinator reconciles afterward. Duplicate/near-duplicate mintings across
  concurrently-running agents are expected and are the reconciliation phase's
  job to catch, not something to prevent at extraction time.

## 4. Write one self-contained prompt per batch

Each agent starts with zero context - it does not see this conversation or any
other agent's work. Every prompt needs, from scratch:

1. One paragraph of background: what this POC is, what `linked-data/poc/`
   contains, and what phase this is (extraction only).
2. The round's specific framing/hypothesis (from step 1) - what's already known
   from prior rounds, what this batch is testing, what to watch for.
3. The current registry tables (from step 2).
4. The schema and rules (from step 3), with 1-2 worked examples using real
   registry terms so the shape is unambiguous.
5. The concept-id and predicate-naming conventions for this batch's namespace.
6. The literal list of source file paths → output file paths for this batch.
7. A request for a short (~300 word) end-of-run report: files written, what got
   minted and why, and every finding field in full (don't let the agent
   compress or summarize these - they're the reconciliation phase's raw
   material).

## 5. Dispatch in parallel

Use the Agent tool, `subagent_type: "general-purpose"`, one call per batch, all
in a single message so they run concurrently. Don't use `fork` (these need zero
conversation context, a fresh agent is correct) and don't reach for the Workflow
tool for this unless the user has explicitly opted into multi-agent
orchestration - a handful of parallel Agent calls has been sufficient at every
scale tried so far (up to 10 concurrent batches) and doesn't need that scale of
tooling.

## 6. Handle failures

A batch can fail partway (e.g. a session/usage limit - this happened once, on a
10-page batch that got 3 pages done before failing). Before retrying:

- Check what that batch's output directory actually contains - don't assume
  zero progress.
- Validate whatever exists (`python3 -c "import json; json.load(open(f))"` over
  each file) before trusting it.
- Relaunch a new agent covering only the remaining pages, with the same
  registry and schema instructions - not a resend of the whole original batch.

## 7. Validate before moving to reconciliation

Once every batch reports back, validate the whole new set parses as JSON before
touching anything else:

```bash
for f in $(find linked-data/poc/extractions/<new-paths> -name "*.json"); do
  python3 -c "import json; json.load(open('$f'))" || echo "INVALID: $f"
done
```

Then hand off to the `linked-data-reconcile` skill.
