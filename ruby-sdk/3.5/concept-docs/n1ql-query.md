---
title: Querying with SQL++
description: Parallel data management for complex queries over many records,
  using a familiar SQL-like syntax.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.5/modules/concept-docs/pages/n1ql-query.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.5@ruby-sdk:concept-docs:n1ql-query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.5/concept-docs/n1ql-query.html)

# Querying with SQL++

> Parallel data management for complex queries over many records, using a familiar SQL-like syntax. 

Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::7.5@sdk:shared:partial$n1ql-queries.adoc\[\]

Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::7.5@sdk:shared:partial$n1ql-queries.adoc\[\]

For the Ruby SDK, the `adhoc` parameter should be set to `false` for a plan to be prepared, or a prepared plan to be reused. Do not turn off the `adhoc` flag for _every_ query to Server 6.0 and earlier, since only a finite number of query plans (currently 5000) can be stored in the SDK.

```ruby
options = QueryOptions.new
options.adhoc = false
options.positional_parameters(['France'])
result = cluster.query("SELECT count(*) FROM `travel-sample`.inventory.airport WHERE country=$1", options)
```

## [](#indexes)Indexes

The Couchbase query service makes use of [_indexes_](#7.1@server:learn:services-and-indexes/indexes/indexes.adoc) in order to do its work. Indexes replicate subsets of documents from data nodes over to index nodes, allowing specific data (for example, specific document properties) to be retrieved quickly, and to distribute load away from data nodes in [MDS](#7.1@server:learn:services-and-indexes/services/services.adoc) topologies.

> [!IMPORTANT]
> In order to make a bucket queryable, it must have at least one index defined.

You can define a _primary index_ on a bucket. When a _primary_ index is defined you can issue non-covered (see below) queries on the bucket as well. This includes using the `META` function in the queries.

```n1ql
CREATE PRIMARY INDEX ON `users`
```

You can also define indexes over given document fields and then use those fields in the query:

```n1ql
CREATE INDEX ix_name ON `travel-sample`(name);
CREATE INDEX ix_email ON `travel-sample`(email);
```

This would allow you to query the _travel-sample_ bucket regarding a document’s `name` or `email` properties, thus:

```n1ql
SELECT name, email
FROM `travel-sample`
WHERE name="Glasgow Grand Central" OR email="grandcentralhotel@principal-hayley.com";
```

Indexes help improve the performance of a query. When an index includes the actual values of all the fields specified in the query, the index _covers_ the query, and eliminates the need to fetch the actual values from the Data Service. An index, in this case, is called a _covering index_, and the query is called a _covered_ query. For more information, see [Covering Indexes](#7.1@server:n1ql:n1ql-language-reference/covering-indexes.adoc).

You can also create and define indexes in the SDK using:

```ruby
manager = cluster.query_indexes
manager.create_primary_index("travel-sample")
manager.create_index("travel-sample", "index_name", ["name"])
manager.create_index("travel-sample", "index_email", ["email"])
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

```ruby
manager = cluster.query_indexes

options = Management::QueryIndexManager::CreatePrimaryIndexOptions.new
options.defer = true
manager.create_primary_index("travel-sample", options);

options = Management::QueryIndexManager::CreateIndexOptions.new
options.defer = true
manager.create_index("travel-sample", "ix_name", ["name"], options);
manager.create_index("travel-sample", "ix_email", ["email"], options);

manager.build_deferred_indexes("travel-sample")
manager.watch_indexes("travel-sample", ["ix_name", "ix_email", "#primary"], 2_000) # wait for 2 seconds
```

Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::7.5@sdk:shared:partial$n1ql-queries.adoc\[\]

The following options are available:

Unresolved include directive in modules/concept-docs/pages/n1ql-query.adoc - include::7.1@server:learn:page$services-and-indexes/indexes/index-replication.adoc\[\]

Consider the following snippet:

```ruby
random_number = rand(0, 10_000_000)

collection.upsert("user:#{random_number}", {
    "name" => "Brass Doorknob",
    "email" => "brass.doorknob@juno.com",
    "random" => random_number
})

options = QueryOptions.new
options.positional_parameters(["Brass"])
result = cluster.query(
  "SELECT name, email, random, META().id FROM `travel-sample`.inventory.airport WHERE $1 IN name",
  options
)
```

The above query may not return the newly inserted document because it has not yet been indexed. The query is issued immediately after document creation, and in this case the query engine may process the query before the index has been updated.

If the above code is modified to use _RequestPlus_, query processing will wait until all updates have been processed and recalculated into the index from the point in time the query was received:

```ruby
options = QueryOptions.new
options.positional_parameters(["Brass"])
options.scan_consistency = :request_plus
result = cluster.query(
  "SELECT name, email, random, META().id FROM `travel-sample`.inventory.airport WHERE $1 IN name",
  options
)
```

This gives the application developer more control over the balance between performance (latency) and consistency, and allows optimization on a case-by-case basis.