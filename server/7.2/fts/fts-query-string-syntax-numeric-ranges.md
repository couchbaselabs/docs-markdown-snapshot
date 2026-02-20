---
title: Numeric Ranges
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-query-string-syntax-numeric-ranges.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-query-string-syntax-numeric-ranges.adoc[]
---

[View original HTML](/server/7.2/fts/fts-query-string-syntax-numeric-ranges.html)

# Numeric Ranges

You can specify numeric ranges with the `>`, `>=`, `<`, and `<=` operators, each followed by a numeric value.

## [](#example)Example

`reviews.ratings.Cleanliness:>4` performs a [numeric range query](fts-supported-queries-numeric-range.md) on the `reviews.ratings.Cleanliness` field, for values greater than 4.