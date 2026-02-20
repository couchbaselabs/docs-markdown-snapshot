---
title: cbbackupmgr info
description: Return information about the backup archive
editUrl: https://github.com/couchbase/backup/edit/morpheus/docs/modules/backup-restore/pages/cbbackupmgr-info.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:backup-restore:cbbackupmgr-info.adoc[]
---

[View original HTML](/server/current/backup-restore/cbbackupmgr-info.html)

# cbbackupmgr info

Return information about the backup archive

## [](#synopsis)SYNOPSIS

cbbackupmgr info [--archive <archive_dir>] [--repo <repo_name>]
                 [--backup <bucket_list>]
                 [--collection-string <collection_string>]
                 [--json] [--all] [--depth <depth>]
                 [--obj-access-key-id <access_key_id>]
                 [--obj-cacert <cert_path>] [--obj-endpoint <endpoint>]
                 [--obj-no-ssl-verify] [--obj-region <region>]
                 [--obj-staging-dir <staging_dir>]
                 [--obj-secret-access-key <secret_access_key>]
                 [--s3-force-path-style] [--s3-log-level <level>]

## [](#description)DESCRIPTION

This command provides information about the given path, be it the whole archive, repository, backup or bucket. The information can be displayed in a tabular format or JSON. By default only two levels of the data hierarchy will be displayed in tabular format, to see it all use the `--all` flag. For the exact format of the output please see the examples below.

## [](#options)OPTIONS

Below are the required and optional parameters for the info command.

### [](#required)Required

\-a,--archive <archive\_dir>

The location of the backup archive to display information about. When using info against an archive stored in S3 you must prefix the archive path with `s3://${BUCKET_NAME}/`.

### [](#optional)Optional

\-r,--repo <repo\_name>

If specified, the info command will only display information for this backup repository.

\--backup <backup>

If specified, the info command will only display information for this backup. The `--repo` flag must also be specified if this flag is used.

\--collection-string <collection\_string>

A dot separated collection string representing the bucket/scope/collection to get info for. The `--backup` flag must be provided if this flag is used.

\--start <start>

Only backups which fall between the range specified by `--start` and `--end`will be included in the output. `--start` and `--end` must be supplied together and are only valid when getting info for a repository. See [START AND END](#START%5FAND%5FEND) for information on what values are accepted.

\--end <end>

Only backups which fall between the range specified by `--start` and `--end`will be included in the output. `--start` and `--end` must be supplied together and are only valid when getting info for a repository. See [START AND END](#START%5FAND%5FEND) for information on what values are accepted.

\--json

If specified the output will be a json object.

\--all

Show all levels of the data hierarchy. Note that for json output all levels are always returned. This flag will override any value supplied to `--depth`.

\--depth <depth>

Show `depth` layers of additional information when printing non json output to stdout. By default two layers of information will be displayed. Accepts any non-zero positive integer.

### [](#cloud-integration)Cloud integration

Native cloud integration is an Enterprise Edition feature which was introduced in Couchbase Server 6.6.0.

Multiple cloud providers are supported, see the list below for more information.

1. Supported

  * AWS S3 (`s3://`)
  * GCP Google Storage (`gs://`)
  * Azure Blob Storage in 7.1.2+ (`az://`)

#### [](#required-2)Required

\--obj-staging-dir <staging\_dir>

When performing an operation on an archive which is located in the cloud such as AWS, the staging directory is used to store local meta data files. This directory can be temporary (it’s not treated as a persistent store) and is only used during the backup.

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

The info command will display information of the backup archive in a user friendly manner. Let’s imagine we have a backup archive `/backup_archive` and we want to see information about it we would run the command:

$ cbbackupmgr info -a /backup_archive

| Archive
| -------
| Name           | UUID                                 | Size      | # Repos |
| backup_archive | b4b8f2bb-5569-47d9-80c1-00821f711761 | 111.00MiB | 2       |
|
| Repos
| -----
|
| + Repo
|   ----
|   Name   | Size     | # Backups | Encrypted | Default Retention |
|   London | 55.44MiB | 2         | false     | Not set           |
|
| + Repo
|   ----
|   Name       | Size     | # Backups | Encrypted | Default Retention |
|   Manchester | 55.56MiB | 1         | false     | Not set           |

This shows us that the archive `backup_archive` has two repositories and has a total size of 111MB. It will also provide one level more into the hierarchy and show information of the two repositories `Manchester` and `London` and we can see their respective sizes as well as the number of backups each contains.

If we wanted to get more in depth information of the repository we would provide the repository name as follows:

$ cbbackupmgr info -a ~/backup_archive -r London

| Repo
| ----
| Name   | Size     | # Backups | Encrypted | Default Retention |
| London | 55.44MiB | 2         | false     | Not set           |
|
| Backups
| -------
|
| * Backup
|   ------
|   Name                           | Size    | Type | Complete | Retention | Expiry State |
|   2019-03-15T13_19_54.826458Z    | 3.02MiB | INCR | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname              | UUID                             |
|   http://localhost:8091 | 3adac7367a4117b3a8b12bf0e7f322be |
|
|   Services
|   --------
|
|     Eventing
|     --------
|     Functions |
|     1         |
|
|     FTS
|     ---
|     Aliases |
|     2       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
| * Backup
|   ------
|   Name                           | Size     | Type | Complete | Retention | Expiry State |
|   2019-03-15T12_18_00.514284Z    | 52.42MiB | FULL | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname              | UUID                             |
|   http://localhost:8091 | 3adac7367a4117b3a8b12bf0e7f322be |
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

This gives more in depth information about each backup such as the timestamp from when it was made, the size, the type which can be either a full backup (FULL), and incremental backup (INCR) or a merge (MERGE). We can also see the address of the cluster we backed up the data from. The range column is used by merges. If the backup is a merge the range has the start timestamp the end timestamp and the number of backups that where merge in the format `start - end : count`. Event and aliases are the number of events and full text search indexes aliases that where restored. Finally the complete field indicates if the backup finished successfully or not.

It is possible to get information for an individual backup as well by using the following command:

$ cbbackupmgr info -a ~/backup_archive -r London --backup 2019-03-15T12_18_00.514284Z

| Backup
| ------
| Name                           | Size     | Type | Complete | Retention | Expiry State |
| 2019-03-15T12_18_00.514284Z    | 52.42MiB | FULL | true     | Not set   | Not expired  |
|
| Merged Range
| ------------
| Start | End | Count |
| N/A   | N/A | N/A   |
|
| Cluster
| -------
| Hostname              | UUID                             |
| http://localhost:8091 | 3adac7367a4117b3a8b12bf0e7f322be |
|
| Services
| --------
|
|   Eventing
|   --------
|   Functions |
|   1         |
|
|   FTS
|   ---
|   Aliases |
|   2       |
|
|   Query
|   -----
|   UDFs |
|   0    |
|
| Buckets
| -------
|
| - Bucket
|   ------
|   Name        | Size    |
|   beer-sample | 6.85MiB |
|
|   Services
|   --------
|
|     Data
|     ----
|     Mutations | Deletions | Size    |
|     7303      | 0         | 6.85MiB |
|
|     Views
|     -----
|     Definitions |
|     1           |
|
|     Analytics
|     ---------
|     CBAS |
|     0    |
|
|     FTS
|     ---
|     Aliases |
|     0       |
|
|     Indexing
|     --------
|     Indexes |
|     1       |
|
| - Bucket
|   ------
|   Name           | Size    |
|   gamesim-sample | 2.86MiB |
|
|   Services
|   --------
|
|     Data
|     ----
|     Mutations | Deletions | Size    |
|     586       | 0         | 2.86MiB |
|
|     Views
|     -----
|     Definitions |
|     1           |
|
|     Analytics
|     ---------
|     CBAS |
|     0    |
|
|     FTS
|     ---
|     Aliases |
|     0       |
|
|     Indexing
|     --------
|     Indexes |
|     1       |
|
| - Bucket
|   ------
|   Name          | Size     |
|   travel-sample | 42.72MiB |
|
|   Services
|   --------
|
|     Data
|     ----
|     Mutations | Deletions | Size     |
|     31591     | 0         | 42.72MiB |
|
|     Views
|     -----
|     Definitions |
|     0           |
|
|     Analytics
|     ---------
|     CBAS |
|     0    |
|
|     FTS
|     ---
|     Aliases |
|     0       |
|
|     Indexing
|     --------
|     Indexes |
|     10      |

The command above provides information about all buckets in the specific backup. This includes the size of the data in each bucket, the number of items which includes mutations and tombstones, the number of mutations and the number of deletions. For backups made with `cbbackupmgr` older than 6.5 mutations and deletions will always be 0 as this is only supported by archives made with `cbbackupmgr 6.5+`. For the buckets it will also shows the number of view, full text indexes, the number of GSIs and the number of analytics metadata records.

To see information for one bucket only we would use the `--collection-string`flag and give it the name of the bucket and this would return just the information for that bucket.

To see from one level to the last the `--all` flag must be provided this will show the information from the provided level to the bucket level. An example can be seen below:

$ cbbackupmgr info -a ~/backup_archive --all

| Archive
| -------
| Name           | UUID                                 | Size     | # Repos |
| backup_archive | b4b8f2bb-5569-47d9-80c1-00821f711761 | 55.56MiB | 1       |
|
| Repos
| -----
|
| + Repo
|   ----
|   Name       | Size     | # Backups | Encrypted | Default Retention |
|   Manchester | 55.56MiB | 1         | false     | Not set           |
|
|   Backups
|   -------
|
|  *  Backup
|     ------
|     Name                           | Size     | Type | Complete | Retention | Expiry State |
|     2019-03-15T13_52_27.18301Z     | 52.42MiB | FULL | true     | Not set   | Not expired  |
|
|     Merged Range
|     ------------
|     Start | End | Count |
|     N/A   | N/A | N/A   |
|
|     Cluster
|     -------
|     Hostname              | UUID                             |
|     http://localhost:8091 | 3adac7367a4117b3a8b12bf0e7f322be |
|
|     Services
|     --------
|
|       Eventing
|       --------
|       Functions |
|       1         |
|
|       FTS
|       ---
|       Aliases |
|       2       |
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
|       Name        | Size    |
|       beer-sample | 6.85MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size    |
|         7303      | 0         | 6.85MiB |
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
|       Name           | Size    |
|       gamesim-sample | 2.86MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size    |
|         586       | 0         | 2.86MiB |
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
|       travel-sample | 42.72MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size     |
|         31591     | 0         | 42.72MiB |
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

To display only a certain number of layers when displaying info in tabular format you may provide the `--depth` flag with a non-zero positive integer. This gives more fine grained control over what information is displayed that `--all`. Using the `--all` flag will implicitly override any value provided to `--depth`.

$ cbbackupmgr info -a ~/backup_archive --depth 1

| Archive
| -------
| Name           | UUID                                 | Size     | # Repos |
| backup_archive | b4b8f2bb-5569-47d9-80c1-00821f711761 | 55.56MiB | 1       |

The info command also allows for JSON output which can be useful for automation or users that would rather get the information in json format. The output json will have the format seen below. Note that all sizes will be in bytes and that for non-merge backups the range field will be empty.

{
  "name": NAME,
  "archive_uuid": UUID,
  "size": SIZE,
  "repos": [
    {
      "name": NAME,
      "size": SIZE,
      "count": BACKUP_COUNT,
      "backups": [
        {
          "date": DATE,
          "complete: BOOL
          "size": SIZE,
          "type": ["incr"| "full" | "merge"],
          "source": SOURCE,
          "range":[all backups date involved in the merge],
          "merged_range":[all backups date involved in the merge],
          "event": COUNT,
          "fts_alias": COUNT,
          "source_cluster_uuid": UUID,
          "retention": RETENTION,
          "expiry_state": EXPIRY_STATE,
          "buckets": [
            {
              "name": BUCKET_NAME,
              "size": SIZE,
              "items": COUNT,
              "mutations": COUNT,
              "tombstones": COUNT,
              "views_count": COUNT,
              "fts_count": COUNT,
              "analytics": COUNT
            }
          ]
        }
      ]
      "default_retention": DEFAULT_RETENTION,
    }
  ]

Note that the "range" and "merged\_range" fields contain the same data. The range field is included for backwards compatibility but is deprecated.

The info command also supports getting information about an archive which is stored directly in AWS S3\. This will download a very minimal amount of data e.g. it won’t download the whole archive.

$ cbbackupmgr info -a s3://bucket/backup_archive --all --obj-staging-dir ~/backup-archive

| Archive
| -------
| Name           | UUID                                 | Size     | # Repos |
| backup_archive | b4b8f2bb-5569-47d9-80c1-00821f711761 | 55.56MiB | 1       |
|
| Repos
| -----
|
| + Repo
|   ----
|   Name       | Size     | # Backups | Encrypted | Default Retention |
|   Manchester | 55.56MiB | 1         | false     | Not set           |
|
|   Backups
|   -------
|
|  *  Backup
|     ------
|     Name                           | Size     | Type | Complete | Retention | Expiry State |
|     2019-03-15T13_52_27.18301Z     | 52.42MiB | FULL | true     | Not set   | Not expired  |
|
|     Merged Range
|     ------------
|     Start | End | Count |
|     N/A   | N/A | N/A   |
|
|     Cluster
|     -------
|     Hostname              | UUID                             |
|     http://localhost:8091 | 3adac7367a4117b3a8b12bf0e7f322be |
|
|     Services
|     --------
|
|       Eventing
|       --------
|       Functions |
|       1         |
|
|       FTS
|       ---
|       Aliases |
|       2       |
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
|       Name        | Size    |
|       beer-sample | 6.85MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size    |
|         7303      | 0         | 6.85MiB |
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
|       Name           | Size    |
|       gamesim-sample | 2.86MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size    |
|         586       | 0         | 2.86MiB |
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
|       travel-sample | 42.72MiB |
|
|       Services
|       --------
|
|         Data
|         ----
|         Mutations | Deletions | Size     |
|         31591     | 0         | 42.72MiB |
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

The info command allows you to limit the range of backups that are included in the output. This can be used to answer a few important questions before performing a merge/restore. "Is backup X included in a merge/restore with this range?" or "When I merge/restore with this range, will it include a full backup?".

Lets tackle the question "When I merge with this range, will it include a full backup?"

$ cbbackupmgr info -a /archive -r repo

| Repo
| ----
| Name | Size     | # Backups | Encrypted | Default Retention |
| repo | 70.49MiB | 5         | false     | Not set           |
|
| Backups
| -------
|
| * Backup
|   ------
|   Name                                | Size     | Type | Complete | Retention | Expiry State |
|   2020-07-18T18_19_54.057655243+01_00 | 17.62MiB | FULL | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname               | UUID                             |
|   http://172.20.1.1:8091 | 8527d470b07095084cf45e1a772a7ba9 |
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
|     0       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
| * Backup
|   ------
|   Name                                | Size     | Type | Complete | Retention | Expiry State |
|   2020-08-18T18_20_21.319063119+01_00 | 17.62MiB | FULL | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname               | UUID                             |
|   http://172.20.1.1:8091 | 8527d470b07095084cf45e1a772a7ba9 |
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
|     0       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
| * Backup
|   ------
|   Name                                | Size     | Type | Complete | Retention | Expiry State |
|   2020-08-18T18_20_26.250684761+01_00 | 17.62MiB | FULL | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname               | UUID                             |
|   http://172.20.1.1:8091 | 8527d470b07095084cf45e1a772a7ba9 |
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
|     0       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
| * Backup
|   ------
|   Name                                | Size     | Type | Complete | Retention | Expiry State |
|   2020-08-18T18_20_30.765048405+01_00 | 17.62MiB | FULL | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname               | UUID                             |
|   http://172.20.1.1:8091 | 8527d470b07095084cf45e1a772a7ba9 |
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
|     0       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
| * Backup
|   ------
|   Name                               | Size     | Type | Complete | Retention | Expiry State |
|   2020-08-18T18_20_41.39884127+01_00 | 17.62MiB | FULL | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname               | UUID                             |
|   http://172.20.1.1:8091 | 8527d470b07095084cf45e1a772a7ba9 |
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
|     0       |
|
|     Query
|     -----
|     UDFs |
|     0    |

The above repository contains five backups in total where only the first is a full backup. We would like to merge all the backups in August and want to ensure that we will be merging a full backup.

$ cbbackupmgr info -a /archive -r repo --start 01-08-2020 --end 31-08-2020

| Repo
| ----
| Name | Size     | # Backups | Encrypted | Default Retention |
| repo | 70.49MiB | 4         | false     | Not set           |
|
| Backups
| -------
|
| * Backup
|   ------
|   Name                                | Size     | Type | Complete | Retention | Expiry State |
|   2020-08-18T18_20_21.319063119+01_00 | 17.62MiB | FULL | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname               | UUID                             |
|   http://172.20.1.1:8091 | 8527d470b07095084cf45e1a772a7ba9 |
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
|     0       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
| * Backup
|   ------
|   Name                                | Size     | Type | Complete | Retention | Expiry State |
|   2020-08-18T18_20_26.250684761+01_00 | 17.62MiB | FULL | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname               | UUID                             |
|   http://172.20.1.1:8091 | 8527d470b07095084cf45e1a772a7ba9 |
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
|     0       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
| * Backup
|   ------
|   Name                                | Size     | Type | Complete | Retention | Expiry State |
|   2020-08-18T18_20_30.765048405+01_00 | 17.62MiB | FULL | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname               | UUID                             |
|   http://172.20.1.1:8091 | 8527d470b07095084cf45e1a772a7ba9 |
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
|     0       |
|
|     Query
|     -----
|     UDFs |
|     0    |
|
| * Backup
|   ------
|   Name                               | Size     | Type | Complete | Retention | Expiry State |
|   2020-08-18T18_20_41.39884127+01_00 | 17.62MiB | FULL | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start | End | Count |
|   N/A   | N/A | N/A   |
|
|   Cluster
|   -------
|   Hostname               | UUID                             |
|   http://172.20.1.1:8091 | 8527d470b07095084cf45e1a772a7ba9 |
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
|     0       |
|
|     Query
|     -----
|     UDFs |
|     0    |

Given the output above, it’s clear that merging all the backups taken in August will not result in a merged full backup. To result in a merged full backup, we would also need to include backups taken in July.

$ cbbackupmgr merge -a /archive -r repo --start 01-07-2020 --end 31-08-2020
(1/5) Merging backup '2020-07-18T18_19_54.057655243+01_00'
Copied all data in 1.342126932s (Avg. 2.98MB/Sec)                                                   50000 items / 2.98MB
[==============================================================================================================] 100.00%
Merge bucket 'default' succeeded
Mutations merged: 50000, Mutations failed to merged: 0
Deletions merged: 0, Deletions failed to merged: 0

(2/5) Merging backup '2020-08-18T18_20_21.319063119+01_00'
Copied all data in 2.601879822s (Avg. 1.49MB/Sec)                                                   50000 items / 2.98MB
[==============================================================================================================] 100.00%
Merge bucket 'default' succeeded
Mutations merged: 50000, Mutations failed to merged: 0
Deletions merged: 0, Deletions failed to merged: 0

(3/5) Merging backup '2020-08-18T18_20_26.250684761+01_00'
Copied all data in 3.85210489s (Avg. 1016.84KB/Sec)                                                 50000 items / 2.98MB
[==============================================================================================================] 100.00%
Merge bucket 'default' succeeded
Mutations merged: 50000, Mutations failed to merged: 0
Deletions merged: 0, Deletions failed to merged: 0

(4/5) Merging backup '2020-08-18T18_20_30.765048405+01_00'
Copied all data in 5.057777071s (Avg. 610.10KB/Sec)                                                 50000 items / 2.98MB
[==============================================================================================================] 100.00%
Merge bucket 'default' succeeded
Mutations merged: 50000, Mutations failed to merged: 0
Deletions merged: 0, Deletions failed to merged: 0

(5/5) Merging backup '2020-08-18T18_20_41.39884127+01_00'
Copied all data in 6.24708519s (Avg. 508.42KB/Sec)                                                  50000 items / 2.98MB
[==============================================================================================================] 100.00%
Merge bucket 'default' succeeded
Mutations merged: 50000, Mutations failed to merged: 0
Deletions merged: 0, Deletions failed to merged: 0
Merge completed successfully

$ cbbackupmgr info -a /archive -r repo

| Repo
| ----
| Name | Size     | # Backups | Encrypted | Default Retention |
| repo | 24.11MiB | 1         | false     | Not set           |
|
| Backups
| -------
|
| * Backup
|   ------
|   Name                               | Size     | Type         | Complete | Retention | Expiry State |
|   2020-08-18T18_20_41.39884127+01_00 | 24.11MiB | MERGE - FULL | true     | Not set   | Not expired  |
|
|   Merged Range
|   ------------
|   Start               | End                 | Count |
|   2020-07-18T18_19_54 | 2020-08-18T18_20_21 | 5     |
|
|   Cluster
|   -------
|   Hostname               | UUID                             |
|   http://172.20.1.1:8091 | 8527d470b07095084cf45e1a772a7ba9 |
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
|     0       |
|
|     Query
|     -----
|     UDFs |
|     0    |

As we can clearly see, after we modified our backup range to include July, we correctly merged all five backups including the full backup. Which is indicated by the `MERGE - FULL` type for the resulting backup.

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

[cbbackupmgr-cloud](cbbackupmgr-cloud.md)

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite