---
title: Add a Synonym Source
description: Add a Synonym Source to set the collection where your synonym
  documents are stored.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/synonyms/add-synonym-source.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:search:synonyms/add-synonym-source.adoc[]
---

[View original HTML](/cloud/search/synonyms/add-synonym-source.html)

# Add a Synonym Source

> Add a Synonym Source to set the collection where your synonym documents are stored. After you have set the synonym source for your Search index and any child fields, you can run any type of text-based Search query to return results with synonyms. 

For more information about synonym searches with the Search Service, see [Add Synonyms to a Search Index](synonyms-search.md).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../../clusters/modify-database.md).
* You have created an index. For more information, see [Create a Search Index with the Capella UI](../create-search-index-ui.md).
* You have created a type mapping. For more information about how to create a type mapping on an index, see [Create a New Mapping or Type Mapping](../create-type-mapping.md).
* You have created a text child field where you want to run synonym searches. For more information about how to create a child field on an index, see [Create a New Mapping or Type Mapping](../create-type-mapping.md).
* You have logged in to the Couchbase Capella UI.

## [](#procedure)Procedure

To add a synonym source to a Search index with the Capella UI in Advanced Mode:

1. On the **Operational Clusters** page, select the operational cluster where you want to work with the Search Service.
2. Go to **Data Tools** **Search**.
3. Click the name of the index where you want to add synonym support.
4. Make sure to select **Enable Advanced Options**.
5. Click **\+ Add Synonym Source**.
6. In the **Name** field, enter a name for your new synonym source. For example, you could call the source for a collection of English synonyms `synonyms_en`.
7. In the **Collection** list, select the collection where you stored your synonym documents for this specific synonym source.
8. In the **Analyzer** list, select the appropriate analyzer to use with your synonyms. Choose the same analyzer as the text fields where you want to use synonym searches.  
For more information about how to set the analyzer for a child field, see [Field Type Mapping Options](../type-mapping-options.md#field).
9. Click **Save**.
10. Under **Configured Type Mappings**, next to the child field where you want to use your new synonym source, click **Edit**.
11. In the **Synonym Source** list, select the synonym source you added in the previous step.
12. Click **Save**.
13. To finish editing your index, click **Update Index**.

## [](#example-search-index-definition-with-synonyms)Example: Search Index Definition with Synonyms

For example, the following index definition defines a Search index using the `travel-sample` sample dataset. It uses non-default scopes and collections to index the `name`, `description`, and `reviews.content` fields from the `inventory.hotel` collection.

It uses synonyms from the `synonyms_en` synonym source for the `description` and `reviews.content` fields:

```json
{
  "type": "fulltext-index",
  "name": "travel-sample.inventory.travel-sample-index",
  "uuid": "519b7bfa6d2bdeea",
  "sourceType": "gocbcore",
  "sourceName": "travel-sample",
  "sourceUUID": "aa069135219cb1d45923b36ca8239e28",
  "planParams": {
    "maxPartitionsPerPIndex": 128,
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
        "synonym_sources": {
          "synonyms_en": {
            "analyzer": "en",
            "collection": "synonyms"
          }
        }
      },
      "default_analyzer": "en",
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
        "inventory.hotel": {
          "dynamic": false,
          "enabled": true,
          "properties": {
            "description": {
              "dynamic": false,
              "enabled": true,
              "fields": [
                {
                  "analyzer": "en",
                  "docvalues": true,
                  "include_in_all": true,
                  "include_term_vectors": true,
                  "index": true,
                  "name": "description",
                  "store": true,
                  "synonym_source": "synonyms_en",
                  "type": "text"
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
              "default_analyzer": "en",
              "dynamic": false,
              "enabled": true,
              "properties": {
                "content": {
                  "dynamic": false,
                  "enabled": true,
                  "fields": [
                    {
                      "analyzer": "en",
                      "docvalues": true,
                      "include_in_all": true,
                      "include_term_vectors": true,
                      "index": true,
                      "name": "content",
                      "store": true,
                      "synonym_source": "synonyms_en",
                      "type": "text"
                    }
                  ]
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
}
```

> [!TIP]
> To use this index definition on your own cluster, remove the `uuid` parameter and replace the `sourceUUID` parameter with the appropriate UUID for your own `travel-sample` bucket. For more information about how to import a Search index definition, see [Import a Search Index Definition with the Capella UI](../import-search-index.md).

For this example, the `synonyms` collection inside the `travel-sample` bucket has the following 2 synonym documents:

```json
{
  "synonyms": [
    "cheap",
    "inexpensive",
    "affordable",
    "budget-friendly",
    "low-cost",
    "economical"
  ]
}
```

```json
{
  "synonyms": [
    "comfortable",
    "cozy",
    "relaxing",
    "snug",
    "pleasant",
    "restful"
  ]
}
```

With the defined synonym documents and Search index definition, you could run the following Search query with the Capella UI:

```json
{
  "explain": true,
  "fields": [
    "*"
  ],
  "highlight": {
    "style": "html"
  },
  "query": {
    "match": "cheap comfortable",
    "operator": "and",
    "field": "description"
  },
  "size": 40,
  "from": 0
}
```

The query would return results for hotels that include both `cheap` and `comfortable`, or 1 of their defined synonyms, like `affordable` in the `description` field. Results could include `hotel_18843` and `hotel_27821`.

## [](#next-steps)Next Steps

For more information about other features you can add to your Search index, see [Search Index Features](../customize-index.md).