---
title: Use Autocomplete with the Search Service
description: Add autocomplete to your application to provide a search
  engine-like experience for your cluster.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/search-query-auto-complete.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:search:search-query-auto-complete.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/search/search-query-auto-complete.html)

# Use Autocomplete with the Search Service

> Add autocomplete to your application to provide a search engine-like experience for your cluster. 

Also known as auto suggest or type-ahead, autocomplete guesses potential matches for a user’s search input as they type.

Autocomplete can provide a better user experience with search in your application.

## [](#set-up-autocomplete)Set Up Autocomplete

To use autocomplete with the Search Service and your Couchbase Server cluster:

1. Create a compatible Search index. You can create the index [with the UI](search-query-auto-complete-ui.md#ui) or [with the REST API](search-query-auto-complete-ui.md#api).
2. Configure your application to return autocomplete search results from the Search Service. For example code that you can use with your application, see [Add Autocomplete to Your Application](search-query-auto-complete-code.md).

You can use the `travel-sample` dataset to test and configure autocomplete, or use your own data.