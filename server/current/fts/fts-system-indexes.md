---
title: System:indexes - FTS indexes which are eligible to be queried from SQL++
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/fts/pages/fts-system-indexes.adoc
  xref: xref:server:fts:fts-system-indexes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/fts/fts-system-indexes.html)

# System:indexes - FTS indexes which are eligible to be queried from SQL++

Use the following command to find all the FTS indexes in the system table that can be queried from SQL++.

SELECT * FROM system:indexes

An additional link describes various scenarios in which the FTS Index becomes ineligible to be queried by SQL++.

[Scenarios where FTS Index becomes ineligible to be queried by SQL++](#n1ql/pages/n1ql-language-reference/searchfun.adoc#limitations)

> [!NOTE]
> Querying system:indexes only returns indexes on non-system keyspaces. To return all indexes, including indexes on system keyspaces, use the query system:all\_indexes.