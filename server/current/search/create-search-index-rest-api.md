---
title: Create a Search Index with the REST API and curl/HTTP
description: You can create a Search index with the Search Service API.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/create-search-index-rest-api.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:search:create-search-index-rest-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/search/create-search-index-rest-api.html)

# Create a Search Index with the REST API and curl/HTTP

> You can create a Search index with the Search Service API. 

You must create a Search index before you can [run a search](simple-search-rest-api.md) with the Search Service.

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
* Your user account has the [Search Admin](../learn/security/roles.md#search-admin) role for the bucket where you want to create the index.
* You have installed the Couchbase command-line tool (CLI).
* You have the hostname or IP address for the node in your cluster where you’re running the Search Service. For more information about where to find the IP address for your node, see [List Cluster Nodes](../manage/manage-nodes/list-cluster-nodes.md).

## [](#procedure)Procedure

To create a Search index with the REST API:

1. In your command-line tool, enter a `curl` command with the `XPUT` verb.
2. Set your header content to include `"Content-Type: application/json"`.
3. Enter your username, password, and the Search Service endpoint on port `8094` with the name of the index you want to create:  
```console  
curl -s -XPUT -H "Content-Type: application/json" \
    -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/travel-sample/scope/inventory/index/landmark-content-index  
    -d \  
```  
To use SSL, use the `https` protocol in the Search Service endpoint URL and port `18094`.  
> [!NOTE]  
> Your index name must start with an alphabetic character (a-z or A-Z). It can only contain alphanumeric characters (a-z, A-Z, or 0-9), hyphens (-), or underscores (\_).  
>  
> For Couchbase Server version 7.6 and later, your index name must be unique inside your selected bucket and scope. You cannot have 2 indexes with the same name inside the same bucket and scope.
4. Enter the JSON payload for the settings you want in your index.  
Do not include the [uuid](search-index-params.md#uuid) or [sourceUUID](search-index-params.md#sourceuuid) parameters.  
> [!TIP]  
> If you remove the [uuid](search-index-params.md#uuid) and [sourceUUID](search-index-params.md#sourceuuid) parameters, you can copy the Search index definition JSON payload from the Couchbase Server Web Console to use in your REST API call. For more information about how to create an index with the UI, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).

### [](#example-simple-search-index-with-xattrs)Example: Simple Search Index with XATTRs

In the following example, the JSON payload creates a simple index named `landmark-content-index` on the `travel-sample` bucket. It creates a type mapping for the `inventory.landmark` collection, with a child field, `content`, and adds a [dynamic Extended Attributes (XATTRs) mapping](about-mappings.md#xattrs) for any available document metadata fields in the collection:

```console
curl -s -XPUT -H "Content-Type: application/json" \
  -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/travel-sample/scope/inventory/index/landmark-content-index 
  -d \
  '{
      "type": "fulltext-index",
      "name": "landmark-content-index",
      "sourceType": "gocbcore",
      "sourceName": "travel-sample",
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
            "inventory.landmark": {
              "dynamic": false,
              "enabled": true,
                "properties": {
                  "_$xattrs": {
                  "dynamic": true,
                  "enabled": true
                },
                "content": {
                  "dynamic": false,
                  "enabled": true,
                  "fields": [
                    {
                      "docvalues": true,
                      "include_in_all": true,
                      "include_term_vectors": true,
                      "index": true,
                      "name": "content",
                      "store": true,
                      "type": "text"
                    }
                  ]
                }
              }
            }
          }
        },
        "store": {
          "indexType": "scorch",
          "segmentVersion": 15
        }
      },
      "sourceParams": {}
    }'
```

> [!IMPORTANT]
> XATTRs mappings are only available in Couchbase Server version 7.6.2 and later.

For more information about the available JSON properties for a Search index, see [Search Index JSON Properties](search-index-params.md).

If the REST API call is successful, the Search Service returns a `200 OK` and the following JSON response:

```json
{
    "status": "ok",
    "name": "travel-sample.inventory.landmark-content-index",
    "uuid": "49563a96ea6d3686"
}
```

The `"uuid"` is randomly generated for each Search index you create. Your own UUID might not match the value shown in the example.

### [](#example-search-index-with-custom-document-filter)Example: Search Index with Custom Document Filter

Couchbase Server 8.0

In the following example, the JSON payload creates a Search index named `travel-sample-filter` on the `travel-sample` bucket. It has a custom document filter, `cleanliness_AND_free_breakfast`, which uses a [conjunct filter](search-index-params.md#conjunct%5Ffilter) to restrict the documents in the index. Only documents with a cleanliness rating between 3 and 5 and `free_breakfast` set to `true` are included from the `inventory.hotel` collection.

For documents that pass the filter, the index includes the `description`, `free_breakfast`, `name`, `reviews.content`, and `reviews.ratings.Cleanliness` fields:

```console
curl -s -XPUT -H "Content-Type: application/json" \
  -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/travel-sample/scope/inventory/index/travel-sample-filter-index 
  -d \
  '{
    "type": "fulltext-index",
    "name": "travel-sample.inventory.travel-sample-filter",
    "sourceType": "gocbcore",
    "sourceName": "travel-sample",
    "planParams": {
      "maxPartitionsPerPIndex": 128,
      "indexPartitions": 1
    },
    "params": {
      "doc_config": {
        "doc_filter": {
          "cleanliness_AND_free_breakfast": {
            "conjuncts": [
              {
                "field": "reviews.ratings.Cleanliness",
                "inclusive_max": true,
                "max": 5,
                "min": 3
              },
              {
                "bool": true,
                "field": "free_breakfast"
              }
            ],
            "order": 1
          }
        },
        "docid_prefix_delim": "",
        "docid_regexp": "",
        "mode": "scope.collection.custom",
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
          "inventory.hotel.cleanliness_AND_free_breakfast": {
            "dynamic": false,
            "enabled": true,
            "properties": {
              "description": {
                "dynamic": false,
                "enabled": true,
                "fields": [
                  {
                    "docvalues": true,
                    "include_in_all": true,
                    "include_term_vectors": true,
                    "index": true,
                    "name": "description",
                    "store": true,
                    "type": "text"
                  }
                ]
              },
              "free_breakfast": {
                "dynamic": false,
                "enabled": true,
                "fields": [
                  {
                    "docvalues": true,
                    "include_in_all": true,
                    "index": true,
                    "name": "free_breakfast",
                    "store": true,
                    "type": "boolean"
                  }
                ]
              },
              "name": {
                "dynamic": false,
                "enabled": true,
                "fields": [
                  {
                    "docvalues": true,
                    "include_in_all": true,
                    "include_term_vectors": true,
                    "index": true,
                    "name": "name",
                    "store": true,
                    "type": "text"
                  }
                ]
              },
              "reviews": {
                "dynamic": false,
                "enabled": true,
                "properties": {
                  "content": {
                    "dynamic": false,
                    "enabled": true,
                    "fields": [
                      {
                        "docvalues": true,
                        "include_in_all": true,
                        "include_term_vectors": true,
                        "index": true,
                        "name": "content",
                        "store": true,
                        "type": "text"
                      }
                    ]
                  },
                  "ratings": {
                    "dynamic": false,
                    "enabled": true,
                    "properties": {
                      "Cleanliness": {
                        "dynamic": false,
                        "enabled": true,
                        "fields": [
                          {
                            "docvalues": true,
                            "include_in_all": true,
                            "index": true,
                            "name": "Cleanliness",
                            "store": true,
                            "type": "number"
                          }
                        ]
                      }
                    }
                  }
                }
              }
            }
          }
        }
      },
      "store": {
        "indexType": "scorch",
        "segmentVersion": 16
      }
    },
    "sourceParams": {}
  }'
```

For more information about the available JSON properties for a Search index, see [Search Index JSON Properties](search-index-params.md).

If the REST API call is successful, the Search Service returns a `200 OK` and the following JSON response:

```json
{
    "status": "ok",
    "name": "travel-sample.inventory.travel-sample-filter-index",
    "uuid": "5454607bd6b4b3e1"
}
```

The `"uuid"` is randomly generated for each Search index you create. Your own UUID might not match the value shown in the example.

## [](#next-steps)Next Steps

After you create a Search index, you can [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md) to test your Search index.

If you want to edit your index with another REST API call, include the [uuid](search-index-params.md#uuid) parameter with the UUID the Search Service assigned to your Search index.

You can also [Run A Simple Search with the Web Console](simple-search-ui.md) or with one of the Couchbase SDKs:

[.NET](../../../dotnet-sdk/current/howtos/full-text-searching-with-sdk.md)| [Go](../../../go-sdk/current/howtos/full-text-searching-with-sdk.md)| [Java](../../../java-sdk/current/howtos/full-text-searching-with-sdk.md)| [Kotlin](../../../kotlin-sdk/current/howtos/full-text-search.md)| [Node.js](../../../nodejs-sdk/current/howtos/full-text-searching-with-sdk.md)| [PHP](../../../php-sdk/current/howtos/full-text-searching-with-sdk.md)| [Python](../../../python-sdk/current/howtos/full-text-searching-with-sdk.md)| [Ruby](../../../ruby-sdk/current/howtos/full-text-searching-with-sdk.md)| [Scala](../../../scala-sdk/current/howtos/full-text-searching-with-sdk.md)