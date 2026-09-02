#!/usr/bin/env python3
"""Find extracted pages that are one authored page published more than once.

    python3 linked-data/poc/shared-source.py              # clusters + affected ids
    python3 linked-data/poc/shared-source.py --clusters    # just the page clusters
    python3 linked-data/poc/shared-source.py --threshold 0.9
    python3 linked-data/poc/shared-source.py --selftest

Why this is a separate script and not a flag on `recurrence.py`
--------------------------------------------------------------
Round 16's bug #11 was that excluding a relation kind from a *metric* and
excluding it from the *census* are two different editorial decisions, and doing
the first by editing a shared code path silently did the second - 376 of 2,112
ids went invisible to every report at once. The discount this script computes is
exactly that shape of change: a claim that two data points should count as one.
So it is computed *here*, reported *here*, and applied by a human reading the
output. `recurrence.py` keeps counting distinct files, which is what it has
always honestly claimed to count.

What the problem actually is
----------------------------
The promotion rule is "two or more distinct files", and it is a proxy for two or
more independent attestations. The proxy holds as long as distinct files are
independently authored. In this corpus they routinely are not: Couchbase
publishes one Antora module on several branches and adapts it per product, so
`server/current/indexes/covering-indexes.md` and `cloud/indexes/covering-indexes.md`
are the same authored page, differing by frontmatter, an `editUrl`, some `xref:`
targets, and "Query Workbench" becoming "Query tab". Extract both and every term
on the page reports recurrence 2 without a second author ever having agreed to
anything. Add the 7.2 branch and it reports 3.

This is not hypothetical and it is not small: round 16 promoted terms out of
`indexes/` pages while three copies of that module sat in the corpus, and the
"adapted-copy drift" finding shape (see `docs-issues/`, three entries and
counting) is the same phenomenon observed from the other side - when the copies
disagree it is a documentation bug, and when they agree it is a fake data point.
The two readings are the same fact.

How a cluster is decided, and why the test is deliberately conservative
----------------------------------------------------------------------
Same basename, plus a line-level similarity at or above `--threshold` (default
0.75). Both conditions, because either alone is wrong in a way that matters:

- Similarity alone would cluster genuinely independent short pages. Two 20-line
  navigation stubs from unrelated products can hit 0.8 on boilerplate.
- Basename alone would cluster `server/current/indexes/index-scans.md` with any
  other `index-scans.md` however far it had diverged, and divergence is the
  interesting case: `storage-modes.md` differs by 100 of 130 lines between two
  trees, which is not one page published twice, it is a rewrite.

Requiring both means the script under-reports rather than over-reports, which is
the correct direction for a tool whose output *removes* evidence. A page pair it
misses keeps its recurrence, and the worst case is the status quo.

Frontmatter is stripped before comparing, blank lines are dropped, and lines are
stripped of surrounding whitespace. Nothing else is normalised - in particular
`xref:` targets and product names are left alone, so an adapted copy scores
*lower* than a verbatim one and a heavily-adapted copy falls out of its cluster
by itself. That is the intended behaviour, not a limitation to fix.

Clusters are labelled by what kind of duplication they are, and the script takes
no position on which kinds should be discounted:

- `cross-product` - the same module on two products (server + cloud). Almost
  certainly not independent attestation.
- `cross-version` - the same page on two release branches of one product. Also
  usually not independent, but a version pair is sometimes the *point* (a term
  attested in 7.2 and still attested in 8.0 is a real fact about both releases),
  so this is a judgment call and the script refuses to make it.
- `mixed` - both at once.

Known limits, stated because the last three rounds each found an instrument
mislabelled rather than a finding wrong
---------------------------------------------------------------------------
1. **Scope is the extracted corpus, not the documentation.** Only pages with an
   extraction record are compared, because only those can inflate a count. A
   never-extracted twin inflates nothing. This makes the script silent about the
   larger question of whether the corpus samples the docs well, which is a
   different finding (see `reconciliation.md`, "the corpus is not the
   documentation").
2. **A renamed twin is invisible.** `global-secondary-indexes.md` in 7.2 may be
   the ancestor of `indexing-overview.md` in 8.0; same basename is a syntactic
   test and will not see it.
3. **Similarity is measured on the page, attribution is claimed per id.** If two
   copies of a page are 90% identical, an id may still be attested only in the
   10% that differs - one publication genuinely saying something the other does
   not. The script reports the id as discountable anyway, so `--check` exists to
   settle it (below).

And one correction, recorded because this script's own first draft got it wrong
in the direction that flatters the corpus
-----------------------------------------------------------------------------
The draft told the reader to compare the two evidence quotes and said "if they
are different sentences, the recurrence is real." That is a mislabelled
instrument of exactly the kind the last three rounds kept finding. Different
quotes show the two *extractions* were independent of each other - which was
never in doubt, they were written by different agents who could not see each
other - and say nothing about whether the *sources* were. `query-awr.md` is the
worked example: the Server record quotes eight sentences and the Capella record
quotes two entirely different ones, and it is still one authored page published
twice, so `n1ql:automatic-workload-repository` has one source and not two.

What actually rescues a count is narrower and is what `--check` tests: **a quote
that is present on its own page and absent from every other member of the
cluster.** That means the sentence is in the adapted fraction rather than the
shared fraction, so a second author really did write it. Anything else is one
passage counted twice. The check uses `norm()` and `page_text()` imported from
`verify-evidence.py`, so "present on the page" means here exactly what it means
to the write-time gate; a second normaliser would let a quote be quotable to one
tool and not the other, which is the bug that import exists to prevent.
"""

import argparse
import collections
import difflib
import glob
import json
import os
import sys

import importlib.util

import recurrence       # same directory; imported for registry()/resolve() only


def _load(filename, modname):
    """Import a sibling script whose filename isn't a legal module name.

    `verify-evidence.py` has a hyphen, so it cannot be imported normally. Loading
    it by path keeps a single definition of "is this quote on the page" shared
    between the write-time gate, the corpus audit and this script - see the
    docstring's closing paragraph for why a second normaliser would be a bug.
    """
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    spec = importlib.util.spec_from_file_location(modname, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_ve = _load("verify-evidence.py", "verify_evidence")
norm, page_text = _ve.norm, _ve.page_text

POC = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(POC))
EXTRACTIONS = os.path.join(POC, "extractions")

DEFAULT_THRESHOLD = 0.75


def body_lines(path):
    """The page's content, frontmatter and blank lines removed. See the docstring."""
    try:
        raw = open(os.path.join(REPO, path), encoding="utf-8").read().splitlines()
    except (OSError, UnicodeDecodeError):
        return None
    if raw and raw[0].strip() == "---":
        for i in range(1, len(raw)):
            if raw[i].strip() == "---":
                raw = raw[i + 1:]
                break
    return [ln.strip() for ln in raw if ln.strip()]


def similarity(a, b):
    """Line-level ratio in [0, 1]. autojunk off: these files are long enough that
    difflib's popularity heuristic would silently discard real repeated lines."""
    return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()


def records():
    """Every extraction record, as (record_path, source_path, data)."""
    out = []
    for fp in sorted(glob.glob(os.path.join(EXTRACTIONS, "**", "*.json"), recursive=True)):
        try:
            data = json.load(open(fp))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(data, dict):
            continue
        src = data.get("source_path")
        if not isinstance(src, str) or not src.strip():
            # Pre-round-4 records predate the field. Deriving the path from the
            # record's own location would be a guess that reads as data, so the
            # record is reported as unpaired instead.
            src = None
        out.append((fp, src, data))
    return out


def product_of(path):
    return path.split("/", 1)[0] if path else ""


def version_of(path):
    """`server/current/indexes/x.md` -> `current`; `cloud/indexes/x.md` -> ''."""
    parts = path.split("/") if path else []
    if len(parts) > 2 and (parts[1][:1].isdigit() or parts[1] == "current"):
        return parts[1]
    return ""


def cluster_kind(paths):
    products = {product_of(p) for p in paths}
    versions = {(product_of(p), version_of(p)) for p in paths}
    cross_product = len(products) > 1
    cross_version = len(versions) > len(products)
    if cross_product and cross_version:
        return "mixed"
    return "cross-product" if cross_product else "cross-version"


def clusters(threshold):
    """Group extracted source pages into shared-source clusters."""
    by_basename = collections.defaultdict(list)
    for fp, src, _ in records():
        if src:
            by_basename[os.path.basename(src)].append(src)

    bodies, out = {}, []
    for basename, paths in sorted(by_basename.items()):
        paths = sorted(set(paths))
        if len(paths) < 2:
            continue
        for p in paths:
            if p not in bodies:
                bodies[p] = body_lines(p)
        live = [p for p in paths if bodies[p]]

        # Union-find over the pairs that clear the threshold. Transitive on
        # purpose: an 8.0 page similar to both 7.2 and cloud puts all three in
        # one cluster even if the 7.2/cloud pair alone would not clear it, which
        # is right, because there is still only one authored page underneath.
        parent = {p: p for p in live}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        scores = {}
        for i, a in enumerate(live):
            for b in live[i + 1:]:
                r = similarity(bodies[a], bodies[b])
                scores[(a, b)] = r
                if r >= threshold:
                    parent[find(a)] = find(b)

        groups = collections.defaultdict(list)
        for p in live:
            groups[find(p)].append(p)
        for members in groups.values():
            if len(members) < 2:
                continue
            members = sorted(members)
            pair_scores = sorted(
                (scores.get((a, b), scores.get((b, a))), a, b)
                for i, a in enumerate(members) for b in members[i + 1:]
            )
            out.append({
                "basename": basename,
                "members": members,
                "kind": cluster_kind(members),
                "min_similarity": pair_scores[0][0] if pair_scores else 1.0,
                "pairs": pair_scores,
            })
    return out


def ids_by_file(keep_see_also=False):
    """id (aliases resolved) -> set of source paths attesting it."""
    _, _, aliases = recurrence.registry()
    out = collections.defaultdict(set)
    for fp, src, data in records():
        key = src or os.path.relpath(fp, EXTRACTIONS)
        for c in data.get("concepts") or []:
            cid = c.get("candidate_id") if isinstance(c, dict) else None
            if cid:
                out[recurrence.resolve(cid, aliases)].add(key)
        for r in data.get("relations") or []:
            if not isinstance(r, dict):
                continue
            if not keep_see_also and r.get("predicate") == "seeAlso":
                continue
            for slot in ("subject", "object"):
                v = r.get(slot)
                if isinstance(v, str) and v.strip():
                    out[recurrence.resolve(v, aliases)].add(key)
            p = r.get("predicate")
            if isinstance(p, str) and p.strip():
                out[recurrence.resolve(p, aliases)].add(key)
    return out


def discounted(threshold, kinds):
    """Every id whose distinct-file count exceeds its distinct-cluster count."""
    member_of = {}
    for i, cl in enumerate(clusters(threshold)):
        if cl["kind"] not in kinds:
            continue
        for m in cl["members"]:
            member_of[m] = f"cluster-{i}:{cl['basename']}"

    rows = []
    for name, files in ids_by_file().items():
        groups = {member_of.get(f, f) for f in files}
        if len(groups) < len(files):
            rows.append((len(files), len(groups), name, sorted(files)))
    # Biggest drop first, then the ones that fall below the promotion bar.
    rows.sort(key=lambda r: (-(r[0] - r[1]), r[1], r[2]))
    return rows


def quotes_by_id(names):
    """id -> [(source_path, evidence quote), ...] for the ids in `names`."""
    _, _, aliases = recurrence.registry()
    want = set(names)
    out = collections.defaultdict(list)
    for _fp, src, data in records():
        if not src:
            continue
        for r in data.get("relations") or []:
            if not isinstance(r, dict):
                continue
            ev = r.get("evidence")
            if not isinstance(ev, str) or not ev.strip():
                continue
            # A relation carrying `evidence_source` is quoting a third page on
            # purpose, so its quote says nothing about this page's authorship and
            # must not be allowed to rescue a count.
            if r.get("evidence_source"):
                continue
            for slot in ("subject", "object", "predicate"):
                v = r.get(slot)
                if isinstance(v, str) and recurrence.resolve(v, aliases) in want:
                    out[recurrence.resolve(v, aliases)].append((src, ev))
    return out


def check_divergence(threshold, kinds):
    """For each discounted id, does any quote exist on only one cluster member?

    Returns rows of (verdict, files, independent, id, detail). `verdict` is:

      `divergent` - at least one attesting quote is absent from the other copies,
                    so a second author really wrote it and the count stands.
      `shared`    - every attesting quote appears on every copy in its cluster.
                    One authored passage, counted once per publication.
      `unchecked` - no usable quote (a concept named with no relation carrying it,
                    or evidence that is itself unquotable - the corpus still holds
                    443 such relations from before the gate). Reported as its own
                    verdict rather than folded into either answer, because a gap
                    that reads as data is the failure this project keeps finding.
    """
    cls = [c for c in clusters(threshold) if c["kind"] in kinds]
    member_of = {}
    for i, cl in enumerate(cls):
        for m in cl["members"]:
            member_of[m] = i

    rows = discounted(threshold, kinds)
    quotes = quotes_by_id([r[2] for r in rows])
    cache, out = {}, []

    for files, groups, name, paths in rows:
        divergent, checked = [], 0
        for src, ev in quotes.get(name, []):
            i = member_of.get(src)
            if i is None:
                continue
            siblings = [m for m in cls[i]["members"] if m != src]
            q = norm(ev)
            own = page_text(src, cache, root=REPO)
            if not own or q not in own:
                continue          # unquotable here; not evidence of anything
            checked += 1
            if all((page_text(s, cache, root=REPO) or "") and
                   q not in page_text(s, cache, root=REPO) for s in siblings):
                divergent.append((src, ev))
        if not checked:
            verdict, detail = "unchecked", "no quotable evidence on a clustered page"
        elif divergent:
            verdict = "divergent"
            detail = f"{len(divergent)}/{checked} quotes unique to their own copy"
        else:
            verdict = "shared"
            detail = f"all {checked} quotes appear on every copy"
        out.append((verdict, files, groups, name, detail))

    order = {"shared": 0, "unchecked": 1, "divergent": 2}
    out.sort(key=lambda r: (order[r[0]], -(r[1] - r[2]), r[3]))
    return out


def effective(verdict, files, groups):
    """The count a `--check` verdict licenses, and whether the bar is settled.

    Returns `(count, settled)`. This exists because the first `--check` report
    printed **BELOW THE BAR** whenever the *discounted* count fell under 2, no
    matter what the row's own verdict said - so `index:sequential-scan  2 -> 1
    divergent` was rendered as a refusal on the strength of a number the same
    line's verdict had just rejected. Round 17 was one step from refusing a
    candidate its own instrument had vindicated.

    That is bug #12's shape (see `recurrence.py`) appearing inside the tool built
    to detect it: deflation, quiet, in the direction of dropping real evidence.
    Worth stating why it is easy to write: the discount is the interesting
    computation, so the report was built around it, and `--check` was bolted on as
    an extra column rather than as the thing that decides which column counts.

    The three verdicts license three different answers, and only two of them are
    numbers:

    - `divergent` - a quote sits on its own copy and on no sibling, so a second
      author really wrote it. The discount does not apply: use `files`.
    - `shared` - every quotable sentence is on every copy, so this is one authored
      passage counted once per publication. The discount stands: use `groups`.
    - `unchecked` - no quotable evidence on a clustered page, so neither was
      established. Return the discounted count as the conservative figure but
      report `settled=False`, because an id here needs a reader, not a verdict.
      Never mark it below the bar: that would be a gap reading as data, which is
      the failure this project keeps finding.
    """
    if verdict == "divergent":
        return files, True
    if verdict == "shared":
        return groups, True
    return groups, False


def selftest():
    """Checks on the comparison itself, in the style of `recurrence.py --selftest`."""
    checks = []

    def ok(label, cond):
        checks.append((label, bool(cond)))

    a = ["one", "two", "three", "four"]
    ok("identical pages score 1.0", similarity(a, a) == 1.0)

    # `effective()`, i.e. bug #12 inside the bug #12 detector. The first four are
    # the real round-17 rows that exposed it.
    ok("divergent rejects the discount (index:sequential-scan 2 -> 1)",
       effective("divergent", 2, 1) == (2, True))
    ok("divergent at 2 files is therefore NOT below the bar",
       effective("divergent", 2, 1)[0] >= 2)
    ok("shared upholds the discount (index:duplicate-index 3 -> 1)",
       effective("shared", 3, 1) == (1, True))
    ok("shared at 1 independent source IS below the bar",
       effective("shared", 3, 1)[0] < 2)
    ok("unchecked is never settled", effective("unchecked", 4, 1)[1] is False)
    ok("unchecked still reports the conservative count",
       effective("unchecked", 4, 1)[0] == 1)
    ok("shared above the bar stays above it (array-index 7 -> 3)",
       effective("shared", 7, 3) == (3, True))
    ok("disjoint pages score 0.0", similarity(a, ["x", "y", "z"]) == 0.0)
    ok("one changed line of four stays above default threshold",
       similarity(a, ["one", "two", "three", "FOUR"]) >= DEFAULT_THRESHOLD)
    ok("half the page rewritten falls below default threshold",
       similarity(a, ["one", "two", "X", "Y"]) < DEFAULT_THRESHOLD)

    ok("product_of reads the first segment",
       product_of("server/current/indexes/a.md") == "server")
    ok("version_of reads a numeric release", version_of("server/7.2/x/a.md") == "7.2")
    ok("version_of reads the `current` alias",
       version_of("server/current/x/a.md") == "current")
    ok("version_of is empty for a version-less product",
       version_of("cloud/indexes/a.md") == "")
    ok("a two-segment path has no version", version_of("home/index.md") == "")

    ok("server+cloud is cross-product",
       cluster_kind(["server/current/i/a.md", "cloud/i/a.md"]) == "cross-product")
    ok("two server releases are cross-version",
       cluster_kind(["server/7.2/i/a.md", "server/current/i/a.md"]) == "cross-version")
    ok("both at once is mixed",
       cluster_kind(["server/7.2/i/a.md", "server/current/i/a.md",
                     "cloud/i/a.md"]) == "mixed")

    # The frontmatter strip is the whole reason a verbatim copy scores 1.0, so it
    # gets a check that does not depend on any file on disk.
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "f.md")
        open(p, "w").write("---\ntitle: X\neditUrl: y\n---\n\nreal line\n\nsecond\n")
        global REPO
        keep, REPO = REPO, d
        try:
            ok("frontmatter and blank lines are stripped",
               body_lines("f.md") == ["real line", "second"])
            open(p, "w").write("no frontmatter\n")
            ok("a page without frontmatter is unharmed",
               body_lines("f.md") == ["no frontmatter"])
            ok("a missing file returns None rather than an empty page",
               body_lines("nope.md") is None)
        finally:
            REPO = keep

    for label, passed in checks:
        print(f"  {'PASS' if passed else 'FAIL'}  {label}")
    bad = [l for l, p in checks if not p]
    print(f"\n{len(checks)} checks, {len(bad)} failed")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD)
    ap.add_argument("--clusters", action="store_true",
                    help="print the page clusters only, not the affected ids")
    ap.add_argument("--kind", action="append", default=None,
                    choices=["cross-product", "cross-version", "mixed"],
                    help="restrict the discount to these duplication kinds "
                         "(default: all three, and the choice is editorial)")
    ap.add_argument("--check", action="store_true",
                    help="for each discounted id, test whether any attesting "
                         "quote is unique to one copy (the only thing that "
                         "rescues a count - see the docstring)")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        return selftest()

    kinds = set(args.kind or ["cross-product", "cross-version", "mixed"])
    cls = clusters(args.threshold)

    print(f"== shared-source clusters (basename match, similarity >= "
          f"{args.threshold}) ==\n")
    by_kind = collections.Counter(c["kind"] for c in cls)
    for cl in cls:
        print(f"{cl['basename']}  [{cl['kind']}]  min similarity "
              f"{cl['min_similarity']:.2f}")
        for m in cl["members"]:
            print(f"    {m}")
    print(f"\n{len(cls)} clusters covering "
          f"{sum(len(c['members']) for c in cls)} extracted pages "
          f"({dict(by_kind)})")

    if args.clusters:
        return 0

    if args.check:
        rows = check_divergence(args.threshold, kinds)
        print(f"\n== quote-level check on the discounted ids "
              f"(kinds: {sorted(kinds)}) ==\n")
        print("  verdict     files -> independent  effective  id")
        below, unsettled = [], []
        for verdict, files, groups, name, detail in rows:
            # The marker must read the count this row's verdict licenses, never
            # the discounted count unconditionally. See `effective()`.
            eff, settled = effective(verdict, files, groups)
            mark = ""
            if not settled:
                mark = " **NEEDS A READER**"
                unsettled.append(name)
            elif eff < 2 <= files:
                mark = " **BELOW THE BAR**"
                below.append(name)
            print(f"  {verdict:<11s} {files:5d} -> {groups:<10d}  {eff:<9d}  "
                  f"{name}{mark}")
            print(f"                                 {detail}")
        tally = collections.Counter(r[0] for r in rows)
        print(f"\n{len(rows)} discounted ids: {dict(tally)}")
        print("`shared` means one authored passage counted once per publication - "
              "the discount stands, so `effective` is the discounted count. "
              "`divergent` means a second author really wrote it - the discount is "
              "rejected and `effective` is the raw file count. `unchecked` means "
              "neither was established; those are listed as needing a reader, not "
              "marked below the bar.")
        if below:
            print(f"\n{len(below)} id(s) fall below the bar once the discount is "
                  f"upheld: {', '.join(sorted(below))}")
        if unsettled:
            print(f"\n{len(unsettled)} id(s) unsettled: "
                  f"{', '.join(sorted(unsettled))}")
        return 0

    rows = discounted(args.threshold, kinds)
    print(f"\n== ids whose recurrence rests on a shared source "
          f"(kinds: {sorted(kinds)}) ==\n")
    print("  files -> independent    id")
    fell_below = 0
    for files, groups, name, paths in rows:
        mark = " **BELOW THE PROMOTION BAR**" if groups < 2 <= files else ""
        if mark:
            fell_below += 1
        print(f"  {files:5d} -> {groups:<11d}  {name}{mark}")
    print(f"\n{len(rows)} ids counted at least one duplicate page as a distinct "
          f"attestation; {fell_below} of them drop below 2 independent sources.")
    print("A list to check, not a verdict - run --check, which tests the one "
          "thing that rescues a count: a quote unique to a single copy.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
