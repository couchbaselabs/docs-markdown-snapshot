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
quote may just drop the relation rather than hunt for a real one, and the record
it finally writes is clean. Two things catch that, neither of them an exit
status: `hooks/gate-log.jsonl` (see `log()` - a deny followed by an allow on the
same path with a lower `n_relations` is the fingerprint) and the
relations-per-page comparison described in the `linked-data-reconcile` skill.
"""

import datetime
import importlib.util
import json
import os
import re
import sys

POC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # linked-data/poc
ROOT = os.path.dirname(os.path.dirname(POC))                        # repo root
GATED = os.path.join(POC, "extractions")
LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gate-log.jsonl")


def log(outcome, payload, path, problems=(), rec=None):
    """Append one line per *gated* invocation - allows included, not just denials.

    Allows are logged on purpose. A subagent that gets blocked sees the reason on
    its own stderr; the coordinator does not. So without a log, the only account
    of a denial is the agent's end-of-run report - the same self-report channel
    that let round 10's fabrication through as a confident summary. Worse, an
    unlogged clean wave is indistinguishable from a wave where the hook never
    fired at all, which is the specific thing a gate test needs to rule out.
    Logging every verdict makes "9 records written, 9 invocations, 0 denials" a
    real finding instead of an absence of evidence.

    `n_relations` is what makes the gate's own worst failure mode visible. This
    gate converts fabrication into omission: a blocked agent can satisfy it by
    deleting the offending relation, and the resulting record is clean. But the
    retry is a second write to the same path, so the log shows
    `deny(n=13) -> allow(n=12)` - the agent dropped one rather than sourcing it -
    as against `deny(n=13) -> allow(n=13)`, where it went and found the quote.
    Reconciliation should grep for a deny followed by an allow on the same path
    with a lower count. That is a far sharper signal than the relations-per-page
    thinning heuristic, which can only compare a page against its cousins.

    Never allowed to block a write: a full disk or a read-only checkout is not a
    reason to refuse legitimate extraction, so failures here are swallowed.
    """
    try:
        with open(LOG, "a") as fh:
            fh.write(json.dumps({
                "ts": datetime.datetime.now().isoformat(timespec="seconds"),
                "outcome": outcome,
                "tool": payload.get("tool_name", ""),
                "session": payload.get("session_id", ""),
                "path": os.path.relpath(path, ROOT),
                "n_relations": len(rec.get("relations") or []) if rec else None,
                "problems": [list(p) for p in problems],
            }) + "\n")
    except Exception:
        pass


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


NEGATED = re.compile(r"\b(not|no|none|never|isn't|aren't|nor|without|lacks)\b")


def claim_clause(note):
    """The part of a `reused_or_minted` note that states *this* id's provenance.

    Everything up to the first clause break. A record's own provenance is always
    the leading clause ("reused - already promoted", "minted - coarse
    placeholder"); what follows is commentary, and commentary is where both of
    round 11's false positives lived:

      - "reused - extraction-layer id already on disk (...), no registry file.
         ... and none is promoted"      <- true statement, negated
      - "minted - coarse placeholder, following the same pattern the registry
         already uses for the promoted rbac-role:role"   <- about ANOTHER id

    Two agents hit these independently in one 9-page wave, so the naive substring
    test was wrong about roughly as often as it was right. Note that negation
    handling alone would have cleared only the first: the second is an accurate,
    unnegated statement about a different concept entirely, which is why the
    clause boundary - not the polarity - is the load-bearing part.

    This still catches what it was built for. Round 10's real offence read
    "reused - already promoted (candidate_id first seen in ...)", where the claim
    is in the leading clause, unnegated, and about itself.

    Deliberately does NOT split on " - ": the house style is
    "reused - already promoted", so the dash separates the verdict from its
    reason and the claim itself sits after it. Splitting there would discard the
    very words being tested.

    The residual weakness is honest: this is still a machine gate parsing English.
    A `registry_status` enum in the schema would remove the guesswork entirely,
    and is the right fix if this keeps costing agents retries.
    """
    return re.split(r"[,;(.]", (note or "").lower(), maxsplit=1)[0]


def deny(reason, payload=None, path=None, problems=(), rec=None):
    """Block the tool call. Exit 2 puts stderr in front of the calling agent.

    Chosen over the richer JSON `permissionDecision: "deny"` output on purpose:
    if a JSON field name is wrong the hook silently *allows*, and a gate that
    fails open is worse than no gate. Exit 2 fails closed.
    """
    if payload is not None and path is not None:
        log("deny", payload, path, problems, rec)
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
            f"and written once, so this costs nothing.",
            payload, abspath, [("*", f"{tool} refused on an extraction record")],
        )

    content = tool_input.get("content", "")
    try:
        rec = json.loads(content)
    except json.JSONDecodeError as e:
        deny(f"Not valid JSON, so it cannot be an extraction record: {e}",
             payload, abspath, [("*", f"invalid JSON: {e}")])

    evidence_problems = load_verifier().check_record(rec, root=ROOT)
    registry_problems = []

    # Narrow registry check - see module docstring for why "promoted", not "reused",
    # and why only the leading clause counts.
    for c in rec.get("concepts", []) or []:
        note = claim_clause(c.get("reused_or_minted"))
        cid = c.get("candidate_id") or ""
        if "promoted" not in note or ":" not in cid:
            continue
        if NEGATED.search(note) or note.lstrip().startswith("minted"):
            continue
        ns, slug = cid.split(":", 1)
        if not any(os.path.exists(os.path.join(POC, "concepts", ns, slug + ext))
                   for ext in (".json", ".jsonld")):
            registry_problems.append((
                cid,
                f'claims "promoted" but there is no concepts/{ns}/{slug}.json. '
                f"Either drop that claim (reusing an extraction-layer id is fine "
                f"and needs no registry file), or find the id the registry "
                f"really uses.\n      triggered on: {note.strip()!r}",
            ))

    problems = evidence_problems + registry_problems
    if not problems:
        log("allow", payload, abspath, rec=rec)
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
    deny("\n".join(lines), payload, abspath, problems, rec)


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
