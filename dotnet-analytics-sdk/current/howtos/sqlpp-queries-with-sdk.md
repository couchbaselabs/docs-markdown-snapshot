---
title: Querying with SQL++
description: You can query for documents in Couchbase using the SQL++ query
  language, a language based on SQL, but designed for structured and flexible
  JSON documents.
editUrl: https://github.com/couchbase/docs-analytics-sdk-dotnet/edit/release/1.0/modules/howtos/pages/sqlpp-queries-with-sdk.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:dotnet-analytics-sdk:howtos:sqlpp-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-analytics-sdk/current/howtos/sqlpp-queries-with-sdk.html)

# Querying with SQL++

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. 

On this page we dive straight into using the Query Service API from the .NET Analytics SDK. For a deeper look at the concepts, to help you better understand the Query Service, and the SQL++ language, see the links in the [Further Information](#further-information) section at the end of this page.

Here we show queries against the Travel Sample collection, at cluster and scope level, and give links to information on adding other collections to your data.

## [](#before-you-start)Before You Start

This page assumes that you have [installed the .NET Analytics SDK](../hello-world/start-using-sdk.md), added your IP address to the allowlist, and [created a Columnar cluster](../../../analytics/admin/prepare-project.md#cluster).

Create a collection to work upon by [importing the travel-sample dataset](../../../analytics/intro/examples.md#travel-sample) into your cluster.

## [](#querying-your-dataset)Querying Your Dataset

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

## [](#query-options)Query Options

The query service provides an array of options to customize your query. The following table lists them all:

__Table 1\. Available Query Options__
| Name                                                      | Description                                                                                                                                                                                                         |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bool AsStreaming { get; init; }                           | If true, the IQueryResult will be returned as a streaming result.                                                                                                                                                   |
| string ClientContextId { get; init; }                     | The ClientContextId to be used for the query request. Used to identify the query in logs and profiles. If none is provided, a new GUID will be generated.                                                           |
| IDeserializer? Deserializer { get; init; }                | Used to deserialize query rows. Default to StjJsonDeserializer                                                                                                                                                      |
| Dictionary<string, object> NamedParameters { get; init; } | Named parameters for the query request. Use WithNamedParameters(Dictionary<string, object>) or WithNamedParameter(string, object) to create updated copies.                                                         |
| List<object> PositionalParameters { get; init; }          | Positional parameters for the query request. Use WithPositionalParameters(IEnumerable<object>) or WithPositionalParameter(object) to create updated copies.                                                         |
| Dictionary<string, object> Raw { get; init; }             | Raw parameters passed directly to the analytics service for advanced options. Use WithRawParameters(Dictionary<string, object>) or WithRaw(string, object) to create updated copies.                                |
| bool? ReadOnly { get; init; }                             | Specifies that this query should be executed in read-only mode, disabling the ability for the query to make any changes to the data.                                                                                |
| QueryScanConsistency? ScanConsistency { get; init; }      | The scan consistency for the query request.                                                                                                                                                                         |
| TimeSpan? Timeout { get; init; }                          | Sets the overall timeout for the query request. If unset, the default TimeoutOptions’s \`QueryTimeout will be used. Note that if a CancellationToken is used on the query call, it may trigger before this timeout. |

## [](#further-information)Further Information

The [SQL++ for Analytics Reference](../../../server/current/analytics/1%5Fintro.md)offers a complete guide to the SQL++ language for both of our analytics services, including all of the latest additions.