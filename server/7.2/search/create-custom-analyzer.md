---
title: Create a Custom Analyzer
description: Create a custom analyzer with the Couchbase Server Web Console to
  modify the input text from a Search query or Search index and improve search
  results.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/create-custom-analyzer.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/search/create-custom-analyzer.html)

# Create a Custom Analyzer

> Create a custom analyzer with the Couchbase Server Web Console to modify the input text from a Search query or Search index and improve search results. 

## [](#prerequisites)Prerequisites

* You’ve created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* You’ve logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To create a custom analyzer with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the Search index where you want to create a custom analyzer.
3. Click **Edit**.
4. Expand **Customize Index** **Analyzers**.
5. Click **Add Analyzer**.
6. In the **Name** field, enter a name for the new custom analyzer.
7. To remove specific characters from search input before tokenizing, in the **Character Filters** list, do one of the following:

  1. To add a character filter to your analyzer, select a character filter and click **\+ Add**. You can select a default character filter or create your own.  
  For more information, see [Default Character Filters](default-character-filters-reference.md) or [Create a Custom Character Filter](create-custom-character-filter.md).
  2. To remove a character filter from your analyzer, click **remove**.
8. In the **Tokenizer** list, click the tokenizer you want to use to create tokens from Search input. You can select a default tokenizer or create your own.  
For more information, see [Default Tokenizers](default-tokenizers-reference.md) or [Create a Custom Tokenizer](create-custom-tokenizer.md).
9. To modify the tokens created by the tokenizer, in the **Token Filters** list, do one of the following:

  1. To add a token filter to your analyzer, select a token filter and click **\+ Add**. You can select a default token filter or create your own.  
  For more information, see [Default Token Filters](default-token-filters-reference.md) or [Create a Custom Token Filter](create-custom-token-filter.md).
  2. To remove a token filter from your analyzer, click **remove**.
10. Click **Save**.

## [](#next-steps)Next Steps

After you create a custom analyzer, you can [set it as the default analyzer](set-advanced-settings.md#default-analyzer) for your Search index.

You can also use the custom analyzer when you [Create a Type Mapping](create-type-mapping.md), [Create a Child Mapping](create-child-mapping.md), and [Create a Child Field](create-child-field.md).

To continue customizing your Search index, you can also:

* [Set the Type Identifier for a Search Index](set-type-identifier.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Create a Custom Wordlist](create-custom-wordlist.md)
* [Set Search Index Advanced Settings](set-advanced-settings.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).