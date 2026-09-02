# Linked-data POC — sample tree

A proof of concept for the approach described in
[`../linked-data-spec.md`](../linked-data-spec.md): can an LLM propose the ontology
piecemeal, page by page, well enough to be worth iterating on, rather than needing a
week of upfront ontology design?

This is a review artefact, not production output — everything here was extracted
and reconciled to see what the method actually produces before investing in
automating it. Thirteen rounds so far, twelve of them deliberate escalations and
the thirteenth a corrective pass over what they left behind:

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
11. **9 pages, `server/8.0/learn/services-and-indexes`** — deliberately small,
    and the first batch of *conceptual prose* rather than reference syntax: the
    service overview, the seven per-service pages, and the index overview. Also
    the first batch in the project's history written **entirely under the
    write-time evidence gate** — 211 relations, 0 evidence problems. Changing
    the *genre* of page turned out to matter more than changing the tree: ten
    rounds of statement syntax and REST payloads had left the registry with no
    part-whole predicate, no subsumption vocabulary at all across 195 concepts,
    no datatype properties, and no DCP — the streaming protocol the whole
    architecture rests on, absent from the first ~540 pages because reference
    documentation cannot see it. Nine pages of the other kind produced all four.
    It also resolved round 10's deferred index-taxonomy question, and not as
    expected: the docs' two schemes **cross rather than nest**.
12. **30 pages, `server/8.0/learn` wave 2** — `learn/data/` (9),
    `learn/buckets-memory-and-storage/` (8) and `learn/security/` (13), scaling up
    round 11's conceptual-prose result and aiming it deliberately at the one domain
    where ten rounds of *reference* extraction had built the registry's largest
    family. The conceptual pages contradicted it. `learn/security/roles.md` is
    Couchbase Server's authoritative RBAC catalogue — 56 roles — and **eleven ids
    sitting in `concepts/privilege/` are roles**, minted from SQL++
    `Prerequisites` sections that name the bare token without ever classifying it.
    Recurrence had made the error look well-supported rather than flagging it:
    `privilege:query-manage-index` had ten files behind it. Round 10 ruled on this
    exact question and ruled backwards, filing a docs-issue against the page that
    was correct. So this is the first round to find the vocabulary *wrong* rather
    than merely incomplete, and the corrective is an ordering rule: read a
    domain's authoritative conceptual page **before** the reference pages that
    mention its terms. Also the first wave under the required `registry_status`
    enum — 17 true positives, 0 false positives, against the prose parser's 3
    false positives in 9 pages — and the round that found the concept-promotion
    metric had been counting only object slots since round 1, hiding **276**
    candidates.
13. **No new pages** — the first round to audit the corpus against *itself* rather
    than against a new surface, working the two things round 12 exposed and did not
    finish: the promotion backlog the corrected metric revealed, and 18 clusters of
    one term spelled more than one way. The largest defect it found was in the
    registry, not in the records. Nine `concepts/version/` records declared an `id`
    contradicting their own filename (`server-6-5.json` claiming
    `.../version/server-6.5`), so the tooling derived ids from paths while agents
    copied them from `id` fields, agents were **denied by the gate for being
    correct**, and a prior reconciliation had written the whole thing up as *their*
    mistake. It also found round 12's fix was structurally half a fix: an alias is a
    statement about an id, so it can repair a wrong concept and never a wrong
    predicate — `requiresServerRole` had been minted with `recurrence: 20` and zero
    records using it. 16 concepts promoted, three aliases that existed only in prose
    made machine-readable (one recurrence 9 → 50), variant clusters 13 → 1, and two
    new controls: `verify-registry-ids.py` and `normalise-ids.py`.

See `reconciliation.md` for the full round-by-round log, findings, and a
cumulative verdict at the end. See `../ingest-cost-and-time-estimate.md` for the
time/cost projections and how they held up against the round-2 run's real numbers.

## Scope

582 pages total:

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
- **9 more, `server/8.0/learn/services-and-indexes/`** — all nine pages of the
  directory: `services.md`, the seven per-service pages, and `indexes.md`. Note
  that round 2 read *some* of `server/7.2/learn/services-and-indexes/`; this is
  the 8.0 directory read completely, and the first batch anywhere in the corpus
  that is conceptual/architectural prose rather than reference, guide or
  management-plane content. Chosen because round 10 explicitly deferred the index
  taxonomy until this directory was read — the docs' own attempt at that taxonomy
  lives here.
