---
title: Create a Search Index
description: Create a Search index to get started with the Search Service in
  your operational cluster.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/create-search-indexes.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:search:create-search-indexes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/search/create-search-indexes.html)

# Create a Search Index

> Create a Search index to get started with the Search Service in your operational cluster. 

You can create a Search index with:

* The [Couchbase Capella UI](#ui).
* A JSON payload that you [import through the UI](import-search-index.md).

All Search indexes are built from a JSON payload. For more information about the available properties for a Search index JSON payload, see [Search Index JSON Properties](search-index-params.md).

> [!TIP]
> If you’re new to developing with the Search Service, [create a Search index with the UI](#ui). You can export the Search index definition JSON payload from the UI to [Import a Search Index Definition with the Capella UI](import-search-index.md).

## [](#ui)Creating a Search Index with the Capella UI

Couchbase Capella supports creating a Search index with a streamlined experience, or Advanced Options.

When you [create a new Search index](create-search-index-ui.md), you can:

* [Configure global index settings](create-search-index-ui.md#configure-settings), which include:

  * [Setting a default analyzer](customize-index.md#analyzers)
  * [Setting a default date/time parser](customize-index.md#date-time)
* Create [Type mappings and mappings](customize-index.md#type-mappings)
* Configure [Replica and partition settings](customize-index.md#replica)

If you select **Enable Advanced Options** to enable Advanced Mode in the Search index editor, the following additional options become available:

* Creating custom [analyzers](customize-index.md#analyzers), which can include:

  * Custom [character filters](customize-index.md#character-filters)
  * Custom [tokenizers](customize-index.md#tokenizers)
  * Custom [token filters](customize-index.md#token-filters), which can use custom [word lists](customize-index.md#wordlists)
* Creating custom [date/time parsers](customize-index.md#date-time)
* Creating [mappings](customize-index.md#type-mappings) for Extended Attributes (XATTRs) data in documents
* Creating [mappings](customize-index.md#type-mappings) for objects and fields that do not yet exist in your document schema
* Configuring a [document filter](customize-index.md#type-identifiers)
* As of Couchbase Server version 8.0, configuring a [synonym source](synonyms/synonyms-search.md)
* As of Couchbase Server version 8.0, changing your Search index’s [scoring model](customize-index.md#scoring-model)

All initial editing options remain available in Advanced Mode editing.

> [!NOTE]
> For indexes created with Couchbase Server version 7.6 and later, index names must be unique inside a bucket and scope. You cannot have 2 indexes with the same name inside the same bucket and scope on a Capella operational cluster running version 7.6 or later.
> 
> The Capella UI marks indexes as scoped or not scoped to a specific bucket and scope.
> 
> Indexes created with a previous version of Couchbase Server are not scoped.

After you create a Search index, the Search Service streams data from your chosen collection or collections, and any document mutations, into the index builder. Before your index finishes building, you can run a search and return partial results.

## [](#see-also)See Also

* [Search Index Features](customize-index.md)
* [Create Search Index Aliases](index-aliases.md)
* [Run a Search With a Search Index](run-searches.md)