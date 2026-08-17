---
title: Pre-filtering Vector Searches
description: You can specify filters as part of a Vector Search query object to
  restrict the documents searched in a Search index.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/vector-search/pages/pre-filtering-vector-search.adoc
  xref: xref:cloud:vector-search:pre-filtering-vector-search.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/vector-search/pre-filtering-vector-search.html)

# Pre-filtering Vector Searches

> You can specify filters as part of a Vector Search query object to restrict the documents searched in a Search index. 

## [](#about-pre-filtering)About Pre-filtering

The Search Service supports pre-filtering on Vector Search queries. Pre-filtering allows you to execute vector searches over a subset of the vector index, via the means of a filter request that qualifies the subset.

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have a bucket with scopes and collections in your operational cluster. For more information, see [Manage Buckets](../clusters/data-service/manage-buckets.md).
* You have created a Search Vector Index.  
For more information about how to create a Search Vector Index, see [Create a Search Vector Index in Quick Mode](create-vector-search-index-ui.md).  
> [!TIP]  
> You can import a sample dataset to use with the procedure or examples on this page.  
>  
> Go to **Data Tools** **Import** from your cluster and [import the color-vector-sample](../clusters/data-service/import-data-documents.md#import-sample-data) sample data.  
>  
> For the best results, consider using the sample Search Vector Index from [Create a Search Vector Index with the Capella UI](create-vector-search-index-ui.md#example).

## [](#procedure)Procedure

To add pre-filtering to a Vector Search query:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you created your Search Vector Index.
3. Go to **Data Tools** **Search**.
4. Next to your Search Vector Index, click **Search**.
5. In the **Search** field, enter a search query that includes a `filter` object with your `knn` object.  
For more information about the `filter` object, see [filter](../search/search-request-params.md#filter).
6. Press Enter or click **Search**.
7. (Optional) To view a document and its source collection, click a document name in the search results list.

### [](#example-pre-filter-a-vector-search-query-for-the-color-navy)Example: Pre-Filter A Vector Search Query For The Color "Navy"

For example, the following Vector Search query tries to find matches to a color with an RGB value of `[176, 0, 176]` with a minimum brightness of `70` and a maximum of `80`. A pre-filter on the query will narrow the documents searched inside the Search Vector Index to documents that have a `color` field value that closely matches `navy`:

```json
{
  "fields": ["*"],
  "query": {
    "min": 70,
    "max": 80,
    "inclusive_min": false,
    "inclusive_max": true,
    "field": "brightness"
  },
  "knn": [
    {
      "k": 10,
      "field": "colorvect_l2",
      "vector": [ 176, 0, 176 ],
      "filter": {
        "field":  "color",
        "match": "navy"
      }
    }
  ]
}
```