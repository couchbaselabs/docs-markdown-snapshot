---
title: Match Phrase Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-match-phrase.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-supported-queries-match-phrase.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-supported-queries-match-phrase.html)

# Match Phrase Query

The input text is analyzed, and a phrase query is built with the terms resulting from the analysis. This type of query searches for terms in the target that occur _in the positions and offsets indicated by the input_: this depends on _term vectors_, which must have been included in the creation of the index used for the search.

For example, a match phrase query for `location for functions` is matched with `locate the function`, if the standard analyzer is used: this analyzer uses a _stemmer_, which tokenizes `location` and `locate` to `locat`, and reduces `functions` and `function` to `function`. Additionally, the analyzer employs _stop_ removal, which removes small and less significant words from input and target text, so that matches are attempted on only the more significant elements of vocabulary: in this case `for` and `the` are removed. Following this processing, the tokens `locat` and `function` are recognized as _common to both input and target_; and also as being both _in the same sequence as_, and _at the same distance from_ one another; and therefore a match is made.

## [](#example)Example

The following JSON object demonstrates specification of a match phrase query:

```json
{
 "match_phrase": "very nice",
 "field": "reviews.content"
}
```

A demonstration of the match phrase query using the Java SDK can be found in [Searching from the SDK](#3.2@java-sdk::full-text-searching-with-sdk.adoc).