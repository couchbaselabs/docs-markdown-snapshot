---
title: cbbackupmgr restore
description: Restores data from the backup archive to a Couchbase cluster
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/backup/edit/trinity/docs/modules/backup-restore/pages/cbbackupmgr-restore.adoc
  xref: xref:7.6@server:backup-restore:cbbackupmgr-restore.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/backup-restore/cbbackupmgr-restore.html)

# cbbackupmgr restore

Restores data from the backup archive to a Couchbase cluster

## [](#synopsis)SYNOPSIS

cbbackupmgr restore [--archive <archive_dir>] [--repo <repo_name>]
                    [--cluster <host>] [--username <username>]
                    [--password <password>] [--client-cert <path>]
                    [--client-cert-password <password>] [--client-key <path>]
                    [--client-key-password <password>] [--start <start>]
                    [--end <end>] [--include-data <collection_string_list>]
                    [--exclude-data <collection_string_list>]
                    [--map-data <collection_string_mappings>]
                    [--disable-cluster-analytics] [--disable-analytics]
                    [--disable-views] [--disable-gsi-indexes]
                    [--disable-ft-indexes] [--disable-ft-alias]
                    [--disable-data] [--disable-eventing]
                    [--disable-bucket-query] [--disable-cluster-query]
                    [--exclude-tombstones] [--exclude-expired]
                    [--enable-users] [--overwrite-users]
                    [--enable-bucket-config] [--capella]
                    [--replace-ttl <type>][--replace-ttl-with <timestamp>]
                    [--force-updates]
                    [--threads <integer>] [--vbucket-filter <integer_list>]
                    [--no-progress-bar] [--auto-create-buckets]
                    [--autoremove-collections] [--preserve-collection-settings]
                    [--continue-on-cs-failure]
                    [--restore-partial-backups] [--obj-access-key-id <access_key_id>]
                    [--obj-cacert <cert_path>] [--obj-endpoint <endpoint>]
                    [--obj-read-only-mode] [--obj-no-ssl-verify]
                    [--obj-region <region>] [--obj-staging-dir <staging_dir>]
                    [--obj-secret-access-key <secret_access_key>]
                    [--s3-force-path-style] [--s3-log-level <level>]
                    [--point-in-time <time>]
                    [--filter-keys <regexp>] [--filter-values <regexp>]
                    [--passphrase <passphrase>] [--km-key-url <url>]
                    [--km-endpoint <endpoint>] [--km-region <region>]
                    [--km-access-key-id <id>] [--km-secret-access-key <key>]
                    [--km-auth-file <path>] [--purge] [--resume]

## [](#description)DESCRIPTION

Restores data from the backup archive to a target Couchbase cluster. By default all data, index definitions, view definitions, full-text index definitions and users are restored to the cluster unless specified otherwise in the repos backup config or through command line parameters when running the restore command.

The restore command is capable of restoring a single backup or a range of backups. When restoring a single backup, all data from that backup is restored. If a range of backups is restored, then cbbackupmgr will take into account any failovers that may have occurred in between the time that the backups were originally taken. If a failover did occur in between the backups, and the backup archive contains data that no longer exists in the cluster, then the data that no longer exists will be skipped during the restore. If no failovers occurred in between backups then restoring a range of backups will restore all data from each backup. If all data must be restored regardless of whether a failover occurred in between the original backups, then data should be restored one backup at a time.

The restore command is guaranteed to work during rebalances and failovers. If a rebalance is taking place, cbbackupmgr will track the movement of vbuckets around a Couchbase cluster and ensure that data is restored to the appropriate node. If a failover occurs during the restore then the client will wait 180 seconds for the failed node to be removed from the cluster. If the failed node is not removed in 180 seconds then the restore will fail, but if the failed node is removed before the timeout then data will continue to be restored.

Note that if you are restoring indexes then it is highly likely that you will need to take some manual steps in order to properly restore them. This is because by default indexes will only be built if they are restored to the exact same index node that they were backed up from. If the index node they were backed up from does not exist then the indexes will be restored in round-robin fashion among the current indexer nodes. These indexes will be created, but not built and will required the administrator to manually build them. We do this because we cannot know the optimal index topology ahead of time. By not building the indexes the administrator can move each index between nodes and build them when they deem that the index topology is optimal.

If restoring a backup from a cluster running version 7.2 or below to a cluster running version 7.6 or above, because of the `_system` scope present in 7.6 and above, you may need to map one of your scopes or collections where you did not have to before. This would only happen if the cluster you are restoring to has bucket scopes or collections with the same name as the scopes or collections in your backup. In that case the scopes or collections, while they do have the same name, might have different IDs and you would receive this error: `Error restoring cluster: scope 'testScope' with id 0x8 exists with a different name/id on the cluster, a manual remap using '--map-data' is required`. To avoid this you would need to tell cbbackupmgr to ignore the scope IDs and restore the scope in your backup to the scope in your cluster using the `--map-data` flag e.g. `--map-data bucket.testScope=bucket.testScope`.

