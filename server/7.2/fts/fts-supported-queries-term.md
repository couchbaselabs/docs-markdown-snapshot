---
title: Term Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-term.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-supported-queries-term.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-supported-queries-term.html)

# Term Query

A term query is the simplest possible query. It performs an exact match in the index for the provided term.

## [](#example)Example

```json
{
  "term": "locate",
  "field": "reviews.content"
}
```

A demonstration of term queries using the Java SDK can be found in [Searching from the SDK](#3.2@java-sdk::full-text-searching-with-sdk.adoc).