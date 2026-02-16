[View original HTML](/cloud/clusters/backup-restore.html)

> Couchbase recommends a robust scheduled backup and retention time policy as part of an overall disaster recovery plan for production data. 

Couchbase Capella supports on-demand and scheduled backups of bucket data. For backing up all data on a cluster, see [Back Up and Restore An Entire Cluster](cloud-snapshots.md).

## [](#weekly-bucket-backup-schedule)Weekly Bucket Backup Schedule

All buckets can have a **Set Weekly Schedule** for [backing up](manage-backup.md#configure-automatic-backups). You can choose an incremental backup interval from several available hourly options. Alternatively, you can choose not to back up your buckets.

To schedule a backup for all data on your cluster, use [cluster backups](cloud-snapshots.md). If you want to back up data from a cluster and restore it to a different cluster, you must use bucket backups.

## [](#daily-bucket-backup-schedule-deprecated)Daily Bucket Backup Schedule (Deprecated)

From January 2023, the **Set Daily Schedule** bucket backup setting has been deprecated for new Capella users and clusters. You cannot set a daily schedule for bucket backups on new clusters deployed with Couchbase Capella.

**Set Daily Schedule** is still supported indefinitely if you’re a current Capella user who already uses a daily bucket backup schedule on a pre-existing cluster.

## [](#backups-and-cluster-onoff)Backups and Cluster On/Off

Keep the following in mind when scheduling or running backups on your cluster while using scheduled or on-demand on/off operations:

* If you have [scheduled your cluster to turn off](off-on-schedule.md) and there is a pending or active backup or restore, Capella waits for the backup or restore to complete before turning off the cluster.
* If you try to [turn your cluster off on-demand](off-on-database.md) and there is a pending or active backup or restore, Capella returns an error and the cluster does not turn off.

|  | Scheduled backups do not run when your cluster is turned off. Make sure your cluster is on if you want to run a cluster backup on a schedule. For more information about turning a cluster on or off, see [Turn Clusters Off or On](off-on-database.md) or [Schedule Cluster On or Off](off-on-schedule.md). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#per-bucket-backups)Per-Bucket Backups

Capella supports scheduled and on-demand bucket backups on a per-bucket basis. You can schedule backups for each bucket during [bucket creation](data-service/manage-buckets.md#add-bucket) and [modify](manage-backup.md#configure-automatic-backups) the schedule at any time as needed. You can also create [on-demand backups](manage-backup.md#create-manual-backup) as needed.

Couchbase Capella uses its own backup utility. When a bucket backup or restore job begins, Capella starts a separate compute instance that is dedicated to running the backup utility. As the bucket backup utility runs in a separate instance, the impact to your cluster performance is minimized. When a job finishes, the instance running the backup utility is decommissioned.

What’s not included in a bucket backup:

| Type                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Point-in-time Snapshot of Cluster | Capella does not support point-in-time snapshots of cluster data. While the data in a bucket backup is per-item consistent, the consistency across items is not guaranteed. The backup utility tries to provide a strong consistency window, but this is not always possible. For example, if your cluster is under resource pressure or there are network issues, consistency cannot be guaranteed across items. In most cases, the consistency window for a bucket backup will be within a few seconds. The state of one item does not infer the state of another item. |
| Cluster Settings                  | For example, nodes, replication, networking, or cluster access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## [](#bucket-backup-types)Bucket Backup Types

Couchbase Capella supports Full bucket backups and Incremental bucket backups. Every Scheduled bucket backup includes both backup types.

Bucket backup types are described as follows:

| Type               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Full Backup        | Full bucket backups provide the best restore performance but take the most time to complete, require the most storage, and can be demanding on cluster resources. A Full bucket backup includes all bucket data from the time the backup was created and can amount to about 40% of the size of the original dataset. Full backups are taken automatically at the start of every [Scheduled](#series-backup) backup series. You can also create Full bucket backups [on demand](manage-backup.md#create-manual-backup). |
| Incremental Backup | Capella creates an Incremental bucket backup during every [Scheduled](#series-backup) backup series. Incremental backups include the data that has changed since the last Scheduled backup. They take less time and storage space to create than a Full backup. Incremental bucket backups depend on Full bucket backups to be restored. The Full backup is always restored first, followed by the incremental backups.                                                                                                 |
| Scheduled Backup   | Every Scheduled backup series starts with a Full bucket backup. Every subsequent bucket backup during the set retention time period uses an Incremental bucket backup. Scheduled backups reflect all the bucket data present when Capella automatically created the last Incremental backup in the series. By using both Full and Incremental backups, the Scheduled backups provide the best compromise between performance and required storage.                                                                      |

## [](#cost-optimized-retention-policy)Cost Optimized Retention Policy

You can select a cost-optimized retention policy to manage bucket backups, and provide a trade-off between total cost of ownership (TCO) and the recovery point objective (RPO). RPO is the maximum acceptable amount of data loss after an unplanned data-loss incident, expressed as time. The frequency of bucket backups with incremental intervals that are retained across a timeframe impacts RPO.

A cost-optimized retention policy enables you to save money at the expense of RPO. For example, where the retention of bucket backups might be more costly than running the cluster itself. For the cost-optimized retention policy, the retention time is applied only to the monthly restore point, keeping all other bucket backups for four weeks. This policy enables restoring from any backup within the last four weeks. Beyond this time, Capella retains only the monthly restore point.

|  | Your backups will continue to expire when your cluster is turned off. Download backups you want to keep before turning off your cluster, or do not turn your cluster off past the expiration dates of your existing backups. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Weekly full backup scheduled cycles expire as follows:

* Each weekly cycle expires after four weeks.
* The last backup cycle of each monthly period expires at your **Retention Time** setting. Therefore, only the last backup cycle of each monthly period is retained for the retention time you select in the **Set Weekly Schedule**.

|  | For example, suppose you start bucket backups at mid-calendar month, on March 15\. The last backup cycle of the monthly period is in the week of April 15th, and not in the last week of March. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

|  | For **Set Weekly Schedule**, a cycle is the weekly full bucket backup and the incremental bucket backups following it for that week. When the week ends, a new cycle starts. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

You are able to restore:

* From any bucket backup within the last four weeks, which has been backed up incrementally every so many hours, as per your preference.
* The final backup cycle from the monthly period, from your chosen retention time.

RPO intervals and retention time periods are as follows:

| RPO Interval | Retention Time Period                                    |
| ------------ | -------------------------------------------------------- |
| Hourly       | 4 Weeks                                                  |
| Daily        | 4 Weeks                                                  |
| Weekly       | 4 Weeks                                                  |
| Monthly      | User-chosen retention time period \[30 days to 5 years\] |

|  | Only the monthly restore point (RPO) is retained for the user-chosen time retention period. Others are retained for 30 days. |
|  | ---------------------------------------------------------------------------------------------------------------------------- |

## [](#bucket-backup-retention)Bucket Backup Retention

Capella retains a bucket’s scheduled backups based on the **Retention Time** setting in the bucket’s [Backup Schedule](manage-backup.md#configure-automatic-backups). Retention time is from 30 days to five years. After the retention time lapses, Capella schedules the bucket backup for deletion.

|  | The **Retention Time** setting applies to all future backups for a bucket. Changes to this setting do not affect previous backups. |
|  | ---------------------------------------------------------------------------------------------------------------------------------- |

Capella retains on-demand bucket backups for 30 days.

Backups continue to expire if a cluster is turned off. Download backups you want to keep before turning off your cluster, or do not turn your cluster off past the expiration dates of your existing backups.

## [](#downloading-backups)Downloading Bucket Backups

You can download on-demand bucket backups or completed cycles of scheduled bucket backups for storage or use outside Couchbase Capella. The request to create a download file is done in Capella. When the download file is ready, you are notified by email to copy the download URL from the Downloadable Backups in Capella.

|  | You can’t download a bucket backup that’s over 5 TB. |
|  | ---------------------------------------------------- |

You can use the download URL to download the zip archive file using a browser or a utility like [wget](manage-backup.md#download-backup-wget).

Downloadable bucket backups are supported for [AWS](../reference/aws.md), [GCP](../reference/gcp.md), and [Microsoft Azure](../reference/azure.md) cloud providers.

A backup cycle is a Couchbase Capella concept. A cycle is a full bucket backup, and any incremental backups that come after it in a scheduled bucket backup. All bucket backups in a cycle are stored in the same archive repository.

### [](#request-download)Requesting a Download

You can request to create a download file for an on-demand bucket backup, or a completed series (a cycle) of scheduled weekly or daily backups. On-demand bucket backups are available to download as soon as the backup is complete. Scheduled bucket backups are available to download when the backup cycle is complete. For example, if you set a weekly schedule backup, the bucket backup is available to download after one week.

After you request a download, you are notified by email when the downloadable bucket backup file is ready for download. You can then log into your Capella account and copy the download URL from the Downloadable Backups.

You have up to 12 hours, from the time when the downloadable file is ready, to retrieve the download URL. When copied, you must start the download using the URL within 1 hour.

For more information, see [Download a Bucket Backup in the Capella UI](manage-backup.md#download-backups).

### [](#using-download)Using the Download

You can store the bucket backup download file as appropriate for your backup storage policies, or you can unzip the zip archive file and use the Couchbase Server [cbbackupmgr](../reference/command-line-tools.md#cbbackupmgr) utility. You can use this utility to view, examine, or restore the contents of the bucket backup repository.

For more information about the cbbackupmgr utility, see [cbbackupmgr](../reference/command-line-tools.md#cbbackupmgr) in [Command Line Tools](../reference/command-line-tools.md).

As noted in the documentation, if you are running cbbackupmgr commands against Couchbase Capella clusters with the cluster access credentials, there are a few cbbackupmgr disable options that must be used. These restrictions do not apply if you are running cbbackupmgr commands against your self-managed clusters, using the downloaded backup archive.

### [](#downloadable-backup-costs)Downloadable Backup Costs

As part of your Capella bucket backup storage costs, you are charged for the storage that a downloadable backup file uses. Capella stores a downloadable backup file for approximately 24 hours before automatically deleting it.

Using the download URL incurs data transfer charges.

### [](#about-zip-archive-file)About the Zip Archive File

A zip archive file is in the following format: `{cluster name}-{bucket-name}-{type of backup}-{date of backup or date range of backup}.zip`

Where: {type of backup} is scheduled or on-demand.

Examples:

| Backup Type | Format                                                                       |
| ----------- | ---------------------------------------------------------------------------- |
| On-demand   | my-cluster-travel-sample-on-demand-2023-01-01T00:00:00Z                      |
| Scheduled   | my-cluster-travel-sample-scheduled-2023-01-01T00:00:00Z-2023-01-07T20:00:00Z |

When you unzip the downloaded file, its cbbackupmgr archive name is as follows: `<path_to_current_directory>/< cbbackupmgr_archive_repository_name>`

For example:

cbbackupmgr archive name: `<path>/d77896f1-14d2-46d8-89f7-93ce6aaa6758`

cbbackupmgr archive repository name: `d77896f1-14d2-46d8-89f7-93ce6aaa6758`

After you unzip the downloaded bucket backup file (cbbackupmgr zip archive file), you can use the [cbbackupmgr info](../../server/current/backup-restore/cbbackupmgr-info.md) command to view the backups.

For example:

`cbbackupmgr info --archive <path>/d77896f1-14d2-46d8-89f7-93ce6aaa6758 --repo d77896f1-14d2-46d8-89f7-93ce6aaa6758`

### [](#checksum)Using A Downloadable Backup Checksum

The Capella UI now gives a SHA-256 checksum for your downloadable backup files. You can use this to verify your downloaded backup files.

Use an available utility from your OS to determine the SHA-256 hash of your downloaded backup and compare it to the expected value given by Capella. Get the expected SHA-256 hash by clicking **Copy SHA-256** on the **Downloadable Backups** page.

* MacOS
* Windows
* Linux

You can use the [Terminal application](https://support.apple.com/en-ca/guide/terminal/welcome/mac) to check the SHA-256 hash:

1. Using the `cd` command, navigate to the directory where you downloaded your backup `.zip` file:  
```console  
$ cd <path/to/your/backup-file.zip>  
```
2. Run the `shasum` command with the `-a 256` option, which specifies that you want to use the SHA-256 algorithm to get the SHA hash:  
```console  
$ shasum -a 256 backup-file.zip  
```  
Terminal outputs the SHA-256 hash of the file, followed by the filename.
3. (Optional) To compare your hash from the Capella UI to the SHA-256 hash from your downloaded backup, run the following command:  
```console  
$ echo "<HASH_FROM_CAPELLA_UI> backup-file.zip" | shasum -a 256 -c  
```  
Terminal checks the provided hash, `<HASH_FROM_CAPELLA_UI>`, against the computed hash for `backup-file.zip`, and tells you whether the hashes match.

You can use [PowerShell](https://learn.microsoft.com/en-us/powershell/) to check the SHA-256 hash:

1. Use the `Get-FileHash` command with the full path to your downloaded backup `.zip` file:  
```console  
$ Get-FileHash -Algorithm SHA256 -Path "C:\<path\to\your\backup-file.zip>"  
```  
PowerShell returns the SHA-256 hash of the backup file.

On most Linux distributions, you can use the `sha256sum` command to check the SHA-256 hash:

1. Open your terminal application.
2. Run the `sha256sum` command with the full path to your downloaded backup `.zip` file:  
```console  
$ sha256sum <path/to/your/backup-file.zip>  
```  
Your terminal application should return the SHA-256 hash of the backup file.

## [](#see-also)See Also

See the following pages for more information about creating, managing, and deleting bucket backups:

* [Manage Bucket Backups](manage-backup.md)
* [Restore a Bucket Backup](manage-restore.md)
* [clusters:manage-backup.adoc#delete-backup](manage-backup.md#delete-backup)