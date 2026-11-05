---
title: CBFT_ENV_OPTIONS
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-advanced-settings-CBFT-ENV-OPTIONS.adoc
  xref: xref:7.6@server:fts:fts-advanced-settings-CBFT-ENV-OPTIONS.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts/fts-advanced-settings-CBFT-ENV-OPTIONS.html)

# CBFT_ENV_OPTIONS

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

It Specifies the cluster level FTS configuration options. This environment variable allows you to specify the default value for the configuration option on the command line.

## [](#example)Example

export CBFT_ENV_OPTIONS=bleveMaxResultWindow=10000000’