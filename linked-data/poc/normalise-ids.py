#!/usr/bin/env python3
"""Rewrite wrongly-spelled ids and mis-ranged predicates in the extraction records.

    python3 linked-data/poc/normalise-ids.py            # dry run - prints every change
    python3 linked-data/poc/normalise-ids.py --apply    # write them

Alias or rewrite? The rule this script encodes
----------------------------------------------
`recurrence.py --variants` reports ids that are the same term spelled more than
one way. There are two ways to resolve one, and picking the wrong one is how the
registry accumulates either false debt or false vocabulary:

**Alias it** (add the old id to the surviving record's `aliases`, leave the
extraction records alone) when the variant is a *defensible alternative name* -
a different namespace for the same thing (`enum:cluster-access-credential-type`
vs the top-level `cluster-access-credential-type`), or a display label where the
registry uses an internal name (`role:manage-scope-functions` vs
`role:query-manage-functions`). The old id denoted the right thing; only the
filing convention differs. Aliasing is additive, forward-only, and turns any
future reuse of the old form into a gate denial instead of a silent duplicate.
This is round 12's mechanism and it remains the default.

**Rewrite it** (this script) when the variant is *not a legitimate name for the
thing anywhere*: `version:server-6.5` is not how this project spells a release,
`n1ql:createfunction` is not how it spells a statement. Aliasing those would
enshrine a typo as vocabulary and quietly bless the next one. `recurrence.py`'s
docstring (bug #6) already committed to this direction - "fixed in the records
rather than papered over here" - and this script is what carries it out.

There is also a case aliasing *cannot* reach, and it is why this script exists at
all rather than the whole round being alias work. An alias maps one id to
another, so it can fix a wrong **concept**. It cannot fix a wrong **predicate**,
because the same predicate name is legitimately used by a different product for a
different thing: `requiresRole` is Sync Gateway's `requireRole()` sync-function
check, and 18 Server and Capella records use it to mean "requires a Server RBAC
role", which is `requiresServerRole`. Aliasing `requiresRole` would corrupt the
two records that use it correctly. Round 12 hit the concept half of exactly this
error, fixed it by aliasing, and therefore left the predicate half untouched -
minting `requiresServerRole` with a recurrence of 20 that counted the files which
*should* use it, against the zero that did.

Relation to the write-time gate
-------------------------------
`hooks/gate-evidence.py` fires on Write/Edit/MultiEdit and refuses `Edit` on
extraction records outright. This script writes with plain Python file I/O and so
**does not pass through the gate**. That is deliberate, and it is safe only
because of what it refuses to touch: it rewrites `subject`, `predicate`, `object`
and `candidate_id` and nothing else. It never touches `evidence`,
`evidence_source`, `page_id` or `source_path`, so evidence quotability is
preserved by construction - a rename cannot make a quote stop matching a page.

It also never touches `registry_status`. Pre-round-11 records have no such field
and nothing retrofits one; absent means *unknown* and a bulk rewrite is the last
place that should start guessing.

The compensating control is to run, after `--apply`:

    python3 linked-data/poc/verify-evidence.py     # the set as it now is on disk
    python3 linked-data/poc/recurrence.py --variants

The first is the check the extract skill already describes as "not the same claim"
as the gate's per-write check - which is precisely the claim needed here. The
second must come back with fewer clusters than it did before, and the clusters
that remain must be the ones this table deliberately leaves alone.

Idempotent: running it twice changes nothing the second time.
"""

import argparse
import collections
import glob
import json
import os
import sys

POC = os.path.dirname(os.path.abspath(__file__))
EXTRACTIONS = os.path.join(POC, "extractions")
sys.path.insert(0, POC)
import recurrence as R  # noqa: E402  - same directory, and the registry logic must not be duplicated

# --------------------------------------------------------------------------
# Concept-id rewrites. Left-hand side is not a legitimate name for the thing.
# --------------------------------------------------------------------------
ID_RENAMES = {
    # Dotted release numbers. This project spells a release with dashes
    # throughout; the dotted form has never had a registry file.
    "version:server-5.0": "version:server-5-0",
    "version:server-5.5": "version:server-5-5",
    "version:server-6.5": "version:server-6-5",
    "version:server-6.6": "version:server-6-6",
    "version:server-7.0": "version:server-7-0",
    # Round 13, second pass. These three were missed by the first pass because
    # `--variants` clustered the corpus against itself and no extraction record
    # used the dashed form, so each cluster had size one and was skipped - see
    # recurrence.py bug #8. They are the worst case of the dot/dash drift, not the
    # mildest: every file using them was denied by the gate.
    "version:sgw-3.0": "version:sgw-3-0",
    "version:sgw-2.x": "version:sgw-2-x",
    "version:cbl-3.3.0": "version:cbl-3-3-0",
    # Run-together statement names. Minted from the source *filename*
    # (createfunction.md) rather than the statement; every promoted sibling in
    # the n1ql: namespace is kebab-cased.
    "n1ql:createfunction": "n1ql:create-function",
    "n1ql:dropfunction": "n1ql:drop-function",
    "n1ql:updatestatistics": "n1ql:update-statistics",
    "n1ql:createsequence": "n1ql:create-sequence",
    "n1ql:explainfunction": "n1ql:explain-function",
    # Eventing handler names: the docs write onUpdate/onDelete, so the kebab
    # boundary falls after "on".
    "eventing:onupdate-handler": "eventing:on-update-handler",
    "eventing:ondelete-handler": "eventing:on-delete-handler",
}

# --------------------------------------------------------------------------
# Predicate rewrites, conditional on the object. `None` in the mapping means
# "rewrite only when the object resolves to a Server RBAC role id".
# --------------------------------------------------------------------------
PREDICATE_RENAMES = [
    # requiresRole is Sync Gateway's requireRole() sync-function check. Server
    # and Capella records using it to mean "holds a Server RBAC role" want
    # requiresServerRole. The two sync-gateway/ records that mean the SGW thing
    # have object sgw:role, which is not a role: id, so they are left alone.
    ("requiresRole", "requiresServerRole"),
    # Round 12's other half. requiresPrivilege stays correct for its ~16 genuine
    # privilege:capella-* objects; the objects that resolve to role: ids are the
    # eleven roles it re-filed, whose predicate it never updated.
    ("requiresPrivilege", "requiresServerRole"),
]

# Objects that look role-ish but must NOT trigger the predicate rewrite, with
# the reason. Each is a real open question, not an exclusion of convenience.
PREDICATE_RENAME_EXCLUDE = {
    "rbac-role-category:administrative": "a role *category*, not a role - requiresServerRole's range is a single role",
    "rbac-role-category:data": "as above",
    "rbac-role-category:query-and-index": "as above",
    "privilege:underlying-statement-privileges": "a meta-object standing for 'whatever the wrapped statement needs', not a named role",
}

ID_FIELDS = ("subject", "object")

IRI_CONCEPT_PREFIX = "https://docs.couchbase.com/ld/concepts/"


def rename(value):
    """Look up `value` in ID_RENAMES, matching either spelling form, or None.

    Records write ids two ways - the `ns:kebab` shorthand and the full IRI - and
    `recurrence.py` folds the two with `canonical()` before counting. A rename
    table keyed on the shorthand alone therefore misses every IRI-form
    occurrence, which is not a hypothetical: round 13's first pass left 12 dotted
    version IRIs behind and closed only 10 of 13 variant clusters.

    The replacement keeps the form the record used. Shorthand-vs-IRI is a
    separate axis from misspelling (`recurrence.py` bug #5, resolved by folding
    rather than rewriting), and quietly collapsing it here would make this script
    responsible for two normalisations while only documenting one.
    """
    if not isinstance(value, str):
        return None
    new = ID_RENAMES.get(R.canonical(value))
    if not new:
        return None
    if value.startswith(IRI_CONCEPT_PREFIX):
        return IRI_CONCEPT_PREFIX + new.replace(":", "/")
    return new


# Namespaces whose members are Server RBAC role names. `rbac-role:` belongs here
# as well as `role:` - it is a third spelling of the same catalogue, not a
# different thing (rbac-role:query-system-catalog is already an alias of
# role:query-system-catalog). `rbac-role-category:` deliberately does not belong,
# and is excluded above.
SERVER_ROLE_NAMESPACES = ("role:", "rbac-role:")


def resolved_is_server_role(obj, aliases):
    """True when `obj` is an assertion about a member of Server's role catalogue.

    Uses the live registry so that a role promoted earlier in this same round -
    with the old spelling recorded as an alias - is recognised here without the
    spelling needing to appear in ID_RENAMES too. That ordering is load-bearing:
    promote first, normalise second.

    Note this asks whether the page is *asserting a Server role requirement*, not
    whether the named role exists. Two records name roles absent from the
    56-member catalogue - `role:administrator` and `rbac-role:data-admin` - and
    both get the corrected predicate, because what the page means is unambiguous
    even though what it names is wrong. The wrongness is a documentation defect,
    tracked in docs-issues/, not a reason to leave a second defect in the
    predicate slot. Testing the namespace rather than registry membership is what
    makes those two behave the same way; an earlier version of this function
    tested `resolve(...).startswith("role:")` and fixed one of them while leaving
    the other, purely because their namespaces differed.
    """
    if obj in PREDICATE_RENAME_EXCLUDE:
        return False
    return R.resolve(obj, aliases).startswith(SERVER_ROLE_NAMESPACES)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write the changes (default is a dry run)")
    args = ap.parse_args()

    _, _, aliases = R.registry()
    files = sorted(glob.glob(os.path.join(EXTRACTIONS, "**", "*.json"), recursive=True))
    tally = collections.Counter()
    touched, skipped = [], []

    for fp in files:
        short = os.path.relpath(fp, EXTRACTIONS)
        try:
            raw = open(fp).read()
            rec = json.loads(raw)
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            skipped.append((short, str(e)))
            continue

        changes = []

        for c in rec.get("concepts", []):
            new = rename(c.get("candidate_id"))
            if new:
                changes.append(f"concept  {c['candidate_id']} -> {new}")
                tally[f"id: {c['candidate_id']} -> {new}"] += 1
                c["candidate_id"] = new

        for r in rec.get("relations", []):
            for field in ID_FIELDS:
                new = rename(r.get(field))
                if new:
                    changes.append(f"{field:8s} {r[field]} -> {new}")
                    tally[f"id: {r[field]} -> {new}"] += 1
                    r[field] = new
            for old_p, new_p in PREDICATE_RENAMES:
                if r.get("predicate") == old_p and resolved_is_server_role(r.get("object", ""), aliases):
                    changes.append(f"predicate {old_p} -> {new_p}   (object {r.get('object')})")
                    tally[f"predicate: {old_p} -> {new_p}"] += 1
                    r["predicate"] = new_p

        if not changes:
            continue
        touched.append((short, changes))
        if args.apply:
            with open(fp, "w") as fh:
                json.dump(rec, fh, indent=2, ensure_ascii=False)
                fh.write("\n")

    for short, changes in touched:
        print(f"\n{short}")
        for c in changes:
            print(f"    {c}")

    print("\n" + "=" * 72)
    for k, n in sorted(tally.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {n:4d}  {k}")
    print(f"\n{len(touched)} files {'rewritten' if args.apply else 'would change'}, "
          f"{sum(tally.values())} substitutions, {len(files)} scanned")
    if skipped:
        print(f"\n!! {len(skipped)} unreadable, left untouched:")
        for short, e in skipped:
            print(f"   {short}: {e}")
    if not args.apply:
        print("\nDry run. Re-run with --apply to write, then verify-evidence.py and "
              "recurrence.py --variants.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
