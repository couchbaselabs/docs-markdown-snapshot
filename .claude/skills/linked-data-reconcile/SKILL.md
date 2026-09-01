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

### Two things the recurrence count won't tell you

Run these alongside the aggregation, before applying the promotion rule.

**a. Run the whole corpus, not just this round's scope.** Round 10 recomputed
recurrence over all of `extractions/` for the first time and found
`n1ql:query-context` sitting unpromoted at **recurrence 22**, plus `create-index`
at 20 and `tool:cbq-shell` at 18 - eight rounds of promotion debt invisible to
any round that only counted its own files. `<scope>` in the template above should
be empty by default. And when you write the counting script, *test the helpers*:
round 10's first run reported every already-promoted predicate as unpromoted
because of a one-character regex bug (`\.jsonld?` where `\.json(ld)?` was meant),
caught only because the output was implausible.

**b. Check for thinning, because the write-time gate creates a new failure
mode.** `hooks/gate-evidence.py` blocks a record whose evidence isn't quotable.
An agent that can't find a real quote may drop the relation rather than hunt for
one, so the gate converts *fabrication* into *omission* - which no exit status
will ever show you, because an omitted relation leaves no trace. The only place
to catch it is here:

```python
# Relations per page, for the new batch against comparable already-extracted pages.
# A wave-1 statement page averaged ~13; a page returning 2 or 3 wants a look.
for fp in files:
    d = json.load(open(fp))
    print(len(d.get("relations", [])), fp)
```

Compare like with like - a reference page against a reference page, not against a
navigation stub, which legitimately has almost nothing. What you're looking for
is a page whose twin in another tree is dense and whose own record is thin. Treat
that as a finding to check by reading the page, not as a number to accept.

Round 10's own distribution is the baseline to compare against: 38 records, 509
relations, mean 13.4. Its three sparsest records hold 1, 2 and 2 relations
(`exunsupportedhttp`, `exauthhttp`, `exserviceerror`) - all single-example REST
API pages of 30-odd lines, so sparse for real reasons. That's the shape to expect:
a *long* page with a thin record is the signal, not a thin record as such.

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

## 8. Run the checks before committing

```bash
python3 linked-data/poc/verify-evidence.py     # gate: exits non-zero on any problem
python3 linked-data/poc/verify-promotions.py   # report: always exits 0, always read it
```

`verify-promotions.py` lists every `ns:kebab-id` and `camelCaseTerm` named in
`reconciliation.md` that has no registry file. It cannot tell "claimed as
promoted" from "named while being rejected, folded, deferred or watchlisted" -
the prose says which, the string doesn't - so **read the list, don't diff it**.

Run it *after* writing the round's section, not before, and then run it again if
you edit that section. Round 10's first run found 5 real gaps; re-running it once
the writeup was finished found 3 more, including a concept at recurrence 6 whose
own extraction record claimed it was "already promoted". This is the fourth-plus
recurrence of "narrated as promoted, never actually filed" (rounds 2, 3, 5, 8),
which is why the check exists at all rather than being left to care.

Expect known-bad numbers from `verify-evidence.py` over the whole corpus: 322
unquotable relations and 130 with no evidence, nearly all in rounds 1-9, written
before the write-time gate existed. Scope it to the new batch to get a clean
signal, and don't "fix" a historical count by editing old records - round 3's
`sync-gateway` and `couchbase-lite` batches need *re-extraction*, which is a
tracked next step, not a reconciliation task.

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
