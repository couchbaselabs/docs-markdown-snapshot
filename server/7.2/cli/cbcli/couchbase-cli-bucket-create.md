---
title: bucket-create
description: Create a new bucket
editUrl: https://github.com/couchbase/couchbase-cli/edit/neo/docs/modules/cli/pages/cbcli/couchbase-cli-bucket-create.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:cli:cbcli/couchbase-cli-bucket-create.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/cli/cbcli/couchbase-cli-bucket-create.html)

# bucket-create

Create a new bucket

## [](#synopsis)SYNOPSIS

_couchbase-cli bucket-create_ [--cluster <url>] [--username <user>]
    [--password <password>] [--client-cert <path>] [--client-cert-password <password>]
    [--client-key <path>] [--client-key-password <password>] [--bucket <name>]
    [--bucket-type <type>] [--storage-backend <storage>] [--durability-min-level <level>]
    [--bucket-ramsize <size>] [--bucket-replica <num>]
    [--bucket-priority <priority>] [--bucket-eviction-policy <policy>]
    [--max-ttl <seconds>] [--compression-mode <mode>] [--enable-flush <num>]
    [--enable-index-replica <num>] [--conflict-resolution <type>] [--wait]
    [--database-fragmentation-threshold-percentage <perc>]
    [--database-fragmentation-threshold-size <mebibytes>]
    [--view-fragmentation-threshold-percentage <perc>]
    [--view-fragmentation-threshold-size <mebibytes>] [--from-hour <hour>]
    [--from-minute <min>] [--to-hour <hour>] [--to-minute <min>]
    [--abort-outside <0|1>] [--parallel-db-view-compaction <0|1>]
    [--purge-interval <float>] [--history-retention-bytes <bytes>]
    [--history-retention-seconds <seconds>]
    [--enable-history-retention-by-default <0|1>]

## [](#description)DESCRIPTION

Creates a new bucket. Allows creation of Couchbase, Ephemeral, and Memcached buckets, and supports the various configuration parameters for these buckets.

## [](#options)OPTIONS

\-c

\--cluster

Specifies the hostname of a node in the cluster. See the HOST FORMATS section for more information on specifying a hostname.

\-u

\--username <username>

Specifies the username of the user executing the command. If you do not have a user account with permission to execute the command then it will fail with an unauthorized error.

\-p

\--password <password>

Specifies the password of the user executing the command. If you do not have a user account with permission to execute the command then it will fail with an unauthorized error. If this argument is specified, but no password is given then the command will prompt the user for a password through non-echoed stdin. You may also specify your password by using the environment variable CB\_REST\_PASSWORD.

\--client-cert <path>

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `--client-key` as an alternative to the `--username` and `--password` flags. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-cert-password <password>

The password for the certificate provided to the `--client-cert` flag, when using this flag, the certificate/key pair is expected to be in the PKCS#12 format. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-key <path>

The path to the client private key whose public key is contained in the certificate provided to the `--client-cert` flag. May be supplied with `--client-cert` as an alternative to the `--username` and `--password`flags. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-key-password <password>

The password for the key provided to the `--client-key` flag, when using this flag, the key is expected to be in the PKCS#8 format. See the CERTIFICATE AUTHENTICATION section for more information.

\--bucket <name>

The name of the bucket to create. The only characters that can be used for the bucket-name are those in the ranges of A-Z, a-z, and 0-9; plus the underscore, period, dash, and percent characters. The name can be a maximum of 100 characters in length.

\--bucket-type <type>

The type of bucket to create. Accepted bucket types are "couchbase", "ephemeral", and "memcached". The Couchbase bucket is the standard bucket type. It supports data persistence, replication, caching, indexing, views, and N1QL queries. The Ephemeral bucket is an in-memory bucket similar to the Couchbase bucket; but it does not support data persistence or views. The Memcached bucket is a cache-only bucket that does not support persistence, replication, indexing, views, or N1QL querying: this bucket type provides the same behavior as Memcached Server. Memcached buckets are deprecated and Ephemeral buckets should be used instead.

\--storage-backend <storage>

The type of storage to use with the bucket. This is only specified for "couchbase" buckets. Accepted values are "couchstore" or "magma".

\--durability-min-level <level>

