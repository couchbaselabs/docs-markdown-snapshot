# Pass-2 reconciliation log

Three rounds so far, in order run. Each section covers one round; a single
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

## Cumulative verdict (all three rounds)

The vocabulary has now been tested against three genuinely different kinds of
"does this still fit": a different component within one product (round 1), a
different deployment model of the same underlying product (round 2), and
three entirely different products built by different teams (round 3). At every
step it kept doing the same useful thing: not just "the terms still fit," but
surfacing something true and specific about each product it touched - Capella's
credential/role-based access model, Sync Gateway's two-disjoint-systems
architecture and inverted channel-based access model, Couchbase Lite's own
disjoint edition split. That's a stronger and more useful result than a
vocabulary that merely never breaks.

The cost of getting that result cleanly has been a steady retreat from
page-by-page manual reconciliation toward aggregate statistics and explicit,
documented judgment calls - a real trade-off, and the right one at this scale.
Two limits of the method are now visible across multiple rounds, not just
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
