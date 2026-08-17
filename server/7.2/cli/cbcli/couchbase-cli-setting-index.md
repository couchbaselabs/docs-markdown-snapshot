---
title: setting-index
description: Modifies index settings
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/couchbase-cli/edit/neo/docs/modules/cli/pages/cbcli/couchbase-cli-setting-index.adoc
  xref: xref:7.2@server:cli:cbcli/couchbase-cli-setting-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/cli/cbcli/couchbase-cli-setting-index.html)

# setting-index

Modifies index settings

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-index_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--index-max-rollback-points <num>]
    [--index-stable-snapshot-interval <seconds>]
    [--index-memory-snapshot-interval <milliseconds>]
    [--index-storage-setting <type>] [--index-threads <num>]
    [--index-log-level <level>] [--replicas <num>]
    [--optimize-placement <1|0>]

## [](#description)DESCRIPTION

This command sets various advanced settings for the index service.

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

\--index-max-rollback-points <num>

The maximum number of rollback points. The value of this option must be greater than or equal to 1\. If this option is not specified it defaults to 2.

\--index-stable-snapshot-interval <seconds>

Specifies the frequency of persisted snapshots for recovery in seconds. This means that in the event of a failover this is the farthest back we may have to rebuild the index from. This value of this parameter must be greater than 1\. If this option is not specified it defaults to 5000 seconds.

\--index-memory-snapshot-interval <milliseconds>

Specifies the frequency of in-memory snapshots in milliseconds. This determines the earliest possibility of a scan seeing a given KV mutation. This value of this parameter must be greater than 1\. This parameter defaults to 200 if it is not specified.

\--index-storage-setting <type>

Sets the index storage mode for all indexes in this cluster. This parameter may only be changed if there are no nodes running the index service. To specify the disk based forestdb index backend set this parameter to "default". To set the storage mode to use memory optimized indexes set this parameter to `memopt`. This option does not have a default value if not set.

\--index-threads <num>

Sets the number of CPUs that can be used by the indexer. The value of this option must be between 0 and 1024\. If this option is not set then it default to 0.

\--index-log-level <level>

Sets the log level for the index service. Valid log levels include "debug", "silent", "fatal", "error", "warn", "info", "verbose", "timing", and "trace". If this option is not specified it defaults to "info".

\--replicas <num>

Number of index replicas.

\--optimize-placement <1|0>

When enabled (1) it will move the indexes to the new node during a rebalance to eliminate the need of doing a 'swap rebalance'.

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

To set the max index rollback points to 8, the index stable snapshot interval to 40000 seconds, the index memory snapshot interval to 150 milliseconds, the index thread count to 8 and in the index log level to info run the following command.

$ couchbase-cli setting-index -c 127.0.0.1:8091 -u Administrator \
 -p password --index-max-rollback-points 8 --index-threads 8 \
   --index-log-level info --index-stable-snapshot-interval 40000 \
   --index-memory-snapshot-interval 150 \

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

[setting-cluster](couchbase-cli-setting-cluster.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite