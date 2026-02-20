---
title: Boolean Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-boolean-field-query.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-supported-queries-boolean-field-query.adoc[]
---

[View original HTML](/server/7.2/fts/fts-supported-queries-boolean-field-query.html)

# Boolean Query

A _boolean query_ is a combination of conjunction and disjunction queries. A boolean query takes three lists of queries:

* `must`: Result documents must satisfy all of these queries.
* `should`: Result documents should satisfy these queries.
* `must not`: Result documents must not satisfy any of these queries.

```json
{
 "must": {
   "conjuncts":[{"field":"reviews.content", "match": "location"}]},
 "must_not": {
   "disjuncts": [{"field":"free_breakfast", "bool": false}]},
 "should": {
   "disjuncts": [{"field":"free_breakfast", "bool": true}]}
}
```