---
title: Search
description: You can use the Full Text Search service (FTS) to create queryable
  full-text indexes in Couchbase Server.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.0/modules/howtos/pages/full-text-searching-with-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:1.0@cxx-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/1.0/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Full Text Search service (FTS) to create queryable full-text indexes in Couchbase Server. 

Full Text Search or FTS allows you to create, manage, and query full text indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for querying documents, provides relevance scoring on the results of your queries, and has fast indexes for querying a wide range of possible text searches. Some of the supported query types include simple queries like Match and Term queries; range queries like Date Range and Numeric Range; and compound queries for conjunctions, disjunctions, and/or boolean queries. The Scala SDK exposes an API for performing FTS queries which abstracts some of the complexity of using the underlying REST API.

## [](#examples)Examples

The examples below use these imports:

```c++
#include <couchbase/cluster.hxx>
#include <couchbase/fmt/error.hxx>
#include <couchbase/match_all_query.hxx>
#include <couchbase/match_query.hxx>
```

Search queries are executed at Cluster level (not bucket or collection). Here is a simple match\_query that looks for the text "swanky" using a defined index:

```c++
auto request = couchbase::search_request(couchbase::match_query("swanky"));
auto options = couchbase::search_options().limit(10);

auto [err, res] = cluster.search("travel-sample-index-hotel-description", request, options).get();

if (err) {
    fmt::println("Got an error doing search: {}", err);
} else {
    auto& rows = res.rows();
    // Handle rows
}
```

All simple query types are created in the same manner. Some have additional properties, which can be seen in common query type descriptions. Couchbase FTS's [range of query types](#7.6@server:fts:fts-query-types.adoc) enable powerful searching using multiple options, to ensure results are just within the range wanted.

## [](#working-with-results)Working with Results

The result of a search query has three components: rows, facets, and metadata. Rows are the documents that match the query. Facets allow the aggregation of information collected on a particular result set. Metadata holds additional information not directly related to your query, such as total rows and how long the query took to execute in the cluster.

```c++
auto request = couchbase::search_request(couchbase::match_query("swanky"));
auto options = couchbase::search_options().limit(10);

auto [err, res] = cluster.search("travel-sample-index-hotel-description", request, options).get();

if (err) {
    fmt::println("Got an error doing search: {}", err);
} else {
    for (const auto& row : res.rows()) {
        auto id = row.id();
        auto score = row.score();
        // ...
    }

    // Metadata
    auto max_score = res.meta_data().metrics().max_score();
    auto success_count = res.meta_data().metrics().success_partition_count();
}
```

## [](#consistency)Consistency

Like the Couchbase Query Service, FTS allows provides optional _Read-Your-Own-Writes (RYOW)_ consistency, ensuring results contain information from updated indexes:

```c++
const tao::json::value hotel{
    { "name", "Hotel California" },
    { "desc", "Such a lonely place" },
};

auto [insert_err, insert_res] = collection.insert("newHotel", hotel).get();
if (insert_err) {
    fmt::println("Got an error inserting the document: {}", insert_err);
} else {
    auto mutation_state = couchbase::mutation_state();
    mutation_state.add(insert_res);

    auto request = couchbase::search_request(couchbase::match_query("lonely"));
    auto options = couchbase::search_options().limit(10).consistent_with(mutation_state);
    auto [search_err, search_res] = cluster.search("travel-sample-index", request, options).get();
    // ...
}
```