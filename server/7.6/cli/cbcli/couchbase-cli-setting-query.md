---
title: setting-query
description: Manage query engine settings
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/couchbase-cli/edit/trinity/docs/modules/cli/pages/cbcli/couchbase-cli-setting-query.adoc
  xref: xref:7.6@server:cli:cbcli/couchbase-cli-setting-query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbcli/couchbase-cli-setting-query.html)

# setting-query

Manage query engine settings

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-query [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--get] [--set] [--pipeline-batch <num>]
    [--pipeline-cap <num>] [--scan-cap <size>] [--timeout <ms>]
    [--prepared-limit <max>] [--completed-limit <max>]
    [--log-level <trace|debug|info|warn|error|server|none>]
    [--max-parallelism <max>] [--n1ql-feature-control <num>]
    [--temp-dir <path>] [--temp-dir-size <mebibytes>]
    [--cost-based-optimizer <1|0>] [--memory-quota <mebibytes>]
    [--transaction-timeout <duration>] [--node-quota <mebibytes>]
    [--node-quota-val-percent <perc>] [--use-replica <unset|off|on>]
    [--curl-access <restricted|unrestricted>] [--allowed-urls <urls>]
    [--disallowed-urls <urls>]

## [](#description)DESCRIPTION

Manage query service settings

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

\--get

Retrieve current query service settings.

\--set

Set query engine settings.

\--pipeline-batch <num>

Number of items execution operators can batch, the default is 16.

\--pipeline-cap <num>

Maximum number of items each execution operator can buffer, the default 512.

\--scan-cap <size>

Maximum buffer size for index scans; use zero or negative value to disable. The default 512.

\--timeout <ms>

Server execution timeout; use zero or negative value to disable. By default is unlimited.

\--prepared-limit <max>

Maximum number of prepared statements, the default is 16384.

\--completed-limit <max>

Maximum number of completed requests, the default is 4000.

\--completed-threshold <ms>

Cache completed queries lasting longer than this threshold (in milliseconds), the default is 1000.

\--log-level <trace|debug|info|warn|error|server|none>

Query engine log level, the default level is info.

\--max-parallelism <max>

Maximum parallelism per query; use zero or negative value to disable. The default is 1.

\--n1ql-feature-control <num>

SQL++ Feature Controls. 0x0001 (1) Disable Index Aggregation

\--temp-dir <path>

Specify the directory for temporary query data.

\--temp-dir-size <mebibytes>

Maximum size in mebibytes for the temporary query data directory.

\--cost-based-optimizer <1|0>

Enable (1) or disable (0) the Cost Based Optimizer (CBO), which uses statistics and metadata to estimate the amount of processing required and creates a query plan with the least cost. This feature is in Developer Preview and should not be used in production environments.

\--memory-quota <mebibytes>

The maximum amount of memory the query service will use in each node.

\--transaction-timeout <duration>

The timeout for transactional queries. The duration is a number followed by a unit such as (100ns, 10ms, 1s, 1m).

\--node-quota <mebibytes>

The maximum amount of memory that the query service will allow node wide for loaded documents, not including caches, plans or transactions.

\--node-quota-val-percent <perc>

The percentage of node-quota that is reserved for value memory.

\--use-replica <unset|off|on>

Specify whether or not a query can read from replica vBuckets. When set to "unset", whether or not replica vBuckets are read from is set at request level. When set to "off", it is always disabled for all queries and this cannot be overridden. When set to "on", it is by default enabled for all queries, but this can be disabled at request level.

## [](#query-curl-access-options)QUERY CURL ACCESS OPTIONS

\--curl-access <restricted|unrestricted>

Specify either unrestricted or restricted, to determine which URLs are permitted to be accessed by the curl function.

\--allowed-urls <urls>

Comma separated lists of URLs that are allowed to be accessed by the curl function. This option must be provided together with --curl-access restricted. If disallowed-urls also provided then the disallowed list takes precedence.

\--disallowed-urls <urls>

Comma separated lists of URLs that are disallowed to be accessed by the curl function. This option must be provided together with --curl-access restricted. If allowed-urls also provided then the disallowed list takes precedence.

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

To retrieve the query settings:

$ couchbase-cli setting-query -c 127.0.01:8091 -u Administrator \
 -p password --get

To set any of the query settings for example maximum parallelism and log level:

$ couchbase-cli setting-query -c 127.0.01:8091 -u Administrator \
 -p password --set --log-level debug --max-parallelism 4

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

[couchbase-cli](couchbase-cli.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite