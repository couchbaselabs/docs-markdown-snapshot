[View original HTML](/server/7.6/cli/cbcli/couchbase-cli-setting-autofailover.html)

Modifies auto-failover settings

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-autofailover_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--enable-auto-failover <num>]
    [--auto-failover-timeout <seconds>] [--max-failovers <num>]
    [--enable-failover-on-data-disk-issues <num>]
    [--failover-data-disk-period <seconds>] [--can-abort-rebalance <1|0>]

## [](#description)DESCRIPTION

Auto-failover allows unresponsive servers to be failed over automatically by the cluster manager. Data partitions in Couchbase are always served from a single master node. As a result if a server is down in the cluster data from that server will be not be available while that server is down. The server will either need to be manually or automatically failed over in order to promote replica data partitions on replica servers to active data partitions so that they can be accessed by the application.

Since the administrator will not always be able to manually fail servers over quickly enough to avoid application down time Couchbase provides an auto-failover feature. This feature allows the cluster manager to automatically fail over down nodes over and bring the cluster back to a healthy state as quickly as possible.

In Couchbase Server Enterprise Edition nodes can also be automatically failed over when the Data Service reports sustained disk I/O failures.

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

\--enable-auto-failover <num>

Specifies whether or not autofailover is enabled. Set this option to "1" to enable autofailover or "0" to disable autofailover.

\--auto-failover-timeout <seconds>

Specifies the auto-failover timeout. This is the amount of time a node must be unresponsive before the cluster manager considers the node to be down and fails it over. The minimum auto-failover timeout is 30 seconds in Couchbase Community Edition and 5 seconds in Couchbase Enterprise Edition.

\--max-failovers <num>

Specifies the number of auto-failover events that will be handled before requiring user intervention. A single event could be one node failing over or an entire Server Group. The maximum allowed value is 100\. This feature is only available in Couchbase Enterprise Edition.

\--enable-failover-on-data-disk-issues <num>

Specifies whether or not autofailover on Data Service disk issues is enabled. Set this option to "1" to enable failover on Data Service disk issue or "0" to disable it. "--failover-data-disk-period" needs to be set at the same time when enabling this option. This feature is only available in Couchbase Enterprise Edition.

\--failover-data-disk-period <seconds>

Specifies the failover data disk period. This is the period of time over which the Data Service is checked for potential sustained Disk I/O failures. The Data Service is checked every second for disk failures. If 60% of the checks during that time period report disk failures, then the node may be automatically failed over. "--enable-failover-on-data-disk-issues" must be set when this option is used. The failover data disk period ranges from 5 to 3600 seconds.

\--can-abort-rebalance <1|0>

Enables auto-failover to abort rebalance and perform auto-failover. This feature is only available in Couchbase Enterprise Edition.

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

To enable autofailover with a 30 second auto-failover timeout run the following command.

$ couchbase-cli setting-autofailover -c 192.168.1.5 --username Administrator \
 --password password --enable-auto-failover 1 --auto-failover-timeout 30

To enable autofailover with a 120 second auto-failover timeout run the following command.

$ couchbase-cli setting-autofailover -c 192.168.1.5 --username Administrator \
 --password password --enable-auto-failover 1 --auto-failover-timeout 120

To enable autofailover with a 120 second auto-failover timeout and to enable failover on Data Service Disk issue with a 10 second data disk period run the following command.

$ couchbase-cli setting-autofailover -c 192.168.1.5 --username Administrator \
 --password password --enable-auto-failover 1 --auto-failover-timeout 120 \
 --enable-failover-on-data-disk-issues 1 --failover-data-disk-period 10

To enable autofailover with a 120 second auto-failover timeout and allow up to two auto failover events

$ couchbase-cli setting-autofailover -c 192.168.1.5 --username Administrator \
 --password password --enable-auto-failover 1 --auto-failover-timeout 120 \
 --max-failovers 2

To disable autofailover run the following command.

$ couchbase-cli setting-autofailover -c 192.168.1.5 --username Administrator \
 --password password --enable-auto-failover 0

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

[failover](couchbase-cli-failover.md), [recovery](couchbase-cli-recovery.md), [setting-alert](couchbase-cli-setting-alert.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite