---
title: Couchbase Java SDK 3.11
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.11/modules/hello-world/pages/overview.adoc
  xref: xref:3.11@java-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.11/hello-world/overview.html)

# Couchbase Java SDK 3.11

# Couchbase Java SDK 3.11

The Couchbase Java SDK allows Java applications to access a Couchbase cluster — Capella or self-managed.

[Quickstart Guide](start-using-sdk.md) | [SDK Release Notes](../project-docs/sdk-release-notes.md) | [Java SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client/) | [Java SDK source code](https://github.com/couchbase/couchbase-jvm-clients/)

A fast and scalable database is even better when it's easy to develop for. Couchbase gives you the Java APIs to work with Capella, our managed solution, or self-managed options in your private Cloud or datacenter.

* Data Ops (CRUD)
* SQL++ Query (OLTP)
* Vector Search

```java
collection.upsert("my-document", JsonObject.create().put("doc", true),
    upsertOptions().durability(DurabilityLevel.MAJORITY));
```

```java
QueryResult result = cluster.query(
    "select count(*) from `travel-sample`.inventory.airline where country = $country",
    queryOptions().parameters(JsonObject.create().put("country", "France")));
```

```java
SearchRequest request = SearchRequest
        .create(VectorSearch.create(VectorQuery.create("vector_field", vectorQuery)));

SearchResult result = scope.search("vector-index", request);
```

Couchbase is a large platform — covering many services — and Couchbase SDKs are not thin wrappers generated around a REST API, but well thought out interfaces to the platform that make it easier to design and maintain your client code, and work with Couchbase in more natural ways for your platform. Install the SDK, and explore in the way that works best for you.

Installing the SDK via Maven

```xml
<dependencies>
    <dependency>
        <groupId>com.couchbase.client</groupId>
        <artifactId>java-client</artifactId>
        <version>3.11.3</version>
    </dependency>
</dependencies>
```

The Couchbase Java SDK integrates into the Java ecosystem through a number of extensions and connectors, including:

* [Spring Data](https://spring.io/projects/spring-data-couchbase)
* [Spring Boot](https://blog.couchbase.com/couchbase-spring-boot-spring-data/)
* [Couchbase Quarkus Java Extension](../../../quarkus-extension/current/overview.md)
* [Apache Spark Connector](../../../spark-connector/current/java-api.md)

## Exploring the Java SDK

The links in the sections below will take you where you want to go — as will the navigation on the left-hand side of this page. But if you don't know exactly where you need to go, try one of the following:

* Our [Quickstart Guide](start-using-sdk.md) introduces the SDK with a quick install, and CRUD examples against the Data Service.
* Couchbase's familiar SQL-family query language and fuzzy search options (including vector search) are introduced on the [Querying Your Data](../concept-docs/querying-your-data.md) page.
* The Java SDK docs are, necessarily, just a sub-set [Java SDK API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client/) — and a complete listing of all APIs can be found in the reference.
* For a fuller orientation, there is a [guide to the Java SDK docs](../project-docs/metadoc-about-these-sdk-docs.md)

  
##  Using Your Database

How-to guides to help you start your development journey with Couchbase and the Java SDK.

Easy to Connect & Get Started

* [Getting Started](start-using-sdk.md)
* [Quickstart in Couchbase with Spring Boot and Java](sample-application.md)
* [Beginners' Couchbase Tutorial](student-record-developer-tutorial.md)
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

Useful resources to help support your development experience with Couchbase and the Java SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client/)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [SDK source code](https://github.com/couchbase/couchbase-jvm-clients/)

Deployment

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [3rd Party Integrations](../project-docs/third-party-integrations.md)
* [Couchbase Quarkus Java Extension](../../../quarkus-extension/current/overview.md)
* [Full Installation](../project-docs/sdk-full-installation.md)

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase's analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](../../../home/columnar-sdk.md) for more information.