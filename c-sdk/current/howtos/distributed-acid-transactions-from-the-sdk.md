---
title: Using Couchbase Transactions
description: Distributed ACID Transactions are not available for the C SDK.
  Strong durable gurarantees within a single bucket, and some re-architecture,
  may achieve similar ends within the C SDK.
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc
pubDate: 2026-03-12T03:41:48.873Z
link: xref:c-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc[]
---

[View original HTML](/c-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.html)

# Using Couchbase Transactions

Distributed ACID Transactions are not available for the C SDK. Previously a version of C++ Distributed ACID Transactions was built upon the C SDK, although not exposing any C symbols explicitly. This has now been deprecated, and customers are recommended to explore [native C++ SDK ACID transactions](../../../cxx-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md).

Nevertheless, you may find that you can achieve the same result with our [strong durable gurarantees within a single bucket](../concept-docs/durability-replication-failure-considerations.md#durable-writes) and some re-architecture.

Currently, Distributed ACID Transactions are available for:

* The [C++ SDK](../../../cxx-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md).
* The [.NET SDK](../../../dotnet-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md).
* The [Go SDK](../../../go-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md).
* The [Java SDK](../../../java-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md).
* The [Kotlin SDK](../../../kotlin-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md).
* The [Node.js SDK](../../../nodejs-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md).
* The [PHP SDK](../../../php-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md).
* The [Python SDK](../../../python-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md).
* The [Scala SDK](../../../scala-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md).