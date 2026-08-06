---
title: Using Couchbase Transactions
description: Distributed ACID Transactions are not currently available for the
  Ruby SDK. Strong durable gurarantees within a single bucket, and some
  re-architecture, may achieve similar ends within the Ruby SDK.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.8/modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:ruby-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.html)

# Using Couchbase Transactions

Distributed ACID Transactions are not currently available for the Ruby SDK. Nevertheless, you may find that you can achieve the same result with our [strong durable gurarantees within a single bucket](../concept-docs/durability-replication-failure-considerations.md#durable-writes) and some re-architecture.

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