---
title: cluster-init
description: Initializes a Enterprise Analytics cluster
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/cli/pages/couchbase-cli-cluster-init.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.0@enterprise-analytics:cli:couchbase-cli-cluster-init.adoc[]
---

[View original HTML](/enterprise-analytics/2.0/cli/couchbase-cli-cluster-init.html)

# cluster-init

Initializes an Enterprise Analytics cluster

## [](#synopsis)SYNOPSIS

_couchbase-cli cluster-init_ [--cluster <url>] [--cluster-username <username>] [--cluster-password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--cluster-port <port>]
    [--cluster-ramsize <mebibytes>] [--cluster-name <name>]
    [--cluster-index-ramsize <mebibytes>] [--cluster-fts-ramsize <mebibytes>]
    [--cluster-eventing-ramsize <mebibytes>]
    [--cluster-analytics-ramsize <mebibytes>] [--cluster-query-ramsize <mebibytes>]
    [--index-storage-setting <setting>] [--services <services>]
    [--update-notifications <1|0>]
    [--ip-family <ipv4|ipv6|ipv4-only|ipv6-only>] [--node-to-node-encryption <on|off>]

## [](#description)DESCRIPTION

Initializes the first node in an Enterprise Analytics cluster. Before initializing a cluster you need to decide which services you will be running on this node as well as the memory quota for each service you are starting. Services started with cluster-init will be running on this server only. Future servers that are added to this cluster may be configured with different services running on them. NOTE: that the data service is always required on the first node. Memory quotas for each service are global settings and will apply to each node added to the cluster. The memory quota for a service only applies if that service is running on a given server. You may also define the index storage mode which will determine how the global secondary indexes (GSI) are stored.

## [](#options)OPTIONS

\-c

\--cluster

Specifies the hostname of the cluster to initialize. By default, this parameter is set to localhost:8091 for this command. See the HOST FORMATS section for more information about specifying a hostname.

\--cluster-username

When starting a new cluster you need to create the Enterprise Analytics built-in administrator user for the cluster. This user will be able to access the Enterprise Analytics Administration Console as well as be used for data access and future configuration. This option specifies the username for the administrator user.

\--cluster-password

When starting a new cluster you need to create the Enterprise Analytics built-in administrator user for the cluster. This user will be able to access the Enterprise Analytics Administration Console as well as be used for data access and future configuration. This option specifies the password for the administrator user.

\--cluster-ramsize

Specifies the data services memory quota (in MiB). This quota will be assigned to all future nodes added to the cluster with the data service.

\--cluster-fts-ramsize

Sets the full-text service memory quota (in MiB). This parameter is required if the full-text service is specified in the --services option. This quota will be assigned to all future nodes added to the cluster with the full-text service.

\--cluster-index-ramsize

Sets the index service memory quota (in MiB). This parameter is required if the index service is specified in the --services option. This quota will be assigned to all future nodes added to the cluster with the index service.

\--cluster-eventing-ramsize

Sets the Eventing service memory quota (in MiB). This parameter is required if the Eventing service is specified in the --services option. This quota will be assigned to all future nodes added to the cluster with the eventing service.

\--cluster-analytics-ramsize

Sets the Analytics service memory quota (in MiB). This parameter is required if the Analytics service is specified in the --services option. This quota will be assigned to all future nodes added to the cluster with the analytics service.

\--cluster-query-ramsize

Sets the Query service memory quota (in MiB). This parameter is required if the Query service is specified in the --services option. This quota will be assigned to all future nodes added to the cluster with the query service.

\--cluster-name

Sets the name for this cluster. Naming clusters is useful when you have multiple Enterprise Analytics clusters in your deployment.

\--cluster-port

Specifies the port for the Couchbase Administration Console. Defaults to port 8091.

\--index-storage-setting

Specifies the index storage mode for the index service. Accepted storage modes are "default" for the standard index backend or `memopt` for memory optimized indexes. If the index service is specified to be started with the --services command then this parameter defaults to "default". If the index service is not specified to be started then the index storage mode will not be set. You will then be required to set the index storage mode when the first index service is started on a server in the cluster. You may also define the index storage mode even if an index service is not started on the first node and it will be remembered when the first index service is added in the future. You may not change this parameter while there are index nodes in the cluster.

\--services

Specifies the services to start on this cluster. You may not change the services running on this node once the cluster has been initialized. This options takes a comma separated list of services. Accepted services are "data", "index", "query", "fts", "eventing", "analytics" and "backup" specified as a comma-separated list. This parameter defaults to "data".

\--update-notifications

Specifies whether or not software update notifications and sharing of system performance information should be enabled. To enable notifications set this flag to "1". To disable notifications set this flag to "0". By default it’s enabled and notifications will be displayed in the Couchbase web console when a new version of Enterprise Analytics is available. This system also collects information about use and experience with the product every time an administrator interacts with the administrator user interface. It collects configuration, usage and performance data, including cluster information (such as settings and configuration, software version, cluster ID, load levels, and resource quotas), and browser and network information (such as IP address, inferred geolocation only at the city level, and browser type). This does not allow Couchbase to track your specific interactions or usage of Enterprise Analytics. Couchbase, Inc never accesses or collects any data stored within Enterprise Analytics. This feature can be disabled at any time by using 'couchbase-cli-setting-notification.' For more information about this feature, please see the “Couchbase Server Privacy FAQ” in the product documentation, which supplements the Couchbase Privacy Policy available online. This feature is only available in Couchbase Enterprise Edition.

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

To create a Enterprise Analytics cluster with only the data service on the first node and a memory quota of 4096MiB run the following command.

$ couchbase-cli cluster-init -c 127.0.0.1 --cluster-username Administrator \
 --cluster-password password --services data --cluster-ramsize 4096

To create a Enterprise Analytics cluster with the data and index service then you also need to set the memory quotas for each service as well as the index storage mode since you are starting the index service.

To create a cluster with an index memory quota of 1024MiB, a data service memory quota of 2048MiB and a memory optimized index storage mode run the following command.

$ couchbase-cli cluster-init -c 127.0.0.1 --cluster-username Administrator \
 --cluster-password password --services data,index --cluster-ramsize 2048 \
 --cluster-index-ramsize 1024 --index-storage-setting memopt

To create a Enterprise Analytics cluster with all services then you need to set the memory quotas for the Data, Index, Full-Text, Eventing and Analytics service. The quotas are set to 2048MiB, 1024MiB, 1024MiB, 1024MiB and 1024MiB respectively. A quota is not set for the query service since it does not have a memory quota. You also need to set the index storage mode for the index service, which will be set to "default" since the service is started on the first node.

$ couchbase-cli cluster-init -c 127.0.0.1 --cluster-username Administrator \
 --cluster-password password --services data,index,query,fts,analytics \
 --cluster-ramsize 2048 --cluster-index-ramsize 1024 \
 --cluster-eventing-ramsize 1024 --cluster-fts-ramsize 1024 \
 --cluster-analytics-ramsize 1024 --cluster-fts-ramsize 1024 \
 --index-storage-setting default

If you want to set the port number you can do so with the --cluster-port option. In the example below, a cluster is setup on port 5000 and starts only the data service. The memory quota of the data service is set to 2048MiB.

$ couchbase-cli cluster-init -c 127.0.0.1 --cluster-username Administrator \
 --cluster-password password --services data --cluster-ramsize 2048 \
 --cluster-port 5000

## [](#discussion)DISCUSSION

The cluster-init subcommand sets up the first node on a Couchbase cluster. To set per node settings such as the data storage directory, index storage directory, or hostname see the [node-init](couchbase-cli-node-init.md) command. To add nodes to a currently initialized cluster use the [server-add](couchbase-cli-server-add.md) command. Some cluster settings may be changed after a cluster is initialized. Use the [setting-cluster](couchbase-cli-setting-cluster.md) command to edit these settings.

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

[cluster-edit](couchbase-cli-cluster-edit.md), [node-init](couchbase-cli-node-init.md), [server-add](couchbase-cli-server-add.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite