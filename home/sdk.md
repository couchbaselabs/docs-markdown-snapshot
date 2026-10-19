---
title: SDKs for Couchbase Operational Database
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Documentation
    version: master
antora:
  editUrl: https://github.com/couchbase/docs-site/edit/master/home/modules/ROOT/pages/sdk.adoc
  xref: xref:home::sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/home/sdk.html)

# SDKs for Couchbase Operational Database

# SDKs for Couchbase Operational Database

A fast and scalable database is even better when it's easy to develop for. Couchbase gives you the SDK APIs to work with Capella, our managed solution, or self-managed options in your private Cloud or datacenter.

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

collection.reactive.upsert("document-key", json)
    .doOnError(err  => println(s"Error during upsert: ${err}"))
    .doOnNext(_     => println("Success"))
    .subscribe()
```

Couchbase is a large platform — covering many services — and Couchbase SDKs are not thin wrappers generated around a REST API, but well thought out interfaces to the platform that make it easier to design and maintain your client code, and work with Couchbase in more natural ways for your platform.

Explore our SDK documentation for your chosen platform:

* C++
* .NET
* Go
* Java
* Kotlin
* Node.js
* PHP
* Python
* Ruby
* Rust
* Scala

[C++ SDK Docs](../cxx-sdk/current/hello-world/overview.md) | [Quickstart Guide](../cxx-sdk/current/hello-world/start-using-sdk.md) | [SDK Release Notes](../cxx-sdk/current/project-docs/sdk-release-notes.md) | [C++ API Reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client)

  
## Using Your Database 

How-to guides to help you start your development journey with Couchbase and the C++ SDK.

Easy to Connect & Get Started

* [Quickstart Guide](../cxx-sdk/current/hello-world/start-using-sdk.md) — CRUD against a Document Database.
* [Connect your App](../cxx-sdk/current/howtos/managing-connections.md) — connect from dev or production environment.
* [Sample Application](../cxx-sdk/current/hello-world/sample-application.md) — build a full app

Search, Query, Analyze

* [Query with a familiar, SQL-like language](../cxx-sdk/current/howtos/sqlpp-queries-with-sdk.md)
* [Vector Search for your AI app](../cxx-sdk/current/howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../cxx-sdk/current/howtos/full-text-searching-with-sdk.md)
* [OLAP — long running analytical queries](../cxx-sdk/current/howtos/analytics-using-sdk.md)

Lightning Fast Data Service

* [Data Operations](../cxx-sdk/current/howtos/kv-operations.md)
* [Sub-Document Operations](../cxx-sdk/current/howtos/subdocument-operations.md)
* [Field Level Encryption from the SDK](../cxx-sdk/current/howtos/encrypting-using-sdk.md)
* [Multi-Document Distributed ACID Transactions](../cxx-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Handling Errors](../cxx-sdk/current/howtos/error-handling.md)
* [Logging](../cxx-sdk/current/howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../cxx-sdk/current/howtos/slow-operations-logging.md)
* [Health Check](../cxx-sdk/current/howtos/health-check.md)

  
## Resources 

Useful resources to help support your development experience with Couchbase and the C++ SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-cxx-client/)
* [Client Settings](../cxx-sdk/current/ref/client-settings.md)
* [Error Messages](../cxx-sdk/current/ref/error-codes.md)
* [Glossary](../cxx-sdk/current/ref/glossary.md)

Deployment

* [SDK Release Notes](../cxx-sdk/current/project-docs/sdk-release-notes.md)
* [Compatibility](../cxx-sdk/current/project-docs/compatibility.md)
* [Integrations & Ecosystem](../cxx-sdk/current/project-docs/third-party-integrations.md)
* [Full Installation of the C++ SDK](../cxx-sdk/current/project-docs/sdk-full-installation.md)

[.NET SDK Docs](../dotnet-sdk/current/hello-world/overview.md) | [Quickstart Guide](../dotnet-sdk/current/hello-world/start-using-sdk.md) | [SDK Release Notes](../dotnet-sdk/current/project-docs/sdk-release-notes.md) | [.NET API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client/)

  
## Using Your Database 

How-to guides to help you start your development journey with Couchbase and the .NET SDK.

Easy to Connect & Get Started

* [Quickstart Guide](../dotnet-sdk/current/hello-world/start-using-sdk.md) — CRUD against a Document Database.
* [Connect your App](../dotnet-sdk/current/howtos/managing-connections.md) — connect from dev or production environment.
* [Sample Application](../dotnet-sdk/current/hello-world/sample-application.md) — build a full app

Search, Query, Analyze

* [Query with a familiar, SQL-like language](../dotnet-sdk/current/howtos/sqlpp-queries-with-sdk.md)
* [Vector Search for your AI app](../dotnet-sdk/current/howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../dotnet-sdk/current/howtos/full-text-searching-with-sdk.md)
* [OLAP — long running analytical queries](../dotnet-sdk/current/howtos/analytics-using-sdk.md)

Lightning Fast Data Service

* [Data Operations](../dotnet-sdk/current/howtos/kv-operations.md)
* [Sub-Document Operations](../dotnet-sdk/current/howtos/subdocument-operations.md)
* [Encrypting Your Data](../dotnet-sdk/current/howtos/encrypting-using-sdk.md)
* [Multi-Document Distributed ACID Transactions](../dotnet-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Handling Errors](../dotnet-sdk/current/howtos/error-handling.md)
* [Logging](../dotnet-sdk/current/howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../dotnet-sdk/current/howtos/slow-operations-logging.md)
* [Health Check](../dotnet-sdk/current/howtos/health-check.md)

  
## Resources 

Useful resources to help support your development experience with Couchbase and the .NET SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-net-client/)
* [Client Settings](../dotnet-sdk/current/ref/client-settings.md)
* [Error Messages](../dotnet-sdk/current/ref/error-codes.md)
* [Glossary](../dotnet-sdk/current/ref/glossary.md)
* [Travel Sample Data Model](../dotnet-sdk/current/ref/travel-app-data-model.md)

Deployment

* [SDK Release Notes](../dotnet-sdk/current/project-docs/sdk-release-notes.md)
* [Compatibility](../dotnet-sdk/current/project-docs/compatibility.md)
* [Older Versions Archive](https://docs-archive.couchbase.com/home/index.html)
* [Migrating to SDK 3 API](../dotnet-sdk/current/project-docs/migrating-sdk-code-to-3.n.md)
* [3rd Party Integrations](../dotnet-sdk/current/project-docs/third-party-integrations.md)
* [Full Installation](../dotnet-sdk/current/project-docs/sdk-full-installation.md)

[Go SDK Docs](../go-sdk/current/hello-world/overview.md) | [Quickstart Guide](../go-sdk/current/hello-world/start-using-sdk.md) | [SDK Release Notes](../go-sdk/current/project-docs/sdk-release-notes.md) | [Go API Reference](https://pkg.go.dev/github.com/couchbase/gocb/v2)

  
## Using Your Database 

How-to guides to help you start your development journey with Couchbase and the Go SDK.

Easy to Connect & Get Started

* [Quickstart Guide](../go-sdk/current/hello-world/start-using-sdk.md) — CRUD against a Document Database.
* [Connect your App](../go-sdk/current/howtos/managing-connections.md) — connect from dev or production environment.
* [Sample Application](../go-sdk/current/hello-world/sample-application.md) — build a full app

Search, Query, Analyze

* [Query with a familiar, SQL-like language](../go-sdk/current/howtos/sqlpp-queries-with-sdk.md)
* [Vector Search for your AI app](../go-sdk/current/howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../go-sdk/current/howtos/full-text-searching-with-sdk.md)
* [OLAP — long running analytical queries](../go-sdk/current/howtos/analytics-using-sdk.md)

Lightning Fast Data Service

* [Data Operations](../go-sdk/current/howtos/kv-operations.md)
* [Sub-Document Operations](../go-sdk/current/howtos/subdocument-operations.md)
* [Encrypting Your Data](../go-sdk/current/howtos/encrypting-using-sdk.md)
* [Multi-Document Distributed ACID Transactions](../go-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Handling Errors](../go-sdk/current/howtos/error-handling.md)
* [Logging](../go-sdk/current/howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../go-sdk/current/howtos/slow-operations-logging.md)
* [Health Check](../go-sdk/current/howtos/health-check.md)

  
## Resources 

Useful resources to help support your development experience with Couchbase and the Go SDK.

Reference

* [API Reference](https://pkg.go.dev/github.com/couchbase/gocb/v2)
* [Client Settings](../go-sdk/current/ref/client-settings.md)
* [Error Messages](../go-sdk/current/ref/error-codes.md)
* [Glossary](../go-sdk/current/ref/glossary.md)
* [Travel Sample Data Model](../go-sdk/current/ref/travel-app-data-model.md)

Deployment

* [SDK Release Notes](../go-sdk/current/project-docs/sdk-release-notes.md)
* [Compatibility](../go-sdk/current/project-docs/compatibility.md)
* [Older Versions Archive](https://docs-archive.couchbase.com/home/index.html)
* [Migrating to SDK 3 API](../go-sdk/current/project-docs/migrating-sdk-code-to-3.n.md)
* [Integrations & Ecosystem](../go-sdk/current/project-docs/third-party-integrations.md)
* [Couchbase Go SDK Installation](../go-sdk/current/project-docs/sdk-full-installation.md)

[Java SDK Docs](../java-sdk/current/hello-world/overview.md) | [Quickstart Guide](../java-sdk/current/hello-world/start-using-sdk.md) | [SDK Release Notes](../java-sdk/current/project-docs/sdk-release-notes.md) | [Java API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client)

  
## Using Your Database 

How-to guides to help you start your development journey with Couchbase and the Java SDK.

Easy to Connect & Get Started

* [Quickstart Guide](../java-sdk/current/hello-world/start-using-sdk.md) — CRUD against a Document Database.
* [Connect your App](../java-sdk/current/howtos/managing-connections.md) — connect from dev or production environment.
* [Sample Application](../java-sdk/current/hello-world/sample-application.md) — build a full app
* [Beginners' Couchbase Tutorial](../java-sdk/current/hello-world/student-record-developer-tutorial.md) — introduction to the SDK, Document data model, and SQL++ for document databases.

Search, Query, Analyze

* [Query with a familiar, SQL-like language](../java-sdk/current/howtos/sqlpp-queries-with-sdk.md)
* [Vector Search for your AI app](../java-sdk/current/howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../java-sdk/current/howtos/full-text-searching-with-sdk.md)
* [OLAP — long running analytical queries](../java-sdk/current/howtos/analytics-using-sdk.md)

Lightning Fast Data Service

* [Data Operations](../java-sdk/current/howtos/kv-operations.md)
* [Sub-Document Operations](../java-sdk/current/howtos/subdocument-operations.md)
* [Encrypting Your Data](../java-sdk/current/howtos/encrypting-using-sdk.md)
* [Multi-Document Distributed ACID Transactions](../java-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Handling Errors](../java-sdk/current/howtos/error-handling.md)
* [Logging](../java-sdk/current/howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../java-sdk/current/howtos/slow-operations-logging.md)
* [Health Check](../java-sdk/current/howtos/health-check.md)

  
## Resources 

Useful resources to help support your development experience with Couchbase and the Java SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/index.html)
* [Client Settings](../java-sdk/current/ref/client-settings.md)
* [Error Messages](../java-sdk/current/ref/error-codes.md)
* [Glossary](../java-sdk/current/ref/glossary.md)

Deployment

* [SDK Release Notes](../java-sdk/current/project-docs/sdk-release-notes.md)
* [Compatibility](../java-sdk/current/project-docs/compatibility.md)
* [3rd Party Integrations](../java-sdk/current/project-docs/third-party-integrations.md)
* [Full Installation](../java-sdk/current/project-docs/sdk-full-installation.md)

[Kotlin SDK Docs](../kotlin-sdk/current/hello-world/overview.md) | [Quickstart Guide](../kotlin-sdk/current/hello-world/start-using-sdk.md) | [SDK Release Notes](../kotlin-sdk/current/project-docs/sdk-release-notes.md) | [Kotlin API Reference](https://docs.couchbase.com/sdk-api/couchbase-kotlin-client/index.html)

  
[Node.js SDK Docs](../nodejs-sdk/current/hello-world/overview.md) | [Quickstart Guide](../nodejs-sdk/current/hello-world/start-using-sdk.md) | [SDK Release Notes](../nodejs-sdk/current/project-docs/sdk-release-notes.md) | [Node.js API Reference](https://docs.couchbase.com/sdk-api/couchbase-node-client/modules.html)

  
[PHP SDK Docs](../php-sdk/current/hello-world/overview.md) | [Quickstart Guide](../php-sdk/current/hello-world/start-using-sdk.md) | [SDK Release Notes](../php-sdk/current/project-docs/sdk-release-notes.md) | [PHP API Reference](https://github.com/couchbase/couchbase-php-client)

  
## Using Your Database 

How-to guides to help you start your development journey with Couchbase and the PHP SDK.

Easy to Connect & Get Started

* [Quickstart Guide](../php-sdk/current/hello-world/start-using-sdk.md) — CRUD against a Document Database.
* [Connect your App](../php-sdk/current/howtos/managing-connections.md) — connect from dev or production environment.
* [Sample Application](../php-sdk/current/hello-world/sample-application.md) — build a full app

Search, Query, Analyze

* [Query with a familiar, SQL-like language](#php-sdk:howtos:sqlpp-queries-with-sdk.adoc)
* [Vector Search for your AI app](../php-sdk/current/howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../php-sdk/current/howtos/full-text-searching-with-sdk.md)
* [OLAP — long running analytical queries](../php-sdk/current/howtos/analytics-using-sdk.md)

Lightning Fast Data Service

* [Data Operations](../php-sdk/current/howtos/kv-operations.md)
* [Sub-Document Operations](../php-sdk/current/howtos/subdocument-operations.md)
* [Field Level Encryption from the SDK](../php-sdk/current/howtos/encrypting-using-sdk.md)
* [Multi-Document Distributed ACID Transactions](../php-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Handling Errors](../php-sdk/current/howtos/error-handling.md)
* [Logging](../php-sdk/current/howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../php-sdk/current/howtos/slow-operations-logging.md)
* [Diagnosing and preventing Network Problems with Health Check](../php-sdk/current/howtos/health-check.md)

  
## Resources 

Useful resources to help support your development experience with Couchbase and the PHP SDK.

Reference

* [API Reference](https://github.com/couchbase/couchbase-php-client)
* [Client Settings](../php-sdk/current/ref/client-settings.md)
* [Error Messages](../php-sdk/current/ref/error-codes.md)
* [Glossary](../php-sdk/current/ref/glossary.md)
* [Travel Sample Data Model](../php-sdk/current/ref/travel-app-data-model.md)

Deployment

* [SDK Release Notes](../php-sdk/current/project-docs/sdk-release-notes.md)
* [Compatibility](../php-sdk/current/project-docs/compatibility.md)
* [Older Versions Archive](https://docs-archive.couchbase.com/home/index.html)
* [Migrating to SDK 3 API](../php-sdk/current/project-docs/migrating-sdk-code-to-3.n.md)
* [3rd Party Integrations](../php-sdk/current/project-docs/third-party-integrations.md)
* [Full Installation](../php-sdk/current/project-docs/sdk-full-installation.md)

[Python SDK Docs](../python-sdk/current/hello-world/overview.md) | [Quickstart Guide](../python-sdk/current/hello-world/start-using-sdk.md) | [SDK Release Notes](../python-sdk/current/project-docs/sdk-release-notes.md) | [Python API Reference](https://docs.couchbase.com/sdk-api/couchbase-python-client/)

  
## Using Your Database 

How-to guides to help you start your development journey with Couchbase and the Python SDK.

Easy to Connect & Get Started

* [Quickstart Guide](../python-sdk/current/hello-world/start-using-sdk.md) — CRUD against a Document Database.
* [Connect your App](../python-sdk/current/howtos/managing-connections.md) — connect from dev or production environment.
* [Sample Application](../python-sdk/current/hello-world/sample-application.md) — build a full app

Search, Query, Analyze

* [Query with a familiar, SQL-like language](../python-sdk/current/howtos/sqlpp-queries-with-sdk.md)
* [Vector Search for your AI app](../python-sdk/current/howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../python-sdk/current/howtos/full-text-searching-with-sdk.md)
* [OLAP — long running analytical queries](../python-sdk/current/howtos/analytics-using-sdk.md)

Lightning Fast Data Service

* [Data Operations](../python-sdk/current/howtos/kv-operations.md)
* [Sub-Document Operations](../python-sdk/current/howtos/subdocument-operations.md)
* [Encrypting Your Data](../python-sdk/current/howtos/encrypting-using-sdk.md)
* [Multi-Document Distributed ACID Transactions](../python-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Error Handling](../python-sdk/current/howtos/error-handling.md)
* [Logging](../python-sdk/current/howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../python-sdk/current/howtos/slow-operations-logging.md)
* [Health Check](../python-sdk/current/howtos/health-check.md)

  
## Resources 

Useful resources to help support your development experience with Couchbase and the Python SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-python-client/)
* [Client Settings](../python-sdk/current/ref/client-settings.md)
* [Error Messages](../python-sdk/current/ref/error-codes.md)
* [Glossary](../python-sdk/current/ref/glossary.md)
* [Travel Sample Data Model](../python-sdk/current/ref/travel-app-data-model.md)

Deployment

* [SDK Release Notes](../python-sdk/current/project-docs/sdk-release-notes.md)
* [Compatibility](../python-sdk/current/project-docs/compatibility.md)
* [Older Versions Archive](https://docs-archive.couchbase.com/home/index.html)
* [Migrating to SDK 3 API](../python-sdk/current/project-docs/migrating-sdk-code-to-3.n.md)
* [Integrations & Ecosystem](../python-sdk/current/project-docs/third-party-integrations.md)
* [Full Installation](../python-sdk/current/project-docs/sdk-full-installation.md)

[Ruby SDK Docs](../ruby-sdk/current/hello-world/overview.md) | [Quickstart Guide](../ruby-sdk/current/hello-world/start-using-sdk.md) | [SDK Release Notes](../ruby-sdk/current/project-docs/sdk-release-notes.md) | [Ruby API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase.html)

  
## Using Your Database 

How-to guides to help you start your development journey with Couchbase and the Ruby SDK.

Easy to Connect & Get Started

* [Quickstart Guide](../ruby-sdk/current/hello-world/start-using-sdk.md) — CRUD against a Document Database.
* [Connect your App](../ruby-sdk/current/howtos/managing-connections.md) — connect from dev or production environment.
* [Sample Application](../ruby-sdk/current/hello-world/sample-application.md) — build a full app

Search, Query, Analyze

* [Query with a familiar, SQL-like language](#ruby-sdk:howtos:sqlpp-queries-with-sdk.adoc)
* [Vector Search for your AI app](../ruby-sdk/current/howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../ruby-sdk/current/howtos/full-text-searching-with-sdk.md)
* [OLAP — long running analytical queries](../ruby-sdk/current/howtos/analytics-using-sdk.md)

Lightning Fast Data Service

* [Data Operations](../ruby-sdk/current/howtos/kv-operations.md)
* [Sub-Document Operations](../ruby-sdk/current/howtos/subdocument-operations.md)
* [Encrypting Your Data](../ruby-sdk/current/howtos/encrypting-using-sdk.md)
* [Multi-Document Distributed ACID Transactions](../ruby-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Handling Errors](../ruby-sdk/current/howtos/error-handling.md)
* [Logging](../ruby-sdk/current/howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../ruby-sdk/current/howtos/slow-operations-logging.md)
* [Diagnosing and preventing Network Problems with Health Check](../ruby-sdk/current/howtos/health-check.md)

  
## Resources 

Useful resources to help support your development experience with Couchbase and the Ruby SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase.html)
* [Client Settings](../ruby-sdk/current/ref/client-settings.md)
* [Error Messages](../ruby-sdk/current/ref/error-codes.md)
* [Glossary](../ruby-sdk/current/ref/glossary.md)
* [Travel Sample Data Model](../ruby-sdk/current/ref/travel-app-data-model.md)

Deployment

* [SDK Release Notes](../ruby-sdk/current/project-docs/sdk-release-notes.md)
* [Compatibility](../ruby-sdk/current/project-docs/compatibility.md)
* [Older Versions Archive](https://docs-archive.couchbase.com/home/index.html)
* [Migrating from SDK2 to SDK3 API](../ruby-sdk/current/project-docs/migrating-sdk-code-to-3.n.md)
* [3rd Party Integrations](../ruby-sdk/current/project-docs/third-party-integrations.md)
* [ruby-sdk:project-docs:sdk-full-installation.adoc](#ruby-sdk:project-docs:sdk-full-installation.adoc)

[Rust SDK Docs](../rust-sdk/current/hello-world/overview.md) | [Quickstart Guide](../rust-sdk/current/hello-world/start-using-sdk.md) | [SDK Release Notes](../rust-sdk/current/project-docs/sdk-release-notes.md) | [Rust API Reference](https://docs.rs/couchbase/latest/couchbase/)

  
## Using Your Database 

How-to guides to help you start your development journey with Couchbase and the Rust SDK.

Easy to Connect & Get Started

* [Quickstart Guide](../rust-sdk/current/hello-world/start-using-sdk.md) — CRUD against a Document Database.
* [Connect your App](../rust-sdk/current/howtos/managing-connections.md) — connect from dev or production environment.
* [Sample Application](#rust-sdk:hello-world:sample-application.adoc) — build a full app

Search, Query, Analyze

* [Query with a familiar, SQL-like language](../rust-sdk/current/howtos/sqlpp-queries-with-sdk.md)
* [Vector Search for your AI app](../rust-sdk/current/howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../rust-sdk/current/howtos/full-text-searching-with-sdk.md)
* [OLAP — long running analytical queries](#rust-sdk:howtos:analytics-using-sdk.adoc)

Lightning Fast Data Service

* [Data Operations](../rust-sdk/current/howtos/kv-operations.md)
* [Sub-Document Operations](../rust-sdk/current/howtos/subdocument-operations.md)
* [rust-sdk:howtos:encrypting-using-sdk.adoc](#rust-sdk:howtos:encrypting-using-sdk.adoc)
* [Multi-Document Distributed ACID Transactions](../rust-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Handling Errors](../rust-sdk/current/howtos/error-handling.md)
* [Logging](../rust-sdk/current/howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../rust-sdk/current/howtos/slow-operations-logging.md)
* [Health Check](../rust-sdk/current/howtos/health-check.md)

  
## Resources 

Useful resources to help support your development experience with Couchbase and the Rust SDK.

Reference

* [API Reference](https://docs.rs/couchbase/latest/couchbase/)
* [Client Settings](../rust-sdk/current/ref/client-settings.md)
* [Error Messages](../rust-sdk/current/ref/error-codes.md)
* [Glossary](../rust-sdk/current/ref/glossary.md)

Deployment

* [SDK Release Notes](../rust-sdk/current/project-docs/sdk-release-notes.md)
* [Compatibility](../rust-sdk/current/project-docs/compatibility.md)
* [Integrations & Ecosystem](../rust-sdk/current/project-docs/third-party-integrations.md)
* [Couchbase Rust SDK Installation](../rust-sdk/current/project-docs/sdk-full-installation.md)

[Scala SDK Docs](../scala-sdk/current/hello-world/overview.md) | [Quickstart Guide](../scala-sdk/current/hello-world/start-using-sdk.md) | [SDK Release Notes](../scala-sdk/current/project-docs/sdk-release-notes.md) | [Scala API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/index.html)

  
## Using Your Database 

How-to guides to help you start your development journey with Couchbase and the Scala SDK.

Easy to Connect & Get Started

* [Quickstart Guide](../scala-sdk/current/hello-world/start-using-sdk.md)
* [Sample Application](../scala-sdk/current/hello-world/sample-application.md)
* [Managing Connections](../scala-sdk/current/howtos/managing-connections.md)
* [Beginners' Couchbase Tutorial](../scala-sdk/current/hello-world/student-record-developer-tutorial.md)

Search, Query, Analyze

* [Query with a familiar, SQL-like language](../scala-sdk/current/howtos/sqlpp-queries-with-sdk.md)
* [Vector Search for your AI app](../scala-sdk/current/howtos/vector-searching-with-sdk.md)
* [Fuzzy Search with text and Geo data](../scala-sdk/current/howtos/full-text-searching-with-sdk.md)
* [OLAP — long running analytical queries](../scala-sdk/current/howtos/analytics-using-sdk.md)

Lightning Fast Data Service

* [Data Operations](../scala-sdk/current/howtos/kv-operations.md)
* [Sub-Document Operations](../scala-sdk/current/howtos/subdocument-operations.md)
* [Field Level Encryption from the SDK](../scala-sdk/current/howtos/encrypting-using-sdk.md)
* [Multi-Document Distributed ACID Transactions](../scala-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)

Observability & Error Handling

* [Handling Errors](../scala-sdk/current/howtos/error-handling.md)
* [Logging](../scala-sdk/current/howtos/collecting-information-and-logging.md)
* [Slow Operations Logging](../scala-sdk/current/howtos/slow-operations-logging.md)
* [Health Check](../scala-sdk/current/howtos/health-check.md)

  
## Resources 

Useful resources to help support your development experience with Couchbase and the Scala SDK.

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/index.html)
* [Client Settings](../scala-sdk/current/ref/client-settings.md)
* [Error Messages](../scala-sdk/current/ref/error-codes.md)
* [Glossary](../scala-sdk/current/ref/glossary.md)

Deployment

* [SDK Release Notes](../scala-sdk/current/project-docs/sdk-release-notes.md)
* [Compatibility](../scala-sdk/current/project-docs/compatibility.md)
* [Integrations & Ecosystem](../scala-sdk/current/project-docs/third-party-integrations.md)
* [Couchbase Scala SDK Installation](../scala-sdk/current/project-docs/sdk-full-installation.md)

The links above will take you to the latest version of your chosen SDK. Should you need to look up something for an older release, you'll discover there a dropdown version selector (in the left-hand navigation) for each SDK release — and links to docs for older, unsupported versions in the [docs archive](https://docs-archive.couchbase.com/home/index.html).

Couchbase C SDK - `libcouchbase` (`lcb`) - is also available, and supported, but is no longer actively added to with new Server features.

[C SDK Docs](../c-sdk/current/hello-world/overview.md)| [C Getting Started](../c-sdk/current/hello-world/start-using-sdk.md)| [C API Reference](https://docs.couchbase.com/sdk-api/couchbase-c-client/index.html)

For new projects, choose instead the [C++ SDK](../cxx-sdk/current/hello-world/overview.md) — or possibly [Go](../go-sdk/current/hello-world/overview.md) or [Rust](../rust-sdk/current/hello-world/overview.md) — for a modern, fully-featured SDK, with excellent performance.

  
### Alternatives to SDKs

The Data API gives access to data in Capella Operational clusters — for when to use the Data API, or Capella's other REST APIs, see [Data API vs. Couchbase SDKs](../cloud/data-api-guide/data-api-sdks.md).

  
## The Bigger Picture

SDKs are also available for our real-time analytics service, [Operational Insights](#columnar:intro:intro.adoc) — see the [Operational Insights SDKs pages](operational-insights-sdk.md):

* .NET
* Go
* Java
* Node.js
* Python

[.NET Operational Insights SDK Docs](../dotnet-operational-insights-sdk/current/hello-world/overview.md) | [Quickstart](../dotnet-operational-insights-sdk/current/hello-world/start-using-sdk.md) | | [.NET API Reference](https://docs.couchbase.com/sdk-api/operational-insights-dotnet-client)

[Go Operational Insights SDK Docs](../go-operational-insights-sdk/current/hello-world/overview.md) | [Quickstart](../go-operational-insights-sdk/current/hello-world/start-using-sdk.md) | [Go API Reference](https://pkg.go.dev/github.com/couchbase/gocboperational-insights)

[Java Operational Insights SDK Docs](../java-operational-insights-sdk/current/hello-world/overview.md) | [Quickstart](../java-operational-insights-sdk/current/hello-world/start-using-sdk.md) | [Java API Reference](https://docs.couchbase.com/sdk-api/couchbase-operational-insights-java-client/)

[Node.js Operational Insights SDK Docs](../nodejs-operational-insights-sdk/current/hello-world/overview.md) | [Quickstart](../nodejs-operational-insights-sdk/current/hello-world/start-using-sdk.md) | [Node.js API Reference](https://docs.couchbase.com/sdk-api/operational-insights-nodejs-client)

[Python Operational Insights SDK Docs](../python-operational-insights-sdk/current/hello-world/overview.md) | [Quickstart](../python-operational-insights-sdk/current/hello-world/start-using-sdk.md) | [Python API Reference](https://docs.couchbase.com/sdk-api/operational-insights-python-client)

  
More developer documentation is available for:

* Connectors

  * <https://docs.couchbase.com/elasticsearch-connector/current/getting-started.html>
  * <https://docs.couchbase.com/kafka-connector/current/quickstart.html>
  * <https://docs.couchbase.com/spark-connector/current/getting-started.html>
  * <https://docs.couchbase.com/server/current/connectors/odbc-jdbc-drivers.html>
* Mobile — [Edge development with Couchbase Lite](../couchbase-lite/current/index.md).
* AI Data Plane — [MCP Python SDK](#mcp-server::intro.adoc)

  
## Couchbase Community

###### 

Community Help

In addition to the Couchbase [Support Team](https://www.couchbase.com/support-policy), help can be found from the community in our [forums](https://forums.couchbase.com/), and on our official [Couchbase Discord server](https://discord.com/invite/K7NPMPGrPk?utm%5Fsource=forums&utm%5Fmedium=post&utm%5Fcampaign=discord).

###### 

Integrations

Information on some 3rd-party SDK integrations, such as [Spring Data](../java-sdk/current/project-docs/compatibility.md#spring-compat), can be found in the SDK docs.

###### 

Tutorials

The [developer bootstrap exercises and other tutorials](https://docs.couchbase.com/tutorials/quick-start/quickstart-java3-native-intellij-firstquery-cb65.html) highlight the use of Couchbase SDKs in the stacks you are most likely to use in development, such as Spring Data, Node Ottoman, and Python Flask.