---
title: Querying with SQL++
description: Parallel data management for complex queries over many records,
  using a familiar SQL-like syntax.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/concept-docs/pages/n1ql-query.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:4.2@php-sdk:concept-docs:n1ql-query.adoc[]
---

[View original HTML](/php-sdk/4.2/concept-docs/n1ql-query.html)

# Querying with SQL++

> Parallel data management for complex queries over many records, using a familiar SQL-like syntax. 

Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::7.5@sdk:shared:partial$n1ql-queries.adoc\[\]

Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::7.5@sdk:shared:partial$n1ql-queries.adoc\[\]

For the PHP SDK, the `adhoc` parameter should be set to `false` for a plan to be prepared, or a prepared plan to be reused. Do not turn off the `adhoc` flag for _every_ query to Server 6.0 and earlier, since only a finite number of query plans (currently 5000) can be stored in the SDK.

```php
$query = "SELECT count(*) FROM `travel-sample`.inventory.airport where country = $1";
$opts = new QueryOptions();
$opts->adhoc(false);
$opts->positionalParameters(['France']);

$result = $cluster->query($query, $opts);
foreach ($result->rows() as $row) {
    // do something
}
```

> [!CAUTION]
> **When running an application using Prepared Statements through the PHP SDK** — if you plan to upgrade Couchbase Server from 6.0.x or earlier to 6.5.0 or later, and are running a version of the PHP SDK with an underlying LCB prior to 2.10.6, you will need to [restart the app or otherwise work around](#7.1@server:install:upgrade-strategy-for-features.adoc#prepared-statements) a change in the Server’s behaviour.

## [](#indexes)Indexes

The Couchbase query service makes use of [_indexes_](#7.1@server:learn:services-and-indexes/indexes/indexes.adoc) in order to do its work. Indexes replicate subsets of documents from data nodes over to index nodes, allowing specific data (for example, specific document properties) to be retrieved quickly, and to distribute load away from data nodes in [MDS](#7.1@server:learn:services-and-indexes/services/services.adoc) topologies.

> [!IMPORTANT]
> In order to make a bucket queryable, it must have at least one index defined.

You can define a _primary index_ on a bucket. When a _primary_ index is defined you can issue non-covered (see below) queries on the bucket as well. This includes using the `META` function in the queries.

```n1ql
CREATE PRIMARY INDEX ON `travel-sample`
```

You can also define indexes over given document fields and then use those fields in the query:

```n1ql
CREATE INDEX ix_name ON `travel-sample`(name);
CREATE INDEX ix_email ON `travel-sample`(email);
```

This would allow you to query the _users_ bucket regarding a document’s `name` or `email` properties, thus:

```n1ql
SELECT name, email
FROM `travel-sample`
WHERE name="Glasgow Grand Central" OR email="grandcentralhotel@principal-hayley.com";
```

Indexes help improve the performance of a query. When an index includes the actual values of all the fields specified in the query, the index _covers_ the query, and eliminates the need to fetch the actual values from the Data Service. An index, in this case, is called a _covering index_, and the query is called a _covered_ query. For more information, see [Covering Indexes](#7.1@server:n1ql:n1ql-language-reference/covering-indexes.adoc).

You can also create and define indexes in the SDK using:

```php
$mgr = $cluster->queryIndexes();

$mgr->createPrimaryIndex('travel-sample');
$mgr->createIndex('travel-sample', 'ix_name', ['name']);
$mgr->createIndex('travel-sample', 'ix_email', ['email']);
```

## [](#index-building)Index Building

Creating indexes on buckets with many existing documents can take a long time. You can build indexes in the background, creating _deferred_ indexes. The deferred indexes can be built together, rather than having to re-scan the entire bucket for each index.

```sql
CREATE PRIMARY INDEX ON `travel-sample` WITH {"defer_build": true};
CREATE INDEX ix_name ON `travel-sample`(name) WITH {"defer_build": true};
CREATE INDEX ix_email ON `travel-sample`(email) WITH {"defer_build": true};
BUILD INDEX ON `travel-sample`(`#primary`, `ix_name`, `ix_email`);
```

The indexes are not built until the `BUILD INDEX` statement is executed. At this point, the server scans all of the documents in the `travel-sample` bucket, and indexes it for all of the applicable indexes (in this case, those that have a `name` or `email` field).

Building deferred indexes can also be done via the SDK:

```php
$indexOpts = new CreateQueryIndexOptions();
$primaryIndexOpts = new CreateQueryPrimaryIndexOptions();

$mgr->createPrimaryIndex('travel-sample', $primaryIndexOpts->deferred(true));
$mgr->createIndex('travel-sample', 'ix_name', ['name'], $indexOpts->deferred(true));
$mgr->createIndex('travel-sample', 'ix_email', ['email'], $indexOpts->deferred(true));

$indexesToBuild = $mgr->buildDeferredIndexes('travel-sample');
$mgr->watchIndexes('travel-sample', $indexesToBuild, 2);
```

Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::7.5@sdk:shared:partial$n1ql-queries.adoc\[\]

The following options are available:

Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::7.1@server:learn:page$services-and-indexes/indexes/index-replication.adoc\[\]

Consider the following snippet:

```php
$indexOpts = new CreateQueryIndexOptions();
$primaryIndexOpts = new CreateQueryPrimaryIndexOptions();

$mgr->createPrimaryIndex('travel-sample', $primaryIndexOpts->deferred(true));
$mgr->createIndex('travel-sample', 'ix_name', ['name'], $indexOpts->deferred(true));
$mgr->createIndex('travel-sample', 'ix_email', ['email'], $indexOpts->deferred(true));

$indexesToBuild = $mgr->buildDeferredIndexes('travel-sample');
$mgr->watchIndexes('travel-sample', $indexesToBuild, 2);
```

The above query may not return the newly inserted document because it has not yet been indexed. The query is issued immediately after document creation, and in this case the query engine may process the query before the index has been updated.

If the above code is modified to use _RequestPlus_, query processing will wait until all updates have been processed and recalculated into the index from the point in time the query was received:

```php
$queryOpts->scanConsistency(QueryScanConsistency::REQUEST_PLUS);
$queryOpts->positionalParameters(['Brass']);
$cluster->query(
    "SELECT name, email, random, META().id FROM `travel-sample`.inventory.airport WHERE $1 IN name",
    $queryOpts,
);
```

This gives the application developer more control over the balance between performance (latency) and consistency, and allows optimization on a case-by-case basis.