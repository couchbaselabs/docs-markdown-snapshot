---
title: Couchbase .NET SDK 3.10
pubDate: 2026-10-16T07:26:40.932Z
meta:
  component:
    title: .NET SDK
    version: "3.10"
antora:
  editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/release/3.10/modules/hello-world/pages/overview.adoc
  xref: xref:dotnet-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/current/hello-world/overview.html)

# Couchbase .NET SDK 3.10

# Couchbase .NET SDK 3.10

The Couchbase .NET SDK allows .NET applications to access a Couchbase cluster — Capella or self-managed.

[Quickstart Guide](start-using-sdk.md) | [SDK Release Notes](../project-docs/sdk-release-notes.md) | [.NET SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client/) | [.NET SDK source code](https://github.com/couchbase/couchbase-net-client/)

A fast and scalable database is even better when it's easy to develop for. Couchbase gives you the .NET APIs to work with Capella, our managed solution, or self-managed options in your private Cloud or datacenter.

* Data Ops (CRUD)
* SQL++ Query (OLTP)
* Vector Search

```csharp
var document = new { foo = "bar", bar = "foo" };
var result = await collection.UpsertAsync("document-key", document,
    options =>
    {
        options.Expiry(TimeSpan.FromMinutes(1));
        options.Durability(PersistTo.One, ReplicateTo.One);
        options.Timeout(TimeSpan.FromSeconds(5));
    }
);
```

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

```csharp
var searchRequest = SearchRequest.Create(
    VectorSearch.Create(new VectorQuery("vector_field").WithVector(preGeneratedVectors))
);

var searchResult = scope.SearchAsync("travel-vector-index", searchRequest, new SearchOptions());
```

Couchbase is a large platform — covering many services — and Couchbase SDKs are not thin wrappers generated around a REST API, but well thought out interfaces to the platform that make it easier to design and maintain your client code, and work with Couchbase in more natural ways for your platform. Install the SDK, and explore in the way that works best for you.

Installation

```console
Install-Package CouchbaseNetClient
```

The links below will take you where you want to go — as will the navigation on the left-hand side of this page. But if you don't know exactly where you need to go, try one of the following:

* Our [Quickstart Guide](start-using-sdk.md) introduces the SDK with a quick install, and CRUD examples against the Data Service.
* Couchbase's familiar SQL-family query language and fuzzy search options (including vector search) are introduced on the [Querying Your Data](../concept-docs/querying-your-data.md) page.
* The .NET SDK docs are, necessarily, just a sub-set [.NET SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client/) — and a complete reference of all APIs can be found there.
* For a fuller orientation, there is a [guide to the .NET SDK docs](../project-docs/metadoc-about-these-sdk-docs.md)

  
##  Using Your Database

How-to guides to help you start your development journey with Couchbase and the .NET SDK.

Easy to Connect & Get Started

* [Quickstart Guide](start-using-sdk.md)
* [Sample Application](sample-application.md)
* [Managing Connections](../howtos/managing-connections.md)

Search, Query, Analyze

* [Query with a familiar, SQL-like language](../howtos/sqlpp-queries-with-sdk.md)
* [Vector Search for your AI app](../howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../howtos/full-text-searching-with-sdk.md)
* [OLAP — long running analytical queries](../howtos/analytics-using-sdk.md)

Lightning Fast Data Service

* [Data Operations](../howtos/kv-operations.md)
* [Sub-Document Operations](../howtos/subdocument-operations.md)
* [Encrypting Your Data](../howtos/encrypting-using-sdk.md)
* [Multi-Document Distributed ACID Transactions](../howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Handling Errors](../howtos/error-handling.md)
* [Logging](../howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../howtos/slow-operations-logging.md)
* [Health Check](../howtos/health-check.md)

  
##  Resources

Useful resources to help support your development experience with Couchbase and the .NET SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client/)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [SDK source code](https://github.com/couchbase/couchbase-net-client/)
* [Glossary](../ref/glossary.md)
* [Travel Sample Data Model](../ref/travel-app-data-model.md)

Deployment

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Older Versions Archive](https://docs-archive.couchbase.com/home/index.html)
* [Migrating to SDK 3 API](../project-docs/migrating-sdk-code-to-3.n.md)
* [3rd Party Integrations](../project-docs/third-party-integrations.md)
* [Full Installation](../project-docs/sdk-full-installation.md)
  
  
##  Couchbase Operational Cluster Feature Compatibility

All of the SDKs have API compatibility with most of the features in Couchbase Operational Clusters — whether self-managed, or Capella. The following table covers possible exceptions, and gives the version of the .NET SDK and Couchbase Server with which some features were introduced.

__Table 1\. Couchbase Server and SDK Supported Version Matrix__
|                                                                                              | Server 7.2 | Server 7.6.x     | Server 8.0 |
| -------------------------------------------------------------------------------------------- | ---------- | ---------------- | ---------- |
| KV Range Scan                                                                                | N/A        | From 3.4.6       |            |
| Zone aware replica reads                                                                     | N/A        | From 3.8.0       |            |
| Vector Search with Search Vector Index                                                       | N/A        | From 3.5.1       |            |
| Vector Query using Hyperscale Vector Index                                                   | N/A        | From SDK 3.8.0 ① |            |
| Vector Query using Composite (GSI & vector) index                                            | N/A        | From SDK 3.8.0 ① |            |
| Distributed ACID Transactions                                                                | From 3.0.0 |                  |            |
| DNS SRV refresh for serverless environments (AWS Lambda, Azure Functions, and GCP Functions) | From 3.3.6 |                  |            |
| Circuit Breakers                                                                             | From 3.0.0 |                  |            |
| Response Time Observability with OTel                                                        | From 3.0.4 |                  |            |
| Field Level Encryption                                                                       | From 3.2.4 |                  |            |
| Cloud Native Gateway                                                                         | From 3.9.0 |                  |            |

| **1** | As part of the standard SDK SQL++ API, it should be compatible with all earlier versions of the SDK — but it has not been tested. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------- |

  
> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase's analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](../../../home/columnar-sdk.md) for more information.