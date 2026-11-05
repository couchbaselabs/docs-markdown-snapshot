---
title: diskinfo
description: Provides data and file size information.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbstats/cbstats-diskinfo.adoc
  xref: xref:7.6@server:cli:cbstats/cbstats-diskinfo.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbstats/cbstats-diskinfo.html)

# diskinfo

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> Provides data and file size information. 

## [](#syntax)Syntax

Request syntax:

cbstats [host]:11210 diskinfo

## [](#description)Description

This command provides information on data and file sizes.

## [](#options)Options

None

## [](#example)Example

**Request**

cbstats 10.5.2.54:11210 diskinfo

**Response**

ep_db_data_size: 121104
ep_db_file_size: 19036812