## [](#options)OPTIONS

Below is a list of required and optional parameters for the restore command.

### [](#required)Required

\-a,--archive <archive\_dir>

The directory containing the backup repository to restore data from. When restoring from an archive stored in S3 prefix the archive path with `s3://${BUCKET_NAME}/`.

\-r,--repo <repo\_name>

The name of the backup repository to restore data from.

\-c,--cluster <hostname>

The hostname of one of the nodes in the cluster to restore data to. See the [HOST FORMATS](#HOST%5FFORMATS) section below for hostname specification details.

\-u,--username <username>

The username for cluster authentication. The user must have the appropriate privileges to restore data.

\-p,--password <password>

The password for cluster authentication. The user must have the appropriate privileges to restore data. If not password is supplied to this option then you will be prompted to enter your password.

\--client-cert <path>

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `--client-key` as an alternative to the `--username` and `--password` flags. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION)section for more information.

\--client-cert-password <password>

The password for the certificate provided to the `--client-cert` flag, when using this flag, the certificate/key pair is expected to be in the PKCS#12 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

\--client-key <path>

The path to the client private key whose public key is contained in the certificate provided to the `--client-cert` flag. May be supplied with `--client-cert` as an alternative to the `--username` and `--password`flags. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

\--client-key-password <password>

The password for the key provided to the `--client-key` flag, when using this flag, the key is expected to be in the PKCS#8 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

### [](#optional)Optional

\--start <start>