The minimum durability level for the bucket. Accepted values for "ephemeral" buckets are "none" or "majority". Accepted values for "couchbase" buckets are "none", "majority", "majorityAndPersistActive", or "persistToMajority".

"none" specifies mutations to the bucket are asynchronous and offer no durability guarantees. "majority" specifies mutations must be replicated to (that is, held in the memory allocated to the bucket on) a majority of the Data Service nodes. "majorityAndPersistActive" specifies mutations must be replicated to a majority of the Data Service nodes. Additionally, it must be written to disk on the node hosting the active vBucket for the data. "persistToMajority" specifies mutations must be persisted to a majority of the Data Service nodes. Accordingly, it will be written to disk on those nodes.

\--bucket-ramsize <size>

The amount of memory to allocate to the cache for this bucket, in mebibytes. The memory quota of this bucket must fit into the overall cluster memory quota. The minimum cache size is 100MiB.

\--bucket-replica <num>

The number of servers to which data is replicated. Replicas provide protection against data loss by keeping copies of this bucket's data on multiple servers. By default, the number of replicas is one, even if there is only a single server in the cluster. The minimum number of replicas is zero, and the maximum three. This option is valid for Couchbase and Ephemeral buckets only.

\--bucket-priority <priority>

Specifies the priority of this bucket's background tasks. This option is valid for Couchbase and Ephemeral buckets only. For Couchbase buckets, background task-types include disk I/O, DCP stream-processing, and item-paging. For Ephemeral buckets, background task-types are the same as for Couchbase buckets, with the exception of disk I/O, which does not apply to Ephemeral buckets. The value of this option may be "high" or "low". The default is "low". Specifying "high" may result in faster processing; but only when more than one bucket is defined for the cluster, and when different priority settings have been established among the buckets. When Couchbase and Ephemeral buckets have different priority settings, this affects the prioritization only of task-types other than disk I/O.

\--bucket-eviction-policy <policy>

The memory-cache eviction policy for this bucket. This option is valid for Couchbase and Ephemeral buckets only.

Couchbase buckets support either "valueOnly" or "fullEviction". Specifying the "valueOnly" policy means that each key stored in this bucket must be kept in memory. This is the default policy: using this policy improves performance of key-value operations, but limits the maximum size of the bucket. Specifying the "fullEviction" policy means that performance is impacted for key-value operations, but the maximum size of the bucket is unbounded.

Ephemeral buckets support either "noEviction" or "nruEviction". Specifying "noEviction" means that the bucket will not evict items from the cache if the cache is full: this type of eviction policy should be used for in-memory database use-cases. Specifying "nruEviction" means that items not recently used will be evicted from memory, when all memory in the bucket is used: this type of eviction policy should be used for caching use-cases.

\--enable-flush <num>

Specifies whether or not the flush operation is allowed for this bucket. To enable flushing, set this option to "1". To disable flushing, set this option to "0". By default, flushing is disabled.

\--enable-index-replica <num>

Enables view index replication for the current bucket. This option is valid for Couchbase buckets only. To enable, set the value of this option to "1". To disable, set the value of this option to "0". By default, view index replication is disabled. There may be at most one replica view index.

\--conflict-resolution <type>

Specifies this bucket's conflict resolution mechanism; which is to be used if a conflict occurs during Cross Data-Center Replication (XDCR). Sequence-based and timestamp-based mechanisms are supported.

Sequence-based conflict resolution selects the document that has been updated the greatest number of times since the last sync: for example, if one cluster has updated a document twice since the last sync, and the other cluster has updated the document three times, the document updated three times is selected; regardless of the specific times at which updates took place.

Timestamp-based conflict resolution selects the document with the most recent timestamp: this is only supported when all clocks on all cluster-nodes have been fully synchronized.

\--max-ttl <seconds>

Specifies the maximum TTL (time-to-live) for all documents in bucket in seconds. If enabled and a document is mutated with no TTL or a TTL greater than than the maximum, its TTL will be set to the maximum TTL. Setting this option to 0 disables the use of max-TTL and the largest TTL that is allowed is 2147483647\. This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.

\--compression-mode <mode>

Specifies the compression-mode of the bucket. There are three options; off, passive and active. All three modes are backwards compatible with older SDKs, where Couchbase Server will automatically uncompress documents for clients that do not understand the compression being used. This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.

