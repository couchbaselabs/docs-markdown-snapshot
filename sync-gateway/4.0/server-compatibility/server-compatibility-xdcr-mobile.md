---
title: Bi-directional XDCR with Mobile Clusters
description: Enable active-active deployments between mobile clusters using
  bi-directional Cross Data Center Replication (XDCR) with Sync Gateway 4.0.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/server-compatibility/pages/server-compatibility-xdcr-mobile.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.0@sync-gateway:server-compatibility:server-compatibility-xdcr-mobile.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/4.0/server-compatibility/server-compatibility-xdcr-mobile.html)

# Bi-directional XDCR with Mobile Clusters

> Enable active-active deployments between mobile clusters using bi-directional Cross Data Center Replication (XDCR) with Sync Gateway 4.0.  
> Sync Gateway 4.0 introduces bi-directional XDCR support between mobile clusters through a fundamental architectural change from revision trees to version vectors.

_Related topics_: [Buckets](server-compatibility-buckets.md) | [Collections](server-compatibility-collections.md) | [Eventing](server-compatibility-eventing.md) | [Transactions](server-compatibility-transactions.md) | [XDCR](server-compatibility-xdcr.md) | [Backup and restore](server-compatibility-backups.md)

_Other Topics_: [Compatibility Matrix](../product-notes/compatibility.md)

## [](#introduction)Introduction

Bi-directional XDCR between mobile clusters represents a significant architectural evolution in Sync Gateway 4.0.

This enables active-active deployments where multiple clusters process writes simultaneously while maintaining data consistency across geographically distributed datacenters.

This relies on a change in how Sync Gateway tracks document revisions, transitioning from revision trees to version vectors, which enables consistent revision tracking across all participating clusters.

## [](#revision-tracking)Revision Tracking

Sync Gateway 4.0 fundamentally changes how it tracks document revisions to enable bi-directional XDCR between mobile clusters.

SGW 4.0 switches from revision trees to version vectors for implementing and managing bi-directional XDCR deployments.

### [](#revision-trees)Revision Trees

Sync Gateway versions prior to 4.0 tracked document revisions using revision trees with Multi-Version Concurrency Control (MVCC).

This approach created a tree structure for each document where branches represented conflicting updates and nodes contained revision IDs. While effective for mobile replication protocols, revision trees maintained cluster-specific metadata that prevented meaningful bi-directional replication with XDCR. Each cluster maintained its own revision tree, making it impossible to preserve revision history when documents replicated between clusters.

### [](#version-vectors)Version Vectors

Version vectors provide a proven mechanism for tracking causality in distributed systems.

A version vector consists of hybrid logical clocks maintained by each component capable of updating documents in the distributed environment. Each instance of Couchbase Lite represents its own component in the version vector, while Sync Gateway and XDCR interact with the component associated with the cluster-specific Couchbase Server bucket. Each component increments its own count when making changes, creating a vector that captures the complete update history across all participating actors.

This architectural change enables:

* Unified revision tracking that both XDCR and Sync Gateway understand
* Consistent revision identification across all clusters
* Preservation of causality relationships between document versions
* Automatic conflict detection based on vector comparison

The version vector metadata travels with documents during replication, ensuring that revision history remains intact regardless of which cluster processes the document.

#### [](#conflict-resolution-with-version-vectors)Conflict Resolution with Version Vectors

The shift to version vectors changes the default conflict resolution strategy from revision trees' Most-Write-Wins to Last-Write-Wins.

Last-Write-Wins uses hybrid logical clock timestamp comparison to resolve conflicts deterministically across all clusters. Configure custom conflict resolvers at the XDCR level for specific business logic requirements.

## [](#architecture-and-data-flow)Architecture and Data Flow

The bi-directional XDCR architecture coordinates multiple components to maintain consistency.

### [](#document-processing-pipeline)Document Processing Pipeline

Document mutations flow through an orchestrated pipeline that preserves mobile metadata while preventing replication loops.

When a document changes in either cluster, Sync Gateway assigns version vector updates that include the identifier and incremented count. XDCR recognizes these version vectors and replicates the document while preserving the metadata. The receiving cluster's Sync Gateway processes the incoming document through its import mechanism, recognizing that the version vector indicates an external update that does not require additional versioning.

### [](#metadata-filtering)Metadata Filtering

XDCR automatically filters cluster-specific metadata to prevent corruption of local state.

System documents with the `_sync:` prefix remain local to each cluster — these include sequence trackers, user definitions, and role assignments. Document-level sync metadata in extended attributes gets selectively replicated, with cluster-local information like sequence numbers filtered while global metadata like version vectors passes through. This filtering happens transparently without requiring manual configuration.

## [](#configuration-requirements)Configuration Requirements

Enabling bi-directional XDCR requires specific configuration at both the bucket and replication levels.

### [](#bucket-configuration)Bucket Configuration

Enable cross-cluster versioning on all participating buckets to support version vectors.

Apply the `enableCrossClusterVersioning=true` configuration to buckets on both source and target clusters before establishing replication.

### [](#sync-gateway-configuration)Sync Gateway Configuration

Sync Gateway 4.0 requires no additional configuration for bi-directional XDCR support.

Sync Gateway 4.0 enforces shared bucket access by default, enabling coexistence with direct SDK writes and XDCR replication. Sync Gateway Enterprise Edition enables document import processing by default, automatically handling replicated documents from XDCR.

### [](#two-active-active-clusters)Two Active-Active Clusters

The configuration involves two clusters with bi-directional replication between them.

Both clusters run Sync Gateway in active mode, processing reads and writes from mobile clients. Load balancers distribute traffic based on geographic proximity or availability. This topology provides the foundation for zero-downtime disaster recovery and global data distribution. Testing and validation have focused primarily on two-cluster deployments.

### [](#checkpoint-management)Checkpoint Management

Clients maintain independent checkpoints for each cluster they connect to.

When a client connects to a cluster for the first time, it begins replication from sequence zero, checking which documents are missing and need downloading. The client stores this checkpoint locally, associated with the cluster's identifier. Subsequent connections to the same cluster resume from the stored checkpoint, downloading only changes since the last sync. This mechanism prevents redundant data transfer when clients switch between clusters.

### [](#version-compatibility)Version Compatibility

Different Couchbase Lite versions exhibit varying levels of support for bi-directional XDCR deployments.

Couchbase Lite 4.0 provides full support, including the ability to switch between clusters while maintaining consistency. Earlier versions (3.x and 2.x) can synchronize with Sync Gateway 4.0 but cannot switch between clusters without potential consistency issues.

> [!NOTE]
> XDCR does not replicate Sync Gateway users, roles, or channel access grants between clusters.

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