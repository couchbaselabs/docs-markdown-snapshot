---
title: cluster-edit
description: Edits cluster settings
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/couchbase-cli/edit/morpheus/docs/modules/cli/pages/cbcli/couchbase-cli-cluster-edit.adoc
  xref: xref:server:cli:cbcli/couchbase-cli-cluster-edit.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/cli/cbcli/couchbase-cli-cluster-edit.html)

# cluster-edit

Edits cluster settings

## [](#synopsis)SYNOPSIS

_couchbase-cli cluster-edit_ [--cluster <url>] [--cluster-username <username>] [--cluster-password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--cluster-port <port>]
    [--cluster-ramsize <mebibytes>] [--cluster-name <name>]
    [--cluster-index-ramsize <mebibytes>] [--cluster-fts-ramsize <mebibytes>]

## [](#description)DESCRIPTION

DEPRECATED: Please use the [setting-cluster](couchbase-cli-setting-cluster.md) command which provides the same functionality as this command.

This command is used to modify cluster level settings. It allows users to change the Couchbase Server built-in administrator username and password, change the port that the cluster manager listens on, and modify the data, index, and full-text service memory quotas.

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

\--cluster-username

Specifies the new username for the Couchbase Server administrator user.

\--cluster-password

Specifies the new password for the Couchbase Server administrator user.

\--cluster-ramsize

Sets the data service memory quota (in MiB). This quota will be assigned to all future nodes added to the cluster with the data service.

\--cluster-fts-ramsize

Sets the full-text service memory quota (in MiB). This parameter is required if the full-text service is specified in the --services option. This quota will be assigned to all future nodes added to the cluster with the full-text service.

\--cluster-index-ramsize

Sets the index service memory quota (in MiB). This parameter is required if the index service is specified in the --services option. This quota will be assigned to all future nodes added to the cluster with the index service.

\--cluster-name

Sets the name for this cluster. Naming clusters is useful when you have multiple Couchbase Server clusters in your deployment.

\--cluster-port

Specifies the port for the Couchbase Server Administration Console. Defaults to port 8091.

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

To change the username and password of the Couchbase Server administrator user run the following command.

$ couchbase-cli cluster-edit -c 192.168.1.5:8091 --username current_user \
 --password current_password --cluster-username new_username \
 --cluster-password new_password

To change the port number that the cluster manager listens on and the cluster name to "new\_name" run the following command.

$ couchbase-cli cluster-edit -c 192.168.1.5:8091 --username Administrator \
 --password password --cluster-port 5000 --cluster-name new_name

To change the memory quota of the data service to 2048MiB and the memory quota of the index service to 4096MiB run the following command.

$ couchbase-cli cluster-edit -c 192.168.1.5:8091 --username Administrator \
 --password password --cluster-ramsize 2048 --cluster-index-ramsize 4096

All of the parameters in this command can be specified at the same time. To change the username and password of the Couchbase Server administrator user, change the port number to 5000, change the cluster name to "new\_name", change the memory quota of the data service to 2048MiB and change the memory quota of the index service to 4096MiB run the following command.

$ couchbase-cli cluster-edit -c 192.168.1.5:8091 --username current_user \
 --password current_password --cluster-username new_username \
 --cluster-password new_password --cluster-port 5000 \
 --cluster-name new_name --cluster-ramsize 2048 --cluster-index-ramsize 4096

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

[cluster-init](couchbase-cli-cluster-init.md), [setting-cluster](couchbase-cli-setting-cluster.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite