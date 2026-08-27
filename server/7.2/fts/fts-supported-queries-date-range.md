---
title: Date Range Query
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-date-range.adoc
  xref: xref:7.2@server:fts:fts-supported-queries-date-range.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-supported-queries-date-range.html)

# Date Range Query

A _date\_range_ query finds documents containing a date value, in the specified field within the specified range.

Dates should be in the format specified by RFC-3339, which is a specific profile of ISO-8601.

Define the endpoints using the fields `start` and `end`. You can omit any one endpoint, but not both.

The `inclusive_start` and `inclusive_end` properties in the query JSON control whether or not the endpoints are included or excluded.

## [](#example)Example

```json
{
 "start": "2001-10-09T10:20:30-08:00",
 "end": "2016-10-31",
 "inclusive_start": false,
 "inclusive_end": false,
 "field": "review_date"
}
```