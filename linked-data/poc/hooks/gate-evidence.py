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
2. **Every concept and predicate declares its registry state as an enum, and the
   declaration is true.** `registry_status` must be one of `promoted`,
   `extraction-layer` or `minted`, and it is checked against the registry
   (aliases included). Three things are refused: claiming `promoted` when no
   registry file exists (round 10's offence - a record read `"reused - already
   promoted (candidate_id first seen in ...)"` for a concept with no file at all,
   every clause accurate except the two words that mattered); claiming `minted`
   for something the registry already promotes, which is the re-minting failure
   that produced `requiresMinVersionFor` after it had been folded into
   `availableSince`; and claiming `extraction-layer` for a promoted term, which
   means the registry was not checked.

   Note what is *not* refused: reusing an id that only exists at the extraction
   layer. That is correct and expected - it's the two-layer design, and
   `sdk:durability` has been legitimately reused across rounds without ever being
   promoted. `extraction-layer` is a first-class answer, not a confession.

   Why an enum and not the prose: until round 11 this check parsed the English of
   `reused_or_minted`, and produced three false positives in nine pages - a
   truthful negative ("and none is promoted") and a true statement about a
   *different* id ("the same pattern as the promoted rbac-role:role"). Each fix
   was one unpredicted sentence shape away from the next false positive. An enum
   removes the guesswork entirely, so the ~40 lines of clause-splitting and
   negation-detection that used to live here are gone. The prose note stays in the
   schema, because it tells a reviewer things an enum cannot - the gate simply
   doesn't read it any more.

   Applies to predicates as well as concepts, and arguably matters more there:
   the canonical re-minting failure in this project's history was a predicate,
   not a concept. Reported once per distinct predicate rather than once per
   relation, so one wrong declaration doesn't produce twenty identical lines.

   Records written before round 11 have no `registry_status` at all. That is
   fine and deliberate: this is a write-time gate, so it only ever sees new
   records, and nothing rewrites the 552 already on disk. Anything reading the
   corpus must treat a missing field as *unknown*, never as `extraction-layer` -
   a gap that reads as data is the same failure shape as an omitted relation.

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
import glob
import importlib.util
import json
import os
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


VALID_STATUS = ("promoted", "extraction-layer", "minted")


def kebab_to_camel(name):
    """`serves-service` -> `servesService`, matching how predicates are written in
    records versus filed in `relations/`."""
    parts = name.split("-")
    return parts[0] + "".join(p.title() for p in parts[1:])


def registry_index():
    """Every id the registry promotes, mapped to the file that promotes it -
    **including aliases**.

    Alias-awareness is not a nicety here, it is what stops this check
    manufacturing the false positives the enum was introduced to remove. 24 ids
    across 14 registry files are promoted under a *different* name than the one
    extraction records use: `server:dcp-protocol` is promoted as
    `protocol:dcp`, `n1ql:cbq` as `tool:cbq-shell`, `streamsMutationsVia` as
    `usesProtocol`, `version:server-8.0` as `version:server-8-0`. Every one of
    those is legitimately `promoted`, and a naive file-exists test would deny all
    of them.

    Reads both `.json` and `.jsonld`, because a term promoted to full JSON-LD has
    two files and either may be the one carrying `aliases`.
    """
    idx = {}
    for kind in ("concepts", "relations"):
        base = os.path.join(POC, kind)
        for fp in sorted(glob.glob(os.path.join(base, "**", "*.json*"), recursive=True)):
            if not fp.endswith((".json", ".jsonld")):
                continue
            stem = os.path.splitext(os.path.relpath(fp, base))[0]
            canonical = (stem.replace(os.sep, ":") if kind == "concepts"
                         else kebab_to_camel(os.path.basename(stem)))
            idx.setdefault(canonical, fp)
            try:
                aliases = json.load(open(fp)).get("aliases") or []
            except Exception:
                continue
            for a in aliases:
                idx.setdefault(a, fp)
    return idx


def check_status(term_id, status, idx, what):
    """Validate one `registry_status` declaration. Returns a problem, or None.

    Fails closed on a missing or unrecognised value rather than skipping it: an
    unchecked declaration is indistinguishable from a false one, and this gate
    exists because "nothing checked" was the state of the world for nine rounds.
    """
    if not status:
        return (term_id, (
            f'missing "registry_status". Every {what} needs one, as an exact '
            f'string: "promoted" (a registry file exists in concepts/ or '
            f'relations/), "extraction-layer" (reused from an earlier extraction '
            f'record but never promoted - a normal, expected answer), or '
            f'"minted" (new here). Run `python3 linked-data/poc/registry-digest.py` '
            f"if you are unsure which applies - it prints what is promoted right now."
        ))
    if status not in VALID_STATUS:
        return (term_id, (
            f'"registry_status": {status!r} is not one of '
            f"{' | '.join(VALID_STATUS)}. Exact strings only."
        ))

    promoted_by = idx.get(term_id)
    if status == "promoted" and not promoted_by:
        return (term_id, (
            f'declares "promoted" but the registry has no file for it. Either use '
            f'"extraction-layer" (reusing an unpromoted id is fine and needs no '
            f"file), or find the id the registry really uses - it may be promoted "
            f"under a different name, which counts as promoted."
        ))
    if status == "minted" and promoted_by:
        return (term_id, (
            f'declares "minted" but the registry already promotes this id, in '
            f"{os.path.relpath(promoted_by, POC)}. Reuse it and mark it "
            f'"promoted" rather than minting a second term for it. (This is the '
            f"failure that re-created `requiresMinVersionFor` after it had been "
            f"folded into `availableSince`.)"
        ))
    if status == "extraction-layer" and promoted_by:
        return (term_id, (
            f'declares "extraction-layer" but this id IS promoted, in '
            f'{os.path.relpath(promoted_by, POC)}. Change it to "promoted".'
        ))
    return None


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
    idx = registry_index()

    for c in rec.get("concepts", []) or []:
        if not isinstance(c, dict):
            continue
        p = check_status(c.get("candidate_id") or "(unnamed concept)",
                         c.get("registry_status"), idx, "concept")
        if p:
            registry_problems.append(p)

    # Once per distinct predicate, not once per relation. A record can use one
    # predicate twenty times; twenty identical denial lines teach agents to skim.
    seen = set()
    for r in rec.get("relations", []) or []:
        if not isinstance(r, dict):
            continue
        pred = r.get("predicate") or "(unnamed predicate)"
        status = r.get("registry_status")
        if (pred, status) in seen:
            continue
        seen.add((pred, status))
        p = check_status(pred, status, idx, "predicate")
        if p:
            registry_problems.append(p)

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
