[View original HTML](/server/7.6/backup-restore/cbbackupmgr-merge.html)

Merges two or more backups together

## [](#synopsis)SYNOPSIS

cbbackupmgr merge [--archive <archive_dir>] [--repo <repo_name>]
                  [--start <start>] [--end <end>]
                  [--date-range <range>] [--threads <num>]
                  [--no-progress-bar] [--passphrase <passphrase>]
                  [--km-key-url <url>] [--km-endpoint <endpoint>]
                  [--km-region <region>] [--km-access-key-id <id>]
                  [--km-secret-access-key <key>] [--km-auth-file <path>]

## [](#description)DESCRIPTION

The merge command is an Enterprise Edition command which can be used to merge two or more backups together. Since cbbackupmgr is a utility that always attempts to take incremental backups it is sometimes desirable to reduce the number of files and reclaim disk space. The merge command will always reclaim space taken up by metadata from each individual backup, and with the SQLite format it will deduplicate identical keys in backup files merged together in order to create a single smaller backup file. Note that this deduplication does not currently happen with the Rift format.

Doing merges should replace the full backup step by taking multiple incremental backups of a Couchbase cluster and converting them into a single full backup. Since this process takes place in the backup archive there is no cluster overhead to merging data together. See [cbbackupmgr-strategies](cbbackupmgr-strategies.md) for suggestions on using the merge command in your backup process.

## [](#options)OPTIONS

Below are a list of required parameters for the merge command.

### [](#required)Required

\-a,--archive <archive\_dir>

The archive directory to merge data in.

\-r,--repo <repo\_name>

The name of the backup repository to merge data in.

### [](#optional)Optional

\--start <start>

The first backup to merge. See [START AND END](#START%5FAND%5FEND) for information on what values are accepted.

\--end <end>

The final backup to merge. See [START AND END](#START%5FAND%5FEND) for information on what values are accepted.

\--date-range <range>

This flag will accept a comma separated range in the same formats as `--start` and `--end`. See [START AND END](#START%5FAND%5FEND) section for more information on the accepted formats.

\-t,--threads <num>

Specifies the number of concurrent vBuckets that will be merged at a time. Increasing the threads will make the merge faster but will also increase the resource used by the client. This parameter defaults to 1 but it is recommended to increase it to match the number of CPUs in the client machine.

\--no-progress-bar

By default, a progress bar is printed to stdout so that the user can see how long the merge is expected to take, the amount of data that is being transferred per second, and the amount of data that has been merged. Specifying this flag disables the progress bar and is useful when running automated jobs.

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

## [](#examples)EXAMPLES

In order to merge data, you need to have a backup repository with at least two backups. Below is an example of merging a backup repository named "example" that has two backups in it. The first backup contains the initial dataset. The second backup was taken after four items were updated.

$ cbbackupmgr info -a /data/backups -r example --all
| Repo
| ----
| Name    | Size     | # Backups | Encrypted | Point in Time |
| example | 24.11MiB | 2         | false     | false         |
|
| Backups
| -------
|
| * Backup
|   ------
|   Name                            | Size    | Type | Complete |
|   2020-06-02T07_58_32.42306+01_00 | 2.38MiB | FULL | true     |
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
|     example | 2.38MiB |
|
|     Services
|     --------
|
|       Data
|       ----
|       Mutations | Deletions | Size    |
|       8192      | 0         | 2.38MiB |
|
|         Point in Time
|         -------------
|         Mutations | Deletions | Duplicate Size |
|         8192      | 0         | 0B             |
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
|   Name                            | Size      | Type | Complete |
|   2020-06-03T08_00_22.62763+01_00 | 654.70KiB | INCR | true     |
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
|     Name    | Size      |
|     example | 654.70KiB |
|
|     Services
|     --------
|
|       Data
|       ----
|       Mutations | Deletions | Size      |
|       4         | 0         | 654.70KiB |
|
|         Point in Time
|         -------------
|         Mutations | Deletions | Duplicate Size |
|         4         | 0         | 0B             |
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

$ cbbackupmgr merge -a /data/backup -r example --start 2020-06-02T07_58_32.42306+01_00 \
 --end 2020-06-03T08_00_22.62763+01_00

$ cbbackupmgr info -a /data/backups -r example --all
| Repo
| ----
| Name    | Size    | # Backups | Encrypted | Point in Time |
| example | 2.38MiB | 1         | false     | false         |
|
| Backups
| -------
|
| * Backup
|   ------
|   Name                            | Size    | Type         | Complete |
|   2020-06-03T08_00_22.62763+01_00 | 2.38MiB | MERGE - FULL | true     |
|
|   Merged Range
|   ------------
|   Start               | End                 | Count |
|   2020-06-02T07_58_32 | 2020-06-03T08_00_22 | 2     |
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
|     example | 2.38MiB |
|
|     Services
|     --------
|
|       Data
|       ----
|       Mutations | Deletions | Size    |
|       8192      | 0         | 2.38MiB |
|
|         Point in Time
|         -------------
|         Mutations | Deletions | Duplicate Size |
|         8192      | 0         | 0B             |
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

Upon completion of the merge the number of items in the backup files is the same. This is because the keys in the second backup were also contained in the first backup, but the keys in the second backup contained newer values and overwrote the keys in the first backup during the merge. The timestamp of the backup folder is also the same as the timestamp of the latest backup because the new backup is a snapshot of the cluster at that point in time.

## [](#discussion)DISCUSSION

It is important that internally the merge command is able to merge backups together without corrupting the backup archive or leaving it in an intermediate state. In order to ensure this behavior cbbackupmgr always creates a new backup and completely merges all data before removing any backup files. When a merge is started a .merge\_status file is created in the backup repository to track the merge progress. cbbackupmgr then copies the first backup to the .merge folder and begins merging the other backups into .merge folder. After each backup is merged the .merge\_status file is updated to track the merge progress. if all backups are merged together successfully, cbbackupmgr will start deleting the old backups and then copy the fully merged backup into a folder containing the same name as the backup specified by the --end flag. If the cbbackupmgr utility fails during this process, then the merge will either be completed or the partial merge files will be removed from the backup repository during the next invocation of the cbbackupmgr.

Since the merge command creates a new backup file before it removes the old ones it is necessary to have at least as much free space as the backups that are to be merge together.

For more information on suggestions for how to use the merge command in your backup process see [cbbackupmgr-strategies](cbbackupmgr-strategies.md)

## [](#environment-and-configuration-variables)ENVIRONMENT AND CONFIGURATION VARIABLES

CB\_ARCHIVE\_PATH

Specifies the path to the backup archive. If the archive path is supplied as a command line argument then this value is overridden.

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

.merge\_status

File storing information on the progress of the merge.

.merge

Directory storing intermediate merge data.

## [](#see-also)SEE ALSO

[cbbackupmgr-info](cbbackupmgr-info.md), [cbbackupmgr-strategies](cbbackupmgr-strategies.md), [cbbackupmgr-encryption](cbbackupmgr-encryption.md), [cbbackupmgr-network-filesystems](cbbackupmgr-network-filesystems.md)

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite