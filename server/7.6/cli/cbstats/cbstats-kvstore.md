---
title: kvstore
description: Provides low-level stats from the underlying KV storage system.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbstats/cbstats-kvstore.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:cli:cbstats/cbstats-kvstore.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbstats/cbstats-kvstore.html)

# kvstore

> Provides low-level stats from the underlying KV storage system. 

## [](#syntax)Syntax

Request syntax:

cbstats [hostname]:11210 kvstore

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

cbstats 10.5.2.54:11210 kvstore

**Response**

 ro_0:backend_type:  couchstore
 ro_0:close:         0
 ro_0:failure_get:   0
 ro_0:failure_open:  0
 ro_0:numLoadedVb:   0
 ro_0:open:          0
 ro_1:backend_type:  couchstore
 ro_1:close:         0
 ro_1:failure_get:   0
 ro_1:failure_open:  0
 ro_1:numLoadedVb:   0
 ro_1:open:          0
 ro_2:backend_type:  couchstore
 ro_2:close:         0
 ro_2:failure_get:   0
 ro_2:failure_open:  0
 ro_2:numLoadedVb:   0
 ro_2:open:          0
 ro_3:backend_type:  couchstore
 ro_3:close:         0
 ro_3:failure_get:   0
 ro_3:failure_open:  0
 ro_3:numLoadedVb:   0
 ro_3:open:          0
 rw_0:backend_type:  couchstore
 rw_0:close:         0
 rw_0:failure_del:   0
 rw_0:failure_get:   0
 rw_0:failure_open:  0
 rw_0:failure_set:   0
 rw_0:failure_vbset: 0
 rw_0:lastCommDocs:  0
 rw_0:numLoadedVb:   0
 rw_0:open:          0
 rw_1:backend_type:  couchstore
 rw_1:close:         0
 rw_1:failure_del:   0
 rw_1:failure_get:   0
 rw_1:failure_open:  0
 rw_1:failure_set:   0
 rw_1:failure_vbset: 0
 rw_1:lastCommDocs:  0
 rw_1:numLoadedVb:   0
 rw_1:open:          0
 rw_2:backend_type:  couchstore
 rw_2:close:         0
 rw_2:failure_del:   0
 rw_2:failure_get:   0
 rw_2:failure_open:  0
 rw_2:failure_set:   0
 rw_2:failure_vbset: 0
 rw_2:lastCommDocs:  0
 rw_2:numLoadedVb:   0
 rw_2:open:          0
 rw_3:backend_type:  couchstore
 rw_3:close:         0
 rw_3:failure_del:   0
 rw_3:failure_get:   0
 rw_3:failure_open:  0
 rw_3:failure_set:   0
 rw_3:failure_vbset: 0
 rw_3:lastCommDocs:  0
 rw_3:numLoadedVb:   0
 rw_3:open:          0