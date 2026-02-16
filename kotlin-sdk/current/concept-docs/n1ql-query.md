[View original HTML](/kotlin-sdk/current/concept-docs/n1ql-query.html)

> Parallel data management for complex queries over many records, using a familiar SQL-like syntax. 

The [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) Query Language provides a familiar, SQL-like experience for querying documents stored in Couchbase. You can [read up on the language in our reference guide](../../../server/current/n1ql/n1ql-language-reference/index.md), but you probably just want to [dive into a practical example](#howtos:n1ql-queries-with-sdk.adoc).

Below, we fill in some of the gaps between reference and rolling-up-your-sleeves practicality, with discussion of a few areas of the Query Service where more background knowledge will help you to better program your application.

## [](#prepared-statements-for-query-optimization)Prepared Statements for Query Optimization

When a SQL++ query string is sent to the server, the server will inspect the string and parse it, planning which indexes to query. Once this is done, it generates a _query plan_ (see the [SQL++ reference](../../../server/current/n1ql/n1ql-language-reference/prepare.md), which gives more information on how to optimize queries using prepared statements). The computation for the plan adds some additional processing time and overhead for the query.

Often-used queries can be _prepared_ so that its _plan_ is generated only once. Subsequent queries using the same query string will use the pre-generated plan instead, saving on the overhead and processing of the plan each time. This is done for queries from the SDK by setting the `adhoc` query option to `false`.

For Couchbase Server 6.0 and earlier, the plan is cached by the SDK (up to a limit of 5000), as well as the Query Service. On Couchbase Server 6.5 and newer, the plan is stored by the Query Service — up to an adjustable limit of 16 384 plans per Query node.

For Couchbase Server 6.0 and earlier, the generated plan is not influenced by placeholders. Thus parameterized queries are considered the same query for caching and planning purposes, even if the supplied parameters are different. With Couchbase Server 6.5 and newer, if a statement has placeholders, _and_ a placeholder is supplied, the Query Service will generate specially optimized plans. Therefore, if you are supplying the placeholder each time, `adhoc = true` will actually return a better-optimized plan (at the price of generating a fresh plan for each query).

If your queries are highly dynamic, we recommend using parameterized queries if possible (epecially when prepared statements are not used). Parameterized queries are more cache efficient and will allow for better performance. The maximum client-side query cache size is 5000 entries.

```java
Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::example$N1qlQueryExample.java[]
```

## [](#indexes)Indexes

The Couchbase Query Service makes use of [_indexes_](#7.1@server:learn:services-and-indexes/indexes/indexes.adoc) in order to do its work. Indexes replicate subsets of documents from data nodes over to index nodes, allowing specific data (for example, specific document properties) to be retrieved quickly, and to distribute load away from data nodes in [MDS](#7.1@server:learn:services-and-indexes/services/services.adoc) topologies.

|  | In order to make a bucket queryable, it must have at least one index defined. |
|  | ----------------------------------------------------------------------------- |

You can define a _primary index_ on a bucket. When a _primary_ index is defined you can issue non-covered (see below) queries on the bucket as well. This includes using the `META` function in the queries.

```n1ql
CREATE PRIMARY INDEX ON `users`
```

You can also define indexes over given document fields and then use those fields in the query:

```n1ql
CREATE INDEX ix_name ON `users`(name);
CREATE INDEX ix_email ON `users`(email);
```

This would allow you to query the _users_ bucket regarding a document’s `name` or `email` properties, thus:

```n1ql
SELECT name, email FROM `users` WHERE name="Monty Python" OR email="monty@python.org";
```

Indexes help improve the performance of a query. When an index includes the actual values of all the fields specified in the query, the index _covers_ the query, and eliminates the need to fetch the actual values from the Data Service. An index, in this case, is called a _covering index_, and the query is called a _covered_ query. For more information, see [Covering Indexes](#7.1@server:n1ql:n1ql-language-reference/covering-indexes.adoc).

You can also create and define indexes in the SDK using:

```java
Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::example$N1qlQueryExample.java[]
```

## [](#index-building)Index Building

Creating indexes on buckets with many existing documents can take a long time. You can build indexes in the background, creating _deferred_ indexes. The deferred indexes can be built together, rather than having to re-scan the entire bucket for each index.

```sql
CREATE PRIMARY INDEX ON `users` WITH {"defer_build": true};
CREATE INDEX ix_name ON `users`(name) WITH {"defer_build": true};
CREATE INDEX ix_email ON `users`(email) WITH {"defer_build": true};
BUILD INDEX ON `users`(`#primary`, `ix_name`, `ix_email`);
```

The indexes are not built until the `BUILD INDEX` statement is executed. At this point, the server scans all of the documents in the `users` bucket, and indexes it for all of the applicable indexes (in this case, those that have a `name` or `email` field).

Building deferred indexes can also be done via the SDK:

```java
Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::example$N1qlQueryExample.java[]
```

## [](#index-consistency)Index Consistency

Because indexes are by design outside the Data Service, they are _eventually consistent_ with respect to changes to documents and, depending on how you issue the query, may at times not contain the most up-to-date information. This may especially be the case when deployed in a write-heavy environment: changes may take some time to propagate over to the index nodes.

The asynchronous updating nature of [Global Secondary Indexes (GSIs)](../../../server/current/indexes/indexing-overview.md) means that they can be very quick to query and do not require the additional overhead of index recaclculations at the time documents are modified. SQL++ queries are forwarded to the relevant indexes, and the queries are done based on indexed information, rather than the documents as they exist in the data service.

With default query options, the query service will rely on the current index state: the most up-to-date document versions are not retrieved, and only the indexed versions are queried. This provides the best performance. Only updates occurring with a small time frame may not yet have been indexed. For cases where consistency is more important than performance, the `scan_consistency` property of a query may be set to `REQUEST_PLUS`. ensuring that indexes are synchronized with the data service before querying.

The following options are available:

Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::7.1@server:learn:page$services-and-indexes/indexes/index-replication.adoc\[\]

Consider the following snippet:

```java
Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::example$N1qlQueryExample.java[]
```

The above query may not return the newly inserted document because it has not yet been indexed. The query is issued immediately after document creation, and in this case the Query Engine may process the query before the index has been updated.

If the above code is modified to use _REQUEST\_PLUS_, query processing will wait until all updates have been processed and recalculated into the index from the point in time the query was received:

```java
Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::example$N1qlQueryExample.java[]
```

This gives the application developer more control over the balance between performance (latency) and consistency, and allows optimization on a case-by-case basis.

## [](#collections-and-scopes-and-the-query-context)Collections and Scopes, and the Query Context

From Couchbase Server release 7.0 the [Collections](#7.1@server:learn:data/scopes-and-collections.adoc) feature lets you logically group similar documents into Collections.

You can query collections in SQL++, by referring to a fully qualified keyspace. For example, to list the documents in the `airline` collection in the `inventory` scope:

```n1ql
SELECT * FROM `travel-sample`.inventory.airline;
```

As a convenience, you can also query a partial keyspace from the [Query Context](#7.1@server:n1ql:n1ql-intro:sysinfo.adoc#query-context) of a specific Scope. For example, from the context of `` `travel-sample`.inventory ``, you could abbreviate the previous query to:

```n1ql
SELECT * FROM airline;
```

To do this, you can [Set a Query Context](#7.1@server:tools:query-workbench.adoc#query-context) in the Query Workbench or [query at scope level](#howtos:n1ql-queries-with-sdk.adoc#querying-at-scope-level) using the SDK.