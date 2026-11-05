---
title: vbucket
description: Provides detailed statistics on a per vbucket granularity.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbstats/cbstats-vbucket.adoc
  xref: xref:7.6@server:cli:cbstats/cbstats-vbucket.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbstats/cbstats-vbucket.html)

# vbucket

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> Provides detailed statistics on a per vbucket granularity. 

## [](#syntax)Syntax

Request syntax:

cbstats host:11210 [common options] vbucket

## [](#description)Description

This command lists all available vBuckets and provides information about their type: active, replica, pending or dead.

## [](#options)Options

There are no options for this command. For common `cbstats` options, see [cbstats](../cbstats-intro.md).

## [](#example)Example

**Request**

cbstats -u Administrator -p password -b beer-sample localhost:11210 vbucket

**Response**

 vb_0:    replica
 vb_1:    replica
 vb_10:   replica
 vb_100:  active
 vb_1000: replica
 vb_1001: replica
 vb_1002: replica
 vb_1003: replica
 vb_1004: replica
 vb_1005: replica
 ...