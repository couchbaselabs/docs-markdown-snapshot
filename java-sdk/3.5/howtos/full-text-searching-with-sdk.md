---
title: Search
description: You can use the Full Text Search service (FTS) to create queryable
  full-text indexes in Couchbase Server.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.5/modules/howtos/pages/full-text-searching-with-sdk.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.5@java-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.5/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Full Text Search service (FTS) to create queryable full-text indexes in Couchbase Server. 

Full Text Search or FTS allows you to create, manage and query full text indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for indexing and querying documents, provides relevance scoring on the results of your queries and has fast indexes for querying a wide range of possible text searches.

Some of the supported query-types include simple queries like Match and Term queries, range queries like Date Range and Numeric Range and compound queries for conjunctions, disjunctions and/or boolean queries.

The Full Text Search service also supports vector search from Couchbase Server 7.6 onwards.

## [](#getting-started)Getting Started

After familiarizing yourself with how to create and query a Search index in the UI you can query it from the SDK.

There are two APIs for querying search: `cluster.searchQuery()`, and `cluster.search()`. Both are also available at the Scope level.

The former API supports FTS queries (`SearchQuery`), while the latter additionally supports the `VectorSearch` added in 7.6\. Most of this documentation will focus on the former API, as the latter is in @Stability.Volatile status.

