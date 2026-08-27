---
title: Couchbase .NET SDK 3.6
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.6/modules/hello-world/pages/overview.adoc
  xref: xref:3.6@dotnet-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.6/hello-world/overview.html)

# Couchbase .NET SDK 3.6

# Couchbase .NET SDK 3.6

```csharp
await collection
    .InsertAsync(key, Encoding.UTF8.GetBytes("hello"), options =>
    {
        options.Expiry(TimeSpan.FromSeconds(30));
        options.Timeout(TimeSpan.FromMinutes(5));
    })
    .ConfigureAwait(false);

using var result = await collection.GetAsync(key, options => options.Transcoder(new LegacyTranscoder()))
    .ConfigureAwait(false);
```

The Couchbase .NET client allows applications to connect to Couchbase Server using any Common Language Runtime (CLR) language, including C#, F#, and VB.NET. The SDK is written in C#, and some of its idiomatic patterns reflect that choice.

  
##  Using Your Database

How-to guides and tutorials to help you start your development journey with Couchbase and the .NET SDK.

Getting Started

* [Start Using the .NET SDK](start-using-sdk.md)
* [Data Operations](../howtos/kv-operations.md)
* [SQL++ Queries from the SDK](../howtos/n1ql-queries-with-sdk.md)
* [Search](../howtos/full-text-searching-with-sdk.md)
* [Sample Application](sample-application.md)

Transactions

* [Distributed ACID Transactions from the .NET SDK](../howtos/distributed-acid-transactions-from-the-sdk.md)
* [Transaction Concepts](../concept-docs/transactions.md)

Working with Data

* [Sub-Document Operations](../howtos/subdocument-operations.md)
* [Analytics](../howtos/analytics-using-sdk.md)
* [Encrypting Your Data](../howtos/encrypting-using-sdk.md)
* [Working with Collections](../howtos/working-with-collections.md)

Managing Couchbase

* [Managing Connections](../howtos/managing-connections.md)
* [Authenticating](../howtos/sdk-authentication.md)
* [Provisioning Cluster Resources](../howtos/provisioning-cluster-resources.md)
* [User Management](../howtos/sdk-user-management-example.md)

Errors & Diagnostics

* [Handling Errors](../howtos/error-handling.md)
* [Logging](../howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../howtos/slow-operations-logging.md)

##  Learn

Take a deep-dive into the SDK concept material and learn more about Couchbase.

Data Concepts

* [Data Model](../concept-docs/data-model.md)
* [Service Selection](../concept-docs/data-services.md)
* [Field Level Encryption](../concept-docs/encryption.md)

Errors & Diagnostics Concepts

* [Errors and Diagnostics](../concept-docs/errors.md)
* [Tracing](../concept-docs/response-time-observability.md)
* [Failure Considerations](../concept-docs/durability-replication-failure-considerations.md)

##  Resources

Useful resources to help support your development experience with Couchbase and the .NET SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client/)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [Glossary](../ref/glossary.md)
* [Travel Sample Data Model](../ref/travel-app-data-model.md)

Project Docs

* [Couchbase .NET SDK Release Notes and Archives](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Older Versions Archive](https://docs-archive.couchbase.com/home/index.html)
* [Migrating to SDK 3 API](../project-docs/migrating-sdk-code-to-3.n.md)
* [Full Installation](../project-docs/sdk-full-installation.md)

This page covers using our operational .NET SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase's analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](../../../home/columnar-sdk.md) for more information.