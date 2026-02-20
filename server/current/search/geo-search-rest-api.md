---
title: Run a Geospatial Search Query with the REST API and curl/HTTP
description: Search for geospatial data in your Couchbase Server cluster with a
  compatible Search index, the REST API and curl/HTTP.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/geo-search-rest-api.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:search:geo-search-rest-api.adoc[]
---

[View original HTML](/server/current/search/geo-search-rest-api.html)

# Run a Geospatial Search Query with the REST API and curl/HTTP

> Search for geospatial data in your Couchbase Server cluster with a compatible Search index, the REST API and curl/HTTP. 

For more information about how the Search Service scores documents in search results, see [Scoring for Search Queries](run-searches.md#scoring).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
* You have documents in your cluster that contain geospatial data.  
For more information about the supported data types, see [geopoint](field-data-types-reference.md#geopoint) or [geoshape](field-data-types-reference.md#geoshape).
* Your user account has the [Search Admin](../learn/security/roles.md#search-admin) role for the bucket where you want to create the Search index.  
If you only want to run a search, you only need the **Search Reader** role.
* You installed the Couchbase command-line tool (CLI).
* You have the hostname or IP address for the node in your cluster where you’re running the Search Service. For more information about where to find the IP address for your node, see [List Cluster Nodes](../manage/manage-nodes/list-cluster-nodes.md).

## [](#procedure)Procedure

To run a geospatial Search query, [create a Search index with a geospatial type mapping](#geospatial-index).

Then, [run a Search query from the Couchbase Server Web Console](#geospatial-query).

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
        "scoring_model": "tf-idf",
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
                    //Replace with "geoshape" if your field contains GeoJSON data, instead.
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
2. Set your header content to include `"Content-Type: application/json"`.
3. Enter your username, password, and the Search Service endpoint on port `8094` with the name of the index you want to query:  
```console  
curl -s -XPOST -H "Content-Type: application/json" \
    -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/${BUCKET-NAME}/scope/${SCOPE-NAME}/index/${INDEX-NAME}/query -d \  
```  
To use SSL, use the `https` protocol in the Search Service endpoint URL and port `18094`.
4. Enter the JSON payload for your query.

### [](#example-geopoint-query)Example: Geopoint Query

For example, the following query searches a geospatial field, `geo`, for any locations within a 100 mile radius of the coordinates `-2.235143, 53.482358` with a [Distance/Radius-Based Geopoint Query](search-request-params.md#geopoint-queries-distance):

```console
curl -s -XPOST -H "Content-Type: application/json" \
    -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/${BUCKET-NAME}/scope/${SCOPE-NAME}/index/${INDEX-NAME}/query 
    -d '{
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
    }'
```

If the REST API call is successful, the Search Service returns a `200 OK`. Using the `landmark` collection, the query can return the following JSON response:

```json
{
    "status": {
        "total": 1,
        "failed": 0,
        "successful": 1
    },
    "hits": [
        {
            "index": "travel-sample.inventory.geo-index_78125822b3de7be3_4c1c5584",
            "id": "landmark_17411",
            "score": 0.009274733001968816,
            "sort": [
                " \u0001?E#9\u003eN\u000c\"e"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_78125822b3de7be3_4c1c5584",
            "id": "landmark_17409",
            "score": 0.009274733001968816,
            "sort": [
                " \u0001?O~i*(kD,"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_78125822b3de7be3_4c1c5584",
            "id": "landmark_17403",
            "score": 0.009274733001968816,
            "sort": [
                " \u0001?Sg*|/t\u001f\u0002"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_78125822b3de7be3_4c1c5584",
            "id": "landmark_17410",
            "score": 0.009274733001968816,
            "sort": [
                " \u0001?Z3T6 \u0010\u0019@"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_78125822b3de7be3_4c1c5584",
            "id": "landmark_17412",
            "score": 0.009274733001968816,
            "sort": [
                " \u0001?]-\u000fm?\u000b\u0014#"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_78125822b3de7be3_4c1c5584",
            "id": "landmark_17408",
            "score": 0.009274733001968816,
            "sort": [
                " \u0001?^DV7\u0014t:^"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_78125822b3de7be3_4c1c5584",
            "id": "landmark_17406",
            "score": 0.009274733001968816,
            "sort": [
                " \u0001?_\u003c\u00009\u001eW\u0013\u0012"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_78125822b3de7be3_4c1c5584",
            "id": "landmark_17397",
            "score": 0.009274733001968816,
            "sort": [
                " \u0001?c\u001cx\u0010n\u0016Wl"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_78125822b3de7be3_4c1c5584",
            "id": "landmark_17407",
            "score": 0.009274733001968816,
            "sort": [
                " \u0001?c!7\u0001@SwS"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_78125822b3de7be3_4c1c5584",
            "id": "landmark_17391",
            "score": 0.009274733001968816,
            "sort": [
                " \u0001?dgzZ[\u0007;y"
            ],
            "partial_match": true
        }
    ],
    "total_hits": 640,
    "cost": 157249,
    "max_score": 0.17106779096990765,
    "took": 15349178,
    "facets": null
}
```

### [](#example-geojson-query)Example: GeoJSON Query

> [!TIP]
> To run the following example against the `landmark` collection in the `travel-sample` dataset, run the following SQL++ query from the [Query Workbench](../tools/query-workbench.md):
> 
> ```sqlpp
> UPDATE `travel-sample`.inventory.landmark
>     SET geojson = { "type": "Point", "coordinates": [geo.lon, geo.lat] }
>     WHERE geo IS NOT null;
> ```

For example, the following query searches a geospatial field, `geojson`, for any locations within a defined shape with a [Polygon GeoJSON Query](search-request-params.md#geojson-queries-polygon):

```console
curl -s -XPOST -H "Content-Type: application/json" \
    -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/${BUCKET-NAME}/scope/${SCOPE-NAME}/index/${INDEX-NAME}/query 
    -d '{
        "query": {
            "field": "geojson",
            "geometry": {
                "shape": {
                    "coordinates": [
                    [
                        [
                        -3.272607322511618,
                        53.94443025530833
                        ],
                        [
                        -3.369506040138134,
                        53.2576036482846
                        ],
                        [
                        -1.531900030030954,
                        53.352538254565076
                        ],
                        [
                        -0.08209172686298416,
                        53.568703110993994
                        ],
                        [
                        -0.4648577685729265,
                        53.86797332814126
                        ],
                        [
                        -1.612712602375666,
                        54.022352820673774
                        ],
                        [
                        -2.2803785770867933,
                        54.05470383755585
                        ],
                        [
                        -3.272607322511618,
                        53.94443025530833
                        ]
                    ]
                    ],
                    "type": "Polygon"
                },
                "relation": "within"
            }
        }
    }'
```

If the REST API call is successful, the Search Service returns a `200 OK`. Using the `landmark` collection, the query can return the following JSON response:

```json
{
    "status": {
        "total": 1,
        "failed": 0,
        "successful": 1
    },
    "hits": [
        {
            "index": "travel-sample.inventory.geo-index_642c3761fc0a2c73_4c1c5584",
            "id": "landmark_40010",
            "score": 0.1332053777355554,
            "sort": [
                "_score"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_642c3761fc0a2c73_4c1c5584",
            "id": "landmark_40011",
            "score": 0.1332053777355554,
            "sort": [
                "_score"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_642c3761fc0a2c73_4c1c5584",
            "id": "landmark_554",
            "score": 0.016920542554627847,
            "sort": [
                "_score"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_642c3761fc0a2c73_4c1c5584",
            "id": "landmark_11323",
            "score": 0.016920542554627847,
            "sort": [
                "_score"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_642c3761fc0a2c73_4c1c5584",
            "id": "landmark_37316",
            "score": 0.016920542554627847,
            "sort": [
                "_score"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_642c3761fc0a2c73_4c1c5584",
            "id": "landmark_581",
            "score": 0.016920542554627847,
            "sort": [
                "_score"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_642c3761fc0a2c73_4c1c5584",
            "id": "landmark_15903",
            "score": 0.016920542554627847,
            "sort": [
                "_score"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_642c3761fc0a2c73_4c1c5584",
            "id": "landmark_570",
            "score": 0.016920542554627847,
            "sort": [
                "_score"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_642c3761fc0a2c73_4c1c5584",
            "id": "landmark_566",
            "score": 0.016920542554627847,
            "sort": [
                "_score"
            ],
            "partial_match": true
        },
        {
            "index": "travel-sample.inventory.geo-index_642c3761fc0a2c73_4c1c5584",
            "id": "landmark_22565",
            "score": 0.016920542554627847,
            "sort": [
                "_score"
            ],
            "partial_match": true
        }
    ],
    "total_hits": 257,
    "cost": 35339,
    "max_score": 0.1332053777355554,
    "took": 10019436,
    "facets": null
}
```

## [](#next-steps)Next Steps

You can [customize your Search index](customize-index.md) to improve search results and performance.

You can also:

* Change the JSON payload [for your Search index](search-index-params.md).
* Change the JSON payload [for your Search query](search-request-params.md).

If you want to add autocomplete to your cluster’s search, see [Use Autocomplete with the Search Service](search-query-auto-complete.md).