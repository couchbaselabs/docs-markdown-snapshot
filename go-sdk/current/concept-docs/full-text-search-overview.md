---
title: Search
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.11/modules/concept-docs/pages/full-text-search-overview.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:go-sdk:concept-docs:full-text-search-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/current/concept-docs/full-text-search-overview.html)

# Search

> _Full Text Search_ (FTS) lets you create, manage, and query specially purposed _indexes_, defined on JSON documents within a Couchbase bucket. 

## [](#what-is-full-text-search)What is Full Text Search?

_Full Text Search_ provides extensive capabilities for _natural-language querying_: this allows special search-constraints to be applied to text-queries. Results can be _scored_, to indicate match-relevancy; and result-sets ordered correspondingly. _Conjunctive_ and _disjunctive_ searches can be performed, whereby common result-subsets from multiple queries can either be returned or omitted.

A full overview of Full Text Search is provided in [Full Text Search: Fundamentals](#7.1@server:fts:full-text-intro.adoc). This includes information on the principal features of Couchbase Full Text Search, its architecture, and the latest feature-additions. Other information-sources include:

* [Performing Searches](../../../server/7.2/fts/fts-perform-searches.md): An explanation of the steps required to prepare for and perform Full Text Search.
* [Searching from the UI](../../../server/7.2/fts/fts-searching-from-the-UI.md): A brief introduction to the Full Text Search user interface provided by the Couchbase Web Console, with a step-by-step example of how to create a simple Full Text Index, and perform a search on it.
* [Searching with the REST API](../../../server/7.2/fts/fts-searching-with-curl-http-requests.md): Basic examples of how Full Text Search is performed with REST, and pointers to more complex examples.
* [Creating Indexes](../../../server/7.2/fts/fts-creating-indexes.md): A full description of the index-creation facility provided by the Couchbase Web Console, with explanations of each component to be used, and illustrations of how indexes can be designed to include specific subsets of documents and their fields.
* [Understanding Analyzers](../../../server/7.2/fts/fts-index-analyzers.md): An explanation of _analyzers_, which are used to process the text to be included in Full Text Indexes.
* [Queries](../../../server/7.2/fts/fts-search-request.md): A detailed account of available query types, response objects, and result-sorting options.

## [](#performing-full-text-search-from-the-sdk)Performing Full Text Search from the SDK

Couchbase SDKs provides an API for the support of Full Text Search querying. A detailed example of performing Full Text Search queries from the SDK is provided in [Searching from the SDK](../howtos/full-text-searching-with-sdk.md).

Note that to access Full Text Search, users require appropriate _roles_. The role **FTS Admin** must therefore be assigned to those who intend to create indexes; and the role **FTS Searcher** to those who intend to perform searches. For information on creating users and assigning roles, see the [RBAC Roles page](#7.1@server:learn:security/roles.adoc#search-admin).

## [](#search-from-sql)Search from SQL++

The search service can be accessed by [search functions in SQL++ Query](../../../server/7.2/n1ql/n1ql-language-reference/searchfun.md) (formerly N1QL).