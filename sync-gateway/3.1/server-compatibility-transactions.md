---
title: Transactions&#8201;&#8212;&#8201;Server Compatibility
description: How Sync Gateway works with <em>Couchbase Server Transactions</em>
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/server-compatibility-transactions.adoc
  xref: xref:3.1@sync-gateway::server-compatibility-transactions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/server-compatibility-transactions.html)

# Transactions&#8201;&#8212;&#8201;Server Compatibility

> How Sync Gateway works with _Couchbase Server Transactions_  

_Related topics_: [XDCR](server-compatibility-xdcr.md) | [Eventing](server-compatibility-eventing.md) | Transactions | [Collections](server-compatibility-collections.md)

_Other Topics_: [Compatibility Matrix](compatibility.md)

## [](#introduction)Introduction

Couchbase Server provides the backing data store for Sync Gateway.

> [!TIP]
> See: [Compatibility Matrix](compatibility.md) for version compatibility information.

Both Couchbase Server and Couchbase mobile (Sync Gateway and Couchbase Lite) support local transactions.

Here we provide details on how Couchbase Server's [Couchbase Transactions](../../server/current/learn/data/transactions.md) feature relates to the Couchbase mobile ecosystem.

## [](#local-transactions)Local Transactions

Within the Couchbase mobile ecosystem all transactions are local, either to the Couchbase Server or to the Couchbase Lite database:

* Couchbase Server supports server side transactions — see: [Couchbase Transactions](../../server/current/learn/data/transactions.md).  
Changes made on the server within a transaction block are guaranteed to be imported by the Sync Gateway only after all the changes in a transaction are committed.
* Similarly, Couchbase Lite supports transactions that are local to the Couchbase Lite database — see: [Database.inBatch()](http://docs.couchbase.com/mobile/3.1.12/couchbase-lite-swift/Classes/Database.html#/s:18CouchbaseLiteSwift8DatabaseC7inBatch5usingyyyKXE%5FtKF).  
Only committed transactions will ever reach Sync Gateway.

There is no guarantee that a series of updates made within a transaction block, on either the Couchbase Server or Couchbase Lite client side, will be ACID compliant when they sync to the other end.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](#sync-function-overview.adoc)
* [Import filter](import-processing.md)
* [Access Control](configuration-schema-access-control.md)
* [Add/Update Sync Function](#rest-api-admin.html#/Access%5FControl/update%5Fsync%5Ffunction)
* [Sync Function Overview](#sync-function-overview.adoc)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)