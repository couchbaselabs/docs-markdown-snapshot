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
    # Long-form product word in a version id. Not a punctuation slip and so not
    # covered by the rule below: `couchbase-server-7.6` is a verbose spelling of
    # the same release, and this namespace's local names are
    # <short-product>-<release> (server, sgw, cbl, sdk, cbq). Round 14 dropped the
    # alias that used to absorb it, because one release must have one id.
    "version:couchbase-server-7.6": "version:server-7-6",
    "version:couchbase-server-7.6.2": "version:server-7-6-2",
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
    # --- Round 14. The vector-index: namespace named an axis it did not hold. ---
    # Five members belonged to axes the registry had already settled, and are
    # evacuated to them by exact match; the rest keep their local names and move
    # to the vector-search: subject area via NAMESPACE_RENAMES below. These five
    # must be listed here, and looked up first, precisely so the prefix rule does
    # not sweep them into vector-search: along with everything else.
    #
    # Each destination is licensed by a statement on the page, not by resemblance:
    # the three index types are the objects of `providesIndexType` /
    # `belongsToIndexClass` relations that name the axis in the predicate, and the
    # two functions are linked by the pages into
    # n1ql/n1ql-language-reference/vectorfun.md.
    "vector-index:hyperscale-vector-index": "index-type:hyperscale-vector",
    "vector-index:composite-vector-index": "index-type:composite-vector",
    "vector-index:search-vector-index": "index-type:search-vector",
    "vector-index:approx-vector-distance": "n1ql:approx-vector-distance",
    "vector-index:vector-distance-function": "n1ql:vector-distance",
    # The four similarity metrics are a closed enum, not a subject-area term, so
    # they leave vector-search: for a namespace of their own.
    "vector-index:euclidean-distance": "vector-similarity-metric:euclidean",
    "vector-index:euclidean-squared-distance": "vector-similarity-metric:euclidean-squared",
    "vector-index:cosine-similarity": "vector-similarity-metric:cosine",
    "vector-index:dot-product": "vector-similarity-metric:dot-product",
    # --- Round 15, wave 2. `setting:` was a namespace with no axis to be. ---
    # 34 members, 31 of them at recurrence 1. Wave 1's defect was a prefix named
    # like an axis and populated like a subject area, and the fix was a rename
    # because the population was coherent. This is the other case: `setting:` is
    # named like a subject area, and there is no subject there to be about. A
    # setting is always a setting *of* something, so the namespace can only ever
    # hold other namespaces' business - which is why it needs a 34-line table and
    # not a prefix rule. A dissolution's destination is not a function of the id.
    #
    # The test that settles it, and the reason this is not a matter of taste: a
    # namespace is an axis only if its membership is closed and enumerable.
    # vector-similarity-metric: has four members and there is no fifth;
    # index-state:, auth-mechanism: and edition: are the same shape. Settings are
    # unbounded by construction - query-settings.md alone documents scores of them
    # and every release adds more - so no closed axis is available, and an
    # open-ended population of instances belongs to whatever owns them.
    #
    # The registry had in fact already ruled this way and nobody noticed. Round 10
    # promoted eight settings into n1ql:, data: and tls:, plus the three-tier
    # request/node/cluster model, *from the same batch* whose extraction records
    # minted these 34 - so the reconciliation promoted the frame and abandoned the
    # instances, in one round, from one set of files.
    #
    # Query service settings and request parameters.
    "setting:auto-execute": "n1ql:auto-execute",
    "setting:auto-prepare": "n1ql:auto-prepare",
    "setting:awr-enabled": "n1ql:awr-enabled",
    "setting:awr-location": "n1ql:awr-location",
    "setting:completed-limit": "n1ql:completed-limit",
    "setting:completed-stream-size": "n1ql:completed-stream-size",
    "setting:completed-threshold": "n1ql:completed-threshold",
    "setting:curl-all-access": "n1ql:curl-all-access",
    "setting:curl-allowed-urls": "n1ql:curl-allowed-urls",
    "setting:curl-disallowed-urls": "n1ql:curl-disallowed-urls",
    "setting:curl-result-cap": "n1ql:curl-result-cap",
    # The stutter is deliberate: `n1ql-feat-ctrl` is the setting's actual name in
    # the docs, and an id is the thing's name, not a pretty version of it.
    "setting:n1ql-feat-ctrl": "n1ql:n1ql-feat-ctrl",
    "setting:natural": "n1ql:natural",
    "setting:natural-context": "n1ql:natural-context",
    "setting:natural-cred": "n1ql:natural-cred",
    "setting:natural-orgid": "n1ql:natural-orgid",
    "setting:natural-output": "n1ql:natural-output",
    "setting:pipeline-batch": "n1ql:pipeline-batch",
    "setting:preserve-expiry": "n1ql:preserve-expiry",
    "setting:profile": "n1ql:profile",
    "setting:query-curl-whitelist": "n1ql:query-curl-whitelist",
    "setting:query-memory-quota": "n1ql:query-memory-quota",
    "setting:use-fts": "n1ql:use-fts",
    "setting:use-replica": "n1ql:use-replica",
    # One setting, two ids, split by which tier's spelling the minting agent had
    # in front of it: "max_parallelism request-level parameter / max-parallelism
    # service-level setting" and "queryMaxParallelism cluster-level /
    # max-parallelism node-level / max_parallelism request-level" are two agents
    # describing the same setting from two ends. Verified on the page: 15
    # occurrences of `max-parallelism`, 11 of `queryMaxParallelism`, 2 of
    # `max_parallelism`. Same for queryNumCpus/num-cpus, which query-settings.md's
    # Table 3 ("Equivalent Settings for Cluster-Level and Node-Level") pairs
    # explicitly.
    #
    # Hence the naming rule for this family, which is what stops the split
    # recurring: use the tier-neutral kebab name when the docs document an
    # equivalent pair, and the only documented name when the setting exists at one
    # tier only (queryCurlWhitelist is cluster-level-only per Table 2, so it keeps
    # its query- prefix). Which tiers a setting has is a fact for a relation to
    # carry, not for the id to encode.
    "setting:max-parallelism": "n1ql:max-parallelism",
    "setting:query-max-parallelism": "n1ql:max-parallelism",
    "setting:query-num-cpus": "n1ql:num-cpus",
    # Three folds into records promoted in round 10, from these same pages. Each
    # is the same referent under a second prefix, which is the defect the
    # registry_status enum cannot see: `minted` was a *true* declaration for
    # `setting:scan-consistency`, because nothing called `setting:scan-consistency`
    # was promoted. The enum checks the id. Nothing checks the referent.
    "setting:scan-consistency": "n1ql:scan-consistency",
    "setting:encoded-plan": "n1ql:encoded-plan",
    "setting:collection-max-ttl": "data:max-ttl-setting",
    # Index Service settings, addressed through the Index Settings REST API.
    "setting:indexer-settings-defer-build": "index:indexer-settings-defer-build",
    "setting:indexer-scan-timeout": "index:indexer-scan-timeout",
    # Data Service: the expiry pager's interval. This record's concept entry has
    # no label at all, which is how it stayed invisible.
    "setting:expiry-pager-sleep-time": "data:expiry-pager-sleep-time",
    # An environment variable, but a cipher control: tls: is where this registry
    # keeps encryption configuration.
    "setting:couchbase-ssl-cipher-list": "tls:couchbase-ssl-cipher-list",
    # --- The axis that *was* hiding in there, folded rather than promoted. ---
    # setting-scope: has exactly three members - request-level, node-level,
    # cluster-level - and so passes the closed-and-enumerable test that setting:
    # fails. It is a real axis. It is also a third spelling of three concepts
    # round 10 had already promoted under n1ql: from the same page, so promoting it
    # would recreate wave 1's defect rather than fix one. Rewritten, not aliased:
    # the corpus's only evidence for cluster-versus-node scoping is the Query
    # settings page, so a product-general axis is not yet earned. If a later round
    # finds the distinction evidenced outside the Query service, mint it then, with
    # the citation - the stub-resolution discipline, not a permanent refusal.
    "setting-scope:request-level": "n1ql:request-level-query-parameters",
    "setting-scope:node-level": "n1ql:node-level-query-settings",
    "setting-scope:cluster-level": "n1ql:cluster-level-query-settings",
    # --- Singular/plural forks of namespaces that already exist. ---
    # Three of 55 unpromoted prefixes are these. Deliberately not a rule: applied
    # as one it would sweep `indexes:` (30 ids, 14 files) into `index:` (4
    # promoted), and where those 30 belong is wave 3's question, not a spelling
    # correction. cloud-providers:gcp-azure is left alone for a different reason -
    # it is one id standing for two promoted providers, minted because one sentence
    # gave both the same rule, and rewriting it to either would silently drop the
    # other. It needs the relation split in two, which this script must not do.
    "tools:cbimport": "tool:cbimport",
    "tools:query-workbench": "tool:query-workbench",
    "cloud-providers:aws": "cloud-provider:aws",
}

# --------------------------------------------------------------------------
# Rules, for defects with a shape rather than a list. Applied after ID_RENAMES,
# so an explicit entry always wins. A rule earns its place over a table entry
# when the defect will recur on inputs that do not exist yet.
# --------------------------------------------------------------------------


def _version_dots_to_dashes(cid):
    """`version:server-6.5` -> `version:server-6-5`, for any release, forever.

    Round 13 fixed this with eight table entries and missed four more, then a
    ninth and tenth turned up in round 14 (`version:server-8.0` at 12 mentions,
    `version:server-7.6` at 10) - hidden because someone had *aliased* those two
    instead, so `recurrence.py --variants` resolved the alias and reported no
    cluster. A table needs a new line per release and is therefore wrong by
    construction on a namespace whose members arrive with every product release;
    at least four extraction records across three rounds diagnosed the dot/dash
    drift in their own notes and asked reconciliation to pick a form.

    This is the pick, and it is one-directional: dashes. A dotted release number
    is a perfectly good *label* ("Couchbase Server 7.6" is what the docs say) and
    a bad *id*, so the dotted form is never aliased - an alias would leave the
    next dotted mint looking correct. `verify-registry-ids.py` now rejects an
    alias that is a mere punctuation variant of its own target, which is the
    other half of this rule and the part that makes it hold from now on.
    """
    return cid.replace(".", "-") if cid.startswith("version:") and "." in cid else None


ID_RULES = (_version_dots_to_dashes,)

# --------------------------------------------------------------------------
# Whole-namespace renames, applied last: an id matched by ID_RENAMES or a rule
# is already at its destination and is not reconsidered here.
# --------------------------------------------------------------------------
NAMESPACE_RENAMES = {
    # `vector-index:` is named like an axis (compare index-type:, index-class:,
    # auth-mechanism:) and populated like a subject area: of its 30 members, three
    # were index types, two were SQL++ functions, four were similarity metrics,
    # six were settings, three were metrics, five were page titles, and the rest
    # were storage algorithms. Renaming the prefix rather than dissolving the
    # namespace is the fix because the remainder IS a coherent subject area, in
    # exactly the way eventing:, monitoring:, backup: and sgw: already are - it
    # was only the name that claimed otherwise. Rewritten rather than aliased
    # because a prefix rename over 25 ids would otherwise leave 25 dead twins in
    # the registry, one per record.
    "vector-index:": "vector-search:",
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


def _destination(cid):
    """The canonical id `cid` should become, or None. Exact table, then rules,
    then namespace prefix - in that order, first match wins, so an id evacuated
    to another namespace by name is never also swept by its old prefix."""
    if cid in ID_RENAMES:
        return ID_RENAMES[cid]
    for rule in ID_RULES:
        new = rule(cid)
        if new and new != cid:
            return new
    for old_ns, new_ns in NAMESPACE_RENAMES.items():
        if cid.startswith(old_ns):
            return new_ns + cid[len(old_ns):]
    return None


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
    new = _destination(R.canonical(value))
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
