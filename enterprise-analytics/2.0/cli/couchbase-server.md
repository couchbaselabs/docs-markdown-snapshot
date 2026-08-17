---
title: couchbase-server
description: The <code>couchbase-server</code> command is used to start, stop,
  and retrieve status on a <em>non-root-installed</em> server, on any supported
  Linux platform.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/cli/pages/couchbase-server.adoc
  xref: xref:2.0@enterprise-analytics:cli:couchbase-server.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/cli/couchbase-server.html)

# couchbase-server

The `couchbase-server` command is used to start, stop, and retrieve status on a _non-root-installed_ server, on any supported Linux platform.

## [](#syntax)Syntax

couchbase-server [
          [ --start ]
          [ --status | -s ]
          [ --stop | -k ]
          [ --help | -h ]
          [ --version | -v ]
         ]

## [](#description)Description

The `couchbase-server` command is used to control aspects of a Couchbase Server that has been installed, on a supported Linux platform, by means of the _non-root_ procedure. This command _cannot_ be used to control a Couchbase Server installed by the standard, package-based install procedure.

The `--start` flag causes the non-root Couchbase Server to start. This is the default option, and is invoked if no flag is specified.

The `--status` flag returns status on the non-root Couchbase Server, indicating whether it has been started, or has been stopped.

The `--stop` flag causes a running non-root Couchbase Server to stop.

The `--help` flag prints help text to the console.

The `--version` flag prints to the console the version number of the non-root Couchbase Server.

## [](#examples)Examples

The following examples show how the `couchbase-server` command and its parameters can be used. The examples assumes that the current working directory is `<install-location/opt/enterprise-analytics/bin`.

### [](#start-non-root-couchbase-server)Start

To start a non-root Couchbase Server, enter the following command:

./couchbase-server --start

This starts a non-root Couchbase Server. No output is displayed.

### [](#get-status-on-non-root-couchbase-server)Get Status

To get status on whether a non-root Couchbase Server is running, enter the following command.

./couchbase-server --status

If a non-root Couchbase Server is running, the following is displayed:

Couchbase Server is running

If a non-root-installed Couchbase Server is _not_ running, the following is displayed:

Couchbase Server is not running

### [](#stop-non-root-couchbase-server)Stop

To stop a non-root Couchbase Server, enter the following command:

./couchbase-server --stop

This stops a running, non-root Couchbase Server. The output might appear as follows:

2020-06-30 09:33:03 cb_dist: terminating with reason: shutdown

If no non-root Couchbase Server was running, no output is displayed.

### [](#get-version-number)Get Version Number

To get the version number of the non-root Couchbase Server, enter the following:

./couchbase-server --version

If successful, the command prints the version number and edition of the non-root Couchbase Server, as follows:

Couchbase Server 6.6.0-7853 (EE)

## [](#see-also)See Also

Links to standard, package-based install procedures are provided in [Install Enterprise Analytics on Linux](../install/linux-installation.md).