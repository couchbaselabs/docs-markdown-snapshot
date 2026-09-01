#!/usr/bin/env python3
"""Check that every relation's `evidence` really appears on the page it claims.

Run from the repo root, after each extraction wave and before committing:

    python3 linked-data/poc/verify-evidence.py                    # whole corpus
    python3 linked-data/poc/verify-evidence.py extractions/server/current

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


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else EXTRACTIONS
    if not os.path.isdir(root):
        sys.exit(f"not a directory: {root}")

    pages = {}          # source path -> normalised text, cached
    records = 0
    relations = 0
    cross_page = 0
    problems = []

    for fp in sorted(glob.glob(os.path.join(root, "**", "*.json"), recursive=True)):
        try:
            rec = json.load(open(fp))
        except json.JSONDecodeError as e:
            problems.append((fp, None, f"invalid JSON: {e}"))
            continue
        records += 1
        own_src = rec.get("source_path")

        for r in rec.get("relations", []):
            relations += 1
            src = r.get("evidence_source", own_src)
            if r.get("evidence_source"):
                cross_page += 1
            pred = r.get("predicate", "?")

            if not src:
                problems.append((fp, pred, "record has no source_path"))
                continue
            if src not in pages:
                if not os.path.exists(src):
                    pages[src] = None
                else:
                    pages[src] = norm(open(src, errors="ignore").read())
            if pages[src] is None:
                problems.append((fp, pred, f"source file not found: {src}"))
                continue

            ev = norm(r.get("evidence", ""))
            if not ev:
                problems.append((fp, pred, "empty evidence"))
            elif ev not in pages[src]:
                problems.append((fp, pred, f"not on {src}: {ev[:90]}"))

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
