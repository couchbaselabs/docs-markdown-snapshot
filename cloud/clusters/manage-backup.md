---
title: Manage Bucket Backups
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/manage-backup.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:cloud:clusters:manage-backup.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/manage-backup.html)

# Manage Bucket Backups

> Bucket backups contain bucket data. You can take a bucket backup on-demand or use a configurable automatic schedule. 

Use the procedures on this page to create on-demand bucket backups, schedule automatic bucket backups, and manage bucket backups. To learn more about how bucket backups work in Couchbase Capella, see [Back Up and Restore Bucket Data](backup-restore.md).

To backup an entire cluster, see [Back Up and Restore An Entire Cluster](cloud-snapshots.md).

## [](#view-and-manage-bucket-backups)View and Manage Bucket Backups

> [!IMPORTANT]
> Permissions Required
> 
> To view and manage bucket backups in the Capella UI:
> 
> * You must have the [Project Owner](../projects/project-roles.md#project-owner-role) role for the project that contains the cluster. If you have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role, you already have [Project Owner](../projects/project-roles.md#project-owner-role) access.

> [!NOTE]
> Backup options are unavailable in the UI for your free tier operational cluster. To back-up and transfer your data from your old free tier operational cluster to a new free tier or paid operational cluster, you must use the `cbbackupmgr` tool. For more information about using the `cbbackupmgr` tool, see [Backup a Free Tier Capella Operational Cluster](cli-backup-restore.md#backup-free-cluster).

### [](#accessing-bucket-backups-in-the-capella-ui)Accessing Bucket Backups in the Capella UI

You can access a cluster's bucket backups from the **Backup** page.

1. Open the **Backup** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to work with backups.

    1. Go to **Backups**.

![The cluster’s 'Backups' tab.](_images/cluster-backup-restore-tab-hosted.png) 

#### [](#backup-summary)Bucket Backup Summary

A cluster's **Backups** page shows a summary of the latest backups per bucket that exist for the cluster. You can sort the backup information by bucket name.

Each bucket includes the following information about its most recent backup:

| Field             | Description                                                                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bucket Name**   | The name of the bucket.                                                                                                                                                                                                                           |
| **Latest Backup** | The last time there was a backup of the bucket, the [backup type](backup-restore.md#bucket-backup-types), the backup size, and how long it took.                                                                                                  |
| **Items**         | The number of items in the backup.                                                                                                                                                                                                                |
| **Tombstones**    | The number of [tombstones](../../server/current/learn/buckets-memory-and-storage/storage-settings.md#tombstones), or records for removed items, in the backup. This number includes tombstones for deleted documents and any dropped collections. |
| **GSI**           | The number of [Global Secondary Indexes (GSI)](../indexes/indexing-overview.md) in the backup.                                                                                                                                                    |
| **FTS**           | The number of [Search indexes](../search/search.md) in the backup.                                                                                                                                                                                |
| **CBAS**          | The number of indexes for the [Couchbase Analytics Service (CBAS)](analytics-service/analytics-service.md) in the backup.                                                                                                                         |
| **Event**         | The number of [eventing functions](../eventing/eventing-overview.md) in the backup.                                                                                                                                                               |
| **Expires On**    | The date the backup expires and is deleted.                                                                                                                                                                                                       |

### [](#configure-automatic-backups)Configure Scheduled Bucket Backups

If you have a cluster that uses scheduled bucket backups, your bucket automatically backs up based on the chosen schedule.

Couchbase recommends that you change each bucket's Backup Schedule according to your [Recovery Time Objective](https://en.wikipedia.org/wiki/Recovery%5Ftime%5Fobjective) (RTO) and [Recovery Point Objective](https://en.wikipedia.org/wiki/Recovery%5Fpoint%5Fobjective) (RPO). For example, buckets in production clusters might require a much smaller backup window and a much longer backup retention time period than buckets in development clusters.

You can edit a bucket's backup schedule when [modifying a bucket](data-service/manage-buckets.md#edit-bucket) or from the **Backup** page for your cluster.

To change a bucket's backup schedule from the **Backup** page:

1. Open the **Backup** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to work with backups.

    1. Go to **Backups**.
2. Select the bucket you want to change.
3. Click **Edit Schedule**.
4. If it's not already selected, use the **Bucket** list to choose the bucket you want to change.  
> [!TIP]  
> Using the **Bucket** list, you can select multiple buckets to bulk edit backup schedules.
5. Choose a backup schedule for the bucket according to the relative importance of the workload and data.

  * **Do Not Backup**: Do not schedule any backups.  
  > [!WARNING]  
  > **Do Not Backup** is not recommended for production clusters. To avoid data loss, you should regularly back up a production cluster.
  * **Set Weekly Schedule**: Set a weekly incremental schedule.

    1. Choose the **Day of the week** when you want Capella to take the full backup. The default value is `Sunday`.
    2. Set the **Start at** time of day for the full backup.  
      Select a **Start at** time when your application isn't using Capella heavily unless you've chosen a cluster configuration with more capacity than you need.
    3. Use the **Incremental Every** list to set the frequency of incremental backups.  
      > [!TIP]  
      > If you change the **Start at** time, the next incremental backup might happen at a different time than you expect. Capella calculates the **Incremental Value** backward from the configured **Start at** time.  
      >  
      > For example, **Incremental Every** is `8 hours`, and the **Start at** time is 4 AM. If the current time is 9 PM, Capella takes an incremental backup at 8 PM, an eight-hour interval backward from 4 AM. If you change the **Start at** to 6 AM, you would see another incremental backup at 10 PM, two hours after the last backup. The backup occurs at this time because Capella recalculates the eight-hour backup interval back from the new 6 AM **Start at** time.
    4. Set a **Retention Time** in line with your data retention policy.  
      If you enabled **Cost Optimized Retention**, the **Retention Time** applies only to the monthly restore point.  
      Capella preserves each backup from `30 Days` to `5 Years`. After the retention time lapses, Capella schedules the backup for deletion.  
      > [!NOTE]  
      > The **Retention Time** setting applies to all future backups for a bucket. Changes to this setting do not affect previous backups.
    5. Enable or disable **Cost Optimized Retention**. When enabled, the cost optimized retention policy applies to your bucket backup. For more information, see [Cost Optimized Retention Policy](backup-restore.md#cost-optimized-retention-policy).
6. Click **Apply**.  
The first automatic backup occurs at the next increment of the **Incremental Every** value, calculated backward from the configured **Start at** time.

### [](#create-manual-backup)Create an On-Demand Bucket Backup

> [!CAUTION]
> Capella keeps on-demand bucket backups for 30 days.

An on-demand backup of a bucket is always a Full bucket backup. Capella schedules on-demand backups to start immediately.

1. Open the **Backup** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to work with backups.

    1. Go to **Backups**.
2. Select the bucket you're creating an on-demand backup for.
3. Click **Backup Now**.
4. Use the **Bucket** list to choose the buckets you want to back up.
5. Click **Backup Now**.  
There can be a slight delay while Capella schedules the bucket backup.  
The [Activity Log](monitoring/activity-log.md) lists on-demand bucket backup events. This includes when a backup was triggered, when it started, and when it finished.

The **Backup** page shows the details of a bucket's backup when it's done.

### [](#view-backup-details)View Bucket Backup Details

You can view the details of a bucket backup by inspecting it in the Capella UI.

1. Open the **Backup** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to work with backups.

    1. Go to **Backups**.  
The **Backup** page shows the details of the most recent backup for each bucket in the cluster.
2. Select the bucket with the backups you want to view.  
The bucket page lists recent backups grouped by the on-demand and scheduled backup types:  
![The ](_images/backup-all-backup-details.png)  
Each bucket backup has the date and time it was created, the [backup type](backup-restore.md#backup-types), and the expiry time. A Scheduled bucket backup also includes a number for the backup's position in the backup series.

#### [](#view-bucket-backups-by-date)View Bucket Backups by Date

A bucket's page shows backups for the current backup cycle. To view backups that belong to previous cycles:

* Use the **From Date** date picker to select the start date for the backup cycle you want to view.  
Choosing a new **From Date** automatically refreshes the page to show scheduled and on-demand bucket backups based on this new date.

### [](#delete-backup)Delete a Bucket Backup

> [!WARNING]
> Deleting a bucket backup is a permanent action.

When you delete a cluster, you also delete its bucket backups. When you delete a bucket, Capella keeps its backups until their configured retention time.

In Couchbase Capella, bucket backups are deleted as follows:

Manual deletion

You can manually delete a set of scheduled bucket backups or individual manual bucket backups. You cannot undo a bucket backup deletion.

1. Open the **Backup** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to work with backups.

    1. Go to **Backups**.
2. Select the bucket with the backups you want to delete.
3. Click **Delete** for the bucket backup you want to delete.  
If you're deleting a scheduled series of bucket backups, delete the most recent backup.
4. Confirm the bucket backup deletion request.

  1. Type `delete` into the provided field.
  2. Click **Delete Backup**.

Exceeding the retention time

If a bucket backup's age is greater than the retention time set in the [Backup Schedule](#configure-automatic-backups), Capella automatically deletes the bucket backup.

Deleting a cluster

If you [delete a cluster](delete-database.md) with bucket backups, all the backups stored in the cluster are also deleted.

## [](#download-backup)Download a Bucket Backup in the Capella UI

You can [download bucket backups](backup-restore.md#downloading-backups) from the Capella UI or using wget.

### [](#prerequisites)Prerequisites

* You must be a [Project Owner](../projects/project-roles.md#project-owner-role).
* [Enable email notifications](monitoring/alerts.md#manage-email-notifications).

### [](#procedure)Procedure

To download a bucket backup in the Capella UI:

1. From the **Backup** tab for your cluster, select a bucket.
2. Navigate to one of the following pages:

  1. Bucket Backup  
  Contains the latest and partially completed backups for a selected bucket. You cannot download a backup series (backup cycle) where all incremental bucket backups are not complete.
  2. Completed Backups  
  Contains all completed backups for a selected bucket.
3. \[Optional\] Filter by backups, a date range, or a type. For example, Scheduled or On-Demand backup types.
4. \[Optional\] Expand a backup card to view its details.
5. Click **Download** on a bucket backup.  
A dialog box is displayed.
6. Click **Proceed** to start the download file creation.
7. An email is sent to you when the downloadable bucket backup file is ready.
8. After receiving an email, from the Backup tab for your cluster, select a bucket, and click **Downloadable Backups**.  
A list of ready-to-download bucket backups is displayed.
9. Click **Copy URL** on the appropriate downloadable backup.  
You have up to 12 hours after the download file has been created to copy the Download URL. Each copy generates a unique URL. After you copy the download URL, it expires in 1 hour. You must start the download before the URL expires. After starting the download, you have at least 12 hours before the download file is removed.
10. To download the file using a browser, paste the download URL into a browser window and **Enter**.  
The .zip file containing the bucket backup is downloaded. The downloaded file is a zip of a cbbackupmgr archive.
11. Unzip the downloaded bucket backup zip archive file in an appropriate location.
12. Use the Couchbase [cbbackupmgr](../reference/command-line-tools.md#cbbackupmgr) utility to view, examine, or restore the bucket backup.

## [](#download-backup-wget)Download Using wget with the Download URL

You can download the bucket backup zip archive file using an utility like wget or curl.

To download using wget:

| Description                                                                                                 | Action                                                                    |
| ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| To use the filename set in the response-content-disposition/content-disposition option of the download URL. | wget --content-disposition "<download\_url>"                              |
| To rename the file when downloading using the download URL.                                                 | wget -O capella\_cluster\_testbucket1\_backup\_0219.zip "<download\_url>" |