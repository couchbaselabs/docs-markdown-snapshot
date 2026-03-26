---
title: Analytics
description: Parallel data management for complex queries over many records,
  using a familiar SQL++ syntax.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.8/modules/howtos/pages/analytics-using-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.8@dotnet-sdk:howtos:analytics-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.8/howtos/analytics-using-sdk.html)

# Analytics

> Parallel data management for complex queries over many records, using a familiar SQL++ syntax. 

This page covers using our operational .NET SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase's analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](../../../home/columnar-sdk.md) for more information.

For complex and long-running queries, involving large ad hoc join, set, aggregation, and grouping operations, Couchbase Data Platform offers the [Couchbase Analytics Service (CBAS)](../../../server/current/analytics/introduction.md). This is the analytic counterpart to our [operational data focussed Query Service](n1ql-queries-with-sdk.md).

The analytics service is available in [Capella operational](../../../cloud/clusters/analytics-service/analytics-service.md)or the Enterprise Edition of self-managed Couchbase Server.

## [](#getting-started)Getting Started

After familiarizing yourself with our [introductory primer](../../../server/current/analytics/primer-beer.md), in particular creating a dataset and linking it to a bucket to shadow the operational data, try Couchbase Analytics using the .NET SDK. Intentionally, the API for analytics is very similar to that of the query service. In .NET SDK 2.6 and 2.7, Analytics was only available on the `Bucket` object; in .NET SDK 3.x, Analytics queries are submitted using the Cluster reference, not a Bucket or Collection:

```csharp
var result = await cluster.AnalyticsQueryAsync<dynamic>("SELECT \"hello\" as greeting;");

foreach (var row in result.Rows)
{
    Console.WriteLine(row.greeting);
}
```

## [](#queries)Queries

A query can either be `simple` or be `parameterized`. If parameters are used, they can either be `positional` or `named`. Here is one example of each:

```csharp
var result = await cluster.AnalyticsQueryAsync<dynamic>("select airportname, country from airports where country = 'France';");
```

The query may be performed with positional parameters:

```csharp
var result = await cluster.AnalyticsQueryAsync<dynamic>("select airportname, country from airports where country = ?;")
    .AddPositionalParameter("France");
```

Alternatively, the query may be performed with named parameters:

```csharp
var result = await cluster.AnalyticsQueryAsync<dynamic>("select airportname, country from airports where country = $country;")
    .AddNamedParameter("country", "France");
```

> [!NOTE]
> As timeouts are propagated to the server by the client, a timeout set on the client side may be used to stop the processing of a request, in order to save system resources. See example in the next section.

## [](#fluent-api)Fluent API

Additional parameters may be sent as part of the query, using the fluent API. There are currently three parameters:

* **Client Context ID**, sets a context ID that is returned back as part of the result. Uses the `ClientContextId(String)` builder; default is a random UUID
* **Server Side Timeout**, customizes the timeout sent to the server. Does not usually have to be set, as the client sets it based on the timeout on the operation. Uses the `Timeout(TimeSpan)` builder, and defaults to the Analytics timeout set on the client (75s). This can be adjusted at the [cluster global config level](../ref/client-settings.md#timeout-options).
* **Priority**, set if the request should have priority over others. The `Priority(boolean)` builder defaults to `false`.

Here, we give the request priority over others, and set a custom, server-side timeout value:

```csharp
var result = await cluster.AnalyticsQueryAsync<dynamic>("select airportname, country from airports where country = 'France';",
    options =>
    {
        options.WithPriority(true);
        options.WithTimeout(TimeSpan.FromSeconds(100));
    }
);
```

## [](#handling-the-response)Handling the Response

After checking that `QueryStatus` is success, we iterate over the rows. These rows may contain various sorts of data and metadata, depending upon the nature of the query, as you will have seen when working through our [introductory primer](../../../server/current/analytics/primer-beer.md).

```csharp
try
{
    var result = await cluster.AnalyticsQueryAsync<dynamic>("SELECT \"hello\" as greeting;");

    if (result.Rows.Any()) // check there are results
    {
        foreach (var row in result.Rows)
        {
            Console.WriteLine($"Greeting: {row.greeting}");
        }
    }
}
catch (AnalyticsException exception)
{
    foreach (var error in exception.Errors)
    {
        Console.WriteLine($”Error: {error.Message}”);
    }
}
```

Check the xref:\[Errors\] list for possible values to be returned in the `List<Error>`, should `QueryStatus` return as `Errors`.

Common errors are listed in our [Errors Reference doc](../ref/error-codes.md#analytics-errors), with exceptions caused by resource unavailability (such as timeouts and _Operation cannot be performed during rebalance_ messages) leading to an [automatic retry](error-handling.md#retry) by the SDK.

### [](#metadata)MetaData

The `Metrics` object contains useful metadata, such as `ElapsedTime`, and `ResultCount`. Here is a snippet using several items of metadata

```csharp
var result = await cluster.AnalyticsQueryAsync<dynamic>("SELECT \"hello\" as greeting;");

Console.WriteLine($”Elapsed time: {result.MetaData.Metrics.ElapsedTime}”);
Console.WriteLine($”Execution time: {result.MetaData.Metrics.ExecutionTime}”);
Console.WriteLine($”Result count: {result.MetaData.Metrics.ResultCount}”);
Console.WriteLine($”Error count: {result.MetaData.Metrics.ErrorCount}”);
```

For a listing of available `Metrics` in `MetaData`, see the [Understanding Analytics](../concept-docs/analytics-for-sdk-users.md) SDK doc.

## [](#advanced-analytics-topics)Advanced Analytics Topics

From Couchbase Data Platform 6.5, _Deferred Queries_ and _KV Ingestion_ are added to CBAS.

### [](#kv-ingest)KV ingest

You can ingest the results of an Analytics query directly back into a given collection. This then allows the results themselves to be queried in turn.

> [!NOTE]
> From .NET SDK 3.1, KV Ingest has an Interface Level of [Uncommited](../project-docs/compatibility.md#interface-stability).

```csharp
await cluster.IngestAsync<dynamic>(
    statement,
    collection,
    options =>
    {
        options.WithTimeout(TimeSpan.FromSeconds(75));
        options.WithExpiration(TimeSpan.FromDays(1));
    }
);
```

## [](#scoped-queries-on-named-collections)Scoped Queries on Named Collections

In addition to creating a dataset with a WHERE clause to filter the results to documents with certain characteristics, from SDK 3.1 you can now create a dataset against a named collection, for example:

```n1ql
ALTER COLLECTION `travel-sample`.inventory.airport ENABLE ANALYTICS;

-- NB: this is more or less equivalent to:
CREATE DATAVERSE `travel-sample`.inventory;
CREATE DATASET `travel-sample`.inventory.airport ON `travel-sample`.inventory.airport;
```

We can then query the Dataset as normal, using the fully qualified keyspace:

```csharp
var result = await cluster.AnalyticsQueryAsync<dynamic>(
    "SELECT airportname, country FROM `travel-sample`.inventory.airport WHERE country='France' LIMIT 3");

await foreach (var row in result)
{
    Console.WriteLine("Result: " + row);
}
```