Off: Couchbase Server will only compress document values when persisting to disk. This is suitable for use cases where compression could have a negative impact on performance. Please note it is expected that compression in most use cases will improve performance.

Passive: Documents which were compressed by a client, or read compressed from disk will be stored compress in-memory. Couchbase Server will make no additional attempt to compress documents that are not already compressed.

Active: Couchbase Server will actively and aggressively attempt to compress documents, even if they have not been received in a compressed format. This provides the benefits of compression even when the SDK clients are not complicit.

\--wait

The create bucket command is asynchronous by default. Specifying this option makes the operation synchronous: so that the command returns only after the bucket has been fully created.

\--database-fragmentation-threshold-percentage <perc>

Sets the database fragmentation trigger threshold as a percentage. Can be set to values between 2 and 100.

\--database-fragmentation-threshold-size <mebibytes>

Sets the database fragmentation trigger threshold as a number of mebibytes. It accepts integers greater than 1.

\--view-fragmentation-threshold-percentage <perc>

Sets the view fragmentation trigger threshold as a percentage. Can be set to values between 2 and 100.

\--view-fragmentation-threshold-size <mebibytes>

Sets the view fragmentation trigger threshold as a number of mebibytes. It accepts integers greater than 1.

\--from-hour <hour>

Sets the hour of the start time. Used together with \\-\\-from\\-minutes to set the start time of the interval in which compaction is allowed to run. To set the interval ensure both start and end time are set.

\--from-minute <min>

Sets the minute of the start time. Used together with \\-\\-from\\-hour to set the start time of the interval in which compaction is allowed to run. To set the interval ensure both start and end time are set.

\--to-hour <hour>

Sets the hour of the end time. Used together with \\-\\-to\\-minute to set the end time of the interval in which compaction is allowed to run. To set the interval ensure both start and end time are set.

\--to-minute <min>

Sets the minute of the end time. Used together with \\-\\-to\\-hour to set the end time of the interval in which compaction is allowed to run. To set the interval ensure both start and end time are set.

\--abort-outside <0|1>

Will set the option that terminate compaction if the process takes longer than the allowed time. Options are \[1, 0\].

\--parallel-db-view-compaction <0|1>

Run index and data compaction in parallel. Global setting only.

\--purge-interval <float>

Sets the frequency of the tombstone (metadata) purge interval. The default value is three days.

\--history-retention-bytes <bytes>

Specifies how many bytes of document history the bucket should aim to retain on disk. This option is valid for Couchbase buckets with Magma storage backend only. By default, history retention in bytes is set to 0, which means that no history is retained and all stale data is removed during compaction.

\--history-retention-seconds <seconds>

Specifies how many seconds of document history the bucket should aim to retain on disk. This option is valid for Couchbase buckets with Magma storage backend only. By default, history retention in seconds is set to 0, which means that no history is retained and all stale data is removed during compaction.

\--enable-history-retention-by-default <0|1>

Specifies whether or not the document history retention should be enabled by default for new collections in this bucket. This option is valid for Couchbase buckets with Magma storage backend only. To enable the document history retention for new collections, set this option to "1". To disable the document history retention for new collections, set this option to "0". By default, the document history retention for new collections is enabled. To create a collection with a non-default history retention setting use the **collection-manage**command with **\--enable-history** flag set to either "0" or "1".

## [](#host-formats)HOST FORMATS

When specifying a host for the couchbase-cli command the following formats are expected:

* `couchbase://<addr>` or `couchbases://<addr>`
* `http://<addr>:<port>` or `https://<addr>:<port>`
* `<addr>:<port>`

It is recommended to use the couchbase://<addr> or couchbases://<addr> format for standard installations. The other formats allow an option to take a port number which is needed for non-default installations where the admin port has been set up on a port other that 8091 (or 18091 for https).

## [](#certificate-authentication-mtls-authentication)CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)

This tool supports authenticating against a Couchbase Cluster by using certificate based authentication (mTLS authentication). To use certificate based authentication a certificate/key must be supplied, there a currently multiple ways this may be done.

### [](#pem-encoded-certificatekey)PEM ENCODED CERTIFICATE/KEY

