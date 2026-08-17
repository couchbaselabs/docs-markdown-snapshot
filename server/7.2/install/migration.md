---
title: Enabling Timestamp-based Conflict Resolution for Migrated Data
description: The Timestamp-based Conflict Resolution is a new conflict
  resolution type added in version 4.6.0.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/migration.adoc
  xref: xref:7.2@server:install:migration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/install/migration.html)

# Enabling Timestamp-based Conflict Resolution for Migrated Data

> The Timestamp-based Conflict Resolution is a new conflict resolution type added in version 4.6.0\. This new feature is supported for **new** buckets that are created in Couchbase Server version 4.6.0\. You cannot change the conflict resolution mode to the _Timestamp-based Conflict Resolution_ for existing buckets after upgrading to version 4.6.0\. 

If you wish to enable the timestamp-based conflict resolution for your existing data, then you must migrate your data to version 4.6.0 cluster using the `cbbackupmgr` tool. To learn more about the tool, See [Backup and Restore](../manage/manage-backup-and-restore/manage-backup-and-restore.md).

> [!IMPORTANT]
> This is a one time migration and the bucket must be switched to a new conflict resolution type as part of the migration.

To understand more about timestamp-based Conflict Resolution, see [Timestamp-Based Conflict Resolution](../learn/clusters-and-availability/xdcr-conflict-resolution.md#timestamp-based-conflict-resolution).

Here are two scenarios:

* Scenario 1 - In case of unidirectional replication, for example, for a disaster recovery where Cluster 1 (Bucket A) has one way replication streams to Cluster 2 (Bucket A').
* Scenario 2 - In case of bidirectional replication, for example, for data locality where Cluster 1 (Bucket A) has both ways replication streams to Cluster 2 (Bucket A').

For Scenario 1, perform the following steps to migrate your data to a new cluster:

1. Stop application traffic coming into Cluster 1 (Bucket A).  
> [!NOTE]  
> Allow _enough tim_e for the replication queues to drain. Check the **outbound XDCR mutation** statistics to confirm. For instructions, see [Monitoring Outgoing XDCR](../manage/monitor/monitor-intro.md#outgoing%5Fxdcr%5Fstats).
2. Stop and delete Replication stream to Cluster 2 (Bucket A'). For instructions, see [XDCR Management Overview](../manage/manage-xdcr/xdcr-management-overview.md).
3. Run the `cbbackupmgr` tool to back up the entire bucket's (Bucket A) data. For instructions, see [Backup](../backup-restore/enterprise-backup-restore.md).
4. Delete Bucket A from Cluster 1\. For instructions, see [Delete a Bucket](../manage/manage-buckets/delete-bucket.md).
5. Upgrade Cluster 1 to Couchbase Server version 4.6.0\. For instructions, see [Upgrading Couchbase Server](upgrade.md).
6. Create a new Bucket B with the conflict resolution type as **Timestamp** selected. For instructions, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
7. Run the `cbbackupmgr` tool to restore data. When restoring data from backup (use the `--force-updates` option). Make sure to disable the **Conflict Resolution** option during the restore. This is required since the conflict resolution types of the source and destination clusters do not match.
8. Once the restore operation is completed on Cluster 1, delete Bucket A' from Cluster 2.
9. Upgrade Cluster 2 to Couchbase Server version 4.6.0.
10. Create a new Bucket B' with the Conflict Resolution type as **Timestamp** selected.
11. Create a new unidirectional replication for Bucket B. See [XDCR Management Overview](../manage/manage-xdcr/xdcr-management-overview.md).

For Scenario 2, perform the following steps to migrate your data to a new cluster:

1. Stop application traffic coming to Cluster 1 (Bucket A) and Cluster 2 (Bucket A').  
> [!NOTE]  
> Note: Allow _enough time_ for the replication queues to drain. Check the **outbound XDCR mutation** statistics to confirm. For instructions, see [Monitoring Outgoing XDCR](../manage/monitor/monitor-intro.md#outgoing%5Fxdcr%5Fstats).
2. Stop and delete replication to both clusters. For instructions, see [XDCR Management Overview](../manage/manage-xdcr/xdcr-management-overview.md).
3. Run the `cbbackupmgr` tool to backup the entire bucket data on both clusters. For instructions, see [Backup](../backup-restore/enterprise-backup-restore.md).
4. Delete the Bucket A from Cluster 1 and Bucket A' from Cluster 2\. For instructions, see [Delete a Bucket](../manage/manage-buckets/delete-bucket.md).
5. Upgrade both clusters to Couchbase Server version 4.6.0\. For instructions, see [Upgrading Couchbase Server](upgrade.md).
6. Create new buckets on both clusters with the conflict resolution type as **Timestamp** selected. For instructions, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
7. Run the `cbbackupmgr` tool to restore data. When restoring data from backup (use the `--force-updates` option). Make sure to disable **Conflict Resolution** option during the restore. This is required because the conflict resolution types of the source and destination do not match.
8. Once the restore operation is completed on both clusters, create replication streams both ways from Cluster 1 and Cluster 2\. See [XDCR Management Overview](../manage/manage-xdcr/xdcr-management-overview.md).