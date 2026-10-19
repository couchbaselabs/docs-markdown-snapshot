---
title: .NET Operational Insights SDK Quickstart Guide
description: Install, connect, try. A quick start guide to get you up and
  running with Operational Insights and the .NET Operational Insights SDK.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: .NET Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-dotnet/edit/release/1.0/modules/hello-world/pages/start-using-sdk.adoc
  xref: xref:dotnet-operational-insights-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-operational-insights-sdk/current/hello-world/start-using-sdk.html)

# .NET Operational Insights SDK Quickstart Guide

> Install, connect, try. A quick start guide to get you up and running with Operational Insights and the .NET Operational Insights SDK. 

[Operational Insights](../../../operational-insights-cloud/intro/intro.md) is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Although maintaining some syntactic similarities with [the operational SDKs](../../../home/sdk.md), the .NET Operational Insights SDK is developed from the ground-up for column-based analytical use cases, and supports streaming APIs to handle large datasets.

## [](#before-you-start)Before You Start

Install and configure an [Operational Insights Cluster](../../../operational-insights/current/intro/intro.md).

### [](#minimum-dotnet-version)Minimum .NET Version

The .NET Operational Insights SDK requires .NET 8 or later. We recommend using the most recent long-term support (LTS) version of .NET (at the time of SDK release, .NET 10).

## [](#adding-the-sdk-to-an-existing-project)Adding the SDK to an Existing Project

Add the NuGet package to your `*.csproj` file, or add it using the command line:

```shell
dotnet add package Couchbase.OperationalInsightsClient
```

```xml
<PackageReference Include="Couchbase.OperationalInsightsClient" Version="1.0.0" />
```

## [](#connecting-and-executing-a-query)Connecting and Executing a Query

Support for JWT and client certificate authentication, as well as a new Server Async poll-based API that uses request handles to fetch results, was introduced in the Operational Insights Enterprise Server 2.2\. This API eliminates the need for long-running server connections.

The examples in this first section of the page are for the standard API — async on the client side — working with Operational Insights 2.0 and later (with Server Async examples following in the [Server Async section](#server-asynchronous-api)). You can still use this API with Operational Insights 2.2 and later, in addition to the new API.

### [](#server-synchronous-api)Server Synchronous API

```csharp
using Couchbase.OperationalInsightsClient;
using Couchbase.OperationalInsightsClient.HTTP;
using Couchbase.OperationalInsightsClient.Options;

var credential = Credential.Create("username", "password");

var cluster = Cluster.Create(
    connectionString: "https://insights.my-couchbase.example.com:18095",
    credential: credential)
);

var result = await cluster.ExecuteQueryAsync("SELECT i from ARRAY_RANGE(1, 100) AS i;").ConfigureAwait(false);

await foreach (var row in result.ConfigureAwait(false))
{
    Console.WriteLine(row.ContentAs<JsonElement>());
}
```

### [](#server-asynchronous-api)Server Asynchronous API

Operational Insights 2.2 introduced an asynchronous request API. The SDK sends a request, polls for results, and then fetches once the result is available. The SDK supports each stage of this information flow:

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

### [](#connection-string)Connection String

The `connectionString` in the above example should take the form of "https://<your\_hostname>:" + PORT

The default port is 443, for TLS connections. You do not need to give a port number if you are using port 443 — `hostname = "https://<your_hostname>"` is effectively the same as \`hostname = "https://<your\_hostname>:" + "443"

If you are using a different port — for example, connecting to a cluster without a load balancer, directly to the Analytics port, `18095` — or not using TLS, then see the [Connecting to Operational Insights](../howtos/managing-connections.md) page.

## [](#migration-from-row-based-analytics)Migration from Row-Based Analytics

If you are migrating a project from CBAS — our Analytics service on Capella Operational and Couchbase Server, using our operational SDKs — then information on migration can be found in the [Operational Insights docs](../../../operational-insights/current/migration/overview.md).

In particular, refer to the [SDK section](../../../operational-insights/current/migration/migration-process.md#sdk-migration) of the Operational Insights migration pages.