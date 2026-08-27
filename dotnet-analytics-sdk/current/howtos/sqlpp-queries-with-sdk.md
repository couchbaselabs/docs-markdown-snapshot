---
title: Querying with SQL++
description: You can query for documents in Couchbase using the SQL++ query
  language -- a language based on SQL, but designed for structured and flexible
  JSON documents.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-analytics-sdk-dotnet/edit/release/1.1/modules/howtos/pages/sqlpp-queries-with-sdk.adoc
  xref: xref:dotnet-analytics-sdk:howtos:sqlpp-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-analytics-sdk/current/howtos/sqlpp-queries-with-sdk.html)

# Querying with SQL++

> You can query for documents in Couchbase using the SQL++ query language — a language based on SQL, but designed for structured and flexible JSON documents. 

On this page we dive straight into using the Query Service API from the .NET Analytics SDK. For a deeper look at the concepts, to help you better understand the Query Service, and the SQL++ language, see the links in the [Further Information](#further-information) section at the end of this page.

## [](#before-you-start)Before You Start

This page assumes that you have [installed the .NET Analytics SDK](../hello-world/start-using-sdk.md), added your IP address to the allowlist, and [created an Enterprise Analytics cluster](#analytics:manage:manage-nodes/create-cluster.adoc#cluster).

Create a collection to work upon by [importing the travel-sample dataset](#analytics:intro:connecting-to-data-sources.adoc#import-the-travel-sample-collections) into your cluster.

## [](#querying-your-dataset)Querying Your Dataset

> [!TIP]
> API Enhancements & Async
> 
> The 1.1 .NET Analytics SDK adds support for JWT and client certificate authentication, as well as a new poll-based Server Asynchronous Request API that uses request handles to fetch results, introduced in self-managed Enterprise Analytics Server 2.2, and eliminating the need for long-running server connections.
> 
> The examples in this section are for the standard API, working with all 2.x releases of Enterprise Analytics (with Server Asynchronous Request API examples following in the [Server Async section](#server-asynchronous-api)). Note, you will still be able to use this API with 2.2+ releases of Enterprise Analytics, in addition to the new API.

Execute a query and buffer all result rows in client memory:

Scope Level

```csharp
IQueryResult result = await scope.ExecuteQueryAsync("select 1").ConfigureAwait(false);
await foreach (var row in result.ConfigureAwait(false))
{
    Console.WriteLine("Got row: " + row.ContentAs<JsonElement>());
}
```

Cluster Level

```csharp
IQueryResult result = await cluster.ExecuteQueryAsync("select 1").ConfigureAwait(false);
await foreach (var row in result.ConfigureAwait(false))
{
    Console.WriteLine("Got row: " + row.ContentAs<JsonElement>());
}
```

### [](#positional-and-named-parameters)Positional and Named Parameters

Supplying parameters as individual arguments to the query allows the query engine to optimize the parsing and planning of the query. You can either supply these parameters by name or by position.

Execute a streaming query with positional arguments:

Positional Parameters

```csharp
var result = await cluster.ExecuteQueryAsync("select ?=1", options => options.WithPositionalParameter(1)).ConfigureAwait(false);
await foreach (var row in result.ConfigureAwait(false))
{
    Console.WriteLine("Got row: " + row.ContentAs<JsonElement>());
}
```

Execute a streaming query with named arguments:

Named Parameters

```csharp
var result = await cluster.ExecuteQueryAsync("select $foo=1", options => options.WithNamedParameter("foo", 1)).ConfigureAwait(false);
await foreach (var row in result.ConfigureAwait(false))
{
    Console.WriteLine("Got row: " + row.ContentAs<JsonElement>());
}
```

> [!WARNING]
> Helper methods `WithNamedParameter` and `WithPositionalParameter` take 1 parameter, and add it to the existing collection in the options. The methods `WithNamedParameters` and `WithPositionalParameters` (note the plural) take a collection of parameters, and replace all the parameters in the existing collection.

## [](#server-asynchronous-api)Server Asynchronous Request API

Enterprise Analytics Server 2.2 adds a Server Asynchronous Request API. The SDK will send a request, poll for results, and then fetch once the result is available. The SDK supports each stage of this information flow:

`cluster.StartQueryAsync()` → `QueryHandle` → `QueryStatus` → `QueryResultsHandle`

Server Asynchronous API Example

```csharp

// ──────────────────────────────────────────────
//  Start an async query
// ──────────────────────────────────────────────

var statement = """SELECT VALUE SLEEP("x", 100) FROM RANGE(1, 100) AS id;""";

var handle = await cluster.StartQueryAsync(statement, opts => opts
    .WithQueryTimeout(TimeSpan.FromSeconds(60)));

Console.WriteLine($"Query submitted. Handle: {handle}");

// ──────────────────────────────────────────────
//  Poll until results are ready
// ──────────────────────────────────────────────

var resultHandle = await WaitForQueryResultsAsync(handle, pollDelay: TimeSpan.FromSeconds(2.5), timeout: TimeSpan.FromSeconds(120));

Console.WriteLine($"Results ready. {resultHandle}");

// ──────────────────────────────────────────────
//  Fetch and display results
// ──────────────────────────────────────────────

// IQueryResult implements IAsyncDisposable. The 'await using' declaration
// ensures the underlying HTTP response stream is released after consumption.
// Forgetting this will leak connections.
await using var results = await resultHandle.FetchResultsAsync();

await foreach (var row in results.Rows)
{
    Console.WriteLine($"Found row: {row.ContentAs<JsonElement>()}");
}

Console.WriteLine($"Metadata: RequestId={results.MetaData.RequestId}, " +
                  $"ResultCount={results.MetaData.Metrics?.ResultCount}, " +
                  $"ElapsedTime={results.MetaData.Metrics?.ElapsedTime}");

// ──────────────────────────────────────────────
//  Discard results on the server
// ──────────────────────────────────────────────

await resultHandle.DiscardResultsAsync();
Console.WriteLine("Results discarded.");

// ──────────────────────────────────────────────
//  Helper: poll query status until ready
// ──────────────────────────────────────────────

/// <summary>
/// Polls the query handle at regular intervals until the server reports
/// that results are ready, or the timeout is reached.
/// </summary>
/// <param name="handle">The query handle returned by StartQueryAsync.</param>
/// <param name="pollDelay">Time between status polls.</param>
/// <param name="timeout">Maximum time to wait before throwing a TimeoutException.</param>
/// <returns>A <see cref="QueryResultHandle"/> that can be used to fetch results.</returns>
/// <exception cref="TimeoutException">Thrown when results are not ready within the timeout.</exception>
static async Task<QueryResultHandle> WaitForQueryResultsAsync(
    QueryHandle handle,
    TimeSpan pollDelay,
    TimeSpan timeout)
{
    var stopwatch = Stopwatch.StartNew();

    while (true)
    {
        try
        {
            var status = await handle.FetchStatusAsync();
            if (status.ResultsReady)
            {
                return status.ResultHandle();
            }

            Console.WriteLine($"Query status: {status}");
        }
        catch (Exception ex)
        {
            // Depending on the use case, you might want to break here or continue retrying.
            Console.WriteLine($"Error fetching query status: {ex.Message}");
        }

        if (stopwatch.Elapsed + pollDelay > timeout)
        {
            throw new TimeoutException($"Query results not ready within {timeout.TotalSeconds} seconds.");
        }

        Console.WriteLine($"Query results not ready yet, sleeping for {pollDelay.TotalSeconds}s...");
        await Task.Delay(pollDelay);
    }
}
```

## [](#query-options)Query Options

The query service provides an array of options to customize your query. The following table lists them all:

__Table 1\. Available Query Options__
| Name                                                      | Description                                                                                                                                                                                                       |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bool AsStreaming { get; init; }                           | If true, the IQueryResult will be returned as a streaming result.                                                                                                                                                 |
| string ClientContextId { get; init; }                     | The ClientContextId to be used for the query request. Used to identify the query in logs and profiles. If none is provided, a new GUID will be generated.                                                         |
| IDeserializer? Deserializer { get; init; }                | Used to deserialize query rows. Default to StjJsonDeserializer                                                                                                                                                    |
| Dictionary<string, object> NamedParameters { get; init; } | Named parameters for the query request. Use WithNamedParameters(Dictionary<string, object>) or WithNamedParameter(string, object) to create updated copies.                                                       |
| List<object> PositionalParameters { get; init; }          | Positional parameters for the query request. Use WithPositionalParameters(IEnumerable<object>) or WithPositionalParameter(object) to create updated copies.                                                       |
| Dictionary<string, object> Raw { get; init; }             | Raw parameters passed directly to the analytics service for advanced options. Use WithRawParameters(Dictionary<string, object>) or WithRaw(string, object) to create updated copies.                              |
| bool? ReadOnly { get; init; }                             | Specifies that this query should be executed in read-only mode, disabling the ability for the query to make any changes to the data.                                                                              |
| QueryScanConsistency? ScanConsistency { get; init; }      | The scan consistency for the query request.                                                                                                                                                                       |
| TimeSpan? Timeout { get; init; }                          | Sets the overall timeout for the query request. If unset, the default TimeoutOptions's QueryTimeout will be used. Note that if a CancellationToken is used on the query call, it may trigger before this timeout. |

## [](#further-information)Further Information

The [SQL++ for Analytics Reference](../../../analytics/sqlpp/1%5Fintro.md)offers a complete guide to the SQL++ language for both of our analytics services, including all of the latest additions.