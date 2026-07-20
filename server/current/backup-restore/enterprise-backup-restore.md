---
title: cbbackupmgr
description: <code>cbbackupmgr</code> is a tool for managing the backup and
  restore of Couchbase-Server data.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/backup-restore/pages/enterprise-backup-restore.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:server:backup-restore:enterprise-backup-restore.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/backup-restore/enterprise-backup-restore.html)

# cbbackupmgr

> `cbbackupmgr` is a tool for managing the backup and restore of Couchbase-Server data. 

## [](#understanding-cbbackupmgr)Understanding cbbackupmgr

The `cbbackupmgr` tool backs up and restores data, scripts, configurations, and more. It allows large data sets to be managed with high performance. Use of AWS S3 storage is supported.

Only Full Administrators can use `cbbackupmgr`; which is available for both Couchbase Server Enterprise Edition and Couchbase Server Community Edition.

> [!NOTE]
> `cbbackupmgr` is not backward compatible with backups created by means of `cbbackup`.
> 
> In Couchbase Enterprise Server 7.2 and later, `cbbackupmgr` is available in the `Tools` package that must be downloaded. See [Server Tools Packages](../cli/cli-intro.md#server-tools-packages).

### [](#planning-for-disaster-recovery)Planning for Disaster Recovery

Backup and restore capabilities are critical to an overall Disaster Recovery Plan and ensuring thereby business continuity. Administrators are therefore recommended to define plans for both [Recovery Time Objective](https://en.wikipedia.org/wiki/Recovery%5Ftime%5Fobjective) (RTO) and [Recovery Point Objective](https://en.wikipedia.org/wiki/Recovery%5Fpoint%5Fobjective) (RPO) and make use of `cbbackupmgr` correspondingly.

### [](#backup-repositories)Backup Repositories

All backup is stored in and recovered from a \[.term\]Backup Repository. In turn, a \[.term\]Backup Repository is stored in a Backup Archive on the filesystem. Each backup job in the \[.term\]Backup Repository stores its backup in 2 ways:

* You can store all bucket data in a small, secondary database.
* You can store all bucket creation scripts and configuration files on the filesystem, as files.

### [](#whats-backed-up)What's Backed Up

By default, backups include your database's data and metadata.

You can change what the tool backs up and restores by using arguments to the `cbbackupmgr config` command. For example, if you only want to back up your cluster's metadata, use the `--disable-data` command line flag when configuring your backup repository. You may choose to use this flag if you want to transfer settings to a new database cluster. When you use this flag, `cbbackupmgr` backs up just the following:

* analytic collections and indexes for local links and synonyms
* bucket configuration
* eventing functions
* Full-Text Search indexes and aliases
* Global Secondary Indexes
* Query SQL++ User-Defined Functions
* scopes and collections definitions (Couchbase Server version 7.6 and later)
* views

> [!NOTE]
> `cbbackupmgr` does not back up query function libraries such as user-created JavaScript libraries. You must back up these libraries separately.

Another useful flag is `--enable-users` which backs up users and user groups. Users and groups are not backed up by default. This option is useful for preventing the loss of users and groups in case of disaster.

> [!NOTE]
> Backups that include users contain the user's hashed passwords.

Other flags let you exclude specific metadata, or select a subset of data to back up. See [cbbackupmgr configuration](cbbackupmgr-config.md) for a list of the arguments you can use to control what `cbbackupmgr` backs up.

You can also use command line flags to control how the `cbbackupmgr restore` command restores data. For example, use `--overwrite-users` to have `cbbackupmgr` overwrite existing users and groups in the database if the backup contains a matching user or group. By default, `cbbackupmgr` does not overwrite existing users in the database. Instead, it restores just the users in the backup that do not exist in the database. See [cbbackupmgr restore](cbbackupmgr-restore.md) for a list of the arguments you can use to control what `cbbackupmgr` restores.

### [](#tool-locations)Tool Locations

When installed as part of the Couchbase Server installation, `cbbackupmgr` tool is stored with all other tools in the following per-platform locations:

__Table 1\. Backup Tool Locations__
| Operating system | Directory locations                                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| Linux            | _/opt/couchbase/bin/cbbackupmgr_                                                               |
| Windows          | _C:\\Program Files\\Couchbase\\Server\\bin\\cbbackupmgr_ Assumes default installation location |
| Mac OS X         | _/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/cbbackupmgr_         |

## [](#how-the-backup-and-restore-tool-works)How the Backup and Restore Tool Works

By default, the `cbbackupmgr` tool performs incremental backups to back up only the new data. However, on a new cluster and for the first time, this tool generates a full backup. Each of the subsequent, incremental backups take a fraction of the time taken by the full backup.

## [](#archive-repository)Archive Repository

The backup archive is a directory that contains a set of backup repositories as well as logs for the backup client. The backup directory should be modified only by the backup client, and any modifications that are not done by that client might result in the corruption of backup data.

Only 1 backup client can access the backup archive at 1 time. If multiple instances of the backup client are running on the same archive at the same time, this might result in corruption. To prevent such corruption instances, you may be required to create multiple backup archives depending on your use case.

## [](#version-compatibility)Version Compatibility

For 7.2 and later versions, you can use `cbbackupmgr` to back up data either from a cluster running its own version, or from a cluster running a prior, `compatible` version. You can also use it to restore data to any of these versions from backups created on any of them.

The following table lists the compatible cluster-versions for each version of `cbbackupmgr`. Unless otherwise specified, backup and restore apply both to local and to cloud data.

__Table 2\. Compatibility Requirements for Backup and Restore__
|                                            | cbbackupmgr version → |   |     |     |     |
| ------------------------------------------ | --------------------- | - | --- | --- | --- |
|                                            |                       |   | 8.0 | 7.6 | 7.2 |
| Compatible withCouchbase Server version: ↓ | 8.0                   | ✓ |     |     |     |
| 7.6                                        | ✓                     | ✓ |     |     |     |
| 7.2                                        | ✓                     | ✓ | ✓   |     |     |

## [](#restoring-metadata-and-users)Restoring Metadata and Users

* When restoring metadata to a newer Server version, if the feature that the metadata applies to no longer exists in the newer Server version, then the metadata may not be restorable.
* If the user roles no longer exist in the version that you want to restore to, then an error is logged for the target user.
* In general, if you can upgrade to the new version, then you should be able to restore the users. If you cannot upgrade directly, then restoring users may cause errors. For example, if some of the user roles no longer exist in the newer Server version.