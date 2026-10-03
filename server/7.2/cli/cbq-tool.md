---
title: cbq
description: The cbq tool enables you to run SQL++ queries from the command line.
pubDate: 2026-10-03T04:27:21.374Z
meta:
  component:
    title: Couchbase Server
    version: "7.2"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cli/pages/cbq-tool.adoc
  xref: xref:7.2@server:cli:cbq-tool.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/cli/cbq-tool.html)

# cbq

> The `cbq` tool enables you to run SQL++ queries from the command line. 

## [](#example)Example

The basic syntax is:

cbq> create primary index on `beer-sample`;
cbq> select * from `beer-sample` limit 1;

For detailed information, see [cbq: The Command Line Shell for SQL++](../tools/cbq-shell.md).