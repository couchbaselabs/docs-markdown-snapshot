---
title: Create a Vector Search Index with the REST API and curl/HTTP
description: You can create a Vector Search index with the Search Service API.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/vector-search/pages/create-vector-search-index-rest-api.adoc
  xref: xref:7.6@server:vector-search:create-vector-search-index-rest-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/vector-search/create-vector-search-index-rest-api.html)

# Create a Vector Search Index with the REST API and curl/HTTP

> You can create a Vector Search index with the Search Service API. 

You must create a Search index before you can [run a search](run-vector-search-rest-api.md) with the Search Service.

> [!TIP]
> Vector Search indexes can include all the same features and settings as a Search index. For more information about Search indexes, see the [Search documentation](../search/search.md).

> [!IMPORTANT]
> You cannot use Vector Search on Windows platforms. You can use Vector Search on Linux from Couchbase Server version 7.6.0 and MacOS from version 7.6.2.
> 
> You can still use other features of the [Search Service](../search/search.md).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../../current/manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../../current/manage/manage-buckets/create-bucket.md).
* You have documents in a keyspace inside your bucket that contain vector embeddings.  
> [!TIP]  
> You can download a sample dataset to use with the procedure or examples on this page:  
>  
> [Download color\_data\_2vectors.zip](https://cbc-remote-execution-examples-prod.s3.amazonaws.com/color%5Fdata%5F2vectors.zip)  
>  
> To get the best results with using the sample data with the examples in this documentation, [import the sample files](../guides/import.md) from the dataset into your database with the following settings:  
>  
> * Use a bucket called `vector-sample`.  
> * Use a scope called `color`.  
> * Use a collection called `rgb` for `rgb.json`.  
> * To set your document keys, use the value of the `id` field from each JSON document.
* Your user account has the **Search Admin** role for the bucket where you want to create the index.
* You have installed the Couchbase command-line tool (CLI).
* You have the hostname or IP address for the node in your cluster where you're running the Search Service. For more information about where to find the IP address for your node, see [List Cluster Nodes](../../current/manage/manage-nodes/list-cluster-nodes.md).

## [](#procedure)Procedure

To create a Search index with the REST API:

1. In your command-line tool, enter a `curl` command with the `XPUT` verb.
2. Set your header content to include `"Content-Type: application/json"`.
3. Enter your username, password, and the Search Service endpoint on port `8094` with the name of the index you want to create:  
```console  
curl -s -XPUT -H "Content-Type: application/json" \
    -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/${BUCKET_NAME}/scope/${SCOPE_NAME}/index/${INDEX_NAME}  
    -d \  
```
4. Enter the JSON payload for the settings you want in your index.  
Do not include the [uuid](../search/search-index-params.md#uuid) or [sourceUUID](../search/search-index-params.md#sourceuuid) parameters.  
> [!TIP]  
> If you remove the [uuid](../search/search-index-params.md#uuid) and [sourceUUID](../search/search-index-params.md#sourceuuid) parameters, you can copy the Search index definition JSON payload from the Couchbase Server Web Console to use in a REST API call. For more information about how to create a Vector Search index with the UI, see [Create a Vector Search Index with the Server Web Console](create-vector-search-index-ui.md).

### [](#example)Example

In the following example, the JSON payload creates an index named `color-index` on the `vector-sample.color.rgb` keyspace. It creates two child field mappings, `colorvect_l2` and `embedding_vector_dot` on two different vector fields in the keyspace's documents.

It also adds 3 normal Search index fields (`brightness`, `color`, and `description`) to add more usable data to the Vector Search index:

```console
curl -s -XPUT -H "Content-Type: application/json" \
    -u ${CB_USERNAME}:${CB_PASSWORD} http://${CB_HOSTNAME}:8094/api/bucket/vector-sample/scope/color/index/color-index 
    -d \
  '{
    "type": "fulltext-index",
    "name": "vector-sample.color.color-index",
    "sourceType": "gocbcore",
    "sourceName": "vector-sample",
    "sourceUUID": "789365cccdf940ee2814a5dd2752040a",
    "planParams": {
      "maxPartitionsPerPIndex": 512,
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
          "dynamic": false,
          "enabled": false
        },
        "default_type": "_default",
        "docvalues_dynamic": false,
        "index_dynamic": false,
        "store_dynamic": false,
        "type_field": "_type",
        "types": {
        "color.rgb": {
          "dynamic": false,
          "enabled": true,
          "properties": {
            "brightness": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "index": true,
                  "name": "brightness",
                  "store": true,
                  "type": "number"
                }
              ]
            },
            "color": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "analyzer": "en",
                  "index": true,
                  "name": "color",
                  "store": true,
                  "type": "text"
                }
              ]
            },
            "colorvect_dot": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "dims": 3,
                  "index": true,
                  "name": "colorvect_dot",
                  "similarity": "dot_product",
                  "type": "vector"
                }
              ]
            },
            "colorvect_l2": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "dims": 3,
                  "index": true,
                  "name": "colorvect_l2",
                  "similarity": "l2_norm",
                  "type": "vector"
                }
              ]
            },
            "description": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "analyzer": "en",
                  "index": true,
                  "name": "description",
                  "store": true,
                  "type": "text"
                }
              ]
            },
            "embedding_vector_dot": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "dims": 1536,
                  "index": true,
                  "name": "embedding_vector_dot",
                  "similarity": "dot_product",
                  "type": "vector"
                }
              ]
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

> [!NOTE]
> This sample JSON Vector Search index is the same as the one provided in [Create a Vector Search Index with the Server Web Console](create-vector-search-index-ui.md).

For more information about all the available JSON properties for a Search index, see [Search Index JSON Properties](../search/search-index-params.md).

If the REST API call is successful, the Search Service returns a `200 OK` and the following JSON response:

```json
{
    "status": "ok",
    "name": "vector-sample.color.color-index",
    "uuid": "629266a5f4e09384"
}
```

The `"uuid"` is randomly generated for each Search index you create. Your own UUID might not match the value shown in the example.

## [](#next-steps)Next Steps

After you create a Search index, you can [Run a Vector Search with the REST API and curl/HTTP](run-vector-search-rest-api.md) to test your Search index.

If you want to edit your index with another REST API call, include the [uuid](../search/search-index-params.md#uuid) parameter with the UUID the Search Service assigned to your Vector Search index.

You can also [Create a Vector Search Index with the Server Web Console](create-vector-search-index-ui.md).