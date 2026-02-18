---
title: Run a Geospatial Search Query with the Web Console
description: Search for geospatial data in your Couchbase database with a
  compatible Search index and the Couchbase Server Web Console.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/geo-search-ui.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/search/geo-search-ui.html)

# Run a Geospatial Search Query with the Web Console

> Search for geospatial data in your Couchbase database with a compatible Search index and the Couchbase Server Web Console. 

## [](#prerequisites)Prerequisites

* You’ve deployed the Search Service on a node in your database.
* You have a bucket with scopes and collections in your database.
* Your user account has the **Search Admin** role for the bucket where you want to create the index.
* You’ve logged in to the Couchbase Server Web Console.

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
4. In the **Bucket** list, select the bucket where you want to create the index.
5. [Create a Type Mapping](create-type-mapping.md) on the scope and collection in your database that you want to search.
6. [Create a Child Field](create-child-field.md) on the new type mapping with the following settings:

  1. In the **Field** field, enter the name of the field in your documents that contains the geospatial data you want to search.
  2. In the **Type** list, select **geopoint**.
  3. Select **Index**.
  4. Select **Include in \_all field**.
7. Click **Submit**.
8. Click **Create Index**.

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

## [](#next-steps)Next Steps

You can [customize your Search index](customize-index.md) to improve search results and performance.

If you want to add autocomplete to your database’s search, see [Use Autocomplete with the Search Service](search-query-auto-complete.md).