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

### Five things the recurrence count won't tell you

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

Three specific ways the count has lied, every one found because the output looked
wrong rather than by reading the code:

- **`seeAlso` objects are pages, not concepts.** At recurrence 425 it put
  documentation pages above every real concept in round 11's first ranking.
  Exclude it from object recurrence; the candidate list went 465 -> 356 and the
  round's promotions changed.
- **Folded ids read as unpromoted.** An id listed in a surviving record's
  `aliases` array *is* promoted. Resolve aliases before counting debt, or
  `n1ql:cbq` (13 files, long since folded into `tool:cbq-shell`) appears as a top
  offender.
- **A missing `registry_status` is not a value.** Records predating round 11
  don't carry the field at all. Treat absent as *unknown*, never as
  `extraction-layer`, or an old record silently asserts something it never
  claimed.

**b. Check for thinning, because the write-time gate creates a new failure
mode.** `hooks/gate-evidence.py` blocks a record whose evidence isn't quotable.
An agent that can't find a real quote may drop the relation rather than hunt for
one, so the gate converts *fabrication* into *omission* - which no exit status
will ever show you, because an omitted relation leaves no trace.

**Read `hooks/gate-log.jsonl` first - it is the sharper instrument.** Every
verdict is there, allows included, with `n_relations`, so a deny followed by an
allow on the same path with a *lower* count is the fingerprint of exactly this
failure, where `deny(38) -> allow(38)` means the agent went and found the quote.
It also tells you the hook actually fired, which an absence of denials does not:

```python
import json, collections
log = [json.loads(l) for l in open("linked-data/poc/hooks/gate-log.jsonl")]
by_path = collections.defaultdict(list)
for r in log: by_path[r["path"]].append((r["outcome"], r["n_relations"]))
for path, seq in by_path.items():
    if any(o == "deny" for o, _ in seq): print(seq, path)
```

Report the scoreboard honestly in `reconciliation.md`, including false positives
and including this: a run with no denials cannot distinguish "the gate deterred
fabrication" from "no fabrication was attempted." Then use the relations-per-page
comparison as the backstop, for thinning that happened without a denial at all:

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

**c. Decide by namespace, not by rank, once the backlog is a long tail.** The
recurrence bar answers "is this term real?" and is structurally silent on "do this
namespace's members answer the same question?" Thirteen rounds took the
highest-recurrence candidates and decided each on its merits; round 14 grouped the
backlog by prefix and immediately found two defects that are invisible per-item:

```bash
python3 linked-data/poc/recurrence.py --unpromoted-only --min 2   # the worklist
python3 linked-data/poc/candidate-evidence.py --ns vector-index:  # read one namespace
```

`candidate-evidence.py` dumps every mention of a candidate id or a whole namespace
with page, relation slot, predicate and evidence quote, plus whether the id is
already promoted under another name. Its counts are every mention and are
deliberately **not** the promotion metric.

Do this before promoting any member of a namespace you have not looked at as a
whole, and in this order:

1. **Read the namespace's existing promoted records first.** `fts:` versus
   `search:` looks like a one-member collision and is a documented, deliberate
   resolution of a five-way split; a tidying pass would have destroyed a correct
   decision. The record explains itself - so read it before deciding it.
2. **Ask which kind of namespace it is.** Both kinds are legitimate: **subject
   areas** (`eventing:`, `capella:`, `monitoring:`, `backup:`) and **closed axes**
   (`index-type:`, `index-class:`, `auth-mechanism:`). `vector-index:` was named as
   the second and populated as the first for three rounds. When the answer is
   "axis-named, subject-populated", the fix is usually a **rename** - the remainder
   is a coherent subject area and only the name claimed otherwise - plus exact-match
   evacuations for the members that belong to axes that already exist.

   The test for the second kind: **a namespace is an axis only if its membership is
   closed and enumerable.** `edition:`, `index-state`, `auth-mechanism:` and
   `vector-similarity-metric:` pass - you can write the list down and a new member is
   news. `setting:` fails *by construction*, because a product acquires settings for
   as long as it is developed, so no wave will ever close it. Apply the test before
   asking which kind of namespace something is, because a third answer exists and it
   is the expensive one: a prefix that is **neither** an axis nor a subject area,
   because it names a *part of speech* rather than a topic. `setting:` had no subject
   to be about; "settings" is what its members *are*, not what they are *about*.

   The remedy differs, and it is the remedy that costs. A misnamed namespace gets a
   **rename**: one prefix rule in `normalise-ids.py`, 25 ids in round 14, cheap. A
   namespace with no subject gets a **dissolution**, member by member, into the
   subject areas that own the mechanisms - and that cannot be a prefix rule, because
   **a dissolution's destination is not a function of the id.** Nothing about the
   string `setting:query-max-parallelism` says it belongs with `n1ql:`; only reading
   what the setting configures does. Budget one decision per member (34 of them in
   round 15) and expect the rename table to carry them as exact matches, which is
   also where any *merges* get expressed.
3. **Check whether a member is already promoted under another prefix**, and do not
   assume the majority spelling is the promoted one. `index-type:hyperscale-vector`
   was promoted at recurrence 2 while `vector-index:hyperscale-vector-index` had 5
   files in another product tree. Same defect shape as round 12's misfiled roles:
   the wrong answer looked better-evidenced.

   Check the **referent**, not just the id, and expect no help from the gate here:
   `registry_status: minted` was a *true* declaration for `setting:scan-consistency`
   (no file had that id) while the thing it denotes had been promoted for five rounds
   as `n1ql:scan-consistency`. **The enum checks the id and never the referent** -
   "is this id in the registry" is mechanical, "is this *thing* in the registry" is
   the reading you are doing right now. Three of `setting:`'s 34 members were
   duplicates of this kind, and the two id features that hide them are a **tier**
   (`setting:collection-max-ttl` against the promoted `data:max-ttl-setting`) and a
   part of speech (`setting:encoded-plan` against `n1ql:encoded-plan`). Resolve by
   writing an `aliases` entry on the surviving record and folding the recurrence, not
   by deleting the duplicate: the extraction records that used the other spelling are
   evidence and stay as they are.
4. **Read the predicates the namespace's relations use.** They are the reliable
   signal, because there are ~100 predicates and every agent prompt lists them all,
   against ~300 concepts where the table an agent gets is partial - so the relation
   layer converges while the concept layer forks. `service:search-service
   -providesIndexType-> vector-index:search-vector-index` names the axis in the
   predicate and contradicts it in the object.

Expect a namespace pass to *retire* ids as well as promote them, and expect
families that straddle the bar (five page ids above it, five real concepts below
it, in one namespace). A family straddling the bar is an argument for reading the
family, not for lowering the bar.

**d. The unit of recurrence is the page, and pages duplicate each other.** Round 15
promoted `n1ql:curl-all-access` at recurrence 2 whose two files carry *one* table:
`curl.md` and `query-settings.md` describe the CURL access list in byte-identical
cells (244, 429 and 389 characters, measured), so two agents minted the same three
properties independently. Two files, one statement. The inverse also happens: a
canonical reference table mints its rows at recurrence 1 by construction, because
there is exactly one place to document them - so **the better the documentation, the
less promotable its contents**, and `query-settings.md` has eight settings
(`node-quota`, `prepared-limit`, `loglevel`, `controls`, `functions-limit`,
`keep-alive-length`, `max-index-api`, `tmpspace-dir`/`-size`) that no extraction has
ever minted at all and no queue will ever surface.

**e. The corpus is not the documentation, and a low count can mean the pages were
never read.** Round 16 spent a whole wave reorganising the index namespaces and then
found that `server/8.0/indexes/` - 11 pages, the canonical documentation of indexes -
**has never been extracted**, because round 12 went looking for those pages under
`learn/` after Antora had already moved them out of it. Every recurrence figure in
that wave was partly a fact about which directories nine rounds happened to walk. So
before reading a namespace's counts as evidence about the docs, check that the docs'
own directory for that subject is *in the sample*:

```bash
# does the subject have a directory nobody has extracted?
ls server/8.0/indexes/ | wc -l; ls linked-data/poc/extractions/server/8.0/indexes/ 2>&1
```

A missing directory reports as a low count, not as a gap, and there is no number
anywhere that distinguishes the two. When you find one, the wave's honest output is a
*re-extraction round*, not a set of promotions made on the evidence that happens to
exist - which is why round 16 refused to promote Plasma, Forestdb and Nitro despite
having read the sentences that define them.

Taken with (a) and the variant problem, the five failures are one failure:
**recurrence measures repetition, and repetition is an editorial property of the
documentation, not of the concept.** Keep the bar - it is still the best cheap signal
there is - and treat a measured duplication as a `docs-issues/` entry plus a
`recurrence_note` on the record saying what the count really counts. State the metric's
number and correct it in prose; do not quietly adjust the figure, because the next
round recomputes it and will find your adjustment unreproducible. Likewise never
trust a `recurrence` field you did not just recompute: `n1ql:encoded-plan` carried a
2 that counted *relations*, and nothing re-checks a recorded count after the round
that wrote it.

Round 16 measured how far that has gone - `recurrence.py --stale-recurrence` reports
**153 of 324 promoted records (47%) agreeing with the current query** - and the
finding is not that the fields are wrong. They record what was true when a human
wrote them, on an instrument that has since been replaced three times. The hazard is
that **a record's prose reasons about its own weight** ("a minor, low-stakes
promotion", written of a term the query now puts at 8), and a reconciliation pass
reads prose. So: re-measure before you quote, and **do not rewrite the fields to
agree** - the report is read-only on purpose, because a stale measurement is data and
a silently refreshed one is a lost audit trail. If a round's reasoning depended on a
field's value, put the re-measured number in a `recurrence_note` and say which
instrument produced each.

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

  The test that makes this decidable rather than a feeling: **if a promoted record
  cannot state what it *is* without naming a sub-threshold sibling, that sibling is
  part of the family.** `n1ql:curl-all-access` is a boolean whose whole definition is
  that it gates whether `allowed_urls` and `disallowed_urls` are consulted at all, so
  the two of them come in with it at recurrence 1. The test earns its keep by
  **refusing**: `n1ql:curl-result-cap` sits on the same page at the same recurrence
  and stays out, because nothing in the access list's definition names it. If a test
  cannot exclude anything on the page that suggested it, it is not a test.
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

**A record's `id` must mirror its own file path**, and this is now checked:
`python3 linked-data/poc/verify-registry-ids.py` exits non-zero on any mismatch.
It is not a formatting rule. The pipeline derives a term's id from its *path*
(`recurrence.py`), while extraction agents copy the id from the record's *`id`
field*, so when the two disagree the tooling and the agents believe different
things and both behave correctly. Nine `concepts/version/` records declared
dotted ids (`.../version/server-6.5`) under dashed filenames
(`server-6-5.json`); agents copied the dots faithfully and their correctness
registered as unpromoted debt for several rounds, while two of them diagnosed the
cause in their notes and asked reconciliation to settle it. `pages/*.jsonld` is
exempt and excluded by the checker: those records describe a real documentation
page, so their `@id` is that page's public URL, which the registry does not own.

**An id names its subject, not its location.** Round 16 found `covering-index`
spelled five ways across three namespaces - `index-type:`, `indexes:`, `index:`,
`n1ql:covering-index` and `n1ql:covering-indexes` - and the cause is not
carelessness: `covering-indexes.md` sits at a different path in each of four doc
trees, so an agent minting an id from the page in front of it produced a different
prefix each time, correctly, every time. No pass that reads one page at a time can
see this; only a namespace wave can. Three earlier instances have the same shape
(`tool:cbq-shell`, `protocol:dcp`, `tool:cbbackupmgr` were each split across three
namespaces by one directory naming them two ways). So when you file a record, ask
what the term *is*, never where it was read: a prefix that names a directory is a
smell, and `--variants` cannot catch these because the local names differ by a plural
as well as by prefix.

