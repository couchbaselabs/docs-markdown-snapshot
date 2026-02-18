---
title: Couchbase Quarkus Java Extension
description: The Couchbase Quarkus extension integrates the Couchbase Java SDK
  within the Quarkus ecosystem.
editUrl: https://github.com/couchbase/docs-quarkus-extension/edit/release/1.2/modules/ROOT/pages/overview.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/quarkus-extension/current/overview.html)

# Couchbase Quarkus Java Extension

The Couchbase Quarkus extension integrates the Couchbase Java SDK within the Quarkus ecosystem. Most notably this extension provides GraalVM native-image support to the existing Java SDK, in addition to other Quarkus integration such as Health Checks, ArC dependency injection, Micrometer metrics, DevServices and more.

## [](#key-features)Key Features

* **Dependency Injection**: Easily inject a Couchbase `Cluster` into your application using Quarkus' CDI.
* **Simplified Configuration**: Manage Couchbase connection and cluster settings through `application.properties`.
* **Native-Image Support**: Compatible with GraalVM/Mandrel for building native images.
* **Couchbase Operations**: Support for KV, Query, Transactions, Analytics, Search, and Management operations.
* **Micrometer Metrics**: Integrates with `quarkus-micrometer`.
* **Health Checks**: Provides a readiness check via `quarkus-smallrye-health`.
* **Dev Services**: Simplifies local development with automatic startup of a Couchbase TestContainer.

## [](#current-limitations)Current Limitations

* **OpenTelemetry Tracing**: The `tracing-opentelemetry` package for the Couchbase Java SDK is not currently supported.
* **Exhaustive Cluster configuration**: Cluster configurations via `application.properties` are limited to those listed below.