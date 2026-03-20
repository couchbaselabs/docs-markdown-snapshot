---
title: Search
description: You can use the Full Text Search service (FTS) to create queryable
  full-text indexes in Couchbase Server.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/full-text-searching-with-sdk.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:rust-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Full Text Search service (FTS) to create queryable full-text indexes in Couchbase Server. 

Full Text Search or FTS allows you to create, manage, and query full text indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for querying documents, provides relevance scoring on the results of your queries, and has fast indexes for querying a wide range of possible text searches. Some of the supported query types include simple queries like Match and Term queries; range queries like Date Range and Numeric Range; and compound queries for conjunctions, disjunctions, and/or boolean queries. The Rust SDK exposes an API for performing FTS queries which abstracts some of the complexity of using the underlying REST API.

## [](#examples)Examples

The examples below use these imports:

```rust
use couchbase::options::search_options::SearchOptions;
use couchbase::scope::Scope;
use couchbase::search::queries::{MatchAllQuery, MatchQuery, Query};
use couchbase::search::request::SearchRequest;
use couchbase::search::vector::{VectorQuery, VectorSearch};
use futures::StreamExt;
use serde_json::json;
```

Search queries are executed at Cluster level (not bucket or collection). Here is a simple MatchQuery that looks for the text “swanky” using a defined index:

```rust
let result = scope
    .search(
        "travel-sample-index-hotel-description",
        SearchRequest::with_search_query(Query::Match(MatchQuery::new("swanky"))),
        SearchOptions::new().limit(10),
    )
    .await;

match result {
    Ok(mut res) => {
        println!("Search successful");
        let rows = res.rows();
        // use rows
    }
    Err(e) => {
        println!("Error performing search: {e}");
    }
}
```

All simple query types are created in the same manner. Some have additional properties, which can be seen in common query type descriptions. Couchbase FTS’s [range of query types](#8.0@server:fts:fts-query-types.adoc) enable powerful searching using multiple options, to ensure results are just within the range wanted.

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

```rust
let mut result = scope
    .search(
        "travel-sample-index-hotel-description",
        SearchRequest::with_search_query(Query::Match(MatchQuery::new("swanky"))),
        SearchOptions::new().limit(10),
    )
    .await?;

{
    let mut rows = result.rows();
    while let Some(row) = rows.next().await {
        // Each individual row read can error.
        let row = row?;
        let id = row.id;
        let score = row.score;
        // ...
    }
}

// Metadata - can only be read after all rows have been read.
let metadata = result.metadata()?;
let total_hits = metadata.metrics.total_hits;
let success_count = metadata.metrics.max_score;
```

## [](#consistency)Consistency

Like the Couchbase Query Service, FTS allows provides optional _Read-Your-Own-Writes (RYOW)_ consistency, ensuring results contain information from updated indexes:

```rust
let insert_result = scope
    .collection("hotels")
    .insert(
        "newHotel",
        json!({"name": "Hotel California", "desc": "Such a lonely place"}),
        None,
    )
    .await?;

// MutationState can be created from a token directly.
let mutation_state = MutationState::from(insert_result.mutation_token().unwrap().clone());

let result = scope
    .search(
        "travel-sample-index-hotel-description",
        SearchRequest::with_search_query(Query::Match(MatchQuery::new("lonely"))),
        SearchOptions::new()
            .limit(10)
            .consistent_with(mutation_state),
    )
    .await?;
```