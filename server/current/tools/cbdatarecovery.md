---
title: cbdatarecovery
editUrl: https://github.com/couchbase/backup/edit/morpheus/docs/modules/tools/pages/cbdatarecovery.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:tools:cbdatarecovery.adoc[]
---

[View original HTML](/server/current/tools/cbdatarecovery.html)

# cbdatarecovery

Transfers key value data from a Couchbase Server data directory into an active cluster.

## [](#synopsis)SYNOPSIS

cbdatarecovery [--cluster <connection_string>] [--cacert <path>]
               [--username <username>] [--password <password>]
               [--client-cert <path>] [--client-cert-password <password>]
               [--client-key <path>] [--client-key-password <password>]
               [--data-path <path>] [--dump-bucket-deks-path <path>]
               [--gosecrets-path <path>] [--gosecrets-config-path <path>]
               [--master-password <password>] [--map-data <mappings>]
               [--vbucket-filter <filter>] [--filter-keys <regex>]
               [--filter-values <regex>] [--replace-ttl <type>]
               [--replace-ttl-with <timestamp>]
               [--include-data <collection_strings>]
               [--exclude-data <collection_strings>]
               [--vbucket-state <state>] [--log-file <path>]
               [--threads <threads>] [--force-updates]
               [--create-missing-collections] [--no-ssl-verify]
               [--skip-wal-recovery] [--verbose] [--no-progress-bar]
               [--start-seqno <seqno> [--end-seqno <seqno>] [--version]

## [](#description)DESCRIPTION

cbdatarecovery transfers key value data stored in Couchstore or Magma files from a Couchbase Server data directory into an active cluster. This can be used to recover data from offline/failed over nodes.

## [](#options)OPTIONS

### [](#required)Required

\-c, --cluster <connection\_string>

A connection string representing a Couchbase node/cluster which will be the destination for the recovered data. See the [HOST FORMATS](#HOST%5FFORMATS) section for more information.

\-u,--username <username>

The username for cluster authentication. The user must have the appropriate privileges to recover data.

\-p,--password <password>

The password for cluster authentication. The user must have the appropriate privileges to recover data. If not password is supplied to this option then you will be prompted to enter your password.

\--client-cert <path>

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `--client-key` as an alternative to the `--username` and `--password` flags. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION)section for more information.

\--client-cert-password <password>

The password for the certificate provided to the `--client-cert` flag, when using this flag, the certificate/key pair is expected to be in the PKCS#12 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

\--client-key <path>

The path to the client private key whose public key is contained in the certificate provided to the `--client-cert` flag. May be supplied with `--client-cert` as an alternative to the `--username` and `--password`flags. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

\--client-key-password <password>

The password for the key provided to the `--client-key` flag, when using this flag, the key is expected to be in the PKCS#8 format. See the [CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)](#CERTIFICATE%5FAUTHENTICATION) section for more information.

\-d, --data-path <path>

The path to a Couchbase Server data directory. For example `/opt/couchbase/lib/couchbase/data`.

### [](#optional)Optional

\--cacert <path>

Specifies a CA certificate that will be used to verify the identity of the server being connecting to. Either this flag or the --no-ssl-verify flag must be specified when using an SSL encrypted connection.

\--dump-bucket-deks-path <path>

The path to the dump-bucket-deks executable. This should only be used if the data is encrypted, and a non-standard path is required.

\--gosecrets-path <path>

The path to the gosecrets executable. This should only be used if the data is encrypted, and a non-standard path is required.

\--gosecrets-config-path <path>

The path to the gosecrets config file. This should only be used if the data is encrypted, and a non-standard path is required.

\--master-password <password>

The Couchbase master password for the data. This should only be used if the data is encrypted, and a non-empty master password was used to encrypt the data.

\--map-data <mappings>

Specified when you want to transfer source data into a different location. For example this argument may be used to remap buckets/scopes/collections with the restriction that they must be remapped at the same level. For example a bucket may only be remapped to a bucket, a scope to a scope and a collection to a collection. The argument expects a comma separated list of collection string mappings e.g. `bucket1=bucket2,bucket3.scope1=bucket3.scope2,bucket4.scope.collection1=bucket4.scope.collection2`

\--vbucket-filter <filter>

Specifies a list of vBuckets that should be transferred. vBuckets are specified as a comma separated list of integers/ranges. For example `0,1,2`and `0-2` represent the same subset of vBuckets. If no filter is provided, then all vBuckets will be transferred.

\--filter-keys <regex>

Only transfer data where the key matches a particular regular expression. The regular expressions provided must follow [RE2 syntax](https://github.com/google/re2/wiki/Syntax).

\--filter-values <regex>

Only transfer data where the value matches a particular regular expression. The regular expressions provided must follow [RE2 syntax](https://github.com/google/re2/wiki/Syntax).

\--replace-ttl <type>

Sets a new expiration (time-to-live) value for the specified keys. This parameter can either be set to "none", "all" or "expired" and should be used along with the --replace-ttl-with flag. If "none" is supplied then the TTL values are not changed. If "all" is specified then the TTL values for all keys are replaced with the value of the --replace-ttl-with flag. If "expired" is set then only keys which have already expired will have the TTL’s replaced.

\--replace-ttl-with <timestamp>

Updates the expiration for the keys specified by the --replace-ttl parameter. The parameter has to be set when --replace-ttl is set to "all". There are two options, RFC3339 time stamp format (2006-01-02T15:04:05-07:00) or "0". When "0" is specified the expiration will be removed. Please note that the RFC3339 value is converted to a Unix time stamp on the cbbackupmgr client. It is important that the time on both the client and the Couchbase Server are the same to ensure expiry happens correctly.

\--include-data <collection\_strings>

Only transfer data included in this comma list of collection strings. Note that this flag can’t be specified at the same time `--exclude-data`.

\--exclude-data <collection\_strings>

Don’t transfer the data for the buckets/scopes/collections in this comma separated list of collection strings. Note that this flag can’t be specified at the same time as `--include-data`.

\--vbucket-state <state>

Only transfer vBuckets which are in the provided stated. Accepts the values `active`, `replica` or `dead`.

\--threads <threads>

Specifies the number of concurrent clients to use when transferring data. Fewer clients means restores will take longer, but there will be less cluster resources used to complete the restore. More clients means faster restores, but at the cost of more cluster resource usage. This parameter defaults to 1 if it is not specified and it is recommended that this parameter is not set to be higher than the number of CPUs on the machine where the restore is taking place.

\--force-updates

Forces data in the Couchbase cluster to be overwritten even if the data in the cluster is newer. By default updates are not forced and all updates use Couchbase’s conflict resolution mechanism to ensure that if newer data exists on the cluster that is not overwritten by older restore data.

\--create-missing-collections

Automatically create any scopes/collections which exist in the data directory on disk but not in the remote cluster. This behavior is disabled by default.

\--no-ssl-verify

Skips the SSL verification phase. Specifying this flag will allow a connection using SSL encryption, but will not verify the identity of the server you connect to. You are vulnerable to a man-in-the-middle attack if you use this flag. Either this flag or the --cacert flag must be specified when using an SSL encrypted connection.

\--skip-wal-recovery

For Magma buckets skip replaying the WAL.

\--verbose

Increase logging verbosity; useful when debugging. Disabled by default.

\--no-progress-bar

By default, a progress bar is printed to stdout so that the user can see how long the transfer is expected to take, the amount of data that is being transferred per second, and the amount of data that has been transferred. Specifying this flag disables the progress bar and is useful when running automated jobs.

\--start-seqno

The seqno to start recovery from. This can only be passed if a single vBucket has been specified in `--vbucket-filter`.

\--end-seqno

The seqno to end recovery at. This can only be passed if a single vBucket has been specified in `--vbucket-filter`. A value of `0` causes us to stream to the end.

\--version

Prints the cbdatarecovery suite version that the cbdatarecovery program came from.

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

## [](#automatic-collection-creation)AUTOMATIC COLLECTION CREATION

By design, users may not recreate the `_default` collection once it has been deleted. Therefore, this means that the `_default` collection can’t (and won’t) be recreated if it’s missing. Before performing a transfer, a check will take place to see if the `_default` collection will be required when it’s missing. If this is the case, the command will exit early and you will be required to remap the `_default` collection using the `--map-data` flag.

## [](#REMAPPING)REMAPPING

During a transfer, scopes/collections can be remapped from one location to another. There are several rules that are enforced when remapping scopes/collections, they are as follows:

* You may not remap the `_default` scope (discussed in THE DEFAULT SCOPE).
* You may not restore users while remapping scopes/collections, the restoring of users will be skipped.
* You may only remap scopes/collections at the same level meaning scopes may be remapped to other scopes, and collections to other collections, however, a scope can’t be remapped to a collection or vice versa.
* Scopes/collections may only be remapped within the same bucket. For example the mapping `bucket1.scope.collection=bucket2.scope.collection` is invalid.
* Scopes/collections may only be remapped once. For example the mapping `bucket1.scope1=bucket1.scope2,bucket1.scope1=bucket1.scope3` is invalid.
* Remapping may only take place at one level at once meaning that if a parent bucket/scope is already remapped, the child scopes/collections may not also be remapped. For example the mapping `bucket1.scope1=bucket1.scope2,bucket1.scope1.collection1=bucket1.scope3.collection9`is invalid.

### [](#remapping-a-scopecollection-without-renaming)REMAPPING A SCOPE/COLLECTION WITHOUT RENAMING

During a transfer, it’s possible for a scope/collection to encounter a conflict (for example, because it has been recreated). It may not be preferable to rename the scope/collection during the transfer.

For this reason, the `--map-data` flag, allows you to remap a scope/collection to itself; this indicates that the scope/collection that exists in the target (with a different id) should be treated as the same.

As an example, the following error message indicates that a collection has been recreated prior to a restore.

Error restoring cluster: collection 8 with name 'collection1' in the scope '_default' exists with a different name/id on the cluster, a manual remap is required

Using the `--map-data` flag with the argument `bucket._default.collection1=bucket._default.collection1` would cause `cbbackupmgr` to treat `collection1` (with id 8) as `collection1` (with the id it exists with in the target).

### [](#the-default-scope)THE DEFAULT SCOPE

As mentioned in AUTOMATIC COLLECTION CREATION, it’s not possible to recreate the `_default` scope/collection. This means you can’t remap the `_default`scope because the tool may be unable to create a destination scope/collection. This may be worked around by remapping each collection inside the `_default`scope.

### [](#bucket-to-collection-remapping)BUCKET TO COLLECTION REMAPPING

As discussed in REMAPPING, it’s not possible to remap data at different levels; buckets must be remapped to buckets, scopes to scopes and collections to collections. However, there is one supported edge case, which is remapping a bucket into a collection to allow migration from a collection unaware to collection aware datasets.

To remap a bucket into a collection using `--map-data` you may supply `--map-data bucket._default._default=bucket.scope.collection`. This functionality is compatible with cross bucket mapping, for example you may also supply `--map-data bucket1._default._default=bucket2.scope.collection`.

Note that once you’ve provided a mapping to remap a bucket into a collection you may not remap that bucket elsewhere. For example `--map-data bucket1._default._default=bucket2.scope.collection,bucket1=bucket3` is invalid.

### [](#remapping-multiple-data-sources-into-a-single-target-source)REMAPPING MULTIPLE DATA SOURCES INTO A SINGLE TARGET SOURCE

As outlined in the rules discussed in REMAPPING, it’s not possible to remap a bucket/scope/collection multiple times, however, it is possible to remap to a single destination multiple times. For example the mapping `bucket1=dest,bucket2=dest,bucket3=dest` is valid.

Although valid, this manor of remapping is dangerous and can result in data not being transferred due to conflicting key spaces. If this style of remapping is detected a warning will be printed before proceeding.

## [](#operations-during-major-cluster-configuration-changes)OPERATIONS DURING MAJOR CLUSTER CONFIGURATION CHANGES

Operations (commands or sub-commands) which connect to a cluster are not supported during major cluster configuration changes.

For example, performing an import/export, making a backup or performing a restore whilst changing the TLS configuration/security settings is unsupported.

These types of changes (e.g. changing the TLS mode to strict) are not expected to be time consuming so it’s generally expected that operations should be started after completing the configuration change.

Please note that this does not include rebalances; operations may be performed during a rebalance. The reason for this distinction, is that major cluster configuration changes are generally quick, whilst rebalances for large data sets may be time consuming.

## [](#examples)EXAMPLES

The cbdatarecovery tool may be used to recover key value data from a Couchbase Server data directory. By default, all the active vBuckets for all the detected buckets will be transferred.

$ cbdatarecovery -c 172.20.1.1 -u Administrator -p asdasd -d /opt/couchbase/lib/couchbase/data
Recovering to '172.20.1.1'
Copied all data in 505ms (Avg. 11.06MB/Sec)                                                                               17722 items / 11.06MB
[=====================================================================================================================================] 100.00%

| Transfer
| --------
| Status    | Avg Transfer Rate | Started At                        | Finished At                     | Duration |
| Succeeded | 11.06MB           | Tue, 23 Feb 2021 11:13:51 +0000/s | Tue, 23 Feb 2021 11:13:52 +0000 | 535ms    |

| Bucket
| ------
| Name        | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| beer-sample | Succeeded | 740.46KB    | 740.46KB/s        | Tue, 23 Feb 2021 11:13:51 +0000 | Tue, 23 Feb 2021 11:13:51 +0000 | 21ms     |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 1836     | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

| Bucket
| ------
| Name           | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| gamesim-sample | Succeeded | 29.82KB     | 29.82KB/s         | Tue, 23 Feb 2021 11:13:51 +0000 | Tue, 23 Feb 2021 11:13:51 +0000 | 3ms      |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 137      | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

| Bucket
| ------
| Name          | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| travel-sample | Succeeded | 10.31MB     | 10.31MB/s         | Tue, 23 Feb 2021 11:13:51 +0000 | Tue, 23 Feb 2021 11:13:52 +0000 | 222ms    |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 15749    | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

To recover only a subset of the available buckets, the `--include-data` and `--exclude-flags` may be used. Note that these flags are mutually exclusive meaning they can’t be used at the same time.

$ cbdatarecovery -c 172.20.1.1 -u Administrator -p asdasd -d /opt/couchbase/lib/couchbase/data --include-data travel-sample
Recovering to '172.20.1.1'
Copied all data in 273ms (Avg. 10.31MB/Sec)                                                                              15749 items / 10.31MB
[====================================================================================================================================] 100.00%

| Transfer
| --------
| Status    | Avg Transfer Rate | Started At                        | Finished At                     | Duration |
| Succeeded | 10.31MB           | Tue, 23 Feb 2021 11:14:14 +0000/s | Tue, 23 Feb 2021 11:14:15 +0000 | 300ms    |

| Bucket
| ------
| Name          | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| travel-sample | Succeeded | 10.31MB     | 10.31MB/s         | Tue, 23 Feb 2021 11:14:14 +0000 | Tue, 23 Feb 2021 11:14:15 +0000 | 189ms    |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 15749    | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

$ cbdatarecovery -c 172.20.1.1 -u Administrator -p asdasd -d /opt/couchbase/lib/couchbase/data --exclude-data travel-sample
Recovering to '172.20.1.1'
Copied all data in 202ms (Avg. 770.28KB/Sec)                                                                              1973 items / 770.28KB
[=====================================================================================================================================] 100.00%

| Transfer
| --------
| Status    | Avg Transfer Rate | Started At                        | Finished At                     | Duration |
| Succeeded | 770.28KB          | Tue, 23 Feb 2021 11:26:43 +0000/s | Tue, 23 Feb 2021 11:26:43 +0000 | 227ms

| Bucket
| ------
| Name        | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| beer-sample | Succeeded | 740.46KB    | 740.46KB/s        | Tue, 23 Feb 2021 11:26:43 +0000 | Tue, 23 Feb 2021 11:26:43 +0000 | 26ms     |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 1836     | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

| Bucket
| ------
| Name           | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| gamesim-sample | Succeeded | 29.82KB     | 29.82KB/s         | Tue, 23 Feb 2021 11:26:43 +0000 | Tue, 23 Feb 2021 11:26:43 +0000 | 4ms      |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 137      | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

To recover only a subset of the available vBuckets, the `--vbucket-filter` flag may be used. Note that by default all the available vBuckets will be recovered.

$ cbdatarecovery -c 172.20.1.1 -u Administrator -p asdasd -d /opt/couchbase/lib/couchbase/data --vbucket-filter 0-128
Recovering to '172.20.1.1'
Copied all data in 199ms (Avg. 5.31MB/Sec)                                                                                 7971 items / 5.31MB
[====================================================================================================================================] 100.00%

| Transfer
| --------
| Status    | Avg Transfer Rate | Started At                        | Finished At                     | Duration |
| Succeeded | 5.31MB            | Tue, 23 Feb 2021 11:28:05 +0000/s | Tue, 23 Feb 2021 11:28:05 +0000 | 227ms

| Bucket
| ------
| Name          | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| travel-sample | Succeeded | 5.31MB      | 5.31MB/s          | Tue, 23 Feb 2021 11:28:05 +0000 | Tue, 23 Feb 2021 11:28:05 +0000 | 114ms    |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 7971     | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

When recovering data to a different cluster or a cluster which has changed over time, it’s possible for some scopes/collections to have been dropped. This may cause the recovery to fail because the required scopes/collections no longer exist. The `--auto-create-collections` flag can be used to automatically create any missing scopes/collections.

$ cbdatarecovery -c 172.20.1.1 -u Administrator -p asdasd -d /opt/couchbase/lib/couchbase/data --auto-create-collections
Recovering to '172.20.1.1'
Copied all data in 534ms (Avg. 11.06MB/Sec)                                                                               17722 items / 11.06MB
[=====================================================================================================================================] 100.00%

| Transfer
| --------
| Status    | Avg Transfer Rate | Started At                        | Finished At                     | Duration |
| Succeeded | 11.06MB           | Tue, 23 Feb 2021 11:15:19 +0000/s | Tue, 23 Feb 2021 11:15:20 +0000 | 563ms    |

| Bucket
| ------
| Name        | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| beer-sample | Succeeded | 740.46KB    | 740.46KB/s        | Tue, 23 Feb 2021 11:15:20 +0000 | Tue, 23 Feb 2021 11:15:20 +0000 | 25ms     |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 1836     | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

| Bucket
| ------
| Name           | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| gamesim-sample | Succeeded | 29.82KB     | 29.82KB/s         | Tue, 23 Feb 2021 11:15:20 +0000 | Tue, 23 Feb 2021 11:15:20 +0000 | 3ms      |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 137      | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

| Bucket
| ------
| Name          | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| travel-sample | Succeeded | 10.31MB     | 10.31MB/s         | Tue, 23 Feb 2021 11:15:20 +0000 | Tue, 23 Feb 2021 11:15:20 +0000 | 200ms    |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 15749    | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

To recover only `replica` vBuckets, the `--vbucket-state` flag may be used. This flag accepts either `active` or `replica` resulting in the recovery of only the vBuckets in the provided state. Note that by default only `active`vBuckets will be recovered.

In the examples below, note the difference in the number of items recovered when recovering replica vBuckets; this is due to the way active/replica vBuckets are distributed.

$ cbdatarecovery -c 172.20.1.1 -u Administrator -p asdasd -d /opt/couchbase/lib/couchbase/data
Recovering to '172.20.1.1'
Copied all data in 279ms (Avg. 10.31MB/Sec)                                                                              15749 items / 10.31MB
[====================================================================================================================================] 100.00%

| Transfer
| --------
| Status    | Avg Transfer Rate | Started At                        | Finished At                     | Duration |
| Succeeded | 10.31MB           | Tue, 23 Feb 2021 11:17:52 +0000/s | Tue, 23 Feb 2021 11:17:53 +0000 | 306ms

| Bucket
| ------
| Name          | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| travel-sample | Succeeded | 10.31MB     | 10.31MB/s         | Tue, 23 Feb 2021 11:17:52 +0000 | Tue, 23 Feb 2021 11:17:53 +0000 | 194ms    |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 15749    | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

$ cbdatarecovery -c 172.20.1.1 -u Administrator -p asdasd -d /opt/couchbase/lib/couchbase/data --vbucket-state replica
Recovering to '172.20.1.1'
Copied all data in 188ms (Avg. 10.33MB/Sec)                                                                              15893 items / 10.33MB
[====================================================================================================================================] 100.00%

| Transfer
| --------
| Status    | Avg Transfer Rate | Started At                        | Finished At                     | Duration |
| Succeeded | 10.33MB           | Tue, 23 Feb 2021 11:17:55 +0000/s | Tue, 23 Feb 2021 11:17:55 +0000 | 213ms

| Bucket
| ------
| Name          | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| travel-sample | Succeeded | 10.33MB     | 10.33MB/s         | Tue, 23 Feb 2021 11:17:55 +0000 | Tue, 23 Feb 2021 11:17:55 +0000 | 101ms    |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 15893    | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

When recovering data to a cluster which has changed over time, it’s possible for one or more target scopes/collections to have been recreated. The `--map-data` flag can be used to recover data to a scope/collection whose id has changed (but the name remains the same).

$ cbdatarecovery -c 172.20.1.1 -u Administrator -p asdasd -d /opt/couchbase/lib/couchbase/data \
    --map-data travel-sample.inventory=travel-sample.inventory
Recovering to '172.20.1.1'
Copied all data in 290ms (Avg. 10.31MB/Sec)                                                                              15749 items / 10.31MB
[====================================================================================================================================] 100.00%

| Transfer
| --------
| Status    | Avg Transfer Rate | Started At                        | Finished At                     | Duration |
| Succeeded | 10.31MB           | Tue, 23 Feb 2021 11:46:38 +0000/s | Tue, 23 Feb 2021 11:46:38 +0000 | 318ms

| Bucket
| ------
| Name          | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| travel-sample | Succeeded | 10.31MB     | 10.31MB/s         | Tue, 23 Feb 2021 11:46:38 +0000 | Tue, 23 Feb 2021 11:46:38 +0000 | 201ms    |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 15749    | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

The `--map-data` flag may also be used to remap data from one location to another, for example to rename a scope/collection. Note the addition of the `--auto-create-collections` flag because in this case the scope `storage` did not exist.

$ cbdatarecovery -c 172.20.1.1 -u Administrator -p asdasd -d /opt/couchbase/lib/couchbase/data \
    --map-data travel-sample.inventory=travel-sample.storage --auto-create-collections
Recovering to '172.20.1.1'
Copied all data in 401ms (Avg. 10.31MB/Sec)                                                                              15749 items / 10.31MB
[====================================================================================================================================] 100.00%

| Transfer
| --------
| Status    | Avg Transfer Rate | Started At                        | Finished At                     | Duration |
| Succeeded | 10.31MB           | Tue, 23 Feb 2021 11:20:23 +0000/s | Tue, 23 Feb 2021 11:20:23 +0000 | 429ms

| Bucket
| ------
| Name          | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| travel-sample | Succeeded | 10.31MB     | 10.31MB/s         | Tue, 23 Feb 2021 11:20:23 +0000 | Tue, 23 Feb 2021 11:20:23 +0000 | 227ms    |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 15749    | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

When recovering encrypted data, you’ll need to provide the encryption-related flags.

$ cbdatarecovery -c 172.20.1.1 -u Administrator -p asdasd \
    -d /opt/couchbase/lib/couchbase/data \
    --dump-bucket-deks-path /opt/couchbase/bin/dump-bucket-deks \
    --gosecrets-config-path /opt/couchbase/var/lib/couchbase/config/gosecrets.cfg \
    --gosecrets-path /opt/couchbase/bin/gosecrets \
    --master-password couchbase123 \
    --force-updates
Recovering to '172.20.1.1'
Copied all data in 505ms (Avg. 11.06MB/Sec)                                                                               17722 items / 11.06MB
[=====================================================================================================================================] 100.00%

| Transfer
| --------
| Status    | Avg Transfer Rate | Started At                        | Finished At                     | Duration |
| Succeeded | 11.06MB           | Tue, 23 Feb 2021 11:13:51 +0000/s | Tue, 23 Feb 2021 11:13:52 +0000 | 535ms    |

| Bucket
| ------
| Name          | Status    | Transferred | Avg Transfer Rate | Started At                      | Finished At                     | Duration |
| travel-sample | Succeeded | 10.31MB     | 10.31MB/s         | Tue, 23 Feb 2021 11:13:51 +0000 | Tue, 23 Feb 2021 11:13:52 +0000 | 222ms    |
|
| Mutations                    | Deletions                    | Expirations                  |
| ---------                    | ---------                    | -----------                  |
| Received | Errored | Skipped | Received | Errored | Skipped | Received | Errored | Skipped |
| 15749    | 0       | 0       | 0        | 0       | 0       | 0        | 0       | 0       |

Note that `--gosecrets-path` is only needed if you’re using a non-standard path for the gosecrets executable.

If the data files have been moved to a different location, the paths in the gosecrets.cfg file will need to be updated.

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

CB\_MASTER\_PASSWORD

The Couchbase master password used to encrypt the data the cluster was from. If the master password is supplied as a command line argument then this value is overridden.