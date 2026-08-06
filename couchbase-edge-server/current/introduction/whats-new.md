---
title: New In 1.1
description: Couchbase Edge Server -- What's new in the latest release
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.1/modules/introduction/pages/whats-new.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-edge-server:introduction:whats-new.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/current/introduction/whats-new.html)

# New In 1.1

## [](#release-1-1-june-2026)Release 1.1 June 2026

### [](#new-features)New Features

#### [](#fine-grained-access-control)Fine-Grained Access Control

Couchbase Edge Server now supports fine-grained access control for downstream edge clients. You can define read and write permissions per user at the database, scope, and collection level, enabling multiple applications to share a single Couchbase Edge Server instance without exposing data across application boundaries.

Access control is opt-in and is enabled at the server level using the `enable_user_access_control` configuration property. Named query access can also be restricted based on a user's collection-level permissions.

For more information, see:

* [Access Control](../access-control/access-control-concept.md)
* [Configure Access Control](../access-control/configure-access-control.md)
* [Configure Named Query Access Control](../access-control/configure-query-access.md)

#### [](#token-rotation-without-restart)Token Rotation Without Restart

Couchbase Edge Server now supports JWT-based replication credential rotation without requiring a server restart. Instead of embedding the JWT token inline in the replication configuration, you specify a file path to the token. Couchbase Edge Server loads the token when a replication starts, and can optionally monitor the file for changes and reconnect with the updated token automatically.

For more information, see [Rotate Replication Credentials Without Restart](../administer/token-rotation.md).

#### [](#cors-support)CORS Support

Couchbase Edge Server now supports configurable Cross-Origin Resource Sharing (CORS) policies. This enables browser-based clients and JavaScript SDKs, including the Couchbase Lite JavaScript SDK, to replicate directly with Couchbase Edge Server. CORS is disabled by default and must be explicitly enabled in the database configuration.

For more information, see [Configure CORS](../rest-based-access/cors.md).

#### [](#windows-support)Windows Support

Couchbase Edge Server is now supported on Windows Server 2022, Windows Server 2025, Windows 10, and Windows 11 (x86\_64). Windows 10 and Windows 11 are supported for development and testing only.

For more information, see [Supported Platforms](../product-notes/supported-platforms.md).

#### [](#linux-arm64-support)Linux ARM64 Support

Couchbase Edge Server is now supported on Linux ARM64 (aarch64), including Ubuntu 22.04+. This enables deployment on ARM-based edge devices, single-board computers, and industrial gateways.

For more information, see [Supported Platforms](../product-notes/supported-platforms.md).

### [](#couchbase-edge-server-release-notes)Couchbase Edge Server Release Notes

[Read the full 1.1 release notes here](../product-notes/release-notes.md).

## [](#release-1-0-march-2025)Release 1.0 (March 2025)

### [](#new-features-2)New Features

#### [](#couchbase-edge-server)Couchbase Edge Server

Couchbase Edge Server is a lightweight REST and sync server for Couchbase Mobile databases based on Couchbase Lite Core (LiteCore).

With Couchbase Edge Server, you can perform scalable, offline-first data sync at the edge in resource constrained environments.

Couchbase Edge Server possesses the following features:

* Compact and lightweight: \~10 MB codebase, typically uses < 50 MB RAM.
* Flexible data handling: Serves existing Couchbase Lite database files, or can create its own CRUD-based document access.
* Real-time updates: Push notifications for data changes on the changes feed to save bandwidth caused by polling and reduce latency.
* Advanced querying: Supports SQL++ queries.
* Local synchronization: Acts as a database sync server for local Couchbase Lite clients.
* Upstream integration: Functions as a database sync client for upstream Sync Gateway, Capella App Services, or other instances of Edge Server.

For more information, see:

* [Introducing Couchbase Edge Server](intro.md)
* [Getting Started](../get-started/get-started-landing.md)
* [Edge Server Configuration](../configuration/edge-server-configuration.md)
* [Edge Server REST API](../rest-based-access/rest-api-landing.md)
* [Get Started with the Edge Server REST API](../rest-based-access/rest-api-start.md)
* [Sync](../sync/sync-landing.md)

### [](#couchbase-edge-server-release-notes-2)Couchbase Edge Server Release Notes

[Read the full 1.1 release notes here](../../1.0/product-notes/release-notes.md).