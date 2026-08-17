---
title: SDK Extension Libraries
description: Field Level Encryption and Response Time Observability (Tracing)
  libraries ship separately from each SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-extensions/edit/main/modules/ROOT/pages/index.adoc
  xref: xref:sdk-extensions::index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sdk-extensions/index.html)

# SDK Extension Libraries

Field Level Encryption and Response Time Observability (Tracing) libraries ship separately from each SDK. As does Spring Data and others which are not applicable for each SDK. These pages are for common material across a number of SDKs.

If you have landed on this page, you most likely wish to be on a general page for one of the extension libraries. These are outlined in the next section. If you want to be on a particular SDK's extension library page, you will find them listed at the [end of the page](#additional-information).

## [](#distributed-acid-transactions-fle-and-rto)Distributed ACID Transactions, FLE, and RTO

Couchbase provides several SDKs to allow applications to access a Couchbase cluster, as well as Mobile SDKs to carry your application to the edge.

### [](#distributed-acid-transactions)Distributed ACID Transactions

Distributed ACID Transactions are operations that ensure that when multiple documents need to be modified such that only the successful modification of all justifies the modification of any, either all the modifications do occur successfully; or none of them occurs. Earlier release shipped as a separate library, but these are now incorporated within each SDK.

[Distributed ACID Transactions intro](distributed-acid-transactions.md).

### [](#field-level-encryption)Field Level Encryption

Fields within a JSON document can be securely encrypted by the SDK to support FIPS 140-2 compliance. This is a client-side implementation, with encryption and decryption handled by the Couchbase client SDK.

[Field Level Encryption intro](field-level-encryption.md).

### [](#response-time-observability)Response Time Observability

Health indicators can tell you a lot about the performance of an application. Monitoring them is vital both during its development and production lifecycle. For a database, performance is best encapsulated via per-request performance.

[Response Time Observability intro](response-time-observability.md).

## [](#spring-data-couchbase)Spring Data Couchbase

[Spring Data for Couchbase](https://spring.io/projects/spring-data-couchbase) is part of the umbrella Spring Data project which aims to provide a familiar and consistent Spring-based programming model for new datastores while retaining store-specific features and capabilities.

The Spring Data Couchbase project provides integration with the Couchbase Server database and any of our JVM SDKs. Key functional areas of Spring Data Couchbase are a POJO centric model for interacting with Couchbase Buckets or Collections, and easily writing a Repository style data access layer.

[Spring Data Couchbase intro](spring-data-couchbase.md).

## [](#additional-information)Additional Information

* Distributed ACID Transactions in [C++](../cxx-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md), [.NET (C#)](../dotnet-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md), [Go](../go-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md), [Java](../java-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md), [Kotlin](../kotlin-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md), [Node.js](../nodejs-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md), [PHP](../php-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md), [Python](../python-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md), and [Scala](../scala-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md).
* Field Level Encryption pages for [C++](../cxx-sdk/current/howtos/encrypting-using-sdk.md), [.NET](../dotnet-sdk/current/howtos/encrypting-using-sdk.md), [Go](../go-sdk/current/howtos/encrypting-using-sdk.md), [Java](../java-sdk/current/howtos/encrypting-using-sdk.md), [Node.js](../nodejs-sdk/current/howtos/encrypting-using-sdk.md), [Python](../python-sdk/current/howtos/encrypting-using-sdk.md), and [Scala](../scala-sdk/current/howtos/encrypting-using-sdk.md).
* RTO pages for [C++](../cxx-sdk/current/howtos/slow-operations-logging.md), [.NET](../dotnet-sdk/current/howtos/slow-operations-logging.md), [Go](../go-sdk/current/howtos/slow-operations-logging.md), [Java](../java-sdk/current/howtos/observability-tracing.md), [Node.js](../nodejs-sdk/current/howtos/slow-operations-logging.md), [PHP](../php-sdk/current/howtos/slow-operations-logging.md), [Python](../python-sdk/current/howtos/slow-operations-logging.md), [Rust](../rust-sdk/current/howtos/slow-operations-logging.md), and [Scala](../scala-sdk/current/howtos/observability-tracing.md).