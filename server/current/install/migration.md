---
title: Enabling Timestamp-based Conflict Resolution for Migrated Data
description: The Timestamp-based Conflict Resolution method is the latest
  conflict resolution type available for a bucket.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/install/pages/migration.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:install:migration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/install/migration.html)

# Enabling Timestamp-based Conflict Resolution for Migrated Data

Use timestamp-based conflict resolution for transactions and the latest Couchbase features. You cannot change the conflict resolution type of an existing bucket. If the bucket was not created with timestamp-based conflict resolution, migrate the data to use it.

> The Timestamp-based Conflict Resolution method is the latest conflict resolution type available for a bucket. Couchbase Server supports this feature for new buckets. 

To enable timestamp-based conflict resolution for existing data, migrate the data to a new bucket with the timestamp-based conflict resolution type, using the `cbbackupmgr` tool. For more information about the `cbbackupmgr` tool, see [Backup and Restore](../manage/manage-backup-and-restore/manage-backup-and-restore.md).

> [!IMPORTANT]
> This is a one time migration. The bucket without timestamp-based conflict resolution must be removed and a new bucket with the [timestamp-based conflict resolution](../learn/clusters-and-availability/xdcr-conflict-resolution.md#timestamp-based-conflict-resolution) type must be created as part of the migration.

These are 2 scenarios:

* Scenario 1: Unidirectional replication for disaster recovery - Cluster 1 (Bucket A) continuously replicates data into Cluster 2 (Bucket A'), which is one way.
* Scenario 2: Bidirectional replication for data locality - Cluster 1 (Bucket A) and Cluster 2 (Bucket A’) replicate data into each other.

## [](#migration-during-unidirectional-replication)Migration during Unidirectional Replication

Follow these steps to migrate your data to a new bucket during unidirectional replication:

1. Stop application traffic coming into Cluster 1 (Bucket A).  
> [!NOTE]  
> Allow enough time for the replication queues to drain. Confirm by reviewing the XDCR Total Outbound Mutations statistic derived from `xdcr_changes_left_total`. For more information, see [manage:monitor/monitor-intro.html#monitoring-with-the-ui](#manage:monitor/monitor-intro.html#monitoring-with-the-ui).
2. Stop and delete the replication stream to Cluster 2 (Bucket A’). For instructions, see [XDCR Management Overview](../manage/manage-xdcr/xdcr-management-overview.md).
3. Run the `cbbackupmgr` tool to back up the bucket’s (Bucket A) data. For instructions, see [Backup](../backup-restore/enterprise-backup-restore.md).
4. Delete Bucket A from Cluster 1\. For instructions, see [Delete a Bucket](../manage/manage-buckets/delete-bucket.md).
5. Create Bucket B on Cluster 1 and select the Timestamp-based Conflict Resolution type. For instructions, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
6. Run the `cbbackupmgr` tool on Cluster 1 to restore data to Bucket B. Use the [cbbackupmgr restore](#backup-restore/cbbackupmgr-restore.adoc) command with the option `--force-updates` to restore data from the backup. This option disables conflict resolution during the restore, and it’s needed because the bucket you’re restoring to has a different conflict resolution type than the bucket the backup originated from.  
> [!NOTE]  
> The `--force-updates` option also updates the CAS of the restored documents.
7. After the data restore operation is complete on Cluster 1, delete Bucket A’ from Cluster 2.
8. Create Bucket B’ on Cluster 2 and select the Timestamp-based Conflict Resolution type.
9. Create a new unidirectional replication for Bucket B. See [XDCR Management Overview](../manage/manage-xdcr/xdcr-management-overview.md).

## [](#migration-during-bidirectional-replication)Migration during Bidirectional Replication

Follow these steps to migrate your data to a new bucket during bidirectional replication:

1. Stop application traffic coming into Cluster 1 (Bucket A) and Cluster 2 (Bucket A’).  
> [!NOTE]  
> Allow enough time for the replication queues to drain. Confirm by reviewing the XDCR Total Outbound Mutations statistic derived from `xdcr_changes_left_total`. For more information, see [manage:monitor/monitor-intro.html#monitoring-with-the-ui](#manage:monitor/monitor-intro.html#monitoring-with-the-ui).
2. Stop and delete the replication streams to both clusters. For instructions, see [XDCR Management Overview](../manage/manage-xdcr/xdcr-management-overview.md).
3. Run the `cbbackupmgr` tool on both clusters to backup the bucket data. For instructions, see [Backup](../backup-restore/enterprise-backup-restore.md).
4. Delete the Bucket A from Cluster 1 and Bucket A’ from Cluster 2\. For instructions, see [Delete a Bucket](../manage/manage-buckets/delete-bucket.md).
5. Create buckets on both clusters and select the Timestamp-based Conflict Resolution type. For instructions, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
6. Run the `cbbackupmgr` tool to restore data. Use the [cbbackupmgr restore](#backup-restore/cbbackupmgr-restore.adoc) command with the option `--force-updates` to restore data from the backup. This option disables conflict resolution during the restore, and it’s needed because the bucket you’re restoring to has a different conflict resolution type than the bucket the backup is from.  
> [!NOTE]  
> The `--force-updates` option also updates the CAS of the restored documents.
7. After the restore operation is complete on both clusters, create replication streams both ways between Cluster 1 and Cluster 2\. For more information, see [XDCR Management Overview](../manage/manage-xdcr/xdcr-management-overview.md).