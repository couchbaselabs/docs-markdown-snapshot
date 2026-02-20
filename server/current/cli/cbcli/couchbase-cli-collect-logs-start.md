---
title: collect-logs-start
description: Start log collection
editUrl: https://github.com/couchbase/couchbase-cli/edit/morpheus/docs/modules/cli/pages/cbcli/couchbase-cli-collect-logs-start.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:cli:cbcli/couchbase-cli-collect-logs-start.adoc[]
---

[View original HTML](/server/current/cli/cbcli/couchbase-cli-collect-logs-start.html)

# collect-logs-start

Start log collection

## [](#synopsis)SYNOPSIS

_couchbase-cli collect-logs-start_ [--cluster <url>] [--username <user>]
    [--password <password>] [--client-cert <path>] [--client-cert-password <password>]
    [--client-key <path>] [--client-key-password <password>] [--all-nodes] [--nodes <node_list>]
    [--redaction-level <level>] [--salt <string>]
    [--output-directory <directory>] [--temporary-directory <directory>]
    [--upload] [--upload-host <host>] [--upload-proxy <host>]
    [--customer <customer>] [--ticket <ticket>]
    [--encryption-password <password>]

## [](#description)DESCRIPTION

This command collects all Couchbase Server log files from one or more nodes in the cluster. Log collection is useful when there are failures in the cluster and you need to figure out what is going on. Since there are many log files on various different server the collect-logs-start command helps in aggregating all of the different log file Couchbase Server creates.

To get the location of the collected log files you can run the [collect-logs-status](couchbase-cli-collect-logs-status.md) command either while the log collection task is running or after the log collection task has completed. If the --upload flag is specified then the logs will also be uploaded to the host specified in the --upload-host flag. The upload flag is intended for Couchbase Server Enterprise Edition users who need to upload logs to the Couchbase Support Team to aid in diagnosing support tickets that they have filed.

Note that only one log collection task may be running at any given time in the cluster.

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

\--all-nodes

Specifies that log collection should take place on all nodes in the cluster. May not be specified at the same time as --nodes.

\--nodes <node\_list>

A list of one or more nodes to collect logs from, the nodes must include the administrator port. The nodes should be comma separated. This option may not be specified at the same time as the --all-nodes option.

\--redaction-level <level>

Specifies what level the logs should be redacted too. This option has two levels "none" and "partial". If partial is set then data such as usernames, keys and values will be redacted from the logs. If none is set then no data will be redacted. Please note that increasing the level of redaction can have an impact on debugging problems.

\--salt <string>

Specifies the string to used as the salt. This option can only be used when --redaction-level is set to "partial". The salt is used to increase the security of the redacted log files. If the option is not specified then a salt is generated each time the logs are collected. It is important to specify the salt if logs are from multiple collections or logs from client SDKs have to be cross referenced against each other.

\--output-directory <directory>

Specifies the directory on the node to place the logs. This is the location where the logs will be placed after collection has finished. Log collection will fail for the nodes that do not have this directory. It will also fail if the directory does not have enough space.

\--temporary-directory <directory>

Specifies the temporary directory on the node to use while generating the logs. During log collection a number of temporary files are created before being compressed. If this temporary location does not have enough space log collection will fail. All nodes in the cluster must have this directory. When it is not specified then the operating system temporary directory will be used.

\--upload

Specifies that the logs should be uploaded to the host specified with the --upload-host option. This option should be used by Couchbase Server Enterprise customers when uploading logs for the Couchbase Support Team.

\--upload-proxy <host>

Specifies the proxy to use when uploading logs. This is useful when a cluster is deployed in secure environments and do not have a direct outbound connection to the internet to upload logs.

\--upload-host <host>

Once log collection is completed, the logs zip file should be uploaded to this URL. This parameter is required if the --upload flag is specified.

\--customer <name>

The name of the customer who is uploading these logs. This option is required if the --upload flag is specified.

\--ticket <num>

The ticket number that the support team has created to track the issue filed. This parameter is optional when specifying the --upload flag, but recommended if you have a ticket number.

\--encryption-password <encryption\_password>

The password to use to encrypt (with AES-256) the resulting zip file.

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

To collect logs on all nodes without uploading them run the following command.

$ couchbase-cli collect-logs-start -c 192.168.1.5 --username Administrator \
 --password password --all-nodes

If there is a three node cluster with IP addresses 192.168.1.5, 192.168.1.6, and 192.168.1.7 and you only want to collect logs on the first two nodes and don’t want to upload the logs then run the command below.

$ couchbase-cli collect-logs-start -c 192.168.1.5 --username Administrator \
 --password password --nodes 192.168.1.5:8091,192.168.1.6:8091

If you are a Couchbase Server Enterprise Edition user and you need to upload logs for all nodes for a support ticket then you can run the following command.

$ couchbase-cli collect-logs-start -c 192.168.1.5 --username Administrator \
 --password password --all-nodes --upload --customer customer_name \
 --upload-host s3.amazonaws.com/cb-customers --ticket 12345

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

[collect-logs-status](couchbase-cli-collect-logs-status.md), [collect-logs-stop](couchbase-cli-collect-logs-stop.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite