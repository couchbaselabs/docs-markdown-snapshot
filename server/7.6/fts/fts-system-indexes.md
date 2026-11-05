---
title: System:indexes - FTS indexes which are eligible to be queried from SQL++
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-system-indexes.adoc
  xref: xref:7.6@server:fts:fts-system-indexes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts/fts-system-indexes.html)

# System:indexes - FTS indexes which are eligible to be queried from SQL++

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

Use the following command to find all the FTS indexes in the system table that can be queried from SQL++.

SELECT * FROM system:indexes

An additional link describes various scenarios in which the FTS Index becomes ineligible to be queried by SQL++.

[Scenarios where FTS Index becomes ineligible to be queried by SQL++](#n1ql/pages/n1ql-language-reference/searchfun.adoc#limitations)

> [!NOTE]
> Querying system:indexes only returns indexes on non-system keyspaces. To return all indexes, including indexes on system keyspaces, use the query system:all\_indexes.