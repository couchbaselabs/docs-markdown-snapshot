---
title: New In 1.0
description: Couchbase Lite for JavaScript -- What's new in the latest release
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/whats-new.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:couchbase-lite-javascript::whats-new.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite-javascript/current/whats-new.html)

# New In 1.0

## [](#release-1-0-1-june-2026)Release 1.0.1 (June 2026)

Couchbase Lite JavaScript Release 1.0.1 introduces fixes and enhancements.

For a full breakdown of the individual issues resolved, see the [Release Notes](releasenotes.md).

## [](#release-1-0-november-2025)Release 1.0 (November 2025)

### [](#new-features)New Features

#### [](#couchbase-lite-for-javascript)Couchbase Lite for JavaScript

Couchbase Lite for JavaScript delivers a fully featured and supported, offline-first local database for the browser, combining secure storage, powerful querying, and seamless sync.

Build modern web applications that work reliably without connectivity, with data automatically synchronized when online.

The SDK integrates smoothly with React, Vue, Angular, and contemporary tooling, supports PWAs, and leverages IndexedDB for persistent local storage.

Developers can query local data using SQL++ with built-in powerful indexing to speed up queries—and react to changes with document, collection, and query listeners.

Security features include Web Crypto-based encryption and TLS data sync connection.

Conflict resolution is also available, with automatic handling or custom logic.

Attachments (blobs) are fully supported, replication runs over WebSockets, and the API can be used in conjunction with TypeScript definitions for schema-safe, strongly typed development.

#### [](#why-use-couchbase-lite-javascript)Why Use Couchbase Lite JavaScript?

* **Offline-first**: Build web applications that work seamlessly without internet connectivity, automatically syncing data when back online.
* **Official Couchbase Mobile support**: The officially supported database for browser applications, providing a reliable alternative to unsupported solutions like PouchDB with Sync Gateway.
* **Modern framework integration**: First-class support for React, Vue, and Angular, with seamless integration into modern web development workflows.
* **Enterprise-grade security**: Field-level and full database encryption using Web Crypto API, with secure TLS connection for data sync.
* **Progressive Web App ready**: Full support for PWAs with offline caching strategies.
* **Powerful querying**: Query documents using SQL++ (N1QL) with support for live queries, joins, aggregations, and indexing.

#### [](#key-capabilities)Key Capabilities

* **Local JSON document database**: Store and query JSON documents locally in the browser using IndexedDB.
* **SQL++ queries**: Execute complex queries with SELECT, WHERE, JOIN, GROUP BY, and aggregation functions.
* **Live queries**: Get real-time updates when query results change, perfect for reactive UIs.
* **Bi-directional sync**: Sync data with Sync Gateway using WebSocket-based replication with automatic conflict resolution.
* **Change listeners**: React to document, collection, and replication changes with event listeners.
* **Blob support**: Store and sync binary attachments like images and files.
* **TypeScript support**: Full TypeScript type definitions with compile-time type safety for document schemas.
* **Encryption**: Built-in encryption support for sensitive data.
* **Indexing**: Create indexes on document properties for faster queries.

For more information, see:

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Databases](database.md)
* [SQL++ Queries](query-n1ql-mobile.md)
* [Remote Sync Gateway](replication.md)

### [](#couchbase-lite-for-javascript-release-notes)Couchbase Lite for JavaScript Release Notes

[Read the full 1.0 release notes here](releasenotes.md).