**Filing convention for Server RBAC roles: use the internal name, not the
display label.** `roles.md` gives every role both - "Role: Manage Global
Functions (query_manage_global_functions)" - and the registry files under
`role:query-manage-global-functions`, recording `internal_name` as a field and
the label form in `aliases`. Two reasons this has to be a rule rather than a
preference. First, the label is not a stable key: 20 of the 55 role tables have a
label word absent from the internal name, and in eight of those the internal name
uses an entirely different word (`Application Access` is `bucket_full_access`),
so two ids minted from the two names share no substring and
`recurrence.py --variants` can never cluster them - it catches typography, not
synonymy. Second, `roles.md` itself mislabels at least one table, so the label is
sometimes simply wrong where the internal name is right.

**Filing convention for settings documented at more than one tier: use the
tier-neutral kebab name.** SQL++ settings exist at request, node and cluster level
with different spellings of the same thing - `max_parallelism` as a request
parameter, `queryMaxParallelism` as a cluster setting - so file
`n1ql:max-parallelism` and alias the rest. Use the documented name unchanged only
when a setting exists at *one* tier and nowhere else (`n1ql:query-curl-whitelist` is
cluster-only, `n1ql:completed-stream-size` node-only). The reason is the same one
that governs folds: **tier membership is a fact for a relation, not for a fact about
an id.** Putting the tier in the id also produces the duplicate that no gate can
see - `setting:collection-max-ttl` against the promoted `data:max-ttl-setting` - and
it splits one setting's recurrence across two rare ids, so two members of a namespace
can each sit below the bar while the setting is well above it.

Do **not** push either convention upstream into the extract skill. An agent extracting a SQL++
reference page sees only the display label; requiring the internal name would
mean every such agent reads `roles.md` first. Minting the label form at
extraction time is correct, and re-filing to the internal name with an alias is
reconciliation's job - which is exactly the two-layer split the pipeline is built
on.

**When you fold one id into another, record it in an `aliases` array on the
surviving record.** This used to be documentation; it is now load-bearing. The
write-time gate resolves aliases when it checks an extraction record's
`registry_status`, so an unrecorded fold makes the gate deny a *correct*
declaration: an agent reusing `server:dcp-protocol` and truthfully marking it
`promoted` gets blocked unless `concepts/protocol/dcp.json` says it owns that
alias. 24 ids across 14 files are currently promoted under a different name than
extraction records use, and every one of them depends on this. Same for
predicates - `relations/uses-protocol.json` aliases `streamsMutationsVia`.

**Do not merge or cross-link two concepts just because they share a name or
surface similarity, unless a source page states the relationship explicitly.**
When two things collide on a name (this ontology currently has three unrelated
concepts all called "role," from three different products), document the
collision plainly in each record and in `reconciliation.md`, and leave them
separate. Inventing the relationship would be adding a fact, not extracting
one - if a later round's evidence resolves it, merge then, with the citation.

**But search the extraction layer, not just the registry, before refusing a merge -
a refusal is only as good as the set it searched.** Round 12 minted an enum, compared
it against the registry, correctly refused to merge it with `index-state` in writing,
and was blind to `index:indexer-node-state`, which was already in the corpus with the
same three values - because it had never been promoted, so `registry-digest.py` could
not show it. Four rounds later the same thing existed twice under two prefixes. A
registry digest answers "what may I declare as `promoted`?"; it is the wrong
instrument for "has anyone named this already?", which is
`candidate-evidence.py --ns <prefix>` or a grep over `extractions/`. This is the
second well-argued refusal overturned by evidence that was already on disk.

