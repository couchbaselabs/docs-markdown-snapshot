---
title: Run a Search With a Search Index
description: Run a Search query to search and return the contents of a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/run-searches.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/search/run-searches.html)

# Run a Search With a Search Index

> Run a Search query to search and return the contents of a Search index. 

If you use the default search result [sorting](search-request-params.md#sort) of `_score`, a document’s [score](#scoring) determines where it appears in your search results.

> [!NOTE]
> You must [create a Search index](create-search-indexes.md) before you can run a search with the Search Service.

You can run a search against a Search index with:

* The [Couchbase Capella UI](#ui).
* A [SQL++ query](#sql).
* The Couchbase SDKs:  
[.NET](../../dotnet-sdk/current/howtos/full-text-searching-with-sdk.md)| [Go](../../go-sdk/current/howtos/full-text-searching-with-sdk.md)| [Java](../../java-sdk/current/howtos/full-text-searching-with-sdk.md)| [Kotlin](../../kotlin-sdk/current/howtos/full-text-search.md)| [Node.js](../../nodejs-sdk/current/howtos/full-text-searching-with-sdk.md)| [PHP](../../php-sdk/current/howtos/full-text-searching-with-sdk.md)| [Python](../../python-sdk/current/howtos/full-text-searching-with-sdk.md)| [Ruby](../../ruby-sdk/current/howtos/full-text-searching-with-sdk.md)| [Scala](../../scala-sdk/current/howtos/full-text-searching-with-sdk.md)

To run a Search query against multiple Search indexes at once, [Create a Search Index Alias with the Capella UI](create-search-index-alias.md).

## [](#scoring)Scoring for Search Queries

As of Couchbase Server version 8.0, you can choose between 2 scoring algorithms for your Search index:

* [tf-idf](#tf-idf)
* [bm25](#bm25)

> [!TIP]
> Scoring can also change based on whether you’re using synonyms in your Search index. For more information, see [Running a Search for Synonyms](synonyms/synonyms-search.md#run-synonym-search).

### [](#tf-idf)tf-idf Search Scoring

To determine a document’s score in search results, the Search Service can use the [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) algorithm. `tf-idf` increases the score of a document based on term frequency, or the number of times a term appears in a document divided by the total number of terms in the document. It penalizes document frequency, or how often a term appears across all documents.

The `tf-idf` score is calculated at a partition level in a Search index.

The Search Service uses `tf-idf` to calculate the hit score for a document, multiplied by any [boost](search-request-params.md#boost) parameters applied to each query inside the [query object](search-request-params.md#query-object):

hit_score = (query_1_boost * query_1_hit_score) + (query_2_boost * query_2_hit_score)

If one of your Search queries is a [Vector Search query](../vector-search/vector-search.md), the calculation changes to:

hit_score = (query_1_boost * query_1_hit_score) + (knn_boost * knn_distance)

When running a hybrid search with the [Web Console](#ui) or [REST API](#api), the Search Service displays results as a disjunct (`OR`) between your regular Search and Vector Search queries.

> [!TIP]
> When running a hybrid Search query and the `tf-idf` algorithm, you should add a `boost` value to your regular Search query to level the `tf-idf` score with the knn distance. Otherwise, you might see unexpected search results. This is because of the differences in the scoring algorithms between the 2 query types.

### [](#bm25)bm25 Search Scoring

Couchbase Server version 8.0

As of Couchbase Server version 8.0, you can choose to use the [bm25](https://en.wikipedia.org/wiki/Okapi%5FBM25) algorithm instead of `tf-idf` for your Search index.

`bm25` ranks documents based on the query terms that appear in each document, regardless of proximity. It calculates the number of times a term appears in a document, with penalties for more common terms like `tf-idf`, but also includes:

* Diminishing returns for a term that continues to frequently appear in documents, based on a saturation parameter (`k1`).
* An adjustment to the resulting score, based on the total length of the current document field, divided by a normalized average length of the field across all documents (`b`).

The value of `k1` limits just how much a single query term’s frequency can affect the scoring of a document. `k1` reduces the effect of term repetition and the risk of documents with excessively repeated content inflating your relevance scores. For example, spam or clickbait content would have reduced scores in `bm25` over the same document sentence being scored with `tf-idf`.

The Search Service chooses reasonable defaults for the value of `k1` and `b`.

Unlike `tf-idf`, `bm25` rewards term frequency, but penalizes document frequency.

The calculation for a basic Search query is still based on the document’s score for a query multiplied by any [boost](search-request-params.md#boost) parameters:

hit_score = (query_1_boost * query_1_hit_score) + (query_2_boost * query_2_hit_score)

The calculation when running a hybrid Search query, that includes [a Vector Search query](../vector-search/vector-search.md), is still:

hit_score = (query_1_boost * query_1_hit_score) + (knn_boost * knn_distance)

When running a hybrid search with the [Capella UI](#ui) or [REST API](#api), the Search Service displays results as a disjunct (`OR`) between your regular Search and Vector Search queries.

`bm25` supports better hybrid search results and richer result rankings. It also gives more stable result ordering across Search index partitions, when [global\_scoring](search-request-params.md#global%5Fscoring) is enabled.

## [](#ui)Run a Search with the Capella UI

You can use the Capella UI to test your Search index before you integrate search into your application.

You can enter a basic search query in the Capella UI, or use a [query object](search-request-params.md#query) and other JSON properties for a more complex search.

For more information about how to run a search with the Capella UI, see [Run A Simple Search with the Capella UI](simple-search-ui.md).

For more information about how to configure a Search index and search for geospatial data, see [Run a Geospatial Search Query with the Capella UI](geo-search-ui.md).

## [](#sql)Run a Search with a SQL++ Query

Use the [Query tab](../clusters/query-service/query-workbench.md) to search using natural-language search and SQL++ features in the same query.

When using SQL++ with a hybrid [Vector Search](../vector-search/vector-search.md) query, you have more flexibility in how you choose to display your search results. When running a hybrid search with the [Web Console](#ui) or [REST API](#api), the Search Service displays results as a disjunct (`OR`) between your 2 search queries. For example:

{
    "query":
    {
        "match_phrase": "my regular query"
    }
}

OR

{
    "knn": [
        "k": 5,
        "field": "vector_field",
        "vector": [0, 0, 128]
    ]
}

SQL++ allows you to choose whether to return search results as a conjunct (`AND`) or a disjunct (`OR`) for hybrid search queries.

As a conjunct, the Search Service:

* Returns matches that score highly for both the regular Search query and the Vector Search query.
* Excludes matches that only match the Vector Search query. For example:

```sqlpp
SELECT meta().id FROM <key_space>
WHERE text = "content"
AND SEARCH(<key_space>, {"query": {"match": "content", "field": "text"}, "knn": {"vector": <vector_embedding>", "field": "vector_field", "k": 5}});
```

As a disjunct, the Search Service:

* Returns matches for the regular Search query, followed by matches for the Vector Search query.

As a result, you could see matches for the Vector Search query that do not contain matches for the regular Search query.

For example:

```sqlpp
SELECT meta().id FROM <key_space>
WHERE SEARCH (<key_space>, {"query": {"match": "content", "field": "text"}, "knn": {"vector": <vector_embedding>", "field": "vector_field", "k": 5}});
```

For more information about how to use the Search Service from a SQL++ query, see [Search Functions](../n1ql/n1ql-language-reference/searchfun.md).

## [](#see-also)See Also

* [Create a Search Index](create-search-indexes.md)
* [Search Index Features](customize-index.md)
* [Create Search Index Aliases](index-aliases.md)