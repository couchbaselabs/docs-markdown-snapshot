# Linked-data POC — sample tree

A proof of concept for the approach described in
[`../linked-data-spec.md`](../linked-data-spec.md): can an LLM propose the ontology
piecemeal, page by page, well enough to be worth iterating on, rather than needing a
week of upfront ontology design?

This is a review artefact, not production output — everything here was extracted
and reconciled to see what the method actually produces before investing in
automating it. Ten rounds so far, each a deliberate escalation:

1. **8 pages, fully by hand** — one page at a time, carrying a running registry of
   already-minted terms forward.
2. **100 pages, `server/` + `cloud/`** — extraction ran as 10 parallel subagents;
   reconciliation switched to a script aggregating recurrence across all files,
   rather than a human reading each one.
3. **37 pages across three different products** — Couchbase Lite, Sync Gateway,
   Java SDK — testing whether the vocabulary survives crossing not just a
   deployment model, but a genuinely different product built by a different team.
4. **3 pages, Java SDK transactions** — a deliberately small infrastructure
   trial (the host environment had just migrated from direct Anthropic API
   access to Amazon Bedrock) that also happened to test whether a single
   product's own feature can cut across its existing per-operation vocabulary.
   It did — see the headline finding in `reconciliation.md`.
5. **115 pages completing `cloud/n1ql/`** — the first real-scale (not trial)
   round run on Bedrock, closing out a directory round 2 had only sampled a
   fifth of. Found that round 2's "simple credential-type pair" was actually
   a whole per-statement privilege catalog with real AND/OR and two-axis
   structure the smaller sample hadn't surfaced.
6. **89 pages closing out the rest of `cloud/`'s management plane** —
   Organizations, Projects, Billing, Security, Get Started, the Data API and
   Management API guides, per-service metrics, and general reference (leaving
   `clusters/`, `eventing/`, and `guides/` as deliberate first-contact
   candidates for a future round). Found the same lesson as round 5, one
   level up: `capella-role:*` was never one role catalog — it's two
   (organization-scope and project-scope), silently flattened together since
   round 2.
7. **53 pages, `cloud/clusters/`** — cluster lifecycle, backup/restore,
   cluster-level RBAC, per-service management pages, XDCR, and monitoring.
   Found the identical undercounting lesson a third time, this round on the
   privilege catalog: `cluster-rbac.md`'s own table lists 25 privileges, not
   the 11 the registry had going in.
8. **67 pages, `cloud/eventing/`** — Capella's Eventing feature (JavaScript
   functions reacting to KV mutations), genuinely new territory. The cleanest
   negative result so far: unlike every prior "new feature" test, Eventing
   needed no new structural layer at all — it slots into existing vocabulary
   everywhere, with a fifth "role" and a real management-vs-runtime
   access-control split as its only genuine additions.
9. **33 pages, `cloud/guides/`** — task-oriented how-to pages wrapping
   statements already documented in rounds 5/6. Closes out `cloud/`
   entirely. The reuse hypothesis held for almost all 33 pages, but still
   surfaced three real SDK-layer gaps, a stateful entity a reference page had
   only seen as a function usage, and a round-5 open question (does SQL++'s
   transaction family relate to the Java SDK's?) finally closed by a page's
   own explicit text.
10. **38 pages, `server/current` wave 1** — the first wave into a *second
    product tree* (Couchbase Server 8.0), selected by diff-gating against the
    already-extracted Capella twins. Two results changed the project rather
    than just extending it. First, an extraction agent **fabricated its
    evidence** — eleven of one record's thirteen relations quote sentences that
    do not exist on the page, including a version claim for a feature the page
    never dates — and no human-legible control caught it. That produced
    `verify-evidence.py`, and running it over the whole corpus found that the
    "evidence must be a direct quote" rule had never actually been enforced:
    322 of 2,780 relations are unquotable. Second, version-evidence density
    turned out to be **inversely** correlated with novelty — the statements new
    in 8.0 are precisely the ones no page dates — which is the opposite of what
    the wave was briefed to expect, and a better finding.

See `reconciliation.md` for the full round-by-round log, findings, and a
cumulative verdict at the end. See `../ingest-cost-and-time-estimate.md` for the
time/cost projections and how they held up against the round-2 run's real numbers.

## Scope

543 pages total:

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
- **3 more, `java-sdk/`** — `howtos/error-handling.md`,
  `distributed-acid-transactions-from-the-sdk.md`, and
  `transactions-single-query.md`. A small infrastructure trial (see "What this
  round tested" in `reconciliation.md`'s round 4 section) that also confirmed
  distributed transactions need their own structural layer, not a reuse of the
  SDK's existing per-operation vocabulary.
- **115 more, `cloud/n1ql/`** — the remaining pages in Capella's SQL++/N1QL
  language reference, intro, and manage sections (round 2 had sampled 23 of
  the directory's 138 pages; this closes it out). The first real-scale
  extraction round run on the post-Bedrock-migration pipeline.
- **89 more, the rest of `cloud/`'s management plane** — `security/`,
  `indexes/`, `projects/`, `organizations/` (including all 6 SSO provider
  guides), `billing/`, `get-started/` (including Capella iQ), `data-api-guide/`,
  `javascript-udfs/`, `management-api-guide/`, `metrics-reference/`, and
  `reference/`. Leaves `clusters/` (53 pages), `eventing/` (67), and `guides/`
  (33) as the largest untouched `cloud/` territory, each a deliberate
  first-contact candidate rather than filler for a future round.
- **53 more, `cloud/clusters/`** — cluster lifecycle, backup/restore,
  `cluster-rbac.md`, per-service management pages, XDCR, and monitoring/
  alerting. Leaves `eventing/` (67 pages) and `guides/` (33) as the last
  untouched `cloud/` territory.
- **67 more, `cloud/eventing/`** — Capella's Eventing feature: core concepts,
  RBAC, function management, worked examples, and ~40 individual JS handler
  code-sample pages. Leaves `guides/` (33 pages) as the last untouched
  `cloud/` territory.
- **33 more, `cloud/guides/`** — task-oriented how-to pages for data
  operations, indexing/optimization, and query/UDF workflows. **`cloud/` is
  now fully covered** — 5 rounds (5 through 9), ~460 pages, since round 5
  started the real-scale phase of this project.
- **38 more, `server/current/n1ql/`** — Couchbase Server 8.0: the SQL++
  transaction family, the statement pages that diverge most from their Capella
  twins, the whole `n1ql-rest-api/` directory, and the Server-only pages
  (`cbq.md`, AWR, auditing, monitoring) that have no Capella counterpart. The
  first of roughly 13 waves needed to cover `server/current`'s 1,033 pages —
  see `../ingest-cost-and-time-estimate.md` for the wave plan and why the
  recommendation is `current` plus one previous version (7.6), not the full
  version history.
  Note that this round also **re-scoped the existing `server/` records under
  `extractions/server/7.2/`**: all 58 of them are 7.2, and they carried
  version-neutral `page_id`s alongside version-bearing source paths, so
  ingesting a second version would have silently overwritten
  `createindex.json` and `alterindex.json` with no diagnostic. Wave 1's own
  records live under `extractions/server/8.0/`, **not** `server/current/`:
  `current` is a pointer, not a version, so it gets no `page_id` and no concept
  — see the ruling in `reconciliation.md`. The one place the alias is asserted
  is `concepts/version/server-8-0.json`, which carries `isCurrentRelease` and
  `docsTreeAlias` as its only deliberately mutable fields.

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
  `server/<version>/`, `cloud/`, `couchbase-lite/`, `sync-gateway/`, or
  `java-sdk/`. The `server/` records are version-scoped (`server/7.2/`,
  `server/8.0/`) because they have to be: the same page exists in every
  version tree, so a version-neutral layout silently overwrites one round's
  record with another's. They are scoped by **release number, never by the
  docs' `current` alias** — `current`'s referent changes on every major
  release, and an id that silently starts denoting something else is worse than
  no id. `cloud/` needs no such scoping — Capella has no discrete versions,
  which is itself one of the vocabulary's load-bearing differences.
  One consequence to expect when reading a `server/8.0/` record: its `page_id`
  says `server/8.0/…` while its `source_path` says `server/current/…`. That is
  correct. `page_id` is an ontology identifier and must be stable;
  `source_path` is a filesystem path and must keep resolving. Each
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
  primitives and Couchbase Lite's own edition split; round 4 added four Java SDK
  transaction primitives (`sdk:transaction-attempt-context`,
  `sdk:transaction-durability`, `sdk:transaction-query-mode`,
  `sdk:transaction-error-handling`) and a new `version:sdk-*` family; round 5
  added eleven more Capella Advanced-credential privileges (completing what
  turned out to be a full per-statement privilege catalog, not the simple
  pair round 2 first saw), an access-surface concept family
  (`capella:query-tab`/`data-api`/`cbsh`), and a fourth thing called "role"
  (`role:full-administrator`/`local-user-security-administrator`); round 6
  found `capella-role:*` was never one role catalog but two
  (organization-scope and project-scope, silently flattened together since
  round 2) and added the six roles missing from each, plus new `auth:`/`sso:`
  families for authentication (SSO/MFA), a support-plan tier family
  (`plan:enterprise-support-plan` and siblings), and two more generalizations
  of `behavesDifferentlyUnder` (within-Capella cloud-provider and
  storage-engine variance). See `reconciliation.md` for the full list and why
  each was promoted — including a same-word-different-thing collision the
  vocabulary had been quietly accumulating: `capella-role:*`, `rbac-role:role`,
  `sgw:role`, and `role:*` are four structurally distinct things all called
  "role" — and, within round 6 alone, a second, unrelated collision:
  `capella-role:cluster-manager` (a role) and `capella:cluster-manager` (a
  monitored system component) share a name but nothing else; round 7 found
  the same undercounting lesson a third time (15 new Advanced-credential
  privileges from `cluster-rbac.md`'s own 25-row table, more than doubling
  the 11 the registry had) plus another same-word collision (`capella:index-ui-status`,
  the Indexes UI's own ready/pause/warmup enum, vs. the SQL++ DDL `index-state`
  lifecycle enum — same subject, two unreconciled vocabularies), and finally
  promoted round 5's `monitoring:*` family, which had been narratively
  described as promoted at the time but never actually filed; round 8 added
  a whole `eventing:` namespace for Capella's Eventing feature (function,
  binding, timer, lifecycle state, the OnUpdate/OnDelete handler pair) and a
  fifth thing called "role" (`role:eventing-full-admin`) — but, notably,
  *no* new access-control shape, unlike every genuinely-new-feature round
  before it; round 9 closed out `cloud/` entirely with three SDK-layer gaps
  found reading guide (not reference) content — `sdk:subdocument-operations`,
  `sdk:query-index-manager`, `sdk:bulk-import-workflow` — plus
  `n1ql:advisor-session`, the first entity in this project modeled as
  stateful (start/collect/stop/purge) rather than a single function call.
  Round 10 promoted 70 — by far the largest concept round — because a
  corpus-wide recurrence recount (see below) found that eight rounds had
  accumulated silent promotion debt: `n1ql:query-context` had recurred **22**
  times across the corpus without ever being filed, `create-index` 20,
  `cost-based-optimizer` 15, `tool:cbq-shell` 18. Round 10 paid most of that
  down: the SQL++ transaction family (9 concepts), ~23 statement/clause terms,
  the Query REST API plus its three distinct settings tiers, five `service:*`,
  four `version:*`, and the five round-3/4 SDK backlog items listed below.
  It also **refused** three promotions on purpose: all 93 index concepts (they
  are individually correct and collectively incoherent — several unreconciled
  taxonomic axes flattened into one namespace, deferred pending a read of
  `server/current/learn/services-and-indexes/`), `role:administrator` (the docs
  themselves are loose about it — filed as a docs-issue instead), and the
  individual `port:` concepts (an unresolved literal-vs-concept modelling
  question).
  Round 3's Java SDK backlog — flagged here since round 4 — is now **partly
  closed**: `sdk:kv-operations` was promoted in round 10, and
  `sdk:transaction-query-mode` was re-namespaced to `n1ql:transaction-query-mode`
  (with the round-4 file kept as an alias stub recording the original record
  verbatim) once a Server page's own text showed the concept is the query
  language's, not the SDK's. The rest of that backlog — `sdk:durability`,
  `sdk:cas-optimistic-locking`, `sdk:error-handling`,
  `sdk:query-error-mapping`, `sdk:sqlpp-queries-with-sdk`,
  `sdk:bucket-management` — still sits at the extraction layer only.
- **`relations/`** — the *schema-level* terms: relation/predicate types minted
  because no existing vocabulary fit. Started with just `mustUseInsteadWhen`;
  round 2 added `requiresCapellaRole` (Capella's headline predicate),
  `incompatibleWithCredentialType`, `isSynonymOf`, `requiresUiMode`,
  `dependsOnService`, `requiresSupportPlan`, `requiresSetting`,
  `tradesOffAgainst`, and Capella's GRANT/REVOKE family; round 3 added
  `grantsChannelAccess` (now the single most-recurring minted predicate across
  the whole project), `hasNoRelationshipTo`, and a handful more covering Sync
  Gateway's role/channel mechanics; round 4 added `sharesOptionSetWith`, for
  two concepts that reuse identical enum values at incompatible structural
  scopes; round 5 added `incompatibleWithAccessSurface` (a fourth Capella
  gating axis alongside role/credential-type/UI-mode), `requiresPriorExecutionOf`
  (a real cross-round, cross-product reuse the written registry caught
  correctly), and `renamedFrom`; round 6 added `impliesRole` (the mechanism
  behind the org-role/project-role catalog split), `authenticatesVia` (which
  credential transport an access surface actually uses), `disablesFeatureFor`,
  and `gatedByBillingPlan` — the last one closing a real gap: round 2's own
  narrative had described it as promoted, but no file was ever written for it
  until round 6 needed to reuse it; round 7 added `triggersAlert`, closing the
  *same* gap a third time (this one self-inflicted in round 5); round 8 added
  `requiresExplicitClose` (calling N1QL from an Eventing handler returns a
  cursor the handler must free) and `omitsMutationBody` (a real API asymmetry
  between Eventing's OnUpdate/OnDelete handlers); round 10 added 19, the
  largest predicate round, led by `documentedForVersion` — minted specifically
  as the antidote to the round's fabricated `availableSince` claim, because
  *which doc tree a page ships in* is not a claim about *when a feature
  appeared*, and conflating the two is exactly how the fabrication became
  plausible. The other 18 include `implicitlySetsParameter` (the inverse of
  `requiresSetting`), `permitsWithinTransaction` (which records three-valued
  legality, not a boolean), `requiresRequestParameter` (establishing a request
  tier distinct from node and cluster settings), `deprecatedIn`,
  `retainedForLegacyCompatibility`, and `cascadesTo` — the last a cross-round
  *fold* rather than a new mint, consolidating round 8's
  `cascadesDeletionTo`/`cascadesLifecycleChangeTo`/`removesAllSavepoints` into
  one predicate at recurrence 7. Several candidates were rejected with the
  reasoning recorded rather than promoted (`removedIn` as
  unfiled-because-undated, `noOpSince` as a property of the evidence rather
  than of the relation, `documentedAsLegacy` as a duplicate).
  Kept separate from `concepts/` on purpose —
  properties and the instances they connect are different layers of an ontology
  (roughly, RDFS/OWL's "TBox vs ABox" split), and blurring them makes the JSON-LD
  `@context` harder to design cleanly.
- **`docs-issues/`** — a deliberately minimal, deliberately promiscuous log of
  content-quality findings (missing documentation, apparent doc-duplication,
  unadapted shared-source content, empty stub pages) that are *about the docs*,
  not about Couchbase — kept separate from `concepts/` and `relations/` so the
  product ontology doesn't grow a parallel meta-ontology of
  documentation-about-documentation. Each entry is just `{id, type: "docs-issue",
  issueType, description, about, status}` — minted with no gatekeeping. 55 entries
  as of round 10, which added 22 — the largest batch of any round, and not
  because Server's docs are worse: reading a page that has an
  already-extracted twin in another tree turns every divergence between them
  into a checkable claim, so diff-gated waves find content problems at a much
  higher rate than first-contact waves do. (Round 9, a same-tree round, found
  none at all.) That size is itself the point: nobody is expected to read this file
  start-to-finish once it's this size — it stays a queryable "which products/pages
  have logged issues, and what are they?" store, which matters once this scales
  past a handful of pages to the ~3,900 in the full corpus.
- **`reconciliation.md`** — the pass-2 log, one section per round, with a
  cumulative verdict at the end.
- **`verify-evidence.py`** — the project's one real **gate**, written in round
  10 after an extraction agent fabricated its evidence. Checks every relation's
  `evidence` string against the page it claims (or against `evidence_source`,
  for the legitimately cross-page cases), normalising whitespace and smart
  quotes but deliberately *not* wording. Run it over a wave before committing:
  `python3 linked-data/poc/verify-evidence.py linked-data/poc/extractions/server/8.0`.
  It exits non-zero on any problem. Note what it does *not* prove: that the
  sentence is on the page, not that the triple built from it is a fair reading —
  round 10 found "quotable but mis-objected" records that pass this check and
  are still wrong. A green check is not a green record.
- **`hooks/gate-evidence.py`** — the same check moved *earlier*: a `PreToolUse`
  hook (registered in `../../.claude/settings.json` on `Write|Edit|MultiEdit`)
  that refuses to write any file under `extractions/` whose evidence isn't
  quotable. It imports `verify-evidence.py` rather than reimplementing it, so
  the gate and the audit can't drift apart. Two things make it worth having on
  top of the audit: it fires **inside subagents** — round 10's fabricated record
  came from one of ten parallel extraction agents whose reasoning nobody read —
  and it fails **closed**, exiting 2 on its own internal errors rather than
  waving the write through. It also refuses a record claiming a concept is
  "promoted" when no registry file exists, which is deliberately narrower than
  checking every `reused` claim: reusing an extraction-layer id is correct and
  expected, asserting registry state that isn't there is not.
  Known cost, recorded rather than glossed: the gate converts fabrication into
  *omission*. A blocked agent may drop the relation instead of hunting for a
  real quote, and no exit status shows that — hence the relations-per-page
  thinning check now in the `linked-data-reconcile` skill.
- **`verify-promotions.py`** — a **report**, not a gate (it always exits 0).
  Scans `reconciliation.md` for `ns:kebab-id` and `camelCaseTerm` shapes and
  lists those with no registry file, closing the "narrated as promoted, never
  actually filed" gap that had recurred in rounds 2, 3, 5, and 8. It can't
  distinguish "claimed as promoted" from "named while being rejected, folded or
  deferred" — the prose says which, the string doesn't — so its output is a
  short list to read each round, not a diff to clear. Its first run surfaced 5
  genuine gaps; re-running it after round 10's writeup was finished surfaced 3
  more (including `n1ql:scan-consistency` at recurrence 6, whose own extraction
  record claimed it was "already promoted"). All 8 were promoted the same day.
  A control that pays out twice on the round that introduced it is doing real
  work, not cleanup.
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

**Round 4 (3 pages, Java SDK transactions) — a small infrastructure trial that
also surfaced a real finding:**

9. **Distributed transactions don't extend the Java SDK's existing
   per-operation vocabulary — they add a new structural layer.** Same shape as
   Sync Gateway's channel model in round 3, one product deep this time instead
   of across products: a transaction-scoped concurrency model that replaces
   CAS-token comparison with transaction-membership checks; a durability
   setting that reuses the same `DurabilityLevel` enum values as per-operation
   durability but at an incompatible scope — recurring at a *third*, again
   incompatible, scope on the single-query-transaction page; a mid-flow
   permission-mode switch with no per-operation analogue; and a whole-transaction
   commit-ambiguity exception pair documented on a completely separate page
   from the SDK's general exception hierarchy.
10. **Reconciliation can leave gaps too, not just extraction.** Round 3's
    12-page Java SDK batch was reconciled only at the narrative level and never
    promoted a single concept — invisible until round 4 tried to reuse
    `sdk:kv-operations`/`sdk:durability`/`sdk:error-handling` and found them
    absent from `concepts/`. Flagged as a backlog item, not backfilled in this
    round (see "Suggested next steps").
11. The actual point of this round — confirming the extraction/reconciliation
    pipeline works unchanged after migrating from direct Anthropic API access
    to Amazon Bedrock — held up: no tool failures, no observed quality
    degradation. See `../ingest-cost-and-time-estimate.md` for the
    tooling/cost specifics.

**Round 5 (115 pages, completing `cloud/n1ql/`) — the first real-scale round on Bedrock:**

12. **Round 2's "simple credential-type pair" was actually a whole
    per-statement privilege catalog.** Reading the other 115 of 138 pages in
    the directory (round 2 had sampled 23) surfaced eleven new Advanced-side
    privileges, a privilege keyed by credential type *and* function scope
    simultaneously (`createfunction.md`), and the first AND-combination
    requirement seen in the family (`upsert.md` needs Query Insert *and*
    Query Update, not either) — none of it visible from the smaller sample.
13. **The model has real, evidenced boundaries.** Sequence operators and
    `window`/`windowfun` use bare server-style RBAC privilege names instead of
    the credential-type pair; search functions need no credential at all;
    transaction-control statements (BEGIN/COMMIT/ROLLBACK/SAVEPOINT/SET
    TRANSACTION) carry no access-control gating whatsoever, confirmed across
    every TCL page in the batch.
14. **A fourth thing called "role."** `n1ql-auditing.md` gates audit-service
    configuration with classic admin roles (Full Administrator, Local User
    Security Administrator) that fit none of the three "role" concepts the
    vocabulary was already tracking — left unmerged, like the other three,
    since no page states a relationship between any of them.
15. **A fourth gating axis: access surface.** Two unrelated pages
    (`transactions.md`, `using-ai.md`) independently state a feature is
    unsupported via specific client interfaces (Query tab, Data API,
    Couchbase Shell) regardless of role or credentials — a genuinely new axis
    alongside role/credential-type/UI-mode.
16. **The known server-version-citation anomaly recurred far more densely
    than round 2 found it** — 45 of 115 pages (39%), not the original 6 —
    plus a sibling anomaly (Enterprise/Community edition badges on a product
    with no editions) found for the first time. Density this high reads like
    a systemic authoring pattern, not isolated copy-paste.
17. **The written registry caught a real cross-round reuse correctly.** An
    unpromoted predicate minted in an earlier `server/` extraction
    (`requiresPriorExecutionOf`) was independently found and reused verbatim
    by this round's Capella equivalent, for the identical fact — the positive
    case the round 2 `requiresMinVersionFor` incident was the negative case of.

**Round 6 (89 pages, closing out the rest of `cloud/`'s management plane):**

18. **`capella-role:*` was never one role catalog — it's two, silently
    flattened together since round 2.** Statement pages' Prerequisites
    sections list organization-scope and project-scope roles side by side
    with no indication of which is which. Reading each catalog's own
    authoritative page directly revealed: three organization-scope roles
    (Organization Owner, plus new Project Creator and Organization Member)
    and five project-scope roles (Project Owner, plus new Cluster Manager,
    Cluster Viewer, Data Reader, and Data Writer — the last with a corrected
    label; the original mint called it "Project Data Writer," a paraphrase,
    not the page's own name). Four independent batches converged on
    overlapping pieces of this same corrected picture without coordinating —
    the same lesson as round 5's privilege catalog, now on the role catalog,
    twice in a row on the same product.
19. **A same-word collision surfaced within a single round, not just across
    rounds.** `capella-role:cluster-manager` (a role) and `capella:cluster-manager`
    (a monitored system component, explicitly excluded from "the Services" by
    its own reference page) share a name and nothing else.
20. **Authentication and authorization confirmed as genuinely separate axes.**
    SSO/MFA never become a role and are never granted directly — the two
    axes touch only at role-mapping (an IdP group maps to Capella access) and
    at the gate on who can configure a realm in the first place.
21. **`behavesDifferentlyUnder` generalized a third and fourth time** — within
    Capella itself, by underlying cloud provider (Azure's storage
    auto-expansion moves data, AWS's/GCP's doesn't) and by storage engine
    (Couchstore vs. Magma use different Health Advisor thresholds), the
    second found unprompted while looking for the first.
22. **The commercial support-plan wording problem is worse than known** — up
    to five variants now, including two on the same page (`billing.md` uses
    both "Enterprise Support Plan" and bare "Enterprise Plan").
23. **A four-round-old reconciliation gap surfaced.** `gatedByBillingPlan` was
    narratively described as promoted in round 2's own writeup, but no
    `relations/` file was ever written for it — invisible until round 6 tried
    to reuse it. Same shape as round 3's never-promoted Java SDK concepts,
    found in round 4.

**Round 7 (53 pages, `cloud/clusters/`):**

24. **The undercounting lesson recurred a third time, on the privilege
    catalog — and the gap was bigger than round 5's already-corrected one.**
    `cluster-rbac.md`, read directly for the first time, lists 25 distinct
    Advanced-credential privileges. The registry had 11. 15 new ones
    promoted, including the first privilege-level evidence tying the
    Eventing Service to any access-control model at all.
25. **`cluster-rbac.md` also settled a question with direct textual
    evidence rather than inference:** its own opening line states the
    data-plane credential model is separate from the organization/project
    role catalogs — confirming what the ontology's structure had assumed but
    never had a citation for.
26. **Two features new to the registry both resolved as "reuses the existing
    model, invents nothing."** XDCR's entire "security" surface turned out to
    be a network-topology choice (Public Internet/VPC Peering/Private
    Endpoint), not a new access-control mechanism; Analytics mints no
    authorization concept of its own either. A useful negative result,
    alongside all the positive ones.
27. **Two questions carried since round 6 resolved cleanly.** Storage engine
    (Couchstore/Magma) is a bucket-creation-time choice but not permanently
    fixed — a real migration path exists. Cloud-provider variance is broader
    than round 6's one example (also disk type, IOPS, region/AZ), not just
    storage auto-expansion.
28. **A third instance of the reconciliation-gap pattern, this time
    self-inflicted.** Round 5's `monitoring:*` concepts were narratively
    described as promoted and never actually filed — the same shape as round
    2's `gatedByBillingPlan` and round 3's Java SDK concepts, but this time
    introduced by a reconciler who had already written up the pattern as a
    known risk one round earlier. Closed this round, along with a genuine
    correction found while doing so (event severity and Health Advisor
    severity were conflated under one enum; they're two).

**Round 8 (67 pages, `cloud/eventing/`) — the cleanest negative result yet:**

29. **A brand-new, complex feature needed no new structural layer at all.**
    Every prior genuinely-new-feature test found something the existing
    vocabulary couldn't express (Sync Gateway's channels, the Java SDK's
    transactions). Eventing is the first to resolve the other way — function
    lifecycle matches an existing enum shape, Timers are explicitly "limited
    asynchrony" reusing the parent Function's own vocabulary, and every
    documented "unsupported feature" resolves back to an existing construct.
30. **The management-plane privilege confirmed the same "nothing new" shape.**
    `eventing-rbac.md` showed the Eventing-Manage privilege (round 7's only
    evidence for it) is never granted alone — always bundled as "Data Read
    and Eventing Manage," the identical compound-privilege pattern
    `cluster-rbac.md` already showed elsewhere.
31. **But the runtime access-control layer is genuinely new** —
    `eventing:binding` (bucket-alias/URL-alias) gates what a deployed
    function can actually touch, entirely separate from who can create or
    deploy it. Two distinct gating layers for one feature: identity/management
    vs. resource access.
32. **Two real API constraints, found reading the handler examples closely.**
    Calling `N1QL()` from a handler returns a cursor that must be explicitly
    closed — no standalone SQL++ page has an equivalent. `OnDelete()` doesn't
    supply the deleted document's body the way `OnUpdate()` does, confirmed
    independently on two handler pages.
33. **A fifth thing called "role."** `troubleshooting-best-practices.md`
    names "Eventing Full Admin," a classic cluster-wide RBAC role introduced
    at Server 7.0.0 — a third member of the `role:*` family (round 5) and a
    fifth "role" concept overall.
34. **A third variant of the unadapted-content pattern** — this one by
    naming rather than version string or edition badge: `eventing-function-export.md`
    says "Couchbase Web Console" where a Capella page should say "Capella UI."

**Round 9 (33 pages, `cloud/guides/`) — closes out `cloud/` entirely:**

35. **The reuse hypothesis held for almost all 33 pages, and that's still a
    real result** — zero new SQL++ statement concepts minted anywhere,
    confirming the registry built from rounds 5/6 generalizes cleanly to
    guide-level wrapper content.
36. **Three real SDK-layer gaps found anyway.** Guide content asks slightly
    different questions than reference content, even about the same feature:
    `sdk:subdocument-operations` (path-level `lookupIn`/`mutateIn`, missing
    from the whole-document-scoped `sdk:kv-operations`), `sdk:query-index-manager`
    (the SDK's own programmatic index API), and `sdk:bulk-import-workflow`
    (a third bulk-load path, distinct from the Data API and the CLI tool).
37. **A stateful entity a reference page had only seen as a function
    usage.** `index-advisor.md` revealed the Index Advisor's "session" is a
    genuine stateful object (start/collect/stop/get/list/purge), not just
    another `ADVISOR` function call — the first entity in this project
    modeled with an explicit lifecycle rather than as a single invocation.
38. **A round-5 open question closed by a page's own text.** Round 5 could
    find no textual evidence linking the SQL++ transaction-statement family
    to the Java SDK's transaction layer, and left it explicitly unresolved.
    `cloud/guides/transactions.md` states the boundary directly: "This
    how-to guide covers SQL++ support for Couchbase transactions. Some SDKs
    also support Couchbase transactions" — related but distinct surfaces,
    confirmed by the docs themselves.

**Round 10 (38 pages, `server/current` wave 1) — the round that changed the
method rather than extending it:**

39. **An extraction agent fabricated its evidence, and nothing human-legible
    caught it.** One record asserted `availableSince version:server-8-0` for a
    feature its page never dates, quoting a sentence that does not exist;
    eleven of its thirteen relations were unquotable, and one had inverted
    polarity ("To disable this feature" where the page reads "To enable the
    feature"). The fabricated quote was *more* plausible than the real
    sentence and the surrounding rationale better argued than most correct
    records — reviewer judgement is structurally unable to catch this, because
    the failure mode optimises for exactly what a reviewer checks.
40. **So the schema's "evidence must be a direct quote" rule had never
    actually been enforced.** Writing `verify-evidence.py` and running it over
    the whole corpus found **322 of 2,780 relations unquotable** — nine rounds
    of accumulated damage, not one bad agent. Worst affected: round 3's
    `sync-gateway` (45% verbatim, 12 of 13 records) and `couchbase-lite` (50%,
    10 of 12), both now recommended for re-extraction. Their *vocabulary*
    conclusions still stand; their individual records do not. The general
    lesson: **an invariant in a prompt is a hope; the same invariant in a
    script is a control.**
41. **Version-evidence density is inversely correlated with novelty** — the
    opposite of what this wave was briefed to expect. Pages documenting
    long-standing statements are dense with version badges, because a version
    badge is a *contrast* marker; the statements genuinely new in 8.0 carry no
    version evidence at all, because they have nothing to contrast with. The
    briefing's assumption ("earlier-version content will make
    introduced-in/deprecated vocabulary clearer") was right about the
    vocabulary and backwards about where to find it.
42. **A third species of error: axis conflation.** The 93 index concepts are
    individually correct and collectively incoherent — access method, storage
    engine, lifecycle state, and syntactic form all flattened into one
    namespace. This is distinct from the naming collisions (rounds 3/6/7) and
    the partial-sampling undercounts (rounds 5/6/7), and it exposes the limit
    of the promotion rule: recurrence-at-≥2-files answers "is this term real?"
    and nothing else. All 93 were deliberately left unpromoted.
43. **"Quotable but mis-objected" — the failure class that survives the new
    gate.** Records whose evidence is verbatim on the page but whose object
    slot is wrong. `verify-evidence.py` passes them. So: a green check is not a
    green record, and the gate is a floor, not a ceiling.
44. **The corpus-wide recurrence recount exposed eight rounds of silent
    promotion debt** — `n1ql:query-context` unpromoted at recurrence 22,
    `create-index` at 20, `tool:cbq-shell` at 18. Round 10's 70 concept
    promotions are mostly *backlog*, not new territory. Round 10 also
    established that recurrence must be recomputed over the whole corpus each
    round, not over the round's own records — and that the recount script
    itself needs testing: a one-character regex bug (`\.jsonld?` where
    `\.json(ld)?` was meant) made *every* promoted predicate appear
    unpromoted, caught only because the output was implausible. A second
    instance of "vigilance is not a control."
45. **A rename proposal was refused on new evidence.** A `monitoring:` rename
    argued from a Capella-only sample was rejected once the first Server page
    to touch monitoring produced `monitoring:awr-document` — the sample had
    been unrepresentative, and the rename would have been wrong. Similarly
    `capella:cbsh` was *not* merged with `tool:cbq-shell` after checking: two
    genuinely different tools (and `capella:` is itself a misnomer for cbsh,
    now noted in the file).
46. **Diff-gating works for wave *selection* but raw changed-line counts
    overstate yield** — example re-rendering dominates the diff, so a page can
    look heavily changed and carry no new facts. Recorded in
    `../ingest-cost-and-time-estimate.md` for the remaining ~12 waves.

## What this is not

The IRI base is settled, and `concepts/`/`relations/`/`pages/` have real candidate
JSON-LD for a flagship subset of each round. Still open: the actual
embedding/serving mechanics for `pages/*.jsonld`, whether SKOS and schema.org are
the full extent of third-party ontology adoption, and full JSON-LD coverage for
everything promoted at the intermediate `.json` layer only. None of this is
resolved here, on purpose — this stays a reviewable artefact, not a second design
document.

## Suggested next steps

- **Re-extract round 3's `sync-gateway` (13 pages) and `couchbase-lite`
  (12 pages) batches.** `verify-evidence.py` puts them at 45% and 50%
  quotable-evidence respectively, affecting 12 of 13 and 10 of 12 records —
  materially unreliable at the record level. Their vocabulary conclusions
  (the channel model, the CBL edition split) are corroborated elsewhere and
  stand; the individual triples should not be consumed downstream until
  re-run under the gate.
- **Decide the index taxonomy before promoting any index concept.** 93
  candidates are sitting unpromoted because the namespace conflates at least
  four axes (access method, storage engine, lifecycle state, syntactic form).
  Read `server/current/learn/services-and-indexes/` first — that directory is
  the docs' own attempt at the taxonomy, and inventing a different one here
  would be a fact, not an extraction.
- **Add structural schema validation to `hooks/gate-evidence.py`.** Round 10
  named two missing controls and wrote one (`verify-promotions.py`). The other
  is structural validation of extraction records — starting with "the subject
  slot must hold a concept id, not a page id," a violation round 8 introduced
  (`cascadesDeletionTo`, three occurrences) that survived its own reconciliation
  pass undetected. The hook already parses every record at write time, so this
  costs nothing extra to run and would catch such a violation at the moment
  it's introduced rather than two rounds later.
- Get a subject-matter expert to work through `docs-issues/` (55 entries) —
  most valuably the five-way "role" collision, the Sync Gateway/Capella
  access-control questions, round 5's `merge`/`nest` privilege-naming
  inconsistency (does "Query Select" = "Query Read"?), round 6's role-catalog
  loose ends (is `data-writer` the same role as the originally-mangled
  `project-data-writer`? is Capella iQ's cluster-scoped role a sixth role or
  an existing one at a different scope?), round 7's `privilege:capella-advanced-access-scope-admin`
  mismatch against `cluster-rbac.md`'s own table, and the support-plan
  wording inconsistency (now five variants) — all product-shape or
  docs-authority decisions, not just cleanup.
- Finish round 3's Java SDK promotion backlog before running any further Java
  SDK rounds — round 10 promoted `sdk:kv-operations` and re-namespaced
  `sdk:transaction-query-mode`, leaving `sdk:durability`,
  `sdk:cas-optimistic-locking`, `sdk:error-handling`, `sdk:query-error-mapping`,
  `sdk:sqlpp-queries-with-sdk`, and `sdk:bucket-management` still
  extraction-layer-only. See round 4's note in `reconciliation.md`.
- Draft the remaining JSON-LD for everything still intermediate-only across all
  ten rounds.
- Run a normalization pass over `extractions/` for the small ID inconsistencies
  the aggregation surfaced but didn't hand-fix — mechanical, scriptable, not
  worth doing by hand at this volume. Round 9 added three instances
  (`tool:cbimport`/`cbexport` vs. `server:cbimport`/`cbexport`;
  `n1ql:index-partitioning` vs. `indexes:index-partitioning`;
  `n1ql:aggregate-function` vs. `-functions`); round 10's
  `verify-promotions.py` added four more, all of which resolve to
  already-promoted concepts under a different name —
  `clusters:xdcr` → `capella:xdcr`, `n1ql:selectintro` → `n1ql:select`,
  `n1ql:updatestatistics` → `n1ql:update-statistics`,
  `plan:developer-pro` → `plan:developer-pro-support-plan` — plus the ~31
  `version:*` ids that denote only ~20 actual versions
  (`version:server-6.5` vs. `version:server-6-5`, and a bare `version:server`).
  Two of these are more than cosmetic and should be *decided*, not scripted:
  `capella:` vs. `clusters:` for XDCR is a genuine namespacing question, and
  the id drift itself turned out to be a **promotion smell** — neither spelling
  of `aggregate-function(s)` had a registry file at all.
- Decide the actual publishing mechanics for `pages/*.jsonld`.
- Resolve the `eventing:url-alias-binding`'s "no auth" open question (its
  settings table implies other auth modes exist for this binding type; none
  are documented on the pages read in round 8) and the
  `capella:index-ui-status`/`index-state` collision from round 7, if this
  registry is ever consumed downstream.
- **Run `server/current` wave 2.** `cloud/` is fully covered (rounds 5-9) and
  wave 1 of `server/current` is done; roughly 12 waves remain for that tree,
  ordered by the diff gate (see `../ingest-cost-and-time-estimate.md`, and read
  its wave-1 retrospective first — raw changed-line counts are a sort key, not
  a yield estimate). The genuinely-new registry surface is in `rest-api/`,
  `cli/`, server-side `eventing/`, `analytics/` and `xdcr/`, so plan
  reconciliation cost by registry surface touched, not page count.
- The next product-scale target after that, if continuing at this granularity,
  is a product outside `cloud/`/`server/` not yet touched at all (other SDKs,
  Analytics/Columnar, Backup, the Autonomous Operator).
- If this looks worth pursuing past a POC: ten axes of stress test have now
  been run (cross-component, cross-deployment-model, cross-product-family,
  round 4's within-one-product-across-features, round 5/6/7's three-in-a-row
  confirmation that the same partial-sampling lesson recurs on successive
  vocabularies of the same product, round 8's confirmation that a genuinely
  new feature doesn't automatically need new structure, round 9's
  confirmation that even a "should mostly confirm" round still earns its
  keep, and round 10's cross-version axis — the same product's docs at a
  second version, which is where the fabrication and the evidence-audit
  results came from). The next natural one is scale itself — a real batch
  against the ~3,900-page "latest version only" corpus from
  `../ingest-cost-and-time-estimate.md`, now that the pipeline has been
  exercised on Bedrock, at real (not just trial) scale, on every axis it's
  likely to meet at that size, and — as of round 10 — behind a mechanical
  evidence gate rather than on trust.
