---
title: Set the Type Identifier for a Search Index
description: Use a type identifier with a type mapping to add an extra filter to
  the documents you want to include in a Search index.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/set-type-identifier.adoc
  xref: xref:server:search:set-type-identifier.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/search/set-type-identifier.html)

# Set the Type Identifier for a Search Index

> Use a type identifier with a type mapping to add an extra filter to the documents you want to include in a Search index. 

For example, if you added a filter to your type mapping that checked if the value of a field was `true`, only documents with the value `true` for that field would be included in your Search index under that type mapping. Based on your settings, [child fields](create-child-field.md) or [child mappings](create-child-mapping.md) that you define for documents that pass the filter on this type mapping will be returned in search results.

You can filter based on the value of a field, or part of the value of your document IDs.

As of Couchbase Server version 8.0, you can filter documents with custom filters based on the value of:

* [A boolean field](search-index-params.md#boolean%5Ffilter).
* [A date field, within a specific range](search-index-params.md#date%5Frange%5Ffilter).
* [A numeric field, within a specific range](search-index-params.md#numeric%5Frange%5Ffilter).
* [A term in a text field](search-index-params.md#term%5Ffilter).
* A [conjunct](search-index-params.md#conjunct%5Ffilter) or [disjunct](search-index-params.md#disjunct%5Ffilter) object that combines 2 or more of the available filters.

You can add up to a maximum of 100 custom document filters on a single Search index.

For more information about type identifiers and type mappings, see [Customize a Search Index with the Web Console](customize-index.md#type-identifiers).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
* You have created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You have created at least one type mapping in your Search index. For more information, see [Create a Type Mapping](create-type-mapping.md).
* Your user account has the [Search Admin](../learn/security/roles.md#search-admin) role for the bucket where you want to edit an index.
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To set a type identifier for a Search index with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the index where you want to set a type identifier.
3. Click **Edit**.
4. Expand **Type Identifier**.
5. Do one of the following:

  1. [Create a JSON Type Field Type Identifier](#json-type)
  2. [Create a Doc ID Up To Separator Type Identifier](#doc-id-sep)
  3. [Create a Doc ID with Regex Type Identifier](#doc-id-regex)
  4. (Couchbase Server version 8.0 and later) [Create a Custom Document Filter Type Identifier](#custom)

> [!WARNING]
> You cannot use custom document filters with another type of type identifier on your Search index. If you select an option other than **Custom** after you have defined custom document filters, you'll lose any defined custom filters on your Search index.

### [](#json-type)Create a JSON Type Field Type Identifier

To only add documents to your Search index that contain a specific field with a specified string value:

1. Select **JSON type field**.
2. In the **JSON Type Field** field, enter the name of the field in your documents that you want to use to filter documents in your Search index.  
For example, if your documents include a `type` field, you could enter `type` in the **JSON Type Field** field.  
> [!NOTE]  
> You cannot use a field as a type identifier if the field name contains a period (.).
3. Under **Type Mappings**, next to the type mapping where you want to add the type identifier, click **Edit**.
4. In the **#** field, add a period (.) to the end of the current type mapping name.
5. After the period, add the exact string from the document field that you want to use as a filter.  
For example, if you wanted your type mapping to only include documents that had a value of `hotel` in the `type` field, you could enter `scope.collection.hotel` in the type mapping **#** field.
6. Click **OK**.
7. Click **Update Index**.

### [](#doc-id-sep)Create a Doc ID Up To Separator Type Identifier

To only add documents to your Search index that have IDs that match a specified prefix:

1. Select **Doc ID up to Separator**.
2. In the **Doc ID up to Separator** field, enter the ID prefix, up to the separator character, that you want to use to filter documents in your Search index.  
For example, if you know all of your document ID values are prefixed by a string and an underscore (\_), enter `_`.
3. Under **Type Mappings**, next to the type mapping where you want to add the type identifier, click **Edit**.
4. In the **#** field, add a period (.) to the end of the current type mapping name.
5. After the period, add the exact prefix from the document's ID value that you want to use as a filter.  
For example, if you wanted your type mapping to only include documents that have an prefix of `landmark_` in their ID values, you could enter `scope.collection.landmark` in the type mapping **#** field.
6. Click **OK**.
7. Click **Update Index**.

### [](#doc-id-regex)Create a Doc ID with Regex Type Identifier

To only add documents to your Search index that have IDs that match a specified [RE2](https://github.com/google/re2/wiki/Syntax) regular expression:

1. Select **Doc ID with Regex**.
2. In the **Doc ID with Regex** field, enter the regular expression that you want to use to filter documents in your Search index.  
For example, if you wanted only documents with ID values that contained `_40`, you could enter `_[3-5]0` as your regular expression.
3. Under **Type Mappings**, next to the type mapping where you want to add the type identifier, click **Edit**.
4. In the **#** field, add a period (.) to the end of the current type mapping name.
5. After the period, add a match for the regular expression from the document's ID value that you want to use as a filter.  
For example, if you wanted your type mapping to only include documents with ID values that contained `_40`, you could enter `scope.collection._40` in the type mapping **#** field.
6. Click **OK**.
7. Click **Update Index**.

### [](#custom)Create a Custom Document Filter Type Identifier

Couchbase Server 8.0

To create a new custom document filter on a Search index with the Couchbase Server Web Console:

1. Select **Custom**.
2. Click **\+ Add Document Filter**.
3. In the **Type** field, enter a name for your new document filter.
4. In the **Filter** code editor, enter a JSON object to define your document filter.  
For more information about the properties for each document filter type, see:

  * [Boolean Document Filters](search-index-params.md#boolean%5Ffilter)
  * [Date Range Document Filters](search-index-params.md#date%5Frange%5Ffilter)
  * [Numeric Range Document Filters](search-index-params.md#numeric%5Frange%5Ffilter)
  * [Term Document Filters](search-index-params.md#term%5Ffilter)
  * [Conjunct Document Filters](search-index-params.md#conjunct%5Ffilter)
  * [Disjunct Document Filters](search-index-params.md#disjunct%5Ffilter)  
  > [!TIP]  
  > Do not add the name of your document filter to your filter definition when defining a custom document filter through the Server Web Console. Define the document filter as an unnamed object with the specific properties you need for your document filter type.
5. Click **Save**.
6. Under **Type Mappings**, next to the type mapping where you want to add the type identifier, click **Edit**.
7. In the **#** field, add a period (.) to the end of the current type mapping name.
8. After the period, enter the name of the custom document filter that you want to use to filter documents on this type mapping.  
For example, if you defined a custom document filter named `free_breakfast_true`, enter `scope.collection.free_breakfast_true` in the type mapping **#** field.
9. Click **OK**.
10. Click **Update Index**.

## [](#next-steps)Next Steps

After you set the type identifier for your Search index, you can continue to customize your Search index:

* [Create a Type Mapping](create-type-mapping.md)
* [Create a Child Field](create-child-field.md)
* [Create a Child Mapping](create-child-mapping.md)
* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Wordlist](create-custom-wordlist.md)
* [Set Search Index Advanced Settings](set-advanced-settings.md)
* [Add Synonyms to a Search Index](synonyms/synonyms-search.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).