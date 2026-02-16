[View original HTML](/server/7.2/fts/fts-supported-queries-regexp.html)

A _regexp_ query finds documents containing terms that match the specified regular expression. Please note that the regex query is a non-analytic query, meaning it won’t perform any text analysis on the query text.

```json
{
 "regexp": "inter.+",
 "field": "reviews.content"
}
```

A demonstration of a regexp query using the Java SDK can be found in [Searching from the SDK](#3.2@java-sdk::full-text-searching-with-sdk.adoc).