---
title: Create an XATTRs Mapping
description: Use the Server Web Console to create a mapping for Extended
  Attributes (XATTRs) and search for them with the Search Service, on Couchbase
  Server version 7.6.2 and later.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/create-xattrs-mapping.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/search/create-xattrs-mapping.html)

# Create an XATTRs Mapping

> Use the Server Web Console to create a mapping for Extended Attributes (XATTRs) and search for them with the Search Service, on Couchbase Server version 7.6.2 and later. 

You must add an XATTRs mapping to your Search index to use and search for XATTRs metadata in your documents.

## [](#prerequisites)Prerequisites

* Your cluster is running Couchbase Server version 7.6.2 or later.
* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../../current/manage/manage-nodes/node-management-overview.md).
* You have created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You have created a type mapping for a collection. For more information about how to create a type mapping on an index, see [Create a Type Mapping](create-type-mapping.md).
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To add an XATTRs mapping to your Search index from the Server Web Console:

1. Go to **Search**.
2. Click the index where you want to create an XATTRs mapping.
3. Click **Edit**.
4. Expand **Customize Index** **Mappings**.
5. Point to an existing collection type mapping and click **+**.
6. Click **insert xattrs mapping**.
7. (Optional) To only index the fields you add to the XATTRs mapping, select **only index specified fields**.  
Otherwise, your XATTRs mapping is a [dynamic mapping](customize-index.md#type-mappings) that includes all child fields from your documents' metadata.
8. (Optional) To set a different analyzer for the XATTRs mapping, in the **Analyzer** list, select an analyzer.  
You can select a [default analyzer](default-analyzers-reference.md) or [create your own](create-custom-analyzer.md).
9. Click **OK**.

## [](#next-steps)Next Steps

After you create a XATTRs mapping, you can choose to add or remove fields in your document metadata from your Search index.

XATTRs mappings, child mappings, and type mappings use child fields to add and remove fields from a Search index.

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

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).