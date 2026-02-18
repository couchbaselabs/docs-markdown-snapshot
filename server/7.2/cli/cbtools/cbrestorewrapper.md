---
title: cbrestorewrapper
description: A wrapper around cbrestore that was made to improve performance for
  enterprise users. Superseded by cbbackupmgr, which should be used instead of
  this tool.
editUrl: https://github.com/couchbase/couchbase-cli/edit/neo/docs/modules/cli/pages/cbtools/cbrestorewrapper.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/cli/cbtools/cbrestorewrapper.html)

# cbrestorewrapper

(Deprecated) A wrapper around `cbrestore` that was made to improve performance for enterprise users. Superseded by `cbbackupmgr`, which should be used instead of this tool.

## [](#synopsis)SYNOPSIS

_cbrestorewrapper_ [--username <user>] [--password <password>] [--ssl]
                   [--bucket-source <name>] [--bucket-destination <name>]
                   [--add] [--from-date <start>] [--to-date <end>]
                   [--path <path>] [--port <port>] [--verbose]
                   [--extra <options>] [--help] backup_dir cluster

## [](#description)DESCRIPTION

DEPRECATION WARNING: This tool has been deprecated please use cbbackupmgr instead.

`cbrestorewrapper` invokes multiple instances of `cbrestore` to restore the directory `backup_dir` to the target cluster.

## [](#options)Options

\-u,--username <user>

Specifies the username of the user executing the command. If you do not have a user account with permission to execute the command then it will fail with an unauthorized error.

\-p,--password <password>

Specifies the password of the user executing the command. If you do not have a user account with permission to execute the command then it will fail with an unauthorized error.

\-s,--ssl

(Deprecated) Specifies that the connection should use SSL verification. If this flag is used then SSL will be used but the cluster certificate will not be verified by the Certificate Authority. This flag is deprecated and not recommended. If you wish to use SSL encryption it is recommended that you specify the cluster host name using either _couchbases://_ or _https://_. Each of these connection schemes will ensure that the connection is encrypted with SSL. You may then use either --no-ssl-verify or --cacert in order to customize how your SSL connection is set up.

\-b,--bucket-source <bucket>

Single named bucket from source cluster to transfer. If the backup directory only contains a single bucket, then that bucket is automatically used.

\-B,--bucket-destination <bucket>

Specify the bucket to restore the data to in the target cluster. If not provided it will default to match the `--bucket-source`.

\-a,--add

Used to not override the existing items in the destination.

\--from-date <start>

Restore data from the first specified backup in the format `yyyy-mm-dd`\*. By default the starting point will be the first backup.

\--to-date <end>

Restore data until the date specified as `yyyy-mm-dd`\*. By default, all data collected is restored.

\--path <path>

Specifies the path to the `cbbackup` executable. Defaults to the current directory.

\--port <port>

Specifies the bucket port. Defaults to 11210

\-v,--verbose

Verbose logging; more `-v’s` provide more verbosity. Max is `-vvv`

\-x,--extra <options>

Provide extra, uncommon configuration parameters. Comma-separated key=val pairs

## [](#extras)EXTRAS

The following are extra, specialized command options with the `cbrestorewrapper -x` parameter.

__Table 1\. cbrestorewrapper -x options__
| \-x options              | Description                                                                                                                                                                                                                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| backoff\_cap=10          | Maximum backoff time during the rebalance period.                                                                                                                                                                                                                                                          |
| batch\_max\_bytes=400000 | Transfer this # of bytes per batch.                                                                                                                                                                                                                                                                        |
| batch\_max\_size=1000    | Transfer this # of documents per batch.                                                                                                                                                                                                                                                                    |
| cbb\_max\_mb=100000      | Split backup file on destination cluster if it exceeds the MiB.                                                                                                                                                                                                                                            |
| conflict\_resolve=1      | By default, disable conflict resolution. This option doesn’t work in Couchbase Server versions 4.0 and 4.1 but will be re-implemented in version 4.1.1 and in subsequent versions.                                                                                                                         |
| data\_only=0             | For value 1, transfer only data from a backup file or cluster.                                                                                                                                                                                                                                             |
| design\_doc\_only=0      | For value 1, transfer only design documents from a backup file or cluster. Default: 0. Back up only design documents which include view and secondary index definitions from a cluster or bucket with the option design\_doc\_only=1. Restore only design documents with cbrestore -x design\_doc\_only=1. |
| max\_retry=10            | Max number of sequential retries if the transfer fails.                                                                                                                                                                                                                                                    |
| mcd\_compatible=1        | For value 0, display extended fields for stdout output.                                                                                                                                                                                                                                                    |
| nmv\_retry=1             | 0 or 1, where 1 retries transfer after a NOT\_MY\_VBUCKET message. Default: 1.                                                                                                                                                                                                                             |
| recv\_min\_bytes=4096    | Amount of bytes for every TCP/IP batch transferred.                                                                                                                                                                                                                                                        |
| rehash=0                 | For value 1, rehash the partition id’s of each item. This is required when transferring data between clusters with different number of partitions, such as when transferring data from an Mac OS X server to a non-Mac OS X cluster.                                                                       |
| report=5                 | Number batches transferred before updating progress bar in console.                                                                                                                                                                                                                                        |
| report\_full=2000        | Number batches transferred before emitting progress information in console.                                                                                                                                                                                                                                |
| seqno=0                  | By default, start at sequence number 0.                                                                                                                                                                                                                                                                    |
| try\_xwm=1               | Transfer documents with metadata. Default: 1\. Value of 0 is only used when transferring from 1.8.x to 1.8.x.                                                                                                                                                                                              |
| uncompress=0             | For value 1, restore data in uncompressed mode. This option is unsupported. To create backups with compression, use cbbackupmgr, which is available for Couchbase Server Enterprise Edition only. See [Backup](../../backup-restore/enterprise-backup-restore.md).                                         |

## [](#example)EXAMPLE

To perform a backup with `cbrestorewrapper` run:

$ cbrestorewrapper ~/backups http://10.112.193.101:8091\
  -u Administrator -p password