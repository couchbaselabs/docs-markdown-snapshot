#!/usr/bin/env python3
"""Regression test for `gate-evidence.py`. Run it after touching that file.

    python3 linked-data/poc/hooks/test-gate.py

Exits non-zero on any failure. Feeds crafted `PreToolUse` payloads to the hook as
a subprocess - the same interface Claude Code uses - and checks the verdict and,
for denials, that the message names the actual reason.

Why this exists
---------------
The gate is a live `PreToolUse` hook on `Write|Edit|MultiEdit`. Breaking it does
not break a report; it blocks every extraction write in the repo, for every agent,
including the ones a coordinator can't see. Round 15 added two id-shape rules to
it, which is the first time it grew a rule that can *deny* something new, and
"blocks the thing it should block" and "still allows everything it allowed
yesterday" are separate claims. The second one is the expensive one to get wrong.

The synthetic fixture is the point, not a shortcut
--------------------------------------------------
This file builds its own record instead of replaying a real one from
`extractions/`, because the obvious version of that test fails - and finding out
why was the most interesting result of writing it.

Replaying `server/8.0/learn/security/authentication-overview.json`, a round-12
record written *under* the enum gate and allowed at the time, now produces five
denials: it declares `extraction-layer` for `auth-mechanism:x509-certificate` and
`minted` for `rbac-model:privilege`, both of which later rounds promoted. The
record was true when written and is false now.

So `registry_status` is a claim about a moving target, and the gate's verdicts have
a shelf life. Two consequences worth stating plainly, because both are tempting
mistakes:

  - Do not re-run this gate over the corpus as an audit. It would report a
    denial count proportional to how much has been promoted since each record was
    written, and every one of those would be a false alarm. `verify-evidence.py`
    is the corpus-wide check; its claim (is this sentence on that page?) is about
    two fixed things and does not decay.
  - Do not "fix" old records to match the current registry. Their declarations
    describe the registry they were written against, which is information; making
    them agree with today's would destroy it and would have to be redone at the
    next promotion.

A fixture built from currently-promoted ids has the same shelf life, which is why
it uses only long-stable terms (`n1ql:curl-function`, `seeAlso`) and asserts on the
new rules with ids that are deliberately fictional.
"""

import copy
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
HOOK = os.path.join(HERE, "gate-evidence.py")
GATED = "linked-data/poc/extractions/server/8.0/tmp-gate-test.json"

# One promoted concept, one promoted predicate, one quote that really is on the
# page - the minimum record that should sail through untouched.
BASE = {
    "page_id": "server/8.0/n1ql/n1ql-language-reference/curl",
    "source_version": "8.0",
    "source_path": "server/current/n1ql/n1ql-language-reference/curl.md",
    "concepts": [
        {"candidate_id": "n1ql:curl-function", "label": "CURL()",
         "registry_status": "promoted", "reused_or_minted": "reused"},
    ],
    "relations": [
        {"subject": "n1ql:curl-function", "predicate": "seeAlso",
         "object": "n1ql:curl-all-access",
         "registry_status": "promoted", "reused_or_minted_predicate": "reused",
         "evidence": "This field set must be set to false to enable the "
                     "allowed\\_urls and disallowed\\_urls fields."},
    ],
}


def run(rec, path=GATED, tool="Write"):
    payload = {"tool_name": tool, "session_id": "gate-test", "cwd": ROOT,
               "tool_input": {"file_path": path, "content": json.dumps(rec)}}
    p = subprocess.run([sys.executable, HOOK], input=json.dumps(payload),
                       capture_output=True, text=True)
    return p.returncode, p.stderr.strip()


FAILURES = []


def case(name, rec, expect, needle=None, **kw):
    rc, err = run(rec, **kw)
    got = "allow" if rc == 0 else "deny"
    ok = got == expect and (needle is None or needle in err)
    if not ok:
        FAILURES.append(name)
    print(f"{'PASS' if ok else 'FAIL'}  {name} -> {got}")
    if not ok:
        print(f"      expected {expect}"
              + (f" mentioning {needle!r}" if needle else "")
              + f"\n      stderr: {err[:400]}")


def with_concept(cid, status):
    rec = copy.deepcopy(BASE)
    rec["concepts"].append({"candidate_id": cid, "label": "test concept",
                            "registry_status": status,
                            "reused_or_minted": f"{status} - test fixture"})
    return rec


def main():
    case("a clean record is allowed", BASE, "allow")

    # Round 15, rule 1: no singular/plural fork of an existing namespace.
    case("minted `indexes:` is refused", with_concept("indexes:thing", "minted"),
         "deny", "variant of `index:`")
    case("minted `cloud-providers:` is refused",
         with_concept("cloud-providers:oracle", "minted"), "deny",
         "variant of `cloud-provider:`")
    case("minted `tools:` is refused", with_concept("tools:cbstats", "minted"),
         "deny", "variant of `tool:`")

    # Round 15, rule 2: no file extension in an id.
    case("minted id ending .adoc is refused",
         with_concept("rest-api:some-page.adoc", "minted"), "deny", "file extension")
    case("minted id ending .md is refused",
         with_concept("n1ql:selectintro.md", "minted"), "deny", "file extension")

    # Forward-only: both rules are scoped to new mints, so the corpus's existing
    # 43 shadow prefixes and its one `.adoc` id stay reusable. Without this, the
    # re-extraction rounds that fix them would be the rounds the gate blocks.
    case("reusing an `indexes:` id is allowed",
         with_concept("indexes:thing", "extraction-layer"), "allow")
    case("reusing the existing .adoc id is allowed",
         with_concept("rest-api:compaction-rest-api.adoc", "extraction-layer"), "allow")

    # Depluralisation must not eat short real prefixes, and a genuinely new
    # namespace must still be free to appear - minting is the expected answer.
    for prefix in ("tls", "sgw", "js-udf", "n1ql", "index", "tool",
                   "cloud-provider", "vector-search", "brand-new-ns"):
        case(f"minted `{prefix}:` is allowed",
             with_concept(f"{prefix}:brand-new-thing", "minted"), "allow")

    # The rules the gate already had must be untouched.
    rec = copy.deepcopy(BASE)
    rec["relations"][0]["evidence"] = "a sentence that is certainly not on the page"
    case("unquotable evidence is still refused", rec, "deny", "not on")

    rec = copy.deepcopy(BASE)
    rec["concepts"][0]["registry_status"] = "wat"
    case("an unrecognised registry_status is still refused", rec, "deny", "not one of")

    rec = copy.deepcopy(BASE)
    rec["concepts"][0]["registry_status"] = "minted"
    case("re-minting a promoted id is still refused", rec, "deny", "already promotes")

    rec = copy.deepcopy(BASE)
    del rec["concepts"][0]["registry_status"]
    case("a missing registry_status is still refused", rec, "deny", 'missing "registry_status"')

    case("Edit is still refused on an extraction record", BASE, "deny",
         "not allowed on extraction records", tool="Edit")

    # And the cheap path test: this hook lives in a repo shared with people who
    # have nothing to do with the POC.
    case("a file outside extractions/ is ignored", {"not even a record": True},
         "allow", path="linked-data/poc/concepts/n1ql/whatever.json")

    print()
    if FAILURES:
        print(f"{len(FAILURES)} FAILED: {', '.join(FAILURES)}")
        return 1
    print("all gate checks pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
