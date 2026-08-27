---
title: Take or Schedule a Cluster Backup
description: You can take an on-demand cluster backup to back up your entire
  Couchbase Capella cluster, or schedule backups.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/take-cloud-snapshot.adoc
  xref: xref:cloud:clusters:take-cloud-snapshot.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/take-cloud-snapshot.html)

# Take or Schedule a Cluster Backup

> You can take an on-demand cluster backup to back up your entire Couchbase Capella cluster, or schedule backups. 

> [!TIP]
> If your cluster uses Couchbase Server version 7.6.6 or later and is deployed on AWS or Azure, you can choose to replicate your backups to 2 regions, other than the region where your cluster is deployed. You can restore a replicated backup like any other backup for your cluster. Cluster backups for GCP clusters cannot be replicated to additional regions.

## [](#prerequisites)Prerequisites

* You have the **Project Owner** role for the project with the cluster you want to back up. If you have the **Organization Owner** role, you have Project Owner permissions.  
For more information about roles in Capella, see [Manage Organizations and Access](../organizations/organization-projects-overview.md).

## [](#on-demand)Take an On-Demand Cluster Backup

To take an on-demand backup on your Capella cluster:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to take a backup.
3. Go to **Backup** **Cluster Backups**.
4. Click **Take Backup Now**.
5. In the **Backup Retention** list, choose how long to keep your backup on your cluster.  
The default retention period for cluster backups is 7 days.
6. (Optional) To replicate your cluster backup to up to 2 additional regions, select **Enable Cross-Region Backups**.

  1. In the **Copy to Region** list, select the specific regions where you want to replicate your cluster backup.
7. Click **Start Cluster Backup**.

> [!TIP]
> To take a cluster backup from the Capella Management API, see [Create Cloud Snapshot Backup](../management-api-reference/index.md#tag/Cloud-Snapshot-Backups-and-Restore/operation/createCloudSnapshotBackup).

## [](#schedule)Schedule Cluster Backups

To create a schedule for cluster backups on your Capella cluster:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to schedule regular backups.
3. Go to **Backup** **Cluster Backups**.
4. Click **Set Schedule** or **Edit Schedule**.
5. Enter the time you want your cluster backups to start.
6. Choose how frequently Capella should take a cluster backup, and how long scheduled backups should be retained on your cluster.  
By default, Capella shows a schedule to take cluster backups every 4 hours and keep them for 7 days.
7. (Optional) If you change your backup retention while editing your schedule, choose whether Capella should apply the new retention to existing scheduled cluster backups.
8. (Optional) To replicate your cluster backup to up to 2 additional regions, select **Enable Cross-Region Backups**.

  1. In the **Copy to Region** list, select the specific regions where you want to replicate your cluster backup.
9. Click **Set Backup Schedule** or **Save Backup Schedule**.

> [!NOTE]
> Capella displays the estimated number of cluster backups that will be taken by your schedule. Azure limits your total number of incremental backups to a maximum of 500\. After 500 incremental snapshot backups, Azure starts using full cluster backups and your cluster backup costs will greatly increase.

> [!TIP]
> To schedule cluster backups from the Capella Management API, see [Upsert Backup Schedule](../management-api-reference/index.md#tag/Cloud-Snapshot-Backups-Schedule/operation/upsertCloudSnapshotBackupSchedule).

## [](#next-steps)Next Steps

If you set a schedule for your cluster backups, Capella starts your schedule at the time you specified in UTC. Using your cloud service provider's snapshot service, Capella takes a backup of your cluster at the interval set in the schedule.

If you want to stop taking cluster backups on a schedule, click **Delete Schedule**.

You can change your cluster backup schedule at any time.

If you chose to replicate your backups to multiple regions, wait until the UI shows that your cross-region copies are available before trying to restore.

For more information about how to restore a cluster backup, see [Restore a Cluster Backup](restore-cloud-snapshot.md).