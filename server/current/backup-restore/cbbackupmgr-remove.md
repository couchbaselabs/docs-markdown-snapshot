---
title: cbbackupmgr remove
description: Removes a backup repository from the backup archive
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/backup/edit/morpheus/docs/modules/backup-restore/pages/cbbackupmgr-remove.adoc
  xref: xref:server:backup-restore:cbbackupmgr-remove.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/backup-restore/cbbackupmgr-remove.html)

# cbbackupmgr remove

Removes a backup repository from the backup archive

## [](#synopsis)SYNOPSIS

cbbackupmgr remove [--archive <archive_dir>] [--repo <repo_name>]
                   [--backups <backup_range>] [--disable-safe-remove-check]
                   [--obj-access-key-id <access_key_id>]
                   [--obj-cacert <cert_path>] [--obj-endpoint <endpoint>]
                   [--obj-no-ssl-verify] [--obj-region <region>]
                   [--obj-staging-dir <staging_dir>]
                   [--obj-secret-access-key <secret_access_key>]
                   [--s3-force-path-style] [--s3-log-level <level>]

## [](#description)DESCRIPTION

Removes a backup repository from the backup archive. All contents of the specified repository will be deleted from disk.

## [](#options)OPTIONS

Below are a list of parameters for the remove command.

\-a,--archive <archive\_dir>

The location of the archive directory. If the archive is stored in S3 prefix the archive path with `s3://${BUCKET_NAME}/`.

\-r,--repo <repo\_name>

The name of the backup repository to remove.

### [](#optional)Optional

\--start <start>

