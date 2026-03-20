---
title: Search
description: You can use the Full Text Search (FTS) service to find JSON
  documents that have certain words, phrases, or geographic coordinates -- and
  for vector searches against Server 7.6.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/1.3/modules/howtos/pages/full-text-search.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:1.3@kotlin-sdk:howtos:full-text-search.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/1.3/howtos/full-text-search.html)

# Search

> You can use the Full Text Search (FTS) service to find JSON documents that have certain words, phrases, or geographic coordinates — and for vector searches against Server 7.6\. 

The Full Text Search (FTS) service finds JSON documents that have certain words, phrases, or geographic coordinates. It can also search numeric and date/time fields.

The Full Text Search service also supports vector search from Couchbase Server 7.6 onwards.

When searching for words and phrases, you can look for an exact match or similar words (like "beauty" and "beautiful"). For numbers and dates, you can look for values in a range. For geographic coordinates, you can look for values near a location or within a region.

For all kinds of FTS searches, you can ask the server to count the number of matching documents that belong to different categories, called "facets."

## [](#prerequisites)Before You Start

You should know [how to create a Full Text Search index](../../../server/7.6/search/create-search-indexes.md).

You should know [how to connect to a Couchbase cluster](connecting.md).

The examples on this page use the `travel-sample` and `beer-sample` [sample buckets](../../../server/7.6/manage/manage-settings/install-sample-buckets.md).

## [](#simple-example)A Simple FTS Search

This example searches for documents that have the word "pool" in one of the indexed fields.

If you want to run this example, first create an index called `travel-sample-index` on the `travel-sample` bucket. Then run:

```kotlin
val searchResult: SearchResult = cluster
    .searchQuery(
        indexName = "travel-sample-index",
        query = SearchQuery.queryString("pool"), (1)
    )
    .execute() (2)

searchResult.rows.forEach { row: SearchRow ->
    println("Document ${row.id} has score ${row.score}")
    println(row)
}
```

| **1** | The argument to queryString uses the same syntax as when you search an index using the Couchbase web UI. SearchQuery has other companion factory methods for doing different kinds of searches. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The searchQuery method returns a Flow<SearchFlowItem>. Nothing happens until you collect the flow. Calling execute is an easy way to collect the flow.                                          |

## [](#query-types)Queries

The FTS service can do [many kinds of queries](../../../server/7.6/search/search-request-params.md). The Kotlin SDK’s `SearchQuery` class has a companion factory method for each kind of query.

## [](#result-rows)Result Rows

Each matching document is returned as a `SearchRow`. By default, a `SearchRow` only has a document ID, a score, and the name of the FTS index partition it came from. The `searchQuery` method has optional parameters that let you request more information about the matching document.

### [](#score)Score

The server gives each row a numeric score. A higher score means the row is a better match.

#### [](#explain-score)Explain the score

If you want to know how the server calculated the score, pass `explain = true` when calling `searchQuery`, like this:

Explain scoring

```kotlin
val searchResult: SearchResult = cluster
    .searchQuery(
        indexName = "travel-sample-index",
        query = SearchQuery.queryString("pool"),
        explain = true, (1)
    )
    .execute()

searchResult.rows.forEach { row ->
    println(String(row.explanation)) (2)
}
```

| **1** | This line tells the server you want to know how each score is calculated. If you don’t do this, row.explanation is an empty ByteArray. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | row.explanation is a ByteArray holding a JSON Object. This example just prints it, but you can parse it as JSON if you want.           |

#### [](#disable-score)Disable scoring

Calculating the score takes time. If you don’t need the score, tell the server to give each row a score of zero, like this:

> [!NOTE]
> Disabling scoring requires Couchbase Server 6.6.1 or later.

Disable scoring

```kotlin
val searchResult: SearchResult = cluster
    .searchQuery(
        indexName = "travel-sample-index",
        query = SearchQuery.queryString("pool"),
        score = Score.none(), (1)
    )
    .execute()
```

| **1** | This line tells the server you don’t care about scores. |
| ----- | ------------------------------------------------------- |

### [](#fields)Fields

By default, the server does not return any document content. You can tell the server to return stored document fields. Pass `fields = listOf("*")` when calling `searchQuery` to include all stored fields in the result. If you only want fields "foo" and "bar", pass `fields = listOf("foo", "bar")`.

> [!TIP]
> Only stored fields are included. If you’re not getting the results you expect, check the index definition.

Include stored fields in result rows

```kotlin
val searchResult: SearchResult = cluster
    .searchQuery(
        indexName = "travel-sample-index",
        query = SearchQuery.queryString("pool"),
        fields = listOf("*"), (1)
    )
    .execute()

searchResult.rows.forEach { row ->
    println(row.fieldsAs<Map<String, Any?>>()) (2)
}
```

| **1** | This line tells the server you want the result rows to include _all_ stored fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | row.fields is a ByteArray holding a JSON object that has the requested fields. The row.fieldsAs<T> method uses data binding to convert the JSON into an instance of T? (in this case, a Kotlin Map). If you want, you can convert the fields into an instance of a user-defined class instead of a Map. See [Working with JSON](json.md) for more information about data binding. If all requested fields are missing or unstored, and you’re not searching a multi-collection index, row.fields is null and row.fieldsAs<T> returns null. |

### [](#collections)Collections

Couchbase 7.0 and later let you define an index on multiple collections in the same scope. You can limit the search to specific collections using the optional `collections` parameter of the `searchQuery` method.

> [!TIP]
> When searching a multi-index collection, the server always returns a field called `_$c`. The value of this field is the name of the matching document’s parent collection.

```kotlin
val searchResult: SearchResult = cluster
    .searchQuery(
        indexName = "travel-sample-multi-collection-index",
        query = SearchQuery.queryString("San Francisco"),
        collections = listOf("airport", "landmark") (1)
    )
    .execute()

searchResult.rows.forEach { row ->
    val fields = row.fieldsAs<Map<String, Any?>>()
    val collection = fields?.get("_\$c") (2)
    println("Found document ${row.id} in collection $collection")
}
```

| **1** | The server only searches in these collections                             |
| ----- | ------------------------------------------------------------------------- |
| **2** | The \_$c field is always present when searching a multi-collection index. |

> [!CAUTION]
> Be careful when using [keyset pagination](#keyset-pagination) with a multi-collection index. Documents in different collections can have the same ID, so sorting by ID does not necessarily guarantee a total ordering of the results.

### [](#highlight)Highlight (fragments)

You can ask the server to include a fragment of a matching field value, and highlight the search term within the fragment.

> [!TIP]
> Highlighting requires storing the field value and including term vectors. If you’re not getting the results you expect, check the index definition.

Highlight matches

```kotlin
val searchResult: SearchResult = cluster
    .searchQuery(
        indexName = "travel-sample-index",
        query = SearchQuery.queryString("pool"),
        highlight = Highlight.html() (1)
    )
    .execute()

searchResult.rows.forEach { row ->
    println(row.locations) (2)
    println(row.fragments) (3)
}
```

| **1** | This line tells the server you want the result to include fragments, and you want the matching text to be wrapped in HTML tags, like this: <mark>pool</mark>. Alternatively, you can use Highlight.ansi() to mark the matches using ANSI escape codes. The Highlight.html and ansi methods have an optional fields parameter that limits highlighting to only the fields you specify. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | When you request highlighting, the server also tells you the location of the matched text within the field.                                                                                                                                                                                                                                                                           |
| **3** | The row.fragments property is a Map<String, List<String>>. Each key is name of a field where a search term was found. The value is a list of fragments of the field text, with the search term highlighted.                                                                                                                                                                           |

### [](#locations)Locations

When you request [highlighting](#highlight), the server also return the locations of the matched terms within the field value. The `SearchRow.locations` property is a list of `SearchLocation` objects.

If you want the location information, but don’t need fragments, pass `includeLocations = true` when calling `searchQuery` instead of passing a value for `highlight`.

> [!TIP]
> To get locations, the index must include term vectors for the field. If you’re not getting the results you expect, check the index definition.

## [](#sorting)Sorting

By default, result rows are sorted by score, from highest to lowest. Use the `sort` parameter to tell the server to sort the rows differently.

This example sorts the results by the value of the "country" field:

Sort by `country` field

```kotlin
val searchResult: SearchResult = cluster
    .searchQuery(
        indexName = "travel-sample-index",
        query = SearchQuery.queryString("pool"),
        sort = SearchSort.byField("country"), (1)
    )
    .execute()
```

| **1** | byField also has optional parameters. We will talk about them next. |
| ----- | ------------------------------------------------------------------- |

`SearchSort` has companion factory methods for creating `SearchSort` objects. These objects tell the server how to sort the results.

### [](#sorting-by-field)Sorting by field value

`SearchSort.byField` tells the server to sort the rows using the value of a document field.

Required parameter:

* **`field: String`** — Name of the field to use.

Optional parameters:

* **`direction: Direction`** — Can be `ASCENDING` (A to Z) or `DESCENDING` (Z to A). The default direction is `ASCENDING`.
* **`missing: Missing`** — Tells the server where to put rows that don’t have a value for the field. Can be `FIRST` or `LAST`. The default is `LAST`.
* **`type: FieldType`** — The type of the field. Can be `STRING`, `NUMBER`, `DATE`, or `AUTO`. The default type is `AUTO`, which tells the server to infer the type.
* **`mode: Mode`** — A field can have more than one value. This happens if the value is an array, or if the value is a string that is analyzed as more than one token. The `mode` parameter tells the server which value to use for sorting. If a field does not have more than one value, this parameter does nothing. Possible values:

  * **`MIN`** — Use the minimum value.
  * **`MAX`** — Use the maximum value.
  * **`DEFAULT`** — The server sorts the rows the same way every time, but the order is unspecified.  
  The default mode is `DEFAULT`.

### [](#sorting-by-score)Sorting by score

`SearchSort.byScore` tells the server to sort the rows using each row’s score.

Optional parameters:

* **`direction: Direction`** — `ASCENDING` (low to high) or `DESCENDING` (high to low). The default direction is `DESCENDING`.

### [](#sorting-by-id)Sorting by document ID

`SearchSort.byId` tells the server to sort the rows using each row’s document ID.

Optional parameters:

* **`direction: Direction`** — `ASCENDING` (A to Z) or `DESCENDING` (Z to A). The default direction is `ASCENDING`.

### [](#sorting-by-geo-distance)Sorting by geographic distance

`SearchSort.byGeoDistance` tells the server to look at a field that has a geographic location, and sort the rows based on how far the field value is from some other location.

Required parameters:

* **`field: String`** — Name of the field to use. The field must be indexed as a geographic point.
* **`location: GeoPoint`** — The starting point for measuring distance.

Optional parameters:

* **`direction: Direction`** — `ASCENDING` (near to far) or `DESCENDING` (far to near). The default direction is `ASCENDING`.
* **`unit: GeoDistanceUnit`** — The unit of measurement to use for reporting the distance. The default unit is `GeoDistanceUnit.METERS`.

### [](#sorting-by-string-syntax)Sorting with string syntax

`SearchSort.by` lets you specify the sort using the syntax described in [Sorting with Strings](../../../server/7.6/fts/fts-search-response.md#sorting-with-strings). For example:

Sorting with strings

```kotlin
val sort: SearchSort = SearchSort.by(
    "country", "state", "city", "-_score"
)
```

### [](#multi-level-sorting)More than one sort

You can join `SearchSort` objects to create a sort with more than one level. Here are two examples that do the same thing in different ways:

Multi-level sort using the `then` infix method

```kotlin
val multiLevelSort: SearchSort =
    SearchSort.byField("country") then SearchSort.byId()
```

Multi-level sort using the `SearchSort.of` companion factory method

```kotlin
val multiLevelSort: SearchSort = SearchSort.of(
    listOf(
        SearchSort.byField("country"),
        SearchSort.byId(),
    )
)
```

First, the rows are sorted by the value of the "country" field. Then, rows with the same country are sorted by document ID.

> [!NOTE]
> The example for [Sorting with string syntax](#sorting-by-string-syntax) also creates a multi-level sort.

## [](#pagination)Pagination

If you don’t need all the result rows at once, you can ask the server to return one page at a time.

The `searchQuery` method has a `limit` parameter that tells the server how many rows to return. This is the page size.

There is also a `page` parameter that tells the server which rows to include in the results. There are two ways to ask for a page.

### [](#offset-pagination)Offset pagination

With offset pagination, you tell the server how many result rows to skip before it should start including rows in the result.

For example, this code skips the first 10 rows:

Offset-based pagination

```kotlin
val searchResult: SearchResult = cluster
    .searchQuery(
        indexName = "travel-sample-index",
        query = SearchQuery.queryString("pool"),
        page = SearchPage.startAt(offset = 10), (1)
        limit = 10,
    )
    .execute()
```

| **1** | Offsets are zero-based, so this skips the first 10 rows. |
| ----- | -------------------------------------------------------- |

This kind of pagination is unstable, because a row’s offset can change if a different document is changed, added, or removed. Imagine this happens:

1. You ask for the first page, using offset 0 and limit 10.
2. Someone removes from Couchbase the document at offset 3.
3. You ask for the second page, using offset 10 and limit 10.

After step 2, the row that would have been the first row of the second page is now the last row of the first page. Now in step 3, you don’t see the row that "moved" to the first page.

Offset pagination can be expensive if the offset is very large.

### [](#keyset-pagination)Keyset pagination

> [!NOTE]
> Keyset pagination requires Couchbase Server 6.6.1 or later.

When the server sorts the search results, it assigns a "sort key" to each row. The sort key is also called the "keyset".

With keyset pagination, you tell the server to return the page after (or before) a row whose keyset you remember from a previous search.

Here’s an example that uses offset pagination to get the first page. Then it uses keyset pagination to get the next page.

Keyset-based pagination

```kotlin
val indexName = "travel-sample-index"
val query = SearchQuery.queryString("pool")
val sort = SearchSort.byId()
val pageSize = 10

val firstPage: SearchResult = cluster
    .searchQuery(
        indexName = indexName,
        query = query,
        sort = sort,
        limit = pageSize,
        page = SearchPage.startAt(offset = 0), (1)
    )
    .execute()

check(firstPage.rows.isNotEmpty()) { "Oops, no results!" }
val lastRowOfFirstPage: SearchRow = firstPage.rows.last()

val nextPage: SearchResult = cluster
    .searchQuery(
        indexName = indexName,
        query = query,
        sort = sort,
        limit = pageSize,
        page = SearchPage.searchAfter( (2)
            lastRowOfFirstPage.keyset
        ),
    )
    .execute()
```

| **1** | Starting at offset 0 is the default. You can remove this line.               |
| ----- | ---------------------------------------------------------------------------- |
| **2** | There is also a searchBefore method. You can pass SearchKeyset or SearchRow. |

Keyset pagination is less expensive than offset pagination when the offset is large. Keyset pagination is stable if you are careful about sorting. See the cautions below.

> [!CAUTION]
> For stable keyset pagination, the `sort` argument must not let any two rows have the same keyset. It’s good to always use a [multi-level sort](#multi-level-sorting) that ends with `[SearchSort.byId()](#sorting-by-id)`, so no two rows have the same keyset. Be careful when searching a multi-collection index, since document IDs are only guaranteed to be unique within a single collection. Also be aware that including score in the sort might cause unstable pagination, since a document’s score can change when other documents are added or removed.

> [!CAUTION]
> Changing the sort invalidates a keyset (unless the new sort is the total opposite of the old sort). If you use a keyset to search with a different sort, you get bad results.

> [!TIP]
> `keyset.serialize()` converts a `SearchKeyset` to a string, so you can send it to a client. When you receive the string back from the client, pass it to the `SearchKeyset.deserialize` companion factory method to turn it back into a `SearchKeyset`.

### [](#total-rows)Total number of rows

The search result metadata has a `totalRows` property that tells you how many rows matched the query, even if you limit the results to fewer rows.

Getting the total number of rows

```kotlin
val searchResult: SearchResult = cluster
    .searchQuery(
        indexName = "travel-sample-index",
        query = SearchQuery.queryString("pool"),
        limit = 10,
    )
    .execute()

val total = searchResult.metadata.metrics.totalRows (1)
println("Total matching rows: $total")
```

| **1** | This can be greater than the limit argument. |
| ----- | -------------------------------------------- |

## [](#compound-queries)Compound Queries

You can use boolean logic to combine queries into a "compound query."

Imagine Alice is searching for a hotel. She would prefer a hotel with a sauna, but she would settle for a swimming pool.

Alice can use a `disjunction` query to search for "sauna" _or_ "pool". She can _boost_ the "sauna" query, so hotels with a sauna get higher scores relative to other hotels.

"OR" query with boost

```kotlin
val saunaOrPool: SearchQuery = SearchQuery.disjunction(
    SearchQuery.match("sauna") boost 1.5, (1)
    SearchQuery.match("pool"),
)
val searchResult: SearchResult = cluster
    .searchQuery(
        indexName = "travel-sample-index",
        query = saunaOrPool,
    )
    .execute()
```

| **1** | Alice thinks saunas are better than swimming pools, so she boosts this part of the query. |
| ----- | ----------------------------------------------------------------------------------------- |

> [!NOTE]
> Boosting a query has no effect unless the query is part of a compound query.

There are other kinds of compound queries. Use `conjunction` for "and". Use `negation` for "not". Use `boolean` for a complex query with "must", "should", and "mustNot" sub-queries.

## [](#facets)Facets

A facet is like a histogram. For each document matching the search query, the server inspects a field of the document to see which bin (or "category") the field value belongs to.

The FTS service supports three kinds of facets: `numeric`, `date`, and `term`.

For `numeric` and `date` facets, you specify the categories up front as value ranges. Common use cases include counting the number of documents in certain price ranges, like: $1 to $5, $5 to $20, and $20+, or time ranges like: "today", "yesterday", and "before yesterday".

> [!TIP]
> Unlike a histogram, it’s okay if the ranges overlap. If a field value matches more than one range, each matching range has its count incremented.

For `term` facets, the server creates one category for each distinct value it sees in the field.

For example, let’s say your documents have a "color" field where the value is one of "red", "green", or "blue". The result of a `term` facet on the "color" field tells you the number of times each color appears as the field value.

Facets have a `size` parameter, which is an upper bound on the number of categories reported in the facet result. For example, if you request a `size` of 3, the server does its best to return the 3 largest categories. To be more precise, it selects the top 3 categories from each partition executing the query, and then merges each partition’s result into the final result.

> [!NOTE]
> If you are using multiple partitions and require an exact result, the size must be >= the number of categories; otherwise the result should be considered an estimate.

Facet results are not affected by query pagination.

To create a facet, use one of the `SearchFacet` companion factory methods. To retrieve the result in a type-safe way, pass the facet to `SearchResult.get` (or `SearchMetadata.get`). Alternatively, iterate over `SearchResult.facets` (or `SearchMetadata.facets`) and cast each `FacetResult` to the appropriate type.

> [!NOTE]
> Facets and/or ranges with no matching documents are omitted from the results.

This example uses the `beer-sample` bucket. It requires an index called `beer-sample-index`, with fields "abv" and "category" indexed as stored fields.

Searching with facets

```kotlin
// Count results that fall into these "alcohol by volume" ranges.
// Optionally assign names to the ranges.
val low = NumericRange.bounds(min = 0, max = 3.5, name = "low")
val high = NumericRange.lowerBound(3.5, name = "high")
val abv = SearchFacet.numeric(
    field = "abv",
    ranges = listOf(low, high),
    name = "Alcohol by volume",
)

// Find the 5 most frequent values in the "category" field.
val beerType = SearchFacet.term("category", size = 5)

val result = cluster.searchQuery(
    indexName = "beer-sample-index",
    query = SearchQuery.matchAll(),
    facets = listOf(abv, beerType),
).execute()

// Print all facet results. Results do not include empty facets
// or ranges. Categories are ordered by size, descending.
result.facets.forEach { facet ->
    println(facet.name)
    facet.categories.forEach { println("  $it") }
    facet.other.let { if (it > 0) println("  <other> ($it)") }
    println()
}

// Alternatively, print results for a specific facet:
val abvResult = result[abv]
if (abvResult == null) {
    println("No search results matched any of the 'abv' facet ranges.")
} else {
    println("Alcohol by volume (again)")
    println(" low (${abvResult[low]?.count ?: 0})")
    println(" high (${abvResult[high]?.count ?: 0})")
    println()
}
```

## [](#scoped-vs-global-indexes)Scoped vs Global Indexes

The FTS APIs exist at both the `Cluster` and `Scope` levels.

This is because FTS supports, as of Couchbase Server 7.6, a new form of "scoped index" in addition to the traditional "global index".

It’s important to use the `Cluster.searchQuery()` or `Cluster.search()` methods for global indexes, and `Scope.search()` for scoped indexes.

## [](#vector-search)Vector Search

As of Couchbase Server 7.6, the FTS service supports vector search in addition to traditional full text search queries.

Suppose you have a scoped index called `vector-index`, and this index says the document field named `vector_field` contains a vector (an array of numbers). The following examples show different ways to do vector searches on this field.

> [!CAUTION]
> The following examples use `cluster/scope.search()` and `SearchSpec`. These bits of the SDK are currently experimental and may change without notice.

### [](#examples)Examples

#### [](#single-vector-search)Single vector search

This first example shows how to find documents whose `vector_field` value is near a single target vector:

Single vector query

```kotlin
val searchResult: SearchResult = scope.search( (1)
    indexName = "vector-index",
    spec = SearchSpec.vector(
        "vector_field",
        floatArray, (2)
        numCandidates = 5, (3)
    ),
).execute() (4)
```

| **1** | This happens to be a scoped index, so we are using scope.search(). If it was a global index we would use cluster.search() instead. See [Scoped vs Global Indexes](#scoped-vs-global-indexes).              |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Couchbase itself is not involved in generating the float array; it typically comes from an external source such as an embeddings API.                                                                      |
| **3** | The numCandidates parameter affects how many results are returned. It is optional, and defaults to 3.                                                                                                      |
| **4** | The search method returns the same Flow<SearchFlowItem> described earlier. Nothing happens until you collect the flow. Calling execute is an easy way to collect the flow and turn it into a SearchResult. |

#### [](#compound-vector-search)Compound vector search

You can build compound vector queries using `SearchSpec.allOf` or `SearchSpec.anyOf`.

Compound vector search

```kotlin
val searchResult: SearchResult = scope.search(
    indexName = "vector-index",
    spec = SearchSpec.anyOf( (1)
        SearchSpec.vector("vector_field", floatArray) boost 1.5, (2)
        SearchSpec.vector("vector_field", anotherFloatArray),
    )
).execute()
```

| **1** | SearchSpec.anyOf combines the child queries using a logical OR operator. For logical AND, use SearchSpec.allOf instead. |
| ----- | ----------------------------------------------------------------------------------------------------------------------- |
| **2** | Vector queries can be boosted just like non-vector queries. Boost is optional, and defaults to 1.0.                     |

#### [](#combining-vector-and-non-vector-search)Combining vector and non-vector search

You can use `SearchSpec.mixedMode` to combine a traditional FTS search query with vector search.

Mixed mode search

```kotlin
val searchResult: SearchResult = scope.search(
    indexName = "vector-and-non-vector-index",
    spec = SearchSpec.mixedMode(
        SearchSpec.match("beautiful"), (1)
        SearchSpec.vector("vector_field", floatArray),
    )
).execute()
```

| **1** | A traditional textual search query. |
| ----- | ----------------------------------- |

A mixed mode search always uses logical `OR` to combine the vector and non-vector results.

#### [](#textual-search)Textual search

Note that `cluster.search()` and `scope.search()` also work with traditional FTS queries, without vector search.

Traditional textual search

```kotlin
val searchResult: SearchResult = scope.search(
    indexName = "travel-sample-index",
    spec = SearchSpec.match("beautiful"), (1)
).execute()
```

| **1** | A traditional textual search query. |
| ----- | ----------------------------------- |

## [](#scan-consistency)Scan Consistency

When you change a document in Couchbase, it takes time for the FTS service to index the document. An FTS index "runs behind" the KV service. When you execute an FTS search, you get to choose if you want to wait for the index to "catch up" to the latest KV changes.

### [](#scan-consistency-unbounded)Unbounded

By default, the FTS service does not wait. It only searches documents that were already indexed when the search started. This is called "unbounded" scan consistency.

This is the default value for the `searchQuery` method’s `consistency` parameter.

### [](#scan-consistency-consistent-with)Consistent With

If you made some changes, you can tell the server to wait for the changes to be indexed. In other words, the search results are "consistent with" the changes you made. To use this kind of scan consistency, you must keep track of the mutation tokens from the changes you want to wait for.

```kotlin
val collection = cluster
    .bucket("travel-sample")
    .defaultCollection()

val mutationResult: MutationResult =
    collection.upsert(
        id = "my-fake-hotel",
        content = mapOf("description" to "This hotel is imaginary.")
    )

val mutationState = MutationState()
mutationState.add(mutationResult)

val queryResult: SearchResult = cluster
    .searchQuery(
        indexName = "travel-sample-index",
        query = SearchQuery.match("imaginary"),
        consistency = SearchScanConsistency
            .consistentWith(mutationState),
    )
    .execute()
```

## [](#partial-failures)Partial Failures

An FTS index can have multiple partitions that live on different Couchbase Server nodes. If there is a problem with a partition, the FTS service gives you the results from only the healthy partitions. Documents indexed by an unhealthy partition are not included in the results.

> [!NOTE]
> If no partitions are healthy, the `searchQuery` method throws an exception.

If you want to know if the FTS service was able to search all partitions, check the `SearchMetadata.errors` property. This property is a map where the key is the name of an index partition, and the value is an error reported by that partition.

```kotlin
val searchResult: SearchResult = cluster
    .searchQuery(
        indexName = "travel-sample-index",
        query = SearchQuery.queryString("pool")
    )
    .execute()

if (searchResult.metadata.errors.isNotEmpty()) {
    println("Partial failure!")
}

searchResult.metadata.errors.forEach { (indexPartition, errorMessage) ->
    println("Partition $indexPartition reported error: $errorMessage")
}
```

## [](#streaming)Streaming

The previous examples store all result rows in memory. If there are many rows, this can use a lot of memory.

To use less memory, pass a lambda to `execute` and work on each row one at a time, like this:

```kotlin
val searchMetadata: SearchMetadata = cluster
    .searchQuery(
        indexName = "travel-sample-index",
        query = SearchQuery.queryString("pool"),
    )
    .execute { row ->
        println("Found row: $row")
    }
```

> [!NOTE]
> The streaming version of `execute` returns `SearchMetadata` instead of `SearchResult`.