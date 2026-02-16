[View original HTML](/dotnet-analytics-sdk/current/hello-world/start-using-sdk.html)

> Install, connect, try. A quick start guide to get you up and running with Enterprise Analytics and the .NET Analytics SDK. 

[Enterprise Analytics](../../../analytics/intro/intro.md) is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Although maintaining some syntactic similarities with [the operational SDKs](#home::sdk.adoc), the .NET Analytics SDK is developed from the ground-up for column-based analytical use cases, and supports streaming APIs to handle large datasets.

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
<PackageReference Include="Couchbase.AnalyticsClient" Version="1.0.1" />
```

## [](#connecting-and-executing-a-query)Connecting and Executing a Query

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

### [](#connection-string)Connection String

The `connectionString` in the above example should take the form of "https://<your\_hostname>:" + PORT

The default port is 443, for TLS connections. You do not need to give a port number if you are using port 443 — `hostname = "https://<your_hostname>"` is effectively the same as \`hostname = "https://<your\_hostname>:" + "443"

If you are using a different port — for example, connecting to a cluster without a load balancer, directly to the Analytics port, `18095` — or not using TLS, then see the [Connecting to Enterprise Analytics](../howtos/managing-connections.md) page.

## [](#migration-from-row-based-analytics)Migration from Row-Based Analytics

If you are migrating a project from CBAS — our Analytics service on Capella Operational and Couchbase Server, using our operational SDKs — then information on migration can be found in the [Enterprise Analytics docs](../../../enterprise-analytics/current/migration/overview.md).

In particular, refer to the [SDK section](../../../enterprise-analytics/current/migration/migration-process.md#sdk-migration) of the Enterprise Analytics migration pages.