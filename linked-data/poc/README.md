# Linked-data POC — sample tree

A proof of concept for the approach described in
[`../linked-data-spec.md`](../linked-data-spec.md): can an LLM propose the ontology
piecemeal, page by page, well enough to be worth iterating on, rather than needing a
week of upfront ontology design?

This is a review artefact, not production output — everything here was extracted
and reconciled to see what the method actually produces before investing in
automating it. Three rounds so far, each a deliberate escalation:

1. **8 pages, fully by hand** — one page at a time, carrying a running registry of
   already-minted terms forward.
2. **100 pages, `server/` + `cloud/`** — extraction ran as 10 parallel subagents;
   reconciliation switched to a script aggregating recurrence across all files,
   rather than a human reading each one.
3. **37 pages across three different products** — Couchbase Lite, Sync Gateway,
   Java SDK — testing whether the vocabulary survives crossing not just a
   deployment model, but a genuinely different product built by a different team.

See `reconciliation.md` for the full round-by-round log, findings, and a
cumulative verdict at the end. See `../ingest-cost-and-time-estimate.md` for the
time/cost projections and how they held up against the round-2 run's real numbers.

## Scope

145 pages total:

- **The original 8** — 5 pages from `server/7.2/n1ql/n1ql-language-reference/`
  (`CREATE INDEX`, `DROP INDEX`, `BUILD INDEX`, `DROP PRIMARY INDEX`,
  `CREATE PRIMARY INDEX`, `Index Partitioning`) plus 2 from `server/7.2/search/`
  and `server/7.2/fts/`.
- **100 more** — 50 from `server/` (continuing into `learn/services-and-indexes/`,
  `manage/`, more of `search/` and `fts/`) and 50 from `cloud/` (Capella),
  the latter deliberately loaded toward the statement family and security surface
  most likely to break the server/-built vocabulary. It did — see the headline
  finding in `reconciliation.md` that Capella's access-control model is a
  genuinely different shape, not a renamed one.
- **37 more, across three different products** — 12 from `couchbase-lite/android/`
  (an embedded, on-device database with no server-side RBAC at all), 13 from
  `sync-gateway/` (a sync/access-control middleware with its own channel- and
  role-based model), 12 from `java-sdk/` (a client library — testing whether SDK
  pages should reuse the existing statement-level concepts or need their own).

## Identifiers

Concept, relation, and docs-issue nodes use real IRIs under
`https://docs.couchbase.com/ld/`, mirroring this directory's own structure
(`.../ld/concepts/...`, `.../ld/relations/...`, `.../ld/docs-issues/...`). Nothing
is actually served at that path yet — this is a forward commitment to where these
things would live once there's a publishing pipeline, the same way most ontologies
mint IRIs before they're dereferenceable. `extractions/` records still use short
local working identifiers (`n1ql:create-index`, `sgw:channel`) — they're
pass-1/pass-2 working data, not yet promoted, so they haven't earned a real IRI.
That promotion-to-IRI step is exactly what separates "in `concepts/`/`relations/`"
from "still in `extractions/`."

## How to read this directory

- **`extractions/`** — one JSON record per source page, mirroring its path under
  `server/`, `cloud/`, `couchbase-lite/`, `sync-gateway/`, or `java-sdk/`. Each
  record is the pass-1 output: candidate concepts, candidate relations, an
  `evidence` quote for every relation, and whether each term was reused from the
  registry or freshly minted (with a reason). Records also carry `notable_absence`,
  `cross_component_finding` (different component, same product), or
  `cross_product_finding` (different product/deployment model) fields where
  relevant — things the extraction noticed that aren't ontology relations at all,
  cross-linked to a `docs-issues/` entry where one exists.
- **`concepts/`** — the *instance-level* terms promoted to first-class nodes.
  Started with the original privilege/edition/version/enum family; round 2 added
  Capella's management-plane roles, credential-type-keyed privileges, and a
  `deployment:capella` concept; round 3 added Sync Gateway's channel/role/user
  primitives and Couchbase Lite's own edition split. See `reconciliation.md` for
  the full list and why each was promoted — including a same-word-different-thing
  collision the vocabulary had been quietly accumulating: `capella-role:*`,
  `rbac-role:role`, and `sgw:role` are three structurally distinct things all
  called "role."
- **`relations/`** — the *schema-level* terms: relation/predicate types minted
  because no existing vocabulary fit. Started with just `mustUseInsteadWhen`;
  round 2 added `requiresCapellaRole` (Capella's headline predicate),
  `incompatibleWithCredentialType`, `isSynonymOf`, `requiresUiMode`,
  `dependsOnService`, `requiresSupportPlan`, `requiresSetting`,
  `tradesOffAgainst`, and Capella's GRANT/REVOKE family; round 3 added
  `grantsChannelAccess` (now the single most-recurring minted predicate across
  the whole project), `hasNoRelationshipTo`, and a handful more covering Sync
  Gateway's role/channel mechanics. Kept separate from `concepts/` on purpose —
  properties and the instances they connect are different layers of an ontology
  (roughly, RDFS/OWL's "TBox vs ABox" split), and blurring them makes the JSON-LD
  `@context` harder to design cleanly.
- **`docs-issues/`** — a deliberately minimal, deliberately promiscuous log of
  content-quality findings (missing documentation, apparent doc-duplication,
  unadapted shared-source content, empty stub pages) that are *about the docs*,
  not about Couchbase — kept separate from `concepts/` and `relations/` so the
  product ontology doesn't grow a parallel meta-ontology of
  documentation-about-documentation. Each entry is just `{id, type: "docs-issue",
  issueType, description, about, status}` — minted with no gatekeeping. 17 entries
  as of round 3, which is itself the point: nobody is expected to read this file
  start-to-finish once it's this size — it stays a queryable "which products/pages
  have logged issues, and what are they?" store, which matters once this scales
  past a handful of pages to the ~3,900 in the full corpus.
- **`reconciliation.md`** — the pass-2 log, one section per round, with a
  cumulative verdict at the end.
- **`candidate-faqs/`** — a small, separate experiment: `generate_candidates.py`
  mechanically turns promoted relations + extraction evidence into draft
  FAQ-shaped question/answer pairs (14 so far, across `requiresPrivilege`,
  `requiresEdition`, `availableSince`, `incompatibleWithCredentialType`,
  `mustUseInsteadWhen`, `hasNoRelationshipTo`, `shouldNotBeConfusedWith`, and a
  grouped `requiresCapellaRole`). Every answer is a verbatim evidence quote, not
  new prose — see `index.md` there for the full list and the script's docstring
  for scope/caveats. This is downstream of the ontology, not part of pass-1/pass-2
  reconciliation, and every candidate is explicitly `status: draft-unverified`
  until a human checks it against the live page.
- **`faq/server.jsonld`** — a further sketch: one `schema:FAQPage` per component,
  built from the same relations/evidence as `candidate-faqs/` but assembled into
  a single document with `mainEntity` (a flat, schema.org-valid list of
  `Question`/`Answer` pairs, each tagged `schema:about` the concept it concerns)
  plus a `faqGroups` index clustering those same questions by concept for
  navigation/rendering. `faqGroups` is declared inline in the file's own
  `@context`, not added to the shared `context.jsonld` — this is a sketch, not a
  promoted addition. One entry (the DROP PRIMARY INDEX/DROP INDEX pair) has no
  concept group, on purpose: it's a relationship between two page-level
  statements, not something that hangs off a single promoted concept node — not
  every FAQ groups cleanly, and forcing one would misrepresent the relation.

## The JSON-LD layer

`context.jsonld`, `relations/*.jsonld`, `concepts/*.jsonld`, and `pages/*.jsonld` are
the actual candidate JSON-LD — what would be served, as opposed to the working
`.json` files sitting alongside most of them, which stay as internal bookkeeping
(promotion reasoning, recurrence counts, occurrence lists — fields agreed early on
not to be worth denormalizing into anything served publicly). Only a flagship
subset of each round's promotions has a full `.jsonld` treatment so far
(round 1: `mustUseInsteadWhen`; round 2: `requiresCapellaRole` and the
credential-type family; round 3: `grantsChannelAccess`, `hasNoRelationshipTo`, and
the core `sgw:channel`/`role`/`user` concepts) — the rest are promoted at the
intermediate `.json` layer only, flagged rather than rushed.

**Two different serving locations, on purpose:**

- `concepts/`, `relations/`, and (if it's ever exposed this way) `docs-issues/` are
  entities that don't have one natural page of their own — a privilege, an edition, a
  relation type — so they get real endpoints under the agreed `https://docs.couchbase.com/ld/`
  prefix, mirroring this directory's own structure.
- `pages/*.jsonld` deliberately does **not** sit under `/ld/`. Each file's `@id` is
  the real page's own canonical URL — the `.jsonld` file is just another
  representation of that same resource, the way `.html` and `.md` already are.
  `pages/` in this POC tree is a stand-in for wherever that `.jsonld` sibling would
  actually be served from, once there's a rewrite rule for it — not a fourth
  top-level `/ld/` bucket. (Only the original 8 pages have a `pages/*.jsonld` file
  so far; rounds 2 and 3 stopped at the `concepts/`/`relations/` layer.)

**Neither of these resolves today.** Same forward-commitment pattern as everything
else in this POC: the IRIs are real and consistent, but nothing is being served at
them yet.

**Modeling choices worth checking, not just accepting:**

- **Sub-statement subjects.** Some relations belong to the whole statement, but
  some belong to a specific clause or option within it (`num_replica` requiring
  Enterprise Edition, not the whole `CREATE INDEX` statement) — modeled as nested
  `cb:StatementOption` nodes rather than flattened onto the page.
- **`index-state` is a `skos:ConceptScheme`, not a `skos:Concept`** — a small
  enumeration, not a single term.
- **`rdfs:seeAlso` is reused as-is**, not a custom relation.
- **`behavesDifferentlyUnder`'s range has now generalized three times** without
  changing shape: edition (round 1), deployment variant (round 2's
  `deployment:capella`), and product family (round 3's CBL-vs-server SQL++
  dialect comparison). Worth treating as a validated, general-purpose "varies by
  X" relation rather than something scoped narrowly to editions.

## Headline findings

**Round 1 (8 pages):** the privilege/version/edition vocabulary held up cleanly
across components, and surfaced a real content gap — some page templates never
document required privileges — and what looks like two overlapping documentation
generations (`fts/` vs `search/`).

**Round 2 (100 pages, server/ vs. cloud/):**

1. **Capella's access-control model isn't server/'s RBAC with different names —
   it's a genuinely different shape.** Management-plane roles gating DDL; a
   credential-type-keyed privilege pair; a role-hierarchy model for GRANT/REVOKE;
   billing- and support-plan gates with no edition equivalent. Not "does the
   vocabulary still fit" but "what does it look like when it genuinely doesn't,
   and can the method tell the difference." It could.
2. **The most-recurring anomaly wasn't an ontology problem at all** — at least 11
   relations across 6 Capella pages cite literal `server/`-style version strings
   on a product with no discrete versions. Reads as shared source content copied
   without full adaptation.
3. Two agents, blind to each other, independently minted what may be the same
   privilege under two different names — a concrete demonstration that a written
   registry stops re-minting *already-promoted* terms but does nothing to stop
   two agents duplicating something *new* in the same run.
4. Reconciliation itself changed method at this scale: aggregating recurrence
   with a script, rather than reading every file.

**Round 3 (37 pages, three different products) — the most consequential round yet:**

5. **Sync Gateway runs two disjoint access-control systems, and neither is
   `requiresPrivilege`.** Its own docs state its channel/role model and its
   reused server-RBAC model "have no relationship" — one product deliberately
   running two unrelated systems, not one system under two names. The
   channel-based model itself inverts the whole shape: documents are tagged with
   channels, users/roles are granted channel membership, and a read is a pure
   set-intersection with no per-operation gate anywhere. `grantsChannelAccess` is
   now the single most-recurring minted predicate in the whole project.
6. **A same-word-different-thing collision surfaced, and was deliberately left
   unresolved.** `capella-role:*`, `rbac-role:role`, and `sgw:role` are three
   structurally distinct things, all called "role." No page states they're
   unrelated, so they weren't merged or cross-linked — inventing that link
   without textual evidence would be a fact, not an extraction.
7. Couchbase Lite has its own Enterprise/Community split gating an entirely
   different feature set than server/'s — and one internal inconsistency (Vector
   Search isn't edition-gated despite looking like it should be) is now a
   docs-issue rather than something the extraction silently resolved.
8. The Java SDK batch showed the method can make — and check — a genuine
   judgment call: it correctly reused existing statement concepts where a page
   wraps one, minted new SDK-specific concepts where it doesn't, and in one case
   explicitly rejected a hint from its own briefing after checking the actual
   page content.

## What this is not

The IRI base is settled, and `concepts/`/`relations/`/`pages/` have real candidate
JSON-LD for a flagship subset of each round. Still open: the actual
embedding/serving mechanics for `pages/*.jsonld`, whether SKOS and schema.org are
the full extent of third-party ontology adoption, and full JSON-LD coverage for
everything promoted at the intermediate `.json` layer only. None of this is
resolved here, on purpose — this stays a reviewable artefact, not a second design
document.

## Suggested next steps

- Get a subject-matter expert to work through `docs-issues/` (17 entries) —
  most valuably the three-way "role" collision and the Sync Gateway/Capella
  access-control questions, since those are product-shape decisions, not just
  docs cleanup.
- Draft the remaining JSON-LD for everything still intermediate-only across all
  three rounds.
- Run a normalization pass over `extractions/` for the small ID inconsistencies
  the aggregation surfaced but didn't hand-fix — mechanical, scriptable, not
  worth doing by hand at this volume.
- Decide the actual publishing mechanics for `pages/*.jsonld`.
- If this looks worth pursuing past a POC: three axes of stress test have now
  been run (cross-component, cross-deployment-model, cross-product-family). The
  next natural one is scale itself — a real batch against the ~3,900-page
  "latest version only" corpus from `../ingest-cost-and-time-estimate.md`, now
  that the extraction/reconcile/promote pipeline has been exercised on all three
  axes it's likely to meet at that size.
