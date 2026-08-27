---
title: New In 1.0
description: Couchbase Edge Server -- What's new in the latest release
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.0/modules/introduction/pages/whats-new.adoc
  xref: xref:1.0@couchbase-edge-server:introduction:whats-new.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/1.0/introduction/whats-new.html)

# New In 1.0

## [](#release-1-0-march-2025)Release 1.0 (March 2025)

### [](#new-features)New Features

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

### [](#couchbase-edge-server-release-notes)Couchbase Edge Server Release Notes

[Read the full 1.0 release notes here](../product-notes/release-notes.md).