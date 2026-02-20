---
title: Release Notes
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.0/modules/product-notes/pages/release-notes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:couchbase-edge-server:product-notes:release-notes.adoc[]
---

[View original HTML](/couchbase-edge-server/current/product-notes/release-notes.html)

# Release Notes

## [](#maint-latest)1.0.1 — November 2025

Version 1.0.1 of Couchbase Edge Server delivers the following features and enhancements:

### [](#enhancements)Enhancements

None for this release.

### [](#issues-and-resolutions)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

* [CBL-7243 — Fix use-after-free bug in conflict resolver](https://jira.issues.couchbase.com/browse/CBL-7243)
* [CBL-7650 — Add expiry support to Edge Server REST API](https://jira.issues.couchbase.com/browse/CBL-7650)

#### [](#known-issues)Known Issues

None for this release.

### [](#breaking-changes)Breaking Changes

None for this release.

### [](#deprecations)Deprecations

None for this release.

## [](#1-0-0march-2025)1.0.0 — March 2025

Version 1.0.0 of Couchbase Edge Server delivers the following features and enhancements:

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

* [Introducing Couchbase Edge Server](../introduction/intro.md)
* [Getting Started](../get-started/get-started-landing.md)
* [Edge Server Configuration Schema](../configuration/edge-server-configuration.md)
* [Edge Server REST API](../rest-based-access/rest-api-landing.md)
* [Get Started with the Edge Server REST API](../rest-based-access/rest-api-start.md)
* [Sync](../sync/sync-landing.md)

### [](#maint-1-0-0)Fixed Issues

None for this release.

### [](#enhancements-2)Enhancements

None for this release.

### [](#known-issues-2)Known Issues

None for this release.

### [](#deprecations-2)Deprecations

None for this release

## [](#see-also)See Also

* [Product Notes](product-notes-landing.md)
* [Product Compatibility](compatibility.md)
* [Supported Platforms](supported-platforms.md)