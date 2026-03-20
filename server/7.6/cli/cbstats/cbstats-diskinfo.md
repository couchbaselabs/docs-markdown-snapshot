---
title: diskinfo
description: Provides data and file size information.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbstats/cbstats-diskinfo.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:cli:cbstats/cbstats-diskinfo.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbstats/cbstats-diskinfo.html)

# diskinfo

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