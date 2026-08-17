---
title: New In 4.1
description: Couchbase Sync Gateway -- What's new in the latest release
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/ROOT/pages/whatsnew.adoc
  xref: xref:sync-gateway::whatsnew.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/whatsnew.html)

# New In 4.1

> Couchbase Sync Gateway — What's new in the latest release  
> This content covers the new features introduced in Sync Gateway 4.1

> [!CAUTION]
> Sync Gateway 4.0 introduces some breaking changes. If you're upgrading from 3.x, see [Upgrading Sync Gateway](upgrading.md).

## [](#overview-4-1)Overview 4.1

Sync Gateway 4.1 focuses on operational reliability and scalability for production deployments. This release introduces non-disruptive rolling upgrades with a safe rollback path, distributed resync for large datasets, channel history management APIs, and an opt-in migration to isolate Sync Gateway internal metadata from user application data, and document channel history management APIs.

## [](#non-disruptive-rolling-upgrades)Non-Disruptive Rolling Upgrades

Sync Gateway 4.1 introduces cluster compatibility version, which transforms rolling upgrades into a low-risk, routine operational task.

* Upgrade a cluster node by node without downtime and without reducing cluster capacity or throughput.
* Freeze the cluster compatibility version before starting an upgrade to preserve a safe rollback path throughout the upgrade window. A freeze persists across node restarts and is cluster-wide.
* Roll back any upgraded node to the previous version at any point before starting an upgrade, without data loss or invasive operations such as bucket flushing or backup and restore.
* Unfreeze when all nodes are on the new version to start an upgrade and activate new cluster-wide features.

Three new Admin REST API endpoints support this workflow: `GET /_cluster_compat_version`, `POST /_cluster_compat_version/freeze`, and `POST /_cluster_compat_version/unfreeze`.

For more information, see [Cluster Compatibility Version](cluster-compatibility-version.md).

## [](#distributed-resync)Distributed Resync

Sync Gateway 4.1 redesigns the resync mechanism to distribute work in parallel across all nodes in the cluster.

In previous versions, resync ran sequentially on a single node, making it impractical for large datasets. In Sync Gateway 4.1, resync distributes the workload automatically across all available nodes without any configuration changes. Resync runs alongside live application traffic with bounded resource usage, and adding nodes to the cluster increases resync throughput.

The `GET /{db}/_resync` response adds two new fields: `docs_targeted` for tracking estimated total documents to process across the cluster, and `docs_errored` for per-node error counts. Two new Prometheus metrics, `sgw_database_resync_docs_targeted` and `sgw_database_resync_errors_total`, support monitoring distributed resync runs.

For more information, see [Resync](manage/resync.md).

## [](#channel-history-management)Channel History Management

Sync Gateway 4.1 introduces Admin REST API endpoints for managing channel history in both user and document metadata.

In deployments with high channel grant and revocation frequency, channel history grows without bound. This causes two operational problems: metadata bloat on documents and user records, and unnecessary revocation messages sent to clients during zero-checkpoint replications such as after an app reinstall or checkpoint rollback.

* **User channel history:** Two new endpoints let administrators retrieve a user's channel access history and selectively remove specific channel entries, preventing Sync Gateway from re-sending old revocations during future zero-checkpoint replications.
* **Document channel history:** Two new endpoints let administrators retrieve inactive channel history for specific documents and remove entries older than a specified sequence number. Using the current head sequence performs a deep clean of all historical channel metadata for the targeted documents without affecting document content.

Both operations are non-destructive to user data and do not interrupt active continuous replications.

For more information, see [Channel History Management](manage/channel-history.md).

## [](#metadata-isolation-migrate-to-system-collection)Metadata Isolation: Migrate to System Collection

Sync Gateway 4.1 introduces an opt-in migration that moves Sync Gateway internal metadata from the default collection (`_default._default`) to the system collection (`_system._mobile`).

* Sync Gateway metadata is isolated from user application data in its own collection.
* Internal Sync Gateway documents no longer appear alongside user-modifiable documents in the Capella UI.
* Eventing functions and SQL++ queries against the default collection no longer process Sync Gateway system documents.

The migration is opt-in at both the cluster level and per database, and is never applied automatically at upgrade. Databases remain fully available for reads and writes throughout the migration. The migration is a one-way operation and cannot be reversed.

A new Admin REST API endpoint `GET|POST /{db}/_metadata_migration` lets operators monitor migration status and manually start, stop, or retry the operation. Seven new Prometheus metrics track migration progress per database under the `sgw_metadata_migration` subsystem.

For more information, see [Migrate Metadata to System Collection](migrate-metadata-system-collection.md).

## [](#compatibility)Compatibility

* You must use Couchbase Server 7.6.0 or later. Use 7.6.6 or later for bi-directional XDCR features.
* See the [Compatibility Matrix](product-notes/compatibility.md) for full version compatibility details.

## [](#see-also)See Also

[What's new in the previous version 4.0](../4.0/whatsnew.md).

### [](#sync-gateway-release-notes)Sync Gateway Release Notes

[Read the full 4.1 release notes here](product-notes/release-notes.md).

## [](#upgrading)Upgrading

[Upgrade Sync Gateway](upgrading.md).

> [!IMPORTANT]
> Downgrading from Sync Gateway 4.1 to an earlier version is not supported after the full cluster has been upgraded. Use [Cluster Compatibility Version](cluster-compatibility-version.md) to preserve a rollback path during the upgrade window.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](access-control/sync-function/sync-function.md)
* [Import filter](sync/import-processing.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api/rest-api.md)
* [Admin REST API](rest-api/rest-api-admin.md)
* [Metrics REST API](rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)