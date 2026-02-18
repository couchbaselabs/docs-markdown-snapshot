---
title: Create a Child Field
description: Create a child field with the Couchbase Server Web Console to add
  or remove a specific field's content from a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/create-child-field.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/search/create-child-field.html)

# Create a Child Field

> Create a child field with the Couchbase Server Web Console to add or remove a specific field’s content from a Search index. 

## [](#prerequisites)Prerequisites

* You’ve created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You’ve created a type mapping. For more information about how to create a type mapping on an index, see [Create a Type Mapping](create-type-mapping.md).
* You’ve logged in to the Couchbase Server Web Console.

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
> The field must contain either a single value or an array. If the field contains a JSON object, [Create a Child Mapping](create-child-mapping.md), instead.
8. In the **Type** list, select the data type for the field.  
For more information about the available data types, see [Field Data Types](field-data-types-reference.md).
9. Configure optional settings for the child field:

| Option                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Searchable As          | Set a different name that you can use to search the field’s contents in a query. The default value is the value set in **Field**.                                                                                                                                                                                                                                                                                                              |
| Analyzer               | Choose an analyzer for the content in the child field. You can choose a default analyzer or a custom analyzer. For more information about the available default analyzers, see [Default Analyzers](default-analyzers-reference.md). For more information about how to create a custom analyzer, see [Create a Custom Analyzer](create-custom-analyzer.md).                                                                                     |
| Index                  | To include the child field in the index, select **Index**. To remove the child field from the index, clear **Index**.                                                                                                                                                                                                                                                                                                                          |
| Store                  | To store the values from the field in the index and return them in search results, select **Store**. This increases your index’s size and indexing time. To remove the field’s values from the index, clear **Store**.                                                                                                                                                                                                                         |
| Include in \_all field | The \_all field is a composite field that has the content from multiple fields in an index. It allows searches to query the content of a field without specifying the field’s name. To include this field in the \_all field, select **Include in \_all field**. To exclude this field from the \_all field, clear **Include in \_all field**. To change the name of the \_all field, see [Default Field](set-advanced-settings.md#all-field). |
| Include Term Vectors   | Term vectors store the location of terms in a field for an index. You can use term vectors to highlighting matching search terms in search results, and perform phrase searches. Term vectors increase your index’s size and indexing time. To enable term vectors for this field, select **Include Term Vectors**. To turn off term vectors, clear **Include Term Vectors**. To enable term vectors, you must also enable [Store](#store).    |
| Doc Values             | Doc values are the value for each instance of the field in an index. Use doc values for Search [Facets](search-request-params.md#facets) and sorting search results. To store doc values, select **Doc Values**. To exclude doc values from the index, clear **Doc Values**.                                                                                                                                                                   |
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

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).