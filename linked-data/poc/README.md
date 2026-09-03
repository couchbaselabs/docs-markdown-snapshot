# Linked-data POC — sample tree

A proof of concept for the approach described in
[`../linked-data-spec.md`](../linked-data-spec.md): can an LLM propose the ontology
piecemeal, page by page, well enough to be worth iterating on, rather than needing a
week of upfront ontology design?

This is a review artefact, not production output — everything here was extracted
and reconciled to see what the method actually produces before investing in
automating it. Nineteen rounds so far, fifteen of them deliberate escalations and
four corrective passes over what they left behind:

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
    322 of 2,780 relations were unquotable (313 of 3,522 as re-measured in round 16,
    after round 15 fixed the de-escaping bug in the comparison itself). Second, version-evidence density
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
    made machine-readable (one recurrence 9 → 50), variant clusters 16 → 1, and two
    new controls: `verify-registry-ids.py` and `normalise-ids.py`.
14. **No new pages** — the **namespace coherence pass**, wave 1. Round 13 left a
    206-item backlog; this round worked it the way round 10 concluded it must be
    worked, *one namespace at a time, deciding the namespace's internal structure
    before promoting any member*, and found two defects that are invisible per-item
    and obvious per-group. First, the promotion metric: round 11 excluded
    documentation pages from the concept ranking, round 12 broadened that ranking
    from the object slot to *either* slot, and the second change silently cancelled
    the first because the exclusion lived in the branch it replaced. Page ids came
    back in as `seeAlso` **subjects** — `search:customize-index` has 24 relations,
    all of them `seeAlso`, and a page title for a label. **27 of 203 backlog items
    were this**, 9 of them with no non-`seeAlso` relation at all. Second,
    `vector-index:` was a namespace *named* like an axis and *populated* like a
    subject area: its 30 members answered five different questions, two of them
    were already promoted under `index-type:` at recurrence 2 while their
    `vector-index:` spellings sat at 5 in another product tree, and one record used
    both prefixes at once. Renamed to `vector-search:` with five members evacuated
    to axes that already existed. 18 concepts promoted, 30 ids retired, and the
    `version:` namespace given one treatment (rewrite, dashes) where it had been
    carrying two. The whole `vector-index:` finding turns out to have been written
    down in round 11 by an extraction agent, in the right words — "FOUR
    NAMESPACES, ONE LIST … the fix is a reconciliation decision" — and left
    unactioned for three rounds because its remedy was to refactor already-promoted
    records, and reconciliation had no output shaped like that.
15. **No new pages** — the namespace coherence pass, wave 2: **`setting:`**, 34 ids
    across 14 files. Wave 1 asked whether a namespace's members answer the same
    question; this one asks a prior question — *is there a question at all?* The test
    that settled it: **a namespace is an axis only if its membership is closed and
    enumerable.** `edition:`, `index-state`, `auth-mechanism:` pass. `setting:`
    fails **by construction**, because a product acquires settings for as long as it
    is developed, so `setting:` was never an axis and had no subject to be about
    either: it was a *part of speech*. Dissolved, member by member, into the subject
    areas that own the mechanisms — 29 to `n1ql:`, 2 each to `index:` and `data:`,
    1 to `tls:` — because a dissolution's destination is not a function of the id
    and cannot be done with a prefix rule the way wave 1's rename could. Three of
    the 34 were **duplicates of already-promoted concepts** (`setting:scan-consistency`
    and the promoted `n1ql:scan-consistency` are the same thing), which is how the
    round found that the write-time enum **checks the id and never the referent**:
    `registry_status: minted` was a *true* declaration for a term the same round's
    reconciliation promoted under another name. 10 concepts promoted, and a
    correction to wave 1: `vector-search:product-quantization`'s two files collapse
    to one, because a round-1 relation quotes a sentence verbatim from a *different*
    page than the one it names — misattribution, not fabrication, but it costs a
    recurrence, and it is the failure mode a *promoted* record can commit that no
    gate watches. Two forward-only id-shape rules added to the gate, plus
    `hooks/test-gate.py` (23 cases) — because a control's verdict can expire: a real
    round-12 record replayed through the gate today produces five denials, since
    `registry_status` describes the registry the record was written against.
16. **No new pages** — the namespace coherence pass, wave 3: **`indexes:`,
    `index-type:`, `index:`**, and it turned into a round about the *instruments*
    rather than about the namespace. The finding that had to come first: the census
    column of `recurrence.py`, labelled "any mention", had not meant any mention since
    round 14, when one `keep` flag excluded `seeAlso` from a metric — correctly — and
    from the census, silently. **376 ids, 18% of the corpus, appeared in no report
    this project produces**, including `--variants`, whose only job is to find
    spellings; five misspellings of promoted SQL++ statements were sitting in that
    gap, and a concept at 14 files read as recurrence 0. With that fixed, the
    namespace's real defect was visible: **`covering-index` was spelled five ways
    across three prefixes**, because `covering-indexes.md` lives at a different path
    in each of four trees and ids had been minted from paths. Hence the round's naming
    rule — **an id names its subject, not its location** — and a third answer to wave
    2's axis test: `indexes:` was neither an axis nor a subject area but a **plural
    fork of `index:`**, retired entirely; `index-type:` kept the axis and shed two
    storage *modes* that are not kinds of index. 59 renames across 36 files, 21
    aliases retired, `indexes:`/`vector-index:`/`setting:`/`setting-scope:`/`tools:`
    all at 0 occurrences, and the gate now refuses a retired prefix in *any* slot.
    Two second-order findings, both about this file's own numbers: a `recurrence`
    field in a promoted record is **a measurement with a date and records neither**
    (171 of 324 disagree with the query; none is a bug, and this round's first draft
    believed a stale one and wrote a false causal story from it), and **the corpus is
    not the documentation** — `server/8.0/indexes/`, eleven pages, the canonical
    documentation of this very subject, has never been extracted, because round 12
    went looking for it under `learn/` after Antora had moved it out. That sets round
    17's scope. Also the first deletion of a promoted record in the POC's history
    (`capella:index-ui-status`, folded into `indexer-node-state` on the strength of
    one near-identical defining sentence in each tree), and 6 new docs-issues.
17. **22 pages, the `indexes/` module, two jobs run together** — `server/8.0/indexes/`
    (11 pages, **never extracted**, first contact) and `cloud/indexes/` (11 pages,
    extracted pre-gate and thin), paired so each is the other's diff-gate. It is the
    round that puts a number on round 16's "the corpus is not the documentation":
    **the same eleven Capella pages went from 35 relations to 343, a 9.8× recovery**,
    and first contact on the server tree produced 400 relations at a mean of 36.4
    against round 10's baseline of 13.4 — the densest material the project has read.
    743 relations, 0 evidence problems. The substantive results all follow from having
    read the pages: the **pushdown family** (7 concepts) had been met at recurrence
    1–3 for six rounds because the page whose title, lede and six headings define it
    had never been extracted; the **storage stack settles** on a one-to-many map (one
    storage setting, implemented by Plasma in Enterprise Edition and Forestdb in
    Community Edition — so a setting cannot be an engine), promoting the three engines
    round 16 ruled on correctly and could not support; and **`index:index-span`** folds
    five ids for one concept, two of them minted by different agents in this very
    round. The round's own method finding is about the promotion metric's **proxy**:
    "two distinct files" stands for "two independent attestations", and both
    instruments that measure how that substitution fails were built here —
    `shared-source.py` for inflation (one Antora module published on three branches is
    one witness) and `recurrence.py --forks` for deflation (one term spelled in two
    namespaces sits below the bar twice). They **reversed four promotion decisions in
    both directions**, rescuing `index-type:array-index`, `index-type:functional-index`
    and `index:sequential-scan`, and refusing `index:duplicate-index` — which has the
    round's most quotable defining sentence and three files that are three copies of
    one page. Also: the corpus contains **exactly six sentences** licensing a merge,
    four of them on the Capella Management API reference, which let a cross-product
    bucket-terminology discrepancy be folded *with a citation* after sixteen rounds;
    and 11 new docs-issues, headed by a documented "switch on" procedure that uses XOR
    on a bitmask and **disables the feature the reader was enabling**.
18. **67 pages, the `eventing/` module, first contact paired against round 8's twin**
    — `server/8.0/eventing/` + `server/8.0/eventing-rest-api/`, never extracted,
    read against the already-extracted `cloud/eventing/` exactly as round 17
    recommended. 400 relations, 0 evidence problems, 1.64× round 8's density — a
    real gain, much smaller than round 17's 9.8×, because the module turns out to be
    the corpus's **most heavily duplicated**: Server/Capella page pairs run
    0.89–1.00 similarity, and `shared-source.py`'s below-the-bar count jumps from 38
    to 89 in one round. The round's headline finding is exactly that split: **a
    pairing strategy's payoff has two independent axes — defect-finding and
    promotion-independence — and a good result on one does not transfer to the
    other.** Defect-finding worked as prescribed (12 new docs-issues, headed by a
    structural asymmetry: all nine Server worked-examples gate Function creation
    behind Full Admin/Eventing Full Admin, absent from every Capella twin, because
    Capella's access model is project-scope roles, not Server's cluster-wide
    catalogue); promotion-independence mostly didn't, because there was little
    independence in the module to buy. Also found: four Eventing entry points, not
    two — `eventing:on-deploy-handler` and `eventing:timer-callback` join the
    promoted OnUpdate/OnDelete pair under a new `eventing-handler-family` scheme —
    and a **fourth fork species**: two agents naming one mechanism through two
    different predicates mint two same-prefix ids with no shared substring, four
    times in one round, invisible to both `--variants` and `--forks`. And a
    self-caught error: this round's own dispatch briefing asserted Capella has no
    Eventing memory-quota control, unchecked, and one of its own batches found
    Capella's FAQ contradicting it.
19. **22 pages, two small modules dispatched together** — `server/8.0/backup-restore/`
    (18 pages, the whole `cbbackupmgr` CLI reference, **no Capella twin exists at all**)
    and `server/8.0/javascript-udfs/` (4 pages, paired against round 6's twin, similarity
    **measured before dispatch** at 0.92–1.00 — the exact caution round 18 closed with).
    158 relations, 0 evidence problems. The pre-check paid off immediately: told in
    advance its module was heavily duplicated, the javascript-udfs batch minted
    **nothing** and spent its attention on divergence instead — two real unadapted-
    Capella-wording defects and a genuine interop question (does a JS UDF called from
    SQL++, calling back into SQL++, actually recurse? yes — resource-pool exhaustion is
    the limit, not a documented depth cap). The `cbbackupmgr` half shows the fork problem
    at a finer grain than rounds 17–18 found it: the dispatch briefing named two real
    collisions in advance (`js-udf:` vs. `eventing:`; `object-store:` vs.
    `cloud-provider:`) and both were avoided cleanly — and the same two batches, sharing
    that briefing, still independently minted one concept twice under **four other,
    un-warned-about name pairs** (`backup:repository`/`cbbackupmgr-repository`,
    `cloud-integration`/`native-cloud-integration`, the merge command twice, one RBAC
    role twice — the second time reaching back to a round-12 mint left unpromoted for
    seven rounds). **Warning about a specific collision prevents that collision and
    nothing else.** The sharpest fork happened because an agent did exactly what it was
    told — check the registry before minting — and still missed, because the answer
    was sitting in a *relation* from round 11 (`tool:cbbackupmgr acquiresLockOn
    backup:repository`), not in the label `registry-digest.py` prints: **a concept's
    existing relations are part of what "already in the registry" means.** Also found
    a real three-way contradiction within `cbbackupmgr`'s own pages over who may run
    it and under which edition, with none of the three pages cross-referencing the
    others.

See `reconciliation.md` for the full round-by-round log, findings, and a
cumulative verdict at the end. See `../ingest-cost-and-time-estimate.md` for the
time/cost projections and how they held up against the round-2 run's real numbers.

## Scope

682 pages total:

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
- **11 more, `server/8.0/indexes/`** — the whole module: the index overview,
  `storage-modes.md`, `index_pushdowns.md`, `index-scans.md`,
  `indexing-and-query-perf.md`, `groupby-aggregate-performance.md`,
  `query-without-index.md`, `index-replication-and-partitioning.md`,
  `index-lifecycle.md`, `plasma-key-value-storage-engine.md` and
  `indexing-best-practices.md`. **Never extracted before round 17** — not deprioritised
  but *missed*, because round 12 walked `learn/` after Antora had moved these pages out
  of it. 400 relations at a mean of 36.4, the densest batch in the project.
- **11 re-extracted, `cloud/indexes/`** — the same module in Capella, read in round 6
  before the write-time gate existed and thin at a mean of 3.2 relations. Re-read
  under the gate: **35 relations → 343**. The page count is unchanged by this half of
  the round; the content is not.
- **67 more, `server/8.0/eventing/` + `server/8.0/eventing-rest-api/`** — the whole
  module, never extracted before round 18: the overview, lifecycle, RBAC, language
  constructs, memory quota, timers, statistics, debugging, troubleshooting, FAQ,
  curl spec, advanced keyspace accessors, buckets-to-collections, function export,
  terminology glossary, the REST API reference, 9 worked-example pages and 41
  individual JS handler code-sample pages. Paired against round 8's already-extracted
  `cloud/eventing/` (67 pages, same feature) exactly as round 17 recommended. 400
  relations, 0 evidence problems, 1.64× round 8's density.
- **18 more, `server/8.0/backup-restore/`** — the whole `cbbackupmgr` CLI reference:
  the tool overview, the Enterprise-vs-Community page, best-practice strategies, the
  backup/restore/merge/compact/remove/examine/config/info/generate/collect-logs
  commands, encryption, network-filesystem and cloud-object-store targets, help, and
  a worked tutorial. **No Capella twin exists at all** — Capella exposes no equivalent
  CLI. 158 relations combined with the batch below.
- **4 more, `server/8.0/javascript-udfs/`** — paired against round 6's already-extracted
  `cloud/javascript-udfs/` (4 pages, identical filenames), whose similarity was
  **measured before dispatch** at 0.92–1.00 per round 18's closing recommendation.

Rounds 13 through 16 added **no pages**. All four worked the existing 582 records:
round 13 the role slice and the variant sweep, rounds 14, 15 and 16 waves 1, 2 and 3
of the namespace coherence pass. So the page count above was stable for four
rounds while the registry changed substantially, which is worth stating explicitly —
the corpus and the registry are separate things to keep track of, and the interesting
defects of those four rounds were all in the second.

Round 16 adds a third thing to keep track of, and it is the one this list gets wrong
most easily: **the corpus is not the documentation.** The scope list above is a list
of directories that were walked, and directories move. `server/8.0/indexes/` — 11
pages, the canonical documentation of indexes — was absent from this list not because
it was judged low-value but because round 12 looked for it under `learn/`, where it
used to be. So a low recurrence count is not evidence about the docs until someone
checks that the pages exist in the sample at all. Round 17 closed both halves of that
gap and measured the cost of having left it open: the eleven never-read server pages
yielded 400 relations, and re-reading the eleven thin Capella records yielded
**9.8× what they held**. Two failure modes, one symptom — a modest recurrence count —
and only one of them makes any checkable claim for a control to catch.

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
  Round 14 promoted 18 and **retired 30 ids**, working by namespace rather than by
  rank. `vector-index:` was renamed to `vector-search:`, because a namespace named
  like a closed axis (compare `index-type:`, `index-class:`, `auth-mechanism:`) was
  populated like a subject area (compare `eventing:`, `monitoring:`, `backup:`) —
  both kinds are legitimate and this one was filed as the wrong kind. Five members
  left it for axes that already existed: `index-type:search-vector` joined
  `index-type:hyperscale-vector` and `composite-vector` — which had been **promoted
  since round 11 under the minority spelling**, at recurrence 2 each, while
  `vector-index:hyperscale-vector-index` and `…composite-vector-index` were used in
  5 files apiece and read as unpromoted debt, split by product tree with one
  `cloud/` record using both prefixes at once (round 12's misfiled-roles shape,
  fixed by union: 2 → 7) — and the two vector functions became
  `n1ql:approx-vector-distance` and `n1ql:vector-distance`, on the pages' own link
  targets into the SQL++ reference rather than on resemblance. The fold also
  supplied a citation round 11 had explicitly *declined to invent*: its
  `tradesOffAgainst` refusal was right about `indexes.md` and wrong about the
  corpus, where the head-on comparison existed under the other namespace's ids —
  **a refusal recorded on a record is invisible to the round that acquires the
  missing evidence.** New: `vector-similarity-metric:euclidean`/`euclidean-squared`/
  `cosine`/`dot-product`, a closed enum filed as its own namespace, all four at
  recurrence 1 under the family exception because the source states them as a set
  with a support matrix; six `vector-search:*` tuning terms (`reranking`,
  `recall-rate`, `memory-footprint`, `persist-full-vector`,
  `product-quantization`, plus `scalar-quantization` at recurrence 1, promoted
  because a two-valued choice half-built is the exact incoherence this pass exists
  to remove); and three maintenance releases (`version:server-7-6-2`/`-4`/`-6`),
  unpromoted at recurrence 6 purely because nothing had ever compared the
  `version:` namespace's records against its candidates. Refused, with reasons on
  the record: `setting:` was not created (three unpromoted members from three
  unrelated areas and no promoted member — filing a vector setting into an unbuilt
  axis would mean filing it twice); IVF/flat/HNSW were not promoted as an algorithm
  family, because whether quantization is also an algorithm is unresolved and
  merging on the resemblance is what the never-merge-without-evidence rule forbids;
  and `fts:` versus `search:` was **confirmed rather than tidied**, because
  `concepts/fts/full-text-search.json` turned out to record a deliberate resolution
  of a five-way split, with two documented legitimate non-folds — a coherence pass
  that cleaned it up would have destroyed a correct decision.
  Round 15 ran wave 2 over `setting:` and **dissolved it**, which is the answer round
  14's refusal had already half-given. Wave 1's rename worked because
  `vector-index:` was named like an axis and populated like a subject area; wave 2's
  namespace was named like a subject area with *no subject to be about*. The test
  that settles this is **whether membership is closed and enumerable**: `edition:`,
  `auth-mechanism:`, `index-state` and `vector-similarity-metric:` are, `setting:` is
  not and cannot become so, because a product acquires settings for as long as it is
  developed. So the 34 members went to the subject areas that own the mechanisms —
  29 `n1ql:`, 2 `index:`, 2 `data:`, 1 `tls:` — one at a time, since a dissolution's
  destination is not a function of the id and no prefix rule can compute it. Three
  members were **already promoted under another name** (`setting:scan-consistency` /
  `n1ql:scan-consistency`, `setting:collection-max-ttl` / `data:max-ttl-setting`,
  `setting:encoded-plan` / `n1ql:encoded-plan`), and two more (`setting:max-parallelism`
  and `setting:query-max-parallelism`) were the same setting spelled at two tiers;
  all five now carry `aliases`. New: the **CURL access-list family**
  (`n1ql:curl-all-access` plus `curl-allowed-urls`, `curl-disallowed-urls` and the
  `query-curl-whitelist` container that holds them) and the **completed-requests
  family** (`n1ql:system-completed-requests`, `completed-limit`,
  `completed-threshold`, `completed-stream-size`), promoted on a sharpened version
  of the family exception: *if a promoted record cannot state what it **is** without
  naming a sub-threshold sibling, that sibling is part of the family* — mechanical
  enough to refuse with, which is how `n1ql:curl-result-cap` stayed out despite
  sitting on the same page at the same recurrence. Plus `n1ql:max-parallelism` and
  `index:indexer-settings-defer-build`, the latter the first *setting* in a namespace
  otherwise holding storage modes and index kinds, which is wave 3's question.
  Tier-neutral naming became a rule here: a setting documented at more than one tier
  gets the tier-neutral kebab name (`max-parallelism`, `completed-limit`) and keeps
  the documented one only when single-tier (`query-curl-whitelist` is cluster-only,
  `completed-stream-size` node-only), because **tier membership is a fact for a
  relation, not for an id**.
  Round 16 ran wave 3 over the index namespaces and promoted only **five**, which is
  the smallest concept round since round 4 and the right shape for it: the work was
  the *rewrite*. `indexes:` — a plural fork of `index:` — was retired entirely, and
  59 ids across 36 files were renamed so that **an id names its subject, not its
  location**, the rule forced by `covering-indexes.md` living at a different path in
  each of four doc trees and producing five spellings of one concept across three
  prefixes. `index:covering-index` is the fold of those five, promoted on the
  semantic-weight exception at recurrence **0** on the promotion metric and 14 files
  in the census, and filed under `index:` rather than `index-type:` on the strength of
  the docs' own grammar (the index covers *the query*) and of a page that lists it as
  a type and then defines it *after* index selection — **a type you cannot know at
  `CREATE INDEX` time is not a type**. `concepts/indexer-node-state.json` is the
  round's fold and the POC's **first deletion of a promoted record**: it absorbs
  round 12's `capella:index-ui-status` on the strength of the same defining sentence
  appearing in each tree differing by one word, with the Capella table's missing
  fourth value documented rather than either list winning. Plus
  `index:file-based-index-rebalancing` and `index:index-redistribution-setting` (the
  second answering a question round 15 deferred), and `index-type:view` **re-filed**
  from `concepts/index/view.json` — it was always a kind of index; only its filing
  was wrong. Two ids were re-filed *out* of `index-type:` for the mirror reason
  (`moi` and `standard-gsi-plasma` are storage **modes**, not kinds of index), and
  the three storage engines under them (Plasma, Forestdb, Nitro) were deliberately
  **not** promoted, because their only evidence is a page in the never-extracted
  `server/8.0/indexes/` module. That is round 17's.
  Round 17 read that module and promoted **22**, all of them things the corpus could
  not previously support. `concepts/index-storage-stack.json` holds the four levels the
  docs' two overlapping phrases had been flattening — the setting, its two values, the
  engine implementing a value, and (Forestdb only) the engine's write mode — settled by
  a **one-to-many map**: standard index storage is backed by Plasma in Enterprise
  Edition and by Forestdb in Community Edition, so a setting cannot be an engine.
  `storage-engine:plasma` (2), `forestdb` (3) and `nitro` (**1**, the thinnest evidence
  behind any concept here) are promoted as a family, because a partly-promoted family
  is worse than none of it: the gap would be indistinguishable from a fact. The
  **pushdown family** is seven — `index:index-pushdown` (6),
  `predicate-pushdown` (6), `group-aggregate-pushdown` (4), `pagination-pushdown` (3),
  `index-projection` (3), `order-pushdown` (2) and `operator-pushdown` (1, family
  exception) — plus that family's two above-bar members, `n1ql:min-pushdown` and
  `n1ql:max-pushdown`, promoted separately at 3 divergent files each after a correction
  to the round's first pass: the family record had been filed at recurrence 1 while
  recording that two of its members clear the bar, which is the rule upside down, and
  **a `members` list is not reachable by alias resolution and does not stand in for a
  record** — and the reason six rounds met these at recurrence
  1–3 is that `index_pushdowns.md`, whose title, lede and six H2s *are* the family, had
  never been read. It is also **defined twice**, by that page and by
  `groupby-aggregate-performance.md`, each presenting the other as a sibling topic:
  **a recurrence count sees a term used, not a term owned.** Four types joined the
  axis — `index-type:composite-secondary-index` (5, the round's best-attested),
  `array-index` (3), `functional-index` (2), `partial-index` (2, whose second source is
  a *guide* rather than a second copy of a reference page, which is stronger
  corroboration than the metric can express). Plus `index:index-span` (4), folding
  **five** ids for one concept, two of them minted by different agents in this same
  round; `index:sequential-scan` (2, and it turns round 12's re-filing of
  `role:query-use-sequential-scans` out of `privilege:` from a judgement call into a
  cited correction); and the plan-field pair `concepts/query-plan-index-fields.json`
  plus `index:covers-plan-field` (3), filed under `index:` rather than a proposed
  `plan-field:` prefix precisely because a new prefix for a suffix that already exists
  elsewhere is the namespace fork this round built an instrument to detect. Two aliases
  were folded **with a citation** — `bucket:memory-only-bucket` into the promoted
  `bucket:ephemeral-bucket`, `bucket:memory-and-disk-bucket` into
  `bucket:couchbase-bucket` — on one sentence in Capella's Management API reference,
  which resolves a cross-product discrepancy the registry had carried since round 6;
  see `concepts/terminology-equivalences.json` for that sentence and the five others
  like it, which are **all** the corpus contains. Refused, with reasons recorded:
  `index:duplicate-index` (an explicit defining sentence and three files that are three
  copies of one page — **1** independent source), `index:span-inclusion` (a genuine
  closed 0–3 value set, attested once, and the best candidate for a later round),
  `index:index-storage-setting` (the top level of the storage stack is real; its *name*
  is not yet earned), and eight more.
  Round 18 read `server/8.0/eventing/` and promoted **17**, most of them the product of
  folding forks rather than minting fresh terms. `concepts/eventing-handler-family.json`
  corrects a count sixteen rounds carried unquestioned: Eventing has **four** declared
  entry points, not two. `eventing-Terminologies.md` — extracted since round 8 — states
  "The Eventing Service calls the OnUpdate, OnDelete, and Timer Callback handlers" in
  one sentence, and only the first two were ever filed; `eventing:on-deploy-handler`
  was missed for a structural reason rather than an oversight — its own page frames it
  as a *lifecycle step*, not a handler, so an agent reading only that page extracts it
  under `createsOnAction` rather than `hasHandler`. Both new members were also each
  independently minted **twice**, and the two misses are different species: `on-deploy-handler`
  vs. `ondeploy-handler` is a hyphen-only variant that `recurrence.py --variants` catches
  and `normalise-ids.py` rewrites (the same treatment round 8's own `onupdate-handler`
  got); `timer-callback` (minted via `firesCallback`) vs. `timer-callback-handler`
  (minted via `hasHandler`) shares a prefix and no substring, so **neither `--variants`
  nor `--forks` catches it** — a fourth fork species, found only by reading the folded
  pair side by side, with zero file overlap once merged (16 distinct files, the best
  independence signal in the round). The identical shape recurred at smaller scale on
  three Advanced Keyspace Accessor operations (`lookupin-operation`, `mutatein-operation`,
  `touch-operation`, each folding an overview-page mint with a worked-example-page mint).
  Function-configuration concepts: `eventing:eventing-storage` (13, the metadata keyspace
  whose deletion undeploys every Function using it, a hazard stated only in a glossary
  entry), `eventing:function-scope` (5, divergent, the RBAC-grouping bucket.scope pair),
  `eventing:listen-to-location` (5, divergent, the DCP mutation source), `eventing:deployment-feed-boundary`
  (2, exactly at the bar). `eventing:recursive-mutation` (4) corrects a round-8 misuse of
  `shouldNotBeConfusedWith` — reserved for two things a reader might wrongly conflate,
  not a hazard a Function can exhibit. `eventing:cas-conditioned-write` generalises
  round 8's `eventing:cas-conditioned-delete` onto the near-identical REPLACE harness
  round 8 had explicitly left unmodeled while flagging the asymmetry. `eventing:visual-debugger`
  (3, no shared-source discount) corrects this round's *own* dispatch framing, which
  treated the debugger as Server-only; Capella's own terminology glossary describes the
  identical mechanism in one entry rather than a dedicated page. And `eventing:bucket-binding`
  folded as an alias into the already-promoted `eventing:bucket-alias-binding` — the same
  mechanism minted twice **within round 8 itself**, not across rounds.
  The round's method finding is that its own recommended pairing strategy split on an
  axis nobody had separated before: `server/8.0/eventing/`'s Capella twin is the corpus's
  most heavily duplicated pairing (0.89–1.00 page-similarity, `shared-source.py`'s
  below-the-bar count jumping from 38 to 89 in one round), so the pairing found real
  defects (12 new docs-issues) while buying almost no independence for newly-minted
  concepts — the two payoffs round 17's indexes module had delivered together came apart.
  Round 19 tested round 18's own closing recommendation — check a pairing's
  page-similarity before dispatching it — for the first time, and promoted **14**.
  `javascript-udfs/`'s pairing was measured at 0.92–1.00 before dispatch; briefed with
  that number, the batch minted nothing new and instead confirmed **seven** concepts
  round 6 had left unpromoted for thirteen rounds: `js-udf:global-function`/
  `scoped-function` (5 each, the visibility/keyspace-resolution pair), `js-udf:udf-library`
  (4, the container both attach to), `js-udf:external-function`/`sql-managed-udf`
  (3 each, the two ways to back a `CREATE FUNCTION ... LANGUAGE JAVASCRIPT` statement,
  which `tradesOffAgainst` each other explicitly), and `js-udf:inline-statement-call`/
  `n1ql-function-call` (2 each, exactly at the bar, the two ways to run SQL++ from
  inside a JS UDF). The last is deliberately **not** merged with the already-promoted
  `eventing:n1ql-function-call` despite the identical local name — the same `N1QL()`
  built-in, invoked from two different JavaScript runtimes with different available
  parameter support per the page's own wording — and `recurrence.py --forks` now
  carries the pair as a documented non-merge rather than an unexplained collision.
  `server/8.0/backup-restore/` (no Capella twin at all) promoted **7**, and four of
  them are same-round self-folds: two batches sharing one dispatch briefing, working
  concurrently on the same 18-page module, independently minted one concept twice under
  four name pairs the briefing hadn't warned about. `backup:repository` (7, folding
  `backup:cbbackupmgr-repository`) is the sharpest instance — the batch that minted the
  new spelling explicitly checked `registry-digest.py` first and still missed the
  reuse, because the correspondence was stated in a *relation* from round 11
  (`tool:cbbackupmgr acquiresLockOn backup:repository`), not in the label a digest
  prints. `backup:archive` (7, no fork) is the container `backup:repository` sits
  inside. `backup:native-cloud-integration` (6, folding `cloud-integration`) and
  `backup:cbbackupmgr-merge-command` (4, folding `merge-operation`) are the tool's own
  self-forks. `role:data-backup` (4, folding `role:data-backup-and-restore` — a
  round-12 mint left unpromoted for seven rounds, independently re-spelled twice more
  this round) and `role:analytics-admin` (4) are two more service-specific admin roles
  `cbbackupmgr` requires for cluster-level data, joining the already-promoted
  `role:eventing-full-admin`/`role:fts-admin`. `tool:cbcollect-info` (3, mostly
  pre-existing) is notable for what it explicitly does **not** collect — audit logs and
  Eventing's own Application log. The round's method finding is the fork problem at a
  finer grain than rounds 17–18 found it: the dispatch briefing named two real
  collisions in advance and both were avoided cleanly, while the same briefing did
  nothing for the four collisions nobody had thought to name — **warning about a
  specific collision prevents that collision and nothing else.**
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
  Round 14 added **none**, which is itself a result — a coherence pass over two
  concept namespaces needed no new predicate, because all seven predicates the
  forked `vector-index:` records used were already promoted and correctly reused
  across both product trees. **The relation layer converged while the concept layer
  forked**, and mechanically that follows: there are ~100 predicates and every agent
  prompt lists them all, against ~300 concepts where the table an agent gets is
  necessarily partial. It also means the fork was a *type error* in records that
  passed the evidence gate cleanly — `service:search-service -providesIndexType->
  vector-index:search-vector-index` has a predicate naming the axis and an object
  whose namespace contradicts it — which is the concrete case arguing for the
  subject/object slot-type validation still on the backlog. What the round did find
  in this layer is the same drift it found in namespaces:
  `relations/trades-off-against.json` describes its range as two vector-index
  *strategies*, while **not one of its 10 occurrences relates two index types** —
  every one is a knob against a cost (`nprobes` against `recall-rate`,
  `persist-full-vector` against `memory-footprint`). A record's prose describes the
  sample that produced it, not the corpus that has since used it. Left as a
  finding, because correcting the range means deciding whether to drop the
  strategy-comparison reading or split it into a second predicate, and that is a
  promotion decision rather than an edit.
  Round 16 added **none** either, and did to one predicate what round 14 declined to
  do: `isSynonymOf`'s range is **widened** from statement pairs to concept pairs, on
  one explicit sentence — "A secondary index is also called a Global Secondary Index
  (GSI)." The two concepts stay **unmerged**, which is the point of owning the
  predicate: both spellings are in live use (`index-type:secondary-index` at 3 files
  on the promotion metric and 6 in the census, `index-type:gsi` at 8 and 16), a reader
  searching either should land somewhere, and **synonymy is a fact to record, not an
  instruction to deduplicate.** Two rounds of no new predicates against 59 concept
  renames is the converged-relations/forked-concepts asymmetry above, measured a
  second time.
  Round 17 added **three**, and the first is the highest-recurrence predicate the
  corpus had left unpromoted: `indicatesInQueryPlan` (8). Every other predicate here
  says what the product *does*; this one says what it *shows*, and the indexing
  documentation is built on that distinction — a reader is told to check `EXPLAIN` for
  `index_group_aggs` to find out whether a pushdown happened. `appliesToIndexType` (4)
  gives the type axis a predicate pointing *at* it, and `eliminatesFetchFrom` (3)
  finally separates **covering** an index, where the fetch never happens, from
  **pushing down**, where it happens on fewer documents — two mechanisms the registry
  had only been able to describe with the same words. `isSupportedOnStorageMode` was
  refused at 1, and `requiresMinVersionFor` remains unpromoted at 5 files because it
  is a fold into `availableSince`, not a candidate.
- **`docs-issues/`** — a deliberately minimal, deliberately promiscuous log of
  content-quality findings (missing documentation, apparent doc-duplication,
  unadapted shared-source content, empty stub pages) that are *about the docs*,
  not about Couchbase — kept separate from `concepts/` and `relations/` so the
  product ontology doesn't grow a parallel meta-ontology of
  documentation-about-documentation. Each entry is just `{id, type: "docs-issue",
  issueType, description, about, status}` — minted with no gatekeeping. **135
  entries** as of round 19. The filename convention is `<product>-<slug>`, and since
  round 16 a reference to a `docs-issues/` slug with no file behind it is a
  `verify-registry-ids.py` failure: two references written in earlier rounds pointed
  at the un-prefixed name and nothing noticed for four rounds, which fails in the
  worst direction — a promoted record says "see `docs-issues/X` for the
  contradiction", a reader finds nothing, and concludes the caveat was never real. Round 14 added **none**, and that was a result rather than
  an omission: round 14 read no pages, and this bucket is for facts about the
  documentation. Its writeup first named four new entries; writing the files closed
  none of them. Two were findings about *this registry* wearing a docs-issue's
  clothing (an id fork across two trees, an unmodelled quantity), and two were
  factually wrong about the page they described — a table row said not to identify
  its columns, which a header row two lines above it does, and a concept described
  as "documented only as a link target" that has a dedicated 200-line page in both
  trees. The rule the episode produced: **an extraction record is evidence about a
  page, never a substitute for one.** Records are lossy by design — they hold the
  sentences an agent chose to quote and none of the structure around them — so a
  round working from records alone can reason about the registry and must go back to
  the file before asserting anything about the docs. Round 13 added 4 and rewrote 1 — the rewrite being the
  more useful half: `server-role-label-does-not-match-internal-name` claimed 2
  instances where there are **20 of 55**, had inherited round 12's "58 role tables"
  (the heading count, not the table count — 55 tables, 56 roles, one in prose only),
  and diagnosed the Manage/Use Sequences case backwards. An unmeasured docs-issue is
  a hunch with a filename. Round 15 added **1**, and the measurement is the entry:
  the CURL access-list table appears on `curl.md` and `query-settings.md` with
  byte-identical descriptive cells (244, 429 and 389 characters, counted), neither
  page cross-referencing the other's copy, and the duplicated prose carries a
  fail-open security condition. It also had a measurable effect on the registry —
  two agents reading the two pages minted the same three properties independently,
  which is the whole of `n1ql:curl-all-access`'s recurrence 2. Three further
  candidates that round were examined and **rejected** as facts about the product
  rather than the documentation (an inverted `-1` sentinel, a setting documented
  under two spellings, a "whitelist" whose properties are named allowed/disallowed).
  Round 16 added **6**, all of them about index documentation and all found by
  reading the pages the namespace rewrite kept pointing at: index pages relocated
  between versions (the finding that makes `server/8.0/indexes/` round 17's scope),
  an index-type taxonomy that mixes kinds with storage modes, **two enumerations of
  the index types that do not agree with each other**, "storage engine" naming two
  different layers on two pages of one module, three unreconciled index/indexer state
  vocabularies, and a `status` field documented with four values in Server and three
  in Capella. The last two are the ones an SME could settle in a sentence, and one of
  them licensed the round's fold: the Server/Capella sentences are identical to
  within one word, which is what made `capella:index-ui-status` and
  `indexer-node-state` the same enum.
  Round 17 added **11**, the highest count since round 11 and for the same reason —
  reading pages rather than records. The one to act on first is
  `server-sequential-scan-switch-on-procedure-uses-xor`: the N1QL Feature Controller is
  a disable **mask**, "switch off" correctly documents OR with `16384`, and "switch on"
  documents **XOR**, which toggles rather than clears. Starting from `76` — the value
  the page's own earlier example uses as a typical enabled state — the documented
  procedure yields `16460` and **disables the feature the reader was trying to
  enable**; the correct operation is AND NOT, and the page's own example hides it by
  assuming the bit is already set. It compounds with
  `server-n1ql-feature-controller-named-four-ways` (four spellings across four
  surfaces, on a bitmask the docs say is "usually reserved for support purposes", so
  the reader most likely to run the procedure is an administrator on a production
  cluster). Two are notable for how they were found: the extracting agent
  **deliberately declined to extract** Table 1 of `groupby-aggregate-performance.md`,
  which marks SUM and COUNT unsupported for the commonest case that thirteen of the
  same page's examples demonstrate, rather than put a false negative into the ontology
  with a quotable citation behind it — the failure the evidence gate cannot see,
  because the quote is verbatim and the table really says that. And
  `server-index-pushdowns-version-facts-removed` records a consequence for this
  registry rather than for a reader: the 5.5 MIN/MAX history was **deleted** between
  7.2 and 8.0, so a correctly-extracted, still-true `availableSince` relation now
  quotes a sentence that no longer exists, and **nothing distinguishes "unquotable
  because fabricated" from "unquotable because the docs changed."** The rest:
  prose contradicting tables on `index-scans.md` (four instances, surviving in all
  three copies), the `exact` flag that decides pushdown versus early filtering shown
  ~30 times and defined on another page, a module hub page with no way out of it, an
  operator named in two callouts and present in no plan on the page, eight names for
  three services across five pages, and a 1730-line page published byte-identically in
  two products. `server-index-state-vocabularies-inconsistent` was **updated rather
  than duplicated**, and its increment kills the simplest reconciliation: "the indexer
  goes into the Paused mode on that node. Although the indexes remain in `Active`
  state" — two subjects holding simultaneously, so the two values cannot belong to one
  enum.
  Round 18 added **12**, headed by `server-eventing-worked-examples-rbac-gate-missing-from-capella`:
  all nine Server worked-example pages carry the identical Full Admin/Eventing Full Admin
  gate sentence, absent from every Capella twin — round 8's own extraction had flagged
  the absence without an explanation, and this round supplies one (Capella's access
  model for Eventing is project-scope roles, a materially different shape). Second:
  `server-eventing-memory-quota-premise-contradicted`, filed against this round's *own*
  dispatch briefing, which asserted Capella auto-manages Eventing memory without checking
  it — one of the round's own batches, reading a Capella page for background exactly as
  instructed, found Capella's own FAQ stating a user-configurable memory-quota knob in
  near-identical wording to the Server page. The rest: an LCB error code documented as
  `272` on one page and `1` on its sibling for the identical error object, four
  version-since badges present on Capella pages with zero counterpart on the otherwise
  byte-identical Server twins (consistent with a rendering macro rather than four
  independent omissions), a REST API reference using two different port/path schemes
  for the same kind of setting, and five smaller concretely-diagnosed inconsistencies
  (a copy-paste log message, an undocumented handler parameter, stale cleanup
  instructions naming the wrong example, a goal description that doesn't match its
  handler's behaviour, a role label drift). One correction rather than a new filing:
  round 8 characterized a broken cross-reference as Capella-specific unadapted content;
  round 18 confirms the identical break is on the Server 8.0 original too.
  Round 19 added **7**, headed by `server-cbbackupmgr-edition-and-role-three-way-contradiction`:
  `cbbackupmgr.md` states the tool is Enterprise-only, `enterprise-backup-restore.md`
  contradicts that directly and adds that only Full Administrators may use it, and the
  tool's own RBAC sections contradict *that*, showing bucket-level work needs only the
  narrower `data_backup` role — three pages, none cross-referencing the others. The
  rest: a best-practices page recommending a strategy without repeating that the
  command it depends on is Enterprise-only, a storage-format change large enough to
  retire a whole command landing in the same release as a new feature with no stated
  connection between the two (`needs-sme`), a third backup-type value in the tool's own
  output that the promoted two-member enum doesn't cover, two independently-designed
  "key protected by a secret" encryption mechanisms with no stated relationship, and
  two `javascript-udfs/` findings — unadapted "in Capella" wording on two Server pages
  where a sibling page has the correctly adapted text for the identical sentence
  (proving the adaptation was attempted and applied inconsistently), and one version
  badge dropped where an adjacent one on the same page was kept.
  Round 11 had 76 entries, having added 21 from just
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
  Round 15 added two **id-shape** rules, and they are deliberately forward-only:
  they apply to `minted` ids only, so nothing already on disk is retroactively
  illegal and no migration is implied. A new id may not use a plural namespace when
  the singular already exists in the registry (`indexes:` when there is `index:`,
  `tools:` when there is `tool:`), and may not carry a file extension
  (`rest-api:compaction-rest-api.adoc` is a page, not a concept). Both mistakes are
  in the corpus, both cost a later round a rename sweep, and reuse of the existing
  spelling is still allowed — which is the point. This is the control point that
  makes "from now on" true rather than aspirational: reuse whatever the corpus has,
  mint nothing new that repeats these two mistakes.
  Round 16 added the rule that **withdraws** that permission for a namespace a round
  has retired: no id under a prefix in `hooks/retired-prefixes.json` is accepted at
  all, whatever its `registry_status` says. Reuse-is-allowed was right while a
  namespace was merely misshapen and wrong once it had been rewritten out of the
  corpus — every `indexes:` id now resolves to an `index:` id, so accepting the old
  spelling re-creates the fork the round spent 59 renames closing. The rule reads
  relation **subjects and objects** as well as `concepts[]`, and that is the whole
  reason it catches anything: 376 of the corpus's 2,112 ids — 18% — appear only in a
  relation slot and are never declared in any record's `concepts[]`. Denials are
  deduped per record, since one retired id declared once and used as nine objects is
  one mistake, not ten.
- **`hooks/test-gate.py`** — 30 crafted `PreToolUse` payloads fed to the hook as a
  subprocess, added in round 15 when the gate acquired rules that are not "is this
  sentence on the page". Its own construction is the finding. The obvious fixture is
  a real extraction record, and a real record **fails**: replaying a round-12
  security page produces five denials, because `registry_status` describes the
  registry the record was written against, and 200 promotions later `minted` is a
  false claim about ids the registry now has. So **a control's verdict can expire**,
  and two things follow — do not re-run the gate over the corpus as an audit, and
  do not "fix" old records to match today's registry, because the declaration was
  true when it was made. The fixtures are synthetic, built from long-stable
  promoted terms.
  Round 16 is where this file earned its second keep: the retired-prefix rule
  *withdraws* a permission, so one assertion here **flipped from allow to deny** —
  "reusing an `indexes:` id is allowed" was a correct test of round 15's design and is
  a wrong test of round 16's. A flip like that belongs in this file with the reasoning
  written beside it, because in a diff it is indistinguishable from a test loosened to
  make a change pass. The seven new cases pin the rest: a retired id is refused under
  all three `registry_status` values, in the subject slot and in the object slot alike,
  and the one namespace round 16 deliberately did **not** sweep (`cloud-providers:`,
  one live occurrence) is asserted to still be allowed — so "not yet retired" is a
  tested state rather than an absence.
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
  Scans `reconciliation.md` for `ns:kebab-id`, `camelCaseTerm` and (since round 14)
  long-kebab docs-issue slugs, and
  lists those with no registry file, closing the "narrated as promoted, never
  actually filed" gap that had recurred in rounds 2, 3, 5, and 8. It can't
  distinguish "claimed as promoted" from "named while being rejected, folded or
  deferred" — the prose says which, the string doesn't — so its output is a
  short list to read each round, not a diff to clear. Its first run surfaced 5
  genuine gaps; re-running it after round 10's writeup was finished surfaced 3
  more (including `n1ql:scan-consistency` at recurrence 6, whose own extraction
  record claimed it was "already promoted"). All 8 were promoted the same day.
  A control that pays out twice on the round that introduced it is doing real
  work, not cleanup. Round 14 found the gap in its *coverage* rather than in its
  logic: three artefact families are written by hand each round and this scanned
  two, so a writeup naming four new `docs-issues/` entries and filing none of them
  drew no comment. Slugs are now scanned too. **A control's coverage is itself an
  unchecked claim** — the way to find out what a check does not look at is to be
  wrong in that place first.
- **`recurrence.py`** — the aggregate query the whole promotion rule rests on:
  distinct-file counts per predicate and per concept over the entire
  `extractions/` tree, resolving aliases and both id spellings, with
  `--unpromoted-only` for the backlog, `--variants` for ids that are one term
  spelled two ways, `--forks` for one local name spelled in two namespaces, and
  `--findings` to dump the finding fields in full. It has
  been wrong in **twelve** distinct ways across rounds 10–17, every one caught because
  the output looked implausible and none by anyone reading the code, so all twelve
  are pinned as regression cases in `--selftest` (32 checks) — the point being that
  its corrections accumulate rather than being re-derived from memory each round.
  The worst was structural rather than a bug: until round 12 it counted only the
  **object** slot, so any concept a page was *about* was invisible to the promotion
  signal, which had hidden 276 candidates since round 1. Bug #10, found in round 14,
  is the reason `--selftest` matters more than the fixes it records: round 11
  excluded `seeAlso` from the concept ranking, round 12 broadened the ranking from
  the object slot to *either* slot, and the second change silently cancelled the
  first, because the exclusion lived in the branch the broadening replaced. Page
  titles counted as concepts again for two rounds. **Two correct fixes to the same
  query cancelled**, and what was missing was not care but a test pinning the
  earlier fix to a named instance — which the three new cases now are.
  Bug #11, found in round 16, is bug #10's other half and the worst of the eleven by
  reach: the same round-14 exclusion also applied to the **census** — the column
  headed "any mention" — so **376 ids, 18% of the corpus, appeared in no report this
  script produces**, including `--variants`, whose only job is to find one term spelled
  two ways. Five misspellings of promoted SQL++ statements were hiding there, each
  causing gate denials nobody could account for, and a concept with 14 files behind it
  read as recurrence 0. The lesson is not "test the code" but a design rule now
  enforced by `scan()`'s shape: **excluding a relation kind from a metric and excluding
  it from a census are different decisions**, and doing the first by editing a shared
  code path silently does the second. `scan()` returns `mentions`, `slots`, `labels`
  and `see_also_objects` as four separate tables, so a caller has to say which
  question it is asking.
  Round 16 also added two reports, deliberately separate from each other and from the
  ranking. **`--page-ids`** measures the *part of speech* problem wave 2 named: 392 of
  2,116 ids (18%) are only ever linked to and never labelled — page ids wearing concept
  clothing, which a corpus-wide `page:` sweep would fix and which is still on the
  backlog. **`--stale-recurrence`** compares every promoted record's `recurrence` field
  against the query: **153 of 324 agree (47%)**. None of the other 171 is a bug — the
  instrument has been replaced three times — and the report is **read-only on
  purpose**, because auto-refreshing the fields would trade the only record of what
  each round measured for agreement with a query that has been wrong three times. It
  exists because this round's own first draft believed a stale field over the query and
  wrote a false causal story from it.
  Bug #12, found in round 17, is the one that had been costing promotions rather than
  reports: `variant_key()` strips punctuation and **keeps the prefix**, so
  `index:early-filtering` and `n1ql:early-filtering` never cluster. A term forked across
  two namespaces has its files split across two rows and sits below the bar *twice*,
  reading as two weak terms instead of one adequate one — the exact inverse of the
  variant problem `--variants` was built for, and invisible to it for seventeen rounds.
  `--forks` reports **62 local names spelled in more than one namespace, 20 of which
  would cross the bar only if merged**. It is deliberately a list to check and not a
  defect list: the registry keeps five unrelated things called "role" apart on purpose,
  and round 17 confirmed `data:kv-range-scan`/`sdk:kv-range-scan` and
  `index:index-partitioning`/`fts:index-partitioning` are genuinely different things.
  Any tool that compares suffixes will flag those, which is why the report's job is to
  hand a human a short list.
- **`shared-source.py`** — round 17's other new instrument, and the counterpart to
  `--forks`: it measures the direction in which the promotion rule **over**-counts.
  "Two distinct files" is a proxy for "two independent attestations", and it fails
  because Couchbase publishes one Antora module on several branches — three copies of
  `indexing-and-query-perf.md` are one authored page, and
  `groupby-aggregate-performance.md` is byte-identical (1730 lines, similarity **1.00**)
  between Server and Capella. It clusters near-duplicate pages by basename with a
  difflib ratio (`--clusters`, default threshold 0.75), lists the ids whose recurrence
  rests partly on a shared source (the default report; `--clusters` stops at the pages,
  `--kind` restricts which duplications count), and — the part that decides
  anything — `--check` asks whether a *specific* id's evidence rescues it: **a quote
  present on its own copy and absent from every sibling copy** is an independent
  attestation regardless of how similar the pages are. Corpus-wide: **95 clusters over
  195 extracted pages, 293 discounted ids** (`shared` 173, `divergent` 108, `unchecked`
  12), **103 below the bar** once the discount is upheld — up from 5 before round 17,
  because extracting a module that exists in three trees buys density and not
  independence, and round 18's `eventing:` module turned out to be the most heavily
  duplicated pairing in the corpus (0.89–1.00 page-similarity, more than doubling the
  cluster count in one round; round 19's `javascript-udfs/` pairing added a fourth
  cluster at 0.92–1.00 with its similarity known before dispatch, which is why it minted
  nothing new against the discount rather than adding to the below-the-bar count).
  Two rules are enforced in code rather than left to a reader.
  `effective()` makes **the verdict decide which count applies**: `divergent` rejects
  the discount and licenses the raw file count, `shared` upholds it, and `unchecked`
  settles nothing and is never marked below the bar. And the report says
  `**NEEDS A READER**` rather than a number wherever nothing is settled. That function
  exists because the first version of `--check` did not have it and printed
  `**BELOW THE BAR**` on `index:sequential-scan 2 -> 1 divergent` — a refusal justified
  by a number the same row had just rejected — which is bug #12's own shape occurring
  inside the tool built to detect it. `--selftest` (22 checks) pins it on the round's
  real rows. It imports `recurrence.py` for id resolution, so the two cannot disagree
  about what an alias means.
- **`verify-registry-ids.py`** — a **gate** (exits non-zero), written in round 13:
  every record's declared `id` must mirror its own file path, since round 14 no alias
  may be a mere punctuation variant of its own target, and since round 16 every
  `docs-issues/<slug>` a record points at must have a file behind it. 636 records, 0
  problems. It exists because nine `concepts/version/` records had drifted
  (`server-6-5.json` declaring `.../version/server-6.5`) and the consequence was
  not cosmetic: the pipeline derives ids from **paths** while agents copy them from
  **`id` fields**, so agents wrote the dotted form, the write-time gate denied them
  as unpromoted, and the term landed in the backlog with nothing indicating the
  registry had caused it. Two agents diagnosed it correctly in their notes and a
  reconciliation pass recorded it as *their* error. `pages/*.jsonld` is excluded:
  its `@id` is the described page's public URL, a resource the registry names and
  does not own — the rule is about ownership, not about strings. The round-16 addition
  found two references four rounds old pointing at un-prefixed docs-issue names
  (`docs-issues/dcp-name-drift` for `server-dcp-name-drift`), which is the
  `verify-promotions.py` failure shape in the opposite direction — narrated as
  existing, filed under another name — and it scans a record's serialised text rather
  than named fields, because these references live in free prose across at least seven
  keys and enumerating the keys would just be a list to keep up to date.
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
  over the whole corpus: 582 records, 3,522 relations, and a problem count identical
  on both sides of every run — 452 across 151 substitutions in 67 files (round 13), a
  further 224 in 24 files (round 14), and a further 101 in 14 files (round 15, now
  against a baseline of 443). Round 14 added two things to it. A **rule** (`version:` ids get dots
  replaced with dashes, forever) rather than another table entry, because a table
  needs a new line per release and is wrong by construction on a namespace whose
  members arrive with every product release — round 13's eight entries missed four,
  and round 14 found two more. And a **whole-namespace rename**
  (`vector-index:` → `vector-search:`), resolved after exact matches and rules so
  that an id evacuated to another namespace by name is never also swept by its old
  prefix. That resolution order matters: nine `vector-index:` members went to
  `index-type:`, `n1ql:` and `vector-similarity-metric:` while the remaining 25 rode
  the prefix rule. Rewriting rather than aliasing is the right call at that size —
  25 aliases would be 25 dead twins — which makes the **size** of a change part of
  the alias-or-rewrite judgment, not just its kind.
  Round 15 needed the opposite shape and got the table instead of a rule: dissolving
  `setting:` is 34 exact-match entries, because **a dissolution's destination is not a
  function of the id**. Wave 1's rename compressed 25 ids into one prefix line; wave
  2's `setting:query-max-parallelism → n1ql:max-parallelism` cannot be computed from
  the string, only decided by reading what the setting configures. 40 renames, 101
  substitutions, 14 files, and three of the destinations are ids the registry already
  had — so the table is also where a *merge* gets expressed, which no prefix rule can
  do.
  Round 16 is the largest sweep so far and used both shapes at once: **59 renames, 160
  substitutions, 36 files** — one prefix rule retiring `indexes:` wholesale, plus exact
  entries for the ids whose destination had to be decided (`indexes:covering-index`
  and four other spellings of one concept collapsing into `index:covering-index`,
  `index-type:moi` leaving the type axis because a storage mode is not a kind of
  index). `indexes:`, `vector-index:`, `setting:`, `setting-scope:` and `tools:` are
  all at **0** occurrences afterwards; `cloud-providers:` is deliberately left at 1,
  since round 14 renamed it without settling the relation split underneath it, and a
  namespace half-retired is worse than one openly pending. The round also added a
  third alias state, because two were doing three jobs: `aliases` is a spelling
  deliberately left **live** and resolved by the gate, a rewrite leaves the old
  spelling **dead**, and **`folded_spellings`** records a spelling that was rewritten
  out — history, read by nothing, and the answer to "why does the log say this id was
  renamed when the registry has never heard of it". 21 aliases were retired this round
  by moving them there.
- **`candidate-evidence.py`** — the namespace pass's reading tool, written in round
  14. `recurrence.py` answers "is this term real?" by counting distinct files, and
  is structurally unable to answer "do this namespace's members answer the same
  question?" — so this dumps every mention of a candidate id, or of a whole
  namespace (`--ns vector-index:`), with the page, the relation slot, the predicate
  and the evidence quote, plus whether the id is already promoted under another
  name. It answers three questions the ranking cannot: is this already promoted
  under a different spelling, is this a concept or a page id, and do these members
  share an axis. Its file counts are every mention — `concepts[]` membership and
  `seeAlso` included — and are deliberately **not** the promotion metric, which
  excludes both; the output says so on every run, because a term is routinely 4 here
  and 1 there.
  Round 15 put the quotability check on this path too: every printed quote is checked
  against the page it cites, an unquotable one is marked `!! UNQUOTABLE` inline, and
  `--audit` reduces a run to just the ids that have one. `verify-evidence.py` could
  always find these; the difference is *when* it runs. The reconcile skill says to
  scope the audit to the round's new batch, which assumes a round has one — and a
  registry-input round doesn't, so rounds 14 and 15 promoted concepts out of records
  written in the first POC commit with nothing re-checking them. One such promotion
  quotes a sentence that is verbatim on a *different* page in the same directory than
  the one the relation names, which is the entire reason `evidence_source` exists, and
  it cost a recurrence: credited to the page that carries it,
  `vector-search:product-quantization` drops from 2 files to 1. The gate protects
  records as they are written; **promotion reads records written long before it
  existed**, so the check now sits on the action a coherence pass actually performs.
  Fixing a false positive in the shared `norm()` was the precondition: this Markdown
  snapshot escapes punctuation, so a record quoting `completed_requests` failed
  against a page that says `completed\_requests` — 9 of 322 corpus failures, and an
  alarm that includes non-defects is an alarm people learn to skim.
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
    of accumulated damage, not one bad agent. (The current figure is **313
    unquotable plus 130 with no evidence at all, 443 of 3,522**: round 15 removed 9
    false positives by de-escaping Markdown punctuation in the comparison itself, and
    round 16 re-derived the total after five rounds of quoting the older number.
    Nothing was repaired — the fix for rounds 1–9 is re-extraction, which is a
    tracked next step and not a reconciliation task.) Worst affected: round 3's
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
    at the intent of records from eleven rounds. Round 15 found the second instance
    and it is worse than a synonym problem: `n1ql:encoded-plan` was promoted with
    `recurrence: 2` when it was the subject of one relation in one file and the object
    of none — the 2 counted *relations*. So **a recorded recurrence is a claim nothing
    re-checks after the round that wrote it**, and the only reason this one surfaced is
    that a fold happened to recompute it. The same round found the deeper version:
    recurrence counts *pages*, and pages duplicate each other, so byte-identical prose
    on two pages is two files and one statement — `n1ql:curl-all-access` is recurrence
    2 by the metric and 1 editorially. Unified, the four ways the metric misreports
    (a per-item rule that never brings a namespace up for decision; a canonical
    reference table that mints its rows at recurrence 1 by construction, so *the better
    the documentation, the less promotable its contents*; tier and spelling splits that
    make one concept several rare ones; and duplicated pages that make one statement
    several files) are all one thing: **recurrence measures repetition, and repetition
    is an editorial property of the documentation, not of the concept.**
67. **The loud half of a variant problem hides the quiet half.** A promoted term
    read as unpromoted is loud — it shows up as a big number in the backlog. A
    genuine candidate held *below* the promotion bar because its count is split
    across two spellings shows up as nothing at all. Five terms had silently
    suffered it, including `n1ql:explain-function` at recurrence 7, split between
    `explainfunction` and `explain-function` and invisible to every round.
    Variant clusters went 16 → 1. Note two limits, both found the hard way.
    `--variants` keys on typography, so it catches `createfunction` and never
    `Application Access` vs `bucket_full_access` — the reason role ids are now filed
    under internal names rather than display labels. And it originally clustered the
    corpus against *itself*, so a spelling the corpus used **uniformly** while the
    registry used another gave a cluster of size one and was skipped silently: the
    worst case, since every file using it was gate-denied. Three clusters were
    invisible for that reason, one at 6 files (`version:sgw-3.0` against the
    promoted `version:sgw-3-0`) — the round's own headline defect, hidden from the
    check written to enumerate it, and caught only when a by-namespace summary of
    the remaining backlog put it on screen. The registry is now seeded in as a
    speller, asserted by `--selftest` as bug #8.
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
**Round 14 (no new pages) — the namespace coherence pass, wave 1:**

70. **The unit of reconciliation decides which defects are visible.** Thirteen
    rounds reconciled by *rank*: take the highest-recurrence candidates, decide each
    on its merits. Round 14 reconciled by *namespace* and immediately found two
    defects that are invisible per-item and obvious per-group — a prefix asserting
    an axis whose 30 members answered five different questions, and a term promoted
    at recurrence 2 sitting beside its own unpromoted spelling at 5. Neither is a
    judgment anyone got wrong; both are questions the per-item view cannot ask. The
    uncomfortable corollary: there are presumably other units — by predicate range,
    by source tree, by competency question — each making a different class of defect
    obvious, and no reason to think these three are the last.
71. **A namespace's name is an unchecked assertion.** The registry uses two kinds of
    namespace and both are legitimate: **subject areas** (`eventing:`, `capella:`,
    `monitoring:`, `backup:`, `sgw:`) and **closed axes** (`index-type:`,
    `index-class:`, `auth-mechanism:`). `vector-index:` was named as the second and
    populated as the first, for three rounds, and nothing in the pipeline compares a
    prefix against what it holds. So the fix was a *rename*, not a dissolution — the
    remainder is a perfectly coherent subject area, and only the name claimed
    otherwise. One mechanical check would have caught the sharpest instance: the
    corpus asserts `service:search-service -providesIndexType->
    vector-index:search-vector-index`, where the predicate names the axis and the
    object's namespace contradicts it. A range check on predicate slots — still
    unwritten — turns that from a reading task into a write-time denial.
    Wave 2 found the third case, which is neither kind: `setting:` was named like a
    subject area with **no subject to be about** — a part of speech, not a topic. The
    test that separates the two legitimate kinds from that one is **whether membership
    is closed and enumerable**: `edition:`, `auth-mechanism:` and
    `vector-similarity-metric:` are, and `setting:` cannot be, because a product
    acquires settings for as long as it is developed. That distinction also decides the
    *remedy*, which is the part that costs: a namespace named wrongly gets a rename and
    a one-line prefix rule; a namespace with no subject gets a **dissolution**, and
    since a dissolution's destination is not a function of the id, it is one decision
    per member — 34 of them, read one at a time.
72. **Two correct fixes to the same query can cancel.** Round 11 excluded
    documentation pages from the concept ranking; round 12 broadened that ranking
    from the object slot to *either* slot; the second silently undid the first,
    because the exclusion lived in the branch the broadening replaced. Two rounds of
    promotions then ran on a metric that counted page titles, and 27 of 203 backlog
    items turned out to be pages — `search:customize-index`, 24 relations, every one
    a `seeAlso`, labelled "Customize a Search Index with the Web Console". What was
    missing was not care but a test pinning the *earlier* fix to a named instance.
    Two things worth keeping apart, though: dropping out of the queue is not a
    verdict that an id denotes a page. `index-type:covering-index` is `seeAlso`-only
    and a perfectly real concept whose links were all mis-typed — **the label
    settles it, not the predicate.** A page id labels itself with a page title; a
    concept labels itself with a noun phrase.
73. **A refusal recorded on a record is invisible to the round that acquires the
    missing evidence.** Round 11 declined to relate the two vector index types by
    `tradesOffAgainst`, on the correct grounds that `indexes.md` never compares
    them, and wrote the refusal into the record. The comparison existed in the
    corpus all along — "A key difference between Hyperscale and Composite Vector
    indexes is how they handle scalar values in queries" — under the *other*
    namespace's ids, where nothing joined it to the record doing the declining. The
    refusal was right and unretractable by design. This is the same shape as the
    round-11 agent finding ("FOUR NAMESPACES, ONE LIST … the fix is a reconciliation
    decision") that sat unactioned for three rounds: **reconciliation acts on the
    parts of a finding that map onto its existing outputs and drops the parts whose
    remedy is refactoring records already promoted.** Four instances are now on the
    board, and there is still no output shaped like "re-examine a recorded refusal".
74. **A rule enforced on one slot of a record is not enforced on the record.** One
    shape, found three times in a single round: `seeAlso` excluded from the metric's
    object slot but not its subject slot; `providesIndexType` checked as a predicate
    name but not against its object's namespace; and "never write `current` into an
    id" enforced on `page_id` and the output path while **86 `seeAlso` objects
    across 21 files** name a page through the `current` alias that will move on the
    next major release (30 of them also keeping a `.md` extension, 7 an `#anchor`).
    In each case the invariant was written down correctly and applied at the
    position where it was first violated.
75. **A control's coverage is itself an unchecked claim.** Round 14's writeup named
    four new `docs-issues/` entries and filed none of them, and
    `verify-promotions.py` — the control that exists precisely to catch "narrated as
    promoted, never filed", after four recurrences — reported nothing, because it
    scanned concept ids and predicate names and had never looked at docs-issue
    slugs. Three artefact families are hand-written each round; the check covered
    two. Extending it took eight lines and it immediately surfaced all four phantoms
    plus a fifth entry the same section referenced and that never existed. The way
    to find out what a check does not look at is to be wrong in that place first.
76. **A gate-passing quote can under-determine its own triple.** Three
    `availableSince` relations quote the identical table row
    `| **First Available in Version** | 8.0 | 8.0 | 7.6 |` as evidence for three
    different objects. All three are right; nothing in the evidence could have told
    you if one were wrong, because what disambiguates the row is the header row two
    lines above it — the table's *geometry*, not any quotable line. This is a new
    species alongside round 10's "quotable but mis-objected": verbatim, on the right
    page, about the right subject, and equally supportive of three different claims.
    A gate that compares strings cannot reach it, and nothing in the schema lets
    tabular evidence carry its header along with the cell.
**Round 15 (no new pages) — the namespace coherence pass, wave 2:**

77. **A control's verdict can expire, and a verification instruction can assume a
    fact about the round.** Building `hooks/test-gate.py` started from the obvious
    fixture — a real extraction record that passed the gate when it was written — and
    it now produces five denials, because `registry_status` describes the registry the
    record was written *against*, and 200 promotions later `minted` is false about ids
    the registry has since acquired. The record was true when written and is false now,
    with no edit to either side. Two consequences: the gate cannot be re-run over the
    corpus as an audit, and old records must not be "fixed" to match today's registry.
    The same shape on the instruction side — the reconcile skill says to scope
    `verify-evidence.py` to the round's new batch, which silently assumes a round has
    one. Rounds 14 and 15 had no new batch and rewrote ids across the whole corpus, so
    the verification step verified nothing while the round's real risk was elsewhere;
    the promotions it made were licensed by records from the first POC commit, and one
    of those quotes a sentence from a page it does not name. **A check is scoped to a
    kind of round, and a round can change kind.**
78. **The enum checks the id and never the referent.** `registry_status: minted` was a
    *true* declaration for `setting:scan-consistency`: no file had that id. The thing
    it denotes had been promoted for five rounds as `n1ql:scan-consistency`, and the
    same round's reconciliation promoted it again. Three of `setting:`'s 34 members
    were duplicates of this kind, and the gate could not have caught one of them,
    because "is this id in the registry" and "is this *thing* in the registry" are
    different questions and only the first is mechanical. A tier or a part of speech in
    the id is what makes a duplicate look like a different thing —
    `setting:collection-max-ttl` against the promoted `data:max-ttl-setting`. The
    remedy is not a stronger gate but the reading pass: this is exactly what a
    namespace coherence wave is for, and it is why aliases get written rather than the
    duplicate being deleted.

**Round 16 (no new pages) — the namespace coherence pass, wave 3 (`indexes:`,
`index-type:`, `index:`):**

79. **Excluding a relation kind from a metric is not excluding it from a census.**
    Round 14 removed `seeAlso` from the concept-promotion metric for a good reason — a
    link between pages is not a claim about a term — and, because the exclusion lived
    in a shared code path, removed 376 ids from the corpus **census** at the same
    time. **18% of the corpus appeared in no report this project produces**, including
    `--variants`, whose only job is to enumerate spellings. Five misspellings of
    promoted SQL++ statements were hiding in the gap, each causing gate denials nobody
    could account for, and a concept with 14 files behind it read as recurrence 0. The
    shadow-prefix count quoted in the last two rounds' writeups (43) was measured with
    the same blind instrument and is really 55. The fix is structural, not careful: a
    census must not share a code path with a metric, because the two differ precisely
    in what they are allowed to ignore. And the general form is worse than the bug —
    **every number in these writeups inherits the instrument that produced it, and
    nothing records which instrument that was.**
80. **An id names its subject, not its location.** `covering-index` was spelled five
    ways across three namespaces, and the cause is mechanical rather than careless:
    `covering-indexes.md` lives at a different path in each of four doc trees
    (`n1ql/n1ql-language-reference/`, `indexes/`, `learn/services-and-indexes/`), and
    an agent minting an id from the page in front of it produced a different prefix
    each time. No pass that reads one page at a time can see this, which is why it
    took a namespace wave, and it is the same defect `tool:cbq-shell`,
    `protocol:dcp` and `tool:cbbackupmgr` each turned out to be. The rule is the fix,
    and it is checkable at mint time in the one case that matters: a prefix that names
    a directory is a smell.
81. **A namespace can be a plural fork rather than an axis or a subject area.**
    Wave 1 found a namespace named like an axis and populated like a subject area;
    wave 2 found one named like a subject area with no subject; wave 3's `indexes:`
    was neither — it was **`index:` with an `s`**, 30 ids that would have been filed
    under the singular by an agent who happened to see a different page first. Retired
    wholesale, which makes it the cheapest of the three remedies and the one the gate
    can now prevent recurring. `index-type:` kept its axis and shed two members that
    were never types (`moi` and `standard-gsi-plasma` are storage **modes**), and the
    round's one hard call went the other way: **`covering-index` is not a type either**,
    because the docs define it *after* index selection — **a type you cannot know at
    `CREATE INDEX` time is not a type** — so it is filed in `index:` at recurrence 0
    on the promotion metric and 14 files in the census, on the semantic-weight
    exception.
82. **A `recurrence` field in a promoted record is a measurement with a date, and it
    carries neither.** `--stale-recurrence` puts **153 of 324 promoted records (47%)**
    in agreement with the current query. None of the other 171 is a bug: the
    instrument has been replaced three times, and each field records what was true
    when a human wrote it. The danger is that **a record's prose reasons about its own
    weight** — "a minor, low-stakes promotion", written of a term now at recurrence
    8 — and the next round reads the prose. This round's first draft did exactly that,
    believed a stale 2, and wrote a false causal story about what a fold had achieved.
    The report is therefore deliberately **read-only**: a stale measurement is data, a
    silently refreshed one is a lost audit trail.
83. **The corpus is not the documentation.** `server/8.0/indexes/` — 11 pages, the
    canonical documentation of the subject this wave spent its whole length
    reorganising — has **never been extracted**, because round 12 went looking for
    those pages under `learn/` after Antora had already moved them out of it. So every
    recurrence figure in this wave is partly a fact about which directories nine
    rounds happened to walk, and a term's thinness in the corpus is not evidence of
    its thinness in the docs. This is the sharpest form of round 15's result:
    recurrence is an editorial property of *the sample*, and the sample was chosen by
    directory name. It sets round 17's scope, and it is why the three storage engines
    (Plasma, Forestdb, Nitro) were left unpromoted rather than promoted on one page's
    evidence.
84. **An alias is a claim about a referent, and nothing checks referents.** Wave 2
    found that the write-time enum checks ids and not things; wave 3 found the
    inverse risk in the remedy that wave prescribed. Resolving aliases before checking
    an id is what makes `promoted` decidable — and it makes an alias the one field in
    the registry that can make two genuinely different things pass as one,
    permanently and invisibly. This round wrote 21 in a single pass, and the only
    check on any of them was a person reading both records. `verify-registry-ids.py`
    catches the syntactic abuse; nothing reaches the semantic one. So the rule is
    procedural: **fold under an alias only where a source sentence licenses the
    identity, and quote the sentence in the record** — which is what
    `concepts/indexer-node-state.json` does for the POC's first deletion of a
    promoted record.

**Round 17 (22 pages, `server/8.0/indexes/` first contact + `cloud/indexes/`
re-extraction):**

85. **Re-reading pages the corpus already covered recovered 9.8× their content.**
    The eleven `cloud/indexes/` records, written in round 6 before the evidence gate
    existed, held **35** relations between them; re-extracted, the same eleven pages
    hold **343**, a mean of 3.2 rising to 31.2. First contact on the eleven
    never-extracted `server/8.0/indexes/` pages produced **400** at a mean of 36.4,
    against round 10's baseline of 13.4. This is the number round 16's "the corpus is
    not the documentation" was missing: the two failure modes it identified — a
    directory never walked, and a directory walked badly — present the identical
    symptom of a modest recurrence count, and between them they were hiding roughly
    nine tenths of the content of the module the previous three rounds spent their
    whole length reorganising. Pairing the two jobs in one round is what made either
    trustworthy: each batch was the other's diff-gate.
86. **A promotion is only as good as the set it counted.** The three storage engines
    were correctly identified, quoted and reasoned about in **round 16** — in this
    repository, in `docs-issues/server-storage-engine-used-at-two-levels`, reaching the
    same conclusion round 17 reaches. They sat at recurrence **0** because
    `recurrence.py` reads `extractions/`. The evidence was neither missing nor
    undiscovered; it was in a directory the counting tool does not open. Round 16's
    lesson was that a refusal is only as good as the set it searched; this is the same
    sentence one layer out, and any pipeline that decides promotions from a single
    directory will keep re-losing what the project has already worked out. (What
    settled the question itself is worth keeping too: **a one-to-many map ends a
    fold argument without appealing to anyone's intuition.** Standard index storage is
    backed by Plasma in Enterprise Edition and Forestdb in Community Edition, so
    `standard` cannot be another name for either.)
87. **A promotion metric's proxy fails in both directions, and only one direction had
    an instrument.** "Two distinct files" has stood in for "two independent
    attestations" since round 1. It **inflates** when one Antora module is published on
    several branches — 40 clusters over 85 extracted pages, 188 ids resting partly on a
    shared source, 38 of them below the bar once discounted, up from 5 before this
    round. It **deflates** when a term is spelled in two namespaces, because
    `variant_key()` keeps the prefix — 63 forked local names, 20 of which would cross
    the bar only if merged. And it **understates** independence when a reference page
    and a guide document one feature, which no count can see. Both instruments were
    built in this round and immediately **reversed four decisions in both directions**:
    `index-type:array-index`, `index-type:functional-index` and `index:sequential-scan`
    were rescued, and `index:duplicate-index` — three files that are three copies of
    one page — was refused despite having the round's most quotable defining sentence.
    Two rules fell out. **The verdict decides which count applies** (`divergent`
    rejects the discount, `shared` upholds it, `unchecked` settles nothing). And **a
    discount computed over a partial corpus is not conservative, it is wrong**: this
    round twice drafted a refusal on a mid-round count and twice found the completed
    corpus put the term at 2 or 3 independent sources. A proxy with no error bars gets
    reported as a measurement.
88. **The tool built to catch a bias can embody it.** `shared-source.py --check` exists
    to decide when a discount should be **rejected**, and its first report printed
    `**BELOW THE BAR**` on any row whose discounted count fell below 2, ignoring the
    verdict on the same line. So `index:sequential-scan  2 -> 1  divergent` rendered as
    a refusal justified by a number that row had just rejected, and the round came one
    step from refusing a candidate its own new instrument had vindicated. The cause is
    more useful than the bug: the discount is the interesting computation, so the report
    was organised around it and the verdict was bolted on as an extra column rather
    than as the thing that selects which column counts. Selftests written from real
    rows caught it; nothing else would have. **Quiet deflation is this project's
    recurring failure mode — it removes real evidence and leaves no trace.**
89. **Ask an evidentiary rule the other way round at least once.** The reconcile skill
    forbids merging two concepts "unless a source page states the relationship
    explicitly", and seventeen rounds applied it correctly — always as a test to
    *fail*. Nobody asked which sentences in the corpus **grant** the licence. There are
    **six**, findable by grepping two phrasings, and four of them are on
    `cloud/management-api-reference/index.md`, for a structural reason worth mining
    deliberately: its job is to document API field names, so wherever a field name
    differs from the documentation's word it says so. One of them folded Capella's
    Memory Only buckets into Server's ephemeral buckets *with a citation*, resolving a
    discrepancy the registry had carried since round 6 — and the cost of not having
    known is invisible by construction, because a refused merge and a genuine
    distinction produce identical output: two separate records. **A rule that is only
    ever used to reject has an evidence base nobody has counted.**

**Round 18 (67 pages, the `eventing/` module, first contact paired against round 8's
twin):**

90. **A pairing strategy's payoff has two independent axes, and a good result on one
    does not transfer to the other.** Round 17's indexes module delivered
    defect-finding *and* promotion-independence together; round 18 paired the same way
    against a module that turned out to be the corpus's most heavily duplicated
    (0.89-1.00 Server/Capella page-similarity, "all quotes appear on every copy" on
    most concepts). Defect-finding still worked (12 docs-issues, the RBAC-gate
    asymmetry); promotion-independence barely did, because there was no independence in
    the module to buy. **The two payoffs came apart for the first time**, and reading a
    paired round's output now means checking both meters separately.
91. **Eventing has four declared entry points, not two, and two of them were minted
    twice under names no existing instrument catches.** `eventing:on-deploy-handler`
    and `eventing:timer-callback` join the long-promoted OnUpdate/OnDelete pair -
    both had been named on pages already in the corpus since round 8, just never filed.
    Both were also independently minted a second time: one a hyphen variant
    (`--variants` catches it), one a same-prefix synonym fork -
    `firesCallback`-minted `timer-callback` vs. `hasHandler`-minted
    `timer-callback-handler`, sharing a prefix and no substring, invisible to both
    `--variants` and `--forks`. **A fourth fork species**, found four times in one
    round by reading records side by side and by no instrument.
92. **A round's framing paragraph is a hypothesis with the coordinator's own name on
    it.** Round 18's own dispatch briefing asserted Capella auto-manages Eventing
    memory, unchecked - one of its own batches, reading a Capella page for background
    exactly as instructed, found Capella's FAQ contradicting it. The same
    read-the-page discipline every extraction agent is held to caught its own
    coordinator's error.

**Round 19 (22 pages, `cbbackupmgr` first contact + `javascript-udfs` paired and
pre-checked):**

93. **A pre-dispatch similarity check pays for itself in what a batch doesn't do.**
    Round 18 closed by recommending a similarity check before pairing; round 19 tried
    it. Briefed that `javascript-udfs/`'s twin measured 0.92-1.00 similarity, the batch
    minted nothing new and spent its attention on divergence instead - two real
    unadapted-Capella-wording defects and a genuine interop question. The saving is
    invisible in the output (a report with no new mints looks identical to a lazy
    one) and shows up only in what the batch read instead.
94. **Warning about a specific collision prevents that collision, and nothing else.**
    Round 19's dispatch briefing named two real namespace collisions in advance and
    both were avoided cleanly - one even correctly filed as a documented non-merge
    (`js-udf:n1ql-function-call` vs. the promoted `eventing:n1ql-function-call`). The
    same two batches, sharing that same briefing, independently minted one concept
    twice under **four other name pairs the briefing hadn't named**
    (`backup:repository`/`cbbackupmgr-repository`,
    `cloud-integration`/`native-cloud-integration`, the merge command twice, one RBAC
    role twice). A targeted warning fixes the case it names and carries no information
    about the cases it doesn't.
95. **A concept's existing relations are part of what "already in the registry"
    means, and a label-only check will miss it.** The sharpest of round 19's four
    forks happened because an agent did exactly what it was told - check the registry
    before minting - and still missed the reuse, because the correspondence
    (`tool:cbbackupmgr acquiresLockOn backup:repository`) was stated in a *relation*
    written by round 11, not in the label `registry-digest.py` prints. Round 10's
    lesson ("a refusal is only as good as the set it searched") recurring a third
    time, in its most granular form yet.

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
  re-run under the gate. Round 15 added a second, smaller, more urgent instance:
  **`cloud/vector-index/` needs re-extraction too** — 7 records from the first POC
  commit, written pre-gate, 3 of them with unquotable evidence, and wave 1 promoted
  **22 concepts out of them**. Both defects found there were in a single record;
  nobody has checked the other six against their pages.
- **Build an admission test for reference-table instances.** `query-settings.md`
  documents `node-quota`, `prepared-limit`, `loglevel`, `controls`,
  `functions-limit`, `keep-alive-length`, `max-index-api` and
  `tmpspace-dir`/`-size`, and **no extraction has ever minted any of them**, so they
  are invisible to every queue this project produces — a coherence pass can only
  reorganise what was extracted. This is the second instance of round 14's
  mint-blindness and the first with an obvious mechanical source: a settings table's
  own rows. It also has to be reconciled with the fact that a canonical reference
  table mints its rows at recurrence 1 by construction, so the admission test cannot
  be a recurrence threshold.
- **Two small registry repairs round 15 found and left.** `cloud-providers:gcp-azure`
  is one id naming two providers, and needs its relation split in two — it survived
  the plural-fork fix because the defect is in the *local name*, not the prefix. And
  `rest-api:compaction-rest-api.adoc` is a page id in concept clothing: now refused
  for new mints, but the existing one still needs retiring or re-typing.
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
  Round 14 added the three vector types to that axis and left a measured defect in it:
  covering index spelled four ways. Round 16 settled that — five ways, in fact, folded
  into `index:covering-index`, and **not** onto the type axis, because the docs define
  it after index selection. Round 17 read the module and closed all of
  that: the **pushdown family** (7), the three storage engines plus the four-level
  `concepts/index-storage-stack.json`, `index:sequential-scan`, `index:index-span`
  (folding five spellings) and four key-shape types. What is left on this axis is
  smaller and now enumerable: `index:span-inclusion` (a genuine closed 0–3 value set,
  attested once — the best single candidate for a later round),
  `index:composite-predicate-pushdown` (1, and the 8.0 page grew a whole section for it
  between releases, so a 7.6 or 7.2 read would settle it), a **scan-operator enum**
  that exists nowhere in the docs though five operators are cited as decisive on three
  pages, and `index:index-storage-setting` — the top level of the storage stack is real
  and its name is not yet earned. Round 17 also named the gap the registry cannot
  express at all: the decisive storage sentences turn on **Enterprise versus Community
  Edition**, and no promoted predicate carries an edition (`availableSince` takes a
  version). An ontology that cannot say "EE only" cannot answer a large class of real
  questions about Couchbase; minting `availableInEdition` is on the backlog rather than
  done, because one page's two sentences is where this project would normally decline
  to mint.
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
- **Diff every wave plan's paths against what is on disk before dispatching it.**
  Round 17 did the `indexes/` module — first contact on `server/8.0/indexes/`, and
  re-extraction of `cloud/indexes/` — and the result argues for making this check
  routine rather than for treating the round as having closed it: the eleven never-read
  pages yielded 400 relations, and the eleven thin records yielded **9.8× what they
  held**. **A coverage plan written as a list of directories inherits every
  reorganisation the docs have undergone since the plan was written**, and reports the
  resulting hole as a low recurrence count rather than as a hole. Two adjacent jobs are
  now measured and worth queueing: `server/8.0/indexes/` has version twins in **7.6 and
  7.2** whose content demonstrably differs (the 5.5 MIN/MAX history was deleted between
  7.2 and 8.0; 8.0 grew a composite-predicate-pushdown section), and the whole of
  `server/8.0/` is ~1,033 pages of which 177 have now been read.
- **The pairing strategy has two payoff axes, and round 18 is the case where they
  split — read both, every time, rather than assuming one implies the other.**
  Round 17's indexes module delivered on defect-finding (11 docs-issues) *and*
  promotion-independence (a 9.8× recovery, four reversed decisions) together. Round
  18's eventing module delivered on the first (12 docs-issues, the RBAC-gate
  asymmetry) and barely on the second, because Server/Capella page-pairs in that
  module run 0.89–1.00 similarity — closer to verbatim republication than the
  indexes module's 0.16–1.00 spread — so `shared-source.py`'s below-the-bar count
  jumped from 38 to 89 in one round while only a handful of newly-minted concepts
  cleared the bar on real independent evidence. Round 18 recommended checking a
  pairing's page-similarity before dispatching it, and round 19 is the round that
  tried it: `javascript-udfs/`'s pairing was measured at 0.92–1.00 before dispatch, and
  briefed with that number the batch minted nothing new at all, spending its whole
  attention on divergence instead. **The check paid off in what the batch chose not to
  do** — a real saving, and one that is invisible in the output, since a report with no
  new mints looks identical whether the briefing was good or the batch was lazy; the
  only way to tell the two apart is reading what the batch found instead (round 19's
  batch found two real unadapted-content defects and a genuine interop question).
  `shared-source.py --clusters` on a small pilot batch before committing the whole
  module remains the right check, now with one confirmed payoff behind it.
- **Continue the namespace coherence pass — wave 4.** Round 12's
  corrected metric exposed 276 unpromoted concepts at recurrence ≥ 2; rounds 12 and
  13 took it to 206, round 14's wave 1 (`vector-index:` and `version:`) took it
  to 163 — 27 of those retired by the metric fix rather than promoted, because
  they were documentation pages the widened metric had let back in — and round 15's
  wave 2 (`setting:`, dissolved) took it to 159, and round 16's wave 3 (`indexes:`,
  retired) to **156**. Round 17 took it **up to 233**, round 18 (another 67-page
  content round, not a coherence pass) took it **up to 256**, and round 19 (22 more
  pages, and 14 of the round's own mints promoted straight out of the backlog) took it
  **up to 261** — the expected direction, not a regression: dense new pages mint far
  more candidates than a round's own promotions retire, and the backlog is a function
  of the corpus. Three numbers should be read beside it from now on, because a raw
  count of candidates at ≥2 no longer means what it did: **293 of the corpus's ids rest
  partly on a shared source and 103 fall below the bar once that is discounted**
  (`shared-source.py`), **63 local names are forked across namespaces, 21 of which
  would cross the bar only if merged** (`recurrence.py --forks`), and — round 18's
  addition, with no instrument yet — an unknown number of **same-prefix synonym
  forks**, where two agents name one mechanism through two different predicates and
  mint two ids sharing a prefix and no substring; four confirmed instances in round 18
  and **four more, of a related but distinct shape, in round 19** — two batches
  minting the same concept under two full names with no shared substring at all,
  inside one round, despite a shared dispatch briefing that had already warned about
  two other collisions and prevented both. Shadow prefixes, the other measure of the same debt, are at
  **55 holding 210 ids** — which is *up* from the 43 reported in rounds 14 and 15, with
  no change to the corpus: those two figures were measured with the census bug in
  place, and 55 is the first honest count. Treat it as the new baseline, not as a
  regression. What is left is
  a long tail with no double-digit debt in it, and the method is settled: work it
  **one namespace at a time, deciding the namespace's internal structure before
  promoting any member**, using `recurrence.py --unpromoted-only --min 2` for the
  worklist and `candidate-evidence.py --ns <prefix> --audit` to read one and check
  that what you are reading is real. The queue, in the
  order the coherence question is answerable:
  `capella:`/`capellaiq:` (`capella-iq` is in both); `plan:`/`billing:`; `backup:`
  (`cluster-backup`/`bucket-backup` at 5 look like a *scope* axis crossing the
  promoted *type* axis — round 11's crossing shape, and round 19 added a dozen more
  `backup:` members from `cbbackupmgr` without checking whether any of them cross the
  same axis - the per-sub-command `backup:cbbackupmgr-*-command` family in particular
  looks like it could be one);
  `js-udf:` (round 19 read the module properly - 7 members promoted, six confirmed
  `shared`-verdict-below-bar and six left genuinely `unchecked` rather than refused -
  close enough to settled that it may not need its own coherence wave);
  `eventing:` (round 18 grew this from 22 to 40+ promoted members and folded four
  same-prefix synonym forks as a side effect of reading the module, but did not run a
  coherence pass over it — the ~10 individual Advanced Keyspace Accessor operations
  still have inconsistent per-operation naming beyond the three folded that round, and
  are the obvious next member to check); then `search:` and `n1ql:`, largest but also
  the two the metric fix most changed.
  Five cautions from waves 1 to 3. Read the namespace's existing records *before*
  deciding it — `fts:`/`search:` looks like a one-member collision and is a documented,
  correct resolution of a five-way split, which a tidying pass would have destroyed.
  Check each member against the registry's *referents* and not just its ids: three of
  `setting:`'s 34 were already promoted under another name, and the write-time enum
  reports such a member as legitimately `minted`. Search the **extraction layer** as
  well as the registry before refusing a merge — round 12 refused one correctly on the
  evidence it had and was wrong, because the id it needed had never been promoted and
  `registry-digest.py` therefore could not show it: **a refusal is only as good as the
  set it searched.** Do not believe a promoted record's `recurrence` field; re-measure
  it (`--stale-recurrence` says 47% are current). And budget for the remedy, not the
  namespace — a rename is one prefix rule for 25 ids, a dissolution is one decision
  each, and a plural fork is one line.
  And the 18 unpromoted **predicates** at ≥2 remain a different job: the top one,
  `requiresMinVersionFor` (5), was folded into `availableSince` in round 2 and
  re-minted since, so it needs a fold, not a promotion. Roughly 15 `sgw:`/`cbl:`
  tail items are not promotable at all until round 3's two trees are re-extracted.
- **Sweep the corpus for page ids in concept clothing.** `recurrence.py --page-ids`
  measures this: **392 of 2,116 ids (18%)** are only ever linked to and never labelled
  in any record's `concepts[]` — they are page identifiers occupying concept
  namespaces, 305 of them with no prefix at all. Wave 2 named the shape (a namespace
  can be a *part of speech*) and round 16 gave it a `page:` prefix and a re-runnable
  measurement; the sweep itself is not done. It is mostly mechanical, but not
  entirely — an id both linked to *and* labelled is a genuine concept that also has a
  page, so the report deliberately excludes those.
- **Give concurrent batches a way to see each other's mints mid-round, or accept the
  fork cost and fold afterward.** Round 19 dispatched two batches against the same
  18-page module with one shared context file, and they independently minted one
  concept twice under four different name pairs — none of them among the two
  collisions the briefing had explicitly warned about. Naming specific collisions in
  advance works (both named ones were avoided cleanly) and does not generalise (the
  four un-named ones happened anyway), so the remedy that would actually prevent this
  is structural: either serialize batches touching one namespace so each can see what
  the last one minted, or give concurrent batches a shared, live scratch file of
  same-round mints to check against before minting their own. Neither has been tried;
  reconciling the forks after the fact (what rounds 18 and 19 both did) costs roughly
  one extra read-the-relations pass per fork and has been sufficient so far, but it
  will not scale past a handful of concurrent batches on one namespace.
- **Add a variant ratchet to the gate.** Round 13 took the variant clusters from 13
  to 1 (the survivor is the `1`/`1%` literal pair, which is the object-typing
  question below, not a spelling one; round 17 added a second of exactly the same kind
  — `#sequentialscan`/`sequentialscan`, the two plan tokens a page names for one
  mechanism — so **both surviving "variant" clusters are literals in an object slot,
  not spellings of a concept**, which is an argument for typing the slot rather than
  for another spelling check) and wrote the alias-vs-rewrite rule down in
  `normalise-ids.py`. What is still missing is prevention: a gate check that refuses
  a *new* id which is a punctuation-variant near-miss of a promoted one. It needs a
  minimum-length guard — `variant_key` produced a degenerate `"1"` cluster on its
  first run — and it cannot catch the synonymy case at all (`Application Access` vs
  `bucket_full_access` share no substring), which is exactly why the role-id
  convention had to be written into the reconcile skill instead. This is the
  cheapest remaining control and the one that would make round 13's cleanup stay
  clean. Round 14 built the half of it that applies to the **registry** rather than
  to new mints — `verify-registry-ids.py` now rejects an alias that differs from its
  own target only in punctuation — after finding that the corpus's two largest dotted
  version variants were invisible to `--variants` precisely because someone had
  aliased them, and `--variants` resolves aliases before clustering. Aliasing a
  punctuation variant turns out to be *worse* than leaving the defect in place: it
  makes the wrong spelling pass the gate, which removes the only pressure to fix it,
  and it blinds the check written to enumerate the drift. The gate-side ratchet for
  newly-minted ids is still open.
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
  Round 14 supplies the concrete argument for the **object** half, which had been
  the vaguer one. The corpus asserts `service:search-service -providesIndexType->
  vector-index:search-vector-index`: the predicate names the axis, the object's
  namespace contradicts it, and the record passed the evidence gate cleanly. If
  `providesIndexType`'s object must be an `index-type:` id, a namespace fork that
  survived three rounds of reading was a *type error* detectable at write time. The
  relation layer had converged while the concept layer forked — ~100 predicates that
  every agent prompt lists in full, against ~300 concepts where the table an agent
  gets is necessarily partial — so the predicates are the reliable place to anchor a
  check on the ids.
- **Decide what a `seeAlso` object is, then normalise 86 of them.** Round 10 ruled
  that `current` is a pointer and not a version, and the extract skill has since
  forbidden it in a `page_id` or an output path. Both are clean; the **object slot**
  is not. 76 distinct ids containing `/current/` appear as the objects of 86
  `seeAlso` relations across 21 files, 30 keeping a `.md` extension and 7 an
  `#anchor` — three spellings of "a page" in one slot, none of them what a promoted
  `pages/` record uses. The rewrite is mechanical once the destination is chosen (a
  resolved page id, a `pages/` IRI, or a literal URL), and choosing is the whole
  task; round 14 declined to file into an undecided structure on the same grounds it
  refused to create `setting:`. This is also the third instance of one shape —
  **a rule enforced on one slot of a record is not enforced on the record** — so it
  is worth fixing alongside the structural validation above rather than separately.
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
  fifteen rounds. `context.jsonld` is a deliberately curated flagship subset (15 of
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
