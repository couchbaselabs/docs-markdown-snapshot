---
title: Using Couchbase Transactions
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.5/modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc
  xref: xref:3.5@ruby-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.5/howtos/distributed-acid-transactions-from-the-sdk.html)

# Using Couchbase Transactions

> {description} 

Distributed ACID Transactions are not currently available for the Ruby SDK. Nevertheless, you may find that you can achieve the same result with our [strong durable gurarantees within a single bucket](../concept-docs/durability-replication-failure-considerations.md#durable-writes) and some re-architecture.

Currently, Distributed ACID Transactions are available for:

* The [C++ API](#1.0@cxx-txns::distributed-acid-transactions-from-the-sdk.adoc).
* The [.NET SDK](#3.3@dotnet-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc).
* The [Go SDK](#2.4@go-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc).
* The [Java SDK](#3.3@java-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc).
* The [node.js SDK](#4.0@nodejs-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc).