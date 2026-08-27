---
title: Match Query
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-match.adoc
  xref: xref:7.2@server:fts:fts-supported-queries-match.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-supported-queries-match.html)

# Match Query

A term without any other syntax is interpreted as a match query for the term in the default field. The default field is `_all`.

For example, `pool` performs match query for the term `pool`.

A match query _analyzes_ input text and uses the results to query an index. Options include specifying an analyzer, performing a _fuzzy match_, and performing a _prefix match_.

By default, the analyzer used for the search text is what was set for the specified field during index creation. For information on analyzers, see [Understanding Analyzers](fts-index-analyzers.md).

> [!NOTE]
> If the field is not specified, the match query will target the `_all` field within the index. Including content within the `_all` field is a setting during index creation.

When fuzzy matching is used, if the single parameter is set to a non-zero integer, the analyzed text is matched with a corresponding level of fuzziness. The maximum supported fuzziness is 2.

When a prefix match is used, the `prefix_length` parameter specifies that for a match to occur, a prefix of specified length must be shared by the input-term and the target text-element.

When an operator field is used, the `operator` decides the boolean logic used to interpret the text in the match field.

For example, an operator value of `"and"` means the match query text would be treated like `location` AND `hostel`. The default operator value of `"or"` means the match query text would be treated like `location` OR `hostel`.

A demonstration of the match query using the Java SDK can be found in [Searching from the SDK](../../../java-sdk/current/howtos/full-text-searching-with-sdk.md).

## [](#example)Example

The following JSON object demonstrates the specification of a match query:

```json
{
 "match": "location hostel",
 "field": "reviews.content",
 "analyzer": "standard",
 "fuzziness": 2,
 "prefix_length": 4,
 "operator": "and"
}
```