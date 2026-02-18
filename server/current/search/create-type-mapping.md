---
title: Create a Type Mapping
description: Create a type mapping with the Couchbase Server Web Console to
  control what documents are included or excluded from a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/create-type-mapping.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/search/create-type-mapping.html)

# Create a Type Mapping

> Create a type mapping with the Couchbase Server Web Console to control what documents are included or excluded from a Search index. For more information, see [Collection Mappings](about-mappings.md#collections). 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To create a type mapping with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the index where you want to create a type mapping.
3. Click **Edit**.
4. Expand **Customize Index** **Mappings**.
5. Click **Add Type Mapping**.
6. Do one of the following:

  1. If you selected **Use non-default scope/collection(s)**, in the **Collection** list, select the collection where you want to create the type mapping.
  2. If you cleared **Use non-default scope/collection(s)**, in the **#** field, enter the name of a type field where you want to create a type mapping.
7. (Optional) To only include documents from a collection based on a specific filter, add the name of the filter or the filter value to the end of the collection in the **#** field.  
For example, `inventory.hotel.free_breakfast_true` or `inventory.hotel.hotel`.  
For more information, see [Set the Type Identifier for a Search Index](set-type-identifier.md).
8. (Optional) To use a specific analyzer for documents in the type mapping, in the **Analyzer** list, select an analyzer.  
You can [use a default analyzer](default-analyzers-reference.md) or [create your own](create-custom-analyzer.md).
9. (Optional) To switch from a [dynamic type mapping](about-mappings.md#dynamic) to a [static type mapping](about-mappings.md#static), select **Only index specified fields**.

  1. To choose which fields to add or remove from the static type mapping, see [Create a Child Field](create-child-field.md).
  2. To add a child mapping for a document field that contains a JSON object, see [Create a Child Mapping](create-child-mapping.md).
10. (Optional) To remove all documents that match the type mapping from your Search index, clear the checkbox for that type mapping.  
By leaving the checkbox selected, all matching documents will be included in the Search index.
11. Click **OK**.

## [](#next-steps)Next Steps

After you create a static type mapping, you can [Create a Child Field](create-child-field.md) to add or remove specific document fields from your Search index.

To add an extra filter to the documents selected by your type mapping, you can also [Set the Type Identifier for a Search Index](set-type-identifier.md).

If you have a document field that contains a JSON object, [Create a Child Mapping](create-child-mapping.md) for that field.

To continue customizing your Search index, you can:

* [Set the Type Identifier for a Search Index](set-type-identifier.md)
* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Wordlist](create-custom-wordlist.md)
* [Set Search Index Advanced Settings](set-advanced-settings.md)
* [Add Synonyms to a Search Index](synonyms/synonyms-search.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).