The first backup to restore. See [START AND END](#START%5FAND%5FEND) for information on what values are accepted.

\--end <end>

The final backup to restore. See [START AND END](#START%5FAND%5FEND) for information on what values are accepted.

\--include-data <collection\_string\_list>

Overrides the repository configuration to restore only the data specified in the <collection\_string\_list>. This flag takes a comma separated list of collection strings and can't be specified at the same time as `--exclude-data`. Note that including data at the scope/collection level is an Enterprise Edition feature.

\--exclude-data <collection\_string\_list>

Overrides the repository configuration to skip restoring the data specified in the <collection\_string\_list>. This flag takes a comma separated list of collection strings and can't be specified at the same time as `--include-data`. Note that excluding data at the scope/collection level is an Enterprise Edition feature.

\--filter-keys

Only restore data where the key matches a particular regular expression. The regular expressions provided must follow [RE2 syntax](https://github.com/google/re2/wiki/Syntax).

\--filter-values

Only restore data where the value matches a particular regular expression. The regular expressions provided must follow [RE2 syntax](https://github.com/google/re2/wiki/Syntax).

\--enable-bucket-config

Enables restoring the bucket configuration.

\--disable-views

Skips restoring view definitions for all buckets.

\--disable-gsi-indexes

Skips restoring gsi index definitions for all buckets.

\--disable-ft-indexes

Skips restoring full-text index definitions for all buckets.

\--disable-ft-alias

Skips restoring full-text alias definitions.

\--disable-data

Skips restoring all key-value data for all buckets, but scopes and collections are created.

\--disable-cluster-analytics

Skips restoring analytics cluster level analytics metadata e.g. Synonyms.

\--disable-analytics

Skips restoring bucket level analytics metadata.

\--disable-eventing

Skips restoring the eventing service metadata.

\--disable-bucket-query

Skips restoring bucket level Query Service metadata.

\--disable-cluster-query

Skips restoring cluster level Query Service metadata.

\--exclude-tombstones

Skips restoring tombstones.

\--exclude-expired

Skips restoring expired items. This can reduce restore times and decrease load on the cluster.

\--enable-users

Enables restoring cluster level users. As backup/restore of users is only available for CB version 7.6 and upwards, the flag is ignored for previous versions. When performing a restore, the user will only be allowed to restore users if it has permission to create those same users. This means the following:

* For Full Admin, restoring users will always be permitted.
* For Local User Security Admin, restoring users from a backup containing only local users is permitted.
* For External User Security Admin, restoring users from a backup containing only external users is permitted.
* For Read-Only Admin, restoring users is not permitted.

This flag can be used in conjunction to the overwrite-users flag to overwrite the already existing users in the cluster. If the overwrite-users flag is not set, the default behavior of restore of users is to skip already existing users.

\--overwrite-users

Overwrites the already existing users in the cluster as the default behavior of backup/restore of users is to skip already existing users, this flag can be used to overwrite this behavior. As backup/restore of users is only available for CB version 7.6 and upwards, the flag is ignored for previous versions. Note that it should be used with `--enable-users`.

\--capella

Skips restoring services that are not supported with Capella including: analytics, cluster analytics, bucket query, cluster query, views and users. This flag can be used to enable restoring from an on-premise cluster to a Capella one.

\--force-updates

Forces data in the Couchbase cluster to be overwritten even if the data in the cluster is newer. By default updates are not forced and all updates use Couchbase's conflict resolution mechanism to ensure that if newer data exists on the cluster that is not overwritten by older restore data.

\--map-data <collection\_string\_mappings>

Specified when you want to restore source data into a different location. For example this argument may be used to remap buckets/scopes/collections with the restriction that they must be remapped at the same level. For example a bucket may only be remapped to a bucket, a scope to a scope and a collection to a collection. The argument expects a comma separated list of collection string mappings e.g. `bucket1=bucket2,bucket3.scope1=bucket3.scope2,bucket4.scope.collection1=bucket4.scope.collection2`If used to remap a bucket into a collection then it will only restore data for the data service and will skip data for all the other services. See [REMAPPING](#REMAPPING) for additional information about this option.

\--replace-ttl <type>

Sets a new expiration (time-to-live) value for the specified keys. This parameter can either be set to "none", "all" or "expired" and should be used along with the --replace-ttl-with flag. If "none" is supplied then the TTL values are not changed. If "all" is specified then the TTL values for all keys are replaced with the value of the --replace-ttl-with flag. If "expired" is set then only keys which have already expired will have the TTL's replaced. For more information about the behavior of `--replace-ttl`see the [REPLACE TTL](#REPLACE%5FTTL).

\--replace-ttl-with <timestamp>

Updates the expiration for the keys specified by the --replace-ttl parameter. The parameter has to be set when --replace-ttl is set to "all". There are two options, RFC3339 time stamp format (2006-01-02T15:04:05-07:00) or "0". When "0" is specified the expiration will be removed. Please note that the RFC3339 value is converted to a Unix time stamp on the cbbackupmgr client. It is important that the time on both the client and the Couchbase Server are the same to ensure expiry happens correctly. For more information about the behavior of `--replace-ttl-with` see the [REPLACE TTL](#REPLACE%5FTTL).

\--vbucket-filter <list>

Specifies a list of VBuckets that should be restored. VBuckets are specified as a comma separated list of integers. If this parameter is not set then all vBuckets which were backed up are restored.

\--no-ssl-verify

Skips the SSL verification phase. Specifying this flag will allow a connection using SSL encryption, but will not verify the identity of the server you connect to. You are vulnerable to a man-in-the-middle attack if you use this flag. Either this flag or the --cacert flag must be specified when using an SSL encrypted connection.

\--cacert <cert\_path>

Specifies a CA certificate that will be used to verify the identity of the server being connecting to. Either this flag or the --no-ssl-verify flag must be specified when using an SSL encrypted connection.

\-t,--threads <num>

Specifies the number of concurrent clients to use when restoring data. Fewer clients means restores will take longer, but there will be less cluster resources used to complete the restore. More clients means faster restores, but at the cost of more cluster resource usage. This parameter defaults to 1 if it is not specified and it is recommended that this parameter is not set to be higher than the number of CPUs on the machine where the restore is taking place.

\--no-progress-bar

By default, a progress bar is printed to stdout so that the user can see how long the restore is expected to take, the amount of data that is being transferred per second, and the amount of data that has been restored. Specifying this flag disables the progress bar and is useful when running automated jobs.

\--auto-create-buckets

It will create the destination buckets if not present in the server.

\--autoremove-collections

Automatically delete scopes/collections which are known to be deleted in the backup. See [\[SCOPE\_COLLECTION\_DELETION\]](#SCOPE%5FCOLLECTION%5FDELETION) for more details.

\--preserve-collection-settings

Do not overwrite existing collection settings on the target cluster. By default, if a collection exists on both the backup and the target cluster but with different settings, the settings from the backup will overwrite the cluster's settings. When this flag is specified, existing collection settings on the target cluster will be preserved.

\--continue-on-cs-failure

It's possible that during a restore, a checksum validation will fail; in this case the restore will fail fast. Supplying this flag will mean that the restore will attempt to continue upon receiving a checksum failure. See [CHECKSUM FAILURE](#CHECKSUM%5FFAILURE)for more information.

\--restore-partial-backups

Allow a restore to continue when the final backup in the restore range is incomplete. This flag is incompatible with the `--obj-read-only` flag.

\--point-in-time <time>

(Beta) Specifies the point in time to restore to. The value accepted is ISO8601 date time format (YYYY-MM-DDTHH:MM:SS). This feature is currently in Beta and is not supported, this should only be used in test environments.

\--purge

If the last restore failed before it finished, then remove it's progress (which is persisted to disk) then restart from zero. Note that only the restore progress is purge, no backup data will be removed.

\--resume

If the last restore failed before it finished, then try to continue from where it left off.

### [](#cloud-integration)Cloud integration

Native cloud integration is an Enterprise Edition feature which was introduced in Couchbase Server 6.6.0.

Multiple cloud providers are supported, see the list below for more information.

1. Supported

  * AWS S3 (`s3://`)
  * GCP Google Storage (`gs://`)
  * Azure Blob Storage in 7.1.2+ (`az://`)

#### [](#required-2)Required

\--obj-staging-dir <staging\_dir>

When performing an operation on an archive which is located in the cloud such as AWS, the staging directory is used to store local meta data files. This directory can be temporary (it's not treated as a persistent store) and is only used during the backup. NOTE: Do not use `/tmp` as the `obj-staging-dir`. See `Disk requirements` in [cbbackupmgr-cloud](cbbackupmgr-cloud.md) for more information.

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

\--obj-read-only

Enable read only mode. When interacting with a cloud archive modifications will be made e.g. a lockfile will be created, log rotation will take place and the modified logs will be uploaded upon completion of the subcommand. This flag disables these features should you wish to interact with an archive in a container where you lack write permissions. This flag should be used with caution and you should be aware that your logs will not be uploaded to the cloud. This means that it's important that if you encounter an error you don't remove you staging directory (since logs will still be created in there and collected by the `collect-logs` subcommand).

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

## [](#HOST%5FFORMATS)HOST FORMATS

When specifying a host/cluster for a command using the `-c`/`--cluster` flag, the following formats are accepted:

* `<addr>:<port>`
* `http://<addr>:<port>`
* `https://<addr>:<port>`
* `couchbase://<addr>:<port>`
* `couchbases://<addr>:<port>`
* `couchbase://<srv>`
* `couchbases://<srv>`
* `<addr>:<port>,<addr>:<port>`
* `<scheme>://<addr>:<port>,<addr>:<port>`

The `<port>` portion of the host format may be omitted, in which case the default port will be used for the scheme provided. For example, `http://` and `couchbase://` will both default to 8091 where `https://` and `couchbases://` will default to 18091\. When connecting to a host/cluster using a non-default port, the `<port>` portion of the host format must be specified.

### [](#connection-strings-multiple-nodes)Connection Strings (Multiple nodes)

The `-c`/`--cluster` flag accepts multiple nodes in the format of a connection string; this is a comma separated list of `<addr>:<port>` strings where `<scheme>` only needs to be specified once. The main advantage of supplying multiple hosts is that in the event of a failure, the next host in the list will be used.

For example, all of the following are valid connection strings:

* `localhost,[::1]`
* `10.0.0.1,10.0.0.2`
* `http://10.0.0.1,10.0.0.2`
* `https://10.0.0.1:12345,10.0.0.2`
* `couchbase://10.0.0.1,10.0.0.2`
* `couchbases://10.0.0.1:12345,10.0.0.2:12345`

### [](#srv-records)SRV Records

The `-c`/`--cluster` flag accepts DNS SRV records in place of a host/cluster address where the SRV record will be resolved into a valid connection string. There are a couple of rules which must be followed when supplying an SRV record which are as follows:

* The `<scheme>` portion must be either `couchbase://` or `couchbases://`
* The `<srv>` portion should be a hostname with no port
* The `<srv>` portion must not be a valid IP address

For example, all of the following are valid connection string using an SRV record:

* `couchbase://hostname`
* `couchbases://hostname`

### [](#alternate-addressing-caok8s)Alternate Addressing (CAO/K8S)

Users of the CAO (Couchbase Autonomous Operator) or K8S may need to supply the `network=external` query parameter to force connection via the defined alternate addressing.

For example, the following are valid connection strings:

* `https://10.0.0.1:12345,10.0.0.2?network=default`
* `https://10.0.0.1:12345,10.0.0.2?network=external`

## [](#CERTIFICATE%5FAUTHENTICATION)CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)

This tool supports authenticating against a Couchbase Cluster by using certificate based authentication (mTLS authentication). To use certificate based authentication a certificate/key must be supplied, there a currently multiple ways this may be done.

### [](#pem-encoded-certificatekey)PEM ENCODED CERTIFICATE/KEY

An unencrypted PEM encoded certificate/key may be supplied by using: - `--client-cert <path>`\- `--client-key <path>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

The file passed to `--client-key` must contain at most one private key, the key can be in one of the following formats:

* PKCS#1
* PKCS#8
* EC

Currently, only the following key types are supported:

* RSA
* ECDSA
* ED25519

### [](#pem-encoded-certificatepem-or-der-encrypted-pkcs8-key)PEM ENCODED CERTIFICATE/PEM OR DER ENCRYPTED PKCS#8 KEY

An encrypted PKCS#8 formatted key may be provided using:

* `--client-cert <path>`
* `--client-key <path>`
* `--client-key-password <password>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

Currently, only the following key types are supported:

* RSA
* ECDSA
* ED25519

### [](#encrypted-pkcs12-certificatekey)ENCRYPTED PKCS#12 CERTIFICATE/KEY

An encrypted PKCS#12 certificate/key may be provided using:

* `--client-cert <path>`
* `--client-cert-password <password>`

The file passed to `--client-cert` must contain the client certificate and exactly one private key. It may also contain the chain required to authenticate the client certificate.

Currently, only the following key types are supported:

* RSA
* ECDSA
* ED25519

## [](#rbac)RBAC

When performing a backup/restore with a user which is using RBAC, there are a couple of things that should be taken into consideration each of which is highlighted in this section.

### [](#bucket-level)Bucket Level

Bucket level data may be backed up/restored using the `data_backup` (Data Backup & Restore) role.

The `data_backup` role does not have access to cluster level data such as:

* Analytics Synonyms
* Eventing Metadata
* FTS Aliases

Backing up/restoring cluster level data with the `data_backup` role will cause permission errors like the one below.

Error backing up cluster: {"message":"Forbidden. User needs one of the following permissions","permissions":["cluster.fts!read"]}

When presented with an error message such as the one above, there's two clear options.

The first option is to provide the user with the required credentials using either the cli, REST API or Couchbase Server WebUI. This can be done by editing the user and adding the required role. See `Cluster Level` for more information about the required roles.

Secondly, backing up/restoring the specific service can be disabled. For backups this must be done when configuring the repository with the `config`command using the `--disable` style flags. For restore, these flags may be used directly to disable one or more services. See the backup/restore documentation for more information.

### [](#cluster-level)Cluster Level

Backing up/restoring cluster level data requires additional RBAC roles, each of which is highlighted below:

Analytics Synonyms

`analytics_admin` (Analytics Admin)

Eventing Metadata

`eventing_admin` (Eventing Full Admin)

FTS Aliases

`fts_admin` (Search Admin)

These additional roles are required since this is cluster level data which may encompass multiple buckets.

## [](#supported-backup-versions)Supported Backup Versions

The `restore` sub-command currently supports restoring backups created by previous versions of `cbbackupmgr` above and including 6.5.0\. Versions before 6.5.0 used the `ForestDB` storage format which is no longer supported.

Backups created by these versions are still safe and usable, however, they must be restored/merged with a version of `cbbackupmgr` which supports interacting with 6.0.x archives e.g. 6.5.x, 6.6.x, 7.0.x and 7.1.x.

### [](#example)Example

Imagine you have a backup created by a 6.0.x version of `cbbackupmgr`, this will use the `ForestDB` storage format. You'd like to restore this backup, however, the latest version no longer supports interacting with this format.

In this case, you could either:

1. Restore the backup using `cbbackupmgr` from 6.5.x, 6.6.x, 7.0.x or 7.1.x.
2. Merge two or more backups using `cbbackupmgr` from 6.5.x, 6.6.x, 7.0.x or 7.1.x then restore it using the latest version.

## [](#REPLACE%5FTTL)REPLACE TTL

The behavior of the --replace-ttl/--replace-ttl-with flags is well defined, however, there are some conditions where the behavior may seem surprising or unexpected due to conflict resolution.

Imagine the case where a backup contains one or more documents which have an expiry which has now elapsed. There are several possible scenarios which could take place when restoring these documents when using the `--replace-ttl` and `--replace-ttl-with` flags. These scenarios are enumerated below.

### [](#restoring-to-a-new-clusterbucket)RESTORING TO A NEW CLUSTER/BUCKET

When restoring to a new cluster it's expected that all the documents which match the all/expired condition will be restored with their new/updated ttl values.

### [](#restoring-to-the-same-bucket)RESTORING TO THE SAME BUCKET

The most interesting/unexpected cases occur when restoring the backup to the same bucket at some point in the future.

#### [](#expired-documents-have-not-been-purged)EXPIRED DOCUMENTS HAVE NOT BEEN PURGED

In the event that the restore takes place and the expired documents have not been purged yet, conflict resolution will take precedence and the documents will not be restored. This behavior will manifest itself as skipped mutations which will be displayed in restore sub-command output.

Restoring backup '2021-05-17T11_00_15.843794944+01_00'
Copied all data in 1.773s (Avg. 21.03MiB/Sec)                                                                           31591 items / 21.03MiB
[====================================================================================================================================] 100.00%

| Transfer
| --------
| Status    | Avg Transfer Rate | Started At                        | Finished At                     | Duration |
| Succeeded | 21.03MiB          | Mon, 17 May 2021 11:00:25 +0100/s | Mon, 17 May 2021 11:00:26 +0100 | 1.785s   |

| Bucket
| ------
| Name          | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| travel-sample | Succeeded | 21.03MiB    | 21.03MiB/s        | Mon, 17 May 2021 11:00:25 +0100 | Mon, 17 May 2021 11:00:26 +0100 | 1.713s   |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 0        | 0       | 31591   | 0        | 0       | 0       | 0        | 0       | 0       |

Restore completed successfully

#### [](#expired-documents-have-been-purged)EXPIRED DOCUMENTS HAVE BEEN PURGED

If the restore is performed after the user-defined purge interval where a compaction has taken place, the documents would be restored because the expired documents would no longer exist in the cluster.

#### [](#forcing-updates)FORCING UPDATES

The above behavior may be overridden by using the `--force-updates` flag which will bypass conflict resolution and result in the documents from the backup being restored.

The `--force-updates` flag will affect all the documents being restored and not just those which contain an expiry which is being replaced. This may result in documents being overwritten with older versions from the backup; if the expired documents keys are known beforehand, a mixed use of `--force-updates` and `--filter-keys` may be more precise.

### [](#collection-and-bucket-max-ttl)COLLECTION AND BUCKET MAX TTL

The `--replace-ttl` and `--replace-ttl-with` flags only modify document-level TTL values. They do not modify collection-level or bucket-level maxTTL settings.

Couchbase Server's maxTTL setting acts as both a default expiration and an upper limit. If a document's expiration is 0 (no expiry), the server applies the maxTTL as the expiration. If a document's expiration exceeds the maxTTL, the server caps it at the maxTTL value. For example, restoring with `--replace-ttl all --replace-ttl-with 0` will not remove expiry from documents if the target collection has a maxTTL configured.

To achieve the desired TTL behavior, either modify the collection/bucket maxTTL settings after the restore, or configure the target cluster's collections with the desired maxTTL settings beforehand and use the `--preserve-collection-settings` flag to prevent them from being overwritten.

## [](#examples)EXAMPLES

The restore command can be used to restore a single backup or range of backups in a backup repository. In the examples below, we will look a few different ways to restore data from a backup repository. All examples will assume that the backup archive is located at /data/backups and that all backups are located in the "example" backup repository.

The first thing to do when getting ready to restore data is to decide which backups to restore. The easiest way to do this is to use the info command to see which backups are available to restore.

$ cbbackupmgr info --archive /data/backups --repo example --all
| Repo
| ----
| Name    | Size    | # Backups | Encrypted | Point in Time |
| example | 4.38MiB | 3         | false     | false         |
|
| Backups
| -------
|
| * Backup
|   ------
|   Name                             | Size    | Type | Complete |
|   2020-06-02T07_49_11.281004+01_00 | 1.69MiB | FULL | true     |
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
|         Point in Time
|         -------------
|         Mutations | Deletions | Duplicate Size |
|         4096      | 0         | 0B             |
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
|   Name                             | Size    | Type | Complete |
|   2020-06-03T07_49_52.577901+01_00 | 1.34MiB | INCR | true     |
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
|         Point in Time
|         -------------
|         Mutations | Deletions | Duplicate Size |
|         2048      | 0         | 0B             |
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
|   Name                             | Size    | Type | Complete |
|   2020-06-04T07_50_06.908787+01_00 | 1.34MiB | INCR | true     |
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
|         Point in Time
|         -------------
|         Mutations | Deletions | Duplicate Size |
|         2048      | 0         | 0B             |
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

From the information of the backup repository we can see we have three backups that we can restore in the "examples" backup repository. If we just want to restore one of them we set the --start and --end flags in the restore command to the same backup name and specify the cluster that we want to restore the data to. In the example below we will restore only the oldest backup.

$ cbbackupmgr restore -a /data/backups -r example \
 -c couchbase://127.0.0.1 -u Administrator -p password \
 --start 2020-06-02T07_49_11.281004+01_00 \
 --end 2020-06-02T07_49_11.281004+01_00

If we want to restore only the two most recent backups then we specify the --start and --end flags with different backup names in order to specify the range we want to restore.

$ cbbackupmgr restore -a /data/backups -r example \
 -c couchbase://127.0.0.1 -u Administrator -p password \
 --start 2020-06-02T07_49_11.281004+01_00 \
 --end 2020-06-03T07_49_52.577901+01_00

If we want to restore all of the backups in the "examples" directory then we can omit the --start and --end flags since their default values are the oldest and most recent backup in the backup repository.

$ cbbackupmgr restore -a /data/backups -r example \
 -c couchbase://127.0.0.1 -u Administrator -p password

Restore also allows filtering the data restored by document key and/or value by passing regular expressions to the flags `--filter-keys` and `--filter-values` respectively. Say we backup the sample bucket 'beer-sample' if we only wanted to restore only the documents that have a key that starts with '21st\_amendment\_brewery\_cafe'. This can be done using the flag `--filter-keys` as shown below.

$ cbbackupmg restore -c http://127.0.0.1:8091 -u Administrator -p password \
 -a /data/backups -r beer --filter-keys '^21st_amendment_brewery_cafe.*'

Restore also allows filtering by value. Let's say we only want to restore documents that contain the JSON field `address`. This could be done by passing the regular expression `{.*"address":.*}` to the `--filter-values` flag as illustrated below.

$ cbbackupmgr restore -c http://127.0.0.1:8091 -u Administrator -p password \
 -a /data/backups -r beer --filter-values '{.*"address":.*}'

Restore also allows overwriting users. Let's say we want to restore all the users and overwrite any existing ones, as restore skips existing users by default. This could be done by passing the `--overwrite-users` flag as illustrated below.

$ cbbackupmgr restore -c http://127.0.0.1:8091 -u Administrator -p password \
 -a /data/backups -r beer --overwrite-users

Finally, we can combine both flags to filter by both key and value. Imagine you want to restore the values for beers that start with the key '21st\_amendment\_brewery\_cafe' and have the JSON field `"category":"North American Ale"`. This can be done by using the command below.

$ cbbackupmgr restore -c http://127.0.0.1:8091 -u Administrator -p password \
 -a /data/backups -r beer --filter-values '{.*"category":"North American Ale".*}' \
 --filter-keys '^21st_amendment_brewery_cafe.*'

The regular expressions provided must follow [RE2 syntax](https://github.com/google/re2/wiki/Syntax).

## [](#CHECKSUM%5FFAILURE)CHECKSUM FAILURE

A checksum failure may occur during a restore and indicates that a document has changed since the creation of the backup. Depending on the type of corruption we may be able to restore by skipping only the corrupted documents. However, if the size of the data file has changed (e.g. not a bit flip or byte for byte modification) **all** documents after the corruption (for that vBucket) will be unusable.

## [](#automatic-collection-creation)AUTOMATIC COLLECTION CREATION

By design, users may not recreate the `_default` collection once it has been deleted. Therefore, this means that the `_default` collection can't (and won't) be recreated if it's missing. Before performing a transfer, a check will take place to see if the `_default` collection will be required when it's missing. If this is the case, the command will exit early and you will be required to remap the `_default` collection using the `--map-data` flag.

## [](#automatic-collection-deletion)AUTOMATIC COLLECTION DELETION

During a backup cbbackupmgr will take note of which scopes/collections were create/deleted/modified up to the point that the backup began. This behavior can be leveraged to automatically delete any scopes/collections which are marked as deleted in the backup. We will only delete scopes/collections which are identical to the ones which are stored in the backup; ones which match by both id and name.

## [](#REMAPPING)REMAPPING

During a transfer, scopes/collections can be remapped from one location to another. There are several rules that are enforced when remapping scopes/collections, they are as follows:

* You may not remap the `_default` scope (discussed in THE DEFAULT SCOPE).
* You may not restore users while remapping scopes/collections, the restoring of users will be skipped.
* You may only remap scopes/collections at the same level meaning scopes may be remapped to other scopes, and collections to other collections, however, a scope can't be remapped to a collection or vice versa.
* Scopes/collections may only be remapped within the same bucket. For example the mapping `bucket1.scope.collection=bucket2.scope.collection` is invalid.
* Scopes/collections may only be remapped once. For example the mapping `bucket1.scope1=bucket1.scope2,bucket1.scope1=bucket1.scope3` is invalid.
* Remapping may only take place at one level at once meaning that if a parent bucket/scope is already remapped, the child scopes/collections may not also be remapped. For example the mapping `bucket1.scope1=bucket1.scope2,bucket1.scope1.collection1=bucket1.scope3.collection9`is invalid.

### [](#remapping-a-scopecollection-without-renaming)REMAPPING A SCOPE/COLLECTION WITHOUT RENAMING

During a transfer, it's possible for a scope/collection to encounter a conflict (for example, because it has been recreated). It may not be preferable to rename the scope/collection during the transfer.

For this reason, the `--map-data` flag, allows you to remap a scope/collection to itself; this indicates that the scope/collection that exists in the target (with a different id) should be treated as the same.

As an example, the following error message indicates that a collection has been recreated prior to a restore.

Error restoring cluster: collection 8 with name 'collection1' in the scope '_default' exists with a different name/id on the cluster, a manual remap is required

Using the `--map-data` flag with the argument `bucket._default.collection1=bucket._default.collection1` would cause `cbbackupmgr` to treat `collection1` (with id 8) as `collection1` (with the id it exists with in the target).

### [](#the-default-scope)THE DEFAULT SCOPE

As mentioned in AUTOMATIC COLLECTION CREATION, it's not possible to recreate the `_default` scope/collection. This means you can't remap the `_default`scope because the tool may be unable to create a destination scope/collection. This may be worked around by remapping each collection inside the `_default`scope.

### [](#bucket-to-collection-remapping)BUCKET TO COLLECTION REMAPPING

As discussed in REMAPPING, it's not possible to remap data at different levels; buckets must be remapped to buckets, scopes to scopes and collections to collections. However, there is one supported edge case, which is remapping a bucket into a collection to allow migration from a collection unaware to collection aware datasets.

To remap a bucket into a collection using `--map-data` you may supply `--map-data bucket._default._default=bucket.scope.collection`. This functionality is compatible with cross bucket mapping, for example you may also supply `--map-data bucket1._default._default=bucket2.scope.collection`.

Note that once you've provided a mapping to remap a bucket into a collection you may not remap that bucket elsewhere. For example `--map-data bucket1._default._default=bucket2.scope.collection,bucket1=bucket3` is invalid.

### [](#remapping-multiple-data-sources-into-a-single-target-source)REMAPPING MULTIPLE DATA SOURCES INTO A SINGLE TARGET SOURCE

As outlined in the rules discussed in REMAPPING, it's not possible to remap a bucket/scope/collection multiple times, however, it is possible to remap to a single destination multiple times. For example the mapping `bucket1=dest,bucket2=dest,bucket3=dest` is valid.

Although valid, this manor of remapping is dangerous and can result in data not being transferred due to conflicting key spaces. If this style of remapping is detected a warning will be printed before proceeding.

## [](#restoring-a-collection-aware-backup-to-a-collection-unaware-cluster)RESTORING A COLLECTION AWARE BACKUP TO A COLLECTION UNAWARE CLUSTER

The restore sub-command supports restoring collection aware backups to collection unaware cluster. When restoring a collection aware backup to a cluster which doesn't support collections, `cbbackupmgr` will restore the `_default._default` collection into the target bucket; no data will be transferred for any other collections.

This allows you to utilize a collection aware cluster, without using the collections feature and still be able to restore your data to a cluster which is running a previous version of Couchbase which is collection unaware.

## [](#discussion)DISCUSSION

The restore command works by replaying the data recorded in backup files. During a restore each key-value pair backed up by cbbackupmgr will be sent to the cluster as either a "set" or "delete" operation. The restore command replays data from each file in order of backup time to guarantee that older backup data does not overwrite newer backup data. The restore command uses Couchbase's conflict resolution mechanism by default to ensure this behavior. The conflict resolution mechanism can be disable by specifying the --force-updates flag when executing a restore.

Starting in Couchbase 4.6 each bucket can have different conflict resolution mechanisms. cbbackupmgr will backup all meta data used for conflict resolution, but since each conflict resolution mechanism is different cbbackupmgr will prevent restores to a bucket when the source and destination conflict resolution methods differ. This is done because by default cbbackupmgr will use the conflict resolution mechanism of the destination bucket to ensure an older value does not overwrite a newer value. If you want to restore a backup to a bucket with a different conflict resolution type you can do by using the --force-updates flag. This is allowed because forcing updates means that cbbackupmgr will skip doing conflict resolution on the destination bucket.

Like backups, restores may be resumed if they fail using the `--resume` flag.

## [](#environment-and-configuration-variables)ENVIRONMENT AND CONFIGURATION VARIABLES

CB\_CLUSTER

Specifies the hostname of the Couchbase cluster to connect to. If the hostname is supplied as a command line argument then this value is overridden.

CB\_USERNAME

Specifies the username for authentication to a Couchbase cluster. If the username is supplied as a command line argument then this value is overridden.

CB\_PASSWORD

Specifies the password for authentication to a Couchbase cluster. If the password is supplied as a command line argument then this value is overridden.

CB\_CLIENT\_CERT

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `CB_CLIENT_KEY` as an alternative to the `CB_USERNAME` and `CB_PASSWORD` variables. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION)section for more information.

CB\_CLIENT\_CERT\_PASSWORD

The password for the certificate provided to the `CB_CLIENT_CERT` variable, when using this variable, the certificate/key pair is expected to be in the PKCS#12 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

CB\_CLIENT\_KEY

The path to the client private key whose public key is contained in the certificate provided to the `CB_CLIENT_CERT` variable. May be supplied with `CB_CLIENT_CERT` as an alternative to the `CB_USERNAME` and `CB_PASSWORD`variables. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

CB\_CLIENT\_KEY\_PASSWORD

The password for the key provided to the `CB_CLIENT_KEY` variable, when using this variable, the key is expected to be in the PKCS#8 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

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

[cbbackupmgr-backup](cbbackupmgr-backup.md), [cbbackupmgr-info](cbbackupmgr-info.md), [cbbackupmgr-cloud](cbbackupmgr-cloud.md) [cbbackupmgr-network-filesystems](cbbackupmgr-network-filesystems.md)

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite