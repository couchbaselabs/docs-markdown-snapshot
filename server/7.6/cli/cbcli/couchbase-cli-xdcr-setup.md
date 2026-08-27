---
title: xdcr-setup
description: Manage references to remote clusters
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/couchbase-cli/edit/trinity/docs/modules/cli/pages/cbcli/couchbase-cli-xdcr-setup.adoc
  xref: xref:7.6@server:cli:cbcli/couchbase-cli-xdcr-setup.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbcli/couchbase-cli-xdcr-setup.html)

# xdcr-setup

Manage references to remote clusters

## [](#synopsis)SYNOPSIS

_couchbase-cli xdcr-setup_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--create] [--delete] [--edit] [--list]
    [--xdcr-cluster-name <name>] [--xdcr-hostname <hostname>]
    [--xdcr-username <username>] [--xdcr-password <password>]
    [--xdcr-user-certificate <path>] [--xdcr-user-key <path>]
    [--xdcr-certificate <file>] [--xdcr-secure-connection <type>]

## [](#description)DESCRIPTION

This command is used to manage the remote clusters that are available to be replicated to.

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

\--create

Creates an new XDCR remote reference.

\--delete

Deletes an XDCR remote reference.

\--edit

Edits an XDCR remote reference.

\--list

List all XDCR remote references.

\--xdcr-cluster-name <name>

The name for the remote cluster reference.

\--xdcr-hostname <hostname>

The hostname of the remote cluster reference.

\--xdcr-username <username>

The username of the remote cluster reference.

\--xdcr-password <password>

The password of the remote cluster reference.

\--xdcr-user-certificate <path>

The user certificate for authentication

\--xdcr-user-key <path>

The user key for authentication

\--xdcr-certificate <path>

The certificate used for encryption

\--xdcr-secure-connection <type>

Specifies the type of encryption to use. This flag may either be set to either "half", "full", or "none". Half encryption means that passwords are encrypted, but data is not. This results in faster data transfer, but less security. Full encryption means that all data and passwords are encrypted which increases security, but reduces overall data transfer speed. If no encryption is needed then "none" can be specified. This flag defaults to "none" if it is not specified.

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

To create a new remote reference to a Couchbase cluster named "east" run the following command.

$ couchbase-cli xdcr-setup -c 192.168.1.5 -u Administrator \
 -p password --create --xdcr-cluster-name east --xdcr-hostname 192.168.1.6
 --xdcr-username Administrator --xdcr-password password

If the new remote reference should always be encrypted then make sure to enable encryption.

$ couchbase-cli xdcr-setup -c 192.168.1.5 -u Administrator \
 -p password --create --xdcr-cluster-name east --xdcr-hostname 192.168.1.6 \
 --xdcr-username Administrator --xdcr-password password \
 --xdcr-demand-encryption 1 --xdcr-certificate /root/cluster.cert

To list all current XDCR cluster references run the following command.

$ couchbase-cli xdcr-setup -c 192.168.1.5 -u Administrator \
 -p password --list

If you need to edit a cluster references named "east" and change the password run the following command.

$ couchbase-cli xdcr-setup -c 192.168.1.5 -u Administrator \
 -p password --edit --xdcr-cluster-name east --xdcr-hostname 192.168.1.6
 --xdcr-username Administrator --xdcr-password new_password

Note in the above example that you need to specify all of the current unchanging configuration parameters also to avoid them being reset to defaults.

If you no longer need an XDCR remote reference then you can delete it. We should this below using the "east" remote reference as an example.

$ couchbase-cli xdcr-setup -c 192.168.1.5 -u Administrator \
 -p password --delete --xdcr-cluster-name east

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

[setting-xdcr](couchbase-cli-setting-xdcr.md), [xdcr-replicate](couchbase-cli-xdcr-replicate.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite