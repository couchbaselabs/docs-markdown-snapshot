---
title: Vector Search
description: Vector Search from the SDK, to enable AI integration, semantic
  search, and the RAG framework.
editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.0/modules/howtos/pages/vector-searching-with-sdk.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:1.0@cxx-sdk:howtos:vector-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/1.0/howtos/vector-searching-with-sdk.html)

# Vector Search

> Vector Search from the SDK, to enable AI integration, semantic search, and the RAG framework. 

This is currently implemented using [Search Indexes](full-text-searching-with-sdk.md), and can even be combined with traditional full text search queries. Vector embeddings can be an array of floats or a [base64 encoded string](../../../server/current/vector-search/run-vector-search-ui.md#base64).

## [](#prerequisites)Prerequisites

Couchbase Server 7.6.0 (7.6.2 for base64-encoded vectors) — or recent Capella instance.

#### [](#single-vector-query)Single vector query

In this first example we are performing a single vector query:

```c++
couchbase::search_request request(couchbase::vector_search(couchbase::vector_query("vector_field", vector_query)));

auto [err, res] = scope.search("vector-index", request).get();
```

Let’s break this down. We create a `search_request`, which can contain a traditional FTS query `search_query` and/or the new `vector_search`. Here we are just using the latter.

The `vector_search` allows us to perform one or more `vector_query` s.

The `vector_query` itself takes the name of the document field that contains embedded vectors ("vector\_field" here), plus actual vector query in the form of a `std::vector<double>`.

(Note that Couchbase itself is not involved in generating the vectors, and these will come from an external source such as an embeddings API.)

Finally we execute the `search_request` against the FTS index "vector-index", which has previously been setup to vector index the "vector\_field" field.

This happens to be a scoped index so we are using `scope.search()`. If it was a global index we would use `cluster.search()` instead - see [\[Scoped vs Global Indexes\]](#Scoped vs Global Indexes).

It returns the same `search_result` detailed earlier.

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

## [](#further-reading)Further Reading

* [Vector Search for AI Apps docs (self-managed Couchbase Server)](../../../server/current/vector-search/vector-search.md)
* [Vector Search for AI Apps docs (Capella DBaaS)](#cloud::vector-search:vector-search.adoc)
* Vector Search in the [Scala API reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/classcouchbase%5F1%5F1vector%5F%5Fsearch.html).