---
title: cbq
description: The cbq tool enables you to run SQL++ queries from the command line.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbq-tool.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:cli:cbq-tool.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbq-tool.html)

# cbq

> The `cbq` tool enables you to run SQL++ queries from the command line. 

## [](#example)Example

The basic syntax is:

cbq> create primary index on `beer-sample`;
cbq> select * from `beer-sample` limit 1;

For detailed information, see [cbq: The Command Line Shell for SQL++](../n1ql/n1ql-intro/cbq.md).