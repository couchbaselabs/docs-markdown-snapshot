---
title: Prefix Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-prefix-query.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-supported-queries-prefix-query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-supported-queries-prefix-query.html)

# Prefix Query

A _prefix_ query finds documents containing terms that start with the specified prefix. Please note that the prefix query is a non-analytic query, meaning it won’t perform any text analysis on the query text.

```json
{
 "prefix": "inter",
 "field": "reviews.content"
}
```