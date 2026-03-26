---
title: Create a Search Index
description: Create a Search index to get started with the Search Service in your cluster.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/create-search-indexes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.6@server:search:create-search-indexes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/search/create-search-indexes.html)

# Create a Search Index

> Create a Search index to get started with the Search Service in your cluster. 

You can create a Search index with:

* The [Couchbase Server Web Console](#ui).
* The [Search Service REST API](#api).

> [!TIP]
> If you're new to developing with the Search Service, [create a Search index with the UI](#ui). You can copy the Search index definition JSON payload from the UI to create your index [with the REST API](create-search-index-rest-api.md), or [Import a Search Index Definition with the Web Console](import-search-index.md).

## [](#ui)Creating a Search Index with the Web Console

To [create a basic Search index](create-search-index-ui.md), provide the following information:

* The name of the index.
* The bucket where you want to create the index.

Many of the examples in the Search Service documentation use the `travel-sample` sample data bucket. For more information about how to load this sample data on your own cluster, see [Sample Buckets](../manage/manage-settings/install-sample-buckets.md).

> [!NOTE]
> For indexes created with Couchbase Server version 7.6 and later, index names must be unique inside a bucket and scope. You cannot have 2 indexes with the same name inside the same bucket and scope on a Couchbase Server cluster running version 7.6.
> 
> The Couchbase Server Web Console marks indexes as scoped or not scoped to a specific bucket and scope.
> 
> Indexes created with a previous version of Couchbase Server are not scoped.
> 
> To view the full, scoped name for an index, go to the **Search** tab and point to the **Index Name**. Use the scoped name with the [Search Service REST API](../rest-api/rest-fts.md), for any endpoints that do not include the bucket and scope in their path.

If you want to restrict the documents you add to an index, you can also:

* [Create a Type Mapping](create-type-mapping.md).
* [Add child fields](create-child-field.md) to add or remove document fields from the index.

After you create a Search index, the Search Service streams data from your chosen collection or collections, and any document mutations, into the index builder. Before your index finishes building, you can run a search and return partial results.

You can also customize a Search index to improve search results and performance. For more information about how you can customize a Search index with the Web Console, see [Customize a Search Index with the Web Console](customize-index.md).

### [](#creating-a-search-index-with-the-quick-editor)Creating a Search Index with the Quick Editor

The Web Console also has a Quick Index editor.

You can use the Quick Index editor to create a Search index by selecting fields from a document from your cluster.

The Quick Index editor works best when you need to create a basic Search index to start testing and prototyping with the Search Service. If you want to have greater control over how the Search Service returns results, such as changing your [analyzer](customize-index.md#analyzers), use [the standard editor](create-search-index-ui.md).

You can edit an index that you created with the Quick Index editor in the standard editor later. You cannot edit an index that you created with the standard editor in the Quick Index editor.

For more information about how to create an index with the Quick Index editor, see [Create a Search Index with the Quick Editor](create-quick-index.md).

## [](#api)Creating a Search Index with the REST API

You can create a Search index with the REST API through a JSON payload. Most properties in the JSON payload correspond to settings in the Web Console. You can also copy the Search index definition JSON payload from a Search index in the Web Console to use in a REST API call.

> [!NOTE]
> Use the scoped name for an index with the [Search Service REST API](../rest-api/rest-fts.md) for any endpoints that do not include the bucket and scope in their path. For example, you must use `bucket.scope.index_name` as the format for your index name with the `analyzeDoc` endpoint, but not with the new 7.6 `query` endpoint.

For more information about how to use the REST API to create a Search index, see [Create a Search Index with the REST API and curl/HTTP](create-search-index-rest-api.md).

For more information about the available properties for a Search index, see [Search Index JSON Properties](search-index-params.md).

## [](#see-also)See Also

* [Customize a Search Index with the Web Console](customize-index.md)
* [Create Search Index Aliases](index-aliases.md)
* [Run a Search With a Search Index](run-searches.md)