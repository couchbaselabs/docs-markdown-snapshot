---
title: Couchbase Go SDK 2.8
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.8/modules/hello-world/pages/overview.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@go-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.8/hello-world/overview.html)

# Couchbase Go SDK 2.8

# Couchbase Go SDK 2.8

```go
// get a default collection reference
collection := bucket.DefaultCollection()

// for a named collection and scope
scope := bucket.Scope("inventory")
collection = scope.Collection("airport")
```

The Couchbase Go SDK 2.x is a complete rewrite of the API, reducing the number of overloads to present a simplified surface area, and adding support for Couchbase Server features like Collections and Scopes (available from Couchbase Server 7.0). The Go 2.x SDK also introduces improved error handling providing extra error information.

  
##  Using Your Database

How-to guides to help you start your development journey with Couchbase and the Go SDK.

Getting Started

* [Start Using the Go SDK](start-using-sdk.md)
* [Data Operations](../howtos/kv-operations.md)
* [Query](../howtos/n1ql-queries-with-sdk.md)
* [Search](../howtos/full-text-searching-with-sdk.md)
* [Sample Application](sample-application.md)

Transactions

* [Using Couchbase Transactions](../howtos/distributed-acid-transactions-from-the-sdk.md)
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

Useful resources to help support your development experience with Couchbase and the Go SDK.

Reference

* [API Reference](https://pkg.go.dev/github.com/couchbase/gocb/v2)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [Glossary](../ref/glossary.md)
* [Travel Sample Data Model](../ref/travel-app-data-model.md)

Project Docs

* [SDK Release Notes](../project-docs/sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Older Versions Archive](https://docs-archive.couchbase.com/home/index.html)
* [Migrating to SDK 3 API](../project-docs/migrating-sdk-code-to-3.n.md)
* [Full Installation](../project-docs/sdk-full-installation.md)