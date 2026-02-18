---
title: Default Date/Time Parsers
description: Use a date/time parser to tell the Search Service how to interpret
  date and time data in your documents.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/default-date-time-parsers-reference.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/search/default-date-time-parsers-reference.html)

# Default Date/Time Parsers

> Use a date/time parser to tell the Search Service how to interpret date and time data in your documents. 

You can set a [default date/time parser](customize-index.md#date-time) for your Search index, or set a date/time parser when you [create a single document field mapping](create-type-mapping.md#field) with a `datetime` type.

The following default date/time parsers are available:

| Date/Time Parser  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| datetime optional | The default date/time parser. The default date/time parser can parse dates in the following formats: %Y-%m-%dT%H:%M:%S.%N%z:M: For example, a date/time string like 2023-09-15T14:24:50.1567+05:30 %Y-%m-%dT%H:%M:%S%z:M: For example, a date/time string like \`2023-09-15T14:24:50+05:30 %Y-%m-%dT%H:%M:%S: For example, a date/time string like 2023-09-15T14:24:50 %Y-%m-%d %H:%M:%S: For example, a date/time string like 2023-09-15 14:24:50 %Y-%m-%d %H:%M:%S %z: For example, a date/time string like 2023-09-15 14:24:50 +0530 %Y-%m-%d: For example, a date/time string like 2023-09-15 |
| disabled          | The default date/time parser is disabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| unix\_micro       | For date/time data formatted as the number of microseconds since the Unix epoch 1970-01-01T00:00:00Z.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| unix\_milli       | For date/time data formatted as the number of milliseconds since the Unix epoch 1970-01-01T00:00:00Z.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| unix\_nano        | For date/time data formatted as the number of nanoseconds since the Unix epoch 1970-01-01T00:00:00Z.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| unix\_sec         | For date/time data formatted as the number of seconds since the Unix epoch 1970-01-01T00:00:00Z.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## [](#see-also)See Also

* [Create a Custom Date/Time Parser](create-custom-date-time-parser.md)
* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Search Index](create-search-indexes.md)