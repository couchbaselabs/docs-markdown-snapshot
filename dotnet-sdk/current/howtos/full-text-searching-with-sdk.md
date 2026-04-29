---
title: Search
description: You can use the Search service to create queryable search indexes
  in Couchbase Server.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.9/modules/howtos/pages/full-text-searching-with-sdk.adoc
pubDate: 2026-04-29T05:35:23.064Z
link: xref:dotnet-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/current/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Search service to create queryable search indexes in Couchbase Server. 

The Search Service allows you to create, manage, and query Search indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for indexing and querying documents, provides relevance scoring on the results of your queries, and has fast indexes for querying a wide range of possible text searches.

Some of the supported query-types include simple queries like Match and Term queries, range queries like Date Range and Numeric Range and compound queries for conjunctions, disjunctions and/or boolean queries.

The Search Service also supports vector search from Couchbase Server 7.6 onwards.

The .NET SDK exposes an API for performing Search queries which abstracts some of the complexity of using the underlying REST API.

## [](#getting-started)Getting Started

After familiarizing yourself with how to create and query a Search index in the UI you can query it from the SDK.

There are two APIs for querying search: `cluster.searchQuery()`, and `cluster.search()`. Both are also available at the Scope level.

The former API supports Search queries (`SearchQuery`), while the latter additionally supports the `VectorSearch` added in 7.6\. Most of this documentation will focus on the former API, as the latter is in @Stability.Volatile status.

We will perform a Search query here - see the [\[vector-search\]](#vector-search) section for examples of that.

## [](#examples)Examples

Search queries are executed at Cluster level. As of Couchbase Server 7.6, they can also be executed at the Scope level.

Here is a simple MatchQuery that looks for the text "swanky" using a defined index:

```csharp
// as a cluster-level search
var searchResult = await cluster.SearchAsync(
    "travel-sample.inventory.index-hotel-description",
    SearchRequest.Create(new MatchQuery("swanky")),
    new SearchOptions().Limit(10)
);

// as a scope-level search
[data-source-url=https://github.com/couchbase/docs-sdk-dotnet/blob/c1fdad02d8282a7c1e59d1c483795ef4ecbc47ea/modules/howtos/examples/Couchbase.Examples.SearchV2/SearchV2Examples/Program.cs#L59-L62]
var searchResult = await scope.SearchAsync("index-hotel-description",
    SearchRequest.Create(
        new MatchQuery("swanky")),
    new SearchOptions().Limit(10));
```

All simple query types are created in the same manner, some have additional properties, which can be seen in common query type descriptions. Couchbase Search Service's [range of query types](#8.0@server:fts:fts-query-types.adoc) enable powerful searching using multiple options, to ensure results are just within the range wanted. Here is a date range query that looks for dates between 1st January 2021 and 31st January:

```csharp
var searchResult = await scope.SearchAsync("index-name",
    SearchRequest.Create(
        new DateRangeQuery()
            .Start(DateTime.Parse("2021-01-01"), inclusive: true)
            .End(DateTime.Parse("2021-02-01"), inclusive: false)
        ), new SearchOptions().Limit(10));
```

A conjunction query contains multiple child queries; its result documents must satisfy all of the child queries:

```csharp
var searchResult = await scope.SearchAsync("index-name",
    SearchRequest.Create(
        new ConjunctionQuery(
        new DateRangeQuery()
            .Start(DateTime.Parse("2021-01-01"), inclusive: true)
            .End(DateTime.Parse("2021-02-01"), inclusive: false),
        new MatchQuery("swanky"))
    ), new SearchOptions().Limit(10));
```

> [!TIP]
> Search Results Limit
> 
> By default, the Search Service returns only the first 10 matches (`size: 10`, `from: 0`). To retrieve more results, you must explicitly define pagination settings such as `size` or `from` in your query.
> 
> For information about formatting your Search query and specifying limits, see [Search Request JSON Properties](../../../server/current/search/search-request-params.md).
> 
> For information about pagination in Search responses, see [Pagination](../../../server/current/fts/fts-search-response.md#pagination).

## [](#working-with-results)Working with Results

The result of a search query has three components: hits, facets, and metdata. Hits are the documents that match the query. Facets allow the aggregation of information collected on a particular result set. Metdata holds additional information not directly related to your query, such as success total hits and how long the query took to execute in the cluster.

Iterating hits

```csharp
foreach (var hit in searchResult.Hits)
{
    string documentId = hit.Id;
    double score = hit.Score;
    Log.Information("Hit: {id}: {score}", documentId, score);
}
```

Iterating facets

```csharp
foreach (var keyValuePair in searchResult.Facets)
{
    var facet = keyValuePair.Value;
    var name = facet.Name;
    var total = facet.Total;
    Log.Information("Facet: {key}={name},{total}", keyValuePair.Key, name, total);
}
```

## [](#consistency)Consistency

Like the Couchbase Query Service, Search Service allows `RequestPlus` queries — _Read-Your-Own\_Writes (RYOW)_ consistency, ensuring results contain information from updated indexes:

```csharp
var mutationResult =  await collection.UpsertAsync("key",new {description = "swanky"});
var mutationState = MutationState.From(mutationResult);

var searchResult = cluster.SearchQueryAsync("travel-sample-index",new QueryStringQuery("swanky"),
            new SearchOptions().ConsistentWith(mutationState));
```

## [](#scoped-vs-global-indexes)Scoped vs Global Indexes

The Search APIs exist at both the `Cluster` and `Scope` levels.

This is because Search Service supports, as of Couchbase Server 7.6, a new form of "scoped index" in addition to the traditional "global index".

It's important to use the `Cluster.SearchAsync()` for global indexes, and `Scope.SearchAsync()` for scoped indexes. (`Cluster.SearchQueryAsync()` is still available for compatibility with earlier versions of the SDK)