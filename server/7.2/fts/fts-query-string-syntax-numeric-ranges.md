---
title: Numeric Ranges
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-query-string-syntax-numeric-ranges.adoc
  xref: xref:7.2@server:fts:fts-query-string-syntax-numeric-ranges.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-query-string-syntax-numeric-ranges.html)

# Numeric Ranges

You can specify numeric ranges with the `>`, `>=`, `<`, and `<=` operators, each followed by a numeric value.

## [](#example)Example

`reviews.ratings.Cleanliness:>4` performs a [numeric range query](fts-supported-queries-numeric-range.md) on the `reviews.ratings.Cleanliness` field, for values greater than 4.