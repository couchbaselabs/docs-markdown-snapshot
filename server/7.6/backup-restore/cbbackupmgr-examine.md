---
title: cbbackupmgr examine
description: Searches one or more backups by key for a specific document
editUrl: https://github.com/couchbase/backup/edit/trinity/docs/modules/backup-restore/pages/cbbackupmgr-examine.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:backup-restore:cbbackupmgr-examine.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/backup-restore/cbbackupmgr-examine.html)

# cbbackupmgr examine

Searches one or more backups by key for a specific document

## [](#synopsis)SYNOPSIS

cbbackupmgr examine [--archive <archive_dir>] [--repo <repo_name>]
                    [--collection-string <collection_string>] [--key <key>]
                    [--start start] [--end end] [--search-partial-backups]
                    [--json] [--no-meta] [--no-xattrs] [--no-value]
                    [--hex-meta] [--hex-xattrs] [--hex-value]
                    [--obj-access-key-id <access_key_id>]
                    [--obj-cacert <cert_path>] [--obj-endpoint <endpoint>]
                    [--obj-no-ssl-verify] [--obj-region <region>]
                    [--obj-staging-dir <staging_dir>]
                    [--obj-secret-access-key <secret_access_key>]
                    [--s3-force-path-style] [--s3-log-level <level>]
                    [--passphrase <passphrase>] [--km-key-url <url>]
                    [--km-endpoint <endpoint>] [--km-region <region>]
                    [--km-access-key-id <id>] [--km-secret-access-key <key>]
                    [--km-auth-file <path>] [--point-in-time <time>]

## [](#description)DESCRIPTION

Examine is an Enterprise Edition command used to find information about a given key. Examine will produce a timeline highlighting events related to the key during the backups e.g. first appearance, mutation and deletion.

