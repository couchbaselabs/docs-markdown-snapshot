---
title: Vector Search
description: Vector Search from the SDK, to enable AI integration, semantic
  search, and use of RAG frameworks.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.3/modules/howtos/pages/vector-searching-with-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cxx-sdk:howtos:vector-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/current/howtos/vector-searching-with-sdk.html)

# Vector Search

> Vector Search from the SDK, to enable AI integration, semantic search, and use of RAG frameworks. 

Vector Search has been available in Couchbase Capella Operational and self-managed Server since version 7.6, using the Couchbase Search Service. Version 8.0 introduces vector query using Global Secondary Indexes (GSI), the Query Service index — using either a fast Hyperscale index, or a composite index to combine scalar queries with semantic search.

For fast and scalable vector queries, use one of the above two GSI choices — detailed in the next section. If you don't require the speed and scale of vector query with GSI, or need to combine vector, geo-spatial search, range search, and traditional fuzzy text searches, then consider [Vector Search With the Search Service](#vector-search-with-the-search-service).

## [](#vector-search-with-the-query-service-and-gsi)Vector Search With the Query Service and GSI

From the SDK, a vector query using GSI is the same as any other query. However, you will need to build one or more indexes.

### [](#prerequisites)Prerequisites

* Couchbase Server 8.0.0 or newer — or a recent Capella instance.
* Your chosen [vector index](../../../server/current/vector-index/use-vector-indexes.md) — hyperscale or composite.

You will need to refer to the [Use Vector Indexes for AI Applications](../../../server/current/vector-index/vectors-and-indexes-overview.md) pages for a full discussion of using Vector Indexes with Vector Queries. In particular, you will need to [create a Vector Index](../../../server/current/vector-index/hyperscale-filter.md#creating-a-hyperscale-vector-index-with-included-scalar-values).

### [](#examples)Examples

The [Use Vector Indexes for AI Applications](../../../server/current/vector-index/vectors-and-indexes-overview.md) pages contain examples using both hyperscale and compound indexes.

Here is the [Hyperscale Index](../../../server/current/vector-index/hyperscale-vector-index.md#query-example) example, wrapped inside the C++ SDK Query API.

Hyperscale Index Example

```c++
auto [err, res] =
  cluster
    .query(
      "SELECT d.id, d.question, d.wanted_similar_color_from_search, "
      "  ARRAY_CONCAT( "
         "d.couchbase_search_query.knn[0].vector[0:4], "
         "['...'] "
      ") AS vector "
      "FROM `vector-sample`.`color`.`rgb-questions` AS d "
      "WHERE d.id = '#87CEEB';",
      couchbase::query_options().metrics(true)
    )
    .get();
if (err) {
    fmt::println("Error: {}", err);
} else {
    auto rows = res.rows_as<couchbase::codec::tao_json_serializer>();
    for (const auto& row : rows) {
        fmt::println("Row: {}", tao::json::to_string(row));
    }
}
```

Parameterizing the query, as with [regular queries](sqlpp-queries-with-sdk.md#parameterized-queries), will allow the reuse of the [Query Plan](../../../server/current/n1ql/n1ql-intro/queriesandresults.md#prepare-stmts). This can be more efficient, unless you are doing a lot of optimization to your query.

Parameterized Vector Query

```c++
auto [err, res] =
  cluster
    .query(
      "SELECT d.id, d.question, d.wanted_similar_color_from_search, "
      "  ARRAY_CONCAT( "
         "d.couchbase_search_query.knn[0].vector[0:4], "
         "['...'] "
      ") AS vector "
      "FROM `vector-sample`.`color`.`rgb-questions` AS d "
      "WHERE d.id = $id;",
      couchbase::query_options().named_parameters(std::make_pair("id", "#87CEEB"))
    )
    .get();
if (err) {
    fmt::println("Error: {}", err);
} else {
    auto rows = res.rows_as<couchbase::codec::tao_json_serializer>();
    for (const auto& row : rows) {
        fmt::println("Row: {}", tao::json::to_string(row));
    }
}
```

## [](#vector-search-with-the-search-service)Vector Search With the Search Service

Vector search is also implemented using [Search Indexes](full-text-searching-with-sdk.md), and can be combined with traditional full text search queries. Vector embeddings can be an array of floats or a [base64 encoded string](../../../server/current/vector-search/run-vector-search-ui.md#base64).

### [](#prerequisites-2)Prerequisites

Couchbase Server 7.6.0 (7.6.2 for base64-encoded vectors) — or recent Capella instance.

### [](#examples-2)Examples

#### [](#single-vector-query)Single vector query

In this first example we are performing a single vector query:

```c++
couchbase::search_request request(couchbase::vector_search(couchbase::vector_query("vector_field", vector_query)));

auto [err, res] = scope.search("vector-index", request).get();
```

Let's break this down. We create a `search_request`, which can contain a traditional FTS query `search_query` and/or the new `vector_search`. Here we are just using the latter.

The `vector_search` allows us to perform one or more `vector_query` s.

The `vector_query` itself takes the name of the document field that contains embedded vectors ("vector\_field" here), plus actual vector query in the form of a `std::vector<double>`.

(Note that Couchbase itself is not involved in generating the vectors, and these will come from an external source such as an embeddings API.)

Finally we execute the `search_request` against the FTS index "vector-index", which has previously been setup to vector index the "vector\_field" field.

This happens to be a scoped index so we are using `scope.search()`. If it was a global index we would use `cluster.search()` instead - see [\[Scoped vs Global Indexes\]](#Scoped vs Global Indexes).

It returns the same `search_result` detailed earlier.

#### [](#pre-filters)Pre-Filters

From Couchbase Server 7.6.4 — and in Capella Operational clusters — [pre-filtering with similarity search](../../../server/current/vector-search/pre-filtering-vector-search.md#about-pre-filtering) is available. This is a non-vector query that the server executes first to get an intermediate result. Then it executes the vector query on the intermediate result to get the final result.

```c++
template<typename SearchQuery>
auto prefilter(SearchQuery prefilter) -> couchbase::vector_query&
```

If no prefilter is specified, the server executes the vector query on all indexed documents.

```c++
couchbase::vector_query("vector_field", vector_query)
  .num_candidates(num_candidates)
  .prefilter(couchbase::match_query("primary")
    .field("color_wheel_pos"))
```

Note that `num_candidates` sets how many similar vectors are returned. If it is not set, then the Cluster's default of `3` will be used — this corresponds with `k` on the Server side, for K-Nearest Neighbors.

The prefilter can be any Search Query — from a simple match, as above, to a string query:

```c++
  .prefilter(couchbase::query_string_query("+description:sea -color_hex:fff5ee"))
```

See the [API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/classcouchbase%5F1%5F1vector%5F%5Fquery.html#aed005b80a8376445e114b59935f9465f).

#### [](#multiple-vector-queries)Multiple vector queries

You can run multiple vector queries together:

```c++
std::vector<couchbase::vector_query> vector_queries{
    couchbase::vector_query("vector_field", vector_query).num_candidates(2).boost(0.3),
    couchbase::vector_query("vector_field", another_vector_query).num_candidates(5).boost(0.7)
};

auto request = couchbase::search_request(couchbase::vector_search(vector_queries));
auto [err, res] = scope.search("vector-index", request).get();
```

How the results are combined (ANDed or ORed) can be controlled with `vector_search_options.query_combination()`.

#### [](#combining-fts-and-vector-queries)Combining FTS and vector queries

You can combine a traditional FTS query with vector queries:

```c++
auto request = couchbase::search_request(couchbase::match_all_query())
                 .vector_search(couchbase::vector_search(couchbase::vector_query("vector_field", vector_query)));

auto [err, res] = scope.search("vector-and-fts-index", request).get();
```

How the results are combined (ANDed or ORed) can be controlled with `vector_search_options.query_combination()`.

Scoring for these hybrid search queries combines the boost multipliers to get to the final score.

hit_score = (query_1_boost * query_1_hit_score) + (query_2_boost * query_2_hit_score)

### [](#query-methods)Query Methods

As part of the Search service, you can use the same [Search query methods](full-text-searching-with-sdk.md#search-queries) as regular Searches. See a fuller list, with Vector properties, in the [Capella docs](../../../cloud/search/search-request-params.md).

## [](#further-reading)Further Reading

### [](#vector-query)Vector Query

* [Vector Query for AI Apps docs (self-managed Couchbase Server)](../../../server/current/vector-index/vectors-and-indexes-overview.md).
* [Vector Query for AI Apps docs (Capella DBaaS)](#cloud::vector-index/vectors-and-indexes-overview.adoc)
* Vector GSI Query is just like any other query from the SDK to the Query service: [C++ SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/classcouchbase%5F1%5F1vector%5F%5Fquery.html).

### [](#vector-search)Vector Search

* [Vector Search for AI Apps docs (self-managed Couchbase Server)](../../../server/current/vector-search/vector-search.md)
* [Vector Search for AI Apps docs (Capella DBaaS)](#cloud::vector-search:vector-search.adoc)
* Vector Search in the [C++ SDK API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/classcouchbase%5F1%5F1vector%5F%5Fsearch.html).