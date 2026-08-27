---
title: Migrate Metadata to System Collection
description: Opt in to migrating Sync Gateway internal metadata from the default
  collection to the system collection in Sync Gateway 4.1.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/ROOT/pages/migrate-metadata-system-collection.adoc
  xref: xref:sync-gateway::migrate-metadata-system-collection.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/migrate-metadata-system-collection.html)

# Migrate Metadata to System Collection

> Opt in to migrating Sync Gateway internal metadata from the default collection to the system collection in Sync Gateway 4.1.  

Related _Application Deployment_ topics: [Release Notes](product-notes/release-notes.md) | [Compatibility Matrix](product-notes/compatibility.md)

## [](#overview)Overview

Sync Gateway stores internal metadata, including user documents, role documents, session documents, replication state, and DCP checkpoints, in the default collection (`_default._default`). This couples Sync Gateway's internal bookkeeping with customer document data in the same collection.

Sync Gateway 4.1 introduces an opt-in migration that relocates this metadata to the system collection (`_system._mobile`). Migrating provides the following benefits:

* Metadata is isolated from user application data.
* Sync Gateway metadata no longer appears alongside user-modifiable documents in the Capella UI.
* Eventing functions and SQL++ queries running against the default collection no longer process Sync Gateway internal documents.

> [!IMPORTANT]
> This migration is opt-in and is never applied automatically at upgrade. Your existing deployment is unaffected until you enable the feature.
> 
> This feature is only supported when all nodes in the cluster have been upgraded to Sync Gateway 4.1 and the cluster compatibility version is running at 4.1\. If you are using [Cluster Compatibility Version](cluster-compatibility-version.md) to stage your upgrade, ensure the freeze has been cleared and the compatibility version has advanced to 4.1 before enabling this migration.
> 
> The opt-in configuration flags are one-way. Once enabled, the migration cannot be reversed. There is no supported path to move metadata back to `_default._default`.

> [!NOTE]
> The migration runs in the background and does not impact your workloads. Databases remain fully available for reads and writes throughout the migration. New databases created after opting in have their Sync Gateway metadata stored in `_system._mobile` from the start, with no migration step required.

## [](#prerequisites)Prerequisites

* Sync Gateway 4.1 or later on all nodes in the cluster.
* Couchbase Server version that supports the `_system._mobile` collection.
* The `_system._mobile` collection must be available on the target bucket. Sync Gateway rejects the opt-in configuration if this collection is unavailable.

## [](#how-the-migration-works)How the Migration Works

The migration uses a two-level opt-in: one at the cluster level and one per database.

### [](#cluster-level-flag)Cluster-level flag

The bootstrap configuration flag `use_system_metadata_collection` acts as the cluster-wide feature gate. Enabling it allows individual databases to opt in and enables the dual-collection read behaviour at bootstrap. By itself, enabling the cluster flag does not migrate any data.

### [](#per-database-opt-in)Per-database opt-in

The database configuration field `use_system_metadata_collection` opts an individual database into the migration. You can opt in a database even if the cluster flag is not set.

Once you apply the opt-in configuration to a database, Sync Gateway waits until the configuration is confirmed applied on all nodes in the cluster, then starts the migration automatically. You do not need to call any API to trigger the migration.

### [](#what-migrates)What migrates

The migration relocates the following internal Sync Gateway metadata from `_default._default` to `_system._mobile`:

* User, role, and email index documents
* Session documents (TTL is preserved)
* Replication state and status documents
* DCP checkpoint documents
* Background process heartbeat and status documents
* Database state documents
* Sync Gateway configuration documents

The following are not migrated and remain in their existing locations:

* Collection-scoped document data (`_sync:rev:*`, `_sync:att*:*`)
* Metadata belonging to other databases on the same bucket (sibling databases)

Bucket-level bootstrap documents (`_sync:registry`, database config docs) migrate only after every database on the bucket has completed its migration.

### [](#database-availability-during-migration)Database availability during migration

Databases remain fully available for reads and writes throughout the migration. Sync Gateway uses a dual-collection read strategy during migration: reads go to `_system._mobile` first and fall back to `_default._default` only for keys not yet migrated. Writes always go to `_system._mobile` from the moment opt-in is applied.

Once the migration is complete, the fallback read path is disabled. Reads consult only `_system._mobile`.

New databases with no existing metadata skip the migration entirely and are marked complete immediately.

## [](#enable-the-migration)Enable the Migration

### [](#step-1-enable-the-cluster-level-flag)Step 1: Enable the cluster-level flag

Add the following to your Sync Gateway bootstrap configuration:

```json
{
  "bootstrap": {
    "use_system_metadata_collection": true
  }
}
```

This is a one-way change. Once set to `true`, the flag cannot be set back to `false`.

### [](#step-2-opt-in-each-database)Step 2: Opt in each database

Add the following to the database configuration for each database you want to migrate:

```json
{
  "use_system_metadata_collection": true
}
```

This is also a one-way change per database.

After you apply the database configuration, Sync Gateway starts the migration automatically once the configuration is confirmed on all nodes. No further action is required to start the migration.

## [](#monitor-migration-progress)Monitor Migration Progress

Use the `GET /{db}/_metadata_migration` endpoint on the Admin REST API to check the status of a migration.

> [!NOTE]
> This endpoint is available on the Admin port (`:4985`) only.

**Example request:**

```bash
GET /{db}/_metadata_migration
```

**Example response:**

```json
{
  "status": "running",
  "migration_id": "a1b2c3d4-...",
  "docs_processed": 45200,
  "docs_attempted": 45200,
  "docs_failed": 0,
  "docs_out_of_scope": 12,
  "passes": 2
}
```

| Field                | Description                                                                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| status               | Current migration status: running, completed, or error.                                                                                                |
| migration\_id        | Unique identifier for this migration run.                                                                                                              |
| docs\_processed      | Number of metadata documents successfully moved to \_system.\_mobile in this run.                                                                      |
| docs\_attempted      | Total number of documents the migrator has attempted to process.                                                                                       |
| docs\_failed         | Number of documents that encountered an error during migration. A non-zero value means some keys may not have migrated. Check last\_error for details. |
| docs\_out\_of\_scope | Number of keys observed in the fallback collection that belong to other databases or to bucket-level bootstrap documents. These are left in place.     |
| passes               | Number of scan passes the migrator has completed. The migration is complete when a pass finds no remaining in-scope keys.                              |

## [](#manual-migration-controls)Manual Migration Controls

The migration starts automatically after opt-in. Use the `POST /{db}/_metadata_migration` endpoint to intervene manually if needed.

**Required RBAC role:** Sync Gateway Architect

| Query parameter | Description                                                               |
| --------------- | ------------------------------------------------------------------------- |
| action          | start (default) to start or resume the migration, or stop to halt it.     |
| reset           | Set to true to discard previous progress and start a fresh migration run. |

**Retry after an error:**

```bash
POST /{db}/_metadata_migration?action=start
```

**Stop a running migration:**

```bash
POST /{db}/_metadata_migration?action=stop
```

> [!NOTE]
> A `400` response is returned if the database has not opted in to `use_system_metadata_collection`.

For the full API reference, see [GET /{db}/\_metadata\_migration](rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/get%5Fdb-%5Fmetadata%5Fmigration).

## [](#prometheus-statistics)Prometheus Statistics

Sync Gateway 4.1 adds seven Prometheus metrics under the `sgw_metadata_migration` subsystem, each labelled per database.

| Metric                                               | Type    | Description                                                                                                                                                                                                                   |
| ---------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| sgw\_metadata\_migration\_docs\_scanned\_total       | Counter | Total fallback keys observed across all scan passes.                                                                                                                                                                          |
| sgw\_metadata\_migration\_docs\_migrated             | Counter | Documents successfully moved or removed from the fallback collection.                                                                                                                                                         |
| sgw\_metadata\_migration\_docs\_out\_of\_scope       | Gauge   | Keys in the fallback collection belonging to other databases or bucket-level bootstrap documents on the most recent pass. This is a snapshot of the last pass, not a cumulative total.                                        |
| sgw\_metadata\_migration\_docs\_unknown\_prefix      | Gauge   | Unrecognized keys in the fallback collection on the most recent pass. A persistently non-zero value indicates the migration will not complete without intervention. Contact Couchbase Support if this value remains non-zero. |
| sgw\_metadata\_migration\_errors                     | Counter | Per-document errors during move or delete operations.                                                                                                                                                                         |
| sgw\_metadata\_migration\_seq\_poison\_pill\_applied | Counter | Number of times this node applied the sequence counter handoff during migration. Typically 0 or 1 per migration run.                                                                                                          |
| sgw\_metadata\_migration\_passes                     | Counter | Number of scan passes executed.                                                                                                                                                                                               |

For general Prometheus monitoring, see [Prometheus Monitoring](manage/stats-monitoring-prometheus.md).

## [](#troubleshooting)Troubleshooting

### [](#migration-stops-without-completing)Migration stops without completing

If `status` shows `error` or `docs_unknown_prefix` is persistently non-zero, the migration encountered keys it could not process. Use `POST /{db}/_metadata_migration?action=start` to retry. If the issue persists, contact Couchbase Support with the output of `GET /{db}/_metadata_migration` and your SGCollect bundle.

### [](#migration-not-starting-after-opt-in)Migration not starting after opt-in

The migration starts only after the opted-in configuration is confirmed applied on all nodes. In a multi-node cluster, verify all nodes have picked up the updated database configuration before expecting the migration to start.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Getting Started

* [Prepare](start-here/get-started-prepare.md)
* [Install](start-here/get-started-install.md)
* [Configure](start-here/get-started-configure.md)

###### [](#-3)

Product Information

* [Release Notes](product-notes/release-notes.md)
* [Compatibility Matrix](product-notes/compatibility.md)
* [Supported OS](product-notes/supported-environments.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)