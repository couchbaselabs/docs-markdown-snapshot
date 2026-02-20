---
title: Create a Type Mapping
description: Create a type mapping with the Couchbase Server Web Console to
  control what documents are included or excluded from a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/create-type-mapping.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:search:create-type-mapping.adoc[]
---

[View original HTML](/server/7.2/search/create-type-mapping.html)

# Create a Type Mapping

> Create a type mapping with the Couchbase Server Web Console to control what documents are included or excluded from a Search index. For more information, see [Customize a Search Index with the Web Console](customize-index.md#type-mappings). 

## [](#prerequisites)Prerequisites

* You’ve created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You’ve logged in to the Couchbase Server Web Console.

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
7. (Optional) To only include documents of a specific type from a collection, in the **#** field, add the document type to the end of the collection.  
For example, `scope.collection.document_type`.
8. (Optional) To use a specific analyzer for documents in the type mapping, in the **Analyzer** list, select an analyzer.  
You can [use a default analyzer](default-analyzers-reference.md) or [create your own](create-custom-analyzer.md).
9. (Optional) To switch from a [dynamic type mapping to a static type mapping](customize-index.md#type-mappings), select **Only index specified fields**.

  1. To choose which fields to add or remove from the static type mapping, see [Create a Child Field](create-child-field.md).
10. (Optional) To add a child type mapping for a document field that contains a JSON object, see [Create a Child Mapping](create-child-mapping.md).
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

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).