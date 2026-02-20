---
title: Set Search Index Advanced Settings
description: Configure advanced settings with the Couchbase Server Web Console
  for a Search index to improve an index's search results and performance.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/set-advanced-settings.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:search:set-advanced-settings.adoc[]
---

[View original HTML](/server/7.6/search/set-advanced-settings.html)

# Set Search Index Advanced Settings

> Configure advanced settings with the Couchbase Server Web Console for a Search index to improve an index’s search results and performance. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../../current/manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../../current/manage/manage-buckets/create-bucket.md).
* You have created an index. For more information, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).
* Your user account has the **Search Admin** role for the bucket where you want to edit an index.
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To set advanced settings for a Search index with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click the index that you want to edit.
3. Click **Edit**.
4. Expand **Customize Index** **Advanced**.
5. Configure any of the following advanced settings for your index:

| Option                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Default Type                 | Change the default type assigned to documents in the index. The default value is \_default.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Default Analyzer             | Change the default analyzer assigned to type mappings in the index. For more information about the available default analyzers, see [Default Analyzers](default-analyzers-reference.md). For more information about how to create your own custom analyzer, see [Create a Custom Analyzer](create-custom-analyzer.md).                                                                                                                                                                                                         |
| Default Date/Time Parser     | Change the default date/time parser used for date data in your documents. For more information about the available default date/time parsers, see [Default Date/Time Parsers](default-date-time-parsers-reference.md). For more information about how to create your own custom date/time parser, see [Create a Custom Date/Time Parser](create-custom-date-time-parser.md).                                                                                                                                                   |
| Default Field                | When you [create a mapping for a child field](create-child-field.md), you can choose to include that field in an \_all field. You can add fields to the \_all field to search their contents without specifying their field name in your search query. Enter a value in the **Default Field** field to change the name of this default field.                                                                                                                                                                                  |
| Store Dynamic Fields         | Select **Store Dynamic Fields** to include field values in search results from a [dynamic type mapping](customize-index.md#type-mappings) in the index.                                                                                                                                                                                                                                                                                                                                                                        |
| Index Dynamic Fields         | Select **Index Dynamic Fields** to include fields from a [dynamic type mapping](customize-index.md#type-mappings) in the index.                                                                                                                                                                                                                                                                                                                                                                                                |
| DocValues for Dynamic Fields | Select **DocValues for Dynamic Fields** to include the values of each field from a [dynamic type mapping](customize-index.md#type-mappings) in the index for [Facets](search-request-params.md#facets) and sorting search results.                                                                                                                                                                                                                                                                                             |
| Index Replicas               | Set the number of replicas that the Search Service creates for the index. If a node running the Search Service is lost, you can use an index replica to keep using your data. Replicas exist on nodes separate from the current active replica or any other replicas. You must have enough nodes running the Search Service to support any selection you make for this setting. For more information about replication and the Search Service, see [High Availability for Search](../fts/fts-high-availability-for-search.md). |
| Index Type                   | This setting is included for compatibility only. For new indexes, this setting is always **Version 6.0 (Scorch)**.                                                                                                                                                                                                                                                                                                                                                                                                             |
| Index Partitions             | Enter a number greater than one to divide the index into partitions across multiple nodes running the Search Service. This can improve query latency for large, aggregated queries and help with horizontal scaling for large Search indexes.                                                                                                                                                                                                                                                                                  |
6. Click **Update Index**.

## [](#next-steps)Next Steps

After you change the settings for your Search index, you can continue to customize your Search index:

* [Set the Type Identifier for a Search Index](set-type-identifier.md)
* [Create a Type Mapping](create-type-mapping.md)
* [Create a Child Field](create-child-field.md)
* [Create a Child Mapping](create-child-mapping.md)
* [Create a Custom Analyzer](create-custom-analyzer.md)
* [Create a Custom Character Filter](create-custom-character-filter.md)
* [Create a Custom Token Filter](create-custom-token-filter.md)
* [Create a Custom Tokenizer](create-custom-tokenizer.md)
* [Create a Custom Wordlist](create-custom-wordlist.md)

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).