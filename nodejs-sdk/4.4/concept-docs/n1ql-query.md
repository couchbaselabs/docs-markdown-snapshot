---
title: Querying with SQL++
description: Parallel data management for complex queries over many records,
  using a familiar SQL-like syntax.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.4/modules/concept-docs/pages/n1ql-query.adoc
  xref: xref:4.4@nodejs-sdk:concept-docs:n1ql-query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.4/concept-docs/n1ql-query.html)

# Querying with SQL++

> Parallel data management for complex queries over many records, using a familiar SQL-like syntax. 

The [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) Query Language provides a familiar, SQL-like experience for querying documents stored in Couchbase. You can [read up on the language in our reference guide](#7.1@server:n1ql:n1ql-language-reference/index.adoc), but you probably just want to [dive into a practical example](../howtos/n1ql-queries-with-sdk.md).

Below, we fill in some of the gaps between reference and rolling-up-your-sleeves practicality, with discussion of a few areas of the Query Service where more background knowledge will help you to better program your application.

## [](#prepared-statements-for-query-optimization)Prepared Statements for Query Optimization

When a SQL++ query string is sent to the server, the server will inspect the string and parse it, planning which indexes to query. Once this is done, it generates a _query plan_ (see the [SQL++ reference](../../../server/current/n1ql/n1ql-language-reference/prepare.md), which gives more information on how to optimize queries using prepared statements). The computation for the plan adds some additional processing time and overhead for the query.

Often-used queries can be _prepared_ so that its _plan_ is generated only once. Subsequent queries using the same query string will use the pre-generated plan instead, saving on the overhead and processing of the plan each time. This is done for queries from the SDK by setting the `adhoc` query option to `false`.

For Couchbase Server 6.0 and earlier, the plan is cached by the SDK (up to a limit of 5000), as well as the Query Service. On Couchbase Server 6.5 and newer, the plan is stored by the Query Service — up to an adjustable limit of 16 384 plans per Query node.

For Couchbase Server 6.0 and earlier, the generated plan is not influenced by placeholders. Thus parameterized queries are considered the same query for caching and planning purposes, even if the supplied parameters are different. With Couchbase Server 6.5 and newer, if a statement has placeholders, _and_ a placeholder is supplied, the Query Service will generate specially optimized plans. Therefore, if you are supplying the placeholder each time, `adhoc = true` will actually return a better-optimized plan (at the price of generating a fresh plan for each query).

If your queries are highly dynamic, we recommend using parameterized queries if possible (epecially when prepared statements are not used). Parameterized queries are more cache efficient and will allow for better performance.

For the Node.js SDK, the `adhoc` parameter should be set to `false` for a plan to be prepared, or a prepared plan to be reused. Do not turn off the `adhoc` flag for _every_ query to Server 6.0 and earlier, since only a finite number of query plans (currently 5000) can be stored in the SDK.

```javascript
async function queryNamed() {
  const query = `
    SELECT airportname, city
    FROM \`travel-sample\`.inventory.airport
    WHERE city='London';`

  try {
    let result = await cluster.query(query, { adhoc: false })
    results.rows.forEach((row) => {
      console.log('Query row: ', row)
    return result
  } catch (error) {
    console.error('Query failed: ', error)
  }
}
```

> [!CAUTION]
> **When running an application using Prepared Statements through the Node.js SDK** — if you plan to upgrade Couchbase Server from 6.0.x or earlier to 6.5.0 or later, and are running a version of the Node.js SDK with an underlying LCB prior to 2.10.6, you will need to [restart the app or otherwise work around](#6.5@server:install:upgrade-strategy-for-features.adoc#prepared-statements) a change in the Server's behaviour.

## [](#indexes)Indexes

The Couchbase query service makes use of [_indexes_](../../../server/7.6/learn/services-and-indexes/indexes/indexes.md) in order to do its work. Indexes replicate subsets of documents from data nodes over to index nodes, allowing specific data (for example, specific document properties) to be retrieved quickly, and to distribute load away from data nodes in [MDS](../../../server/7.6/learn/services-and-indexes/services/services.md) topologies.

> [!IMPORTANT]
> In order to make a bucket queryable, it must have at least one index defined.

You can define a _primary index_ on a bucket. When a _primary_ index is defined you can issue non-covered (see below) queries on the bucket as well. This includes using the `META` function in the queries.

```n1ql
CREATE PRIMARY INDEX ON `users`
```

You can also define indexes over given document fields and then use those fields in the query:

```n1ql
CREATE INDEX ix_name ON `travel-sample`.inventory.hotel(name);
CREATE INDEX ix_email ON `travel-sample`.inventory.hotel(email);
```

This would allow you to query the _travel-sample_ bucket's hotel collection regarding a document's `name` or `email` properties, thus:

```n1ql
SELECT name, email
FROM `travel-sample`.inventory.hotel
WHERE name="Glasgow Grand Central" OR email="grandcentralhotel@example.com";
```

Indexes help improve the performance of a query. When an index includes the actual values of all the fields specified in the query, the index _covers_ the query, and eliminates the need to fetch the actual values from the Data Service. An index, in this case, is called a _covering index_, and the query is called a _covered_ query. For more information, see [Covering Indexes](../../../server/7.6/n1ql/n1ql-language-reference/covering-indexes.md).

You can also create and define indexes in the SDK using:

```javascript
const indexMgr = cluster.queryIndexes();
await indexMgr.createPrimaryIndex('bucket_name')
await indexMgr.createIndex('bucket_name', 'ix_name', ['name'])
await indexMgr.createIndex('bucket_name', 'ix_email', ['email'])
```

## [](#index-building)Index Building

Creating indexes on buckets with many existing documents can take a long time. You can build indexes in the background, creating _deferred_ indexes. The deferred indexes can be built together, rather than having to re-scan the entire bucket for each index.

```n1ql
CREATE PRIMARY INDEX ON `travel-sample`.inventory.hotel WITH {"defer_build": true};
CREATE INDEX ix_name ON `travel-sample`.inventory.hotel(name) WITH {"defer_build": true};
CREATE INDEX ix_email ON `travel-sample`.inventory.hotel(email) WITH {"defer_build": true};
BUILD INDEX ON `travel-sample`.inventory.hotel(`#primary`, `ix_name`, `ix_email`);
```

The indexes are not built until the `BUILD INDEX` statement is executed. At this point, the server scans all of the documents in the `users` bucket, and indexes it for all of the applicable indexes (in this case, those that have a `name` or `email` field).

Building deferred indexes can also be done via the SDK:

```javascript
const indexMgr = cluster.queryIndexes();
await indexMgr.createPrimaryIndex('bucket_name', {deferred: true})
await indexMgr.createIndex('bucket_name', 'ix_name', ['name'], {deferred: true})
await indexMgr.createIndex('bucket_name', 'ix_email', ['email'], {deferred: true})
await indexMgr.buildDeferredIndexes('bucket_name')
await indexMgr.watchIndexes('bucket_name', ['ix_name', 'ix_email', '#primary'], 2000)
```

## [](#index-consistency)Index Consistency

Because indexes are by design outside the Data Service, they are _eventually consistent_ with respect to changes to documents and, depending on how you issue the query, may at times not contain the most up-to-date information. This may especially be the case when deployed in a write-heavy environment: changes may take some time to propagate over to the index nodes.

The asynchronous updating nature of [Global Secondary Indexes (GSIs)](#7.1@server:learn:services-and-indexes/indexes/global-secondary-indexes.adoc) means that they can be very quick to query and do not require the additional overhead of index recaclculations at the time documents are modified. SQL++ queries are forwarded to the relevant indexes, and the queries are done based on indexed information, rather than the documents as they exist in the data service.

With default query options, the query service will rely on the current index state: the most up-to-date document versions are not retrieved, and only the indexed versions are queried. This provides the best performance. Only updates occurring with a small time frame may not yet have been indexed. For cases where consistency is more important than performance, the `scan_consistency` property of a query may be set to `REQUEST_PLUS`. ensuring that indexes are synchronized with the data service before querying.

The following options are available:

* `not_bounded`: Executes the query immediately, without requiring any consistency for the query. If index maintenance is running behind, out-of-date results may be returned.
* `at_plus`: Executes the query, requiring indexes first to be updated to the timestamp of the last update. If index maintenance is running behind, the query waits for it to catch up.
* `request_plus`: Executes the query, requiring the indexes first to be updated to the timestamp of the current query request. If index maintenance is running behind, the query waits for it to catch up.
* `statement_plus`: Executes the query with strong consistency per statement. Before processing each statement, the service obtains a current vector timestamp and uses it as a lower bound for that statement.

For SQL++, the default consistency is `not_bounded`.

Consider the following snippet:

```javascript
var randomNumber = Math.floor(Math.rand() * 10000000)

await collection.upsert(`user:${randomNumber}`, {
  name: 'Brass Doorknob',
  email: 'brass.doorknob@juno.com',
  random: randomNumber
})

var res = await cluster.query(
  'SELECT name, email, random, META(default).id FROM default WHERE "Brass" IN name')
```

The above query may not return the newly inserted document because it has not yet been indexed. The query is issued immediately after document creation, and in this case the query engine may process the query before the index has been updated.

If the above code is modified to use _RequestPlus_, query processing will wait until all updates have been processed and recalculated into the index from the point in time the query was received:

```javascript
var res = await cluster.query(
  'SELECT name, email, random, META(default).id FROM default WHERE "Brass" IN name', {
    scanConsistency: couchbase.QueryScanConsistency.RequestPlus,
  })
```

This gives the application developer more control over the balance between performance (latency) and consistency, and allows optimization on a case-by-case basis.