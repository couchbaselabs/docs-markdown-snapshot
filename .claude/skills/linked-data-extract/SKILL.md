---
name: linked-data-extract
description: Dispatch parallel subagents to extract candidate ontology concepts/relations from a new batch of Couchbase docs pages into linked-data/poc/extractions/. Use when extending or stress-testing the linked-data POC with a new set of pages (a new product, component, or scale round). Phase 1 of 2 - see the linked-data-reconcile skill for phase 2.
---

# Linked-data extraction batch

Phase 1 of the linked-data POC pipeline (extraction → reconciliation - see the
`linked-data-reconcile` skill for phase 2). Produces one pass-1 JSON record per
source page under `linked-data/poc/extractions/`, using parallel subagents.
See `linked-data/poc/reconciliation.md` for what past rounds found, and
`linked-data/README.md` / `linked-data/poc/README.md` for the current state of
the ontology this process has produced.

## 1. Decide scope

- How many pages, from which product/component/directory tree.
- State the round's hypothesis up front (e.g. "does the vocabulary survive a
  different deployment model of the same product", "does it survive a
  genuinely different product family", "build density in an already-covered
  area"). It becomes the framing paragraph in every agent's prompt and shapes
  which pages you pick.
- Deliberately load some of the selection toward areas likely to break current
  assumptions, not just areas likely to confirm them. A product's own
  security/access-control surface has been the most reliable source of
  structural findings so far.
- Batch size: ~10-15 pages per agent keeps prompts and output manageable for
  reference/procedure-heavy scope. Group pages by theme (same component, same
  statement family) so one agent's report is coherent, not scattered.
- **Size down to 5-8 pages per agent for judgment-call-heavy content**
  (access-control/security-surface, dense cross-page evidence citations,
  content likely to trigger evidence-gate retries). Measured per-batch usage
  data (see `linked-data/ingest-cost-and-time-estimate.md`) shows `cache_read`
  tokens scale roughly with the *square* of an agent's tool-call count, because
  every tool-use turn re-reads that agent's entire accumulated conversation -
  so cost tracks content complexity (how many tool calls the work needs), not
  raw page count. Splitting a mechanical batch further mostly just re-pays the
  fixed per-agent startup cost (registry excerpt + schema + rules, repeated in
  full in every prompt) without shrinking much real work.

## 2. Build the current registry fresh - do not reuse a memorized or previously-written table

Before drafting any agent prompt, regenerate the registry from the actual
current state of the repo - it only grows, and a stale table causes agents to
re-mint things that are already promoted under a different name.

```bash
python3 linked-data/poc/registry-digest.py
```

This prints every promoted concept and relation, generated fresh from disk
each time, so it can't be stale the way a hand-maintained table would be.
It's also large (~46K tokens in full) and only growing, and unlike
`reconciliation.md`/`README.md` there's no anchor to grep for, since a
near-duplicate concept could be anywhere in it. When a batch has a clear
namespace focus (most do), scope the concepts section to those namespaces
before pasting it into an agent prompt (keep the full relations/predicates
section regardless - predicates are reused across domains, not
namespace-scoped, so there's no safe way to trim that list):

```bash
python3 linked-data/poc/registry-digest.py > /tmp/digest.txt
grep -E '^`(namespace1|namespace2|...):' /tmp/digest.txt   # scoped concepts excerpt
```

Tell agents explicitly that a scoped excerpt may be partial and that they can
run `registry-digest.py`/`candidate-evidence.py` themselves for anything
outside it - don't silently hand them a partial table as if it were exhaustive.

From the (possibly scoped) concepts section and the full relations section,
build two short tables for the agent prompts, or point agents at the commands
above and let them run their own:

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
  "page_id": "<product>/<release, if the product has releases>/<path-without-extension>",
  "source_version": "<version string, or the product's own name if version-less>",
  "source_path": "<the real source path you read, exactly as it is on disk>",
  "concepts": [
    { "candidate_id": "<namespace>:<kebab-case>", "label": "...",
      "registry_status": "promoted | extraction-layer | minted",
      "reused_or_minted": "reused | minted - reason" }
  ],
  "relations": [
    { "subject": "...", "predicate": "...", "object": "...",
      "registry_status": "promoted | extraction-layer | minted",
      "reused_or_minted_predicate": "...",
      "evidence": "<direct quote from the page - required, every time>" }
  ],
  "notable_absence": { "predicate": "...", "finding": "..." },
  "cross_component_finding": "...",
  "cross_product_finding": "..."
}
```

A relation may additionally carry two optional fields, for the case where a
fact is true and load-bearing but genuinely not stated on the page being
extracted:

```json
{ "subject": "...", "predicate": "availableSince", "object": "version:server-8-0",
  "evidence": "<direct quote from the OTHER page>",
  "evidence_source": "server/current/introduction/whats-new.md",
  "evidence_provenance": "cross-page: query-awr.md states no version; whats-new.md dates the feature" }
```

Use them rather than dropping the relation, and rather than attributing an
off-page quote to the page. Cross-page evidence is legitimate; silent
misattribution is not.

`registry_status` is an **enum, mechanically checked**, and it is separate from
the `reused_or_minted` prose on purpose. Exactly one of three exact strings, for
every concept and every relation:

- `promoted` - a file for this id exists in `linked-data/poc/concepts/` or
  `relations/`. Being promoted under a *different* name counts: aliases are
  resolved, so `server:dcp-protocol` is `promoted` because
  `concepts/protocol/dcp.json` lists it.
- `extraction-layer` - reused from an earlier extraction record, never promoted
  to the registry. **This is a normal, expected answer, not a confession.** The
  two-layer design means most reused ids are here; `sdk:durability` has been
  legitimately reused across rounds without ever being promoted.
- `minted` - new in this record. Also expected. But do not declare `minted` for
  something the registry already has under a different name (e.g. a
  consolidated predicate) - the gate now refuses that.

If unsure which applies, run `python3 linked-data/poc/registry-digest.py` - it
prints what is promoted *right now*, so it cannot be stale. Keep the prose note
as well: it says things an enum cannot ("reused - same statement as the Capella
page, different privilege model"), and reconciliation reads it. The gate reads
only the enum.

Records written before the gate existed have no `registry_status`. Nothing
rewrites them, and anything aggregating the corpus must treat a missing field
as *unknown* - never as `extraction-layer`. A gap that reads as data is the
same failure shape as an omitted relation.

Rules to state explicitly in every prompt:

- Every concept and relation needs a `registry_status`. It is checked at write
  time, including against aliases, and a wrong declaration blocks the write.
- Every relation needs a direct-quote `evidence` field. No inference without
  textual evidence. **This is mechanically enforced at write time** - see
  "The evidence gate" below. An agent that cannot find a real quote must either
  use `evidence_source`/`evidence_provenance` or omit the relation; it must not
  paraphrase, reconstruct from memory, or write a sentence that "should" be
  there.
- Structural Markdown links (`[text](file.md)`) become `"predicate": "seeAlso"`
  - a reused standard term (`rdfs:seeAlso`), never minted.
- Thin/reference pages can have empty `concepts`/`relations` arrays - don't force
  content that isn't there.
- Reuse a concept id from the registry when the underlying thing is genuinely
  the same (e.g. the same SQL++ statement documented on two products) - note the
  cross-reuse in `reused_or_minted`. Don't force a reuse that isn't really there;
  when in doubt, mint and flag the judgment call in a finding field. An agent
  correctly *rejecting* a coordinator's suggested reuse after checking the
  actual page content is the desired behavior, not something to discourage.
- Mint a new predicate/concept whenever nothing in the registry fits - this is
  expected and desired, not a failure. Name predicates as camelCase verb
  phrases (`grantsChannelAccess`), concepts as `namespace:kebab-case`
  (`sgw:channel`). Mint from the name the page actually gives you - if a page
  shows a Server RBAC role only as "Manage Global Functions", `role:manage-global-functions`
  is the correct thing to write, and reconciliation will re-file it under the
  internal name (`role:query-manage-global-functions`) with yours recorded as an
  alias. Don't go and look the internal name up; the two-layer design exists so
  that this kind of normalisation is the coordinator's cost, paid once, rather
  than every agent's.
- `notable_absence` / `cross_component_finding` / `cross_product_finding` are
  for things noticed that aren't ontology relations at all (missing docs,
  content duplication, unadapted copy, internal contradictions, empty stub
  pages). Use them liberally - they cost nothing and the reconciliation phase
  decides what to do with them.
- Extraction only. Agents must not write to `concepts/`, `relations/`, or
  `docs-issues/` - only to `extractions/`.
- Output path: mirror the source path under `linked-data/poc/extractions/`,
  **keeping the version segment and resolving any alias in it to a real release
  number**:

  | source path | output path |
  |---|---|
  | `server/7.2/n1ql/...` | `extractions/server/7.2/n1ql/...` |
  | `server/current/n1ql/...` | `extractions/server/8.0/n1ql/...` |
  | `couchbase-lite/current/...` | `extractions/couchbase-lite/<release>/...` |
  | `cloud/n1ql/...` | `extractions/cloud/n1ql/...` (Capella has no versions) |

  Two rules matter here:

  1. **Keep the version segment.** A version-neutral output path collides by
     construction: `server/7.2/.../createindex.md` and
     `server/8.0/.../createindex.md` would map to the same output file, and a
     later multi-version ingest would silently overwrite an earlier record.
  2. **Never write `current` into a path or a `page_id`.** `current` is a
     pointer, not a version - it denotes whichever release is newest at the
     moment of reading, so an id containing it silently starts denoting a
     different page on the next major release. Resolve it (check the page's own
     `source_version`, or `introduction/whats-new.md`) and use the number.

  `source_path` is the exception to rule 2: it is a **filesystem** path and must
  keep pointing at the file that actually exists on disk, alias and all. So a
  correct record has `"page_id": "server/8.0/n1ql/.../transactions"` alongside
  `"source_path": "server/current/n1ql/.../transactions.md"`. Those two
  disagreeing is right, not a mistake - one is an identifier, the other is a
  location.
- Tell every agent explicitly: don't try to reconcile against other batches,
  don't guess what a sibling agent running concurrently might be doing. A
  coordinator reconciles afterward. Duplicate/near-duplicate mintings across
  concurrently-running agents are expected and are the reconciliation phase's
  job to catch, not something to prevent at extraction time.

## 3a. The evidence gate (already active - just tell agents about it)

`.claude/settings.json` registers a `PreToolUse` hook,
`linked-data/poc/hooks/gate-evidence.py`, on `Write|Edit|MultiEdit`. For any file
under `linked-data/poc/extractions/` it parses the record and **refuses the
write** unless every relation's `evidence` is verbatim on the page it cites (or
on its `evidence_source`). It also checks every `registry_status` declaration
against the registry, aliases resolved: claiming `promoted` for something with no
file, claiming `minted` for something already promoted, or claiming
`extraction-layer` for something that is promoted are all refused, as is a
missing or misspelled value. Nothing needs enabling; it fires for subagents as
well as the main session - a fabricated record from one of several parallel
subagents is otherwise invisible, since nobody reads a subagent's reasoning.

