---
title: Prefix Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-prefix-query.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/fts/fts-supported-queries-prefix-query.html)

# Prefix Query

A _prefix_ query finds documents containing terms that start with the specified prefix. Please note that the prefix query is a non-analytic query, meaning it won’t perform any text analysis on the query text.

```json
{
 "prefix": "inter",
 "field": "reviews.content"
}
```