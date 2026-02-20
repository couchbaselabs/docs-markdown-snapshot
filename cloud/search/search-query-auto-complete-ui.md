---
title: Configure an Autocomplete Search Index
description: Create a Search index with the Capella UI or import a JSON Search
  index payload to start using autocomplete with the Search Service.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/search-query-auto-complete-ui.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:search:search-query-auto-complete-ui.adoc[]
---

[View original HTML](/cloud/search/search-query-auto-complete-ui.html)

# Configure an Autocomplete Search Index

> Create a Search index with the Capella UI or import a JSON Search index payload to start using autocomplete with the Search Service. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have a bucket with scopes and collections in your operational cluster. For more information, see [Manage Buckets](../clusters/data-service/manage-buckets.md).
* You have logged in to the Couchbase Capella UI.

## [](#procedure)Procedure

You can create a compatible Search index with the [Capella UI in Advanced Mode](#ui) or [import a JSON payload](#import).

### [](#ui)Create an Autocomplete Search Index Manually with the Capella UI

To create the Search index in the Capella UI with Advanced Mode:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with the Search Service.
3. Go to **Data Tools** **Search**.
4. Click **Create Search Index**.
5. Click **Enable Advanced Options**.
6. In the **Index Name** field, enter a name for the Search index.  
> [!NOTE]  
> Your index name must start with an alphabetic character (a-z or A-Z). It can only contain alphanumeric characters (a-z, A-Z, or 0-9), hyphens (-), or underscores (\_).  
>  
> For Couchbase Server version 7.6 and later, your index name must be unique inside your selected bucket and scope. You cannot have 2 indexes with the same name inside the same bucket and scope.
7. In the **Bucket**, **Scope**, and **Collection** lists, choose the bucket and scope where you want to create your Search index, and the collections you want to include.
8. [Create a Custom Analyzer](create-custom-analyzer.md) with the following settings:

  1. In the **Name** field, enter `keyword_to_lower`.
  2. In the **Tokenizer** list, select **single**.
  3. In the **Token Filters** list, select and add the **to\_lower** token filter.
9. [Create another custom analyzer](create-custom-analyzer.md) with the following settings:

  1. In the **Name** field, enter `edge_ngram`.
  2. In the **Tokenizer** list, select **unicode**.
  3. [Create a custom token filter](create-custom-token-filter.md#edge-ngram) with the following settings:

    1. In the **Name** field, enter `edge_ngram_2_8`.
    2. In the **Type** list, select **edge\_ngram**.
    3. In the **Min** box, enter `2`, or the minimum number of characters you want the Search index to use for autocomplete.
    4. In the **Max** box, enter `8`, or the maximum number of characters you want the Search index to use for autocomplete.
  4. In the **Token Filters** list for your custom analyzer, click both the **to\_lower** and your custom **edge\_ngram\_2\_8** token filter.
10. [Set your default analyzer](create-search-index-ui.md#configure-settings) to your custom **keyword\_to\_lower** analyzer.
11. Under **Type Mappings**, in your document schema, click the name of a field that contains the data you want to search.
12. Configure the field:

  1. In the **Analyzer/Language** list, select your **edge\_ngram** analyzer.
  2. Select **Include in search results**.
  3. Select **Support field agnostic search**.
13. Click **Create Index**.

### [](#import)Import a Search Index Payload

1. [Import a Search Index Definition with the Capella UI](import-search-index.md) with the following JSON payload, replacing all placeholder values that start with a `$`:  
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
        "scoring_model": "tf-idf",  
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