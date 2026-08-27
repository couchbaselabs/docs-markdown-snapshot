---
title: Create a Custom Wordlist
description: Create a custom wordlist with the Couchbase Server Web Console to
  use with a custom token filter.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/create-custom-wordlist.adoc
  xref: xref:7.6@server:search:create-custom-wordlist.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/search/create-custom-wordlist.html)

# Create a Custom Wordlist

> Create a custom wordlist with the Couchbase Server Web Console to use with a custom token filter. 

A custom wordlist gives greater control over the input you want to remove from [tokenizer](customize-index.md#tokenizers) results.

For more information about how to create a custom token filter, see [Create a Custom Token Filter](create-custom-token-filter.md).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../../current/manage/manage-nodes/node-management-overview.md).
* You have created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To create a custom wordlist with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the Search index where you want to create a custom wordlist.
3. Click **Edit**.
4. Expand **Customize Index** **Custom Filters**.
5. Click **Add Wordlist**.
6. In the **Name** field, enter a name for the wordlist.
7. In the **Word to be added** field, enter a word you want to add to the wordlist.
8. To add the word to the list, do one of the following:

  1. Click **Add**.
  2. Press Enter.
9. (Optional) To add more words to the wordlist, repeat the previous steps.
10. Click **Save**.

## [](#next-steps)Next Steps

After you create a custom wordlist, you can use it with [a custom token filter](create-custom-token-filter.md).

To continue customizing your Search index, you can also:

* [Set the Type Identifier for a Search Index](set-type-identifier.md)
* [Create a Type Mapping](create-type-mapping.md)
* [Create a Child Field](create-child-field.md)
* [Create a Child Mapping](create-child-mapping.md)
* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Set Search Index Advanced Settings](set-advanced-settings.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).