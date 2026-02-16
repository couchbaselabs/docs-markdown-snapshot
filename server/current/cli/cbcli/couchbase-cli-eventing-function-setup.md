[View original HTML](/server/current/cli/cbcli/couchbase-cli-eventing-function-setup.html)

Manage Events

## [](#synopsis)SYNOPSIS

_couchbase-cli eventing-function-setup_ [--cluster <url>] [--username <user>]
    [--password <password>] [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--import] [--export] [--export-all] [--delete] [--list] [--deploy]
    [--undeploy] [--boundary <from-everything|from-now>] [--pause] [--resume] [--name <name>] [--file <file>]

## [](#description)DESCRIPTION

This command is used to manage functions in the Event service

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

\--import

Import function(s) from a file. This option requires --file to be specified. The file provided should be from the --export option.

\--export

Export a named function to a file. This option requires --file and --name to be specified.

\--export-all

Export all functions to a file. This option requires --file to be specified.

\--delete

Deletes a named function. Functions can only be deleted when in the undeployed state. This option requires --name to be specified.

\--list

List all functions.

\--deploy

Deploys the named function. This option requires --name to be specified, as well as --bucket and --scope for collection-aware functions.

\--undeploy

Undeploys the named function. This option requires --name to be specified, as well as --bucket and --scope for collection-aware functions.

\--pause

Pause the named function. This option requires --name to be specified, as well as --bucket and --scope for collection-aware functions. See the PAUSE VS UNDEPLOY section for more information.

\--resume

Resume the named function. This option requires --name to be specified, as well as --bucket and --scope for collection-aware functions. See the PAUSE VS UNDEPLOY section for more information.

\--name <name>

The name of the function to take a action against. This is used by --deploy, --undeploy, --pause, --resume and --delete options.

\--bucket <bucket>

The bucket to which the function to take an action against belongs. This needs to be specified together with --scope or both should be omitted for collection-unaware functions. This is used by --deploy, --undeploy, --pause, --resume and --delete options.

\--scope <scope>

The scope to which the function to take an action against belongs. This needs to be specified together with --bucket or both should be omitted for collection-unaware functions. This is used by --deploy, --undeploy, --pause, --resume and --delete options.

\--boundary <from-everything|from-now>

(Deprecated) The place to start at when deploying a new function. Accepts 'from-now' or 'from-everything' defaulting to 'from-everything' if the --boundary flag is omitted.

\--file <file>

The file to import and export functions to. This is used by --export and --import options only.

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

To import functions from a file called _functions.json_:

$ couchbase-cli eventing-function-setup -c 192.168.1.5 -u Administrator \
 -p password --import --file functions.json

To export a function called _alert\_function_ to a file called _functions.json_:

$ couchbase-cli eventing-function-setup -c 192.168.1.5 -u Administrator \
 -p password --export --name alert_function --file functions.json

To export all functions to a file called _functions.json_:

$ couchbase-cli eventing-function-setup -c 192.168.1.5 -u Administrator \
 -p password --export-all --file functions.json

To list all functions:

$ couchbase-cli eventing-function-setup -c 192.168.1.5 -u Administrator \
 -p password --list

To delete a function called _alert\_function_:

$ couchbase-cli eventing-function-setup -c 192.168.1.5 -u Administrator \
 -p password --delete --name alert_function

To deploy a function called _alert\_function_ and process both all historical data and new data:

$ couchbase-cli eventing-function-setup -c 192.168.1.5 -u Administrator \
 -p password --deploy --name alert_function --boundary from-everything

To deploy a function called _alert\_function_ and process only new data:

$ couchbase-cli eventing-function-setup -c 192.168.1.5 -u Administrator \
 -p password --deploy --name alert_function --boundary from-now

To undeploy a function called _alert\_function_:

$ couchbase-cli eventing-function-setup -c 192.168.1.5 -u Administrator \
 -p password --undeploy --name alert_function

To pause a function called _alert\_function_:

$ couchbase-cli eventing-function-setup -c 192.168.1.5 -u Administrator \
 -p password --pause --name alert_function

To resume a function called _alert\_function_:

$ couchbase-cli eventing-function-setup -c 192.168.1.5 -u Administrator \
 -p password --resume --name alert_function

## [](#undeploy-vs-pause)UNDEPLOY VS PAUSE

Once you undeploy an eventing function you will have no opportunity to resume from the point at which the function was undeployed; this is not the case for pause/resume. Pausing an eventing function allows you to make changes to it or its settings while retaining the ability to continue from the point at which the function was paused.

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