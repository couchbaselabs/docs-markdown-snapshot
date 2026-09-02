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

Also checked, since round 14: **no alias may be a mere punctuation variant of its
own target.** `concepts/version/server-8-0.json` used to list `version:server-8.0`
as an alias, which is the alias-or-rewrite rule applied backwards. Aliasing a
punctuation variant is worse than leaving it broken, in a specific way: it makes
the 12 records using the dotted form pass the gate, which removes the only
pressure to fix them, and it hides the defect from `recurrence.py --variants`,
which resolves aliases *before* clustering and therefore reported no variant at
all. Two of the largest instances of the very drift round 13 set out to enumerate
were invisible for exactly this reason.

The test is mechanical and does not need a list of releases: strip every
non-alphanumeric character from the alias and from its target, and if what remains
is identical, the alias adds no name - only punctuation. That discriminates
correctly in both directions. `version:couchbase-server-7.6` differs from
`version:server-7-6` by a word as well as by dots, so it is a real alternative
name and passes (round 14 chose to rewrite it anyway, on a separate argument about
this namespace's local-name convention, but the check does not force that);
`role:manage-scope-functions` against `role:query-manage-functions` passes for the
same reason. A punctuation variant belongs in `normalise-ids.py`, where the fix is
applied to the records and the next mint of the bad form is denied.

And since round 16: **every `docs-issues/<slug>` a registry record points at must
have a file.** Two references written in earlier rounds pointed at slugs that were
never filed under that name, and nothing noticed for four rounds - see
`dangling_docs_issues` for why a broken caveat pointer is worse than a missing one.

Deliberately not checked here: whether an id is *well-formed* beyond matching its
path (that would be a naming-convention checker, a different and much more
opinionated job), and whether two records denote the same thing (that is
`recurrence.py --variants` plus human judgment).
"""

import glob
import json
import os
import re
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


def squash(name):
    """`version:server-8.0` and `version:server-8-0` both -> `versionserver80`."""
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def punctuation_aliases(data, own_id):
    """Aliases that differ from `own_id` only in punctuation. See the docstring."""
    al = data.get("aliases") or data.get("alias") or []
    al = [al] if isinstance(al, str) else al
    # The record's own shorthand, e.g. `.../concepts/version/server-8-0` ->
    # `version:server-8-0`, so an alias written in shorthand can be compared to it.
    short = own_id.replace(BASE + "concepts/", "").replace("/", ":")
    return [a for a in al
            if isinstance(a, str) and a.strip() and squash(a) == squash(short)]


DOCS_ISSUE_REF = re.compile(r"docs-issues/([a-z0-9][a-z0-9-]*)")


def dangling_docs_issues(data):
    """Slugs a record points at under `docs-issues/` that have no file. See below.

    Added in round 16, when writing six new issues turned up two references from
    earlier rounds pointing at files that do not exist - `docs-issues/dcp-name-drift`
    and `docs-issues/who-creates-analytics-indexes-contradiction`, both of which are
    filed with a `server-` prefix. Neither was ever a typo in the ordinary sense: the
    author wrote the issue's descriptive name and the directory's convention is
    `<product>-<name>`, so the reference was plausible, adjacent to a real file, and
    wrong. Nothing read it, so nothing complained, for four rounds.

    Worth checking because the reconcile skill asks for exactly this kind of
    cross-link ("Cross-link from the originating record's finding field to the new
    docs-issue id") and a broken one fails silently in the direction that matters
    most: a promoted record says "see docs-issues/X for the contradiction", a reader
    goes looking, finds nothing, and concludes the caveat was never real rather than
    that the pointer was wrong. This is the same failure shape as `verify-promotions.py`
    - narrated as existing, never actually filed - in the other direction.

    Scans the record's serialised text rather than named fields on purpose: these
    references live in free prose inside `note`, `recurrence_note`, `description` and
    at least four other keys, and enumerating the keys would just be a list to keep
    up to date. `extractions/` is not scanned - it is history, and rewriting a past
    record to fix a pointer is the thing this project refuses to do.
    """
    text = json.dumps(data)
    return sorted({m for m in DOCS_ISSUE_REF.findall(text)
                   if not os.path.exists(os.path.join(POC, "docs-issues", m + ".json"))})


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
        for a in punctuation_aliases(data, want):
            problems.append((short, f"alias {a!r} is a punctuation variant of "
                                    f"this record's own id",
                             "rewrite the records with normalise-ids.py instead"))
        for slug in dangling_docs_issues(data):
            problems.append((short, f"points at docs-issues/{slug}, which has no file",
                             "file the issue, or fix the reference "
                             "(the convention is <product>-<slug>)"))

    for short, got, want in problems:
        print(f"FAIL  {short}\n        declares: {got}\n        path says: {want}")
    print(f"\n{checked} registry records checked, {len(problems)} problems "
          f"(path/id mismatch, an alias that only re-punctuates the id, or a "
          f"dangling docs-issues/ reference)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
