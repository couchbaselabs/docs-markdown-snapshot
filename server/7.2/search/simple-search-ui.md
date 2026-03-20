---
title: Run A Simple Search with the Web Console
description: Run a Search query from the Couchbase Server Web Console to preview
  the search results from a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/simple-search-ui.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:search:simple-search-ui.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/search/simple-search-ui.html)

# Run A Simple Search with the Web Console

> Run a Search query from the Couchbase Server Web Console to preview the search results from a Search index. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your database.
* Your user account has the **Search Admin** or **Search Reader** role.
* You have created a Search index.  
For more information about how to create a Search index, see [Create a Search Index](create-search-indexes.md).
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To run a simple search with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the index or [index alias](#index-alises.adoc) where you want to run a search.
3. In the **Search this index** field, enter a search query.  
For example, the following query searches for the strings `view`, `food`, and `beach`:  
```json  
{  
    "explain": true,  
    "fields": [  
      "*"  
    ],  
    "highlight": {},  
    "query": {  
      "query": "+view +food +beach"  
    },  
    "size": 10,  
    "from": 0  
}  
```  
The query payload enables scoring explanations and term highlighting. It also returns all available fields in the index, and returns 10 results per page.  
> [!TIP]  
> Use a [Search index alias](index-aliases.md) to search multiple Search indexes in a single search query. Use the [collections parameter](search-request-params.md#collections) in your request to specify an array of collections to search from the Search index.
4. Press Enter or click **Search**.
5. (Optional) To view the contents of a document, click the document name in the search results list.

## [](#next-steps)Next Steps

If you do not get the search results you were expecting, you can change the [JSON payload for your Search query](search-request-params.md).

You can also [Customize a Search Index with the Web Console](customize-index.md).