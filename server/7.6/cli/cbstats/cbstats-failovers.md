---
title: failovers
description: Provides information about IDs, sequence, and number of entries.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbstats/cbstats-failovers.adoc
  xref: xref:7.6@server:cli:cbstats/cbstats-failovers.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbstats/cbstats-failovers.html)

# failovers

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> Provides information about IDs, sequence, and number of entries. 

## [](#syntax)Syntax

Request syntax:

cbstats [host]:11210 failovers

## [](#description)Description

This command provides information about entries such as IDs, sequence, and number.

## [](#options)Options

None

## [](#example)Example

**Request**

cbstats 10.5.2.54:11210 failovers

**Response**

 vb_0:0:id:           81829249447048
 vb_0:0:seq:          0
 vb_0:num_entries:    1
 vb_1000:0:id:        118586517042384
 vb_1000:0:seq:       0
 vb_1000:num_entries: 1
 vb_1001:0:id:        113450262512702
 vb_1001:0:seq:       0
 vb_1001:num_entries: 1
...
 vb_999:0:id:         138916609758424
 vb_999:0:seq:        0
 vb_999:num_entries:  1
 vb_99:0:id:          2666503649134
 vb_99:0:seq:         0
 vb_99:num_entries:   1
 vb_9:0:id:           71096982888618
 vb_9:0:seq:          0
 vb_9:num_entries:    1