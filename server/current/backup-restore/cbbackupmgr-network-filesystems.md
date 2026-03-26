---
title: cbbackupmgr network filesystems
editUrl: https://github.com/couchbase/backup/edit/morpheus/docs/modules/backup-restore/pages/cbbackupmgr-network-filesystems.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:backup-restore:cbbackupmgr-network-filesystems.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/backup-restore/cbbackupmgr-network-filesystems.html)

# cbbackupmgr network filesystems

Storing cbbackupmgr archive on centralized storage using network filesystems

## [](#description)DESCRIPTION

A document which covers some important topics related to using cbbackupmgr with common network filesystems such as NFS and CIFS/SMB.

## [](#performance)PERFORMANCE

The cbbackupmgr tool uses SQLite when storing data on disk, SQLite has a read-modify-write update pattern; this means that for each key we insert into our SQLite index we have to perform a read to the underlying storage. For local filesystems, this isn't significantly expensive because the operating systems filesystem cache is extremely likely to cache these repeated reads. This isn't always the case for network filesystems.

On the most commonly used network filesystems, these reads will not be cached meaning the underlying client must perform one or more network operations resulting in significantly higher latency than would be experienced when using a local filesystem.

SQLite usually relies on file locking which can be problematic on networked filesystems because they often do not implement it. For that reason cbbackupmgr instructs SQLite not to use file locking and it handles the locking itself at the archive level. Care should be taken to ensure that programs other than cbbackupmgr do not access the archive files whilst cbbackupmgr is running to avoid corruption.

## [](#cifssmb)CIFS/SMB

During normal operation `cbbackupmgr` will create and overwrite unix style hidden files ("dotfiles"). Depending on the version of CIFS/SMB the config option `hide dot files = no` may need to be set otherwise these operations will fail with `permission denied` errors. Please note that by default, this option will be set to `yes`. When hitting `permission denied` errors for files beginning with a `.` you should retry setting `hide dot files = no`before contacting support.

## [](#see-also)SEE ALSO

[cbbackupmgr-backup](cbbackupmgr-backup.md), [cbbackupmgr-restore](cbbackupmgr-restore.md), [cbbackupmgr-merge](cbbackupmgr-merge.md),

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite