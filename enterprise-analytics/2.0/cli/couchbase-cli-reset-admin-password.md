---
title: reset-admin-password
description: Resets the Enterprise Analytics administrator password
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/cli/pages/couchbase-cli-reset-admin-password.adoc
  xref: xref:2.0@enterprise-analytics:cli:couchbase-cli-reset-admin-password.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/cli/couchbase-cli-reset-admin-password.html)

# reset-admin-password

Resets the Enterprise Analytics administrator password

## [](#synopsis)SYNOPSIS

_couchbase-cli reset-admin-password_ [--regenerate] [--new-password <password>]
    [--port <port>] [--config-path <path>]

## [](#description)DESCRIPTION

This command is used to reset the built-in Enterprise Analytics Administrator password. There is only one built-in Administrator account, which is managed separately from the internal and external Administrator users. External and internal Administrator accounts can be managed using the [user-manage](couchbase-cli-user-manage.md) command.

The `reset-admin-password` command must be run locally on a node that is part of the cluster (i.e. must connect to the host the command is run on). This is required, as `reset-admin-password` relies on a local authentication token, which is used to authenticate with the server and change the password. As a result, the command does not require credentials to be passed.

## [](#options)OPTIONS

\--new-password <password>

Sets the password for the Enterprise Analytics administrator user to the value specified by the argument. If no password is specified, the command prompts the user for the new password through non-echoed stdin.

\--regenerate

Sets the password for the Enterprise Analytics administrator user to a randomly generated value. The new password is printed to the command line after the password is changed.

\--port

Specify the REST API port of the locally running Enterprise Analytics. If no port is specified the default port 8091 is used.

\--config-path

Manually specify the path to the Enterprise Analytics configuration file. This is only needed if the configuration file is not in the default location, otherwise it can be found at `var/lib/couchbase` within the Couchbase Server installation directory.

## [](#examples)EXAMPLES

To change the administrator password to `new_pwd`, run the following command:

  $ couchbase-cli reset-admin-password --new-password new_pwd

To change the administrator password to a randomly generated value, run the following command. The new password will be printed to stdout if the password is successfully changed:

$ couchbase-cli reset-admin-password --regenerate jXjNW6LG

## [](#see-also)SEE ALSO

[admin-manage](#couchbase-cli-admin-manage.adoc), [setting-ldap](couchbase-cli-setting-ldap.md), [user-manage](couchbase-cli-user-manage.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite