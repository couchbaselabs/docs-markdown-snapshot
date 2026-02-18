---
title: collection-manage
description: Manage collections and scopes in a bucket
editUrl: https://github.com/couchbase/couchbase-cli/edit/morpheus/docs/modules/cli/pages/cbcli/couchbase-cli-collection-manage.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/cli/cbcli/couchbase-cli-collection-manage.html)

# collection-manage

Manage collections and scopes in a bucket

## [](#synopsis)SYNOPSIS

_couchbase-cli collection-manage_ [--cluster <url>] [--username <user>]
    [--password <password>] [--client-cert <path>] [--client-cert-password <password>]
    [--client-key <path>] [--client-key-password <password>] [--bucket <bucket>]
    [--create-scope <scope>] [--drop-scope <scope>] [--list-scopes]
    [--create-collection <collection>] [--edit-collection <collection>]
    [--drop-collection <collection>] [--list-collections [<scope_list>]]
    [--max-ttl <seconds>] [--no-expiry] [--enable-history-retention <0|1>]

## [](#description)DESCRIPTION

This command is used to manage collections and scopes in a bucket. Collections allow the user to categorize the data in the bucket by creating collections and specifying a collection when adding documents to a bucket. Scopes are the grouping of collections, which allows further categorization and ease of management.

The following rules define a valid collection or scope name:

* Must be between 1 and 251 bytes long
* Can only contain characters A-Z, a-z, 0-9 and the following symbols \_ - %
* Cannot start with \_ or %

Only Couchbase and Ephemeral bucket has Collection support.

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

\--bucket <bucket>

The name of the bucket.

\--create-scope <scope>

Makes a scope in the bucket with the name provided.

\--drop-scope <scope>

Removes the scope from the bucket with the name provided.

\--list-scopes

Shows all scopes in the bucket.

\--create-collection <collection>

Makes the collection in the scope. The option takes a path in dot format (scope.collection), specifying the scope in which the collection and the name to be created.

\--edit-collection <collection>

Edits the collection in the scope. The option takes a path in dot format (scope.collection), specifying the collection in a scope which is to be edited.

\--drop-collection <collection>

Removes the collection from the scope. The option takes a path in dot format (scope.collection), specifying the scope from which the collection and collection-name are to be removed.

\--list-collections \[<scope\_list>\]

Takes an optional comma separated list of scope names. It will show all the collections inside those scopes. If no scopes are provided it will show all the collections.

\--max-ttl <seconds>

Specifies the maximum TTL (time-to-live) for all documents in the collection, in seconds. If enabled and a document is mutated with no TTL or a TTL greater than than the maximum, its TTL will be set to the maximum TTL. Setting this option to 0 will make the collection use the bucket TTL. The largest TTL that is allowed is 2147483647\. Cannot be used in conjunction with -no-expiry.

\--no-expiry

Disables the maximum TTL (time-to-live) for all documents in the collection, regardless of the bucket’s maximum TTL. Cannot be used in conjunction with --max-ttl.

\--enable-history-retention <0|1>

Specifies whether or not the document history retention should be enabled for the collection. To enable the document history retention, set this option to "1". To disable the document history retention, set this option to "0". This setting can be edited after a collection has been created.

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

To create a new scope called "chairs" in the furniture bucket.

$ couchbase-cli collection-manage -c 192.168.1.5 -u Administrator \
 -p password --bucket furniture --create-scope chairs

To create a new collection called "couches" in the chairs scope in the furniture bucket.

$ couchbase-cli collection-manage -c 192.168.1.5 -u Administrator \
 -p password --bucket furniture --create-collection chairs.couches

To edit the collection called "couches" in the chairs scope in the furniture bucket.

$ couchbase-cli collection-manage -c 192.168.1.5 -u Administrator \
 -p password --bucket furniture --edit-collection chairs.couches
 --enable-history-retention 1

To list all of the collections in the chairs and tables scopes in the furniture bucket.

$ couchbase-cli collection-manage -c 192.168.1.5 -u Administrator \
 -p password --bucket furniture --list-collections chairs,tables

To drop the couches collection from the chairs scope in the furniture bucket.

$ couchbase-cli collection-manage -c 192.168.1.5 -u Administrator \
 -p password --bucket furniture --drop-collection chairs.couches

To drop the chair scope from the furniture bucket

$ couchbase-cli collection-manage -c 192.168.1.5 -u Administrator \
 -p password --bucket furniture --drop-scope chairs

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

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite