---
title: cbbackupmgr cloud
description: Storing cbbackupmgr archives directly in the cloud
editUrl: https://github.com/couchbase/backup/edit/morpheus/docs/modules/backup-restore/pages/cbbackupmgr-cloud.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:backup-restore:cbbackupmgr-cloud.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/backup-restore/cbbackupmgr-cloud.html)

# cbbackupmgr cloud

Storing cbbackupmgr archives directly in the cloud

## [](#description)DESCRIPTION

A document which should give you a basic understanding of how to utilize cbbackupmgr’s Enterprise Edition feature, native cloud interactions.

## [](#tutorial)TUTORIAL

### [](#credentials)CREDENTIALS

Backing up directly to an external cloud provider will mean that we require permissions to access the given data store. Each provider has its own way of authentication; see the sections below on how to authenticate for your chosen cloud provider.

#### [](#aws)AWS

When using AWS S3, there are multiple different ways that you can supply credentials to authorize yourself to AWS S3\. Below is a list of the supported techniques:

1. When running in EC2, credentials may be obtained via the instance metadata service by setting/supplying:

  * `CB_AWS_ENABLE_EC2_METADATA=true`
  * `--obj-auth-by-instance-metadata`
2. Providing a set of environment variables including:

  * `CB_OBJSTORE_REGION`
  * `CB_OBJSTORE_ACCESS_KEY_ID`
  * `CB_OBJSTORE_SECRET_ACCESS_KEY`
3. Loading credentials from the shared config files located at:

  * `$HOME/.aws/config`
  * `$HOME/.aws/credentials`
4. Providing static config/credentials using the cli flags:

  * `--obj-access-key-id`
  * `--obj-region`
  * `--obj-secret-access-key`

Setting up cbbackupmgr to interact with AWS should be a very similar process to setting up the `aws-cli`. The steps to configure the `aws-cli` can be found at <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration>.

For more information about authenticating using the EC2 instance metadata service, please see the [CLOUD PROVIDER SPECIFIC FEATURES](#CLOUD%5FPROVIDER%5FSPECIFIC%5FFEATURES) section.

#### [](#azure-7-1-2)Azure (7.1.2+)

As with AWS, there are multiple accepted methods for authorizing against Azure. Below is a list of the supported techniques:

1. Providing static credentials using the cli flags:

  * `--obj-access-key-id`
  * `--obj-secret-access-key`
2. Providing a set of environment variables including:

  * `AZURE_STORAGE_ACCOUNT`
  * `AZURE_STORAGE_KEY`
3. Providing a connection string via an environment variable:

  * `AZURE_STORAGE_CONNECTION_STRING`
4. Obtaining a service principle token through the environment, using:

  1. Client credentials

    * `AZURE_CLIENT_ID`
    * `AZURE_TENANT_ID`
    * `AZURE_CLIENT_SECRET`
  2. A client certificate

    * `AZURE_CLIENT_ID`
    * `AZURE_TENANT_ID`
    * `AZURE_CERTIFICATE_PATH`
  3. A username/password

    * `AZURE_CLIENT_ID`
    * `AZURE_TENANT_ID`
    * `AZURE_USERNAME`
    * `AZURE_PASSWORD`
  4. A managed identity

When using Azure Active Directory to authenticate, `cbbackupmgr` may not be able to determine the storage account name and, as a consequence, the URL that it should use to connect to the Azure Blob Storage service. In this case it will return an error such as the one below.

failed to determine account name, checked '--obj-access-key-id', 'AZURE_STORAGE_ACCOUNT' and
'AZURE_STORAGE_CONNECTION_STRING'

The account name will need to be supplied by using one of the following options: - The `--obj-access-key-key` flag - The `AZURE_STORAGE_ACCOUNT` environment variable - The `AZURE_STORAGE_CONNECTION_STRING` environment variable (by specifically setting the `AccountName` key)

#### [](#gcp)GCP

As with AWS/Azure, GCP supports multiple methods of authenticating. Below is a list of the supported techniques:

1. Providing static credentials using the cli flags:

  * `--obj-access-key-id`
  * `--obj-secret-access-key`
  * `--obj-refresh-token`
2. Providing an SDK style auth file

  1. Using a static flag

    * `--obj-auth-file`
  2. Using an environment variable

    * `GOOGLE_APPLICATION_CREDENTIALS`
3. Using a "well known" credentials file

  * `$HOME/.config/gcloud/application_default_credentials.json`
4. Using the first generation app engine runtime
5. Using the metadata service when running in Google Compute Engine

### [](#STAGING%5FDIRECTORY)THE STAGING DIRECTORY

One of the most important concepts behind how backup to object store works is the staging directory. The staging directory is a location on disk where temporary data is stored during the execution of a sub-command. For a backup/restore this will be DCP metadata and storage indexes.

When creating an archive to store in a cloud provider you are required to provide a location for the `obj-staging-dir`. This is a local location where archive meta data will be stored. During a backup, files will be stored here before they are uploaded to the cloud. Note that cbbackupmgr doesn’t store any document values in the staging directory; they are streamed directly to the cloud.

Each cloud archive must have a unique staging directory i.e. they can’t be shared. cbbackupmgr will detect cases where the staging directory is being reused across archives.

Any modifications to the cloud archive (using the web-ui or cli tools) and not cbbackupmgr are not supported whilst using the same staging directory. If a cloud archive has been modified, the staging directory should be removed and recreated before using cbbackupmgr to interact with the archive again.

The staging directory is only used during operations e.g. backup/restore and can be safely deleted once an operation completes; this is because all the files will have been uploaded to the cloud.

The staging directory can become quite large during a normal backup depending on the number of documents being backed up, and the size of their keys. See the [DISK REQUIREMENTS](#DISK%5FREQUIREMENTS) section for more information about how to provision the staging directory.

If the staging directory is empty, then cbbackupmgr will repopulate it using the files from the cloud archive. Depending on the size of the archive, the network speed, and the CPU resources available, this could take a very long time. As a rule of thumb, we recommend limiting the number of backups in a repository to around 50, and periodically creating new repositories. By doing this, you can avoid excessive staging directory repopulation times in case your staging directory is deleted.

### [](#configuring-cloud-backups)CONFIGURING CLOUD BACKUPS

The first step is to create a backup archive in object store. This can be done with the `config` command and only needs to be done once. All other commands will automatically download the archive meta data in the directory provided via the `obj-staging-dir`argument prior to performing any operations; this is done regardless of whether the archive exists locally because we must ensure the archive in the staging directory is up to date. Below is an example of how you would configure an archive in AWS S3.

$ cbbackupmgr config -a s3://bucket/archive -r repo --obj-staging-dir /mnt/staging

Backup repository `repo` created successfully in archive `s3://bucket/archive`

Assuming your credentials are correct, the archive should now reside directly in the provided S3 bucket. To verify, you could use the `aws-cli` to list the contents off the bucket and they should be identical to that which would exist for a local backup.

Although it’s possible to have cbbackupmgr coexist in the same S3 bucket as other general purpose storage, we recommend using a bucket which cbbackupmgr has exclusive access too.

#### [](#azure-data-lake-storage-gen-2)Azure Data Lake Storage Gen 2

Please note that using Azure storage accounts with Data Lake Storage Gen 2 enabled (also known as "hierarchical namespace") will not work with `cbbackupmgr`and is not a supported configuration.

### [](#backing-up-a-cluster)BACKING UP A CLUSTER

Once an archive is configured performing a backup works in a similar fashion to performing a local backup. It’s important to note that when backing up directly to S3 a certain amount of disk space will be used to stage local meta data files and storage indexes. See the [THE STAGING DIRECTORY](#STAGING%5FDIRECTORY) section for more information. Below is an example of doing a backup and storing directly in AWS S3.

$ cbbackupmgr backup -a s3://bucket/archive -r repo --obj-staging-dir /mnt/staging \
  -c http://10.101.101.112:8091 -u Administrator -p password

Copied all data in 1m2.525397237s (Avg. 51.61KB/Sec)      7303 items / 3.12MB
beer-sample             [===========================================] 100.00%

Backup successfully completed
Backed up bucket "beer-sample" succeeded
Mutations backedup; 7303, Mutations failed to backup: 0
Deletions backedup: 0, Deletions failed to backup: 0

Performing incremental backups works exactly as it would if you were performing an incremental locally; simply rerun the command above and an incremental backup would be created.

When choosing the amount of threads to use it’s important to consider that when backing up to the cloud, cbbackupmgr buffers data in memory before uploading it. This means that choosing an extremely large amount of threads when using a poor internet connection could lead to a scenario where your machine runs out of memory.

To learn more about backup options see [cbbackupmgr-backup](cbbackupmgr-backup.md).

### [](#restoring-a-backup-multiple-incremental-backups)RESTORING A BACKUP / MULTIPLE INCREMENTAL BACKUPS

Once you have created a backup, restoring it works in a similar way to restoring a local backup. It’s worth noting that restoring a backup to a cluster that’s hosted outside of AWS is likely to be significantly more expensive than performing a backup (depending on the size of your dataset). See [COSTING](#COSTING) for more information.

Below is an example of restoring a backup that is store in AWS S3.

$ cbbackupmgr restore -a s3://bucket/archive -r repo --obj-staging-dir /mnt/staging \
  -c http://10.101.101.112:8091 -u Administrator -p password

(1/1) Restoring backup 2020-03-19T15_35_00.467487218Z
Copied all data in 28.048019272s (Avg. 103.21KB/Sec)     7303 items / 2.82MB
beer-sample             [==========================================] 100.00%

Restore bucket 'beer-sample' succeeded
Mutations restored: 7303, Mutations failed to restore: 0
Deletions restored: 0, Deletions failed to restore: 0
Skipped due to purge number or conflict resolution: Mutations: 0 Deletions: 0
Restore completed successfully

#### [](#DISK%5FREQUIREMENTS)DISK REQUIREMENTS

As discussed in `Staging Directory`, you will be required to provision enough disk space to store all the keys for your dataset on disk during a backup. We would recommend doing a simple calculation to determine the approximate size of the staging directory.

Using the formula below, you can calculate the approximate size of the staging directory in gigabytes:

\\$frac{text(Number of items) times (text(Average key size in bytes) + 30)}{1000^3} + frac{text(Number of backups)}{60}\\$

Note that this is a rough estimate which doesn’t account for factors such as fragmentation, however, it should be a good starting point. Using this formula and given a dataset with 50 million keys with an average size of 75 bytes, we’d expect to need to provision at least about 5GiB of disk space, not including metadata.

The second term is a rough estimate of the amount of disk space required to store the metadata for the number of backups in the repository. We assume that each backup has a minimum of 16MB of metadata, but this is a rough estimate. The size of the metadata per backup will go up as the number of backups in the repository increases.

When approximating the size of the staging directory, we don’t need to account for the size of the document values because they are never stored on disk; they are uploaded directly to object store.

#### [](#COSTING)COSTING

Before using any `cbbackupmgr` sub-commands, it’s worth ensuring that you understand the costing related to using your chosen cloud provider; often the pattern being that it’s cheap to upload/store data, but (comparatively) expensive to access/download (to the wider internet). We recommend using one of the following calculators.

AWS

<https://calculator.s3.amazonaws.com/index.html>

Azure

<https://azure.microsoft.com/en-gb/pricing/calculator>

GCP

<https://cloud.google.com/products/calculator>

##### [](#backup)BACKUP

Backing up data from outside/inside AWS S3 is cheap; this is because at the time of writing, it doesn’t cost anything to transfer data into S3 (you only pay for the storage/requests).

##### [](#restore)RESTORE

Restoring data is another matter, AWS S3 charges users for pulling data from AWS onto the internet. This means that restoring large datasets can become quite costly if your cluster is not in AWS. Before performing a restore, use info (as described below in Interrogating backups) to determine the size of your backup. You can then use this to calculate how much it will cost to restore your backup.

At the time of writing, restoring a backup to a cluster stored inside AWS S3 will not be significantly costly since AWS do not charge for the bandwidth inside AWS. No matter whether your cluster is hosted in/outside AWS it’s worth calculating the costs before performing a restore.

### [](#merging)MERGING

One of the main reasons for merging incremental backups is to save disk space. In AWS S3 space is cheap and bandwidth (to the broader internet) is expensive. This means that there isn’t a financially viable reason for merging cloud backups. For this reason merging incremental backups stored in the cloud is not supported.

Restoring will continue to support applying incremental backups in chronological order in the same fashion that it’s would when merging e.g. you will end up with the same data in your Couchbase cluster.

### [](#interrogating-backups)INTERROGATING BACKUPS

Several tools have been made available for use with archives stored directly in the cloud, currently these are:

examine

[cbbackupmgr-examine](cbbackupmgr-examine.md)

info

[cbbackupmgr-info](cbbackupmgr-info.md)

#### [](#examine)EXAMINE

Examine can be used to query whether a document with the given key exists in given collection (possibly across multiple backups), the examine tools supports directly querying the data in S3.

$ cbbackupmgr examine -a s3://bucket/archive -r repo --obj-staging-dir /mnt/staging \
 --collection-string beer-sample --key '21st_amendment_brewery_cafe'

   Key: 21st_amendment_brewery_cafe
   SeqNo: 5
   Backup: 2020-01-08T17_21_20.232087665Z
   Deleted: false
   Size: 27B (key), 29B (meta), 666B (value)
   Meta: {"flags":33554432,"cas":1578502228728479744,"revseqno":1,"datatype":1}
   Value: {"address":["563 Second Street"],"city":"San Francisco","code":"94107","country":"United States","description":"The 21st Amendment Brewery offers a variety of award winning house made brews and American grilled cuisine in a comfortable loft like setting. Join us before and after Giants baseball games in our outdoor beer garden. A great location for functions and parties in our semi-private Brewers Loft. See you soon at the 21A!","geo":{"accuracy":"ROOFTOP","lat":37.7825,"lon":-122.393},"name":"21st Amendment Brewery Cafe","phone":"1-415-369-0900","state":"California","type":"brewery","updated":"2010-10-24 13:54:07","website":"http://www.21st-amendment.com/"}

To learn more about examine options see [cbbackupmgr-examine](cbbackupmgr-examine.md).

#### [](#info)INFO

The info command can be used to query a broader archive to understand its structure and to gain an understanding of what data is backed up and where.

$ cbbackupmgr info -a s3://bucket/archive -r repo --obj-staging-dir /mnt/staging --all
| Repo
| ----
| Name | Size | # Backups | Encrypted | Default Retention |
| repo | 796B | 1         | false     | Not set           |
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
|   Buckets
|   -------
|
|  -  Bucket
|     ------
|     Name        | Size |
|     beer-sample | 790B |
|
|     Services
|     --------
|
|       Data
|       ----
|       Mutations | Deletions | Size |
|       7303      | 0         | 790B |
|
|       Views
|       -----
|       Definitions |
|       1           |
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

To learn more about info options see [cbbackupmgr-info](cbbackupmgr-info.md).

### [](#archive-locking)ARCHIVE LOCKING

It’s important that only one instance of cbbackupmgr has access to the archive at a time; this is enforced using a lockfile meaning most of the time you shouldn’t need to worry about this. However, there are some situations where cbbackupmgr may fail to ensure exclusive access to the archive:

1. Another process (on another machine, or the local machine) already has an active lockfile.
2. A stale lockfile exists which belongs to a system with a different hostname.

In cases where cbbackupmgr fails to lock an archive a few simple steps can be taken:

1. Manually ensure that nobody else is using the archive
2. If you are certain nobody else is using the archive, locate the lockfile in S3 (it has the format `lock-${UUID}.lk` and is stored in the top-level of the archive).
3. Remove the lockfile and try to continue using the archive with your own instance of cbbackupmgr.

It’s extremely important that you only manually remove the lockfile if you a certain that there isn’t another instance of cbbackupmgr using the archive. Having two instances of cbbackupmgr running against the same archive could cause data loss through overlapping key prefixes.

Below is an example of an archive which contains a lockfile from a system that crashed where the lockfile was never cleaned up.

$ aws s3 ls s3://backups --recursive
2020-04-27 09:34:10        120 archive/.backup
2020-04-27 09:34:23         34 archive/lock-14eb923b-60a7-480a-849e-8af48e47f9ea.lk
2020-04-27 09:34:10        520 archive/logs/backup-0.log
2020-04-27 09:34:10        651 archive/repo/backup-meta.json

If we attempt to use cbbackupmgr to create a backup, we should see a message similar to the one below:

$ cbbackupmgr backup -a s3://bucket/archive -r repo --obj-staging-dir /mnt/staging \
  -c 172.20.1.1:8091 -u admin -p password
Error backing up cluster: the process '{PID}' running on '{HOSTNAME}' already holds the lock

In this case, cbbackupmgr will not remove the lock automatically since it cannot safely determine whether the other process is active or not. We can use the information about which machine the other instance of cbbackupmgr is running on to check whether it is active. If this machine has crashed and that instance of cbbackupmgr is no longer using the archive, we can manually remove the lockfile.

$ aws s3 rm s3://backups/archive/lock-14eb923b-60a7-480a-849e-8af48e47f9ea.lk
delete: s3://backups/archive/lock-14eb923b-60a7-480a-849e-8af48e47f9ea.lk

If we attempt to perform the backup once again we will see that it continues successfully; in the case that the other machine failed during a backup you may be asked to purge the previous backup using the `--purge` flag before you can create a new backup:

$ cbbackupmgr backup -a s3://bucket/archive -r repo --obj-staging-dir /mnt/staging \
  -c 172.20.1.1:8091 -u admin -p password

Copied all data in 1m2.525397237s (Avg. 51.61KB/Sec)      7303 items / 3.12MB
beer-sample             [===========================================] 100.00%

Backup successfully completed
Backed up bucket "beer-sample" succeeded
Mutations backedup; 7303, Mutations failed to backup: 0
Deletions backedup: 0, Deletions failed to backup: 0

## [](#compatible-object-stores)COMPATIBLE OBJECT STORES

cbbackupmgr is tested against the cloud providers that are supported, however, in some cases it will work with compatible object stores e.g. Localstack/Scality. It’s important to note that experience may be different when interacting with compatible object stores because some have slightly different behaviors which cbbackupmgr may not explicitly handle.

### [](#aws-2)AWS

It should be possible to use cbbackupmgr with S3 compatible object stores, however, there are some things that need to be taken into consideration. First and foremost is the features that cbbackupmgr leverages. Below is a list of S3 API features that cbbackupmgr uses but not all compatible object stores support:

* ListObjectsV2 <https://docs.aws.amazon.com/AmazonS3/latest/API/API%5FListObjectsV2.html>
* MultipartUploads <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html>

It’s important that you check whether these features are implemented on your S3 compatible object store because without them cbbackupmgr will not work as expected.

AWS also has a slightly newer virtual addressing style the documentation for which can be found at <https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html>. Not all S3 compatible object stores support this style of addressing. The errors that are returned by the SDK (and therefore cbbackupmgr) in these cases are not always clear. Before raising a support ticket about cbbackupmgr not working with an S3 compatible object store you should first try using the `--s3-force-path-style` argument. This will force cbbackupmgr to use the old path style addressing. From our testing with S3 compatible object stores it’s very common for this flag to be required.

### [](#azuregcp)Azure/GCP

As with AWS S3 support, Azure/GCP should work compatible object storage solutions. You also shouldn’t need to provide any specific flags when using compatible storage solutions.

It should however, be noted that Azure/GCP will only work when the underlying compatible object storage solution implements all the required features and it should be noted that this behavior is not exhaustively validated by Couchbase.

## [](#CLOUD%5FPROVIDER%5FSPECIFIC%5FFEATURES)CLOUD PROVIDER SPECIFIC FEATURES

As stated above in the 'Compatible Object Stores' section it’s possible to use cbbackupmgr with other providers which expose an S3 compatible API. It’s important to note that some features may only be accessible to those using the AWS.

### [](#aws-3)AWS

When running cbbackupmgr in an AWS instance, it may use the EC2 instance metadata to get credentials. This is disabled by default, however, may be enabled by either supplying the `--obj-auth-by-instance-metadata` flag or setting the `CB_AWS_ENABLE_EC2_METADATA` environment variable to `true`.

For example, if we wanted to use cbbackupmgr with the EC2 instance metadata we would: . Create a role with a policy which allows S3 data manipulation (e.g. S3 Full Admin) . Attach that role to the instance .. Run `export CB_AWS_ENABLE_EC2_METADATA=true` to enable fetching EC2 instance metadata .. Add the `--obj-auth-by-instance-metadata` flag to your cbbackupmgr command. . Run cbbackupmgr as described elsewhere in this tutorial

### [](#azure-7-1-2-2)Azure (7.1.2+)

When running in an Azure VM, `cbbackupmgr` will attempt to fetch a service principle token from the environment which will be used to authenticate against blob storage. In this case, the correct RBAC permissions should be provided to allow `cbbackupmgr` access to the chosen storage account. As apposed to AWS, this behavior is enabled by default.

### [](#gcp-2)GCP

When running in Google Compute, `cbbackupmgr` will using the instance metadata server to fetch credentials which may be used to authenticate against Google Storage. As with AWS/Azure, the correct RBAC permissions should be provided to allow `cbbackupmgr` access to the given bucket. As apposed to AWS, this behavior is enabled by default.

## [](#rbac)RBAC

It’s quite common to run `cbbackupmgr` with an account with limited permissions, this section covers any cloud provider specific permissions which are required. Please note that any permissions listed in the following sections are subject to change between releases.

### [](#aws-4)AWS

The following is a list of the actions required by `cbbackupmgr` when interacting with a remote archive in AWS.

* `AbortMultipartUpload`
* `CompleteMultipartUpload`
* `CreateMultipartUpload`
* `DeleteObject`
* `DeleteObjects`
* `GetObject`
* `HeadObject`
* `ListObjectsV2`
* `ListObjects`
* `ListParts`
* `PutObject`

### [](#azure)Azure

The following are the required RBAC roles required by `cbbackupmgr` when interacting with a remote archive in Azure.

* `Storage Blob Data Owner` or `Storage Blob Data Contributor`

### [](#gcp-3)GCP

The following are the required RBAC roles required by `cbbackupmgr` when interacting with a remote archive in GCP.

* `Storage Object Admin`

## [](#see-also)SEE ALSO

[cbbackupmgr-config](cbbackupmgr-config.md), [cbbackupmgr-backup](cbbackupmgr-backup.md), [cbbackupmgr-restore](cbbackupmgr-restore.md), [cbbackupmgr-merge](cbbackupmgr-merge.md), [cbbackupmgr-examine](cbbackupmgr-examine.md) [cbbackupmgr-info](cbbackupmgr-info.md)

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite