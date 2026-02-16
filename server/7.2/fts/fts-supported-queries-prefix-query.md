[View original HTML](/server/7.2/fts/fts-supported-queries-prefix-query.html)

A _prefix_ query finds documents containing terms that start with the specified prefix. Please note that the prefix query is a non-analytic query, meaning it won’t perform any text analysis on the query text.

```json
{
 "prefix": "inter",
 "field": "reviews.content"
}
```