- **30 more, `server/8.0/learn/` wave 2** — `learn/data/` (9: the document data
  model, scopes and collections, expiration, durability, transactions),
  `learn/buckets-memory-and-storage/` (8: bucket types, vBuckets, memory and
  ejection, storage engines, compression) and `learn/security/` (13: the security
  overview, authentication and its domains, `authorization-overview.md`,
  **`roles.md`** — the 56-role RBAC catalogue — certificates, on-the-wire
  security, encryption at rest, and auditing). `learn/security/` was loaded into
  the batch deliberately: it was round 11's largest content gap, and it is the
  authoritative source for the privilege/role family the registry had built up
  across rounds 2, 5, 6, 7 and 10 *entirely from reference pages*. Reading it
  corrected that family rather than extending it — see round 12 in
  `reconciliation.md`.

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
  Round 11 promoted 25, resolving round 10's deferred index taxonomy: the
  two index **classes** (`index-class:traditional`/`vector`) as an axis
  *crossing* the type and providing-service axes rather than sitting above them,
  four index types, the two Index Service storage modes (storage mode turns out
  to be a property of the *service's configuration*, not of an index), and
  `index:index` as a deliberately coarse supertype so that the pages' many
  unqualified statements about "an index" have an honest subject. Plus
  `protocol:dcp` — the streaming protocol the architecture rests on, absent from
  the first ~540 pages and then on four of nine, folding a same-round cross-agent
  duplicate (`server:dcp-protocol`) caused by one directory naming it two ways;
  `service:backup-service`, the seventh service, which ten rounds never needed and
  which collides by name with the CSP snapshot facility in `cloud/`; the
  Multi-Dimensional Scaling family (`server:node`, `server:rebalance`,
  `server:service-memory-quota`, `server:multi-dimensional-scaling`) which has **no
  Capella counterpart anywhere** — Capella decides placement for you, so the
  ontology now holds two disjoint views of one service set joined only by the
  shared `service:*` ids; and `tool:cbbackupmgr`, folding a *second*
  three-namespace split of a single CLI tool (`tool:cbq-shell` was the first).
  It also paid down the corpus's highest-recurrence promotion debt, found by the
  whole-corpus query rather than by reading this round's records:
  `capella:collection` (14), `capella:scope` (13), `capella:bucket` (13),
  `capella:cluster-access-credentials` (13) — the data hierarchy, unpromoted
  since round 6/7 for exactly the reason round 10 identified, that recurrence 14
  is load-bearing but not *interesting*.
  Round 12 promoted 55 and, for the first time, **re-filed** rather than only
  added - 66 concept records in all, once the eleven re-filings are counted. Eleven `privilege:*` ids that `learn/security/roles.md` documents as
  *roles* moved to `concepts/role/`, keeping the old ids in each record's
  `aliases` — which is the point, not a courtesy: an agent reusing
  `privilege:query-delete` and truthfully declaring it `extraction-layer` passes
  the write-time gate, so an aliased promoted record is the only thing that turns
  the category error into a gate denial. Five of the eleven are at recurrence 1
  and promoted on that reasoning alone. `concepts/privilege/` now holds **exactly
  Capella's 28-member catalogue and zero non-Capella entries**, matching the
  evidence that Capella has the corpus's only enumerable privilege tier. The new
  families: the abstract `rbac-model:role`/`privilege` layer, kept separate from
  the concrete `role:*` catalogue precisely so the registry can record that
  Server's docs define a privilege tier and never name a member of it;
  `auth-domain:local`/`external`; `auth-mechanism:*`; `idp:ldap`/`saml`/
  `ldap-group` (deliberately *not* merged with Capella's `sso:*` family — they
  federate to an external directory for structurally different downstream
  authorization models); the four `security:*` facilities from
  `security-overview.md`'s own bullet list; the `cert:*` chain and `tls:*` wire
  settings; `encryption:*` (whose `master-password` carries an explicit "not a
  user credential" clause — the one password-shaped term here that isn't a
  login); the `data:item`/`document`/`attribute` model (item and document are a
  superset/subset pair, not synonyms, because an item's value need not be JSON);
  and the buckets/memory/storage family, including the five-member
  `memory:ejection-policy` enum whose value sets are **disjoint by bucket type** —
  a conditional-enum structure the registry has no predicate for and records as a
  modelling gap. `role:admin` was folded into `role:full-administrator` (three
  display labels, one internal name `admin`, which is the join key), removing the
  below-bar exception that record was originally promoted under. Also promoted a
  four-way parallel-namespace set — `server:bucket`/`scope`/`xdcr`/
  `cluster-manager` alongside the existing `capella:*` four — and left the split
  standing after searching `cloud/` for a statement that the constructs are the
  same and finding none, but with a better reason than absent evidence: Server's
  bucket has a type, ejection policy, storage engine and memory quota, while
  `capella:bucket` asserts only that it is the top of a hierarchy. That is the
  difference between a construct you configure and one you navigate. Three ids
  reaching recurrence 2 were refused as **literals, not concepts** (`1`, `1%`,
  `10%`), and `relational:table` was refused as a foreign-domain term this
  ontology does not own.
  Round 13 promoted 16 with no new pages read, all of them debt the corrected
  metric or the variant sweep had been hiding. The eight-member SQL++ function-role
  family (`role:query-manage-global-functions` and siblings) is filed under each
  role's **internal name** from `roles.md`, with the display label in `aliases` —
  now a written convention rather than a habit, because the label is not a stable
  key: 20 of the 55 role tables have a label word absent from the internal name and
  8 share no word at all (`Application Access` is `bucket_full_access`), so ids
  minted from the two names can never be clustered by spelling. Four of the eight
  are at recurrence 1 and promoted under the family exception. Also
  `role:data-reader` (3, aliasing `rbac-role:data-reader`), `n1ql:curl-function`
  (2), `n1ql:explain-function` (7) and `n1ql:create-sequence` (3), and three
  versions — the last five were sitting *below* the promotion bar only because
  their counts were split across two spellings, which is the quiet half of the
  variant problem: a promoted term reading as unpromoted is loud, a real candidate
  held under the bar shows up as nothing. Three records whose `note` described a
  fold and whose `aliases` array had never been written got one, which moved
  `cluster-access-credential-type` from recurrence 9 to **50**, `sso:realm` from 8
  to 12, and `plan:free-tier-plan` from 2 to 14. Four refusals are recorded:
  `n1ql:curl-function` is not `eventing:curl-function` and `role:data-reader` is
  not `capella-role:data-reader` (different service, different control plane —
  shared names only), while `role:administrator` and `rbac-role:data-admin` name
  nothing in the 56-role catalogue and became docs-issues rather than concepts.
  And `role:query-use-sequences`, promoted in round 12 as "Manage Sequences", was
  relabelled: `roles.md`'s own table heading is wrong (the internal name is
  `query_use_sequences` and the permission table grants `execute`), so the record's
  `evidence` quotes verbatim a line that is false. Every control passed it — the
  sharpest instance yet of "a green check is not a green record", because correct
  extraction of an incorrect source is indistinguishable from correct extraction.
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
  Round 11 added 23 and closed three structural gaps at once. **Part-whole:**
  `hasInternalComponent` — 15 of `data-service.md`'s 30 relations decompose the
  KV engine into named components, and after ten rounds the registry had no way to
  say "X is part of Y." **Subsumption:** `isSubtypeOf` and `belongsToIndexClass`,
  the registry's first taxonomic predicates; nothing across 195 concepts and 64
  predicates could previously say "X is a kind of Y," because reference
  documentation states behaviour and parameters, not taxonomy. The two are kept
  deliberately separate so the crossing index axes cannot be silently collapsed
  later. **Datatype properties:** ten rounds produced only object properties;
  `requiresMinimumNodeCount` (integer) and `hasInternalServiceIdentifier` (string —
  a 7-member mapping from each service to its wire id: `kv`, `n1ql`, `index`,
  `fts`, `cbas`, `eventing`, `backup`) are the first predicates whose objects are
  literals by design, which the JSON-LD drafting step has not yet had to handle.
  The rest: `usesProtocol` (folding the same-round duplicate
  `streamsMutationsVia`), `usesExecutionModel`, `providesIndexType`,
  `configuredPerNode`, `offersConfigurationChoice`, `mayDelegateOperationTo`, the
  MDS family (`providesService`, `requiresMemoryQuota`, `exemptFromMemoryQuota`,
  `requiresCoDeployedService`, `requiresDedicatedNode`), and four earlier-round
  debts at recurrence ≥3 (`createsOnAction`, `hasHandler`, `firesCallback`,
  `cascadesDeletionTo`). Two carry recorded caveats rather than being quietly
  cleaned up: `requiresDedicatedNode` is minted from a page that says "should,"
  not "must" — the predicate name is stronger than its evidence — and
  `servesService` carries a CONTRADICTION WARNING, because two pages in the same
  directory disagree about which service indexes Analytics data. And `seeAlso` is
  filed at recurrence **425** purely to document a distortion: its objects are
  *pages*, not concepts, which silently invalidated this round's first
  concept-recurrence ranking (documentation pages outranked every real concept).
  Kept separate from `concepts/` on purpose —
  properties and the instances they connect are different layers of an ontology
  (roughly, RDFS/OWL's "TBox vs ABox" split), and blurring them makes the JSON-LD
  `@context` harder to design cleanly.
  Round 12 added 10. `requiresServerRole` (recurrence 20) is the other half of the
  privilege-to-role re-filing: `requiresPrivilege`'s declared range is a privilege
  and it was pointing at eleven roles across 20 files. `requiresRole` was
  **rejected** for reuse — its own record defines it as Sync Gateway's
  sync-function `requireRole()` check — so there are now three structurally
  distinct "requires a role" predicates, each record saying why it is not the
  other two. `hasPrivilege` is promoted **for what it does not contain**: all
  three occurrences are the identical abstract `rbac-model:role hasPrivilege
  rbac-model:privilege` glossary claim, with zero concrete instances anywhere in
  the corpus, because all 55 permission tables in `roles.md` express permissions
  as prose ("Can list buckets.") rather than as named privileges. Promoting it
  makes that absence queryable instead of merely described. `verifiesIdentityOf`
  is the certificate family's core predicate and the reason the promotion metric
  changed this round — all four of its triples have `cert:trust-store` as
  *subject*, so object-only counting could not see the mechanism at the centre of
  the family. `isAnalogousTo` carries an unusually strong warning in its own type
  description, because its entire purpose is to record a comparison the docs draw
  for pedagogy (collections explained as relational tables) and a consumer reading
  it as identity would conclude Couchbase has tables. The rest:
  `hasDefaultValue`, `takesPrecedenceOver` (a bucket-level max TTL silently
  capping a longer per-item one — the class of fact that surprises an
  administrator in production), `scopedToKeyspace`, `requiresCapability` (motivated
  by the sharpest cross-family fact of the round: `persistToMajority` needs disk
  persistence, which ephemeral buckets lack, so a bucket-type choice silently
  removes a durability level), `hasMinimumMemoryToDataRatio` (kept separate from
  `hasDefaultValue` on purpose — a minimum *requirement* and a *default* are
  different claims, and folding them would make the registry state that 1% is
  Magma's default memory ratio, which is not what the page says), and
  `monitoredVia`. One relation was deliberately consumed rather than kept:
  an agent correctly reused the already-promoted `isSynonymOf` (round 2, recurrence
  4) to link `role:admin` and `role:full-administrator`, and reconciliation folded
  that into an alias instead of retaining the triple — synonymy between two ids
  naming one role is a registry artefact to resolve, while synonymy between two
  distinct statements, which is what `isSynonymOf` was promoted for, is a fact
  about the product.
  Round 13 added one — `requiresPrivilege`, which had a `.jsonld` file and no
  `.json` sibling, so the one place a record says *what it must not be used for*
  did not exist for the predicate whose misuse round 12 was about — and corrected
  two. `requiresServerRole` was minted in round 12 with `recurrence: 20` while
  **no extraction record used it at all**; the 20 counted the files that *should*
  have. It is now a real 43 files / 76 occurrences, and carries
  `recurrence_at_minting: 0` so the discrepancy is on the face of the record. The
  reason round 12 left it unused is a limit of its mechanism rather than an
  oversight: an alias is a statement about an id, so it repairs a wrong concept and
  never a wrong predicate — `requiresPrivilege` could not be aliased into
  `requiresServerRole` because 48 files use it correctly for Capella's genuinely
  separate catalogue. Round 13 also found the error was a species deeper than
  measured: alongside 38 `requiresPrivilege` occurrences pointing at roles, **18
  Server and Capella records used `requiresRole`** — Sync Gateway's sync-function
  check — to mean "must hold this Server RBAC role", and had neither marker round
  12's sweep keyed on. `requiresRole` is now down to 5 occurrences in 3 files, of
  which 3 are deliberately left wrong: their objects are `rbac-role-category:*`,
  and neither predicate's range admits a role *category*, so minting
  `requiresServerRoleInCategory` for 3 occurrences in one file would be minting
  vocabulary to avoid recording an open question.
- **`docs-issues/`** — a deliberately minimal, deliberately promiscuous log of
  content-quality findings (missing documentation, apparent doc-duplication,
  unadapted shared-source content, empty stub pages) that are *about the docs*,
  not about Couchbase — kept separate from `concepts/` and `relations/` so the
  product ontology doesn't grow a parallel meta-ontology of
  documentation-about-documentation. Each entry is just `{id, type: "docs-issue",
  issueType, description, about, status}` — minted with no gatekeeping. **98
  entries** as of round 13, which added 4 and rewrote 1 — the rewrite being the
  more useful half: `server-role-label-does-not-match-internal-name` claimed 2
  instances where there are **20 of 55**, had inherited round 12's "58 role tables"
  (the heading count, not the table count — 55 tables, 56 roles, one in prose only),
  and diagnosed the Manage/Use Sequences case backwards. An unmeasured docs-issue is
  a hunch with a filename. Round 11 had 76 entries, having added 21 from just
  **9 pages** — by far the highest rate
  per page of any round, because conceptual prose makes claims that can
  contradict each other in a way syntax tables cannot. Round 11 also introduced
  an optional `severity` field, used so far for two values: `needs-sme` for the
  two findings genuinely undecidable from the pages (which service creates
  Analytics indexes; whether "arbiter" and "serviceless node" are the same
  thing), and `tooling` for a snapshot-conversion bug rather than an authoring
  one. Round 10 added 22 — and not
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
  thinning check now in the `linked-data-reconcile` skill, and hence
  `hooks/gate-log.jsonl` below.
  Round 11 is the first batch written entirely under it, and the result is mixed
  in a way worth reading before trusting the gate: the omission failure mode
  **did not occur** (both denied records came back at the same relation count),
  but **all three flagged ids were false positives** — none on the evidence
  check, all on the registry-status check, which parses English prose, and two
  agents hit them independently in nine pages. The check now reads only the
  leading clause of `reused_or_minted`, and then, immediately after round 11
  closed, stopped parsing prose altogether: **`registry_status` is now a required
  enum** (`promoted` / `extraction-layer` / `minted`) on every concept *and* every
  relation, checked against the registry with aliases resolved. The ~40 lines of
  clause-splitting and negation-detection are deleted, and the false-positive
  shapes are structurally impossible rather than mitigated. The prose note stays
  in the schema — it tells a reviewer things an enum can't — the gate just doesn't
  read it. Two controls fell out for free: declaring `minted` for something the
  registry already promotes is now refused (the failure that re-created
  `requiresMinVersionFor` after it was folded into `availableSince`), as is
  declaring `extraction-layer` for a promoted term, which means the registry was
  never checked. Enforced in the hook only, never in `verify-evidence.py`: the 552
  records already on disk predate the field, nothing rewrites them, and a corpus
  audit with a permanently red baseline stops being read. Anything aggregating the
  corpus must treat a missing value as *unknown*, never as `extraction-layer`.
  Note also what a scoreboard of 0 true positives cannot tell you: whether
  the gate *deterred* fabrication, or whether none was attempted.
- **`hooks/gate-log.jsonl`** — the gate's own append-only verdict log
  (gitignored: it grows on every write and would conflict on every merge; when a
  line in it is a finding, it gets quoted into `reconciliation.md`, which is the
  durable record). It exists because the gate had enforcement and no
  *instrument*: hook stderr on exit 2 reaches the calling **subagent**, not the
  coordinator, so a denial was only ever visible through the same self-report
  channel that let round 10's fabrication through as a confident summary. It logs
  every verdict including allows — an unlogged clean wave is indistinguishable
  from a wave where the hook never fired — and records `n_relations`, which is
  what makes the omission failure mode visible: `deny(n=13) → allow(n=12)` on the
  same path means the agent dropped a relation rather than sourcing it, where
  `deny(13) → allow(13)` means it went and found the quote. In round 11 it
  surfaced a denial roughly six minutes before the agent that hit it reported.
  The generalization, extending round 10's: **agent self-report is a hope; a log
  written by the gate itself is a control.**
- **`registry-digest.py`** — prints the promoted registry as compact tables for
  extraction-agent prompts, run by the agents themselves at dispatch time rather
  than pasted into a briefing, so it cannot go stale — the failure that got
  `requiresMinVersionFor` re-minted after having been consolidated. It prints each
  term's description *in full* rather than truncating, because that line is where
  a record says what it must not be confused with, and surfaces every recorded
  do-not-confuse warning verbatim in its own section (19 of them as of round 11).
  Worth recording that its first version committed the exact failure it was built
  to prevent: merging each term's files newest-wins let terse `.jsonld` records
  shadow rich `.json` ones, printing `availableSince | rdf:Property` with the
  predicate's shape dropped. A `.jsonld` file and its `.json` sibling are not
  supersets of each other, so it now keeps all of a term's files and takes the
  most informative value across them.
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
- **`recurrence.py`** — the aggregate query the whole promotion rule rests on:
  distinct-file counts per predicate and per concept over the entire
  `extractions/` tree, resolving aliases and both id spellings, with
  `--unpromoted-only` for the backlog, `--variants` for ids that are one term
  spelled two ways, and `--findings` to dump the finding fields in full. It has
  been wrong in eight distinct ways across rounds 10–13, every one caught because
  the output looked implausible and none by anyone reading the code, so all eight
  are pinned as regression cases in `--selftest` (17 checks) — the point being that
  its corrections accumulate rather than being re-derived from memory each round.
  The worst was structural rather than a bug: until round 12 it counted only the
  **object** slot, so any concept a page was *about* was invisible to the promotion
  signal, which had hidden 276 candidates since round 1.
- **`verify-registry-ids.py`** — a **gate** (exits non-zero), written in round 13:
  every record's declared `id` must mirror its own file path. 514 records, 0
  mismatches. It exists because nine `concepts/version/` records had drifted
  (`server-6-5.json` declaring `.../version/server-6.5`) and the consequence was
  not cosmetic: the pipeline derives ids from **paths** while agents copy them from
  **`id` fields**, so agents wrote the dotted form, the write-time gate denied them
  as unpromoted, and the term landed in the backlog with nothing indicating the
  registry had caused it. Two agents diagnosed it correctly in their notes and a
  reconciliation pass recorded it as *their* error. `pages/*.jsonld` is excluded:
  its `@id` is the described page's public URL, a resource the registry names and
  does not own — the rule is about ownership, not about strings.
- **`normalise-ids.py`** — the odd one out on this shelf, and the only one that
  **writes**. It rewrites wrongly-spelled ids and mis-ranged predicates in the
  extraction records (dry run by default, `--apply` to commit, idempotent). Its
  docstring carries the decision that turns `--variants` output into action:
  **alias** when the variant is a defensible alternative name (a different
  namespace, a display label against an internal name) — additive, forward-only,
  and it converts future reuse into a gate denial; **rewrite** when the variant is
  not a legitimate name for the thing anywhere (`version:server-6.5`,
  `n1ql:createfunction`), because aliasing a typo enshrines it as vocabulary. It
  also reaches the case aliasing cannot: an alias maps one id to another, so it can
  repair a wrong concept and never a wrong **predicate**. Because it uses plain
  file I/O it **bypasses `hooks/gate-evidence.py`**, which is stated plainly rather
  than buried; it is safe because it touches only `subject`, `predicate`, `object`
  and `candidate_id` — never `evidence`, `evidence_source`, `page_id`,
  `source_path` or `registry_status` — so a rename cannot make a quote stop
  matching a page. The compensating control is a before/after `verify-evidence.py`
  over the whole corpus: 582 records, 3,522 relations, 452 problems, identical
  across 151 substitutions in 67 files.
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

**Round 11 (9 pages, `server/8.0/learn/services-and-indexes`) — the round where
the *kind* of page mattered more than the tree:**

47. **Extracting a directory is not extracting a genre.** Round 5's lesson was
    that a fifth of a directory doesn't generalize to the directory. This is a
    level up. Ten rounds of reference, guide and management-plane pages left the
    registry with no part-whole predicate, no subsumption vocabulary at all
    across 195 concepts, no datatype properties, and no DCP — and none of those
    absences was caused by insufficient coverage. Nine hundred more reference
    pages would not have surfaced any of them, because reference documentation
    describes what a *user writes* and conceptual documentation describes what
    the *machine does*. Nine pages of the second kind produced all four. Also
    denser: 23.4 relations per page against round 10's 13.4, which is the
    opposite of what ten rounds of reference extraction would predict.
48. **DCP was absent from the first ~540 pages, then appeared on four of nine.**
    The protocol by which the Data Service feeds mutations to the Index, Search
    and Analytics services and to other clusters — arguably the most load-bearing
    internal mechanism in the architecture — is invisible to statement syntax and
    REST payloads, because nothing a user writes names it. Two agents in one wave
    minted it independently in two namespaces with identical labels, which is the
    textbook cross-agent duplicate; the immediate cause is a docs bug, one page
    writing "the DCP protocol" without expanding it and another "Database Change
    Protocol" without abbreviating it, neither linking the other.
49. **The index taxonomy has two axes that cross, and the natural reading is
    wrong.** Round 10 deferred all 93 index concepts pending this directory.
    `indexes.md` declares "two classes of indexes" (Traditional and Vector) and
    then organises its content by index *type* and *providing service* — and the
    schemes do not nest. A Search index is Traditional while a Search Vector index
    is Vector, so class cuts across service; a Composite Vector Index is stated to
    *be* a GSI, so class cuts across type. A reader building a hierarchy from this
    page builds one the page's own examples refute. This is a distinct outcome
    from round 10's diagnosis: the problem was never that the docs had one clean
    taxonomy the extraction had flattened — the docs have two real axes and never
    say so.
50. **A contradiction between two pages in the same directory, undecidable from
    either.** `services.md` says the Index Service maintains indexes for Query,
    Search *and Analytics*; `indexes.md` attributes Analytics indexes to the
    Analytics Service. The extraction records both with a CONTRADICTION WARNING
    rather than picking a winner, and the docs-issue is the first marked
    `severity: needs-sme`. The three-way duplication logged alongside it is *how*
    this happens: the same service descriptions live in `services.md`, in each
    service's own page, and in Capella's feature descriptions, and they are not
    identical.
51. **Two disjoint views of one service set, joined only by ids.**
    Multi-Dimensional Scaling — each service independently placeable, quota'd and
    scalable — is the load-bearing concept of `services.md` and has **no Capella
    counterpart anywhere in ~180 management-plane pages**, because Capella decides
    placement for the user. So `server/` sees deployable components with topology
    and Capella sees a managed feature list, sharing only the `service:*` ids. The
    seventh service (Backup) is a smaller instance of the same asymmetry: ten
    rounds never needed it, "which services does Couchbase have" answers six or
    seven depending on which tree was ingested, and `cloud/`'s single occurrence
    of the phrase "backup service" refers to the cloud provider's snapshots — the
    fifth documented name collision and the first to span products.
52. **The gate held; its own worst failure mode didn't fire; and every denial was
    a false positive.** First batch written entirely under
    `hooks/gate-evidence.py`: 11 gated invocations, 9 allowed, 2 denied, both
    denied records returning at the *same* relation count, so the
    fabrication-becomes-silent-omission risk demonstrably did not materialise, and
    corpus evidence problems stayed at 452 — all pre-gate. But all three flagged
    ids were false positives, all on the registry-status check parsing English,
    hit by two agents independently in nine pages. Reported as a scoreboard of
    0 true positives and 3 false positives, with the honest caveat that one clean
    wave cannot distinguish deterrence from an absence of attempts.
53. **A high-recurrence predicate can silently invalidate the promotion rule.**
    The first concept-recurrence ranking of this round put documentation *pages*
    above every real concept, because `seeAlso` occurs 425 times and its objects
    are pages. Excluding them cut the candidate list from 465 to 356 and changed
    what got promoted. The rule counts object recurrence and assumes objects are
    concepts; one predicate breaks that assumption at 425 occurrences.
54. **A tool built to prevent a failure committed it.** `registry-digest.py`
    exists so no agent is handed a stale registry table, and its first version
    printed `availableSince | rdf:Property` with the predicate's shape dropped —
    a stale table, generated fresh, by the anti-staleness tool. Third instance of
    "vigilance is not a control," and, like round 10's regex bug, invisible in the
    code and obvious in the output.

**Round 12 (30 pages, `server/8.0/learn` wave 2):**

55. **The registry had eleven roles filed as privileges, and recurrence argued
    for the error.** `learn/security/roles.md` is Couchbase Server's authoritative
    RBAC catalogue (56 roles, 55 with machine-readable
    `| Role: <label> (<internal_name>)` tables). Eleven ids in
    `concepts/privilege/` have their own sections in it — `query-select` (6 files),
    `query-manage-index` (10), `query-system-catalog` (5), `fts-admin` (4) and
    seven more. All were minted from SQL++ statement and monitoring pages whose
    `Prerequisites` sections name the bare token (`query_manage_index`) without
    ever classifying it, and ten rounds of reference extraction reinforced the
    guess by repetition. **The wrong answer was the well-evidenced one.**
    Recurrence measures how often a token appears; it has no way to check what
    kind of thing the token is, and here it ranked the error at the top of the
    corpus. This is the first round to find the vocabulary *wrong* rather than
    incomplete.
56. **The genres do not merely differ — where they overlap, they disagree, and
    the reference genre gets there first.** Round 11 established that page genre
    predicts vocabulary. Round 12's sharper version: reference documentation is
    higher-volume and earlier in any sane coverage plan, so its category errors
    arrive first and then accumulate evidence. The corrective is an ordering rule
    rather than more coverage — read a domain's authoritative conceptual page
    *before* the hundred reference pages that mention its terms. `learn/security/`
    was picked to fill a content gap and instead corrected the registry's largest
    family.
57. **Round 10 ruled on this exact question and ruled backwards.** Its section
    states that `query-system-catalog` and `query-manage-system-catalog` "are
    privileges, not roles," moving both *out* of a role namespace and *into* the
    wrong one, and filed a docs-issue against `metafun.md` for calling the token a
    role. `metafun.md` was right. Two bullets later the same round wrote the
    correct rule — "`role:` is the Server RBAC namespace… genuine Server RBAC role
    names documented in `server/current/learn/security/roles.md`" — and did not
    apply it, because nobody had read `roles.md`. The surviving record also cited
    a "round-6 precedent" for the fold that **does not exist**. Three layers of
    error in one place, all corrected in place with the original text retained.
58. **Server documents a two-tier access model whose second tier has no
    members.** `security-overview.md` says users are assigned roles "these
    themselves corresponding to system-defined _privileges_", and
    `authorization-overview.md` defines both tiers. No page in 570 pages names a
    single Server privilege: all 55 permission tables in `roles.md` express
    permissions as prose ("Can list buckets."). `hasPrivilege` is therefore
    promoted **for what it does not contain** — three abstract occurrences, zero
    concrete instances — so the absence is queryable rather than merely described.
    Capella, by contrast, has a real 28-member catalogue, which is why
    `concepts/privilege/` is now exclusively Capella's.
59. **The concept-promotion metric had been biased since round 1, hiding 276
    candidates.** Concept recurrence was counted from the *object* slot only,
    which cannot see a concept a page is *about* — those are subjects.
    `cert:trust-store` is the subject of all four `verifiesIdentityOf` triples and
    an object once, so the mechanism at the centre of the certificate family
    scored 1. Counting either relation slot, the corpus holds **276 unpromoted
    concepts at recurrence ≥ 2**, including `search:customize-index` at 7 — a
    larger backlog than round 10's `n1ql:query-context`-at-22 discovery, and
    invisible for the same reason: nine rounds of scrutiny went to the extraction
    records and none to the query aggregating them. Question the query, not just
    the data.
60. **A required enum beat a prose parser outright.** First wave under the
    `registry_status` enum: 43 gated invocations, 31 allow / 12 deny, 37 problems
    — **17 on `registry_status`, all 17 true positives, zero false positives**,
    against round 11's prose parser scoring 3 false positives in 9 pages.
    Removing the English removed the class of failure rather than narrowing it.
    One denial refused an agent declaring `availableSince` **minted** — the exact
    historical failure the whole registry-digest control exists because of — at
    write time rather than two rounds later. The dominant error was unpredicted:
    11 of 17 are agents tracking promotion status correctly for concepts and
    forgetting predicates need it too, which belongs in the prompt template.
61. **Promotion can be a control point, not only a conclusion.** The
    misclassification was contagious: an agent reusing `privilege:query-delete`
    and truthfully declaring it `extraction-layer` passes the gate, because the
    claim about the registry is true. A promoted `role:` record that *aliases* the
    `privilege:` form converts that silent reuse into a denial. Five of the eleven
    ids are at recurrence 1 and promoted on this reasoning alone. A correction in
    a reconciliation log is a hope; the same correction in an aliased registry
    record is a control.
62. **A "needs an SME" verdict can be a coverage gap in disguise, and resolving
    a collision can *create* a promotion.**
    `docs-issues/search-admin-fts-admin-role-overlap` sat open from round 2
    carrying the note that it "needs a subject-matter expert, not more
    extraction." One line of `roles.md` answered it. The split had also cost a
    real promotion — `privilege:fts-admin` (1 file) and `privilege:search-admin`
    (3) each sat below the bar while the single role they both name clears it at
    4. Collisions suppress recurrence, so deduplication feeds the promotion signal
    rather than merely tidying it.
63. **Six green checks passed over a ten-file-deep category error.** The gate
    allowed every record (each `registry_status` claim was true),
    `verify-evidence.py` passed (the quotes were on the pages),
    `verify-promotions.py` passed (the ids resolved to files), and
    `recurrence.py` ranked the error first. Every control checks *form*; none
    checks *reading*. The scripts are worth having because they free the attention
    that reading requires — not because they replace it.

**Round 13 (no new pages) — the first audit of the corpus against itself:**

64. **The registry was the source of the drift it had been blaming on agents.**
    Nine of thirteen `concepts/version/` records declared an `id` contradicting
    their own filename: `concepts/version/server-6-5.json` claiming
    `.../version/server-6.5`. The pipeline derives ids from **paths**; agents copy
    them from **`id` fields**. So the tooling believed `version:server-6-5` was
    promoted, agents wrote `version:server-6.5`, the write-time gate **denied them
    for being correct**, and the term landed in the unpromoted backlog with nothing
    indicating why. Two extraction agents diagnosed it precisely in their own notes
    — "the registry file's `id` field uses the dot form while the filename uses
    hyphens … reconciliation must pick one" — and a reconciliation pass overruled
    them, recording the dotted spellings as *their* mistake. A wrong authoritative
    record teaches every future agent to be wrong, and their correctness registers
    as debt. Now checked by `verify-registry-ids.py` (514 records, 0 mismatches),
    because the reconcile skill had required this since round 1 and nothing
    enforced it.
65. **An alias repairs a wrong concept and can never repair a wrong predicate.**
    Round 12's additive fix was structurally half a fix, and nothing about the
    result looked unfinished. `requiresPrivilege` could not be aliased into
    `requiresServerRole` because 48 files use it correctly for Capella's separate
    catalogue — aliasing a predicate two products use for two things corrupts the
    correct users to fix the incorrect ones. So the new predicate was minted with
    `recurrence: 20` against **zero records using it**, the 20 counting files that
    *should* have. It is now a real 43/76. Round 13 also found the error one species
    deeper: 18 Server and Capella records used `requiresRole`, Sync Gateway's
    sync-function check, and carried neither marker round 12's sweep keyed on. When
    a correction has a concept half and a predicate half, they need two mechanisms.
66. **A recurrence figure has to say which question it answers.** Everywhere in the
    registry `recurrence` means "distinct files that use this term" — except on that
    one record, where it meant "files that should", in the same field, with nothing
    to distinguish them. More broadly the field is true when written and never
    recomputed, so across 100-odd records it mixes current counts with historical
    ones. Flagged rather than mass-updated, because a bulk rewrite would be guessing
    at the intent of records from eleven rounds.
67. **The loud half of a variant problem hides the quiet half.** A promoted term
    read as unpromoted is loud — it shows up as a big number in the backlog. A
    genuine candidate held *below* the promotion bar because its count is split
    across two spellings shows up as nothing at all. Five terms had silently
    suffered it, including `n1ql:explain-function` at recurrence 7, split between
    `explainfunction` and `explain-function` and invisible to every round.
    Variant clusters went 13 → 1. Note the limit: `--variants` keys on typography,
    so it catches `createfunction` and never `Application Access` vs
    `bucket_full_access` — the reason role ids are now filed under internal names,
    not display labels.
68. **A record can be correct extraction of an incorrect source, and no control on
    this shelf can tell.** `role:query-use-sequences` was promoted as "Manage
    Sequences" because `roles.md`'s table heading says so; the internal name is
    `query_use_sequences` and the permission table grants `execute`, so the heading
    is wrong. The record's `evidence` therefore quotes, verbatim, a false line. The
    gate passed it, `verify-evidence.py` passed it, `verify-promotions.py` passed
    it, and all three were right. This is the sharpest form of "a green check is not
    a green record": not a mis-read quote, but a faithful one. The only checks that
    reach it are a second source or someone who knows the product.
69. **Three notes claimed a consolidation and none of them was machine-readable.**
    Round 12's aliasing mechanism only works if the alias is actually written, and
    three records described a fold in prose with no `aliases` array — so the folded
    ids' files stayed in the backlog and any agent reusing the old form would have
    been denied for declaring something true. Recording them moved
    `cluster-access-credential-type` from recurrence 9 to **50**. Two of the three
    were written in the same round, which makes it a gap in the procedure rather
    than three oversights: nothing checked that a note claiming a fold was backed by
    an entry. `--variants` is now that check, run every round.

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
- **Finish the index taxonomy now that its axes are known.** Round 11 read
  `server/8.0/learn/services-and-indexes/` and settled the shape round 10 was
  waiting on: two index *classes* crossing the type and providing-service axes
  rather than sitting above them, plus storage mode as a property of the Index
  Service's configuration and lifecycle state as a fourth, separate axis. Twelve
  index concepts and the two class terms are promoted; the bulk of round 10's 93
  candidates still are not, and can now be sorted by axis rather than deferred.
  The remaining judgement call is `index-type:gsi` vs
  `index-type:secondary-index` — the docs state on two pages that these are the
  same thing, so they are linked by `isSynonymOf` rather than collapsed, and
  whether to keep both surface terms permanently is a decision, not a cleanup.
- **Fix the three gaps round 12's enum wave exposed.** The enum itself is
  settled — 17 true positives, 0 false positives across 43 invocations, and agents
  did *not* default to `promoted` as feared. Three follow-ups remain, in order of
  cheapness. (a) Tell agents explicitly that **predicates need `registry_status`
  too**: 11 of the 17 denials are that single uniform slip, not a judgement
  failure, so it is a prompt-template fix. (b) Make the hook log `n_relations`
  **even when JSON parsing fails** — it currently logs `None` on exactly the
  malformed writes, so the thinning check is blindest where it most needs to see.
  (c) Add the benign-mode caveat to the reconcile skill's thinning heuristic:
  `allow → deny → allow` with fewer relations is the documented fabrication-becomes-
  omission signal, and round 12's only instance was a correctly-dropped relation.
  Only reading the page distinguishes them.
- **Work the remaining backlog by namespace, not by rank.** Round 12's corrected
  metric exposed 276 unpromoted concepts at recurrence ≥ 2; rounds 12 and 13 took
  it to **206**, and the shape matters more than the number — the highest remaining
  is `eventing:eventing-storage` at **8**, so the double-digit debt is fully
  cleared and what is left is a long tail. That tail wants a coherence pass per
  namespace rather than promotion by rank, because the question that held back 93
  index concepts applies directly: `vector-index:` has two members at 6 and no
  promoted parent, `backup:` has two at 5. `recurrence.py --unpromoted-only --min 2`
  is the worklist. Note the 18 unpromoted **predicates** at ≥2 are a different job:
  the top one, `requiresMinVersionFor` (5), was folded into `availableSince` in
  round 2 and re-minted since, so it needs a fold, not a promotion. And roughly 15
  `sgw:`/`cbl:` tail items are not promotable at all until round 3's two trees are
  re-extracted.
- **Add a variant ratchet to the gate.** Round 13 took the variant clusters from 13
  to 1 (the survivor is the `1`/`1%` literal pair, which is the object-typing
  question below, not a spelling one) and wrote the alias-vs-rewrite rule down in
  `normalise-ids.py`. What is still missing is prevention: a gate check that refuses
  a *new* id which is a punctuation-variant near-miss of a promoted one. It needs a
  minimum-length guard — `variant_key` produced a degenerate `"1"` cluster on its
  first run — and it cannot catch the synonymy case at all (`Application Access` vs
  `bucket_full_access` share no substring), which is exactly why the role-id
  convention had to be written into the reconcile skill instead. This is the
  cheapest remaining control and the one that would make round 13's cleanup stay
  clean.
- **Add `object_type: concept | literal` to the extraction schema.** Round 12
  promoted two predicates (`hasDefaultValue`, `hasMinimumMemoryToDataRatio`) whose
  objects are usually literals, and had to exclude `1`, `1%` and `10%` from
  promotion **by hand** because the schema has a single `object` field with no type
  distinction — so a default of `1%` is recorded as an id indistinguishable from
  `bucket:ephemeral-bucket`. This compounds with the datatype-property gap round 11
  found in the JSON-LD layer; both want fixing together.
- **Give the registry a way to state a conditional value set.**
  `memory:ejection-policy` is one named setting whose legal values are **disjoint
  by bucket type** — Couchbase buckets choose value-only or full ejection,
  ephemeral buckets choose no-ejection or eject-when-full. `usesEnum` cannot
  express that, so round 12 recorded it as a modelling gap and promoted all five
  members rather than publishing a partial enum. Worth solving properly before the
  next configuration-heavy directory, since settings whose options depend on
  another setting's value will not be rare.
- **Extract deliberately by genre, not just by directory.** Round 11's clearest
  result is that nine pages of a *different kind* of documentation produced four
  structural gaps that ten rounds of reference pages could not. The remaining
  `server/` waves should include conceptual/architectural directories on purpose
  — `learn/clusters-and-availability/` is the largest remaining one, now that
  round 12 took `learn/data/`, `learn/buckets-memory-and-storage/` and
  `learn/security/` — rather than treating them as leftovers to be swept up after
  the reference tree, and the same question should be asked of `cloud/`, which was
  covered completely but almost entirely as management-plane and guide content.

  Round 12 turned this from a coverage preference into an **ordering rule**, and
  that is the part to carry forward. The genres do not merely cover different
  ground; where they overlap they disagree, and the reference genre is louder and
  earlier, so its category errors accumulate evidence before the page that would
  correct them is ever read. Eleven roles spent ten rounds filed as privileges for
  exactly this reason. So: for each domain, read the authoritative conceptual page
  **first**. The concrete next instance is
  `learn/clusters-and-availability/`, which is the authority for the
  failover/rebalance/availability vocabulary that rounds 10 and 11 have already
  been minting from reference and service pages — the same setup that produced the
  privilege/role error, one domain over.
- **Add structural schema validation to `hooks/gate-evidence.py`.** Round 10
  named two missing controls and wrote one (`verify-promotions.py`). The other
  is structural validation of extraction records — starting with "the subject
  slot must hold a concept id, not a page id," a violation round 8 introduced
  (`cascadesDeletionTo`, three occurrences) that survived its own reconciliation
  pass undetected. The hook already parses every record at write time, so this
  costs nothing extra to run and would catch such a violation at the moment
  it's introduced rather than two rounds later. The `registry_status` enum added
  after round 11 is the first piece of this — a required, machine-checked field
  rather than prose — so the remaining work is the subject/object slot types.
- Get a subject-matter expert to work through `docs-issues/` (98 entries; 1 now
  `resolved`) —
  starting with the two round 11 marked `severity: needs-sme`, which are
  undecidable from the pages rather than merely unresolved: **which service
  creates Analytics indexes** (`services.md` and `indexes.md` contradict each
  other, and the answer changes which service a reader must deploy and quota),
  and whether **"arbiter" and "serviceless node"** name the same thing (if they
  do, one term should be retired; if not, the difference is architecturally
  significant). Then the five-way "role" collision, the Sync Gateway/Capella
  access-control questions, round 5's `merge`/`nest` privilege-naming
  inconsistency (does "Query Select" = "Query Read"?), round 6's role-catalog
  loose ends (is `data-writer` the same role as the originally-mangled
  `project-data-writer`? is Capella iQ's cluster-scoped role a sixth role or
  an existing one at a different scope?), round 7's `privilege:capella-advanced-access-scope-admin`
  mismatch against `cluster-rbac.md`'s own table, and the support-plan
  wording inconsistency (now five variants) — all product-shape or
  docs-authority decisions, not just cleanup.

  Round 13 adds four that are unusually cheap for an SME to settle, because each is
  a single yes/no against the role catalogue: `roles.md`'s **Use Sequences table is
  mislabelled** "Manage Sequences" (the internal name and the permission table both
  say `use`/`execute`, so this is a heading fix, but only an SME can confirm which
  side is authoritative); its **four external-function role tables carry permission
  rows that look copy-pasted** from their non-external siblings; and two pages
  require roles that **do not exist in the 56-member catalogue** — "Data Admin"
  (`searchfun.md`) and "Administrator" (several `n1ql/` pages, where the catalogue
  offers Full Admin, Cluster Admin and several scoped admins).
- Finish round 3's Java SDK promotion backlog before running any further Java
  SDK rounds — round 10 promoted `sdk:kv-operations` and re-namespaced
  `sdk:transaction-query-mode`, leaving `sdk:durability`,
  `sdk:cas-optimistic-locking`, `sdk:error-handling`, `sdk:query-error-mapping`,
  `sdk:sqlpp-queries-with-sdk`, and `sdk:bucket-management` still
  extraction-layer-only. See round 4's note in `reconciliation.md`.
- Draft the remaining JSON-LD for everything still intermediate-only across all
  thirteen rounds. `context.jsonld` is a deliberately curated flagship subset (15 of
  97 predicates), not a complete mapping. Note round 11 added a case the layer has never had to handle:
  `requiresMinimumNodeCount` and `hasInternalServiceIdentifier` are **datatype
  properties**, so their objects are literals rather than `@id`s — 12 relations in
  the corpus now have literal objects, and every existing `.jsonld` file assumes
  otherwise.
- **Sweep the Markdown snapshot for `%5F` in link targets.** Round 11 found a
  link to `7%5Fusing%5Findex.md` — percent-encoded underscores in a filesystem
  path, a conversion artifact rather than an authoring error, which means the link
  does not resolve and the same bug will affect every converted link containing an
  underscore. Mechanical, and cheaper to fix at the converter than page by page.
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
- If this looks worth pursuing past a POC: eleven axes of stress test have now
  been run (cross-component, cross-deployment-model, cross-product-family,
  round 4's within-one-product-across-features, round 5/6/7's three-in-a-row
  confirmation that the same partial-sampling lesson recurs on successive
  vocabularies of the same product, round 8's confirmation that a genuinely
  new feature doesn't automatically need new structure, round 9's
  confirmation that even a "should mostly confirm" round still earns its
  keep, round 10's cross-version axis — the same product's docs at a
  second version, which is where the fabrication and the evidence-audit
  results came from — and round 11's cross-*genre* axis, which found four
  structural vocabulary gaps in nine pages that 543 pages of reference,
  guide and management-plane content had not). The next natural one is scale
  itself — a real batch
  against the ~3,900-page "latest version only" corpus from
  `../ingest-cost-and-time-estimate.md`, now that the pipeline has been
  exercised on Bedrock, at real (not just trial) scale, on every axis it's
  likely to meet at that size, and — as of round 10 — behind a mechanical
  evidence gate rather than on trust.
