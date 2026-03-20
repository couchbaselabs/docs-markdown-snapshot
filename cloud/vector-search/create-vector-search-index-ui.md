---
title: Create a Search Vector Index in Quick Mode
description: Use Quick Mode to create a Search Vector Index in Couchbase Capella.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/vector-search/pages/create-vector-search-index-ui.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:vector-search:create-vector-search-index-ui.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/vector-search/create-vector-search-index-ui.html)

# Create a Search Vector Index in Quick Mode

> Use Quick Mode to create a Search Vector Index in Couchbase Capella. 

Quick Mode works best when you need to create a basic Search index to start testing and prototyping with the Search Service. You must use Advanced Mode to have greater control over how the Search Service returns such results, such as changing your [analyzer](../search/customize-index.md#analyzers).

For more information about how to create a Search index in Advanced Mode, see [Create a Search Index with the Capella UI](../search/create-search-index-ui.md).

> [!TIP]
> Search Vector Indexes can include all the same features and settings as a Search index. For more information about Search indexes, see the [Search documentation](../search/search.md).

You must create a Search Vector Index before you can [run a search](run-vector-search-ui.md) that supports vector comparisons.

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have a bucket with scopes and collections in your operational cluster. For more information, see [Manage Buckets](../clusters/data-service/manage-buckets.md).
* You have documents in a keyspace inside your bucket that contain vector embeddings. Embeddings can be an array of floats or a base64 encoded string.  
> [!TIP]  
> You can import a sample dataset to use with the procedure or examples on this page.  
>  
> Go to **Data Tools** **Import** from your cluster and [import the color-vector-sample](../clusters/data-service/import-data-documents.md#import-sample-data) sample data.
* You have logged in to the Couchbase Capella UI.

## [](#procedure)Procedure

To create a Search Vector Index in Capella:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to create a Search Vector Index.
3. Do 1 of the following:

  1. Use the [Vector Index creation flow](#vector-indexes-flow).
  2. Use the [Search creation flow](#search-flow).

> [!NOTE]
> If you use the [Vector Index creation flow](#vector-indexes-flow), you cannot add fields other than vector fields to your index during your initial index creation.

### [](#vector-indexes-flow)Create a Search Vector Index from Vector Indexes

To use the **Vector Indexes** creation flow to create a new Search Vector Index:

1. Go to **Data Tools** **Vector Indexes**.
2. On the **Vector Indexes** page, click **\+ Create Vector Index**.
3. Click **Search Vector Index**.
4. In the **Index Name** field, enter a name for the Search Vector Index.  
> [!NOTE]  
> Your index name must start with an alphabetic character (a-z or A-Z). It can only contain alphanumeric characters (a-z, A-Z, or 0-9), hyphens (-), or underscores (\_).  
>  
> For Couchbase Server version 7.6 and later, your index name must be unique inside your selected bucket and scope. You cannot have 2 indexes with the same name inside the same bucket and scope.
5. In the **Bucket** and **Scope** lists, choose the bucket and scope where you want to create your Search Vector index.
6. In the **Collections** list, select the collection or collections that contain documents with vector embeddings.
7. Under **Type Mappings**, in your document schema, expand a collection that contains these documents.
8. In your document schema, select the child field that contains your vector embeddings.
9. Configure the options for the child field as follows:

  1. In the **Type** list, select 1 of the following:

    1. If your child field contains vector embeddings as an array, click **vector**.  
      Vector embeddings formatted as arrays appear as `{field-name} [ number ]` in the editor.
    2. (Couchbase Server version 7.6.2 or later) If your child field contains vector embeddings formatted as a base64 encoded string, click **vector\_base64**.  
      Vector embeddings formatted as base64 strings appear as `{field-name} [ string ]` in the Capella Quick Mode editor.
  2. In the **Dimension** field, check that the value matches the total number of elements in your vector embeddings array.  
  The Search Service supports arrays up to 4096 elements. Capella automatically fills in the dimension value for your selected child field when you choose the **vector** or **vector\_base64** type.
  3. In the **Similarity metric** list, choose the method to use to calculate the similarity between search term and Search index vectors.  
  For more information, see [Field Type Mapping Options](../search/type-mapping-options.md#field).
  4. In the **Optimized for** list, choose whether the Search Service should optimize Search queries for accuracy (**recall**) or speed (**latency**).  
  For more information, see [Field Type Mapping Options](../search/type-mapping-options.md#field).
10. Click **Add To Index**.
11. Click **Review Index**.
12. Click **Create Index**.

> [!TIP]
> After you create your Search Vector Index, click the index name to go back into the editor and add additional collections or child field type mappings to your index. For example, you could add the text field that you used to generate your vector embeddings. For more information, see [Add Type Mappings and Mappings](../search/create-search-index-ui.md#add-mapping).

### [](#search-flow)Create a Search Vector Index from Search

To use the **Search** creation flow to create a new Search Vector Index:

1. Go to **Data Tools** **Search**.
2. Click **Create Search Index**.
3. In the **Index Name** field, enter a name for the Search Vector Index.  
> [!NOTE]  
> Your index name must start with an alphabetic character (a-z or A-Z). It can only contain alphanumeric characters (a-z, A-Z, or 0-9), hyphens (-), or underscores (\_).  
>  
> For Couchbase Server version 7.6 and later, your index name must be unique inside your selected bucket and scope. You cannot have 2 indexes with the same name inside the same bucket and scope.
4. In the **Bucket** and **Scope** lists, choose the bucket and scope where you want to create your Search index.
5. In the **Collections** list, select the collection or collections that contain documents with vector embeddings.
6. Under **Type Mappings**, in your document schema, expand a collection that contains these documents.
7. In your document schema, select the child field that contains your vector embeddings.
8. Configure the options for the child field as follows:

  1. In the **Type** list, select 1 of the following:

    1. If your child field contains vector embeddings as an array, click **vector**.  
      Vector embeddings formatted as arrays appear as `{field-name} [ number ]` in the Capella Quick Mode editor.
    2. (Couchbase Server version 7.6.2 or later) If your child field contains vector embeddings formatted as a base64 encoded string, click **vector\_base64**.  
      Vector embeddings formatted as base64 strings appear as `{field-name} [ string ]` in the Capella Quick Mode editor.
  2. In the **Dimension** field, check that the value matches the total number of elements in your vector embeddings array.  
  The Search Service supports arrays up to 4096 elements. Capella automatically fills in the dimension value for your selected child field when you choose the **vector** or **vector\_base64** type.
  3. In the **Similarity metric** list, choose the method to use to calculate the similarity between search term and Search index vectors.  
  For more information, see [Field Type Mapping Options](../search/type-mapping-options.md#field).
  4. In the **Optimized for** list, choose whether the Search Service should optimize Search queries for accuracy (**recall**) or speed (**latency**).  
  For more information, see [Field Type Mapping Options](../search/type-mapping-options.md#field).
  5. Select **Include in search results**.
9. Click **Add To Index**.
10. (Optional) Add additional collections or child field type mappings to your index.  
For example, you could add the text field that you used to generate your vector embeddings. For more information, see [Add Type Mappings and Mappings](../search/create-search-index-ui.md#add-mapping).
11. Click **Create Index**.

### [](#example)Example: Creating a Search Vector Index for Vector Search Query Examples

If you want to use the sample dataset for the examples in [Run a Vector Search with the Capella UI](run-vector-search-ui.md) and [Run a Vector Search with a Couchbase SDK](run-vector-search-sdk.md), then you can [import](../search/import-search-index.md) the following Search index definition into Capella UI:

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
      "scoring_model": "bm25",
      "store_dynamic": false,
      "type_field": "_type",
      "types": {
       "color.rgb": {
        "dynamic": false,
        "enabled": true,
        "properties": {
         "description": {
          "enabled": true,
          "dynamic": false,
          "fields": [
           {
            "name": "description",
            "type": "text",
            "store": true,
            "index": true,
            "include_term_vectors": true,
            "include_in_all": false,
            "docvalues": true
           }
          ]
         },
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
    "sourceName": "color-vector-sample",
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

This Search Vector Index has a type mapping for a `color.rgb` collection and includes the following fields:

* The **brightness number** field, which is included in search results and supports sorting and faceting.
* The **color string** and **description string** fields, which are included in search results, support highlighting, phrase matching, and sorting and faceting.
* The **colorvect\_l2 \[ number \]** field, which has a Dimension of `3` and uses the **l2\_norm** Similarity Metric.
* The **embedding\_vector\_dot \[ number \]** field, which has a dimension of `1536` and uses the **dot\_product** Similarity Metric.

## [](#next-steps)Next Steps

This basic Search Vector Index includes the vector embeddings from the child field you specified in your type mapping. If you chose to add additional child fields and enabled **Include in search results**, the Search Service can also return data from those fields when you run a Vector Search query.

For example, if you used the Vector Search sample data, you might want to add another child field for the **color** string field to your Search Vector Index, to return color names with your Search query. For more information about how to add additional child fields to your index, see [Add Type Mappings and Mappings](../search/create-search-index-ui.md#add-mapping).

You can customize your Search Vector Index like any other Search index to add additional data and improve search results. For more information about how to customize an index, see [Search Index Features](../search/customize-index.md).

> [!CAUTION]
> Some Search index features are only available in Advanced Mode. If you edit your Search index in Advanced Mode, you cannot make any additional edits in Quick Mode without losing all Advanced Mode settings.

For more information about how to run a search against a Search Vector Index, see [Run a Vector Search with the Capella UI](run-vector-search-ui.md).