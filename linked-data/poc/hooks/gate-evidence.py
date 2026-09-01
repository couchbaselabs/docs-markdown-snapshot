#!/usr/bin/env python3
"""PreToolUse gate: refuse to write an extraction record whose evidence isn't
findable on the page it cites.

Wired up in `.claude/settings.json` as a `PreToolUse` hook matching `Write|Edit`.
Reads the tool call as JSON on stdin, exits 0 to allow, exits 2 to block (with
the reason on stderr, which Claude Code feeds back to the calling agent).

Why a hook and not just the audit script
----------------------------------------
`verify-evidence.py` finds fabricated evidence after the fact. This finds it
before the file exists, and - the reason it's worth the trouble - **it fires
inside subagents**. Round 10's fabricated record came from one of ~10 parallel
extraction subagents whose full reasoning nobody ever saw; what came back was a
300-word report. A PreToolUse hook is the only control in this pipeline that
sits inside that agent's own loop rather than downstream of its summary.

The checking logic lives in `verify-evidence.py` and is imported, not copied.
See that file's "Shared with the write-time gate" note for why.

What it checks
--------------
1. **Every relation's `evidence` is verbatim on its source page** (or on its
   `evidence_source`, for legitimate cross-page facts). Whitespace and smart
   quotes are normalised; wording is not.
2. **No record claims a concept is "promoted" unless it is.** Deliberately
   narrow: an extraction record reusing an id that only exists at the extraction
   layer is *correct and expected* - that's the two-layer design, and
   `sdk:durability` has been legitimately reused across rounds without ever
   being promoted. What is not allowed is asserting registry state that isn't
   there. Round 10 found a record reading `"reused - already promoted
   (candidate_id first seen in ...)"` for a concept with no registry file at all:
   every clause accurate except the two words that mattered. So the trigger is
   the word "promoted", not the word "reused".

What it does NOT check
----------------------
That the triple built from a quotable sentence is a *fair reading* of it. Round
10 found "quotable but mis-objected" records - verbatim evidence, wrong object -
which pass this gate and are still wrong. A green check is not a green record.

Failure mode to watch for at reconciliation
-------------------------------------------
This gate converts fabrication into omission. An agent blocked from inventing a
quote may just drop the relation rather than hunt for a real one, and nothing
here would show that. The countermeasure isn't in this script - it's the
relations-per-page comparison described in the `linked-data-reconcile` skill.
"""

import importlib.util
import json
import os
import sys

POC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # linked-data/poc
ROOT = os.path.dirname(os.path.dirname(POC))                        # repo root
GATED = os.path.join(POC, "extractions")


def load_verifier():
    """Import verify-evidence.py by path - its hyphen makes it un-importable by
    name, and renaming it would break the documented command line.

    `dont_write_bytecode` matters here: without it every single Write in the repo
    that reaches this point drops a `__pycache__/` directory into
    `linked-data/poc/`. A hook that litters the tree it guards gets switched off.
    """
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location(
        "verify_evidence", os.path.join(POC, "verify-evidence.py")
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def deny(reason):
    """Block the tool call. Exit 2 puts stderr in front of the calling agent.

    Chosen over the richer JSON `permissionDecision: "deny"` output on purpose:
    if a JSON field name is wrong the hook silently *allows*, and a gate that
    fails open is worse than no gate. Exit 2 fails closed.
    """
    print(reason, file=sys.stderr)
    sys.exit(2)


def main():
    payload = json.load(sys.stdin)
    tool = payload.get("tool_name", "")
    if tool not in ("Write", "Edit", "MultiEdit"):
        return 0

    tool_input = payload.get("tool_input", {})
    path = tool_input.get("file_path", "")
    if not path:
        return 0

    cwd = payload.get("cwd") or ROOT
    abspath = path if os.path.isabs(path) else os.path.abspath(os.path.join(cwd, path))

    # Cheap path test first: this hook is checked into a repo shared with people
    # who have nothing to do with the POC, so everything else must be free.
    if not abspath.startswith(GATED + os.sep):
        return 0

    if tool != "Write":
        deny(
            f"{tool} is not allowed on extraction records. Rewrite the whole "
            f"record with Write instead.\n\n"
            f"Reason: the evidence gate needs the complete document to parse it "
            f"as JSON, and an Edit only supplies a fragment. Records are small "
            f"and written once, so this costs nothing."
        )

    content = tool_input.get("content", "")
    try:
        rec = json.loads(content)
    except json.JSONDecodeError as e:
        deny(f"Not valid JSON, so it cannot be an extraction record: {e}")

    evidence_problems = load_verifier().check_record(rec, root=ROOT)
    registry_problems = []

    # Narrow registry check - see module docstring for why "promoted", not "reused".
    for c in rec.get("concepts", []) or []:
        note = (c.get("reused_or_minted") or "").lower()
        cid = c.get("candidate_id") or ""
        if "promoted" not in note or ":" not in cid:
            continue
        ns, slug = cid.split(":", 1)
        if not any(os.path.exists(os.path.join(POC, "concepts", ns, slug + ext))
                   for ext in (".json", ".jsonld")):
            registry_problems.append((
                cid,
                f'claims "promoted" but there is no concepts/{ns}/{slug}.json. '
                f"Either drop that claim (reusing an extraction-layer id is fine "
                f"and needs no registry file), or find the id the registry "
                f"really uses.",
            ))

    problems = evidence_problems + registry_problems
    if not problems:
        return 0

    lines = [
        f"BLOCKED: {len(problems)} problem(s) in {os.path.relpath(abspath, ROOT)}",
        "",
    ]
    lines += [f"  [{pred}] {msg}" for pred, msg in problems]

    # Only give the evidence advice when there's an evidence problem to advise
    # on. A wall of irrelevant remediation text teaches agents to skim it.
    if evidence_problems:
        lines += [
            "",
            "Every relation's `evidence` must be a sentence that is actually on "
            "the page, copied exactly. Re-read the source file and quote it "
            "verbatim.",
            "",
            "If the fact is true but genuinely not stated on this page, that is "
            "a legitimate case: quote the page that DOES state it and add "
            '`"evidence_source": "<that path>"` and `"evidence_provenance": '
            '"cross-page: ..."` to the relation.',
            "",
            "If you cannot find textual support either way, omit the relation "
            "and say so in a finding field. Do not reconstruct a plausible "
            "sentence.",
        ]
    deny("\n".join(lines))


if __name__ == "__main__":
    try:
        sys.exit(main() or 0)
    except SystemExit:
        raise
    except Exception as e:
        # Fail closed. A gate that lets writes through when it breaks is a gate
        # that a malformed record can walk past.
        print(f"evidence gate errored, refusing the write: {e!r}", file=sys.stderr)
        sys.exit(2)
