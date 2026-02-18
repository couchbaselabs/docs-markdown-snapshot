---
title: Numeric Range Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-numeric-range.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/fts/fts-supported-queries-numeric-range.html)

# Numeric Range Query

A _numeric range_ query finds documents containing a numeric value in the specified field within the specified range.

Define the endpoints using the fields `min` and `max`. You can omit any one endpoint, but not both.

The `inclusive_min` and `inclusive_max` properties control whether or not the endpoints are included or excluded.

By default, `min` is inclusive and `max` is exclusive.

A demonstration of the numeric range Query using the Java SDK can be found in [Searching from the SDK](#3.2@java-sdk::full-text-searching-with-sdk.adoc).

## [](#example)Example

```json
{
 "min": 100, "max": 1000,
 "inclusive_min": false,
 "inclusive_max": false,
 "field": "id"
}
```

## [](#numeric-ranges)Numeric Ranges

You can specify numeric ranges with the `>`, `>=`, `<`, and `<=` operators, each followed by a numeric value.

### [](#example-2)Example

```json
`reviews.ratings.Cleanliness:>4`
```

The above qeury performs numeric range query on the `reviews.ratings.Cleanliness` field, for values greater than 4.