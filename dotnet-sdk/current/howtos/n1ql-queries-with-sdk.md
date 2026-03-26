---
title: SQL++ Queries from the SDK
description: You can query for documents in Couchbase using the SQL++ query
  language, a language based on SQL, but designed for structured and flexible
  JSON documents.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.9/modules/howtos/pages/n1ql-queries-with-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:dotnet-sdk:howtos:n1ql-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/current/howtos/n1ql-queries-with-sdk.html)

# SQL++ Queries from the SDK

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. Querying can solve typical programming tasks such as finding a user profile by email address, facebook login, or user ID. 

Our query service uses SQL++ (formerly N1QL), which will be fairly familiar to anyone who's used any dialect of SQL. [Further resources](#additional-resources) for learning about SQL++ are listed at the bottom of the page. Before you get started you may wish to checkout the [SQL++ intro page](../../../server/current/n1ql/n1ql-language-reference/index.md), or just dive in with a query against [our travel sample data set](../../../server/current/manage/manage-settings/install-sample-buckets.md). In this case, the one thing that you need to know is that in order to make a Bucket queryable, it must have at least one index defined. You can define a _primary_ index on a bucket. When executing queries, if a suitable index is not found, the primary index will ensure that the query will be executed anyway (the primary index should not be used in production to prevent scanning of the whole bucket).

To execute SQL++, you can use [Query Workbench](../../../server/current/tools/query-workbench.md) (or you can use the [cbq command line tool](../../../server/current/n1ql/n1ql-intro/cbq.md)). Open it, and enter the following:

```n1ql
CREATE PRIMARY INDEX ON `travel-sample`
```

or replace _travel-sample_ with a different Bucket name to build an index on a different Bucket.

> [!NOTE]
> If you are using _travel-sample_, it comes with a primary index already created.

Note that building indexes is covered in more detail on the [Query concept page](../concept-docs/n1ql-query.md#index-building) — and in the [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Management.Query.CreateQueryIndexOptions.html).

## [](#parameterized-queries)Parameterized Queries

Parameters allow you to specify variable constraints for an otherwise constant query. Parameterization is also a good defense against [SQL injection](https://owasp.org/www-community/attacks/SQL%5FInjection). There are two variants of parameters: positional and named. Positional parameters use a numbered placeholder for substitution and named parameters use a named placeholder. A named or positional parameter can be used in the WHERE, LIMIT or OFFSET clauses of a query.

Positional parameter example:

```csharp
var result = await cluster.QueryAsync<dynamic>(
    "SELECT t.* FROM `travel-sample` t WHERE t.type=$1",
    options => options.Parameter("landmark")
);
```

Named parameter example:

```csharp
var result = await cluster.QueryAsync<dynamic>(
    "SELECT t.* FROM `travel-sample` t WHERE t.type=$type",
    options => options.Parameter("type", "landmark")
);
```

## [](#handling-results)Handling Results

In most cases your query will return more than one result, and you may be looking to iterate over those results:

```csharp
var result = await cluster.QueryAsync<dynamic>(
    "SELECT t.* FROM `travel-sample` t WHERE t.type=$type",
    options => options.Parameter("type", "landmark")
);
```

```csharp
        // check query was successful
        if (result.MetaData.Status != QueryStatus.Success)
        {
            // error
        }

        // iterate over rows
        await foreach (var row in result)
        {
            // each row is an instance of the Query<T> call (e.g. dynamic or custom type)
            var name = row.name;        // "Hollywood Bowl"
            var address = row.address;      // "4 High Street, ME7 1BB"
            Console.WriteLine($"{name},{address}");
        }
```

## [](#query-results)Query Results

When performing a query, the response you receive is an `IQueryResult`. If no exception gets raised, the request succeeded and provides access to both the rows returned and also associated `QueryMetaData`.

A type parameter must be used with `QueryAsync`, that will specify the type of rows that will be returned. This can be as generic as using `dynamic` or you can specify a POCO of your choice. For example, any of these are valid:

```csharp
        var resultDynamic = await cluster.QueryAsync<dynamic>("SELECT t.* FROM `travel-sample` t WHERE t.type='landmark' LIMIT 10");
        IAsyncEnumerable<dynamic> dynamicRows = resultDynamic.Rows;

        var resultPoco = await cluster.QueryAsync<Landmark>("SELECT t.* FROM `travel-sample` t WHERE t.type='landmark' LIMIT 10");
        IAsyncEnumerable<Landmark> pocoRows = resultPoco.Rows;
```

The `QueryMetaData` object (e.g. returned from `result.MetaData`) provides insight into some basic profiling/timing information as well as information like the clientContextId.

__Table 1\. QueryMetaData__
| Type               | Name            | Description                                                                      |
| ------------------ | --------------- | -------------------------------------------------------------------------------- |
| string             | RequestId       | Returns the request identifer of this request.                                   |
| string             | ClientContextId | Returns the context ID either generated by the SDK or supplied by the user.      |
| QueryStatus        | Status          | An enum simply representing the state of the result.                             |
| QueryMetrics       | Metrics         | Returns metrics provided by the query for the request if enabled.                |
| dynamic            | Signature       | If a signature is present, it will be available to consume in a dynamic fashion. |
| List<QueryWarning> | Warnings        | Non-fatal errors are available to consume as warnings on this method.            |
| dynamic            | Profile         | If enabled returns additional profiling information of the query.                |

For example, here is how you can print the executionTime of a query:

```csharp
        var result = await cluster.QueryAsync<dynamic>("SELECT 1=1", options => options.Metrics(true));

        var metrics = result.MetaData.Metrics;

        Console.WriteLine($"Execution time: {metrics.ExecutionTime}");
```

## [](#query-options)Query Options

The query service provides an array of options to customize your query. The following table lists them all:

__Table 2\. Available Query Options__
| Name                                  | Description                                                                                                                       |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| ClientContextId(string)               | Sets a context ID returned by the service for debugging purposes. See "Client Context Id" section for more detail                 |
| Parameter(object)                     | Allows to set positional arguments for a parameterized query.                                                                     |
| Parameter(string, object)             | Allows to set named arguments for a parameterized query.                                                                          |
| Raw(string, object)                   | Escape hatch to add arguments that are not covered by these options.                                                              |
| Readonly(bool)                        | Tells the client and server that this query is readonly. See "Readonly" section for more detail.                                  |
| Adhoc(bool)                           | If set to false will prepare the query and later execute the prepared statement.                                                  |
| ConsistentWith(MutationState)         | Allows to be consistent with previously written mutations (AtPlus / "read your own writes").                                      |
| MaxServerParallelism(int)             | Tunes the maximum parallelism on the server.                                                                                      |
| Metrics(bool)                         | Enables the server to send metrics back to the client as part of the response.                                                    |
| PipelineBatch(int)                    | Sets the batch size for the query pipeline.                                                                                       |
| PipelineCap(int)                      | Sets the cap for the query pipeline.                                                                                              |
| Profile(QueryProfile)                 | Allows to enable additional query profiling as part of the response (Off/Phases/Times)                                            |
| ScanWait(TimeSpan)                    | Allows to specify a maximum scan wait time.                                                                                       |
| ScanCap(int)                          | Specifies a maximum cap on the query scan size.                                                                                   |
| ScanConsistency(QueryScanConsistency) | Sets a different scan consistency for this query (NotBounded/RequestPlus). See "Scan Consistency" section below for more details. |
| Serializer                            | Allows setting a different serializer (ITypeSerializer) for the deserialization of the rows.                                      |
| StreamResults(bool)                   | If using .NET < 5.0, set this to true to stream large (>2Gb) results                                                              |

### [](#scan-consistency)Scan Consistency

Setting a staleness parameter for queries, with `scan_consistency`, enables a tradeoff between latency and (eventual) consistency.

* A SQL++ query using the default **Not Bounded** Scan Consistency will not wait for any indexes to finish updating before running the query and returning results, meaning that results are returned quickly, but the query will not return any documents that are yet to be indexed.

ScanConsistency (NotBounded)

```csharp
var result = await cluster.QueryAsync<dynamic>(
    "SELECT t.* FROM `travel-sample` t WHERE t.type=$1",
    options => options.Parameter("user")
        .ScanConsistency(QueryScanConsistency.NotBounded)
);
```

* With Scan Consistency set to **RequestPlus**, all document changes and index updates are processed before the query is run. Select this when consistency is always more important than performance.

ScanConsistency (RequestPlus)

```csharp
var result = await cluster.QueryAsync<dynamic>(
    "SELECT t.* FROM `travel-sample` t WHERE t.type=$1",
    options => options.Parameter("user")
        .ScanConsistency(QueryScanConsistency.RequestPlus)
);
```

* For a middle ground, **AtPlus** is a "read your own write" (RYOW) option, which means it just waits for the new documents that you specify to be indexed, rather than an entire index of multiple documents.

ScanConsistency (AtPlus/RYOW example)

```csharp
        // create / update document (mutation)
        var upsertResult = await collection.UpsertAsync("doc1", new { name = "Mike AtPlus", type = "user" });

        // create mutation state from mutation results
        var state = MutationState.From(upsertResult);

        // use mutation state with query option
        var result = await cluster.QueryAsync<dynamic>(
            "SELECT t.* FROM `travel-sample` t WHERE t.type=$1",
            options => options.ConsistentWith(state)
                .Parameter("user")
        );
```

### [](#client-context-id)Client Context Id

The SDK will always send a client context ID with each query, even if none is provided by the user. By default a UUID/GUID will be generated that is mirrored back from the query engine and can be used for debugging purposes. A custom string can always be provided if you want to introduce application-specific semantics into it. For example, in a network dump it will show up with a certain identifier). Whatever is chosen, make sure it is unique enough that different queries can be distinguished during debugging or monitoring.

```csharp
var result = await cluster.QueryAsync<dynamic>("SELECT 1=1", 
    options => options.ClientContextId($"azure-resource-group-1-{Guid.NewGuid()}"));
```

### [](#readonly)Readonly

If the query is marked as readonly, both the server and the SDK can improve processing of the operation. On the client side, the SDK can be more liberal with retries because it can be sure that there are no state-mutating side-effects happening. The query engine will ensure that no data is actually mutated when parsing and planning the query.

```csharp
var result = await cluster.QueryAsync<dynamic>("SELECT 1=1", 
    options => options.Readonly(true));
```

### [](#custom-json-serializer)Custom JSON Serializer

Like with all JSON apis, it is possible to customize the JSON serializer. Setting `Serializer` in query options allows to plug in your own library. This in turn makes it possible to serialize rows into POCOs or other structures that your application defines and the SDK has no idea about.

Please see the [documentation on transcoding and serialization](transcoders-nonjson.md) for more information

## [](#streaming-large-result-sets)Streaming Large Result Sets

By default the .NET SDK streams the result set from the server, where the client starts a persistent connection with the server and only read the header until the Rows are enumerated; then, each row or JSON object is de-serialized one at a time.

This decreases pressure on CLR Garbage Collection and helps to prevent an `OutOfMemoryException` being thrown.

> [!NOTE]
> In .NET < 5.0, you will need to set `QueryOptions.StreamResults(true)`, which allows for streaming of results > 2Gb. If you do this, you must also be sure to call `Dispose()` on the QueryResult object to prevent leaking HTTP connections. In later versions of .NET, this is not necessary and the option isn't necessary.

## [](#querying-at-scope-level)Querying at Scope Level

From version 3.0.5 of the .NET SDK, it is possible to query off the [Scope level](../../../server/current/learn/data/scopes-and-collections.md) _with the Couchbase Server release 7.0_ onwards, using the `QueryOptions() {QueryContext = "namespace:bucket:scope:collection"}` method.

The following code snippet shows how to run a query to fetch 10 random rows from `travel-sample.inventory` and print the results.

```csharp
        var myscope = bucket.Scope("inventory");

        var queryResult = await myscope.QueryAsync<dynamic>("select * from airline LIMIT 10", new Couchbase.Query.QueryOptions());
        await foreach (var row in queryResult)
        {
            Console.WriteLine(row);
        }
```

A complete list of `QueryOptions` can be found in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Query.QueryOptions.html).

## [](#additional-resources)Additional Resources

> [!NOTE]
> SQL++ is not the only query option in Couchbase. Be sure to check that [your use case fits your selection of query service](../concept-docs/data-services.md).

* For a deeper dive into SQL++ from the SDK, refer to our [SQL++ SDK concept doc](../concept-docs/n1ql-query.md).
* The [Server doc SQL++ intro](../../../server/current/n1ql/n1ql-language-reference/index.md) introduces a complete guide to the SQL++ language, including all of the latest additions.
* The [SQL++ interactive tutorial](http://query.pub.couchbase.com/tutorial/#1) is a good introduction to the basics of SQL++ use.
* For scaling up queries, be sure to [read up on Indexes](../../../server/current/indexes/index-replication.md).
* The Query Service is for operational queries; for analytical workloads, read more on [when to choose Analytics](../concept-docs/data-services.md#long-running-queries-big-data).