[View original HTML](/server/current/backup-restore/cbbackupmgr.html)

A utility for backing up and restoring a Couchbase cluster

## [](#synopsis)SYNOPSIS

cbbackupmgr [--version] [--help] <command> [<args>]

## [](#description)DESCRIPTION

cbbackupmgr is a high performance backup and restore client for Couchbase Server.

See [cbbackupmgr-tutorial](cbbackupmgr-tutorial.md) to get started. For more information on how specific commands work you can run "cbbackupmgr <command> --help". For backup strategies see [cbbackupmgr-strategies](cbbackupmgr-strategies.md).

## [](#options)OPTIONS

\--version

Prints the cbbackupmgr suite version that the cbbackupmgr program came from.

\--help

Prints the synopsis and a list of commands. If a cbbackupmgr command is named, this option will bring up the manual page for that command.

## [](#cbbackupmgr-commands)CBBACKUPMGR COMMANDS

[cbbackupmgr-backup](cbbackupmgr-backup.md)

Backs up data from a Couchbase cluster.

[cbbackupmgr-collect-logs](cbbackupmgr-collect-logs.md)

Collects diagnostic information.

[cbbackupmgr-compact](cbbackupmgr-compact.md)

Compacts a backup.

[cbbackupmgr-config](cbbackupmgr-config.md)

Creates a new backup repository.

[cbbackupmgr-info](cbbackupmgr-info.md)

Command that displays information about the backups in the archive.

[cbbackupmgr-merge](cbbackupmgr-merge.md)

Merges backups together.

[cbbackupmgr-remove](cbbackupmgr-remove.md)

Deletes a backup repository.

[cbbackupmgr-restore](cbbackupmgr-restore.md)

Restores a backup from the archive.

## [](#identifier-terminology)IDENTIFIER TERMINOLOGY

<archive>

The root directory containing multiple backup repositories. This is the top-level backup directory and contains all backup data as well as backup logs.

<repository>

Contains a backup configuration used for taking actual backups. A repository should be created for a specific Couchbase cluster and it will contain multiple incremental backups.

<backup>

A backup of a Couchbase cluster at a given point in time. All backups are incremental backups.

<bucket>

A backup may consist of one or more buckets. Each bucket is stored separately.

<collection\_string>

A dot separated string which indicates the location of documents on a Couchbase cluster. Collection strings are expected in the format 'bucket.scope.collection'. The collection string 'food.produce.fruit' refers to the 'fruit' collection inside the 'produce' scope which is contained in the 'food' bucket. In the case where the bucket name contains a '.' character you should escape the '.' character. e.g. 'fo\\.od.produce.fruit' is a valid collection string. You are also free to omit the scope/collection portion of the collection string; in this case the absence of a scope/collection is treated as a wildcard indicating all collections inside a scope or all scopes inside a bucket. For example the collection string 'food.produce' indicates that we are that we are talking about all of the collections that fall inside of the 'produce' scope inside of the 'food' bucket.

## [](#environment-and-configuration-variables)ENVIRONMENT AND CONFIGURATION VARIABLES

CB\_CLUSTER

Specifies the hostname of the Couchbase cluster to connect to. If the hostname is supplied as a command line argument then this value is overridden.

CB\_USERNAME

Specifies the username for authentication to a Couchbase cluster. If the username is supplied as a command line argument then this value is overridden.

CB\_PASSWORD

Specifies the password for authentication to a Couchbase cluster. If the password is supplied as a command line argument then this value is overridden.

CB\_CLIENT\_CERT

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `CB_CLIENT_KEY` as an alternative to the `CB_USERNAME` and `CB_PASSWORD` variables. See the [\[CERTIFICATE\_AUTHENTICATION\]](#CERTIFICATE%5FAUTHENTICATION)section for more information.

CB\_CLIENT\_CERT\_PASSWORD

The password for the certificate provided to the `CB_CLIENT_CERT` variable, when using this variable, the certificate/key pair is expected to be in the PKCS#12 format. See the [\[CERTIFICATE\_AUTHENTICATION\]](#CERTIFICATE%5FAUTHENTICATION) section for more information.

CB\_CLIENT\_KEY

The path to the client private key whose public key is contained in the certificate provided to the `CB_CLIENT_CERT` variable. May be supplied with `CB_CLIENT_CERT` as an alternative to the `CB_USERNAME` and `CB_PASSWORD`variables. See the [\[CERTIFICATE\_AUTHENTICATION\]](#CERTIFICATE%5FAUTHENTICATION) section for more information.

CB\_CLIENT\_KEY\_PASSWORD

The password for the key provided to the `CB_CLIENT_KEY` variable, when using this variable, the key is expected to be in the PKCS#8 format. See the [\[CERTIFICATE\_AUTHENTICATION\]](#CERTIFICATE%5FAUTHENTICATION) section for more information.

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

## [](#discussion)DISCUSSION

The cbbackupmgr command is used for backing up Couchbase clusters, managing those backups, and restoring them.

The cbbackupmgr command was built around the concept of taking only incremental backups. This concept is important because as the data in a cluster grows it becomes increasingly difficult to take full backups in a reasonable amount of time. By taking incremental backups we are able to reduce the time it takes to backup a cluster by ensuring that we transfer the smallest amount of data possible each time we back the cluster up.

A consequence of taking incremental backups is that we must know about the previous backups that we have taken in order to know where we left off. This means that the cbbackupmgr command must manage the backups it has taken. The cbbackupmgr command does this by using the concept of a backup archive and a backup repository. A backup repository is a directory that contains a backup configuration for backing up a specific cluster. Normally there will be one backup repository per Couchbase cluster. Each time you want to back up this cluster you will specify this backup repository with the cbbackupmgr-backup command and the backup tool will automatically find where the last backup finished and incrementally backup new data in that cluster.

The backup archive is the top-level directory and contains one or more backup repositories and a logs folder. Logging for all backup repositories is contained in the logs folder in the backup.log file.

In an incremental approach the amount of data being stored in the backup archive is always increasing. To handle this issue the backup command allows backups to be merged together. This allows data to be deduplicated resulting in a single backup that takes up less disk space than the multiple previous backups. More information about how to take advantage of incremental backups and merges is contained in [cbbackupmgr-strategies](cbbackupmgr-strategies.md).

The minimum hardware requirement for running cbbackupmgr is four CPU cores, 8GiB RAM. The recommend hardware is sixteen CPU cores, 16GiB RAM and SSD disks.

## [](#operations-during-major-cluster-configuration-changes)OPERATIONS DURING MAJOR CLUSTER CONFIGURATION CHANGES

Operations (commands or sub-commands) which connect to a cluster are not supported during major cluster configuration changes.

For example, performing an import/export, making a backup or performing a restore whilst changing the TLS configuration/security settings is unsupported.

These types of changes (e.g. changing the TLS mode to strict) are not expected to be time consuming so it’s generally expected that operations should be started after completing the configuration change.

Please note that this does not include rebalances; operations may be performed during a rebalance. The reason for this distinction, is that major cluster configuration changes are generally quick, whilst rebalances for large data sets may be time consuming.

## [](#further-documentation)FURTHER DOCUMENTATION

A tutorial for getting started with the backup command is also available in [cbbackupmgr-tutorial](cbbackupmgr-tutorial.md).

A guide for production backup strategies is available in [cbbackupmgr-strategies](cbbackupmgr-strategies.md).

## [](#authors)AUTHORS

cbbackupmgr is a Couchbase Enterprise Edition tool and was written by Couchbase.

## [](#reporting-bugs)REPORTING BUGS

Report urgent issues to the Couchbase Support Team at [support@couchbase.com](mailto:support@couchbase.com). Bugs can be reported to the Couchbase Jira Bug Tracker at <http://www.couchbase.com/issues>.

## [](#see-also)SEE ALSO

[cbbackupmgr-tutorial](cbbackupmgr-tutorial.md), [cbbackupmgr-config](cbbackupmgr-config.md), [cbbackupmgr-backup](cbbackupmgr-backup.md), [cbbackupmgr-restore](cbbackupmgr-restore.md)

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite