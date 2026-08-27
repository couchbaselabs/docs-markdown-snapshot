---
title: Date and Time Functions - Working with Queries
description: Couchbase Lite database data querying concepts -- data and time function
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/android/pages/query-date-time.adoc
  xref: xref:2.8@couchbase-lite:android:query-date-time.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/android/query-date-time.html)

# Date and Time Functions - Working with Queries

> Description — _Couchbase Lite database data querying concepts — data and time function_  
> Related Content — [Predictive Query](#couchbase-lite:android:query-predictive.adoc) | [Live Query](../../current/android/query-live.md) | [Queries](../../current/android/querybuilder.md)

## [](#available-functions)Available Functions

Couchbase Lite documents support a [date type](#initializers) that internally stores dates in ISO 8601 with the GMT/UTC timezone.

Couchbase Lite 2.5 adds the ability to run date comparisons in your Couchbase Lite queries. To do so, four functions have been added to the Query Builder API:

`Function.StringToMillis(Expression.Property("date_time"))`

The input to this will be a validly formatted ISO 8601 `date_time` string. The end result will be an expression (with a numeric content) that can be further input into the query builder.

`Function.StringToUTC(Expression.Property("date_time"))`

The input to this will be a validly formatted ISO 8601 `date_time` string. The end result will be an expression (with string content) that can be further input into the query builder.

`Function.MillisToString(Expression.Property("date_time"))`

The input for this is a numeric value representing milliseconds since the Unix epoch. The end result will be an expression (with string content representing the date and time as an ISO 8601 string in the device's timezone) that can be further input into the query builder.

`Function.MillisToUTC(Expression.Property("date_time"))`

The input for this is a numeric value representing milliseconds since the Unix epoch. The end result will be an expression (with string content representing the date and time as a UTC ISO 8601 string) that can be further input into the query builder.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Queries](../../current/android/querybuilder.md)
* [Live Query](../../current/android/query-live.md)
* [Predictive Query](#couchbase-lite:android:query-predictive.adoc)
* [Full Text Search](../../current/android/fts.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/android/database.md)
* [Documents](../../current/android/document.md)
* [Blobs](../../current/android/blob.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)