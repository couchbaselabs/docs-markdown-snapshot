---
title: Couchbase Scala SDK 3.9
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.9/modules/hello-world/pages/overview.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.9@scala-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/3.9/hello-world/overview.html)

# Couchbase Scala SDK 3.9

# Couchbase Scala SDK 3.9

The Couchbase Scala SDK allows Scala applications to access a Couchbase cluster — Capella or self-managed.

[Quickstart Guide](start-using-sdk.md) | [SDK Release Notes](../project-docs/sdk-release-notes.md) | [Scala SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/index.html) | [Scala SDK source code](https://github.com/couchbase/couchbase-jvm-clients/tree/master/scala-client)

> [!NOTE]
> From 3.9.0 on, all Couchbase JVM SDKs have an aligned version number to make it easier to users to track changes. So the version has jumped from 1.8.x to 3.9.x.

What's the point of a fast and scalable database if it's not easy to develop for? Couchbase gives you the Scala APIs to work with Capella, our managed solution, or self-managed options in your private Cloud or datacenter.

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
libraryDependencies += "com.couchbase.client" %% "scala-client" % "3.9.2"
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

This page covers using our operational Scala SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase's analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](../../../home/columnar-sdk.md) for more information.