---
title: Term Range Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-term-range.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-supported-queries-term-range.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-supported-queries-term-range.html)

# Term Range Query

A _term range_ query finds documents containing a term in the specified field within the specified range. Define the endpoints using the fields `min` and `max`. You can omit one endpoint, but not both. The `inclusive_min` and `inclusive_max` properties control whether or not the endpoints are included or excluded. By default, `min` is inclusive and `max` is exclusive.

```json
{
 "min": "foo", "max": "foof",
 "inclusive_min": false,
 "inclusive_max": false,
 "field": "desc"
}
```