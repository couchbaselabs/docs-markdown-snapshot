[View original HTML](/couchbase-lite-javascript/current/index.html)

Couchbase Lite JavaScript is a lightweight offline-first embedded NoSQL JSON document database for browser based frontend apps that provides rich query, indexing and data synchronization capabilities with Capella App Services or Sync Gateway.

With Couchbase Lite JavaScript, you can build resilient web applications that work seamlessly online and offline, with automatic data synchronization to Sync Gateway when connectivity is restored.

Couchbase Lite JavaScript runs entirely in the browser, storing data locally using [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB%5FAPI) and synchronizing with [Sync Gateway](../../sync-gateway/current/introduction.md) via WebSockets for secure, bi-directional replication.

![Couchbase Lite JavaScript Architecture](_images/cbl-js-architecture.png) 

## Why Use Couchbase Lite JavaScript?

* **Offline-first**: Build web applications that work seamlessly without internet connectivity, automatically syncing data when back online.
* **Official Couchbase Mobile support**: The officially supported database for browser applications, providing a reliable alternative to unsupported solutions like PouchDB with Sync Gateway.
* **Modern framework integration**: First-class support for React, Vue, and Angular, with seamless integration into modern web development workflows.
* **Enterprise-grade security**: Field-level and full database encryption using Web Crypto API, with secure authentication via Basic Auth or OIDC/JWT.
* **Progressive Web App ready**: Full support for PWAs with Service Worker integration and offline caching strategies.
* **Powerful querying**: Query documents using SQL++ (N1QL) with support for live queries, joins, aggregations, and indexing.

## Key Capabilities

* **Local JSON document database**: Store and query JSON documents locally in the browser using IndexedDB.
* **SQL++ queries**: Execute complex queries with SELECT, WHERE, JOIN, GROUP BY, and aggregation functions.
* **Live queries**: Get real-time updates when query results change, perfect for reactive UIs.
* **Bi-directional sync**: Sync data with Sync Gateway using WebSocket-based replication with automatic conflict resolution.
* **Change listeners**: React to document, collection, and replication changes with event listeners.
* **Blob support**: Store and sync binary attachments like images and files.
* **TypeScript support**: Full TypeScript type definitions with compile-time type safety for document schemas.
* **Encryption**: Built-in encryption support for sensitive data.
* **Indexing**: Create indexes on document properties for faster queries.

# 

|  | For more information about what’s new in Couchbase Lite JavaScript, see [Release Notes](releasenotes.md). |
|  | --------------------------------------------------------------------------------------------------------- |

## Getting Started

Get started with Couchbase Lite JavaScript, from installation to building and running your first application.

* [Preparing for Couchbase Lite JavaScript](gs-prereqs.md)
* [Installing Couchbase Lite JavaScript](gs-install.md)

## Working with Databases

Learn how to create, configure, and manage databases in your browser applications.

* [Databases](database.md)
* [Scopes and Collections](scopes-collections-manage.md)

## Documents and Data

Work with JSON documents and blobs.

* [Documents](document.md)
* [Blobs](blob.md)

## Queries and Indexing

Query your local data with powerful SQL++ queries and optimize performance with indexing.

* [SQL++ for Mobile](query-n1ql-mobile.md)
* [Query Resultsets](query-resultsets.md)
* [Live Queries](query-live.md)
* [Indexing](indexing.md)

## Data Synchronization

Sync data between your browser application and Sync Gateway with automatic conflict resolution.

* [Remote Sync Gateway](replication.md)
* [CORS Configuration](cors-configuration.md)
* [Data Conflicts](conflict.md)

## Migration

Migrate your existing PouchDB applications to Couchbase Lite JavaScript.

* [Migrating from PouchDB](migrate-from-pouchdb.md)

## Troubleshooting

Diagnose and resolve common issues with logging, storage, and synchronization.

* [Logging](logging.md)

## API Reference

Complete API documentation generated from TypeScript definitions.

* [API References](https://docs.couchbase.com/mobile/1.0.0/couchbase-lite-javascript/index.html)

## Product Notes

View supported browsers, compatibility matrices, and detailed release notes.

* [Release Notes](releasenotes.md)
* [Compatibility](compatibility.md)
* [Supported Browsers](supported-browsers.md)