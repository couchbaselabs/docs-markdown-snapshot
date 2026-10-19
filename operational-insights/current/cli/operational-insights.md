---
title: operational-insights
description: The <code>operational-insights</code> command is used to start,
  stop, and retrieve status on a <em>non-root-installed</em> node, on any
  supported Linux platform.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/cli/pages/operational-insights.adoc
  xref: xref:enterprise-analytics:cli:operational-insights.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/cli/operational-insights.html)

# operational-insights

The `operational-insights` command is used to start, stop, and retrieve status on a _non-root-installed_ node, on any supported Linux platform.

## [](#syntax)Syntax

operational-insights [
          [ --start ]
          [ --status | -s ]
          [ --stop | -k ]
          [ --help | -h ]
          [ --version | -v ]
         ]

## [](#description)Description

The `operational-insights` command is used to control aspects of an Operational Insights node that has been installed, on a supported Linux platform, by means of the _non-root_ procedure. This command _cannot_ be used to control a node installed by the standard, package-based install procedure, which runs Operational Insights as the `operational-insights` service.

The `--start` flag causes the non-root node to start. This is the default option, and is invoked if no flag is specified.

The `--status` flag returns status on the non-root node, indicating whether it has been started, or has been stopped.

The `--stop` flag causes a running non-root node to stop.

The `--help` flag prints help text to the console.

The `--version` flag prints to the console the version number of the non-root node.

## [](#examples)Examples

The following examples show how the `operational-insights` command and its parameters can be used. The examples assumes that the current working directory is `<install-location>/opt/couchbase/bin`.

### [](#start-non-root-couchbase-server)Start

To start a non-root node, enter the following command:

./operational-insights --start

This starts a non-root node. No output is displayed.

### [](#get-status-on-non-root-couchbase-server)Get Status

To get status on whether a non-root Operational Insights is running, enter the following command.

./operational-insights --status

If a non-root Operational Insights is running, the following is displayed:

Operational Insights is running

If a non-root-installed node is _not_ running, the following is displayed:

Operational Insights is not running

### [](#stop-non-root-couchbase-server)Stop

To stop a non-root node, enter the following command:

./operational-insights --stop

This stops a running, non-root node. The output might appear as follows:

2020-06-30 09:33:03 cb_dist: terminating with reason: shutdown

If no non-root node was running, no output is displayed.

### [](#get-version-number)Get Version Number

To get the version number of the non-root node, enter the following:

./operational-insights --version

If successful, the command prints the version number and edition of the non-root node, as follows:

Operational Insights 3.0.0-nnnn (EE)

## [](#see-also)See Also

Links to standard, package-based install procedures are provided in [Install on Linux](../install/linux-installation.md).