---
title: Create a Child Field
description: Create a child field with the Couchbase Server Web Console to add
  or remove a specific field's content from a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/create-child-field.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/search/create-child-field.html)

# Create a Child Field

> Create a child field with the Couchbase Server Web Console to add or remove a specific field’s content from a Search index. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You have created a type mapping. For more information about how to create a type mapping on an index, see [Create a Type Mapping](create-type-mapping.md).
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To add or remove a child field from a Search index with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the index where you want to create a child field.
3. Click **Edit**.
4. Expand **Customize Index** **Mappings**.
5. Point to an existing mapping and click **+**.
6. Click **insert child field**.
7. In the **Field** field, enter the name of a field in your documents that you want to add or remove from the index.  
> [!NOTE]  
> The field must contain either a single value or an array. If the field contains a JSON object, [create a child mapping](create-child-mapping.md) instead. Field names must not contain periods (`.`).
8. In the **Type** list, select the data type for the field.  
For more information about the available data types, see [Field Data Types](field-data-types-reference.md).
9. Configure optional settings for the child field.  
For more information about the available settings for child fields, see [Child Field Options](child-field-options-reference.md).
10. Click **OK**.

## [](#next-steps)Next Steps

You can continue to create child fields to add or remove the contents of a document from your Search index.

If a field in your documents contains a JSON object, [Create a Child Mapping](create-child-mapping.md), instead.

To continue customizing your Search index, you can also:

* [Set the Type Identifier for a Search Index](set-type-identifier.md)
* [Create a Type Mapping](create-type-mapping.md)
* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Create a Custom Wordlist](create-custom-wordlist.md)
* [Set Search Index Advanced Settings](set-advanced-settings.md)
* [Add Synonyms to a Search Index](synonyms/synonyms-search.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).