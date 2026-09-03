# Pass-2 reconciliation log

Fifteen rounds so far, in order run. Each section covers one round; a single
cumulative verdict sits at the end. Rounds 13-15 read no new pages: they audit the
corpus and the registry against themselves.

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
(`fts-index-management-content-duplication`, `fts-search-doc-overlap`,
`server-storage-engine-split-duplicated-across-components`, and now this) it is a structural property of the doc set, not four local mistakes.

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
  something the gate refuses. It is the schema-change discipline of preferring an
  additive, forward-only change over a migration: find the point where "from now
  on" becomes enforceable rather than aspirational.
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

## Round 14 — the namespace coherence pass, wave 1 (`vector-index:` and `version:`)

No new pages. Round 13 left a 206-item backlog and an explicit instruction about
how to work it: **one namespace at a time, deciding the namespace's internal
structure before promoting any member**, rather than in rank order. Round 10 is
the precedent — it refused all 93 index concepts because they were individually
correct and collectively incoherent — and round 11 then found that the axes
*cross* rather than nest. The recurrence bar answers "is this term real?" and is
structurally silent on "do this namespace's members answer the same question?"

This wave took the two namespaces where that second question had the sharpest
answer. It promoted 18 terms, retired 30 ids, and found a defect in the promotion
metric itself that had been inflating the backlog by 13%.

### Headline finding: the metric let page ids back in through the subject door

`search:customize-index` has 24 relations. Every one is a `seeAlso`. Its label is
"Customize a Search Index with the Web Console", which is a page title. It sat in
the round-13 backlog at recurrence 2, and it should never have been a concept.

Round 11 established that `seeAlso` objects are pages, not concepts — at
recurrence 425 they outranked every real concept — and excluded them. Round 12
then found the opposite problem, that counting objects only hides every concept a
page is *about*, and broadened the promotion metric from the object slot to
**either** slot. That broadening silently undid round 11's exclusion, because the
exclusion was written into the object branch of the counting loop and the new
subject branch had no equivalent. Every page id re-entered the metric as a link
*source*. Two rounds of promotions ran on the widened metric.

Of the 203 backlog items, **27 fall below the bar** once `seeAlso` is excluded
from both slots, and **9 have no non-`seeAlso` relation whatsoever**. The backlog
was 176, not 203. The ghosts cluster where you would expect — `search:` 7,
`n1ql:` 7 — in the two namespaces whose candidates most look like filenames.

Two things worth separating, because conflating them is the next mistake:

- **Dropping out of the promotion queue is not a verdict that the id denotes a
  page.** `index-type:covering-index` is `seeAlso`-only and is a perfectly real
  concept: "Covering indexes are applicable to secondary index scans and can be
  used with global secondary indexes (GSI)". Its relations are all mis-typed —
  born as Markdown links and recorded as `seeAlso` — so it is correctly below the
  bar for want of non-link evidence and correctly still a concept. It was one
  edit away from being promoted as a sixth index type in this very round; the
  measurement caught it, not the reading.
- **The label settles it, not the predicate.** A page id labels itself with a page
  title ("Use Vector Indexes for AI Applications (overview)"); a concept labels
  itself with a noun phrase ("Covering Index / Covered Query"). `seeAlso`-only is
  a smell that requires a look.

Only 18 of the 27 ghosts are page-shaped; the other 9 are genuine concepts now
correctly at recurrence 1, i.e. watchlist material rather than debt.

### `vector-index:` — a namespace named like an axis and populated like a subject area

The registry uses two kinds of namespace and both are fine: **subject areas**
(`eventing:`, `capella:`, `monitoring:`, `backup:`, `sgw:`) and **closed axes**
(`index-type:`, `index-class:`, `auth-mechanism:`, `index-state`).
`vector-index:` was named as the second and populated as the first. Its 30
members answered five different questions:

| family | members | destination |
|---|---|---|
| index types | hyperscale, composite, search vector index | `index-type:` (the axis round 11 settled) |
| SQL++ functions | `APPROX_VECTOR_DISTANCE()`, `VECTOR_DISTANCE()` | `n1ql:` |
| similarity metrics | euclidean, euclidean-squared, cosine, dot-product | `vector-similarity-metric:` (new closed enum) |
| settings | `persist_full_vector`, nList, nProbes, `train_list`, replicas, partitions | `vector-search:` for now — see below |
| algorithms, metrics, page titles | IVF, flat, HNSW; recall, memory, QPS; 5 page ids | `vector-search:`, or retired |

So the fix is a **rename, not a dissolution**: the remainder genuinely is a
coherent subject area, in exactly the way `eventing:` and `monitoring:` are. It
was only the name that claimed otherwise. `vector-index:` → `vector-search:`,
with five members evacuated by name to axes that already existed.

**The two vector index types were already promoted — under the minority
spelling.** `index-type:hyperscale-vector` and `index-type:composite-vector` have
had registry files since round 11 at recurrence 2 each, while
`vector-index:hyperscale-vector-index` and `vector-index:composite-vector-index`
were used in 5 files each and read as unpromoted debt. Same labels, verbatim.
The split is by product tree: `cloud/` minted one pair, `server/8.0/` the other,
and `cloud/indexes/indexing-and-query-perf.json` mixes both namespaces inside a
single record. This is round 12's misfiled-roles shape exactly — the majority
usage was the wrong one and looked well-supported. Recurrence 2 → 7 on both, as
the union of the two file sets, not a new count.

The merge is licensed by explicit statements rather than by matching labels:
"Composite Vector indexes are a type of Composite Secondary Index which contain a
single vector field and one or more scalar fields" restates
`index-type/composite-vector.json`'s own `type` line almost word for word.

**The fold supplied a citation round 11 had explicitly declined to invent.**
`index-type/hyperscale-vector.json` carried this note: *"Deliberately NOT related
to `index-type:composite-vector` by `tradesOffAgainst` … indexes.md describes each
one's strengths in separate entries and never compares them, so the comparison
would be the extractor's inference rather than the page's statement."* That
refusal was right about `indexes.md` and wrong about the corpus:
`cloud/vector-index/use-vector-indexes.md` compares them head-on — "A key
difference between Hyperscale and Composite Vector indexes is how they handle
scalar values in queries" — and the relation was *already in the corpus*, under
`vector-index:` ids, where nothing joined it to the record doing the declining.
The lesson is not that round 11 was too cautious. It is that **a refusal recorded
on a record is invisible to the round that acquires the missing evidence.**

### The finding was in the corpus for three rounds, in the right words

Round 11's `indexes.json` record contains this, in a `cross_component_finding`:

> **FOUR NAMESPACES, ONE LIST.** The eight index kinds this page presents as one
> flat enumeration already live in the corpus under four different prefixes:
> `index-type:*` …, `search:*` (full-text-index), `vector-index:*`
> (search-vector-index), `index:*` (view). I reused every one of them rather than
> mint a clean parallel set, so this record deliberately contains the incoherence
> instead of hiding it behind eight new ids. **The fix is a reconciliation
> decision**; the evidence for it is this page, which proves the docs treat all
> eight as one kind of thing.

Round 11 read that record — its taxonomy findings are quoted at length in round
11's own section, and the class/type overlap it describes became
`index-class:`/`index-type:`. It acted on the half of the finding whose remedy was
"promote a concept" and dropped the half whose remedy was "rename 30 ids across
two namespaces." That is the pattern, and it is not carelessness:
**reconciliation acts on the parts of a finding that map onto its existing
outputs, and silently drops the parts that would require refactoring records
already promoted.** There was no slot for this one. Rounds 12 and 13 then
inherited it.

Four instances of the same shape are now on the board — an agent diagnosing a
registry-level defect correctly, in writing, and the diagnosis outliving several
rounds: the nine drifted `concepts/version/` ids (two records, one of which said
"reconciliation must pick one"), `version:server-8-0.json`'s own note filing the
dot/dash count "to the id-normalization backlog", `tradesOffAgainst`'s note asking
a coordinator to re-check its `mustUseInsteadWhen` neighbours, and this one.

### What `providesIndexType` knew

`server/8.0/.../indexes.json` asserts both of these:

- `service:search-service -providesIndexType-> vector-index:search-vector-index`
- `vector-index:search-vector-index -belongsToIndexClass-> index-class:vector`

The predicate names the axis. The object's namespace contradicts it. All seven
predicates the `vector-index:` records use — `providesIndexType`,
`belongsToIndexClass`, `behavesDifferentlyUnder`, `mustUseInsteadWhen`,
`sharesOptionSetWith`, `requiresSetting`, `tradesOffAgainst` — were already
promoted and correctly reused across both trees. **The relation layer converged
while the concept layer forked**, which makes sense mechanically: there are ~100
predicates and every agent prompt lists them, against ~300 concepts where the
table an agent gets is necessarily partial.

It also means a range check would have caught this at write time. If
`providesIndexType`'s object must be an `index-type:` id, the fork was a type
error in a record that passed the evidence gate cleanly. That is the
subject/object slot-type validation already on the backlog, and this is the
concrete instance arguing for it.

### `version:` — one defect, two treatments, and the check that could not see either

Round 13 rewrote nine dotted release ids and reported the corpus clean at one
remaining variant cluster. Twelve dotted spellings were still there, across 31
mentions, headed by `version:server-8.0` (12) and `version:server-7.6` (10).

They were invisible because someone had **aliased** them. `--variants` resolves
aliases before clustering, so an aliased variant collapses to one form and the
cluster vanishes — correctly by the tool's own logic, since an aliased id passes
the gate. But for this defect the alias was the wrong remedy, and worse than
leaving it broken: it made the 12 records pass, which removed the only pressure to
fix them, and it blinded the check built to enumerate the drift to its own two
largest instances.

So the namespace held one defect under two treatments — nine rewritten, two
aliased, one (`version:couchbase-server-7.6`, a long-form spelling) aliased on a
different and better argument. Round 14 gave it one treatment: **rewrite, dashes,
one release one id.** Twelve spellings rewritten across 24 files, both dotted
aliases dropped.

The user had deferred a version-naming policy as "fine for now" on the
understanding that aliasing was what was happening. Both halves of that turn out
to have been half-true — the corpus was doing both — so rather than write a policy
document, round 14 made the policy a control:

- `normalise-ids.py` gained a **rule** rather than table entries:
  any `version:` id containing a dot has its dots replaced with dashes. A table
  needs a new line per release and is wrong by construction on a namespace whose
  members arrive with every product release. Round 13's eight table entries missed
  four, then two more.
- `verify-registry-ids.py` now **rejects an alias that is a mere punctuation
  variant of its own target** — squash both to alphanumerics and compare. This is
  the half that makes it hold from now on: aliasing a punctuation variant is the
  alias-or-rewrite rule applied backwards, and nothing had ever said so.

The check discriminates in both directions, which is why it can be a gate:
`version:couchbase-server-7.6` differs from `version:server-7-6` by a word as
well as by dots and passes; `role:manage-scope-functions` against
`role:query-manage-functions` passes for the same reason. Verified by temporarily
re-adding the bad alias alongside a legitimate one — it flags the first and
ignores the second.

### The 18 promotions

Two of the eighteen are folds into records that already existed (the vector index
type pair); the other sixteen are new files.

**Index types (the axis now has six members, three of them vector):**

| id | recurrence | note |
|---|---|---|
| `index-type:hyperscale-vector` | 2 → **7** | fold; alias `vector-index:hyperscale-vector-index` |
| `index-type:composite-vector` | 2 → **7** | fold; alias `vector-index:composite-vector-index` |
| `index-type:search-vector` | **4** | new; the Search Service's vector index |

**SQL++ functions, re-filed on the pages' own link targets** — both are linked as
`n1ql/n1ql-language-reference/vectorfun.md#…`, and one extraction record says in
as many words "treated as the same real-world function". A link into the SQL++
reference is the source stating which namespace a term belongs to.

- `n1ql:approx-vector-distance` (3) — the only way to make a query use a vector index
- `n1ql:vector-distance` (3) — the brute-force exact alternative

The old pair was also spelled inconsistently with itself:
`vector-index:vector-distance-function` carried a category word in its local name
that `vector-index:approx-vector-distance` did not, and the `n1ql:` namespace
names neither `n1ql:create-function-statement` nor `n1ql:curl-function-function`.

**`vector-search:` (5):** `reranking` (2), `recall-rate` (2), `memory-footprint`
(2), `persist-full-vector` (2), `product-quantization` (2), plus
`scalar-quantization` at **recurrence 1, promoted below the bar under the family
exception and saying so on the record** — PQ and SQ are the two alternatives of a
single choice, and "You do not choose a quantization method for Search Vector
Indexes. Instead, they automatically choose whether to use quantization"
presupposes exactly two options where you do choose. Promoting only the member
that cleared the threshold would leave a two-valued enum half-built, which is the
specific incoherence this round exists to remove. A family straddling the bar is
an argument for reading the family, not for lowering the bar.

**`vector-similarity-metric:` (4, new namespace):** `euclidean`,
`euclidean-squared`, `cosine`, `dot-product`. All four at recurrence 1, all four
promoted together under the same exception, because the source states them as a
closed set with an explicit support matrix — "Only Hyperscale Vector and Composite
Vector indexes support this metric. Search Vector Indexes do not support it." The
competency question *which similarity metrics can this index type use* is
answerable from the docs and was inexpressible in the registry. Filed as its own
namespace rather than inside `vector-search:` because it is a genuine closed enum,
matching `index-class:`, not a subject area.

**`version:` (3):** `server-7-6-2` (6), `server-7-6-4` (2), `server-7-6-6` (2) —
unpromoted at 6 only because the namespace had never been swept *as* a namespace:
14 releases had records, three maintenance releases at ≥2 did not, and nothing
compared the two lists. This is the cheapest possible demonstration of why the
pass is by namespace.

### What the round declined to do

- **`setting:` was not created**, so `vector-search:persist-full-vector` and the
  five watchlisted vector settings stay in the subject area. `setting:` has three
  unpromoted members drawn from three unrelated areas (indexer defer-build, curl
  allowed-URL access, a stream size limit) and no promoted member at all. Filing a
  vector setting into an unbuilt axis would mean filing it twice. It is the next
  namespace this pass should take.
- **`fts:` versus `search:` was confirmed, not fixed.** It looks like a
  one-member-namespace collision and is not: `fts/full-text-search.json` records
  a deliberate resolution of a five-way split, keeping the *capability* distinct
  from `search:full-text-index`, the *index artifact*, with the reasoning and the
  two legitimate non-folds (`cbl:` is a different product, `sdk:…-with-sdk` is a
  page id) written on the record. No new evidence, so no change. A coherence pass
  that "tidied" this would have destroyed a correct decision — which is the
  argument for reading each namespace's existing records before deciding it.
- **IVF / flat / HNSW were not promoted** as an algorithm family, though the
  source compares them directly ("Search Vector Indexes use a flat index when
  indexing datasets with 1000 or fewer vectors … Composite Vector indexes only
  support the next algorithm, IVF"). The namespace question is unresolved: one
  page calls IVF "one of several algorithms to organize its data", which would
  make quantization an algorithm too, and no page says so. Merging on that
  resemblance is exactly what the never-merge-without-evidence rule forbids.
  Watchlisted at recurrence 1.
- **The five page ids were retired, not promoted**:
  `vector-search:vector-index-best-practices`,
  `vectors-and-indexes-overview`, `choose-the-right-vector-index`,
  `hyperscale-filter`, `hyperscale-reranking`. The last is worth naming: it is the
  title of the page "Hyperscale Vector Index Reranking and Full Vector
  Persistence" and it outranked the actual `reranking` concept on every mention
  count (4 against 2) until `seeAlso` stopped counting as recurrence. Same word,
  one page and one concept.
- **`tradesOffAgainst` was not re-typed.** Its own record asks a coordinator to
  check whether some `mustUseInsteadWhen` relations between vector-index
  statements should become `tradesOffAgainst`, and the evidence is now in: the
  hyperscale/composite pair carries `mustUseInsteadWhen` in *both* directions
  across different files, which is precisely the "pointing in opposite directions
  depending on context" shape that note describes. Re-typing means rewriting the
  predicate on evidence-bearing relations, which `normalise-ids.py` can do but
  which needs the pair enumerated first. Deferred with the evidence attached
  rather than left as an impression.

### A predicate whose documented range contradicts its use

`relations/trades-off-against.json` describes itself as a "comparative relation
between two vector-index **strategies** with opposite strengths/weaknesses (e.g.
Hyperscale vs Composite Vector Index)". Its actual use in the corpus is
knob-against-cost: `nprobes -tradesOffAgainst-> recall-rate`,
`persist-full-vector -tradesOffAgainst-> memory-footprint`, `reranking
-tradesOffAgainst-> recall-rate`. Not one of its 10 occurrences relates two index
types.

The description was written from three files early on and never revisited, which
is the same failure as a namespace drifting from its name — **a record's prose
describes the sample that produced it, not the corpus that has since used it** —
and it is worth noting that the coherence pass finds this in the relation layer
too, not only in namespaces. Left as a finding rather than an edit, because
correcting the range means deciding whether the strategy-comparison reading should
be dropped or split into a second predicate, and that is a promotion decision.

### New `docs-issues/`: none — and the four this section first claimed

`docs-issues/` stays at **98**. This section, as first written, listed four new
entries and described them as filed. Sitting down to write the four files closed
none of them and reclassified all four, which is worth recording in full rather
than quietly deleting, because the reclassification is the same test in every case:
**`docs-issues/` is for facts about Couchbase's documentation, and a pass whose
input is the registry rather than a page produces facts about the registry.** Round
14 read no pages. It was always going to produce zero docs-issues, and four slugs
got drafted anyway, in the shape of the bucket the previous thirteen rounds filled.

- `vector-index-namespace-fork-across-trees` — **not a docs defect; the docs are
  correctly adapted.** The claim was that `cloud/` and `server/8.0/` document the
  same vector index types divergently. Both trees do carry all seven
  `vector-index/*.md` pages, and they differ on 18–163 lines each, so the shape
  looked right. Reading one diff end to end shows the differences are *deliberate
  and correct*: `editUrl`/`xref` retargeted per tree, "Couchbase Capella" →
  "Couchbase Server" in every prose sentence, the sample bucket renamed
  `color-vector-sample` → `vector-sample`, and one query idiom changed
  (`USE KEYS "#87CEEB"` → `WHERE meta().id = "#87CEEB"`). That is what
  well-maintained shared source looks like, and it is the opposite of the
  `unadapted-shared-source-content` entries rounds 2 and 12 filed. So **the fork
  was purely a registry artefact**: two rounds of agents read near-identical pages
  and minted different prefixes, which makes it a stronger argument for the
  namespace pass, not a docs finding. Recorded here; no file.
- `qps-unmodelled-in-vector-tuning-tradeoffs` — **a registry gap, and the more
  interesting version of it is a blind spot in the whole method.** QPS is in almost
  every vector tuning statement ("it always decreases queries per second (QPS) when
  enabled", "increasing the number of replicas linearly increases the QPS and
  linearly reduces the latency"), and latency is in several. Neither has ever been
  minted: the corpus contains **zero** ids matching `qps` or `queries-per-second`,
  and one `n1ql:query-throughput` in a single file. So the tuning story has three
  quantities — accuracy, memory, throughput — and the registry holds
  `vector-search:recall-rate` and `vector-search:memory-footprint`.
  The generalisation matters more than the gap: **the backlog can only contain
  terms an agent minted.** `recurrence.py` ranks candidate ids, so a concept the
  docs use constantly and no agent ever named has recurrence *nothing* — not a low
  rank, no row at all. Every promotion queue this project has produced has been
  blind to that class by construction, and this is the first instance identified.
  Watchlisted with the quotes; not a docs-issue, and not promotable without a mint.
- `version-table-column-ambiguity` — **the table is fine; the quote is not.** The
  claim was that the row `| **First Available in Version** | 8.0 | 8.0 | 7.6 |`
  does not identify which column belongs to which index type. As a statement about
  the page that is false: two lines above it, `use-vector-indexes.md` has a header
  row naming Hyperscale, Composite and Search Vector Index in order. What is true
  is the narrower thing — **three `availableSince` relations quote that one row
  verbatim as evidence for three different objects**, and all three pass the gate.
  Two say `version:server-8-0` and one says `version:server-7-6`; all three happen
  to be right, and nothing in the evidence could have told you if one were wrong.
  This is a new species of round 10's "quotable but mis-objected": a quote that is
  verbatim, on the right page, about the right subject, and **under-determines its
  own triple** because the disambiguating information is in the table's geometry
  rather than in any quotable line. A gate that compares strings cannot reach it.
  Filed as a limit of the gate, in "Fifteen limits" below.
- `covering-index-documented-only-as-a-link-target` — **false as written, and the
  truth is worse.** `indexes/covering-indexes.md` is a real 200-line page in both
  trees, it *was* extracted, and it is where the concept's own definition quote
  comes from. So the concept is documented and extracted. What is actually wrong is
  that it is spelled **four ways** across the corpus — `index-type:covering-index`
  (5 files), `indexes:covering-index` (2), `index:covering-index` (2, `server/7.2`)
  and `n1ql:covering-index`/`n1ql:covering-indexes` (6 files, `server/7.2`) — and
  that **every relation any of them appears in, in every spelling, is a `seeAlso`**,
  including on its own dedicated page. `--variants` cannot cluster them: the local
  names differ by a plural as well as the prefix. It is simultaneously a four-way
  namespace split, an all-`seeAlso` concept, and a singular/plural variant, which
  is the `index-type:` namespace's coherence problem in one term. Queued for the
  wave that takes `index-type:`, with the counts recorded so that wave starts from
  a measurement.

**No existing entry was corrected either, and this section also said one was.** It
claimed `dotted-version-id-drift` was "closed by this round rather than reduced";
there has never been a docs-issue by that name. The dot/dash drift was recorded on
`concepts/version/server-8-0.json`'s own note ("filed to the id-normalization
backlog with a count") and nowhere else — which is correct filing, by the same test
as above. Five claims about `docs-issues/` in one section, all five wrong in the
same direction, is worth more than an apology: it is this file's fifth-plus
instance of naming a record that was never written (rounds 2, 3, 5, 8, 10), and
`verify-promotions.py` would not have caught any of it, because it scans for
`ns:kebab-id` and `camelCaseTerm` shapes and never looks at docs-issue slugs. That
is now a known gap in the control, listed in the limits below.

### 86 relation objects identify a page by an alias that will move

Found while checking the `version:` claims, and it is the same defect one layer
out. Round 10 ruled that `current` is a pointer, not a version, and the extract
skill has said since then: *never write `current` into a path or a `page_id`,*
because an id containing it silently starts denoting a different page on the next
major release. That rule was written for the record's own `page_id` and its output
path, and both are clean.

The **object slot is not**. 76 distinct ids containing `/current/` appear as the
objects of **86 `seeAlso` relations across 21 files** —
`server/current/learn/data/data`, `server/current/indexes/indexing-overview`,
`java-sdk/current/howtos/encrypting-using-sdk`. Every occurrence is a `seeAlso`
object and no other predicate is involved, which is what makes it tractable: these
are Markdown link targets, converted to ids by the rule the skill gives for
structural links, and nothing in that rule resolves the alias the way the `page_id`
rule does. 30 of the 76 also keep a `.md` extension and 7 keep an `#anchor`, so one
slot holds three spellings of "a page" that no promoted `pages/` record uses.

Worth stating as a shape rather than a to-do: **a rule enforced on one slot of a
record is not enforced on the record.** The same sentence describes bug #10 —
`seeAlso` excluded from the object slot and not the subject slot — and it describes
the fork `providesIndexType` was carrying. Three instances, all found in this round,
all of the form "the invariant was checked where it was first violated." Not fixed
here: rewriting 86 link targets is `normalise-ids.py` work whose destination depends
on a decision this round did not take (whether a `seeAlso` object should be a
resolved page id, a `pages/` IRI, or a literal URL), and it is refused on the same
grounds as `setting:` — filing into an undecided structure means filing twice.

### What this round taught about the method

- **The recurrence bar and the coherence question fail in opposite directions.**
  The bar over-promotes page ids that recur and under-promotes families whose
  members individually do not. Both showed up here in the same namespace: five
  page ids above the bar, five real concepts below it.
- **A namespace's *name* is an unchecked assertion.** `vector-index:` claimed an
  axis for three rounds. Nothing in the pipeline compares a prefix against what it
  contains, and nothing can, mechanically — but a range check on predicates like
  `providesIndexType` would catch the specific case where a relation and a
  namespace disagree about what an id is.
- **The fix to a metric bug is not always more strictness.** Round 11 excluded
  `seeAlso`, round 12 broadened the slots, and the two corrections silently
  cancelled. Each was right on its own. What was missing was a self-test asserting
  the *earlier* fix still held; `--selftest` now has three cases pinning bug #10 to
  a named instance, and is at 21 checks.
- **Rewriting beats aliasing at namespace scale, and loses at term scale.** A
  25-id prefix rename aliased would leave 25 dead twins, one per record; a single
  display-label variant rewritten would discard a defensible name. The
  alias-or-rewrite rule already said this; what was new is that the *size* of the
  change is itself part of the judgment.
- **Read the namespace's existing records before deciding it.** `fts:`/`search:`
  survived only because the record explained itself. Two of round 14's decisions
  were reversals of what the aggregate view suggested — that one, and
  `index-type:covering-index`.
- **A rule enforced on one slot of a record is not enforced on the record.** Bug
  #10 (`seeAlso` excluded from objects, not subjects), the `providesIndexType` fork
  (predicate checked, object namespace not), and the 86 `/current/` link targets
  (`page_id` resolved, object slot not) are one shape found three times in one
  round.
- **Writing the file is the check; the writeup is not.** Four docs-issues were
  drafted in prose and none was fileable — two were registry findings wearing a
  docs-issue's clothes, and two were factually wrong about the page in ways that
  only reading the page revealed (a header row that does identify the columns; a
  dedicated 200-line page for a concept described as "documented only as a link
  target"). The prose was written from the extraction records, and **an extraction
  record is evidence about a page, not a substitute for it.** A round that reads no
  pages has to go back to one before it may assert anything about one.

### Where the backlog stands

163 concepts at recurrence ≥ 2, down from 203 as counted before this round: 27
retired by the metric fix, 13 absorbed by promotions. 18 predicates unchanged,
still headed by `requiresMinVersionFor` (5), which is a fold into `availableSince`
and not a promotion.

The queue for the next waves, in the order the coherence question is answerable:
`setting:` (does a cross-cutting settings axis exist, or do settings belong to
their subject areas?); `capella:`/`capellaiq:` (`capella-iq` is in both);
`plan:`/`billing:` (`developer-pro` against the promoted
`developer-pro-support-plan`; `paid-support-plan` against `billing:paid-plan`);
`backup:` (`cluster-backup`/`bucket-backup` at 5 look like a *scope* axis crossing
the promoted *type* axis of `full-backup`/`incremental-backup` — the round-11
crossing shape); `js-udf:` (6 members, none promoted, parallel to the `n1ql:`
function vocabulary); `eventing:` (22, the largest); then `search:` and `n1ql:`,
which are largest but also the two the metric fix most changed. Roughly 15 `sgw:`
and `cbl:` candidates remain unpromotable until round 3's trees are re-extracted.

`index-type:` moves up that queue on this round's evidence, with the measurement
already taken: **covering index is spelled four ways** — `index-type:covering-index`
(5 files), `indexes:covering-index` (2), `index:covering-index` (2, `server/7.2`)
and `n1ql:covering-index`/`covering-indexes` (6 files, `server/7.2`) — every one of
its relations in every spelling is a `seeAlso`, and `--variants` cannot cluster them
because the local names differ by a plural as well as by prefix. Round 14 added
three members to that axis and left a four-way split in it, which is the honest
statement of where the pass has got to: the axis is now correct about vectors and
still wrong about pushdowns.

## Round 15 — the namespace coherence pass, wave 2 (`setting:`)

No new pages. Round 14 queued `setting:` next with the question stated as *does a
cross-cutting settings axis exist, or do settings belong to their subject areas?*
The answer is no, and it took one measurement: **34 members, 31 of them at
recurrence 1.**

Wave 1 and wave 2 are the same defect and opposite repairs, which is the useful
thing about doing them consecutively. `vector-index:` was **named like an axis and
populated like a subject area**, so the fix was a rename — one prefix rule, 25 ids,
five evacuated by name. `setting:` is **named like a subject area with no subject to
be about**, so the fix is a dissolution — a 34-line table, because a dissolution's
destination is not a function of the id. A setting is always a setting *of*
something, so the namespace can only ever hold other namespaces' business.

### The axis test

Round 14 named the registry's two legitimate namespace kinds — subject areas
(`eventing:`, `monitoring:`, `sgw:`) and closed axes (`index-type:`,
`auth-mechanism:`, `index-state`) — and left the choice to judgment. This round
has a test for the second one:

> **A namespace is an axis only if its membership is closed and enumerable.**

`vector-similarity-metric:` passes: four members, and there is no fifth, because
`VECTOR_DISTANCE()` takes one of exactly four. `index-state`, `auth-mechanism:`,
`edition:` pass the same way. `setting:` fails, and fails *by construction* rather
than by accident — a product acquires settings for as long as it is developed, so
an enumeration of them is a snapshot with no closing condition. The test is worth
writing down because it is answerable from the namespace alone, before any member
is read, and the wrong answer is what three rounds of promotions were built on
top of.

### The dissolution

All 34 members, by where they went:

| destination | n | note |
|---|---|---|
| `n1ql:` | 29 | Query settings and request parameters — `auto-execute` … `use-fts`, `n1ql-feat-ctrl` (stutter kept: the product's own name is `queryN1QLFeatCtrl`), the `completed-*` family, the `curl-*` family |
| `index:` | 2 | `indexer-settings-defer-build`, `indexer-scan-timeout` — Index service properties, the only members that belonged in neither `n1ql:` nor `data:` |
| `data:` | 2 | `expiry-pager-sleep-time`, `collection-max-ttl` |
| `tls:` | 1 | `couchbase-ssl-cipher-list` |

Three of those 34 are **folds onto a concept the registry already promoted**
(`scan-consistency`, `encoded-plan`, `collection-max-ttl` — see below) and two more
are a **merge of one setting minted twice under two tier names**
(`max-parallelism` + `query-max-parallelism` → one id), so 34 ids resolve to 31
destinations.

Plus `setting-scope:`, a three-member namespace holding `request-level`,
`node-level` and `cluster-level` — the three tiers **round 10 promoted as
concepts**, from the same batch. And three singular/plural fork renames cleared
while the table was open: `tools:` → `tool:` (2 ids), `cloud-providers:` →
`cloud-provider:`.

40 renames, applied: 14 files rewritten, 101 substitutions, 582 scanned.
`setting:` and `setting-scope:` no longer exist in the corpus.

### Three reasons nobody reviewed a 34-member namespace for five rounds

Not carelessness, and worth separating because each has a different remedy.

**1. The promotion rule is per-item, so a namespace can be built entirely out of
items that individually never come up for a decision.** 31 of 34 sat at recurrence
1. Every reconciliation pass since round 10 looked at this namespace and correctly
saw nothing to do.

**2. A canonical reference table mints N terms each at recurrence 1, by
construction.** `query-settings.md` is the one page that documents Query settings.
A term documented in exactly one authoritative place cannot reach recurrence 2
except by a second page repeating it — so **the better the documentation, the less
promotable its contents.** This is the inverse of round 12's finding that
repetition manufactures confidence in an error: repetition is the entire promotion
signal, and single-sourcing is an editorial virtue that reads as absence. Round
14 found the metric blind to concepts no agent ever minted; this is the metric
blind to concepts documented too well to recur. The remedy is not a lower bar —
it is an **admission test for reference-table instances**, recorded below as a
next step.

**3. Round 10 promoted the frame and abandoned the instances.** The commit that
minted these 34 ids (`8425e2ad8`) is the batch whose reconciliation
(`901398912`) promoted the three-tier request/node/cluster model, the
`requiresRequestParameter` predicate, and eight individual settings into `n1ql:`,
`data:` and `tls:`. So the round *did* read this material and did make the right
call about its structure. What it left behind was the extraction layer's own
spelling of the same things, under a prefix its own promotions had just declined
to use. That is a shape worth naming: **promoting a model does not retire the ids
the model was inferred from**, and nothing in the pipeline notices that the
registry and the corpus now disagree about where a concept lives.

### Three members were duplicates of already-promoted concepts, and the enum was right about all three

`setting:scan-consistency`, `setting:encoded-plan` and `setting:collection-max-ttl`
denote things the registry already promotes as `n1ql:scan-consistency`,
`n1ql:encoded-plan` and `data:max-ttl-setting`. Two of the three were promoted by
the same round that minted the duplicate.

Each was declared `registry_status: minted`, and **each declaration was true.**
Nothing named `setting:scan-consistency` was promoted. The round-14 enum exists to
stop re-minting, catches the case that produced `requiresMinVersionFor` twice, and
cannot reach this one, because:

> **The enum checks the id, never the referent.**

A truthful `minted` and a duplicate concept are fully compatible, and no
mechanical check can close the gap — deciding that two ids denote one thing is the
reading step. What *can* be improved is where the reading happens, and the answer
is the same as wave 1's: at the namespace, not at the item. All three duplicates
are obvious the moment 34 members are listed together and invisible one record at
a time.

Consequences recorded on the fold targets: `n1ql:scan-consistency` 6 → 7,
`data:max-ttl-setting` 2 → 3, `n1ql:encoded-plan` 1 → 2. That last one exposed a
separate small thing — round 10 filed `encoded-plan` at `recurrence: 2` under a
metric that counted relation *objects*, and this concept is the object of nothing;
it is the subject of both its relations. The 2 was a count of relations. So **a
recorded recurrence is a claim nothing re-checks after the round that writes it**,
and it happens to be true now for a different reason than it was written for.

### Naming a setting that exists at three tiers

The same setting is spelled three ways: `queryMaxParallelism` (cluster),
`max-parallelism` (node), `max_parallelism` (request). Round 10's extraction minted
the cluster and node spellings as two ids, each at recurrence 1, and nothing could
promote either. Folding them gives recurrence 2 and one concept. The rule this
round adopts:

- Use the **tier-neutral kebab name** when the docs document equivalent settings at
  more than one tier (`max-parallelism`, `num-cpus`, `completed-limit`,
  `completed-threshold`).
- Use the **only documented name** when the setting exists at one tier only
  (`query-curl-whitelist`, which `query-settings.md` files under "Cluster-Level
  Only Settings"; `completed-stream-size`, node-level only).

Because **tier membership is a fact for a relation, not for an id** — the registry
already has `n1ql:cluster-level-query-settings` and its two siblings to be the
object of one. A tier baked into an id splits one concept into three rare ones,
which is exactly what happened, and `setting:collection-max-ttl` shows the same
mistake with a *scope* instead of a tier.

### Promotions: 10 concepts, 4 of them below the bar

| id | recurrence | basis |
|---|---|---|
| `n1ql:system-completed-requests` | 2 | the bar |
| `n1ql:completed-stream-size` | 2 | the bar |
| `n1ql:completed-limit` | 1 | family |
| `n1ql:completed-threshold` | 1 | family |
| `n1ql:curl-all-access` | 2 | the bar, with a correction — see below |
| `n1ql:query-curl-whitelist` | 1 | family |
| `n1ql:curl-allowed-urls` | 1 | family |
| `n1ql:curl-disallowed-urls` | 1 | family |
| `n1ql:max-parallelism` | 2 | the bar, reached by the merge |
| `index:indexer-settings-defer-build` | 2 | the bar |

The family exception has been available since round 2 and has always been the
softest thing in the method — "a small family of individually-low-recurrence terms
that together cover one well-evidenced mechanism" is a description, not a test.
This round has one:

> **If a promoted record cannot state what it *is* without naming a sub-threshold
> sibling, that sibling is part of the family.**

Mechanical enough to apply and to *refuse*. `n1ql:system-completed-requests` is a
bounded, filtered log, and the two things that bound and filter it are
`completed-limit` and `completed-threshold`, each on one page: in. `all_access`
"must be set to false to enable the allowed\_urls and disallowed\_urls fields": in,
and so is the object they live inside. `n1ql:curl-result-cap` is on the same page,
in the same feature, at the same recurrence — and nothing in the access list's
definition names it, so it stays out and stays on the watchlist. Without the test
that call is a matter of taste, and taste admits everything on the page.

`n1ql:num-cpus` also stays out at recurrence 1: the fold renamed it, which is not a
promotion, and no promoted record needs it to define itself.

### Recurrence counts pages, so duplicated content counts one statement twice

`n1ql:curl-all-access` reached 2 on `curl.md` and `query-settings.md`. Those two
pages carry the *same table*: the three descriptive cells for `all_access`,
`allowed_urls` and `disallowed_urls` are byte-identical across both files — 244,
389 and 429 characters, measured, not eyeballed. Two agents read one editorial
statement on two pages and minted the same three properties independently.

That is a third distinct way the promotion metric misleads, alongside round 14's
page-ids-as-concepts and this round's mint-blindness: **the unit of recurrence is
the page, and the docs contain the same content on more than one page.** Filed as
`curl-access-list-table-duplicated-verbatim` — a real docs-issue, because the
duplicated prose is a security control and carries the fail-open condition, and
neither copy references the other.

The same shape, found in wave 1's promotions by the new audit: **the promotion of
`vector-search:product-quantization` rested on one page counted twice.**
`vector-index-best-practices.json`'s only PQ relation quotes "Use PQ when you're
willing to trade some accuracy for higher compression and less memory use", which
is verbatim — on `vectors-and-indexes-overview.md`, the other page. Misattribution,
not fabrication, and precisely what `evidence_source` exists for. Credited to the
page that carries it, the two files collapse to one, so PQ is recurrence 1 and the
quantization pair is symmetric: 1 and 1, promoted as a two-member closed family,
which is what its own record already claimed as its reason. The record is corrected
to say so, and so is `scalar-quantization`'s note asserting a split that does not
exist. Round 14's other error in the same record was a one-word insertion —
`note` quoted "Hyperscale Vector indexes and Composite Vector indexes" where the
page reads "Hyperscale Vector and Composite Vector indexes" — **a paraphrase
presented as a quotation inside a promoted record, which is the one place no gate
looks**, since `gate-evidence.py` reads `extractions/` only.

### Quotability moved onto the promotion path

Both of those were findable by `verify-evidence.py` and had been on disk since the
first POC commit. The reason round 14 promoted off them is a gap in an
*instruction*, not in a script: the reconcile skill says to scope
`verify-evidence.py` to the round's new batch, and **that silently assumes a round
has a new batch.** A registry-input round adds none, so "verify the new batch"
verified nothing, while the same round rewrote ids across the whole corpus.

So the check now runs where a coherence pass actually looks.
`candidate-evidence.py` — the tool for reading a namespace before deciding it —
checks every quote it prints against the page it cites, marks failures
`!! UNQUOTABLE` inline, and `--audit` reduces a run to only the affected ids.
Reading a namespace and checking that what you are reading is real are now one
action with no separate step to forget. All 10 of this round's promotions were
audited before being written.

Making it usable required fixing a false positive first, in `norm()`, where the
gate and the audit share their one definition of "verbatim": this Markdown snapshot
escapes punctuation in prose, so a record quoting `completed_requests` — what a
human reads — was failed against a page that says `completed\_requests`. 9 of 322
corpus failures were this. A small number with an outsized cost, because it lands
on the marker: **an alarm that includes non-defects is an alarm people learn to
skim**, and this one now runs where skimming is the failure it exists to prevent.
Escaping is a rendering artefact, not wording, so de-escaping cannot change a word.
Corpus problems 452 → 443, unquotable 322 → 313.

Two hits survive that look like the same class and are not: a `seeAlso` quote
starting mid-sentence and lowercasing the page's leading "You". Case is wording,
`norm` rightly does not fold it, and truncating a sentence and then editing its
first letter is a real, if tiny, edit. Both are in `seeAlso` relations, which the
promotion metric excludes anyway.

### Two forward-only gate rules, and a test for the gate

The waves keep spending their time on defects that were free to prevent and
expensive to repair. Two are now refused at write time, in `gate-evidence.py`:

- **No singular/plural fork of a namespace the registry already has.** `indexes:`
  beside `index:`, `tools:` beside `tool:`, `cloud-providers:` beside
  `cloud-provider:`. Verified against the current registry: no two existing
  namespaces depluralise to the same string, so the rule cannot fire on anything
  already promoted.
- **No file extension in an id.** The corpus has exactly one
  (`rest-api:compaction-rest-api.adoc`), which is what makes it worth gating now:
  one is a slip, and the rule costs nothing while it is still one.

Both apply to `minted` terms **only**, and that scope is the design rather than a
compromise. 43 shadow prefixes and that one `.adoc` id already exist; refusing to
*reuse* them would block the re-extraction rounds that are how they get fixed, and
would deny a record for a decision an earlier round made. Reuse anything the corpus
has; mint nothing new that repeats the mistake. It is the schema-change discipline
of preferring an additive, forward-only change to a migration — find the point
where "from now on" becomes enforceable instead of aspirational, and put the rule
there.

This is the first time the gate grew a rule that can **deny** something new, and
"blocks what it should block" and "still allows everything it allowed yesterday"
are two claims. The second is the expensive one: the gate is a live `PreToolUse`
hook, so breaking it does not break a report, it blocks every extraction write in
the repo for every agent, including the ones a coordinator cannot see. Hence
`hooks/test-gate.py`, 23 cases, run as a subprocess through the same stdin
interface Claude Code uses.

**Writing it produced the round's most surprising small result.** The obvious
fixture — replay a real record from `extractions/` and assert it is allowed —
fails. `server/8.0/learn/security/authentication-overview.json` was written under
the enum gate and allowed at the time; today it draws five denials, because it
declares `extraction-layer` for `auth-mechanism:x509-certificate` and `minted` for
`rbac-model:privilege`, both of which later rounds promoted. The record was true
when written and is false now. So:

> **`registry_status` is a claim about a moving target, and the gate's verdicts
> have a shelf life.**

Two tempting mistakes follow, and both are wrong. Do not re-run the gate over the
corpus as an audit — it would report denials in proportion to how much has been
promoted since, all of them false. And do not "fix" old records to agree with
today's registry: their declarations describe the registry they were written
against, which is information, and it would have to be redone at the next
promotion. `verify-evidence.py` is the corpus-wide check precisely because its
claim — is this sentence on that page? — relates two fixed things and does not
decay.

### New `docs-issues/`

- `curl-access-list-table-duplicated-verbatim` — the CURL() access-list table
  appears in full on `n1ql-language-reference/curl.md` and on
  `n1ql-manage/query-settings.md` (as the `Access` schema the `queryCurlWhitelist`
  row links to), with all three descriptive cells byte-identical. Neither page
  cross-references the other's copy, and `curl.md` never mentions
  `queryCurlWhitelist`, which is the setting the access list is written to. Filed
  because it is a security control: whichever copy is edited, a reader following
  the other gets the older rule.

One entry, from a round that read four pages, and the count is the point rather
than an apology. Round 14 drafted four docs-issues in prose and filed none —
two were registry findings in a docs-issue's clothing, two were wrong about the
page. The rule it wrote for itself was *open the page before filing*, and the
observable effect here is a smaller, checked list: the CURL duplication is a
measurement, and the three near-misses that did not get filed (the tier tables'
inverted `-1` sentinel, the `threshold`/`completed-threshold` double spelling, the
"whitelist" setting whose own properties are named allowed/disallowed) are product
facts or product naming, not documentation defects.

### What this round taught about the method

- **A namespace is an axis only if its membership is closed and enumerable.** The
  first coherence question in this pass that can be answered before reading a
  single member.
- **The better a thing is documented, the less promotable it is.** Recurrence
  cannot see anything documented in exactly one authoritative place, and a
  canonical reference table produces those by the dozen. Round 14 found the metric
  blind to what no agent minted; this is blindness to what is single-sourced. Both
  are the same underlying fact — *the metric measures repetition, and repetition is
  an editorial property of the docs, not a property of the concept.*
- **The unit of recurrence is the page, and pages duplicate each other.** A
  byte-identical table on two pages is two files and one statement. Two of this
  round's ten promotions were affected, one of them from wave 1.
- **The enum checks the id, never the referent.** Three duplicates of promoted
  concepts were declared `minted`, truthfully. There is no mechanical fix; there is
  a better place to look, which is the namespace.
- **Promoting a model does not retire the ids it was inferred from.** Round 10
  promoted the three-tier settings model and left `setting-scope:` holding its own
  three tiers, in the same commit pair.
- **A control's verdict can expire.** The write-time gate reads a registry that
  grows, so replaying an old record through it produces false denials. Worth
  knowing before someone reaches for it as an audit — which is what a green,
  cheap-looking script invites.
- **A verification instruction can assume a fact about the round.** "Scope
  `verify-evidence.py` to the new batch" is correct advice that silently verifies
  nothing when the round's input is the registry. Round 14 is the first round that
  had no batch, and it promoted 18 concepts out of pre-gate records; two defects in
  one of them survived to be found here.
- **Rename versus dissolve is decided by whether the destination is a function of
  the id.** Wave 1's fix was a prefix rule over 25 ids; wave 2's needed a 34-line
  table for 34 members. Both namespaces were incoherent in the same way and the
  repairs have nothing in common, so "how do I fix this namespace" is not a
  question with one answer.

### Where the backlog stands

159 concepts at recurrence ≥ 2, down from 163: 31 `setting:` members were never in
it (recurrence 1), which is the whole point of the round — the debt this wave
cleared was invisible to the count that measures debt. 18 predicates unchanged,
still headed by `requiresMinVersionFor` (5), a fold rather than a promotion.
Shadow prefixes — a prefix in `extractions/` with no namespace behind it in
`concepts/` — are down from 55 holding 271 ids to **43**, and only two
singular/plural forks remain, both now refused for new mints.

**Wave 3 is `indexes:`**, and it merges with the `index-type:` work round 14 queued:
30 ids across 14 files against `index:`'s 4 promoted members, with covering index
spelled four ways across `index-type:`, `indexes:`, `index:` and `n1ql:`. This
round adds a member to `index:` (`indexer-settings-defer-build`, a setting in a
namespace otherwise holding storage modes and index kinds), so that namespace's own
coherence question is now open too and should be answered in the same wave.

Then, unchanged from round 14's queue: `capella:`/`capellaiq:`, `plan:`/`billing:`,
`backup:`, `js-udf:`, `eventing:` (22, the largest), then `search:` and `n1ql:`.

New next steps this round surfaced:

- **`cloud/vector-index/` needs re-extraction, not repair.** 7 records from the
  first POC commit, pre-gate, 3 with unquotable evidence, and wave 1 promoted 22
  concepts out of them. Two defects found here were in one record; nobody has
  checked the other six against their pages.
- **An admission test for reference-table instances.** Something that can propose
  `node-quota`, `prepared-limit`, `loglevel`, `controls`, `functions-limit`,
  `keep-alive-length`, `max-index-api`, `tmpspace-dir`/`-size` — all documented on
  `query-settings.md`, none ever minted by any extraction, so all invisible to
  every queue this project produces. Second instance of round 14's mint-blindness,
  and the first with an obvious mechanical source: a settings table's own rows.
- **`cloud-providers:gcp-azure` needs its relation split in two.** One id naming
  two providers, surviving the fork fix because the local name is the defect.
- **`rest-api:compaction-rest-api.adoc` should not be a concept.** Now refused for
  new mints; the existing one still needs retiring or re-typing.

## Round 16 — the namespace coherence pass, wave 3 (`indexes:`, `index-type:`, `index:`)

No new pages. Round 15 queued `indexes:` — 30 ids across 14 files — and noted that
two other namespaces had to be settled in the same wave: `index-type:`, whose
covering-index split round 14 had deferred, and `index:` itself, which round 15 had
just added a *setting* to and which already held storage modes and index kinds. So
this wave is three prefixes at once, for a reason worth stating up front: **they are
one subject, and every defect in them came from a different round naming that
subject after a different directory.**

### The measurement that had to come first

`indexes:` could not be read before fixing the query used to read it. Bug #10 (round
14) excluded `seeAlso` from the promotion metric in both slots, correctly, by putting
one `keep` flag in front of a shared block. That block also fed `mention_files`, the
table printed under the heading **"any mention, incl. bare `concepts[]` entries"**.
So from round 14 onward an id that the corpus only ever *linked to* appeared in no
table at all — including `--variants`, whose entire job is to enumerate spellings.

The heading was false and the consequence was not a wrong count but invisibility.
Fixing it (bug #11, one line, unconditional) took the census from **1,736 to 2,112
distinct ids on an unchanged corpus — 376 ids, 18%, that no report this project has
ever produced had named**. Among them:

- **Five misspellings of already-promoted SQL++ statements** — `n1ql:createprimaryindex`,
  `n1ql:dropprimaryindex`, `n1ql:alterindex`, `n1ql:dropindex`, `n1ql:orderby`. Every
  file using one was being denied by the write-time gate as unpromoted, and
  `--variants` — the check built to enumerate exactly this — reported **1 cluster**
  before the fix and **6** after.
- **`covering-index` at 14 distinct files, in five spellings, across three
  namespaces**, reading as recurrence **0** on the promotion metric and appearing in
  no report whatsoever.

Both promotion tables are still right to exclude `seeAlso`: a Markdown link is not an
assertion. The generalisable lesson is about how the exclusion was implemented:
**excluding a relation kind from a metric and excluding it from a census are
different decisions, and doing the first by editing a shared code path silently does
the second.** Bug #10's fix made the two slot tables symmetric and left the mention
table lopsided, in the same edit, and the tests written for bug #10 passed.

A second number moved for the same reason and is worth recording because it was
quoted in the last two writeups: shadow prefixes — a prefix in `extractions/` with no
namespace behind it in `concepts/` — were reported as **43** in round
15 (172 ids by that method) and are **55 holding 210** here, with no change to the corpus. Round 15's figure
was counted from `concepts[]` declarations alone. Nothing was fixed and nothing
regressed; the smaller number was measured with the blind instrument.

### The diagnosis: one subject, three directories, three prefixes

`covering-indexes.md` exists in four trees, at three different paths:

| tree | path |
|---|---|
| `server/7.2`, `server/7.6` | `n1ql/n1ql-language-reference/covering-indexes.md` |
| `server/8.0` | `indexes/covering-indexes.md` |
| Capella | `cloud/indexes/covering-indexes.md` |

Three rounds extracted it, from three directories, and each named the concept after
the directory it was reading in: `n1ql:covering-indexes`, `index:covering-index`,
`indexes:covering-index` — plus `index-type:covering-index` and `n1ql:covering-index`
for good measure. Nobody was careless. In 8.0 Couchbase moved nine `learn/`
index pages into a new top-level `indexes/` module and Capella mirrors the new
layout, so the directory genuinely changed under the same content
(`docs-issues/server-index-pages-relocated-between-versions`).

The rule this wave adds, and the one worth carrying forward:

> **An id names its subject, not its location.** A directory name is evidence about
> where an editorial team files a page, and a page's path is not stable across
> releases even when its content is.

`indexes:` existed for one reason only — Capella files these pages under `indexes/` —
and it was minted in the POC's first commit and honestly carried forward by five
rounds since.

### The axis test, third application

Round 15's test — *a namespace is an axis only if its membership is closed and
enumerable* — applied to three prefixes gives three different answers, and the third
one is new:

| prefix | verdict | contents |
|---|---|---|
| `index-type:` | **axis** | kinds of index, and nothing else |
| `index:` | **subject area** | everything else true of indexes: settings, storage modes, rebalance methods, pushdowns, scan mechanics, on-disk artifacts |
| `index-class:` | axis, untouched | two members (Traditional, Vector), closed, already correct |
| `page:` | **neither** | a *part of speech*: an id that denotes a document |

`page:` is the new answer. Round 15 said a third possibility existed; this round had
to use it. An id like `indexes:storage-modes` is not a badly-filed concept, it is a
page reference that has learned to look like a concept id, and no prefix naming a
subject area can hold it honestly.

### The rewrite

59 renames. Applied: **36 files rewritten, 160 substitutions, 582 scanned, 21
registry aliases retired.**

| from → to | n | what moved |
|---|---|---|
| `indexes:` → `index:` | 21 | the pushdown family, scan mechanics, lifecycle, on-disk artifacts |
| `index:` → `index-type:` | 12 | **the shadow copy** — see below |
| `indexes:` → `page:` | 6 | six page references (eight ids, two of them duplicate spellings) |
| `index-type:` → `index:` | 6 | `covering-index`, `duplicate-index`, `index-span`, `group-aggregate-pushdown`, and the two storage modes `moi` / `standard-gsi-plasma` |
| `n1ql:` → `n1ql:` | 5 | the five run-together statement names bug #11 had hidden |
| `indexes:` → `vector-search:` | 2 | `reranking`, `codebook` |
| `index:` → `page:` | 2 | `index-scans`, `storage-modes` — the same two pages, spelled again |
| `n1ql:` → `index:` | 2 | two more covering-index spellings |
| `indexes:`/`index-type:` → `storage-engine:` | 2 | `plasma`, `forestdb` |
| `index-type:` → `index-type:` | 1 | `secondary` → `secondary-index` |

`indexes:` now has **0** occurrences in the corpus, as do `vector-index:`, `setting:`,
`setting-scope:` and `tools:` from earlier waves. `cloud-providers:` stays at 1 on
purpose: `cloud-providers:gcp-azure` is one id standing for two promoted providers,
and rewriting it to either would silently drop the other. `--variants` is back to
**1 cluster** from 6, and the survivor is junk (`"1"` and `"1%"` used as relation
objects — queued, not fixed).

### The shadow copy

Twelve of the renames are one defect: **`index:` had accumulated a second, partial
copy of the `index-type:` axis.** `array-index`, `functional-index`, `partial-index`,
`composite-secondary-index`, `named-primary-index`, `primary`, `primary-index`,
`secondary-index`, `secondary-gsi`, `global-secondary-indexes`, `analytics`, `view` —
twelve ids resolving to nine members of an axis that already existed.

Two rounds read the same enumeration in two different directories and each minted
from the directory it was in.

The part worth measuring is what the shadow was made of. **Eleven of the twelve were
bare `concepts[]` entries at one file each** — declared, never used in a relation, and
therefore contributing nothing to the promotion metric and nothing to the axis's
apparent weight. Only `index:view` carried real evidence (3 files in either slot), and
it is the one that needed a re-filed record rather than a fold. So the shadow was not
suppressing the axis's recurrence; it was **debt in waiting** — twelve ids that every
future extraction of those pages would have kept minting, none of which would ever
have crossed the promotion bar, and all of which the census would have reported as
unpromoted candidates forever.

### Promotions

Five new registry records, one deleted, one re-filed.

- **`concepts/index/covering-index.json`** — recurrence **0** on the promotion metric,
  14 files in the census, promoted on the **semantic-weight exception** and the
  fold licensed by the labels rather than by any relation: all five spellings label
  themselves as the thing ("Covering Index / Covered Query"), none as a page title.
  Filed in `index:` and not `index-type:` on the strength of the page's own grammar —
  the index covers *the query* — and of the disqualifying definition in
  `indexing-and-query-perf.md`, which lists Covering Index among its types and then
  defines it *after* index selection. **A type you cannot know at CREATE INDEX time
  is not a type.**
- **`concepts/indexer-node-state.json`** — recurrence 3, an enum, and the round's
  clearest fold: it merges `capella:index-ui-status`, promoted in round 12, whose
  file is **deleted**. First deletion of a promoted record in this POC. The licence is
  the strongest kind here recognised — the same defining sentence in each tree,
  differing by one word — and the interesting part is why it took four rounds.
- **`concepts/index/file-based-index-rebalancing.json`** (2) and
  **`concepts/index/index-redistribution-setting.json`** (2) — the second answers a
  question round 15 deferred when it moved `indexer-settings-defer-build` into
  `index:`.
- **`concepts/index-type/view.json`** — re-filed from `concepts/index/view.json`
  (recurrence 3). It was always a kind of index; only its filing was wrong.
- **`relations/is-synonym-of.json`** — recurrence 4 → 5, **range widened** from
  statement pairs to concept pairs, on one explicit sentence: "A secondary index is
  also called a Global Secondary Index (GSI)." The two concepts are still **not**
  merged, and that is the point of having the predicate: both spellings are in live use
  (`secondary-index` at 3 files on the promotion metric and 6 in the census, `gsi` at 8
  and 16), a reader searching either should land somewhere, and
  **synonymy is a fact to record, not an instruction to deduplicate.**

### A `recurrence` field is a measurement with a date

This one was found by being wrong, in this document, and re-measuring.

`index-type:gsi` carried `recurrence: 2` and the note "a minor, low-stakes promotion".
This section's first draft explained the field's move to **8** as the effect of folding
`index:secondary-gsi` and `index:global-secondary-indexes` into it. That is false. Both
were bare `concepts[]` entries at one file each; the metric said 8 before this round
touched anything, and the census said 16. The field was measured in round 2 with the
object-only metric that bug #7 replaced, and **nothing re-measures a promoted record.**

Measured across the registry: **153 of 324 promoted concepts (47%) carry a `recurrence`
that matches the current metric.** The 171 that disagree do so in both directions and by
as much as 40 — `capella-role:organization-owner` claims 10 where the metric says 50
(the corpus grew), `n1ql:query-context` claims 22 where it says 7 (the instrument
changed: that 22 was measured before `seeAlso` came out of the count).

**None of those is an error**, and this must never become a rewrite: the number records
the evidence base at the moment of promotion, which is information about the decision —
the same argument that stops `hooks/test-gate.py` from "fixing" old records to match
today's registry. The hazard is narrower and it is the one that bit here: a promoted
record's prose reasons about its own weight, a reconciliation pass reads that prose, and
it is now wrong about a term's standing 54% of the time. So `recurrence.py
--stale-recurrence` reports the disagreements and says in its own comment that it is not
a fix-it list. One more consequence, applied immediately: `search:full-text-index` was
written this round with `recurrence: 5`, which is its *census* figure — the promotion
metric says 3. The report caught it, and the field now carries the metric the promotion
rule is stated in terms of, with the other number in prose beside it.

### A refusal is only as good as the set it searched

The `indexer-node-state` fold is worth its own subsection, because the reason it was
missed is not carelessness and recurs.

Round 12 minted `capella:index-ui-status`, checked it against the registry, and
**refused** to merge it with `index-state` — correctly, in writing: *"a value set
(ready/pause/warmup) that does NOT match the existing index-state enum's values …
Kept as a distinct concept rather than merged, since no page reconciles the two
vocabularies."* That refusal was right about `index-state` and blind to
`index:indexer-node-state`, which was already in the corpus with the same three
values, because it had never been promoted — so `registry-digest.py`, the tool the
brief tells agents to run, could not show it.

The agent searched the registry. The id it needed was in the **extraction layer**. A
registry digest is the wrong set for "has anyone named this already?", and this is
the second time a well-argued refusal has been overturned by evidence that was
already on disk. Round 12's *other* refusal — not merging `index-state` with the
node-state enum — is reaffirmed: those are genuinely different things, an index's
lifecycle versus a node's Index Service, and no page reconciles them.

### Deliberate refusals

Not everything with a destination got a record. Named here so the next round does not
re-derive them:

- **The pushdown family** (`index:index-pushdown`, `predicate-pushdown`,
  `order-pushdown`, `pagination-pushdown`, `operator-pushdown`, `index-projection`,
  plus `group-aggregate-pushdown` at recurrence 3). This is exactly the shape the
  promotion rule's *family* exception was written for, and it is still refused,
  because **the head page of the mechanism, `server/8.0/indexes/index_pushdowns.md`,
  has never been extracted.** Promoting a family out of six passing mentions while
  its defining page is unread would be promoting the corpus's shape rather than the
  documentation's.
- **The three storage engines** — `storage-engine:plasma`, `forestdb`, and Nitro
  (never minted at all). Same reason: their only evidence is `storage-modes.md`, in
  the same unextracted module.
- **`index:sequential-scan`, `index:index-span`, `index:order-pushdown`,
  `index:index-consistency`, `index:skiplist`** — recurrence 1, real terms, and left
  on the watchlist rather than promoted on a sample of one.

### `folded_spellings`: the third alias state

Round 14's rule was binary — a spelling is either aliased or rewritten. This round
needed a third state, and found it by nearly writing the wrong thing.

The plan was to record all 59 folds in each target's `aliases` array. That is wrong,
and `--variants` is what makes it wrong: it seeds the registry as a speller, so a
registry alias with zero corpus occurrences shows up as a cluster forever — permanent
false debt, a symptom already visible from round 14's seven `vector-index:` aliases.

So: **`aliases` = a spelling deliberately left live in the corpus. `folded_spellings`
= a spelling rewritten out, kept as history, read by nothing.** 21 dead aliases moved
across by `sweep_dead_aliases()`, whose first version got it wrong in the instructive
direction: testing only "no corpus occurrences" flagged 24, two of them legitimate —
`relations/see-also.json`'s `rdfs:seeAlso` (an external-vocabulary mapping) and
`role/ro-admin.json`'s `role:read-only-admin` (a display-name alias, the exact case
the docstring endorses). The fix requires *both* zero occurrences **and** membership
in this script's own rename tables: **an unused alias and a killed alias are not the
same thing, and only the second is history.**

### An alias is a claim about a referent, and nothing checks referents

`concepts/fts/full-text-search.json` listed `index:full-text` as an alias. Full-Text
Search is a service; `index:full-text` is an *index*. The alias was a category error
sitting inside the mechanism the gate trusts to resolve ids, which means the gate had
been resolving a wrong claim as authoritative. Moved to
`concepts/search/full-text-index.json` (recurrence 4 → 5).

Round 15 recorded that **the enum checks the id, never the referent.** The corollary
this round adds: **an alias is a claim about a referent, and nothing checks
referents.** There is no mechanical fix available; there is a place to look, which is
the same one as last time — the namespace, read as a set.

### `page:` — measured, and made re-runnable

Eight ids were swept into `page:` as a pilot, collapsing to six page references. The
population is much larger. By the honest census: **392 of 2,116 distinct ids (18%)
appear only as the object of a `seeAlso`, are never declared in any record's
`concepts[]`, and have no registry file** — 305 of them not even carrying a namespace
(bare paths like `cloud/eventing/eventing-advanced-keyspace-accessors`, at 9 files),
the rest wearing a prefix that asserts they are concepts of some subject area.

That measurement is now `recurrence.py --page-ids` rather than a paragraph here,
which is the round's small methodological commitment: **a next step you can re-run is
a next step; a number in prose is a memory.** The report is deliberately a *candidate
list* and not a rewrite table — `covering-index` was in this exact set at 14 files
and earned a promoted record, not a prefix change. The discriminator is the label: a
term no record has ever bothered to label is a term no extraction thought it was
naming.

### Controls added, each because something was wrong first

- **The retired-prefix rule** (`hooks/gate-evidence.py` + `hooks/retired-prefixes.json`).
  Five prefixes are now refused at write time: `indexes:`, `vector-index:`, `setting:`,
  `setting-scope:`, `tools:`. Two things distinguish it from the round-15 id-shape
  rules, and both were forced by the material:
  - **It fires whatever `registry_status` says, `extraction-layer` included.** The
    round-15 rules are scoped to new mints so that reuse — and therefore repair —
    stays legal, and that is right while the ids are still in the corpus. A prefix is
    entered in `retired-prefixes.json` only once its sweep is verified complete, so
    "reused from an earlier extraction record" has nothing left to refer to and is
    necessarily false. The reuse rule is what propagated `indexes:` through five
    honest rounds in the first place, so the fix has to sit outside the status enum.
  - **It reads relation subjects and objects, not just declarations.** Bug #11's
    measurement is the argument: 18% of the corpus's ids never appear in any record's
    `concepts[]`, so a check that reads declared concepts is blind to a fifth of the
    vocabulary — the same defect, in a second place. `hooks/test-gate.py` grows eight
    cases, and **one existing assertion flips from allow to deny**: the first time a
    verdict in that file has been reversed. A flip like that belongs in the test with
    its reasoning attached, because the diff is otherwise indistinguishable from a
    test loosened to make a change pass.
- **`verify-registry-ids.py` now checks that every `docs-issues/<slug>` a registry
  record points at has a file.** Writing this round's six issues turned up two
  references from earlier rounds pointing at slugs that do not exist —
  `docs-issues/dcp-name-drift` and `docs-issues/who-creates-analytics-indexes-contradiction`,
  both filed with the directory's `server-` prefix. Neither is a typo in the ordinary
  sense: the author wrote the issue's descriptive name, and the reference was
  plausible, adjacent to a real file, and wrong for four rounds. This is
  `verify-promotions.py`'s failure shape — narrated as existing, never filed — in the
  other direction, and it fails silently in the direction that matters most: a
  promoted record says "see `docs-issues/X` for the contradiction", a reader finds
  nothing, and concludes the caveat was never real.
- **`recurrence.py --page-ids`** and **`recurrence.py --stale-recurrence`**, both
  above, plus two new self-test guards for the tables they read. Neither is a gate:
  they are re-runnable measurements standing in for two sentences this writeup would
  otherwise have asked a future round to remember.

### New `docs-issues/` (6, taking the total to 105)

- **`server-index-pages-relocated-between-versions`** — nine index pages moved out of
  `learn/services-and-indexes/indexes/` into a new top-level `indexes/` module in 8.0,
  and `covering-indexes.md` moved out of the SQL++ reference. Not a docs bug;
  everything that keys off a path pays for it, including this project.
- **`server-index-type-taxonomy-mixes-kinds`** — `Types of Primary and Secondary Index`
  presents eleven H2s as types of index and its own prose disqualifies two of them
  ("A duplicate index is not a special type of index, but a feature of Couchbase
  indexing", and Covering Index defined post-selection).
- **`server-two-index-type-enumerations-do-not-agree`** — two pages enumerate the
  types of index on two different keys: eight keyed by providing service in `learn/`,
  eleven keyed by key shape in `indexes/`. The intersection is four. Neither page
  mentions the other's scheme, so "how many kinds of index are there?" has two
  answers depending on where a reader landed.
- **`server-storage-engine-used-at-two-levels`** — "Grouping and aggregate pushdown is
  supported on both storage engines: Standard GSI and Memory Optimized GSI (MOI)" on
  one page; Plasma / Forestdb / Nitro named as the storage engines *under* those two
  modes on another. A reader who reads the second page first will conclude pushdown
  is unsupported on Forestdb, which nothing says.
- **`server-index-state-vocabularies-inconsistent`** — three unreconciled state
  vocabularies (index lifecycle; indexer node status; `Active`/`Warmup`/`Paused` used
  in two sentences of `storage-modes.md` at two different levels). `Active` appears in
  neither enumerated vocabulary.
- **`server-indexer-status-enum-value-sets-differ`** — the same field documented with
  four values in Server and three in Capella, in otherwise near-identical sentences.
  This is the discrepancy the `indexer-node-state` merge carries rather than resolves.

### Two transcription defects, in promoted records

Both found by `candidate-evidence.py --audit`, both in records this project wrote,
and they are the same species:

1. **The elided quote** — two real fragments of a page joined by a literal `...`,
   presented as one quotation.
2. **The de-formatted quote** — `* **status**. The current state …` cited as
   `status. The current state …`. Word-perfect, meaning unchanged, and unquotable.

Neither is a comprehension failure and neither survives comparison against the file,
which is exactly why a careful reader will pass both. Recorded as corrections inside
the records rather than silently repaired upstream. Note what is still unchecked: the
quotes inside *promoted* records are read by no script at all (`verify-notes.py`
remains a queued next step), and both of these were in that blind spot.

### Where the backlog stands

**156** concepts at promotion-metric recurrence ≥ 2 unpromoted, down from 159. **454**
at census recurrence ≥ 2, a table that did not exist honestly before this round.
**18** predicates, unchanged, still headed by `requiresMinVersionFor` (5) — a fold, not
a promotion. Shadow prefixes **55 holding 210 ids**, by the honest census (43/172 by
the old one). Registry: 327 concepts, 93 relations, 105 docs-issues — and **153 of
those 324 recurrence fields (47%) still agree with the metric**, which is a number this
project did not have before today and should not try to make 100%.

`verify-evidence.py` over the whole corpus: **443 problems — 313 unquotable + 130
empty**, unchanged before and after this round's 160 substitutions, which is the
result to want from a pure rename. Note that `README.md` and this file have both been
quoting **322 unquotable** since round 10; the correct figure is 313, and the 130 is
right.

### Round 17 is a content round, and this wave is why

**Extract `server/8.0/indexes/` (11 pages) and re-extract `cloud/indexes/` (11).**
Two different jobs, and the wording matters, because this round's own draft called
both of them a re-extraction and thereby mis-filed the more important half.
`server/8.0/indexes/` has *never been extracted* — round 12 walked `learn/` looking
for these pages and they had already moved out of it — so it is **first contact**
with the canonical documentation of the subject this wave spent its whole length
reorganising, and its success criterion is new coverage: what does the module say
that nine rounds have never read? `cloud/indexes/` is the other kind — 11 records
that exist, written pre-gate, thin at 35 relations over 11 pages (mean 3.2, against
round 10's baseline of 13.4) with three defective quotes — so it joins
`sync-gateway/`, `couchbase-lite/` and `cloud/vector-index/` on the remediation
list, where the criterion is that the records become trustworthy and the *existing*
conclusions either survive or are corrected.

The distinction is the finding, not pedantry. A never-walked directory and a
badly-walked one both report as a low recurrence count, and **nothing in this
pipeline distinguishes them** — but they fail differently. Bad records make claims
that can be checked and found wrong; a directory nobody read makes no claims at all,
so it produces no defect for any control to catch, and the only symptom is a number
that looks like modest importance. Filing the first kind under "re-extraction" hides
it inside a backlog whose whole framing is "these records are unreliable", which is
the one thing that is not wrong with it. Run them together anyway: each is the
other's diff-gate, and a diff-gated wave finds content problems at the highest rate
this project has measured.

This is the round's largest finding about the method, and it is not about namespaces:
**the corpus is not the documentation.** Recurrence measures extraction history. Every
count in this section — `covering-index` at 14, the pushdown family at 1-3 apiece,
the storage engines at 0-2 — is a fact about which directories nine rounds happened
to walk, and the subject's own module was not one of them. Round 15 established that
recurrence measures repetition rather than importance; this adds that it measures
repetition *within the sample*, and that a coverage plan built from directory names
inherits every reorganisation the docs have ever undergone.

Then, and only then, promote out of the new records: the pushdown family, the three
storage engines, `index:sequential-scan`, `index:index-span`, and the key-shape index
types (`array-index`, `functional-index`, `partial-index`, `composite-secondary-index`,
`named-primary-index`) with real evidence behind them rather than a shadow copy's.

**Wave 4**, unchanged from round 14's queue: `capella:`/`capellaiq:`, `plan:`/`billing:`,
`backup:`, `js-udf:`, `eventing:` (22, the largest), then `search:` and `n1ql:`.

## Round 17 — the indexes module: first contact and re-extraction, run together

**Scope.** 22 pages, two jobs, deliberately paired. `server/8.0/indexes/` (11 pages,
never extracted) as **first contact**; `cloud/indexes/` (11 pages, extracted pre-gate)
as **re-extraction**. 743 relations, 0 cross-page, **0 problems** under
`verify-evidence.py`, corroborated independently by `hooks/gate-log.jsonl` (19 allows,
2 denials, both diagnosed below).

**The density result, which is what the round was commissioned to measure.**

| | pages | relations | mean | against |
|---|---|---|---|---|
| `cloud/indexes/` re-extraction | 11 | **343** | 31.2 | the same pages' pre-gate records: 35 total, mean 3.2 |
| `server/8.0/indexes/` first contact | 11 | **400** | 36.4 | round 10's baseline of 13.4 |

Re-extraction recovered **9.8× more relations from the same eleven pages**. The old
records were not slightly thin; they were missing roughly nine tenths of what the
pages state. First contact came in at 2.7× the project's baseline, making this the
densest material extracted in seventeen rounds. Both halves of the pairing earned
their place, and the second is the reason the first was trustworthy: each batch was
the other's diff-gate.

### The storage stack: settled, and the evidence had been written down two rounds ago

Round 16 ruled that `storage-engine:` must stay separate from `index:*-storage` and
could not promote the engines. `server/8.0/indexes/storage-modes.md` settles it, in
the strongest form available — **one setting value maps to two engines, by edition**:

> In Couchbase Server Enterprise Edition, standard index storage is supported by the
> Plasma storage engine.
> In Couchbase Server Community Edition, standard index storage is supported by the
> Forestdb storage engine.

A one-to-many map ends the argument without appealing to anyone's intuition about
what a "mode" is: if `standard` were another name for Plasma it could not also be
Forestdb. Four levels, now recorded in `concepts/index-storage-stack.json` — setting
→ its two values → the engine implementing a value → (Forestdb only) the engine's
write mode.

**The part worth keeping is where the evidence was.** This round's first draft of
that record said round 16 "could not cite a source". That was wrong, and the
correction is recorded in the record itself: round 16 *did* cite it.
`docs-issues/server-storage-engine-used-at-two-levels` quotes storage-modes.md
naming Nitro and states the conclusion this round reached — "Plasma / Forestdb /
Nitro belong in `storage-engine:` beside couchstore and magma". Round 16 was right,
in writing, and did not promote the terms.

Why not: the engine names existed in **the prose of a defect log** and in no
extraction record, because the page had never been extracted. `recurrence.py` reads
`extractions/`. So three terms sat at recurrence 0 by the only measure the promotion
machinery consults, while being correctly written down elsewhere in the same
repository. Round 16 taught that a refusal is only as good as the set it searched;
this is the same lesson one layer out — **a promotion is only as good as the set it
counted**, and any pipeline that decides promotions from one directory will do this
again.

`storage-engine:nitro` is promoted at **recurrence 1** — one sentence in 593 records,
the thinnest evidence behind any concept in this POC — under the family exception,
because promoting Plasma and Forestdb without it would assert by omission that one of
the two storage settings is implemented by no engine. **A partly-promoted family is
worse than none of it, because the gap is indistinguishable from a fact.**

### Two instruments, four reversed decisions, in both directions

`shared-source.py` (new) and `recurrence.py --forks` (new flag) were built in this
round to measure the two ways the promotion rule's "two distinct files" proxy fails.
Both changed real decisions, which is the only test that matters:

- **`index-type:array-index` and `index-type:functional-index`: refusal → promotion.**
  Mid-round, on a partial corpus, both appeared to rest solely on
  `indexing-and-query-perf.md`, whose copies score 0.94 — one authored page twice —
  and the round was drafting a refusal citing shared source. Completing all 22
  records added `index-scans.md` and `groupby-aggregate-performance.md` in both trees:
  different authored pages, 3 and 2 independent sources. **A shared-source discount
  computed over a partial corpus is not conservative, it is wrong**, and it errs
  toward refusing real terms — subtracting inflation from an incomplete count yields
  a number with no interpretation at all.
- **`index:duplicate-index`: promotion → refusal.** It had the round's most quotable
  sentence ("A duplicate index is not a special type of index, but a feature of
  Couchbase indexing"), which documents a type/non-type boundary this registry had
  only inferred. Its three files are the three copies of one page. **1 independent
  source.** Refused. A perfect quote is not a second witness.
- **`index:sequential-scan`: promoted on a rejected discount.** Two files at 0.88
  similarity, so the discount would cut it to 1. `--check` returns `divergent`, and
  the detail is the vindication: of 23 relations citing it, nine rest on sentences
  present on one copy and absent from the other, and the nine are *exactly the
  product adaptation* — Capella's are billing plans, access surfaces and cluster
  credentials; the server's are the feature controller and the global default. Two
  authors adapted one skeleton. The shared 12% is the skeleton.

**Measured inflation, corpus-wide:** 40 clusters covering 85 extracted pages; **188
ids** whose recurrence rests partly on a shared source (`shared` 101, `divergent` 83,
`unchecked` 4); **38 ids fall below the bar** once the discount is upheld. Before this
round the same instrument reported 36 clusters, 91 ids and 5 below the bar — so
extracting a module that exists in three trees roughly doubled the discounted set.
That is the honest cost of this round's shape: **re-extracting a page's twin buys
density, not independence.** `groupby-aggregate-performance.md` is the extreme case —
1730 body lines, similarity **1.00** between products, 102 relations extracted across
the two copies, and one authored source. (Checked before filing: it mentions
"Couchbase Server" zero times, so it is genuinely product-neutral, not a leaked Server
page. The round nearly filed an unadapted-content issue that does not exist.)

### Bug #12, and bug #13 inside the detector for bug #12

**#12, namespace-fork deflation.** `variant_key()` strips punctuation but keeps the
prefix, so `index:early-filtering` and `n1ql:early-filtering` never cluster: a fork
splits one term's files across two rows, and a genuine candidate sits below the bar
*twice*, reading as two weak terms rather than one adequate one. Sixteen rounds had
an instrument for the opposite error and none for this. `--forks` reports **63 local
names spelled in more than one namespace, 20 of which would cross the bar only if
merged**. It is a list to check, not a defect list — the registry deliberately keeps
five unrelated things called "role" apart, and this round confirmed
`data:kv-range-scan` / `sdk:kv-range-scan` and `index:index-partitioning` /
`fts:index-partitioning` are genuinely different things that any suffix-comparing
tool will flag.

**#13, and it is #12's own shape occurring inside the tool built to find it.** The
first `--check` report printed `**BELOW THE BAR**` whenever the *discounted* count
fell under 2, regardless of the row's verdict. So `index:sequential-scan  2 -> 1
divergent` rendered as a refusal justified by a number the same line had just
rejected. Round 17 was one step from refusing a candidate its own instrument had
vindicated. Fixed by adding `effective()`, which makes the verdict decide which count
applies, plus seven selftest checks built from the real rows. Easy to write because
the discount is the interesting computation, so the report was built around it and
`--check` was bolted on as an extra column rather than as the thing that decides which
column counts. **Quiet deflation is the failure mode this project keeps producing: it
removes real evidence and leaves no trace.**

### The six sentences that license a merge, never once enumerated

The reconcile skill forbids merging two concepts "unless a source page states the
relationship explicitly". Seventeen rounds applied that as a test to *fail*: an agent
proposes a merge, no citation surfaces, the collision is documented, the terms stay
apart. Nobody asked it the other way round — **which sentences in the corpus grant the
licence?** Grepping the handful of phrasings a technical writer uses for a synonym
returns **six results in the entire corpus**, now recorded in
`concepts/terminology-equivalences.json`. Small enough to read in a minute, and a grep
away for seventeen rounds.

Four of the six are on one page, for a structural reason: `cloud/management-api-reference/index.md`
documents API field names, so wherever a field name differs from the documentation's
word it says so. **It is a Rosetta stone**, and it should be mined deliberately rather
than stumbled upon. It settled two things immediately:

> The options may also be referred to as Memory and Disk (Couchbase), Memory Only
> (Ephemeral) in the Couchbase documentation.

which folds Capella's `bucket:memory-only-bucket` into the promoted
`bucket:ephemeral-bucket` as a **cited** alias — and it matters, because
`query-without-index.md` states the same restriction on sequential scans in each tree
using each noun, so without that sentence the registry would have recorded two
unrelated-looking constraints. And:

> A cluster may be referred to as a "database" in the documentation and in the
> Couchbase Capella user interface.

which is recorded but *not acted on*: `capella:cluster` sits at 1 file and is not
promoted, so there is no record to attach it to. That is the case the new record
exists for — **a refusal to merge is invisible in the output**, two separate records
look exactly like two distinct concepts, so the cost of not knowing a licence exists
is a permanent silent duplication.

### Promotions

**The pushdown family (7), and the question three rounds deferred.** Rounds 11–16 kept
meeting individual pushdowns at recurrence 1–3 with no page that recognised them as a
family. `index_pushdowns.md` *is* that page — the family is its title, its lede and
its six H2 headings — and it had never been extracted. **The family was not
undocumented; it was unread.** Promoted: `index:index-pushdown` (6, divergent),
`index:predicate-pushdown` (6, divergent), `index:group-aggregate-pushdown` (4),
`index:pagination-pushdown` (3), `index:index-projection` (3),
`index:order-pushdown` (2), and `index:operator-pushdown` (1, family exception),
whose members `n1ql:min-pushdown` and `n1ql:max-pushdown` are **promoted in their own
right at 3 divergent files each** — better attested than the term that collects them.
Filing them took a correction to this round's own first pass, and it is the promotion
rule applied upside down: the family record was written at recurrence 1 under the
exception while stating in its own `recurrence_note` that two of its members clear the
bar, and then leaving them unfiled. **A `members` list is not reachable by alias
resolution and does not stand in for a record** — an agent reusing `n1ql:min-pushdown`
would have truthfully declared `extraction-layer` for a term reconciliation had already
decided about. The family record still earns its place: `n1ql:count-pushdown` and
`n1ql:count-distinct-pushdown` really are at 1 file each, and it is the only thing that
makes them reachable.

Both members carry a caveat the round writeup should not absorb: their three files are
three copies of one authored page across two products and two releases, and the
`divergent` verdict is honest — 7.2 carries version history 8.0 deleted, 8.0 carries
collation statements the others lack — but **divergence across releases of one lineage
is a weaker independence than two separately authored pages.** One editor changed one
page over time. Recorded on the records so a later round revisits it rather than
rediscovering it.

It is *defined twice*, which is why no count found it: `groupby-aggregate-performance.md`
also claims the family in its own abstract, while `index_pushdowns.md` mentions
grouping and aggregate pushdown only under Related Links. Each page presents itself as
the family's home and the other as a sibling topic. **A recurrence count sees a term
used, not a term owned.**

**Index types (4):** `index-type:composite-secondary-index` (5 independent sources —
the round's best-attested promotion), `index-type:array-index` (3),
`index-type:functional-index` (2), `index-type:partial-index` (2). The last is worth a
note in the other direction: its second source is a Capella *guide*, not a second copy
of a reference page — two genres about one feature, which is stronger corroboration
than a duplicate would be, and **the promotion rule cannot see that distinction
either.** The proxy sometimes understates independence.

**Scan mechanics (2):** `index:index-span` (4), folding **five** ids for one concept
(`n1ql:span` from the 7.2 round, `index:index-span` from the Capella round, plus
`index:exact-span` and `index:exact-index-span` minted concurrently by two agents in
*this* round, none aware of the others); and `index:sequential-scan` (2), which also
turns round 12's re-filing of `role:query-use-sequential-scans` out of `privilege:`
from a judgement call into a documented correction — the page calls it a role, in bold,
twice.

**The plan-field family (2):** `concepts/query-plan-index-fields.json` as a scheme plus
`index:covers-plan-field` (3), the only member clearing the bar alone. Agents proposed
a `plan-field:` namespace for these; refused, because that is precisely bug #12 and
this round built the instrument that finds it. The asymmetry recorded there is the
interesting part: these eight fields appear in well over a hundred plan listings across
five pages and are **documented far better than they are defined** — `filter_covers` is
defined by analogy to a field that is itself never defined, and `exact` is shown thirty
times on the page that owns it and explained only on the page that consumes it.

**Predicates (3):** `indicatesInQueryPlan` (8 — the highest of any unpromoted predicate
in the corpus; every other predicate says what the product *does*, this one says what it
*shows*, and the indexing documentation is built on that distinction),
`appliesToIndexType` (4), `eliminatesFetchFrom` (3 — it finally distinguishes *covering*
an index, where the fetch never happens, from *pushing down*, where it happens on fewer
documents).

**Cited aliases (2):** `bucket:ephemeral-bucket` ← `bucket:memory-only-bucket`,
`bucket:couchbase-bucket` ← `bucket:memory-and-disk-bucket`.

**Deliberate refusals**, all for lack of *independent* sources rather than lack of
importance: `index:duplicate-index` (1), `index:composite-predicate-pushdown` (1, though
the 8.0 page grew a whole section for it between releases), `index:early-order-and-pagination`,
`index:empty-span`, `index:span-inclusion` (a genuine closed 0–3 value set, attested
once — the best candidate for a later round), `index:span-combination-rules`,
`index:full-index-scan`, `n1ql:count-pushdown`, `n1ql:count-distinct-pushdown`,
`n1ql:skip-key-range-scan`, `n1ql:array-agg`, `index:index-storage-setting` (1 — the top
level of the storage stack is real, its *name* is not yet earned), and
`isSupportedOnStorageMode`. `requiresMinVersionFor` remains unpromoted at 5 files: it is
a fold into `availableSince`, not a candidate.

### New `docs-issues/` (11, taking the total to 116)

- `server-sequential-scan-switch-on-procedure-uses-xor` — **the round's most
  consequential defect, and the only one where following the documentation produces the
  opposite of the stated outcome.** The N1QL Feature Controller is a disable mask.
  "Switch off" correctly says OR with `16384`. "Switch on" says **XOR** — which toggles,
  not clears; the correct operation is AND NOT. Example 6 hides it by assuming the bit is
  already set. Starting from `76` — the value the page's own Example 5 uses as a typical
  enabled state — the documented procedure yields `16460` and **disables the feature the
  reader was trying to enable**. It is a bitmask controlling unrelated query features, and
  the page says the setting is "usually reserved for support purposes", so the reader most
  likely to run it is an administrator on a production cluster.
- `server-n1ql-feature-controller-named-four-ways` — four surfaces, four spellings
  (`N1QL Feature Controller`, `--n1ql-feature-control`, `queryN1QLFeatCtrl`,
  `n1ql-feat-ctrl`), on a bitmask. Compounds with the above: the procedure is wrong *and*
  the thing it operates on is named differently everywhere. Found *from* the page's own
  Table 1, which is good documentation; the defect is upstream, in the product's naming.
- `server-groupby-table1-contradicts-examples` — Table 1 marks SUM/COUNT unsupported for
  the commonest case, which thirteen of the page's own examples demonstrate. **The
  extracting agent deliberately refused to extract it**, to avoid putting "a false
  negative into the ontology with a quotable citation behind it" — the exact failure the
  evidence gate cannot catch, because the quote is verbatim and the table is really there.
- `server-groupby-array-agg-documented-three-ways` — supported, unsupported, and
  unsupported-in-all-four-columns, in three places on one page.
- `server-index-scans-prose-contradicts-tables` — four prose/table disagreements, all
  surviving in all three copies. One (Example 8) is not wrong but under-specified: the two
  answers describe two stages of one transformation and the page presents them as one.
- `server-index-scans-exact-flag-undefined` — the flag that decides pushdown versus early
  filtering, shown ~30 times, defined on another page.
- `server-index-scans-no-related-links` — the module's hub page is the one page with no way
  out of it; all four siblings link into its anchor. Three different link conventions
  across five pages.
- `server-index-pushdowns-version-facts-removed` — the 5.5 MIN/MAX history was **deleted**
  between 7.2 and 8.0. Consequence for this registry, recorded rather than tidied: the
  existing 7.2 record asserts `availableSince version:server-5-5` on a sentence that no
  longer exists. **The first case in the POC of a correctly-extracted, still-true relation
  whose evidence was deleted upstream — and nothing distinguishes "unquotable because
  fabricated" from "unquotable because the docs changed."**
- `server-indexcountscan3-absent-from-plan-output` — two callouts name an operator that
  appears in no plan on the page. Noted alongside a real gap: no scan-operator enum exists
  anywhere, though five operators are cited as decisive on three pages.
- `server-indexes-module-service-naming-drift` — eight names for three services across five
  pages; two are outright wrong ("The SQL++ indexer will do 2nd level of aggregation",
  contradicted by the page's own Example C).
- `capella-groupby-page-published-verbatim-in-two-products` — 1730 identical lines.

Updated rather than duplicated: `server-index-state-vocabularies-inconsistent` gains
round 17's third and fourth senses of "index state" and the sentence that **kills the
simplest reconciliation** — "the indexer goes into the Paused mode on that node. Although
the indexes remain in `Active` state, traffic is routed away from the node." Paused (the
indexer) and Active (the indexes) hold *simultaneously*, so they cannot be members of one
value set. A page titled "Index Lifecycle" names zero states in either tree, modelling
four activities with phases instead: the lifecycle docs and the registry are not
disagreeing about values, they are modelling different things, and nothing joins them.

### The two gate denials

Both legitimate catches, both fixed by the agents, no relation lost and no evidence
reworded:

1. `cloud/indexes/groupby-aggregate-performance.json` — invalid JSON (a missing brace).
   Re-issued identically with the brace: `deny(n_relations=null)` → `allow(39)`.
2. `server/8.0/indexes/storage-modes.json` — declared `minted` for `usesEnum` when only
   its *objects* were new. **A relation's `registry_status` describes the predicate, not
   its objects.** Changed to `promoted`, explanation moved into
   `reused_or_minted_predicate`.

A third denial, on `groupby-aggregate-performance.json` in the server tree, is the most
interesting of the round: the agent quoted the DISTINCT Case-2 rule as
"the leading GROUP BY key(s) + 1 (the immediate next key)" — a conflation of the page's
*two* statements of the same rule, which differ in wording and capitalisation. The gate
refused it, the agent re-read and quoted one verbatim, and recorded the discrepancy as a
defect. **This is the gate catching a fabrication assembled entirely from real fragments
of the page it cites** — the shape closest to undetectable by review.

### What this round taught about the method

- **A metric's proxy fails in both directions, and only one direction had an
  instrument.** "Two distinct files" stands in for "two independent attestations". Shared
  source inflates it; namespace forks deflate it; a page published verbatim in three trees
  is one witness while a guide and a reference page are two. Seventeen rounds ran with an
  instrument for neither, then built both in one round and immediately reversed four
  decisions. The lesson is not "the rule was wrong" — it held up well — but that **a proxy
  with no error bars is reported as a measurement.**

- **The evidence may already be written down somewhere the tooling does not read.** The
  three storage engines were correctly identified, quoted and reasoned about in round 16,
  in a `docs-issues/` file, and sat at recurrence 0 because `recurrence.py` reads
  `extractions/`. Promotion decisions made from one directory will keep missing what the
  project already knows.

- **Ask an evidentiary rule the other way round.** "Never merge without a citation" was
  applied as a filter for seventeen rounds without anyone enumerating the sentences that
  provide one. There are six. The cost of that gap is invisible by construction: a refused
  merge and a genuine distinction look identical in the output.

- **A partial measurement of inflation is worse than none.** Both of the round's reversals
  only became visible with all 22 records on disk. A discount subtracted from an incomplete
  count is not conservative; it is meaningless, and it errs toward discarding real terms.

- **The tool built to catch a bias can embody it.** `--check` marked a vindicated candidate
  as below the bar using a number its own verdict had rejected, because the report was
  organised around the interesting computation rather than around the decision. Selftests
  built from real rows caught it; nothing else would have.

## Round 18 — the eventing module: first contact, paired with round 8's twin

**Scope.** 67 pages, `server/8.0/eventing/` + `server/8.0/eventing-rest-api/`, first
contact — never extracted before this round. Paired against round 8's already-extracted
`cloud/eventing/` (67 pages, same feature, same page structure, most of them
byte-identical filenames). 400 relations, 0 evidence problems, 8 gate denials all
fixed at the same relation count (no thinning). This is the shape round 17 recommended
for round 18 explicitly: run first contact on a module whose twin is already
extracted, so each tree is the other's diff-gate.

**The density result was smaller than round 17's, for a reason worth recording rather
than treating as a shortfall.** Server's 400 relations over 67 pages (mean 5.97)
against Capella's round-8 244 (mean 3.64) is a real 1.64× improvement, not the 9.8×
recovery round 17 found on the indexes module. The difference is the material: over
40 of these 67 pages are individual JS handler code-sample pages, several of them
genuinely and honestly near-empty (`eventing-handler-dateToEpochConversion.md`,
`eventing-handler-deepCloneAndModify.md` and four others extracted at **0
relations** — pure data-transformation JavaScript with no Couchbase-specific
mechanism to extract). A thin record is not a defect when the page has nothing to
say; round 17's own reconcile skill says this and round 18 is the clean
demonstration. The densest pages (`eventing-Terminologies.md` at 34,
`eventing-rest-api/index.md` at 24, `eventing-language-constructs.md` and
`eventing-debugging-and-diagnosability.md` at 22) are the reference/terminology
pages, exactly where round 17's density gain also concentrated.

### Four handler entry points, not two, and a fork no existing instrument catches

Round 8 promoted `eventing:on-update-handler` and `eventing:on-delete-handler` as
*the* Eventing handler pair. Round 18 found two more, on pages round 8 had already
extracted: `eventing-Terminologies.md` states plainly — "The Eventing Service calls
the OnUpdate, OnDelete, **and Timer Callback** handlers on mutations and fired
timers" — three explicit handlers in one sentence, on a page read in round 8, and
only two of the three were ever filed. **OnDeploy** is even easier to miss: its own
page (`eventing-lifecycle.md`) frames it as a *lifecycle step* ("runs once when a
Function is deployed or resumed") rather than as a handler, so an agent reading only
that page reasonably extracts it under `createsOnAction`/`behavesDifferentlyUnder`.
It took the Terminologies glossary, on a different page, to state it as a fourth
entry point in the same breath as the first three. `concepts/eventing-handler-family.json`
now holds all four; each is promoted separately.

Two of the four were independently minted **twice**, under names neither existing
instrument catches, and the two misses are different species:

- `eventing:on-deploy-handler` (round 18, server) vs. `eventing:ondeploy-handler`
  (round 8, cloud) — a pure hyphen difference. **`recurrence.py --variants` catches
  this one.** Resolved the way round 8's identical `onupdate-handler`/`ondelete-handler`
  slip was resolved: rewritten via `normalise-ids.py`'s `ID_RENAMES` table, not
  aliased — `verify-registry-ids.py` correctly refused the alias as a mere
  punctuation variant of its own target, and the rewrite folded it automatically
  once no corpus occurrence of the old spelling remained.
- `eventing:timer-callback` (used with `firesCallback`, from the pages that
  demonstrate a Timer actually firing) vs. `eventing:timer-callback-handler` (used
  with `hasHandler`, from the pages that state the entry-point list) — **not a
  punctuation variant, and neither `--variants` nor `--forks` catches it.**
  `--variants` groups by stripped-punctuation string equality; `timer-callback` and
  `timer-callback-handler` share no such equality. `--forks` groups by
  cross-*namespace* forks; both already carry the `eventing:` prefix, so there is no
  cross-namespace signal to find. Two agents, reading the mechanism through two
  different predicates, minted two names for it, and it is a genuinely new species
  of fork — **a same-prefix synonym fork**, distinct from bug #12 (cross-namespace)
  and from an ordinary spelling variant. Zero file overlap between the two names —
  16 distinct files once merged, spanning both code-sample pages and reference
  pages, which is a *better* independence signal than a duplicate pair would give.
  Folded by hand; no instrument exists yet that would have found it un-prompted.

The same genre-fork shape recurred at smaller scale on three Advanced Keyspace
Accessor operations: `eventing-advanced-keyspace-accessors.md` (the operation-list
overview page) names LookupIn, MutateIn and Touch generically, while each
operation's own worked-example page (`eventing-handler-advancedLookupInOp.md`,
`-advancedMutateInArray.md`/`-advancedMutateInField.md`, `-advancedTouchOp.md`)
independently minted its own name for the identical mechanism. All three folded
(`eventing:lookupin-operation`, `eventing:mutatein-operation`,
`eventing:touch-operation`), each promoted at 3-4 files with zero overlap between
the folded pair. **A reference/overview page and a worked-demonstration page
naming the same mechanism is now a recognised, recurring shape, not a one-off** —
four instances in one round, all invisible to the same two instruments, all found
only by reading records side by side.

### The corpus's most heavily duplicated module yet, and what that does to the promotion metric

`shared-source.py --clusters` went from 40 clusters/85 pages (round 17) to **91
clusters/187 pages** in this round alone — the `eventing:` module's Server/Capella
page pairs measure **0.89 to 1.00 similarity**, higher and more uniform than the
indexes module's spread (0.16-1.00). Most of these 65 page-pairs are not merely
similar, they are close to verbatim republication: `--check`'s own diagnostic line
reads "all N quotes appear on every copy" for the overwhelming majority of
eventing-namespaced ids, where round 17's index module returned a healthy mix of
`shared` and `divergent`. The discounted-id count rose from 188 to **272**, and the
below-the-bar count from 38 to **89** — a bigger jump than round 17's, on a
smaller-page module, because eventing's Server and Capella docs are simply closer
to one authored source republished twice.

This matters for how the pairing strategy itself should be read going forward:
**round 17's recommendation — run first contact on a module whose twin is already
extracted, because each is the other's diff-gate — worked exactly as prescribed for
finding *content* defects (11 docs-issues, the RBAC-gate asymmetry, the LCB error
code inconsistency), and did nothing to buy *independence* for newly-minted
concepts, because this particular module's independence was never there to buy.**
The strategy's payoff has two separate axes — defect-finding and promotion
evidence — and round 17's indexes module happened to deliver on both; round 18's
eventing module delivered on the first and not the second. A handful of round 18's
concepts cleared the bar anyway, either because they had a real second, differently-
framed source (the four-instance genre-fork pattern above) or because they were
attested on genuinely distinct pages beyond the duplicate pair
(`eventing:function-scope`, `eventing:listen-to-location`, both `divergent` at 7→5).
Most of what a single duplicate pair minted on its own did not.

### Promotions

**The handler family (2 new members + 1 scheme):** `eventing:on-deploy-handler` (5,
folding `eventing:ondeploy-handler`) and `eventing:timer-callback` (16, folding
`eventing:timer-callback-handler`) join the already-promoted OnUpdate/OnDelete pair
under `concepts/eventing-handler-family.json`.

**Function-configuration concepts (4):** `eventing:eventing-storage` (17→13, the
metadata bucket/scope/collection a Function uses as a scratchpad — deleting it
undeploys *every* Function using it, cluster-wide, a hazard stated only in the
terminology glossary and nowhere on the settings page itself);
`eventing:function-scope` (7→5, divergent, the RBAC-grouping bucket.scope pair — the
wildcard `*.*` form requires Full Admin or Eventing Full Admin);
`eventing:listen-to-location` (7→5, divergent, the DCP mutation source, explicitly
distinguished from a binding); `eventing:deployment-feed-boundary` (4→2, exactly at
the bar, the Everything/From-Now DCP-replay setting that doubles as the Paused-resume
checkpoint marker).

**Operation/mechanism concepts (6):** the three Advanced Accessor genre-folds above
(`lookupin-operation`, `mutatein-operation`, `touch-operation`);
`eventing:meta-keyspace-parameter` (4→2, exactly at the bar, the required argument
for a wildcard-scoped binding); `eventing:n1ql-result-iterator` (5→3, the cursor
object `requiresExplicitClose` already governs — and one page in its own batch
doesn't close it, filed as a docs-issue); `eventing:recursive-mutation` (6→4, a
correction to round 8's own record, which had filed it under `shouldNotBeConfusedWith`
— reserved for two things a reader might wrongly conflate, not a hazard a Function
can exhibit — refiled under `createsOnAction`).

**Error concepts (2):** `eventing:lcb-key-eexists-error` and
`eventing:lcb-key-enoent-error` (5→3 each), the two libcouchbase KV errors surfaced
to handlers — `EEXISTS` is overloaded across two conditions (CAS mismatch on a
conditioned write vs. duplicate key on insert) with no shared predicate to
distinguish them, and its numeric code is documented inconsistently across two
sibling pages (docs-issues below).

**A generalisation of an existing record:** `eventing:cas-conditioned-write` widens
round 8's `eventing:cas-conditioned-delete` to cover the near-identical harness
`eventing-handler-advancedReplaceOp.md` demonstrates for REPLACE. Round 8 had reasoned
the DELETE version was "standard Data Service optimistic-concurrency behavior, not
Eventing-specific" and left REPLACE's version unmodeled entirely; this round's own
extraction of the REPLACE page kept that call for consistency, but flagged the
asymmetry explicitly rather than repeating it silently — **applied evenly, that
reasoning should mint neither page's harness or both**, and reconciliation chose
both, generalizing the name rather than leaving one operation's evidence stranded
under the other's id.

**One concept:** `eventing:visual-debugger` (3 files, no shared-source discount —
its files aren't a duplicate pair). Corrects this round's *own* dispatch framing:
the briefing treated `eventing-debugging-and-diagnosability.md` as Server-only
evidence for a Server-only debugger, but Capella's own `eventing-Terminologies.md`
glossary describes the identical mechanism in one entry rather than a dedicated
page. **"No twin page" does not mean "no twin feature"** — what is genuinely
Server-only on that page is the node/OS-administration content (`static_config`
editing, NAT workarounds, log paths), not the debugger itself.

**A same-round self-fork, folded without a merge decision:** `eventing:bucket-binding`
(5 files, minted in round 8) turned out to be round 8's own restatement of round 8's
own already-promoted `eventing:bucket-alias-binding` — the same mechanism minted
twice **within one round**, not across two. Folded as an alias into the existing
promoted record; no new concept.

**Deliberately not promoted:** `eventing:rest-api` and half a dozen node-administration
concepts (`worker-process`, `eventing-producer-process`, `residency-ratio`, and
similarly) sit at 1 file each — real, but this round's REST API page is the corpus's
only extraction of that surface, and Capella genuinely has no equivalent (node-topology
controls a managed service cannot hand to customers). `writesToBinding` (2 files, no
server-side reuse this round) and the ~25 ids the shared-source discount actually put
below the bar (full list in the shared-source.py run) stay in the extraction layer.

### New `docs-issues/` (12, taking the total to 128)

- `server-eventing-worked-examples-rbac-gate-missing-from-capella` — **the round's
  structural headline.** All nine Server worked-example pages carry the identical
  sentence gating Function creation behind Full Admin/Eventing Full Admin; every one
  of their Capella twins is silent on any equivalent gate, and round 8's own
  extraction had flagged "no privilege/capella-role gate anywhere" as an unexplained
  absence. Now explained: Capella's access model for Eventing is project-scope
  roles (Data Reader/Writer/Project Owner), a materially different shape from
  Server's classic cluster-wide role catalog plus per-scope RBAC grouping — not a
  documentation gap, a real product asymmetry.
- `server-eventing-memory-quota-premise-contradicted` — this round's *own* dispatch
  briefing reasoned that `eventing-memory-quota.md` has no Capella twin because
  Capella manages memory automatically, and never checked that premise before
  acting on it. Capella's own `eventing-faq.md` states a user-configurable
  256MB→512MB memory-quota knob in near-identical wording to the Server page. Either
  the automatic-management premise is wrong, or Capella's FAQ carries stale
  un-adapted Server language describing a control Capella customers cannot reach —
  filed `needs-sme` because no page resolves which, and recorded plainly as a
  briefing error this round made and then caught by reading the pages it named.
- `server-eventing-lcb-error-code-inconsistent` — the identical `LCB_KEY_ENOENT`
  error object is documented with `"code": 272` on one page and `"code": 1` on its
  sibling in the same batch.
- `server-eventing-advanced-keyspace-accessors-orphaned-version-badges` — four
  "Couchbase Server 7.6/7.6.2" version-since badges on Capella pages with zero
  matching mentions on the byte-identical-otherwise Server 8.0 twins, on four
  separate pages — consistent with a version-since macro rendering on the Capella
  build and not the current Server build, rather than four independent omissions.
- Five smaller, concretely diagnosed inconsistencies: a copy-paste log message
  (`advancedDecrementOp` logs "increment"), an undocumented third `OnUpdate`
  parameter on one handler page inconsistent with every sibling's two-argument
  signature, a worked example whose cleanup instructions name the *other* example's
  Function, a goal description ("redact sensitive data") that doesn't match its
  handler's actual behaviour (domain normalisation, no redaction), and a role
  display label that doesn't match `roles.md`'s own canonical spelling.
- Two REST/config-surface findings: an internal port/path inconsistency within the
  REST API reference itself (8091/`_p/event` vs. 8096/`api/v1` for the same kind of
  setting), and one N1QL()-call worked example that never closes its result
  iterator where three siblings in the same batch do.
- One duplication finding **corrected rather than newly filed**: round 8's Capella
  extraction characterized a broken cross-reference on
  `eventing-buckets-to-collections.md` as Capella-specific unadapted content; this
  round confirms the identical broken link is present on the Server 8.0 original,
  so it is a pre-existing defect in the shared source, not something Capella's
  adaptation introduced.

### What this round taught about the method

- **A pairing strategy's payoff has two independent axes, and a good result on one
  round does not transfer to the other.** Round 17 recommended "first contact on a
  module whose twin is already extracted" because it delivered on both
  defect-finding and promotion evidence at once. Round 18 shows the two can split:
  the eventing module delivered eleven real docs-issues and the RBAC-gate finding —
  defect-finding worked exactly as prescribed — while its near-total
  cross-product duplication (0.89-1.00 similarity, "all quotes appear on every
  copy") meant most newly-minted concepts got no independence boost from the pairing
  at all. **The strategy is still right; its output has to be read on two separate
  meters, not one.**
- **A same-prefix synonym fork is a fourth failure mode, and nothing catches it
  yet.** Bug #12 (cross-namespace fork) has `--forks`. An ordinary spelling variant
  has `--variants`. This round found a third shape — two agents reading the same
  mechanism through two different *predicates* (`firesCallback` vs. `hasHandler`)
  and minting two names that share a prefix and share no substring — four times in
  one round, at zero file overlap each time, meaning zero collision-detection signal
  for either existing instrument to work from. No script is proposed for it here;
  the pattern (a reference/overview page names an operation generically while its
  own worked-example page names it specifically) is at least now a named thing to
  read for, the way "extraction record vs. registry" collisions became a named thing
  to read for after round 12.
- **The briefing itself is not exempt from the "verify before recommending" rule.**
  Round 18's own dispatch prompt asserted a Capella/Server asymmetry (no memory-quota
  twin because Capella auto-manages memory) without checking the claim against
  Capella's own pages first — and one of the five batches, reading the Capella FAQ
  for background as instructed, found the premise contradicted. **A round's framing
  paragraph is a hypothesis with the coordinator's own name on it, and it is exactly
  as unverified as anything an extraction agent might assert** until a page confirms
  it.

## Cumulative verdict (all eighteen rounds)

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

Round 14 is the second such round, and it found that the audit itself had a blind
spot of the same kind. Working the backlog *by namespace* rather than by rank -
the discipline round 10 arrived at when it refused 93 individually-correct index
concepts - turned up two things no amount of reading records one at a time would
have: a namespace whose name asserted an axis it did not hold (`vector-index:`,
30 members answering five different questions, two of them already promoted under
a minority spelling in another prefix), and a promotion metric in which round 11's
exclusion of documentation pages had been silently cancelled by round 12's
broadening of the slots, so that 27 of 203 backlog items were page ids counted as
concepts. Both defects were *invisible per-item and obvious per-namespace*, which
is the argument for the unit of work rather than for more care. The round also
found the same finding written down three rounds earlier, in the right words, by an
extraction agent - "FOUR NAMESPACES, ONE LIST ... the fix is a reconciliation
decision" - and never acted on, because its remedy was to refactor already-promoted
records and reconciliation had no output shaped like that.

It then did the same thing to itself, which is the part worth keeping. This
section's own `docs-issues/` subsection named four new entries; writing the files
closed none of them, because two were findings about *this registry* wearing a
docs-issue's clothing and two were plainly wrong about the page they described - and
`verify-promotions.py`, the control that exists precisely to catch "narrated as
promoted, never filed", reported nothing, having only ever scanned for concept ids
and predicate names. So a round auditing the registry for coherence produced, in its
own writeup, an incoherence of exactly the kind it was hunting, in the one artefact
family no control covered. The check now covers docs-issue slugs too. The durable
lesson is not about care: **a control's coverage is itself an unchecked claim**, and
the way to find out what a control does not look at is to be wrong in that place
first.

Round 15 is the third registry-input round and the one that says something about
the *measurement* rather than about the registry. Wave 2 dissolved a 34-member
namespace, 31 of whose members sat at recurrence 1 — so the largest single piece of
incoherence found in three audit rounds was, throughout, invisible to the count
that exists to find work. Three distinct reasons why are now on the board and they
generalise past this namespace: the promotion rule is per-item, so a namespace can
be built entirely from items that never come up for a decision; a canonical
reference table mints its rows at recurrence 1 *by construction*, which means the
better a thing is documented the less promotable it is; and pages duplicate each
other, so one editorial statement on two pages counts twice. Together with round
14's finding that the backlog can only contain terms an agent actually minted,
that is four ways the metric misreports, all of the same species: **recurrence
measures repetition, and repetition is an editorial property of the documentation
rather than a property of the concept.** Nine rounds treated it as the latter.

The round also found the audit-of-the-audit result that follows from round 14's:
the instruction to scope `verify-evidence.py` to the round's new batch quietly
assumes a round has one. Round 14 had none, promoted 18 concepts out of records
written before any gate existed, and two defects in one of those records survived
to be found here — one of them a quote that is verbatim on the wrong page, which
cost a recurrence, and one a paraphrase presented as a quotation inside a
*promoted* record, the one artefact family the write-time gate does not read. So
the quotability check moved onto the path a coherence pass actually walks
(`candidate-evidence.py --audit`), and the two id-shape defects the waves keep
paying to repair moved to write time, scoped to new mints only so that reuse — and
therefore repair — stays legal. Testing that gate change turned up the last small
surprise: replaying a real record through the gate now fails, because
`registry_status` is a claim about a registry that grows. **A control's verdict can
expire**, which is worth knowing before someone reaches for a cheap green script as
an audit.

Round 16 is the fourth registry-input round, and it lands on the *instruments*
rather than on the registry or the metric's subject matter. Three of them turned out
to be reporting something other than what their labels said, and in each case the
label was written by this project:

- The column headed **"any mention"** had not been any mention since round 14. One
  `keep` flag in a shared code path excluded `seeAlso` from a metric — correctly — and
  from the census, silently. 376 ids, 18% of the corpus, appeared in **no report this
  project produces**, including the one whose whole job is to enumerate spellings.
  Five misspellings of promoted SQL++ statements were sitting in that gap, each one
  causing gate denials nobody could account for, and a concept at 14 files reading as
  recurrence 0.
- The **shadow-prefix count** quoted in the last two writeups was measured with the
  same blind instrument: 43 becomes 55 with no change to the corpus.
- A **`recurrence` field in a promoted record** is a measurement with a date and no
  instrument recorded, and 171 of 324 no longer agree with the query. None of them is
  wrong. But a record's prose reasons about its own weight — "a minor, low-stakes
  promotion", written of a term at recurrence 8 — and reconciliation reads the prose.
  This section's own first draft believed a stale field over the query and wrote a
  false causal story from it, which is as clean a demonstration as the failure allows.

Rounds 13-15 each found the audit looking in the wrong place; this one found it
looking through the wrong lens, three times, and the generalisation is narrower and
more useful than "check the code": **excluding a relation kind from a metric and
excluding it from a census are different decisions, and doing the first by editing a
shared code path silently does the second.** Every number in a writeup inherits the
instrument that produced it, and nothing in this pipeline records which instrument
that was.

The round's substantive finding is separate and simpler, and it is the one that sets
round 17's scope: **the corpus is not the documentation.** `server/8.0/indexes/` — 11
pages, the canonical documentation of indexes, the subject this wave spent its entire
length reorganising — has never been extracted, because round 12 walked `learn/`
looking for those pages after Antora had already moved them out of it. So every
recurrence count in the wave is a fact about which directories nine rounds happened
to walk. Round 15 established that recurrence measures repetition rather than
importance; round 16 adds that it measures repetition *within the sample*, and that a
coverage plan built from directory names inherits every reorganisation the docs have
undergone. That is also, exactly, why `covering-index` was spelled five ways across
three namespaces: **an id names its subject, not its location.**

Round 17 acts on that and returns the first quantified answer to the question the
previous four rounds could only pose. `server/8.0/indexes/` extracted as **first
contact** yields 400 relations over 11 pages, mean 36.4 against round 10's baseline
of 13.4; the same 11 pages of `cloud/indexes/`, extracted pre-gate, held 35 relations
and now hold 343. **A 9.8× recovery from re-reading pages the corpus already
covered.** So the hole round 16 identified was not a rounding error in the coverage
plan, and thinness in the corpus was, in this case, worth nine tenths of the content.
The round's substantive results follow from that directly: the pushdown family had
been met at recurrence 1-3 for six rounds because the page whose title, lede and six
headings define it had never been read; the three storage engines settle a ruling
round 16 made correctly and could not promote, because a **one-to-many map** - one
storage setting implemented by Plasma in Enterprise Edition and Forestdb in Community
Edition - forecloses the fold that a decade of "storage mode" prose invites.

The engines are also the round's sharpest methodological finding, and it is not about
coverage. Round 16 had already quoted the decisive page and reached the right
conclusion, **in this repository, in a `docs-issues/` file**. The terms nonetheless sat
at recurrence 0, because `recurrence.py` reads `extractions/`. The evidence was neither
missing nor undiscovered; it was in a directory the counting tool does not open. Round
16's lesson was that a refusal is only as good as the set it searched. This is the same
sentence one layer out: **a promotion is only as good as the set it counted**, and a
pipeline that decides promotions from one directory will keep re-losing what it has
already worked out.

Round 18 pairs the same strategy against a module where the answer comes out
differently, and the difference is itself the finding. `server/8.0/eventing/`
first contact yields 400 relations over 67 pages, 1.64× round 8's `cloud/eventing/`
baseline of 244 - a real gain, and much smaller than round 17's 9.8×, because most
of these 67 pages are individual JS handler samples and several are honestly
near-empty. The module also turns out to be the corpus's most heavily duplicated:
Server/Capella page-pair similarity runs 0.89-1.00, `shared-source.py` finds "all
quotes appear on every copy" on the overwhelming majority of its concepts, and the
below-the-bar count jumps from 38 to 89 in one round. **Round 17's pairing
recommendation delivered on defect-finding again - eleven docs-issues, the RBAC-gate
asymmetry - and did nothing for promotion independence, because this module's two
trees are close enough to one authored source republished twice that there was no
independence to buy.** A strategy that worked on both axes at once in round 17 is
shown, one round later, to have two axes that can come apart; reading a paired
round's output now means checking defect-finding and promotion-evidence separately
rather than assuming a good result on one implies the other.

Round 10 also changed what this project believes about its own reliability. Up
to round 9, the evidence quality of the corpus was assumed on the strength of
the extraction schema requiring direct quotes. It isn't: **313** of 3,522
relations quote text that does not appear on the page they cite, 130 more
carry no evidence at all (round 16 re-derived these; rounds 10-15 quoted 322
against a smaller corpus, and the figure was carried forward unrechecked), and two whole product trees from round 3
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
Round 15 completes the thought a third time, from the direction of the *metric's
subject matter* rather than its code: the query is correct and its input is now
consistent, and it still cannot see a 34-member namespace, because what it counts
is how often the docs repeat a term. Nothing is wrong; the number simply does not
mean what five rounds of promotions took it to mean. Round 16 closes the sequence a
fourth time, at the *labels* on the aggregates: the query is correct, its input is
consistent, its subject matter is understood — and two of its column headings and half
its recorded outputs described something other than what they contained. An aggregate
is code, its input is data, its subject matter is editorial, and **its label is a claim
nobody checks.** Round 17 closes it a fifth time, at the metric's *proxy*: "two distinct
files" stands in for "two independent attestations", and seventeen rounds ran with no
instrument for either direction in which that substitution fails. Shared source inflates
the count (one page published verbatim in three trees is one witness); namespace forks
deflate it (one term split across two prefixes sits below the bar twice); and a
reference page plus a guide are *more* independent than the number can express. Building
both instruments in one round immediately reversed four promotion decisions, in both
directions. The aggregate was correct, its input consistent, its subject matter
understood and its label accurate — and **a proxy with no error bars gets reported as a
measurement.** Round 18 closes it a sixth time, at a shape neither instrument built in
round 17 can see: two agents naming one mechanism through two different *predicates* -
`firesCallback` from the page demonstrating a Timer firing, `hasHandler` from the page
stating the entry-point list - mint two ids that share a prefix and share no substring,
so `--variants` finds no punctuation match and `--forks` finds no cross-namespace
signal. Four instances, one round, zero file overlap each time, caught only by reading
the folded pair side by side. `divergent`/`shared`/`unchecked` answers "does the
discount apply"; nothing yet answers "are these the same term."**

Twenty-nine limits of the method are now visible across multiple rounds, not just
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

  Round 15 states the general form, which subsumes both directions above:
  **recurrence measures repetition, and repetition is an editorial property of the
  documentation, not a property of the concept.** Four consequences are now
  observed rather than reasoned about. A term documented in exactly one
  authoritative place cannot reach the bar at all, so `query-settings.md`'s 34
  settings arrived at recurrence 1 by construction and a namespace's whole contents
  went five rounds without a decision - *the better the documentation, the less
  promotable its contents*. A term no agent ever minted has no row rather than a
  low one (round 14's QPS). A term whose spellings differ is several rare terms
  rather than one common one (`max-parallelism` at 1 + 1). And a term documented on
  two pages that carry byte-identical prose is two files and one statement, which
  inflated two of round 15's ten promotions - the CURL access-list table, and, from
  wave 1, `vector-search:product-quantization`, whose second file quotes a sentence
  that lives on the first. None of these is a bug in `recurrence.py`; all four are
  the metric answering the question it was asked.

- **A control's verdict can expire, and a verification instruction can assume a
  fact about the round.** Two halves of one limit, both found in round 15 while
  testing a gate change. The reconcile skill says to scope `verify-evidence.py` to
  the round's new batch - correct advice that verifies *nothing* when the round's
  input is the registry, which is what rounds 13, 14 and 15 are, and round 14
  promoted 18 concepts out of pre-gate records under it. And replaying a real
  extraction record through `gate-evidence.py` today produces false denials, because
  `registry_status` describes the registry the record was written against and the
  registry grows: a round-12 record allowed at write time now draws five. So the
  gate cannot be repurposed as a corpus audit, and old records must not be
  "corrected" to match today's registry - their declarations are a fact about when
  they were written. `verify-evidence.py` is the corpus-wide check precisely because
  its claim relates two fixed things and does not decay. The generalisation: **a
  check's scope, and the shelf life of its verdict, are claims as much as its
  result is** - and neither is visible in an exit status.

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

  Round 14 adds a second species, which is not mis-reading but
  **under-determination**: three `availableSince` relations in
  `use-vector-indexes.json` quote the identical table row
  `| **First Available in Version** | 8.0 | 8.0 | 7.6 |` as evidence for three
  different objects. All three are right, and nothing in the evidence could have
  told you if one were not, because the information that disambiguates the row is
  the *header row two lines above it* - the table's geometry rather than any
  quotable line. A gate that compares strings cannot reach this class at all: the
  quote is verbatim, on the correct page, about the correct subject, and supports
  any of three triples equally. Tabular evidence needs its header to travel with
  it, which nothing in the schema currently provides for.
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
- **The unit of reconciliation decides which defects are visible.** Thirteen
  rounds reconciled by *rank* - take the highest-recurrence candidates, decide
  each on its merits. Round 14 reconciled by *namespace* and immediately found two
  defects that are invisible per-item and obvious per-group: a prefix asserting an
  axis whose members answered five different questions, and a promoted term at
  recurrence 2 sitting beside its own unpromoted spelling at 5. Neither is a
  judgment anyone got wrong; both are questions the per-item view cannot ask. The
  corollary is uncomfortable: there are presumably other units of work - by
  predicate range, by source tree, by competency question - each of which would
  make a different class of defect obvious, and no reason to think the current
  three are the last.

- **A rule enforced on one slot of a record is not enforced on the record.** Round
  14 found one shape three times. `seeAlso` was excluded from the promotion metric
  in the object slot and not the subject slot, so page ids re-entered as link
  *sources* (bug #10). `providesIndexType` was checked as a predicate name and its
  object's namespace was not, so a record could assert that a service provides an
  index type whose id says it is not one. And "never write `current` into an id" was
  enforced on `page_id` and the output path while **86 `seeAlso` objects across 21
  files** name a page through the `current` alias. In each case the invariant was
  written down correctly and applied at the position where it was first violated.
  The general remedy is not more rules but stating each rule over *records* rather
  than over fields, which for the schema checks means the structural validation
  still missing from `gate-evidence.py`.

- **A record is evidence about a page, never a substitute for one.** Round 14 read
  no pages, wrote four docs-issues in prose from the extraction records, and could
  file none of them: two were registry findings in a docs-issue's clothing, and two
  were **factually wrong about the page** in ways only the page could reveal - a
  table row claimed not to identify its columns, which a header row two lines up
  does, and a concept described as "documented only as a link target" that has a
  dedicated 200-line page in both trees. Extraction records are lossy by design;
  they hold the sentences an agent chose to quote and none of the structure around
  them. So the reconciliation layer can reason about the *registry* from records
  alone, and cannot assert anything about the *documentation* without going back to
  the file. This is the mirror image of "an unmeasured docs-issue is a hunch with a
  filename" from round 13: measurement over records is necessary and, for claims
  about the docs, not sufficient.

- **Two correct fixes to the same query can cancel.** Round 11 excluded
  documentation pages from the concept ranking; round 12 broadened that ranking
  from one relation slot to either. Each was right, each was written up, and the
  second silently undid the first because the exclusion lived in the branch the
  broadening replaced. Two rounds of promotions then ran on a metric that counted
  page titles. What was missing was not care but a self-test pinning the *earlier*
  fix to a named instance, which is now what `--selftest`'s bug-#10 cases are.

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

  Round 14 adds a sixth, in the one artefact family nobody had thought to check:
  its own `### New docs-issues/` subsection named four entries and filed none, while
  `verify-promotions.py` reported nothing, because it scans for `ns:kebab-id` and
  `camelCaseTerm` and had never looked at docs-issue slugs. Three families are
  written by hand each round and the control covered two. Extending it took eight
  lines - backticked kebab slugs of three or more segments, minus the local names of
  concepts and predicates - and on its first run it surfaced exactly the four
  phantoms plus this file's reference to a fifth entry that never existed, inside 17
  candidates of which the other 12 are visibly prose. The lesson is the narrow one:
  **a control's coverage is a claim in itself**, and this one silently asserted that
  the only checkable claims in `reconciliation.md` were about concepts and
  predicates.

  Ten controls now exist where nine rounds had none: the write-time gate
  (`hooks/gate-evidence.py`, which since round 15 also refuses a new mint under a
  singular/plural fork of an existing namespace, or an id containing a file
  extension, and which since round 16 refuses any id in a namespace that round
  retired - reading relation subjects and objects as well as `concepts[]`, which is
  18% of the corpus and the entire reason the rule catches anything, with the list
  itself in `hooks/retired-prefixes.json` so the gate and its test cannot disagree
  about what is retired), its own regression test (`hooks/test-gate.py`, 30 cases - the gate is
  live on every `Write` in the repo, so a change that breaks it blocks every agent's
  extraction rather than breaking a report), its verdict log
  (`hooks/gate-log.jsonl`), the
  dispatch-time registry digest (`registry-digest.py`), the corpus audit
  (`verify-evidence.py`), the promotion report (`verify-promotions.py`, which since
  round 14 also checks docs-issue slugs), the
  self-testing recurrence query (`recurrence.py --selftest`, 25 checks, which since
  round 16 also reports spelling variants, `page:` candidates and stale `recurrence`
  fields as three deliberately separate views), the
  registry path/id check (`verify-registry-ids.py`, 550 records, which since round
  14 also rejects an alias that merely re-punctuates its own target and since round
  16 also refuses a `docs-issues/` reference with no file behind it), the
  candidate evidence dump (`candidate-evidence.py`, the namespace pass's reading
  tool, which since round 15 checks every quote it prints against the page it cites
  and has an `--audit` mode for exactly the promotion set a wave is about to write),
  and the id normaliser (`normalise-ids.py`) - which is the odd one out, being the only one
  that *writes*, and the only one that bypasses the gate. It is allowed to because
  it touches `subject`, `predicate`, `object` and `candidate_id` and nothing else,
  so it cannot make a quote stop matching a page; the compensating control is a
  before/after `verify-evidence.py` over the whole corpus, byte-identical across
  151 substitutions in 67 files in round 13 and a further 224 in 24 files in round
  14. Round 15 is the one exception, and it is a *reduction*: 101 substitutions in
  14 files left the problem count 9 lower, because the same round de-escaped
  Markdown punctuation in `norm()` - the shared definition of "verbatim" that the
  gate and the audit both import. 452 → 443, 322 → 313 unquotable. An alarm whose
  false positives land on the marker is worse than a slightly narrower alarm.
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

  Round 16 adds a seventh instance, and it is the one that should retire the word
  "instance": the *census* column of `recurrence.py`, headed "any mention", which
  had not meant any mention since round 14. One `keep` flag, correct for the metric
  it was written for, excluded `seeAlso` from the census as well, and 376 ids - 18%
  of the corpus - were absent from every report this project produces, including
  `--variants`, whose only job is to find spellings. The pattern of the previous six
  holds exactly: the invariant was documented, the tool was purpose-built, the
  output agreed with itself, and the check that would have caught it did not exist
  because the number looked plausible. See "a metric change is a census change"
  below for what was done about it.

  Round 17 adds the case where the shelf grew a check that embodied the bias it was
  built to detect. `shared-source.py --check` exists to decide when a discounted count
  should be *rejected*, and its first report printed `**BELOW THE BAR**` on any row
  whose discounted count fell under 2 — regardless of the verdict on the same line. So
  `index:sequential-scan  2 -> 1  divergent` rendered as a refusal justified by a
  number that row had just rejected, and the round came within one step of refusing a
  candidate its own new instrument had vindicated. The cause is worth more than the
  bug: the discount is the interesting computation, so the report was organised around
  it and the verdict was bolted on as an extra column, rather than as the thing that
  decides which column counts. `effective()` now makes the verdict select the count,
  and seven selftests assert it on the round's real rows. The same round also
  demonstrated the gate reaching something no earlier round had: it refused a quote
  assembled entirely from **real fragments of the page it cites** - the DISTINCT
  Case-2 rule, stated twice on one page in different words, conflated into a third
  wording. That is the fabrication shape closest to undetectable by review, and only
  byte comparison sees it.

- **A metric change is a census change, and nothing says so.** Excluding a relation
  kind from a *measurement* and excluding it from an *enumeration* are different
  editorial decisions, and making the first by editing a shared code path silently
  makes the second. Round 14 excluded `seeAlso` from the concept-promotion metric
  for a good reason - a link between pages is not a claim about a term - and in the
  same edit removed 376 ids from the corpus census, from `--variants`, and from the
  shadow-prefix count quoted in two writeups (43, which is really 55). Five
  misspellings of promoted SQL++ statements were sitting in that gap, each causing
  gate denials nobody could account for, and a concept at 14 files read as
  recurrence 0. The fix is structural rather than careful: a census must not share a
  code path with a metric, because the two differ precisely in what they are allowed
  to ignore, so `scan()` now returns `mentions`, `slots`, `labels` and
  `see_also_objects` as separate tables and a caller has to state which question it
  is asking. The general form is worse than the bug: **every number in this file
  inherits the instrument that produced it, and nothing in the pipeline records
  which instrument that was.**

- **A `recurrence` field in a promoted record is a measurement with a date, and it
  carries neither.** 171 of 324 promoted records disagree with the current query,
  and none of them is a bug: the instrument has been replaced three times (bugs #7,
  #10, #11) and each field records what was true when a human wrote it. The danger
  is not the drift, it is that **a record's prose reasons about its own weight** -
  "a minor, low-stakes promotion", written of a term the query now puts at
  recurrence 8 - and the next reconciliation reads the prose rather than re-running
  the query. This section's first draft did exactly that, believed a stale 2, and
  wrote a false causal story about what a fold had achieved. Two responses, and the
  ordering matters: `--stale-recurrence` exists so the gap is visible, and it is
  deliberately read-only, because auto-rewriting the fields would destroy the only
  record of what each round actually measured in exchange for agreement with a query
  that has been wrong three times. **A stale measurement is data; a silently
  refreshed one is a lost audit trail.**

- **The corpus is not the documentation.** `server/8.0/indexes/` - eleven pages, the
  canonical documentation of the subject this entire wave spent its length
  reorganising - has never been extracted, because round 12 went looking for those
  pages under `learn/` after Antora had already moved them out of it. So every
  recurrence figure in the wave is partly a fact about which directories nine rounds
  happened to walk, and a term's thinness in the corpus is not evidence of its
  thinness in the docs. This is the sharpest form yet of "recurrence is an editorial
  property": it is an editorial property of *the sample*, and the sample was chosen
  by directory name. A coverage plan written as a list of paths inherits every
  reorganisation the documentation has undergone since the plan was written, and
  then reports the resulting hole as a low count rather than as a hole. The
  corollary is the round's naming rule, and it is why `covering-index` ended up
  spelled five ways across three namespaces: **an id names its subject, not its
  location.**

- **An alias is a claim about a referent, and nothing checks referents.** The
  write-time gate resolves aliases before checking an id, which is what makes
  `promoted` a decidable question - and it means an alias is the one field in the
  registry that can make two genuinely different things pass as one, permanently and
  invisibly. Round 16 wrote 21 of them in a single pass while folding namespaces,
  each asserting that a retired spelling denoted the same thing as its target, and
  the only check on any of those 21 was a person reading both records.
  `verify-registry-ids.py` catches the syntactic abuse (an alias that merely
  re-punctuates its target); no check reaches the semantic one, and none can, for
  the same reason nothing can catch a quotable-but-mis-objected relation. So the
  rule has to be procedural: **fold under an alias only where a source sentence
  licenses the identity, and quote the sentence in the record** - which is what
  `indexer-node-state`'s note does for the one deletion of a promoted record this
  POC has made, and what makes that deletion reviewable by someone who was not in
  the room.

- **A promotion metric's proxy fails in both directions, and only one direction had an
  instrument.** "Two distinct files" has stood in for "two independent attestations"
  since round 1, and it is a good proxy, which is why the substitution went seventeen
  rounds unexamined. It inflates when Couchbase publishes one Antora module on several
  branches: 40 clusters now cover 85 extracted pages, 188 ids rest partly on a shared
  source, and 38 of them fall below the bar once the discount is upheld — up from 5
  before this round, because extracting a module that exists in three trees buys
  density and not independence. It deflates when a term is spelled in two namespaces,
  because `variant_key()` keeps the prefix: 62 local names are forked, 20 of which
  would cross the bar only if merged. And it *understates* independence when two
  genres — a reference page and a guide — document one feature, which is stronger
  corroboration than a duplicate and which no count can see. Two rules follow. **The
  verdict decides which count applies**: `divergent` rejects the discount and licenses
  the raw file count, `shared` upholds it, `unchecked` establishes neither and must
  never be marked below the bar. And **a discount computed over a partial corpus is
  not conservative, it is wrong** — round 17 twice drafted a refusal on a mid-round
  count and twice found the completed corpus put the term at 2 or 3 independent
  sources. Subtracting inflation from an incomplete count produces a number with no
  interpretation at all, and it errs toward discarding real terms.

- **Ask an evidentiary rule the other way round at least once.** The reconcile skill
  forbids merging two concepts "unless a source page states the relationship
  explicitly", and seventeen rounds applied it correctly — as a test to *fail*. Nobody
  asked which sentences in the corpus grant the licence. There are **six**, four of
  them on one page, and the search that finds them is a grep for the two phrasings a
  technical writer uses for a synonym. The cost of that gap is invisible by
  construction: a refused merge and a genuine distinction produce identical output —
  two separate records — so a missing licence becomes a permanent silent duplication,
  which is exactly what happened to Capella's Memory Only buckets and Server's
  ephemeral buckets, whose identical restriction on sequential scans this registry
  would have recorded as two unrelated constraints. The structural reason the six
  cluster is worth more than the six: `cloud/management-api-reference/index.md`
  documents API field names, so it is the only page in the corpus with a systematic
  incentive to state equivalences. **A rule that only ever gets used to reject has an
  evidence base nobody has counted**, and finding out how small it is takes a minute.

- **A same-prefix synonym fork is a fourth failure mode, and no instrument watches
  for it.** Bug #12 (cross-namespace fork) has `--forks`; an ordinary misspelling has
  `--variants`. Round 18 found a third shape neither covers: two agents extracting
  different pages about one mechanism — a reference/overview page and its own
  worked-demonstration page — minted two ids sharing the `eventing:` prefix and no
  substring (`eventing:timer-callback` vs. `eventing:timer-callback-handler`,
  `eventing:lookupin-operation` vs. `eventing:lookupin-subdocument-operation`, and two
  more). Four instances in one round, zero file overlap in every case, which is a
  *good* sign about independence and a bad sign about detectability: nothing lexical
  joins the two names, so nothing but reading the folded pair side by side would ever
  find the fork. Filed as a named pattern to read for, not as a fifth script — the
  same status "extraction record vs. registry" collisions had before round 12 gave
  them one.

- **A round's framing paragraph is a hypothesis with the coordinator's name on it,
  and it is exactly as unverified as an extraction agent's claim until a page
  confirms it.** Round 18's own dispatch briefing asserted that
  `eventing-memory-quota.md` has no Capella twin because Capella manages Eventing
  memory automatically — a plausible, unchecked inference from "no file with that
  name exists in `cloud/eventing/`." One of the round's own batches, reading a
  Capella page for background exactly as instructed, found `cloud/eventing/eventing-faq.md`
  stating a user-configurable 256MB→512MB memory-quota knob in wording close to the
  Server page's own. The premise was wrong, or at best incomplete, and the round
  caught its own coordinator's error using the same read-the-page discipline every
  extraction agent is held to. **The "before recommending, verify the memory names a
  file that exists" rule this project's own memory-management guidance states applies
  one level up too: before asserting a structural asymmetry in a briefing, check it
  against the pages on both sides, not just the directory listing on one.**
