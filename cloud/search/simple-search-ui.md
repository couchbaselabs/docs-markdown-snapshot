---
title: Run A Simple Search with the Capella UI
description: Run a Search query from the Couchbase Capella UI to preview the
  search results from a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/simple-search-ui.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/search/simple-search-ui.html)

# Run A Simple Search with the Capella UI

> Run a Search query from the Couchbase Capella UI to preview the search results from a Search index. 

For more information about how the Search Service scores documents in search results, see [Scoring for Search Queries](run-searches.md#scoring).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have created a Search index.  
For more information about how to create a Search index, see [Create a Search Index](create-search-indexes.md).
* You have logged in to the Couchbase Capella UI.

## [](#procedure)Procedure

To run a simple search with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you created your Search index.
3. Go to **Data Tools** **Search**.
4. Next to your Search index or [index alias](index-aliases.md), click **Search**.
5. In the **Search** field, enter a search query.
6. Press Enter.
7. (Optional) To view a document and its source collection, click a document name in the search results list.

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
> Use the [collections parameter](search-request-params.md#collections) in your request to specify an array of collections to search from the Search index.

### [](#example-validate-a-search-query)Example: Validate a Search Query

Couchbase Server 7.6.5

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

If you do not get the search results you were expecting, you can change the [JSON payload for your Search query](search-request-params.md).

You can also [Search Index Features](customize-index.md).