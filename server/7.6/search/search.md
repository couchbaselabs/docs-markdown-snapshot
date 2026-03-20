---
title: Add Search to Your Application
description: Use the Search Service to create a customizable search experience
  for your cluster and your end-user applications.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/search.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:search:search.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/search/search.html)

# Add Search to Your Application

> Use the Search Service to create a customizable search experience for your cluster and your end-user applications. 

The Search Service offers near real-time search capabilities for a diverse range of data types. For example, you can use the Search Service with:

* [Vectors](#vector-search)
* Structured or unstructured text
* Dates
* Numbers
* CIDR notation
* Geospatial data

Use a [Search index](#indexes) to efficiently store your data, and retrieve it with a [Search query](#queries).

## [](#indexes)Search Indexes

A Search index tells the Search Service what content to use from the documents in your cluster for processing [Search queries](#queries). A Search index can use any field across multiple collections in a single scope. If your cluster is running Couchbase Server version 7.6.2 and later, it can also include any document metadata stored in Extended Attributes (XATTRs).

You can choose to exclude content to improve search performance and improve the relevance of search results.

A Search index can also analyze and modify the content in your Search index or Search query to improve matching and search results. The Search Service has default components that you can use to customize a Search index, or you can create your own.

You need to create a Search index before you can use the Search Service to search the contents of your cluster from your application.

For more information about how to create a Search index, see [Create a Search Index](create-search-indexes.md).

> [!NOTE]
> Updating Search indexes
> 
> Search indexes are updated automatically, reflecting changes from the Data Service.

You can create a Search index:

* [With the Couchbase Server Web Console](create-search-index-ui.md)
* [From the REST API](create-search-index-rest-api.md)

## [](#queries)Search Queries

A Search query tells the Search Service what to search for in the contents of a Search index.

Search queries use a simple string-based query syntax or JSON objects to control how the Search Service retrieves search results.

For more information about how you can run a search against a Search index, see [Run a Search With a Search Index](run-searches.md).

You can run a Search query:

* [With the Couchbase Server Web Console](simple-search-ui.md)
* [From the REST API](simple-search-rest-api.md)

## [](#vector-search)Vector Search for AI Applications

Vector Search builds on Couchbase Server’s Search Service to provide vector index support for Retrieval Augmented Generation (RAG) with an existing Large Language Model (LLM).

Vector Search adds a new index type to the Search Service to support AI application development, known as a Vector Search index. Using Vector Search and Couchbase Server, you can develop applications with an existing LLM while giving context and up-to-date information from your own data.

For more information about Vector Search, see [Use Vector Search for AI Applications](../vector-search/vector-search.md).

## [](#see-also)See Also

* [Create a Search Index](create-search-indexes.md)
* [Customize a Search Index with the Web Console](customize-index.md)
* [Create Search Index Aliases](index-aliases.md)
* [Run a Search With a Search Index](run-searches.md)
* [Use Vector Search for AI Applications](../vector-search/vector-search.md)