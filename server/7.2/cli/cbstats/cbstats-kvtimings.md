---
title: kvtimings
description: Provides low-level timings from the underlying KV storage system.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cli/pages/cbstats/cbstats-kvtimings.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:cli:cbstats/cbstats-kvtimings.adoc[]
---

[View original HTML](/server/7.2/cli/cbstats/cbstats-kvtimings.html)

# kvtimings

> Provides low-level timings from the underlying KV storage system. 

## [](#syntax)Syntax

Request syntax:

cbstats [hostname]:11210 kvtimings

## [](#description)Description

This command is useful to understand various states of the storage system.

__Table 1\. Couchstore database engine stats__
| Stat           | Description                            |
| -------------- | -------------------------------------- |
| backend\_type  | Type of backend database engine        |
| close          | Number of database close operations.   |
| failure\_get   | Number of failed get operations.       |
| failure\_open  | Number of failed open operations.      |
| failure\_set   | Number of failed set operations.       |
| failure\_vbset | Number of failed vbucket set operation |
| lastCommDocs   | Number of docs in the last commit.     |
| numLoadedVb    | Number of Vbuckets loaded into memory. |
| open           | Number of database open operations.    |

## [](#options)Options

None

## [](#example)Example

**Request**

cbstats 10.5.2.54:11210 kvtimings

## [](#sample-histogram)Sample histogram

 rw_3:commit (50457 total)
        1ms - 2ms     : (  0.34%)   173
        2ms - 4ms     : ( 10.52%)  5136 ##############
        4ms - 8ms     : ( 67.06%) 28528 ##############################################################################
        8ms - 16ms    : ( 97.09%) 15152 #########################################
        16ms - 32ms   : ( 99.93%)  1432 ###
        32ms - 65ms   : ( 99.98%)    27
        65ms - 131ms  : ( 99.99%)     6
        131ms - 262ms : (100.00%)     1
        262ms - 524ms : (100.00%)     2
        Avg           : (    5ms)