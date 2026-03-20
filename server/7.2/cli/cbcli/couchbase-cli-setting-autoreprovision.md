---
title: setting-autoreprovision
description: Modifies auto-reprovision settings
editUrl: https://github.com/couchbase/couchbase-cli/edit/neo/docs/modules/cli/pages/cbcli/couchbase-cli-setting-autoreprovision.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:cli:cbcli/couchbase-cli-setting-autoreprovision.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/cli/cbcli/couchbase-cli-setting-autoreprovision.html)

# setting-autoreprovision

Modifies auto-reprovision settings

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-autoreprovision_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--enabled <1|0>] [--max-nodes <num>]

## [](#description)DESCRIPTION

Auto-reprovisioning is used in order to prevent data loss in ephemeral buckets during failure scenarios when a node crashes and restarts quickly. Under this scenario auto-reprovisioning ensures that an ephemeral bucket’s replica vBuckets are promoted to active state. This mechanism is not needed for Couchbase buckets because a Couchbase buckets data is persisted to disk and can be loaded back into memory after a node restarts. Ephemeral buckets on the other hand completely lose their data when a node crashes and replicas must be relied upon in order to prevent data loss. If ephemeral buckets are not in use this setting has no effect on the cluster.

Auto-reprovisioning can either be enabled or disabled. If you have ephemeral buckets it is always recommended that auto-reprovisioning is enabled otherwise the cluster will experience data loss if a node crashes or is restarted. Users can also specify the number of nodes that can be auto-reprovisioned before the cluster is rebalanced. An auto-reprovision event occurs if a cluster has at least one ephemeral bucket and a node crashes and restarts. If the number of crashes and restarts exceed the maximum number of nodes that can be auto-reprovisioned then the next crash and restart will result in data loss for all ephemeral buckets in the cluster.

When setting the max nodes parameter, note that specifying the max nodes to be too high could result in cascading node failures. This can happen because when a node fails and restarts the server load for the crashed node is distributed to the rest of the servers in the cluster. This extra load could cause the one or more of the remaining servers in the cluster to become overloaded and unresponsive leading to more failures. On the other hand specifying max nodes to be too small could lead to data loss if there are many failures in the cluster at the same time. How this variable is set depends on the cluster size, workload, and configuration. However, it is always recommended that auto-reprovisioning is at least enabled and that max nodes is set to at least 1.

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

\--enabled <num>

Specifies whether or not auto-reprovisioning is enabled. Set this option to "1" to enable autofailover or "0" to disable autofailover.

\--max-nodes <num>

Specifies the maximum number of servers that can be auto-reprovisioned before a rebalance must take place (which resets the count). This parameter must always be set to a number greater than or equal to 1.

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

To enable auto-reprovisioning and allow up to three nodes be auto-reprovisioned before a rebalance takes place run the following command.

$ couchbase-cli setting-autoreprovision -c 192.168.1.5 -u Administrator \
 -p password --enabled 1 --max-nodes 3

To disable auto-reprovisioning run the following command.

$ couchbase-cli setting-autoreprovision -c 192.168.1.5 -u Administrator \
 -p password --enabled 0

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

[setting-autofailover](couchbase-cli-setting-autofailover.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite