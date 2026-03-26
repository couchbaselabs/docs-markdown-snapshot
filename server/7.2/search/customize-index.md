---
title: Customize a Search Index with the Web Console
description: Configure additional options for a Search index to improve
  performance and fine tune your search results.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/customize-index.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:search:customize-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/search/customize-index.html)

# Customize a Search Index with the Web Console

> Configure additional options for a Search index to improve performance and fine tune your search results. 

You can add the following components and configure the following options for a Search index:

| Option            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type Identifier   | Set a type identifier to add a filter to the documents added to your Search index: JSON Type Field: Selects only documents that contain a specific field with a specified string value. Doc ID up to Separator: Selects only documents with an ID or key up to a specific substring. Doc ID with Regex: Selects only documents with an ID or key that matches a regular expression. For more information about how to configure a type identifier, see [Set the Type Identifier for a Search Index](set-type-identifier.md).                                                                                                                                                                                                                                                                                                                        |
| Mappings          | Use a type mapping to include or exclude specific documents in a scope or collection from an index, based on their type. You can create two types of type mappings: **Dynamic type mappings**: Add all available fields from a matching document type to an index. **Static type mappings**: Add only specific fields from a matching document type to an index. By default, all indexes have a dynamic type mapping that includes all documents from the **\_default** scope and **\_default** collection in a bucket. Add [child fields](create-child-field.md) to a type mapping to create a static type mapping. Child fields set the specific fields from a document that you want to include or exclude from an index. For more information about how to add a type mapping to an index, see [Create a Type Mapping](create-type-mapping.md). |
| Analyzers         | Use analyzers to improve and customize the search results in your index. Analyzers transform input text into tokens, which give you greater control over your index's text matching. You can use one of Couchbase's built-in analyzers or create your own. For more information about how to create a custom analyzer, see [Create a Custom Analyzer](create-custom-analyzer.md). Analyzers have different components that control how text is transformed for search. When you create a custom analyzer, you can choose these components. Both custom and default analyzers can contain custom filters.                                                                                                                                                                                                                                            |
| Custom Filters    | Use custom filters to add more customization to a custom analyzer. For more information about these filters, see the [Custom Filters](#custom-filters) section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Date/Time Parsers | If the documents in your index contain date and time data in a format other than RFC-3339 (ISO-8601), then you need to create a date/time parser. A custom date/time parser tells the Search index how to interpret date data from your documents. For more information about how to add a custom date/time parser, see [Create a Custom Date/Time Parser](create-custom-date-time-parser.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Advanced          | Set advanced settings to change your index's default analyzer, replication, and more. For more information about how to change advanced settings, see [Set Search Index Advanced Settings](set-advanced-settings.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## [](#custom-filters)Custom Filters

Custom filters are components of a Search index [analyzer](#analyzers).

Create and add these components to a custom analyzer to improve search results and performance for an index.

You can create the following custom filters:

* [Character Filters](#character-filters)
* [Tokenizers](#tokenizers)
* [Token Filters](#token-filters)
* [Wordlists](#wordlists)

### [](#character-filters)Character Filters

Character filters remove unwanted characters from the input for a search. For example, the default **html** character filter removes HTML tags from your search content.

You can use a default character filter in an analyzer or create your own.

For more information about the available default character filters, see [Default Character Filters](default-character-filters-reference.md).

For more information about how to create your own custom character filter, see [Create a Custom Character Filter](create-custom-character-filter.md).

### [](#tokenizers)Tokenizers

Tokenizers separate input strings into individual tokens. These tokens are combined into token streams. The Search Service takes token streams from search queries to determine matches for token streams in search results.

You can use a default tokenizer in an analyzer or create your own.

For more information about the available default tokenizers, see [Default Tokenizers](default-tokenizers-reference.md).

For more information about how to create your own tokenizer, see [Create a Custom Tokenizer](create-custom-tokenizer.md).

### [](#token-filters)Token Filters

Token filters take the token stream from a tokenizer and modify the tokens.

A token filter can create stems from tokens to increase the matches for a search term. For example, if a token filter creates the stem `play`, a search can return matches for `player`, `playing`, and `playable`.

The Search Service has default tokenizers available. For a list of all available tokenizers, see [Default Token Filters](default-token-filters-reference.md).

You can also create your own token filters. Custom token filters can use [Wordlists](#wordlists) to modify their tokens. For more information about how to create your own token filter, see [Create a Custom Token Filter](create-custom-token-filter.md).

### [](#wordlists)Wordlists

Wordlists define a list of words that you can use with a [token filter](#token-filters) to create tokens.

You can use a wordlist to find words and create tokens, or remove words from a tokenizer's token stream.

When you create a custom token filter, the Search Service has a set of default wordlists. For more information about the available default wordlists, see [Default Wordlists](default-wordlists-reference.md).

For more information about how to create your own wordlist, see [Create a Custom Wordlist](create-custom-wordlist.md).