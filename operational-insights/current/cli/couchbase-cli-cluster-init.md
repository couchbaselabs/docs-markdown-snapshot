---
title: cluster-init
description: Initializes an Operational Insights cluster
pubDate: 2026-10-28T04:21:06.350Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/cli/pages/couchbase-cli-cluster-init.adoc
  xref: xref:enterprise-analytics:cli:couchbase-cli-cluster-init.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/cli/couchbase-cli-cluster-init.html)

# cluster-init

Initializes an Operational Insights cluster

## [](#synopsis)SYNOPSIS

_couchbase-cli cluster-init_ [--cluster <url>] [--cluster-username <username>] [--cluster-password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--cluster-port <port>]
    [--cluster-ramsize <mebibytes>] [--cluster-name <name>]
    [--cluster-analytics-ramsize <mebibytes>]
    [--update-notifications <1|0>]
    [--ip-family <ipv4|ipv6|ipv4-only|ipv6-only>] [--node-to-node-encryption <on|off>]

## [](#description)DESCRIPTION

Initializes the first node in an Operational Insights cluster. Before you initialize the cluster, configure its object storage with the [setting-operational-insights](couchbase-cli-setting-operational-insights.md) command. If you have not configured the object storage, cluster-init fails. Memory quotas are global settings, and apply to each node added to the cluster.

## [](#options)OPTIONS

\-c

\--cluster

Specifies the hostname of the cluster to initialize. By default, this parameter is set to localhost:8091 for this command. See the HOST FORMATS section for more information about specifying a hostname.

\--cluster-username

When starting a new cluster you need to create the Operational Insights built-in administrator user for the cluster. This user will be able to access the Operational Insights Administration Console as well as be used for data access and future configuration. This option specifies the username for the administrator user.

\--cluster-password

When starting a new cluster you need to create the Operational Insights built-in administrator user for the cluster. This user will be able to access the Operational Insights Administration Console as well as be used for data access and future configuration. This option specifies the password for the administrator user.

\--cluster-ramsize

Sets a memory quota (in MiB). Operational Insights fixes this quota at 100MiB, so always set it to 100.

\--cluster-analytics-ramsize

Sets the Analytics memory quota (in MiB). This quota is assigned to all future nodes added to the cluster.

\--cluster-name

Sets the name for this cluster. Naming clusters is useful when you have multiple Operational Insights clusters in your deployment.

\--cluster-port

Specifies the port for the Couchbase Administration Console. Defaults to port 8091.

\--update-notifications

Specifies whether or not software update notifications and sharing of system performance information should be enabled. To enable notifications set this flag to "1". To disable notifications set this flag to "0". By default it's enabled and notifications will be displayed in the Couchbase web console when a new version of Operational Insights is available. This system also collects information about use and experience with the product every time an administrator interacts with the administrator user interface. It collects configuration, usage and performance data, including cluster information (such as settings and configuration, software version, cluster ID, load levels, and resource quotas), and browser and network information (such as IP address, inferred geolocation only at the city level, and browser type). This does not allow Couchbase to track your specific interactions or usage of Operational Insights. Couchbase, Inc never accesses or collects any data stored within Operational Insights. This feature can be disabled at any time by using 'couchbase-cli-setting-notification.' For more information about this feature, please see the "Couchbase Server Privacy FAQ" in the product documentation, which supplements the Couchbase Privacy Policy available online. This feature is only available in Couchbase Enterprise Edition.

\--ip-family

Specifies what IP family the cluster should used. The default option is 'ipv4'. When 'ipv4-only' or 'ipv6-only' is used the cluster will only listen on that address.

\--node-to-node-encryption

Specifies if node to node encryption should be used. The default option is 'off'. When set to 'on' all communications between nodes will be over a encrypted connection.

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

To initialize an Operational Insights cluster with an Analytics memory quota of 4096MiB, run the following command.

$ couchbase-cli cluster-init -c 127.0.0.1 --cluster-username Administrator \
 --cluster-password password --cluster-ramsize 100 \
 --cluster-analytics-ramsize 4096

To set the port number, use the --cluster-port option. The following example sets up a cluster on port 5000.

$ couchbase-cli cluster-init -c 127.0.0.1 --cluster-username Administrator \
 --cluster-password password --cluster-ramsize 100 \
 --cluster-analytics-ramsize 4096 --cluster-port 5000

## [](#discussion)DISCUSSION

The cluster-init subcommand sets up the first node of an Operational Insights cluster. To set per-node settings such as the data storage directories or the hostname, see the [node-init](couchbase-cli-node-init.md) command. To add nodes to an initialized cluster, use the [server-add](couchbase-cli-server-add.md) command. Some cluster settings can be changed after a cluster is initialized. Use the [setting-cluster](couchbase-cli-setting-cluster.md) command to edit these settings.

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

[cluster-edit](couchbase-cli-cluster-edit.md), [setting-operational-insights](couchbase-cli-setting-operational-insights.md), [node-init](couchbase-cli-node-init.md), [server-add](couchbase-cli-server-add.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite