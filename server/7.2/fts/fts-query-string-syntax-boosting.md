---
title: Boosting
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-query-string-syntax-boosting.adoc
  xref: xref:7.2@server:fts:fts-query-string-syntax-boosting.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-query-string-syntax-boosting.html)

# Boosting

When you specify multiple query-clauses, you can specify the relative importance to a given clause by suffixing it with the `^` operator, followed by a number or by specifying the `boost` parameter with the number to boost the search.

## [](#example)Example

```json
description:pool name:pool^5
```

The above syntax performs Match Queries for **pool** in both the `name` and `description` fields, but documents having the term in the `name` field score higher.

```json
"query": {
  ​​​​​  "disjuncts": [
         {
      ​​​​​"match": "glossop",
      "field": "city",
      "boost": 10
    }​​​​​,
         {
      ​​​​​"match": "glossop",
      "field": "title"
    }​​​​​
  ]
}​​​​​
```

The above syntax performs Match Queries for a city **glossop** in both the `city` and `title` fields, but documents having the term in the `city` field score higher.