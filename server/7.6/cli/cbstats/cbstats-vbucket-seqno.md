---
title: vbucket-seqno
description: Provides seqno statistics for vBuckets.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbstats/cbstats-vbucket-seqno.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/cli/cbstats/cbstats-vbucket-seqno.html)

# vbucket-seqno

> Provides seqno statistics for vBuckets. 

## [](#syntax)Syntax

Request syntax:

cbstats host:11210 [common options] vbucket-seqno [vbid]

## [](#description)Description

This command provides details connected to the sequence number (seqno) for the specified vBucket, or for each vBucket if none is specified.

The identifier for each vBucket statistic begins with the string `vb_` followed by the vBucket ID and a colon. For example, for vBucket 1023, the identifier for the `uuid` statistic is `vb_1023:uuid`.

__Table 1\. vBucket seqno statistics__
| Name                         | Description                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------- |
| abs\_high\_seqno             | The last seqno assigned by this vBucket.                                                                |
| high\_seqno                  | The last seqno assigned by this vBucket, or in case of replica, the last closed checkpoint’s end seqno. |
| last\_persisted\_seqno       | The last persisted seqno for the vBucket.                                                               |
| purge\_seqno                 | The last seqno purged by the compactor.                                                                 |
| uuid                         | The current vBucket uuid.                                                                               |
| last\_persisted\_snap\_start | The last persisted snapshot start seqno for the vBucket.                                                |
| last\_persisted\_snap\_end   | The last persisted snapshot end seqno for the vBucket.                                                  |

## [](#options)Options

__Table 2\. vbucket-seqno options__
| Option | Description                                                                                                                                        |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| vbid   | vBucket ID. In a standard system this will be between 0 and 1023\. If not provided as part of the command then details for all vBuckets are shown. |

For common `cbstats` options, see [cbstats](../cbstats-intro.md).

## [](#example)Example

**Request**

cbstats localhost:11210 -u Administrator -p password -b beer-sample vbucket-seqno 1023

**Response**

 vb_1023:abs_high_seqno:            10
 vb_1023:high_seqno:                10
 vb_1023:last_persisted_seqno:      10
 vb_1023:last_persisted_snap_end:   10
 vb_1023:last_persisted_snap_start: 10
 vb_1023:purge_seqno:               0
 vb_1023:uuid:                      66069026212209