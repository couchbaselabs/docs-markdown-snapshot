---
title: DocID Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-supported-queries-DocID-query.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:fts:fts-supported-queries-DocID-query.adoc[]
---

[View original HTML](/server/7.6/fts/fts-supported-queries-DocID-query.html)

# DocID Query

A DocID query returns the indexed document or documents among the specified set. This is typically used in conjunction queries, to restrict the scope of other queries’ output.

{
"query":{"ids":["airport_8850", "airport_8851"]}
}