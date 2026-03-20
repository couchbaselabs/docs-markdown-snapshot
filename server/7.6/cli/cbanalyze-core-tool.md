---
title: cbanalyze-core
description: The <code class="cmd">cbanalyze-core</code> tool is used to parse
  and analyze core dump data.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/cli/pages/cbanalyze-core-tool.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:cli:cbanalyze-core-tool.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/cli/cbanalyze-core-tool.html)

# cbanalyze-core

> The `cbanalyze-core` tool is used to parse and analyze core dump data. 

## [](#syntax)Syntax

The basic syntax is:

cbanalyze-core -r [root] -f [reportfile] [corefile]

## [](#description)Description

The command `cbanalyze-core` tool is a helper script to parse and analyze core dump from a Couchbase Server node.

> [!NOTE]
> The `cbanalyze-core` tool cannot analyze minidump core files and should only be used when directed by Couchbase Support.

Depending upon your platform, this tool is at the following locations:

| Operating system | Location                                                                          |
| ---------------- | --------------------------------------------------------------------------------- |
| Linux            | _/opt/couchbase/bin/tools/_                                                       |
| Windows          | (Not available on this platform)                                                  |
| Mac OS X         | _/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/tools/_ |

## [](#options)Options

The following are the command options:

| Options            | Description                        |
| ------------------ | ---------------------------------- |
| \-r \[root\]       | Search for the binary in root.     |
| \-f \[reportfile\] | Use the specified file for output. |