---
title: Revisions
description: About Sync Gateway's use of Revisions, Revision Trees and Revision Caches.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.2/modules/ROOT/pages/revisions.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/3.2/revisions.html)

# Revisions

> About Sync Gateway’s use of Revisions, Revision Trees and Revision Caches.  
> Revisions are at the heart of Couchbase Mobile’s ability to respond flexibly and securely to changing data from server to edge.

## [](#introduction)Introduction

### [](#generation)Generation

_Documents_ and _buckets_ (collections of, usually related, documents) are the basic units of data within Couchbase.

Remember that within _Couchbase Mobile_, each document comprises:

* A Document ID
* A current revision ID
* A JSON body
* Metadata

Binary data such as images, audio and other multimedia objects are stored separately from the document in an entity known as a _blob_ (or _attachment_).

Each change to a document (even its creation and deletion) is recorded as a [revisions](#lbl-revs). Changes to _blobs_ do not generate revisions.

### [](#lbl-revs)Format

Couchbase creates a revision whenever a document is created, updated or deleted. Each revision is given a unique _Revision ID_ in addition to the _Document ID_.

The _revisions_ are contained within a document’s _metadata_, as a [revision tree](#lbl-revtree).

Sync Gateway uses a _revision id_ to resolve conflicts arising when making concurrent changes to replicated copies of distributed data. It comprises two parts:

* A generation ID  
This is a sequential auto-incrementing number. It is specific to the database on which the document resides. Couchbase Lite generates simple integers. Sync Gateway generates more complex long base64 values.  
The contents of remote revision IDs are implementation dependent. Do not base any processing logic on their contents.
* A hash derived from the document contents

### [](#lbl-revtree)Structure

The revisions for each document form a _revision tree_ within its metadata.

This revision tree comprises all revisions made to the document throughout its lifetime to date, in sequence. The _current revision_ (the most recent version of the document) being the tip of the tree, the _leaf_ node.

A revision tree’s growth is unlimited. So Couchbase periodically removes obsolete revisions to maintain performance levels. This process is known as [Revision Pruning](#lbl-prune).

## [](#lbl-prune)Revision Pruning

In the section

[Algorithm](#lbl-alg) | [Controls](#lbl-rtctrl) | [Constraints](#lbl-rtcons) | [Learn More](#lbl-rt-more)

Pruning is the process of removing obsolete revisions. It automatically runs whenever a new revision is generated.

> [!TIP]
> Use the Admin Rest API endpoint for [Database Configuration](rest%5Fapi%5Fadmin.md#tag/Database-Configuration) to provision any configuration changes to properties described in this content.

### [](#lbl-alg)Algorithm

Although fundamentally the same, the pruning algorithm works slightly differently between Sync Gateway and Couchbase Lite.

On Sync Gateway, the pruning algorithm is applied to the shortest, non-tombstoned branch in the revision tree.

The algorithm allows the branch to retain a configurable number of revisions (revs\_limit) and removes all older revisions.

### [](#lbl-rtctrl)Controls

You can vary the number of retained revisions using the Configuration File’s [revs\_limit](configuration-schema-database.md#database-revs%5Flimit)setting.

So, for example, with a `revs_limit` of 1,000 the algorithm will keep the last 1,000 revisions in the shortest non-tombstoned branch and remove any others from that branch.

> [!NOTE]
> Do not set `revs_limit` below 100 when `allow_conflicts = true`  
> **Otherwise** …​ you may adversely affect the conflict resolution process, as there may be insufficient revision history to resolve a given conflict.

The default and minimum values of `revs_limit` are dependent on whether [allow conflicts](#configuration-schema-database.html#database-allow%5Fconflicts)is set True or False — see [Table 1](#tbl%5Fmin%5Fdefault%5Fvals).

The process to remove obsolete revisions is called pruning and runs automatically every time a revision is added. Although fundamentally the same, the pruning algorithm works slightly differently between Sync Gateway and Couchbase Lite. On Sync Gateway, the pruning algorithm is applied to the shortest, non-tombstoned branch in the revision tree.

If there are conflicting revisions, the document may end up with **disconnected branches** after the pruning process.

In the animation below, the document has a conflicting branch (revisions `4'` \- `1001'`). When the shortest branch (in this case the conflicting branch) reaches the 1003rd update, it gets is cut off. The revision tree is not in a corrupted state and the logic that chooses the winning revision still applies. But it may make it impossible to do certain merges (n-way merge) to resolve conflicts and will occupy disk space that could have been freed if the conflict was resolved early on.

![pruning sg](https://cl.ly/3C1G3t3R1v19/pruning-sg.gif) 

Figure 1\. Pruning

If the revision tree gets into this state then the only option to resolve the conflict is to pick a winning branch and tombstone all the non-winning conflicting branches.

> [!NOTE]
> Setting the `revs_limit` to a value below 100 when `allow_conflicts = true` may adversely affect the conflict resolution process, as there may be insufficient revision history to resolve a given conflict.

__Table 1\. Default and Minimum Values__
| Release | Revs Limit | Allow Conflicts setting |         |
| ------- | ---------- | ----------------------- | ------- |
| True    | False      |                         |         |
| 2.6+    | default    | \+ 100                  | \+ 50   |
| minimum | \+ 20      | \+ 1                    |         |
| 2.0-2.5 | default    | \+ 100                  | \+ 1000 |
| minimum | \+ 50      | \+ 1                    |         |
| 1.x     | default    | \+ 1000                 | \+ 1000 |
| minimum | \+ 20      | \+ 20                   |         |

### [](#lbl-rtcons)Constraints

The default and minimum values of `revs_limit` are dependent on whether [allow\_conflicts](configuration-schema-database.md#database-allow%5Fconflicts) is True or False.

The presence of multiple unresolved conflicts in a revision tree can impair the pruning process. It may result in obsolete revisions not being pruned or in the premature pruning of revisions.

### [](#lbl-rt-more)Learn More

To learn more about revision pruning and database size management in general see our blog: [Pruning — Managing DB Sizes in Couchbase Mobile](https://blog.couchbase.com/database-sizes-and-conflict-resolution/#pruning).

## [](#lbl-caching)Caching

In this section

[Control](#lbl-ctrl) | [Cache Limit Configuration](#lbl-cache-limit-config) | [Sharding](#lbl-sharding) | [Delta Sync](#lbl-deltasync) | [Disabling the Cache](#lbl-disable)

Whenever a document is accessed its revision tree (or at least some portion of its revision tree) is also cached.

### [](#lbl-ctrl)Control

You can control the size of the revision cache using the [database.cache.rev\_cache](configuration-schema-database.md#database-cache-rev%5Fcache) settings within the configuration file, specifically:

* [rev\_cache.max\_memory\_count\_mb](configuration-schema-database.md#cache-rev%5Fcache-max%5Fmemory%5Fcount%5Fmb)
* [rev\_cache.shard\_count](configuration-schema-database.md#database-cache-rev%5Fcache-shard%5Fcount)
* [rev\_cache.size](configuration-schema-database.md#database-cache-rev%5Fcache-size)

### [](#lbl-cache-limit-config)Cache Limit Configuration

There are two ways to configure the size of the revision cache: set a memory limit in MB using [rev\_cache.max\_memory\_count\_mb](configuration-schema-database.md#cache-rev%5Fcache-max%5Fmemory%5Fcount%5Fmb), or set the maximum number of document revisions in cache [rev\_cache.size](configuration-schema-database.md#cache-rev%5Fcache%5Fsize). These configurations allow you to configure both limits to the number of documents and the maximum memory usage within the rev cache to reduce the risk of Out of Memory (OOM) issues. If both configs are set, this results in eviction behavior of the rev cache based on both the memory footprint and number of items in the cache. If any of these limits are reached, cache eviction will be performed.

#### [](#cache-size)Cache Size

Use the [rev\_cache.size](configuration-schema-database.md#database-cache-rev%5Fcache-size) setting to specify the total number of document revisions to be cached in memory for all (recently accessed) documents.

When the revision cache is full, Sync Gateway will remove older document revisions to make room for newer ones.

By adjusting this setting you can fine-tune Sync Gateway’s memory consumption. This can be useful when working on servers with limited memory and in cases when Sync Gateway creates and-or updated many new documents relative to the number of read operations.

#### [](#cache-maximum-memory)Cache Maximum Memory

You can use the [rev\_cache.max\_memory\_count\_mb](configuration-schema-database.md#cache-rev%5Fcache-max%5Fmemory%5Fcount%5Fmb) setting to specify the maximum amount of memory the revision cache should take up in MB. Setting the value to `0` will disable any eviction based on memory at rev cache.

> [!IMPORTANT]
> `rev_cache.max_memory_count_mb` is an Enterprise only setting.

### [](#lbl-sharding)Sharding

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

The **Community Edition** is configured with the default value and ignores any [rev\_cache.shard\_count](configuration-schema-database.md#database-cache-rev%5Fcache-shard%5Fcount) value in the configuration file.

You can control the number of shards into which Sync Gateway will split its revisions cache by using the [rev\_cache.shard\_count](configuration-schema-database.md#database-cache-rev%5Fcache-shard%5Fcount)

More shards means lower cache contention when accessing distinct revisions, at the cost of some memory overhead per-shard.

> [!IMPORTANT]
> Do not change the default [database.cache.rev\_cache.shard\_count](configuration-schema-database.md#database-cache-rev%5Fcache-shard%5Fcount) unless advised to do so by Couchbase Support — see: [Couchbase Support Policy](https://www.couchbase.com/support-policy).

### [](#lbl-deltasync)Delta Sync

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

When executing a write operation with delta\_sync enabled the revision body is backed up in the bucket and retained for [database.delta\_sync.rev\_max\_age\_seconds](configuration-schema-database.md#database-delta%5Fsync-rev%5Fmax%5Fage%5Fseconds), during which time it is available for the calculation of future revision deltas.

As a result, new deltas can only be generated for read requests that come in within the [database.delta\_sync.rev\_max\_age\_seconds](configuration-schema-database.md#database-delta%5Fsync-rev%5Fmax%5Fage%5Fseconds) time window.

Storing backed up revision bodies for delta sync incurs additional bucket storage, the size of which equates to:  
`(doc_size * updates_per_day * rev_max_age_seconds) / 86400` — see [Example 1](#ex-deltastor).

Example 1\. Calculating Additional Delta-Sync Storage

Enabling delta sync would take up an additional 400 KB of storage on Couchbase Server, assuming:

* An average document size of 4 KB
* 100 writes/day
* The default {`rev_max_age_seconds`} value

Equating to: `(4 * 100 * 86400)/86400 = 400 KB`

Setting [database.delta\_sync.rev\_max\_age\_seconds](configuration-schema-database.md#database-delta%5Fsync-rev%5Fmax%5Fage%5Fseconds) to zero will generate deltas opportunistically on pull replications, with no additional storage requirements.

### [](#lbl-disable)Disabling the Cache

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

Disabling the revision cache can be useful when there are very large documents or if you expect a very low cache hit rate. Otherwise it can negatively impact the latency of replications.

> [!NOTE]
> Do not disable the revision cache, unless advised to do so by Couchbase Support — see: [Couchbase Support Policy](https://www.couchbase.com/support-policy).

To disable the revision cache entirely, set [rev\_cache.size](configuration-schema-database.md#database-cache-rev%5Fcache-size) to zero. Community Edition ignores a zero setting.

## [](#compacting)Compacting

Attachments added post 3.0 are automatically removed from the bucket upon reference removal, document delete or document purge. This contrasts with the behavior of Legacy attachments, which can remain in the bucket even after their reference removal, document delete or document purge.

The compaction garbage collection process (`/{db}/_compact`) can be used to remove these legacy attachments and reclaim the underlying storage.

You can run the garbage collection process in one of two modes:

* tombstone  
Purges the JSON bodies of non-leaf revisions.
* attachment  
Removes redundant legacy attachments.  
The legacy attachment compaction process scans all documents in the bucket, removing unreferenced attachments.

See the REST API call endpoint [{db}/\_compact](rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Fcompact).

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](#sync-function-overview.adoc)
* [Import filter](import-processing.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)