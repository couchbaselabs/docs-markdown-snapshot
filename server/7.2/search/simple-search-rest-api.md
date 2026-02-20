---
title: Run a Simple Search with the REST API and curl/HTTP
description: You can use the REST API and a curl command to run a search against
  a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/simple-search-rest-api.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:search:simple-search-rest-api.adoc[]
---

[View original HTML](/server/7.2/search/simple-search-rest-api.html)

# Run a Simple Search with the REST API and curl/HTTP

> You can use the REST API and a curl command to run a search against a Search index. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your database.
* Your user account has the **Search Admin** or **Search Reader** role.
* You installed the Couchbase command-line tool (CLI).
* You have the hostname or IP address for your database.
* You’ve created a Search index.  
For more information about how to create a Search index, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md) or [Create a Search Index with the REST API and curl/HTTP](create-search-index-rest-api.md).

## [](#procedure)Procedure

To run a search with the REST API:

1. In your command-line tool, enter a `curl` command with the `XPOST` verb.
2. Set your header content to include `Content-Type: application/json`.
3. Enter your username, password, and the Search Service endpoint on port `8094` with the name of the index you want to query:  
```console  
curl -s -XPUT -H "Content-Type: application/json" \
-u $CB_USERNAME:$CB_PASSWORD http://$CB_HOSTNAME:8094/api/index/$INDEX-NAME/query -d \  
```  
To use SSL, use the `https` protocol in the Search Service endpoint URL and port `18094`.
4. Enter the JSON payload for your query.  
> [!TIP]  
> You can copy the JSON for a Query Request from the Couchbase Server Web Console to use in your REST API call. For more information about how to perform a search with the UI, see [Run A Simple Search with the Web Console](simple-search-ui.md).  
In the following example, the JSON payload queries an index named `landmark-content-index` for the strings `view`, `food`, and `beach`:  
```console  
curl -XPOST -H "Content-Type: application/json" \
  -u $CB_USERNAME:$CB_PASSWORD http://$CB_HOSTNAME:8094/api/index/landmark-content-index/query \
-d '{  
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
}'  
```  
For more information about the available properties for a Search query JSON payload, see [Search Request JSON Properties](search-request-params.md).

## [](#next-steps)Next Steps

If you don’t get the search results you were expecting, you can change the JSON payload [for your Search index](search-index-params.md) or [for your Search query](search-request-params.md).

You can also [Customize a Search Index with the Web Console](customize-index.md).