---
title: Search
description: You can use the Search Service to create queryable Search indexes
  in Couchbase Server.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.8/modules/howtos/pages/full-text-searching-with-sdk.adoc
  xref: xref:ruby-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/current/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Search Service to create queryable Search indexes in Couchbase Server. 

The Search Service allows you to create, manage, and query Search indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for querying documents, provides relevance scoring on the results of your queries, and has fast indexes for querying a wide range of possible text searches.

Some of the supported query types include simple queries like Match and Term queries; range queries like Date Range and Numeric Range; and compound queries for conjunctions, disjunctions, and/or boolean queries.

There are two APIs for querying search: `cluster.searchQuery()`, and `cluster.search()`. Both are also available at the Scope level.

The former API supports Search queries (`SearchQuery`), while the latter additionally supports the `VectorSearch` added in 7.6\. Most of this documentation will focus on the former API, as the latter is in @Stability.Volatile status.

> [!TIP]
> Search Results Limit
> 
> By default, the Search Service returns only the first 10 matches (`size: 10`, `from: 0`). To retrieve more results, you must explicitly define pagination settings such as `size` or `from` in your query.
> 
> For information about formatting your Search query and specifying limits, see [Search Request JSON Properties](../../../server/current/search/search-request-params.md).
> 
> For information about pagination in Search responses, see [Pagination](../../../server/current/fts/fts-search-response.md#pagination).

## [](#index-creation)Index Creation

For the purposes of the below examples we will use the Beer Sample sample bucket. Search indexes can be [created through the UI or throuth the REST API](../../../server/current/search/create-search-indexes.md), or created programatically as follows:

```ruby
Unresolved include directive in modules/howtos/pages/full-text-searching-with-sdk.adoc - include::example$search.rb[]
```

## [](#examples)Examples

In versions of Couchbase Server starting from 7.6, Search queries are executed at either the Scope or the Cluster level; in earlier versions, they are just performed at the cluster level. (not bucket or collection).

We will perform a Search query here - see the [\[vector search\]](#vector search) section for examples of that. Here is a simple query that looks for the text "hop beer" using the defined index:

```ruby
Unresolved include directive in modules/howtos/pages/full-text-searching-with-sdk.adoc - include::example$search.rb[]
```

`match_phrase()` builds a phrase query is built from the results of an analysis of the terms in the query phrase; here it's built on a search in the name field.

```ruby
Unresolved include directive in modules/howtos/pages/full-text-searching-with-sdk.adoc - include::example$search.rb[]
```

## [](#working-with-results)Working with Results

The result of a Search query has three components: rows, facets, and metdata. Rows are the documents that match the query. Facets allow the aggregation of information collected on a particular result set. Metdata holds additional information not directly related to your query, such as success, total hits, and how long the query took to execute in the cluster.

Iterating Rows

Here we are iterating over the rows that were returned in the results. Highlighting has been selected for the description field in each row, and the total number of rows is taken from the `metrics` returned in the metadata:

```ruby
Unresolved include directive in modules/howtos/pages/full-text-searching-with-sdk.adoc - include::example$search.rb[]
```

With `skip` and `limit` a slice of the returned data may be selected:

```ruby
Unresolved include directive in modules/howtos/pages/full-text-searching-with-sdk.adoc - include::example$search.rb[]
```

Ordering rules can be applied via `sort` and `SearchSort`:

```ruby
Unresolved include directive in modules/howtos/pages/full-text-searching-with-sdk.adoc - include::example$search.rb[]
```

Facets

```ruby
Unresolved include directive in modules/howtos/pages/full-text-searching-with-sdk.adoc - include::example$search.rb[]
```

## [](#scoped-vs-global-indexes)Scoped vs Global Indexes

The Search APIs exist at both the `Cluster` and `Scope` levels.

This is because the Search Service supports, as of Couchbase Server 7.6, a new form of "scoped index" in addition to the traditional "global index".

It's important to use the `Cluster.searchQuery()` / `Cluster.search()` for global indexes, and `Scope.search()` for scoped indexes.

```ruby
Unresolved include directive in modules/howtos/pages/full-text-searching-with-sdk.adoc - include::example$search.rb[]
```

The `SearchQuery` is created in the same way as detailed earlier.

## [](#consistency)Consistency

Like the [Couchbase Query Service](n1ql-queries-with-sdk.md#scan-consistency), the Search Service allows `consistent_with()` queries — _Read-Your-Own\_Writes (RYOW)_ consistency, ensuring results contain information from updated indexes:

```ruby
Unresolved include directive in modules/howtos/pages/full-text-searching-with-sdk.adoc - include::example$search.rb[]
```