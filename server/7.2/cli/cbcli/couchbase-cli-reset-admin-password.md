[View original HTML](/server/7.2/cli/cbcli/couchbase-cli-reset-admin-password.html)

Resets the Couchbase Server administrator password

## [](#synopsis)SYNOPSIS

_couchbase-cli reset-admin-password_ [--regenerate] [--new-password <password>]
    [--port <port>]

## [](#description)DESCRIPTION

This command is used to reset the built-in Couchbase Server Administrator password. There is only one built-in Administrator account, which is managed separately from the internal and external Administrator users. External and internal Administrator accounts can be managed using the [user-manage](couchbase-cli-user-manage.md) command.

The `reset-admin-password` command must be run locally on a node that is part of the cluster (i.e. must connect to the host the command is run on). This is required, as `reset-admin-password` relies on a local authentication token, which is used to authenticate with the server and change the password. As a result, the command does not require credentials to be passed.

## [](#options)OPTIONS

\--new-password <password>

Sets the password for the Couchbase Server administrator user to the value specified by the argument. If no password is specified, the command prompts the user for the new password through non-echoed stdin.

\--regenerate

Sets the password for the Couchbase Server administrator user to a randomly generated value. The new password is printed to the command line after the password is changed.

\--port

Specify the REST API port of the locally running Couchbase Server. If no port is specified the default port 8091 is used.

## [](#examples)EXAMPLES

To change the administrator password to `new_pwd`, run the following command:

  $ couchbase-cli reset-admin-password --new-password new_pwd

To change the administrator password to a randomly generated value, run the following command. The new password will be printed to stdout if the password is successfully changed:

$ couchbase-cli reset-admin-password --regenerate jXjNW6LG

## [](#see-also)SEE ALSO

[setting-ldap](couchbase-cli-setting-ldap.md), [user-manage](couchbase-cli-user-manage.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite