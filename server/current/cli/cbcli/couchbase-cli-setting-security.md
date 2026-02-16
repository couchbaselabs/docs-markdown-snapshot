[View original HTML](/server/current/cli/cbcli/couchbase-cli-setting-security.html)

Manage security policies

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-security_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--set] [--get] [--disable-http-ui <0|1>]
    [--disable-www-authenticate <0|1>]
    [--cluster-encryption-level <all|control|strict>]
    [--tls-min-version <tlsv1.2|tlsv1.3>]
    [--tls-honor-cipher-order <0|1>] [---cipher-suites <ciphers>]
    [--hsts-max-age <seconds] [--hsts-preload-enabled <0|1>]
    [--hsts-include-sub-domains-enabled <0|1>]

## [](#description)DESCRIPTION

This command allows configuring cluster wide security settings.

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

Gets current security settings.

\--set

Set new security settings.

\--disable-http-ui <0|1>

Specifies whether the Couchbase Web Console can be accessible over http. To disable access set this option to "1". To enable access set this option to "0". By default, access to the UI over http is enabled. Notice that this will only disable http access to the endpoints that are used by the Web UI and not all endpoints that use the http port (e.g. setting this option to "1" will disable access to the `<http://<addr>:8091>`endpoint but will not disable access to the `<http://<addr>:8091/logs>` endpoint since it is used by the REST API and not Web UI). If your goal is to disable non-local http access completely, you should use the `--cluster-encryption-level`flag and set its value to "strict".

\--disable-www-authenticate <0|1>

Specifies whether Couchbase Server will respond with WWW-Authenticate to unauthenticated requests. By default this is enabled which may result in browsers prompting the user for username/password and then caching the information.

\--cluster-encryption-level <all|control|strict>

Specifies the cluster encryption level. The level is used when cluster encryption is turned on. If the level is "all" then both data and control messages between the nodes in the cluster will be sent over encrypted connections. If the level is "control" only control messages will be sent encrypted. If the level is "strict" it is the same as having the level "all" but all non-TLS ports on non-loopback interfaces will be closed. By default when cluster encryption is turned on, the level will be "control". Before setting the level to "strict" you will need to perform a number of important actions, see [Enforcing TLS](https://docs.couchbase.com/server/current/manage/manage-security/manage-tls.html#enforcing-tls).

\--tls-min-version <tlsv1.2|tlsv1.3>

Specify the minimum TLS protocol version to be used across all of the Couchbase services.

\--tls-honor-cipher-order <1|0>

Specifies whether the cipher-order must be followed across all of the services. When set to 1, this allows weaker ciphers to be included in the cipher list for backwards compatibility of older clients/browsers while still forcing the newer clients to use stronger ciphers.

\--cipher-suites <cipher>

Specify the cipher suite to be used across all of the couchbase services. The ciphers have to be a comma separated list. If an empty string is given ("") then the cipher list will be reset to its default.

\--hsts-max-age <seconds>

Specifies the max-ages directive in seconds the server uses in the Strict-Transport-Security header.

\--hsts-preload-enabled <1|0>

Specifies whether the preload directive for the Strict-Transport-Security header the server uses should be set.

\--hsts-include-sub-domains-enabled <1|0>

Specifies whether the includeSubDomains directive for the Strict-Transport-Security header the server uses should be set.

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

To disable the Couchbase Administration Console over HTTP run the following command.

$ couchbase-cli setting-security -c localhost -u Administrator \
 -p password --set --disable-http-ui 1

To change the encryption level to "all" run the following command.

$ couchbase-cli setting-security -c localhost -u Administrator \
 -p password --set --cluster-encryption-level all

To change max-ages directive for Strict-Transport-Security header to 10 seconds.

$ couchbase-cli setting-security -c localhost -u Administrator \
 -p password --set --hsts-max-age 10

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

[couchbase-cli](couchbase-cli.md) [node-to-node-encryption](couchbase-cli-node-to-node-encryption.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite