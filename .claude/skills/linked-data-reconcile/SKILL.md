---
name: linked-data-reconcile
description: Reconcile a batch of linked-data/poc/extractions/ records into promoted concepts/relations/docs-issues, and update reconciliation.md and README.md. Use after running the linked-data-extract skill, once a new extraction batch has landed. Phase 2 of 2.
---

# Linked-data reconciliation pass

Phase 2 of the linked-data POC pipeline (see the `linked-data-extract` skill for
phase 1). Turns raw pass-1 extraction records into promoted ontology terms and a
tracked docs-issue log, without reading every extraction file individually -
reconciling by aggregating recurrence, the same discipline phase 1 asks agents
to extract with.

## 1. Aggregate, don't eyeball

Once past a handful of pages, read no more extraction files individually than
you have to. Run a script over the new batch (or the whole `extractions/` tree,
if checking for cross-round collisions) to count:

- **Predicate recurrence**: how many distinct *files* use each predicate name
  (not total occurrences - two uses on the same page are one data point, not
  two).
- **Object recurrence**: how many distinct files reference each object id -
  this is the concept-promotion signal.
- Every `notable_absence` / `cross_component_finding` / `cross_product_finding`
  field, collected in full (not summarized) for review.

Template:

```python
import json, glob, collections

files = sorted(glob.glob("linked-data/poc/extractions/<scope>/**/*.json", recursive=True))
predicate_files = collections.defaultdict(set)
object_files = collections.defaultdict(set)
findings = {"notable_absence": [], "cross_component_finding": [], "cross_product_finding": []}

for fp in files:
    data = json.load(open(fp))
    for r in data.get("relations", []):
        if r.get("predicate"): predicate_files[r["predicate"]].add(fp)
        if r.get("object"): object_files[r["object"]].add(fp)
    for k in findings:
        if k in data: findings[k].append((fp, data[k]))

# predicates/objects with len(files) >= 2 are promotion candidates
```

## 2. Apply the promotion rule

**A predicate or concept is a promotion candidate once it recurs across two or
more distinct pages/files** - not two uses on one page. This threshold has held
up across three rounds; don't lower it just because a single-occurrence term
looks obviously important. A genuinely important but single-occurrence term is
better left on a documented watchlist than promoted on a sample size of one.

Two exceptions call for judgment rather than the mechanical rule:

- **A small family of individually-low-recurrence predicates that together
  cover one well-evidenced mechanism** (e.g. a product's GRANT/REVOKE/CREATE
  GROUP statement family, where most individual predicates are single-occurrence)
  can be promoted as a group, documented as a family, even though no single
  member crosses the threshold alone.
- **A predicate whose semantic significance outweighs its recurrence** (e.g. a
  relation minted specifically because it was the sharpest evidence for a
  headline finding) can be promoted below the usual bar - but say so explicitly
  in its record; don't silently apply a different standard without noting it.

## 3. Write the promoted records

Concepts go in `linked-data/poc/concepts/<namespace>/<name>.json` (or a
top-level `concepts/<name>.json` for scheme-like enums, matching the pattern
used for enumerations that are a small closed set rather than a single term).
Relations go in `linked-data/poc/relations/<kebab-case-name>.json`. **Never file
a relation under `concepts/`** - properties and instances are different
ontology layers (roughly RDFS/OWL's TBox/ABox split, explained in
`linked-data/poc/README.md`); this was gotten wrong once, early on, and
corrected - don't reintroduce it.

Every record needs: `id` (the real `https://docs.couchbase.com/ld/...` IRI,
mirroring the file's own path), `label`, a `type`/description explaining what
it is and - critically - what it must **not** be confused with if a
same-named-but-different thing exists elsewhere in the registry, `promoted:
true`, `recurrence`, and a short `note` with the promotion reasoning.

**Do not merge or cross-link two concepts just because they share a name or
surface similarity, unless a source page states the relationship explicitly.**
When two things collide on a name (this ontology currently has three unrelated
concepts all called "role," from three different products), document the
collision plainly in each record and in `reconciliation.md`, and leave them
separate. Inventing the relationship would be adding a fact, not extracting
one - if a later round's evidence resolves it, merge then, with the citation.

Only draft full `.jsonld` (with `@context`, `@id`, `@type` against a real
class) for a **flagship subset** - the highest-recurrence or most
semantically-significant new terms from the round. Leave the rest at the
intermediate `.json` layer and say so explicitly in `README.md` - full JSON-LD
coverage is a deliberately deferred step at every round so far, not an
oversight.

## 4. Decide what's a `docs-issue` vs. an ontology promotion

Ask: is this a fact about **the product** (a real mechanism, however unusual)
or a fact about **the documentation** (a gap, a duplication, unadapted copy, an
internal contradiction, an empty stub page)? The former gets modeled as
concepts/relations. The latter goes to
`linked-data/poc/docs-issues/<kebab-case-slug>.json`:

```json
{
  "id": "https://docs.couchbase.com/ld/docs-issues/<slug>",
  "type": "docs-issue",
  "issueType": "<short category, minted freely>",
  "description": "...",
  "about": ["<page ids affected>"],
  "foundDuring": "<this round's label>",
  "status": "open"
}
```

`issueType` examples already in use: `missing-privilege-documentation`,
`possible-content-duplication`, `unadapted-shared-source-content`,
`content-gap`, `possible-concept-duplication`, `title-content-mismatch`,
`possible-content-inconsistency`. Mint new ones freely - this bucket is
deliberately ungatekept (see `README.md`'s reasoning: at scale, nobody reads
this file top to bottom, they query it). Cross-link from the originating
`extractions/` record's finding field to the new docs-issue id, but do **not**
reference a docs-issue from a public-facing `pages/*.jsonld` file - that's
internal QA, not something a public consumer of the page's structured data
needs to see.

## 5. Resolve stubs across batches

If an earlier batch minted a placeholder stub for something owned by a
different (possibly not-yet-run) batch, note in `reconciliation.md` that the
stub now resolves to the real promoted concept, once that concept exists. Don't
silently delete or rewrite the original extraction record - the stub was a
reasonable, honestly-labeled guess at the time; the resolution is new
information, not a correction of an error.

## 6. Update `reconciliation.md`

One section per round, in run order, containing: scope, headline finding(s),
other promotions, new `docs-issues/` (list with one line each), and anything
learned about the *method* itself (a limitation, a re-discovered consolidation,
a naming collision worth flagging). End the file with a single cumulative
verdict reflecting all rounds so far, not a new verdict appended per round - if
the file starts accumulating multiple "Updated verdict" headers, that's a sign
it needs a full rewrite into clean chronological order with one verdict at the
end, not another patch on top.

## 7. Update `README.md`

Keep in sync: the page-count-and-round summary at the top, the `Scope` section,
the `concepts:`/`relations:`/`docs-issues:` bullet descriptions in "How to read
this directory" (these go stale fast - they should always describe the
*current* families, not just the first round's), the "Headline findings"
section (append the new round's findings, keep prior rounds'), and "Suggested
next steps" (remove what's now done, add what the round surfaced as the next
natural thing to try).

## Principles that govern the judgment calls throughout

- **Competency-question discipline.** Don't promote a concept or relation that
  doesn't answer one of the questions this exercise exists to answer. The POC
  has stayed small and reviewable precisely because "does this earn its place"
  gets asked at every promotion, not just at the start.
- **Recurrence is a query, not hand-tracked state.** Don't ask an agent (or
  yourself) to remember or maintain a count - compute it from the actual
  extraction files, every time, fresh.
- **Reuse real vocabulary where it genuinely fits** (`rdfs:seeAlso`,
  `skos:Concept`/`skos:ConceptScheme`, `schema:TechArticle`) **and mint
  product-specific terms without hesitation where nothing fits** - both
  directions of this call matter equally; defaulting to either "always reuse"
  or "always mint" produces a worse ontology than checking each time.
- **A structural finding about the docs is not a failure of the ontology
  method** - it's a genuine, separate kind of value this process produces
  alongside the ontology itself. Don't try to make the extraction schema "fix"
  what a human needs to look at; route it to `docs-issues/` and move on.
