[View original HTML](/server/7.2/backup-restore/cbbackupmgr-config.html)

Creates and configures a new backup repository

## [](#synopsis)SYNOPSIS

cbbackupmgr config [--archive <archive_dir>] [--repo <repo_name>]
                   [--include-data <collection_string_list>]
                   [--exclude-data <collection_string_list>]
                   [--disable-bucket-config] [--disable-views] [--disable-eventing]
                   [--disable-gsi-indexes] [--disable-ft-indexes]
                   [--disable-data] [--vbucket-filter <integer_list>]
                   [--disable-cluster-analytics] [--disable-analytics] [--disable-ft-alias]
                   [--disable-bucket-query] [--disable-cluster-query]
                   [--obj-access-key-id <access_key_id>] [--obj-cacert <cert_path>]
                   [--obj-endpoint <endpoint>] [--obj-no-ssl-verify]
                   [--obj-region <region>] [--obj-staging-dir <staging_dir>]
                   [--obj-secret-access-key <secret_access_key>]
                   [--s3-force-path-style] [--s3-log-level <level>]
                   [--readme-author <name>] [--point-in-time]
                   [--encrypted] [--passphrase <passphrase>]
                   [--encryption-algo <algo>] [--derivation-algo <algo>]
                   [--km-key-url <url>] [--km-endpoint <endpoint>]
                   [--km-region <region>] [--km-access-key-id <id>]
                   [--km-secret-access-key <key>] [--km-auth-file <path>]

## [](#description)DESCRIPTION

Creates a new backup repository with a new backup configuration. The configuration created is used for all backups in this backup repository.

By default a backup configuration is created that will backup all buckets in the cluster. Each bucket will have its bucket configuration, views definitions, gsi index definitions, full-text index definitions, and data backed up. Specifying various flags, the config command can modify the configuration to backup a subset of the data.

Once a backup repository is created its configuration cannot be changed.

## [](#options)OPTIONS

Below are a list of required and optional parameters for the config command.

### [](#required)Required

\-a,--archive <archive\_dir>

The directory where the new backup repository will be created. If it does not already exist, an attempt will be made to create it. When configuring an archive in S3 you must prefix the archive path with `s3://${BUCKET_NAME}/`.

\-r,--repo <repo\_name>

The name of the new backup repository.

### [](#optional)Optional

\--include-data <collection\_string\_list>

Modifies the repository configuration to backup only the data specified in the <collection\_string\_list>. This flag takes a comma separated list of collection strings and can’t be specified at the same time as `--exclude-data`. Note that including data at the scope/collection level is an Enterprise Edition feature.

\--exclude-data <collection\_string\_list>

Modifies the repository configuration to skip restoring the data specified in the <collection\_string\_list>. This flag takes a comma separated list of collection strings and can’t be specified at the same time as `--include-data`. Note that excluding data at the scope/collection level is an Enterprise Edition feature.

\--disable-views

Modifies the repository configuration to disable backing up view definitions for all buckets.

\--disable-gsi-indexes

Modifies the repository configuration to disable backing up gsi index definitions for all buckets.

\--disable-ft-indexes

Modifies the repository configuration to disable backing up full-text index definitions for all buckets.

\--disable-ft-alias

Modifies the repository configuration to disable backing up full-text alias definitions.

\--disable-data

Modifies the repository configuration to disable backing up all key-value data for all buckets.

\--disable-cluster-analytics

Modifies the repository configuration to disable backing up the cluster level analytics data. For example, the Synonyms are backed up at the cluster level.

\--disable-analytics

Modifies the repository configuration to disable backing up analytics data.

\--disable-eventing

Modifies the repository configuration to disable backing up the Eventing service metadata.

\--disable-bucket-query

Modifies the repository configuration to disable backing up Query Service metadata for all buckets.

\--disable-cluster-query

Modifies the repository configuration to disable backing up the cluster level Query Service metadata.

\--vbucket-filter <list>

Specifies a list of VBuckets that should be backed up in the repo being created. VBuckets are specified as a comma separated list of integers. If this parameter is not set then all vbuckets are backed up. The comma separated list can also take sequences denoted as e.g: 0-5 this is equivalent to 0,1,2,3,4,5.

\--readme-author <name>

Specifies the name of the creator of the repository. This information will be recorded in a README file at the top-level of the repository.

\--point-in-time

(BETA) This enables Point in Time feature. Which is currently in Beta and is not supported, this should only be used in test environments. When it’s enabled cbbackupmgr will get historical data from the cluster. This will allow restoring to a single point in time. This will increase the amount of space needed to store the backup. The cluster also has to have Point In Time configured to use this feature.

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

### [](#encryption-developer-preview)Encryption (Developer Preview)

\--encrypted

Enables configuring an encrypted repository.

\--encryption-algo <algo>

The encryption algorithm to use. Currently supported are \[AES256CBC, AES256GCM\]. Defaults to AES256GCM.

\--derivation-algo <algo>

The derivation algorithm used when running with passphrase that creates the repository encryption key. Currently supported \[ARGON2ID, PBKDF2\]. Defaults to ARGON2ID.

\--passphrase <passphrase>

Passphrase can be used instead of an external key manager. This is not supported on production and should only be used in development or testing.

\--km-key-url <url>

Provides the Key Identifier in the external Key Management system. Currently supported KMSs are AWS KMS, GCP KMS, Azure KeyVault, HashiCorp Vault Transit secrets engine. The option can also be provided using the environmental variable `CB_KM_KEY_URL`. For more on how to authenticate using the different providers see [cbbackupmgr-encryption](cbbackupmgr-encryption.md).

For AWS the expected key format is `awskms://<KEY-ID|KEY-ALIAS>`, for example `awskms://alias\keyAlias`.

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

\--km-auth-file <path>

 The path to a file containing the authentication credentials for the key management service. It can also be provided via the `CB_KM_AUTH_FILE`environmental variable. Please refer to [cbbackupmgr-encryption](cbbackupmgr-encryption.md) for the required authentication for each provider. :!config:

## [](#examples)EXAMPLES

The config command is used to create a backup repository and define the repositories backup configuration. In the examples below, the backup archive is located at /data/backups. Since this is the first backup repository we are creating in a new backup archive, we need to ensure that /data/backups is an empty directory. Archives are created automatically if an archive doesn’t already exist at the archive path, but are only created if the directory at that path is empty. In order to create a backup repository called "example" with the default configuration use the following command:

$ cbbackupmgr config -a /data/backups -r example

Upon creation of a new backup repository there will be a new directory in the backup archive containing a backup configuration. You can see this new directory using the cbbackupmgr-info\[1\] command.

$ cbbackupmgr info -a ~/data/backups
Name     | UUID                                  | Size  | # Repos  |
backups  | 0db3337c-96b0-4b3a-a7fb-bbfd53790e5f  | 0B    | 1        |

*  Name     | Size  | # Backups  |
*  example  | 0B    | 0          |

Using the optional parameters of the create command, you can modify the backup configuration settings. To create a backup repository with a backup configuration that only backs up the buckets "airline\_data" and "ticket\_prices" and does not back up bucket configuration data, you can run the following:

$ cbbackupmgr config -a /data/backups -r example \
 --include-data airline_data,ticket_prices --disable-bucket-config

To create a backup repository with a backup configuration that backs up only data on all buckets, you can run the following command:

$ cbbackupmgr config -a /data/backups -r example --disable-bucket-config \
 --disable-views --disable-gsi-indexes --disable-ft-indexes

When creating an archive in an object store such as S3 due care must be taken to ensure that the provided directory is empty and can be managed by cbbackupmgr.

$ cbbackupmgr config -a s3://bucket/archive -r repo --obj-staging-dir /staging

## [](#discussion)DISCUSSION

Though not required, it is recommended that there is a single backup repository per cluster. Backup repositories are managed so that all backups can be taken incrementally and merged together as backup data ages. Backing up in this manner allows backups to transfer the least amount of data necessary which reduces back up time and cluster resource usage. For more details on backup strategies see cbbackupmgr-strategies\[7\].

When a backup repository is created, it should only be modified by the cbbackupmgr utility. Any modifications done outside of this utility can cause corruption of backup files.

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

## [](#files)FILES

backup-meta.json

The config command creates a backup configuration file in the backup repository called backup-meta.json. This file contains the backup configuration for all backups run in the backup repository it was created in. It should never be modified and treated as a read-only file.

## [](#see-also)SEE ALSO

[cbbackupmgr-info](cbbackupmgr-info.md), [cbbackupmgr-strategies](cbbackupmgr-strategies.md), [cbbackupmgr-cloud](cbbackupmgr-cloud.md), [cbbackupmgr-encryption](cbbackupmgr-encryption.md)

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite