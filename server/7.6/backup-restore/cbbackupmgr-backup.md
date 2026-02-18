---
title: cbbackupmgr backup
description: Backs up data from a Couchbase cluster
editUrl: https://github.com/couchbase/backup/edit/trinity/docs/modules/backup-restore/pages/cbbackupmgr-backup.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/backup-restore/cbbackupmgr-backup.html)

# cbbackupmgr backup

Backs up data from a Couchbase cluster

## [](#synopsis)SYNOPSIS

cbbackupmgr backup [--archive <archive_dir>] [--repo <repo_name>]
                   [--cluster <url>] [--username <username>]
                   [--password <password>] [--client-cert <path>]
                   [--client-cert-password <password>] [--client-key <path>]
                   [--client-key-password <password>] [--resume] [--purge]
                   [--threads <num>] [--cacert <file>] [--no-ssl-verify]
                   [--value-compression <type>] [--no-progress-bar]
                   [--skip-last-compaction] [--consistency-check <window>]
                   [--full-backup] [--obj-access-key-id <access_key_id>]
                   [--obj-cacert <cert_path>] [--obj-endpoint <endpoint>]
                   [--obj-no-ssl-verify] [--obj-region <region>]
                   [--obj-staging-dir <staging_dir>]
                   [--obj-secret-access-key <secret_access_key>]
                   [--s3-force-path-style] [--s3-log-level <level>]
                   [--passphrase <passphrase>] [--km-key-url <url>]
                   [--km-endpoint <endpoint>] [--km-region <region>]
                   [--km-access-key-id <id>] [--km-secret-access-key <key>]
                   [--km-auth-file <path>]

## [](#description)DESCRIPTION

Backs up a Couchbase cluster into the backup repository specified. Before running the backup command, a backup repository must be created. See [cbbackupmgr-config](cbbackupmgr-config.md) for more details on creating a backup repository. The backup command uses information from the previous backup taken in order to backup all new data on a Couchbase cluster. If no previous backup exists then all data on the cluster is backed up. The backup is taken based on the backup repository’s backup configuration. Each backup will create a new folder in the backup repository. This folder will contain all data from the backup and is named to reflect the time that the backup was started.

As the backup runs, it tracks its progress which allows failed backups to be resumed from the point where they left off. If a backup fails before it is complete it is considered a partial backup. To attempt to complete the backup process, the backup may be resumed with the --resume flag. It may also be deleted and resumed from the previous successful backup with the --purge flag.

The backup command is capable of backing up data when there is a cluster rebalance operation in progress. During a rebalance, the backup command will track data as it moves around the cluster and complete the backup. However, users should use caution when running backups during a rebalance since both the rebalance and backup operations can be resource intensive and may cause temporary performance degradations in other parts of the cluster. See the --threads flag for information on how to lower the impact of the backup command on your Couchbase cluster.

The backup command is also capable of backing up data when there are server failures in the target backup cluster. When a server failure occurs the backup command will wait for 180 seconds for the failed server to come back online or for the failed server to be failed over and removed from the cluster. If 180 seconds passes without the failed server coming back online or being failed over then the backup command will mark the data on that node as failed and attempt to back up the rest of the data from the cluster. The backup will be marked as a partial backup in the backup archive and will need to be either resumed or purged when the backup command is invoked again.

Note that if backing up a cluster running version 7.6 or above the `_system`scope (used for internal Couchbase services) will be backed up too.

## [](#options)OPTIONS

Below are a list of required and optional parameters for the backup command.

### [](#required)Required

\-a,--archive <archive\_dir>

The location of the backup archive directory. When backing up directly to S3 prefix the archive path with `s3://${BUCKET_NAME}/`.

\-r,--repo <repo\_name>

The name of the backup repository to backup data into.

\-c,--cluster <hostname>

The hostname of one of the nodes in the cluster to back up. See the [HOST FORMATS](#HOST%5FFORMATS) section below for hostname specification details.

\-u,--username <username>

The username for cluster authentication. The user must have the appropriate privileges to backup data.

\-p,--password <password>

The password for cluster authentication. The user must have the appropriate privileges to backup data. If not password is supplied to this option then you will be prompted to enter your password.

\--client-cert <path>

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `--client-key` as an alternative to the `--username` and `--password` flags. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION)section for more information.

\--client-cert-password <password>

The password for the certificate provided to the `--client-cert` flag, when using this flag, the certificate/key pair is expected to be in the PKCS#12 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

\--client-key <path>

The path to the client private key whose public key is contained in the certificate provided to the `--client-cert` flag. May be supplied with `--client-cert` as an alternative to the `--username` and `--password`flags. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

\--client-key-password <password>

The password for the key provided to the `--client-key` flag, when using this flag, the key is expected to be in the PKCS#8 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

### [](#optional)Optional

\--resume

If the previous backup did not complete successfully it can be resumed from where it left off by specifying this flag. Note that the resume and purge flags may not be specified at the same time.

\--purge

If the previous backup did not complete successfully the partial backup will be removed and restarted from the point of the previous successful backup by specifying this flag. Note that the purge and resume flags may not be specified at the same time.

\--no-ssl-verify

Skips the SSL verification phase. Specifying this flag will allow a connection using SSL encryption, but will not verify the identity of the server you connect to. You are vulnerable to a man-in-the-middle attack if you use this flag. Either this flag or the --cacert flag must be specified when using an SSL encrypted connection.

\--cacert <cert\_path>

Specifies a CA certificate that will be used to verify the identity of the server being connecting to. Either this flag or the --no-ssl-verify flag must be specified when using an SSL encrypted connection.

\--value-compression <compression\_policy>

Specifies a compression policy for backed up values. When Couchbase sends data to the backup client the data stream may contain all compressed values, all uncompressed values, or a mix of compressed and uncompressed values. To backup all data in the same form that the backup client receives it you can specify "unchanged". If you wish for all values to be uncompressed then you can specify "uncompressed". This policy will however uncompress any compressed values received from Couchbase and may increase the backup file size. To compress all values you can specify "compressed". This will compress any uncompressed values before writing them to disk. The default value for this option is "compressed".

\-t,--threads <num>

Specifies the number of concurrent clients to use when taking a backup. Fewer clients means backups will take longer, but there will be less cluster resources used to complete the backup. More clients means faster backups, but at the cost of more cluster resource usage. This parameter defaults to 1 if it is not specified and it is recommended that this parameter is not set to be higher than the number of CPUs on the machine where the backup is taking place.

\--no-progress-bar

By default, a progress bar is printed to stdout so that the user can see how long the backup is expected to take, the amount of data that is being transferred per second, and the amount of data that has been backed up. Specifying this flag disables the progress bar and is useful when running automated jobs.

\--consistency-check <window>

When a window larger than 1 is provided it will enable the consistency checker. This will show a warning if the backup consistency window is larger than the one provided in seconds. This is an Enterprise Edition feature and is currently in developer preview. See [DISCUSSION](#DISCUSSION) for more information.

\--full-backup

Force a full backup in the same backup repository. This can be used to more easily manage backups.

### [](#cloud-integration)Cloud integration

Native cloud integration is an Enterprise Edition feature which was introduced in Couchbase Server 6.6.0.

Backing up directly to object store is only supported for Couchbase Server 6.6.0 and above. It’s likely that backing up older clusters will result in significantly higher memory consumption.

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

When presented with an error message such as the one above, there’s two clear options.

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

## [](#examples)EXAMPLES

The following command is used to take a backup of a Couchbase cluster.

$ cbbackupmgr config --archive /data/backups --repo example
$ cbbackupmgr backup -a /data/backups -r example \
 -c couchbase://172.23.10.5 -u Administrator -p password

Once the backup has finished there will be a new directory in the specified backup repository containing the backed up data. You can see this new directory using the [cbbackupmgr-info](cbbackupmgr-info.md) command.

$ cbbackupmgr info -a /data/backups --all

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
|   Name       | Size     | # Backups | Encrypted | Point in Time |
|   Manchester | 55.56MiB | 1         | false     | false         |
|
|   Backups
|   -------
|
|  *  Backup
|     ------
|     Name                           | Size     | Type | Complete |
|     2019-03-15T13_52_27.18301Z     | 52.42MiB | FULL | true     |
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
|           Point in Time
|           -------------
|           Mutations | Deletions | Duplicate Size |
|           7303      | 0         | 0B             |
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
|           Point in Time
|           -------------
|           Mutations | Deletions | Duplicate Size |
|           586       | 0         | 0B             |
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
|           Point in Time
|           -------------
|           Mutations | Deletions | Duplicate Size |
|           31591     | 0         | 0B             |
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

If a backup fails then it is considered a partial backup and the backup client will not be able to back up any new data until the user decides whether to resume or purge the partial backup. This decision is made by specifying either the --resume or the --purge flag on the next invocation of the backup command. Below is an example of how this process works if the user wants to resume a backup.

$ cbbackupmgr config -a /data/backups -r example

$ cbbackupmgr backup -a /data/backups -r example \
 -c 172.23.10.5 -u Administrator -p password

Error backing up cluster: Not all data was backed up due to connectivity
issues. Check to make sure there were no server side failures during
backup. See backup logs for more details on what wasn't backed up.

$ cbbackupmgr backup -a /data/backups -r example \
 -c 172.23.10.5 -u Administrator -p password

Error backing up cluster: Partial backup error 2016-02-11T17:00:19.594970735-08:00

$ cbbackupmgr backup -a /data/backups -r example -c 172.23.10.5 \
 -u Administrator -p password --resume

Backup successfully completed

To backup a cluster with a different amount of concurrent clients and decrease the backup time you can specify the --threads flag. Remember that specifying a higher number of concurrent clients increases the amount of resources the cluster uses to complete the backup. Below is an example of using 16 concurrent clients.

$ cbbackupmgr config -a /data/backups -r example

$ cbbackupmgr backup -a /data/backups -r example \
 -c 172.23.10.5 -u Administrator -p password -t 16

To force the creation of a full backup, use the `--full-backup` flag. This will result in cbbackupmgr streaming all the available data again. It’s expected that more disk space will be used and that the full backup will take longer than performing an incremental backup (the default).

In the example below, the first backup is implicitly a full backup, the second backup is an incremental (where no additional data needed to be backed up) and the third is a forced full backup (note that we backed up the same amount of items as the first backup).

$ cbbackupmgr backup -a ~/Projects/couchbase-archive -r repo -c 172.20.1.1 -u Administrator -p asdasd
Backing up to '2021-02-09T13_35_15.426546996Z'
Copied all data in 2.865028528s (Avg. 10.53MB/Sec)                                                                                        31591 items / 21.06MB
[=====================================================================================================================================================] 100.00%
Backup completed successfully
Backed up bucket "travel-sample" succeeded
Mutations backed up: 31591, Mutations failed to backup: 0
Deletions backed up: 0, Deletions failed to backup: 0

$ cbbackupmgr backup -a ~/Projects/couchbase-archive -r repo -c 172.20.1.1 -u Administrator -p asdasd
Backing up to '2021-02-09T13_35_21.580950579Z'
Copied all data in 504.852625ms (Avg. 56.00KB/Sec)                                                                                            0 items / 56.00KB
[=====================================================================================================================================================] 100.00%
Backup completed successfully
Backed up bucket "travel-sample" succeeded
Mutations backed up: 0, Mutations failed to backup: 0
Deletions backed up: 0, Deletions failed to backup: 0
Skipped due to purge number or conflict resolution: Mutations: 0 Deletions: 0

$ cbbackupmgr backup -a ~/Projects/couchbase-archive -r repo -c 172.20.1.1 -u Administrator -p asdasd --fullbackup
Backing up to '2021-02-09T13_35_24.18890408Z'
Copied all data in 2.85286061s (Avg. 10.53MB/Sec)                                                                                         31591 items / 21.06MB
[=====================================================================================================================================================] 100.00%
Backup completed successfully
Backed up bucket "travel-sample" succeeded
Mutations backed up: 31591, Mutations failed to backup: 0
Deletions backed up: 0, Deletions failed to backup: 0
Skipped due to purge number or conflict resolution: Mutations: 0 Deletions: 0

## [](#collection-aware-backups)COLLECTION AWARE BACKUPS

The 7.0.0 release of Couchbase Server introduced collections supports. The following section will briefly discuss how this affects backups created by cbbackupmgr.

### [](#what-makes-a-backup-collection-aware)What makes a backup collection aware?

cbbackupmgr is not limited to only backing up the cluster version it was released with; it may be used to backup previous versions of Couchbase Server. This means that cbbackupmgr is able to create backups which are collection aware or unaware.

The distinction between collection aware/unaware is simple; if you backup a cluster prior to 7.0.0 your backup will be collection unaware. If you backup a cluster version which supports collections (starting at 7.0.0) your backup will be collection aware.

The default behavior of backup for the cluster versions which support collections is to back up all available scopes/collections in a bucket.

### [](#what-if-i-dont-want-to-use-collections)What if I don’t want to use collections?

This is perfectly valid use case and is supported by Couchbase Server and cbbackupmgr. When interacting with backups created of a collection aware cluster, cbbackupmgr will only output collection aware information if the backup contains a non-default collection manifest (which implies the use of collections).

This means you may continue using cbbackupmgr without needing to interact with collections. Note that you may still need to update/change the flags being passed to some sub-commands. For example, when examining a backup, you will still need to use the `--collection-string` flag. For example instead of `--bucket default` you should supply `--collection-string default`.

## [](#DISCUSSION)DISCUSSION

This command always backs up data incrementally. By using the vbucket sequence number that is associated with each item, the backup command is able to examine previous backups in order to determine where the last backup finished.

When backing up a cluster, data for each bucket is backed up in the following order:

* `Bucket Settings`
* `View Definitions`
* `Global Secondary Index (GSI) Definitions`
* `Full-Text Index Definitions`
* `Key-Value Data`

The backup command will store everything that is persisted to disk on the Couchbase Server nodes at the time the backup is started. Couchbase server is consistent at a vBucket level and not across a whole bucket. The tool tries to provide a strong consistency window by opening all connection to every node at the same time. Being a distributed system there are times when this is not possible such as when the cluster is under-resourced or there are network issues. These may affect the consistency of the backup across the vBuckets. `cbbackupmgr backup` provides an Enterprise Edition, developer preview feature that checks that the backup is inside a consistency window (see `--consistency-check`).

## [](#rollback)ROLLBACK

During a backup, it’s possible for cbbackupmgr to receive a rollback from the cluster; this will be returned to you (the user) in the form of a message similar to `client received rollback, either purge this backup or create a new backup repository`.

There are two sensible actions which can be taken at this point (which are briefly alluded in the above message):

1. You can rerun the backup using the `--purge` flag, this will remove the failed backup creating a new incremental backup if possible, otherwise falling back to creating a full backup.
2. You could create a new backup repository and begin creating backups there, this method has the advantage of preserving any possible data which was backed up prior to receiving the rollback.

In most cases, option one will be sufficient, however, if may be the case that the partial backup taken by cbbackupmgr contains data which you don’t want to delete. In this case, option two allows you to retain this data which could be restored using the `--restore-partial-backups` flag.

Note that the `--restore-partial-backups` flag is only supported for local backups; backups stored in object store which failed due to a rollback must be purged using the `--purge` flag.

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

## [](#files)FILES

restrictions.json

Keeps a list of restrictions used to ensure data is not restored to a cluster with an incompatible version or a bucket with an incompatible conflict resolution type.

bucket-config.json

Stores the bucket configuration settings for a bucket.

views.json

Stores the view definitions for a bucket.

gsi.json

Stores the global secondary index (GSI) definitions for a bucket.

full-text.json

Stores the full-text index definitions for a bucket.

users.json

The config command creates a users configuration file in the backup repository called users.json. This file contains the users configuration for all the users in the cluster including their roles, permissions and groups they are a part of. It should never be modified and treated as a read-only file.

index\_\*.sqlite.0

Stores an index of document keys in the given vBucket.

data\_\*.rift.0

Stores the document values in the given vBucket.

## [](#see-also)SEE ALSO

[cbbackupmgr-config](cbbackupmgr-config.md), [cbbackupmgr-info](cbbackupmgr-info.md), [cbbackupmgr-strategies](cbbackupmgr-strategies.md), [cbbackupmgr-cloud](cbbackupmgr-cloud.md), [cbbackupmgr-encryption](cbbackupmgr-encryption.md), [cbbackupmgr-network-filesystems](cbbackupmgr-network-filesystems.md)

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite