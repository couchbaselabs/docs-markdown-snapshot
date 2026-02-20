---
title: Run a Geospatial Search Query with the Capella UI
description: Search for geospatial data in your Couchbase Capella operational
  cluster with a compatible Search index and the Capella UI.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/geo-search-ui.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:search:geo-search-ui.adoc[]
---

[View original HTML](/cloud/search/geo-search-ui.html)

# Run a Geospatial Search Query with the Capella UI

> Search for geospatial data in your Couchbase Capella operational cluster with a compatible Search index and the Capella UI. 

For more information about how the Search Service scores documents in search results, see [Scoring for Search Queries](run-searches.md#scoring).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have a bucket with scopes and collections in your operational cluster. For more information, see [Manage Buckets](../clusters/data-service/manage-buckets.md).
* You have documents in your operational cluster that contain geospatial data.
* You have logged in to the Couchbase Capella UI.

## [](#procedure)Procedure

To run a geospatial Search query, [create a Search index with a geospatial type mapping in Advanced Mode](#geospatial-index).

Then, [run a Search query from the Capella UI](#geospatial-query).

### [](#geospatial-index)Create a Search Index with a Geospatial Type Mapping

To create the Search index in the Capella UI with Advanced Mode:

1. On the **Operational Clusters** page, select the operational cluster where you want to create a Search index.
2. Go to **Data Tools** **Search**.
3. Click **Create Search Index**.
4. In the **Index Name** field, enter a name for the Search index.  
> [!NOTE]  
> Your index name must start with an alphabetic character (a-z or A-Z). It can only contain alphanumeric characters (a-z, A-Z, or 0-9), hyphens (-), or underscores (\_).  
>  
> For Couchbase Server version 7.6 and later, your index name must be unique inside your selected bucket and scope. You cannot have 2 indexes with the same name inside the same bucket and scope.
5. In the **Bucket** and **Scope** lists, choose the bucket and scope where you want to create your Search index. This bucket and scope should contain the collection and documents that have your geospatial data.
6. In your document schema, expand the collection that holds the documents with your geospatial data.
7. Click the name of the field that holds your geospatial data.
8. In the **Type** list, select **Geopoint**.
9. Select **Include in search results**.
10. Select **Support field agnostic search**.
11. Click **Add To Index**.
12. Click **Create Index**.

### [](#geospatial-query)Run a Geospatial Search Query

To run a Search query against the Search index from the Capella UI:

1. Next to your [geospatial type mapping Search index](#geospatial-index), click **Search**.
2. In the **Search** field, enter a search query for geospatial data.  
For example, the following query searches a geospatial field, `geo`, for any locations within a 100 mile radius of the coordinates `-2.235143, 53.482358`:  
```json  
{  
    "from": 0,  
    "size": 10,  
    "query": {  
      "location": {  
        "lon": -2.235143,  
        "lat": 53.482358  
       },  
        "distance": "100mi",  
        "field": "geo"  
      },  
    "sort": [  
      {  
        "by": "geo_distance",  
        "field": "geo",  
        "unit": "mi",  
        "location": {  
        "lon": -2.235143,  
        "lat": 53.482358  
        }  
      }  
    ]  
  }  
```

## [](#next-steps)Next Steps

For more information about the different features you can add to your Search index to improve performance and search results, see [Search Index Features](customize-index.md).

If you want to add autocomplete to your operational cluster’s search, see [Use Autocomplete with the Search Service](search-query-auto-complete.md).