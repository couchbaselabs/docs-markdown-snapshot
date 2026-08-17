---
title: Revisions
description: About Sync Gateway's use of Revisions, Revision Trees and Revision Caches.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/revisions.adoc
  xref: xref:2.8@sync-gateway::revisions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/revisions.html)

# Revisions

> About Sync Gateway's use of Revisions, Revision Trees and Revision Caches.  
> Revisions are at the heart of Couchbase Mobile's ability to respond flexibly and securely to changing data from server to edge.

_Related concepts topics_: [Users](../current/access-control/users.md) | [Roles](../current/access-control/roles.md) | [Channels](../current/access-control/channels.md) | Revisions | [Tombstones](../current/manage/managing-tombstones.md)

_Other related topics_: [Pruning — Managing DB Sizes in Couchbase Mobile](https://blog.couchbase.com/database-sizes-and-conflict-resolution/#pruning) | [Data Replication Protocol - Revision Trees](https://blog.couchbase.com/data-replication-couchbase-mobile/#revision-trees) | [MVCC — Demystifying Conflict Resolution](https://blog.couchbase.com/conflict-resolution-couchbase-mobile/#multi-version-concurrency-control)\]

## [](#introduction)Introduction

_Documents_ and _buckets_ (collections of, usually related, documents) are the basic units of data within Couchbase.

Remember that within Couchbase Mobile a document comprises:

* A Document ID
* A current revision ID
* A JSON body
* Metadata

Each change to a document (even its creation and deletion) is recorded as a _revision_. The document's [revisions](#lbl-revs) are contained within its _metadata_, which stores the revision history as a [revision tree](#lbl-revtree).

Note that binary data such images, audio or other multimedia objects are stored separately from the document,in an entity known as a _blob_ (or _attachment_). Changes to _blobs_ do not generate revisions.

## [](#lbl-revs)Revisions

Couchbase creates a revision whenever a document is created, updated or deleted. So, each document comprises a series of one or more revisions, a _revision tree_.

Each revision is given a unique _Revision ID_ in addition to the _Document ID_.

The revision id is used when resolving any conflicts arising when concurrent changes are made to replicated copies of distributed data. It comprises two parts:

* a generation ID  
This is a sequential auto-incrementing number, specific to the database on which the document resides. Couchbase Lite generates simple integers. Sync Gateway generates more complex long base64 values.  
The contents of remote revision IDs are implementation dependent. Do not base any processing logic on their contents.
* a hash derived from the document contents

## [](#lbl-revtree)Revision Trees

A document's _revision tree_ comprises each revision — in sequence — that has been made to the document throughout its lifetime to date. The tip of that tree, the _leaf_ node, is the _current revision_ — the most recent version of the document.

A revision tree's growth is unlimited and obsolete revisions need to be removed in order to maintain performance levels. This process is know as [Revision Tree Pruning](#lbl-prune).

## [](#lbl-prune)Revision Tree Pruning

In the section

[Algorithm](#lbl-alg) | [Controls](#lbl-rtctrl) | [Constraints](#lbl-rtcons) | [Learn More](#lbl-rt-more)

The process of removing obsolete revisions (_pruning_) runs automatically every time a revision is added.

### [](#lbl-alg)Algorithm

Although fundamentally the same, the pruning algorithm works slightly differently between Sync Gateway and Couchbase Lite.

On Sync Gateway, the pruning algorithm is applied to the shortest, non-tombstoned branch in the revision tree.

The algorithm allows the branch to retain a configurable number of revisions (revs\_limit) and removes all older revisions.

### [](#lbl-rtctrl)Controls

You can vary the number of retained revisions using the Configuration File's [revs\_limit](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-revs%5Flimit) setting.

So, for example, with a `revs_limit` of 1000 the algorithm will keep the last 1000 revisions in the shortest non-tombstoned branch and remove any others from that branch.

> [!NOTE]
> Do not set `revs_limit` below 100 when `allow_conflicts = true`  
> **Otherwise** …​ you may adversely affect the conflict resolution process, as there may be insufficient revision history to resolve a given conflict.

### [](#lbl-rtcons)Constraints

The default and minimum values of `revs_limit` are dependent on whether [allow\_conflicts](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-allow%5Fconflicts) is True or False.

The presence of multiple unresolved conflicts in a revision tree can impair the pruning process. This may result in obsolete revisions not being pruned, or in revisions being pruned prematurely.

### [](#lbl-rt-more)Learn More

To learn more about revision pruning and database size management in general see our blog: [Pruning — Managing DB Sizes in Couchbase Mobile](https://blog.couchbase.com/database-sizes-and-conflict-resolution/#pruning).

## [](#lbl-caching)Revision Caching

In this section

[Control](#lbl-ctrl) | [Size](#lbl-size) | [Sharding](#lbl-sharding) | [Delta Sync and Revisions](#lbl-deltasync) | [Disabling the Revision Cache](#lbl-disable)

Whenever a document is accessed its revision tree (or at least some portion of its revision tree) is also cached.

### [](#lbl-ctrl)Control

You can control the size of the revision cache using the [rev\_cache](../current/configuration/configuration-properties-legacy.md#databases-cache-rev-cache) settings within the configuration file, specifically:

* [rev\_cache.size](../current/configuration/configuration-properties-legacy.md#databases-cache-rev-cache-size)
* [rev\_cache.shard\_count](../current/configuration/configuration-properties-legacy.md#databases-cache-rev-cache-shard%5Fcount)

### [](#lbl-size)Size

Use the [rev\_cache.size](../current/configuration/configuration-properties-legacy.md#databases-cache-rev-cache-size) setting to specify the total number of document revisions to be cached in memory for all (recently accessed) documents.

When the revision cache is full, Sync Gateway will remove older document revisions to make room for newer ones.

By adjusting this setting you can fine-tune Sync Gateway's memory consumption. This can be useful when working on servers with limited memory and in cases when Sync Gateway creates and-or updated many new documents relative to the number of read operations.

### [](#lbl-sharding)Sharding

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

The **Community Edition** is configured with the default value and ignores any [rev\_cache.shard\_count](../current/configuration/configuration-properties-legacy.md#databases-cache-rev-cache-shard%5Fcount) value in the configuration file.

You can control the number of shards ino which Sync Gateway will split its revisions cache by using the [rev\_cache.shard\_count](../current/configuration/configuration-properties-legacy.md#databases-cache-rev-cache-shard%5Fcount)

More shards means lower cache contention when accessing distinct revisions, at the cost of some memory overhead per-shard.

> [!NOTE]
> Do not change the default [rev\_cache.shard\_count](../current/configuration/configuration-properties-legacy.md#databases-cache-rev-cache-shard%5Fcount) unless advised to do so by Couchbase Support — see: [Couchbase Support Policy](https://www.couchbase.com/support-policy).

### [](#lbl-deltasync)Delta Sync and Revisions

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

When executing a write operation with delta\_sync enabled the revision body is backed up in the bucket and retained for [this\_db.delta\_sync.rev\_max\_age\_seconds](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-delta%5Fsync-rev%5Fmax%5Fage%5Fseconds), during which time it is available for the calculation of future revision deltas.

As a result, new deltas can only be generated for read requests that come in within the [this\_db.delta\_sync.rev\_max\_age\_seconds](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-delta%5Fsync-rev%5Fmax%5Fage%5Fseconds) time window.

Storing backed up revision bodies for delta sync incurs additional bucket storage, the size of which equates to:  
\`(doc\_size \* updates\_per\_day \* rev\_max\_age\_seconds) / 86400 \` — see [Example 1](#ex-deltastor).

Example 1\. Calculating Additional Delta-Sync Storage

Enabling delta sync would take up an additional 400 KB of storage on Couchbase Server, assuming:

* An average document size of 4 KB
* 100 writes/day
* The default {`rev_max_age_seconds`} value

Equating to: `(4 * 100 * 86400)/86400 = 400 KB`

Setting [this\_db.delta\_sync.rev\_max\_age\_seconds](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-delta%5Fsync-rev%5Fmax%5Fage%5Fseconds) to zero will generate deltas opportunistically on pull replications, with no additional storage requirements.

### [](#lbl-disable)Disabling the Revision Cache

> [!IMPORTANT]
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

Disabling the revision cache can be useful when there are very large documents or if you expect a very low cache hit rate. Otherwise it can negatively impact the latency of replications.

> [!NOTE]
> Do not disable the revision cache, unless advised to do so by Couchbase Support — see: [Couchbase Support Policy](https://www.couchbase.com/support-policy).

To disable the revision cache entirely, set [rev\_cache.size](../current/configuration/configuration-properties-legacy.md#databases-cache-rev-cache-size) to zero. Community Edition ignores a zero setting.

## [](#related-content)Related Content

###### [](#)

Learn more …​

* [Sync Function](../current/access-control/sync-function/sync-function.md)
* [Import filter](../current/sync/import-processing.md)

###### [](#-2)

Reference material …​

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)