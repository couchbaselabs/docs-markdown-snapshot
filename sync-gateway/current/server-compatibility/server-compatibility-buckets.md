---
title: Buckets&#8201;&#8212;&#8201;Server Compatibility
description: How <em>Sync Gateway</em> works with <em>Couchbase Server's</em>
  <em>Buckets</em>
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/server-compatibility/pages/server-compatibility-buckets.adoc
  xref: xref:sync-gateway:server-compatibility:server-compatibility-buckets.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/server-compatibility/server-compatibility-buckets.html)

# Buckets&#8201;&#8212;&#8201;Server Compatibility

> How _Sync Gateway_ works with _Couchbase Server's_ _Buckets_  

_Related topics_: [Buckets](server-compatibility-buckets.md) | [Collections](server-compatibility-collections.md) | [Eventing](server-compatibility-eventing.md) | [Transactions](server-compatibility-transactions.md) | [XDCR](server-compatibility-xdcr.md) | [Backup and restore](server-compatibility-backups.md)

_Other Topics_: [Compatibility Matrix](../product-notes/compatibility.md)

## [](#introduction)Introduction

A bucket in Couchbase Server is the fundamental space for storing data. Each bucket contains a hierachy of Scopes and Collections to logically group keys and values.

For more information, see [Buckets](../../../server/current/learn/buckets-memory-and-storage/buckets.md)

> [!TIP]
> See: [Compatibility Matrix](../product-notes/compatibility.md) for version compatibility information.

You can find details here about compatibility between Couchbase Server buckets and the Couchbase Mobile ecosystem.

## [](#durability)Durability

Sync Gateway does not support non-default durability settings at the bucket level for [durable writes](../../../server/current/learn/data/durability.md). Make sure your buckets have their bucket durability setting set to `None`. If this is not the case you'll get a [failure scenario](../../../server/current/learn/data/durability.md#failure-scenarios), `Write while SyncWrite is pending`, and the attempt at a durable write fails.

You can still use high durability settings when set on the client side. For more information about how to configure client-level durability for durable writes, see [specifying levels](../../../server/current/learn/data/durability.md#specifying-levels).

## [](#time-to-live-ttl)Time To Live (TTL)

> [!IMPORTANT]
> Document TTL is an Enterprise Edition only feature.

Couchbase Server Enterprise Edition lets you have documents expire after a period of time, called the document's Time To Live (TTL). This feature only works in Couchbase and Ephemeral buckets. It does not work in Memcached buckets. For more information, see [Expiration](../../../server/current/learn/data/expiration.md).

Sync Gateway does not support Bucket-level TTL, make sure your buckets have their `maxTTL` setting set to `0`. If the bucket setting has a non-zero `maxTTL` value set, Sync Gateway returns an error prompting you to set the value to `0` in the Couchbase Server Admin UI.

Similarly, do not set Collection-level TTL (`maxTTL` on collections) as this can interfere with Sync Gateway's internal documents, including those with `_sync` prefixes and other system documents that are essential for proper operation. If these system documents expire due to collection-level TTL, Sync Gateway may malfunction or fail to operate properly. You can use per-collection sync functions to set expiry on all documents within a collection when you need TTL-like behavior at the collection level, while preserving Sync Gateway's system documents.

> [!NOTE]
> You can still set Document expiration settings on individual documents.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](../access-control/sync-function/sync-function.md)
* [Import filter](../sync/import-processing.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Add/Update Sync Function](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
* [Sync Function Overview](../access-control/sync-function/sync-function.md)

###### [](#-3)

Reference material …​

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)