---
title: cbq
description: The cbq tool enables you to run SQL++ queries from the command line.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbq-tool.adoc
  xref: xref:7.6@server:cli:cbq-tool.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbq-tool.html)

# cbq

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> The `cbq` tool enables you to run SQL++ queries from the command line. 

## [](#example)Example

The basic syntax is:

cbq> create primary index on `beer-sample`;
cbq> select * from `beer-sample` limit 1;

For detailed information, see [cbq: The Command Line Shell for SQL++](../n1ql/n1ql-intro/cbq.md).