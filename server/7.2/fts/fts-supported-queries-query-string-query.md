---
title: Query String Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-query-string-query.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/fts/fts-supported-queries-query-string-query.html)

# Query String Query

A _query string_ can be used, to express a given query by means of a special syntax.

```json
{ "query": "+nice +view" }
```

A demonstration of a query string Query using the Java SDK can be found in [Searching from the SDK](#3.2@java-sdk::full-text-searching-with-sdk.adoc).

> [!NOTE]
> The Full Text Searches conducted with the Couchbase Web Console themselves use query strings. (See [Searching from the UI](fts-searching-from-the-UI.md).)

Certain queries supported by FTS are not yet supported by the query string syntax. These include wildcards and regular expressions.

More detailed information is provided in [Query String Syntax](fts-query-string-syntax.md)