---
title: Run A Simple Search with the Web Console
description: Run a Search query from the Couchbase Server Web Console to preview
  the search results from a Search index.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/simple-search-ui.adoc
  xref: xref:server:search:simple-search-ui.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/search/simple-search-ui.html)

# Run A Simple Search with the Web Console

> Run a Search query from the Couchbase Server Web Console to preview the search results from a Search index. 

For more information about how the Search Service scores documents in search results, see [Scoring for Search Queries](run-searches.md#scoring).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
* You have created a Search index.  
For more information about how to create a Search index, see [Create a Search Index](create-search-indexes.md).
* Your user account has the [Search Admin](../learn/security/roles.md#search-admin) or [Search Reader](../learn/security/roles.md#search-reader) role for the bucket or buckets that contain the Search indexes you want to search.
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To run a simple search with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the index where you want to run a search.
3. In the **Search this index** field, enter a search query.
4. Press Enter or click **Search**.
5. (Optional) To view the full contents of a document returned in the search results, click one of the results.
6. (Optional) To view the results of document scoring in search results, click **Show Scoring**.
7. (Couchbase Server version 7.6.2 and later) To directly edit the [Search request JSON payload](search-request-params.md) for your Search query and run a new search:

  1. Click **show advanced query settings**.
  2. Click **Edit**.
  3. Edit the JSON payload. For more information about the available parameters, see [Search Request JSON Properties](search-request-params.md).
  4. Click **Execute**.

### [](#example-simple-text-search)Example: Simple Text Search

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

### [](#example-validate-a-search-query)Example: Validate a Search Query

Couchbase Server 7.6.4

For example, the following query searches a Search index, `landmark-content-index`, using a [Distance/Radius-Based Geopoint Query](search-request-params.md#geopoint-queries-distance) on the `geo` field. The query includes the [ctl object](search-request-params.md#ctl) with the `validate` property to validate the query:

```json
{
    "explain": true,
    "fields": [
      "content"
    ],
    "highlight": {},
    "query": {
        "location": {
            "lon": -2.235143,
            "lat": 53.482358
        },
            "distance": "100mi",
            "field": "geo"
    },
    "ctl": {
        "validate": true
    },
    "size": 10,
    "from": 0
}
```

Since the `landmark-content-index` does not include a mapping for the `geo` field and the `validate` property is included in the query, the Web Console returns the following error:

query_validate: field not indexed, name: geo, type: geopoint

## [](#next-steps)Next Steps

If you do not get the search results you were expecting, you can change the [JSON payload for your Search query](search-request-params.md). If your cluster is running Couchbase Server version 7.6.2 and later, you can edit the JSON payload directly in the UI by clicking **show advanced query settings**.

Run any changes to your JSON payload by clicking **Execute**.

You can also [Customize a Search Index with the Web Console](customize-index.md).