---
title: Customize a Search Index with the Web Console
description: Configure additional options for a Search index to improve
  performance and fine tune your search results.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/customize-index.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:search:customize-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/search/customize-index.html)

# Customize a Search Index with the Web Console

> Configure additional options for a Search index to improve performance and fine tune your search results. 

Some Search index options are only available when you [use the standard editor](create-search-index-ui.md).

You can add the following components and configure the following options for a Search index:

| Option            | Quick Editor | Standard Editor | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------- | ------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Type Identifier   |              | ✓               | Set a type identifier to add a filter to the documents added to your Search index through a [type mapping](#type-mapping): JSON Type Field: Selects only documents that contain a specific field with a specified string value. Doc ID up to Separator: Selects only documents with an ID or key up to a specific substring. Doc ID with Regex: Selects only documents with an ID or key that matches a regular expression. Couchbase Server 8.0 Custom: As of Couchbase Server version 8.0, custom document filters select only documents that match a custom filter, based on the values of specific fields. Type identifiers add a more granular filter to the documents in a type mapping. If a type mapping has a type identifier, only documents that match the type identifier can be included in the Search index. For more information about how to configure a type identifier, see [Set the Type Identifier for a Search Index](set-type-identifier.md). |
| Mappings          | ✓            | ✓               | Use a type mapping to include or exclude specific documents in a collection from an index. For more information about the different kinds of mappings in a Search index, see [Map Document Collections, Objects, and Fields](about-mappings.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Analyzers         |              | ✓               | Use analyzers to improve and customize the search results in your index. Analyzers transform input text into tokens, which give you greater control over your index's text matching. You can use one of Couchbase's built-in analyzers or create your own. For more information about how to create a custom analyzer, see [Create a Custom Analyzer](create-custom-analyzer.md). Analyzers have different components that control how text is transformed for search. When you create a custom analyzer, you can choose these components. For more information, see [Custom Filters](#custom-filters).                                                                                                                                                                                                                                                                                                                                                             |
| Custom Filters    |              | ✓               | Use custom filters to add more customization to a custom analyzer. For more information about these filters, see the [Custom Filters](#custom-filters) section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Date/Time Parsers |              | ✓               | If the documents in your index contain date and time data in a format other than RFC-3339 (ISO-8601), then you need to create a date/time parser. A custom date/time parser tells the Search index how to interpret date data from your documents. If any values are missing from a date/time string in your documents, the Search Service automatically fills in [default date/time values](default-date-time-parsers-reference.md#missing-values) to make it easier to compare date/time strings. For more information about how to add a custom date/time parser, see [Create a Custom Date/Time Parser](create-custom-date-time-parser.md). For more information about the available default date/time parsers, see [Default Date/Time Parsers](default-date-time-parsers-reference.md).                                                                                                                                                                        |
| Advanced          |              | ✓               | Set advanced settings to change your index's default analyzer, replication, and more. For more information about how to change advanced settings, see [Set Search Index Advanced Settings](set-advanced-settings.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Synonym Sources   | ✓            | ✓               | Couchbase Server 8.0 As of Couchbase Server version 8.0 and later, you can add a Synonym Source to a Search index to use synonym searches on text fields. After you [create a synonym collection and synonym documents](synonyms/create-synonym-collection-docs.md), and [add a synonym source](synonyms/add-synonym-source.md), you can run a search for a term and return results that include terms with similar meanings. For example, you could run a search for happy and get results for joyful, cheerful, or delighted. You can also [add Synonym Sources with the Quick Editor](synonyms/add-synonym-source-quick.md). For more information about synonym search for the Search Service, see [Add Synonyms to a Search Index](synonyms/synonyms-search.md) or [Add Synonyms with the Quick Editor](synonyms/synonyms-search-quick.md), based on your preferred editor.                                                                                     |

## [](#custom-filters)Custom Filters

Custom filters are components of a Search index [analyzer](#analyzers).

Create and add these components to a custom analyzer to improve search results and performance for an index with the [standard editor](create-search-index-ui.md).

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

## [](#see-also)See Also

* [Set the Type Identifier for a Search Index](set-type-identifier.md)
* [Create a Type Mapping](create-type-mapping.md)
* [Create a Child Field](create-child-field.md)
* [Create a Child Mapping](create-child-mapping.md)
* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Create a Custom Wordlist](create-custom-wordlist.md)
* [Set Search Index Advanced Settings](set-advanced-settings.md)
* [Add Synonyms to a Search Index](synonyms/synonyms-search.md)
* [Run a Search With a Search Index](run-searches.md)
* [Create Search Index Aliases](index-aliases.md)