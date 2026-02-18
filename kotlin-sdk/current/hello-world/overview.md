---
title: Couchbase Kotlin SDK 3.9
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/release/3.9/modules/hello-world/pages/overview.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/kotlin-sdk/current/hello-world/overview.html)

# Couchbase Kotlin SDK 3.9

# Couchbase Kotlin SDK 3.9

The Couchbase Kotlin SDK allows Kotlin applications to access a Couchbase cluster — Capella or self-managed.

[Quickstart Guide](start-using-sdk.md) | [SDK Release Notes](../project-docs/sdk-release-notes.md) | [Kotlin SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client/index.html) | [Kotlin SDK SDK source code](https://github.com/couchbase/couchbase-jvm-clients)

What’s the point of a fast and scalable database if it’s not easy to develop for? Couchbase gives you the Kotlin APIs to work with Capella, our managed solution, or self-managed options in your private Cloud or datacenter.

The Couchbase Kotlin SDK is built on top of the same high performance I/O core as the Couchbase Java SDK.  
It provides idiomatic Kotlin features like default arguments, suspend functions, and tasteful DSLs.

* Data Ops (CRUD)
* SQL++ Query (OLTP)
* Vector Search

```java
Unresolved include directive in modules/hello-world/pages/overview.adoc - include::devguide:example$java/KvOperations.java[]
```

```java
Unresolved include directive in modules/hello-world/pages/overview.adoc - include::devguide:example$java/Queries.java[]
```

```java
Unresolved include directive in modules/hello-world/pages/overview.adoc - include::devguide:example$java/Search.java[]
```

Couchbase is a large platform — covering many services — and Couchbase SDKs are not thin wrappers generated around a REST API, but well thought out interfaces to the platform that make it easier to design and maintain your client code, and work with Couchbase in more natural ways for your platform. Install the SDK, and explore in the way that works best for you.

Installing the SDK via Maven

```xml
<dependency>
  <groupId>com.couchbase.client</groupId>
  <artifactId>kotlin-client</artifactId>
  <version>3.9.0</version>
</dependency>
```

The Couchbase Kotlin SDK SDK integrates into the Java ecosystem through a number of extensions and connectors, including:

* [Spring Data](https://spring.io/projects/spring-data-couchbase)
* [Spring Boot](https://blog.couchbase.com/couchbase-spring-boot-spring-data/)
* [Apache Spark Connector](../../../spark-connector/current/java-api.md)

## Exploring the Kotlin SDK SDK

The links in the sections below will take you where you want to go — as will the navigation on the left-hand side of this page. But if you don’t know exactly where you need to go, try one of the following:

* Our [Quickstart Guide](start-using-sdk.md) introduces the SDK with a quick install, and CRUD examples against the Data Service.
* Couchbase’s familiar SQL-family query language and fuzzy search options (including vector search) are introduced on the [concept-docs:querying-your-data.adoc](#concept-docs:querying-your-data.adoc) page.
* The Kotlin SDK docs are, necessarily, just a sub-set [Kotlin SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client/index.html) — and a complete listing of all APIs can be found in the reference.
* For a fuller orientation, there is a [guide to the Kotlin SDK docs](#project-docs:metadoc-about-these-sdk-docs.adoc)

  
##  Using Your Database

How-to guides to help you start your development journey with Couchbase and the Kotlin SDK.

Easy to Connect & Get Started

* [Getting Started](start-using-sdk.md)
* [Quickstart in Couchbase with Kotlin and Ktor](sample-application.md)
* [Beginners' Couchbase Tutorial](student-record-developer-tutorial.md)
* [Managing Connections](../howtos/managing-connections.md)

Search, Query, Analyze

* [Query with a familiar, SQL-like language](#howtos:sqlpp-queries-with-sdk.adoc)
* [Vector Search for your AI app](#howtos:vector-searching-with-sdk.adoc)
* [Fuzzy Search with text and Geo data](#howtos:full-text-searching-with-sdk.adoc)
* [OLAP — long running analytical queries](../howtos/analytics-using-sdk.md)

Lightning Fast Data Service

* [Data Operations](../howtos/kv-operations.md)
* [howtos:subdocument-operations.adoc](#howtos:subdocument-operations.adoc)
* [howtos:encrypting-using-sdk.adoc](#howtos:encrypting-using-sdk.adoc)
* [Multi-Document Distributed ACID Transactions](../howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [howtos:error-handling.adoc](#howtos:error-handling.adoc)
* [howtos:collecting-information-and-logging.adoc](#howtos:collecting-information-and-logging.adoc)
* [howtos:slow-operations-logging.adoc](#howtos:slow-operations-logging.adoc)
* [howtos:health-check.adoc](#howtos:health-check.adoc)

  
##  Resources

Useful resources to help support your development experience with Couchbase and the Kotlin SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client/index.html)
* [Client Settings for the Java SDK](../ref/client-settings.md)
* [Error Codes](../ref/error-codes.md)
* [SDK source code](https://github.com/couchbase/couchbase-jvm-clients)

Deployment

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [project-docs:third-party-integrations.adoc](#project-docs:third-party-integrations.adoc)
* [Couchbase Quarkus Java Extension](../../../quarkus-extension/current/overview.md)
* [project-docs:sdk-full-installation.adoc](#project-docs:sdk-full-installation.adoc)

This page covers using our operational Kotlin SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase’s analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](#home::analytics-sdk.adoc) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](#home::columnar-sdk.adoc) for more information.