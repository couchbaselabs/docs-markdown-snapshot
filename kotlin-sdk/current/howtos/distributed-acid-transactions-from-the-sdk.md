---
title: Distributed Transactions from the Kotlin SDK
description: Distributed ACID Transactions with JVM SDKs.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/3.12/modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc
  xref: xref:kotlin-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.html)

# Distributed Transactions from the Kotlin SDK

> Distributed ACID Transactions with JVM SDKs. Kotlin transactions are available as a developer preview, or use Java ACID transactions within the Kotlin SDK 

With Kotlin SDK 1.4.4, multi-document ACID transactions is available as a developer preview — the Kotlin transactions API is still "volatile", meaning it could change without notice as we refine it.

## [](#kotlin-transactionsdeveloper-preview)Kotlin Transactions — Developer Preview

If you are interested in trying out the developer preview of Kotlin multi-document ACID transactions, introduced with SDK 1.4.4, the following resources will help you to get started:

* Kotlin [API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client-1.4.4/kotlin-client/com.couchbase.client.kotlin.transactions/index.html).
* Intro guide in [Couchbase Forum post](https://www.couchbase.com/forums/t/kotlin-sdk-1-4-4-adds-experimental-support-for-couchbase-transactions/39307).

> [!WARNING]
> The Kotlin transactions API is still "volatile", meaning it could change without notice as we refine it based on your feedback.

## [](#java-transactions-from-the-kotlin-sdk)Java Transactions from the Kotlin SDK

To implement the Java SDK implementation of distributed ACID transactions into your Kotlin client code, you will need to include the Couchbase Java SDK in your project.

Create a `com.couchbase.client.java.Cluster` in your Kotlin app with the [normal Java calls](../../../java-sdk/current/howtos/managing-connections.md) `(Cluster.connect(…​))`, and then do transactions on it as normal, e.g.:

```java
javaCluster.transactions().run(ctx => { /* your transaction logic here */ })
```

So in your app you have both a `com.couchbase.client.java.Cluster` and a `com.couchbase.client.kotlin.Cluster`, which are independent connections.

## [](#additional-information)Additional Information

For more information on Java transactions, read our guide in the Java documentation:

* [Distributed ACID Transactions from the Java SDK](../../../java-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)

  * [Single Query Transactions](../../../java-sdk/current/howtos/transactions-single-query.md)
  * [Tracing](../../../java-sdk/current/howtos/transactions-tracing.md)
* [Transaction Concepts](../../../java-sdk/current/concept-docs/transactions.md)

  * [Cleanup](../../../java-sdk/current/concept-docs/transactions-cleanup.md)
  * [Error Handling](../../../java-sdk/current/concept-docs/transactions-error-handling.md)