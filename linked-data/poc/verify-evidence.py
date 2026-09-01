#!/usr/bin/env python3
"""Check that every relation's `evidence` really appears on the page it claims.

Run from the repo root, after each extraction wave and before committing:

    python3 linked-data/poc/verify-evidence.py                    # whole corpus
    python3 linked-data/poc/verify-evidence.py linked-data/poc/extractions/server/8.0

Note that records are checked against `source_path` (a real path on disk, which
keeps the docs' `server/current/` alias) and never against `page_id` (an
ontology identifier, which names the release: `server/8.0/`). Those two fields
disagreeing is correct - see the "`current` is not a version" ruling in
`reconciliation.md`.

Why this exists
---------------
The extraction schema requires `evidence` to be a direct quote. Wave 1 of the
server/8.0 ingest showed that requirement is not self-enforcing: an extraction
agent produced a confident, well-argued, internally-consistent record asserting
`availableSince version:server-8-0` for a feature whose page states no version
at all, quoting a sentence that does not exist. Eleven of that record's thirteen
relations had unquotable evidence, and one had inverted polarity ("To disable
this feature" where the page reads "To enable the feature").

Reviewer judgement does not catch this. The fabricated quote was more plausible
than the real sentence, and the surrounding rationale was better argued than
most correct records. Only mechanical comparison against the source file catches
it, which is what this script does.

Note that this checks *quotability*, not correctness: it proves the sentence is
on the page, not that the triple built from it is a fair reading. It is a floor,
not a ceiling.

Cross-page evidence
-------------------
Some facts are true and load-bearing but unquotable from the page under
extraction - e.g. AWR is new in 8.0, which `query-awr.md` never says but
`introduction/whats-new.md` states outright. Those relations carry:

    "evidence_source": "server/current/introduction/whats-new.md",
    "evidence_provenance": "cross-page: ..."

and are checked against `evidence_source` instead. Anything without that field
is checked against the record's own `source_path`. Cross-page evidence is
legitimate; silently attributing an off-page quote to the page is not.

Shared with the write-time gate
-------------------------------
`hooks/gate-evidence.py` imports `norm()` and `check_record()` from here rather
than reimplementing them. That is deliberate: if the PreToolUse gate and this
corpus audit ever normalised quotes differently, records would pass at write
time and fail the audit, which is worse than having no gate - it teaches you to
distrust the audit. One implementation, two entry points.
"""

import json
import os
import re
import sys
import glob

EXTRACTIONS = "linked-data/poc/extractions"


def norm(s):
    """Whitespace- and quote-normalise, so formatting differences don't cause
    false alarms. Deliberately does NOT normalise wording."""
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def page_text(src, cache, root="."):
    """Normalised text of a source page, or None if it isn't on disk.

    `src` is repo-root-relative (that's what records store), so `root` lets a
    caller running from somewhere else - the hook - resolve it correctly.
    """
    if src not in cache:
        path = src if os.path.isabs(src) else os.path.join(root, src)
        cache[src] = norm(open(path, errors="ignore").read()) if os.path.exists(path) else None
    return cache[src]


def check_record(rec, cache=None, root="."):
    """Return [(predicate, message)] for every relation whose evidence can't be
    found on the page it claims. Empty list means the record passes.

    Note what this does NOT check: that the triple built from the quote is a
    fair reading. Round 10 found "quotable but mis-objected" records that pass
    here and are still wrong. A green check is not a green record.
    """
    if cache is None:
        cache = {}
    problems = []
    own_src = rec.get("source_path")

    for r in rec.get("relations", []):
        src = r.get("evidence_source", own_src)
        pred = r.get("predicate", "?")

        if not src:
            problems.append((pred, "record has no source_path"))
            continue
        text = page_text(src, cache, root)
        if text is None:
            problems.append((pred, f"source file not found: {src}"))
            continue

        ev = norm(r.get("evidence", ""))
        if not ev:
            problems.append((pred, "empty evidence"))
        elif ev not in text:
            problems.append((pred, f"not on {src}: {ev[:90]}"))

    return problems


def main():
    # Every path given, not just the first. This used to read argv[1] alone and
    # silently ignore the rest, so validating a multi-directory wave reported a
    # clean result for one directory and looked identical to a clean result for
    # all of them. A checker that under-reports its own coverage is worse than
    # one that fails, so the roots are explicit and the record count is the only
    # thing that reveals the difference.
    roots = sys.argv[1:] or [EXTRACTIONS]
    for root in roots:
        if not os.path.isdir(root):
            sys.exit(f"not a directory: {root}")

    pages = {}          # source path -> normalised text, cached
    records = 0
    relations = 0
    cross_page = 0
    problems = []

    targets = []
    for root in roots:
        targets += glob.glob(os.path.join(root, "**", "*.json"), recursive=True)

    for fp in sorted(set(targets)):
        try:
            rec = json.load(open(fp))
        except json.JSONDecodeError as e:
            problems.append((fp, None, f"invalid JSON: {e}"))
            continue
        records += 1
        relations += len(rec.get("relations", []))
        cross_page += sum(1 for r in rec.get("relations", []) if r.get("evidence_source"))

        problems += [(fp, pred, msg) for pred, msg in check_record(rec, pages)]

    for fp, pred, msg in problems:
        rel = fp.split("extractions/", 1)[-1]
        where = f"{rel} [{pred}]" if pred else rel
        print(f"FAIL  {where}\n      {msg}")

    print(
        f"\n{records} records, {relations} relations "
        f"({cross_page} cross-page), {len(problems)} problems"
    )
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