You may optionally use the `--start` and `--end` flags to limit the range of backups for which an event timeline is produced. See [START AND END](#START%5FAND%5FEND) for more information.

Examine also supports outputting the event timeline in multiple formats, including being able to hexdump/include/omit portions of a document.

## [](#options)OPTIONS

Below is a list of parameters for the examine command.

### [](#required)Required

\-a,--archive <archive\_dir>

The archive directory to examine. When using examine against an archive stored in S3 prefix the archive path with `s3://${BUCKET_NAME}/`

\-r,--repository <repo\_name>

The name of the backup repository to examine.

\--collection-string <collection\_string>

A dot separated collection string representing the bucket/collection which contains the key you are trying to examine. When interacting with a collection unaware backup the collection string must only contain a bucket e.g. `--collection-string default`. When interacting with a collection aware backup the collection string must contain the path to a collection e.g. `--collection-string default.scope.collection`. Note that you may omit the scope/collection for collection aware backups which only contain the `_default` scope and collection e.g. `--collection-string default` is internally translated to `--collection-string default._default._default`. For more information see `COLLECTION AWARE BACKUPS` in [cbbackupmgr-backup](cbbackupmgr-backup.md).

\-k,--key

The name of the key you are trying to find.

### [](#optional)Optional

\--start <start>

The first backup to examine. See [START AND END](#START%5FAND%5FEND) for information on what values are accepted.

\--end <end>

The final backup to examine. See [START AND END](#START%5FAND%5FEND) for information on what values are accepted.

\--search-partial-backups

By default examine will skip backups which are incomplete. This flag may be supplied to attempt to search incomplete backups, however, the resulting search may fail, or not find the key you’re looking for.

\-j,--json

Return any output as a JSON structure.

\--no-meta

Do not return any of the documents metadata. Mutually exclusive with the `--hex-meta` flag.

\--no-xattrs

Do not return any of the documents extended attributes. Mutually exclusive with the `--hex-xattrs` flag.

\--no-value

Do not return the documents value. Mutually exclusive with the `--hex-value`flag.

\--hex-meta

Return the metadata encoded in hex. Mutually exclusive with the `--no-meta`flag.

\--hex-xattrs

Return the extended attributes encoded in hex. Mutually exclusive with the `--no-xattrs` flag.

\--hex-value

Return the value encoded in hex. Mutually exclusive with the `--no-value`flag.

\--point-in-time <time>

(Beta) Only examine documents up to the given point in time. The value accepted is ISO8601 date time format (YYYY-MM-DDTHH:MM:SS). This feature is currently in Beta and is not supported, this should only be used in test environments.

### [](#cloud-integration)Cloud integration

Native cloud integration is an Enterprise Edition feature which was introduced in Couchbase Server 6.6.0.

Multiple cloud providers are supported, see the list below for more information.

1. Supported

  * AWS S3 (`s3://`)
  * GCP Google Storage (`gs://`)
  * Azure Blob Storage in 7.1.2+ (`az://`)

#### [](#required-2)Required

\--obj-staging-dir <staging\_dir>

When performing an operation on an archive which is located in the cloud such as AWS, the staging directory is used to store local meta data files. This directory can be temporary (it’s not treated as a persistent store) and is only used during the backup. NOTE: Do not use `/tmp` as the `obj-staging-dir`. See `Disk requirements` in [cbbackupmgr-cloud](cbbackupmgr-cloud.md) for more information.

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

### [](#encryption)Encryption

\--passphrase <passphrase>

Passphrase can be used instead of an external key manager. This is not supported on production and should only be used in development or testing.

\--km-key-url <url>

Provides the Key Identifier in the external Key Management system. Currently supported KMSs are AWS KMS, GCP KMS, Azure KeyVault, HashiCorp Vault Transit secrets engine. The option can also be provided using the environmental variable `CB_KM_KEY_URL`. For more on how to authenticate using the different providers see [cbbackupmgr-encryption](cbbackupmgr-encryption.md).

For AWS the expected key format is `awskms://<KEY-ID|KEY-ALIAS>`, for example `awskms://alias/keyAlias`.

For GCP the expected key format is `gcpkms://<KEY-RESOURCE-ID>`, for example `gcpkms://projects/project-id/locations/location/keyRings/keyring/cryptoKeys/key`.

For Azure key vault the expected key format is `azurekeyvault://<KEY-IDENTIFIER>`for example: `azurekeyvault://vault-name.vault.azure.net/object-type/object-name/object-version`.

For HashiCorp Vault the expected format is `hashivaults://<HOST>/<KEY-NAME>`for example: `hashivaults://127.0.0.1:8200/keyName`.

\--km-region <region>

Required when using AWS KMS, it allows you to set the key region.

\--km-endpoint <endpoint>

The host or address to use as your KMS. It will override the default SDK one.

\--km-access-key-id <id>

The user ID used to connect to the key management service. It can also be provided via `CB_KM_ACCESS_KEY_ID` environmental variable. Please refer to [cbbackupmgr-encryption](cbbackupmgr-encryption.md) for the required authentication for each provider.

\--km-secret-access-key <key>

The key used to connect to the key management service. It can also be provided via the `CB_KM_SECRET_ACCESS_KEY` environmental variable. Please refer to [cbbackupmgr-encryption](cbbackupmgr-encryption.md) for the required authentication for each provider.

\--km-tenant-id <id>

The tenant ID used to connect to the key management service. It can also be provided via the `CB_KM_TENANT_ID` environmental variable. This argument is only required when doing access key authentication with Azure. Please refer to [cbbackupmgr-encryption](cbbackupmgr-encryption.md) for the required authentication for each provider.

\--km-auth-file <path>

The path to a file containing the authentication credentials for the key management service. It can also be provided via the `CB_KM_AUTH_FILE`environmental variable. Please refer to [cbbackupmgr-encryption](cbbackupmgr-encryption.md) for the required authentication for each provider.

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

## [](#search-space)SEARCH SPACE

The examine command supports searching though multiple backups, this section explains how to use examine to search multiple backups and how it behaves when a repository contains backups from an older version or mixed collection aware/unaware backups.

### [](#backups-from-older-versions-of-cbbackupmgr)BACKUPS FROM OLDER VERSIONS OF CBBACKUPMGR

The examine command only supports searching backups created using a version of cbbackupmgr greater than or equal to 6.5.0.

When examine encounters a range of backups where no backups can be searched an error will be returned to you.

When examine encounters a mixed range of backups where one or more backups can be searched examine will skip the old backups and only search the supported backups. Note that a warning will be displayed indicating how many backups were skipped.

### [](#searching-collection-awareunaware-backups)SEARCHING COLLECTION AWARE/UNAWARE BACKUPS

When searching a collection unaware backup, the `--collection-string` argument expects only a bucket and will throw an error if provided with a scope or collection.

When searching a collection aware backup, the `--collection-string` argument expects a collection in the format `bucket.scope.collection` and will throw an error if provided with a bucket or scope.

See the [EXAMPLES](#EXAMPLES) section for examples of examining collection aware/unaware backups.

### [](#searching-mixed-collection-awareunaware-backups)SEARCHING MIXED COLLECTION AWARE/UNAWARE BACKUPS

When examining a range of backups which transition from collection unaware to collection aware (for example after upgrading the target cluster to 7.0.0) examine will stop search upon hitting the first collection aware backup.

Examine will print a warning indicating that it stopped searching prematurely, this warning will contain the name of the backup which can be passed into the `--start` flag to allow you to examine only the collection aware backups.

$ cbbackupmgr examine -a $PWD/archive -r repo --collection-string 'travel-sample' --key 'airline_10'
Warning: Finished examining collection unaware backups, 1 collection aware backup(s) remain(s); use the --start/--end flags to examine the collection aware backup(s) starting at '2021-01-27T13_35_53.284474589Z'
-- Backup 2021-01-27T13_33_08.986105547Z --
Description: First occurrence of key 'airline_10' in this timeline, document created
Cluster UUID: 59845c6cdce57b81bd6f450e5043bee7
Bucket: travel-sample (61ca19c7819478f27e03b398c6a540e7)
Document:
  Key: airline_10
  Sequence Number: 1
  Deleted: false
  Size: 159B (Key: 10B) (Meta: 29B) (Value: 120B) (XATTRS: 0B)
  Meta:
    Flags: 33554432
    Expiry: 0
    Locktime: 0
    CAS: 1611754171980709888
    Revseqno: 1
    Datatype: 3 (snappy,json)
  Value:
    {
        "callsign": "MILE-AIR",
        "country": "United States",
        "iata": "Q5",
        "icao": "MLA",
        "id": 10,
        "name": "40-Mile Air",
        "type": "airline"
    }

## [](#EXAMPLES)EXAMPLES

The examine command can be used to determine whether a collection unaware backup contains a specific document. See `COLLECTION AWARE BACKUPS` in [cbbackupmgr-backup](cbbackupmgr-backup.md) for information on what makes a backup collection aware/unaware.

$ cbbackupmgr examine -a $PWD/archive -r repo --collection-string 'travel-sample' --key 'airline_10'
-- Backup 2021-01-27T12_36_59.013718359Z --
Description: First occurrence of key 'airline_10' in this timeline, document created
Cluster UUID: d22cb6cbb72f9d6a86b75317478f60b0
Bucket: travel-sample (2de1c5edcd2daca4a08360c130ea6b19)
Document:
  Key: airline_10
  Sequence Number: 1
  Deleted: false
  Size: 159B (Key: 10B) (Meta: 29B) (Value: 120B) (XATTRS: 0B)
  Meta:
    Flags: 33554432
    Expiry: 0
    Locktime: 0
    CAS: 1611750671350693888
    Revseqno: 1
    Datatype: 3 (snappy,json)
  Value:
    {
        "id": 10,
        "type": "airline",
        "name": "40-Mile Air",
        "iata": "Q5",
        "icao": "MLA",
        "callsign": "MILE-AIR",
        "country": "United States"
    }

The same principle applies when searching a collection aware backup, the only difference being that the `--collection-string` argument requires a collection.

$ cbbackupmgr examine -a $PWD/archive -r repo --collection-string 'travel-sample.inventory.airline' --key 'airline_10'
-- Backup 2021-01-27T12_38_21.55739452Z --
Description: First occurrence of key 'airline_10' in this timeline, document created
Cluster UUID: 4fb26863aa5224ff97c9f17415c7bd92
Bucket: travel-sample (13c11d3be4bfba95f9e4da73bf8d1960)
Scope: inventory (8)
Collection: airline (10)
Document:
  Key: airline_10
  Sequence Number: 44
  Deleted: false
  Size: 159B (Key: 10B) (Meta: 29B) (Value: 120B) (XATTRS: 0B)
  Meta:
    Flags: 0
    Expiry: 0
    Locktime: 0
    CAS: 1611751097702088704
    Revseqno: 1
    Datatype: 3 (snappy,json)
  Value:
    {
        "id": 10,
        "type": "airline",
        "name": "40-Mile Air",
        "iata": "Q5",
        "icao": "MLA",
        "callsign": "MILE-AIR",
        "country": "United States"
    }

When more than one backup exists in a repository, examine will continue searching and output information for each backup it searches.

$ cbbackupmgr examine -a ~/Projects/couchbase-archive -r repo --collection-string 'travel-sample.inventory.airline' --key 'airline_10'
-- Backup 2021-01-27T12_38_21.55739452Z --
Description: First occurrence of key 'airline_10' in this timeline, document created
Cluster UUID: 4fb26863aa5224ff97c9f17415c7bd92
Bucket: travel-sample (13c11d3be4bfba95f9e4da73bf8d1960)
Scope: inventory (8)
Collection: airline (10)
Document:
  Key: airline_10
  Sequence Number: 44
  Deleted: false
  Size: 159B (Key: 10B) (Meta: 29B) (Value: 120B) (XATTRS: 0B)
  Meta:
    Flags: 0
    Expiry: 0
    Locktime: 0
    CAS: 1611751097702088704
    Revseqno: 1
    Datatype: 3 (snappy,json)
  Value:
    {
        "id": 10,
        "type": "airline",
        "name": "40-Mile Air",
        "iata": "Q5",
        "icao": "MLA",
        "callsign": "MILE-AIR",
        "country": "United States"
    }

-- Backup 2021-01-27T12_41_13.009708335Z --
Description: Mutation for document with key 'airline_10'
Cluster UUID: 4fb26863aa5224ff97c9f17415c7bd92
Bucket: travel-sample (13c11d3be4bfba95f9e4da73bf8d1960)
Scope: inventory (8)
Collection: airline (10)
Document:
  Key: airline_10
  Sequence Number: 75
  Deleted: false
  Size: 191B (Key: 10B) (Meta: 29B) (Value: 152B) (XATTRS: 0B)
  Meta:
    Flags: 33554438
    Expiry: 0
    Locktime: 0
    CAS: 1611751269058281472
    Revseqno: 2
    Datatype: 3 (snappy,json)
  Value:
    {
        "id": 10,
        "type": "airline",
        "name": "40-Mile Air",
        "iata": "Q5",
        "icao": "MLA",
        "callsign": "MILE-AIR",
        "country": "United States",
        "new_field": "new_value"
    }

-- Backup 2021-01-27T12_42_07.578485175Z --
Description: Deletion for document with key 'airline_10'
Cluster UUID: 4fb26863aa5224ff97c9f17415c7bd92
Bucket: travel-sample (13c11d3be4bfba95f9e4da73bf8d1960)
Scope: inventory (8)
Collection: airline (10)
Document:
  Key: airline_10
  Sequence Number: 76
  Deleted: true
  Size: 39B (Key: 10B) (Meta: 29B) (Value: 0B) (XATTRS: 0B)
  Meta:
    Flags: 0
    Expiry: 0
    Locktime: 0
    CAS: 1611751325090316288
    Revseqno: 3
    Datatype: 0 (binary)

-- Backup 2021-01-27T12_42_18.322132022Z --
Description: Collection 'airline' dropped
Cluster UUID: 4fb26863aa5224ff97c9f17415c7bd92
Bucket: travel-sample (13c11d3be4bfba95f9e4da73bf8d1960)
Scope: inventory (8)

-- Backup 2021-01-27T12_42_23.72226735Z --
Description: Scope 'inventory' dropped
Cluster UUID: 4fb26863aa5224ff97c9f17415c7bd92
Bucket: travel-sample (13c11d3be4bfba95f9e4da73bf8d1960)

-- Backup 2021-01-27T12_42_34.08410595Z --
Description: Bucket 'travel-sample' dropped
Cluster UUID: 4fb26863aa5224ff97c9f17415c7bd92

-- Backup 2021-01-27T12_42_35.395081659Z --
Description: Bucket 'travel-sample' not found
Cluster UUID: 4fb26863aa5224ff97c9f17415c7bd92

When searching are large range of backups, the `--start` and `--end` flags (see [START AND END](#START%5FAND%5FEND) for more information) may be used to filter which backups are searched.

$ cbbackupmgr examine -a ~/Projects/couchbase-archive -r repo --collection-string 'travel-sample.inventory.airline' --key 'airline_10' --start 2021-01-27T12_42_18.322132022Z --end 2021-01-27T12_42_35.395081659Z
-- Backup 2021-01-27T12_42_18.322132022Z --
Description: Collection 'airline' not found
Cluster UUID: 4fb26863aa5224ff97c9f17415c7bd92
Bucket: travel-sample (13c11d3be4bfba95f9e4da73bf8d1960)
Scope: inventory (8)

-- Backup 2021-01-27T12_42_23.72226735Z --
Description: Scope 'inventory' dropped
Cluster UUID: 4fb26863aa5224ff97c9f17415c7bd92
Bucket: travel-sample (13c11d3be4bfba95f9e4da73bf8d1960)

-- Backup 2021-01-27T12_42_34.08410595Z --
Description: Bucket 'travel-sample' dropped
Cluster UUID: 4fb26863aa5224ff97c9f17415c7bd92

-- Backup 2021-01-27T12_42_35.395081659Z --
Description: Bucket 'travel-sample' not found
Cluster UUID: 4fb26863aa5224ff97c9f17415c7bd92

By default, the examine will output binary documents as a hexdump (for the human readable format) and as a hexstring (for the JSON format).

$ cbbackupmgr examine -a $PWD/archive -r repo --collection-string 'default' --key 'pymc0'
-- Backup 2021-01-27T14_00_38.445404421Z --
Description: First occurrence of key 'pymc0' in this timeline, document created
Cluster UUID: 59845c6cdce57b81bd6f450e5043bee7
Bucket: default (7c8cb0f0bb9e2835d79e8dd91a5b0d67)
Document:
  Key: pymc0
  Sequence Number: 1
  Deleted: false
  Size: 84B (Key: 5B) (Meta: 29B) (Value: 50B) (XATTRS: 0B)
  Meta:
    Flags: 0
    Expiry: 0
    Locktime: 0
    CAS: 1611756033524170752
    Revseqno: 1
    Datatype: 0 (binary)
  Value:
    00000000  4d 59 4e 42 49 51 50 4d  5a 4a 50 4c 53 47 51 45  |MYNBIQPMZJPLSGQE|
    00000010  4a 45 59 44 54 5a 49 52  57 5a 54 45 4a 44 58 43  |JEYDTZIRWZTEJDXC|
    00000020  56 4b 50 52 44 4c 4e 4b  54 55 47 52 50 4f 51 49  |VKPRDLNKTUGRPOQI|
    00000030  42 5a                                             |BZ|

$ cbbackupmgr examine -a $PWD/archive -r repo --collection-string 'default' --key 'pymc0' --json | jq
[
  {
    "backup": "2021-01-27T14_00_38.445404421Z",
    "event_type": 1,
    "event_description": "First occurrence of key 'pymc0' in this timeline, document created",
    "cluster_uuid": "59845c6cdce57b81bd6f450e5043bee7",
    "bucket_uuid": "7c8cb0f0bb9e2835d79e8dd91a5b0d67",
    "scope_id": 0,
    "collection_id": 0,
    "document": {
      "key": "pymc0",
      "sequence_number": 1,
      "value": "4d594e424951504d5a4a504c534751454a455944545a4952575a54454a445843564b5052444c4e4b54554752504f5149425a",
      "metadata": {
        "flags": 0,
        "expiry": 0,
        "locktime": 0,
        "cas": 1611756033524170800,
        "revseqno": 1,
        "datatype": 0
      },
      "deleted": false
    }
  }
]

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

CB\_ENCRYPTION\_PASSPHRASE

Specifies the passphrase used for encryption.

CB\_KM\_KEY\_URL

Specifies the URL identifying the encryption key on the KMS. See `--km-key-url` for the expected format and accepted KMSs.

CB\_KM\_ACCESS\_ID

Specifies the key/user ID used to connect to the KMS.

CB\_KM\_SECRET\_ACCESS\_KEY

Specifies the secret key/token used to connect to the KMS.

CB\_KM\_AUTH\_FILE

Specifies a path to a file containing the required credentials to connect to the KMS.

CB\_KM\_TENANT\_ID

Specifies the cloud provider tenant to connect to the KMS with. This value is only for when using access key authentication in Azure.

## [](#see-also)SEE ALSO

[cbbackupmgr-cloud](cbbackupmgr-cloud.md)

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite