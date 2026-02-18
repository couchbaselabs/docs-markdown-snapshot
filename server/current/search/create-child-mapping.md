---
title: Create a Child Mapping
description: Create a child mapping with the Couchbase Server Web Console to add
  or remove a field that contains a JSON object from a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/create-child-mapping.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/search/create-child-mapping.html)

# Create a Child Mapping

> Create a child mapping with the Couchbase Server Web Console to add or remove a field that contains a JSON object from a Search index. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You have created a type mapping. For more information about how to create a type mapping on an index, see [Create a Type Mapping](create-type-mapping.md).
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To create a child mapping with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the index where you want to create a child mapping.
3. Click **Edit**.
4. Expand **Customize Index** **Mappings**.
5. Point to an existing mapping and click **+**.
6. Click **insert child mapping**.
7. In the **{}** field, enter the name of a field in a document that contains a JSON object.
8. (Optional) To only index the fields you add to the child mapping, select **only index specified fields**.  
Otherwise, your child mapping is a [dynamic mapping](about-mappings.md#dynamic) that includes all child fields of the JSON object.
9. (Optional) To set a different analyzer for the child mapping, in the **Analyzer** list, select an analyzer.  
You can select a [default analyzer](default-analyzers-reference.md) or [create your own](create-custom-analyzer.md).
10. Click **OK**.

## [](#next-steps)Next Steps

After you create a child mapping, you can choose to add or remove fields in the JSON object from your Search index.

Both child mappings and type mappings use child fields to add and remove fields from a Search index.

For more information about how to add or remove fields from a mapping, see [Create a Child Field](create-child-field.md).

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