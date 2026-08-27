---
title: Create a Custom Analyzer
description: Create a custom analyzer with the Couchbase Capella UI's Advanced
  Mode to modify the input text from a Search query or Search index and improve
  search results.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/create-custom-analyzer.adoc
  xref: xref:cloud:search:create-custom-analyzer.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/search/create-custom-analyzer.html)

# Create a Custom Analyzer

> Create a custom analyzer with the Couchbase Capella UI's Advanced Mode to modify the input text from a Search query or Search index and improve search results. For more information, see [Search Index Features](customize-index.md#analyzers). 

> [!NOTE]
> You must use Advanced Mode to add a custom analyzer to your Search index. For more information, see [Advanced Mode Editing](create-search-indexes.md#advanced-mode).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have logged in to the Couchbase Capella UI.

## [](#procedure)Procedure

To create a custom analyzer with the Capella UI in Advanced Mode:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with the Search Service.
3. Go to **Data Tools** **Search**.
4. Do one of the following:

  1. To work with an existing Search index, click the name of the index where you want to create a custom analyzer.
  2. To create a new Search index, click **Create Search Index**.
5. Make sure to select **Enable Advanced Options**.
6. Expand **Global Index Settings**.
7. Click **Add Custom Analyzer**.
8. In the **Analyzer Name** field, enter a name for the new custom analyzer.
9. [Configure the components of your analyzer](#configure-components).
10. Click **Add Custom Analyzer**.

### [](#configure-analyzer-components)Configure Analyzer Components

For more information about analyzers and their components, see [Analyzers](customize-index.md#analyzers).

Add the following components to a custom analyzer to take input text from a document or Search query and convert it into tokens:

1. [Tokenizers](#tokenizers)
2. [Character Filters](#character-filters)
3. [Token Filters](#token-filters)

#### [](#tokenizers)Configure Tokenizers

For more information about tokenizers, see [Tokenizers](customize-index.md#tokenizers).

To configure the tokenizer for a custom analyzer:

1. (Optional) Create a custom tokenizer. For more information, see [Create a Custom Tokenizer](create-custom-tokenizer.md).
2. In the **Tokenizer** list, select a tokenizer to use in your custom analyzer. You can choose your custom tokenizer or [use a default tokenizer](default-tokenizers-reference.md).

#### [](#character-filters)Configure Character Filters

For more information about character filters, see [Character Filters](customize-index.md#character-filters).

To add a character filter or character filters to a custom analyzer:

1. (Optional) Create 1 or more custom character filters. For more information, see [Create a Custom Character Filter](create-custom-character-filter.md).
2. In the **Character Filters** list, select 1 or more character filters to use in your custom analyzer. You can choose your custom character filter or [use the default character filters](default-character-filters-reference.md).

Remove a character filter from your custom analyzer by clicking the **x** next to a listed filter.

#### [](#token-filters)Configure Token Filters

For more information about token filters, see [Token Filters](customize-index.md#token-filters).

To add a token filter or token filters to a custom analyzer:

1. (Optional) Create 1 or more custom token filters. For more information, see [Create a Custom Token Filter](create-custom-token-filter.md).
2. In the **Token Filters** list, select 1 or more token filters to use in your custom analyzer. You can choose your custom token filter or [use the default token filters](default-token-filters-reference.md).

Remove a token filter from your custom analyzer by clicking the **x** next to a listed filter.

## [](#next-steps)Next Steps

After you create a custom analyzer, you can [set it as the default analyzer](set-advanced-settings.md#default-analyzer) for your Search index.

You can also use the custom analyzer when you create a type mapping or mapping while you [Create a Search Index with the Capella UI](create-search-index-ui.md).

To continue customizing your Search index, you can also:

* [Set a Document Filter](set-type-identifier.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Add Synonyms to a Search Index](synonyms/synonyms-search.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Capella UI](simple-search-ui.md).