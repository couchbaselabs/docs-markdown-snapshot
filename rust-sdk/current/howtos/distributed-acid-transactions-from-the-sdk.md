---
title: Using Couchbase Transactions
description: Distributed ACID Transactions are not currently available for the
  Rust SDK. Strong durable gurarantees within a single bucket, and some
  re-architecture, may achieve similar ends within the Rust SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc
  xref: xref:rust-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/rust-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.html)

# Using Couchbase Transactions

Distributed ACID Transactions are not currently available for the Rust SDK. Nevertheless, you may find that you can achieve the same result with our [strong durable gurarantees within a single bucket](../concept-docs/durability-replication-failure-considerations.md#durable-writes) and some re-architecture.

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