An unencrypted PEM encoded certificate/key may be supplied by using: - `--client-cert <path>`\- `--client-key <path>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

The file passed to `--client-key` must contain at most one private key, the key can be in one of the following formats: - PKCS#1 - PKCS#8

Currently, only the following key types are supported: - RSA - DSA

### [](#pem-encoded-certificatepem-or-der-encrypted-pkcs8-key)PEM ENCODED CERTIFICATE/PEM OR DER ENCRYPTED PKCS#8 KEY

An encrypted PKCS#8 formatted key may be provided using: - `--client-cert <path>`\- `--client-key <path>`\- `--client-key-password <password>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

Currently, only the following key types are supported: - RSA - DSA

### [](#encrypted-pkcs12-certificatekey)ENCRYPTED PKCS#12 CERTIFICATE/KEY

An encrypted PKCS#12 certificate/key may be provided using: - `--client-cert <path>`\- `--client-cert-password <password>`

The file passed to `--client-cert` must contain the client certificate and exactly one private key. It may also contain the chain required to authenticate the client certificate.

Currently, only the following key types are supported: - RSA - DSA

## [](#examples)EXAMPLES

To create a Couchbase bucket named "travel-data" with a memory cache size of 1GB, run the following command.

$ couchbase-cli bucket-create -c 192.168.1.5:8091 --username Administrator \
 --password password --bucket travel-data --bucket-type couchbase \
 --bucket-ramsize 1024

To create a Couchbase bucket named "airline-data" with a memory cache size of 1GB, two data replicas, high background-task priority, full eviction, flushing enabled, and view index replication enabled, run the following command.

$ couchbase-cli bucket-create -c 192.168.1.5:8091 --username Administrator \
 --password password --bucket travel-data --bucket-type couchbase \
 --bucket-ramsize 1024 --bucket-replica 2 --bucket-priority high \
 --bucket-eviction-policy fullEviction --enable-flush 1 \
 --enable-index-replica 1

To create a Memcached bucket named "travel-data" with a memory cache size of 1GB, run the following command.

$ couchbase-cli bucket-create -c 192.168.1.5:8091 --username Administrator \
 --password password --bucket travel-data --bucket-type memcached \
 --bucket-ramsize 1024

To create an Ephemeral bucket named "hotel-data" synchronously, with a memory cache size of 256MiB, flushing enabled, "nruEviction", and timestamp-based conflict resolution, run the following command.

$ couchbase-cli bucket-create -c 192.168.1.5:8091 --username Administrator \
--password password --bucket hotel-data --bucket-type ephemeral \
--bucket-ramsize 256 --enable-flush 1 --bucket-eviction-policy nruEviction \
--conflict-resolution timestamp --wait

## [](#environment-and-configuration-variables)ENVIRONMENT AND CONFIGURATION VARIABLES

CB\_REST\_USERNAME

Specifies the username to use when executing the command. This environment variable allows you to specify a default argument for the -u/--username argument on the command line.

CB\_REST\_PASSWORD

Specifies the password of the user executing the command. This environment variable allows you to specify a default argument for the -p/--password argument on the command line. It also allows the user to ensure that their password are not cached in their command line history.

CB\_CLIENT\_CERT

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `CB_CLIENT_KEY` as an alternative to the `CB_USERNAME` and `CB_PASSWORD` variables. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_CERT\_PASSWORD

The password for the certificate provided to the `CB_CLIENT_CERT` variable, when using this variable, the certificate/key pair is expected to be in the PKCS#12 format. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_KEY

The path to the client private key whose public key is contained in the certificate provided to the `CB_CLIENT_CERT` variable. May be supplied with `CB_CLIENT_CERT` as an alternative to the `CB_USERNAME` and `CB_PASSWORD`variables. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_KEY\_PASSWORD

The password for the key provided to the `CB_CLIENT_KEY` variable, when using this variable, the key is expected to be in the PKCS#8 format. See the CERTIFICATE AUTHENTICATION section for more information.

## [](#see-also)SEE ALSO

[bucket-compact](couchbase-cli-bucket-compact.md), [bucket-delete](couchbase-cli-bucket-delete.md), [bucket-edit](couchbase-cli-bucket-edit.md), [bucket-flush](couchbase-cli-bucket-flush.md), [bucket-list](couchbase-cli-bucket-list.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite