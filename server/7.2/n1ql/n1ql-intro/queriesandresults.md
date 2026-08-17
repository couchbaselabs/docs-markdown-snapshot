---
title: SQL++ Queries and Results
description: An overview of common concepts that you will need to understand in
  order to use the Query service.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-intro/queriesandresults.adoc
  xref: xref:7.2@server:n1ql:n1ql-intro/queriesandresults.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-intro/queriesandresults.html)

# SQL++ Queries and Results

> An overview of common concepts that you will need to understand in order to use the Query service. 

## [](#queries)Queries

A SQL++ query is a string parsed by the query service. The SQL++ query language is based on SQL, but designed for structured and flexible JSON documents.

As with SQL, you can have nested sub-queries. SQL++ queries run on JSON documents, and you can query over multiple documents by using the `JOIN` clause.

Because data in SQL++ can be nested, there are operators and functions that let you navigate through nested arrays. Because data can be irregular, you can specify conditions in the `WHERE` clause to retrieve data.

You can use standard `GROUP BY`, `ORDER BY`, `LIMIT`, and `OFFSET` clauses as well as a rich set of functions to transform the results as needed.

## [](#results)Results

The result for each query is a set of JSON documents. The returned document set is not required to be uniform, though it can be. A `SELECT` statement that specifies a fixed set of attribute (column) names results in a uniform set of documents and a `SELECT` statement that specifies the wild card (\*) results in a non-uniform result set. The only guarantee is that every returned document meets the query criteria.

Here's a sample query and the result returned:

Query

```sqlpp
SELECT name, brewery_id from `beer-sample` WHERE brewery_id IS NOT MISSING LIMIT 2;
```

Result

```json
{
    "requestID": "fbea9e79-a2e2-4ab8-9fdc-14e098838cc1",
    "signature": {
        "brewery_id": "json",
        "name": "json"
    },
    "results": [
        {
            "brewery_id": "big_horn_brewing_the_ram_2",
            "name": "Schaumbergfest"
        },
        {
            "brewery_id": "ballast_point_brewing",
            "name": "Wahoo Wheat Beer"
        }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "131.492184ms",
        "executionTime": "131.261322ms",
        "resultCount": 2,
        "resultSize": 205
    }
}
```

## [](#keyspace-reference)Keyspace References

Couchbase stores data within a logical hierarchy of buckets, scopes, and collections. This enables separation between documents of different types. For most queries, you must provide one or more keyspace references to specify the data sources for the query.

A keyspace reference may be a _full_ keyspace reference: a path comprising the bucket, the scope, and the collection which contains the documents you want.

Alternatively, the keyspace reference may be a _partial_ keyspace reference, comprising the collection name only. When a query contains partial keyspace references, you must set the [query context](#query-context) to specify a bucket and scope before running a query. Partial keyspace references are resolved using the bucket and scope supplied by the query context.

For compatibility with legacy versions of Couchbase Server, a keyspace reference may comprise the bucket name only, when referring to the default collection in the default scope within a bucket. In this case, the [query context](#query-context) must not be set.

## [](#query-context)Query Context

The _query context_ specifies the the namespace, bucket, and scope used to resolve partial keyspace references.

When the query context is set, you can refer to a collection using just the collection name, without having to enter the keyspace path. When the query context is not set, it defaults to the `default` namespace, with no bucket, scope, or collection.

* To set the query context in the Query Workbench, use the the [query context](../../tools/query-workbench.md#query-context) drop-down menu in the Query Editor.
* To set the query context from the cbq shell or the REST API, use the [query\_context](../../settings/query-settings.md#query%5Fcontext) request-level parameter.

> [!IMPORTANT]
> Tenant separation
> 
> By using queries with partial keyspace references, which are resolved using the query context, a database application can be switched from one scope to another simply by changing the query context. This can be used to support the separation of tenant data in a multi-tenancy environment.

## [](#paths)Paths

One of the main differences between JSON and flat rows is that JSON supports a nested structure, allowing documents to contain other documents, also known as sub-documents. SQL++ provides _paths_ to support nested data. Paths use dot notation syntax to identify the logical location of an attribute within a document. For example, to get the street from a customer order, use the path `orders.billTo.street`. This path refers to the value for `street` in the `billTo` object. A path is used with arrays or nested objects to get to attributes within the data structure.

Array syntax in the path can also be used to get to information. For example, the path `orders.items[0].productId` evaluates to the `productId` value for the first array element under the order item, `items`.

Paths provide a method for finding data in document structures without having to retrieve the entire document or handle it within an application. Any document data can be requested and returned to an application. When only relevant information is returned to an application, querying bandwidth is reduced.

See [Nested Path Expressions](../n1ql-language-reference/index.md#nested-path-expressions) for more details.

## [](#named-placeholders)Parameterized Queries

SQL++ allows the use of placeholders to declare dynamic query parameters. When the query is constructed, it may receive arguments, with each argument being used as the placeholder value in the query.

Placeholders in the query may be numbered positional placeholders, unnumbered positional placeholders, or named placeholders.

* A numbered positional placeholder takes the form `$1`. Thus, in the query, `$1` refers to the first argument,`$2` to the second, and so on.
* An unnumbered positional parameter takes the form of a question mark `?`. The first occurrence of `?` refers to the first argument, the second occurrence of `?` to the second, and so on.
* Named placeholders take the form of `$name`. This is particularly useful when there are many query parameters, and ensuring that they are all in the correct order may be cumbersome.

You can set query parameter values when you run the query, using the cbq query shell, the Query Workbench, or the SQL++ REST API.

For more information and examples, refer to [Named Parameters and Positional Parameters](../../settings/query-settings.md#section%5Fsrh%5Ftlm%5Fn1b).

## [](#prepare-stmts)Query Optimization Using Prepared Statements

When a SQL++ query string is sent to the server, the server will inspect the string and parse it, planning which indexes to query. Once this is done, it generates a _query plan_. The computation for the plan adds some additional processing time and overhead for the query.

A frequently-used query can be _prepared_ so that its _plan_ is generated only once. Subsequent queries using the same query string will use the pre-generated _plan_ instead, saving on the overhead and processing of the plan each time.

> [!NOTE]
> Parameterized queries are considered the same query for caching and planning purposes, even if the supplied parameters are different.

For more information on how to optimize queries using prepared statements, refer to the [PREPARE](../n1ql-language-reference/prepare.md) statement.

## [](#indexes)Indexes

The Couchbase query service makes use of _indexes_ in order to do its work. Indexes replicate subsets of documents from data nodes over to index nodes, allowing specific data (for example, specific document properties) to be retrieved quickly, (and to distribute load away from data nodes in MDS topologies).

In order to make a keyspace queryable, it must have at least one index defined.

* You can define a _primary index_ on a keyspace. Primary indexes are based on the unique key of every item in a specified collection. A primary index is intended to be used for simple queries, which have no filters or predicates.
* You can also create a _secondary index_ on specific fields in a keyspace. Secondary indexes, often referred to as Global Secondary Indexes or GSIs, constitute the principal means of indexing documents to be accessed by the Query Service.  
For example, creating a secondary index on the `name` and `email` fields in the `users` keyspace would allow you to query the keyspace regarding a document's `name` or `email` properties.

Indexes help improve the performance of a query. When an index includes the actual values of all the fields specified in the query, the index covers the query and eliminates the need to fetch the actual values from the Data Service. An index, in this case, is called a covering index and the query is called a covered query.

For more information, refer to [Using Indexes](../../learn/services-and-indexes/indexes/global-secondary-indexes.md).

## [](#index-building)Index Building

Index creation happens in two phases: the _creation phase_ and the _build phase_. During the creation phase, the Index Service validates the user input, decides the host node for the index, and creates the index metadata on the host node. During the build phase, the Index Service reads the documents from the Data Service and builds the index. The build phase cannot start until the creation phase is complete.

Creating and building indexes can take a long time on keyspaces with lots of existing documents. When you create an index, you can choose to _defer_ the build phase, and then build the deferred index later. This allows multiple indexes to be built at once rather than having to re-scan the entire keyspace for each index.

For more information and examples, refer to [CREATE PRIMARY INDEX](../n1ql-language-reference/createprimaryindex.md), [CREATE INDEX](../n1ql-language-reference/createindex.md), and [BUILD INDEX](../n1ql-language-reference/build-index.md).

## [](#index-consistency)Index Consistency

Because indexes are by design outside the data service, they are eventually consistent with respect to changes to documents and, depending on how you issue the query, may at times not contain the most up-to-date information. This may especially be the case when deployed in a write-heavy environment: changes may take some time to propagate over to the index nodes.

The asynchronous updating nature of global secondary indexes means that they can be very quick to query and do not require the additional overhead of index recalculations at the time documents are modified. SQL++ queries are forwarded to the relevant indexes and the queries are done based on indexed information, rather than the documents as they exist in the data service.

With default query options, the query service will rely on the current index state: the most up-to-date document versions are not retrieved, and only the indexed versions are queried. This provides the best performance. Only updates occurring with a small time frame may not yet have been indexed.

The query service can use the latest versions of documents by modifying the `consistency` of the query. This is done by setting the `scan_consistency` parameter to `REQUEST_PLUS`. When using this consistency mode, the query service will ensure that the indexes are synchronized with the data service before querying. For more information, refer to [Query Settings](../../settings/query-settings.md#scan%5Fconsistency).