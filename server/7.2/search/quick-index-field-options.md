---
title: Quick Index Field Options
description: When you create a Search index with the Quick Editor, you must set
  options for each field you add to the index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/quick-index-field-options.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/search/quick-index-field-options.html)

# Quick Index Field Options

> When you create a Search index with the Quick Editor, you must set options for each field you add to the index. 

For more information about how to create a Search index with the Quick Editor, see [Create a Search Index with the Quick Editor](create-quick-index.md).

The following options are available for fields in the Quick Editor:

| Option                                        | Description                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Index this field as an identifier (Text Only) | To use the field to set the document’s type in the index, select **Index this field as an identifier**. To not use the field as the document’s type, clear **Index this field as an identifier**.                                                                                                                                           |
| Language (Text Only)                          | Select the language for the content inside a text field. The Search Service automatically applies an [analyzer](customize-index.md#analyzers) to the field’s contents based on the selected language. For more information about the available language options, see [Quick Index Supported Languages](quick-index-supported-languages.md). |
| Include in search results                     | To include content from the field in search results, select **Include in search results**. To exclude the field’s content from search results, clear **Include in search results**.                                                                                                                                                         |
| Support highlighting                          | The Search Service can highlight matching search terms in search results from an index. To enable highlighting in search results, select **Support highlighting**. To turn off highlighting in search results, clear **Support highlighting**. To enable **Support highlighting**, you must also enable **Include in search results**.      |
| Support phrase matching                       | To support searches for whole phrases, select **Support phrase matching**. To turn off phrase matching, clear **Support phrase matching**.                                                                                                                                                                                                  |
| Support field agnostic search                 | To search the field’s contents without specifying the field name in a search query, select **Support field agnostic search**. To turn off field agnostic search, clear **Support field agnostic search**.                                                                                                                                   |
| Support sorting and faceting                  | To sort search results and use [facets](search-request-params.md#facets) with the field’s contents, select **Support sorting and faceting**. To turn off sorting and facets, clear **Support sorting and faceting**.                                                                                                                        |
| Searchable As                                 | Set a different name that you can use to search the field’s contents in a query. The default value is the field’s name.                                                                                                                                                                                                                     |