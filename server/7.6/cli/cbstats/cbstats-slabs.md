---
title: slabs
description: Gives statistics on current memory allocation.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbstats/cbstats-slabs.adoc
  xref: xref:7.6@server:cli:cbstats/cbstats-slabs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbstats/cbstats-slabs.html)

# slabs

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> Gives statistics on current memory allocation. 

## [](#syntax)Syntax

Request syntax:

cbstats host:11210 [common options] slabs

## [](#description)Description

For `memcached` buckets only. This command gives statistics on current memory allocation (slab allocator).

## [](#options)Options

There are no options for this command. For common `cbstats` options, see [cbstats](../cbstats-intro.md).

## [](#example)Example

**Request**

cbstats localhost:11210 -u Administrator -p password -b orders slabs

**Response**

 2:chunk_size:      144
 2:chunks_per_page: 7281
 2:free_chunks:     0
 2:free_chunks_end: 7276
 2:mem_requested:   661
 2:total_chunks:    7281
 2:total_pages:     1
 2:used_chunks:     5
 active_slabs:      1
 total_malloced:    1048464