The first backup to remove. See [START AND END](#START%5FAND%5FEND) for information on what values are accepted.

\--end <end>

The final backup to remove. See [START AND END](#START%5FAND%5FEND) for information on what values are accepted.

\--backups <backup\_range>

This flag will accept either a single backup directory (e.g. `--backups 2019-08-23T09_36_56.957232625Z`) a comma separated range in the same formats as `--start` and `--end`. See [START AND END](#START%5FAND%5FEND) section for more information on the accepted formats.

\--disable-safe-remove-check

By default, the remove command will not delete backups which would cause dependencies to be broken i.e. a backup cannot be deleted if an incremental backup depends on it, unless those same incremental backups are being deleted in the same command.

For example, if you have a full backup and two subsequent incremental
backups, you cannot delete the full backup without also deleting the
incremental backups, or delete the first incremental backup without also
deleting the second incremental backup.

This flag will disable that check. Use with caution.

### [](#cloud-integration)Cloud integration

Native cloud integration is an Enterprise Edition feature which was introduced in Couchbase Server 6.6.0.

Multiple cloud providers are supported, see the list below for more information.

1. Supported

  * AWS S3 (`s3://`)
  * GCP Google Storage (`gs://`)
  * Azure Blob Storage in 7.1.2+ (`az://`)

#### [](#required)Required

\--obj-staging-dir <staging\_dir>

When performing an operation on an archive which is located in the cloud such as AWS, the staging directory is used to store local meta data files. This directory can be temporary (it's not treated as a persistent store) and is only used during the backup.

> [!NOTE]
> Do not use `/tmp` as the `obj-staging-dir`.  
> See `Disk requirements` in [cbbackupmgr-cloud](cbbackupmgr-cloud.md) for more information.
> 
> Bear in mind that deleting individual directories within the staging directory is not supported; doing so may lead to abnormal behavior. If you wish to delete the staging directory, then it must be removed entirely.

#### [](#optional-2)Optional

\--obj-access-key-id <access\_key\_id>

The access key id which has access to your chosen object store. This option can be omitted when using the shared config functionality provided by your chosen object store. Can alternatively be provided using the `CB_OBJSTORE_ACCESS_KEY_ID` environment variable.

When using AWS, this option expects an access key id. See <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>for more information.

When using Azure, this option expects an account name. See <https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview#storage-account-endpoints>for more information.

When using GCP, this option expects a client id. See <https://cloud.google.com/storage/docs/authentication> for more information.

\--obj-cacert <cert\_path>

Specifies a CA certificate that will be used to verify the identity of the object store being connected to.

\--obj-endpoint <endpoint>

The host/address of your object store.

\--obj-no-ssl-verify

Skips the SSL verification phase when connecting to the object store. Specifying this flag will allow a connection using SSL encryption, but you are vulnerable to a man-in-the-middle attack.

\--obj-region <region>

The region in which your bucket/container resides. For AWS this option may be omitted when using the shared config functionality. See the AWS section of the cloud documentation for more information.

\--obj-secret-access-key <secret\_access\_key>

The secret access key which has access to you chosen object store. This option can be omitted when using the shared config functionality provided by your chosen object store. Can alternatively be provided using the `CB_OBJSTORE_SECRET_ACCESS_KEY` environment variable.

When using AWS, this option expects a secret access key. See <https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys>for more information.

When using Azure, this option expects an account key. See <https://docs.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal>for more information.

When using GCP, this option expects a client secret. See <https://cloud.google.com/storage/docs/authentication> for more information.

\--obj-log-level <level>

Set the log level for the cloud providers SDK. By default logging will be disabled. Valid options are cloud provider specific and are listed below.

The valid options for the AWS SDK are `debug`, `debug-with-signing`, `debug-with-body`, `debug-with-request-retries`, `debug-with-request-errors`, and `debug-with-event-stream-body`.

The valid options for the Azure SDK are `info`, `debug`, `debug-with-request-retries` and `debug-with-request-retries-and-lro`.

The Google Storage SDK does not expose advanced logging configuration meaning this option is explicitly ignored, however, this behavior may change in the future.

\--obj-auth-by-instance-metadata

Depending on the cloud provider, using instance metadata for authentication is disabled by default. Supplying this flag will allow the fetching credentials/auth tokens from (VM) internal instance metadata endpoints.

By default, this option is disabled for AWS.

By default, this option is enabled for Azure.

By default, this option is enabled for GCP.

\--obj-auth-file

GCP offers the ability to use a file which contains credentials which will be used to perform authentication. The `--obj-auth-file` flag accepts a path to an authentication file. This flag is unsupported for the AWS/Azure cloud providers.

\--obj-refresh-token

GCP requires a refresh token when using static credentials, this will be used to refresh oauth2 tokens when accessing remote storage.

#### [](#aws-s3-options)AWS S3 Options

##### [](#optional-3)Optional

\--s3-force-path-style

By default the updated virtual style paths will be used when interfacing with AWS S3\. This option will force the AWS SDK to use the alternative path style URLs which are often required by S3 compatible object stores.

## [](#START%5FAND%5FEND)START AND END

This sub-command accepts a `--start` and `--end` flag. These flags accept multiple values to allow you to flexibly operate on a range of backups.

### [](#indexes)Indexes

Indexes may be supplied to operate on a range of backups, for example `--start 1 --end 2` will include start at the first backup and will finish with the second backup. Note that the first backup is 1 and not 0 and that the `--end` flag is inclusive.

### [](#short-dates)Short Dates

Short dates may be supplied in the format `day-month-year`. For example `--start 01-08-2020 --end 31-08-2020` will operate on all the backups which were taken during August of 2020\. Note that the end date is inclusive.

When supplying short dates, you may supply `start` or `oldest` as a placeholder for the date on which the first backup in this repository was taken. The keywords `end` or `latest` may be used as a placeholder for the date last backup in the repository was taken.

### [](#backup-names)Backup Names

Backup names may be supplied as they exist on disk. For example `--start 2020-08-13T20_01_08.894226137+01_00 --end 2020-08-13T20_01_12.348300092+01_00`will cause the sub-command to operate on all the backups which inclusively fall between these two backups.

When supplying backup names, you may supply `start` or `oldest` as a placeholder for the first backup in the repository. The keywords `end` or `latest` may be used as a placeholder for the final backup in the repository.

## [](#examples)EXAMPLES

The remove command is used to remove a backup repository from disk. Below is an example of how to run the remove command. The /data/backup directory is used as the archive directory and the backup repository is named "example".

$ cbbackupmgr info --archive /data/backups --repo example --all
| Repo
| ----
| Name    | Size    | # Backups | Encrypted | Default Retention |
| example | 4.38MiB | 3         | false     | Not set           |
|
| Backups
| -------
|
| * Backup
|   ------
|   Name                             | Size    | Type | Complete | Retention | Expiry State |
|   2020-06-02T07_49_11.281004+01_00 | 1.69MiB | FULL | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname              | UUID                             |
|   http://localhost:8091 | c044f5eeb1dc16d0cd49dac29074b5f9 |
|
|   Services
|   --------
|
|     Eventing
|     --------
|     Functions |
|     0         |
|
|     FTS
|     ---
|     Aliases |
|     1       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
|   Buckets
|   -------
|
|  -  Bucket
|     ------
|     Name    | Size    |
|     example | 1.69MiB |
|
|     Services
|     --------
|
|       Data
|       ----
|       Mutations | Deletions | Size    |
|       4096      | 0         | 1.69MiB |
|
|       Views
|       -----
|       Definitions |
|       0           |
|
|       Analytics
|       ---------
|       CBAS |
|       0    |
|
|       FTS
|       ---
|       Aliases |
|       0       |
|
|       Indexing
|       --------
|       Indexes |
|       0       |
|
| * Backup
|   ------
|   Name                             | Size    | Type | Complete | Retention | Expiry State |
|   2020-06-03T07_49_52.577901+01_00 | 1.34MiB | INCR | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname              | UUID                             |
|   http://localhost:8091 | c044f5eeb1dc16d0cd49dac29074b5f9 |
|
|   Services
|   --------
|
|     Eventing
|     --------
|     Functions |
|     0         |
|
|     FTS
|     ---
|     Aliases |
|     1       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
|   Buckets
|   -------
|
|  -  Bucket
|     ------
|     Name    | Size    |
|     example | 1.34MiB |
|
|     Services
|     --------
|
|       Data
|       ----
|       Mutations | Deletions | Size    |
|       2048      | 0         | 1.34MiB |
|
|       Views
|       -----
|       Definitions |
|       0           |
|
|       Analytics
|       ---------
|       CBAS |
|       0    |
|
|       FTS
|       ---
|       Aliases |
|       0       |
|
|       Indexing
|       --------
|       Indexes |
|       0       |
|
| * Backup
|   ------
|   Name                             | Size    | Type | Complete | Retention | Expiry State |
|   2020-06-04T07_50_06.908787+01_00 | 1.34MiB | INCR | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname              | UUID                             |
|   http://localhost:8091 | c044f5eeb1dc16d0cd49dac29074b5f9 |
|
|   Services
|   --------
|
|     Eventing
|     --------
|     Functions |
|     0         |
|
|     FTS
|     ---
|     Aliases |
|     1       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
|   Buckets
|   -------
|
|  -  Bucket
|     ------
|     Name    | Size    |
|     example | 1.34MiB |
|
|     Services
|     --------
|
|       Data
|       ----
|       Mutations | Deletions | Size    |
|       2048      | 0         | 1.34MiB |
|
|       Views
|       -----
|       Definitions |
|       0           |
|
|       Analytics
|       ---------
|       CBAS |
|       0    |
|
|       FTS
|       ---
|       Aliases |
|       0       |
|
|       Indexing
|       --------
|       Indexes |
|       0       |

$ cbbackupmgr remove -a /data/backup -r example
Backup repository `example` deleted successfully from archive `/tmp/backup`

$ cbbackupmgr info -a ~/data/backups --all
| Archive
| -------
| Name    | UUID                                 | Size | # Repos |
| backups | 0db3337c-96b0-4b3a-a7fb-bbfd53790e5f | 0B   | 0       |

The remove command can also be used to remove backups from inside a repository given the following archive:

$ cbbackupmgr info -a /data/backup -r example
| Repo
| ----
| Name    | Size     | # Backups | Encrypted | Default Retention |
| example | 36.01MiB | 4         | false     | Not set           |
|
| Backups
| -------
|
| * Backup
|   ------
|   Name                             | Size     | Type | Complete | Retention | Expiry State |
|   2019-09-18T11_13_58.136188+01_00 | 12.00MiB | FULL | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname              | UUID                             |
|   http://localhost:8091 | c044f5eeb1dc16d0cd49dac29074b5f9 |
|
|   Services
|   --------
|
|     Eventing
|     --------
|     Functions |
|     0         |
|
|     FTS
|     ---
|     Aliases |
|     1       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
| * Backup
|   ------
|   Name                             | Size     | Type | Complete | Retention | Expiry State |
|   2019-09-19T11_14_29.026324+01_00 | 12.00MiB | INCR | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname              | UUID                             |
|   http://localhost:8091 | c044f5eeb1dc16d0cd49dac29074b5f9 |
|
|   Services
|   --------
|
|     Eventing
|     --------
|     Functions |
|     0         |
|
|     FTS
|     ---
|     Aliases |
|     1       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
| * Backup
|   ------
|   Name                             | Size     | Type | Complete | Retention | Expiry State |
|   2019-09-19T11_14_40.410627+01_00 | 12.00MiB | INCR | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname              | UUID                             |
|   http://localhost:8091 | c044f5eeb1dc16d0cd49dac29074b5f9 |
|
|   Services
|   --------
|
|     Eventing
|     --------
|     Functions |
|     0         |
|
|     FTS
|     ---
|     Aliases |
|     1       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
| * Backup
|   ------
|   Name                             | Size     | Type | Complete | Retention | Expiry State |
|   2019-09-20T11_14_43.410627+01_00 | 12.00MiB | INCR | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname              | UUID                             |
|   http://localhost:8091 | c044f5eeb1dc16d0cd49dac29074b5f9 |
|
|   Services
|   --------
|
|     Eventing
|     --------
|     Functions |
|     0         |
|
|     FTS
|     ---
|     Aliases |
|     1       |
|
|     Query
|     -----
|     UDFs |
|     0    |

We can delete the first two backups using indices range such as 1,2:

$ cbbackupmgr remove -a ~/backup_repo -r example --backups 1,2
Backup `2019-09-18T11_13_58.136188+01_00` deleted successfully from archive `/Users/carlosbetancourt/backup_repo` repository `example`
Backup `2019-09-19T11_14_29.026324+01_00` deleted successfully from archive `/Users/carlosbetancourt/backup_repo` repository `example`
All backups in range `1,2` were deleted

To delete only backup `2019-09-19T11_14_29.026324+01_0` we can do as follows:

$ cbbackupmgr remove -a ~/backup_repo -r example --backups 2019-09-19T11_14_29.026324+01_0
Backup `2019-09-19T11_14_29.026324+01_00` deleted successfully from archive `/Users/carlosbetancourt/backup_repo` repository `example`

To delete backups between the 18-09-2019 and 19-09-2019 we can do as follows:

$ cbbackupmgr remove -a ~/backup_repo -r example --backups 18-09-2019,19-09-2019
Backup `2019-09-18T11_13_58.136188+01_00` deleted successfully from archive `/Users/carlosbetancourt/backup_repo` repository `example`
Backup `2019-09-19T11_14_29.026324+01_00` deleted successfully from archive `/Users/carlosbetancourt/backup_repo` repository `example`
Backup `2019-09-19T11_14_40.410627+01_00` deleted successfully from archive `/Users/carlosbetancourt/backup_repo` repository `example`
Backup `2019-09-19T11_14_29.026324+01_00` deleted successfully from archive `/Users/carlosbetancourt/backup_repo` repository `example`
All backups in range `18-09-2019,18-09-2019` were deleted

Finally, we can also provide exact backup archive name ranges such as 2019-09-18T11\_13\_58.136188+01\_00,2019-09-19T11\_14\_29.026324+01\_00.

$ cbbackupmgr remove -a ~/backup_repo -r example --backups 2019-09-18T11_13_58.136188+01_00,2019-09-19T11_14_29.026324+01_00
Backup `2019-09-18T11_13_58.136188+01_00` deleted successfully from archive `/Users/carlosbetancourt/backup_repo` repository `example`
Backup `2019-09-19T11_14_29.026324+01_00` deleted successfully from archive `/Users/carlosbetancourt/backup_repo` repository `example`
All backups in range `2019-09-18T11_13_58.136188+01_00,2019-09-19T11_14_29.026324+01_00` were deleted

Removing data that is stored in AWS S3 is very similar to removing a local repository/backup, below is an example command which remove a given backup:

$ cbbackupmgr remove -a s3://storage/backup_archive -r backup_repo --obj-staging-dir ~/backup-archive --backups '2020-04-22T14_10_18.372643628+01_00'
Backup `2020-04-22T14_10_18.372643628+01_00` deleted successfully from archive `backup_archive` repository `backup_repo`

## [](#discussion)DISCUSSION

The remove command is used to safely remove a backup repository from an archive. This command is provided because only the cbbackupmgr utility should ever be used to access or modify a backup archive. Removing a backup repository will remove data permanently from disk. Data is not recoverable once it has been removed.

## [](#environment-and-configuration-variables)ENVIRONMENT AND CONFIGURATION VARIABLES

CB\_ARCHIVE\_PATH

Specifies the path to the backup archive. If the archive path is supplied as a command line argument then this value is overridden.

CB\_OBJSTORE\_STAGING\_DIRECTORY

Specifies the path to the staging directory. If the `--obj-staging-dir`argument is provided in the command line then this value is overridden.

CB\_OBJSTORE\_REGION

Specifies the object store region. If the `--obj-region` argument is provided in the command line then this value is overridden.

CB\_OBJSTORE\_ACCESS\_KEY\_ID

Specifies the object store access key id. If the `--obj-access-key-id`argument is provided in the command line this value is overridden.

CB\_OBJSTORE\_SECRET\_ACCESS\_KEY

Specifies the object store secret access key. If the `--obj-secret-access-key` argument is provided in the command line this value is overridden.

CB\_OBJSTORE\_REFRESH\_TOKEN

Specifies the refresh token to use. If the `--obj-refresh-token` argument is provided in the command line, this value is overridden.

CB\_AWS\_ENABLE\_EC2\_METADATA

By default cbbackupmgr will disable fetching EC2 instance metadata. Setting this environment variable to true will allow the AWS SDK to fetch metadata from the EC2 instance endpoint.

## [](#see-also)SEE ALSO

[cbbackupmgr-config](cbbackupmgr-config.md), [cbbackupmgr-info](cbbackupmgr-info.md), [cbbackupmgr-strategies](cbbackupmgr-strategies.md)

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite