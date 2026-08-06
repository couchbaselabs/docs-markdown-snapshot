---
title: server-readd
description: Adds a node back to the cluster after a failover
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/cli/pages/couchbase-cli-server-readd.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:cli:couchbase-cli-server-readd.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/cli/couchbase-cli-server-readd.html)

# server-readd

Adds a node back to the cluster after a failover

## [](#synopsis)SYNOPSIS

_couchbase-cli server-readd_ [--cluster <url>] [--username <username>] [--password <password>] [--client-cert <path>]
    [--client-cert-password <password>] [--client-key <path>] [--client-key-password <password>]
    [--server-add <servers>] [--group-name <name>] [--server-username <username>] [--server-password <password>]

## [](#description)DESCRIPTION

DEPRECATED: This command was deprecated in 5.0.0 and will be removed in future releases. Please use the [recovery](couchbase-cli-recovery.md) subcommand which provides similar functionality to this command.

The server-readd subcommand is used to add a server back to the cluster. This operation is useful after a node is failed over and also when a node is removed from the cluster for maintenance.

When a node is failed over and removed from the cluster it may be able to be added back to the cluster. An example of this is when a node loses power. This node might get failed over and removed from the cluster, but once power is restored to the node you may want to add it back to the cluster.

Another use case is taking a node out of the cluster for maintenance. This is done by gracefully failing over a node to ensure there is no data loss. The administrator can then perform maintenance on the removed node and add it back with the server-readd command.

It is also possible to add a server back to the cluster without removing the data and instead having the server recover data from where it left off. This is called delta recovery and is available from the [recovery](couchbase-cli-recovery.md) subcommand.

> [!NOTE]
> After the server-readd subcommand is run you must rebalance the cluster. See the [rebalance](couchbase-cli-rebalance.md) command for more information about rebalancing a cluster.

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

\--server-add <servers>

A comma separated list of nodes to readd. The each server should correspond to the hostname or IP address of a server to be added back to the cluster.

\--server-username <username>

Adding a node back to the cluster can only be done by a user with the appropriate credentials. This flag specifies the username for a user who has the ability to modify the cluster topology of the node being added back.

\--server-password <password>

Adding a node back to the cluster can only be done by a user with the appropriate credentials. This flag specifies the password for a user who has the ability to modify the cluster topology of the node being added back.

\--group-name <name>

The name of the group to add the node to.

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

If there is a node at 192.168.1.6:8091 that you want to add back and that node has credentials that allow us to change the cluster topology with "Administrator" as the username and "password" as the password, run the following command.

$ couchbase-cli server-readd -c 192.168.1.5:8091 --username Administrator \
 --password password --server-add 192.168.1.6:8091 \
 --server-username Administrator --server-password password

If you need to add back multiple nodes then you would run the following command.

$ couchbase-cli server-readd -c 192.168.1.5:8091 --username Administrator \
 --password password --server-add 192.168.1.6:8091,192.168.1.7:8091 \
 --server-username Administrator --server-password password

If you wanted the nodes being added back to the cluster to be a part of the "East" group we would run the following command

$ couchbase-cli server-readd -c 192.168.1.5:8091 --username Administrator \
 --password password --server-add 192.168.1.6:8091 --group-name East \
 --server-username Administrator --server-password password

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

[rebalance](couchbase-cli-rebalance.md), [recovery](couchbase-cli-recovery.md), [server-add](couchbase-cli-server-add.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite