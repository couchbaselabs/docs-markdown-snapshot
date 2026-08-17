---
title: Search
description: You can use the Search service to create queryable Search indexes
  in Couchbase Server.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.3/modules/howtos/pages/full-text-searching-with-sdk.adoc
  xref: xref:cxx-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/current/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Search service to create queryable Search indexes in Couchbase Server. 

The Search Service allows you to create, manage, and query Search indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for querying documents, provides relevance scoring on the results of your queries, and has fast indexes for querying a wide range of possible text searches. Some of the supported query types include simple queries like Match and Term queries; range queries like Date Range and Numeric Range; and compound queries for conjunctions, disjunctions, and/or boolean queries. The C++ SDK exposes an API for performing Search queries which abstracts some of the complexity of using the underlying REST API.

## [](#examples)Examples

The examples below use these imports:

```c++
#include <couchbase/cluster.hxx>
#include <couchbase/fmt/error.hxx>
#include <couchbase/match_all_query.hxx>
#include <couchbase/match_query.hxx>
```

Search queries are executed at Cluster level (not bucket or collection). Here is a _match\_query_ example that looks for the text 'swanky' using a defined index:

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

> [!TIP]
> Search Results Limit
> 
> By default, the Search Service returns only the first 10 matches (`size: 10`, `from: 0`). To retrieve more results, you must explicitly define pagination settings such as `size` or `from` in your query.
> 
> For information about formatting your Search query and specifying limits, see [Search Request JSON Properties](../../../server/current/search/search-request-params.md).
> 
> For information about pagination in Search responses, see [Pagination](../../../server/current/fts/fts-search-response.md#pagination).

All simple query types are created in the same manner. Some have additional properties, which can be seen in common query type descriptions. Couchbase Search Service's [range of query types](#8.0@server:fts:fts-query-types.adoc) enable powerful searching using multiple options, to ensure results are just within the range wanted.

## [](#working-with-results)Working with Results

The result of a Search query has three components: rows, facets, and metadata. Rows are the documents that match the query. Facets allow the aggregation of information collected on a particular result set. Metadata holds additional information not directly related to your query, such as total rows and how long the query took to execute in the cluster.

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

Like the Couchbase Query Service, the Search Service allows provides optional _Read-Your-Own-Writes (RYOW)_ consistency, ensuring results contain information from updated indexes:

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