Every verdict, allows included, is appended to
`linked-data/poc/hooks/gate-log.jsonl` (gitignored). Read it during
reconciliation rather than relying on what agents report: hook stderr goes to
the *calling subagent*, so a coordinator that doesn't read the log only learns
about denials through the same self-report channel a fabrication could evade.

Why this exists: an early extraction agent once asserted a version fact for a
feature whose page states no version at all, quoting a sentence that did not
exist - and the fabricated quote was *more* plausible than the real sentence,
with better-argued reasoning than most correct records. Reviewing harder does
not fix this; only mechanical comparison against the file does.

**What to put in agent prompts because of it:**

- State that the gate exists and that a blocked Write means re-reading the page,
  not rewording the record.
- State the two legitimate escapes explicitly - `evidence_source` +
  `evidence_provenance` for a true-but-off-page fact, or omitting the relation
  and explaining in a finding field. Without both spelled out, a blocked agent's
  most available move is to quietly delete the relation, and **the gate turns
  fabrication into omission**, which is harder to notice than what it replaced.
- Warn that `Edit` is refused on extraction records; write the whole record with
  `Write`.
- Give agents the three `registry_status` values and tell them to run
  `registry-digest.py` rather than guess. Say explicitly that `extraction-layer`
  and `minted` are normal answers - an agent that reads `promoted` as the
  approved-looking value will guess it, and guessing is exactly what the enum
  replaced. A check that instead parses the prose note (rather than the enum)
  is known to misfire on a truthful negative ("and none is promoted") and on an
  accurate statement about a *different* id - the enum exists so there is no
  English left to misread.

**What the gate does not do**, and must not be described to agents as doing: it
proves the sentence is on the page, never that the triple built from it is a fair
reading. A "quotable but mis-objected" record - verbatim evidence, wrong object -
passes cleanly. A green check is not a green record, so reconciliation still
reads records rather than trusting the exit status.

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

A batch can fail partway (e.g. a session/usage limit). Before retrying:

- Check what that batch's output directory actually contains - don't assume
  zero progress.
- Validate whatever exists (`python3 -c "import json; json.load(open(f))"` over
  each file) before trusting it.
- Relaunch a new agent covering only the remaining pages, with the same
  registry and schema instructions - not a resend of the whole original batch.

## 7. Validate before moving to reconciliation

Once every batch reports back, run the audit over the new set. The write-time
gate should mean this comes back clean, and a surprise here means the gate was
bypassed (a record written before the hook was active, a path outside
`extractions/`, or a hook that didn't fire):

```bash
python3 linked-data/poc/verify-evidence.py linked-data/poc/extractions/<new-paths>
```

It exits non-zero on any problem, reports invalid JSON as well as unquotable
evidence, and so subsumes the bare `json.load` sweep this step used to do.

Do not skip it on the grounds that the gate already ran. The gate checks each
record as it is written; this checks the set as it now exists on disk, which is
not the same claim - and confirming that the two agree is how you find out the
gate is still working.

Then hand off to the `linked-data-reconcile` skill.
