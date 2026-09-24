---
title: setting-operational-insights
description: Manage Operational Insights service settings
pubDate: 2026-09-24T04:27:44.823Z
antora:
  editUrl: https://github.com/couchbase/couchbase-cli/edit/morpheus/docs/modules/cli/pages/cbcli/couchbase-cli-setting-operational-insights.adoc
  xref: xref:server:cli:cbcli/couchbase-cli-setting-operational-insights.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/cli/cbcli/couchbase-cli-setting-operational-insights.html)

# setting-operational-insights

Manage Operational Insights service settings

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-operational-insights_ [--cluster <url>] [--username <user>]
    [--password <password>] [--client-cert <path>] [--client-cert-password <password>]
    [--client-key <path>] [--client-key-password <password>] [--get] [--set]
    [--partitions <num>] [--scheme <scheme>] [--bucket <bucket>]
    [--prefix <prefix>] [--region <region>] [--endpoint <endpoint>]
    [--anonymous-auth <0|1>] [--path-style-addressing <0|1>]
    [--disable-ssl-verify <0|1>] [--certificate <path>] [--access-key-id <id>]
    [--secret-access-key <key>] [--checksum-behavior <behavior>]
    [--azure-client-id <id>] [--skip-validation <0|1>]

## [](#description)DESCRIPTION

Manage Operational Insights service settings.

Most settings may be changed at any time, but `--partitions` and `--scheme` fix the shape of the storage the cluster is built on: once the cluster has been initialized and its BLOB storage configured, changing either is rejected. Set them with `--set` before running `cluster-init`.

Several settings apply to one BLOB storage scheme only, and are rejected when they conflict with the configured `--scheme`. `--region`, `--certificate`, `--path-style-addressing`, `--access-key-id`, `--secret-access-key` and `--checksum-behavior` apply to `s3` alone; `--azure-client-id` applies to `azblob` alone; and `--anonymous-auth` is not supported by `azblob`.

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

\-s

\--ssl

(Deprecated) Specifies that the connection should use SSL verification. If this flag is used then SSL will be used but the cluster certificate will not be verified by the Certificate Authority. This flag is deprecated and not recommended. If you wish to use SSL encryption it is recommended that you specify the cluster host name using either _couchbases://_ or _https://_. Each of these connection schemes will ensure that the connection is encrypted with SSL. You may then use either --no-ssl-verify or --cacert in order to customize how your SSL connection is set up.

\--no-ssl-verify

Specifies that SSL verification should be used but that verifying that the cluster certificate is valid should be skipped. Use of this flag is not recommended for production environments because it does not protect the user from a man-in-the-middle attack.

\--cacert <path>

Specifies that the SSL connection should use the cacert provided when connecting to the cluster. This argument takes the path the certificate file as its value. This is the most secure way to connect to your cluster.

\--client-cert <path>

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `--client-key` as an alternative to the `--username` and `--password` flags. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-cert-password <password>

The password for the certificate provided to the `--client-cert` flag, when using this flag, the certificate/key pair is expected to be in the PKCS#12 format. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-key <path>

The path to the client private key whose public key is contained in the certificate provided to the `--client-cert` flag. May be supplied with `--client-cert` as an alternative to the `--username` and `--password`flags. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-key-password <password>

The password for the key provided to the `--client-key` flag, when using this flag, the key is expected to be in the PKCS#8 format. See the CERTIFICATE AUTHENTICATION section for more information.

\--get

Retrieve current Operational Insights service settings.

\--set

Set Operational Insights settings.

\--partitions <num>

The number of storage partitions (positive integer, lower than the configured maximum)

\--scheme <scheme>

The BLOB storage scheme, one of `s3`, `gs` or `azblob`

\--bucket <bucket>

The BLOB storage bucket

\--prefix <prefix>

The BLOB storage prefix

\--region <region>

The BLOB storage region

\--endpoint <endpoint>

The BLOB storage endpoint

\--anonymous-auth <0|1>

Allow BLOB storage anonymous auth

\--path-style-addressing <0|1>

Use BLOB storage path style addressing

\--disable-ssl-verify <0|1>

Disable verification of the BLOB storage TLS certificate

\--certificate <path>

The path to a certificate used to verify the BLOB storage endpoint. Supply this option once for each certificate.

\--access-key-id <id>

The BLOB storage access key ID. Must be supplied together with `--secret-access-key`.

\--secret-access-key <key>

The BLOB storage secret access key. Must be supplied together with `--access-key-id`.

\--checksum-behavior <behavior>

The BLOB storage checksum behavior, either `when_required` or `when_supported`.

\--azure-client-id <id>

The BLOB storage Azure client ID

\--skip-validation <0|1>

Skip validation of the supplied BLOB storage settings. Validation writes to, reads back and deletes a test object, so it is worth skipping only where the settings are known to be good and the round trip is unwanted. Skipping validation also lifts the restriction on changing `--partitions` and `--scheme` after the cluster has been initialized, which will leave existing data unreachable — do not use it for that purpose.

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

To retrieve the Operational Insights service settings:

$ couchbase-cli setting-operational-insights -c 127.0.01:8091 -u Administrator \
 -p password --get

To set the BLOB storage scheme to s3:

$ couchbase-cli setting-operational-insights -c 127.0.01:8091 -u Administrator \
 -p password --set --scheme s3

To point the cluster at an S3-compatible endpoint with static credentials, and verify it with a private certificate authority:

$ couchbase-cli setting-operational-insights -c 127.0.01:8091 -u Administrator \
 -p password --set --scheme s3 --bucket my-bucket --region us-east-1 \
 --endpoint https://storage.example.com --path-style-addressing 1 \
 --access-key-id my-key-id --secret-access-key my-secret \
 --certificate /path/to/ca.pem

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