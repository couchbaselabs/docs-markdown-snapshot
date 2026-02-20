---
title: Revisions
description: About Sync Gateway's revision tracking using version vectors and
  revision caches in 4.0+.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/manage/pages/revisions.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:sync-gateway:manage:revisions.adoc[]
---

[View original HTML](/sync-gateway/current/manage/revisions.html)

# Revisions

> About Sync Gateway’s revision tracking using version vectors and revision caches in 4.0+.  
> Revisions are at the heart of Couchbase Mobile’s ability to respond flexibly and securely to changing data from server to edge.

## [](#introduction)Introduction

### [](#generation)Generation

_Documents_ and _collections_ are the basic units of data within Couchbase.

Remember that within _Couchbase Mobile_, each document comprises:

* A Document ID
* A current revision ID
* A JSON body
* Metadata

Binary data such as images, audio and other multimedia objects are stored separately from the document in an entity known as a _blob_ (or _attachment_).

An application records each change to a document as a revision. Document creation and deletion also generate revisions.

### [](#lbl-revs)Revision Tracking in 4.0+

Starting with Sync Gateway 4.0+, revision tracking changed from revision trees to [version vectors](../server-compatibility/server-compatibility-xdcr-mobile.md#version-vectors) for improved distributed system support.

#### [](#version-vectors-4-0)Version Vectors (4.0+)

Sync Gateway 4.0+ uses [version vectors](../server-compatibility/server-compatibility-xdcr-mobile.md#version-vectors) to track document revisions.

A version vector stores the version history of a document across multiple sources to enable consistent conflict resolution across a distributed deployment.

Sync Gateway uses the Hybrid Logical Vector implementation described in [HLV Data Maintained in xattr](../../../server/current/learn/clusters-and-availability/xdcr-enable-crossclusterversioning.md#hlv-data-maintained-in-xattr) for XDCR compatibility. Each element of a version vector is composed of two parts: a timestamp and a unique ID of the source (Couchbase Lite client or Couchbase Server cluster).

Timestamps for Sync Gateway are implemented using a _Hybrid Logical Clock_. This is a combination of a physical and a logical clock: the physical clock is the time returned by the system, in nanoseconds. The logical clock is a counter, which is incremented when the physical clock yields a value either smaller than or equal to the currently stored, physical clock-value.

For more information, see [Time Synchronization](../../../server/current/learn/clusters-and-availability/xdcr-conflict-resolution.md#time-synchronization).

Each Couchbase Lite instance runs its own _Hybrid Logical Clock_.

* A version vector contains 1 entry for each unique source consisting of the latest modified timestamp
* The number of sources preserved is at least 5, and revisions older than [versionPruningWindowHrs](../../../server/current/learn/clusters-and-availability/xdcr-enable-crossclusterversioning.md#version-pruning-window-hrs) are pruned on document modification

The contents of version vectors are implementation dependent. Do not base any processing logic on their contents.

#### [](#revision-trees-legacy-compatibility)Revision Trees (Legacy Compatibility)

Sync Gateway 4.0+ maintains parallel revision trees for backward compatibility with Couchbase Lite versions earlier than 4.0+. These revision trees:

* Write in parallel alongside [version vectors](../server-compatibility/server-compatibility-xdcr-mobile.md#version-vectors) for legacy client support
* Exist solely for backward compatibility - not used for conflict resolution in 4.0+ environments
* Follow the traditional structure with generation IDs and content hashes
* Are automatically pruned to maintain performance
* Preserve existing documents that used revision trees before the 4.0+ upgrade

For detailed information about revision trees, see [Revisions](../../3.3/manage/revisions.md).

### [](#automatic-conflict-resolution)Automatic Conflict Resolution

Sync Gateway 4.0+ resolves conflicts automatically using Last Write Wins strategy. The document timestamps to resolve conflicts. The timestamps associated with the most recent updates of source and target documents are compared. The document whose update has the more recent timestamp prevails. This eliminates the need for extensive revision history and allows for efficient storage management.

## [](#lbl-prune)Revision Pruning

In the section

[Version Vector Pruning (4.0+)](#lbl-alg) | [Controls](#lbl-rtctrl) | [\[lbl-rtcons\]](#lbl-rtcons) | [Learn More](#lbl-rt-more)

Pruning is the process of removing obsolete revisions. It automatically runs whenever a new revision is generated.

> [!TIP]
> Use the Admin Rest API endpoint for [Database Configuration](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration) to provision any configuration changes to properties described in this content.

### [](#lbl-alg)Version Vector Pruning (4.0+)

Sync Gateway 4.0+ uses a simplified pruning approach for [version vectors](../server-compatibility/server-compatibility-xdcr-mobile.md#version-vectors):

* The number of sources preserved is at least 5, and revisions older than [versionPruningWindowHrs](../../../server/current/learn/clusters-and-availability/xdcr-enable-crossclusterversioning.md#version-pruning-window-hrs) are pruned on document modification
* 1 revision exists per client that wrote a document or resolved a conflict

This approach eliminates the complexity of revision tree management while ensuring sufficient history for conflict resolution.

### [](#lbl-rtctrl)Controls

You can configure revision retention using the Configuration File’s [revs\_limit](../configuration/configuration-schema-database.md#database-revs%5Flimit) setting.

For Sync Gateway 4.0+ with automatic conflict resolution enabled, low `revs_limit` values provide optimal performance and storage efficiency. The Last Write Wins conflict resolution strategy supports values as low as 1.

### [](#legacy-compatibility)Legacy Compatibility

For compatibility with Couchbase Lite versions earlier than 4.0+, Sync Gateway maintains legacy revision tree structures. These are automatically managed and do not require manual configuration in 4.0+ deployments.

### [](#automatic-conflict-resolution-4-0)Automatic Conflict Resolution (4.0+)

Sync Gateway 4.0+ uses Last Write Wins conflict resolution by default, which eliminates the need for extensive revision history.

* Sync Gateway maintains both revision tree IDs and a version vector
* `revs_limit` applies to the number of revision tree IDs stored, not to version vector elements
* Version vector elements are controlled by `versionPruningWindowHrs` XDCR bucket setting
* No manual conflict resolution configuration required

### [](#lbl-rt-more)Learn More

To learn more about revision pruning and database size management in general see our blog: [Pruning — Managing DB Sizes in Couchbase Mobile](https://blog.couchbase.com/database-sizes-and-conflict-resolution/#pruning).

## [](#lbl-caching)Caching

In this section

[Control](#lbl-ctrl) | [Cache Limit Configuration](#lbl-cache-limit-config) | [Sharding](#lbl-sharding) | [Delta Sync](#lbl-deltasync) | [Disabling the Cache](#lbl-disable)

Whenever a document is accessed, its revision data is cached for improved performance.

### [](#lbl-ctrl)Control

You can control the size of the revision cache using the [database.cache.rev\_cache](../configuration/configuration-schema-database.md#database-cache-rev%5Fcache) settings within the configuration file, specifically:

* [rev\_cache.max\_memory\_count\_mb](../configuration/configuration-schema-database.md#cache-rev%5Fcache-max%5Fmemory%5Fcount%5Fmb)
* [rev\_cache.shard\_count](../configuration/configuration-schema-database.md#database-cache-rev%5Fcache-shard%5Fcount)
* [rev\_cache.size](../configuration/configuration-schema-database.md#database-cache-rev%5Fcache-size)

### [](#lbl-cache-limit-config)Cache Limit Configuration

You can configure the revision cache size in two ways: set a memory limit in MB using [rev\_cache.max\_memory\_count\_mb](../configuration/configuration-schema-database.md#cache-rev%5Fcache-max%5Fmemory%5Fcount%5Fmb), or set the maximum number of document revisions in cache [rev\_cache.size](../configuration/configuration-schema-database.md#cache-rev%5Fcache%5Fsize). These configurations allow you to configure both limits to the number of documents and the maximum memory usage within the rev cache to reduce the risk of Out of Memory (OOM) issues. If you set both configs, the rev cache evicts entries based on both the memory footprint and number of items in the cache. When either limit reaches its threshold, Sync Gateway performs cache eviction.

#### [](#cache-size)Cache Size

Use the [rev\_cache.size](../configuration/configuration-schema-database.md#database-cache-rev%5Fcache-size) setting to specify the total number of document revisions to be cached in-memory for all (recently accessed) documents.

When the revision cache is full, Sync Gateway removes older document revisions to make room for newer ones.

By adjusting this setting you can fine-tune Sync Gateway’s memory consumption. This can be useful when working on servers with limited memory and in cases when Sync Gateway creates and-or updated new documents relative to the number of read operations.

#### [](#cache-maximum-memory)Cache Maximum Memory

You can use the [rev\_cache.max\_memory\_count\_mb](../configuration/configuration-schema-database.md#cache-rev%5Fcache-max%5Fmemory%5Fcount%5Fmb) setting to specify the maximum amount of memory the revision cache should take up in MB. Setting the value to `0` disables any eviction based on memory at rev cache.

> [!IMPORTANT]
> `rev_cache.max_memory_count_mb` is an Enterprise only setting.

### [](#lbl-sharding)Sharding

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

The **Community Edition** is configured with the default value and ignores any [rev\_cache.shard\_count](../configuration/configuration-schema-database.md#database-cache-rev%5Fcache-shard%5Fcount) value in the configuration file.

You can control the number of shards into which Sync Gateway will split its revisions cache by using the [rev\_cache.shard\_count](../configuration/configuration-schema-database.md#database-cache-rev%5Fcache-shard%5Fcount)

More shards means lower cache contention when accessing distinct revisions, at the cost of some memory overhead per-shard.

> [!IMPORTANT]
> Do not change the default [database.cache.rev\_cache.shard\_count](../configuration/configuration-schema-database.md#database-cache-rev%5Fcache-shard%5Fcount) unless advised to do so by Couchbase Support — see: [Couchbase Support Policy](https://www.couchbase.com/support-policy).

### [](#lbl-deltasync)Delta Sync

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

When executing a write operation with delta\_sync enabled the revision body is backed up in the bucket and retained for [database.delta\_sync.rev\_max\_age\_seconds](../configuration/configuration-schema-database.md#database-delta%5Fsync-rev%5Fmax%5Fage%5Fseconds), during which time it is available for the calculation of future revision deltas.

As a result, new deltas can only be generated for read requests that come in within the [database.delta\_sync.rev\_max\_age\_seconds](../configuration/configuration-schema-database.md#database-delta%5Fsync-rev%5Fmax%5Fage%5Fseconds) time window.

Storing backed up revision bodies for delta sync incurs additional bucket storage, the size of which equates to:  
`(doc_size * updates_per_day * rev_max_age_seconds) / 86400` — see [Example 1](#ex-deltastor).

Example 1\. Calculating Additional Delta-Sync Storage

Enabling delta sync would take an additional 400 KB of storage on Couchbase Server, assuming:

* An average document size of 4 KB
* 100 writes/day
* The default {`rev_max_age_seconds`} value

Equating to: `(4 * 100 * 86400)/86400 = 400 KB`

Setting [database.delta\_sync.rev\_max\_age\_seconds](../configuration/configuration-schema-database.md#database-delta%5Fsync-rev%5Fmax%5Fage%5Fseconds) to zero generates deltas opportunistically on pull replications, with no additional storage requirements.

### [](#lbl-disable)Disabling the Cache

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

Disabling the revision cache can be useful when there are large documents or if you expect a low cache hit rate. Otherwise it can negatively impact the latency of replications.

> [!NOTE]
> Do not disable the revision cache, unless advised to do so by Couchbase Support — see: [Couchbase Support Policy](https://www.couchbase.com/support-policy).

To disable the revision cache entirely, set [rev\_cache.size](../configuration/configuration-schema-database.md#database-cache-rev%5Fcache-size) to zero. Community Edition ignores a zero setting.

## [](#compacting)Compacting

Attachments added post 3.0 are automatically removed from the bucket upon reference removal, document delete or document purge. This contrasts with the behavior of Legacy attachments, which can remain in the bucket even after their reference removal, document delete or document purge.

The compaction garbage collection process (`/{db}/_compact`) can be used to remove these legacy attachments and reclaim the underlying storage.

You can run the garbage collection process in one of two modes:

* tombstone  
Purges the JSON bodies of non-leaf revisions.
* attachment  
Removes redundant legacy attachments.  
The legacy attachment compaction process scans all documents in the bucket, removing unreferenced attachments.

See the REST API call endpoint [{db}/\_compact](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Fcompact).

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](../access-control/sync-function/sync-function.md)
* [Import filter](../sync/import-processing.md)

###### [](#-3)

Reference material …​

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)