---
title: DocID Query
pubDate: 2026-10-03T04:27:21.374Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-supported-queries-DocID-query.adoc
  xref: xref:7.6@server:fts:fts-supported-queries-DocID-query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/fts/fts-supported-queries-DocID-query.html)

# DocID Query

A DocID query returns the indexed document or documents among the specified set. This is typically used in conjunction queries, to restrict the scope of other queries' output.

{
"query":{"ids":["airport_8850", "airport_8851"]}
}