---
title: Back Up and Restore An Entire Cluster
description: With a Cloud Snapshot cluster backup, you can backup and restore an
  entire cluster and all of its buckets in a single backup.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/cloud-snapshots.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:clusters:cloud-snapshots.adoc[]
---

[View original HTML](/cloud/clusters/cloud-snapshots.html)

# Back Up and Restore An Entire Cluster

> With a Cloud Snapshot cluster backup, you can backup and restore an entire cluster and all of its buckets in a single backup. 

Specifically, Couchbase Capella uses the following snapshot services, based on your chosen cloud service provider (CSP) for your cluster:

* [Amazon EBS Snapshots](https://aws.amazon.com/ebs/snapshots/)
* [Google Cloud Provider Standard Disk Snapshots](https://cloud.google.com/compute/docs/disks/snapshots)
* [Azure Disk Backup](https://learn.microsoft.com/en-us/azure/backup/disk-backup-overview)

Data transfer costs during backup and restore operations are based on your cluster’s chosen CSP.

## [](#backup-types)Backup Types

Each Cloud Snapshot cluster backup stands on its own as a full, complete backup of your cluster’s storage. This is different from [bucket backups](backup-restore.md), which can be full or incremental. You can restore or delete a backup independently - each cluster backup does not depend on other backups to be restored.

Your CSP’s backup service, which is the underlying backup mechanism for your cluster backups, takes incremental storage snapshots for any backup after your first cluster backup. Even though the incrementality of your backups is determined by your CSP, each of your backups can still be restored or deleted independently through Capella. When you delete a cluster backup or it expires, your CSP manages the deletion so that only the data that’s no longer needed to restore another backup is removed.

The incrementality of your backups, or how much data has changed between each of your backups, is determined by your CSP’s backup service. Your backup size and backup retention policies determine your backup costs. Capella bases your billing for your cluster backups on the backup storage usage reports from your CSP.

> [!CAUTION]
> If you use Cloud Snapshot backups on an Azure cluster, Azure limits your total number of incremental backups to a maximum of 500\. After 500 snapshot backups, Azure starts using full cluster backups. If you exceed 500 snapshot backups stored on your Azure-hosted cluster, your cluster backup costs will greatly increase.

## [](#bucket-backups-and-cloud-snapshot-cluster-backups)Bucket Backups and Cloud Snapshot Cluster Backups

Similar to [bucket backups](backup-restore.md), you can take [on-demand cluster backups](take-cloud-snapshot.md#on-demand). You can also choose to [schedule cluster backups](take-cloud-snapshot.md#schedule).

Cloud Snapshots back up and restore the entire storage for your cluster. Use bucket backups to back up and restore the data in a single bucket. For example, an on-demand bucket backup can back up data from a single bucket for data migration and granular backups and restores of data.

You cannot download cluster backups. If you need to download a backup to use with [cbbackupmgr](cli-backup-restore.md), use a bucket backup.

Cluster backups do not capture **Memory Only** bucket data. Use a bucket backup to back up a **Memory Only** bucket.

Cluster backups are stored at the project level in your organization, and can be restored even after a cluster is deleted.

Cluster backups support faster end-to-end recovery of your cluster, including restoring indexes. Use cluster backups to reduce the risk of downtime during disaster recovery and restore your cluster, typically within minutes.

Cluster backups are stored within the same cloud provider and cloud region as your cluster, giving you better governance over your data and reducing performance issues related to backups.

> [!TIP]
> If your cluster has a write-heavy workload, try making the interval between your cluster backups as long as possible. This reduces your backup costs and increases the value of your individual backups.

## [](#backup-encryption)Backup Encryption

If your cluster uses customer-managed encryptions keys (CMEK) for cluster storage encryption, any cluster backups you create for that cluster use your CMEK. Otherwise, Capella uses its standard encryption for cluster backups.

You cannot choose to use CMEK for a cluster backup if your cluster is not already encrypted with a CMEK. Bucket backups still do not support CMEK.

> [!CAUTION]
> Do not delete a Key Management System (KMS) Key ID until any cluster backups using that Key ID have expired. If you delete the Key ID, your backup becomes unusable. Encryption Key IDs must be enabled and available to restore an encrypted backup to a Capella cluster.
> 
> If you delete your CMEK ID from Capella, contact Couchbase Capella Support to use your backups.
> 
> To view the CMEK ID and Key IDs currently used by your backups, use the Management API or go to **Backup** **Cluster Backups** and expand the entry for a backup.

For more information about CMEK in Capella, see [Use Customer-Managed Encryption Keys (CMEK) at Rest](../security/cmek.md).

## [](#cross-region)Cluster Backup Creation and Cross-Region Copies

When you take a cluster backup on an AWS or Azure cluster running Couchbase Server version 7.6.6 and later, you can choose to copy your backup to 2 additional regions. You can choose any region available from your cloud service provider through Capella. By choosing to copy your backup to additional regions, you can add better backup resilience and reliability to your cluster. If a problem occurs with the backup stored in the same region as your cluster, Capella can still use 1 of your cross-region copies.

During the backup process, Capella queues and processes any backup copies in the background, after processing the backup in your primary region. Capella automatically deletes backup copies when your original backup expires or when you delete your original backup.

For clusters hosted on GCP, cluster backups cannot be replicated to another region.

> [!NOTE]
> If you want to use a [customer-managed encryption key](../security/cmek.md) for an Azure cluster backup, you cannot use cross-region copies.

## [](#restoring-cluster-backups)Restoring Cluster Backups

When you restore a cluster backup, you can:

* Restore the backup to the same cluster where you took the backup.
* Restore to another compatible cluster.
* Restore the backup to a new cluster with an identical configuration.

For Couchbase Server version 7.6.6 and later, cluster backups for clusters hosted on AWS and Azure can also be replicated to 2 additional regions. Any cross-region copies of your backups can be used to restore, just like the primary backup copy stored in the same region as your cluster. Capella prioritizes the original backup from the same region as your cluster during a restore.

If you use a backup with cross-region copies to create a new cluster, Capella tries to use a backup copy from the same region as where you want to deploy your new cluster. Capella prioritizes the same region as the new cluster, even if you select a different region when choosing your restore options. This reduces your data transfer costs.

> [!NOTE]
> You can only restore a backup to a different compatible cluster if both clusters are currently running Couchbase Server version 7.6.6 or later. If a cluster is running an earlier version of Couchbase Server, you cannot restore its backups to another cluster.
> 
> For example, if you have 2 clusters, with the first cluster on Couchbase Server version 7.6.5 and the second on Couchbase Server version 7.6.6, you cannot restore a backup from the 7.6.5 cluster to the 7.6.6 cluster until you upgrade the 7.6.5 cluster.
> 
> If you do upgrade a 7.6.5 cluster to a later version of Couchbase Server, backups taken while the cluster was on version 7.6.5 can still be restored to that same cluster. Restoring a backup taken on version 7.6.5 will temporarily restore the cluster to Couchbase Server version 7.6.5\. You can run an upgrade to restore the cluster back to a later version at any point after the restore.

For cluster backups across all versions, if the number of nodes deployed in the destination cluster for a restore is different from the node configuration in your backup, Capella scales your cluster configuration up or down to the number of nodes present in the backup. Take care when restoring backups to make sure you do not lose node configuration changes.

Before Capella restores a cluster backup, all existing data on the destination cluster is destroyed. You cannot use your cluster while you’re [restoring a cluster backup](restore-cloud-snapshot.md). Restore operations can take time to complete.

The time it takes to restore your cluster is not considered to be downtime based on the [Capella Cloud Service Availability agreement](https://www.couchbase.com/capellasla/).

> [!CAUTION]
> Restoring a cluster backup also deletes all cluster access credentials and allowed IP addresses on your cluster.
> 
> Before you [restore a cluster backup](restore-cloud-snapshot.md), use version 4 of the Management API to [get a list of all available cluster access credentials](../management-api-reference/index.md#tag/Database-Credentials/operation/listDatabaseCredentials) and [get a list of all allowed IP addresses](../management-api-reference/index.md#tag/Allowed-CIDRs-%28Cluster%29/operation/listAllowedCidrs) on your cluster.
> 
> You can use the list to recreate your cluster access credentials and allowed IP addresses later.
> 
> For more information about cluster access credentials, see [Manage Cluster Access Credentials](manage-database-users.md). For more information about allowed IP addresses, see [Configure Allowed IP Addresses](allow-ip-address.md).

## [](#see-also)See Also

* [Take or Schedule a Cluster Backup](take-cloud-snapshot.md)
* [Restore a Cluster Backup](restore-cloud-snapshot.md)
* [Back Up and Restore Bucket Data](backup-restore.md)