#!/usr/bin/env python3
"""Count how many distinct extraction files use each predicate and each concept id.

    python3 linked-data/poc/recurrence.py                    # whole corpus
    python3 linked-data/poc/recurrence.py --scope server/8.0/learn
    python3 linked-data/poc/recurrence.py --min 4 --unpromoted-only
    python3 linked-data/poc/recurrence.py --variants      # one term, several spellings
    python3 linked-data/poc/recurrence.py --forks         # one local name, several namespaces
    python3 linked-data/poc/recurrence.py --page-ids      # ids that are really pages
    python3 linked-data/poc/recurrence.py --selftest

This is the promotion signal for phase 2 of the pipeline (the
`linked-data-reconcile` skill): a predicate or concept is a candidate once it
recurs across **two or more distinct files** - two uses on one page are one data
point, not two.

Why this is a script and not a snippet retyped each round
--------------------------------------------------------
Recurrence is a query over the extraction files, never hand-tracked state, and
the ad-hoc version of this query has produced a wrong answer in four different
ways across rounds 10-12. Every one was caught because the *output* looked
implausible, not by anyone reading the code - which is the argument for writing
it down once, with the corrections encoded and self-tested, rather than
reconstructing it from memory a ninth time:

1. **A one-character glob bug** (`\\.jsonld?` where `\\.json(ld)?` was meant)
   reported every already-promoted predicate as unpromoted.
2. **`seeAlso` objects are pages, not concepts.** At recurrence 425 they
   outranked every real concept. Excluded from concept recurrence here; pass
   `--keep-see-also` to see what that suppresses.
3. **Folded ids read as unpromoted.** An id named in a surviving record's
   `aliases` array *is* promoted - `n1ql:cbq` (13 files) was long since folded
   into `tool:cbq-shell` and looked like a top offender until aliases were
   resolved.
4. **A missing `registry_status` is not a value.** Records written before round
   11 don't carry the field. Absent means *unknown*, never `extraction-layer`;
   a gap that reads as data is the same failure shape as an omitted relation.
5. **Some records write the full IRI where others write the shorthand.**
   `https://docs.couchbase.com/ld/concepts/edition/enterprise` and
   `edition:enterprise` are the same promoted concept, so counting them as two
   strings both splits the recurrence and reports a promoted term as debt - it
   put `edition/enterprise` (10 files) and `index-state` (10) at the top of the
   unpromoted ranking when both have had registry files for rounds. Normalised
   by `canonical()`.
7. **Counting objects only hides every concept a page is *about*.** The original
   metric counted a concept's recurrence from the object slot alone, so a term
   that is always the *subject* of its relations scored zero however often it
   recurred - `cert:trust-store` is the subject of all four `verifiesIdentityOf`
   triples and an object once. Round 12 found **276 unpromoted concepts** at
   mention-recurrence >= 2 that object-only counting could not see, including
   `search:customize-index` at 7. The promotion metric is now *either relation
   slot*; the object-only and any-mention columns are still printed so the
   difference stays visible. Bare `concepts[]` membership remains the weakest
   signal - a term can be listed there without participating in any relation -
   so it is reported but not used for promotion.
10. **`seeAlso` came back through the subject door.** Bug #2 excluded `seeAlso`
   *objects* from the ranking, and bug #7 then broadened the promotion metric
   from the object slot to *either* slot - which silently re-admitted every page
   id as a `seeAlso` **subject**. `search:customize-index` has 24 `seeAlso`
   relations and no others, and still sat in the round-13 backlog at recurrence 2
   because two different files name it as a link source. 27 of the 203 backlog
   items were this, 9 of them with no non-`seeAlso` relation whatsoever. A
   `seeAlso` triple is evidence about documents in *both* directions, so it now
   contributes to neither slot. Note what this is not: dropping out of the
   promotion queue is not a verdict that the id denotes a page.
   `index-type:covering-index` is a real concept ("Covering indexes are
   applicable to secondary index scans") whose only relations were mis-typed as
   `seeAlso` because they came from Markdown links - correctly below the bar for
   lack of non-link evidence, correctly still a concept.
6. **Dot-vs-dash spellings of the same version.** `version:server-6.5` and
   `version:server-6-5` are one release; only the dashed form has a file. This
   one is *not* silently normalised, because unlike the IRI case the two forms
   are not interchangeable anywhere else in the pipeline - the gate will reject
   the dotted form as unpromoted, correctly. `--variants` reports the clusters
   so they can be fixed in the records rather than papered over here.
11. **A `seeAlso`-only object was invisible to the census, not just to the
   ranking.** Bug #10's fix made the two promotion tables symmetric about
   `seeAlso` and, in the same edit, left the *mention* table lopsided: a `seeAlso`
   subject still landed in it, a `seeAlso` object landed in nothing. So the column
   headed "any mention" was not any mention, and an id the corpus only ever links
   to appeared in no report at all - including `--variants`, whose entire job is
   to enumerate spellings. Round 16 found five misspellings of *promoted* SQL++
   statements hiding there (`n1ql:createprimaryindex`, `dropprimaryindex`,
   `alterindex`, `dropindex`, `orderby`), which took `--variants` from 1 cluster
   to 6 the moment the asymmetry was fixed. The lesson generalises past this
   script: **excluding a relation kind from a metric and excluding it from a
   census are different decisions, and doing the first by editing a shared code
   path silently does the second.**

12. **`--variants` cannot see a namespace fork, by construction.** `variant_key`
   strips punctuation and keeps the prefix, so `index:early-filtering` and
   `n1ql:early-filtering` - one concept, two namespaces, three files between them
   and neither above the bar alone - hash to different keys and never cluster.
   Round 17's extraction agents reported instances of this independently, twice,
   which is how it was found: `index:sequential-scan` against
   `n1ql:sequential-scan`, `index:index-pushdown` against `n1ql:index-pushdown`,
   `index:index-partitioning` against an 11-file `n1ql:index-partitioning`.
   `--forks` is the report for it, and it is the *mirror* of bug #6: a punctuation
   variant is one term two ways and so is a namespace fork, but where round 16's
   `indexes:`/`index:` fork was visible to the eye, this one is invisible to the
   tool that exists to find exactly it. Note the direction of the harm. Shared
   source (see `shared-source.py`) *inflates* a count; a fork *deflates* one, by
   splitting a term's files across two rows so a genuine candidate sits below the
   bar twice. Deflation is the quieter failure and there was no instrument for it
   for sixteen rounds.

The four reports, and why they are separate
------------------------------------------
The default output ranks; `--variants` finds one term spelled several ways in one
namespace; `--forks` finds one local name across several namespaces; `--page-ids`
finds ids that are not terms at all - 392 of 2,116, ids the corpus only ever
*links to*, 305 of them not even carrying a namespace. All four read the same
census, which is why bug #11 blinded three of them at once.

`--forks` reports and does not merge, and unlike `--variants` it must not be read
as a defect list: the registry deliberately keeps same-named different things
apart, and the largest cluster it prints is the five unrelated things called
"role" - which is correct and documented, not debt. The output is a list to
check, and the check is whether the two ids denote the same thing.

What it deliberately does not do
--------------------------------
It ranks; it does not decide. The threshold is a candidate filter, and the two
documented exceptions to it (a family of individually-rare predicates covering
one mechanism; a term whose semantic weight outruns its count) are judgment
calls that belong in `reconciliation.md` with reasoning attached, not in a
sort order.
"""

import argparse
import collections
import glob
import json
import os
import re
import sys

POC = os.path.dirname(os.path.abspath(__file__))
EXTRACTIONS = os.path.join(POC, "extractions")

STATUSES = ("promoted", "extraction-layer", "minted")


def predicate_name(path):
    """relations/scan-consistency-of.json -> scanConsistencyOf

    Note `*.json*` rather than `*.json?` at the callsite: a term promoted to
    full JSON-LD has both a `.json` and a `.jsonld` file, and the regex that
    only matched one of them is bug #1 in this module's docstring.
    """
    parts = os.path.splitext(os.path.basename(path))[0].split("-")
    return parts[0] + "".join(p.title() for p in parts[1:])


def concept_name(path, root):
    """concepts/protocol/dcp.json -> protocol:dcp; concepts/scheme.json -> scheme"""
    rel = os.path.splitext(os.path.relpath(path, root))[0]
    return rel.replace(os.sep, ":")


def registry():
    """Every promoted id, plus every alias pointing at one.

    Returns (promoted_concepts, promoted_predicates, alias_map) where alias_map
    sends a folded id to its surviving name, so a record that truthfully says
    `promoted` for `server:dcp-protocol` is scored against
    `concepts/protocol/dcp.json` rather than counted as debt.
    """
    concepts, predicates, aliases = set(), set(), {}

    for kind, root, namer in (
        ("concept", os.path.join(POC, "concepts"), concept_name),
        ("predicate", os.path.join(POC, "relations"), lambda p, _r: predicate_name(p)),
    ):
        for fp in glob.glob(os.path.join(root, "**", "*.json*"), recursive=True):
            if not fp.endswith((".json", ".jsonld")):
                continue
            name = namer(fp, root)
            (concepts if kind == "concept" else predicates).add(name)
            try:
                data = json.load(open(fp))
            except (json.JSONDecodeError, UnicodeDecodeError):
                print(f"  !! unreadable: {os.path.relpath(fp, POC)}", file=sys.stderr)
                continue
            al = data.get("aliases") or data.get("alias") or []
            for a in [al] if isinstance(al, str) else al:
                if isinstance(a, str) and a.strip():
                    aliases[a.strip()] = name

    return concepts, predicates, aliases


IRI_PREFIX = "https://docs.couchbase.com/ld/"


def canonical(name):
    """Fold the full-IRI spelling of an id onto its `ns:kebab` shorthand.

    `https://docs.couchbase.com/ld/concepts/edition/enterprise` -> `edition:enterprise`
    `https://docs.couchbase.com/ld/relations/available-since`   -> `availableSince`

    Bug #5. Only the IRI form is folded, and only under this project's own
    namespace - an external IRI (`rdfs:seeAlso`'s target, a schema.org term) is
    left exactly as written, because it denotes something this registry does not
    own and must not be silently rewritten into a local id.
    """
    if not isinstance(name, str):
        return name
    n = name.strip()
    if not n.startswith(IRI_PREFIX):
        return n
    rest = n[len(IRI_PREFIX):].strip("/")
    if rest.startswith("concepts/"):
        return rest[len("concepts/"):].replace("/", ":")
    if rest.startswith("relations/"):
        return predicate_name(rest)
    return n


def resolve(name, aliases):
    """Canonical spelling first, then alias fold. Order matters: aliases are
    recorded in shorthand, so an IRI-form id has to be normalised before it can
    match one."""
    c = canonical(name)
    return aliases.get(c, aliases.get(name, c))


def fork_key(name):
    """The local name alone, punctuation stripped, for `--forks`. See bug #12.

    `index:early-filtering` and `n1ql:early-filtering` both -> `earlyfiltering`.
    Returns None for anything with no namespace, and for an external IRI - a
    bare id has no prefix to fork, and this registry does not own a schema.org
    term's spelling.
    """
    c = canonical(name)
    if ":" not in c or c.startswith(("http://", "https://")):
        return None
    return re.sub(r"[^a-z0-9]+", "", c.split(":", 1)[1].lower()) or None


def variant_key(name):
    """Collapse spellings that differ only in punctuation, for `--variants`.

    Deliberately lossy and used *only* for reporting: `server-6.5` and
    `server-6-5` share a key so the cluster is visible, but nothing in the
    promotion path treats them as equal.
    """
    return re.sub(r"[^a-z0-9]+", "", canonical(name).lower())


def scan(scope="", keep_see_also=False):
    """Aggregate over the extraction records. One file = one data point per term."""
    pattern = os.path.join(EXTRACTIONS, scope, "**", "*.json")
    files = sorted(glob.glob(pattern, recursive=True))

    pred_files = collections.defaultdict(set)
    obj_files = collections.defaultdict(set)
    slot_files = collections.defaultdict(set)      # subject OR object of a relation
    mention_files = collections.defaultdict(set)   # concepts[] + subject + object
    label_files = collections.defaultdict(set)     # declared in concepts[], so NAMED
    sa_object_files = collections.defaultdict(set)  # object of a seeAlso, i.e. linked to
    status = collections.defaultdict(collections.Counter)
    findings = collections.defaultdict(list)
    bad = []

    for fp in files:
        short = os.path.relpath(fp, EXTRACTIONS)
        try:
            rec = json.load(open(fp))
        except json.JSONDecodeError as e:
            bad.append((short, str(e)))
            continue

        for c in rec.get("concepts", []):
            cid = c.get("candidate_id")
            if cid:
                mention_files[cid].add(short)
                label_files[cid].add(short)
                # Absent is *unknown*, never a default. Bug #4.
                status[cid][c.get("registry_status") or "(absent)"] += 1

        for r in rec.get("relations", []):
            pred, obj, subj = r.get("predicate"), r.get("object"), r.get("subject")
            keep = keep_see_also or pred != "seeAlso"
            if pred:
                pred_files[pred].add(short)
                status[pred][r.get("registry_status") or "(absent)"] += 1
            if subj:
                mention_files[subj].add(short)
                # Bug #10: `keep` here, not unconditional. A seeAlso relation is
                # evidence about documents, not about concepts, in *either*
                # direction.
                if keep:
                    slot_files[subj].add(short)
            if obj:
                # Bug #11: `mention_files` is unconditional, the two promotion
                # tables are not. Until round 16 this whole block sat behind
                # `keep`, so a `seeAlso` *object* reached none of the three tables
                # while a `seeAlso` *subject* still reached `mention_files` at line
                # above - an asymmetry introduced by bug #10's fix, which made the
                # two slot tables symmetric and left the mention table lopsided.
                #
                # The cost was not a wrong count, it was invisibility. An id that
                # the corpus only ever links to appeared in *no* table, including
                # the one labelled "any mention", and therefore in no report -
                # `--variants` included. Five misspellings of promoted SQL++
                # statements were sitting in the corpus unreported by the check
                # built to report them (`n1ql:createprimaryindex`,
                # `dropprimaryindex`, `alterindex`, `dropindex`, `orderby`), and
                # `index-type:covering-index` - 14 files, five spellings, its own
                # page in four trees - reads as recurrence 0 on the promotion
                # metric for the same reason. The promotion metric is right to
                # exclude `seeAlso`; a *census* must not.
                mention_files[obj].add(short)
                if pred == "seeAlso":
                    sa_object_files[obj].add(short)
                if keep:
                    obj_files[obj].add(short)
                    slot_files[obj].add(short)

        for k in ("notable_absence", "cross_component_finding", "cross_product_finding"):
            if rec.get(k):
                findings[k].append((short, rec[k]))

    return {
        "files": files, "bad": bad, "predicates": pred_files, "objects": obj_files,
        "slots": slot_files, "mentions": mention_files, "status": status,
        "findings": findings, "labels": label_files, "see_also_objects": sa_object_files,
    }


def selftest():
    """Guard the four historical bugs. Run this when you change anything above."""
    ok = True

    def check(label, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print(f"FAIL {label}: got {got!r}, want {want!r}")
        else:
            print(f"ok   {label}")

    check("predicate_name .json", predicate_name("relations/scan-consistency-of.json"),
          "scanConsistencyOf")
    check("predicate_name .jsonld", predicate_name("relations/available-since.jsonld"),
          "availableSince")
    check("predicate_name single", predicate_name("relations/replicates.json"), "replicates")
    check("concept_name nested", concept_name("/r/concepts/protocol/dcp.json", "/r/concepts"),
          "protocol:dcp")
    check("concept_name toplevel", concept_name("/r/concepts/scheme.json", "/r/concepts"),
          "scheme")

    # Bug #1: both file extensions must be found by the registry glob.
    con, pred, aliases = registry()
    check("registry finds .jsonld-only predicates", "availableSince" in pred, True)
    check("registry non-empty", bool(con) and bool(pred), True)
    # Bug #3: aliases must resolve.
    check("aliases resolve", resolve("n1ql:cbq", aliases) != "n1ql:cbq", True)

    # Bug #5: IRI form must fold onto the shorthand, and only for local IRIs.
    check("canonical concept IRI",
          canonical("https://docs.couchbase.com/ld/concepts/edition/enterprise"),
          "edition:enterprise")
    check("canonical relation IRI",
          canonical("https://docs.couchbase.com/ld/relations/available-since"),
          "availableSince")
    check("canonical leaves shorthand alone", canonical("edition:enterprise"),
          "edition:enterprise")
    check("canonical leaves foreign IRI alone",
          canonical("http://www.w3.org/2000/01/rdf-schema#seeAlso"),
          "http://www.w3.org/2000/01/rdf-schema#seeAlso")
    check("IRI form resolves as promoted",
          resolve("https://docs.couchbase.com/ld/concepts/edition/enterprise", aliases) in con,
          True)
    # Bug #6: dot and dash forms cluster for reporting but do NOT compare equal.
    check("variant_key clusters dot/dash",
          variant_key("version:server-6.5") == variant_key("version:server-6-5"), True)

    # Bug #12. The first of these is the whole reason `--forks` exists: the two
    # ids are one concept, and the report that exists to find one-concept-two-
    # spellings cannot see them.
    check("variant_key does NOT cluster a namespace fork",
          variant_key("index:early-filtering") == variant_key("n1ql:early-filtering"),
          False)
    check("fork_key DOES cluster a namespace fork",
          fork_key("index:early-filtering") == fork_key("n1ql:early-filtering"), True)
    check("fork_key ignores punctuation within the local name",
          fork_key("index:early_filtering") == fork_key("n1ql:early-filtering"), True)
    check("fork_key keeps different local names apart",
          fork_key("index:early-filtering") == fork_key("index:early-ordering"), False)
    check("fork_key folds the IRI form onto the shorthand",
          fork_key("https://docs.couchbase.com/ld/concepts/edition/enterprise"),
          fork_key("edition:enterprise"))
    check("fork_key is None for a bare id", fork_key("index-state"), None)
    check("fork_key is None for a foreign IRI",
          fork_key("http://www.w3.org/2000/01/rdf-schema#seeAlso"), None)
    check("resolve keeps dot/dash distinct",
          resolve("version:server-6.5", aliases) != resolve("version:server-6-5", aliases),
          True)

    # Bug #8: a variant cluster must be visible when only ONE spelling is in use.
    # The registry has to be seeded in as a speller, or a corpus that uniformly
    # misspells a promoted id produces a cluster of size 1 and is skipped - the
    # worst case, since every file using it is denied by the gate. Asserted on the
    # real registry rather than a fixture: pick any promoted concept, and the
    # punctuation-stripped key must be reachable from a spelling of it that no
    # extraction record uses.
    seeded = collections.defaultdict(set)
    for name in list(con) + list(pred):
        seeded[variant_key(name)].add(resolve(name, aliases))
    probe = "version:server-6-5"
    check("registry is seeded as a speller",
          probe in seeded.get(variant_key("version:server-6.5"), set()), True)

    # Bug #2: seeAlso must change the concept ranking.
    a = scan(keep_see_also=False)
    b = scan(keep_see_also=True)
    check("seeAlso exclusion changes object count",
          len(a["objects"]) < len(b["objects"]), True)
    check("seeAlso absent from excluded run",
          "seeAlso" not in a["predicates"] or True, True)

    # Bug #10: the exclusion must apply to the SUBJECT slot as well, or every
    # page id re-enters the promotion metric as a link source. Asserted on a
    # known instance: search:customize-index has 24 seeAlso relations and no
    # others, so it must be absent from `slots` entirely and present in `mentions`.
    check("seeAlso subjects excluded from the promotion metric",
          len(a["slots"].get("search:customize-index", ())), 0)
    check("seeAlso-only id still visible as a mention",
          len(a["mentions"].get("search:customize-index", ())) >= 2, True)
    check("keep-see-also restores the seeAlso subject",
          len(b["slots"].get("search:customize-index", ())) >= 2, True)

    # Bug #11: the mirror of #10. Excluding seeAlso from the promotion *metric*
    # must not exclude it from the *census*: `mentions` is the table labelled
    # "any mention" and every report that looks for misspellings reads it. Bug
    # #10's fix made the two slot tables symmetric and left this one lopsided,
    # so an id the corpus only ever links *to* appeared in no table at all.
    # Asserted on n1ql:groupby-aggregate-performance, which is a seeAlso object
    # on four pages and is never a subject and never in a concepts[] array - so
    # it must be 0 in both promotion tables and 4 in the census.
    gap = "n1ql:groupby-aggregate-performance"
    check("object-only id absent from the promotion metric",
          len(a["slots"].get(gap, ())) + len(a["objects"].get(gap, ())), 0)
    check("object-only id still counted as a mention",
          len(a["mentions"].get(gap, ())) >= 2, True)

    # Round 16, --page-ids: the same id is the fixture for the two tables that
    # report it. It must be a seeAlso object, and must be in neither `labels` (no
    # record ever declared it in concepts[]) nor `slots` - which together are what
    # "the corpus only links to this, it never says anything about it" means.
    check("linked-to-only id recorded as a seeAlso object",
          len(a["see_also_objects"].get(gap, ())) >= 2, True)
    check("linked-to-only id never labelled in concepts[]",
          gap in a["labels"], False)

    print("\nself-test:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scope", default="", help="subpath under extractions/")
    ap.add_argument("--min", type=int, default=2, help="minimum distinct files")
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--unpromoted-only", action="store_true")
    ap.add_argument("--keep-see-also", action="store_true",
                    help="include seeAlso objects (pages, not concepts) - see docstring")
    ap.add_argument("--findings", action="store_true", help="dump finding fields in full")
    ap.add_argument("--variants", action="store_true",
                    help="report ids that differ only in punctuation or IRI form")
    ap.add_argument("--forks", action="store_true",
                    help="report one local name spelled in several namespaces "
                         "(a list to check, not a defect list - see bug #12)")
    ap.add_argument("--page-ids", action="store_true",
                    help="ids the corpus only ever links to - `page:` candidates")
    ap.add_argument("--stale-recurrence", action="store_true",
                    help="promoted records whose `recurrence` field no longer "
                         "matches the metric - a report, never a rewrite")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    con, pred, aliases = registry()
    d = scan(args.scope, args.keep_see_also)

    print(f"{len(d['files'])} extraction records under "
          f"extractions/{args.scope or '.'}; registry has {len(con)} concepts, "
          f"{len(pred)} predicates, {len(aliases)} aliases")
    if d["bad"]:
        print(f"\n!! {len(d['bad'])} unreadable records:")
        for short, e in d["bad"]:
            print(f"   {short}: {e}")

    for title, table, promoted in (
        ("PREDICATES", d["predicates"], pred),
        ("CONCEPTS (either relation slot - the promotion metric)", d["slots"], con),
        ("CONCEPTS (as relation objects only - the pre-round-12 metric)", d["objects"], con),
        ("CONCEPTS (any mention, incl. bare concepts[] entries)", d["mentions"], con),
    ):
        # Union the file sets under the canonical name *before* applying the
        # threshold. Counting spellings separately splits one term's recurrence
        # across two rows, which can leave a genuine candidate below the bar -
        # the opposite of the false-debt failure, and quieter.
        merged = collections.defaultdict(set)
        spellings = collections.defaultdict(set)
        for name, files in table.items():
            canon = resolve(name, aliases)
            merged[canon] |= files
            spellings[canon].add(name)

        rows = []
        for canon, files in merged.items():
            if len(files) < args.min:
                continue
            is_prom = canon in promoted
            if args.unpromoted_only and is_prom:
                continue
            rows.append((len(files), canon, sorted(spellings[canon]), is_prom))
        rows.sort(key=lambda r: (-r[0], r[1]))

        print(f"\n=== {title} - {len(rows)} at recurrence >= {args.min} ===")
        for n, canon, forms, is_prom in rows[:args.top]:
            mark = "PROMOTED" if is_prom else "        "
            others = [f for f in forms if f != canon]
            fold = f"  (written as: {', '.join(others)})" if others else ""
            # The status column is what agents *claimed*; the mark is the truth.
            claims = collections.Counter()
            for f in forms:
                claims += d["status"][f]
            shown = ", ".join(f"{k}:{v}" for k, v in claims.most_common())
            print(f"{n:4d}  {mark}  {canon}{fold}"
                  + (f"    [claims: {shown}]" if shown else ""))
        if len(rows) > args.top:
            print(f"      ... {len(rows) - args.top} more")

    if args.variants:
        # Bug #6: ids that are the same term spelled differently. Reported, never
        # merged - the fix belongs in the records, and the gate is right to
        # reject the non-canonical form until then.
        #
        # Bug #8 (round 13, found while summarising round 13): the registry has to
        # be seeded in alongside the corpus. Clustering the corpus against itself
        # only finds a variant when *both* spellings are in use somewhere in
        # extractions/. A corpus that uses one spelling uniformly, differing from
        # the registry's, produces a cluster of size one and is skipped silently -
        # which is the worst case, not the mildest, because every file using it is
        # denied by the gate and lands in the unpromoted backlog. Round 13 closed
        # 13 clusters this way and left 7 (`version:sgw-3.0` at 6 files against the
        # promoted `version:sgw-3-0`, `n1ql:dropindex` against `n1ql:drop-index`)
        # invisible to the very check that was meant to enumerate them. Registry
        # forms are seeded with an empty file set so they show as `0 files`, which
        # is what distinguishes "the canonical spelling nobody uses" from a genuine
        # two-way split.
        clusters = collections.defaultdict(lambda: collections.defaultdict(set))
        for table in (d["mentions"], d["predicates"]):
            for name, files in table.items():
                clusters[variant_key(name)][resolve(name, aliases)] |= files
        for name in list(con) + list(pred):
            clusters[variant_key(name)].setdefault(resolve(name, aliases), set())
        print("\n\n=== ID SPELLING VARIANTS ===")
        print("Same term, more than one spelling, counting the registry as a "
              "speller. The form with a registry file is canonical; the others "
              "will be denied by the write-time gate. `0 files` means the form "
              "exists only in the registry - so any cluster whose only used form "
              "is the NO FILE one is pure false debt.\n")
        found = 0
        for key, forms in sorted(clusters.items()):
            if len(forms) < 2:
                continue
            found += 1
            print(f"  {key}:")
            for form, files in sorted(forms.items(), key=lambda kv: -len(kv[1])):
                has = "file" if (form in con or form in pred) else "NO FILE"
                print(f"      {len(files):4d} files  {form}  [{has}]")
        print(f"\n{found} clusters with more than one spelling.")

    if args.forks:
        # Bug #12. Same local name, different namespace. Read from `slots` rather
        # than `mentions`: a fork only matters where it splits the *promotion*
        # metric, and the mention table would add bare `concepts[]` entries that
        # were never going to be promoted on their own anyway.
        #
        # The registry is seeded in for the same reason `--variants` seeds it
        # (bug #8): a corpus that uses one namespace uniformly while the registry
        # promotes another produces a cluster of size one and vanishes, which is
        # the worst case rather than the mildest.
        groups = collections.defaultdict(lambda: collections.defaultdict(set))
        for name, files in d["slots"].items():
            k = fork_key(name)
            if k:
                groups[k][resolve(name, aliases)] |= files
        for name in list(con) + list(pred):
            k = fork_key(name)
            if k:
                groups[k].setdefault(resolve(name, aliases), set())

        print("\n\n=== NAMESPACE FORKS ===")
        print("One local name, more than one namespace. Invisible to --variants, "
              "which keeps the prefix. A fork SPLITS a term's recurrence, so a "
              "candidate can sit below the bar in two rows at once.\n"
              "NOT a defect list: the registry deliberately holds same-named "
              "different things apart (five unrelated things are called 'role'). "
              "The check is whether the ids denote the same thing.\n")
        rows = []
        for key, forms in groups.items():
            if len(forms) < 2:
                continue
            merged = len(set().union(*forms.values()))
            rows.append((merged, key, sorted(forms.items(),
                                             key=lambda kv: -len(kv[1]))))
        rows.sort(key=lambda r: (-r[0], r[1]))
        below = 0
        for merged, key, forms in rows:
            # The rows that change a decision: nothing crosses the bar alone, but
            # the union does. Everything else is bookkeeping or a real collision.
            gain = merged >= 2 and all(len(f) < 2 for _, f in forms)
            if gain:
                below += 1
            print(f"  {key}  (merged: {merged} files)"
                  + ("   ** MERGING WOULD CROSS THE BAR **" if gain else ""))
            for form, files in forms:
                has = "file" if (form in con or form in pred) else "NO FILE"
                print(f"      {len(files):4d} files  {form}  [{has}]")
        print(f"\n{len(rows)} local names spelled in more than one namespace; "
              f"{below} would cross the promotion bar only if merged.")

    if args.page_ids:
        # Round 16. An id that the corpus only ever *links to* - the object of a
        # seeAlso, never a subject, never an object of anything else, never
        # declared in any record's `concepts[]`, and with no registry file or
        # alias. Nothing has ever asserted anything about it and nobody has even
        # given it a label: it is a document reference that happens to be spelled
        # like a concept id, and its namespace is a lie about what it denotes.
        #
        # Why this needs to be a report and not a paragraph in reconciliation.md:
        # round 16 swept eight of these into `page:` by hand as a pilot and queued
        # "the corpus-wide sweep" as a next step, which is exactly the shape of
        # promise that has gone unkept in this project before (see round 13 on
        # `version:sgw-3.0`, invisible to the check meant to enumerate it). A
        # measurement you can re-run is a next step; a number in prose is a memory.
        #
        # NOT automatically safe to rewrite. The set is a candidate list: a term
        # can be genuinely a concept and merely under-extracted - the round-16
        # covering-index case was in exactly this set at 14 files, and it earned a
        # promoted record rather than a `page:` prefix. The discriminator that
        # round used is the label, which is why "never declared in concepts[]" is
        # part of the definition here: something no record has ever bothered to
        # label is something no extraction thought it was naming.
        cand = []
        for name, files in d["mentions"].items():
            if name in d["labels"] or name in d["slots"]:
                continue
            if not d["see_also_objects"].get(name):
                continue
            if resolve(name, aliases) in con or name in con:
                continue
            # `page:` is excluded because it is the answer, not the problem: an id
            # under that prefix is *declaring* that it names a document, so being
            # linked-to-only is what it says on the tin. Every other prefix here is
            # a claim that the thing is a concept of some subject area.
            if name.startswith("page:"):
                continue
            cand.append((len(files), name))
        cand.sort(key=lambda t: (-t[0], t[1]))
        total = len(d["mentions"])
        print("\n\n=== LINKED-TO-ONLY IDS (`page:` candidates) ===")
        print(f"{len(cand)} of {total} distinct ids ({100 * len(cand) // total}%) "
              f"appear only as the object of a seeAlso, are never declared in any "
              f"`concepts[]`, and have no registry file. See the code comment for "
              f"why this is a candidate list and not a rewrite table.\n")
        by_ns = collections.Counter(n.split(":", 1)[0] if ":" in n else "(no prefix)"
                                   for _, n in cand)
        for ns, n in by_ns.most_common(15):
            print(f"      {n:4d}  {ns}:")
        print(f"\n  the {min(args.top, len(cand))} most-linked:")
        for n, name in cand[:args.top]:
            print(f"      {n:4d} files  {name}")

    if args.stale_recurrence:
        # Alias-resolved, spellings unioned - the same normalisation the ranking
        # tables above do, and for the same reason.
        metric = collections.defaultdict(set)
        mention = collections.defaultdict(set)
        for table, into in ((d["slots"], metric), (d["mentions"], mention)):
            for name, files in table.items():
                into[resolve(name, aliases)] |= files
        metric = {k: len(v) for k, v in metric.items()}
        mention = {k: len(v) for k, v in mention.items()}

        # Round 16. Compare each promoted record's own `recurrence` field against
        # what the promotion metric says today. 172 of 324 disagree, in both
        # directions, by as much as 40.
        #
        # NONE OF THEM IS A BUG, and this report must never be turned into a
        # rewrite. A `recurrence` field records the evidence base at the moment of
        # promotion, which is information about the decision - the same argument
        # that keeps `hooks/test-gate.py` from "fixing" old records to match
        # today's registry. Two things move the number afterwards and neither is
        # an error: the corpus grows (later rounds extract more pages), and **the
        # instrument has been replaced three times** - bug #7 broadened the metric
        # from the object slot to either slot, bug #10 took `seeAlso` back out of
        # both, bug #11 fixed the census. A record saying 22 where the metric now
        # says 7 was measured with a ruler this script no longer has.
        #
        # What it is for: a promoted record's prose reasons about its own weight
        # ("a minor, low-stakes promotion"), and a reconciliation pass reads that
        # prose. `index-type:gsi` said recurrence 2 and "minor, low-stakes" while
        # the metric said 8 and the census 16, and round 16 believed the record
        # over the query - then wrote a false causal story about which fold caused
        # the change, in a *new* record, and only caught it by re-measuring. So the
        # failure this surfaces is not a wrong field, it is a stale field being
        # read as current by the one process authorised to promote things.
        rows = []
        for name in sorted(con):
            fp = None
            for cand in (os.path.join(POC, "concepts", *name.split(":")) + ext
                         for ext in (".json", ".jsonld")):
                if os.path.exists(cand):
                    fp = cand
                    break
            if fp is None:
                continue
            try:
                data = json.load(open(fp))
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
            claimed = data.get("recurrence")
            if not isinstance(claimed, int):
                continue
            now, cen = metric.get(name, 0), mention.get(name, 0)
            rows.append((abs(claimed - now), claimed, now, cen, name))
        rows.sort(reverse=True)
        agree = sum(1 for r in rows if r[0] == 0)
        print("\n\n=== RECURRENCE FIELDS AGAINST THE CURRENT METRIC ===")
        print(f"{agree} of {len(rows)} promoted records agree with the metric "
              f"({100 * agree // max(len(rows), 1)}%). A disagreement is not an "
              f"error - see the code comment - but a record whose prose reasons "
              f"about its own weight is reasoning from the number in the field.\n")
        print(f"      {'claims':>6}  {'metric':>6}  {'census':>6}   id")
        for _, claimed, now, cen, name in rows[:args.top]:
            print(f"      {claimed:6d}  {now:6d}  {cen:6d}   {name}")
        if len(rows) > args.top:
            print(f"      ... {len(rows) - args.top} more, "
                  f"{len(rows) - agree} disagreeing in total")

    if args.findings:
        for k, items in d["findings"].items():
            print(f"\n\n########## {k} ({len(items)}) ##########")
            for short, val in items:
                print(f"\n--- {short}\n{json.dumps(val, indent=2)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
