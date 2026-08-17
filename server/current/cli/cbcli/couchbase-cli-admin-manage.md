---
title: admin-manage
description: Manages the built-in Couchbase Server administrator
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/couchbase-cli/edit/morpheus/docs/modules/cli/pages/cbcli/couchbase-cli-admin-manage.adoc
  xref: xref:server:cli:cbcli/couchbase-cli-admin-manage.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/cli/cbcli/couchbase-cli-admin-manage.html)

# admin-manage

Manages the built-in Couchbase Server administrator

## [](#synopsis)SYNOPSIS

_couchbase-cli admin-manage_ [--ip <ip>] [--port <port>] --lock | --unlock

## [](#description)DESCRIPTION

This command is used to manage the built-in Couchbase Server Administrator user. There is only one built-in Administrator account, which is managed separately from the internal and external Administrator users. External and internal Administrator accounts can be managed using the [user-manage](couchbase-cli-user-manage.md) command.

The `admin-manage` command must be run locally on a node that is part of the cluster (i.e. must connect to the host the command is run on). This is required, as `admin-manage` relies on a local authentication token, which is used to authenticate with the server and perform actions such as locking the user. As a result, the command does not require credentials to be passed.

## [](#options)OPTIONS

\--port

Specify the REST API port of the locally running Couchbase Server. If no port is specified the default port 8091 is used.

\--ip

Specify the IP address of the locally running Couchbase Server. If no ip is specified the default ip localhost is used.

\--lock

Locks the built-in administrator user.

\--unlock

Unlocks the built-in administrator user.

## [](#examples)EXAMPLES

To lock the built-in administrator, run the following command:

  $ couchbase-cli admin-manage --lock

To unlock the built-in administrator, run the following command:

  $ couchbase-cli admin-manage --unlock

## [](#see-also)SEE ALSO

[user-manage](couchbase-cli-user-manage.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite