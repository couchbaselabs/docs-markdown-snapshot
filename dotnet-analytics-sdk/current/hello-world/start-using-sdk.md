---
title: .NET Analytics SDK Quickstart Guide
description: Install, connect, try. A quick start guide to get you up and
  running with Enterprise Analytics and the .NET Analytics SDK.
editUrl: https://github.com/couchbase/docs-analytics-sdk-dotnet/edit/release/1.1/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:dotnet-analytics-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-analytics-sdk/current/hello-world/start-using-sdk.html)

# .NET Analytics SDK Quickstart Guide

> Install, connect, try. A quick start guide to get you up and running with Enterprise Analytics and the .NET Analytics SDK. 

[Enterprise Analytics](../../../analytics/intro/intro.md) is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Although maintaining some syntactic similarities with [the operational SDKs](../../../home/sdk.md), the .NET Analytics SDK is developed from the ground-up for column-based analytical use cases, and supports streaming APIs to handle large datasets.

## [](#before-you-start)Before You Start

Install and configure an [Enterprise Analytics Cluster](../../../enterprise-analytics/current/intro/intro.md).

### [](#minimum-dotnet-version)Minimum .NET Version

The .NET Analytics SDK requires .NET 8 or later. We recommend using the most recent long-term support (LTS) version of .NET.

## [](#adding-the-sdk-to-an-existing-project)Adding the SDK to an Existing Project

Add the NuGet package to your `*.csproj` file, or add it using the command line:

```shell
dotnet add package Couchbase.AnalyticsClient
```

```xml
<PackageReference Include="Couchbase.AnalyticsClient" Version="1.1.0" />
```

## [](#connecting-and-executing-a-query)Connecting and Executing a Query

.NET Analytics SDK 1.1 adds support for JWT and client certificate authentication, as well as a new Server Asynchronous Request API that uses request handles to fetch results. Introduced in the self-managed Enterprise Analytics Server 2.2, this API eliminates the need for long-running server connections.

The examples in this first section of the page are for the standard API — async on the client side — working with Enterprise Analytics 2.0 and later (with Server Asynchronous Request API examples following in the [Server Async section](#server-asynchronous-api)). You can still use this API with Enterprise Analytics 2.2 and later, in addition to the new API.

### [](#server-synchronous-request-api)Server Synchronous Request API

```csharp
using Couchbase.AnalyticsClient;
using Couchbase.AnalyticsClient.HTTP;
using Couchbase.AnalyticsClient.Options;

var credential = Credential.Create("username", "password");

var cluster = Cluster.Create(
    connectionString: "https://analytics.my-couchbase.example.com:18095",
    credential: credential)
);

var result = await cluster.ExecuteQueryAsync("SELECT i from ARRAY_RANGE(1, 100) AS i;").ConfigureAwait(false);

await foreach (var row in result.ConfigureAwait(false))
{
    Console.WriteLine(row.ContentAs<JsonElement>());
}
```

### [](#server-asynchronous-api)Server Asynchronous Request API

Enterprise Analytics 2.2 introduces an asynchronous request API. The SDK sends a request, polls for results, and then fetches once the result is available.

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

If you are using a different port — for example, connecting to a cluster without a load balancer, directly to the Analytics port, `18095` — or not using TLS, then see the [Connecting to Enterprise Analytics](../howtos/managing-connections.md) page.

## [](#migration-from-row-based-analytics)Migration from Row-Based Analytics

If you are migrating a project from CBAS — our Analytics service on Capella Operational and Couchbase Server, using our operational SDKs — then information on migration can be found in the [Enterprise Analytics docs](../../../enterprise-analytics/current/migration/overview.md).

In particular, refer to the [SDK section](../../../enterprise-analytics/current/migration/migration-process.md#sdk-migration) of the Enterprise Analytics migration pages.