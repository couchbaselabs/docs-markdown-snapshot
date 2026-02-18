---
title: Boosting
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/fts/pages/fts-supported-queries-boosting-the-score-query.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/fts/fts-supported-queries-boosting-the-score-query.html)

# Boosting

When you specify multiple query-clauses, you can specify the relative importance to a given clause by suffixing it with the `^` operator, followed by a number or by specifying the `boost` parameter with the number to boost the search.

## [](#example)Example

```json
description:pool name:pool^5
```

The above syntax performs Match Queries for **pool** in both the `name` and `description` fields, but documents having the term in the `name` field score higher.

```json
{
"field":"city", "match": "glossop", "boost":5`, `field":"title", "match": "glossop"}
```

The above syntax performs Match Queries for a city **glossop** in both the `city` and `title` fields, but documents having the term in the `city` field score higher.