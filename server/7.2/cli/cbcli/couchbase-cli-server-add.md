---
title: server-add
description: Adds a server to the cluster
editUrl: https://github.com/couchbase/couchbase-cli/edit/neo/docs/modules/cli/pages/cbcli/couchbase-cli-server-add.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:cli:cbcli/couchbase-cli-server-add.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/cli/cbcli/couchbase-cli-server-add.html)

# server-add

Adds a server to the cluster

## [](#synopsis)SYNOPSIS

_couchbase-cli server-add_ [--cluster <url>] [--username <username>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>] [--client-key-password <password>]
    [--server-add <servers>] [--group-name <name>]
    [--server-add-username <username>] [--server-add-password <password>]
    [--services <services>] [--index-storage-setting <mode>]

## [](#description)DESCRIPTION

The server-add subcommand is used to add one or more servers to a cluster. Before adding a server it is important to decide which services the server will be running and whether or not the server should be a part of a specific group. Keep in mind that if the index service is being added on one of the servers and the cluster is not currently running the index service that you also need to set the index storage mode. This can be done with the --index-storage-setting option.

Note that the server to be added can not be specified using the http scheme since, in 7.1+, addition must occur over a secure connection.

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

\--server-add <servers>

A comma separated list of servers to add to the cluster. The each server in the list should be identified by a hostname or IP address. If a scheme is not provided it will use `https://`

\--server-add-username <username>

Adding a server to the cluster can only be done by a user with the appropriate credentials. This flag specifies the username for a user who has the ability to modify the cluster topology on the server being added.

\--server-add-password <password>

Adding a server to the cluster can only be done by a user with the appropriate credentials. This flag specifies the password for a user who has the ability to modify the cluster topology on the server being added.

\--group-name <name>

The name of the group to add the server to. If this option is not specified then the server is added to the default group.

\--services <services>

A comma separated list of services that this server should be running. Accepted services are "data", "index", "query", "fts", "eventing", "analytics" and "backup".

\--index-storage-setting <mode>

Specifies the index storage mode. This parameter must be set if the servers being added contain the index service and this is the first time the index service is being added in this cluster. You may specify "default" for disk based indexes or `memopt` for memory optimized indexes.

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

If we want to add a server at 192.168.1.6:8091 with the index, data and query service on it then we would run the command below.

$ couchbase-cli server-add -c 192.168.1.5:8091 --username Administrator \
 --password password --server-add https://192.168.1.6:18091 \
 --server-add-username Administrator --server-add-password password
 --services data,index,query

Note that in the example above we set the username and password of the server being added to the same value as the username and password of the servers already in the cluster. This is done if the server being added has not already been initialized. If the server being added has been initialized then you will need to specify an appropriate username and password for the server being added.

Now lets add two server to the East group with data, index,and full-text services. In this example we will also assume that the index is being added for the first time so we need to specify the index storage mode. If we want to index storage mode to be memory optimized then we would run the following command.

$ couchbase-cli server-add -c 192.168.1.5:8091 --username Administrator \
 --password password --server-add https://192.168.1.6:18091,https://192.168.1.7:18091 \
 --server-username Administrator --server-password password
 --services data,fts --group-name --index-storage-setting memopt

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

[rebalance](couchbase-cli-rebalance.md), [server-info](couchbase-cli-server-info.md), [server-list](couchbase-cli-server-list.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite