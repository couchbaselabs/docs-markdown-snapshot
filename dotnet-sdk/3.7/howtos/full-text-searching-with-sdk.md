---
title: Search
description: You can use the Full Text Search service (FTS) to create queryable
  full-text indexes in Couchbase Server.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.7/modules/howtos/pages/full-text-searching-with-sdk.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/dotnet-sdk/3.7/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Full Text Search service (FTS) to create queryable full-text indexes in Couchbase Server. 

Full Text Search or FTS allows you to create, manage and query full text indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for indexing and querying documents, provides relevance scoring on the results of your queries and has fast indexes for querying a wide range of possible text searches.

Some of the supported query-types include simple queries like Match and Term queries, range queries like Date Range and Numeric Range and compound queries for conjunctions, disjunctions and/or boolean queries.

The Full Text Search service also supports vector search from Couchbase Server 7.6 onwards.

The .NET SDK exposes an API for performing FTS queries which abstracts some of the complexity of using the underlying REST API.

## [](#getting-started)Getting Started

After familiarizing yourself with how to create and query a Search index in the UI you can query it from the SDK.

There are two APIs for querying search: `cluster.searchQuery()`, and `cluster.search()`. Both are also available at the Scope level.

The former API supports FTS queries (`SearchQuery`), while the latter additionally supports the `VectorSearch` added in 7.6\. Most of this documentation will focus on the former API, as the latter is in @Stability.Volatile status.

We will perform an FTS query here - see the [Vector Search](#vector-search) section for examples of that.

## [](#examples)Examples

Search queries are executed at Cluster level. As of Couchbase Server 7.6, they can also be executed at the Scope level.

Here is a simple MatchQuery that looks for the text “swanky” using a defined index:

```csharp
// as a cluster-level search
var searchResult = await cluster.SearchAsync(
    "travel-sample.inventory.index-hotel-description",
    SearchRequest.Create(new MatchQuery("swanky")),
    new SearchOptions().Limit(10)
);

// as a scope-level search
[data-source-url=https://github.com/couchbase/docs-sdk-dotnet/blob/f15996b5ee34d72d5a60c6cb4cf62815599cb8f8/modules/howtos/examples/Couchbase.Examples.SearchV2/SearchV2Examples/Program.cs#L59-L62]
var searchResult = await scope.SearchAsync("index-hotel-description",
    SearchRequest.Create(
        new MatchQuery("swanky")),
    new SearchOptions().Limit(10));
```

All simple query types are created in the same manner, some have additional properties, which can be seen in common query type descriptions. Couchbase FTS’s [range of query types](#7.1@server:fts:fts-query-types.adoc) enable powerful searching using multiple options, to ensure results are just within the range wanted. Here is a date range query that looks for dates between 1st January 2021 and 31st January:

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

Like the Couchbase Query Service, FTS allows `RequestPlus` queries — _Read-Your-Own\_Writes (RYOW)_ consistency, ensuring results contain information from updated indexes:

```csharp
var mutationResult =  await collection.UpsertAsync("key",new {description = "swanky"});
var mutationState = MutationState.From(mutationResult);

var searchResult = cluster.SearchQueryAsync("travel-sample-index",new QueryStringQuery("swanky"),
            new SearchOptions().ConsistentWith(mutationState));
```

## [](#scoped-vs-global-indexes)Scoped vs Global Indexes

The FTS APIs exist at both the `Cluster` and `Scope` levels.

This is because FTS supports, as of Couchbase Server 7.6, a new form of "scoped index" in addition to the traditional "global index".

It’s important to use the `Cluster.SearchAsync()` for global indexes, and `Scope.SearchAsync()` for scoped indexes. (`Cluster.SearchQueryAsync()` is still available for compatibility with earlier versions of the SDK)

## [](#vector-search)Vector Search

As of Couchbase Server 7.6, the FTS service supports vector search in additional to traditional full text search queries.

#### [](#single-vector-query)Single vector query

In this first example we are performing a single vector query:

```csharp
var searchRequest = SearchRequest.Create(
    VectorSearch.Create(new VectorQuery("vector_field").WithVector(preGeneratedVectors))
);

var searchResult = scope.SearchAsync("travel-vector-index", searchRequest, new SearchOptions());
```

Let’s break this down. We create a `SearchRequest`, which can contain a traditional FTS query `SearchQuery` and/or the new `VectorSearch`. Here we are just using the latter.

The `VectorSearch` allows us to perform one or more `VectorQuery` s.

The `VectorQuery` itself takes the name of the document field that contains embedded vectors ("vector\_field" here), plus actual vector query in the form of a `float[]`.

(Note that Couchbase itself is not involved in generating the vectors, and these will come from an external source such as an embeddings API.)

Finally we execute the `SearchRequest` against the FTS index "travel-vector-index", which has previously been setup to vector index the "vector\_field" field.

This happens to be a scoped index so we are using `scope.SearchAsync()`. If it was a global index we would use `cluster.SearchAsync()` instead - see [Scoped vs Global Indexes](#scoped-vs-global-indexes).

It returns the same `SearchResult` detailed earlier.

#### [](#multiple-vector-queries)Multiple vector queries

You can run multiple vector queries together:

```csharp
var searchRequest = SearchRequest.Create(
    VectorSearch.Create(new[]
        {
        vectorQuery.WithOptions(
            new VectorQueryOptions().WithNumCandidates(2).WithBoost(0.3f)),
        anotherVectorQuery.WithOptions(
            new VectorQueryOptions().WithNumCandidates(5).WithBoost(0.7f)),
        })
);

// or with C# record syntax
var searchRequest2 = SearchRequest.Create(
    new VectorSearch(new[]
        {
            vectorQuery 
                with { Options = new VectorQueryOptions() { NumCandidates = 2, Boost = 0.3f } },
            anotherVectorQuery
                with { Options = new VectorQueryOptions() { NumCandidates = 5, Boost = 0.3f } },
        },
        Options: new VectorSearchOptions(VectorQueryCombination.And)
    ));

var searchResult = scope.SearchAsync("travel-vector-index", searchRequest, new SearchOptions());
```

How the results are combined (ANDed or ORed) can be controlled with `VectorSearchOptions().WithVectorQueryCombination()`.

#### [](#combining-fts-and-vector-queries)Combining FTS and vector queries

You can combine a traditional FTS query with vector queries:

```casharp
var searchRequest = new SearchRequest(
    SearchQuery: new MatchQuery("swanky"),
    VectorSearch: VectorSearch.Create(new VectorQuery("vector_field", preGeneratedVectors))
);

var searchResult = scope.SearchAsync("travel-index", searchRequest, new SearchOptions());
```