---
title: setting-alert
description: Modifies alert settings
editUrl: https://github.com/couchbase/couchbase-cli/edit/neo/docs/modules/cli/pages/cbcli/couchbase-cli-setting-alert.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:cli:cbcli/couchbase-cli-setting-alert.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/cli/cbcli/couchbase-cli-setting-alert.html)

# setting-alert

Modifies alert settings

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-alert_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--enable-email-alert <num>]
    [--email-recipients <email_list>] [--email-sender <email>]
    [--email-user <user>] [--email-password <password>] [--email-host <host>]
    [--email-port <port>] [--enable-email-encrypt <num>]
    [--alert-auto-failover-node] [--alert-auto-failover-max-reached]
    [--alert-auto-failover-node-down] [--alert-auto-failover-cluster-small]
    [--alert-auto-failover-disable] [--alert-ip-changed] [--alert-disk-space]
    [--alert-meta-overhead] [--alert-meta-oom] [--alert-write-failed]
    [--alert-audit-msg-dropped] [--alert-indexer-max-ram]
    [--alert-timestamp-drift-exceeded] [--alert-node-time] [--alert-disk-analyzer]
    [--alert-memory-threshold] [--alert-bucket-history-size]
    [--alert-indexer-low-resident-percentage] [--alert-memcached-connections]

## [](#description)DESCRIPTION

This command is used to set up email alerts on a cluster. Couchbase provides alerts for various issues that may arise in the cluster where it is recommended that the cluster administrator take action to ensure that applications continue to function properly. When setting up email alerts administrator can decide who gets alert emails and which alerts are sent.

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

\--enable-email-alert <num>

Enables email alerts on this cluster. Set this option to "1" to enable alerts or "0" to disable alerts. This parameter is required.

\--email-recipients <email\_list>

A comma separated list of users to email when an alert is raised in the server.

\--email-sender <email>

If email alerts an enabled then this option will set the sender email address.

\--email-user <user>

The email server username for the sender email address. This field is required if the email address provided requires authentication.

\--email-password <password>

The email server password for the sender email address. This field is required if the email address provided requires authentication.

\--email-host <host>

The email server hostname that hosts the email address specified by the --sender-email option.

\--email-port <port>

The email server port number of the server that hosts the email address specified by the --sender-email option.

\--enable-email-encrypt <num>

Enables SSL encryption when connecting to the email server. Set this option to "1" to enable encryption or "0" to disable encryption. If this option is not set then encryption will be disabled.

\--alert-auto-failover-node

Specifies that an email alert should be sent when a node is automatically failed over.

\--alert-auto-failover-max-reached

Specifies that an email alert should be sent when the maximum amount of auto-failovers is reached.

\--alert-auto-failover-node-down

Specifies that an email alert should be sent when auto-failover could not be completed because another node in the cluster was already down.

\--alert-auto-failover-cluster-small

Specifies that an email alert should be sent when auto-failover could not be completed because the cluster is too small.

\--alert-auto-failover-disable

Specifies that an email alert should be sent when auto-failover could not be completed because auto-failover is disabled on this cluster.

\--alert-ip-changed

Specifies that an email alert should be sent when the IP address on a node in the cluster changes.

\--alert-disk-space

Specifies that an email alert should be sent when the disk usage on a node in the cluster reaches 90% of the available disk space.

\--alert-meta-overhead

Specifies that an email alert should be sent when the metadata overhead on the data service is more than 50%.

\--alert-meta-oom

Specifies that an email alert should be sent when all of the memory in the cache for a bucket is used by metadata. If this condition is hit the bucket will be unusable until more memory is added to the bucket cache.

\--alert-write-failed

Specifies that an email alert should be sent when writing data to disk on the data service has failed.

\--alert-audit-msg-dropped

Specifies that an email alert should be sent when writing event to audit log fails.

\--alert-indexer-max-ram

Specifies that an email alert should be sent when the memory usage for the indexer service on a specific node exceeds the per node memory usage limit. This warning is only shown for if the index storage type is Memory Optimized Indexes (MOI).

\--alert-timestamp-drift-exceeded

Specifies that an email alert should be sent if the remote mutation timestamps exceeds drift threshold. Default is 5 seconds.

\--alert-communication-issue

Specifies that an email alert should be sent when nodes are experiencing communication issues.

\--alert-node-time

Specifies that an email alert should be sent if the clock on a node is out of sync with other nodes in the cluster.

\--alert-disk-analyzer

Specifies that an email alert should be sent if the disk analyzer process gets stuck and cannot fetch disk usage data.

\--alert-memory-threshold

Specifies that an email alert should be sent when any node's system memory usage exceeds a threshold.

\--alert-bucket-history-size

Specifies that an email alert should be sent when the size of history for a bucket reaches 90% of the maximum history size.

\--alert-indexer-low-resident-percentage

Specifies that an email alert should be sent when approaching the indexer low resident percentage.

\--alert-memcached-connections

Specifies that an email alert should be sent when the memcached connection threshold is exceeded.

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

To enable failover related email alerts for two users without email encryption run the following command below:

$ couchbase-cli setting-alert -c 192.168.1.5 --username Administrator \
 --password password --enable-email-alert 1 --email-user admin \
 --email-password password --email-host mail.couchbase.com --email-port 25 \
 --email-recipients user1@couchbase.com,user2@couchbase.com \
 --email-sender noreply@couchbase.com --enable-email-encrypt 0 \
 --alert-auto-failover-node --alert-auto-failover-max-reached \
 --alert-auto-failover-node-down --alert-auto-failover-cluster-small \

To enable all email alerts for a single users with email encryption run the following command below:

$ couchbase-cli setting-alert -c 192.168.1.5 --username Administrator \
 --password password --enable-email-alert 1 --email-user admin \
 --email-password password --email-host mail.couchbase.com --email-port 25 \
 --email-recipients user@couchbase.com --email-sender noreply@couchbase.com \
 --enable-email-encrypt 1 --alert-auto-failover-node \
 --alert-auto-failover-max-reached --alert-auto-failover-node-down \
 --alert-auto-failover-cluster-small --alert-auto-failover-disable \
 --alert-ip-changed --alert-disk-space --alert-meta-overhead \
 --alert-meta-oom --alert-write-failed --alert-audit-msg-dropped \
 --alert-indexer-max-ram --alert-timestamp-drift-exceeded \
 --alert-node-time --alert-disk-analyzer --alert-memory-threshold \
 --alert-bucket-history-size

To disable email alerts run the following command:

$ couchbase-cli setting-alert -c 192.168.1.5 --username Administrator \
 --password password --enable-email-alert 0

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

[setting-notification](couchbase-cli-setting-notification.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite