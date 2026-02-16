[View original HTML](/server/7.2/cli/cbcli/couchbase-cli-master-password.html)

Sends the Couchbase master password

## [](#synopsis)SYNOPSIS

_couchbase-cli master-password_ [--send-password <password>]

## [](#description)DESCRIPTION

Couchbase Server Enterprise Edition has a "Secret Management" feature, which allows users to securely encrypt passwords and other sensitive configuration information that is stored on disk. These secrets must be stored in a secure way, and access must be controlled to reduce the risk of accidental exposure. By using Secret Management in Couchbase Server, secrets are written to disk in encrypted format. To decrypt these secrets, Couchbase requires the entering of a "master password", which is supplied by the user during server startup. This master password can be passed to the server using this command.

By default the Secret Management feature is disabled. To enable the feature, you must first set the master password. Once a master password is set, the user is required to enter it when the server starts up. This can be done by setting the environment variable CB\_MASTER\_PASSWORD=<password> during server startup. Alternatively, you can enter the master password using the couchbase-cli `master-password` command. This command must be run locally on the node that needs to be unlocked and the user running the command must be a member of the `couchbase` group (or be root.)

## [](#options)OPTIONS

\--send-password

Sends the master password to the server that is waiting to start up.

## [](#examples)EXAMPLES

To use the Secret Management feature, the first thing you need to do is set a password on each node of the cluster. To do this, install, start and initialize Couchbase. Once Couchbase has started, run the following command to set the master password for your server.

$ couchbase-cli setting-master-password -c 127.0.0.1 -u Administrator \
  -p password --new-password password

Once the master password is configured restart the server. Upon restarting the cluster you will notice that the server doesn’t fully start. This is because it is waiting for you to enter the master password. You can do this by running the command below. The master-password subcommand has to be run locally on the node that is waiting for the master password and as the user must have be able to read files in the `couchbase` group.

$ couchbase-cli master-password --send-password password

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

[setting-master-password](couchbase-cli-setting-master-password.md), [cluster-init](couchbase-cli-cluster-init.md), [server-add](couchbase-cli-server-add.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite