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

## 0. Run this in a fresh session, and read `reconciliation.md`/`README.md` by anchor, not in full

**Do not run reconciliation inline in a long-running coordinator session that
has accumulated rounds of history.** Cache-read tokens (re-sending the entire
prior conversation on every turn) can dominate a long session's cost, purely as
a function of session length, not of how much genuinely new work a given round
does. Dispatch reconciliation to a fresh agent (or fresh session) with no memory
of prior rounds instead. Everything it needs is on disk: `registry-digest.py`,
`recurrence.py`, `candidate-evidence.py`, the extraction files themselves, and
the tail of `reconciliation.md`/`README.md` for format. A fresh-session
reconciliation gets comparable depth and tool-call volume to an in-session one,
at a cost comparable to a single extraction batch. The coordinator dispatching
it can stay a long-running session (someone has to track the project across
rounds) - the actual reconciliation *work* shouldn't happen inside it.

This matters because `reconciliation.md` and `README.md` are themselves large
and growing every round - but that's a different problem than session-length
cost, if read correctly. A conversation's history must be re-sent in full on
every turn; a *file* can be read selectively. Never read either file end to
end. Use `grep -n` to find the anchor you need (the previous round's own
paragraph in the cumulative verdict, the last numbered entry in a list, the
tail of the `## Round N` sections) and `Read` with a narrow `offset`/`limit`
around it. Find every insertion point by grepping for the previous round's
exact anchor text. If a round's write-up seems to require understanding the
whole document to place correctly, that is a sign the document itself needs
restructuring (see step 6), not a reason to read all of it every round.

The one file that genuinely has no anchor to grep for is the registry digest
(`registry-digest.py`) - a near-duplicate concept could be anywhere in it, so
there's no "just the relevant lines" shortcut the way there is for a log file.
When a round has a clear namespace focus, scope the digest to the relevant
prefixes before handing it to an extraction agent (grep the concepts section
for the namespaces in play, keep the full relations/predicates section, since
predicates are reused across domains and aren't namespace-scoped) rather than
passing the whole thing - this has cut prompt size by roughly 40% with no loss,
since an agent can still run `candidate-evidence.py`/`registry-digest.py`
itself for anything the excerpt left out.

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

**a. Run the whole corpus, not just this round's scope.** `<scope>` in the
template above should be empty by default - restricting the count to the new
batch hides promotion debt accumulated across every earlier round (real
example: a term sitting unpromoted at recurrence 22 while nine rounds each
computed recurrence only over their own files). When you write or change the
counting script, test its regexes before trusting the output - a
one-character bug can silently misclassify every already-promoted predicate as
unpromoted. If the output looks implausible, it probably is; every instance of
this found so far was caught that way, not by reading the code.

Specific ways the count has lied:

- **`seeAlso` objects are pages, not concepts.** Exclude `seeAlso` from object
  recurrence, or documentation pages will outrank every real concept.
- **Folded ids read as unpromoted unless aliases are resolved first.** An id
  listed in a surviving record's `aliases` array *is* promoted - resolve
  aliases before counting debt, or a long-folded id reappears as a top
  "offender".
- **A missing `registry_status` is not a value.** Records predating the gate
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
for fp in files:
    d = json.load(open(fp))
    print(len(d.get("relations", [])), fp)
```

Compare like with like - a reference page against a reference page, not against a
navigation stub, which legitimately has almost nothing. What you're looking for
is a page whose twin in another tree is dense and whose own record is thin. Treat
that as a finding to check by reading the page, not as a number to accept. A
useful baseline: an early, carefully-reviewed 38-record wave averaged 13.4
relations/page, with its three sparsest records (1-2 relations each) being
genuinely short single-example REST pages. That's the shape to expect: a *long*
page with a thin record is the signal, not a thin record as such.

**c. Decide by namespace, not by rank, once the backlog is a long tail.** The
recurrence bar answers "is this term real?" and is structurally silent on "do this
namespace's members answer the same question?" Deciding backlog items one at a
time by highest recurrence misses defects that only show up when a whole
namespace is read together:

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

1. **Read the namespace's existing promoted records first.** A one-member
   apparent collision (e.g. `fts:` vs `search:`) can be a documented, deliberate
   resolution of an earlier multi-way split; a tidying pass would destroy a
   correct decision. The record explains itself - read it before deciding it.
2. **Ask which kind of namespace it is.** Both kinds are legitimate: **subject
   areas** (`eventing:`, `capella:`, `monitoring:`, `backup:`) and **closed axes**
   (`index-type:`, `index-class:`, `auth-mechanism:`). A namespace can be named
   as an axis and populated as a subject area for several rounds before anyone
   notices. When the answer is "axis-named, subject-populated", the fix is
   usually a **rename** - the remainder is a coherent subject area and only the
   name claimed otherwise - plus exact-match evacuations for the members that
   belong to axes that already exist.

   The test for the second kind: **a namespace is an axis only if its membership
   is closed and enumerable.** `edition:`, `index-state`, `auth-mechanism:` and
   `vector-similarity-metric:` pass - you can write the list down and a new
   member is news. `setting:` fails *by construction*, because a product
   acquires settings for as long as it is developed, so no wave will ever close
   it. Apply the test before asking which kind of namespace something is,
   because a third answer exists and it is the expensive one: a prefix that is
   **neither** an axis nor a subject area, because it names a *part of speech*
   rather than a topic. `setting:` had no subject to be about; "settings" is
   what its members *are*, not what they are *about*.

   The remedy differs, and it is the remedy that costs. A misnamed namespace gets
   a **rename**: one prefix rule in `normalise-ids.py`, cheap. A namespace with no
   subject gets a **dissolution**, member by member, into the subject areas that
   own the mechanisms - and that cannot be a prefix rule, because **a
   dissolution's destination is not a function of the id.** Nothing about the
   string `setting:query-max-parallelism` says it belongs with `n1ql:`; only
   reading what the setting configures does. Budget one decision per member, and
   expect the rename table to carry them as exact matches, which is also where
   any *merges* get expressed.
3. **Check whether a member is already promoted under another prefix**, and do not
   assume the majority spelling is the promoted one. A minority spelling promoted
   at low recurrence can predate a majority spelling that accumulated more files
   in a different product tree without ever being checked against it - the wrong
   answer can look better-evidenced.

   Check the **referent**, not just the id, and expect no help from the gate here:
   `registry_status: minted` can be a *true* declaration for an id (no file has
   that exact id) while the thing it denotes has been promoted for many rounds
   under a different prefix. **The enum checks the id and never the referent** -
   "is this id in the registry" is mechanical, "is this *thing* in the registry"
   is the reading you are doing right now. Two id features hide this kind of
   duplicate: a **tier** (a setting id duplicating a `data:`-namespaced promoted
   fact) and a **part of speech** (a `setting:` id duplicating an `n1ql:` id for
   the same referent). Resolve by writing an `aliases` entry on the surviving
   record and folding the recurrence, not by deleting the duplicate: the
   extraction records that used the other spelling are evidence and stay as they
   are.
4. **Read the predicates the namespace's relations use.** They are the reliable
   signal, because there are ~100 predicates and every agent prompt lists them
   all, against ~300+ concepts where the table an agent gets is partial - so the
   relation layer converges while the concept layer forks. A relation whose
   predicate names one axis and whose object contradicts it in the object id is
   the sharpest evidence you'll get for a namespace defect.

Expect a namespace pass to *retire* ids as well as promote them, and expect
families that straddle the bar (some page ids above it, some real concepts below
it, in one namespace). A family straddling the bar is an argument for reading the
family, not for lowering the bar.

**d. The unit of recurrence is the page, and pages duplicate each other.** Two
files can carry byte-identical content (a shared reference table reproduced on
two product pages), so two agents mint the "same" properties independently and
recurrence 2 really means one statement, seen twice. The inverse also happens: a
canonical reference table mints its rows at recurrence 1 by construction,
because there is exactly one place to document them - so **the better the
documentation, the less promotable its contents**, and a well-organized
reference page can hold several settings that no extraction will ever mint at
recurrence ≥2 and no queue will ever surface.

**e. The corpus is not the documentation, and a low count can mean the pages were
never read.** A whole product area's canonical documentation directory can go
unextracted for many rounds because an earlier round looked for those pages
under the wrong path (e.g. after a docs-platform reorganization moved them).
Every recurrence figure for that subject is then partly a fact about which
directories past rounds happened to walk, not about the concept. Before reading
a namespace's counts as evidence about the docs, check that the docs' own
directory for that subject is *in the sample*:

```bash
# does the subject have a directory nobody has extracted?
ls server/8.0/indexes/ | wc -l; ls linked-data/poc/extractions/server/8.0/indexes/ 2>&1
```

A missing directory reports as a low count, not as a gap, and there is no number
anywhere that distinguishes the two. When you find one, the honest output is
**an extraction round**, not a set of promotions made on whatever evidence
happens to exist - don't promote sub-concepts on the strength of sentences read
in passing while the module they belong to has never been properly extracted.

Keep "extract" and "re-extract" distinct when you write that up, because they are
different jobs with different success criteria and the words are the only thing
separating them. A directory nobody walked needs **first-contact extraction**, and
the question is what the pages say that no round has read. A directory walked
badly needs **re-extraction**, and the question is whether the conclusions already
drawn from those records survive. Calling both of them "re-extraction" quietly
files a never-read module under a backlog whose framing is "these records are
unreliable" - which understates what's actually missing.

Taken together, the five failures are one failure: **recurrence measures
repetition, and repetition is an editorial property of the documentation, not of
the concept.** Keep the bar - it is still the best cheap signal there is - and
treat a measured duplication as a `docs-issues/` entry plus a `recurrence_note`
on the record saying what the count really counts. State the metric's number and
correct it in prose; do not quietly adjust the figure, because the next round
recomputes it and will find your adjustment unreproducible. Likewise never trust
a `recurrence` field you did not just recompute - nothing re-checks a recorded
count after the round that wrote it, and a field can silently count the wrong
thing (relations instead of files, for example).

`recurrence.py --stale-recurrence` measures how far the promoted registry's
recorded `recurrence` fields have drifted from a fresh recount - roughly half of
promoted records currently disagree with the current query. That's not evidence
the fields were wrong when written; they recorded what was true on an instrument
that has since been replaced or extended. The hazard is that **a record's prose
reasons about its own weight** (calling a term "a minor, low-stakes promotion"
that the current query would rank far higher), and a reconciliation pass reads
prose. So: re-measure before you quote a recurrence number, and **do not rewrite
the stored fields to agree** - the report is read-only on purpose, because a
stale measurement is data and a silently refreshed one is a lost audit trail. If
a round's reasoning depends on a field's value, put the re-measured number in a
`recurrence_note` and say which instrument produced each number.

## 2. Apply the promotion rule

**A predicate or concept is a promotion candidate once it recurs across two or
more distinct pages/files** - not two uses on one page. Don't lower this
threshold just because a single-occurrence term looks obviously important. A
genuinely important but single-occurrence term is better left on a documented
watchlist than promoted on a sample size of one.

Two exceptions call for judgment rather than the mechanical rule:

- **A small family of individually-low-recurrence predicates that together
  cover one well-evidenced mechanism** (e.g. a product's GRANT/REVOKE/CREATE
  GROUP statement family, where most individual predicates are single-occurrence)
  can be promoted as a group, documented as a family, even though no single
  member crosses the threshold alone.

  The test that makes this decidable rather than a feeling: **if a promoted record
  cannot state what it *is* without naming a sub-threshold sibling, that sibling is
  part of the family.** A boolean whose whole definition is that it gates whether
  two other fields are consulted at all pulls those two fields in with it at
  recurrence 1. The test earns its keep by **refusing**: a sibling predicate on the
  same page at the same recurrence stays out if nothing in the family's definition
  names it. If a test cannot exclude anything on the page that suggested it, it is
  not a test.
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
`linked-data/poc/README.md`).

Every record needs: `id` (the real `https://docs.couchbase.com/ld/...` IRI,
mirroring the file's own path), `label`, a `type`/description explaining what
it is and - critically - what it must **not** be confused with if a
same-named-but-different thing exists elsewhere in the registry, `promoted:
true`, `recurrence`, and a short `note` with the promotion reasoning.

**A record's `id` must mirror its own file path**, and this is checked:
`python3 linked-data/poc/verify-registry-ids.py` exits non-zero on any mismatch.
It is not a formatting rule. The pipeline derives a term's id from its *path*
(`recurrence.py`), while extraction agents copy the id from the record's *`id`
field*, so when the two disagree the tooling and the agents believe different
things and both behave correctly - a dashed filename with a dotted `id` field
(e.g. `.../version/server-6.5` under `server-6-5.json`) causes extraction agents
to faithfully copy the dotted id, which then registers as unpromoted debt.
`pages/*.jsonld` is exempt and excluded by the checker: those records describe a
real documentation page, so their `@id` is that page's public URL, which the
registry does not own.

**An id names its subject, not its location.** A single term (e.g. "covering
index") can end up spelled several different ways across several namespaces,
because the source page sits at a different path in each of several doc trees
and an agent minting an id from the page in front of it produces a different
prefix each time - correctly, every time. No pass that reads one page at a time
can see this; only a namespace wave can. This has happened more than once with
the same shape (a shared tool or protocol name split across namespaces by
directory naming). So when you file a record, ask what the term *is*, never
where it was read: a prefix that names a directory is a smell, and
`--variants` cannot catch these, because the local names can differ by more
than typography (e.g. a plural as well as a prefix).

**Filing convention for Server RBAC roles: use the internal name, not the
display label.** `roles.md` gives every role both - "Role: Manage Global
Functions (query_manage_global_functions)" - and the registry files under
`role:query-manage-global-functions`, recording `internal_name` as a field and
the label form in `aliases`. Two reasons this has to be a rule rather than a
preference. First, the label is not a stable key: many role tables have a label
word absent from the internal name, and some use an entirely different word
(`Application Access` is `bucket_full_access`), so two ids minted from the two
names can share no substring and `recurrence.py --variants` can never cluster
them - it catches typography, not synonymy. Second, `roles.md` itself mislabels
at least one table, so the label is sometimes simply wrong where the internal
name is right.

**Filing convention for settings documented at more than one tier: use the
tier-neutral kebab name.** SQL++ settings exist at request, node and cluster level
with different spellings of the same thing - `max_parallelism` as a request
parameter, `queryMaxParallelism` as a cluster setting - so file
`n1ql:max-parallelism` and alias the rest. Use the documented name unchanged only
when a setting exists at *one* tier and nowhere else (`n1ql:query-curl-whitelist` is
cluster-only, `n1ql:completed-stream-size` node-only). The reason is the same one
that governs folds: **tier membership is a fact for a relation, not a fact about
an id.** Putting the tier in the id also produces a duplicate that no gate can
see, and it splits one setting's recurrence across two rare ids, so two members
of a namespace can each sit below the bar while the setting is well above it.

Do **not** push either convention upstream into the extract skill. An agent
extracting a SQL++ reference page sees only the display label; requiring the
internal name would mean every such agent reads `roles.md` first. Minting the
label form at extraction time is correct, and re-filing to the internal name
with an alias is reconciliation's job - which is exactly the two-layer split
the pipeline is built on.

**When you fold one id into another, record it in an `aliases` array on the
surviving record.** This used to be documentation; it is now load-bearing. The
write-time gate resolves aliases when it checks an extraction record's
`registry_status`, so an unrecorded fold makes the gate deny a *correct*
declaration: an agent reusing an aliased id and truthfully marking it
`promoted` gets blocked unless the surviving record's file says it owns that
alias. Dozens of ids across the registry are currently promoted under a
different name than extraction records use, and every one of them depends on
this. Predicates fold the same way (a predicate file can alias an older
predicate name).

**Do not merge or cross-link two concepts just because they share a name or
surface similarity, unless a source page states the relationship explicitly.**
When two things collide on a name (this ontology currently has three unrelated
concepts all called "role," from three different products), document the
collision plainly in each record and in `reconciliation.md`, and leave them
separate. Inventing the relationship would be adding a fact, not extracting
one - if a later round's evidence resolves it, merge then, with the citation.

**But search the extraction layer, not just the registry, before refusing a merge -
a refusal is only as good as the set it searched.** An enum minted, correctly
compared against the registry, and correctly refused a merge with a
similarly-named promoted enum can still be blind to a third spelling of the same
values already sitting unpromoted in the corpus, because an unpromoted term
never shows up in `registry-digest.py`. A registry digest answers "what may I
declare as `promoted`?"; it is the wrong instrument for "has anyone named this
already?", which is `candidate-evidence.py --ns <prefix>` or a grep over
`extractions/`. This kind of well-argued refusal, overturned later by evidence
already on disk, has happened more than once.

**And when a fold *is* licensed, quote the sentence that licenses it.** An alias is a
claim about a **referent**, and the gate resolves aliases before checking an id -
which makes it the one field in the registry that can make two different things pass
as one, permanently and invisibly. `verify-registry-ids.py` catches an alias that
merely re-punctuates its target; nothing reaches the semantic case and nothing can.
What makes a fold reviewable by someone who wasn't in the room is quoting the two
near-identical defining sentences, one per product tree, side by side, in the
surviving record. Do that every time you fold - including the rare case of
deleting a promoted record outright because it turned out to duplicate another.

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
prefix is the convention, not an option** - a `docs-issues/<slug>` reference
from any registry record with no file behind it is a `verify-registry-ids.py`
failure. That fails in the worst direction: a promoted record says "see
`docs-issues/X` for the contradiction", a reader finds nothing, and concludes
the caveat was never real.

There is a third category, and rounds where the input is the *registry* rather
than a page produce mostly this one: a fact about **this registry** - a
namespace named as a closed axis but populated as a subject area, a predicate
whose declared range contradicts its uses, relation objects pointing at an
alias that will move. None of those is a docs-issue. `docs-issues/` is for
facts about Couchbase's documentation, and filing a registry defect there
misdirects whoever eventually triages the file. Registry defects belong in
`reconciliation.md` - measured, in the round's section, with the fix either
applied or explicitly queued in `README.md`'s next steps. Before filing any
docs-issue, open the page the finding is about - an extraction record's finding
field is evidence *about* a page, never a substitute for reading it; issues
filed without that check have not survived scrutiny.

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
hyphenated prose in backticks; that's the price of catching real misses, where a
"New `docs-issues/`" subsection named entries that were never actually filed,
because the script only checked two of the three hand-written artefact
families at the time. **A control's coverage is itself a claim** - when a round
writes a new kind of file, check that something checks it.

Run it *after* writing the round's section, not before, and then run it again if
you edit that section - a first pass can find real gaps and a second pass, once
the writeup is finished, can still find more, including a concept whose own
extraction record claimed it was "already promoted" when it wasn't. "Narrated as
promoted, never actually filed" is a recurring failure shape, which is why the
check exists at all rather than being left to care.

`recurrence.py --variants` clusters ids that are the same term spelled more than
one way, and every cluster needs a decision - **alias it or rewrite it**, per the
rule in `normalise-ids.py`'s docstring. Alias when the variant is a defensible
alternative name (a different namespace, a display label against an internal
name): that is additive and forward-only, and it converts any future reuse of the
old form into a gate denial rather than a silent duplicate. Rewrite the extraction
records, with `normalise-ids.py`, when the variant is not a legitimate name for
the thing anywhere (a dotted version id, a smashed-together verb form) - aliasing
a typo enshrines it as vocabulary. Then re-run `--variants`: the count must go down, and
each surviving cluster must be one you decided to leave.

Read the `0 files` rows. `--variants` seeds the registry in as a speller, so a
cluster whose *only used* form is the `NO FILE` one is pure false debt: the corpus
spells the term one way, uniformly, and the registry spells it another. That is the
worst case rather than the mildest, because every file using it is gate-denied and
sits in the backlog. It's also a case the check can only see once it clusters the
corpus against itself - a one-sided variant otherwise gives a cluster of size one
and gets skipped in silence, hiding real instances of the same defect.

Run this every round, not only when something looks wrong. The loud failure is a
promoted term reading as unpromoted debt; the quiet one is a genuine candidate
held *below* the promotion bar because its count is split across two spellings.
Note also what the clustering cannot see: it keys on typography, so it catches
`create-function` vs `createfunction` and never `Application Access` vs
`bucket_full_access`. Namespace variants need a separate local-name match.

Expect known-bad numbers from `verify-evidence.py` over the whole corpus (several
hundred unquotable or missing-evidence relations), nearly all in the earliest
rounds, written before the write-time gate existed. Scope it to the new batch to
get a clean signal, and don't "fix" a historical count by editing old records -
some early batches (from before the gate) need *re-extraction*, which is a
tracked next step, not a reconciliation task.

**"Scope it to the new batch" assumes the round has one, and a coherence wave does
not.** A round that takes the registry as input, rather than adding extraction
records, has a different risk: its promotions may be licensed by records written
in the very first extraction batches, long before current controls existed - one
of which can quote a sentence that is verbatim on a *different* page than the one
the relation names (the entire reason `evidence_source` exists), which costs a
recurrence when credited to the wrong page collapses two files into one. So on a
registry-input round the check that matters is on the reading path:

```bash
python3 linked-data/poc/candidate-evidence.py --ns <ns> --audit   # before promoting
```

`--audit` reduces the run to the ids with at least one quote that is not on the page
it cites. Run it over every id you are about to promote or fold. Reading a namespace
and checking that what you are reading is real are then one action, with no separate
step to forget - which matters because the write-time gate protects records *as they
are written*, and promotion reads records written long before it existed.

Two related things not to do. Don't re-run `hooks/gate-evidence.py` over old records
as an audit: a real early record replayed through it today can produce denials,
because `registry_status` describes the registry the record was written *against*,
and many promotions later `minted` can be false about ids the registry has since
acquired. **A control's verdict can expire.** And don't "correct" those records to
match today's registry - the declaration was true when it was made. `hooks/test-gate.py`
is the regression suite for the gate's non-evidence rules, and its fixtures are
synthetic for exactly this reason. When a round adds a rule that *withdraws* a
permission (e.g. retiring a prefix, so "reusing this id is allowed" flips to
wrong), change the assertion **and write the reasoning beside it**, because in a
diff an intentional flip is indistinguishable from a test loosened to make a
change pass.

**If you touch `recurrence.py`, decide separately what the metric ignores and what the
census ignores.** Excluding `seeAlso` from the concept-promotion metric is
correct, but doing it by editing a shared code path can silently exclude those
ids from every *report* this project produces too, including `--variants`, whose
only job is to enumerate spellings - hiding misspellings of promoted statements
for rounds at a time, and understating a shadow-prefix figure quoted in a
writeup. `scan()` returns `mentions`, `slots`, `labels` and `see_also_objects` as
separate tables so a caller has to state which question it is asking; keep it
that way. The general form is worth carrying into every number you write down:
**a figure inherits the instrument that produced it, and nothing in this
pipeline records which instrument that was** - so when a writeup quotes a count,
say which report produced it.

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
- **Session length is its own cost driver, independent of how much a round
  reads or how much it reconciles.** A conversation re-sends its entire prior
  history on every turn; a file on disk does not have to be read that way.
  Keep the coordinator's own reconciliation *work* in fresh, bounded sessions
  (step 0) and keep every read of `reconciliation.md`/`README.md` anchored
  and partial, no matter how natural it feels to "just read the file" once
  it's already open.
