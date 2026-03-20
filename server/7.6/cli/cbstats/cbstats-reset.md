---
title: reset
description: For dev and test use only. Resets the following reset and reset
  histogram statistics.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbstats/cbstats-reset.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:cli:cbstats/cbstats-reset.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbstats/cbstats-reset.html)

# reset

> For dev and test use only. Resets the following reset and reset histogram statistics. 

## [](#syntax)Syntax

Request syntax:

cbstats [host]:11210 reset [options]

## [](#description)Description

For dev and test use only. This command resets the following `reset` and `reset histogram` statistics.

Note: Using the reset command in production can cause production problems, as well as the inability to diagnose issues due to lack of stats. The reset command is not a single atomic operation; therefore, threads may keep updating some stats while the reset operation is causing others to be cleared. This can cause overflows for calculated values and other stats used by the cluster.

__Table 1\. Reset stats__
| Reset Stats                      |
| -------------------------------- |
| ep\_bg\_load                     |
| ep\_bg\_wait                     |
| ep\_bg\_max\_load                |
| ep\_bg\_min\_load                |
| ep\_bg\_max\_wait                |
| ep\_bg\_min\_wait                |
| ep\_commit\_time                 |
| ep\_flush\_duration              |
| ep\_flush\_duration\_highwat     |
| ep\_io\_num\_read                |
| ep\_io\_num\_write               |
| ep\_io\_read\_bytes              |
| ep\_io\_write\_bytes             |
| ep\_items\_rm\_from\_checkpoints |
| ep\_num\_eject\_failures         |
| ep\_num\_pager\_runs             |
| ep\_num\_not\_my\_vbuckets       |
| ep\_num\_value\_ejects           |
| ep\_pending\_ops\_max            |
| ep\_pending\_ops\_max\_duration  |
| ep\_pending\_ops\_total          |
| ep\_storage\_age                 |
| ep\_storage\_age\_highwat        |
| ep\_too\_old                     |
| ep\_too\_young                   |
| ep\_tap\_bg\_load\_avg           |
| ep\_tap\_bg\_max\_load           |
| ep\_tap\_bg\_max\_wait           |
| ep\_tap\_bg\_min\_load           |
| ep\_tap\_bg\_min\_wait           |
| ep\_tap\_bg\_wait\_avg           |
| ep\_tap\_throttled               |
| ep\_tap\_total\_fetched          |
| ep\_vbucket\_del\_max\_walltime  |
| pending\_ops                     |

__Table 2\. Reset histogram stats__
| Reset Histograms stats |
| ---------------------- |
| bg\_load               |
| bg\_wait               |
| bg\_tap\_load          |
| bg\_tap\_wait          |
| chk\_persistence\_cmd  |
| data\_age              |
| del\_vb\_cmd           |
| disk\_insert           |
| disk\_update           |
| disk\_del              |
| disk\_vb\_del          |
| disk\_commit           |
| get\_stats\_cmd        |
| item\_alloc\_sizes     |
| get\_vb\_cmd           |
| notify\_io             |
| pending\_ops           |
| set\_vb\_cmd           |
| storage\_age           |
| tap\_mutation          |
| tap\_vb\_reset         |
| tap\_vb\_set           |

## [](#options)Options

`cbstats` requires a username (`-u`) and a password (`-p`) to execute.

For common `cbstats` options, see [cbstats](../cbstats-intro.md).

## [](#example)Example

**Request**

cbstats 10.5.2.54:11210 reset -u Administrator -p password