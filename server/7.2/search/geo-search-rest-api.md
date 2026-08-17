---
title: Run a Geospatial Search Query with the REST API and curl/HTTP
description: Search for geospatial data in your Couchbase Server database with a
  compatible Search index, the REST API and curl/HTTP.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/geo-search-rest-api.adoc
  xref: xref:7.2@server:search:geo-search-rest-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/search/geo-search-rest-api.html)

# Run a Geospatial Search Query with the REST API and curl/HTTP

> Search for geospatial data in your Couchbase Server database with a compatible Search index, the REST API and curl/HTTP. 

## [](#prerequisites)Prerequisites

* You've deployed the Search Service on a node in your database.
* You have a bucket with scopes and collections in your database.
* Your user account has the **Search Admin** or **Search Reader** role.
* You installed the Couchbase command-line tool (CLI).
* You have the hostname or IP address for your database.

## [](#procedure)Procedure

To run a geospatial Search query, [create a Search index with a geospatial type mapping](#geospatial-index).

Then, [run a Search query from the Web Console](#geospatial-query).

### [](#geospatial-index)Create a Search Index with a Geospatial Type Mapping

To create the Search index with a geospatial type mapping:

1. [Create a Search Index with the REST API and curl/HTTP](create-search-index-rest-api.md) with the following JSON payload, replacing all placeholder values that start with a `$`:  
```json  
{  
    "type": "fulltext-index",  
    "name": "$INDEX_NAME",  
    "sourceType": "gocbcore",  
    "sourceName": "$BUCKET_NAME",  
    "planParams": {  
      "maxPartitionsPerPIndex": 1024,  
      "indexPartitions": 1  
    },  
    "params": {  
      "doc_config": {  
        "docid_prefix_delim": "",  
        "docid_regexp": "",  
        "mode": "scope.collection.type_field",  
        "type_field": "type"  
      },  
      "mapping": {  
        "analysis": {},  
        "default_analyzer": "standard",  
        "default_datetime_parser": "dateTimeOptional",  
        "default_field": "_all",  
        "default_mapping": {  
          "dynamic": true,  
          "enabled": false  
        },  
        "default_type": "_default",  
        "docvalues_dynamic": false,  
        "index_dynamic": true,  
        "store_dynamic": false,  
        "type_field": "_type",  
        "types": {  
          "$SCOPE_NAME.$COLLECTION_NAME": {  
            "dynamic": true,  
            "enabled": true,  
            "properties": {  
              "$FIELD_NAME": {  
                "dynamic": false,  
                "enabled": true,  
                "fields": [  
                  {  
                    "include_in_all": true,  
                    "index": true,  
                    "name": "$FIELD_NAME",  
                    "type": "geopoint"  
                  }  
                ]  
              }  
            }  
          }  
        }  
      },  
      "store": {  
        "indexType": "scorch",  
        "segmentVersion": 15,  
        "spatialPlugin": "s2"  
      }  
    },  
    "sourceParams": {}  
  }  
```

### [](#geospatial-query)Run a Geospatial Search Query

To run a Search query against the Search index:

1. In your command-line tool, enter a `curl` command with the `XPOST` verb.
2. Set your header content to include `Content-Type: application/json`.
3. Enter your username, password, and the Search Service endpoint on port `8094` with the name of the index you want to query:  
```console  
curl -s -XPUT -H "Content-Type: application/json" \
-u $CB_USERNAME:$CB_PASSWORD http://$CB_HOSTNAME:8094/api/index/$INDEX-NAME/query -d \  
```
4. Enter the JSON payload for your query.  
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

You can also:

* Change the JSON payload [for your Search index](search-index-params.md).
* Change the JSON payload [for your Search query](search-request-params.md).

If you want to add autocomplete to your database's search, see [Use Autocomplete with the Search Service](search-query-auto-complete.md).