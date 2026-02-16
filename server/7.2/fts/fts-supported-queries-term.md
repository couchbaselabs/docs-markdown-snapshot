[View original HTML](/server/7.2/fts/fts-supported-queries-term.html)

A term query is the simplest possible query. It performs an exact match in the index for the provided term.

## [](#example)Example

```json
{
  "term": "locate",
  "field": "reviews.content"
}
```

A demonstration of term queries using the Java SDK can be found in [Searching from the SDK](#3.2@java-sdk::full-text-searching-with-sdk.adoc).