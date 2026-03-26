---
title: Search Index Features
description: Search indexes in Couchbase Capella have multiple features that you
  can configure to improve performance and fine tune your search results.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/customize-index.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cloud:search:customize-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/search/customize-index.html)

# Search Index Features

> Search indexes in Couchbase Capella have multiple features that you can configure to improve performance and fine tune your search results. 

Some features are only available in [Advanced Mode editing](create-search-indexes.md#advanced-mode).

You can add the following components and configure the following options for a Search index:

| Option                                                 | Quick Mode | Advanced Mode |
| ------------------------------------------------------ | ---------- | ------------- |
| [Analyzers](#analyzers)                                | ✓          | ✓             |
| [Default Date/Time Parser](#date-time)                 |            | ✓             |
| [Document Filters](#type-identifiers)                  |            | ✓             |
| [Synonym Sources](#synonyms)                           |            | ✓             |
| [Scoring Model](#scoring-model)                        |            | ✓             |
| [Dynamic Fields Settings](#dynamic-fields)             |            | ✓             |
| [Type Mappings and Mappings](#type-mappings)           | ✓          | ✓             |
| [Replica and Partition Settings](#replica)             | ✓          | ✓             |
| [Custom Analyzers and Custom Filters](#custom-filters) |            | ✓             |

## [](#analyzers)Analyzers

Use analyzers to improve and customize the search results in your index.

Analyzers transform input text into tokens, which give you greater control over your index's text matching. The **Default Analyzer** sets the analyzer that's used by default for new [type mappings](#type-mappings) across your Search index.

You can use 1 of Couchbase's built-in analyzers as the **Default Analyzer** or the analyzer for a specific [type mapping](#type-mappings). If you use Advanced Mode, you can create your own analyzer.

Analyzers have different components that control how text is transformed for search. When you create a custom analyzer, you can choose these components. For more information about Search analyzer components, see [Custom Analyzers and Custom Filters](#custom-filters).

For more information about how to create a custom analyzer, see [Create a Custom Analyzer](create-custom-analyzer.md).

## [](#scoring-model)Scoring Model

Couchbase Server version 8.0

As of Couchbase Server version 8.0, in Advanced Mode editing, you can choose the specific scoring model you want to use for a Search index. Your scoring model changes the calculation the Search Service uses for scoring documents and ranking them in your search results.

The following scoring model algorithms are available:

* `tf-idf`: The standard scoring model for the Search Service. A higher tf-idf score for a document places that document higher in your search results.
* `bm25`: A scoring model better suited to hybrid searches with the Search Service. A hybrid Search query uses [Vector Search](../vector-search/vector-search.md) together with a standard Search query.

For more information about the calculations for scoring for each algorithm, see [Scoring for Search Queries](run-searches.md#scoring).

## [](#date-time)Default Date/Time Parser

Set the default format that the Search index should use to interpret date and time data in your Search index.

If the documents in your index contain date and time data in a format other than the [default date/time parsers](default-date-time-parsers-reference.md), you need to create a custom date/time parser. You can only create a custom date/time parser if you switch to Advanced Mode. For more information about how to add a custom date/time parser, see [Create a Custom Date/Time Parser](create-custom-date-time-parser.md).

## [](#type-identifiers)Document Filters

In Advanced Mode, you can also choose and configure an additional document filter to add or remove documents in your Search index that meet certain conditions:

* **JSON Type Field**: Selects only documents that contain a specific field with a specified string value.
* **Doc ID up to Separator**: Selects only documents with an ID or key up to a specific substring.
* **Doc ID with Regex**: Selects only documents with an ID or key that matches a regular expression.
* Couchbase Server 8.0 **Custom**: As of Couchbase Server version 8.0, custom document filters select only documents that match a custom filter, based on the values of specific fields.

Document filters add a more granular filter to the documents in a collection [type mapping](#type-mappings). If a collection mapping has a document filter, only documents that pass the filter can be included in the Search index under that collection.

For more information about how to create a document filter, see [Set a Document Filter](set-type-identifier.md).

## [](#synonyms)Synonym Sources

Couchbase Server 8.0

As of Couchbase Server version 8.0 and later, you can add a Synonym Source to a Search index to use synonym searches on text fields.

After you [create a synonym collection and synonym documents](synonyms/create-synonym-collection-docs.md), and [add a synonym source](synonyms/add-synonym-source.md), you can run a search for a term and return results that include terms with similar meanings.

For example, you could run a search for `happy` and get results for `joyful`, `cheerful`, or `delighted`.

For more information about synonym search for the Search Service, see [Add Synonyms to a Search Index](synonyms/synonyms-search.md).

## [](#scoring-model)Scoring Model

Couchbase Server version 8.0

As of Couchbase Server version 8.0, in Advanced Mode editing, you can choose the specific scoring model you want to use for a Search index. Your scoring model changes the calculation the Search Service uses for scoring documents and ranking them in your search results.

The following scoring model algorithms are available:

* `tfidf`: The standard scoring model for the Search Service. A higher tf-idf score for a document places that document higher in your search results.
* `bm25`: A scoring model better suited to hybrid searches with the Search Service. A hybrid Search query uses [Vector Search](../vector-search/vector-search.md) together with a standard Search query. For more information about the calculations for scoring for each algorithm, see [Scoring for Search Queries](run-searches.md#scoring).

## [](#dynamic-fields)Dynamic Fields Settings

When you add [\[dynamic\]](#dynamic) to your Search index, in **Advanced Mode**, you can choose how the Search Service handles these dynamic type mappings:

* [Store Dynamic Fields](#store-dynamic)
* [Index Dynamic Fields](#index-dynamic)

### [](#store-dynamic)Store Dynamic Fields

If you turn on **Store Dynamic Fields**, the Search Service stores the content of any fields under a dynamic type mapping. Storing field content allows you to return the value of a field in search results.

This increases the size of your index.

### [](#index-dynamic)Index Dynamic Fields

If you turn on **Index Dynamic Fields**, the Search Service includes fields or whole documents in your Search index that match a dynamic type mapping.

This increases the size of your index.

## [](#type-mappings)Type Mappings and Mappings

Use a type mapping to include or exclude specific documents in a collection from an index.

Type mappings can also set a document field's data type and other settings.

Type mappings start at the collection level. Create additional mappings for document fields or JSON objects under a collection's type mapping to restrict the documents added to your index. This can improve Search index performance over indexing entire collections.

For a type mapping defined on a scope and collection, you can create an additional [document filter](#type-identifiers) to restrict the documents added under that type mapping. Only documents from your specified scope and collection that also pass the document filter can be included in your Search index, and potentially returned in search results.

If your operational cluster is running Couchbase Server version 7.6.2 and later, you can also choose to include document metadata inside your Search index by creating an XATTRs mapping. For more information about how to configure settings for the different types of mappings and type mappings, see [Collection, Object, XATTRs, and Field Mapping Options](type-mapping-options.md).

For more information about how to configure a type mapping in the Search index editor, see [Create a New Mapping or Type Mapping](create-type-mapping.md).

For more information about the different types of type mappings, see [About Mapping Collections, Objects and Fields](about-mappings.md).

## [](#replica)Replica and Partition Settings

Use replicas and partitions to add high availability, fault tolerance, and scalability to your Search index.

### [](#number-of-replicas)Number of Replicas

Add Search index replicas to create copies of your Search index on other nodes. If 1 of the nodes running the Search Service in your cluster goes offline, you can still use your indexes if they exist on another node.

Adding more replicas increases the storage used by the Search Service for your indexes. You cannot add more replicas if your cluster configuration does not have the nodes to support those replicas.

### [](#number-of-partitions)Number of Partitions

Add Search index partitions to distribute the contents of a Search index over multiple Search Service nodes in your cluster.

Partitions improve Search index performance, but increase the complexity of a Search index and its resource usage.

It's recommended to set your Search index partitions to the number of nodes running the Search Service in your operational cluster, to get the most efficient resource usage.

## [](#custom-filters)Custom Analyzers and Custom Filters

Custom filters are components of a Search index [analyzer](#analyzers).

Create and add custom filters to a custom analyzer to improve search results and performance for an index in Advanced Mode. You cannot create custom analyzers or custom filters if **Advanced Options** are not enabled.

You can create the following custom filters:

* [Character Filters](#character-filters)
* [Tokenizers](#tokenizers)
* [Token Filters](#token-filters)
* [Word Lists](#wordlists)

### [](#character-filters)Character Filters

Character filters remove unwanted characters from the input for a search. For example, the default **html** character filter removes HTML tags from your search content.

You can use a default character filter in an analyzer or create your own. When you create a custom character filter, you can choose whether your analyzer replaces any removed characters with your own configured string.

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

The Search Service has default token filters available. For a list of all available token filters, see [Default Token Filters](default-token-filters-reference.md).

You can also create your own token filters. Custom token filters can use [Word Lists](#wordlists) to modify their tokens. For more information about how to create your own token filter, see [Create a Custom Token Filter](create-custom-token-filter.md).

### [](#wordlists)Word Lists

Word lists define a list of words that you can use with a [token filter](#token-filters) to create tokens.

You can use a word list to find words and create tokens, or remove words from a tokenizer's token stream.

When you create a custom token filter, the Search Service you can use a default word list, or create your own word list. Only specific custom token filter types use word lists in their configuration:

* [dict\_compound](create-custom-token-filter.md#dict-compound)
* [elision](create-custom-token-filter.md#elision)
* [keyword\_marker](create-custom-token-filter.md#keyword-marker)
* [stop\_tokens](create-custom-token-filter.md#stop-tokens)

For more information about the available default word lists, see [Default Wordlists](default-wordlists-reference.md). For more information about how to create your own word list, see [Create a Custom Token Filter](create-custom-token-filter.md).

## [](#see-also)See Also

* [Create a Search Index with the Capella UI](create-search-index-ui.md)
* [Create a New Mapping or Type Mapping](create-type-mapping.md)
* [Set a Document Filter](set-type-identifier.md)
* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Add Synonyms to a Search Index](synonyms/synonyms-search.md)
* [Run a Search With a Search Index](run-searches.md)
* [Create Search Index Aliases](index-aliases.md)