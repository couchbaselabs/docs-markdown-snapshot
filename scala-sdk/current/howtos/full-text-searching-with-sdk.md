---
title: Search
description: You can use the Search Service to create queryable Search indexes
  in Couchbase Server.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.12/modules/howtos/pages/full-text-searching-with-sdk.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:scala-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/current/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Search Service to create queryable Search indexes in Couchbase Server. 

The Search Service allows you to create, manage, and query Search indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for querying documents, provides relevance scoring on the results of your queries, and has fast indexes for querying a wide range of possible text searches. Some of the supported query types include simple queries like Match and Term queries; range queries like Date Range and Numeric Range; and compound queries for conjunctions, disjunctions, and/or boolean queries. The Scala SDK exposes an API for performing Search queries which abstracts some of the complexity of using the underlying REST API.

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

All simple query types are created in the same manner. Some have additional properties, which can be seen in common query type descriptions. Couchbase Search Service's [range of query types](#8.0@server:fts:fts-query-types.adoc) enable powerful searching using multiple options, to ensure results are just within the range wanted.

> [!TIP]
> Search Results Limit
> 
> By default, the Search Service returns only the first 10 matches (`size: 10`, `from: 0`). To retrieve more results, you must explicitly define pagination settings such as `size` or `from` in your query.
> 
> For information about formatting your Search query and specifying limits, see [Search Request JSON Properties](../../../server/current/search/search-request-params.md).
> 
> For information about pagination in Search responses, see [Pagination](../../../server/current/fts/fts-search-response.md#pagination).

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

Like the Couchbase Query Service, the Search Service provides optional _Read-Your-Own-Writes (RYOW)_ consistency, ensuring results contain information from updated indexes:

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