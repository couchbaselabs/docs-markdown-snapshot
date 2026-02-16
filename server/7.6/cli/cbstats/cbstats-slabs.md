[View original HTML](/server/7.6/cli/cbstats/cbstats-slabs.html)

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