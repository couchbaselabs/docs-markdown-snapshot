---
title: Set Search Index Advanced Settings
description: When using the Advanced Mode editor in Couchbase Capella UI, you
  can configure additional advanced settings for your Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/set-advanced-settings.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/search/set-advanced-settings.html)

# Set Search Index Advanced Settings

> When using the Advanced Mode editor in Couchbase Capella UI, you can configure additional advanced settings for your Search index. 

Advanced Mode adds full customization and advanced features such as [creating custom analyzers](create-custom-analyzer.md) or [setting a document filter](set-type-identifier.md). For more information about the different settings and features available in a Search index, see [Search Index Features](customize-index.md).

You must create a Search index before you can [run a search](simple-search-ui.md) with the Search Service.

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have a bucket with scopes and collections in your operational cluster. For more information, see [Manage Buckets](../clusters/data-service/manage-buckets.md).
* You have created a basic Search index with the Capella UI. For more information, see [Create a Search Index with the Capella UI](create-search-index-ui.md).
* You have logged in to the Couchbase Capella UI.

## [](#procedure)Procedure

To set advanced settings for a Search index with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with the Search Service.
3. Go to **Data Tools** **Search**.
4. Click the name of the index where you want to configure advanced settings.
5. Click **Enable Advanced Mode**.
6. Do any of the following:

  1. In the **Default Analyzer** list, select the [default analyzer](customize-index.md#analyzers) to assign to new [type mappings](customize-index.md#type-mappings) in your index.  
  You can also choose to [Create a Custom Analyzer](create-custom-analyzer.md).
  2. In the **Default Date/Time Parser** list, select the [default date/time parser](customize-index.md#date-time) to use for date data in your index.  
  You can also choose to [Create a Custom Date/Time Parser](create-custom-date-time-parser.md).
  3. Add a document filter to control how documents are included in your type mappings. For more information, see [Set a Document Filter](set-type-identifier.md).
  4. Add a synonym source to support synonym searches. For more information, see [Add Synonyms to a Search Index](synonyms/synonyms-search.md).
  5. Choose the scoring model you want to use with your Search index. For more information about scoring models, see [Scoring Model](customize-index.md#scoring-model).
  6. If you’re using [dynamic type mappings](about-mappings.md#dynamic), choose how to handle dynamic fields in your Search index:

    1. To store the content of any fields added to a Search index from a dynamic type mapping, turn on **Store Dynamic Fields**.
    2. To include fields or whole documents in your Search index that match a dynamic type mapping, turn on **Index Dynamic Fields**.
7. Click **Update Index**.

## [](#next-steps)Next Steps

You can keep adding additional features to your Search index to improve performance and search results. For more information, see [Search Index Features](customize-index.md).

For more information about how to run a search, see [Run A Simple Search with the Capella UI](simple-search-ui.md).