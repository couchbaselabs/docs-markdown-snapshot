---
title: uuid
description: Provides the UUID for a bucket.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbstats/cbstats-uuid.adoc
  xref: xref:7.6@server:cli:cbstats/cbstats-uuid.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbstats/cbstats-uuid.html)

# uuid

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> Provides the UUID for a bucket. 

## [](#syntax)Syntax

Request syntax:

cbstats [host]:11210 uuid [options]

## [](#description)Description

Provides the UUID for a bucket.

## [](#options)Options

| Option            | Description                                                                                                                                                                                         |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \-b <bucket-name> | This flag and value are required: if they are omitted, an error is returned. The bucket-name must be the name of a bucket currently defined on the cluster of which the specified host is a member. |

## [](#example)Example

**Request**

/opt/couchbase/bin/cbstats localhost:11210 uuid -b travel-sample

**Response**

 uuid: 027ea0ff4684d631c491ecfbb812ac6a