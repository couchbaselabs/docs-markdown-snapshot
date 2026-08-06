---
title: Search
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.8/modules/concept-docs/pages/full-text-search-overview.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:ruby-sdk:concept-docs:full-text-search-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/current/concept-docs/full-text-search-overview.html)

# Search

> The _Search Service_ lets you create, manage, and query specially purposed _indexes_, defined on JSON documents within a Couchbase bucket. 

## [](#what-is-the-search-service)What is the Search Service?

The _Search Service_ provides extensive capabilities for _natural-language querying_: this allows special search-constraints to be applied to text-queries. Results can be _scored_, to indicate match-relevancy; and result-sets ordered correspondingly. _Conjunctive_ and _disjunctive_ searches can be performed, whereby common result-subsets from multiple queries can either be returned or omitted.

A full overview of the Search Service is provided in [The Search Service: Fundamentals](../../../server/current/search/search.md). This includes information on the principal features of Couchbase Search Service, its architecture, and the latest feature-additions. Other information-sources include:

* [Performing Searches](../../../server/7.2/fts/fts-perform-searches.md): An explanation of the steps required to prepare for and perform Search.
* [Searching from the UI](../../../server/7.2/fts/fts-searching-from-the-UI.md): A brief introduction to the Search Service user interface provided by the Couchbase Web Console, with a step-by-step example of how to create a simple Search Index, and perform a search on it.
* [Searching with the REST API](../../../server/7.2/fts/fts-searching-with-curl-http-requests.md): Basic examples of how Search is performed with REST, and pointers to more complex examples.
* [Creating Indexes](../../../server/7.2/fts/fts-creating-indexes.md): A full description of the index-creation facility provided by the Couchbase Web Console, with explanations of each component to be used, and illustrations of how indexes can be designed to include specific subsets of documents and their fields.
* [Understanding Analyzers](../../../server/7.2/fts/fts-index-analyzers.md): An explanation of _analyzers_, which are used to process the text to be included in Search Indexes.
* [Queries](../../../server/7.2/fts/fts-search-request.md): A detailed account of available query types, response objects, and result-sorting options.

## [](#performing-search-from-the-sdk)Performing Search from the SDK

Couchbase SDKs provides an API for the support of Search querying. A detailed example of performing Search queries from the SDK is provided in [Searching from the SDK](../howtos/full-text-searching-with-sdk.md).

Note that to access Search, users require appropriate _roles_. The role `fts_admin` must therefore be assigned to those who intend to create indexes; and the role `fts_searcher` to those who intend to perform searches. For information on creating users and assigning roles, see the [RBAC Roles page](#7.1@server:learn:security/roles.adoc#search-admin).

## [](#search-from-sql)Search from SQL++

The search service can be accessed by [search functions in SQL++ Query](../../../server/7.2/n1ql/n1ql-language-reference/searchfun.md) (formerly N1QL).