---
title: Couchbase Scala SDK 3.13
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Scala SDK
    version: "3.13"
antora:
  editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.13/modules/hello-world/pages/overview.adoc
  xref: xref:scala-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/current/hello-world/overview.html)

# Couchbase Scala SDK 3.13

# Couchbase Scala SDK 3.13

The Couchbase Scala SDK allows Scala applications to access a Couchbase operational cluster — Capella or self-managed.

[Quickstart Guide](start-using-sdk.md) | [SDK Release Notes](../project-docs/sdk-release-notes.md) | [Scala SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/index.html) | [Scala SDK source code](https://github.com/couchbase/couchbase-jvm-clients/tree/master/scala-client)

> [!NOTE]
> From 3.9.0 on, all Couchbase JVM SDKs have an aligned version number to make it easier to users to track changes. So the version has jumped from 1.8.x to 3.9.x.

A fast and scalable database is even better when it's easy to develop for. Couchbase gives you the Scala APIs to work with Capella, our managed solution, or self-managed options in your private Cloud or datacenter.

* Data Ops (CRUD)
* SQL++ Query (OLTP)
* Vector Search

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

collection.upsert("document-key", json) match {
  case Success(result)    => println("Document upsert successful")
  case Failure(exception) => println("Error: " + exception)
}
```

```scala
val statement = """select * from `travel-sample` limit 10;"""
val result: Try[QueryResult] = cluster.query(statement)
```

```scala
val request = SearchRequest.vectorSearch(VectorSearch(VectorQuery("vector_field", vectorQuery)))

val result: Try[SearchResult] = scope.search("vector-index", request)
```

Couchbase is a large platform — covering many services — and Couchbase SDKs are not thin wrappers generated around a REST API, but well thought out interfaces to the platform that make it easier to design and maintain your client code, and work with Couchbase in more natural ways for your platform. Install the SDK, and explore in the way that works best for you.

Installing the SDK via Scala Build Tool

```sbt
libraryDependencies += "com.couchbase.client" %% "scala-client" % "3.13.0"
```

The Scala SDK is provided with builds for Scala 2.12, 2.13, and 3.3 through 3.7 (inclusive). `%%` takes care of selecting the right version in Scala Build Tool. If you are using another build tool such as Maven or Gradle, then specify `scala-client_2.12`, `scala-client_2.13`, or `scala-client_3`, as appropriate. The Scala 3 build can be used from applications compiled with Scala 3.3 through 3.7 inclusive, and even Scala 2.13\. It is the recommended build for all users, except those on 2.12.

The links below will take you where you want to go — as will the navigation on the left-hand side of this page. But if you don't know exactly where you need to go, try one of the following:

* Our [Quickstart Guide](start-using-sdk.md) introduces the SDK with a quick install, and CRUD examples against the Data Service.
* Couchbase's familiar SQL-family query language and fuzzy search options (including vector search) are introduced on the [Querying Your Data](../concept-docs/querying-your-data.md) page.
* The Scala SDK docs are, necessarily, just a sub-set [Scala SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/index.html) — and a complete reference of all APIs can be found there.
* For a fuller orientation, there is a [guide to the Scala SDK docs](../project-docs/metadoc-about-these-sdk-docs.md)

  
##  Using Your Database

How-to guides to help you start your development journey with Couchbase and the Scala SDK.

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
* [Field Level Encryption from the SDK](../howtos/encrypting-using-sdk.md)
* [Multi-Document Distributed ACID Transactions](../howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Handling Errors](../howtos/error-handling.md)
* [Logging](../howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../howtos/slow-operations-logging.md)
* [Health Check](../howtos/health-check.md)

  
##  Resources

Useful resources to help support your development experience with Couchbase and the Scala SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/index.html)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [SDK source code](https://github.com/couchbase/couchbase-jvm-clients/tree/master/scala-client)

Deployment

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Integrations & Ecosystem](../project-docs/third-party-integrations.md)
* [Couchbase Scala SDK Installation](../project-docs/sdk-full-installation.md)
  
  
##  Couchbase Operational Cluster Feature Compatibility

All of the SDKs have API compatibility with most of the features in Couchbase Operational Clusters — whether self-managed, or Capella. The following table covers possible exceptions, and gives the version of the Scala SDK and Couchbase Server with which some features were introduced.

__Table 1\. Couchbase Server and SDK Supported Version Matrix__
|                                                                                              | Server 7.2 | Server 7.6.x     | Server 8.0 |
| -------------------------------------------------------------------------------------------- | ---------- | ---------------- | ---------- |
| KV Range Scan                                                                                | N/A        | From 1.4.1       |            |
| Zone aware replica reads                                                                     | N/A        | From 1.8.0       |            |
| Vector Search with Search Vector Index                                                       | N/A        | From 1.6.0       |            |
| Vector Query using Hyperscale Vector Index                                                   | N/A        | From SDK 3.9.0 ① |            |
| Vector Query using Composite (GSI & vector) index                                            | N/A        | From SDK 3.9.0 ① |            |
| Distributed ACID Transactions                                                                | From 1.5.0 |                  |            |
| DNS SRV refresh for serverless environments (AWS Lambda, Azure Functions, and GCP Functions) | From 1.4.0 |                  |            |
| Circuit Breakers                                                                             | From 1.0.0 |                  |            |
| Response Time Observability with OTel                                                        | From 1.2.0 |                  |            |
| Field Level Encryption                                                                       | From 1.0.0 |                  |            |
| Cloud Native Gateway                                                                         | From 1.5.0 |                  |            |

| **1** | As part of the standard SDK SQL++ API, it should be compatible with all earlier versions of the SDK — but it has not been tested. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------- |

Note, from 3.9.0 on, all Couchbase JVM SDKs have an aligned version number to make it easier for users to track changes. Thus the Scala SDK jumped from 1.8 to 3.9 as a minor version bump.\*

  
> [!TIP]
> Operational Insights SDKs
> 
> SDKs for [Operational Insights Enterprise](../../../operational-insights/current/intro/intro.md) — Couchbase's analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Operational Insights Enterprise SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Operational Insights Capella](../../../operational-insights-cloud/intro/intro.md) — as this service does not have Operational Insights Enterprise's load balancer, and uses a different connection protocol. Operational Insights Capella SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Operational Insights Capella (Columnar) SDK pages](../../../home/columnar-sdk.md) for more information.