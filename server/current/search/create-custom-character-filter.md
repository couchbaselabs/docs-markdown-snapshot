---
title: Create a Custom Character Filter
description: Create a custom character filter with the Couchbase Server Web
  Console to remove unwanted characters from a Search query or the contents of a
  Search index.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/create-custom-character-filter.adoc
  xref: xref:server:search:create-custom-character-filter.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/search/create-custom-character-filter.html)

# Create a Custom Character Filter

> Create a custom character filter with the Couchbase Server Web Console to remove unwanted characters from a Search query or the contents of a Search index. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To create a custom character filter with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the Search index where you want to create a custom character filter.
3. Click **Edit**.
4. Expand **Customize Index** **Custom Filters**.
5. Click **Add Character Filter**.
6. In the **Name** field, enter a name for the character filter.
7. In the **Regular Expression** field, enter the regular expression for the character filter.
8. (Optional) In the **Replacement** field, enter a string that replaces any matches for the regular expression.
9. Click **Save**.

## [](#next-steps)Next Steps

After you create a custom character filter, you can use it with [a custom analyzer](create-custom-analyzer.md).

To continue customizing your Search index, you can also:

* [Set the Type Identifier for a Search Index](set-type-identifier.md)
* [Create a Type Mapping](create-type-mapping.md)
* [Create a Child Field](create-child-field.md)
* [Create a Child Mapping](create-child-mapping.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Create a Custom Wordlist](create-custom-wordlist.md)
* [Set Search Index Advanced Settings](set-advanced-settings.md)
* [Add Synonyms to a Search Index](synonyms/synonyms-search.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).