We will perform an FTS query here - see the [\[vector search\]](#vector search) section for examples of that.

```java
try {
  final SearchResult result = cluster.searchQuery("travel-sample-index", SearchQuery.queryString("swanky"));

  for (SearchRow row : result.rows()) {
    System.out.println("Found row: " + row);
  }

  System.out.println("Reported total rows: " + result.metaData().metrics().totalRows());
} catch (CouchbaseException ex) {
  ex.printStackTrace();
}
```

Let’s break it down. The `searchQuery` API takes the name of the index and the type of query as required arguments and then allows to provide additional options if needed (in the example above, no options are specified).

Once a result returns you can iterate over the returned rows, and/or access the `SearchMetaData` associated with the query. If something goes wrong during the execution of the search query, a subclass of the `CouchbaseException` will be thrown that also provides additional context on the operation:

```console
Exception in thread "main" com.couchbase.client.core.error.IndexNotFoundException: Index not found {"completed":true,"coreId":1,"httpStatus":400,"idempotent":true,"lastDispatchedFrom":"127.0.0.1:53818","lastDispatchedTo":"127.0.0.1:8094","requestId":3,"requestType":"SearchRequest","service":{"indexName":"unknown-index","type":"search"},"status":"INVALID_ARGS","timeoutMs":75000,"timings":{"dispatchMicros":18289,"totalMicros":1359398}}
```

## [](#search-queries)Search Queries

The second mandatory argument in the example above used `SearchQuery.queryString("query")` to specify the query to run against the search index. The query string is the simplest form, but there are many more available. The table below lists all of them with a short description of each. You can combine them with `conjuncts` and `disjuncts` respectively.

__Table 1\. Available Search Queries__
| Name                                                                                               | Description                                                                                                                        |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| queryString(String query)                                                                          | Accept query strings, which express query-requirements in a special syntax.                                                        |
| match(String match)                                                                                | A match query analyzes input text, and uses the results to query an index.                                                         |
| matchPhrase(String matchPhrase)                                                                    | The input text is analyzed, and a phrase query is built with the terms resulting from the analysis.                                |
| prefix(String prefix)                                                                              | A prefix query finds documents containing terms that start with the specified prefix.                                              |
| regexp(String regexp)                                                                              | A regexp query finds documents containing terms that match the specified regular expression.                                       |
| termRange()                                                                                        | A term range query finds documents containing a term in the specified field within the specified range.                            |
| numericRange()                                                                                     | A numeric range query finds documents containing a numeric value in the specified field within the specified range.                |
| dateRange()                                                                                        | A date range query finds documents containing a date value, in the specified field within the specified range.                     |
| disjuncts(SearchQuery…​ queries)                                                                   | A disjunction query contains multiple child queries. Its result documents must satisfy a configurable min number of child queries. |
| conjuncts(SearchQuery…​ queries)                                                                   | A conjunction query contains multiple child queries. Its result documents must satisfy all of the child queries.                   |
| wildcard(String wildcard)                                                                          | A wildcard query uses a wildcard expression, to search within individual terms for matches.                                        |
| docId(String…​ docIds)                                                                             | A doc ID query returns the indexed document or documents among the specified set.                                                  |
| booleanField(boolean value)                                                                        | A boolean field query searches fields that contain boolean true or false values.                                                   |
| term(String term)                                                                                  | Performs an exact match in the index for the provided term.                                                                        |
| phrase(String…​ terms)                                                                             | A phrase query searches for terms occurring in the specified position and offsets.                                                 |
| matchAll()                                                                                         | Matches all documents in an index, irrespective of terms.                                                                          |
| matchNone()                                                                                        | Matches no documents in the index.                                                                                                 |
| geoBoundingBox(double topLeftLon, double topLeftLat, double bottomRightLon, double bottomRightLat) | Searches inside the given bounding box coordinates.                                                                                |
| geoDistance(double locationLon, double locationLat, String distance)                               | Searches inside the distance from the given location coordinate.                                                                   |

## [](#the-search-result)The Search Result

Once the Search query is executed successfully, the server starts sending back the resultant hits.

```java
final SearchResult result = cluster.searchQuery("travel-sample-index", SearchQuery.prefix("swim"),
    searchOptions().fields("description"));

for (SearchRow row : result.rows()) {
  System.out.println("Score: " + row.score());
  System.out.println("Document Id: " + row.id());

  // Also print fields that are included in the query
  System.out.println(row.fieldsAs(JsonObject.class));
}
```

The `SearchRow` contains the following methods:

__Table 2\. SearchRow__
| index()                           | The name of the FTS index that gave this result.                |
| --------------------------------- | --------------------------------------------------------------- |
| id()                              | The id of the matching document.                                |
| score()                           | The score of this hit.                                          |
| explanation()                     | If enabled provides an explanation in JSON form.                |
| locations()                       | The individual locations of the hits as SearchRowLocations.     |
| fragments()                       | The fragments for each field that was requested as highlighted. |
| fieldsAs(final Class<T> target)   | Access to the returned fields, decoded via a Class type.        |
| fieldsAs(final TypeRef<T> target) | Access to the returned fields, decoded via a TypeRef type.      |

Note that the `SearchMetaData` also contains potential `errors`, because the SDK will keep streaming results if the initial response came back successfully. This makes sure that even with partial data usually Search results are useable, so if you absolutely need to check if all partitions are present in the result double check the error (and not only catch an exception on the query itself).

## [](#search-options)Search Options

The Search Service provides an array of options to customize your query. The following table lists them all:

__Table 3\. Available Search Options__
| Name                                   | Description                                                          |
| -------------------------------------- | -------------------------------------------------------------------- |
| limit(int)                             | Allows to limit the number of hits returned.                         |
| skip(int)                              | Allows to skip the first N hits of the results returned.             |
| explain(boolean)                       | Adds additional explain debug information to the result.             |
| scanConsistency(SearchScanConsistency) | Specifies a different consistency level for the result hits.         |
| consistentWith(MutationState)          | Allows to be consistent with previously performed mutations.         |
| highlight(HighlightStyle, String…​)    | Specifies highlighting rules for matched fields.                     |
| sort(Object)                           | Allows to provide custom sorting rules.                              |
| facets(Map<String, SearchFacet>)       | Allows to fetch facets in addition to the regular hits.              |
| fields(String…​)                       | Specifies fields to be included.                                     |
| serializer(JsonSerializer)             | Allows to use a different serializer for the decoding of the rows.   |
| raw(String, Object)                    | Escape hatch to add arguments that are not covered by these options. |
| collections(String…​)                  | Limits the search query to a specific list of collection names.      |

### [](#limit-and-skip)Limit and Skip

It is possible to limit the returned results to a maximum amount using the `limit` option. If you want to skip the first N records it can be done with the `skip` option.

```java
SearchResult result = cluster.searchQuery("travel-sample-index", SearchQuery.queryString("swanky"),
    searchOptions().skip(3).limit(4));
```

### [](#scanconsistency-and-consistentwith)ScanConsistency and ConsistentWith

By default, all Search queries will return the data from whatever is in the index at the time of query. These semantics can be tuned if needed so that the hits returned include the most recently performed mutations, at the cost of slightly higher latency since the index needs to be updated first.

There are two ways to control consistency: either by supplying a custom `SearchScanConsistency` or using `consistentWith`. At the moment the cluster only supports `consistentWith`, which is why you only see `SearchScanConsistency.NOT_BOUNDED` in the enum which is the default setting. The way to make sure that recently written documents show up in the rfc works as follows (commonly referred to "read your own writes" — RYOW):

```java
MutationResult mutationResult = collection.upsert("key", JsonObject.create().put("description", "swanky"));
MutationState mutationState = MutationState.from(mutationResult.mutationToken().get());

SearchResult searchResult = cluster.searchQuery("travel-sample-index", SearchQuery.queryString("swanky"),
    searchOptions().consistentWith(mutationState));
```

### [](#highlight)Highlight

It is possible to enable highlighting for matched fields. You can either rely on the default highlighting style or provide a specific one. The following snippet uses HTML formatting for two fields:

```java
SearchResult result = cluster.searchQuery("travel-sample-index", SearchQuery.queryString("swanky"),
    searchOptions().highlight(HighlightStyle.HTML, "description", "type"));
```

### [](#sort)Sort

By default the Search Engine will sort the results in descending order by score. This behavior can be modified by providing a different sorting order which can also be nested.

```java
SearchResult result = cluster.searchQuery("travel-sample-index", SearchQuery.queryString("swanky"),
    searchOptions().sort(SearchSort.byScore(), SearchSort.byField("description")));
```

Facets are aggregate information collected on a result set and are useful when it comes to categorization of result data. The SDK allows you to provide many different facet configurations to the Search Engine, the following example shows how to create a facet based on a term. Other possible facets include numeric and date ranges.

### [](#facets)Facets

```java
Map<String, SearchFacet> facets = new HashMap<>();
facets.put("types", SearchFacet.term("type", 5));

SearchResult result = cluster.searchQuery("travel-sample-index", SearchQuery.queryString("United States"),
    searchOptions().facets(facets));
```

### [](#fields)Fields

You can tell the Search Engine to include the full content of a certain number of indexed fields in the response.

```java
SearchResult result = cluster.searchQuery("travel-sample-index", SearchQuery.queryString("swanky"),
    searchOptions().fields("description", "type"));
```

### [](#collections)Collections

It is now possible to limit the search query to a specific list of collection names.

Note that this feature is only supported with Couchbase Server 7.0 or later.

```java
SearchResult result = cluster.searchQuery("travel-sample-index", SearchQuery.queryString("San Francisco"),
    searchOptions().collections("landmark", "airport"));
```

### [](#custom-json-serializer)Custom JSON Serializer

As with all JSON APIs, it is possible to customize the JSON serializer. You can plug in your own library (like GSON) or custom configure mappings on your own Jackson serializer. This in turn makes it possible to serialize rows into POJOs or other structures that your application defines, and which the SDK has no idea about.

Please see the [documentation on transcoding and serialization](transcoders-nonjson.md) for more information.

## [](#reactive-and-async-apis)Reactive And Async APIs

In addition to the blocking API on `Cluster`, the SDK provides reactive and async APIs on `ReactiveCluster` or `AsyncCluster` respectively (and similar for `Scope`, `ReactiveScope` and `AsyncScope`). If you are in doubt of which API to use, we recommend looking at the reactive first: it builds on top of reactor, a powerful library that allows you to compose reactive computations and deal with error handling and other related concerns (like retry) in an elegant manner. The async API on the other hand exposes a `CompletableFuture` and is more intended for lower level integration into other libraries or if you need the last drop of performance.

There is another reason for using the reactive API here: streaming large results with backpressure from the application side. Both the blocking and async APIs have no means of signalling backpressure in a good way, so if you need it the reactive API is your best option.

> [!TIP]
> Advanced Reactive Concepts Ahead
> 
> Please see recent guides to reactive programming for more information on the basics — this guide dives straight into their impact on querying search.

A simple reactive query is similar to the blocking one:

```java
Mono<ReactiveSearchResult> result = cluster.reactive().searchQuery("travel-sample-index",
    SearchQuery.queryString("swanky"));

result.flatMapMany(ReactiveSearchResult::rows).subscribe(row -> System.out.println("Found reactive row: " + row));
```

This Search query will stream all rows as they become available form the server. If you want to manually control the data flow (which is important if you are streaming a lot of rows which could cause a potential out of memory situation) you can do this by using explicit `request()` calls.

```java
Mono<ReactiveSearchResult> result = cluster.reactive().searchQuery("travel-sample-index",
    SearchQuery.queryString("swanky"));

result.flatMapMany(ReactiveSearchResult::rows).subscribe(new BaseSubscriber<SearchRow>() {
  // Number of outstanding requests
  final AtomicInteger oustanding = new AtomicInteger(0);

  @Override
  protected void hookOnSubscribe(Subscription subscription) {
    request(10); // initially request to rows
    oustanding.set(10);
  }

  @Override
  protected void hookOnNext(SearchRow row) {
    process(row);
    if (oustanding.decrementAndGet() == 0) {
      request(10);
    }
  }
});
```

In this example we initially request a batch size of 10 rows (so streaming can begin). Then as each row gets streamed it is written to a `process()` method which does whatever it needs to do to process. Then a counter is decremented, and once all of the 10 outstanding rows are processed another batch is loaded. Please note that with reactive code, if your `process()` method equivalent is blocking, you **must** move it onto another scheduler so that the I/O threads are not stalled. We always recommend not blocking in the first place in reactive code.