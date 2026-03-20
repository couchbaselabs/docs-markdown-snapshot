---
title: tap-vbtakeover
description: Tracks the progress of rebalance using TAP.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/cli/pages/cbstats/cbstats-tap-vbtakeover.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:cli:cbstats/cbstats-tap-vbtakeover.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/cli/cbstats/cbstats-tap-vbtakeover.html)

# tap-vbtakeover

> Tracks the progress of rebalance using TAP. 

## [](#syntax)Syntax

Request syntax:

cbstats host:11210 [common options] tap-vbtakeover vb name

## [](#description)Description

For internal use only. This command is used by cluster manager (ns\_server) to track the progress of rebalance using TAP.

TAP is an internal protocol that streams information about data changes between cluster nodes. It was replaced by DCP and removed from Couchbase Server in version 5.0\. This command enables you to retrieve statistics from clusters running legacy versions of Couchbase Server.

## [](#options)Options

__Table 1\. tap-vbtakeover options__
| Option | Description  |
| ------ | ------------ |
| vb     | vBucket ID.  |
| name   | Stream name. |

For common `cbstats` options, see [cbstats](../cbstats-intro.md).