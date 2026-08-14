#!/usr/bin/env python3
"""
Generate draft candidate FAQ question/answer pairs from the promoted relation
registry + pass-1 extraction evidence.

This is a flavour demo, not a production generator: it runs against whatever
subset of `relations/` this script's TEMPLATES dict covers, and against
whichever `extractions/` happen to exist on disk at run time (currently 145
pages, 3 rounds - server/, cloud/, couchbase-lite/, sync-gateway/, java-sdk/).
A full pass across the ~3,900-page corpus, with a complete ontology, would
surface far more and would need real dedup (this script does the barest
grouping, not full reconciliation).

Every answer is the verbatim evidence quote captured at extraction time - this
script does not write new prose. That's deliberate: an auto-generated FAQ
answer is only as trustworthy as its citation, and evidence text is the one
thing pass-1 extraction already requires and checks.

Output: one JSON file per candidate under linked-data/poc/candidate-faqs/,
plus candidate-faqs/index.md summarising all of them for human review.
"""
import glob
import json
import os
import re

POC_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_concept_labels():
    labels = {}
    for fp in glob.glob(os.path.join(POC_ROOT, "concepts", "**", "*.json"), recursive=True):
        d = json.load(open(fp))
        if isinstance(d, dict) and d.get("id"):
            labels[d["id"]] = d.get("label", d["id"])
    return labels


def prettify(ref, labels):
    if ref in labels:
        return labels[ref]
    # dotted vs dashed version-id inconsistency (e.g. server-6.5 vs server-6-5) -
    # a known un-normalized spot in the registry; try both forms before falling back.
    alt = re.sub(r"(\d)-(\d)", r"\1.\2", ref)
    if alt in labels:
        return labels[alt]
    tail = ref.rstrip("/").split("/")[-1]
    tail = tail.split(":")[-1]
    words = re.split(r"[-_]", tail)
    pretty = " ".join(w.upper() if w.lower() in ("n1ql", "sdk", "sgw", "sql", "api", "tls", "rbac") else w.capitalize()
                       for w in words if w)
    return pretty or ref


def load_relation_instances():
    files = glob.glob(os.path.join(POC_ROOT, "extractions", "**", "*.json"), recursive=True)
    by_predicate = {}
    for fp in files:
        data = json.load(open(fp))
        for r in data.get("relations", []):
            p = r.get("predicate")
            if not p:
                continue
            by_predicate.setdefault(p, []).append({
                "source_file": os.path.relpath(fp, POC_ROOT),
                "page_id": data.get("page_id"),
                "subject": r.get("subject"),
                "object": r.get("object"),
                "evidence": r.get("evidence"),
            })
    return by_predicate


# One template fn per predicate: (subject_label, object_label, instance) -> question string
TEMPLATES = {
    "requiresPrivilege": lambda s, o, i: f"What privilege do I need to use {s}?",
    "requiresEdition": lambda s, o, i: f"Does {s} require {o}, or is it available in Community Edition too?",
    "availableSince": lambda s, o, i: f"Which version introduced {s}?",
    "incompatibleWithCredentialType": lambda s, o, i: f"Can I use {s} with {o}?",
    "mustUseInsteadWhen": lambda s, o, i: f"Should I use {s} or {o}?",
    "hasNoRelationshipTo": lambda s, o, i: f"Are {s} and {o} related?",
    "shouldNotBeConfusedWith": lambda s, o, i: f"What's the difference between {s} and {o}?",
}

# requiresCapellaRole gets grouped by subject (many roles can satisfy one requirement)
# rather than emitting one near-duplicate question per role.

MAX_PER_PREDICATE = 2


def make_candidate(cid, question, evidence, instances, note=None):
    return {
        "id": cid,
        "status": "draft-unverified",
        "question": question,
        "answer": evidence,
        "groundedIn": [
            {"source_file": inst["source_file"], "page_id": inst["page_id"],
             "subject": inst["subject"], "object": inst["object"]}
            for inst in instances
        ],
        "note": note or "Mechanically generated from a single extracted relation instance. "
                         "Not verified against the live page; treat the answer text as a "
                         "candidate lead, not publishable copy, until a human checks it "
                         "against the current source.",
    }


def main():
    labels = load_concept_labels()
    by_predicate = load_relation_instances()
    candidates = []

    for predicate, template in TEMPLATES.items():
        instances = by_predicate.get(predicate, [])
        seen_subjects = set()
        count = 0
        for inst in instances:
            if count >= MAX_PER_PREDICATE:
                break
            if not inst["evidence"] or not inst["subject"] or not inst["object"]:
                continue
            if inst["subject"] in seen_subjects:
                continue
            seen_subjects.add(inst["subject"])
            s_label = prettify(inst["subject"], labels)
            o_label = prettify(inst["object"], labels)
            question = template(s_label, o_label, inst)
            slug = re.sub(r"[^a-z0-9]+", "-", question.lower()).strip("-")[:70]
            cid = f"https://docs.couchbase.com/ld/candidate-faqs/{slug}"
            candidates.append(make_candidate(cid, question, inst["evidence"], [inst]))
            count += 1

    # requiresCapellaRole: group all satisfying roles per subject into one question
    role_instances = by_predicate.get("requiresCapellaRole", [])
    grouped = {}
    for inst in role_instances:
        grouped.setdefault(inst["subject"], []).append(inst)
    for subj, insts in list(grouped.items())[:2]:
        s_label = prettify(subj, labels)
        roles = sorted({prettify(i["object"], labels) for i in insts})
        question = f"What Capella role do I need to use {s_label}?"
        slug = re.sub(r"[^a-z0-9]+", "-", question.lower()).strip("-")[:70]
        cid = f"https://docs.couchbase.com/ld/candidate-faqs/{slug}"
        evidence = insts[0]["evidence"]
        note = (f"Grouped from {len(insts)} separate requiresCapellaRole relation instances "
                f"({', '.join(roles)}) sharing one page and evidence quote. Mechanically "
                "generated; not verified against the live page.")
        candidates.append(make_candidate(cid, question, evidence, insts, note=note))

    for c in candidates:
        slug = c["id"].rsplit("/", 1)[-1]
        with open(os.path.join(OUT_DIR, f"{slug}.json"), "w") as f:
            json.dump(c, f, indent=2)
            f.write("\n")

    with open(os.path.join(OUT_DIR, "index.md"), "w") as f:
        f.write("# Candidate FAQs (draft, mechanically generated)\n\n")
        f.write(
            f"{len(candidates)} candidates generated from {sum(len(v) for v in by_predicate.values())} "
            "relation instances across the current extractions/ tree (145 pages, 3 rounds). See "
            "generate_candidates.py's docstring for scope and caveats.\n\n"
            "**None of these are verified or ready to publish.** Each answer is a verbatim evidence "
            "quote captured at extraction time, not checked against the current live page. Treat "
            "this as a demonstration of what a full pass could surface, not a content deliverable.\n\n"
        )
        for c in candidates:
            f.write(f"## {c['question']}\n\n")
            f.write(f"> {c['answer']}\n\n")
            src = c["groundedIn"][0]["source_file"]
            f.write(f"Grounded in: `{src}` ({len(c['groundedIn'])} instance(s)) - `{c['id']}`\n\n")

    print(f"Wrote {len(candidates)} candidate FAQ files + index.md to {OUT_DIR}")


if __name__ == "__main__":
    main()
