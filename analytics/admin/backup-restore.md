---
title: Back Up or Restore a Capella Analytics Cluster
description: With a Cloud Snapshot cluster backup, you can backup and restore
  your entire Capella Analytics cluster with a single backup.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/backup-restore.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/analytics/admin/backup-restore.html)

# Back Up or Restore a Capella Analytics Cluster

> With a Cloud Snapshot cluster backup, you can backup and restore your entire Capella Analytics cluster with a single backup. 

Specifically, Capella uses [Amazon S3 Backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/s3-backups.html) to create a storage snapshot for your Capella Analytics S3 bucket.

## [](#backup-types)Backup Types

A Capella Analytics cluster backup is a backup of the Capella Analytics S3 bucket, using your Cloud Service Provider’s (CSP’s) backup service.

Each Capella Analytics cluster backup stands on its own as a full, complete backup of your cluster’s storage. You can restore or delete a backup independently - each cluster backup does not depend on other backups to be restored.

Your CSP’s backup service, which is the underlying backup mechanism for Capella Analytics, takes incremental storage snapshots for any backup after your first cluster backup. Even though the incrementality of your backups is determined by your CSP, each of your backups can still be restored or deleted independently through Capella Analytics. When you delete a cluster backup or it expires, your CSP manages the deletion so that only the data that’s no longer needed to restore another backup is removed.

The incrementality of your backups, or how much data has changed between each of your backups, is determined by your CSP’s backup service. Your backup size and backup retention policies determine your backup costs. Couchbase Capella bases your billing for your cluster backups on the backup storage usage reports from your CSP.

You can take [on-demand cluster backups](#on-demand). You can also choose to [schedule cluster backups](#schedule).

## [](#prerequisites)Prerequisites

To take, manage, and restore backups for your Capella Analytics cluster:

* You must have the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role in your organization, or the [Project Owner](../../cloud/projects/project-roles.md#project-owner-role) role for the project that contains your cluster.

## [](#on-demand)Take an On-Demand Cluster Backup

To take an on-demand backup on your Capella Analytics cluster:

1. On the **Capella Analytics** page, select the cluster you want to back up.
2. Go to **Backup** **Capella Analytics Snapshots**.
3. Click **Take Backup Now**.
4. In the **Backup Retention** list, choose how long to keep your cluster backup.  
The default retention period for a cluster backup is 7 days.
5. Click **Start Backup**.

For more information about how to restore a cluster backup, see [Restore a Cluster Backup](#restore).

## [](#schedule)Schedule Cluster Backups

To create a schedule for cluster backups on your Capella cluster:

1. On the **Capella Analytics** page, select the cluster you want to back up.
2. Go to **Backup** **Capella Analytics Snapshots**.
3. Click **Set Backup Schedule** or **Edit Backup Schedule**.
4. Enter the time you want your cluster backups to start.
5. Choose how frequently Capella should take a cluster backup, and how long scheduled backups should be retained on your cluster.  
By default, Capella takes Cloud Snapshots backups every 4 hours and keeps them for 7 days.
6. (Optional) If you change your backup retention while editing your schedule, choose whether Capella should apply the new retention to existing scheduled cluster backups.
7. Click **Set Backup Schedule** or **Save Backup Schedule**.

### [](#next-steps)Next Steps

If you set a schedule for your cluster backups, Capella starts your schedule at the time you specified in UTC. Using your Cloud Service Provider’s snapshot service, Capella takes a backup of your cluster at the interval set in the schedule.

If you want to stop taking cluster backups on a schedule, click **Delete Schedule**.

You can change your cluster backup schedule at any time.

Capella Analytics displays an estimate of the number of backups you’ll have on your cluster, based on the frequency and retention period set in your schedule.

For more information about how to restore a cluster backup, see [Restore a Cluster Backup](#restore).

## [](#restore)Restore a Cluster Backup

You can restore a cluster backup in a disaster recovery situation to restore your cluster to a previous point in time.

You can only restore cluster backups to the same cluster with an identical configuration to the time of the cluster backup.

Before Capella restores a cluster backup, all existing data on the destination cluster is destroyed. [Allowed IP addresses](ip-allowed-list.md) are removed and must be added again manually after your restore completes. [Access control users](auth/auth-data.md) are not included in restore operations. The existing users on the cluster are not removed or changed during a restore. If you delete a [link](#sources/database-objects.adoc) before restoring a backup, you have to edit the restored link after the restore operation is complete.

You cannot use your cluster while you’re restoring a cluster backup. Restore operations can take time to complete. The time it takes to restore your cluster is not considered to be downtime based on the [Capella Cloud Service Availability agreement](https://www.couchbase.com/capellasla/).

To restore a backup to a cluster:

1. On the **Capella Analytics** page, select the cluster where you want to restore a backup.
2. Go to **Backup** **Capella Analytics Snapshots**.
3. In the list of cluster backups, find the backup you want to restore.
4. Go to **More Options (⋮)** **Restore**.  
> [!CAUTION]  
> Restoring a cluster backup also deletes all allowed IP addresses on your cluster.  
>  
> Before you restore a cluster backup, use version 4 of the Management API to [get a list of all available allowed IP addresses](../management-api-reference/index.md#tag/Allowed-CIDRs-%28Analytics-Cluster%29/operation/listColumnarAllowedCidrs) on your cluster.  
>  
> You can use the list to recreate your allowed IP address list later.
5. Confirm that you want to restore the cluster backup.
6. Click **Restore**.

### [](#export-to-google-cloud-storage-gcs)Export to Google Cloud Storage (GCS)

Capella Analytics allows you to export the data into Google Cloud Storage. This can serve as a backup of your database in Capella Analytics, and the exported database can be loaded back to Capella Analytics in case the original database are corrupted/deleted.

### [](#next-steps-2)Next Steps

Capella starts the restore process for your cluster backup on your current cluster. Your cluster will be unavailable until the restore completes, and this can take some time.

You can view the details and status for all your cluster backup restores on the **Capella Analytics Snapshot Restores** page.

> [!NOTE]
> The **Size** of the cluster used size at the time of your backup is only an estimate. Capella calculates the cluster size information for a backup at the start of the backup process, based on the current size of your cluster. The actual size of a restored cluster may be different from this initial estimate.