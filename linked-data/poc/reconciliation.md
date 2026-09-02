# Pass-2 reconciliation log

Ten rounds so far, in order run. Each section covers one round; a single
cumulative verdict sits at the end.

---

## Round 1 — the original 8-page batch

Covers 5 N1QL index-statement reference pages (`server/`), plus a stress-test
extension into two other components (`search/`, `fts/`) to see whether the
vocabulary holds up outside the page cluster it was built on.

### Clusters resolved automatically (exact string match)

| cluster | recurrence | resolution |
|---|---|---|
| `privilege:query-manage-index` | 5/8 pages | auto-merged, identical phrasing every time |
| `version:server-6.5` | 5/8 pages | auto-merged (pre-minted before extraction started) |
| `version:server-7.0` | 3/8 pages | auto-merged (pre-minted) |
| `edition:enterprise` / `edition:community` | 2-3/8 pages each | auto-merged (pre-minted) |
| `index-state` enum | 3/8 pages | **not** pre-minted - promoted on the second sighting (verbatim-identical enum text), a real example of the recurrence rule catching something the design didn't think to declare upfront |
| `mustUseInsteadWhen` | 2/8 pages | promoted on the second sighting |

### Items flagged for human review (not auto-resolved)

1. **`privilege:query-manage-index` documented-at link disagrees on one page.**
   `createindex.md`, `dropindex.md`, `build-index.md`, and `createprimaryindex.md` all
   link the privilege sentence to `learn/security/authorization-overview.md`.
   `dropprimaryindex.md` links the *same privilege, same wording* to
   `learn/security/roles.md`. Same page under a different name/path, or has the
   docset drifted? A real inconsistency in the source docs, independent of the
   ontology work.

2. **`mustUseInsteadWhen` - real term or one-off?**
   Two occurrences, both describing the same constraint (named vs. unnamed
   primary indexes must be dropped via different statements) from each statement's
   own page. Two is the promotion threshold, so it's in `relations/` - but with
   only one *underlying fact* expressed twice, it's a thinner case than
   `query-manage-index`. (Resolved by round 3: no third occurrence has appeared,
   but the relation held up fine as-is.)

### Cross-component findings, tracked as `docs-issues/`

These say nothing about Couchbase, only about gaps/overlaps in the docs
describing it - recorded as lightweight `docs-issue` instances rather than
promoted into the concept/relation graph, so they stay queryable without
growing a second, parallel ontology of documentation-about-documentation. See
`poc/README.md` for the reasoning.

3. **The "every statement documents its required privilege" pattern is a
   template convention, not a universal one.** All 5 N1QL reference pages have
   an `RBAC Privileges` section. Neither `search/create-search-indexes.md` nor
   `fts/fts-delete-index.md` has anything like it - and `fts-delete-index.md`
   documents a *destructive* action with no privilege mentioned at all. The
   extraction can only report "this page has no privilege relation" - it can't
   tell you whether that's a doc gap or a true absence.
   → `docs-issues/missing-privilege-doc-search-create-search-indexes.json`,
     `docs-issues/missing-privilege-doc-fts-delete-index.json`

4. **`fts/` and `search/` look like two documentation generations covering
   overlapping ground.** Both trees have their own index-alias pages and their
   own create/delete-index pages; `fts-delete-index.md` reads like an
   older-generation doc next to the newer `search/` task pages.
   → `docs-issues/fts-search-doc-overlap.json`

### Findings from drafting the actual JSON-LD

Converting the promoted concepts/relations into real JSON-LD (`context.jsonld`,
`relations/*.jsonld`, `concepts/*.jsonld`, `pages/*.jsonld`) surfaced three
things that weren't visible while everything was still loose intermediate JSON:

5. **`availableSince` and `requiresMinVersionFor` turned out to be the same
   relation wearing two hats.** Both express "since version V, this holds" -
   one applied to a newly-added capability, the other to a longstanding
   constraint's start point. Consolidated into one relation, `availableSince`.
   The original pass-1 extraction files still show both names, unedited, as the
   historical record of what was first proposed.

6. **Not every relation found on a page is *about* that page.**
   `dropprimaryindex.md` and `createprimaryindex.md` both state the same fact -
   named primary indexes drop via `DROP INDEX`, unnamed ones via
   `DROP PRIMARY INDEX` - but the fact's actual subject is always *DROP PRIMARY
   INDEX*, regardless of which page it was read off. Converting extraction
   records (grouped by source page) into page-level JSON-LD (grouped by subject
   entity) means regrouping, not just reformatting.

7. **`docs-issues/` gained a fourth entry** (`privilege-doc-link-inconsistency.json`)
   for item 1 above, so every flagged-for-human item has a structured record.
   The public JSON-LD resolves to the majority link silently; the disagreement
   itself lives only in the docs-issue.

One thing that *didn't* need a workaround: pages with no `requiresPrivilege`
relation simply have no such triple in their JSON-LD. RDF/JSON-LD's open-world
semantics mean an absent triple already means "not stated," which is exactly
the honest epistemic state here.

---

## Round 2 — the 100-page stress test (server/ + cloud/)

Scope: 100 pages, 50 from `server/` (continuing the index-statement thread into
`learn/services-and-indexes/`, `manage/`, `search/`, `fts/`) and 50 from `cloud/`
(Capella) - deliberately loaded toward Capella's own statement family (vector
indexes, and a bucket/user/group/GRANT/REVOKE DDL/DCL set with no server/
equivalent) and its security surface, since those were the areas most likely to
break the vocabulary built on `server/`. Extraction ran as 10 parallel agents
(10 pages each), each given the promoted registry as it stood at the time and
told to extract only - no cross-batch coordination, no reconciliation.

### Headline finding: Capella's access-control model is a different shape, not a renamed one

Every one of the 5 cloud/ batches independently converged on the same
conclusion: Capella does not have a version of `requiresPrivilege` with
different names. It has several structurally distinct access-control
mechanisms server/'s vocabulary has no room for:

- **A management-plane role gate** (`requiresCapellaRole`, object = one of
  `capella-role:organization-owner` / `project-owner` / `project-data-writer`,
  disjunctive) on the Capella-only DDL/DCL statements and the vector-index
  family - 30 occurrences across 10 files, the most-recurring minted predicate
  in that batch.
- **A credential-type-keyed data-plane privilege pair**
  (`enum:cluster-access-credential-type` = Basic/Advanced, gating
  `privilege:capella-basic-access-write` vs.
  `privilege:capella-advanced-access-query-index`) on the index statements,
  plus the mirror-image `incompatibleWithCredentialType`.
- **A role-hierarchy model** for the data-plane RBAC that
  GRANT/REVOKE/CREATE GROUP/CREATE USER manipulate (`grantsRole`,
  `revokesRole`, `assignsRole`, `assignsToGroup`, `groupMembersInheritRole`) -
  roles nest through group membership, rather than a single privilege being
  checked per statement.
- **A billing-plan gate** (`gatedByBillingPlan`) and a **support-plan gate**
  (`requiresSupportPlan`) - commercial-tier gates with no server/ analog.
- **A UI-mode gate** (`requiresUiMode`, object `ui-mode:advanced`) - a
  client-side Web Console affordance, not a server-enforced check.
- **A deployment-variant gate** (`deployment:capella` as an object of
  `behavesDifferentlyUnder`) for clauses disabled specifically on Capella with
  no edition distinction involved - generalizing `behavesDifferentlyUnder`'s
  range from "edition concept" to "edition-or-deployment-variant concept."

All of the above are promoted (`concepts/` and `relations/`, `.json` for all;
`.jsonld` drafted for `requiresCapellaRole` and the credential-type family as a
flagship example - the rest are intermediate-only, noted rather than rushed).

### Other promotions from this round

- `isSynonymOf` (4, 4 files) - statement pairs the docs declare functionally
  identical (e.g. DROP INDEX / DROP VECTOR INDEX on Capella).
- `dependsOnService` (3, 2 files) - service-to-service architectural
  dependency, directly answering "which service implements this operation?"
- `requiresSetting` (2, 2 files).
- `tradesOffAgainst` (10, 3 files) - a comparative relation between two
  vector-index strategies with opposite strengths (Hyperscale vs. Composite).
  At least one file used `mustUseInsteadWhen` in opposite directions between
  the same two statements depending on context - really this relation's shape,
  not a one-way recommendation; some existing `mustUseInsteadWhen` relations
  between vector-index statements may need re-typing.
- `requiresMinVersionFor` was **independently re-minted** by these agents
  despite having been consolidated into `availableSince` in round 1 - the
  agents were only told the promoted predicate *names*, not the design history.
  Folded back into `availableSince`.

### New `docs-issues/` (8)

1. `capella-pages-cite-server-versions` - the single most-recurring anomaly: at
   least 11 relations across 6 pages cite literal "Couchbase Server X.Y"
   strings or link to `/server/...` paths on a product with no discrete
   versions. Reads as server/ content copied with the product name
   substituted.
2. `fts-index-management-content-duplication` - 4 fts/ pages substantially
   duplicate each other's content.
3. `search-admin-fts-admin-role-overlap` - `search/`'s "Search Admin" and
   `fts/`'s "FTS Admin"/"FTS Searcher" were minted as separate concepts by two
   agents who couldn't see each other's work; may be the same roles under old
   vs. new product naming.
4. `capella-storage-modes-vocabulary-mismatch` - a Capella page titled and
   structured around a choice of storage modes that, per its own content,
   doesn't exist on Capella.
5. `capella-search-service-missing-access-control-docs` - Capella's
   Search-index pages document no access control at all, unlike server/'s
   equivalent pages and Capella's own vector-index pages.
6. `server-storage-engine-split-duplicated-across-components` - the EE/Plasma
   vs. CE/ForestDB split restated near-verbatim in two server/ components.
7. `revoke-page-missing-group-parameter-row` - a small, concrete, fixable
   content gap.
8. `audit-management-missing-api-key-scope` - Management API audit endpoints
   with no documented required scope/role.

### How this reconciliation was actually done - and what that implies

At 108 extraction files and roughly 500 relations, reading each one
individually the way round 1 was reconciled stopped being practical. This pass
ran a script over all the extraction JSON to count predicate and object
recurrence and collect every `notable_absence`/`cross_component_finding`/
`cross_product_finding` field - the "recurrence is a query, not hand-tracked
state" principle, now operating at the scale it was designed for. Nothing above
was found by eyeballing 108 files in sequence.

Two things the aggregation surfaced that are **not** ontology findings, but
limits of the method at this scale:

- **A handful of naming inconsistencies** - e.g. one agent wrote
  `n1ql:createindex` instead of the established `n1ql:create-index` (found via
  object-recurrence counting; fixed directly, an unambiguous typo). A few
  similar cases likely remain unfixed (bare `index-state`/`edition:community`
  used instead of the full IRI in a few places) - flagged, not hand-fixed one
  by one, since at this volume that's mechanical cleanup a script should do.
- **Independent, un-coordinated re-minting** - `requiresMinVersionFor` and the
  `search-admin`/`fts-admin`/`fts-searcher` overlap are both cases where two
  agents, each blind to the other's output, proposed different names for what
  may be the same thing. A shared *written* registry catches reuse of
  *already-promoted* terms; it does nothing to stop two agents in the same run
  independently minting near-duplicates of something new.

---

## Round 3 — the cross-product-family test (Couchbase Lite + Sync Gateway + Java SDK)

Scope: 37 pages - 12 from Couchbase Lite/Android (an embedded, on-device
database with no server-side RBAC at all), 13 from Sync Gateway (a
synchronization/access-control middleware between mobile clients and
server/Capella), 12 from the Java SDK (a client library for calling
server/Capella from application code). Extraction ran as 4 parallel agents.
Unlike round 2 (server/ vs. cloud/ - two deployment models of the *same*
product, sharing one query engine), this round tests genuinely different
products, built by different teams, for different runtime environments.

### Headline finding: Sync Gateway runs two disjoint access-control systems, and neither is `requiresPrivilege`

Sync Gateway's own docs state, in nearly these words, that its Public-API
identity model (`sgw:user`/`sgw:role`/`sgw:channel`) and its Admin/Metrics-API
identity model (`sgw:rbac-user`, a reuse of server/'s RBAC) **"have no
relationship"** - one product, deliberately running two unrelated systems, not
one system under two names (unlike Capella, where every access-control
mechanism found so far is at least a variation on a single underlying
platform). The Public-API model itself is also the sharpest structural
departure found in this whole project: `requiresPrivilege` checks an operation
against a named privilege; Sync Gateway instead **tags documents with
channels** (via an imperative JavaScript sync function run per document
revision) and grants **users or roles membership of channels** - a read is a
pure set-intersection with no per-operation gate anywhere in the model.
`grantsChannelAccess` (15 occurrences, 8 files) is the resulting predicate, and
it is now the single most-recurring minted predicate across the whole project.

### The "role" collision, made visible on purpose

This round surfaced a genuine same-word-different-thing problem the vocabulary
had been quietly accumulating: **three structurally distinct things are all
called "role" in this ontology now** -

- `capella-role:*` - a small, fixed catalog of Capella management-plane roles
  (Organization Owner, Project Owner, Project Data Writer).
- `rbac-role:role` - a coarse placeholder for the data-plane RBAC roles that
  GRANT/REVOKE/CREATE GROUP manipulate on server/ and Capella.
- `sgw:role` - an ad hoc, customer-named, uncataloged bundle of channel
  grants, with no fixed catalog at all.

No single page states that these are unrelated, so they have **not** been
merged or cross-linked with `should-not-be-confused-with` (a relation minted
this round for exactly this kind of case) - doing so without textual evidence
would be inventing a fact, not extracting one. They're kept as three separate
concepts, each documented with a note pointing at the other two, so a future
reader (or a future extraction pass) doesn't have to rediscover the collision
from scratch.

### Other findings

- **Couchbase Lite has its own Enterprise/Community edition split**, gating an
  entirely different feature set (Predictive Query, Delta Sync, Database
  Encryption) from server/'s. Minted as `cbl:enterprise-edition`, deliberately
  not merged with `edition:enterprise` - same shape, different product,
  different features. One inconsistency flagged: Vector Search is similarly
  premium/ML-coded but is documented as *not* edition-gated -
  `docs-issues/cbl-vector-search-not-edition-gated-inconsistency`.
- **`behavesDifferentlyUnder`'s range generalized a second time.** Couchbase
  Lite's page comparing its own SQL++ dialect against server/'s mapped every
  documented difference cleanly onto `behavesDifferentlyUnder` - but the
  gating axis is *product family* (`cbl:sql-plus-plus-mobile` vs.
  `cbl:server-sql-plusplus-dialect`), not edition or deployment variant. The
  relation has now absorbed three kinds of "varies by X" - edition, deployment
  (`deployment:capella`), and product family - all legitimately the same
  relation shape, a small, quiet validation that the shape was defined at the
  right level of abstraction.
- **The Java SDK required a page-by-page judgment call, not a batch-wide
  rule.** Pages wrapping a specific server/ statement
  (`provisioning-cluster-resources.md` → `n1ql:create-index` et al.) correctly
  reused the existing concept; pages with no statement-level equivalent
  (`kv-operations.md`, client connection/error vocabulary) correctly minted
  SDK-specific concepts; one page (`vector-searching-with-sdk.md`) split down
  the middle within itself. The extraction agent also directly corrected a
  hint in its own briefing - it checked whether `requiresCapellaRole` applied
  to the user-management pages and reported back that it explicitly does not,
  since those APIs predate and are documented as agnostic to Capella's
  management plane. A positive sign for the method: the agent checked the
  evidence rather than fitting the coordinator's suggestion.
- **Stub concepts from the Couchbase Lite batch now resolve.** That batch, run
  concurrently with the Sync Gateway batches, minted placeholder stubs
  (`cbl:sync-gateway`, `cbl:sync-gateway-channel`) for a system it referenced
  but doesn't own. Now that `sgw:channel` etc. are real, promoted concepts,
  those stubs resolve to the real `sgw:*` ids - the same stub-resolution
  pattern seen with `createprimaryindex.md` in round 1, just crossing a
  product boundary this time instead of a page boundary.

### New `docs-issues/` (5)

1. `sgw-sync-function-require-role-cmd-duplicates-sync-function-page` - likely
   content duplication between two sync-function reference pages.
2. `cbl-vector-search-not-edition-gated-inconsistency` - see above.
3. `java-sdk-advanced-analytics-querying-empty-stub` - an empty stub page.
4. `sgw-silent-default-behaviors-underdocumented` - Sync Gateway's fail-open
   write default and its silent no-op on assigning a nonexistent role are both
   easy to miss on the page, not called out prominently.
5. `sgw-security-page-missing-audit-log-permission` - the security page never
   cross-references the separate audit-logging subsystem's permission model.

---

## Round 4 — Bedrock infrastructure trial (3 Java SDK pages)

Scope: 3 pages, continuing round 3's Java SDK coverage into territory it
didn't touch - `java-sdk/howtos/error-handling.md`,
`distributed-acid-transactions-from-the-sdk.md`, and
`transactions-single-query.md`. Deliberately small: this round's primary
purpose was infrastructural, not ontological - the host environment had just
migrated from direct Anthropic API access to Amazon Bedrock, and the point was
to confirm the extract → reconcile pipeline still works unchanged before
resuming ontology work at any real scale. See
`../ingest-cost-and-time-estimate.md` for the Bedrock-specific tooling/cost
findings from this same trial. The extraction itself was run for real, not as
a dummy exercise, so it's reconciled on the same terms as rounds 1-3.

### Headline finding: distributed transactions don't extend the existing SDK vocabulary - they add a new structural layer

Same shape of finding as Sync Gateway's channel model in round 3: a product
surface that looks at first like it should reuse existing per-operation
vocabulary, and instead needs its own. Four structurally distinct primitives,
none reducible to an existing per-operation concept:

- **`sdk:transaction-attempt-context`** - the transaction-scoped CRUD/query API
  (`ctx.insert`/`get`/`replace`/`remove`/`query`). Replace/remove require a
  prior `ctx.get()` purely so "the SDK can check that the document is not
  involved in another transaction" - a transaction-membership check, not a
  CAS-token comparison. No CAS/CasMismatch language appears anywhere on the
  source page.
- **`sdk:transaction-durability`** - a single `DurabilityLevel` setting applied
  once per transaction attempt (via `TransactionsConfig`/`ClusterEnvironment`),
  not per individual mutation call the way `sdk:durability` works. Same enum
  values, incompatible scope - related via the newly minted
  `sharesOptionSetWith`, not treated as the same concept. The identical enum
  recurs at a **third** distinct scope again on the single-query-transaction
  page (per-single-query-transaction-call), the cleanest confirmation of this
  finding in the batch.
- **`sdk:transaction-query-mode`** - once a transaction runs any SQL++ query,
  that query and every subsequent key-value operation in the same attempt
  switch to the user's query permissions instead of their data permissions.
  No per-operation analogue exists anywhere else in the SDK vocabulary.
- **`sdk:transaction-error-handling`** - `TransactionFailedException` /
  `TransactionCommitAmbiguousException`, expressing whole-transaction commit
  ambiguity, confirmed (via catch-block ordering on
  `transactions-single-query.md`) to be a Java subtype of the general
  `sdk:error-handling` hierarchy - but documented on an entirely separate page
  (`concept-docs/transactions-error-handling.md`) that the general
  error-handling howto never links to or mentions. See docs-issue below.

`sdk:transaction-attempt-context` and `sdk:transaction-query-mode` are promoted
at recurrence 1, below the usual 2-file bar - a judgment call made explicitly,
the same exception used for `hasNoRelationshipTo` in round 3, because both are
the concrete evidence for this round's headline finding rather than incidental
detail.

### Other promotions from this round

- `sharesOptionSetWith` (2, 2 files) - new relation for "two concepts reuse the
  identical enum/option values but at incompatible structural scopes,
  configured through separate, non-interchangeable API surfaces." Deliberately
  distinct from `usesEnum` (a concept consuming a closed enum, not two concepts
  sharing one across scopes) and from `behavesDifferentlyUnder` (one clause
  varying by axis, not two structurally distinct concepts).
- `version:sdk-3.3.0` - first entry in a new, independent Java SDK version
  family, promoted at first sighting following the same precedent as
  `version:cbl-3.3.0` in round 3 (version enums are promoted on sight, not
  held to the 2-file bar).
- `version:server-6.6.1` - **a judgment call, discussed in detail below.**

### The `version:server-*` "closed vocabulary" question, resolved

Round 1 described `version:server-6.5` and `version:server-7.0` as a "closed
vocabulary term... pre-minted before extraction began." This round's
extraction cited a real, differently-scoped minimum-version requirement
("Couchbase Server 6.6.1 or above") that doesn't match either value and can't
be honestly rounded to one - and flagged the tension explicitly rather than
guessing. Reconciliation reads round 1's "closed vocabulary" framing as "these
were the only versions seen so far, promoted without waiting for the usual 2x
recurrence because versions are low-cardinality and high-value" - not a literal
ceiling on the family. `version:sgw-*` already has two sibling entries and
`version:cbl-3.3.0`'s own promotion note says outright to "expect more as more
CBL pages are processed" - both establish that per-product version families
are meant to grow as new versions are encountered in evidence.
`version:server-6.6.1` is promoted on that basis. Worth restating for any
future round: "closed vocabulary" in this project has always meant "a small,
enumerable, pre-declared shape," not "frozen at whatever was first promoted."

### A pre-existing gap this round inherited, not created

This round's extraction reused `sdk:error-handling`, `sdk:durability`,
`sdk:kv-operations`, and `sdk:sqlpp-queries-with-sdk` as if they were
registry-promoted concepts. They aren't - round 3's Java SDK batch (12
`howtos/` + 2 `ref/` pages) was reconciled only at the narrative level ("the
extraction correctly reused... correctly minted...") and never promoted a
single Java SDK concept to `concepts/`, unlike every other product round.
Round 4 doesn't attempt to backfill that sweep - it's a bigger job than a
disposable-scale infra trial should take on - but it's now flagged explicitly:
a full Java SDK concept-promotion pass (`sdk:kv-operations`, `sdk:durability`,
`sdk:cas-optimistic-locking`, `sdk:error-handling`, `sdk:query-error-mapping`,
`sdk:sqlpp-queries-with-sdk`, `sdk:bucket-management`, at minimum - all recur
across multiple round-3/4 extraction files) is the right next step before any
further Java SDK rounds, not another round of new pages.

### Left on the watchlist (extraction-layer only, not promoted)

Recurrence-1, no overriding significance case made: `sdk:retry-strategy`,
`sdk:retry-reason`, `sdk:cloud-native-gateway`, `sdk:bucket-replica-count`,
`sdk:single-query-transaction`, `n1ql:tximplicit-parameter`,
`determinesRetryabilityOf`, `reservesXattrField`, `conflictsWithConcurrent`,
`exposesOperationApi`, `triggersPermissionModeChange`, `specializes`,
`wrapsQueryParameter`. Several placeholder concepts the extraction minted for
linked-but-unextracted pages (`sdk:transaction-concepts`,
`sdk:transactions-migration-guide`, `sdk:xattr`,
`server:distributed-acid-transactions`, `cloud:organizations-access`) remain
honest stubs, to resolve if/when those pages are ever extracted - same pattern
as the Couchbase Lite stubs that resolved once Sync Gateway's concepts landed
in round 3.

### New `docs-issues/` (3)

1. `java-sdk-error-handling-missing-cross-references` - the general
   error-handling page never links to `kv-operations.md` despite its examples
   being entirely KV-based, and never mentions transactions at all.
2. `java-sdk-transaction-error-handling-disconnected-branch` - transactions
   have their own, separately-documented exception pair on a page the general
   error-handling howto neither links to nor mentions.
3. `java-sdk-transactions-single-query-no-cross-references` - this page has no
   markdown links at all despite depending entirely on prerequisite concepts
   introduced on the distributed-transactions page.

### Infrastructure check (the actual point of this round)

Extraction, validation, and reconciliation all ran identically to prior
rounds - no tool failures, no degraded output, no observed difference
attributable to running on Bedrock rather than direct Anthropic API access.
Real token usage came in at roughly 20,700 tokens/page (62,167 tokens across
the 3-page batch, one agent, sequential-with-reuse-checking), noticeably above
round 2's ~11,700 tokens/page benchmark - plausibly because this batch's
subject matter (a whole new structural layer, four new concepts requiring
detailed disambiguation notes) was denser than round 2's largely-CRUD-statement
pages, not necessarily a Bedrock effect; a same-content comparison would be
needed to separate the two, which this small a trial can't provide on its own.
See `../ingest-cost-and-time-estimate.md` for the full tooling/cost writeup.

---

## Round 5 — completing `cloud/n1ql/` (115 pages)

Scope: the remaining 115 of 138 pages in `cloud/n1ql/` (round 2 had sampled
only 23) - the full Capella SQL++/N1QL language reference, intro, and manage
pages. Run as 10 parallel batches of ~12 pages each, on the same Bedrock
infrastructure validated in round 4, at real production scale for the first
time (round 4 was a 3-page trial). Total usage across all 10 batches: ~1.5M
tokens for 115 pages (~13,000 tokens/page) - close to round 2's original
~11,700 tokens/page benchmark, which in hindsight makes round 4's ~20,700
tokens/page look like a content-density outlier for that specific 3-page
batch, not a Bedrock effect. Using the project's established blended-rate
method, that's roughly $4-5 for the whole round.

Hypothesis: does Capella's credential-type/capella-role access-control model
(established in round 2 from CREATE/DROP BUCKET/USER/GROUP, GRANT/REVOKE, and
the vector-index family) extend cleanly across the rest of the DDL surface
(collections, scopes, sequences, UDFs) and the SQL++ transaction-statement
family, or does something new turn up?

### Headline finding: the model held up, but "the credential-type pair" turned out to be a whole privilege catalog, not two values

Round 2 saw Basic/Advanced as a flat two-value pair (Write vs. Query Index).
Round 5 found the Advanced side is actually a **per-statement-family named
privilege catalog** - a new Advanced privilege for nearly every DDL/DML
statement kind, while Basic stays a flat Write/Read binary throughout. Eleven
new Advanced-credential privileges were promoted this round alone (Scope
Admin, Query Insert, Query Update, Query Manage Sequences, Global/scoped
Function Manage, Global/scoped Function Execute, Query Delete, Query Execute,
plus the missing Basic-side Read and Advanced-side Query Read that round 2
never needed). Two genuinely new shapes inside that catalog:

- **A two-axis privilege** (`createfunction.md`): the Advanced privilege is
  keyed by credential type *and* function scope (global vs. scoped)
  simultaneously - `privilege:capella-advanced-access-global-function-manage`
  vs. `-query-manage`, and the execute-side equivalents.
- **A conjunctive (AND) requirement** (`upsert.md`): UPSERT needs Query Insert
  **and** Query Update together, not either - the first AND-combination seen
  in this family, versus `requiresCapellaRole`'s disjunctive (any-one-suffices)
  logic. No existing predicate distinguishes AND from OR combination yet -
  flagged as an open modeling question, not resolved this round.

### The model has real, evidenced boundaries - three places it doesn't apply

- **Sequence operators** (`sequenceops.md`, `n1ql-auditing.md`-adjacent pages)
  use a named, server-style RBAC privilege (minted `privilege:query-use-sequences`
  in the extraction, left unpromoted at 1-file recurrence) instead of the
  Basic/Advanced pair.
- **`window.md`/`windowfun.md`** cite the bare server-style privilege name
  `query_select` directly, with no credential-type table at all - reinforcing
  `createuser.json`'s earlier (round 2) observation that the underlying RBAC
  engine is shared with server/ and only some pages have been migrated to the
  credential-type framing.
- **Search functions** (`searchfun.md`) use named RBAC roles (Data Admin/Data
  Reader) and explicitly state "You do not need credentials for the Search
  Service" - neither capella-role nor credential-type applies at all.
- **Transaction-control statements** (BEGIN/COMMIT/ROLLBACK/SAVEPOINT/SET
  TRANSACTION) carry **no access-control gating whatsoever** - confirmed
  across every TCL page in the batch. The credential-type/capella-role model
  is scoped to management-plane and ordinary data-plane statements, not
  transaction control.

### A fourth thing called "role"

`n1ql-auditing.md` gates audit-service configuration with classic, cluster-wide
admin roles - **Full Administrator** and **Local User Security Administrator**
- that fit neither `capella-role:*` (Capella's fixed management-plane catalog),
`rbac-role:role` (the coarse data-plane RBAC placeholder), nor `sgw:role`
(Sync Gateway's unrelated ad hoc channel-grant bundles). Promoted as
`role:full-administrator`/`role:local-user-security-administrator` below the
usual recurrence bar, the same judgment call used for `hasNoRelationshipTo` in
round 3 and for `sdk:transaction-attempt-context` in round 4 - this is the
concrete evidence extending an already-documented, semantically significant
finding (round 3's three-way "role" collision) to a fourth member. No page
states a relationship between any of the four, so none are merged.

### A fourth gating axis: access surface, not role/credential/UI-mode

Two unrelated pages - `transactions.md` and `using-ai.md` - independently
state that a feature is unsupported via specific client/interfaces (the
Capella Query tab, the Data API, Couchbase Shell), regardless of the caller's
role or credentials. Minted `incompatibleWithAccessSurface` and a small
`capella:query-tab`/`data-api`/`cbsh` concept family, promoted together since
the predicate clears the normal 2-file threshold on its own even though most
individual surface concepts are single-occurrence - the same family-promotion
allowance used for round 2's GRANT/REVOKE set.

### Other promotions

- `requiresPriorExecutionOf` - minted, unpromoted, in an earlier round's
  `server/n1ql/n1ql-language-reference/cost-based-optimizer.json` (Cost-Based
  Optimizer needing `UPDATE STATISTICS` run first); this round's
  `cloud/n1ql/.../cost-based-optimizer.json` extraction **independently
  matched and reused the exact same predicate name** for the identical fact on
  Capella's equivalent page - the written registry catching a real cross-round,
  cross-product reuse, the mirror image of round 2's
  `requiresMinVersionFor`/`availableSince` near-duplicate-minting problem.
- `renamedFrom` - consolidates two independent single-occurrence mints of the
  same relation shape at two different levels: `infer.json` (INFER renamed
  from the legacy DESCRIBE statement) and `query.json` (SQL++ renamed from
  N1QL, minted there as `formerlyKnownAs`). Same lesson as the
  `availableSince`/`requiresMinVersionFor` consolidation - kept `renamedFrom`
  as the canonical name.
- `index-type:gsi` - a minor promotion; Capella secondary indexes must be GSI,
  restated on two statistics pages.

### Left on the watchlist (extraction-layer only, not promoted)

`privilege:query-use-sequences`, `privilege:capella-advanced-access-query-select`
(the likely-duplicate of the promoted `query-read`, see docs-issue below),
`role:full-administrator`'s and other pages' minor single-occurrence
predicates (`hasLimitation`, `differsInEvaluationTimingFrom`, `isCreatedUsing`,
`dependsOnStatement`, `storedIn`) - none cleared the 2-file bar and none carry
the kind of headline significance that earned an exception this round.

### A likely mis-map, left uncorrected in the original extraction record

`prepare.json` reused `privilege:capella-advanced-access-query-index` for
PREPARE's own "Query Update" requirement, rather than the newly-promoted
`privilege:capella-advanced-access-query-update`. Flagged here rather than
hand-edited in the original extraction record, per the project's standing rule
against silently rewriting pass-1 output - worth correcting whenever this
registry is next consumed downstream (JSON-LD drafting, page-layer assembly).

### New `docs-issues/` (5 new, 1 existing updated)

1. **`capella-pages-cite-server-versions` updated, not new** - round 2 found
   this in 6 pages; round 5's sweep found it in **45 of 115 pages (39%)**,
   across nearly every statement/function/clause category. Density this high
   across a directory this broad reads less like isolated copy-paste and more
   like a systemic pattern in how this whole reference tree was authored.
2. `capella-pages-cite-edition-badges` - a sibling anomaly: Enterprise/
   Community edition badges on Capella pages, which have no edition split at
   all. Distinct from the version-string issue but likely the same root cause.
3. `cloud-n1ql-selectintro-privilege-doc-duplication` - the same Read privilege
   described on two unlinked pages, same shape as round 1's original
   privilege-doc-link-inconsistency finding.
4. `cloud-n1ql-clause-pages-missing-prerequisites` - `where.md`,
   `with-recursive.md`, and `execute.md` have no Prerequisites/privilege
   section at all, unlike sibling clause pages. May be deliberate (clauses
   inheriting access from the enclosing statement) rather than a gap - flagged
   for SME judgment, not asserted either way.
5. `cloud-n1ql-error-codes-orphaned-see-also` - a small, concrete, fixable
   content gap (an empty `## See Also` heading).
6. `cloud-n1ql-privilege-naming-inconsistency-select-vs-read` - `merge.md`
   names a privilege "Query Select" where 15 sibling pages name the
   structurally equivalent one "Query Read." Left the two concepts unmerged
   pending confirmation they're the same real privilege.

### What this round confirmed about the method itself

- **A written registry can work exactly as designed across rounds, not just
  within one.** `requiresPriorExecutionOf`'s cross-round, cross-product reuse
  (above) is the positive case the `requiresMinVersionFor` incident in round 2
  was the negative case of - the difference being whether an agent actually
  checked sibling extraction files, not just the registry summary it was
  handed.
- **"Family" promotion below the recurrence bar is now a repeated pattern,
  not a one-off.** Round 3 used it once (`hasNoRelationshipTo`); round 4 used
  it twice; round 5 used it three times (the two `role:*` roles, the
  access-surface family, and implicitly the whole eleven-member Advanced
  privilege catalog, most of whose individual members sit at 2-4 file
  recurrence). Worth treating as a standing part of the method now, not an
  exception invoked occasionally.
- **A single directory can still surprise after a prior round already sampled
  a fifth of it.** Round 2 read 23 of these 138 pages and called the
  credential-type model "a pair." Round 5 read the other 115 and found it was
  a catalog. Partial sampling of a large, structurally uniform-looking
  directory doesn't guarantee the sample generalizes - worth remembering
  before treating any single round's read of a big reference tree as final.

---

## Round 6 — completing `cloud/`'s management plane (89 pages)

Scope: 89 pages closing out every small-to-medium `cloud/` directory left after
round 5 finished the SQL++ statement reference - security (private
link/CMEK), the remaining index-concept pages, Projects, Organizations
(including all 6 SSO provider guides), Billing, Get Started (including
Capella iQ), the Data API guide, JavaScript UDFs, the Management API guide,
the per-service metrics catalog, and the general reference/compatibility
pages. Deliberately left `clusters/` (53 pages), `eventing/` (67), and
`guides/` (33) untouched - each is a large enough first-contact territory to
deserve its own dedicated wave rather than being folded in as filler. Run as
8 parallel batches. Total usage: ~1.05M tokens for 89 pages (~11,800
tokens/page - matching round 2's original benchmark again), roughly $3 by the
project's established blended-rate method.

### Headline finding: `capella-role:*` was never one catalog - it's two, silently flattened together since round 2

Every statement page's Prerequisites section lists whichever `capella-role:*`
roles gate that statement, with no indication of scope. Reading the two
catalogs' own authoritative pages directly for the first time revealed they
are genuinely separate:

- **Organization-scope** (from `organization-user-roles.md`): Organization
  Owner (already known), **Project Creator**, **Organization Member** (both
  new).
- **Project-scope** (from `project-roles.md`): Project Owner (already known),
  **Cluster Manager**, **Cluster Viewer**, **Data Reader**, **Data Writer**
  (all new) - and the page's own label for the fifth is plain "Data Writer,"
  not "Project Data Writer," the name round 2 minted from a statement page's
  paraphrase.

Four independent batches (security/indexes/projects, organizations-core,
get-started/Capella iQ, and billing) converged on overlapping subsets of this
same corrected picture without coordinating - strong triangulation that this
is real, not one agent's misreading. The mechanism connecting the two
catalogs: an organization-scope role (Organization Owner, Project Creator)
**implies** project-scope access rather than being a project-scope role
itself - captured in the newly minted `impliesRole`. Existing ids were kept
stable (dozens of extraction records across rounds 2/5/6 already reference
them) rather than renamed; `organization-owner.json`, `project-owner.json`,
and `project-data-writer.json` were annotated with scope-clarifying notes
instead. Two loose ends deliberately left unresolved: whether
`capella-role:data-writer` (project-roles.md) and `capella-role:project-data-writer`
(the original, differently-labeled mint) are the same role or two, and
whether Capella iQ's cluster-scoped `capella-role:cluster-data-reader-writer`
is a sixth role or the existing Data Reader/Data Writer pair at a different
scope - both flagged for SME review, not guessed at.

Same lesson as round 5's privilege-catalog finding, now landing on the role
catalog: **partial, statement-side-only sampling of an access-control
vocabulary doesn't generalize the way it feels like it should**, twice in a
row now on the same product.

### A same-word collision inside a single wave: two things called "Cluster Manager"

Independent of the role catalog: `metrics-reference.md` explicitly excludes
"the Cluster Manager" (a monitored system component, alongside XDCR) from
"the Services." That's a different real thing from `capella-role:cluster-manager`
(a project-scope role also named "Cluster Manager"). Promoted as
`capella:cluster-manager` (component) vs. `capella-role:cluster-manager`
(role), explicitly disambiguated in both records - the same discipline as the
project's other same-word collisions, just surfacing within one round instead
of across several.

### Authentication and authorization confirmed as genuinely separate axes

The SSO/identity-provider batch confirmed `auth:sso`/`auth:mfa` never become a
role and are never granted - the two axes touch only at `sso:group-mapping`
(mapping an IdP's groups to Capella access) and at the gate on who can
configure a realm in the first place (Organization Owner, via the existing
`requiresCapellaRole`). One open placeholder: whether `sso:group-mapping`'s
target is an organization role, a project role, or the data-plane
`rbac-role:role` family - no page says, left unresolved as `auth:permission-set`
(extraction-layer only).

### behavesDifferentlyUnder generalized a third and fourth time

Prior rounds generalized this relation's range from edition, to deployment
variant (`deployment:capella`), to product family. This round found it
applies within Capella itself along **two more axes**: which underlying cloud
provider a cluster runs on (`cloud-provider:aws`/`azure`/`gcp` - Azure's
storage auto-expansion causes data movement, AWS's/GCP's don't, independently
corroborated by a second page's AWS-specific volume-limit note) and which
storage engine a bucket uses (`storage-engine:couchstore`/`magma` - different
Health Advisor thresholds, found unprompted by a batch that was looking for
the cloud-provider axis and noticed a second one along the way).

### Two access surfaces' credential mechanisms resolved

`capella:data-api` authenticates via the same `cluster-access-credential-type`
Basic-auth model statement pages use (confirmed 4x independently across its
own docs) - it just never uses the "Basic/Advanced" terminology. The separate
`capella:management-api` authenticates via Bearer-token `mgmt-api:api-key`s,
which are themselves associated with `capella-role:*` roles rather than
inventing a new authorization scheme - confirmed by its error catalog naming
`privilege:capella-basic-access-read`/`write` exactly. New relation
`authenticatesVia` captures the credential-transport question neither
`requiresPrivilege` nor `requiresCapellaRole` addressed.

### Other promotions

- `plan:enterprise-support-plan`/`developer-pro-support-plan`/`basic-support-plan`/`free-tier-plan`
  - the four-tier support-plan family, formalized for the first time
  (consolidating several near-duplicate mints across batches: `plan:developer-pro`
  into `-developer-pro-support-plan`, `billing:free-tier-plan` into
  `plan:free-tier-plan`). Directly ties into a much bigger version of an
  already-flagged docs-issue - see below.
- `capella:xdcr` (consolidating `clusters:xdcr`), `service:eventing-service` -
  two components/services never previously in the registry.
- `data-api:private-endpoint`/`api-key-secret` - Data API infrastructure
  concepts.
- `disablesFeatureFor`, `gatedByBillingPlan` - the latter closes a real gap:
  round 2's own reconciliation narrative claimed this predicate was promoted
  ("`gatedByBillingPlan`... All of the above are promoted"), but no
  `relations/` file was ever written for it. Same shape as round 3's
  never-promoted Java SDK concepts (found in round 4) - a reconciliation gap
  invisible until a later round tried to reuse the term.

### Left on the watchlist (extraction-layer only, not promoted)

`capella-role:cluster-data-reader-writer` (Capella iQ's cluster-scoped role -
possible duplicate of Data Reader/Data Writer, see above), `auth:permission-set`
(the unresolved SSO-mapping-target question), `disablesDependentFeature`
(possible near-duplicate of `disablesFeatureFor`, not merged without
evidence), `incompatibleWithFeature` (Azure Private Link's XDCR/Prometheus
exclusion, recurrence 1), and a long tail of single-batch `js-udf:`/`capellaiq:`/
`data-api:` concepts that didn't clear the bar or weren't central enough to
this round's headline findings to justify individual promotion at this
volume - noted here rather than silently dropped.

### New `docs-issues/` (6)

1. `capella-support-plan-wording-inconsistency` - now five wording variants
   (up from round 2's two), including two on the *same page*.
2. `cloud-organizations-sso-provider-inconsistencies` - six real cross-provider
   inconsistencies found reading all 6 SSO setup guides back to back, plus a
   broken `{footnote-1}` template artifact on the Ping page.
3. `cloud-projects-role-naming-drift-cluster-manager` - "Cluster Manager" vs.
   "Project/Cluster Manager," the same small-scale naming-drift pattern seen
   before, this time on the role catalog itself.
4. `cloud-projects-project-roles-page-thin` - the authoritative role-catalog
   page is a 28-line stub with no See Also and no return links from its 3
   siblings.
5. `cloud-billing-small-content-bugs` - a malformed HTML entity and a broken
   anchor-slug cross-reference.
6. `cloud-js-udf-transaction-access-surface-gap` - a genuinely unanswered
   product-behavior question (does the Data API's transaction exclusion
   propagate through a UDF that wraps one?), not resolved by inference.

### What this round confirmed about the method itself

- **The same lesson can recur on the same product, twice, on two different
  axes.** Round 5 found the privilege catalog was richer than a partial
  sample suggested; round 6 found the same thing for the role catalog. Worth
  treating as a standing expectation for any vocabulary built primarily from
  statement pages' Prerequisites sections rather than a feature's own
  authoritative documentation - the former paraphrases and flattens, the
  latter doesn't.
- **Independent, uncoordinated convergence is strong evidence.** Four
  separate batches, none aware of the others' output, each surfaced
  overlapping pieces of the same corrected role picture. That's a materially
  stronger signal than any single batch's finding would have been alone.
- **A reconciliation gap can sit undetected for four rounds.** `gatedByBillingPlan`
  was narratively described as promoted in round 2 and silently wasn't, for
  four rounds, until this one needed to reuse it. Same root cause as round
  4's Java SDK gap - reconciliation's own coverage isn't self-verifying.

---

## Round 7 — `cloud/clusters/` (53 pages)

Scope: all 53 pages of `cloud/clusters/` - cluster lifecycle (create/scale/
upgrade/delete), backup/restore, cluster-level access control
(`cluster-rbac.md`), the Data/Analytics/Index/Query service management pages,
XDCR, and the full monitoring/alerting subdirectory. Zero prior coverage. Run
as 6 parallel batches same-day as rounds 5 and 6. Total usage: ~714,000
tokens for 53 pages (~13,500 tokens/page, a touch above the ~11,700-13,000
this session's other two waves landed on - consistent with this being a
denser, more finding-rich wave), roughly $2 by the project's blended-rate
method.

### Headline finding: the same undercounting lesson, on the privilege catalog this time - and the discrepancy is bigger

Round 6 found `capella-role:*` was two flattened catalogs, discovered by
reading the role catalog's own authoritative page instead of trusting
statement-page citations. Round 7 found the identical shape on the *privilege*
catalog: `cluster-rbac.md` is the authoritative privilege table, and it lists
**25 distinct privileges** - the registry had 11 (round 2's original pair
plus round 5's ten-privilege catalog expansion), all inferred from statement
pages' scattered citations. 15 new privileges promoted this round: a
4-member Analytics family (Read/Admin/Manage/Select), a 3-member Data family
(Read/Manage/Monitor), a 2-member FTS family (Manage/Read), Eventing Manage
(the first privilege-level evidence connecting `service:eventing-service` to
any access-control model), Stats Read, Query Catalog, Query Manage Catalog,
Query Curl Access, and Query Use Sequences (distinct from the already-promoted
Query Manage Sequences - NEXTVAL/PREVVAL vs. CREATE/ALTER/DROP SEQUENCE). One
loose end, not resolved: `privilege:capella-advanced-access-scope-admin`
(round 5) doesn't appear in `cluster-rbac.md`'s table at all - either the
original statement-page citation was wrong, or the authoritative table is
itself incomplete - logged as `docs-issues/cloud-clusters-scope-admin-privilege-mismatch.json`.

`cluster-rbac.md` also settled a question the ontology had been carrying
implicitly rather than confirming with evidence: its own opening line states
the data-plane credential model "are separate from organization roles and
project roles" - explicit textual confirmation (via the already-promoted
`hasNoRelationshipTo`) that the privilege catalog and the round-6 role
catalog are genuinely disjoint mechanisms, not two views of one thing.

### Two open questions from earlier rounds resolved cleanly

- **Storage engine (Couchstore/Magma):** a bucket-creation-time choice, but
  not permanently fixed - a real migration path exists (Management API on
  Server 7.6+, manual recreate-and-copy on 7.2). Round 6 had only seen this
  pair from a single Health Advisor threshold mention and didn't know whether
  it was creation-time-fixed at all.
- **Cloud-provider variance:** broader than round 6's single data point
  (Azure's storage auto-expansion). Reading the cluster-creation flow
  directly found provider choice also affects disk-type options, IOPS
  configurability, and region/AZ availability - the same axis, more surface
  area than one example suggested.

One question surfaced but deliberately left open: does `capella-role:cluster-manager`
(the project-scope role) or the general 8-role catalog get restated on
`cluster-rbac.md`? No - that page turned out to be about a completely
different axis (data-plane credentials/privileges), not the role catalog at
all. A useful negative result: not every "obviously relevant" authoritative
page confirms the hypothesis it was read to test.

### XDCR and Analytics both resolved as "no new mechanism"

Two features whose access-control model was previously unknown (each only
seen via a passing mention in an earlier round) turned out to introduce
nothing new once read directly: XDCR's entire "security" model is a
network-topology choice (Public Internet / VPC Peering / Private Endpoint,
completing that triad with the newly promoted `security:public-internet`),
gated by cloud-provider/node-count/version, not by identity - it fully reuses
`capella-role:project-owner` and the existing credential model. Analytics
likewise mints no authorization concept of its own; its role gating and even
its query-consistency setting are verbatim reuses of the existing catalog and
`n1ql:scan-consistency-values`. Two clean confirmations that "new feature"
doesn't automatically mean "new access-control shape" - it's a real
possibility this project has now found several times (round 6's XDCR-adjacent
finding was actually about metrics, this is the first direct read of XDCR's
own security docs), but not the default outcome.

### A second data-plane access axis for backup/restore

Backup/restore is gated by `capella-role:project-owner`/`organization-owner`
like most management-plane surfaces - except the CLI path (`cli-backup-restore.md`),
which is gated by `cluster-access-credential-type` read/write scope instead,
not `capella-role:*` at all. A genuine second axis specific to this one
surface. Also found: a free-tier asymmetry (bucket-level backups are
unavailable on `plan:free-tier-plan`, forcing a `cbbackupmgr` CLI fallback;
cluster-level snapshot backups have no equivalent restriction) - a real
product fact, not a docs gap, so not logged as a docs-issue.

### A same-word collision found within a single round: two "index status" vocabularies

The Capella Indexes UI has its own status enum (ready/pause/warmup) -
`capella:index-ui-status`, promoted this round - which is a genuinely
different vocabulary from the SQL++ DDL lifecycle enum `index-state`
(scheduled for creation/deferred/building/pending/online/offline/abridged).
Same underlying subject (a GSI index's condition), two unreconciled
vocabularies from two different documentation surfaces. Left unmerged, per
the project's standing rule against inventing a link without textual
evidence.

### Monitoring: a self-inflicted reconciliation gap, closed

Round 5's `reference/` batch minted `monitoring:alert`/`event`/`health-advisor-report`
and others, and that round's own reconciliation writeup described them as
promoted - but no `concepts/monitoring/` files were ever actually written.
This round's direct read of `monitoring.md`/`alerts.md`/`health-advisor.md`
confirmed the underlying concepts cleanly (unlike the role catalog, no
correction was needed to the *content*) but surfaced the gap in the
*process*: promoted now, for the first time, along with a genuine
correction found along the way - round 5 had conflated event severity
(Info/Warning/Critical) and Health Advisor severity (Good/Needs Review/Warning)
under one candidate name; they're split into `monitoring:event-severity-enum`
and `monitoring:health-advisor-severity-enum` now that both are read
authoritatively. This is the **third** instance of the same reconciliation-gap
shape - after round 2's `gatedByBillingPlan` (closed in round 6) and round 3's
Java SDK concepts (found in round 4) - and notably the first one this
reconciler introduced itself while already aware of the pattern.

### Other findings, left at the extraction layer (not promoted this round)

A recurring role-label-drift pattern, now with a second independent
instance (`analytics-links.md`'s "Cluster Data / Reader" pointing at
`manage-documents.md`'s anchor for "Data Writer") folded into the existing
`docs-issues/cloud-projects-role-naming-drift-cluster-manager.json` rather
than filed separately. A rich alert-integration model (Slack and Microsoft
Teams share one payload schema in different wrappers; Webhooks uses an
entirely different field-naming scheme) and several `xdcr:`/`backup:`/
`analytics:` namespace concepts from this round's batches - not promoted at
this volume, noted here rather than silently dropped, consistent with the
"left on the watchlist" sections of prior rounds.

### What this round confirmed about the method itself

- **The privilege/role undercounting pattern is now confirmed as durable
  across two consecutive rounds on two different vocabularies of the same
  product.** Worth treating as an expected outcome, not a surprise, for any
  remaining Capella vocabulary still built primarily from statement-page
  citations rather than a feature's own reference page.
- **Reading an authoritative page can resolve a question by revealing it was
  the wrong question.** `cluster-rbac.md` was read to test the role catalog;
  it turned out to be about something else entirely (the privilege catalog),
  which is itself informative - not every hypothesis a batch is sent to test
  gets a yes/no answer on its own terms.
- **The reconciliation-gap pattern (narrated as promoted, never filed) has
  now recurred three times, including once where the reconciler already knew
  to watch for it.** Awareness alone doesn't prevent it - some kind of
  automated check (e.g. a script asserting every concept/predicate named in
  a round's reconciliation.md section has a corresponding file) would catch
  this more reliably than reconciler vigilance.

---

## Round 8 — `cloud/eventing/` (67 pages)

Scope: all 67 pages of `cloud/eventing/` - Capella's Eventing feature
(JavaScript functions reacting to KV mutations). Zero prior coverage;
genuinely new territory, the last major untouched `cloud/` directory besides
`guides/`. ~26 conceptual/example pages plus ~41 individual JS handler
code-sample pages (each demonstrating one operation pattern - `advancedGetOp`,
`curl-post`, `simpleTimer`, and so on). Run as 7 parallel batches - one for
core concepts/RBAC, one for function management, one for worked examples, and
four for the handler-sample pages. Total usage: ~735,000 tokens for 67 pages
(~11,000 tokens/page, in line with this session's other waves), roughly $2.

### Headline finding: Eventing needed no new structural layer - a clean negative result

Every genuine "new product/feature" test this project has run so far found
something the existing vocabulary couldn't express (Sync Gateway's channels,
round 3; the Java SDK's transaction layer, round 4). Eventing is the first to
resolve the other way: it slots cleanly into existing concepts everywhere.
Function lifecycle (Deployed/Undeployed/Paused + transitory states) is
structurally identical to `index-state`'s stable-plus-in-progress shape.
Timers are explicitly documented as "limited asynchrony," reusing the parent
Function's option set and lifecycle rather than introducing a new concurrency
model. Every documented "unsupported feature" (no global state, no general
async/await, no browser extensions) is explained by pointing back at an
existing Eventing construct, not by needing a new one. `eventing-rbac.md`
confirmed the same shape at the access-control layer: `privilege:capella-advanced-access-eventing-manage`
(round 7's only evidence for this privilege) is never granted alone - every
target-keyspace row bundles it as "Data Read and Eventing Manage," the exact
compound-privilege shape `cluster-rbac.md` already showed for other
privileges. No new Eventing-specific privilege or Capella role exists; access
is gated purely by the existing `capella-role:*`/credential-type model. This
round joins round 7's XDCR and Analytics findings as a third confirmation
that "genuinely new feature" doesn't automatically mean "genuinely new
access-control shape" - a real, recurring outcome now, not a one-off.

### The real gating mechanism turned out to be a different layer entirely: bindings

While the management-plane privilege model confirmed "nothing new," the
*runtime* access-control layer is a genuinely distinct mechanism this round
promoted for the first time: `eventing:binding` (and its
`bucket-alias`/`url-alias` subtypes) is what actually gates what a deployed
function can touch at runtime - which buckets/scopes/collections, which
external URLs via `curl()` - entirely separate from the
who-can-create/deploy/manage privilege gate. Two distinct gating layers for
one feature, cleanly split by function (identity/management vs.
resource-access), not a contradiction of the "nothing new" finding but a
genuine addition to it.

### Real constraints found reading the handler examples closely

- **N1QL from a handler has one genuine new constraint**: the `N1QL()` call
  returns a streamed cursor the handler must explicitly `.close()` - no
  standalone SQL++ statement-reference page has an equivalent resource to
  release. Also: inline SQL++ is prohibited from updating a handler's own
  source bucket specifically to prevent infinite-recursion loops; `N1QL()`
  must be used instead in that one case.
- **A real API asymmetry**: `OnDelete()` doesn't supply the deleted
  document's body the way `OnUpdate()` does - forcing workarounds (a
  proxy-doc pattern in one example, KEY-prefix filtering instead of a
  `doc.type` check in another) independently confirmed on two separate
  handler pages.
- **`self_recursion`**: a targeted option (not a new API surface) letting a
  handler reinvoke itself to checkpoint-and-continue a long-running paginated
  query - Eventing's version of a continuation pattern, expressed as a flag.
- **Two clean negative results, from pages specifically read to test them**:
  "cascade delete" has no native cross-document consistency/transactional
  primitive at all - it's just an `OnDelete` handler synchronously firing a
  second SQL++ statement, explicitly not transactional. The "high risk
  patterns" page turned out to be about business risk (flagging fraudulent
  transactions), not platform-level safety constraints - contrary to what it
  was read to test, itself a useful result.
- **A fifth thing called "role."** `troubleshooting-best-practices.md` names
  a classic, cluster-wide RBAC role - "Eventing Full Admin," introduced at
  Server 7.0.0 as a deliberate carve-out of Full Admin - joining
  `role:full-administrator`/`local-user-security-administrator` (round 5) as
  a third member of that specific classic-RBAC family, and a fifth distinct
  "role" concept overall alongside `capella-role:*`/`rbac-role:role`/`sgw:role`.

### A third variant of the unadapted-content pattern

Distinct from the known version-string and edition-badge anomalies: several
pages bleed self-managed Server content into the Capella tree by *naming* -
`eventing-function-export.md` says "Couchbase Web Console" where a Capella
page should say "Capella UI"; two example pages reference self-managed-only
CLI tooling. Logged as `docs-issues/cloud-eventing-unadapted-server-content.json`.
Same likely root cause as the other two variants, a different symptom.

### What this round confirmed about the method itself

- **A clean negative result is still a result.** Four rounds now
  (round 3/Sync Gateway, round 4/Java SDK transactions positive; round
  7/XDCR+Analytics, round 8/Eventing negative) have tested "does this new
  feature need new structure," and the negative answer is exactly as
  informative as the positive one once it's this consistent - it's evidence
  about which *kinds* of features tend to need new vocabulary (concurrency
  and identity models) versus which don't (features that compose existing
  primitives with a new access-control wrapper).
- **Splitting one feature's access control into "who can manage it" vs. "what
  it can touch at runtime" is a real, recurring shape**, not specific to
  Eventing - worth watching for on any future feature this project reads,
  the same way the org-scope/project-scope role split (round 6) turned out to
  be a repeatable pattern once named.

---

## Round 9 — `cloud/guides/` (33 pages) - closes out `cloud/` entirely

Scope: all 33 pages of `cloud/guides/` - task-oriented "how to" pages for
data operations, indexing/optimization, and query/UDF workflows. Unlike every
round since round 5, this directory was never expected to be new territory:
it's guide-level content wrapping SQL++ statements and operations already
exhaustively documented (`cloud/n1ql/`, round 5; `cloud/javascript-udfs/`,
round 6). Run as 3 parallel batches. With this round done, **every page in
`cloud/` has now been extracted** - 5 rounds (5 through 9), ~460 pages, since
round 5 started the real-scale phase of this project. Total usage: ~437,000
tokens for 33 pages (~13,200 tokens/page), roughly $1.30.

### Headline finding: the reuse hypothesis held, with three genuine gaps found along the way

Unlike rounds 5-8, this round's expectation was confirmation, not surprise -
and that's mostly what happened: the overwhelming majority of concepts
across all 33 pages were reused verbatim from round 5/6's statement and
operation vocabulary, zero new SQL++ statement concepts minted anywhere.
But reading guide-level content (rather than pure reference content) still
surfaced three real gaps the reference pages never needed to cover:

- **`sdk:subdocument-operations`** - `sdk:kv-operations` (itself still
  unpromoted, part of the round-3 Java SDK backlog) is scoped to
  whole-document operations and never mentions path-level `lookupIn`/`mutateIn`
  - needed by three separate data-operation guides.
- **`sdk:query-index-manager`** - the SDK's own programmatic
  create/drop/watch-index interface, an alternative to the SQL++
  CREATE/DROP INDEX statements that no statement-reference page would have
  reason to mention.
- **`sdk:bulk-import-workflow`** - a third bulk-load path (SDK-scripted
  CSV/JSON parsing + upsert), distinct from both the Data API (round 6) and
  the CLI `cbimport` tool.

### A stateful entity that a reference page had only seen as a function usage

`index-advisor.md` revealed that the Index Advisor's "session" isn't just
another call to the already-promoted `ADVISE`/`ADVISOR` functions - it's a
genuinely stateful object (start -> collect -> stop/get/list/purge) with its
own lifecycle. The reference page (round 5) only flagged this as a function
sub-usage. Promoted `n1ql:advisor-session` below the usual recurrence bar for
this reason - a real modeling upgrade, not just a new label for something
already understood.

### A round-5 open question closed with direct textual evidence

Round 5 flagged, more than once, that no page gave textual evidence linking
the SQL++ transaction-statement family to the Java SDK's `sdk:distributed-transaction`
layer (round 4) - left as an explicit open question each time rather than
guessed at. `cloud/guides/transactions.md` closes it: "This how-to guide
covers SQL++ support for Couchbase transactions. Some SDKs also support
Couchbase transactions" - the guide's own framing draws the boundary
explicitly. The two transaction layers are related but distinct SQL++/SDK
surfaces, confirmed by the docs themselves rather than inferred.

### Minor findings, left as backlog rather than fixed here

- `select.md` re-explains "query context" inline rather than only linking to
  the reference page that already covers it - consistent facts, no
  contradiction, so not logged as a docs-issue (a genuine inconsistency would
  be), but the clearest single instance in this round of re-explaining
  instead of linking.
- The CLI tool `cbimport`/`cbexport` has two unreconciled ids from two
  different rounds (`tool:cbimport`/`cbexport` and `server:cbimport`/`cbexport`),
  neither promoted - folded into the existing "run a normalization pass over
  `extractions/`" backlog item rather than fixed individually.
- Three more small id drifts flagged by this round's batches (`n1ql:index-partitioning`
  vs. `indexes:index-partitioning`; `n1ql:aggregate-function` vs.
  `-functions`; `indexes:groupby-aggregate-performance` vs.
  `index-type:group-aggregate-pushdown`) - same backlog item.

### What this round confirmed about the method itself

- **A "should mostly confirm" round is still worth running in full, not
  skipped.** The reuse hypothesis held for the vast majority of this round's
  33 pages, but the exceptions (three SDK-layer gaps, one stateful-entity
  upgrade, one closed cross-round question) wouldn't have surfaced from
  reading the reference pages alone - guide-level content asks slightly
  different questions of a feature than reference content does, even when
  it's nominally about the same thing.
- **Completing a whole top-level directory is itself a checkpoint worth
  marking.** `cloud/` took 5 rounds (5-9) and roughly 460 pages to cover in
  full, after round 2's original 50-page sample. The registry survived that
  span without needing a restructuring beyond the two-catalog role split
  (round 6) and the privilege-catalog expansion (round 7) - both real, both
  already documented, neither requiring the earlier promoted core
  (privilege/edition/version shapes from round 1) to change.

---

## Round 10 — `server/current` wave 1 (38 pages) - first wave into a second product tree

Scope: the first wave of Couchbase Server 8.0, all of it under `n1ql/` -
25 pages selected by **diff-gating** (the `server/current` pages whose Capella
twins had already been extracted and which diverged most from them, by
`difflib` changed-line count) plus 13 pages that exist only on Server and have
no Capella counterpart at all. Run as 5 parallel batches. Two structural
priorities were given in the brief: version/edition gating vocabulary, which
the registry was weakest at after nine rounds, and reuse of the ids already
established by the `cloud/` rounds.

Before dispatching any agent, the existing 58 `server/` records were moved to
`extractions/server/7.2/` and their `page_id`s rewritten to include the
version. This was not tidying: those records carried version-neutral page ids
(`server/n1ql-language-reference/createindex`) alongside version-bearing source
paths (`server/7.2/…`), so a multi-version ingest collided by construction -
wave 1 would have silently overwritten `createindex.json` and `alterindex.json`
with 8.0 content and no diagnostic. Pure `git mv` plus one field rewrite, and
the reason it's worth recording is that the collision was structural and
invisible: nothing in nine rounds of a single-version-per-product corpus would
have surfaced it.

### Ruling: `current` is not a version, and the extraction tree says so

Wave 1 was first written to `extractions/server/current/`, mirroring the docs
tree. That is now `extractions/server/8.0/`, with every `page_id` rewritten from
`server/current/…` to `server/8.0/…`. The ruling behind the rename:

**`current` is a pointer, not a version.** It has no referent of its own - it
denotes whichever release is newest at the moment of reading. An ontology whose
entire value proposition is stable identifiers cannot mint a node whose meaning
silently changes on every major release. Left as it was, `page_id`
`server/current/n1ql/…/createindex` would come to denote 9.0's page while
continuing to sit in a record whose evidence was quoted from 8.0's - the same
class of latent, structural, no-diagnostic collision as the version-neutral
`server/` ids described above, and found the same way: by asking what the second
version would do to the first.

The distinction that makes this non-obvious is between the three fields, which
now deliberately disagree:

| field | value | why |
|---|---|---|
| `page_id` | `server/8.0/n1ql/…/transactions` | an ontology identifier - must be stable, so it names the release |
| `source_version` | `8.0` | already correct; the rename makes `page_id` agree with it |
| `source_path` | `server/current/n1ql/…/transactions.md` | a **filesystem** path - must keep resolving on disk, so it keeps the alias |

A record whose `page_id` and `source_path` differ in exactly this way is
correct, not inconsistent, and `verify-evidence.py` reads `source_path` (never
`page_id`) precisely because the gate's job is to open a real file. All 38
records still pass it after the rewrite.

Two consequences worth recording, because they cut in opposite directions:

- **`docs-issues/` `about:` entries were rewritten too** (31 ids across 21
  files). Those hold page ids, so they inherit the ruling.
- **`seeAlso` objects pointing at `server/current/…` were deliberately *not*
  rewritten** - 11 of them, all in `cloud/` records. Their evidence is a literal
  Markdown link in the Capella page's own text
  (`../../../server/current/analytics/6_n1ql.md`), and what that page links to
  *is* the floating alias: it will resolve to 9.0 with no edit. Pinning the
  object to `server/8.0` would assert something the source does not say, which
  is the "never invent links" rule applied to a version axis. So the corpus now
  distinguishes a `seeAlso` pinned to a release from one aimed at whatever is
  current - a real difference in what the docs commit to, and one that would
  have been erased by a blanket find-and-replace.

Where does the alias itself live, then? In exactly one place, as the user's own
framing suggested - a single assertion rather than a namespace.
`concepts/version/server-8-0.json` carries `"isCurrentRelease": true` and
`"docsTreeAlias": "server/current"`, flagged in its note as the only
deliberately mutable fields in `concepts/`. On the next major release those two
fields move to the successor's file; nothing else in the registry moves at all.
That is the whole point of refusing to mint `version:server-current`: the cost
of a release becomes one edit instead of a re-pointing pass over every id that
mentioned it.

### Headline finding: an extraction agent fabricated its evidence, and reviewer judgement did not catch it

`prepare.json` came back confident, internally consistent, and better argued
than most correct records. Eleven of its thirteen relations quoted sentences
that **do not appear on the page**. Two were substantive, not stylistic:

- It asserted `n1ql:automatic-reprepare-on-index-changes availableSince
  version:server-8-0`, quoting "In Couchbase Server 8.0 and later, the Query
  service automatically reprepares...". No such sentence exists. The page
  states no version for that behaviour, or for anything else. The only real
  basis for the claim was that the page lives in the 8.0 tree.
- Its `n1ql-feat-ctrl` evidence read "To disable this feature, set bit 23..."
  where the page reads "**To enable** the feature, set bit 23...". Inverted
  polarity, in a quotation.

A third relation claimed prepared statements are "propagated to all query
nodes"; the page describes cache priming, not propagation. The remaining eight
were close paraphrase - the extraction schema has required a direct quote since
round 1, and paraphrase had been drifting past unremarked for nine rounds.

What matters is not that one agent hallucinated - that was always going to
happen at some rate - but **which controls failed**. Every human-legible
control passed: the record parsed, reused promoted ids correctly, gave
plausible mint rationales, and its fabricated sentence was *more* idiomatic
than the real one it displaced. The only control that caught it was mechanical
string comparison against the source file, performed by a sibling batch that
happened to re-read the page.

So the round produced `poc/verify-evidence.py`, now a standing corpus check:
every relation's `evidence` must appear verbatim (whitespace- and
quote-normalised only) in the page named by its `evidence_source`, or, absent
that field, in the record's own `source_path`. Deliberately **not** normalised:
wording. A paraphrase is a failure, by design.

Running it over the whole corpus, after this round's repairs:

| tree | verbatim | unquotable | no evidence field | total relations | records with ≥1 failure |
|---|---|---|---|---|---|
| `server/current` | 509 | 0 | 0 | 509 | 0 of 38 |
| `cloud` | 1,555 | 169 | 0 | 1,724 | 92 of 407 |
| `server/7.2` | 129 | 32 | 130 | 291 | 16 of 58 |
| `sync-gateway` | 56 | 68 | 0 | 124 | 12 of 13 |
| `java-sdk` | 49 | 23 | 0 | 72 | 11 of 15 |
| `couchbase-lite` | 30 | 30 | 0 | 60 | 10 of 12 |
| **all** | **2,328** | **322** | **130** | **2,780** | **141 of 543** |

Read that carefully, because it says two different things. `server/current` at
509/509 is what a wave looks like when the check is run *during*
reconciliation and the failures are repaired - this round's 100% is an
artefact of the check existing, not of the agents being better. `server/7.2`'s
130 relations with no `evidence` field at all are round 1, which predates the
requirement. But `sync-gateway` at 45% verbatim and `couchbase-lite` at 50%,
with 12 of 13 and 10 of 12 records affected, are **materially unreliable** and
should be re-extracted rather than patched; round 3's cross-product test
reached a correct conclusion about vocabulary reuse, but its records are not
sound sources of fact. Filed as backlog, not fixed here.

One honest correction to an earlier count in this document's own history: the
first pass at this audit reported far smaller failure numbers (e.g. 49 for
`cloud`). Those were *records* containing a failure under an earlier script,
not relations, and an intermediate version of that script also let
empty-evidence relations pass silently, because `"" in text` is `True` in
Python. The table above counts relations, and the record counts are given
alongside so the two readings can't be confused again.

### The version-gating result is the opposite of what the brief expected, and it is a better result

The brief called the vector-index pages "prime `availableSince` territory."
They contain none. Neither `createvectorindex.md`, `altervectorindex.md` nor
`dropvectorindex.md` states its own availability version. The single explicit
8.0 gate in the whole wave is on `createindex.md`, and it gates a *capability
added to a pre-existing statement*: "In Couchbase Server 8.0 and later, the
CREATE INDEX statement also allows you to create Composite Vector indexes."

The mechanism is straightforward once seen. An existing statement needs an
"and later" qualifier to mark what changed. A statement introduced wholesale
has nothing to contrast itself with, so it carries no marker at all.
**Version-evidence density is inversely correlated with how new a feature is** -
exactly backwards from what a version-mining pass would assume, and worth
stating as a design constraint on any release-notes-style query built over
this vocabulary.

Two vocabulary consequences, both promoted:

- **`documentedForVersion` (6 files), kept strictly separate from
  `availableSince`.** Batch B minted it to record "I know which documentation
  tree I read this in" without that being upgradeable into "I know when this
  appeared." That is precisely the inference `prepare.json` made illegitimately.
  Two batches in the same wave, given the same brief, went opposite ways on the
  same temptation - and the disciplined one invented vocabulary to stay
  disciplined. `availableSince` now requires the page to state a version;
  `documentedForVersion` requires only that the page exist.
- **`deprecatedIn` (2 files), the gap the brief named.** Nine rounds produced no
  deprecation predicate at all. It folds `deprecatedSince` (round 1's
  `server/7.2` mint for Views, three rounds earlier, identical shape). Two
  proposals were rejected with reasons: `removedIn`, because nothing in the
  corpus dates a removal - both sightings say only "will be removed in a future
  release", so the term is reserved but unfiled; and `noOpSince`, batch B's
  suggestion for `encoded_plan` ("ignored and has no effect" since 6.5),
  because deprecated-versus-inert is a property of the evidence, not of the
  relation.
- **`retainedForLegacyCompatibility` (3 files)** sits beside `deprecatedIn` on a
  clean axis: one dates when a thing stopped being recommended, the other says
  why it nevertheless still exists. Both can hold of the same subject -
  `n1ql:encoded-plan` has both. It folds `documentedAsLegacy`, minted in the
  same wave by a different batch for the same shape.

Also found and **not** solvable with current vocabulary: `join.md` needs to say
"version X **and earlier**" - "Couchbase Server version 4.1 and earlier
supported only lookup joins" is an upper-bounded fact, the mirror image of
`availableSince`, and every predicate in the registry is lower-bounded. Left
open deliberately: one occurrence, and inventing `availableUntil` on a single
sighting is how the registry accumulates near-duplicates.

### A new failure mode: quotable evidence, wrong object

Three relations in this wave quote real sentences and attach them to objects
the sentence does not support:

- `n1ql:lookup-join documentedAsLegacy version:server-4-1`, quoting "A _lookup
  join_ is a legacy syntax for joins." The version is not in that sentence -
  though it *is* on the page, 
  three lines later ("Couchbase Server version 4.1 and earlier supported only
  lookup joins"), so this one is under-quoting rather than invention.
- `n1ql:prepare inheritsPrivilegesFrom n1ql:prepared-statement` - the object
  should be the privilege source, not the artefact.
- `n1ql:fn-evaluate inheritsPrivilegesFromCaller n1ql:misc-utility-functions` -
  the object is the page section, not the caller.

All three pass `verify-evidence.py`, and should. The script's own docstring
predicted this ("checks quotability, not correctness... a floor, not a
ceiling"); this round supplies the first concrete instances. It is a distinct
defect class from fabrication and needs a different control - the write-time
gate under discussion catches fabrication only. Worth being explicit that a
green evidence check is *not* a green record.

### Structural finding: the index namespaces conflate four different axes

Promotion of every index concept in the corpus is **deliberately deferred** this
round, which is the only time in ten rounds a whole high-recurrence family has
been held back. The reason: 93 candidate ids are spread over four namespaces
(`index-type:` 17, `indexes:` 25, `index:` 21, `vector-index:` 30) with real
cross-namespace duplicates - `covering-index` exists in three of them,
`primary-index`, `secondary-index`, `composite-secondary-index`,
`partial-index`, `functional-index`, `array-index` and `duplicate-index` in two
each - and, more seriously, the members answer four different questions:

1. **index kind** - primary, secondary, composite, partial, functional, array, covering
2. **index technology / owning service** - GSI, Search/full-text, Analytics, View, vector
3. **storage engine** - plasma/standard, memory-optimized (MOI), ForestDB
4. **query-execution optimisations that are not index types at all** - group-aggregate
   pushdown, predicate/order/pagination pushdown, bloom filters, early filtering,
   sequential scan

`index-type:gsi` was promoted in round 5 as a minor, low-stakes concept. Filing
`index-type:moi`, `index-type:composite-vector` and `index-type:covering-index`
as its siblings would assert that a storage engine, a vector index kind and a
plan property are the same sort of thing. This is a third distinct species of
error from the two the earlier rounds catalogued: not a naming collision
(round 1, round 6) and not partial-sampling (rounds 5-7), but **axis
conflation** - a namespace whose members are individually correct and
collectively incoherent. Promoting them would encode it permanently, so the
right move is to read `server/current/learn/services-and-indexes/` in a later
wave, which is where the axes are actually documented, and decide the taxonomy
from the authoritative pages rather than from statement pages' passing mentions.
That is the round-5/6/7 lesson - prefer a feature's own reference page - applied
prospectively for once instead of retrospectively.

### A cross-round predicate family, consolidated

Round 8 minted `cascadesDeletionTo` (3 files: deleting a cluster reaches its
backups; switching one off reaches its replications) and
`cascadesLifecycleChangeTo` (3 files: collection and storage-keyspace lifecycle
reaching Eventing functions). Round 10 minted `cascadesTo` (DROP FUNCTION
reaching the managed UDF) and `removesAllSavepoints` (COMMIT and ROLLBACK
tearing down savepoints). Nine occurrences, seven files, three product surfaces,
one shape - folded into **`cascadesTo`**, with the specific verb left in the
evidence rather than the predicate name.

`removesAllSavepoints` is the instructive rejection: a predicate whose name
contains its own object cannot recur outside the page that motivated it, and it
met the 2-file bar only because two sibling pages in one batch state the same
sentence. Its negation was promoted separately as **`doesNotAffect`** (2 files,
2 products) - DROP FUNCTION deliberately leaves the external library in place,
and Capella UI auth and programmatic access are disjoint systems. Absence of
cascade is a stated fact, not a hole in the data.

The trade-off is real and accepted: folding loses the
deletion/lifecycle/teardown distinction at the predicate level, and a consumer
that needs deletions specifically will have to read evidence strings.

### The promotion backlog, quantified and largely paid down

Fixing a bug in this round's own recurrence script (a regex that stripped
`.jsonld` but not `.json`, so every promoted predicate looked unpromoted)
exposed the real state of the registry: **`n1ql:query-context` had recurrence
22 and had never been promoted.** Nor had `n1ql:create-index` (20),
`n1ql:cost-based-optimizer` (15), or the entire SQL++ statement vocabulary the
`cloud/` rounds had been reusing consistently since round 2.

This is the "reconciliation itself can leave gaps" limit at a scale the earlier
rounds only hinted at. Rounds 5-9 reconciled narratively, promoted the
structurally novel material, and left the bread-and-butter statement concepts
in the extraction layer because nothing about them was *interesting*. Recurrence
22 is not interesting; it is load-bearing.

62 concepts promoted this round, most of them that backlog: the SQL++
transaction family (9), the statement and clause vocabulary (23), the Query
service REST API and the request/node/cluster settings tiers (6), five
services, four versions, two tools, and the access-control terms Server states
that Capella does not. 19 predicates promoted.

### Namespace rulings

- **`tool:cbq-shell` is canonical (18 files), folding `n1ql:cbq` (13).** A CLI
  tool is not a SQL++ language construct, so `n1ql:` was wrong. But the
  important half of the ruling is the *refusal* to merge: **`capella:cbsh` is a
  different tool.** Couchbase Shell (`cbsh`) has its own documentation site and
  is listed separately from `cbq` in `cloud/reference/command-line-tools.md`,
  and one page mints both ids side by side, correctly. A name-similarity
  normalization pass would have collapsed them. (`capella:cbsh`'s id is
  nonetheless a misnomer - the page says it works with both Server and Capella -
  filed to the normalization backlog rather than renamed mid-round.)
- **`monitoring:` is not renamed to `capella-alerting:`.** The rename was
  proposed on the basis that all 13 then-known members were Capella pages. The
  first Server page in the corpus to touch monitoring produced
  `monitoring:awr-document`, and a Capella-specific namespace would have forced
  it elsewhere for no reason. A proposal made from a single-product sample,
  refuted by the first page of the second product - the same shape as rounds
  5-7's undercounting lesson, caught before it was acted on rather than after.
- **`api:query-rest-api` folded into `n1ql:query-service-rest-api`.** Six files
  each, disjoint, minted by two batches *in the same wave* for the same
  endpoint. This is the standing "a written registry stops agents re-litigating
  the past, not each other in the present" limit, observed live.
- **`rbac-role:query-system-catalog` and `rbac-role:query-manage-system-catalog`
  are privileges, not roles**, and fold into `privilege:`. The docs themselves
  are the source of the confusion: `metafun.md` calls `query_system_catalog` a
  "role" while the AWR and monitoring pages treat it as a privilege. Filed as a
  docs issue as well as fixed in the registry.
- **`role:` is the Server RBAC namespace.** `n1ql-auditing.md` settles a
  question the round-2 record got backwards: `role:full-administrator` and
  `role:local-user-security-administrator` are genuine Server RBAC role names
  documented in `server/current/learn/security/roles.md`, so their appearance on
  Capella pages is unadapted-content porting, not the Capella model. The
  direction of inheritance is the opposite of what the Capella extraction
  assumed.
- **`role:administrator` (3 files) not promoted.** All three occurrences are the
  docs using "administrator" loosely where the RBAC catalog has specific role
  names. Filed as a docs issue instead - promoting it would launder a docs
  defect into the ontology.
- **Version ids: 31 distinct ids for roughly 20 real versions.** Dash-versus-dot
  is the bulk of it (`version:server-8-0` 16 files vs `version:server-8.0` 3;
  `server-7-6` 6 vs `server-7.6` 4 vs `couchbase-server-7.6` 1). Canonical form
  is the dash-separated one set in round 1. Folded for the four versions
  promoted this round; the rest goes to the normalization backlog now with a
  measured count rather than an impression.
- **`port:` minted as a namespace, but port concepts not promoted.** `usesPort`
  is promoted (below the bar, on significance - the registry had no vocabulary
  for network exposure at all after nine rounds, which is remarkable for a
  database). Whether a port number is a `skos:Concept` or a literal is a real
  modelling question and 8093 is not a concept in the sense `n1ql:select` is.
  Deferred to JSON-LD drafting.

### `sdk:transaction-query-mode` re-namespaced, and a watchlist payoff

Round 4 promoted this concept below the recurrence bar on significance, from a
Java SDK page, and filed it under `sdk:` on the strength of where it was read.
Wave 1 located its defining paragraph at
`server/current/n1ql/n1ql-language-reference/transactions.md:94-96`: it is a
Query-service behaviour that the SDK page *describes*. Now
**`n1ql:transaction-query-mode`**, with the `sdk:` id kept as an alias stub
carrying round 4's record - those extraction records cite it and were not wrong
to; the id was accurate about where the concept was found, only about where it
belongs.

At recurrence 2 across two product trees it no longer needs the significance
exception. Nor does its predicate: `triggersPermissionModeChange` was
watchlisted at recurrence 1 in round 4 and is promoted here on an independent
second sighting from the SQL++ side. Two of the round's promotions are
watchlisted recurrence-1 mints that turned out to be early rather than
over-specific, which is some evidence the watchlist earns its keep.

### Diff-gating: useful for ordering, misleading as a yield estimate

Wave 1 was selected by changed-line count against already-extracted Capella
twins, on the reasoning that divergence predicts new vocabulary. It did order
the wave usefully. But batch A found that the 280-500 changed lines on the
transaction pages are dominated by example re-rendering, with no SQL++ semantics
differing at all, and `cbq.md`'s 162 changed lines reduce to three substitutions
repeated - of which only two are genuine capability differences (multiple
credentials work on Server and are silently ignored on Capella; and `cbq`
itself has no version gate on Server, where it ships in the installation
directory, while the same 7.6.2 sentence is a hard prerequisite on Capella
where the tools package is the only way to get it).

So raw changed-line counts overstate yield. Future gating should weight prose
sections over code blocks and example output. Recorded in
`ingest-cost-and-time-estimate.md` as well, since it affects wave planning, not
just this round.

### Negative results worth recording as results

Three batches reported "nothing to harvest" findings that are more useful than
they look, and the brief did not ask for them:

- **`n1ql-error-codes.md`: zero version annotations on 565 error codes.** Error
  tables are not a version source in this corpus; future waves should not spend
  budget mining them. But diffing the two products' tables shows Capella has 566
  codes and Server 565, differing by exactly one - which is a versioning fact
  neither page can state about itself.
- **The entire `n1ql-rest-api/` directory (12 pages) contains none of "and
  later", "since", "deprecated", "removed in", "Enterprise Edition" or
  "Community Edition".** Version-unannotated end to end, in sharp contrast to
  the SQL++ language reference.
- **`n1ql-auditing.md` contains zero version references of any kind**, and its
  single occurrence of "enterprise" is inside a sample User-Agent string,
  `Couchbase Query Workbench (5.1.0-1434-enterprise)` - an artefact of a
  seven-year-old copied example, not a statement about availability.

Each was verified independently rather than relayed. The wave's framing - which
named version gating as "THE PRIORITY" - is the most likely cause of the one
fabrication, and negative results are the antidote: a brief that treats "this
page says nothing about versions" as a finding of equal standing removes the
incentive to produce something.

### New `docs-issues/` (22)

The largest batch in any round, unsurprisingly for a first pass over a
long-lived tree. Grouped:

- **Wrong content**: `altervectorindex.md` inherits all three of
  `alterindex.md`'s version gates verbatim, so it asserts that ALTER VECTOR
  INDEX has been available since Couchbase Server 5.5 - for a statement that
  cannot predate 8.0. `exnamed.md`'s parameter table says `$davl` where the
  statement and curl command both say `$dval`.
- **Missing version/edition annotation**: the three new vector statements state
  no availability version; `metafun.md` has lost three of the four availability
  badges its Capella twin carries; `stringfun.md` has lost all nine, including
  genuinely-new-in-8.0 `COMPRESS()`/`UNCOMPRESS()`; `n1ql-auditing.md` has no
  Enterprise badge although the auditing page it links to does; the Capella AWR
  page states no version for a feature new in 8.0.
- **Broken or wrong links**: `join.md`'s USE NL hint points at the USE HASH
  anchor (also wrong on the Capella twin, so upstream in shared source);
  `time-series.md`'s `preserve_expiry` link is wrong twice over - wrong anchor
  name *and* a stray `}` inside the URL - and correct on the Capella page;
  Capella's AWR page has unresolved Antora xrefs for the report generator.
- **Stale content**: `insert.md`'s Security Requirements section is written
  against the pre-RBAC SASL-bucket model, directly above a correct RBAC section;
  `extimeout.md` describes timeouts as set "when starting the query engine";
  `monitoring-n1ql-query.md`'s example outputs are all from a 7.0.0 build;
  `n1ql-auditing.md`'s examples are dated 2018.
- **Contradictions and oddities**: `exsuccessful.md` says POST and GET are
  interchangeable while `intro.md` calls GET the "Read-Only Query Service";
  `exserviceerror.md` is malformed three ways at once (a mangled `&lt;` as
  `$lt;`, an unfilled `"code": <int>` placeholder, a stray shell prompt);
  error code 2505 ("not supported in Community Edition") exists only on Capella,
  which has no Community Edition; `metafun.md` gates two EXTRACTDDL flag values
  on 8.0.1, a release later than the page itself; `insert.md` prescribes an
  *Index* Service scan timeout to fix a Data-path INSERT timeout with no
  explanation, where the Capella page names no setting at all.
- **Naming inconsistencies**: one privilege spelled `query_select` on `join.md`
  and _Query Select_ on `insert.md`; `query_system_catalog` called a role on one
  page and a privilege on others.

### Left on the watchlist (extraction-layer only, not promoted)

- `conditionallyPermittedWithinTransaction` (1 file, 2 occurrences). The finding
  behind it is real: transaction statement legality here is three-valued -
  permitted, conditional (EXECUTE FUNCTION and PREPARE, depending on the UDF
  body), prohibited - and the registry has no way to qualify a triple, so the
  conditional case has nowhere to live but a second predicate. A reification
  question for JSON-LD drafting, not a vocabulary question.
- `configuredPerNode` (1 file): configuration *scope* is a real axis (the CURL
  access list is per-node, not cluster-wide) and orthogonal to
  `configurableVia`, which was promoted.
- `hasExecutionConstraint` was promoted but is on the watchlist for a different
  reason: the name is broad enough to attract timeouts, quotas and privilege
  checks, all of which have their own predicates. If it starts collecting them,
  rename rather than widen.
- The `version:server-5-0` on `curl.md` is the version of the *remote* cluster
  CURL() is talking to, not of anything on the page. Currently parked under
  `requiresPrivilege` with an explicit flag rather than dropped. Whether version
  concepts may qualify a remote endpoint is unresolved; if not, the fact should
  be dropped rather than mistyped.
- Batch-reported id drifts, all to the normalization backlog:
  `n1ql:sqlpp`/`n1ql:sql-plus-plus` (folded), `n1ql:selectintro`/`n1ql:select`,
  `n1ql:createfunction`/`n1ql:create-function`,
  `n1ql:updatestatistics`/`n1ql:update-statistics`,
  `n1ql:dropfunction`/`n1ql:drop-function` - the same page-slug-versus-statement-name
  drift found in rounds 8 and 9, now with a pattern: agents mint the page slug
  when they read a page and the statement name when they read a mention of it.
- `cascadesDeletionTo`'s three occurrences use **page ids as subjects**
  (`cloud/clusters/delete-database` in the subject position), a schema violation
  from round 8 that survived that round's reconciliation. Fixing it is part of
  the folding into `cascadesTo`, and it is a reminder that the extraction schema
  has no validator for "subject must be a concept id".

### What this round confirmed about the method itself

- **The evidence requirement was decorative until something checked it.** Nine
  rounds of "evidence is a direct quote from the page - no paraphrase" produced
  2,780 relations of which 322 are unquotable and 130 have no evidence at all.
  The requirement was in every brief, agents cited it approvingly, and it was
  not enforced. Any invariant in a prompt is a hope; the same invariant in a
  script is a control. This is the single most transferable finding of the
  project so far, and it is not specific to hallucination - most of the 322 are
  ordinary paraphrase drift.
- **And a control that runs after the fact is still the wrong end of the
  pipeline.** `verify-evidence.py` finds a fabricated quote once it is committed
  to disk, in a file whose surrounding record may be entirely sound. The
  invariant now also runs *before* the write, as
  `hooks/gate-evidence.py` - a `PreToolUse` hook on `Write` registered in
  `.claude/settings.json`, which parses any record destined for `extractions/`
  and refuses it unless every quote is findable. Three design points are the
  reason it's worth recording rather than just doing:
  1. **It fires inside subagents.** This is the whole argument for a hook over a
     stricter brief. The fabrication came from one of ten parallel extraction
     agents; what reached a reviewer was its own ~300-word self-report. A
     `PreToolUse` hook is the only control in this pipeline that sits inside that
     agent's loop instead of downstream of its summary - and the agent's *own*
     summary is the least reliable available account of what it did, since a
     confidently fabricated quote yields a confidently accurate-sounding report.
  2. **It fails closed.** Exit status 2 blocks; the richer JSON
     `permissionDecision: "deny"` output was deliberately not used, because if a
     field name is wrong the hook silently *allows*. A gate that fails open on
     its own bugs is worse than no gate, since it also removes the suspicion that
     would have made someone check. Any internal exception exits 2 as well.
  3. **It imports the audit's own checking function** rather than
     reimplementing it. Two implementations of "is this quote on the page" would
     eventually disagree about whitespace or smart quotes, and then records would
     pass at write time and fail the audit - which teaches you to distrust the
     audit, the one artefact whose credibility the whole exercise now rests on.
  The gate also carries a second, deliberately narrow check, added because of the
  `n1ql:scan-consistency` finding below: a record may not claim a concept is
  **"promoted"** unless a registry file exists. Note what it does *not* check -
  every `reused` claim - because reusing an id that lives only at the extraction
  layer is correct and expected (`sdk:durability` has done so for seven rounds).
  The offence isn't reuse, it's asserting registry state that isn't there, and a
  gate that confused the two would block correct work daily and get switched off.
- **The gate's own cost, stated rather than discovered later: it converts
  fabrication into omission.** An agent blocked from inventing a quote can
  satisfy the gate by deleting the relation, and an omitted relation leaves no
  trace anywhere - no exit status, no diff, nothing for a later audit to find.
  That is a strictly better failure than a false triple, but it is not nothing,
  and it moves the burden onto reconciliation: the `linked-data-reconcile` skill
  now asks for a relations-per-page comparison against already-extracted twins,
  looking specifically for a *long* page with a thin record. Round 10's own
  distribution is the baseline (38 records, 509 relations, mean 13.4; the three
  sparsest are 30-line single-example REST pages, sparse for real reasons).
  Worth being honest that this countermeasure is weaker than the gate it
  supports - it's a heuristic read by a human, not a check - which is why it's
  recorded here as a known limit rather than as a solution.
- **Priming an extraction wave has a measurable cost.** The brief named version
  gating "THE PRIORITY FOR THIS WAVE" and listed `availableSince` first among
  the predicates to look for. The one fabricated triple in 509 was an
  `availableSince`. Batch C's prompt additionally called the vector pages "prime
  `availableSince` territory" - and those pages turned out to contain none at
  all, which is exactly the condition under which an agent asked to find
  something will produce it. The mitigation is not a milder instruction but an
  explicit statement that negative results carry equal weight, plus a mechanical
  check on the way out.
- **A green check is not a green record.** Three relations this round quote real
  sentences and hang them on wrong objects. Evidence verification is a floor.
  The next control needed is not more verification of the same kind but
  something that tests whether the *triple* is a fair reading of the quote,
  which is a judgement task and therefore the expensive kind.
- **Deferring a promotion is sometimes the finding.** Holding back all 93 index
  concepts is the first time in ten rounds that recurrence has been overruled
  by incoherence. The recurrence bar answers "is this term real?" and says
  nothing about "is this namespace's axis single?" - a gap in the promotion rule
  itself, not in this round's data.
- **Promotion debt compounds silently and is cheap to measure.** `query-context`
  at recurrence 22, unpromoted for eight rounds, was found by a one-line script,
  not by reading. The recurrence query should be run against the *whole* corpus
  every round, not just the round's own records - which is the same lesson as
  round 5's "sampled is not read", applied to reconciliation output instead of
  input. `poc/verify-promotions.py`, written at the end of this round, closes
  the other half: it lists every concept id and camelCase predicate named in
  this file that has no registry file. Its first run found five more real gaps
  (`sdk:kv-operations` at recurrence 8, `n1ql:prepared-statement`,
  `n1ql:encoded-plan`, and both AWR concepts), all promoted before this section
  was finished.
- **Re-running that check after the section was written found three more, which
  is the more interesting result.** A control that only pays out once is a
  cleanup; one that pays out again on the *same* round's freshly-written prose
  is a control. The second run promoted `n1ql:scan-consistency` (recurrence 6,
  spanning `cloud/n1ql`, `cloud/indexes`, `cloud/clusters/analytics-service`,
  `java-sdk` and `server/current/n1ql`), `n1ql:misc-utility-functions` (3), and
  `n1ql:aggregate-functions` (3). Three things worth recording about them:
  1. **A record asserted its own promotion and was wrong.** The
     `analytics-workbench.json` entry for scan consistency reads `"reused -
     already promoted (candidate_id first seen in cloud/indexes/…, recurring a
     third time in java-sdk/…, now a fourth time here)"`. Every clause of that
     provenance is accurate except the first two words: nothing had been
     promoted. This is the same failure shape as the fabricated evidence, one
     layer up - a confident, detailed, checkable-sounding claim about the
     *registry* rather than about the docs - and it argues that
     `reused_or_minted` should be machine-checked against the registry at write
     time, exactly as `evidence` should be machine-checked against the page.
  2. **Singular/plural id drift was hiding a gap, not just being untidy.** The
     `n1ql:aggregate-function`/`-functions` inconsistency was already logged as
     a normalization backlog item. What the check added is that *neither*
     spelling had a file. Cosmetic-looking id drift is worth treating as a
     promotion smell.
  3. **Four more ids resolved to already-promoted concepts under different
     names** - `clusters:xdcr` → `capella:xdcr` (a *namespace* mismatch, the
     first found at recurrence 5), `n1ql:selectintro` → `n1ql:select`,
     `n1ql:updatestatistics` → `n1ql:update-statistics`, and
     `plan:developer-pro` → `plan:developer-pro-support-plan`. Added to the
     normalization backlog rather than fixed here; `capella:` vs `clusters:` for
     XDCR is a real namespacing question, not a typo.
  Two candidates the check surfaced were **deliberately not promoted**:
  `auth:permission-set` (recurrence 2) is the placeholder round 6 minted rather
  than force-link an IdP-group mapping target to one of the five things called
  "role" - promoting it would give a name to an unresolved question; and
  `n1ql:sql-plus-plus` (2) is the language itself, and the only two SQL++
  *dialect* concepts in the registry both sit in the `cbl:` namespace
  (`cbl:server-sql-plusplus-dialect`, `cbl:sql-plus-plus-mobile`) because round
  3 minted them while reading Couchbase Lite. That is backwards - the mobile
  dialect is the variant and the server language is the baseline, yet only the
  variant's namespace has a home for either. Promoting `n1ql:sql-plus-plus`
  without settling that would create a third node in a family whose axis is
  already inverted, so it waits.

---

## Round 11 — `server/8.0/learn/services-and-indexes` (9 pages) - the first conceptual-prose batch, and the first written entirely under the write-time gate

Scope: all nine pages of `server/8.0/learn/services-and-indexes/` - the service
overview, the seven per-service pages, and the index overview - run as two
parallel batches. Small on purpose. Round 10 deferred the index taxonomy
explicitly until this directory was read, and it was worth waiting: after ten
rounds of statement syntax, REST payloads and management-plane forms, this is
the first batch of *architectural prose*. It is also the first batch in the
project's history in which every record was checked mechanically before it
reached disk.

Yield: **9 records, 211 relations, 0 evidence problems.** Mean 23.4 relations
per page, against round 10's 13.4 - conceptual prose is denser in extractable
relationships than reference syntax, which is the opposite of what nine rounds
of reference extraction would have predicted. The distribution:
services 38, backup-service 34, data-service 30, indexes 27, index-service 22,
query-service 21, search-service 17, analytics-service 16, eventing-service 6.

### Headline finding: the index taxonomy has two axes that cross, and one of them was invisible

Round 10 held back 93 index concepts rather than promote them into what it
called a four-way axis conflation, on the grounds that the authoritative page
had not been read. Reading it resolves the question, and not in the direction
round 10 guessed. `indexes.md` opens by declaring **"two classes of indexes"** -
Traditional and Vector - and then presents its content organised by index *type*
and by *providing service*. The class scheme is not a coarser version of the
type scheme. It cuts across it, in both directions:

- **Class cuts across service.** A Search index is Traditional; a Search Vector
  index is Vector. Same service, both classes.
- **Class cuts across type.** A Composite Vector Index is in the Vector class,
  and the page states outright that it *is* a Global Secondary Index - "Composite
  Vector Indexes … which are Global Secondary Indexes (GSIs) with a single vector
  column". So `index-class:vector` and `index-type:gsi` overlap directly.

So the correct model is two orthogonal axes plus a third, `providesIndexType`,
and the mistake available here was the natural one: reading "two classes" as the
top of a hierarchy and hanging the eight types beneath it. That model is refuted
by the page's own examples, which is precisely what a reader building a mental
taxonomy from this page will not notice. Promoted accordingly:
`index-class:traditional` and `index-class:vector` as a two-member closed family
on the page's own word "classes", `belongsToIndexClass` kept deliberately
separate from `isSubtypeOf` so that the two axes cannot be silently collapsed
later, and the four index types the round evidenced
(`index-type:primary-index`, `index-type:secondary-index`,
`index-type:hyperscale-vector`, `index-type:composite-vector`).

Two smaller results fell out of the same page. `index-type:secondary-index` and
`index-type:gsi` are stated to be the same thing by *both* pages independently -
that is the explicit source statement the never-merge-without-evidence rule
requires, so they are linked by `isSynonymOf` rather than left as a suspected
duplicate; both surface terms are kept as ids because the docs use both and a
reader searching either should land somewhere. And `index:view` is the only one
of the eight index kinds with **no** providing service named, because Views come
from a deprecated engine the page declines to name - so an ontology that assumes
every index type has an owning service has a hole in exactly one row
(`server-views-index-no-owning-service`).

### The registry had no subsumption vocabulary at all

Across 195 concepts and 64 predicates, nothing in the registry could say *X is a
kind of Y*. Eleven rounds of extraction had produced a flat vocabulary, because
reference documentation states behaviour and parameters rather than taxonomy;
`isSubtypeOf` is minted here on a single source statement (the Composite Vector
Index sentence above) and promoted below the usual bar under the
semantic-significance exception, because the absence was structural rather than
incidental. Related: `index:index` is minted as a deliberately coarse supertype -
a placeholder, following the registry's existing `rbac-role:role` precedent -
because `index-service.md` and `indexes.md` both make statements about "an index"
with no type qualifier ("By default, an index is saved on the node on which it
is created"; "Each index is created on one keyspace (collection) only") and the
registry offered no honest subject for them. After ~93 index-related ids across
ten rounds, the corpus had no way to say anything about indexes in general.

### DCP: absent from the corpus after roughly 540 pages

`protocol:dcp` (recurrence 4, folding `server:dcp-protocol`) is arguably the most
load-bearing internal mechanism in Couchbase's architecture - the streaming
protocol by which the Data Service feeds mutations to the Index, Search and
Analytics services, and to other clusters. It appears in **none** of the first
540-odd extracted pages, and then on four of round 11's nine. The reason is
structural, not accidental: DCP is invisible to statement syntax and REST
payloads. You cannot see it from a `CREATE INDEX` reference page, because nothing
a user writes names it. It only shows up when the documentation stops describing
the interface and starts describing the machine.

Two agents minted it independently in one wave, in two namespaces, with
identical labels, each noting it recurred - the textbook cross-agent duplicate
that reconciliation exists to fold. And the immediate cause is a documentation
bug worth its own entry: `search-service.md` writes "the DCP protocol" without
ever expanding it, `analytics-service.md` writes "Database Change Protocol"
without ever abbreviating it, and neither links the other
(`server-dcp-name-drift`). Two pages in one directory, two surface forms, no
bridge - and the corpus dutifully produced two ids.

### A contradiction between two pages in the same directory

`services.md`, describing the Index Service, says it creates and maintains
indexes for the Query, **Search and Analytics** services. `indexes.md`'s table
attributes Analytics indexes to the **Analytics Service**. These cannot both be
read as true, and the disagreement is not cosmetic - it changes which service a
reader must deploy, quota and scale to index Analytics data, and it changes
whether a `servesService` edge exists at all. The extraction records both
statements and carries a CONTRADICTION WARNING on the relation rather than
picking a winner, which is the right call: this is not resolvable from the two
pages, and the answer may be version-dependent. Logged as
`server-who-creates-analytics-indexes-contradiction` with `severity:
needs-sme` - the first docs-issue in the log to be explicitly marked as
undecidable without a subject-matter expert.

It is also the strongest argument yet for the three-way duplication issue logged
alongside it (`server-services-three-way-content-duplication`): the same service
descriptions exist in `services.md`, in each service's own page, and in Capella's
feature descriptions, and they are not identical. That is *how* a contradiction
like this arises. At four content-duplication issues across the rounds
(`fts-index-management`, `fts-search-doc-overlap`, `storage-engine-split`, and
now this) it is a structural property of the doc set, not four local mistakes.

### The seventh service, and a cross-product name collision

The `service:` family held six records and looked complete. Ten rounds of
reference and management-plane extraction never needed the seventh, because
nothing a user writes and no Capella form mentions it: `service:backup-service`
is promoted here at recurrence 2. Grepping all of `cloud/` for "Backup Service"
returns exactly one hit - `cloud/clusters/cloud-snapshots.md`, "Your CSP's backup
service" - which refers to the **cloud provider's** snapshot facility and is not
a Couchbase service at all. So "which services does Couchbase have" answers six
or seven depending silently on which tree was ingested, and a reader searching
the combined documentation for "Backup Service" gets two unrelated things
undifferentiated. This is the fifth name collision the POC has documented and
the first to span products rather than sit inside one; recorded as a
do-not-confuse warning on the concept and as
`server-backup-service-name-collides-with-csp-backup-service`.

The seventh service also arrives disconnected: `backup-service.md` never states a
Data Service dependency, so it is the only one of the seven with no
`dependsOnService` edge, sitting outside the graph the other six form purely
because nobody wrote the sentence (`server-backup-service-no-data-service-dependency`).

### Multi-Dimensional Scaling, and the two disjoint views of one service set

`server:multi-dimensional-scaling` is the load-bearing concept of `services.md` -
each service independently placeable, independently quota'd, independently
scalable - and it has **no Capella counterpart anywhere in the corpus**. That
absence is the finding. Capella's ~180 management-plane pages (rounds 6-9) expose
cluster configurations, node counts and service checkboxes, with placement
decided for the user; nothing there needed `server:node`, `server:rebalance` or
`server:service-memory-quota`, all promoted here. So the ontology now holds two
disjoint views of the same seven services - `server/` sees deployable components
with topology, Capella sees a managed feature list - joined only by the shared
`service:*` ids.

The MDS predicate family is promoted as a family under the usual exception, most
members at recurrence 1: `providesService`, `requiresMemoryQuota`,
`exemptFromMemoryQuota` (the Query and Backup services are explicitly exempt),
`requiresMinimumNodeCount`, `requiresDedicatedNode`, `requiresCoDeployedService`.
Two of those carry recorded caveats. `requiresDedicatedNode` is minted on a page
that says a service "should" have a dedicated node, not "must" - the caveat is on
the record, because the predicate name is stronger than its evidence.
`servesService` carries the Analytics contradiction above.

### The registry's first datatype properties

Ten rounds produced only object properties - predicates whose objects are concept
ids. This round has 12 relations whose objects are **literals**, and two of the
promoted predicates are datatype properties by design:
`requiresMinimumNodeCount` (an integer) and
`hasInternalServiceIdentifier` (a string). The latter is a 7-member mapping from
each service to its wire identifier - `kv`, `n1ql`, `index`, `fts`, `cbas`,
`eventing`, `backup` - which is the kind of thing an ontology is unambiguously
good for and which had no home in the vocabulary until now. Worth flagging
for the JSON-LD drafting step, which has so far only ever had to emit
`@id`-valued objects.

### Predicates promoted (23)

Threshold-passing this round: `hasInternalComponent` (3 - the part-whole
predicate the registry lacked; 15 of `data-service.md`'s 30 relations are
component decomposition), `usesProtocol` (4, aliasing the duplicate
`streamsMutationsVia`), `usesExecutionModel` (2), `servesService` (2),
`requiresMinimumNodeCount` (2), `providesIndexType` (2),
`supportsLanguageConstruct` (3, earlier-round debt), `configuredPerNode` (2),
`offersConfigurationChoice` (2). Family exception (MDS): `providesService`,
`requiresMemoryQuota`, `exemptFromMemoryQuota`, `hasInternalServiceIdentifier`.
Significance exception: `requiresCoDeployedService`, `requiresDedicatedNode`,
`isSubtypeOf`, `belongsToIndexClass`, `mayDelegateOperationTo`. Earlier-round
debt at recurrence ≥3, paid down here: `createsOnAction` (4), `hasHandler` (3),
`firesCallback` (3), `cascadesDeletionTo` (3).

And one record that exists to document a distortion rather than a predicate:
`seeAlso` is filed at recurrence **425**, aliasing `rdfs:seeAlso`, purely to
record that its objects are *pages*, not concepts. This matters because it
silently poisoned this round's own aggregation - see the method notes below.

### Concepts promoted (25)

Beyond the index axes, DCP, the seventh service and the MDS family: the two
Index Service storage modes (`index:standard-storage`,
`index:memory-optimized-storage` - storage mode turns out to be a property of the
*service's configuration*, not of an index, an axis the reference tree never
named and one of them edition-gated), the full-text-search split resolved below,
`backup:full-backup` / `backup:incremental-backup` (the only two ids shared
between the self-managed Backup Service vocabulary and Capella's entirely
separate backup ontology), and `tool:cbbackupmgr`.

`tool:cbbackupmgr` folds `backup:cbbackupmgr` (3 files) and
`capella:cbbackupmgr` (1) - five files, three namespaces, one command-line
utility - following the registry's own `tool:cbq-shell` precedent, including its
reasoning that a subject-area namespace is not where a CLI tool belongs. This is
the **second** time the corpus has produced a three-namespace split for a single
command-line tool, which makes it a systematic pattern rather than an accident.

### A five-way id split for full-text search, three of them spurious

The corpus had accumulated `fts:full-text-search`, `search:full-text-index`,
`index:full-text`, `cbl:full-text-search` and
`sdk:full-text-searching-with-sdk` for what looks like one thing. Two of those
splits are legitimate and are **not** folded: `cbl:full-text-search` is a
different product (Couchbase Lite), and `sdk:full-text-searching-with-sdk` is a
page id rather than a concept. The rest was namespace drift across batches, and
it resolves into two ids that are genuinely different things:
`fts:full-text-search` the **capability** (folding `index:full-text`) and
`search:full-text-index` the **artifact** the Search Service builds. Keeping both
is deliberate - `search-service.md` makes statements about each - and the
artifact's index set is stated to be "entirely separate" from the Index Service's,
which is why no Search→Index dependency was invented despite the Index Service
page claiming to serve Search.

### Promotion debt, and what the whole-corpus query found this time

Round 10 established running the recurrence query over the entire corpus rather
than the round's own scope. Doing it again: real promotion debt stands at **350
concepts and 33 predicates** at recurrence ≥2 - "real" meaning after excluding
ids already folded into a promoted term by an `aliases` field, which the first
run of this round's script counted as unpromoted (`n1ql:cbq`, 13 files, is
already `tool:cbq-shell`). Four of the highest-recurrence offenders are paid down
here, and all four have been sitting there since rounds 6-7:
`capella:collection` (14), `capella:scope` (13), `capella:bucket` (13),
`capella:cluster-access-credentials` (13). The data hierarchy - bucket, scope,
collection - was among the most-referenced unpromoted vocabulary in the entire
corpus. It went unpromoted for five rounds for the reason round 10 identified:
recurrence 14 is not *interesting*, and nobody writes a paragraph about it.

Note `capella:bucket` is kept in its extracted namespace and **not** merged with
the `server/` bucket vocabulary that arrived in this same round
(`bucket:couchbase-bucket`, `bucket:ephemeral-bucket`), even though they are
plainly the same construct - no page states it. Flagged as a merge candidate
needing a citation. Also note `index-service.md` calls a collection a "keyspace",
so the two trees have different words for the same leaf.

### Left on the watchlist (extraction-layer only, not promoted)

- `data:vbucket` (1) - minted this round; the unit DCP streams. Certain to
  recur; not promoted on one page.
- `analytics:shadow-collection` (1) vs `capella:analytics-dataset` - the
  strongest merge candidate in the corpus, and still no source statement joining
  them. Left separate for the fourth round running.
- `eventing:event` (1) vs the promoted `monitoring:event` - a genuine
  same-word-different-thing pair, documented in both records, not merged.
- `server:cluster-manager` (1) vs `capella:cluster-manager` - the same
  namespace-duplication shape as `cbbackupmgr`, but with only one file on the
  `server/` side and no statement that the Capella role and the server component
  are related. Round 10 already logged the Capella-side naming drift
  (`cloud-projects-role-naming-drift-cluster-manager`).
- `query-service:optimizer` (1) vs the promoted `n1ql:cost-based-optimizer` -
  deliberately not merged, and probably genuinely different: the CBO is an
  Enterprise feature, while every Query Service has an optimizer of some kind
  (`server-query-optimizer-not-linked-to-cbo`).
- `index-type:gsi` / `index-type:secondary-index` are linked by `isSynonymOf`
  rather than collapsed - see the headline finding.
- `n1ql:searchfun` (3) - real debt at the threshold, and deliberately left,
  because the id is a *page filename* (`searchfun.md`), not a concept name. It
  belongs to the id-normalization backlog alongside `n1ql:createindex` and
  `n1ql:selectintro` rather than being promoted under a name no reader would
  search for. Round 10 already recorded that this id shape is a promotion smell.

### New `docs-issues/` (21)

Two marked `severity: needs-sme` - the first use of that field:

- `server-who-creates-analytics-indexes-contradiction` - `services.md` and
  `indexes.md` disagree on which service indexes Analytics data. Undecidable
  from the pages.
- `server-arbiter-vs-serviceless-node-unreconciled` - "arbiter" and
  "serviceless node" both used for a node running no data-bearing service, with
  no statement whether they are the same thing. If they are, one term should be
  retired; if not, the difference is architecturally significant.

Content gaps:

- `server-learn-services-no-access-control` - **not one mention** of RBAC,
  roles, privileges or permissions across all nine pages. The mirror image of
  the reference tree's gap (statement pages naming a privilege without linking
  its definition): here the axis is simply absent. After 552 records the corpus
  can say what every service does and nothing about who may ask it to.
- `server-learn-services-index-state-absent` - no index lifecycle anywhere in
  the conceptual pages, though the registry holds an `index-state` scheme
  promoted from the reference tree in round 8. The ontology knows about a
  lifecycle the conceptual docs never introduce.
- `server-index-class-vs-type-axes-undocumented` - the headline finding, as a
  docs bug: the page declares two classes and never says how they relate to the
  type and service axes, and its own examples refute the natural reading.
- `server-views-index-no-owning-service` - one of eight index rows has no
  providing service, is produced by an unnamed deprecated engine, and is not
  marked as legacy in the table.
- `server-backup-service-no-data-service-dependency`,
  `server-backup-service-edition-gate-unclear`,
  `server-eventing-service-page-near-empty` (6 relations against a batch mean of
  23 - genuinely thin, not gate-induced; contrast round 8's 67 pages of Capella
  eventing detail, so the depth exists just not at the entry point).

Duplication, collisions and naming:

- `server-services-three-way-content-duplication`,
  `server-backup-service-name-collides-with-csp-backup-service`,
  `server-dcp-name-drift`, `server-query-optimizer-not-linked-to-cbo`,
  `server-supervisor-capitalisation-inconsistent` (is "Supervisor" a named
  component or a common noun? extraction has to decide, and the page doesn't
  say), `server-learn-services-product-name-off-house-style` ("Couchbase
  Enterprise Server 7.6" - wrong in both word order and in embedding a version
  in prose under an 8.0 tree).

Accessibility, tooling and copy:

- `server-architecture-only-in-images` - several architectural relationships,
  including the DCP data flow and the KV engine's internal structure, exist
  **only** in PNG diagrams. Three consequences: inaccessible to screen readers,
  invisible to search, and unextractable - anything stated only in a diagram
  cannot produce a relation with quotable evidence, so the write-time gate
  correctly refuses it. Every architectural relation in this round came from a
  sentence; whatever the diagrams add beyond that is not in the ontology.
- `server-index-page-percent-encoded-underscores` - a link target whose snapshot
  filename is `7%5Fusing%5Findex.md`. A conversion artifact, but it means the
  link doesn't resolve, and it will affect every converted link containing an
  underscore - worth a sweep for `%5F` rather than a one-page fix.
- `server-index-service-anchor-title-mismatch`,
  `server-flusher-destructive-no-warning` (the Flusher is described with no note
  that flushing is destructive, though bucket flush is cautioned everywhere
  else), `server-backup-service-grammar-errors`,
  `server-data-service-stray-apostrophe`.

### What this round confirmed about the method itself

**The write-time gate fired, and its worst failure mode did not occur.** This is
the first batch written entirely under `hooks/gate-evidence.py`. Eleven gated
invocations on real records: 9 allowed, 2 denied, 3 ids flagged. Both denied
records were rewritten and both came back at **the same relation count** -
`deny(n=38) → allow(n=38)` and `deny(n=17) → allow(n=17)`. That is the specific
thing the log exists to see. The gate converts fabrication into omission: a
blocked agent can satisfy it by deleting the offending relation, leaving a clean
record and no trace, and the fingerprint of that would be a deny followed by an
allow on the same path with a *lower* count. It didn't happen here. Final corpus
evidence problems: **452, unchanged** - every one of them predates the gate.

**All three denials were false positives, and the gate is now less wrong.** The
scoreboard has to be reported honestly: 0 true positives, 3 false positives, all
on the registry-status check rather than the evidence check, and two agents hit
them independently in a single 9-page wave - so the naive substring test was
wrong about as often as it was right. The two shapes:

- *A truthful negative.* `"reused - extraction-layer id already on disk …, no
  registry file. … and none is promoted"` - accurate, and blocked for containing
  the word "promoted".
- *A statement about a different id.* `"minted - coarse placeholder, following
  the same pattern the registry already uses for the promoted rbac-role:role"` -
  accurate, unnegated, and about somebody else.

Negation-handling alone would have cleared only the first. The fix reads just the
**leading clause** of `reused_or_minted` - a record's own provenance is always
first, and commentary is where both false positives lived - plus a `minted` guard;
six regression cases pass, including round 10's real offence, which sits in the
leading clause, unnegated, about itself.

**Postscript, written immediately after this round closed: the prose parsing is
gone.** The narrowed check was a mitigation, and each fix to it was one
unpredicted sentence shape away from the next false positive - so
`registry_status` is now a **required enum** (`promoted` / `extraction-layer` /
`minted`) on every concept and every relation, checked against the registry with
aliases resolved, and the ~40 lines of clause-splitting and negation-detection are
deleted. The false-positive shapes are now structurally impossible rather than
handled. The prose note stays in the schema, because it tells a reviewer things an
enum cannot; the gate simply doesn't read it.

Three things worth recording about how that landed, because the shape generalizes
past this field:

- **It could be forward-only *because* the gate is a write-time control.** A
  corpus validator would have made 524 existing records non-conforming and forced
  a migration. A write-time gate only ever sees new records, so requiring the
  field is enforceable from the next write onward while the 552 on disk are never
  touched. The corpus stays mixed; the *entry point* is strict. The corollary is a
  discipline, not a nicety: **absent is not a value.** Anything aggregating the
  corpus must read a missing `registry_status` as *unknown*, never as
  `extraction-layer`, or an old record silently asserts something it never
  claimed - the same failure shape as a dropped relation reading as a page with
  nothing to say.
- **The enum bought two controls for free.** Because the declaration is now
  checkable in both directions, declaring `minted` for something the registry
  already promotes is refused - which is *exactly* the failure that re-created
  `requiresMinVersionFor` after it had been folded into `availableSince`, the
  oldest recurring failure in this project and until now catchable only by a
  human noticing. So is declaring `extraction-layer` for a promoted term, which
  means the registry was never checked. Neither was in the design brief; both fell
  out of replacing a substring test with a typed assertion.
- **Alias resolution is now load-bearing, and that is a new coupling worth
  flagging.** 24 ids across 14 registry files are promoted under a different name
  than extraction records use (`server:dcp-protocol` -> `protocol:dcp`, `n1ql:cbq`
  -> `tool:cbq-shell`, `streamsMutationsVia` -> `usesProtocol`). Without
  alias-awareness the enum check would deny every one of them - manufacturing the
  precise false positives it was introduced to remove. So an unrecorded fold is no
  longer just untidy documentation; it breaks the gate for correct records. The
  `linked-data-reconcile` skill now says so explicitly. 16 regression cases cover
  it, including the reverse direction (`availableSince` declared `minted` is
  denied; `requiresMinVersionFor` declared `minted` is allowed, because it is
  genuinely unpromoted debt).

The predicate half is the part to watch: it is required per-relation, matching the
existing `reused_or_minted_predicate` convention, and reported once per *distinct*
predicate so one wrong declaration doesn't produce twenty identical denial lines.
Whether per-relation repetition is the right shape, or whether predicates want a
per-record manifest instead, is a question the next wave will answer rather than
one worth pre-deciding.

**The log caught a denial before the agent reported it, which was the point.** My
own claim earlier in this round - that agents hitting the gate would surface it
to the coordinator - was wrong. Hook stderr on exit 2 goes to the *calling*
subagent; the coordinator sees only that agent's final summary, which is the
exact channel that let round 10's fabrication through as a confident report. So
the gate had a control and no instrument. `hooks/gate-log.jsonl` (gitignored,
append-only, every verdict including allows) closed that: it showed batch A's
denial about six minutes before that agent's report arrived. Allows are logged on
purpose, because an unlogged clean wave is indistinguishable from a wave where
the hook never fired at all - "9 records, 11 invocations, 2 denials" is a finding;
silence is not. The generalization: **agent self-report is a hope; a log written
by the gate itself is a control** - the same sentence round 10 wrote about
prompts and scripts, applied to observability rather than enforcement.

**A tool built to prevent a failure reproduced it.** `registry-digest.py` prints
the promoted registry fresh from disk at dispatch time, so agents can never be
handed a stale table - the failure that got `requiresMinVersionFor` re-minted
after consolidation. Its first version merged a term's files newest-wins, which
shadowed the rich `.json` records with terse `.jsonld` ones and printed
`availableSince | rdf:Property` with no shape at all: the exact stale-table
failure, inside the tool built to prevent it. A `.jsonld` file and its `.json`
sibling are not supersets of each other, so the digest now keeps all of a term's
files and takes the most informative value across them. The generalizable bit is
that the bug was invisible in the code and obvious in the output - which is also
how round 10's regex bug was caught.

**A high-recurrence predicate can silently invalidate the recurrence query.**
The first concept aggregation ranked documentation *pages* above every real
concept - `search:customize-index` at the top - because `seeAlso` occurs 425
times and its objects are pages, not concepts. Excluding them cut the candidate
list from 465 to 356 and changed what the round promoted. The promotion rule
counts object recurrence; it assumes objects are concepts; one predicate in the
vocabulary breaks that assumption at 425 occurrences. Hence the `seeAlso`
registry record, which exists mainly to document the distortion. A second
correction in the same script: ids already folded by an `aliases` field were
counted as unpromoted debt, overstating it.

**Conceptual prose is a different extraction surface, not just a different
topic.** Denser (23.4 relations per page against 13.4), and it produced the
round's structurally novel vocabulary: the first part-whole predicate
(`hasInternalComponent`), the first subsumption predicate, the first datatype
properties, and DCP. Ten rounds of reference documentation could not have yielded
any of them, because reference pages describe what a user writes and conceptual
pages describe what the machine does. Two of the eleven rounds' most-load-bearing
gaps - no subsumption vocabulary, no DCP - were invisible for as long as they were
because of *which kind of page* the corpus was made of. Worth stating as a
sampling lesson with the same standing as round 5's: coverage of a directory is
not coverage of a documentation genre.

---

## Round 12 — `server/8.0/learn` wave 2 (30 pages) - the genres disagree, and the reference genre got there first

**Scope.** 30 pages across three subtrees of `server/current/learn/`, in three
concurrent batches: `learn/data/` (9), `learn/buckets-memory-and-storage/` (8),
and `learn/security/` (13). Two hypotheses. First, continue round 11's genre
finding by extracting more conceptual prose - round 11 got its four structural
absences from nine pages, and nine pages is one data point. Second, and the
reason `learn/security/` was loaded into the batch deliberately: round 11's
largest content gap was that nothing in `learn/services-and-indexes/` touched
access control at all, while the registry's single largest family by then was
the privilege/role vocabulary built up over rounds 2, 5, 6, 7 and 10 - **entirely
from reference pages**. This batch forced that vocabulary to meet the page that
defines it.

It is also the first wave run under the required `registry_status` enum (see the
postscript to round 11), so agent handling of that field is reported here as a
first-class result rather than a footnote.

39 records, 742 relations, mean 19.0 per page - the densest wave yet, well above
round 10's 13.4 baseline, and no page in the batch is thin relative to its
length. `verify-evidence.py` over the new scope: **0 problems**.

### Headline finding: the reference genre had been quietly misfiling roles as privileges for ten rounds

`server/current/learn/security/roles.md` is Couchbase Server's authoritative RBAC
catalogue: **56 roles**, 55 of them carrying a machine-readable
`| Role: <label> (<internal_name>)` permission table and one - Full Admin -
documented in prose only.

That count is stated carefully because getting it right took three attempts, and
the near-misses are the kind a reader should be able to check. `grep -c '^### '`
returns **58**, but two of those headings ("Roles in Relation to Buckets" and
"User Categories") are prose sections rather than roles. `grep -c '^| Role:'`
returns **55**, which undercounts by one because Full Admin - the most powerful
role in the product - is the single role with no permission table. Neither
mechanical count is the answer; 58 minus the two non-role headings is. An earlier
draft of this section and of all eleven re-filed records asserted 58, which is
the same class of error the round is about: a plausible number from a mechanical
query, not checked against what the rows actually are. Reading it against the
registry showed that **eleven ids sitting in `concepts/privilege/` are roles**,
with their own sections in that catalogue:

`query-select` (recurrence 6), `query-update` (2), `query-insert` (2),
`query-delete` (1), `query-manage-index` (10), `query-system-catalog` (5),
`query-manage-system-catalog` (3), `query-use-sequences` (1),
`query-use-sequential-scans` (1), `fts-admin` (4), `fts-searcher` (1).

All eleven were minted from SQL++ statement pages and monitoring reference pages
- `Prerequisites` sections that name the bare token (`query_manage_index`)
without ever classifying it. Ten rounds of reference extraction then reinforced
the guess by repetition, until `privilege:query-manage-index` had ten files
behind it and looked like one of the best-evidenced concepts in the registry.
Recurrence measured how often the docs mention a token. It cannot measure
whether the token was filed under the right kind of thing, and here it actively
worked against the correction: the wrong answer was the well-evidenced one.

This is round 11's genre finding, sharpened into something less comfortable.
Round 11 said different genres of page yield different *vocabulary*. Round 12
says **the genres disagree, the reference genre is louder, and it gets there
first** - so a coverage plan that reads reference pages before conceptual ones
doesn't merely miss concepts, it bakes in category errors that then look
well-supported. `learn/security/` was picked for this round to fill a content
gap; what it actually did was correct the family that had the most evidence
behind it.

**Round 10 ruled on exactly this question and ruled backwards.** Its section
states that "`rbac-role:query-system-catalog` and `rbac-role:query-manage-system-catalog`
are privileges, not roles, and fold into `privilege:`", blaming the docs for the
confusion because "`metafun.md` calls `query_system_catalog` a 'role' while the
AWR and monitoring pages treat it as a privilege." `metafun.md` was right.
Round 10 moved two ids *out* of a role namespace *into* the wrong one, and filed
`docs-issues/server-query-system-catalog-called-role-and-privilege` against the
page that had it correct. Two bullets further down its own section, the same
round wrote "`role:` is the Server RBAC namespace... genuine Server RBAC role
names documented in `server/current/learn/security/roles.md`" - the right rule,
stated and then not applied, because nobody had read `roles.md`.

Three layers of error in one place, all now corrected in place with the original
text retained: the ruling, the docs-issue that blamed the correct page (verdict
inverted, `correctedIn` added), and a `note` on the surviving record citing a
"round-6 precedent" for the fold that **does not exist** - round 6's section
contains no mention of either id.

### What was done about it

Re-filed as roles, keeping the old ids as aliases, and the reason for the alias
is the interesting part:

> The misclassification is contagious through the extraction layer. An agent
> reusing `privilege:query-delete` and truthfully declaring it
> `extraction-layer` passes the write-time gate - correctly, because the claim
> about the registry is true. A promoted `role:` record that aliases the
> `privilege:` form converts that silent reuse into a gate denial. **Promotion
> here is the control point**, not a claim that one page is enough evidence.

That is a new use for promotion in this project. Five of the eleven are at
recurrence 1 and would not otherwise qualify; they are promoted anyway, under the
family exception, because the family is a misclassification that spreads and the
registry is the only place that can stop it. "An invariant in a prompt is a hope;
the same invariant in a script is a control" now extends to: **a correction in a
reconciliation log is a hope; the same correction in an aliased registry record
is a control.**

The scope of the fix was escalated beyond the three ids that prompted it,
deliberately. Every non-Capella `privilege:*` id was swept against `roles.md`,
because a half-migrated namespace is worse than either endpoint. The result is
that `concepts/privilege/` now contains **exactly Capella's 28-member catalogue
and zero non-Capella entries**, which matches the evidence: Capella is the only
place in the corpus with a genuinely separate, enumerable privilege tier.

Four files were `git rm`'d, six public-facing `pages/*.jsonld` records were
repointed from `privilege/query-manage-index` to `role/query-manage-index`, and
`relations/requires-server-role.json` was minted at recurrence 20 - the other
half of the fix, since `requiresPrivilege`'s declared range is a privilege and it
was pointing at eleven roles across 20 files. `requiresRole` was **rejected** for
reuse: its own record defines it as Sync Gateway's sync-function `requireRole()`
check, an unrelated product. `requiresPrivilege` is kept and remains correct for
its ~35 genuine Capella-privilege objects. There are now three structurally
distinct "requires a role" predicates and each record says why it is not the
other two.

### The corollary finding: Server's privilege tier has no members

Server's documentation defines a two-tier model unambiguously.
`security-overview.md`: users are associated with "specifically assigned _roles_,
these themselves corresponding to system-defined _privileges_."
`authorization-overview.md` gives both glossary definitions. And then no page
anywhere in the corpus names a single Server privilege. All 55 permission tables
in `roles.md` express permissions as **prose** - "Can list buckets." - not as
references to named privileges.

The registry now states this rather than describing it. `hasPrivilege` is
promoted at recurrence 3 with all three occurrences being the identical abstract
`rbac-model:role hasPrivilege rbac-model:privilege` glossary claim and **zero
concrete instances**, and `rbac-model:privilege` is promoted as a model-level
term explicitly separate from the `privilege:` namespace. Keeping the abstract
`rbac-model:*` layer distinct from the concrete `role:*` catalogue is what lets
the registry record that the two layers disagree instead of silently picking a
side - which is what round 10 did. See
`docs-issues/server-rbac-privilege-tier-is-abstract-only`.

### A "needs an SME" docs-issue resolved mechanically, and what that cost

`docs-issues/search-admin-fts-admin-role-overlap` has been open since round 2.
Its text said it "needs a subject-matter expert, not more extraction."
`roles.md` answered it in one line: `fts_admin` is Search Admin, `fts_searcher`
is Search Reader. Status → `resolved`, with the resolution recording that the
original judgement "was wrong in a specific and repeatable way: it needed
extraction from a different **genre** of page."

The split had also cost a real promotion. `privilege:fts-admin` (1 file) and
`privilege:search-admin` (3 files) each sat below the recurrence bar while the
single role they both name clears it at 4. A naming collision doesn't just make
the registry untidy; it suppresses recurrence and hides candidates.

### `role:admin` folded into `role:full-administrator` - the extraction layer working as designed

Three labels, one role. `roles.md`: "The Full Admin role (`admin`)".
`authorization-overview.md`: "the Full Administrator" in prose, then "Admin
(`admin`)" among Community Edition's three fixed roles. The Capella auditing page
round 5 minted the record from: "Full Administrator". The internal name `admin` is
identical across all of them and is the join key; the display labels are not.

Worth recording as a method result: the `roles.md` agent asserted
`role:admin isSynonymOf role:full-administrator` with the verbatim quote, while
the concurrently-running `authorization-overview.md` agent explicitly declined to
fold - "not folded here because this page alone gives only the coarse label, not
the roles.md cross-reference" - and left it for reconciliation. That is exactly
the designed division of labour between the two phases, unprompted.

The `isSynonymOf` relation the agent used is a **promoted predicate already** (round 2, recurrence 4, for statement pairs the docs declare functionally identical), so the reuse was correct. The reconciliation decision is about the instance, not the predicate: this triple was *consumed* by the alias fold rather than retained, because synonymy between two ids naming one role is a registry artefact to be resolved, whereas synonymy between two distinct statements is a fact about the product. The registry expresses the former through the `aliases` array and keeps `isSynonymOf` for the latter.

The fold also removed the reason `role:full-administrator` was originally
promoted below the bar. Combined recurrence is 3; it now stands on the ordinary
rule. And Full Admin turns out to be one of exactly three role sections in
`roles.md` with no permission table - prose only - so the most powerful role in
the product is the one with the least machine-readable evidence for its identity.

### The promotion metric was systematically biased, and the fix found 276 items of debt

Until this round, concept recurrence was counted from the **object slot only**.
That metric cannot see a concept a page is *about*, because those appear as
subjects. `cert:trust-store` is the subject of all four `verifiesIdentityOf`
triples and an object once: the mechanism at the centre of the certificate family
scored 1.

Counting either relation slot instead, the corpus holds **276 unpromoted concepts
at recurrence >= 2** that the old metric could not see, including
`search:customize-index` at 7. That is a larger promotion backlog than round 10's
`n1ql:query-context`-at-22 discovery, and it was invisible for the same reason:
nobody had questioned the query, only the data. `recurrence.py` now reports all
three columns - either-slot (the promotion metric), object-only (the pre-round-12
metric), and any-mention including bare `concepts[]` entries (the weakest signal,
reported but not used) - so the difference stays visible rather than being
silently corrected.

### Recurrence became a script

The skill has said since round 1 that "recurrence is a query, not hand-tracked
state," and the ad-hoc version of that query has now returned a wrong answer in
**seven** distinct ways across rounds 10-12. `poc/recurrence.py` is that query,
written once, with all seven encoded as a `--selftest` mode (17 checks, all
passing). The docstring enumerates them; the ones new this round:

- **Full-IRI versus shorthand spellings split a term's count and report promoted
  terms as debt.** `edition/enterprise` (10 files) and `index-state` (10) topped
  the unpromoted ranking while both have had registry files for rounds.
  Normalised by `canonical()`, which folds only IRIs under this project's own
  namespace - a foreign IRI is left exactly as written, because it denotes
  something this registry does not own.
- **Dot-versus-dash version spellings**, deliberately *not* normalised.
  `version:server-6.5` and `version:server-6-5` are one release but only the
  dashed form has a file, and the gate is right to reject the other. `--variants`
  reports the clusters so they get fixed in the records instead of papered over
  in the query. It found 13 clusters, including `n1ql:createfunction` against the
  promoted `n1ql:create-function`, and 21 file-mentions of dotted version ids -
  eight of them live in *public-facing* `pages/*.jsonld`, pointing at version
  concepts with **no registry file at all**. Fixed.

Every one of the seven was caught because the output looked implausible, never by
anyone reading the code. That is the argument for the script: not that it is
correct, but that its corrections accumulate instead of being re-derived.

One count was hand-checked against the script and the script won:
`privilege:query-manage-system-catalog` looked like recurrence 2 by hand and the
script said 3. The third file was real - `cloud/n1ql/n1ql-manage/query-awr.json`
and `server/8.0/n1ql/n1ql-manage/query-awr.json` are different files in different
trees. Also `server:collection` was assumed to be a candidate alongside
`server:scope` and is only recurrence 1; caught by checking rather than assuming.

### The `registry_status` enum: the verdict this wave was run to get

43 gated invocations, **31 allow / 12 deny**, 37 problems: **17 on
`registry_status`, 19 on evidence not being verbatim**, and 1 `Edit` refusal.

**All 17 enum denials are true positives. Zero false positives.** Round 11's
prose-parsing predecessor produced three false positives in nine pages, on two
shapes nobody predicted (a truthful negative, "and none is promoted"; an accurate
statement about a *different* id, "the same pattern as the promoted
`rbac-role:role`"). Replacing the English with an enum removed the class of
failure rather than narrowing it.

The dominant error is one nobody predicted either: **11 of 17 are agents tracking
promotion status correctly for concepts and forgetting that predicates need it
too** - `groupMembersInheritRole` (3), `doesNotSupport` (2), `authenticatesVia`
(2), `renamedFrom` (2), `configuredPerNode`, `requiresSetting`,
`mustUseInsteadWhen`, `restrictedToContext`. Worth fixing in the prompt template,
since it is a uniform slip rather than a judgement failure.

One denial is the exact historical failure the enum was built for: an agent
declared `availableSince` **minted** - the predicate whose re-minting after
consolidation is the origin story of the whole registry-digest control. It was
refused at write time this round instead of being found two rounds later.

One is a pleasing edge case: an agent declared `hasPrivilege` **promoted** when
the registry had no such file. Denied, correctly - the claim was false when
written. It is promoted now, this round. A gate that checks the registry as it
*is* will always do this, and that is the desired behaviour, not a rough edge.

Three caveats, stated because the scoreboard reads better than the guarantee:

1. **Only `promoted` claims are hard-checkable.** `minted` and
   `extraction-layer` both reduce to "not in the registry," so the edge between
   them is on the honour system. The enum removed the ambiguity of English, not
   the need for honesty.
2. **`n_relations` logs as `None` on exactly the worst writes** - the ones where
   parsing failed - so the thinning check is blindest where it most needs to see.
   The hook should log the field even when JSON parsing fails.
3. **The one apparent thinning signal was benign.** `security-overview` went
   `allow(6) -> deny -> allow(5)`, which is the shape the reconcile skill tells
   you to treat as the gate converting fabrication into omission. Reading the
   page showed the removed relation was genuinely not stated there. The skill's
   heuristic needs this caveat: the signal has a benign mode, and only reading
   the page distinguishes them.

### A cross-round duplicate this project predicted and then walked into

`verify-promotions.py`, run after the round's prose was written, flagged
`data:vbucket` as an id with no registry file. It is round 11's - minted at
recurrence 1 from `search-service.md` as "the unit DCP streams," with round 11's
own note recording that the term was **"certain to"** recur. It recurred in the
very next round, from a different batch, under a different namespace, as
`server:vbucket`. Folded as an alias; combined recurrence 3.

Worth reporting rather than quietly fixing, for two reasons. First, this is the
known near-duplicate failure mode - a written registry prevents re-litigating the
past, not the present - but the usual form is two *concurrent* agents colliding.
This is the sequential form, across rounds, and it is arguably worse: round 11
saw the risk clearly enough to write it down, and writing it down accomplished
nothing, because nothing connects a prediction in a reconciliation log to the id
an agent picks eleven pages later. Second, it was caught by a script rather than
by noticing - and by the one script whose output the skill says to *read* rather
than diff, from a line this round's own prose had written. Same lesson as the
role re-filing, one layer up: a prediction in prose is a hope; an alias in a
record is a control.

### Two reuses declined

Recorded because the standing rule - never merge on a shared name without
explicit textual evidence - was applied twice this round in the **refusal**
direction, which is less often reported than the merges:

- `requiresRole` for Server RBAC (it is Sync Gateway's, per its own record).
- Merging `requiresPrivilege` into the role fix (it is correct for its Capella
  objects; only the Server-role objects moved).

And the four-way parallel-namespace collision was left standing.
`capella:bucket`, `capella:scope`, `capella:xdcr` and `capella:cluster-manager`
already existed; this round promoted `server:bucket`, `server:scope`,
`server:xdcr` and `server:cluster-manager`. Round 11's note on `capella:bucket`
called the pair "a merge candidate needing a source statement, not merged." Round
12 searched the `cloud/` tree for a statement that Capella's construct *is*
Couchbase Server's and found none, so the split stands - but with a better reason
than absence of evidence: **the two records assert different things about their
subject.** Server's bucket has a type from a closed set, an ejection policy, a
storage-engine choice and a memory quota; `capella:bucket` asserts only that it
is the top level of a hierarchy. That is the difference between a construct you
configure and one you navigate, and merging them would attribute Server's
configuration surface to Capella's managed one. `server:scope` is the weakest of
the four and the likeliest to merge first. `server:keyspace` is promoted with the
mismatch noted from both sides: `index-service.md` writes "keyspace
(collection)", which is the closest the corpus comes to stating the equivalence.

### Promotions

**9 predicates**: `verifiesIdentityOf` (2), `hasDefaultValue` (3), `hasPrivilege`
(3, abstract-only - see above), `takesPrecedenceOver` (2), `scopedToKeyspace` (2),
`isAnalogousTo` (2), `requiresCapability` (2), `hasMinimumMemoryToDataRatio` (2),
`monitoredVia` (2). Plus `requiresServerRole` (20), minted as part of the role fix.

`isAnalogousTo` carries an unusually strong warning in its own type description,
because its whole purpose is to record a comparison the docs make for pedagogy -
Server's data-model pages explain collections by analogy to relational tables.
A consumer reading that as identity would conclude Couchbase has tables. Its
object, `relational:table`, is deliberately **not** promoted: a foreign-domain
term this ontology does not own, which reached recurrence 2 only as a bare
`concepts[]` mention and never in a relation slot.

`requiresCapability` overlaps in spirit with `requiresEdition` and
`doesNotSupport`; the boundary is flagged for watching rather than pre-emptively
consolidated.

**55 newly promoted concepts**, plus the **11 re-filed** from `privilege:` to `role:` - 66 concept records in all, across five families:

- **RBAC / identity** - `rbac-model:role`, `rbac-model:privilege` (the abstract
  layer, kept separate from the concrete catalogue on purpose);
  `auth-domain:local`/`external` (a closed two-member axis, the same shape as
  `edition:enterprise`/`community`); `auth-mechanism:username-password`/
  `x509-certificate`; `idp:ldap`, `idp:saml`, `idp:ldap-group`; `server:user`,
  `server:user-group`; `role:ro-admin`, `role:bucket-full-access`; the eleven
  re-filed `role:query-*`/`role:fts-*` records; `port:18091`, first member of a
  `port:` namespace that exists because the wire settings are stated per-port.
- **The four security facilities** - `security:authentication`,
  `security:authorization`, `security:auditing`, `security:encryption`. A closed
  set from `security-overview.md`'s own bullet list, which is structurally the
  table of contents for the entire subtree. `authorization` is at recurrence 1
  and promoted under the family exception rather than leaving the set visibly
  incomplete for no reason but which pages this round sampled.
- **Certificates and the wire** - `cert:trust-store`, `cert:node-certificate`,
  `cert:client-certificate`, plus `cert:root-certificate` and
  `cert:intermediate-certificate` at recurrence 1 under the family exception (a
  chain record that omits its own root documents a broken chain);
  `tls:mutual-tls`, `tls:node-to-node-encryption`, `tls:console-access-setting`;
  `encryption:native-encryption-at-rest`, with
  `encryption:encryption-at-rest-key` and `encryption:master-password` at 1,
  again as a family - a record for the feature that names neither of its secrets
  cannot answer how the data is protected. `encryption:master-password` carries an
  explicit "not a user credential" clause: it is the one password-shaped term in a
  round that promoted a large credential vocabulary which is not a login.
- **Data model** - `data:item`, `data:document`, `data:attribute` (the docs are
  precise that an item's value need not be JSON, so `item` and `document` are a
  superset/subset pair, not synonyms); `data:expiration`,
  `data:max-ttl-setting`; `server:keyspace`, `server:scope`.
- **Buckets, memory and storage** - `server:bucket`;
  `bucket:couchbase-bucket`/`ephemeral-bucket` (a closed two-member set in 8.0);
  `server:vbucket`, `vbucket:active-vbucket`/`replica-vbucket`; the five-member
  `memory:ejection-policy` enum; `storage:tombstone`,
  `compression:data-compression`; `durability:level`, `durability:durable-write`,
  `durability:level-majority`, `durability:level-persist-to-majority`;
  `server:cluster-manager`, `server:xdcr`.

Two of those sets are worth a note each.

`memory:ejection-policy` has a structure the registry cannot currently express:
the *setting* is shared across bucket types but its *value set* is not - a
Couchbase bucket chooses value-only or full ejection, an ephemeral bucket chooses
no-ejection or eject-when-full, and the two value sets are **disjoint**. There is
no predicate for "legal values conditional on another concept's value," so this
is recorded as a modelling gap rather than forced into `usesEnum`. All five
members are promoted (three at recurrence 1) because an enum published with
values missing is worse than useless: a consumer cannot tell an absent value from
an invalid one.

The durability levels are the opposite case and are **knowingly incomplete** -
two of the three recurred, the third did not, and that is stated in both records
so nobody reads the pair as the whole enum. Their sharpest fact is a cross-family
one, and the reason `requiresCapability` was promoted:
`durability:level-persist-to-majority` requires disk persistence, which
`bucket:ephemeral-bucket` does not have, so a bucket-type choice silently removes
a durability level.

**Not promoted, and why:** `1`, `1%` and `10%` all reach recurrence 2 and are
**literals, not concepts**. The extraction schema has a single `object` field
with no type distinction, so a default value of `1%` is recorded as an id
indistinguishable from `bucket:ephemeral-bucket`. They were excluded by hand.
This is `hasDefaultValue`'s and `hasMinimumMemoryToDataRatio`'s shared problem,
and an `object_type: concept|literal` field is the natural fix - on the method
watchlist. `hasMinimumMemoryToDataRatio` was kept separate from `hasDefaultValue`
rather than folded, because a minimum *requirement* and a *default* are different
claims, and conflating them would make the registry state that 1% is Magma's
default memory ratio, which is not what the page says.

`context.jsonld` gains `hasPrivilege` and `verifiesIdentityOf` - the two carrying
the round's findings - and `requiresServerRole`. It remains a deliberately
curated flagship subset (15 of 97 predicates), not a complete mapping; full
JSON-LD coverage is still the deferred step it has been at every round.

### New `docs-issues/` (18)

- `server-rbac-privilege-tier-is-abstract-only` - the corollary finding: the
  two-tier model is defined and asserted, and no privilege is ever named.
- `cloud-sqlpp-pages-cite-server-rbac-roles` - 5 of `requiresServerRole`'s 20
  files are `cloud/` pages naming Server role names; unadapted shared SQL++
  reference content, not a Capella access model.
- `server-role-label-does-not-match-internal-name` - display labels and internal
  names diverge unpredictably across the catalogue.
- `server-authorization-overview-lists-deprecated-role-as-live-ce-role` -
  `roles.md` says of Application Access "Do not grant this role to users";
  `authorization-overview.md` lists it as one of Community Edition's three fixed
  roles with no warning. A CE administrator is told both. Needs an SME: either a
  page is stale, or CE depends on a deprecated role and the blanket warning has
  an unstated exception.
- `server-account-locking-required-role-undocumented`
- `server-authentication-definitional-paragraph-triplicated`
- `server-certificates-names-java-sdk-without-xref`
- `server-encryption-sdk-links-duplicated-verbatim`
- `server-auditing-uses-eventing-generically`
- `server-buckets-page-states-closed-two-type-set-without-noting-removal` and
  `server-cli-bucket-compact-cites-removed-memcached-bucket` - the buckets page
  presents two bucket types as a plain closed set; the CLI reference still
  documents the removed third one.
- `server-relnotes-send-bucket-comparison-to-archived-docs`
- `server-buckets-memory-and-storage-index-has-no-outbound-links`
- `server-cbepctl-setting-migration-stated-piecemeal`
- `server-magma-memory-ratio-figures-duplicated`
- `server-magma-thread-settings-split-across-two-pages`
- `server-change-history-magma-exclusivity-implicit`
- `server-change-history-no-ingest-path-account`

### Existing `docs-issues/` corrected (3)

- `server-query-system-catalog-called-role-and-privilege` - **verdict inverted**,
  `correctedIn` + `correction` added, original description retained inline. The
  page it blamed was right.
- `search-admin-fts-admin-role-overlap` - **resolved** after being open since
  round 2 as "needs a subject-matter expert."
- `server-privilege-naming-two-spellings-adjacent-pages` - sharpened: both
  spellings mislabel the tier.

### What this round taught about the method

- **The genres disagree, and reading order determines which error you inherit.**
  Round 11 established that page genre predicts vocabulary. Round 12 shows the
  genres are not merely complementary: where they conflict, the reference genre
  is higher-volume and usually earlier in any sane coverage plan, so its category
  errors arrive first and then accumulate evidence. Read the authoritative
  conceptual page for a domain *before* extracting a hundred reference pages that
  mention its terms - not after, and not instead.
- **Recurrence measures how often a token appears, never whether it is filed
  under the right kind of thing.** Ten files of evidence made
  `privilege:query-manage-index` look like one of the registry's best-supported
  concepts. High recurrence on a misclassification is not reassurance; it is the
  measure of how far the error spread. This is a second coherence failure of the
  frequency bar, alongside round 10's index-axis conflation, and both were caught
  by a person looking at a list and thinking it looked wrong.
- **Question the query, not just the data.** The object-only metric had been
  wrong since round 1 and produced plausible output every time, hiding 276
  candidates. Nine rounds of scrutiny went to the extraction records and none to
  the aggregation. The corpus is now large enough that the tooling deserves the
  same suspicion the records get - which is what `--selftest` is for.
- **Promotion can be a control point, not only a conclusion.** A promoted record
  with an alias turns a category error from something the log records into
  something the gate refuses. This is the same move as
  `prefers-forward-only-schema-changes`: find the point where "from now on"
  becomes enforceable rather than aspirational.
- **A "needs an SME" verdict can be a coverage gap in disguise.** One open for
  ten rounds was answered by one line of the right page. Before escalating to a
  human expert, check whether the authoritative page for that domain has actually
  been read.
- **Resolving a naming collision can *create* a promotion.** Two sub-threshold
  ids naming one role summed to 4. Collisions suppress recurrence, so the
  dedup pass is not only hygiene - it feeds the promotion signal.
- **The gate's thinning heuristic has a benign mode.** `allow -> deny -> allow`
  with fewer relations is the documented signal for fabrication-becoming-omission,
  and this round's only instance was a correctly-dropped relation. The two are
  indistinguishable without reading the page; the skill should say so.
- **A required enum beat a prose parser outright** - 17 true positives, 0 false
  positives, against 3 false positives in 9 pages the round before. Where a
  check must read agent output, remove the English.

## Round 13 — no new pages: the corrective round round 12 made necessary

**Scope.** No extraction. This round reconciles the corpus as it already stands
(582 records, 3,522 relations) against two things round 12 exposed and did not
finish:

1. **The promotion backlog.** Round 12 found that the concept-promotion metric had
   counted only the *object* slot since round 1, so every concept a page was
   *about* - the subject of its own assertions - was invisible to it. Correcting it
   to either slot took the ≥2-file candidate list from a number that looked like a
   healthy tail to **222**. That is not a queue to be worked through in one pass,
   so this round took the coherent slice: the eight SQL++ function roles, plus
   whatever the second half surfaced.
2. **The spelling variants.** `recurrence.py --variants` reported **13 clusters**
   of one term spelled more than one way, and a separate local-name match found
   **5 more** that differ by namespace rather than by punctuation.

Both are debt this project created, not findings about Couchbase's documentation,
and the round is filed accordingly: its four new `docs-issues/` are incidental,
and its real output is two new controls and a convention written down.

### Headline finding: the registry was the source of the drift it was blaming on agents

Nine of the thirteen `concepts/version/` records declared an `id` that did not
match their own filename. `concepts/version/server-6-5.json` said its id was
`https://docs.couchbase.com/ld/concepts/version/server-6.5`, and the same
disagreement ran through `server-6-6-1`, `server-7-0`, `cbl-3-3-0`, `sdk-3-3-0`,
`sgw-2-x`, `sgw-3-0` and two `.jsonld` siblings. Dotted release numbers read so
naturally that the filing convention simply lost.

The consequence is the part worth keeping. The pipeline derives a term's id from
its **path** (`recurrence.py`'s `concept_name()`); an extraction agent copies the
id from the record's **`id` field**, because that is the authoritative-looking
string in front of it. So the tooling believed `version:server-6-5` was promoted,
agents wrote `version:server-6.5`, the write-time gate rejected it as unpromoted,
and the term landed in the backlog with nothing indicating the registry had caused
it. **A wrong record teaches every future agent to be wrong, and the agents'
correctness registers as debt.**

And it had already been diagnosed correctly, by the parties being blamed. Two
extraction agents wrote it up in their own notes - one of them: "the registry
file's `id` field uses the dot form while the filename uses hyphens ...
reconciliation must pick one" - and a prior reconciliation pass recorded the
dotted spellings as *their* mistake, to be normalised out of the extraction
records. The agents were right and were overruled. There is no amount of care in
an extraction prompt that survives an authoritative file disagreeing with itself,
which is the same argument that produced `gate-evidence.py`, so the fix is the
same shape: `verify-registry-ids.py`, which exits non-zero on any record whose
`id` does not mirror its path. It now checks **514 records, 0 mismatches**.

It overreached on its first run, flagging all 8 `pages/*.jsonld` records. Those
were correct: a `pages/` record is structured data *about* a real documentation
page, so its `@id` is that page's public `docs.couchbase.com` URL - a resource the
registry describes and does not own. `pages/` is excluded, with that reasoning in
the source, because "the id must mirror the path" turns out to be a rule about
ownership rather than about strings.

### Second finding: an alias can repair an object, but never a predicate

Round 12 fixed its category error additively - re-file the eleven roles, record
the old `privilege:` ids as `aliases` - and reported that as a control rather than
a note, because it converts a future silent reuse into a gate denial. That was
right, and it was **half a fix**, in a way that generalises.

An alias maps one id to another, so it can only ever repair a **concept**. Round
12 also minted `requiresServerRole`, the predicate those eleven objects needed,
and could not alias `requiresPrivilege` into it, because 48 files use
`requiresPrivilege` correctly for Capella's genuinely separate privilege
catalogue. Aliasing a predicate that two products use for two different things
corrupts the correct users to fix the incorrect ones. So round 12 did the half
that aliasing reaches and left the other half, and `requiresServerRole` was
minted with `recurrence: 20` while **no extraction record used it at all** - the
20 counted the files that *should* have. Every other recurrence figure in the
registry means "distinct files that use this term," so this one silently meant
something else and read as the best-evidenced new predicate of its round with
zero users.

Round 13 wrote `normalise-ids.py` to close it, and found the error was one species
deeper than round 12 had measured. 38 `requiresPrivilege` occurrences pointed at
objects that resolve to roles - the expected half. But **18 Server and Capella
records used `requiresRole`**, which is Sync Gateway's `requireRole()`
sync-function check, to mean "the user must hold this Server RBAC role." Round
12's sweep keyed on the *other* predicate name and on `privilege:*` object ids, so
those 18 had neither marker and fell between the two sieves. A predicate whose
name is more general than its meaning attracts exactly this.

After the rewrite: `requiresServerRole` is at a real **43 files, 76 occurrences**
(the record now also carries `recurrence_at_minting: 0`, so the discrepancy is on
the face of it rather than in this log), and `requiresRole` is down to 5
occurrences in 3 files - the two `sync-gateway/` records that mean the Sync
Gateway thing, and three in `transactions.json` left deliberately alone, below.

### The new control, and why it is allowed to bypass the gate

`normalise-ids.py` rewrites extraction records in place with plain Python file
I/O, so it **does not pass through `hooks/gate-evidence.py`**. That is worth
stating plainly rather than burying, since the gate is this project's central
control.

It is safe because of what the script refuses to touch. It rewrites `subject`,
`predicate`, `object` and `candidate_id`, and nothing else - never `evidence`,
`evidence_source`, `page_id` or `source_path`, so evidence quotability is
preserved *by construction*: a rename cannot make a quote stop matching a page.
It never touches `registry_status` either, because pre-round-11 records have none
and a bulk rewrite is the last place that should start guessing at one. The
compensating control is a before/after `verify-evidence.py` over the whole corpus:
**582 records, 3,522 relations, 452 problems, identical on both sides of 151
substitutions across 67 files.**

Its docstring carries the round's most reusable decision, the one that turns
`--variants` output into action:

- **Alias** when the variant is a *defensible alternative name* - a different
  namespace for the same thing, or a display label where the registry uses an
  internal name. The old id denoted the right thing; only the filing convention
  differs. Additive, forward-only, and it converts future reuse into a gate
  denial. This stays the default.
- **Rewrite the records** when the variant is *not a legitimate name for the thing
  anywhere*: `version:server-6.5` is not how this project spells a release,
  `n1ql:createfunction` is not how it spells a statement. Aliasing those would
  enshrine a typo as vocabulary and quietly bless the next one.

Variant clusters went **13 → 1**, and the survivor is not an id at all: the
literals `1` and `1%`, two files each, which is a data-modelling question about
untyped literal objects rather than a spelling one.

**Correction, made while writing this section up: that count was wrong, because
`--variants` could not see three of the clusters.** It clustered the corpus
against *itself*, so a variant is only visible when both spellings appear
somewhere in `extractions/`. A corpus that uses one spelling **uniformly**,
differing from the registry's, produces a cluster of size one and is skipped
silently - and that is the *worst* case, not the mildest, because every file using
it is denied by the gate and sits in the unpromoted backlog. Three had it:
`version:sgw-3.0` (6 files, against the promoted `version:sgw-3-0`),
`version:sgw-2.x` (2) and `version:cbl-3.3.0` (2). The same dot/dash drift as the
headline finding, in the same namespace, invisible to the very check written to
enumerate it - and found only because summarising the round's remaining backlog by
namespace put `version:sgw-3.0` on screen next to a `version:` entry that should
not have existed.

Fixed in both places rather than just the records. `--variants` now seeds the
registry in as a speller, printing registry-only forms as `0 files`, so "the
canonical spelling nobody uses" is distinguishable from a genuine two-way split;
`recurrence.py --selftest` gained a case asserting it, as bug #8. Then 15
substitutions across 9 more files, and the count is genuinely **16 → 1**.

Four more punctuation near-misses turned up in the same sweep and are *not*
defects: `n1ql:dropindex`, `n1ql:dropprimaryindex`, `n1ql:createprimaryindex` and
`n1ql:alterindex` appear only as `seeAlso` objects - link targets named after
`dropindex.md`, which are page references rather than concept mentions, and
`scan()` correctly excludes them. That distinction is round 11's `seeAlso` finding
paying off twice: the same exclusion that stopped documentation pages outranking
every real concept also keeps four filename-shaped ids out of this count.

The first pass closed only 10 of the 13, and the reason is a good illustration of
the same trap the round is about: `ID_RENAMES` was keyed on the `ns:kebab`
shorthand, while `recurrence.py` canonicalises IRI and shorthand forms together
before counting, so 11 dotted-version occurrences written as full IRIs survived
untouched and were reported as still-open clusters. The fix looks up
`R.canonical(value)` and then re-emits in whichever form the record used, because
shorthand-versus-IRI is a *separate* axis, already resolved by folding rather than
rewriting.

### The role slice (13 promotions)

**Eight SQL++ function roles**, filed under their internal names with the label
form aliased:

| id | label in the docs | `internal_name` | recurrence |
|---|---|---|---|
| `role:query-manage-global-functions` | Manage Global Functions | `query_manage_global_functions` | 2 |
| `role:query-manage-functions` | Manage Scope Functions | `query_manage_functions` | 2 |
| `role:query-manage-global-external-functions` | Manage Global External Functions | `query_manage_global_external_functions` | 2 |
| `role:query-manage-external-functions` | Manage Scope External Functions | `query_manage_external_functions` | 2 |
| `role:query-execute-global-functions` | Execute Global Functions | `query_execute_global_functions` | 1 |
| `role:query-execute-functions` | Execute Scope Functions | `query_execute_functions` | 1 |
| `role:query-execute-global-external-functions` | Execute Global External Functions | `query_execute_global_external_functions` | 1 |
| `role:query-execute-external-functions` | Execute Scope External Functions | `query_execute_external_functions` | 1 |

The four `execute-*` members are at recurrence 1 and promoted under the
family exception, documented in each record: this is a closed eight-member family
that `roles.md` presents as a single grid, and promoting the manage half while
leaving the execute half unpromoted would split a mechanism down the middle for no
reason but a counting artefact.

Also promoted: **`role:data-reader`** (recurrence 3, with `rbac-role:data-reader`
aliased), and three versions the variant split had been hiding - `version:server-5-0`
(4), `version:server-5-5` (5), `version:server-6-6` (2) - and two SQL++ statements
in the same position, `n1ql:explain-function` (7) and `n1ql:create-sequence` (3).
`n1ql:explain-function` at recurrence 7 had been split across `explainfunction`
and `explain-function` and was sitting below nothing at all; it was simply
invisible.

**The convention this slice needed, now written into the reconcile skill.** Server
RBAC role ids use the **internal name** from `roles.md`'s
`| Role: <label> (<internal_name>)` table; the display label goes in `aliases`.
Two reasons it has to be a rule and not a preference. The label is not a stable
key - 20 of the 55 role tables have a label word absent from the internal name,
and in eight of those the internal name uses a different word entirely
(`Application Access` is `bucket_full_access`), so ids minted from the two names
share no substring and `--variants` can never cluster them: it catches typography,
never synonymy. And `roles.md` itself mislabels at least one table, so the label is
sometimes just wrong where the internal name is right.

The convention deliberately does **not** go into the extract skill as a
requirement. An agent extracting a SQL++ reference page sees only the display
label; making it use the internal name means every such agent reads `roles.md`
first, a per-agent cost for a normalisation the coordinator can do once. The
extract skill now says so explicitly - mint from the name the page gives you, your
id will be re-filed with an alias - which is the two-layer split the pipeline is
built on, applied to a case that had been left to chance.

### Three notes that claimed a consolidation and never made it machine-readable

Round 12's mechanism only works if the alias is actually recorded. Three records
described a fold in their own `note` and had no `aliases` array, so the folded id's
files stayed in the unpromoted backlog and any agent reusing the old form would
have been denied by the gate for declaring something true:

| surviving record | alias it had claimed in prose | recurrence before → after |
|---|---|---|
| `concepts/cluster-access-credential-type.json` | `enum:cluster-access-credential-type` | 9 → **50** |
| `concepts/sso/realm.json` | `auth:realm` | 8 → **12** |
| `concepts/plan/free-tier-plan.json` | `billing:free-tier-plan` | 2 → **14** |

Two of the three were written in the same round, which makes this a gap in the
procedure rather than three oversights: nothing checked that a note claiming a
consolidation was backed by an `aliases` entry. `recurrence.py --variants` is that
check, and the reconcile skill now says to run it every round rather than when
something looks wrong.

### What the round declined to do

Four refusals, listed because "never merge on a shared name without explicit
textual evidence" is a rule that only means anything in the direction of refusal:

- **`n1ql:curl-function` is not `eventing:curl-function`.** Promoted separately
  (recurrence 2). Different language, different service, different authorization
  mechanism; nothing on any page states a relationship.
- **`role:data-reader` is not `capella-role:data-reader`.** Different control
  plane, different grant scope, different catalogue. The name is the only thing
  they share.
- **`role:administrator` and `rbac-role:data-admin` name nothing in the 56-role
  catalogue.** Both were checked against `roles.md` directly rather than by
  impression - the same discipline round 10 used to refuse a merge - and both
  became `docs-issues/` rather than concepts. A promotion would have minted
  vocabulary for a documentation error.
- **Three `rbac-role-category:*` assertions in `transactions.json` keep the wrong
  predicate,** because neither predicate's range admits a role *category*, and
  minting `requiresServerRoleInCategory` for 3 occurrences in 1 file would be
  minting vocabulary to avoid recording an open question. It is recorded as an open
  question instead.

### A green check on a wrong record, again - and this one is the cleanest example yet

`role:query-use-sequences` was promoted in round 12 with the label "Manage
Sequences". `roles.md`'s table for it is headed
`| Role: Manage Sequences (query_use_sequences)` - the label and the internal name
disagree, and the internal name is the correct one, because the role's own
permission table grants `execute` on sequences and not `manage`. The label in the
source is wrong.

So the record's `evidence` field quotes, verbatim, a line that is itself false.
Every control passed it: the gate confirmed the quote was on the page,
`verify-evidence.py` confirmed the same, `verify-promotions.py` confirmed the id
resolved to a file. **"A green check is not a green record"** has been in this log
since round 10 as a caveat about mis-objected triples; this is the sharper form -
correct extraction of an incorrect source. The label is now
`"Use Sequences (Server RBAC role)"` with
`mislabelled_in_source_as: "Manage Sequences"`, and the `evidence` field still
quotes the wrong line, because that is what the page says and the record's job is
to report the page.

### New `docs-issues/` (4)

- `roles-md-use-sequences-table-mislabelled` - the above.
- `roles-md-external-function-role-tables-copy-pasted` - the four external-function
  role tables carry permission rows that appear copied from their non-external
  siblings.
- `searchfun-cites-nonexistent-data-admin-role` - a SQL++ page requires "Data
  Admin"; no such role exists in the catalogue.
- `n1ql-pages-cite-nonexistent-administrator-role` - several pages require an
  "Administrator" role; the catalogue has Full Admin, Cluster Admin and several
  scoped admins, and no "Administrator".

### Existing `docs-issues/` corrected (1)

- `server-role-label-does-not-match-internal-name` - rewritten with measured data.
  It claimed 2 instances; there are **20 of 55**, with 8 where the two names share
  no word. It also inherited round 12's "58 role tables", which is the heading
  count, not the table count (55 tables, 56 roles, one documented in prose only) -
  corrected in place. And its diagnosis of the Manage/Use Sequences case was
  backwards: it read the internal name as the drifted one.

### What this round taught about the method

- **A control's own output is data about the control.** `--variants` had been run
  before and read as a list of agent spelling mistakes. Read as a question - *why
  would an agent write this?* - nine of thirteen clusters turn out to be the
  registry's fault. The output was the same both times; the framing decided
  whether it was actionable.
- **The loud half of a debt problem hides the quiet half.** A promoted term
  reading as unpromoted is loud - it shows up as a big number. A genuine candidate
  held *below* the promotion bar because its count is split across two spellings
  shows up as nothing at all. Five terms had silently suffered it, including one at
  recurrence 7. Both halves come from the same variant, and only one of them
  announces itself.
- **Additive-and-forward-only has a reach, and it is worth knowing where it
  ends.** Aliasing is the right default and round 12 was right to use it. But an
  alias is a statement about an *id*, so a wrong predicate is outside its reach
  entirely, and a round that resolves everything by aliasing will leave exactly the
  predicate half undone - silently, and with a plausible recurrence figure on the
  new record. When a correction has a concept half and a predicate half, they need
  two different mechanisms.
- **A recurrence figure needs to say which question it answers.** `recurrence: 20`
  on a predicate with zero users was not a lie, it was a different measurement -
  files that *should* use the term - recorded in a field that everywhere else means
  files that *do*. The registry now has 100-odd records whose `recurrence` was
  true when written and is not recomputed; that ambiguity is flagged here rather
  than settled, because a mass update would be guessing at the intent of records
  from eleven rounds.
- **Blame direction is worth checking before writing a correction down.** The dot/
  dash drift was recorded as an agent error and normalised out of the records, when
  the records were right and the registry was wrong. A reconciliation pass sits
  above the agents and its verdicts are not reviewed by anything, which makes "the
  agents got this wrong" the cheapest available conclusion and the one to be most
  suspicious of.

### Where the backlog stands

222 → **206** candidates at ≥2 files, and the shape has changed more than the
number: the highest remaining is **recurrence 8** (`eventing:eventing-storage`),
so the double-digit debt round 12 uncovered is fully cleared. What is left is a
long tail that wants a namespace-by-namespace coherence pass rather than more
promotion - `vector-index:` has two members at 6 and no promoted parent,
`backup:` has two at 5, and round 11's index-taxonomy question is the precedent
for what happens if a family gets promoted before its axes are understood. 18
predicates also sit at ≥2, headed by `requiresMinVersionFor` at 5, which was
consolidated into `availableSince` in round 2 and re-minted by a later round -
that one is a fold, not a promotion.

Roughly 15 `sgw:` and `cbl:` candidates in the tail are not promotable at all
until round 3's two trees are re-extracted, since their records are 45%-50%
verbatim. That remains the tracked next step it has been since round 10.

## Cumulative verdict (all thirteen rounds)

The vocabulary has now been tested against eleven genuinely different kinds of
"does this still fit": a different component within one product (round 1), a
different deployment model of the same underlying product (round 2), three
entirely different products built by different teams (round 3), a single
product's own feature that cuts across its existing per-operation model
(round 4's transactions, within the Java SDK already covered in round 3), full
coverage of a directory a prior round had only sampled a fifth of (round 5),
the same partial-sampling lesson recurring on the same product's role catalog
(round 6), that exact lesson recurring a third time on the privilege catalog
(round 7), the cleanest negative result so far - a brand-new, complex feature
(Eventing) needing no new structural layer at all (round 8) - a round expected
to mostly confirm rather than surprise, which is exactly what it did while
still closing a question open since round 5 (round 9, finishing `cloud/`) -
the first wave into a **second product tree**, where the same feature
set is documented twice, by different editorial processes, at different
versions (round 10) - and now a different **genre** of page within a tree
already partly covered: architectural prose rather than reference syntax
(round 11) - and finally the same genre again at three times the scale, aimed
deliberately at the one domain where a decade of reference extraction had built
the registry's largest family, to see whether the conceptual pages would confirm
it or contradict it (round 12: they contradicted it). At every step it kept
doing the same useful thing: not
just "the terms still fit," but surfacing something true and specific about
each surface it touched - Capella's credential/role-based access model
(round 2), Sync Gateway's two-disjoint-systems architecture and inverted
channel-based access model (round 3), Couchbase Lite's own disjoint edition
split (round 3), the Java SDK's transaction layer inverting CAS-based
concurrency into transaction-membership checks (round 4), round 2's "simple
credential-type pair" turning out to be a whole per-statement privilege catalog
(round 5), `capella-role:*` turning out to be two catalogs silently flattened
together since round 2 (round 6), `cluster-rbac.md`'s own 25-privilege table
more than doubling what round 5 had already corrected (round 7), Eventing
confirming that "genuinely new feature" doesn't automatically mean "genuinely
new access-control shape" (round 8), the SQL++-vs-SDK transaction boundary
finally stated explicitly by a page's own text rather than left inferred
(round 9), and version-evidence density turning out to be *inversely*
correlated with how new a feature is - the newest statements in Couchbase
Server 8.0 are the ones no page dates (round 10), and the index taxonomy having
two axes that genuinely cross rather than nest, plus DCP - the protocol the whole
architecture rests on - being absent from the first 540 pages because reference
documentation cannot see it (round 11), and Couchbase Server documenting a
two-tier role-and-privilege access model whose privilege tier has no enumerable
members anywhere in 570 pages, which had caused eleven role names to be filed as
privileges and left there for ten rounds (round 12). That's a stronger and more
useful result than a vocabulary that merely never breaks.

Round 12 adds a harder version of the same point. Eleven rounds found things the
vocabulary had not yet *covered*; round 12 found something it had covered
**wrongly**, in its single largest family, with ten files of evidence behind the
error. Every prior round's surprise was an absence, which a coverage plan can in
principle chase. This one was a confident presence, and no amount of additional
reference coverage would have corrected it - more reference pages were precisely
what made it look well-supported. The check that caught it was reading the one
page that defines the domain.

Round 13 is the first round that read no new pages, and it belongs in this verdict
for a different reason from the twelve before it: it is the first time the corpus
was audited against **itself** rather than against a new surface, and the largest
single defect it found was in the registry. Nine `concepts/version/` records
declared an `id` that contradicted their own filename, so the tooling and the
extraction agents disagreed about what was promoted, agents were denied for being
correct, and a prior reconciliation pass had recorded the whole thing as *their*
error. Twelve rounds of scrutiny went outward, at the documentation and then at the
records and then at the queries. This one went at the authored registry that all
three depend on, and it should not have taken thirteen rounds to look there.

Round 10 also changed what this project believes about its own reliability. Up
to round 9, the evidence quality of the corpus was assumed on the strength of
the extraction schema requiring direct quotes. It isn't: 322 of 2,780
relations quote text that does not appear on the page they cite, 130 more
carry no evidence at all, and two whole product trees from round 3
(`sync-gateway` at 45% verbatim, `couchbase-lite` at 50%) are unreliable
enough to need re-extraction rather than repair. The conclusions those rounds
drew about *vocabulary* still stand - they were reached by reading, and the
reading was sound. The records they left behind are not sound sources of fact.
Distinguishing those two things is now a permanent part of how this corpus
should be read.

The cost of getting the useful result cleanly has been a steady retreat from
page-by-page manual reconciliation toward aggregate statistics and explicit,
documented judgment calls - a real trade-off, and the right one at this scale.
Round 12 found the sharp edge of that trade-off: aggregate statistics are
themselves code, and nine rounds of scrutiny went to the extraction records while
none went to the query aggregating them. The object-only concept metric had been
wrong since round 1, produced plausible output every time, and was hiding 276
promotion candidates. Round 13 completes that thought from the other side: the
aggregates were also being fed a registry that disagreed with itself, so the query
and its input had both gone unaudited while the records were audited twice.
Fourteen limits of the method are now visible across multiple rounds, not just
once, so worth treating as durable rather than one-off:

- **An invariant in a prompt is a hope; the same invariant in a script is a
  control.** Every brief for nine rounds required evidence to be a direct
  quote. Agents cited the rule approvingly and broke it 452 times. Nothing
  checked. The failure was not agent quality - most of the breakage is ordinary
  paraphrase drift, not hallucination - but the absence of any mechanical gate
  between "the record was written" and "the record was accepted." This
  generalizes past evidence: every schema rule this project relies on
  (subject must be a concept id, predicates go in `relations` not `concepts`,
  ids are kebab-case) is currently enforced by hope. Round 11 extends the same
  sentence to *observability*: **agent self-report is a hope; a log written by
  the gate itself is a control.** Hook stderr on exit 2 reaches the calling
  subagent, not the coordinator, so a gate's own verdicts were only visible
  through the identical self-report channel that let round 10's fabrication
  through. `hooks/gate-log.jsonl` records every verdict including allows,
  because an unlogged clean wave is indistinguishable from a wave where the
  hook never fired.
- **Extracting a directory is not extracting a genre.** Round 5's lesson was
  that a fifth of a directory doesn't generalize to the directory. Round 11's is
  a level up: ten rounds of *reference* pages - statement syntax, REST payloads,
  management forms - left the registry with no part-whole predicate, no
  subsumption vocabulary at all across 195 concepts, no datatype properties, and
  no DCP, the protocol the entire architecture rests on. None of those absences
  were caused by insufficient coverage; nine hundred more reference pages would
  not have surfaced any of them, because reference documentation describes what a
  user writes and conceptual documentation describes what the machine does. Nine
  pages of the second kind produced all four. A coverage plan measured in pages
  or directories will miss this; the axis that mattered was which kind of page.

  Round 12 extends this from *incompleteness* to *incorrectness*, which is worse.
  The genres do not merely cover different ground - where they overlap, they
  disagree, and the reference genre is both higher-volume and earlier in any sane
  coverage plan. So its category errors arrive first and then accumulate evidence
  by repetition: eleven Server RBAC role names were filed under `privilege:`
  because SQL++ `Prerequisites` sections name the bare token without classifying
  it, and ten rounds of reference extraction reinforced the guess until
  `privilege:query-manage-index` had ten files behind it. The corrective is an
  ordering rule, not more coverage: **read the authoritative conceptual page for a
  domain before extracting the reference pages that mention its terms.**

- **Recurrence measures how often a token appears, never whether it is filed
  under the right kind of thing.** High recurrence on a misclassification is not
  reassurance - it is the measure of how far the error spread. Round 12's wrong
  answer was the well-evidenced one, and the frequency bar not only failed to
  flag it but actively argued for it. Together with round 10's index-axis
  conflation this is now twice that the bar has been silent on a coherence
  failure, both caught by a person looking at a list and thinking it looked
  wrong. Also worth noting the inverse: a naming collision *suppresses*
  recurrence. `privilege:fts-admin` (1 file) and `privilege:search-admin` (3)
  name one role that clears the bar at 4, so deduplication is not just hygiene -
  it feeds the promotion signal, and leaving collisions in place hides
  candidates.

- **The tooling deserves the suspicion the records get.** Every aggregate this
  project reasons from is a script, and scripts have been wrong in seven distinct
  ways across rounds 10-12 - a regex that stripped one file extension, a
  newest-wins merge in the anti-staleness tool itself, IRI-versus-shorthand
  spellings splitting counts and reporting promoted terms as debt, and a
  promotion metric that could not see any concept a page was *about*. All seven
  were caught because the output looked implausible; none by anyone reading the
  code. That is not a workable control at this corpus size, which is why
  `recurrence.py` encodes all seven as a `--selftest` mode: the point is not that
  the query is correct, but that its corrections accumulate instead of being
  re-derived from memory each round.

  Round 13 supplies an eighth **and a ninth**, and the ninth is in the variant
  reporter itself: it clustered the corpus against itself, so a spelling the corpus
  used *uniformly* while the registry used another produced a cluster of size one
  and was skipped in silence. The check written to enumerate the round's central
  defect could not see three instances of it, including one at 6 files. This is the
  sharpest form of the general point, because it is not a wrong answer - it is a
  question the query cannot ask. `--variants` now seeds the registry in as a
  speller and `--selftest` asserts it.

  The eighth repeats bug #5 in a new script rather than
  in a new form: `normalise-ids.py`'s rename table was keyed on the `ns:kebab`
  shorthand while `recurrence.py` canonicalises shorthand and IRI together before
  counting, so its first pass silently missed 11 dotted-version occurrences written
  as full IRIs and closed only 10 of 13 clusters. `--selftest` covers the same
  mistake in `recurrence.py` and could not carry the lesson across a file boundary.
  A self-test protects the function it tests, not the invariant it was written
  about, which is an argument for putting the canonicalisation in one place and
  importing it - as this script does for the registry, and did not for the keys.

- **Promotion can be a control point, not only a conclusion.** Round 12's
  correction had a contagion problem: an agent reusing `privilege:query-delete`
  and truthfully declaring it `extraction-layer` passes the write-time gate,
  because the claim about the registry is true. Promoting the correct `role:`
  record *with the wrong id as an alias* converts that silent reuse into a gate
  denial. A correction in a reconciliation log is a hope; the same correction in
  an aliased registry record is a control. Five ids below the recurrence bar were
  promoted on this reasoning alone, which is a genuinely new use of promotion in
  this project and is documented as such in each record rather than passed off as
  ordinary.

  Round 13 marks the boundary of the mechanism, which matters as much as the
  mechanism. **An alias is a statement about an id, so it can repair a wrong
  concept and never a wrong predicate.** `requiresPrivilege` could not be aliased
  into `requiresServerRole` because 48 files use it correctly for a different
  product's genuinely separate catalogue - aliasing a predicate that two products
  use for two things corrupts the correct users to fix the incorrect ones. So round
  12 did the concept half, left the predicate half, and minted the new predicate
  with `recurrence: 20` against the zero records that used it, the 20 counting
  files that *should* have. Nothing about that record looked unfinished. When a
  correction has a concept half and a predicate half, they need two mechanisms, and
  the round that only has one will leave the other half silently and plausibly
  undone.

- **A recurrence figure has to say which question it answers.** Everywhere in the
  registry `recurrence` means "distinct files that use this term", except on one
  round-12 record where it meant "files that should", and nothing distinguished
  them. More generally the field is true when written and never recomputed, so
  across 100-odd records it is a mixture of current counts and historical ones.
  Round 13 added `recurrence_at_minting` to the one record it could establish it
  for and flagged the rest rather than mass-updating, because a bulk rewrite would
  be guessing at the intent of records from eleven rounds - but the ambiguity is
  real and any consumer reading these as live counts will be wrong somewhere.

- **A "needs a subject-matter expert" verdict can be a coverage gap in
  disguise.** `search-admin-fts-admin-role-overlap` sat open from round 2 to
  round 12 carrying the note that it "needs a subject-matter expert, not more
  extraction." One line of `roles.md` answered it. Before escalating to a human
  expert, check whether the authoritative page for that domain has been read at
  all - the judgement was not wrong about needing something more, only about
  what.
- **Priming a wave has a measurable cost.** Name a predicate as the wave's
  priority and agents will find instances of it, including where none exist.
  The one fabricated triple in round 10's 509 was an `availableSince`, on a
  page batch C had been told was "prime `availableSince` territory" and which
  contains no version statement at all. Mitigation is not a milder instruction
  but explicitly equal standing for negative results - "this page says nothing
  about versions" has to be a reportable finding, or the incentive runs one way.
- **Verification of quotability is a floor, not a ceiling.** Round 10 produced
  three relations that quote real sentences and attach them to objects the
  sentence does not support. A green evidence check means the sentence exists;
  it says nothing about whether the triple is a fair reading of it. That
  remains a judgement task.
- **The recurrence bar answers "is this term real?" and nothing else.** It
  cannot see that a namespace's members answer four different questions, which
  is why 93 index concepts - several of them well past the bar - were held back
  in round 10 rather than promoted into a permanent axis conflation. A promotion
  rule based on frequency needs a coherence check beside it.
- **Structural silence isn't a naming problem.** The method is good at catching
  "these two labels are probably the same thing" (round 1's link-target
  mismatch, round 2's `search-admin`/`fts-admin` overlap). It has nothing to say
  about "this page is silent on something comparable pages all state" beyond
  flagging the silence - that distinction needs a human, every time.
- **A written registry prevents re-litigating the past, not the present.** Every
  round has produced at least one case of two agents (or one agent revisiting
  old ground) independently minting near-duplicate vocabulary for something new,
  because a static list of already-promoted terms says nothing about what a
  concurrently-running sibling batch is minting right now. Round 10's clearest
  instance: `api:query-rest-api` and `n1ql:query-service-rest-api`, six files
  each, disjoint, same endpoint, same wave. This hasn't gotten worse as the
  vocabulary has grown - if anything the promoted core has stayed remarkably
  stable - but it hasn't gone away either, and a production pipeline would need
  either a live, queryable registry or a mandatory dedup pass, not a bigger
  written briefing.
- **Reconciliation itself can leave gaps, not just extraction - and they
  compound.** Round 3's Java SDK batch was reconciled only narratively and
  promoted nothing, invisible until round 4 tried to reuse those concepts.
  Round 10 found the same debt at scale: `n1ql:query-context` at recurrence 22,
  `n1ql:create-index` at 20, the whole SQL++ statement vocabulary the `cloud/`
  rounds had been reusing since round 2 - none of it promoted, because none of
  it was *interesting* enough to write a paragraph about. Recurrence 22 is not
  interesting; it is load-bearing. The recurrence query is cheap and should be
  run over the whole corpus every round, not just the round's own records.
- **Partial coverage of a large, uniform-looking directory doesn't generalize
  the way it feels like it should.** Round 2 read 23 of `cloud/n1ql/`'s 138
  pages and reasonably concluded the credential-type model was a flat pair.
  Round 5 read the other 115 and found a whole per-statement privilege catalog
  with two-axis and AND-combination structure the smaller sample never
  surfaced. Round 10 caught the same shape prospectively for once: the proposal
  to rename `monitoring:` to `capella-alerting:` was made when all 13 known
  members were Capella pages, and the first Server page to touch monitoring
  refuted it.
- **Vocabulary built from a feature's mentions elsewhere is less reliable than
  vocabulary built from the feature's own authoritative page.** Both
  `capella-role:*` (round 6) and the Advanced-credential privilege catalog
  (round 5) were minted from statement pages' Prerequisites sections -
  paraphrases of the real thing - and both turned out incomplete or mislabeled
  once the authoritative page was read directly. Round 10 applied this
  prospectively too, deferring the index taxonomy until
  `learn/services-and-indexes/` is read.
- **Knowing about a failure mode doesn't prevent it.** The "narrated as
  promoted, never actually filed" gap recurred three times (round 2's
  `gatedByBillingPlan`, round 3's Java SDK concepts, round 5's `monitoring:*`
  family) - the third introduced by this same reconciler after writing up the
  first two as a known risk. Round 10 adds a second instance of the same
  species: a bug in this round's own recurrence script (a regex stripping
  `.jsonld` but not `.json`) made every promoted predicate look unpromoted, and
  was caught only because the output was implausible. Vigilance is not a
  control. Round 10 named two candidate controls and wrote one:
  `poc/verify-promotions.py` checks that every concept and predicate named in a
  round's `reconciliation.md` section resolves to a real file. It found five
  terms this round's own prose leaned on and had not filed - and then found three
  more when re-run after the prose was finished, which is a stronger argument for
  it than the first five were.

  The second is still unwritten: **nothing validates the extraction schema
  structurally.** Nothing checks that a subject slot holds a concept id rather
  than a page id, which is how round 8's `cascadesDeletionTo` violation survived
  its own reconciliation, and it is the obvious next thing to add to
  `hooks/gate-evidence.py` - the hook already parses every record at write time,
  so the structural check costs nothing extra to run and would have caught round
  8's violation at the moment it was introduced rather than two rounds later.

  Round 11 adds a third instance of the species, and it is the sharpest yet
  because the tool was purpose-built against the failure it committed:
  `registry-digest.py` exists so that agents are never handed a stale registry
  table - the failure that got `requiresMinVersionFor` re-minted after
  consolidation - and its first version merged each term's files newest-wins,
  printing `availableSince | rdf:Property` with the predicate's shape dropped
  entirely. A stale table, generated fresh, by the anti-staleness tool. Both it
  and round 10's regex bug were invisible in the code and obvious in the output,
  which is the only reliable check either had.

  Round 12 adds a fourth instance, and the most consequential: the promotion
  metric itself. See "the tooling deserves the suspicion the records get" above.
  Unlike the other three this one was not a bug introduced in a round's own
  throwaway script - it was the definition of the concept-promotion signal, wrong
  since round 1, agreeing with itself every time it ran.

  Round 13 adds a fifth instance, in the registry rather than in a script: nine
  `concepts/version/` records whose declared `id` contradicted their own filename,
  which is the same species again - the reconcile skill had required ids to mirror
  paths since round 1 and nothing checked, so the rule held for as long as care
  held. Two extraction agents diagnosed it correctly and were overruled. Five
  instances now, four of them committed by the reconciler that had already written
  the previous one up as a known risk, is enough to stop calling it a pattern and
  call it the default: **an unchecked invariant decays, and the decay shows up as
  someone else's mistake.**

  Eight controls now exist where nine rounds had none: the write-time gate
  (`hooks/gate-evidence.py`), its verdict log (`hooks/gate-log.jsonl`), the
  dispatch-time registry digest (`registry-digest.py`), the corpus audit
  (`verify-evidence.py`), the promotion report (`verify-promotions.py`), the
  self-testing recurrence query (`recurrence.py --selftest`, 18 checks), the
  registry path/id check (`verify-registry-ids.py`, 514 records), and the id
  normaliser (`normalise-ids.py`) - which is the odd one out, being the only one
  that *writes*, and the only one that bypasses the gate. It is allowed to because
  it touches `subject`, `predicate`, `object` and `candidate_id` and nothing else,
  so it cannot make a quote stop matching a page; the compensating control is a
  before/after `verify-evidence.py` over the whole corpus, byte-identical across
  151 substitutions in 67 files.
  Round 11 is the first batch written entirely under the gate, and reports a
  mixed result honestly. What worked: 11 gated invocations, 2 denials, both
  rewritten records returning at the *same* relation count, so the gate's own
  worst failure mode - converting fabrication into silent omission - demonstrably
  did not occur, and corpus evidence problems stayed at 452, all of them
  pre-gate. What didn't: **all three flagged ids were false positives**, none on
  the evidence check, all on the registry-status check parsing English prose, and
  two agents hit them independently in nine pages. That has since been fixed at
  the root rather than narrowed: `registry_status` is now a required enum, checked
  against the registry with aliases resolved, and the gate no longer parses
  English at all - see the postscript to round 11. And a scoreboard of 0 true
  positives cannot distinguish "the gate
  deterred fabrication" from "no fabrication was attempted"; one clean wave is not
  evidence either way.

  Round 12 settles that question, because it is the first wave run under the enum
  and it is three times the size: 43 gated invocations, 31 allow / 12 deny, 37
  problems - **17 on `registry_status`, all 17 true positives, zero false
  positives**, against the prose parser's 3 false positives in 9 pages. Removing
  the English removed the class of failure rather than narrowing it, and that is
  the generalizable lesson: where a check must read agent output, give it an enum,
  not a sentence. One denial refused an agent declaring `availableSince`
  **minted** - the precise historical failure the registry-digest control exists
  because of - at write time, rather than two rounds later. The dominant error was
  one nobody predicted: 11 of 17 are agents tracking promotion status correctly
  for concepts and forgetting predicates need it too, a uniform slip that belongs
  in the prompt template rather than in an agent-quality argument.

  Three limits stand, and they are the ones to quote when someone reads that
  scoreboard as a guarantee. **Only `promoted` is hard-checkable** - `minted` and
  `extraction-layer` both reduce to "not in the registry," so that edge remains on
  the honour system. **`n_relations` logs as `None` on exactly the writes where
  parsing failed**, so the thinning check is blindest where it most needs to see.
  And **the thinning heuristic has a benign mode**: round 12's one
  `allow -> deny -> allow`-with-fewer-relations sequence, which the reconcile
  skill says to treat as fabrication becoming omission, turned out to be a
  correctly-dropped relation. Only reading the page distinguishes the two, and the
  skill should say so.

  Worth stating plainly what six scripts do and don't buy, because a shelf of
  them invites more confidence than it earns: they all check *form*, none checks
  *reading*. Quotable-but-mis-objected records pass every one. The axis
  conflation that kept 93 index concepts unpromoted was found by a person looking
  at a list and thinking it looked wrong - and its resolution in round 11 (two
  crossing axes, not a hierarchy) came from reading one page's own examples
  closely enough to notice they refuted the obvious model. No script proposed
  here would have found either.

  Round 12 is the strongest case for that caveat so far, and the one to reach for
  if the shelf starts looking like a guarantee. Every control passed on the eleven
  misfiled roles. The gate allowed each record, because each agent's
  `registry_status` declaration was *true* - `privilege:query-manage-index` really
  was in the registry. `verify-evidence.py` passed, because the quotes really were
  on the pages. `verify-promotions.py` passed, because the ids really did resolve
  to files. `recurrence.py` ranked the error at the top of the corpus, correctly
  counting a token it has no way to classify. Six green checks over a
  ten-file-deep category error, and the thing that caught it was reading one page
  and noticing that the registry disagreed with it. The scripts are worth having
  precisely because they free up the attention that reading requires; they are not
  a substitute for it, and after thirteen rounds there is no sign they are becoming
  one.

  Round 13 adds the case where the checks were green because they were checking the
  wrong file. `role:query-use-sequences` carries evidence quoting, verbatim, a table
  heading in `roles.md` that is itself wrong - the label says "Manage Sequences",
  the internal name says `query_use_sequences`, and the role's own permission table
  grants `execute`. The gate confirmed the quote was on the page.
  `verify-evidence.py` confirmed it again. `verify-promotions.py` confirmed the id
  resolved. All three were right, and the record was wrong, because correct
  extraction of an incorrect source is indistinguishable from correct extraction.
  Nothing on this shelf can reach that, and nothing that could be added to it
  would - the only check is a second source, or a person who knows the product.
