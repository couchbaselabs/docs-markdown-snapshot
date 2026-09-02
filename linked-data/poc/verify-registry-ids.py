#!/usr/bin/env python3
"""Check that every registry record's `id` mirrors its own file path.

    python3 linked-data/poc/verify-registry-ids.py     # exits non-zero on any mismatch

The reconcile skill has always required this - "`id` (the real
`https://docs.couchbase.com/ld/...` IRI, mirroring the file's own path)" - and
nothing checked it, so nine records drifted.

Why a mismatch is not cosmetic
------------------------------
The pipeline derives a record's id from its **path** (`recurrence.py`'s
`concept_name()`), while extraction agents copy the id from the record's **`id`
field**, because that is the authoritative-looking string in front of them. When
the two disagree, both parties are behaving correctly and the result is still
broken: the tooling believes `version:server-6-5` is promoted, the agent writes
`version:server-6.5`, the write-time gate rejects it as unpromoted, and the term
lands in the unpromoted backlog with no indication that the registry caused it.

That is what happened. All nine drifted records were in `concepts/version/`,
where dotted release numbers read so naturally that the filing convention lost:
`concepts/version/server-6-5.json` declared its id as `.../version/server-6.5`.
Two extraction agents diagnosed it correctly in their own notes - one wrote "the
registry file's id field uses the dot form while the filename uses hyphens ...
reconciliation must pick one" - and were overruled by a reconciliation pass that
recorded the dotted spellings as *their* mistake to be normalised out of the
records. Round 13's variant sweep found the dotted ids still there and traced
them back to the registry.

So the failure mode this guards is specifically: **a wrong record teaching every
future agent to be wrong, while the agents' correctness registers as debt.**
There is no amount of care in an extraction prompt that survives an authoritative
file that disagrees with itself, which is the same argument that produced
`gate-evidence.py` - an invariant in a prompt is a hope, the same invariant in a
script is a control.

Deliberately not checked here: whether an id is *well-formed* beyond matching its
path (that would be a naming-convention checker, a different and much more
opinionated job), and whether two records denote the same thing (that is
`recurrence.py --variants` plus human judgment).
"""

import glob
import json
import os
import sys

POC = os.path.dirname(os.path.abspath(__file__))
BASE = "https://docs.couchbase.com/ld/"


# `pages/` is deliberately absent. A pages/*.jsonld record is public-facing
# structured data *about* a real documentation page, so its @id is correctly that
# page's docs.couchbase.com URL - an external resource this registry describes but
# does not own. Every other root holds terms the registry does own, whose id is
# its own address. Checking pages/ against its path reported all 8 of them as
# failures on this script's first run, which is a useful reminder that "the id
# must mirror the path" is a rule about ownership, not about strings.
CHECKED_ROOTS = ("concepts", "relations", "docs-issues")


def expected(fp):
    """The id a record at `fp` must declare, derived from its path alone."""
    stem = os.path.splitext(fp)[0]
    for root in CHECKED_ROOTS:
        rootdir = os.path.join(POC, root)
        if not stem.startswith(rootdir + os.sep):
            continue
        rel = os.path.relpath(stem, rootdir)
        # concepts/ nests by namespace; the others are flat, so only the basename
        # is meaningful and a nested path would itself be the anomaly.
        if root != "concepts":
            rel = os.path.basename(rel)
        return BASE + root + "/" + rel.replace(os.sep, "/")
    return None


def main():
    problems, checked = [], 0
    for fp in sorted(glob.glob(os.path.join(POC, "**", "*.json*"), recursive=True)):
        if not fp.endswith((".json", ".jsonld")):
            continue
        want = expected(fp)
        if want is None:          # a helper file, a log, context.jsonld
            continue
        short = os.path.relpath(fp, POC)
        try:
            data = json.load(open(fp))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            problems.append((short, f"unreadable: {e}", ""))
            continue
        if not isinstance(data, dict):
            continue
        checked += 1
        got = data.get("id") or data.get("@id")
        if got is None:
            problems.append((short, "(no id field)", want))
        elif got != want:
            problems.append((short, got, want))

    for short, got, want in problems:
        print(f"FAIL  {short}\n        declares: {got}\n        path says: {want}")
    print(f"\n{checked} registry records checked, {len(problems)} with a "
          f"path/id mismatch")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
