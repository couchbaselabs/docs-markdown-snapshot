---
title: Export and Migrate Data from Capella
description: Learn how to export data from Capella to other Capella clusters, to
  self-managed Couchbase Server, or to third-party databases.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/data-service/export.adoc
  xref: xref:cloud:clusters:data-service/export.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/data-service/export.html)

# Export and Migrate Data from Capella

> Learn how to export data from Capella to other Capella clusters, to self-managed Couchbase Server, or to third-party databases. 

Couchbase Capella provides flexible data export and migration capabilities to support your evolving infrastructure needs. The methods to export data from Capella include:

* Cross datacenter replication (XDCR)
* Cluster backups
* Bucket backups for full or granular migrations
* Command-line tools

Capella supports the following data export and migration scenarios:

* [Export to another Capella cluster](#migrate-capella).
* [Export to self-managed Couchbase Server](#export-selfmanage).
* [Export to a third-party database](#export-external).
* [Export a partial dataset](#partial-migration).
* [Migrate indexes and functions](#schema-index-migration).

> [!TIP]
> Assistance with data export and migration for those with paid plans is available from [Couchbase Support](../../support/manage-support.md). If you're using a free tier cluster, you can find community support through the [Couchbase forums](https://www.couchbase.com/forums/tag/couchbase-capella) and the Couchbase [discord channel](https://discord.com/invite/K7NPMPGrPk?utm%5Fsource=forums).

## [](#data-included)What You Can Export by Method

The following table summarizes what you can export using each method and tool:

| Data Type             | XDCR        | Cluster Backup | Bucket Backup | cbbackupmgr | cbexport |
| --------------------- | ----------- | -------------- | ------------- | ----------- | -------- |
| Documents (JSON)      |             |                |               |             |          |
| Scopes & Collections  | [1](#note1) | [2](#note2)    |               |             |          |
| Indexes (GSI)         | [3](#note3) | [4](#note3)    | [4](#note3)   |             |          |
| Search Indexes        |             |                |               |             |          |
| Eventing Functions    |             |                |               |             |          |
| Cluster Configuration | [5](#note5) | [6](#note6)    | [6](#note6)   |             |          |
| User Accounts & Roles |             |                |               |             |          |
| Allowed IP addresses  |             |                |               |             |          |

[1](#data-included) XDCR replicates data only and does not create scopes or collections on the destination bucket. If matching scopes and collections exist in the destination bucket, XDCR automatically maps data to them unless you choose the explicit mapping option for the replication.

[2](#data-included) `cbexport` does not preserve the scope and collection hierarchy. You can optionally embed the scope and collection names as fields within the exported JSON documents, but they do not restore as scopes and collections on import.

[3](#data-included) You must recreate indexes on the destination cluster. You can extract index definitions using the Capella UI. For more information about exporting index definitions, see [Migrating Indexes and Functions](#schema-index-migration).

[4](#data-included) Bucket backups and `cbbackupmgr` restore GSIs in a deferred state (**Created**), so you must manually build them after restore to get them into the **Ready** state. For more information, see [Migrating Indexes and Functions](#schema-index-migration).

[5](#data-included) Cluster backups include cluster configuration settings, but may need adjustment based on the destination environment.

[6](#data-included) When restoring bucket backups, the bucket configuration only restores if you allow the restore to create the bucket. If the bucket already exists, the restore does not change the configuration of the pre-existing bucket.

## [](#prerequisites)Prerequisites

Before exporting or migrating data, make sure you have the following common prerequisites where applicable. Each export option may have additional specific requirements, so make sure to review the documentation for your chosen option.

* The appropriate permissions:

  * For bucket backups and restores: [Project Owner](../../projects/project-roles.md#project-owner-role) role.
  * For cluster backups and XDCR: [Project Owner](../../projects/project-roles.md#project-owner-role) role.
  * For command-line tools: [Cluster access credentials](../manage-database-users.md).
* Network access configured:

  * [Allowed IP addresses](../allow-ip-address.md) configured.
  * Downloaded [security certificates](../../get-started/create-account.md#next-steps) for secure connections.
* Required tools installed for command-line migration:

  * [Couchbase command-line tools](../../reference/command-line-tools.md) package.

## [](#migrate-capella)Export to Another Capella Cluster

You can migrate data between Capella clusters using several options, depending on your requirements.

### [](#xdcr-migration)Option 1: Cross Datacenter Replication (XDCR)

XDCR replicates data in near-real-time from a source bucket to a destination bucket. When directly migrating to another Capella cluster, you can replicate data between clusters in the same or different regions, but they must share the same cloud service provider (CSP).

**When to use XDCR:**

* When you need to migrate data between operational Capella clusters in the same CSP with minimal downtime.
* When you need continuous data synchronization and can accept eventual consistency.
* When you need to verify data on the destination cluster before cutover.

**What XDCR migrates:**

| Data Type                  | Included         |
| -------------------------- | ---------------- |
| Documents (JSON)           |                  |
| Scopes & Collections       | [1](#xdcr-note1) |
| Indexes (GSI)              | [2](#xdcr-note2) |
| Full-Text Search Indexes   |                  |
| Eventing Functions         |                  |
| Cluster Settings           |                  |
| Cluster access credentials |                  |
| Allowed IP addresses       |                  |

1 XDCR replicates data only and does not create scopes or collections on the destination bucket. If matching scopes and collections exist in the destination bucket, XDCR automatically maps data to them unless the explicit mapping option was chosen for the replication. If you explicitly map source and destination scopes and collections, the scope and collections must exist on the destination bucket or the mapped data does not replicate. To copy the scopes and collections from 1 bucket to another, use [cbbackupmgr](../cli-backup-restore.md) to back up and restore only the scopes and collections without the documents using the `--disable-data` option.

2 XDCR replicates data only and does not create indexes on the destination bucket. If matching indexes already exist in the destination bucket, they index replicated data automatically.

**Limitations:**

* Cannot replicate data between clusters on different CSPs.
* Requires both source and destination clusters to be running simultaneously.
* Not available for free tier clusters.

For more information about using XDCR and for detailed procedures, see:

* [Cross Data Center Replication (XDCR)](../xdcr/xdcr.md)
* [Create a Replication Between Operational Clusters](../xdcr/manage-xdcr-replications.md#between-capella-dbs)
* [Manage Replication Security](../xdcr/manage-xdcr-security.md)

### [](#cluster-backup-restore)Option 2: Cloud Snapshot Cluster Backup

Cloud snapshots create a snapshot of your entire cluster and allow you to restore it to the same or a different cluster.

Using a cloud snapshot, you can back up and restore a cluster and all of its buckets in a single backup. For AWS and Azure clusters, you can restore a cloud snapshot backup to a different region on the same CSP. For GCP clusters, you cannot restore a cloud snapshot backup to a different region.

**When to use cluster backups:**

* Migrating an entire cluster to another Capella cluster.
* Moving to a different region or Availability Zone.
* Creating a copy of a production cluster for testing.

**What cluster backups include:**

| Data Type                  | Included                   |
| -------------------------- | -------------------------- |
| Documents (JSON)           |                            |
| Scopes & Collections       |                            |
| Indexes (GSI)              |                            |
| Search Indexes             |                            |
| Eventing Functions         |                            |
| Cluster Settings           | [1](#cluster-backup-note1) |
| Cluster access credentials |                            |
| Allowed IP addresses       |                            |

1 If the number of nodes differs between the backup and restore, Capella scales your cluster configuration up or down to the number of nodes in the backup.

> [!TIP]
> Before you [restore a cluster backup](../restore-cloud-snapshot.md), use the Couchbase Capella Management API to [get a list of all available cluster access credentials](../../management-api-reference/index.md#tag/Database-Credentials/operation/listDatabaseCredentials) and [get a list of all allowed IP addresses](../../management-api-reference/index.md#tag/Allowed-CIDRs-%28Cluster%29/operation/listAllowedCidrs) on your cluster.

**Limitations:**

* Not available for free tier clusters.
* Cannot restore to a different CSP.
* GCP clusters cannot restore to a different region.
* Restoring to a cluster with a different node count may cause performance issues until the cluster stabilizes after restore.
* Cluster backups do not capture buckets that use the Memory Only bucket type.

For more information about cluster backups, and detailed instructions for creating and restoring cluster backups, see:

* [Back Up and Restore An Entire Cluster](../cloud-snapshots.md)
* [Take or Schedule a Cluster Backup](../take-cloud-snapshot.md)
* [Restore a Cluster Backup](../restore-cloud-snapshot.md)

### [](#bucket-backup-restore)Option 3: Individual Bucket Backups Using the UI

Bucket backups allow you to back up and restore individual buckets, providing more granular control over your migration.

In the Capella UI, you can restore a bucket backup to a cluster in the same or different region, but it must be on the same cloud service provider (CSP). To restore a bucket to a different CSP, [download the backup](../backup-restore.md#downloading-backups) and use [cbbackupmgr](https://docs.couchbase.com/cloud/reference/command-line-tools.html#cbbackupmgr) to restore it to a cluster on a different CSP.

**When to use bucket backups:**

* Migrating specific buckets rather than entire clusters.
* Restoring data to a cluster with a different configuration in the same organization and CSP.
* Creating test environments with data subsets.

**What bucket backups include:**

| Data Type                  | Included |
| -------------------------- | -------- |
| Documents (JSON)           |          |
| Scopes & Collections       |          |
| Indexes (GSI)              |          |
| Search Indexes             |          |
| Eventing Functions         |          |
| Cluster Settings           |          |
| Cluster access credentials |          |
| Allowed IP addresses       |          |

**Limitations:**

* Not available for free tier clusters.
* When using the UI, you can restore to a bucket only to the same cloud service provider (CSP) as the 1 used to create the backup — such as from Azure to Azure.
* You can restore bucket backups only to a cluster running the same or later version of Couchbase Server.
* Bucket backups provide per-item consistency but do not guarantee consistency across items; the consistency window is typically within a few seconds under normal conditions.
* Limited to migrating documents, scopes and collections, indexes, and eventing functions.
* Global Secondary Indexes (GSIs) restore in a deferred state (**Created**). You must manually build them after the restore to make them active (**Ready**).

For more information about bucket backups, and detailed instructions for creating and restoring bucket backups using the UI, see:

* [Back Up and Restore Bucket Data](../backup-restore.md)
* [Manage Bucket Backups](../manage-backup.md)
* [Restore a Bucket Backup](../manage-restore.md)

### [](#cbbackupmgr-migration)Option 4: Command-Line Tools (cbbackupmgr)

Use `cbbackupmgr` for flexible, automated migrations between Capella clusters when you need more control over the backup and restore process. This method allows for migration between CSPs in Capella, but data transfer costs may apply.

**When to use cbbackupmgr:**

* Migrating from free tier clusters.
* When you need to migrate across CSPs.

**What cbbackupmgr migrates:**

| Data Type                  | Included                |
| -------------------------- | ----------------------- |
| Documents (JSON)           | [1](#cbbackupmgr-note1) |
| Scopes & Collections       | [1](#cbbackupmgr-note1) |
| Indexes (GSI)              | [2](#cbbackupmgr-note2) |
| Full-Text Search Indexes   |                         |
| Eventing Functions         |                         |
| Cluster Settings           |                         |
| Cluster access credentials |                         |
| Allowed IP addresses       |                         |

1 Supports filtering to migrate specific subsets of data.

2 GSI indexes restore in a deferred state (**Created**). You must manually build them after the restore to make them active (**Ready**). For more information, see [Build Indexes](../cli-backup-restore.md#build-indexes-2).

**Limitations:**

* Limited to migrating data, scopes, collections, indexes, and eventing functions.
* You can restore backups only to a cluster running the same or later version of Couchbase Server.
* GSIs restore in a deferred state (**Created**), so you must manually build them after restore to get them into the **Ready** state.
* You must create buckets manually.
* You must configure cluster settings manually.

For more information about using `cbbackupmgr` and for detailed instructions, see:

* [Back Up and Restore with Command-Line Tools](../cli-backup-restore.md#backup-free-cluster)

## [](#export-selfmanage)Export to Self-Managed Couchbase Server

You can export data from Capella to self-managed Couchbase Server deployments using several options, depending on your requirements.

### [](#xdcr-selfmanage)Option 1: Cross Datacenter Replication (XDCR)

XDCR can replicate data from a Capella operational cluster to a self-managed Couchbase Server cluster in near-real-time. Self-managed clusters can be on-premises or in a cloud environment. The clusters do not need to be on the same CSP (AWS, GCP, or Azure), but they must have [network connectivity](../xdcr/manage-xdcr-security.md) and run compatible Couchbase Server versions.

**When to use XDCR for self-managed migration:**

* Migrating with minimal downtime while maintaining an active Capella cluster.
* When you need continuous data synchronization during a phased migration.
* Moving data to on-premises or non-Capella cloud deployments.

**What XDCR migrates:**

| Data Type                  | Included         |
| -------------------------- | ---------------- |
| Documents (JSON)           |                  |
| Scopes & Collections       | [1](#xdcr-note1) |
| Indexes (GSI)              | [2](#xdcr-note2) |
| Full-Text Search Indexes   |                  |
| Eventing Functions         |                  |
| Cluster Settings           |                  |
| Cluster access credentials |                  |
| Allowed IP addresses       |                  |

1 XDCR replicates data only and does not create scopes or collections on the destination bucket. If matching scopes and collections exist in the destination bucket, XDCR automatically maps data to them unless the explicit mapping option was chosen for the replication. If you explicitly map source and destination scopes and collections, the scope and collections must exist on the destination bucket or the mapped data does not replicate. To copy the scopes and collections from 1 bucket to another, use [cbbackupmgr](../cli-backup-restore.md) to back up and restore only the scopes and collections without the documents using the `--disable-data` option.

2 XDCR replicates data only and does not create indexes on the destination bucket. If matching indexes already exist in the destination bucket, they index replicated data automatically.

**Limitations:**

* Not available for free tier clusters.
* Requires both source and destination clusters to be running simultaneously.

For more information about using XDCR and for detailed procedures, see:

* [Cross Data Center Replication (XDCR)](../xdcr/xdcr.md)
* [Create a Replication from Capella to a Self-Managed Cluster](../xdcr/manage-xdcr-replications.md#from-capella-to-self-managed)
* [Manage Replication Security](../xdcr/manage-xdcr-security.md)

### [](#cbbackupmgr-external)Option 2: cbbackupmgr

Use `cbbackupmgr` to create backups that you can restore to self-managed Couchbase Server installations.

**When to use cbbackupmgr:**

* Moving data to self-managed Couchbase Server environments.
* Migrating from free tier clusters.
* Creating portable backups for disaster recovery.

**What cbbackupmgr migrates:**

| Data Type                  | Included                |
| -------------------------- | ----------------------- |
| Documents (JSON)           | [1](#cbbackupmgr-note1) |
| Scopes & Collections       | [1](#cbbackupmgr-note1) |
| Indexes (GSI)              | [2](#cbbackupmgr-note2) |
| Full-Text Search Indexes   |                         |
| Eventing Functions         |                         |
| Cluster Settings           |                         |
| Cluster access credentials |                         |
| Allowed IP addresses       |                         |

1 Supports filtering to migrate specific subsets of data.

2 GSI indexes restore in a deferred state (**Created**). You must manually build them after the restore to make them active (**Ready**). For more information, see [Build Indexes](../cli-backup-restore.md#build-indexes-2).

**Limitations:**

* You can restore bucket backups only to a cluster running the same or later version of Couchbase Server.
* Limited to migrating data, scopes/collections, indexes, and eventing functions.
* Global Secondary Indexes (GSIs) restore in a deferred state (**Created**), so you must manually build them after restore to get them into the **Ready** state.

For more information about using `cbbackupmgr` and for detailed instructions, see:

* [Back Up and Restore with Command Line Tools](../cli-backup-restore.md)

### [](#ui-export)Option 3: Download Bucket Backups Using the UI

The Capella UI allows you to download bucket backups as `cbbackupmgr` archives. You can restore these downloads only to Couchbase systems (Capella or self-managed Server), not to third-party databases.

**When to use bucket backup downloads:**

* Restoring to a Capella cluster in a different CSP.
* Moving data to self-managed Couchbase Server environments.
* Creating portable backups for disaster recovery.
* Offline storage of bucket data.

**Limitations:**

* Not available for free tier clusters.
* You can restore downloaded bucket backups only to Couchbase systems (Capella or self-managed Server), not to third-party databases.
* You can restore bucket backups only to a cluster running the same or later version of Couchbase Server.
* Bucket backups provide per-item consistency but do not guarantee consistency across items; the consistency window is typically within a few seconds under normal conditions.
* Limited to migrating documents, scopes and collections, indexes, and eventing functions.
* Global Secondary Indexes (GSIs) restore in a deferred state (**Created**). You must manually build them after the restore to make them active (**Ready**).

For more information about downloading bucket backups using the UI, see:

* [Download a Bucket Backup in the Capella UI](../manage-backup.md#download-backup)

## [](#export-external)Export to Third-Party Systems

When migrating data from Capella to third-party systems, `cbexport` is the recommended option.

### [](#cbexport-method)cbexport

The [cbexport json](../../../server/current/tools/cbexport-json.md) command-line tool exports data from Capella to JSON format ([lines or list format](../../../server/current/tools/cbexport-json.md#DATASET%5FFORMATS)) for import into other systems.

**When to use cbexport:**

* Exporting data for import into third-party databases.
* Exporting data for compliance or archival purposes.
* Migrating from free tier clusters.

**What cbexport can export:**

| Data Type                  | Included             |
| -------------------------- | -------------------- |
| Documents (JSON)           | [1](#cbexport-note1) |
| Scopes & Collections       | [1](#cbexport-note1) |
| Indexes (GSI)              |                      |
| Search Indexes             |                      |
| Eventing Functions         |                      |
| Cluster Settings           |                      |
| Cluster access credentials |                      |
| Allowed IP addresses       |                      |

1 Supports filtering to export specific subsets of data.

**Limitations:**

* You cannot export data from multiple buckets with a single command. You must run separate export commands for each bucket or scope/collection.

For more information about using `cbexport` and for detailed instructions, see:

* [Import and Export Data with Command-Line Tools](../../connect/cli-import-export.md)
* [cbexport json](../../../server/current/tools/cbexport-json.md) in the Couchbase Server documentation

## [](#partial-migration)Partial Dataset Migration

If you need to migrate only specific subsets of your data, you can use filtering options available in some export options.

Filter by Scope and Collection

All migration methods support migrating specific scopes and collections:

* **XDCR**: Use scope and collection mapping to replicate specific data subsets
* **cbbackupmgr**: Use `--include-data` and `--exclude-data` flags
* **cbexport**: Specify scope and collection in export command
* **Bucket backups**: Restore to specific scopes/collections

## [](#schema-index-migration)Migrate Indexes and Functions

If you're using bucket backups or `cbbackupmgr` for migration, Global Secondary Indexes (GSI) do not automatically restore to an active state. Bucket backups and `cbbackupmgr` restore GSIs in a deferred state, so you must manually build them after restore to get them into the **Ready** state. For more information, see [Restore Indexes](../manage-restore.md#restore-indexes) and [Build Indexes](../cli-backup-restore.md#build-indexes-2).

For migration methods that do not include indexes and functions, you need to export and then manually recreate these components on your destination cluster.

### [](#export-indexes)Export GSI Definitions

To export GSI definitions from the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Operational**.
  * Click your current project name or search for a project and go to **Operational**.
  * Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with the Index Service.
3. Go to **Data Tools** **Indexes**.
4. Expand the listing for the index you want to export.
5. Copy the definition by clicking .  
You can then paste the definition into a query editor on your destination cluster.

For more information about indexes, see:

* [Manage Indexes](../index-service/manage-indexes.md)
* [CREATE INDEX](../../../server/current/n1ql/n1ql-language-reference/createindex.md) in the Couchbase Server documentation

### [](#export-fts)Export Search Index Definitions

You can export and import full Search index definitions from Capella using the Capella UI. For instructions, see:

* [Export a Search Index Definition from the Capella UI](../../search/export-search-index.md).
* [Import a Search Index Definition with the Capella UI](../../search/import-search-index.md).

### [](#recreate-functions)Recreate Eventing Functions

XDCR and `cbexport` do not include Eventing functions; you must manually recreate them on the destination cluster. If you're using bucket backups or `cbbackupmgr`, backups include Eventing functions, which restore automatically.

For more information, see [Add Eventing Functions](../../eventing/add-eventing-functions.md).

### [](#migrate-udfs)Migrate Query User-Defined Functions (UDF)

Each migration method handles UDFs in the following way:

* **Cluster backup (Cloud snapshots)**: Include both SQL++ UDF definitions and JavaScript UDF library files, which restore automatically.
* **Bucket backups and `cbbackupmgr`**: Include SQL++ UDF definitions, which restore automatically. JavaScript UDF library files do not back up and you must manually recreate them on the destination cluster.
* **XDCR and `cbexport`**: Do not include either SQL++ UDF definitions or JavaScript UDF library files and you must manually recreate them on the destination cluster.

To manually recreate JavaScript UDF libraries on the destination cluster, use the [library management tools](../../guides/create-javascript-library.md) in the Capella UI.

For more information, see [JavaScript Functions for Query Reference](../../javascript-udfs/javascript-functions-with-couchbase.md).

## [](#see-also)See Also

* [Back Up and Restore Bucket Data](../backup-restore.md)
* [Cluster Backups](../cloud-snapshots.md)
* [Back Up and Restore with Command-Line Tools](../cli-backup-restore.md)
* [Import and Export Data with Command-Line Tools](../../connect/cli-import-export.md)
* [Cross Datacenter Replication (XDCR)](../xdcr/xdcr.md)
* [Import Data with the Capella UI](import-data-documents.md)
* [Management API Reference](../../management-api-reference/index.md)