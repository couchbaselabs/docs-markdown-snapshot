---
title: Restore a Bucket Backup
description: You can restore a bucket backup to the same cluster where it was
  created or another cluster in the same organization.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/manage-restore.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:clusters:manage-restore.adoc[]
---

[View original HTML](/cloud/clusters/manage-restore.html)

# Restore a Bucket Backup

> You can restore a bucket backup to the same cluster where it was created or another cluster in the same organization. 

Use the procedures on this page to restore data from a bucket backup. For more information about how to create and manage bucket backups, see [Manage Bucket Backups](manage-backup.md). For more information about how bucket backups work in Couchbase Capella, see [Back Up and Restore Bucket Data](backup-restore.md).

To backup or restore data for an entire cluster, see [Back Up and Restore An Entire Cluster](cloud-snapshots.md).

## [](#restore-prerequisites)Prerequisites

> [!IMPORTANT]
> Permissions Required
> 
> To view and restore bucket data from a backup:
> 
> * You need the [Project Owner](../projects/project-roles.md#project-owner-role) role for the project with the cluster that created the bucket backup and the project containing the destination cluster for the restore. If you have the `Organization Owner` role, you already have the [Project Owner](../projects/project-roles.md#project-owner-role) role for all projects in the organization.

* The source cluster that created the bucket backup must still exist.
* You can only restore bucket backups to a cluster running the same [major version](databases.md#cluster-version) or later as the cluster that created the bucket backup.
* You can only restore data to an existing bucket with the same name and [conflict resolution methods](data-service/manage-buckets.md#add-bucket) as the bucket from the backup.
* Because of how Capella stores backups, you can only restore to a bucket in the _same_ Cloud Service Provider (CSP) as the one used to create the backup — such as from Azure to Azure. If you need a backup that can be restored across different CSPs, you can use a locally-stored bucket backup — see [Downloadable backups](backup-restore.md#downloading-backups), or the [cbbackupmgr](cli-backup-restore.md#backup-and-restore-examples) command line tool.

## [](#restore-bucket)Restore a Bucket

Couchbase recommends that you only restore data from bucket backups in worst-case scenarios. You should use other recovery methods, such as [XDCR replication](xdcr/xdcr.md) from a redundant cluster as the primary recovery method.

> [!NOTE]
> Capella resolves any conflicts during the restore with the conflict resolution method configured for the buckets. For example, if a key-value pair in the target bucket is newer than the one in the backup, then the one from the backup is not restored unless [otherwise specified](#overwrite-docs) in the restore settings.

1. Open the **Backup** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to work with backups.

    1. Go to **Backups**.
2. Select the bucket you want to restore.
3. Click **Restore** for the bucket backup you want to restore.  
> [!TIP]  
> Clicking the **From Date** date picker allows you to select a previous date for a backup cycle or on-demand bucket backup.
4. Specify the **Destination Cluster**.  
The restore location can be the current cluster (chosen by default) or a different cluster in your organization. If you select **Restore to a different cluster**, the **Cluster** list appears.

  1. When restoring to a different cluster, use the **Cluster** list to select the cluster that’s the destination of the restore. You can only restore to a cluster in the same [organization](../organizations/organizations.md#organizations).
5. Choose the **Services to Restore**.

  1. Select each service you want to restore. By default, all options are selected. You must select at least one service.
6. (Optional) Apply **Other Options**.

  1. **Overwrite Documents From Backup**  
  When enabled, this option overwrites later versions of documents with earlier versions from the bucket backup. By default, this option is deselected.
  2. **Automatically Remove Deleted Collections**  
  When enabled, this option removes empty collections from the restore. By default, this option is deselected.
  3. **Filter Keys**  
  Use this field to enter a regular expression (RE2) to filter keys. You can use Filter Keys to restore a specified portion of your dataset from the bucket backup.
  4. **Filter Values**  
  Use this field to enter a regular expression (RE2) to filter values. You can use Filter Values to restore a specified portion of your dataset from the bucket backup.
  5. **Map Data**  
  This field allows you to map data from the backup to differently named data containers on the cluster. For example, buckets can be remapped to other buckets (`bucket=newbucket`), scopes and collections to other scopes and collections in the same bucket (`bucket.scope=bucket.newscope` or `bucket.scope.collection=bucket.scope.newcollection`). Map sources can only be specified once and cannot overlap.
  6. **Include Data**  
  Use this field to restore only specific data containers from the bucket backup. Use the following format for Include Data items: `bucket.scope`, or `bucket.scope.collection`.  
  > [!TIP]  
  > As bucket names can contain periods, they must be escaped: `my\.bucket.my-scope`.  
  Included data can only be specified once and cannot overlap, for example `bucket1` and `bucket1.scope1`.
  7. **Exclude Data**  
  Use this field to define any buckets, scopes, or collections you want to exclude from the restore. Excludes are defined as follows: `bucket.scope`, and `bucket.scope.collection`.
7. To start the restore, click **Restore Backup**.  
There can be a delay while Capella schedules the restore. Once the restore starts, its status appears on the Cluster page. The restore automatically recreates any missing buckets. Capella also adds backup and restore events to the [Activity Log](monitoring/activity-log.md).

## [](#restore-indexes)Restore Indexes

> [!IMPORTANT]
> Permissions Required
> 
> To access indexes in the Couchbase Capella UI:
> 
> * You need the [Project Owner](../projects/project-roles.md#project-owner-role) or [Data Writer](../projects/project-roles.md#project-cluster-data-reader-writer) role for the project with the cluster.

If GSI indexes were included in the bucket you restored, they’re automatically restored in a round-robin fashion among the current nodes running the Index Service. These indexes are created, but not built.

Indexes are created and not built because Couchbase Capella does not know the optimal index topology ahead of time. By not building the indexes, Capella gives you the option to manually move each index between nodes and build them yourself. However, if you find the automatic index distribution acceptable, you can use the Capella UI to rebuild each index.

To Rebuild an Automatically-Restored GSI Index

1. Open the **Indexes** page for your cluster:

  1. With the **Projects** tab in your organization open, select the project with the cluster you want.
  2. With the **Operational** tab open, select your cluster.
  3. Click the **Data Tools** tab.
  4. In the navigation menu, click **Indexes**.
2. Each restored index displays a status of **Created**. In the **Status** column, click the Play icon  for each index you want to rebuild.  
![The 'Tools > Indexes' tab showing multiple indexes with a status of 'Created' with Play icons.](_images/indexes-tab-rebuild-index-after-restore-hosted.png)  
Each index you build displays the **Ready** status when the process is complete.

## [](#view-restore-downloaded-backup)View and Restore a Downloaded Bucket Backup

When [downloaded](backup-restore.md#downloading-backups), you can unzip a zip archive file and use the Couchbase Server [cbbackupmgr](../reference/command-line-tools.md#cbbackupmgr) utility to view, examine, or restore the contents of the bucket backup repository.

For more information about the download file, see [About the Zip Archive File](backup-restore.md#about-zip-archive-file).

For more information about the cbbackupmgr utility, see [cbbackupmgr](../reference/command-line-tools.md#cbbackupmgr) in [Command Line Tools](../reference/command-line-tools.md).

If you’re running cbbackupmgr commands against Couchbase Capella clusters with the cluster access credentials, there are some cbbackupmgr disable options that you must use. These restrictions do not apply if you’re running cbbackupmgr commands against your self-managed clusters, using the downloaded backup archive.