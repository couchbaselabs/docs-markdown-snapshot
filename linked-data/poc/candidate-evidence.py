#!/usr/bin/env python3
"""Dump every mention of a candidate id, with its evidence, for coherence review.

    python3 linked-data/poc/candidate-evidence.py vector-index:reranking
    python3 linked-data/poc/candidate-evidence.py --ns vector-index      # whole namespace
    python3 linked-data/poc/candidate-evidence.py --ns search --brief    # one line each

Why this exists
---------------
`recurrence.py` answers "is this term real?" and is structurally unable to answer
"do this namespace's members answer the same question?" - the gap that kept 93
index concepts unpromoted in round 10 and that the round-13 backlog is full of.
Closing it means reading the evidence behind a candidate, and the aggregate tools
deliberately don't print evidence: recurrence is a count, and a count that also
dumped quotes would be unreadable at 3,500 relations.

So this is the eyeballing tool, scoped so that the eyeballing is cheap. Given an
id (or a whole namespace) it prints every place the corpus mentions it: which page,
in which relation slot, under which predicate, with the evidence quote that
licensed it. That is enough to decide the three questions a coherence pass asks and
recurrence cannot:

  - Is this the same thing as something already promoted under another name?
    (`vector-index:hyperscale-vector-index` at 6 files versus the promoted
    `index-type:hyperscale-vector` at 4 - two trees, one index type, no join.)
  - Is this a concept at all, or a page id in concept clothing? Ids minted from a
    filename (`n1ql:selectintro`, `search:run-searches`) recur perfectly well and
    denote a document, not a thing. Having only `seeAlso` relations is the tell,
    and is flagged below - but as a smell, not a verdict, and the **label** is
    what settles it. `search:customize-index` labels itself "Customize a Search
    Index with the Web Console", which is a page title; `index-type:covering-index`
    labels itself "Covering Index / Covered Query", which is a thing, and is
    `seeAlso`-only merely because its relations were all born as Markdown links.
    The first should never have been a concept; the second is a concept the corpus
    has so far only ever linked to.
  - Do these members share an axis? A namespace holding two index *types* and eight
    vector-search *tuning parameters* is two families sharing a prefix.

Deliberately not a gate and not a report with a threshold: it prints what the
corpus says and makes no judgement, because the judgement is the part that needs a
person. Reads `extractions/` only - the registry side is `registry-digest.py`.

Quotability, added in round 15
------------------------------
Every printed quote is checked against the page it cites, and an unquotable one is
marked `!! UNQUOTABLE`. `--audit` reduces the run to just the ids that have one.

This is here rather than in `verify-evidence.py` (which has always been able to
find these) because of *when* it gets run. The reconcile skill's verification step
says to scope `verify-evidence.py` to the round's new batch, and that instruction
silently assumes a round has a new batch. Round 14 was the first round whose input
was the registry rather than a corpus of pages: it added no extraction records, so
"verify the new batch" verified nothing, and it promoted 18 concepts out of records
written in the very first POC commit, before any gate existed. One of those
promotions - `vector-search:product-quantization tradesOffAgainst
vector-search:memory-footprint` - cites a sentence that is verbatim on a *different*
page in the same directory than the one the relation names, which is the whole reason
`evidence_source` exists; and the promoted record's `note` quoted a second sentence
with one word inserted. Both were copied from the extraction record in good faith,
and the first one cost a recurrence: credited to the page that carries it, the term's
two files collapse to one.

So the check belongs on the path a coherence pass actually walks. Reading a
namespace before deciding it is now the same action as checking that what you are
reading is real, and there is no separate step to forget. The gate protects records
as they are written; promotion reads records written long before it existed.
"""

import argparse
import collections
import glob
import importlib.util
import json
import os
import sys

POC = os.path.dirname(os.path.abspath(__file__))
EXTRACTIONS = os.path.join(POC, "extractions")
REPO = os.path.dirname(os.path.dirname(POC))
sys.path.insert(0, POC)
import recurrence as R  # noqa: E402

# verify-evidence.py is not an importable module name, and duplicating its
# normalisation would be worse than this: the two must agree on what "verbatim"
# means, or a quote passes one check and fails the other.
_spec = importlib.util.spec_from_file_location(
    "verify_evidence", os.path.join(POC, "verify-evidence.py"))
VE = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(VE)


def quotable(rec, r, cache):
    """None if this relation carries no quote to check, else True/False.

    None and False are different answers and must not be merged: a relation with
    no evidence at all is a pre-gate record, while a relation whose quote is not
    on the page it cites is a fabrication. Round 10 found both and they need
    different responses.
    """
    ev = VE.norm(r.get("evidence") or "")
    if not ev:
        return None
    src = r.get("evidence_source") or rec.get("source_path")
    if not src:
        return None
    text = VE.page_text(src, cache, REPO)
    if text is None:
        return None
    return ev in text


def gather(match):
    """{id: {"labels": Counter, "mentions": [...]}} for every id `match` accepts."""
    found = collections.defaultdict(lambda: {"labels": collections.Counter(),
                                             "mentions": [], "files": set()})
    pages = {}
    for fp in sorted(glob.glob(os.path.join(EXTRACTIONS, "**", "*.json"), recursive=True)):
        short = os.path.relpath(fp, EXTRACTIONS)
        try:
            d = json.load(open(fp))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        for c in d.get("concepts", []):
            cid = c.get("candidate_id")
            if isinstance(cid, str) and match(cid):
                e = found[R.canonical(cid)]
                e["files"].add(short)
                if c.get("label"):
                    e["labels"][c["label"]] += 1
                e["mentions"].append((short, "concepts[]", "",
                                      c.get("reused_or_minted", "") or c.get("registry_status", ""),
                                      None))
        for r in d.get("relations", []):
            if not any(isinstance(r.get(s), str) and match(r[s])
                       for s in ("subject", "object")):
                continue
            ok = quotable(d, r, pages)
            for slot in ("subject", "object"):
                v = r.get(slot)
                if isinstance(v, str) and match(v):
                    e = found[R.canonical(v)]
                    e["files"].add(short)
                    e["mentions"].append((
                        short, slot,
                        f"{r.get('subject')} -{r.get('predicate')}-> {r.get('object')}",
                        (r.get("evidence") or "(no evidence)").replace("\n", " "),
                        ok))
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="*", help="candidate ids, shorthand or IRI")
    ap.add_argument("--ns", help="dump every candidate in this namespace")
    ap.add_argument("--brief", action="store_true", help="one line per id, no evidence")
    ap.add_argument("--audit", action="store_true",
                    help="only ids with at least one unquotable quote; check a promotion set")
    ap.add_argument("--width", type=int, default=150, help="evidence truncation width")
    args = ap.parse_args()

    if args.ns:
        prefix = args.ns.rstrip(":") + ":"
        match = lambda i: R.canonical(i).startswith(prefix)  # noqa: E731
    elif args.ids:
        wanted = {R.canonical(i) for i in args.ids}
        match = lambda i: R.canonical(i) in wanted            # noqa: E731
    else:
        ap.error("give some ids or --ns")

    con, pred, aliases = R.registry()
    found = gather(match)
    if not found:
        print("nothing matched")
        return 1

    print("File counts below are every mention - concepts[] membership and "
          "seeAlso included - and are deliberately NOT the promotion metric, "
          "which excludes both. Use recurrence.py for that; a term is often "
          "4 here and 1 there.")

    shown, bad_total = 0, 0
    for cid in sorted(found, key=lambda c: (-len(found[c]["files"]), c)):
        e = found[cid]
        bad = [m for m in e["mentions"] if m[4] is False]
        bad_total += len(bad)
        if args.audit and not bad:
            continue
        shown += 1
        resolved = R.resolve(cid, aliases)
        if resolved in con or resolved in pred:
            state = "PROMOTED" + (f" as {resolved}" if resolved != cid else "")
        else:
            state = "unpromoted"
        labels = ", ".join(f"{l!r}×{n}" for l, n in e["labels"].most_common(3)) or "-"
        preds = collections.Counter(m[2].split(" -")[1].split("->")[0]
                                    for m in e["mentions"] if m[2])
        # An id mentioned only via seeAlso is a link target: a page, not a concept.
        only_see = preds and set(preds) == {"seeAlso"}
        print(f"\n{'=' * args.width}")
        print(f"{cid}   [{len(e['files'])} files, {state}]"
              + ("   << seeAlso-only: read the label, this may be a page"
                 if only_see else ""))
        print(f"  labels: {labels}")
        if preds:
            print(f"  predicates: {', '.join(f'{p}×{n}' for p, n in preds.most_common())}")
        if bad:
            print(f"  !! {len(bad)} of {len(e['mentions'])} mentions cite a quote that is "
                  f"NOT on the page they name")
        if args.brief:
            continue
        seen = set()
        for short, slot, triple, ev, ok in e["mentions"]:
            if (triple, ev) in seen:
                continue
            seen.add((triple, ev))
            print(f"  - {short}")
            if triple:
                print(f"      {triple}")
            print(f"      {'!! UNQUOTABLE  ' if ok is False else ''}{ev[:args.width]}")
    if args.audit:
        print(f"\n{shown} of {len(found)} matched ids have unquotable evidence "
              f"({bad_total} mentions). A quote that is not on its page cannot license "
              f"a promotion; re-read the page before promoting or folding.")
    else:
        print(f"\n{len(found)} ids matched, {bad_total} mentions unquotable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
