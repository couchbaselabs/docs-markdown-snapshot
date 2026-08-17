---
title: cbbackupmgr compact
description: Compacts a backup to free disk space
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/backup/edit/neo/docs/modules/backup-restore/pages/cbbackupmgr-compact.adoc
  xref: xref:7.2@server:backup-restore:cbbackupmgr-compact.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/backup-restore/cbbackupmgr-compact.html)

# cbbackupmgr compact

Compacts a backup to free disk space

## [](#synopsis)SYNOPSIS

cbbackupmgr compact [--archive <archive_dir>] [--repo <repo_name>]
                    [--backup <backup_name>]

## [](#description)DESCRIPTION

Compacting backups created with a 6.6.0+ version of `cbbackupmgr` is no longer supported/required due to changes in the storage format which significantly reduced backup fragmentation.

Compacts a backup in a backup repository in order to free up disk space. Should be run on each backup after it completes. The amount of freed disk space is displayed when the compaction completes.

## [](#options)OPTIONS

Below are a list of parameters for the compact command.

### [](#required)Required

\-a,--archive <archive\_dir>

The location of the archive directory.

\-r,--repo <repo\_name>

The name of the backup repository where the backup to be compacted is located.

\--backup <backup\_name>

The name of the backup in the backup repository to compact or an index value which references an incremental backup to compact. Valid index values are any positive integer, "oldest", and "latest". If a positive integer is used then it should reference the index of the incremental backup to compact starting from the oldest to the most recent backup. For example, "1" corresponds to the oldest backup, "2" corresponds to the second oldest backup, and so on. Specifying "oldest" means that the index of the oldest backup should be used and specifying "latest" means the index of the most recent backup should be used.

\-t,--threads <num>

Specify the number of files to be compacted in parallel. By default it is set to 1, but it is recommended to set to match the number of CPUs in the system although it can vary depending on the available RAM.

## [](#examples)EXAMPLES

The compact command is used to compact backups in order to free disk space and should be run after each backup. Below is an example of how to run the compaction command. The /data/backup directory is used as the archive directory and the backup repository is named "example".

$ cbbackupmgr config -a /data/backup -r example

$ cbbackupmgr backup -a /data/backup -r example \
 -c 127.0.0.1:8091 -u Administrator -p password

$ cbbackupmgr compact -a /data/backup -r example \
 --backup 2016-02-12T12_45_33.329408761-08_00

Compaction succeeded, 58589184 bytes freed

## [](#discussion)DISCUSSION

The compact command can be run after a backup to reclaim any fragmented disk space in the backup data files. It should be noted however that compaction may be run during the backup itself if the fragmentation in the data file begins to grow too big. Although the compaction can run during the backup it is not guaranteed to be run once the backup has completed, hence the reason for the compact command.

## [](#environment-and-configuration-variables)ENVIRONMENT AND CONFIGURATION VARIABLES

CB\_ARCHIVE\_PATH

Specifies the path to the backup archive. If the archive path is supplied as a command line argument then this value is overridden.

## [](#files)FILES

shard-\*.fdb

The compact command will compact all shard-\*.fdb files in the backup specified by the compact command.

## [](#see-also)SEE ALSO

[cbbackupmgr-backup](cbbackupmgr-backup.md), [cbbackupmgr-info](cbbackupmgr-info.md), [cbbackupmgr-strategies](cbbackupmgr-strategies.md)

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite