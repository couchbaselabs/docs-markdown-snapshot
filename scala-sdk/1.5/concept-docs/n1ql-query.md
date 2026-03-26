---
title: Querying with SQL++
description: Parallel data management for complex queries over many records,
  using a familiar SQL-like syntax.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/1.5/modules/concept-docs/pages/n1ql-query.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:1.5@scala-sdk:concept-docs:n1ql-query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/1.5/concept-docs/n1ql-query.html)

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

For the Scala SDK, the `adhoc` parameter should be set to `false` for a plan to be prepared, or a prepared plan to be reused. Do not turn off the `adhoc` flag for _every_ query to Server 6.0 and earlier, since only a finite number of query plans (currently 5000) can be stored in the SDK.

```scala
val stmt =
  """select count(*)
  from `travel-sample`.inventory.airport
  where country=$1;"""
val result = cluster.query(
  stmt,
  QueryOptions()
    .adhoc(false)
    .parameters(QueryParameters.Positional("United States"))
)
```

## [](#indexes)Indexes

The Couchbase query service makes use of [_indexes_](../../../server/7.2/learn/services-and-indexes/indexes/indexes.md) in order to do its work. Indexes replicate subsets of documents from data nodes over to index nodes, allowing specific data (for example, specific document properties) to be retrieved quickly, and to distribute load away from data nodes in [MDS](../../../server/7.2/learn/services-and-indexes/services/services.md) topologies.

> [!IMPORTANT]
> In order to make a bucket queryable, it must have at least one index defined.

You can define a _primary index_ on a collection. When a _primary_ index is defined you can issue non-covered (see below) queries on the bucket as well. This includes using the `META` function in the queries.

```n1ql
CREATE PRIMARY INDEX ON `users`;
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

Indexes help improve the performance of a query. When an index includes the actual values of all the fields specified in the query, the index _covers_ the query, and eliminates the need to fetch the actual values from the Data Service. An index, in this case, is called a _covering index_, and the query is called a _covered_ query. For more information, see [Covering Indexes](../../../server/7.2/n1ql/n1ql-language-reference/covering-indexes.md).

You can also create and define indexes in the SDK using:

```scala
val result: Try[Unit] =
  cluster.queryIndexes.createPrimaryIndex("users")

result match {
  case Success(_) =>
  case Failure(err) => println(s"Operation failed with err $err")
}

// From now on the examples will use `.get` rather than correct error handling,
// for brevity
cluster.queryIndexes.createIndex("users", "index_name", Seq("name")).get
cluster.queryIndexes.createIndex("users", "index_email", Seq("email")).get
```

## [](#index-building)Index Building

Creating indexes on buckets with many existing documents can take a long time. You can build indexes in the background, creating _deferred_ indexes. The deferred indexes can be built together, rather than having to re-scan the entire bucket for each index.

```sql
CREATE PRIMARY INDEX ON `travel-sample`.inventory.hotel WITH {"defer_build": true};
CREATE INDEX ix_name ON `travel-sample`.inventory.hotel(name) WITH {"defer_build": true};
CREATE INDEX ix_email ON `travel-sample`.inventory.hotel(email) WITH {"defer_build": true};
BUILD INDEX ON `travel-sample`.inventory.hotel(`#primary`, `ix_name`, `ix_email`);
```

The indexes are not built until the `BUILD INDEX` statement is executed. At this point, the server scans all of the documents in the `users` bucket, and indexes it for all of the applicable indexes (in this case, those that have a `name` or `email` field).

Building deferred indexes can also be done via the SDK:

```scala
cluster.queryIndexes.createPrimaryIndex("users", deferred = Some(true))
cluster.queryIndexes.createIndex("users", "index_name",
  Seq("name"), deferred = Some(true)).get
cluster.queryIndexes.createIndex("users", "index_email",
  Seq("email"), deferred = Some(true)).get
cluster.queryIndexes.buildDeferredIndexes("users")

// Wait for the indexes to build
cluster.queryIndexes.watchIndexes("users",
  Seq("index_name", "index_email", "#primary"),
  Duration("30 seconds")).get
```

Note that the build step is still asynchronous, so `watchIndexes` is used to wait for the indexes to be completed. "#primary" is the primary index.

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

* A SQL++ query using the default `NotBounded` scan consistency will not wait for any indexes to finish updating before running the query and returning results, meaning that results are returned quickly, but the query will not return any documents that are yet to be indexed.
* With scan consistency set to `RequestPlus`, all outstanding document changes and index updates are processed before the query is run. Select this when consistency is always more important than performance.
* For a middle ground, `AtPlus` is a "read your own write" (RYOW) option, which means it just waits for the documents that you specify to be indexed.

For SQL++, the default consistency is `not_bounded`.

Here's how to specify the `RequestPlus` scan consistency level:

```scala
val result = cluster.query(
  "select `travel-sample`.* from `travel-sample` limit 10;",
  QueryOptions().scanConsistency(QueryScanConsistency.RequestPlus())
)
```

And the `AtPlus` level is represented with `QueryScanConsistency.ConsistentWith`:

```scala
val result = collection.upsert("id", content)
  .flatMap(upsertResult => {
    val ms = MutationState.from(upsertResult)

    cluster.query(
      "select `travel-sample`.* from `travel-sample` limit 10;",
        QueryOptions().scanConsistency(QueryScanConsistency.ConsistentWith(ms))
    )
  })

result match {
  case Success(_) =>
  case Failure(err) => println(s"Operation failed with error $err")
}
```