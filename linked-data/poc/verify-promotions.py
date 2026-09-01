#!/usr/bin/env python3
"""Check that every concept and predicate `reconciliation.md` claims to promote
really has a registry file.

    python3 linked-data/poc/verify-promotions.py

Why this exists
---------------
"Narrated as promoted, never actually filed" is the project's most persistent
self-inflicted failure. It has happened four times: round 2's
`gatedByBillingPlan`, round 3's Java SDK concepts, round 5's `monitoring:*`
family - that one introduced by the same reconciler who had already written up
the first two as a known risk - and round 8's `cascadesDeletionTo` subject-slot
schema violation surviving its own reconciliation pass. Round 10's cumulative
verdict listed this check as one of two controls that "exist and neither is
written yet". This is that control.

What it does
------------
Scans `reconciliation.md` for anything shaped like a promoted term:

  * `ns:kebab-case-id`   -> expect concepts/<ns>/<id>.json(ld)
  * `camelCasePredicate` -> expect relations/<kebab-case>.json(ld)

and reports the ones with no file. It cannot tell "claimed as promoted" from
"mentioned as rejected, folded, deferred or watchlisted" - the prose says which,
the string does not - so every finding needs a human glance. That is the
intended cost: a short list to read each round beats rediscovering a missing
file three rounds later.

Exit status is always 0. This is a report, not a gate; `verify-evidence.py` is
the gate.
"""

import os
import re
import sys
import glob

POC = os.path.dirname(os.path.abspath(__file__))

# Namespaces that hold instance concepts. Anything matching ns:id where ns is
# not in here is almost certainly prose (a URL, a code sample, a system:
# keyspace) rather than a concept reference.
KNOWN_NS = None  # populated from the concepts/ tree itself


def kebab(camel):
    return re.sub(r"(?<!^)(?=[A-Z])", "-", camel).lower()


def main():
    global KNOWN_NS
    concepts = set()
    for p in glob.glob(os.path.join(POC, "concepts", "**", "*.json*"), recursive=True):
        rel = re.sub(r"\.json(ld)?$", "", os.path.relpath(p, os.path.join(POC, "concepts")))
        concepts.add(rel.replace("/", ":", 1) if "/" in rel else rel)
    KNOWN_NS = {c.split(":")[0] for c in concepts if ":" in c}

    predicates = {
        re.sub(r"\.json(ld)?$", "", os.path.basename(p))
        for p in glob.glob(os.path.join(POC, "relations", "*.json*"))
    }

    text = open(os.path.join(POC, "reconciliation.md"), errors="ignore").read()
    # Strip fenced code blocks: they hold sample JSON, not claims.
    text = re.sub(r"```.*?```", " ", text, flags=re.S)

    named_c = {
        m.group(0)
        for m in re.finditer(r"\b([a-z][a-z0-9]*(?:-[a-z0-9]+)*):([a-z0-9]+(?:-[a-z0-9.]+)*)\b", text)
        if m.group(1) in KNOWN_NS
    }
    named_p = set(re.findall(r"\b([a-z][a-z0-9]*(?:[A-Z][a-z0-9]*){1,})\b", text))

    missing_c = sorted(c for c in named_c if c not in concepts)
    missing_p = sorted(p for p in named_p if kebab(p) not in predicates)

    print(f"registry: {len(concepts)} concepts, {len(predicates)} relations")
    print(f"reconciliation.md names {len(named_c)} concept ids, {len(named_p)} camelCase terms\n")
    print(f"concept ids with no registry file ({len(missing_c)}):")
    for c in missing_c:
        print(f"  {c}")
    print(f"\ncamelCase terms with no relations/ file ({len(missing_p)}):")
    for p in missing_p:
        print(f"  {p}")
    print(
        "\nNot every line above is a defect: rejected, folded, deferred and "
        "watchlisted terms are named in the prose too, and camelCase catches "
        "ordinary identifiers. Read the list; don't diff it."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
