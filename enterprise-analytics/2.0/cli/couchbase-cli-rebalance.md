---
title: rebalance
description: Rebalances data and indexes across nodes in a cluster
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/cli/pages/couchbase-cli-rebalance.adoc
  xref: xref:2.0@enterprise-analytics:cli:couchbase-cli-rebalance.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/cli/couchbase-cli-rebalance.html)

# rebalance

Rebalances data and indexes across nodes in a cluster

## [](#synopsis)SYNOPSIS

_couchbase-cli rebalance_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--server-remove <servers>]
    [--update-services] [--fts-add <servers>] [--fts-remove <servers>]
    [--index-add <servers>] [--index-remove <servers>] [--query-add <servers>]
    [--query-remove <servers>] [--backup-add <servers>]
    [--backup-remove <servers>] [--analytics-add <servers>]
    [--analytics-remove <servers>] [--eventing-add <servers>]
    [--eventing-remove <servers>] [--no-progress-bar] [--no-wait]

## [](#description)DESCRIPTION

Rebalances data and indexes across all nodes in the cluster. This command should be used after nodes are added, removed, or failed over from the cluster in order to ensure that each node in the cluster has a similar "balanced" amount of data and indexes.

To add nodes use the [server-add](couchbase-cli-server-add.md) subcommand. To remove nodes specify the list of nodes to remove using the --server-remove option in the rebalance subcommand. To failover nodes see the [failover](couchbase-cli-failover.md) subcommand. After running the [server-add](couchbase-cli-server-add.md) or [failover](couchbase-cli-failover.md)subcommands ensure that you run the rebalance command to balance data and indexes across the cluster.

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

\--server-remove <servers>

A comma separated list of nodes to remove from the cluster. Each node in the list should correspond to the hostname or IP address of that server.

\--update-services

Should be used when either adding or removing services from a node. This option can not be used with the --server-remove option, and should be used if and only if the services on the node are being updated using one or more of the other flags in this command which add or remove services e.g. --fts-add, --index-remove, etc.

\--fts-add <servers>

A comma separated list of nodes to add the Search Service to.

\--fts-remove <servers>

A comma separated list of nodes to remove the Search Service from.

\--index-add <servers>

A comma separated list of nodes to add the Index Service to.

\--index-remove <servers>

A comma separated list of nodes to remove the Index Service from.

\--query-add <servers>

A comma separated list of nodes to add the Query Service to.

\--query-remove <servers>

A comma separated list of nodes to remove the Query Service from.

\--backup-add <servers>

A comma separated list of nodes to add the Backup Service to.

\--backup-remove <servers>

A comma separated list of nodes to remove the Backup Service from.

\--analytics-add <servers>

A comma separated list of nodes to add the Analytics Service to.

\--analytics-remove <servers>

A comma separated list of nodes to remove the Analytics Service from.

\--eventing-add <servers>

A comma separated list of nodes to add the Eventing Service to.

\--eventing-remove <servers>

A comma separated list of nodes to remove the Eventing Service from.

\--no-progress-bar

Hides the progress bar which tracks the progress of the rebalance. This command will still wait for rebalance completion even if this flag is specified, but the progress bar will not be shown.

\--no-wait

Specifies that this command should not wait for the completion of rebalance before exiting.

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

To rebalance a new node into the cluster you would first add a node using the [server-add](couchbase-cli-server-add.md) command and then start the rebalance with the rebalance command.

$ couchbase-cli server-add -c 192.168.1.5:8091 --username Administrator \
 --password password --server-add 192.168.1.6:8091 \
 --server-add-username Administrator --server-add-password password

$ couchbase-cli rebalance -c 192.168.1.5:8091 --username Administrator \
 --password password

If you just want to remove a node from the cluster and start a rebalance, just run the rebalance command.

$ couchbase-cli rebalance -c 192.168.1.5:8091 --username Administrator \
 --password password --server-remove 192.168.1.6:8091

You can remove multiple nodes at once and run the rebalance with the command below. It will be faster overall removing multiple nodes at once as opposed to removing them one at a time.

$ couchbase-cli rebalance -c 192.168.1.5:8091 --username Administrator \
 --password password --server-remove 192.168.1.6:8091,192.168.1.7:8091

To add a node and remove another node you need to run the [server-add](couchbase-cli-server-add.md) command before starting the rebalance, as shown below.

$ couchbase-cli server-add -c 192.168.1.5:8091 --username Administrator \
 --password password --server-add 192.168.1.6:8091 \
 --server-add-username Administrator --server-add-password password

$ couchbase-cli rebalance -c 192.168.1.5:8091 --username Administrator \
 --password password --server-remove 192.168.1.7:8091

If you add one node to the cluster and remove a node during the same rebalance, Enterprise Analytics will do a "swap rebalance". This means data and indexes from the node being removed are moved to the one being added. This means the rebalance will only occur between these two nodes as opposed to involving all nodes in the cluster.

To add and remove services from particular nodes, you can use the update-services flag along with the appropriate flags. For example, to add the Search Service to a node and remove the Index Service from another node:

$ couchbase-cli rebalance -c 192.168.1.5:8091 --username Administrator \
 --password password --update-services --fts-add 192.168.1.5:8091 \
 --index-remove 192.168.1.6:8091

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

[failover](couchbase-cli-failover.md), [recovery](couchbase-cli-recovery.md), [server-add](couchbase-cli-server-add.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite