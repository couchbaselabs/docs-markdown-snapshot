---
title: Date Range
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-query-string-syntax-date-ranges.adoc
  xref: xref:7.2@server:fts:fts-query-string-syntax-date-ranges.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-query-string-syntax-date-ranges.html)

# Date Range

You can perform date range searches by using the `>`, `>=`, `<`, and `<=` operators, followed by a date value in quotes.

For example, `created:>"2016-09-21"` will perform a [date range query](fts-supported-queries-date-range.md) on the `created` field for values after September 21, 2016.