---
title: setting-rebalance
description: Modifies rebalance retry settings
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/cli/pages/couchbase-cli-setting-rebalance.adoc
  xref: xref:enterprise-analytics:cli:couchbase-cli-setting-rebalance.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/cli/couchbase-cli-setting-rebalance.html)

# setting-rebalance

Modifies rebalance retry settings

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-rebalance [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--set] [--get] [--cancel] [--pending-info] [--enable <1|0>]
    [--wait-for <sec>] [--moves-per-node <num>] [--max-attempts <num>]
    [--rebalance-id <id>]

## [](#description)DESCRIPTION

This command allows configuring and retrieving automatic rebalance retry settings as well as canceling and retrieving information of pending rebalance retries.

## [](#options)OPTIONS

\-c

\--cluster

Specifies the hostname of a node in the cluster. See the HOST FORMATS section for more information about specifying a hostname.

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

\--set

Specify to configure the automatic rebalance retry settings.

\--get

Specify to retrieve the automatic rebalance retry settings.

\--cancel

Specify to cancel a pending rebalance retry, use --rebalance-id together with this option to provide the rebalance id.

\--pending-info

Specify to retrieve information of pending rebalance retries.

\--enable <1|0>

Enable (1) or disable (0) automatic rebalance retry. This flag is required when using --set. By default, automatic rebalance retry is disabled.

\--wait-for <sec>

Specify the amount of time to wait after a failed rebalance before retrying. Time must be a value between 5 and 3600 seconds. By default, the wait time is 300 seconds.

\--max-attempts <num>

Specify the number of times a failed rebalance will be retried. The value provided must be between 1 and 3, the default is 1.

\--moves-per-node <num>

Specify the number of concurrent vBucket to move per a node during a rebalance. The value provided must be between 1 and 64, the default is 4\. A higher setting may improve rebalance performance, at the cost of higher resource consumption; in terms of CPU, memory, disk, and bandwidth. Conversely, a lower setting may degrade rebalance performance while freeing up such resources. However, that rebalance performance can be affected by many additional factors; and that in consequence, changing this parameter may not always have the expected effects. A higher setting, due to its additional consumption of resources, may degrade the performance of other systems, including the Data Service.

\--rebalance-id <id>

Specify the rebalance id of a failed rebalance. Use together with --cancel, to cancel a pending retry.

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

To retrieve the current automatic rebalance retry configuration, use:

$ couchbase-cli setting-rebalance -c 127.0.0.1:8091 -u Administrator \
 -p password --get

To enable automatic rebalance retry use the command bellow.

$ couchbase-cli setting-rebalance -c 127.0.0.1:8091 -u Administrator \
 -p password --set --enable 1

You can also set the `wait-for` period and the maximum number of retries. The command above enables automatic rebalance retry as well as setting the wait time before retrying to 60 seconds and the maximum number of retries to 2.

$ couchbase-cli setting-rebalance -c 127.0.0.1:8091 -u Administrator \
 -p password --set --enable 1 --wait-for 60 --retries 2

To retrieve information of the pending rebalance retries, run the command bellow.

$ couchbase-cli setting-rebalance -c 127.0.0.1:8091 -u Administrator \
 -p password --pending-info

To cancel a pending rebalance retry run the command bellow where `4198f4b1564a800223271af76edd4f98` is the rebalance id, this can be retrieved using the `--pending-info` flag above.

$ couchbase-cli setting-rebalance -c 127.0.0.1:8091 -u Administrator \
 -p password --pending-info --rebalance-id 4198f4b1564a800223271af76edd4f98

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

[rebalance](couchbase-cli-rebalance.md), [rebalance-status](couchbase-cli-rebalance-status.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite