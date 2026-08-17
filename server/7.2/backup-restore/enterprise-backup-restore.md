---
title: cbbackupmgr
description: <code>cbbackupmgr</code> is a tool for managing the backup and
  restore of Couchbase-Server data.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/backup-restore/pages/enterprise-backup-restore.adoc
  xref: xref:7.2@server:backup-restore:enterprise-backup-restore.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/backup-restore/enterprise-backup-restore.html)

# cbbackupmgr

> `cbbackupmgr` is a tool for managing the backup and restore of Couchbase-Server data. 

## [](#understanding-cbbackupmgr)Understanding cbbackupmgr

The `cbbackupmgr` tool backs up and restores data, scripts, configurations, and more. It allows large data sets to be managed with extremely high performance. Use of AWS S3 storage is supported.

Only Full Administrators can use `cbbackupmgr`; which is available for both Couchbase Server _Enterprise Edition_ and Couchbase Server _Community Edition_.

> [!NOTE]
> `cbbackupmgr` is _not_ backward compatible with backups created by means of `cbbackup`.
> 
> In Couchbase Enterprise Server 7.2 and after, `cbbackupmgr` is available in the `Tools` package that must be downloaded. See [Server Tools Packages](../cli/cli-intro.md#server-tools-packages).

### [](#planning-for-disaster-recovery)Planning for Disaster Recovery

Backup and restore capabilities are critical to an overall Disaster Recovery Plan, and ensuring thereby business continuity. Administrators are therefore recommended to define plans for both [Recovery Time Objective](https://en.wikipedia.org/wiki/Recovery%5Ftime%5Fobjective) (RTO) and [Recovery Point Objective](https://en.wikipedia.org/wiki/Recovery%5Fpoint%5Fobjective) (RPO), and make use of `cbbackupmgr` correspondingly.

### [](#backup-repositories)Backup Repositories

All backup is stored in and recovered from a _Backup Repository_. In turn, a _Backup Repository_ is stored in a Backup Archive on the filesystem. Each backup job in the _Backup Repository_ stores its backup in two ways:

* All bucket data is stored in a small, secondary database.
* All bucket creation scripts and configuration files are stored on the file system, as files.

### [](#tool-locations)Tool Locations

The `cbbackupmgr` tool is installed, with all other tools, in the following _per platform_ locations:

__Table 1\. Backup Tool Locations__
| Operating system | Directory locations                                                                            |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| Linux            | _/opt/couchbase/bin/cbbackupmgr_                                                               |
| Windows          | _C:\\Program Files\\Couchbase\\Server\\bin\\cbbackupmgr_ Assumes default installation location |
| Mac OS X         | _/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/cbbackupmgr_         |

## [](#how-the-backup-and-restore-tool-works)How the Backup and Restore Tool Works

By default, the `cbbackupmgr` tool performs incremental backups to back up only the new data. However, on a new cluster and for the first time, this tool generates a full backup. Each of the subsequent, incremental backups take a fraction of the time taken by the full backup.

## [](#archive-repository)Archive Repository

The backup archive is a directory that contains a set of backup repositories as well as logs for the backup client. The backup directory should be modified only by the backup client, and any modifications that are not done by that client might result in a corruption of backup data.

Only one backup client can access the backup archive at one time. If multiple instances of the backup client are running on the same archive at the same time, this might result in corruption. To prevent such corruption instances, you may be required to create multiple backup archives depending on your use case.

## [](#version-compatibility)Version Compatibility

For 6.5 and all later versions, `cbbackupmgr` can be used to back up data either from a cluster running its own version, or from a cluster running a prior, _compatible_ version. For example, the 6.6.0 tool can back up data from a cluster running 6.6.0, 6.5.x, 6.0.x, or 5.5.x. It can also be used to restore _to_ any of those versions data previously backed up _from_ any of those versions.

The following table lists the compatible cluster-versions for each version of `cbbackupmgr`. Unless otherwise specified, backup and restore apply both to _local_ and to _cloud_ data.

__Table 2\. Compatibility Requirements for Backup and Restore__
| **cbbackupmgr version** | **7.2** | **7.1** | **7.0** | **6.6** | **6.5.x** | **6.0.x** | **5.5.x** | **5.0.x** |
| ----------------------- | ------- | ------- | ------- | ------- | --------- | --------- | --------- | --------- |
| 7.2                     | ✓       | ✓       | ✓       | ✓       |           |           |           |           |
| 7.1                     |         | ✓       | ✓       | ✓       | ✓\*       |           |           |           |
| 7.0                     |         |         | ✓       | ✓       | ✓\*       | ✓\*       |           |           |
| 6.6.0 and above         |         |         |         | ✓       | ✓\*       | ✓\*       | ✓\*       |           |
| 6.5                     |         |         |         |         | ✓         | ✓         | ✓         |           |
| 6.0.x                   |         |         |         |         |           | ✓         |           |           |
| 5.5.x                   |         |         |         |         |           |           | ✓         |           |
| 5.0.x                   |         |         |         |         |           |           |           | ✓         |

\* For local backup only — _not_ for cloud.