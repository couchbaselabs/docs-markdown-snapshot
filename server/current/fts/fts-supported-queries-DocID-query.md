---
title: DocID Query
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/fts/pages/fts-supported-queries-DocID-query.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:fts:fts-supported-queries-DocID-query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/fts/fts-supported-queries-DocID-query.html)

# DocID Query

A DocID query returns the indexed document or documents among the specified set. This is typically used in conjunction queries, to restrict the scope of other queries' output.

{
"query":{"ids":["airport_8850", "airport_8851"]}
}