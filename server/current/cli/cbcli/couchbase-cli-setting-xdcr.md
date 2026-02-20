---
title: setting-xdcr
description: Modifies cross data center replication (XDCR) settings
editUrl: https://github.com/couchbase/couchbase-cli/edit/morpheus/docs/modules/cli/pages/cbcli/couchbase-cli-setting-xdcr.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:cli:cbcli/couchbase-cli-setting-xdcr.adoc[]
---

[View original HTML](/server/current/cli/cbcli/couchbase-cli-setting-xdcr.html)

# setting-xdcr

Modifies cross data center replication (XDCR) settings

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-xdcr_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--checkpoint-interval <seconds>]
    [--worker-batch-size <num>] [--doc-batch-size <kilobytes>]
    [--failure-restart-interval <seconds>] [--source-nozzle-per-node <num>]
    [--target-nozzle-per-node <num>] [--bandwidth-usage-limit <num>]
    [--enable-compression <num>] [--stats-interval <milliseconds>]
    [--optimistic-replication-threshold <bytes>] [--log-level <level>]
    [--max-processes <num>]

## [](#description)DESCRIPTION

This command sets global default settings for all XDCR replications. If you only want to change the settings for a single XDCR replication see the [xdcr-replicate](couchbase-cli-xdcr-replicate.md) command.

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

\--checkpoint-interval <seconds>

The interval between checkpoints in seconds. The value of this option must be between 60 and 14,400.

\--worker-batch-size <num>

The worker batch size. The value of this option must be between 500 and 10,000.

\--doc-batch-size <kilobytes>

The document batch size in Kilobytes. The value of this option must be between 10 and 100,000.

\--failure-restart-interval <seconds>

Interval for restarting failed XDCR connections in seconds. The value of this option must be between 1 and 300.

\--optimistic-replication-threshold <bytes>

Document body size threshold in bytes used to trigger optimistic replication.

\--source-nozzle-per-node <num>

The number of source nozzles to each node in the target cluster. The value of this option must be between 1 and 10.

\--target-nozzle-per-node <num>

The number of outgoing nozzles to each node in the target cluster. The value of this option must be between 1 and 10.

\--bandwidth-usage-limit <num>

The default bandwidth limit for XDCR replications in mebibytes per second.

\--enable-compression <num>

Specifies whether or not XDCR compression is enabled. Set this option to "1" to enable compression or "0" to disable compression. This feature is only available in Couchbase Enterprise Edition and can only be used where the target cluster supports compression.

\--log-level <level>

The XDCR log level.

\--stats-interval <milliseconds>

The interval for statistics updates in milliseconds.

\--max-processes <num>

Specify the number of processes allocated to XDCR. As new replications are added, it will require more resources to maintain the replication throughput. This option allows to allocate more resources to XDCR.

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

If we want to change the checkpoint interval to 500 seconds, the worker batch to 1000 documents, the document batch size to 1024KB, the failure restart interval to 60 seconds. the optimistic replication threshold to 102400 bytes, the source nozzles to 8, the target nozzles to 8, the log level to info, and the stats interval to 500 milliseconds run the following command.

$ couchbase-cli setting-xdcr -c 192.168.1.5 -u Administrator \
 -p password --checkpoint-interval 500 --worker-batch-size 1000 \
 --doc-batch-size 1024 --failure-restart-interval 60 \
 --optimistic-replication-threshold 102400 --source-nozzle-per-node 8 \
 --target-nozzle-per-node 8 --log-level Info --stats-interval 500

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

[xdcr-replicate](couchbase-cli-xdcr-replicate.md), [xdcr-setup](couchbase-cli-xdcr-setup.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite