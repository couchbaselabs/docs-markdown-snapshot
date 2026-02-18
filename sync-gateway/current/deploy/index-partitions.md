---
title: Partitioned Indexes
description: Partitioning a large index across multiple nodes
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/deploy/pages/index-partitions.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/current/deploy/index-partitions.html)

# Partitioned Indexes

> Partitioning a large index across multiple nodes  
> Explains how to use partitioned indexes in Sync Gateway

Related _Deploy_ topics: [Deployment](deployment.md) | [REST API Access](../rest-api/rest-api-access.md) | [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

## [](#overview)Overview

Partitioned indexes in Sync Gateway offer horizontal scalability for large deployments by sharding indexes across multiple nodes. This can decrease performance, as each partition is queried separately and results are aggregated. Only `allDocs` and `channels` indexes can be partitioned.

## [](#when-to-use)When to Use Partitioned Indexes

Partitioned indexes are an optimization in Sync Gateway intended only for deployments using Memory-Optimized Indexes (MOI) on Couchbase Server, and only when those MOI indexes have grown too large to fit on a single index node.

> [!IMPORTANT]
> Recommendation
> 
> Partitioned indexes should not be used for experimentation or general performance tuning. Partitioning should be configured only after careful evaluation. It increases resource usage (CPU and memory) on Query nodes, and may introduce performance degradation.

### [](#use-case)Appropriate Use Case

* You are using MOI.
* Your current GSI index size exceeds the memory capacity of a single index node.
* You cannot further split your data (for example, by collections or database sharding) to reduce index size.

In this case, partitioning can help by horizontally scaling the index across multiple nodes to keep it in memory.

### [](#when-not-to-use)When Not to Use Partitioned Indexes

* You’re not using MOI; that is, your indexes are disk-based.
* Your dataset is small or moderate in size, even if you have high concurrency.
* You have a high number of connections or clients, but not many documents.
* Your index size could be reduced by splitting data into multiple collections, which is the preferred approach.

### [](#index-size)What Impacts Index Size?

The size of Sync Gateway’s indexes is correlated to:

* The number of documents in a collection.
* The number of channels each document is assigned to.

If index size is a concern, your first approach should be to split documents across multiple collections.

Query performance is sensitive to channel design. Systems with many small channels tend to perform worse than those using fewer, larger channels. For better scalability and efficiency, prefer broader channel groupings over fine-grained ones.

Only if these strategies are exhausted, and you’re using MOI with oversized indexes, should partitioned indexes be considered.

## [](#migrate)Migrate to Partitioned Indexes

Before switching from non-partitioned to partitioned indexes, it’s important to understand the operational trade-offs and cluster implications. Here are two migration options, designed to accommodate different use cases and resource tolerances.

### [](#migrate-zero-downtime)Option 1: Zero Downtime (Recommended for Production)

This option is ideal for production environments where uptime is critical. It requires temporary over-provisioning of index nodes (2× size) while partitioned indexes are created. The advantage is no downtime; the disadvantage is temporarily higher resource usage.

Procedure

1. Spin up a new Sync Gateway instance.
2. Run [POST /{db}/\_index\_init](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Findex%5Finit) on the new instance with `num_partitions` set to the required number of partitions.
3. Wait for completion via [GET /{db}/\_index\_init](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/get%5Fdb-%5Findex%5Finit).
4. Run [POST /{db}/\_config](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/post%5Fdb-%5Fconfig) with `index.num_partitions` updated in the configuration to use new indexes.
5. Run [POST /\_post\_upgrade](../rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/post%5F%5Fpost%5Fupgrade) to remove old indexes.
6. Optionally, rebalance index nodes using Couchbase Server. For details, see [Index Redistribution](../../../server/current/learn/clusters-and-availability/rebalance.md#index-redistribution) in the Couchbase Server documentation.

> [!WARNING]
> If you are using [configuration groups](../configuration/configuration-overview.md#lbl-config-grp) running on a different index configuration, calling [POST /\_post\_upgrade](../rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/post%5F%5Fpost%5Fupgrade) can delete indexes out from under a running database. Please ensure that all configuration groups have consistent index configuration. For details, see [Configuration Group Considerations](#config-groups).

### [](#migrate-with-downtime)Option 2: With Downtime

This option requires no extra resources, but involves planned downtime. It involves lower intermittent hardware requirements.

Procedure

1. Take the database offline via [POST /{db}/\_config](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/post%5Fdb-%5Fconfig) with `offline` set to `true`.
2. Manually delete old Sync Gateway indexes.
3. Bring the database online using [POST /{db}/\_config](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/post%5Fdb-%5Fconfig) with `index.num_partitions` set to the required number of partitions.
4. Run integration and performance testing.

> [!WARNING]
> Manual index deletion can cause data loss or leave the system in an unstable state. Incorrect deletion of internal indexes can lead to system instability and requires full index rebuilds. We strongly advise using the standard procedure with zero downtime, unless you are fully aware of the implications.

## [](#guardrails)Guardrails

To prevent misconfiguration or accidental misuse, follow these best practices:

* **Never change the number of partitions without a plan**. Indexes are not deletable from Couchbase Server once creation starts. Reverting requires downtime and manual deletion. Make sure only advanced users (typically Architects or Admins) modify partitioning settings.
* Monitor memory and disk usage on index nodes during and after creation to catch unexpected bloat.
* Optionally set feature flags or config validation, if available, to restrict low-risk deployments from using this feature.

Changing the number of partitions "just to test it" may permanently increase index footprint, cause cluster performance issues, and trigger long rebalance operations.

## [](#config-groups)Configuration Group Considerations

If your deployment uses [Configuration Groups](../configuration/configuration-overview.md#lbl-config-grp), ensure that:

* All nodes are updated with the new config before running [POST /\_post\_upgrade](../rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/post%5F%5Fpost%5Fupgrade).
* Import and sync workloads are not unintentionally unbalanced across partitions.

Misalignment between config groups can lead to unexpected deletion of active indexes if [POST /\_post\_upgrade](../rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/post%5F%5Fpost%5Fupgrade) is run. This will result in:

* Couchbase Server (version 7.6 and later) falling back on a sequential scan of the Query nodes, which will seriously degrade Query performance.
* Recreating indexes that were deleted by another config when a node is rebooted with a different `index.num_partitions`, even after [POST /\_post\_upgrade](../rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/post%5F%5Fpost%5Fupgrade) is run.

## [](#supportability)Supportability

### [](#index-config)Identify Index Configuration

To identify the current index configuration, you can:

* Use [GET /{db}/\_config](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/get%5Fdb-%5Fconfig) to check the active configuration in `index.num_partitions`.
* Use [GET /{db}/\_index\_init](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/get%5Fdb-%5Findex%5Finit) to see if there is an index creation in progress.

### [](#failures)Identify Failures

To troubleshoot problems with index configurations, note the following.

* The status returned by [GET /{db}/\_index\_init](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/get%5Fdb-%5Findex%5Finit) includes `last_error`.
* Partial updates across nodes using Configuration Groups may result in mixed indexing behavior.
* If indexes are not removed post-upgrade, [POST /\_post\_upgrade](../rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/post%5F%5Fpost%5Fupgrade) may return a failure or partial success.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)