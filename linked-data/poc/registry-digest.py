#!/usr/bin/env python3
"""Print the current promoted registry as compact tables for extraction-agent prompts.

    python3 linked-data/poc/registry-digest.py

Why this exists as a script rather than a table pasted into each prompt: the
registry only grows, and the `linked-data-extract` skill records a real failure
from a stale one - `requiresMinVersionFor` was re-minted by a later round after
having been consolidated into `availableSince`, because that round's agents were
handed predicate *names* with no meanings or history. A digest computed at
dispatch time cannot be stale, and every agent running it gets the same answer.

It deliberately prints the `type`/description line in full rather than
truncating. That line is where a record says what it must NOT be confused with,
and those warnings are the entire reason a name-only table is dangerous. Notes
are truncated, except that any note carrying a collision warning is surfaced
verbatim in its own section - read that section before minting anything whose
name already appears in it.
"""

import glob
import json
import os
import re
import sys

POC = os.path.dirname(os.path.abspath(__file__))

# Phrases a reconciler reaches for when recording that two same-named things are
# not the same thing. Matched case-sensitively on "NOT" on purpose - the shouted
# form is the house style for exactly this warning.
COLLISION = re.compile(
    r"NOT |not to be confused|collision|collide|unrelated|distinct from|"
    r"different (thing|concept)|do not confuse|shares nothing",
)


def load(pattern):
    """Load every registry file, keyed by shorthand id, keeping ALL of a term's
    files rather than letting one win.

    A term promoted to full JSON-LD has two files, and neither is a superset of
    the other: `available-since.jsonld` carries `@type: rdf:Property` and a real
    class, while `available-since.json` carries the prose shape ("subject = X;
    object = Y; means Z") that an extraction agent actually needs. A
    newest-wins merge printed `availableSince | rdf:Property` and dropped the
    shape - reproducing, in the tool meant to prevent it, the exact stale-table
    failure that got `requiresMinVersionFor` re-minted. So: collect both, and let
    `field()` take the most informative answer across them.
    """
    out = {}
    for fp in sorted(glob.glob(os.path.join(POC, pattern, "**", "*.json*"), recursive=True)):
        if not fp.endswith((".json", ".jsonld")):
            continue
        try:
            data = json.load(open(fp))
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"  !! unreadable: {os.path.relpath(fp, POC)}: {e}", file=sys.stderr)
            continue
        rel = os.path.relpath(fp, os.path.join(POC, pattern))
        out.setdefault(os.path.splitext(rel)[0], []).append(data)
    return out


def field(docs, *names):
    """Longest non-empty value for any of `names`, across all of a term's files.

    Longest rather than first because the useful description and the bare class
    annotation live in different files and either may be found first; between
    "rdf:Property" and a sentence explaining the predicate's domain and range,
    the sentence is always the one worth printing.
    """
    best = ""
    for d in docs if isinstance(docs, list) else [docs]:
        for n in names:
            v = d.get(n) or d.get("@" + n)
            if isinstance(v, list):
                v = "; ".join(str(x) for x in v if x)
            if isinstance(v, dict):
                v = v.get("@value") or v.get("en") or ""
            if v:
                v = str(v).replace("\n", " ").strip()
                if len(v) > len(best):
                    best = v
    return best


def main():
    concepts = load("concepts")
    relations = load("relations")
    collisions = []

    print("# Promoted registry digest")
    print(f"\nGenerated fresh from disk: {len(concepts)} concepts, "
          f"{len(relations)} relations.")
    print("\nReuse a term from these tables when the underlying thing is genuinely "
          "the same. Mint a new one when nothing fits - that is expected, not a "
          "failure. What is not acceptable is minting a near-duplicate of "
          "something already here because you did not check.")

    for title, table, shape in (
        ("## Concepts (reuse as `namespace:kebab-case`)", concepts,
         "`id` | label | what it is"),
        ("## Relations (predicates - camelCase in records)", relations,
         "`predicate` | shape"),
    ):
        print(f"\n{title}\n\n{shape}\n" + "-" * len(shape))
        for key in sorted(table):
            d = table[key]
            if title.startswith("## Concepts"):  # noqa: SIM108
                name = key.replace(os.sep, ":")
            else:
                # relations/scan-consistency-of.json -> scanConsistencyOf
                parts = os.path.basename(key).split("-")
                name = parts[0] + "".join(p.title() for p in parts[1:])
            desc = field(d, "type", "description", "comment", "rdfs:comment")
            label = field(d, "label", "rdfs:label")
            rec = max((x.get("recurrence") or 0 for x in d), default=0)
            extra = f" [recurrence {rec}]" if rec else ""
            aliases = field(d, "aliases")
            extra += f" [aliases: {aliases}]" if aliases else ""
            print(f"`{name}` | {label} | {desc}{extra}")

            note = field(d, "note")
            if note and COLLISION.search(note):
                collisions.append((name, note))

    print("\n## Name collisions and near-misses already recorded\n")
    print("Each of these is a case where two same-named or similar-looking things "
          "were deliberately kept separate. If you are about to mint or reuse "
          "anything named here, read the entry first - and do not merge two of "
          "them on your own authority. Merging requires a source page that states "
          "the relationship; inventing it would be adding a fact, not extracting "
          "one.\n")
    for name, note in collisions:
        print(f"- **`{name}`**: {note}\n")

    print(f"\n({len(collisions)} of {len(concepts) + len(relations)} records carry "
          f"an explicit do-not-confuse warning.)")


if __name__ == "__main__":
    main()
