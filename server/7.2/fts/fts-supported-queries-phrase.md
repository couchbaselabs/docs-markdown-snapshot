---
title: Phrase Query
pubDate: 2026-10-03T04:27:21.374Z
meta:
  component:
    title: Couchbase Server
    version: "7.2"
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-phrase.adoc
  xref: xref:7.2@server:fts:fts-supported-queries-phrase.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-supported-queries-phrase.html)

# Phrase Query

A _phrase query_ searches for terms occurring at the specified position and offsets. It performs an exact term-match for all the phrase-constituents without using an analyzer.

```json
{
  "terms": ["nice", "view"],
  "field": "reviews.content"
}
```

A demonstration of the phrase query using the Java SDK can be found in [Searching from the SDK](#3.2@java-sdk::full-text-searching-with-sdk.adoc).