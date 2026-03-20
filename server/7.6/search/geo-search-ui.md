---
title: Run a Geospatial Search Query with the Web Console
description: Search for geospatial data in your Couchbase Server cluster with a
  compatible Search index and the Couchbase Server Web Console.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/geo-search-ui.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:search:geo-search-ui.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/search/geo-search-ui.html)

# Run a Geospatial Search Query with the Web Console

> Search for geospatial data in your Couchbase Server cluster with a compatible Search index and the Couchbase Server Web Console. 

For more information about how the Search Service scores documents in search results, see [Scoring for Search Queries](run-searches.md#scoring).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../../current/manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../../current/manage/manage-buckets/create-bucket.md).
* You have documents in your cluster that contain geospatial data.
* Your user account has the **Search Admin** role for the bucket where you want to create the Search index.  
If you only want to run a search, you only need the **Search Reader** role.
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To run a geospatial Search query, [create a Search index with a geospatial type mapping](#geospatial-index).

Then, [run a Search query from the Web Console](#geospatial-query).

### [](#geospatial-index)Create a Search Index with a Geospatial Type Mapping

To create the Search index from the Web Console:

1. Go to **Search**.
2. Click **Add Index**.
3. In the **Index Name** field, enter a name for the index.  
> [!NOTE]  
> Your index name must start with an alphabetic character (a-z or A-Z). It can only contain alphanumeric characters (a-z, A-Z, or 0-9), hyphens (-), or underscores (\_).  
>  
> For Couchbase Server version 7.6 and later, your index name must be unique inside your selected bucket and scope. You cannot have 2 indexes with the same name inside the same bucket and scope.
4. In the **Bucket** list, select the bucket where you want to create the index.
5. Expand **Customize Index**.
6. Select **Use non-default scope/collection(s)**.

  1. In the **Scope** list, select the scope that contains the documents you want to include in your index.
7. [Create a Type Mapping](create-type-mapping.md) on the collection in your cluster that you want to search.
8. [Create a Child Field](create-child-field.md) on the new type mapping with the following settings:

  1. In the **Field** field, enter the name of the field in your documents that contains the geospatial data you want to search.
  2. In the **Type** list, select **geopoint**.
  3. Select **Index**.
  4. Select **Include in \_all field**.
9. Click **OK**.
10. Click **Create Index**.

### [](#geospatial-query)Run a Geospatial Search Query

To run a Search query against the Search index from the Web Console:

1. Go to **Search**.
2. Click the index where you want to run a search.
3. In the **Search this index** field, enter a search query.  
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

> [!TIP]
> Couchbase Server version 7.6.2
> 
> You can generate a full command-line curl example from the preceding query in the Server Web Console to use with the REST API. Click **show advanced query settings**, then **show command-line curl example** to get the example code.

## [](#next-steps)Next Steps

You can [customize your Search index](customize-index.md) to improve search results and performance.

If you want to add autocomplete to your cluster’s search, see [Use Autocomplete with the Search Service](search-query-auto-complete.md).