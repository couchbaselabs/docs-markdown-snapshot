---
title: Add Search to Your Application
description: Use the Search Service to create a customizable search experience
  for your operational cluster and your end-user applications.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/search.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:search:search.adoc[]
---

[View original HTML](/cloud/search/search.html)

# Add Search to Your Application

> Use the Search Service to create a customizable search experience for your operational cluster and your end-user applications. 

The Search Service offers near real-time search capabilities for a diverse range of data types. For example, you can use the Search Service with:

* Structured or unstructured text
* Dates
* Numbers
* CIDR notation
* Geospatial data

Use a [Search index](#indexes) to efficiently store your data, and retrieve it with a [Search query](#queries).

## [](#indexes)Search Indexes

A Search index tells the Search Service what content to use from the documents in your operational cluster for processing [Search queries](#queries). A Search index can use any field across multiple collections in a single scope. If your operational cluster is running Couchbase Server version 7.6.2 and later, it can also include any document metadata stored in Extended Attributes (XATTRs).

You can choose to exclude content to improve search performance and improve the relevance of search results.

A Search index can also analyze and modify the content in your Search index or Search query to improve matching and search results. The Search Service has default components that you can use to customize a Search index, or you can create your own.

You need to create a Search index before you can use the Search Service to search the contents of your operational cluster from your application.

For more information about how to create a Search index, see [Create a Search Index](create-search-indexes.md).

You can create a Search index:

* [With the Couchbase Capella UI](create-search-index-ui.md)
* With a [JSON payload](search-index-params.md) that you [import through the UI](import-search-index.md).

As of Couchbase Server version 8.0, you can also add synonym collections to your cluster and Search index to run synonym searches on text fields. For more information about synonym searches, see [Add Synonyms to a Search Index](synonyms/synonyms-search.md).

## [](#queries)Search Queries

A Search query tells the Search Service what to search for in the contents of a Search index.

Search queries use a simple string-based query syntax or JSON objects to control how the Search Service retrieves search results.

For more information about how you can run a search against a Search index, see [Run a Search With a Search Index](run-searches.md).

You can run a Search query:

* [With the Couchbase Capella UI](simple-search-ui.md)
* [With a SQL++ query](../n1ql/n1ql-language-reference/searchfun.md).
* With the Couchbase SDKs:  
[.NET](../../dotnet-sdk/current/howtos/full-text-searching-with-sdk.md)| [Go](../../go-sdk/current/howtos/full-text-searching-with-sdk.md)| [Java](../../java-sdk/current/howtos/full-text-searching-with-sdk.md)| [Kotlin](../../kotlin-sdk/current/howtos/full-text-search.md)| [Node.js](../../nodejs-sdk/current/howtos/full-text-searching-with-sdk.md)| [PHP](../../php-sdk/current/howtos/full-text-searching-with-sdk.md)| [Python](../../python-sdk/current/howtos/full-text-searching-with-sdk.md)| [Ruby](../../ruby-sdk/current/howtos/full-text-searching-with-sdk.md)| [Scala](../../scala-sdk/current/howtos/full-text-searching-with-sdk.md)

## [](#vector-search-for-ai-applications)Vector Search for AI Applications

Vector Search builds on Capella’s Search Service to provide vector index support for Retrieval Augmented Generation (RAG) with an existing Large Language Model (LLM).

Vector Search adds a new index type to the Search Service to support AI application development, known as a Search Vector Index. Using Vector Search and Couchbase Capella, you can develop applications with an existing LLM while giving context and up-to-date information from your own data.

For more information about Vector Search, see [Vector Search Using Search Vector Indexes](../vector-search/vector-search.md).

## [](#see-also)See Also

* [Create a Search Index](create-search-indexes.md)
* [Search Index Features](customize-index.md)
* [Create Search Index Aliases](index-aliases.md)
* [Run a Search With a Search Index](run-searches.md)
* [Vector Search Using Search Vector Indexes](../vector-search/vector-search.md)