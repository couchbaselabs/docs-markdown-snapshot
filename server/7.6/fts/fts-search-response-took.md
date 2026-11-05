---
title: Took
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-search-response-took.adoc
  xref: xref:7.6@server:fts:fts-search-response-took.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts/fts-search-response-took.html)

# Took

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

The time taken (in nanoseconds) to complete the execution of a query.

## [](#example)Example

```json
"total_hits": 56,
"max_score": 0.8041158525040355,
"took": 1449005,
```