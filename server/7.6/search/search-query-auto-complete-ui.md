---
title: Configure an Autocomplete Search Index
description: Create a Search index with the Couchbase Server Web Console or the
  REST API to start using autocomplete with the Search Service.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/search-query-auto-complete-ui.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/search/search-query-auto-complete-ui.html)

# Configure an Autocomplete Search Index

> Create a Search index with the Couchbase Server Web Console or the REST API to start using autocomplete with the Search Service. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../../current/manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../../current/manage/manage-buckets/create-bucket.md).
* Your user account has the **Search Admin** role for the bucket where you want to create the index.
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

You can create a compatible Search index with the [Web Console](#ui) or the [REST API](#api).

### [](#ui)Create the Autocomplete Search Index with the Web Console

To create the Search index with the Web Console:

1. Go to **Search**.
2. Click **Add Index**.
3. In the **Index Name** field, enter a name for the new index.  
> [!NOTE]  
> Your index name must start with an alphabetic character (a-z or A-Z). It can only contain alphanumeric characters (a-z, A-Z, or 0-9), hyphens (-), or underscores (\_).  
>  
> For Couchbase Server version 7.6 and later, your index name must be unique inside your selected bucket and scope. You cannot have 2 indexes with the same name inside the same bucket and scope.
4. In the **Bucket** list, select the bucket where you want to create the index.
5. Expand **Customize Index**.
6. Select **Use non-default scope/collection(s)**.
7. In the **Scope** list, select the scope where you want to create the index.
8. [Create a Custom Analyzer](create-custom-analyzer.md) with the following settings:

  1. In the **Name** field, enter `keyword_to_lower`.
  2. In the **Tokenizer** list, select **single**.
  3. In the **Token Filters** list, select and add the **to\_lower** token filter.
9. Expand **Custom Filters**.
10. [Create a custom token filter](create-custom-token-filter.md#edge-ngram) with the following settings:

  1. In the **Name** field, enter `edge_ngram_2_8`.
  2. In the **Type** list, select **edge\_ngram**.
  3. In the **Min** field, enter `2`, or the minimum number of characters you want the Search index to use for autocomplete.
  4. In the **Max** field, enter `8`, or the maximum number of characters you want the Search index to use for autocomplete.
11. [Create another custom analyzer](create-custom-analyzer.md) with the following settings:

  1. In the **Name** field, enter `edge_ngram`.
  2. In the **Tokenizer** list, select **unicode**.
  3. In the **Token Filters** list, select and add the **to\_lower** and your custom **edge\_ngram\_2\_8** token filter.
12. Under **Mappings**, clear the **default** type mapping.
13. [Create a Type Mapping](create-type-mapping.md) with the following settings:

  1. Clear **index all contained fields**.
14. (Optional) If the field you want to search with autocomplete is nested inside a JSON object in your documents, [Create a Child Mapping](create-child-mapping.md) for the JSON object with the following settings:

  1. Clear **index all contained fields**.
15. Under the type mapping or child mapping, [Create a Child Field](create-child-field.md) with the following settings:

  1. In the **field** field, enter the name of a text field in a document from your selected scope and collection.
  2. In the **analyzer** list, select your **edge\_ngram** analyzer.
  3. Select **index**.
  4. Select **store**.
  5. Select **include in \_all field**.
16. Expand **Advanced**.
17. In the **Default Analyzer** list, select your **keyword\_to\_lower** analyzer.
18. Click **Create Index**

> [!TIP]
> You can use the generated index definition JSON payload from the UI to create a Search index with the REST API.

### [](#api)Create an Autocomplete Search Index with the REST API

To create an autocomplete Search index from the REST API:

1. [Create a Search Index with the REST API and curl/HTTP](create-search-index-rest-api.md) with the following JSON payload, replacing all placeholder values that start with a `$`:  
```json  
{  
    "type": "fulltext-index",  
    "name": "e-ngram-2-8",  
    "uuid": "$GENERATED_INDEX_UUID",  
    "sourceType": "gocbcore",  
    "sourceName": "$BUCKET_NAME",  
    "sourceUUID": "$BUCKET_UUID",  
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
        "analysis": {  
          "analyzers": {  
            "edge_ngram": {  
              "token_filters": [  
                "to_lower",  
                "edge_ngram_2_8"  
              ],  
              "tokenizer": "unicode",  
              "type": "custom"  
            },  
            "keyword_to_lower": {  
              "token_filters": [  
                "to_lower"  
              ],  
              "tokenizer": "single",  
              "type": "custom"  
            }  
          },  
          "token_filters": {  
            "edge_ngram_2_8": {  
              "back": false,  
              "max": 8,  
              "min": 2,  
              "type": "edge_ngram"  
            }  
          }  
        },  
        "default_analyzer": "keyword_to_lower",  
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
            "dynamic": false,  
            "enabled": true,  
            "properties": {  
              "$FIELD_NAME": {  
                "dynamic": false,  
                "enabled": true,  
                "fields": [  
                  {  
                    "analyzer": "edge_ngram",  
                    "include_in_all": true,  
                    "index": true,  
                    "name": "$FIELD_NAME",  
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
  }  
```

## [](#next-steps)Next Steps

To add an autocomplete feature to your application, see [Add Autocomplete to Your Application](search-query-auto-complete-code.md) for example code.