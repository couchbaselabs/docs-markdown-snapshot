---
title: Match Query Syntax
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-query-string-syntax-match.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-query-string-syntax-match.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-query-string-syntax-match.html)

# Match Query Syntax

A term without any other syntax is interpreted as a match query for the term in the default field.

The default field is `_all`.

For example, `pool` performs a [match query](fts-supported-queries-match.md) for the term `pool`.

## [](#example)Example

The following JSON object demonstrates specification of a match query:

```json
{
 "match": "location hostel",
 "field": "reviews.content",
 "analyzer": "standard",
 "fuzziness": 2,
 "prefix_length": 4,
 "operator": "and"
}
```