---
title: Match All Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-match-all.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-supported-queries-match-all.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-supported-queries-match-all.html)

# Match All Query

Matches _all_ documents in an index, irrespective of terms. For example, if an index is created on the `travel-sample` bucket for documents of type `zucchini`, the _match all_ query returns all document IDs from the `travel-sample` bucket, even though the bucket contains no documents of type `zucchini`.

```json
{ "match_all": {} }
```