---
title: Transactions&#8201;&#8212;&#8201;Server Compatibility
description: How Sync Gateway works with <em>Couchbase Server Transactions</em>
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/server-compatibility-transactions.adoc
  xref: xref:2.8@sync-gateway::server-compatibility-transactions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/server-compatibility-transactions.html)

# Transactions&#8201;&#8212;&#8201;Server Compatibility

> How Sync Gateway works with _Couchbase Server Transactions_  

_Related compatibility topics_: [XDCR](../current/server-compatibility/server-compatibility-xdcr.md) | [Eventing](../current/server-compatibility/server-compatibility-eventing.md) | Transactions | [Collections](../current/server-compatibility/server-compatibility-collections.md)

_Other related topics_: [Compatibility Matrix](#sync-gateway::compatibility.adoc)

## [](#introduction)Introduction

Couchbase Server provides the backing data store for Sync Gateway.

> [!TIP]
> See: [Compatibility Matrix](#sync-gateway::compatibility.adoc) for version compatibility information.

Both Couchbase Server and Couchbase mobile (Sync Gateway and Couchbase Lite) support local transactions.

Here we provide details on how Couchbase Server's [Couchbase Transactions](../../server/current/learn/data/transactions.md) feature relates to the Couchbase mobile ecosystem.

## [](#local-transactions)Local Transactions

Within the Couchbase mobile ecosystem all transactions are local, either to the Couchbase Server or to the Couchbase Lite database:

* Couchbase Server supports server side transactions — see: [Couchbase Transactions](../../server/current/learn/data/transactions.md).  
Changes made on the server within a transaction block are guaranteed to be imported by the Sync Gateway only after all the changes in a transaction are committed.
* Similarly, Couchbase Lite supports transactions that are local to the Couchbase Lite database — see: [Database.inBatch()](http://docs.couchbase.com/mobile/2.8.0/couchbase-lite-swift/Classes/Database.html#/s:18CouchbaseLiteSwift8DatabaseC7inBatch5usingyyyKXE%5FtKF).  
Only committed transactions will ever reach Sync Gateway.

Typically, mobile replication does not replicate transactions atomically. There is no guarantee that a series of updates made within a transaction block, on either the Couchbase Server or Couchbase Lite client side, will be ACID compliant when they sync to the other end.

## [](#related-content)Related Content

###### [](#)

Learn more …​

* [Sync Function](../current/access-control/sync-function/sync-function.md)
* [Import filter](../current/sync/import-processing.md)
* [Inter-Sync Gateway Replication](../current/sync/sync-inter-syncgateway-overview.md)
* [Sync with Couchbase Server](../current/sync/sync-with-couchbase-server.md)

###### [](#-2)

Reference material …​

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)