**And when a fold *is* licensed, quote the sentence that licenses it.** An alias is a
claim about a **referent**, and the gate resolves aliases before checking an id -
which makes it the one field in the registry that can make two different things pass
as one, permanently and invisibly. `verify-registry-ids.py` catches an alias that
merely re-punctuates its target; nothing reaches the semantic case and nothing can.
Round 16 wrote 21 aliases in one pass and deleted a promoted record for the first
time in the POC's history (`capella:index-ui-status` into `indexer-node-state`); what
makes that reviewable by someone who was not in the room is that the record quotes
the two near-identical defining sentences, one per product tree, side by side. Do
that every time you fold.

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
`linked-data/poc/docs-issues/<product>-<kebab-case-slug>.json`. **The `<product>-`
prefix is the convention, not an option** - since round 16, a `docs-issues/<slug>`
reference from any registry record with no file behind it is a
`verify-registry-ids.py` failure, because two references written in earlier rounds
used the descriptive name without the prefix and went unnoticed for four rounds. That
fails in the worst direction: a promoted record says "see `docs-issues/X` for the
contradiction", a reader finds nothing, and concludes the caveat was never real.

There is a third category, and rounds where the input is the *registry* rather
than a page produce mostly this one: a fact about **this registry** - a
namespace named as a closed axis but populated as a subject area, a predicate
whose declared range contradicts its ten uses, 86 relation objects pointing at
an alias that will move. None of those is a docs-issue. `docs-issues/` is for
facts about Couchbase's documentation, and filing a registry defect there
misdirects whoever eventually triages the file. Registry defects belong in
`reconciliation.md` - measured, in the round's section, with the fix either
applied or explicitly queued in `README.md`'s next steps. Round 14 got this
wrong in the other direction too: it wrote up four docs-issues, none of which
survived checking the pages, because an extraction record's finding field is
evidence *about* a page, never a substitute for reading it. Before filing, open
the page the finding is about.

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
python3 linked-data/poc/verify-evidence.py      # gate: exits non-zero on any problem
python3 linked-data/poc/verify-registry-ids.py  # gate: every record's id mirrors its path
python3 linked-data/poc/recurrence.py --selftest
python3 linked-data/poc/verify-promotions.py    # report: always exits 0, always read it
python3 linked-data/poc/recurrence.py --variants  # report: read it, decide alias vs rewrite
python3 linked-data/poc/recurrence.py --stale-recurrence  # report: which `recurrence` fields still hold
python3 linked-data/poc/recurrence.py --page-ids   # report: ids that are only ever linked to
python3 linked-data/poc/candidate-evidence.py --ns <ns>  # while deciding, not at the end
python3 linked-data/poc/candidate-evidence.py --audit <ids...>   # before promoting them
python3 linked-data/poc/hooks/test-gate.py       # gate: only if you changed the gate
```

`verify-promotions.py` lists every `ns:kebab-id`, `camelCaseTerm` and backticked
`long-kebab-slug` named in `reconciliation.md` that has no file in `concepts/`,
`relations/` or `docs-issues/` respectively. It cannot tell "claimed as promoted"
from "named while being rejected, folded, deferred or watchlisted" - the prose
says which, the string doesn't - so **read the list, don't diff it**. The slug
check is looser than the other two by construction and will report ordinary
hyphenated prose in backticks; that is the price of catching round 14's miss,
where a "New `docs-issues/`" subsection named four entries, none of which was
ever filed, and this script reported nothing because it only looked at two of
the three hand-written artefact families. **A control's coverage is itself a
claim** - when a round writes a new kind of file, check that something checks
it.

Run it *after* writing the round's section, not before, and then run it again if
you edit that section. Round 10's first run found 5 real gaps; re-running it once
the writeup was finished found 3 more, including a concept at recurrence 6 whose
own extraction record claimed it was "already promoted". This is the fourth-plus
recurrence of "narrated as promoted, never actually filed" (rounds 2, 3, 5, 8),
which is why the check exists at all rather than being left to care.

`recurrence.py --variants` clusters ids that are the same term spelled more than
one way, and every cluster needs a decision - **alias it or rewrite it**, per the
rule in `normalise-ids.py`'s docstring. Alias when the variant is a defensible
alternative name (a different namespace, a display label against an internal
name): that is additive and forward-only, and it converts any future reuse of the
old form into a gate denial rather than a silent duplicate. Rewrite the extraction
records, with `normalise-ids.py`, when the variant is not a legitimate name for
the thing anywhere (`version:server-6.5`, `n1ql:createfunction`) - aliasing a typo
enshrines it as vocabulary. Then re-run `--variants`: the count must go down, and
each surviving cluster must be one you decided to leave.

Read the `0 files` rows. `--variants` seeds the registry in as a speller, so a
cluster whose *only used* form is the `NO FILE` one is pure false debt: the corpus
spells the term one way, uniformly, and the registry spells it another. That is the
worst case rather than the mildest, because every file using it is gate-denied and
sits in the backlog. It is also the case the check could not see until round 13 -
it clustered the corpus against itself, so a one-sided variant gave a cluster of
size one and was skipped in silence, hiding three instances of the very defect
round 13 was written to fix.

Run this every round, not only when something looks wrong. The loud failure is a
promoted term reading as unpromoted debt; the quiet one is a genuine candidate
held *below* the promotion bar because its count is split across two spellings,
and round 13 found five terms that had silently suffered it. Note also what the
clustering cannot see: it keys on typography, so it catches `create-function` vs
`createfunction` and never `Application Access` vs `bucket_full_access`. Namespace
variants need a separate local-name match, which is how round 13's other five
turned up.

Expect known-bad numbers from `verify-evidence.py` over the whole corpus: 313
unquotable relations and 130 with no evidence (443 problems), nearly all in
rounds 1-9, written before the write-time gate existed. Scope it to the new batch to
get a clean signal, and don't "fix" a historical count by editing old records -
round 3's `sync-gateway` and `couchbase-lite` batches need *re-extraction*, which is
a tracked next step, not a reconciliation task.

**"Scope it to the new batch" assumes the round has one, and a coherence wave does
not.** Rounds 14 and 15 took the registry as input: they added no extraction
records, so that instruction verified nothing, while the round's actual risk was
that its promotions were licensed by records written in the very first POC commit,
years of controls ago. One of them quotes a sentence that is verbatim on a
*different* page than the one the relation names - which is the entire reason
`evidence_source` exists - and it cost a recurrence, because credited to the page
that carries it the term's two files collapse to one. So on a registry-input round
the check that matters is on the reading path:

```bash
python3 linked-data/poc/candidate-evidence.py --ns <ns> --audit   # before promoting
```

`--audit` reduces the run to the ids with at least one quote that is not on the page
it cites. Run it over every id you are about to promote or fold. Reading a namespace
and checking that what you are reading is real are then one action, with no separate
step to forget - which matters because the write-time gate protects records *as they
are written*, and promotion reads records written long before it existed.

Two related things not to do. Don't re-run `hooks/gate-evidence.py` over old records
as an audit: a real round-12 record replayed through it today produces five denials,
because `registry_status` describes the registry the record was written *against*,
and 200 promotions later `minted` is false about ids the registry has since acquired.
**A control's verdict can expire.** And don't "correct" those records to match
today's registry - the declaration was true when it was made. `hooks/test-gate.py`
(30 cases) is the regression suite for the gate's non-evidence rules, and its
fixtures are synthetic for exactly this reason. When a round adds a rule that
*withdraws* a permission - round 16 retired the `indexes:` prefix, so "reusing an
`indexes:` id is allowed" flipped from a correct assertion to a wrong one - change the
assertion **and write the reasoning beside it**, because in a diff an intentional flip
is indistinguishable from a test loosened to make a change pass.

**If you touch `recurrence.py`, decide separately what the metric ignores and what the
census ignores.** Round 14 excluded `seeAlso` from the concept-promotion metric, for a
good reason, by editing a shared code path - and thereby excluded 376 ids, 18% of the
corpus, from the *census* as well: they appeared in no report this project produces,
including `--variants`, whose only job is to enumerate spellings. Five misspellings of
promoted statements hid there for two rounds, and the shadow-prefix figure quoted in
two writeups (43) was really 55. `scan()` now returns `mentions`, `slots`, `labels`
and `see_also_objects` as separate tables so a caller has to state which question it
is asking; keep it that way. The general form is worth carrying into every number you
write down: **a figure inherits the instrument that produced it, and nothing in this
pipeline records which instrument that was** - so when a writeup quotes a count, say
which report produced it.

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
