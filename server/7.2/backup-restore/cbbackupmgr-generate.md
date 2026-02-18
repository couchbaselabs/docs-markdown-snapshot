---
title: cbbackupmgr generate
description: Generate documents and send them to a 'sink', primarily for testing purposes.
editUrl: https://github.com/couchbase/backup/edit/neo/docs/modules/backup-restore/pages/cbbackupmgr-generate.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/backup-restore/cbbackupmgr-generate.html)

# cbbackupmgr generate

Generate documents and send them to a 'sink', primarily for testing purposes.

## [](#synopsis)SYNOPSIS

cbbackupmgr generate [--num-documents <document_count>] [--archive <archive_dir>]
                     [--cluster <cluster_hostname>] [--username <username>]
                     [--password <password>] [--client-cert <path>]
                     [--client-cert-password <password>] [--client-key <path>]
                     [--client-key-password <password>] [--bucket <bucket_name>]
                     [--cacert <certfile_path>] [--no-ssl-verify] [--repo <repository_name>]
                     [--sink <sink_name>] [--prefix <prefix>] [--size <size>] [--json]
                     [--json-fields <field_count>] [--json-field-size <field_size>]
                     [--low-compression] [--xattrs] [--xattr-fields <field_count>]
                     [--xattr-field-size <field_size>] [--compress]
                     [--threads <thread_count>] [--purge] [--resume]
                     [--storage <storage_type>] [--no-progress-bar]

## [](#description)DESCRIPTION

The generate command is primarily meant for testing the internal pipeline for backup/restore. It allows you to very quickly generate documents and send them to a desired 'sink'.

## [](#required)Required

\-n,--num-documents <document\_count>

The number of documents to generate.

\-b,--bucket <bucket\_name>

The bucket to generate documents for.

## [](#optional)Optional

\-a,--archive <archive\_dir>

The archive in which to store generated documents (optionally used for logging when 'sink' is Couchbase).

\-c,--cluster <cluster\_hostname>

The hostname of the test cluster (only required when 'sink' is couchbase).

\-u,--username <username>

The username for cluster authentication. The user must have the appropriate privileges to take a backup.

\-p,--password <password>

The password for cluster authentication. The user must have the appropriate privileges to take a backup. If not password is supplied to this option then you will be prompted to enter your password.

\--client-cert <path>

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `--client-key` as an alternative to the `--username` and `--password` flags. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-cert-password <password>

The password for the certificate provided to the `--client-cert` flag, when using this flag, the certificate/key pair is expected to be in the PKCS#12 format. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-key <path>

The path to the client private key whose public key is contained in the certificate provided to the `--client-cert` flag. May be supplied with `--client-cert` as an alternative to the `--username` and `--password`flags. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-key-password <password>

The password for the key provided to the `--client-key` flag, when using this flag, the key is expected to be in the PKCS#8 format. See the CERTIFICATE AUTHENTICATION section for more information.

\--no-ssl-verify

Skips the SSL verification phase. Specifying this flag will allow a connection using SSL encryption, but will not verify the identity of the server you connect to. You are vulnerable to a man-in-the-middle attack if you use this flag. Either this flag or the --cacert flag must be specified when using an SSL encrypted connection.

\--cacert <cert\_path>

Specifies a CA certificate that will be used to verify the identity of the server being connecting to. Either this flag or the --no-ssl-verify flag must be specified when using an SSL encrypted connection.

\-r,--repo <repo>

The name of a backup repository in an archive (only required when 'sink' is archive).

\-s,--sink <sink>

The sink to send generated documents to (valid options are 'archive', 'blackhole' and 'couchbase')

\-P,--prefix <prefix>

An optional prefix that will be prepended to generated keys.

\-s,--size <size>

The size of generated binary documents in bytes.

\-j,--json

Generated JSON formatted documents instead of binary documents.

\--json-fields <num\_fields>

The number of JSON fields to generate.

\--json-value-size <value\_size>

The size in bytes of the generated JSON values.

\--low-compression

Generate document values/xattr value which are difficult to compress.

\--xattrs

Generate extended attributes.

\--xattr-fields <num\_fields>

The number of fields to generate in the xattrs.

\--xattr-value-size <value\_size>

The size in bytes of the generated xattr values (hard coded limit of 2 bytes).

\--compress

Force compression at the "gocbcore" level (default is uncompressed).

\-t,--threads <thread\_count>

The amount of worker threads to created for document generation.

\--resume

If you previously canceled a backup/generate test there will be a backup directory remaining; continue generating to the same backup.

\--purge

If you previously canceled a backup/generate test there will be a backup directory remaining; remove it before continuing.

\--shard-count <shard\_count>

The number of shards to create when generating to an archive. This option is silently ignored when generating to the 'couchbase' or 'blackhole' sinks.

\--no-progress-bar

By default, a progress bar is printed to stdout so that the user can see how long the generation is expected to take, the amount of data that is being transferred per second, and the amount of data that has been generated. Specifying this flag disables the progress bar and is useful when running automated jobs.

## [](#host-formats)HOST FORMATS

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

## [](#certificate-authentication-mtls-authentication)CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)

This tool supports authenticating against a Couchbase Cluster by using certificate based authentication (mTLS authentication). To use certificate based authentication a certificate/key must be supplied, there a currently multiple ways this may be done.

### [](#pem-encoded-certificatekey)PEM ENCODED CERTIFICATE/KEY

An unencrypted PEM encoded certificate/key may be supplied by using: - `--client-cert <path>`\- `--client-key <path>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

The file passed to `--client-key` must contain at most one private key, the key can be in one of the following formats: - PKCS#1 - PKCS#8 - EC

Currently, only the following key types are supported: - RSA - ECDSA - ED25519

### [](#pem-encoded-certificatepem-or-der-encrypted-pkcs8-key)PEM ENCODED CERTIFICATE/PEM OR DER ENCRYPTED PKCS#8 KEY

An encrypted PKCS#8 formatted key may be provided using: - `--client-cert <path>`\- `--client-key <path>`\- `--client-key-password <password>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

Currently, only the following key types are supported: - RSA - ECDSA - ED25519

### [](#encrypted-pkcs12-certificatekey)ENCRYPTED PKCS#12 CERTIFICATE/KEY

An encrypted PKCS#12 certificate/key may be provided using: - `--client-cert <path>`\- `--client-cert-password <password>`

The file passed to `--client-cert` must contain the client certificate and exactly one private key. It may also contain the chain required to authenticate the client certificate.

Currently, only the following key types are supported: - RSA - ECDSA - ED25519

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

cbbackupmgr generate is used to generate documents and send them through the cbbackupmgr pipeline; this command is primarily intended for testing.

$ cbbackupmgr generate -a /data/backups -c localhost -u admin -p password -n 1000 -s 1024
1000/1000 - 100% - 999D/s - 1.03MB/s
Transfer completed in 1.000174463s

By supplying the optional 'sink' argument you can choose which sink to send the generate documents to; to test the speed to the document generate itself, specify the sink as 'blackhole'.

$ cbbackupmgr generate -a /data/backups -n 100000 -s 1048576 --sink 'blackhole'
100000/100000 - 100% - 9084D/s - 8.87GB/s
Transfer completed in 11.007203014s

## [](#cbbackupmgr)CBBACKUPMGR

Part of the [cbbackupmgr](cbbackupmgr.md) suite