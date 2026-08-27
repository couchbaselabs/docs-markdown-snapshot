# Pass-2 reconciliation log

Nine rounds so far, in order run. Each section covers one round; a single
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

## Cumulative verdict (all nine rounds)

The vocabulary has now been tested against nine genuinely different kinds
of "does this still fit": a different component within one product
(round 1), a different deployment model of the same underlying product
(round 2), three entirely different products built by different teams
(round 3), a single product's own feature that cuts across its existing
per-operation model (round 4's transactions, within the Java SDK already
covered in round 3), full coverage of a directory a prior round had only
sampled a fifth of (round 5), the same partial-sampling lesson recurring on
the same product's role catalog (round 6), that exact lesson recurring a
third time on the privilege catalog (round 7), the cleanest negative result
so far - a brand-new, complex feature (Eventing) needing no new structural
layer at all (round 8) - and, closing out `cloud/` entirely, a round
expected to mostly confirm rather than surprise, which is exactly what it
did, while still finding three real gaps and closing a question left open
since round 5 (round 9). At every step it kept doing the same useful thing:
not just "the terms still fit," but surfacing something true and specific
about each surface it touched - Capella's credential/role-based access model
(round 2), Sync Gateway's two-disjoint-systems architecture and inverted
channel-based access model (round 3), Couchbase Lite's own disjoint edition
split (round 3), the Java SDK's transaction layer inverting CAS-based
concurrency into transaction-membership checks (round 4), round 2's "simple
credential-type pair" turning out to be a whole per-statement privilege
catalog (round 5), `capella-role:*` turning out to be two catalogs silently
flattened together since round 2 (round 6), `cluster-rbac.md`'s own
25-privilege table more than doubling what round 5 had already corrected
(round 7), Eventing confirming that "genuinely new feature" doesn't
automatically mean "genuinely new access-control shape" (round 8), and the
SQL++-vs-SDK transaction boundary finally stated explicitly by a page's own
text rather than left inferred (round 9). That's a stronger and more useful
result than a vocabulary that merely never breaks.

The cost of getting that result cleanly has been a steady retreat from
page-by-page manual reconciliation toward aggregate statistics and explicit,
documented judgment calls - a real trade-off, and the right one at this scale.
Six limits of the method are now visible across multiple rounds, not just
once, so worth treating as durable rather than one-off:

- **Structural silence isn't a naming problem.** The method is good at
  catching "these two labels are probably the same thing" (round 1's
  link-target mismatch, round 2's `search-admin`/`fts-admin` overlap). It has
  nothing to say about "this page is silent on something comparable pages all
  state" beyond flagging the silence - that distinction needs a human, every
  time.
- **A written registry prevents re-litigating the past, not the present.**
  Every round has produced at least one case of two agents (or one agent
  revisiting old ground) independently minting near-duplicate vocabulary for
  something new, because a static list of already-promoted terms says nothing
  about what a concurrently-running sibling batch is minting right now. This
  hasn't gotten worse as the vocabulary has grown - if anything the promoted
  core (privilege/edition/version shapes) has stayed remarkably stable - but it
  hasn't gone away either, and a production pipeline would need either a live,
  queryable registry or a mandatory dedup pass, not a bigger written briefing.
- **Reconciliation itself can leave gaps, not just extraction.** Round 3's
  Java SDK batch was reconciled only at the narrative level and never promoted
  a single concept - a gap invisible until round 4 tried to reuse those
  concepts and found them absent from the registry. The recurrence-based
  promotion discipline only catches what a reconciliation pass actually runs
  over; skipping a product at reconciliation time is a silent debt, not a
  visible one, until a later round trips over it.
- **Partial coverage of a large, uniform-looking directory doesn't generalize
  the way it feels like it should.** Round 2 read 23 of `cloud/n1ql/`'s 138
  pages and reasonably concluded the credential-type model was a flat pair.
  Round 5 read the other 115 and found a whole per-statement privilege
  catalog with two-axis and AND-combination structure the smaller sample never
  surfaced. Not a failure of round 2's method - a fifth of a directory is a
  defensible sample size for a first pass - but a concrete reminder that "this
  directory's vocabulary is settled" should mean "fully read," not "sampled
  and nothing broke yet."
- **Vocabulary built from a feature's mentions elsewhere is less reliable
  than vocabulary built from the feature's own authoritative page.** Both
  `capella-role:*` (round 6) and the Advanced-credential privilege catalog
  (round 5) were originally minted from statement pages' Prerequisites
  sections - paraphrases of the real thing, not the thing's own
  documentation. Both turned out incomplete or mislabeled once the
  authoritative page (`project-roles.md`, `organization-user-roles.md`) was
  read directly. Worth treating as a standing prioritization signal: read a
  feature's own reference page before trusting vocabulary inferred from
  where it's merely mentioned.
- **Knowing about a failure mode doesn't prevent it.** The "narrated as
  promoted, never actually filed" reconciliation gap has now recurred three
  times (round 2's `gatedByBillingPlan`, round 3's Java SDK concepts, round
  5's `monitoring:*` family) - the third one introduced by this same
  reconciler, in round 5, after already having written up the first two as a
  known risk in round 4's cumulative verdict. Vigilance alone isn't a
  reliable control for this; an automated check (script-verify every
  concept/predicate name appearing in a round's reconciliation.md section
  resolves to a real file) would catch it structurally instead of relying on
  memory.
