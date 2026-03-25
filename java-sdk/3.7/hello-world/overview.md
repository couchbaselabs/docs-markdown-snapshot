---
title: Couchbase Java SDK 3.7
editUrl: https://github.com/couchbase/docs-sdk-java/edit/temp/3.7/modules/hello-world/pages/overview.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.7@java-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.7/hello-world/overview.html)

# Couchbase Java SDK 3.7

# Couchbase Java SDK 3.7

```java
Scope scope = bucket.scope("inventory");
Collection collection = scope.collection("airport");
MutationResult result = collection.mutateIn(
        "airport_1254",
        Collections.singletonList(MutateInSpec.upsert("foo", "bar")),
        mutateInOptions().durability(DurabilityLevel.MAJORITY)
);
```

The Couchbase Java SDK allows applications to access a Couchbase cluster. It offers synchronous APIs as well as reactive and asynchronous equivalents to maximize flexibility and performance.

The Couchbase Java SDK integrates into the Java ecosystem through a number of extensions and connectors, including:

* [Spring Data](https://spring.io/projects/spring-data-couchbase)
* [Spring Boot](https://blog.couchbase.com/couchbase-spring-boot-spring-data/)
* [Couchbase Quarkus Java Extension](../../../quarkus-extension/current/overview.md)
* [Apache Spark Connector](../../../spark-connector/current/java-api.md)

  
##  Using Your Database

How-to guides to help you start your development journey with Couchbase and the Java SDK.

Getting Started

* [Start Using the Java SDK](start-using-sdk.md)
* [Data Operations](../howtos/kv-operations.md)
* [Query](../howtos/n1ql-queries-with-sdk.md)
* [Search](../howtos/full-text-searching-with-sdk.md)
* [Sample Application](sample-application.md)
* [Spring Data Sample Application](spring-data-sample-application.md)

Transactions

* [Transactions from the Java SDK](../howtos/distributed-acid-transactions-from-the-sdk.md)
* [Transaction Concepts](../concept-docs/transactions.md)

Working with Data

* [Sub-Document Operations](../howtos/subdocument-operations.md)
* [Analytics](../howtos/analytics-using-sdk.md)
* [Encrypting Your Data](../howtos/encrypting-using-sdk.md)
* [Working with Collections](../howtos/working-with-collections.md)

Managing Couchbase

* [Managing Connections](../howtos/managing-connections.md)
* [Authentication](../howtos/sdk-authentication.md)
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

Useful resources to help support your development experience with Couchbase and the Java SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client/)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [Glossary](../ref/glossary.md)
* [Travel Sample Data Model](../ref/travel-app-data-model.md)

Project Docs

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Older Versions Archive](https://docs-archive.couchbase.com/home/index.html)
* [Migrating to SDK 3 API](../project-docs/migrating-sdk-code-to-3.n.md)
* [3rd Party Integrations](../project-docs/third-party-integrations.md)
* [Couchbase Quarkus Java Extension](../../../quarkus-extension/current/overview.md)
* [Full Installation](../project-docs/sdk-full-installation.md)

This page covers using our operational Java SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase’s analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](../../../home/columnar-sdk.md) for more information.