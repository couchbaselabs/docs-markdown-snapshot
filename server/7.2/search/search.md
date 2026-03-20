---
title: Add Search to Your Application
description: Use the Search Service to create a customizable search experience
  for your database and your end-user applications.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/search.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:search:search.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/search/search.html)

# Add Search to Your Application

> Use the Search Service to create a customizable search experience for your database and your end-user applications. 

The Search Service offers near real-time search capabilities for a diverse range of data types. For example, you can use the Search Service with:

* Structured or unstructured text
* Dates
* Numbers
* CIDR notation
* Geospatial data

Use a [Search index](#indexes) to efficiently store your data, and retrieve it with a [Search query](#queries).

## [](#indexes)Search Indexes

A Search index tells the Search Service what content to use from the documents in your database for processing [Search queries](#queries). A Search index can use any field across multiple collections in a single scope. You can choose to exclude content to improve search performance and improve the relevance of search results.

A Search index can also analyze and modify the content in your Search index or Search query to improve matching and search results. The Search Service has default components that you can use to customize a Search index, or you can create your own.

You need to create a Search index before you can use the Search Service to search the contents of your database from your application.

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

For more information about how you can run a search against a Search index, see [Run a Search](run-searches.md).

You can run a Search query:

* [With the Couchbase Server Web Console](simple-search-ui.md)
* [From the REST API](simple-search-rest-api.md)