---
title: setting-ldap
description: Configure LDAP
editUrl: https://github.com/couchbase/couchbase-cli/edit/neo/docs/modules/cli/pages/cbcli/couchbase-cli-setting-ldap.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:cli:cbcli/couchbase-cli-setting-ldap.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/cli/cbcli/couchbase-cli-setting-ldap.html)

# setting-ldap

Configure LDAP

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-ldap_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--authentication-enabled <1|0>]
    [--authorization-enabled <1|0>] [--hosts <host_list>] [--port <port>]
    [--encryption <tls|startTLS|none>] [--server-cert-validation <1|0>]
    [--ldap-cacert <path>] [--request-timeout <ms>]
    [--user-dn-query <query> | --user-dn-template <template>]
    [--max-parallel <max>] [--max-cache-size <size>]
    [--cache-value-lifetime <ms>] [--bind-dn <dn>] [--bind-password <password>]
    [--ldap-client-cert <path>] [--ldap-client-key <path>]
    [--group-query <query>] [--enable-nested-groups <0|1>]
    [--nested-group-max-depth <depth>]

## [](#description)DESCRIPTION

This command allows administrators to configure and connect LDAP servers.

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

\--authentication-enabled <1|0>

Enables using LDAP to authenticate users

\--authorization-enabled <1|0>

Enables using LDAP to give users authorization

\--hosts <host\_list>

Specifies a comma separated list of LDAP hosts.

\--port <port>

LDAP port.

\--encryption <tls|startTLS|none>

Security used to communicate with LDAP servers. Supported options \[tls, startTLS, none\].

\--server-cert-validation <1|0>

Enable or disable certificate validation when connecting to LDAP server.

\--ldap-cacert <path>

CA certificate to be used for server’s certificate validation, required if certificate validation is not disabled

\--request-timeout <ms>

The timeout for LDAP requests in milliseconds.

\--user-dn-query <query>

LDAP query to get user’s DN. Must contains at least one instance of %u Example: ou=Users,dc=example??one?(uid=%u)

\--user-dn-template <template>

Template to construct user’s DN. Must contain at least one instance of %u Example: uid=%u,ou=Users,dc=example

\--max-parallel <max>

Maximum number of parallel connections that can be established with LDAP servers.

\--max-cache-size <size>

Maximum number of requests that can be cached, defaults to 10000.

\--cache-value-lifetime <ms>

Lifetime of values in cache in milliseconds. Default 300000 ms.

\--bind-dn <dn>

The DN of a user to authenticate as to allow user search and groups synchronization. If bind details or client TLS certificate are not provided anonymous bind will be used instead.

\--bind-password <password>

The bind user password

\--ldap-client-cert <path>

The client TLS certificate to be used to bind against the LDAP Server to allow user and groups synchronization. If bind details or client TLS certificate are not provided anonymous bind will be used instead. '--ldap-client-cert' and '--ldap-client-key' need to be set together.

\--ldap-client-key <path>

The client TLS key. This is used with '--ldap-client-cert' flag for certificate authentication. '--ldap-client-cert' and '--ldap-client-key' need to be set together.

\--group-query <query>

LDAP query, to get the users' groups by username in RFC4516 format. The %u and %D placeholders can be used, for username and user’s DN respectively. If attribute is present in the query, the list of attribute values in the search result is considered as list of user’s groups (single entry result is expected): for example: '%D?memberOf?base'. If the attribute is not present in the query, every returned entry is considered a group, for example: 'ou=groups,dc=example,dc=com??one?(member=%D)'

\--enable-nested-groups <0|1>

If enabled Couchbase server will try to recursively search for groups for every discovered ldap group.

\--nested-groups-max-depth <depth>

Maximum number of recursive groups requests the server is allowed to perform. This option is only valid when nested groups are enabled. The depth is an integer between 1 and 100, default is 10.

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

To enable authentication and authorization using ldap server ldap.couchbase.com with encryption disabled:

$ couchbase-cli setting-ldap -c 192.168.1.5 -u Administrator \
 -p password --authentication-enabled 1 --authorization-enabled 1 \
 --hosts ldap.couchbase.com --encryption none

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

[user-manage](couchbase-cli-user-manage.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite