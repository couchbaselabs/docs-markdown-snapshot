---
title: Search
description: You can use the Full Text Search service (FTS) to create queryable
  full-text indexes in Couchbase Server.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.9/modules/howtos/pages/full-text-searching-with-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.9@scala-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/3.9/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Full Text Search service (FTS) to create queryable full-text indexes in Couchbase Server. 

Full Text Search or FTS allows you to create, manage, and query full text indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for querying documents, provides relevance scoring on the results of your queries, and has fast indexes for querying a wide range of possible text searches. Some of the supported query types include simple queries like Match and Term queries; range queries like Date Range and Numeric Range; and compound queries for conjunctions, disjunctions, and/or boolean queries. The Scala SDK exposes an API for performing FTS queries which abstracts some of the complexity of using the underlying REST API.

## [](#examples)Examples

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

Search queries are executed at Cluster level (not bucket or collection). Here is a simple MatchQuery that looks for the text "swanky" using a defined index:

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

All simple query types are created in the same manner. Some have additional properties, which can be seen in common query type descriptions. Couchbase FTS's [range of query types](#8.0@server:fts:fts-query-types.adoc) enable powerful searching using multiple options, to ensure results are just within the range wanted.

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