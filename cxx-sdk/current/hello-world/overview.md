---
title: Couchbase C++ SDK 1.4
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.4/modules/hello-world/pages/overview.adoc
  xref: xref:cxx-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/current/hello-world/overview.html)

# Couchbase C++ SDK 1.4

# Couchbase C++ SDK 1.4

The Couchbase C++ SDK allows C++ applications to access a Couchbase cluster — Capella or self-managed.

[Quickstart Guide](start-using-sdk.md) | [SDK Release Notes](../project-docs/sdk-release-notes.md) | [C++ SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/) | [C++ SDK source code](https://github.com/couchbaselabs/couchbase-cxx-client/)

A fast and scalable database is even better when it's easy to develop for. Couchbase gives you the C++ APIs to work with Capella, our managed solution, or self-managed options in your private Cloud or datacenter.

* Data Ops (CRUD)
* SQL++ Query (OLTP)
* Vector Search

```c++
auto collection = cluster.bucket(bucket_name).scope(scope_name).collection(collection_name);

const std::string document_id{ "minimal_example" };
const tao::json::value basic_doc{
        { "a", 1.0 },
        { "b", 2.0 },
};

auto [err, res] = collection.upsert(document_id, basic_doc, {}).get();
if (err) {
    fmt::println("Unable to perform upsert: {}", err);
} else {
    fmt::println("id: {}, CAS: {}", document_id, res.cas().value());
}
```

```c++
auto scope = cluster.bucket(bucket_name).scope(scope_name);

auto [err, resp] = scope.query("SELECT * FROM airline WHERE id = 10").get();
if (err) {
    fmt::println("Unable to perform query: {}", err);
}

for (const auto& row : resp.rows_as<couchbase::codec::tao_json_serializer>()) {
    fmt::println("row: {}", tao::json::to_string(row));
}
```

```c++
couchbase::search_request request(couchbase::vector_search(couchbase::vector_query("vector_field", vector_query)));

auto [err, res] = scope.search("vector-index", request).get();

if (err) {
    fmt::println("Got an error doing vector search: {}", err);
} else {
    for (const auto& row : res.rows()) {
        fmt::println("id: {}, score: {}", row.id(), row.score());
    }
}
```

Couchbase is a large platform — covering many services — and Couchbase SDKs are not thin wrappers generated around a REST API, but well thought out interfaces to the platform that make it easier to design and maintain your client code, and work with Couchbase in more natural ways for your platform. Install the SDK, and explore in the way that works best for you.

Building (command-line)

```console
$ cd couchbase-cxx-client
$ mkdir build; cd build
$ cmake ..
$ cmake --build .
```

The links below will take you where you want to go — as will the navigation on the left-hand side of this page. But if you don't know exactly where you need to go, try one of the following:

* Our [Quickstart Guide](start-using-sdk.md) introduces the SDK with a quick install, and CRUD examples against the Data Service.
* Couchbase's familiar SQL-family query language and fuzzy search options (including vector search) are introduced on the [Querying Your Data](../concept-docs/querying-your-data.md) page.
* The C++ SDK docs are, necessarily, just a sub-set [C++ SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/) — and a complete reference of all APIs can be found there.
* For a fuller orientation, there is a [guide to the C++ SDK docs](../project-docs/metadoc-about-these-sdk-docs.md)

  
##  Using Your Database

How-to guides to help you start your development journey with Couchbase and the C++ SDK.

Easy to Connect & Get Started

* [Quickstart Guide](start-using-sdk.md)
* [Quickstart in Couchbase with C++](sample-application.md)
* [Managing Connections](../howtos/managing-connections.md)

Search, Query, Analyze

* [Query with a familiar, SQL-like language](../howtos/sqlpp-queries-with-sdk.md)
* [Vector Search for your AI app](../howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../howtos/full-text-searching-with-sdk.md)
* [OLAP — long running analytical queries](../howtos/analytics-using-sdk.md)

Lightning Fast Data Service

* [Data Operations](../howtos/kv-operations.md)
* [Sub-Document Operations](../howtos/subdocument-operations.md)
* [Multi-Document Distributed ACID Transactions](../howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Handling Errors](../howtos/error-handling.md)
* [Logging](../howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../howtos/slow-operations-logging.md)
* [Health Check](../howtos/health-check.md)

  
##  Resources

Useful resources to help support your development experience with Couchbase and the C++ SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [SDK source code](https://github.com/couchbaselabs/couchbase-cxx-client/)

Deployment

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Integrations & Ecosystem](../project-docs/third-party-integrations.md)
* [Full Installation of the C++ SDK](../project-docs/sdk-full-installation.md)
  
  
##  Couchbase Operational Cluster Feature Compatibility

All of the SDKs have API compatibility with most of the features in Couchbase Operational Clusters — whether self-managed, or Capella. The following table covers possible exceptions, and gives the version of the C++ SDK and Couchbase Server with which some features were introduced.

__Table 1\. Couchbase Server and SDK Supported Version Matrix__
|                                                                                              | Server 7.2   | Server 7.6.x     | Server 8.0 |
| -------------------------------------------------------------------------------------------- | ------------ | ---------------- | ---------- |
| KV Range Scan                                                                                | N/A          | From 1.0.0       |            |
| Zone aware replica reads                                                                     | N/A          | From 1.0.0       |            |
| Vector Search with Search Vector Index                                                       | N/A          | From 1.0.0       |            |
| Vector Query using Hyperscale Vector Index                                                   | N/A          | From SDK 1.2.0 ① |            |
| Vector Query using Composite (GSI & vector) index                                            | N/A          | From SDK 1.2.0 ① |            |
| Distributed ACID Transactions                                                                | From 1.0.0   |                  |            |
| DNS SRV refresh for serverless environments (AWS Lambda, Azure Functions, and GCP Functions) | From 1.0.0   |                  |            |
| Circuit Breakers                                                                             | From 1.3.2   |                  |            |
| OTel                                                                                         | From 1.3.0   |                  |            |
| Field Level Encryption                                                                       | From 1.0.0   |                  |            |
| Cloud Native Gateway                                                                         | From 1.4.0 ② |                  |            |

| **1** | As part of the standard SDK SQL++ API, it should be compatible with all earlier versions of the SDK — but it has not been tested. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Interface Stability = Uncommitted (See [API Stability Guide](#compatibility.adoc#interface-stability)).                           |

  
> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase's analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](../../../home/columnar-sdk.md) for more information.