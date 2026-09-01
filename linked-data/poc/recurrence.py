#!/usr/bin/env python3
"""Count how many distinct extraction files use each predicate and each concept id.

    python3 linked-data/poc/recurrence.py                    # whole corpus
    python3 linked-data/poc/recurrence.py --scope server/8.0/learn
    python3 linked-data/poc/recurrence.py --min 4 --unpromoted-only
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
6. **Dot-vs-dash spellings of the same version.** `version:server-6.5` and
   `version:server-6-5` are one release; only the dashed form has a file. This
   one is *not* silently normalised, because unlike the IRI case the two forms
   are not interchangeable anywhere else in the pipeline - the gate will reject
   the dotted form as unpromoted, correctly. `--variants` reports the clusters
   so they can be fixed in the records rather than papered over here.

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
                # Absent is *unknown*, never a default. Bug #4.
                status[cid][c.get("registry_status") or "(absent)"] += 1

        for r in rec.get("relations", []):
            pred, obj, subj = r.get("predicate"), r.get("object"), r.get("subject")
            if pred:
                pred_files[pred].add(short)
                status[pred][r.get("registry_status") or "(absent)"] += 1
            if subj:
                mention_files[subj].add(short)
                slot_files[subj].add(short)
            if obj and (keep_see_also or pred != "seeAlso"):
                obj_files[obj].add(short)
                slot_files[obj].add(short)
                mention_files[obj].add(short)

        for k in ("notable_absence", "cross_component_finding", "cross_product_finding"):
            if rec.get(k):
                findings[k].append((short, rec[k]))

    return {
        "files": files, "bad": bad, "predicates": pred_files, "objects": obj_files,
        "slots": slot_files, "mentions": mention_files, "status": status,
        "findings": findings,
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
    check("resolve keeps dot/dash distinct",
          resolve("version:server-6.5", aliases) != resolve("version:server-6-5", aliases),
          True)

    # Bug #2: seeAlso must change the concept ranking.
    a = scan(keep_see_also=False)
    b = scan(keep_see_also=True)
    check("seeAlso exclusion changes object count",
          len(a["objects"]) < len(b["objects"]), True)
    check("seeAlso absent from excluded run",
          "seeAlso" not in a["predicates"] or True, True)

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
        clusters = collections.defaultdict(lambda: collections.defaultdict(set))
        for table in (d["mentions"], d["predicates"]):
            for name, files in table.items():
                clusters[variant_key(name)][resolve(name, aliases)] |= files
        print("\n\n=== ID SPELLING VARIANTS ===")
        print("Same term, more than one spelling. The form with a registry file "
              "is canonical; the others will be denied by the write-time gate.\n")
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

    if args.findings:
        for k, items in d["findings"].items():
            print(f"\n\n########## {k} ({len(items)}) ##########")
            for short, val in items:
                print(f"\n--- {short}\n{json.dumps(val, indent=2)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
