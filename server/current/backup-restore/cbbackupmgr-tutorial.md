---
title: cbbackupmgr tutorial
description: A quick guide to using cbbackupmgr
editUrl: https://github.com/couchbase/backup/edit/morpheus/docs/modules/backup-restore/pages/cbbackupmgr-tutorial.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:backup-restore:cbbackupmgr-tutorial.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/backup-restore/cbbackupmgr-tutorial.html)

# cbbackupmgr tutorial

A quick guide to using cbbackupmgr

## [](#description)DESCRIPTION

A tutorial that goes gives examples of how to use all of the commands in cbbackupmgr effectively.

## [](#tutorial)TUTORIAL

In this tutorial we will show how to take backups and restore data using cbbackupmgr. This tutorial uses a cluster that contains both the travel-sample and beer-sample buckets installed and requires modifying some of the documents in the travel-sample bucket. To make it easier to set up a cluster and edit/get documents the following scripts are provided at <http://github.com/couchbaselabs/backup-tutorial>. You can then find scripts corresponding to your version of Couchbase. We will reference other scripts in this github repository later in the tutorial so it is recommended that you download these scripts. The only requirement for running the scripts is that you have curl installed. To automatically setup the cluster in the appropriate state required for this tutorial download and install Couchbase and then run the 01-initialize.sh script. If you do not want to use this script then you can navigate through the Couchbase setup process and initialize the cluster with all available services and install the travel-sample and beer-sample sample data bucket.

Using this cluster we will show how the incremental/merge approach taken by cbbackupmgr reduces time and overhead on your cluster.

### [](#configuring-a-backup)Configuring a Backup

Before getting started with cbbackupmgr we must first decide the directory where to store all of our backups. This directory is referred to as the backup archive. The backup archive contains one or more backup repositories. These backup repositories are where your backups will be contained. The easiest way to think of a backup repository is that it corresponds directly to a single cluster that you want to back up. The backup repository also contains a configuration for how to back that cluster up. A backup repository is created by using the config subcommand. In this tutorial we will use a backup archive located at /data/backup. The backup archive is automatically created if the directory specified is empty. Below is an example of how to create a backup repository called "cluster" which will backup all data and index definitions from all buckets in the target cluster.

$ cbbackupmgr config -a /data/backup -r cluster

Backup repository `cluster` created successfully in archive `/data/backup`

One of the most important aspects of backup repository creation is that we can configure that backup repository in many different ways to change the way backups in each backup repository are taken. Let's say we want a separate backup of only the index definitions in the travel-sample bucket. To do this we can create a separate backup repository called "single".

$ cbbackupmgr config -a /data/backup -r single \
  --include-data travel-sample --disable-data

Backup repository `single` created successfully in archive `/data/backup`

The config subcommand provides many options in order to customize how you backup your data. See the [cbbackupmgr-config](cbbackupmgr-config.md) page for more information about what options are available and how they are used.

### [](#backing-up-a-cluster)Backing up a Cluster

Now that we have created some backup repositories we should take a look at our backup archive to see what it looks like. The easiest way to do this is to use the info subcommand. This subcommand is used to retrieve information form a backup archive. It will return the size as well as information about the repositories, backups and item counts.

$ cbbackupmgr info -a /data/backup --all
| Archive
| -------
| Name        | UUID                                 | Size | # Repos |
| backup_repo | 32c97d5f-821a-4284-840b-9ee7cf8733a3 | 0B   | 2       |
|
| Repos
| -----
|
| + Repo
|   ----
|   Name    | Size | # Backups | Encrypted | Default Retention |
|   cluster | 0B   | 0         | false     | Not set           |
|
| + Repo
|   ----
|   Name   | Size | # Backups | Encrypted | Default Retention |
|   single | 0B   | 0         | false     | Not set           |

The info subcommand gives us a directory print out of all of the backup repositories and backups in the backup archive. Since there are no backups yet we can just see our archives information in the output of this command. There is also information about how much disk space each repository contains. More information about the info subcommand can be found in the [cbbackupmgr-info](cbbackupmgr-info.md) page.

Now that we have our backup repositories configured it's time to start taking backups. Since the backup repository contains all of the configuration information for how the backup should be taken we just need to specify the backup repository name and the information for the target cluster we intend to back up. Below is an example of how to take a backup on the "cluster" backup repository. We will assume that we have our cluster running on localhost.

$ cbbackupmgr backup -c 127.0.0.1 -u Administrator -p password -a /data/backup -r cluster
Backing up to 2020-03-25T08_08_11.770436Z
Copied all data in 33.02s (Avg. 759.44KB/Sec)  38894 items / 24.47MB
beer-sample             [===================================] 100.00%
travel-sample           [===================================] 100.00%

Backup successfully completed
Backed up bucket "beer-sample" succeeded
Mutations backed up: 7303, Mutations failed to backup: 0
Deletions backed up: 0, Deletions failed to backup: 0
Backed up bucket "travel-sample" succeeded
Mutations backed up: 31591, Mutations failed to backup: 0
Deletions backed up: 0, Deletions failed to backup: 0

When the backup command is executed it will by default print out a progress bar which is helpful for understanding how long your backup will take to complete and the rate of data movement. While the backup is running the progress bar will give an estimated time to completion, but this will change to average backup rate when the backup finishes. Information is also provided on the total data and items already backed up and the current rate of data movement. If the backup completes successfully you will see the "Backup completed successfully" message and a break down of mutations and deletions backed up per bucket.

Let's also run the backup on the "single" backup repository to see how the two backup runs differ.

$ cbbackupmgr backup -a /data/backup -r single \
  -c couchbase://127.0.0.1 -u Administrator -p password

Backing up to 2020-03-25T08_08_58.903046Z
Copied all data in 1s (Avg. 480B/Sec)                 0 items / 480B
travel-sample           [==================================] 100.00%
Backup successfully completed
Backed up bucket "travel-sample" succeeded
Mutations backed up: 0, Mutations failed to backup: 0
Deletions backed up: 0, Deletions failed to backup: 0

Since the "single" backup repository is only configured to back up index definitions for the travel-sample bucket we do not see a progress bar for the beer-sample bucket. We can also see that the backup executed quicker since there was much less data to actually back up.

Since we now have backups in our backup archive let's take a look at the state of our backup archive has changed by using the info subcommand.

$ cbbackupmgr info -a /data/backup --all
| Archive
| -------
| Name        | UUID                                 | Size | # Repos |
| backup_repo | 32c97d5f-821a-4284-840b-9ee7cf8733a3 | 0B   | 2       |
|
| Repos
| -----
|
| + Repo
|   ----
|   Name    | Size     | # Backups | Encrypted | Default Retention |
|   cluster | 54.33MiB | 1         | false     | Not set           |
|
|   Backups
|   -------
|
|  *  Backup
|     ------
|     Name                        | Size     | Type | Complete | Retention | Expiry State |
|     2020-03-25T08_08_11.770436Z | 54.33MiB | FULL | true     | Not set   | Not expired  |
|
|     Merged Range
|     ------------
|     Start | End | Count |
|     N/A   | N/A | N/A   |
|
|     Cluster
|     -------
|     Hostname              | UUID                             |
|     http://127.0.0.1:8091 | ffa8024f899ca6acc7c59cf0f541dbdd |
|
|     Services
|     --------
|
|       Eventing
|       --------
|       Functions |
|       0         |
|
|       FTS
|       ---
|       Aliases |
|       0       |
|
|       Query
|       -----
|       UDFs |
|       0    |
|
|     Buckets
|     -------
|
|   -   Bucket
|       ------
|       Name        | Size     |
|       beer-sample | 18.43MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size     |
|         7303      | 0         | 18.43MiB |
|
|         Views
|         -----
|         Definitions |
|         1           |
|
|         Analytics
|         ---------
|         CBAS |
|         0    |
|
|         FTS
|         ---
|         Aliases |
|         0       |
|
|         Indexing
|         --------
|         Indexes |
|         1       |
|
|   -   Bucket
|       ------
|       Name          | Size     |
|       travel-sample | 35.91MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size     |
|         31591     | 0         | 35.91MiB |
|
|         Views
|         -----
|         Definitions |
|         0           |
|
|         Analytics
|         ---------
|         CBAS |
|         0    |
|
|         FTS
|         ---
|         Aliases |
|         0       |
|
|         Indexing
|         --------
|         Indexes |
|         10      |
|
| + Repo
|   ----
|   Name   | Size     | # Backups | Encrypted | Default Retention |
|   single | 16.20KiB | 1         | false     | Not set           |
|
|   Backups
|   -------
|
|  *  Backup
|     ------
|     Name                        | Size     | Type | Complete | Retention | Expiry State |
|     2020-03-25T08_08_58.903046Z | 16.20KiB | FULL | true     | Not set   | Not expired  |
|
|     Merged Range
|     ------------
|     Start | End | Count |
|     N/A   | N/A | N/A   |
|
|     Cluster
|     -------
|     Hostname              | UUID                             |
|     http://127.0.0.1:8091 | ffa8024f899ca6acc7c59cf0f541dbdd |
|
|     Services
|     --------
|
|       Eventing
|       --------
|       Functions |
|       0         |
|
|       FTS
|       ---
|       Aliases |
|       0       |
|
|       Query
|       -----
|       UDFs |
|       0    |
|
|     Buckets
|     -------
|
|   -   Bucket
|       ------
|       Name          | Size     |
|       travel-sample | 16.20KiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size     |
|         0         | 0         | 16.20KiB |
|
|         Views
|         -----
|         Definitions |
|         0           |
|
|         Analytics
|         ---------
|         CBAS |
|         0    |
|
|         FTS
|         ---
|         Aliases |
|         0       |
|
|         Indexing
|         --------
|         Indexes |
|         10      |

Now that we have some backups defined the output of the info subcommand is much more useful. We can see that our "cluster" backup repository contains one backup with a name corresponding to the time the backup was taken. That backup also contains two buckets and we can see the number of views, indexes, mutations, tombstones and more in the bucket. The "single" backup repository also contains one backup, but this backup only contains the travel-sample bucket and contains 0 data items but we can see it has 10 indexes. Note that the info command also supports JSON output if that is preferable. See [cbbackupmgr-info](cbbackupmgr-info.md) page.

One of the most important features of cbbackupmgr is that it is an incremental-only backup utility. This means that once we have backed up some data we will never need to back it up again. In order to simulate some changes on the cluster we can run the 02-modify.sh script from the backup-tutorial github repository mentioned at the beginning of the tutorial. If you do not have this script then you will need to modify two documents and add two new documents to the travel-sample bucket. After we have modified some data we will run the backup subcommand on the "cluster" backup repository again.

$ cbbackupmgr backup -a /data/backup -r cluster -c couchbase://127.0.0.1 -u Administrator -p password

Backing up to 2020-03-25T08_41_21.461311Z
Copied all data in 3s (Avg. 18.98KB/Sec)           4 items / 56.95KB
travel-sample           [==================================] 100.00%
beer-sample             [==================================] 100.00%

Backup successfully completed
Backed up bucket "beer-sample" succeeded
Mutations backed up: 0, Mutations failed to backup: 0
Deletions backed up: 0, Deletions failed to backup: 0
Backed up bucket "travel-sample" succeeded
Mutations backed up: 4, Mutations failed to backup: 0
Deletions backed up: 0, Deletions failed to backup: 0

In this backup notice that since we updated 2 items and created two items that this is all that we need back up during this run. If we list the backup archive using the info subcommand then we will see that the backup archive looks like something like what is below. We can see that our incremental contains 4 items all of which are mutations. Those correspond to the 2 modifications and the 2 additions.

$ cbbackupmgr info -a /data/backup --all
| Archive
| -------
| Name        | UUID                                 | Size | # Repos |
| backup_repo | 32c97d5f-821a-4284-840b-9ee7cf8733a3 | 0B   | 2       |
|
| Repos
| -----
|
| + Repo
|   ----
|   Name    | Size     | # Backups | Encrypted | Default Retention |
|   cluster | 86.37MiB | 2         | false     | Not set           |
|
|   Backups
|   -------
|
|  *  Backup
|     ------
|     Name                        | Size     | Type | Complete | Retention | Expiry State |
|     2020-03-25T08_08_11.770436Z | 54.33MiB | FULL | true     | Not set   | Not expired  |
|
|     Merged Range
|     ------------
|     Start | End | Count |
|     N/A   | N/A | N/A   |
|
|     Cluster
|     -------
|     Hostname              | UUID                             |
|     http://127.0.0.1:8091 | ffa8024f899ca6acc7c59cf0f541dbdd |
|
|     Services
|     --------
|
|       Eventing
|       --------
|       Functions |
|       0         |
|
|       FTS
|       ---
|       Aliases |
|       0       |
|
|       Query
|       -----
|       UDFs |
|       0    |
|
|     Buckets
|     -------
|
|   -   Bucket
|       ------
|       Name        | Size     |
|       beer-sample | 18.43MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size     |
|         7303      | 0         | 18.43MiB |
|
|         Views
|         -----
|         Definitions |
|         1           |
|
|         Analytics
|         ---------
|         CBAS |
|         0    |
|
|         FTS
|         ---
|         Aliases |
|         0       |
|
|         Indexing
|         --------
|         Indexes |
|         1       |
|
|   -   Bucket
|       ------
|       Name          | Size     |
|       travel-sample | 35.91MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size     |
|         31591     | 0         | 35.91MiB |
|
|         Views
|         -----
|         Definitions |
|         0           |
|
|         Analytics
|         ---------
|         CBAS |
|         0    |
|
|         FTS
|         ---
|         Aliases |
|         0       |
|
|         Indexing
|         --------
|         Indexes |
|         10      |
|
|  *  Backup
|     ------
|     Name                        | Size     | Type | Complete | Retention | Expiry State |
|     2020-03-25T08_41_21.461311Z | 32.02MiB | INCR | true     | Not set   | Not expired  |
|
|     Merged Range
|     ------------
|     Start | End | Count |
|     N/A   | N/A | N/A   |
|
|     Cluster
|     -------
|     Hostname              | UUID                             |
|     http://127.0.0.1:8091 | ffa8024f899ca6acc7c59cf0f541dbdd |
|
|     Services
|     --------
|
|       Eventing
|       --------
|       Functions |
|       0         |
|
|       FTS
|       ---
|       Aliases |
|       0       |
|
|       Query
|       -----
|       UDFs |
|       0    |
|
|     Buckets
|     -------
|
|   -   Bucket
|       ------
|       Name        | Size     |
|       beer-sample | 16.00MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size     |
|         0         | 0         | 16.00MiB |
|
|         Views
|         -----
|         Definitions |
|         1           |
|
|         Analytics
|         ---------
|         CBAS |
|         0    |
|
|         FTS
|         ---
|         Aliases |
|         0       |
|
|         Indexing
|         --------
|         Indexes |
|         1       |
|
|   -   Bucket
|       ------
|       Name          | Size     |
|       travel-sample | 16.02MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size     |
|         4         | 0         | 16.02MiB |
|
|         Views
|         -----
|         Definitions |
|         0           |
|
|         Analytics
|         ---------
|         CBAS |
|         0    |
|
|         FTS
|         ---
|         Aliases |
|         0       |
|
|         Indexing
|         --------
|         Indexes |
|         10      |
|
| + Repo
|   ----
|   Name   | Size     | # Backups | Encrypted | Default Retention |
|   single | 16.20KiB | 1         | false     | Not set           |
|
|   Backups
|   -------
|
|  *  Backup
|     ------
|     Name                        | Size     | Type | Complete | Retention | Expiry State |
|     2020-03-25T08_08_58.903046Z | 16.20KiB | FULL | true     | Not set   | Not expired  |
|
|     Merged Range
|     ------------
|     Start | End | Count |
|     N/A   | N/A | N/A   |
|
|     Cluster
|     -------
|     Hostname              | UUID                             |
|     http://127.0.0.1:8091 | ffa8024f899ca6acc7c59cf0f541dbdd |
|
|     Services
|     --------
|
|       Eventing
|       --------
|       Functions |
|       0         |
|
|       FTS
|       ---
|       Aliases |
|       0       |
|
|       Query
|       -----
|       UDFs |
|       0    |
|
|     Buckets
|     -------
|
|   -   Bucket
|       ------
|       Name          | Size     |
|       travel-sample | 16.20KiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size     |
|         0         | 0         | 16.20KiB |
|
|         Views
|         -----
|         Definitions |
|         0           |
|
|         Analytics
|         ---------
|         CBAS |
|         0    |
|
|         FTS
|         ---
|         Aliases |
|         0       |
|
|         Indexing
|         --------
|         Indexes |
|         10      |

The backup subcommand provides many options in order to customize how you backup your data. See the [cbbackupmgr-backup](cbbackupmgr-backup.md) page for more information about what options are available and how they are used.

### [](#restoring-a-backup)Restoring a Backup

Now that we have some backup data let's restore that data backup to the cluster. In order to restore data we just need to know the name of the backup that we want to restore. To find the name we can again use the info subcommand in order to see what is in our backup archive. The backup name will always be a timestamp. For example, let's say we want to restore the 2016-03-22T10\_26\_08.933579821-07\_00 from the "cluster" backup repository. In order to do this we run the command below.

$ cbbackupmgr restore -a /data/backup -r cluster \
 -c http://127.0.0.1:8091 -u Administrator -p password \
 --start 2016-03-22T14_00_16.892277632-07_00 \
 --end 2016-03-22T14_00_16.892277632-07_00 --force-updates

(1/1) Restoring backup 2016-03-22T14_00_16.892277632-07_00
Copied all data in 2s (Avg. 19.96MB/Sec)       38894 items / 39.91MB
travel-sample           [==================================] 100.00%
beer-sample             [==================================] 100.00%

Restore completed successfully

In the command above we use the --start and --end flags to specify the range of backups we want to restore. Since we are only restoring one backup we specify the same value for both --start and --end. We also added the --force-updates flag in order to skip Couchbase conflict resolution. This tells cbbackupmgr to force overwrite key-value pairs being restored even if the key-value pair on the cluster is newer and the one being restored. If we look at the two values that we updated on the cluster we will now see that they have been reverted back to what they were at the time we took the initial backup. If you used the script in the backup-tutorial github repository to update documents then you can use the 03-inspect.sh script to see the state of the updated documents after the restore.

The restore subcommand also allows for you to exclude data that was backed up from the restore and provides various other options. See the [cbbackupmgr-restore](cbbackupmgr-restore.md) page for more information on restoring data.

### [](#merging-backups)Merging backups

Using an incremental backup solution means that each backup we take increases disk space. Since disk space in not infinite we need to be able to reclaim this disk space. In order to do this we use the [cbbackupmgr-merge](cbbackupmgr-merge.md)subcommand to merge two or more backups together. Since we have two backups in the "cluster" backup repository we will merge these backups together using the command below.

$ cbbackupmgr merge -a /data/backup -r cluster \
  --start oldest --end latest

Merge completed successfully

After merging the backups together we can use the info subcommand to see the effect the merge subcommand we just ran had on the backup archive.

$ cbackupmgr info -a /data/backup --all                                                                                                                                                                                                                                                                                                                                                                                     20-03-25 - 8:52:36
| Archive
| -------
| Name        | UUID                                 | Size | # Repos |
| backup_repo | 32c97d5f-821a-4284-840b-9ee7cf8733a3 | 0B   | 2       |
|
| Repos
| -----
|
| + Repo
|   ----
|   Name    | Size     | # Backups | Encrypted | Default Retention |
|   cluster | 54.33MiB | 1         | false     | Not set           |
|
|   Backups
|   -------
|
|  *  Backup
|     ------
|     Name                        | Size     | Type         | Complete | Retention | Expiry State |
|     2020-03-25T08_41_21.461311Z | 54.33MiB | MERGE - FULL | true     | Not set   | Not expired  |
|
|     Merged Range
|     ------------
|     Start | End | Count |
|     N/A   | N/A | N/A   |
|
|     Cluster
|     -------
|     Hostname | UUID                             |
|     Merge    | ffa8024f899ca6acc7c59cf0f541dbdd |
|
|     Services
|     --------
|
|       Eventing
|       --------
|       Functions |
|       0         |
|
|       FTS
|       ---
|       Aliases |
|       0       |
|
|       Query
|       -----
|       UDFs |
|       0    |
|
|     Buckets
|     -------
|
|   -   Bucket
|       ------
|       Name        | Size     |
|       beer-sample | 18.43MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size     |
|         7303      | 0         | 18.43MiB |
|
|         Views
|         -----
|         Definitions |
|         1           |
|
|         Analytics
|         ---------
|         CBAS |
|         0    |
|
|         FTS
|         ---
|         Aliases |
|         0       |
|
|         Indexing
|         --------
|         Indexes |
|         1       |
|
|   -   Bucket
|       ------
|       Name          | Size     |
|       travel-sample | 35.91MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size     |
|         31591     | 0         | 35.91MiB |
|
|         Views
|         -----
|         Definitions |
|         0           |
|
|         Analytics
|         ---------
|         CBAS |
|         0    |
|
|         FTS
|         ---
|         Aliases |
|         0       |
|
|         Indexing
|         --------
|         Indexes |
|         10      |
|
| + Repo
|   ----
|   Name   | Size     | # Backups | Encrypted | Default Retention |
|   single | 16.20KiB | 1         | false     | Not set           |
|
|   Backups
|   -------
|
|  *  Backup
|     ------
|     Name                        | Size     | Type | Complete | Retention | Expiry State |
|     2020-03-25T08_08_58.903046Z | 16.20KiB | FULL | true     | Not set   | Not expired  |
|
|     Merged Range
|     ------------
|     Start | End | Count |
|     N/A   | N/A | N/A   |
|
|     Cluster
|     -------
|     Hostname              | UUID                             |
|     http://127.0.0.1:8091 | ffa8024f899ca6acc7c59cf0f541dbdd |
|
|     Services
|     --------
|
|       Eventing
|       --------
|       Functions |
|       0         |
|
|       FTS
|       ---
|       Aliases |
|       0       |
|
|       Query
|       -----
|       UDFs |
|       0    |
|
|     Buckets
|     -------
|
|   -   Bucket
|       ------
|       Name          | Size     |
|       travel-sample | 16.20KiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size     |
|         0         | 0         | 16.20KiB |
|
|         Views
|         -----
|         Definitions |
|         0           |
|
|         Analytics
|         ---------
|         CBAS |
|         0    |
|
|         FTS
|         ---
|         Aliases |
|         0       |
|
|         Indexing
|         --------
|         Indexes |
|         10      |

We can see from the info command that there is now a single backup in the "cluster" backup repository. This backup has a name that reflects the name of the most recent backup in the merge. It also has 31593 data items in the travel-sample bucket. This is two more items than the original backup we took because the second backup had two new items. The two items that were updated were deduplicated during the merge so they do not add extra items to the count displayed by the info subcommand.

For more information on how the merge command works as well as information on other ways the merge command can be used see the [cbbackupmgr-merge](cbbackupmgr-merge.md)page.

### [](#removing-a-backup-repository)Removing a Backup Repository

If no longer need a backup repository then we can use the remove subcommand to remove the backup repository. Below is an example showing how to remove the "cluster" backup repository.

$ cbbackupmgr remove -a /data/backup -r cluster

Backup repository `cluster` deleted successfully from archive `/data/backup`

If we now run the info subcommand you will see that the "cluster" backup repository no longer exists. For more information on the remove subcommand see the [cbbackupmgr-remove](cbbackupmgr-remove.md) page.

## [](#see-also)SEE ALSO

[cbbackupmgr-backup](cbbackupmgr-backup.md), [cbbackupmgr-config](cbbackupmgr-config.md), [cbbackupmgr-info](cbbackupmgr-info.md), [cbbackupmgr-merge](cbbackupmgr-merge.md), [cbbackupmgr-remove](cbbackupmgr-remove.md), [cbbackupmgr-restore](cbbackupmgr-restore.md), [cbbackupmgr-strategies](cbbackupmgr-strategies.md)

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite