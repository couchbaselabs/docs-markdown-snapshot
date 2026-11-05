---
title: dcp-vbtakeover
description: Tracks the progress of rebalance using Database Change Protocol (DCP).
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbstats/cbstats-dcp-vbtakeover.adoc
  xref: xref:7.6@server:cli:cbstats/cbstats-dcp-vbtakeover.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbstats/cbstats-dcp-vbtakeover.html)

# dcp-vbtakeover

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> Tracks the progress of rebalance using Database Change Protocol (DCP). 

## [](#syntax)Syntax

Request syntax:

cbstats host:11210 [common options] dcp-vbtakeover vb name

## [](#description)Description

For internal use only. This command is used by cluster manager (ns\_server) to track the progress of rebalance using DCP.

## [](#options)Options

__Table 1\. dcp-vbtakeover options__
| Option | Description  |
| ------ | ------------ |
| vb     | vBucket ID.  |
| name   | Stream name. |

For common `cbstats` options, see [cbstats](../cbstats-intro.md).