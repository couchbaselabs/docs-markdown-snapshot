---
title: Conjunction &amp; Disjunction Query
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries-conjuncts-disjuncts.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:fts:fts-supported-queries-conjuncts-disjuncts.adoc[]
---

[View original HTML](/server/7.2/fts/fts-supported-queries-conjuncts-disjuncts.html)

# Conjunction &amp; Disjunction Query

## [](#conjunction-query-and)Conjunction Query (AND)

A _conjunction_ query contains multiple _child queries_. Its result documents must satisfy all of the child queries.

```json
{
 "conjuncts":[
   {"field":"reviews.content", "match": "location"},
   {"field":"free_breakfast", "bool": true}
 ]
}
```

A demonstration of a conjunction query using the Java SDK can be found in [Searching from the SDK](#3.2@java-sdk::full-text-searching-with-sdk.adoc).

## [](#disjunction-query-or)Disjunction Query (OR)

A _disjunction_ query contains multiple _child queries_. Its result documents must satisfy a configurable `min` number of child queries. By default this `min` is set to 1\. For example, if three child queries — A, B, and C — are specified, a `min` of 1 specifies that the result documents should be those returned uniquely for A (with all returned uniquely for B and C, and all returned commonly for A, B, and C, omitted).

```json
{
 "disjuncts":[
   {"field":"reviews.content", "match": "location"},
   {"field":"free_breakfast", "bool": true}
 ]
}
```

A demonstration of a disjunction query using the Java SDK can be found in [Searching from the SDK](#3.2@java-sdk::full-text-searching-with-sdk.adoc).