---
title: Date Range
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-query-string-syntax-date-ranges.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/fts/fts-query-string-syntax-date-ranges.html)

# Date Range

You can perform date range searches by using the `>`, `>=`, `<`, and `<=` operators, followed by a date value in quotes.

For example, `created:>"2016-09-21"` will perform a [date range query](fts-supported-queries-date-range.md) on the `created` field for values after September 21, 2016.