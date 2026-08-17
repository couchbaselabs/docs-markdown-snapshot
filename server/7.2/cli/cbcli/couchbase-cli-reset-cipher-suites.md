---
title: reset-cipher-suites
description: Resets the Couchbase Server cipher suites to the default
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/couchbase-cli/edit/neo/docs/modules/cli/pages/cbcli/couchbase-cli-reset-cipher-suites.adoc
  xref: xref:7.2@server:cli:cbcli/couchbase-cli-reset-cipher-suites.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/cli/cbcli/couchbase-cli-reset-cipher-suites.html)

# reset-cipher-suites

Resets the Couchbase Server cipher suites to the default

## [](#synopsis)SYNOPSIS

_couchbase-cli reset-cipher-suites_ [--force] [--port <port>]

## [](#description)DESCRIPTION

This command is used to reset the cipher suites to the default for Couchbase Server. This command should only be used when the cipher have been configured in a way that breaks remote access. The cipher suit can be managed using the [setting-security](couchbase-cli-setting-security.md) command.

The `reset-cipher-suites` command must be run locally on a node that is part of the cluster (i.e. must connect to the node the command is run on). This is required, as the cluster and ciphers suits could be configured in a way that disables remote access. `reset-cipher-suites` uses the local authentication token as a result the user that execute the command needs to have read access to the local Couchbase Server configuration files.

## [](#options)OPTIONS

\--force

It reset the cipher suites without asking for confirmation.

\--port

Specify the REST API port of the locally running Couchbase Server. If no port is specified the default port 8091 is used.

## [](#examples)EXAMPLES

To reset the cipher suites to the default:

$ couchbase-cli reset-cipher-suites

## [](#see-also)SEE ALSO

[setting-security](couchbase-cli-setting-security.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite