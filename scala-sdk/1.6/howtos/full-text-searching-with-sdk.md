---
title: Search
description: You can use the Full Text Search service (FTS) to create queryable
  full-text indexes in Couchbase Server, and to perform vector searches.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-scala/edit/temp/1.6/modules/howtos/pages/full-text-searching-with-sdk.adoc
  xref: xref:1.6@scala-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/1.6/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Full Text Search service (FTS) to create queryable full-text indexes in Couchbase Server, and to perform vector searches. 

Full Text Search (FTS) allows you to create, manage, and query full text indexes on JSON documents stored in Couchbase buckets.

It uses natural language processing for querying documents, provides relevance scoring on the results of your queries, and has fast indexes for querying a wide range of possible text searches. Some of the supported query types include simple queries like Match and Term queries; range queries like Date Range and Numeric Range; and compound queries for conjunctions, disjunctions, and/or boolean queries. The Scala SDK exposes an API for performing FTS queries which abstracts away the complexity of using the underlying REST API.

From Couchbase Server 7.6, the FTS service also supports powerful vector search.

## [](#examples)Examples

After familiarizing yourself with how to create and query a search index in the UI, you can query it from the SDK.

You'll need to know whether a global or scoped search index has been created - see [Scoped vs Global Indexes](#scoped-vs-global-indexes) for details. If your Couchbase Server is pre 7.6 it will certainly be a global index, otherwise, the UI will tell you which it is.

These APIs are used for querying global search indexes: `cluster.searchQuery()`, and `cluster.search()`. And this one is used for scoped search indexes: `scope.search()`.

The `cluster.searchQuery()` API supports FTS queries (`SearchQuery`), while `scope.search()` additionally supports the `VectorSearch` added in 7.6.

Most of this documentation will focus on the former API, as the latter is in @Stability.Uncommitted status.

We will perform an FTS query here - see the [\[vector search\]](#vector search) section for examples of that.

The examples below use these imports:

```none
import com.couchbase.client.scala._
import com.couchbase.client.scala.json.JsonObject
import com.couchbase.client.scala.kv.MutationState
import com.couchbase.client.scala.search.{SearchOptions, SearchScanConsistency}
import com.couchbase.client.scala.search.queries.{MatchQuery, SearchQuery}
import com.couchbase.client.scala.search.result.{SearchResult, SearchRow}
import com.couchbase.client.scala.search.vector.{SearchRequest, VectorQuery, VectorSearch}

import scala.util.{Failure, Success, Try}
```

The `cluster.searchQuery()` API takes the name of the index and the type of query as required arguments, and allows additional options to be provided if needed.

Here is a simple `MatchQuery` that looks for the text "swanky" using a defined index:

```none
val result: Try[SearchResult] = cluster.searchQuery("travel-sample-index-hotel-description",
  MatchQuery("swanky"),
  SearchOptions().limit(10))

result match {
  case Success(res) =>
    val rows: Seq[SearchRow] = res.rows
    // handle rows
  case Failure(err) => println(s"Failure: ${err}")
}
```

All simple query types are created in the same manner. Some have additional properties, which can be seen in common query type descriptions. Couchbase FTS's [range of query types](#7.6@server:fts:fts-query-types.adoc) enable powerful searching using multiple options, to ensure results are just within the range wanted.

## [](#working-with-results)Working with Results

The result of a search query has three components: rows, facets, and metadata. Rows are the documents that match the query. Facets allow the aggregation of information collected on a particular result set. Metadata holds additional information not directly related to your query, such as total rows and how long the query took to execute in the cluster.

```none
val result: Try[SearchResult] = cluster.searchQuery("travel-sample-index-hotel-description",
  MatchQuery("swanky"),
  SearchOptions().limit(10))

result match {
  case Success(res) =>

    // Rows
    res.rows.foreach(row => {
      val id: String = row.id
      val score: Double = row.score
      // ...
    })

    // Metadata
    val maxScore: Double = res.metaData.metrics.maxScore
    val successCount: Long = res.metaData.metrics.successPartitionCount

  case Failure(err) => println(s"Failure: ${err}")
}
```

## [](#scoped-vs-global-indexes)Scoped vs Global Indexes

The FTS APIs exist on both the `Cluster` and `Scope` objects.

This is because FTS supports, as of Couchbase Server 7.6, a new form of "scoped index" in addition to the traditional "global index".

It's important to use the `Cluster.searchQuery()` or `Cluster.search()` for global indexes, and `Scope.search()` for scoped indexes.

## [](#vector-search)Vector Search

As of Couchbase Server 7.6, the FTS service supports vector search in additional to traditional full text search queries.

### [](#examples-2)Examples

#### [](#single-vector-query)Single vector query

In this first example we are performing a single vector query:

```none
val request = SearchRequest.vectorSearch(VectorSearch(VectorQuery("vector_field", vectorQuery)))

val result: Try[SearchResult] = scope.search("vector-index", request)
```

Let's break this down. We create a `SearchRequest`, which can contain a traditional FTS query `SearchQuery` and/or the new `VectorSearch`. Here we are just using the latter.

The `VectorSearch` allows us to perform one or more `VectorQuery` s.

The `VectorQuery` itself takes the name of the document field that contains embedded vectors ("vector\_field" here), plus actual vector query in the form of a `float[]`.

(Note that Couchbase itself is not involved in generating the vectors, and these will come from an external source such as an embeddings API.)

Finally we execute the `SearchRequest` against the FTS index "vector-index", which has previously been setup to vector index the "vector\_field" field.

This happens to be a scoped index so we are using `scope.search()`. If it was a global index we would use `cluster.search()` instead - see [Scoped vs Global Indexes](#scoped-vs-global-indexes).

It returns the same `SearchResult` detailed earlier.

#### [](#multiple-vector-queries)Multiple vector queries

You can run multiple vector queries together:

```none
val request = SearchRequest
  .vectorSearch(VectorSearch(Seq(
    VectorQuery("vector_field", vectorQuery).numCandidates(2).boost(0.3),
    VectorQuery("vector_field", anotherVectorQuery).numCandidates(5).boost(0.7))))

val result = scope.search("vector-index", request)
```

How the results are combined (ANDed or ORed) can be controlled with `VectorSearch.vectorSearchOptions(VectorSearchOptions().vectorQueryCombination(VectorQueryCombination.And))`.

#### [](#combining-fts-and-vector-queries)Combining FTS and vector queries

You can combine a traditional FTS query with vector queries:

```none
val request = SearchRequest.searchQuery(SearchQuery.matchAll)
  .vectorSearch(VectorSearch(VectorQuery("vector_field", vectorQuery)))

val result = scope.search("vector-and-fts-index", request)
```

#### [](#fts-queries)FTS queries

And note that traditional FTS queries, without vector search, are also supported with the new `cluster.search()` / `scope.search()` APIs:

```none
val request = SearchRequest.searchQuery(SearchQuery.matchAll)

val result = scope.search("travel-sample-index", request)
```

The `SearchQuery` is created in the same way as detailed earlier.

## [](#consistency)Consistency

Like the Couchbase Query Service, FTS allows provides optional _Read-Your-Own-Writes (RYOW)_ consistency, ensuring results contain information from updated indexes:

```none
collection.insert("newHotel",
  JsonObject("name" -> "Hotel California", "desc" -> "Such a lonely place")) match {

  case Success(upsertResult) =>
    upsertResult.mutationToken.foreach(mutationToken => {

      val ms = MutationState(Seq(mutationToken))

      // Will wait until the the index contains the specified mutation
      val result = cluster.searchQuery(
        "travel-sample-index-hotel-description",
        MatchQuery("lonely"),
        SearchOptions()
          .limit(10)
          .scanConsistency(SearchScanConsistency.ConsistentWith(ms))
      )
    })

  case Failure(err) => println(s"Failure: ${err}")
}
```