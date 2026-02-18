---
title: Fuzzy Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-fuzzy.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/fts/fts-supported-queries-fuzzy.html)

# Fuzzy Query

A _fuzzy query_ matches terms within a specified _edit_ (or _Levenshtein_) distance: meaning that terms are considered to match when they are to a specified degree _similar_, rather than _exact_. A common prefix of a stated length may be also specified as a requirement for matching.

> [!NOTE]
> The fuzzy query is a non-analytic query, meaning it won’t perform any text analysis on the query text.

Fuzziness is specified by means of a single integer. A value of `0` indicates that the terms must be identical. The maximum value that you can specify is `2`. For example:

```json
{
 "term": "interest",
 "field": "reviews.content",
 "fuzziness": 2
}
```

A demonstration of _Fuzziness_ using the Java SDK, in the context of the _term query_ (see below) can be found in [Searching from the SDK](#3.2@java-sdk::full-text-searching-with-sdk.adoc).

> [!NOTE]
> Two such queries are specified, with the difference in fuzziness between them resulting in different forms of match, and different sizes of result-sets.