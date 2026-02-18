---
title: node-init
description: Initializes a node
editUrl: https://github.com/couchbase/couchbase-cli/edit/trinity/docs/modules/cli/pages/cbcli/couchbase-cli-node-init.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/cli/cbcli/couchbase-cli-node-init.html)

# node-init

Initializes a node

## [](#synopsis)SYNOPSIS

_couchbase-cli node-init_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--node-init-data-path <path>]
    [--node-init-index-path <path>] [--node-init-analytics-path <path>]
    [--node-init-eventing-path <path>] [--node-init-hostname <hostname>]
    [--node-init-java-home <path>] [--ipv4] [--ipv6]

## [](#description)DESCRIPTION

This command initializes a Couchbase Server node. In particular this command allows the user to set the data path, index path, analytics path, java home and hostname. These settings must be set prior to initializing the cluster or adding the node to an existing cluster as they cannot be changed later. The hostname however can be changed later if the node is the only node in the cluster.

To get the best performance from Couchbase Server, it is recommended that the data, index and analytics paths be set to separate disks.

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

\--node-init-data-path

The path to store data files create by the Couchbase data service. Note that this path is also where view indexes are written on this server. This flag can only be specified against a node that is not yet part of a cluster.

\--node-init-index-path

The path to store files create by the Couchbase index service. This flag can only be specified against a node that is not yet part of a cluster.

\--node-init-analytics-path

The path to store files create by the Couchbase Analytics service. This flag can only be specified against a node that is not yet part of a cluster. Multiple paths can be specified by setting this option multiple times.

\--node-init-eventing-path

The path to store files create by the Couchbase Eventing service. This flag can only be specified against a node that is not yet part of a cluster.

\--node-init-hostname

Specifies the hostname for this server.

\--node-init-java-home

Specifies the location of the Java Runtime Environment for the Analytics service to use.

\--ipv4

Switch the node to use ipv4 for node to node communication

\--ipv6

Switch the node to use ipv6 for node to node communication

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

To initialize a node and set the index path to `/mnt1/indexes` and the data path to `/mnt2/data` run the following command. Note that this command must be run before the node becomes part of a cluster.

$ couchbase-cli node-init -c 192.168.1.5 \
   --node-init-data-path /mnt2/data --node-init-index-path /mnt1/indexes

In the command above, the cluster username and password have not yet been set so you can skip adding these to the command line. If you later initialize the cluster and want to set the hostname for the cluster, then run the command below. Note that this time the cluster is initialized, so you must include the username and password.

$ couchbase-cli node-init -c 192.168.1.5 -u Administrator -p password \
   --node-init-hostname cb1.mydomain.com

You could have alternatively set all five of these options below before initializing the cluster. This can be done with the following command.

$ couchbase-cli node-init -c 192.168.1.5 --node-init-hostname cb1.mydomain.com \
   --node-init-data-path /mnt2/data --node-init-index-path /mnt1/indexes \
   --node-init-analytics-path /mnt3/analytics \
   --node-init-java-home /usr/lib/java/

Again, note that you don’t need the username and password because in this example the cluster has not yet been initialized.

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

[cluster-init](couchbase-cli-cluster-init.md), [server-add](couchbase-cli-server-add.md), [node-reset](couchbase-cli-node-reset.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite