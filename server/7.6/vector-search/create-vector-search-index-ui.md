---
title: Create a Vector Search Index with the Server Web Console
description: You can create a Vector Search index with the Couchbase Server Web Console.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/vector-search/pages/create-vector-search-index-ui.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:vector-search:create-vector-search-index-ui.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/vector-search/create-vector-search-index-ui.html)

# Create a Vector Search Index with the Server Web Console

> You can create a Vector Search index with the Couchbase Server Web Console. 

You must create a Vector Search index before you can [run a search](run-vector-search-ui.md) that supports vector comparisons.

> [!TIP]
> Vector Search indexes can include all the same features and settings as a Search index. For more information about Search indexes, see the [Search documentation](../search/search.md).

> [!IMPORTANT]
> You cannot use Vector Search on Windows platforms. You can use Vector Search on Linux from Couchbase Server version 7.6.0 and MacOS from version 7.6.2.
> 
> You can still use other features of the [Search Service](../search/search.md).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../../current/manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../../current/manage/manage-buckets/create-bucket.md).
* You have documents in a keyspace inside your bucket that contain vector embeddings. Embeddings can be an array of floats or a base64 encoded string.  
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
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To create a Vector Search index with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click **Add Index**.
3. In the **Index Name** field, enter a name for the Vector Search index.  
> [!NOTE]  
> Your index name must start with an alphabetic character (a-z or A-Z). It can only contain alphanumeric characters (a-z, A-Z, or 0-9), hyphens (-), or underscores (\_).  
>  
> For Couchbase Server version 7.6 and later, your index name must be unique inside your selected bucket and scope. You cannot have 2 indexes with the same name inside the same bucket and scope.
4. In the **Bucket** list, select the bucket that contains the documents you want to include in your index.
5. Expand **Customize Index**.
6. Select **Use non-default scope/collection(s)**.

  1. In the **Scope** list, select the scope that contains the documents you want to include in your index.
7. Expand **Mappings** and create a new type mapping on a collection:

  1. Click **Add Type Mapping**.
  2. In the **Collection** list, select the collection that contains the documents you want to include in your index.
  3. Select **Only index specified fields**.
  4. Click **OK**.  
For more information about how to create type mappings, see [Create a Type Mapping](../search/create-type-mapping.md).
8. Create a child field mapping on the new collection type mapping:

  1. In the **Field** field, enter the name of the field in your documents that contains your vector embeddings.  
  Vectors must be represented as an array of floating point numbers.
  2. In the **Type** list, do one of the following:

    1. If your child field contains vector embeddings as an array, click **vector**.
    2. (Couchbase Server version 7.6.2 or later) If your child field contains vector embeddings formatted as a base64 encoded string, click **vector\_base64**.
  3. In the **Dimension** field, enter the total number of elements in the array that holds the vector embeddings for your documents.  
  From Couchbase Server version 7.6.2 and later, the Search Service supports arrays with up to 4096 elements. Arrays can be an array of arrays.
  4. In the **Similarity metric** list, choose the method to use to calculate the similarity between search term and Search index vectors.  
  For more information, see [Child Field Options](../search/child-field-options-reference.md).
  5. In the **Optimized for** list, choose whether the Search Service should optimize Search queries for accuracy (**recall**) or speed (**latency**).  
  For more information, see [Child Field Options](../search/child-field-options-reference.md).
  6. Select **Index**.
  7. Click **OK**.
9. (Optional) Create another child field on the new collection type mapping for any additional fields you want to return in your search results.  
For example, you could add the text field that you used to generate your vector embeddings. For more information about how to create child fields, see [Create a Child Field](../search/create-child-field.md).
10. Next to the `default` dynamic type mapping, clear the checkbox.
11. Click **Create Index**.

### [](#example)Example: Creating a Vector Search Index for Vector Search Query Examples

If you want to use the sample dataset for the examples in [Run A Vector Search with the Server Web Console](run-vector-search-ui.md) and [Run a Vector Search with a Couchbase SDK](run-vector-search-sdk.md), then you can [import](../search/import-search-index.md) the following Search index definition into Server Web Console:

```json
{
    "name": "color-test",
    "type": "fulltext-index",
    "params": {
     "doc_config": {
      "docid_prefix_delim": "",
      "docid_regexp": "",
      "mode": "scope.collection.type_field",
      "type_field": "type"
     },
     "mapping": {
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
       "color.rgb": {
        "dynamic": false,
        "enabled": true,
        "properties": {
         "brightness": {
          "enabled": true,
          "dynamic": false,
          "fields": [
           {
            "docvalues": true,
            "index": true,
            "name": "brightness",
            "store": true,
            "type": "number"
           }
          ]
         },
         "color": {
          "enabled": true,
          "dynamic": false,
          "fields": [
           {
            "docvalues": true,
            "include_term_vectors": true,
            "index": true,
            "name": "color",
            "store": true,
            "type": "text"
           }
          ]
         },
         "colorvect_l2": {
          "enabled": true,
          "dynamic": false,
          "fields": [
           {
            "dims": 3,
            "index": true,
            "name": "colorvect_l2",
            "similarity": "l2_norm",
            "type": "vector",
            "vector_index_optimized_for": "recall"
           }
          ]
         },
         "embedding_vector_dot": {
          "enabled": true,
          "dynamic": false,
          "fields": [
           {
            "dims": 1536,
            "index": true,
            "name": "embedding_vector_dot",
            "similarity": "dot_product",
            "type": "vector",
            "vector_index_optimized_for": "recall"
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
    "sourceType": "gocbcore",
    "sourceName": "vector-sample",
    "sourceParams": {},
    "planParams": {
     "maxPartitionsPerPIndex": 1024,
     "indexPartitions": 1,
     "numReplicas": 0
    },
    "uuid": "42676f35cc30b84a"
   }
```

> [!NOTE]
> Make sure you imported the sample dataset with the recommended settings.

This Vector Search index has a type mapping for a `color.rgb` collection and includes the following fields:

* The **brightness number** field, which is included in search results and supports sorting and faceting.
* The **color string** and **description string** fields, which are included in search results, support highlighting, phrase matching, and sorting and faceting.
* The **colorvect\_l2 \[ number \]** field, which has a Dimension of `3` and uses the **l2\_norm** Similarity Metric.
* The **embedding\_vector\_dot \[ number \]** field, which has a dimension of `1536` and uses the **dot\_product** Similarity Metric.

## [](#next-steps)Next Steps

A basic Vector Search index includes the vector embeddings from the child field you specified in your type mapping. If you choose to add additional child fields and enable **Include in search results**, the Search Service can also return data from those child fields when you run a Vector Search query.

For more information about how to add additional child fields to your index, see [Create a Search Index with the Quick Editor](../search/create-quick-index.md) or [Create a Child Field](../search/create-child-field.md).

For example, if you used the Vector Search sample data, you might want to add another child field for the **color** string field to your Vector Search index, to return color names with your Search query. For more information about how to add additional child fields to your index, see [Create a Child Field](../search/create-child-field.md).

You can customize your Vector Search index like any other Search index to add additional data and improve search results. For more information about how to customize an index, see [Customize a Search Index with the Web Console](../search/customize-index.md).

For more information about how to run a search against a Vector Search index, see [Run A Vector Search with the Server Web Console](run-vector-search-ui.md) or [Run a Vector Search with the REST API and curl/HTTP](run-vector-search-rest-api.md).