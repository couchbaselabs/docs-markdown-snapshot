---
title: setting-alternate-address
description: Modify alternate addresses
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/cli/pages/couchbase-cli-setting-alternate-address.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.0@enterprise-analytics:cli:couchbase-cli-setting-alternate-address.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/cli/couchbase-cli-setting-alternate-address.html)

# setting-alternate-address

Modify alternate addresses

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-alternate-address_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--list] [--set] [--remove] [--hostname <host>]
    [--ports <ports>]

## [](#description)DESCRIPTION

This command is used to set the alternate address for a node. This alternate address allows the node to be connected by a different address, this is useful when an external agent tries to connect via a NAT'd environment such as the cloud or kubernetes.

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

\--list

Show current alternate addresses. Please note only the first 43 characters hostname and alternate address are displayed. The full hostnames are shown in the json output (-o json).

\--set

Set alternate address for the node specified in the -c/--cluster option.

\--remove

Remove alternate address for the node specified in the -c/--cluster option.

\--node <node>

The node in the cluster to take action on. This is required when using --set or --remove flags.

\--hostname <host>

Alternate host address

\--ports <port>

 Alternate port mappings. Specified as a comma separated list: e.g. `--ports kv=9000,kvSSL=9999.`

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

To set the alternate address and custom ports for node 192.168.1.5 we would use the following command:

$ couchbase-cli setting-alternate-address -c 192.168.1.5:8091 --username Administrator \
   --password password --set --node 192.168.1.5 --hostname 10.10.10.10 \
   --ports mgmt=1100,capi=2000,capiSSL=3000

To see the current alternate address configuration we would use the --list flag as follows:

$ couchbase-cli setting-alternate-address -c 192.168.1.5:8091 --username Administrator \
   --password password --list

## [](#discussion)DISCUSSION

All of the ports that can be configured:

__Table 1\. Alternate Ports__
| Port Name         | Encrypted Port Name | Service         | Description                                                                      |
| ----------------- | ------------------- | --------------- | -------------------------------------------------------------------------------- |
| mgmt              | mgmtSSL             | Cluster Manager | The UI and REST API for managing the Cluster                                     |
| kv                | kvSSL               | Data            | Used by the SDKs to transfer data to and from the Data Service                   |
| capi              | capiSSL             | View Engine     | Used by the SDKs                                                                 |
| n1ql              | n1qlSSL             | Query           | Used by the SDKs to query data                                                   |
| fts               | ftsSSL              | Search          | Used by the SDKs to do full text searches                                        |
| cbas              | cbasSSL             | Analytics       | Used by the SDKs to query data managed by the Analytic service                   |
| eventingAdminPort | eventingSSL         | Eventing        | Used by the SDK to transfer data to and from the Eventing Service                |
| eventingDebug     | N/A                 | Eventing        | The Eventing debugger port, this should only be set in development environments. |
| backupAPI         | backupAPIHTTPS      | Backup          | The backup service REST API.                                                     |
| N/A               | backupGRPC          | Backup          | Used by backup nodes to communicate with each other.                             |

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

[cluster-init](couchbase-cli-cluster-init.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite