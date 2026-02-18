---
title: items
description: Gives statistics about items stored in the bucket.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cli/pages/cbstats/cbstats-items.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/cli/cbstats/cbstats-items.html)

# items

> Gives statistics about items stored in the bucket. 

## [](#syntax)Syntax

Request syntax:

cbstats host:11210 [common options] items

## [](#description)Description

For `memcached` buckets only. This command gives statistics about items stored in the specified bucket, or the default bucket if none is specified.

## [](#options)Options

There are no options for this command. For common `cbstats` options, see [cbstats](../cbstats-intro.md).

## [](#example)Example

**Request**

cbstats localhost:11210 -u Administrator -p password -b orders items

**Response**

 items:2:age:             21766
 items:2:evicted:         0
 items:2:evicted_nonzero: 0
 items:2:evicted_time:    0
 items:2:number:          5
 items:2:outofmemory:     0
 items:2:reclaimed:       0
 items:2:tailrepairs:     0