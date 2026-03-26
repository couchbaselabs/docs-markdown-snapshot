---
title: Import a Search Index Definition with the Capella UI
description: Use the Couchbase Capella UI to import a JSON Search index definition.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/import-search-index.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cloud:search:import-search-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/search/import-search-index.html)

# Import a Search Index Definition with the Capella UI

> Use the Couchbase Capella UI to import a JSON Search index definition. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have a bucket with scopes and collections in your operational cluster. For more information, see [Manage Buckets](../clusters/data-service/manage-buckets.md).
* You have a Search index definition saved as a JSON file. For more information about the properties you can include in a Search index definition, see [Search Index JSON Properties](search-index-params.md).  
> [!NOTE]  
> Your JSON file must be smaller than 40 MB.
* You have logged in to the Couchbase Capella UI.

## [](#import-a-search-index-definition)Import a Search Index Definition

To import a full [Search index definition](search-index-params.md) with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Operational**.
  * Click your current project name or search for a project and go to **Operational**.
  * Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with the Search Service.
3. Go to **Data Tools** **Search**.
4. Click **Import Search Index**.
5. Upload a JSON file that contains your Search index definition.  
For example:  
```json  
{  
    "type": "fulltext-index",  
    "name": "travel-sample.inventory.travel-index",  
    "uuid": "2c4b22c60b59c524",  
    "sourceType": "gocbcore",  
    "sourceName": "travel-sample",  
    "sourceUUID": "76a82f1f3471d9fae3b483f9ee75459d",  
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
          "dynamic": false,  
          "enabled": false  
        },  
        "default_type": "_default",  
        "docvalues_dynamic": false,  
        "index_dynamic": false,  
        "store_dynamic": false,  
        "type_field": "_type",  
        "types": {  
          "inventory.airline": {  
            "dynamic": false,  
            "enabled": true,  
            "properties": {}  
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
6. Close the **Index Definition** panel.
7. (Optional) Make changes to your Search index settings.  
For more information, see [Create a Search Index with the Capella UI](create-search-index-ui.md).
8. Click **Create Index**.

## [](#import-a-search-index-alias-definition)Import a Search Index Alias Definition

To import a [Search alias](index-aliases.md) with the Capella UI:

1. On the **Operational Clusters** page, select the operational cluster where you want to import a JSON Search index alias.
2. Go to **Data Tools** **Search**.
3. Click **Create Search Alias**.
4. Click **Alias Definition**.
5. Click **Import from File**.
6. Upload a JSON file that contains your Search alias definition.  
For example:  
```json  
{  
    "name": "travel-color-index",  
    "type": "fulltext-alias",  
    "params": {  
      "targets": {  
        "travel-sample.inventory.travel-index": {},  
        "color-vector-sample.color.color-test": {}  
      }  
    },  
    "sourceType": "nil",  
    "sourceName": "",  
    "sourceUUID": "",  
    "sourceParams": null,  
    "planParams": {},  
    "uuid": "",  
    "id": ""  
  }  
```
7. (Optional) Make changes to your Search index alias settings.  
For more information, see [Create a Search Index Alias with the Capella UI](create-search-index-alias.md).
8. Click **Create Alias**.

## [](#next-steps)Next Steps

To add additional features to your imported Search index, see [Search Index Features](customize-index.md).

To run a search with your Search index, see [Run A Simple Search with the Capella UI](simple-search-ui.md).