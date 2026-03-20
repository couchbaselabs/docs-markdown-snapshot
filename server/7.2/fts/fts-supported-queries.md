---
title: Supported Queries
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-supported-queries.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:fts:fts-supported-queries.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/fts/fts-supported-queries.html)

# Supported Queries

> With Full Text Search you can perform queries on Full Text Indexes. You can perform the queries either by using Couchbase Web Console, the Couchbase REST API, SQL++ (using search functions in the Query service), or the Couchbase SDK. 

## [](#query-specification-options)Query-Specification Options

Full Text Search allows a range of query options. These include:

* Input-text and target-text can be _analyzed_: this transforms input-text into _token-streams_, according to different specified criteria, so allowing richer and more finely controlled forms of text-matching.
* The _fuzziness_ of a query can be specified so that the scope of matches can be constrained to a particular level of exactitude. A high degree of fuzziness means that a large number of partial matches may be returned.
* Multiple queries can be specified for simultaneous processing, with one given a higher _boost_ than another, so ensuring that its results are returned at the top of the set.
* _Regular expressions_ and _wildcards_ can be used in text-specification for search-input.
* _Compound_ queries can be designed, such that appropriate conjunction or disjunction of the total result-set can be returned.

For information on how to execute queries, see [Searching from the UI](fts-searching-from-the-UI.md).

This section includes the following supported queries:

* [Query String Query](fts-supported-queries-query-string-query.md)
* [Match](fts-supported-queries-match.md)
* [Match Phrase](fts-supported-queries-match-phrase.md)
* [Non Analytic](fts-supported-queries-non-analytic-query.md)
* [Compound](fts-supported-queries-compound-query.md)
* [Range](fts-supported-queries-range-query.md)
* [Geospatial](fts-supported-queries-geopoint-spatial.md)
* [Special](fts-supported-queries-special-query.md)
* [Query Options](fts-supported-queries-query-options.md)