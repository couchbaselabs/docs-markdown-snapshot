---
title: dcp-vbtakeover
description: Tracks the progress of rebalance using Database Change Protocol (DCP).
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbstats/cbstats-dcp-vbtakeover.adoc
  xref: xref:7.6@server:cli:cbstats/cbstats-dcp-vbtakeover.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbstats/cbstats-dcp-vbtakeover.html)

# dcp-vbtakeover

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