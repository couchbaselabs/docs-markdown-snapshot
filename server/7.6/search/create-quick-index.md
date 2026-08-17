---
title: Create a Search Index with the Quick Editor
description: Use the Quick Index editor in the Couchbase Server Web Console to
  create a Search index.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/create-quick-index.adoc
  xref: xref:7.6@server:search:create-quick-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/search/create-quick-index.html)

# Create a Search Index with the Quick Editor

> Use the Quick Index editor in the Couchbase Server Web Console to create a Search index. 

The Quick Index editor lets you select the fields that you want to add to a Search index with a document in your cluster.

The Quick Index editor works best when you need to create a basic Search index to start testing and prototyping with the Search Service. If you want to have greater control over how the Search Service returns results, such as changing your [analyzer](customize-index.md#analyzers), see [Create a Basic Search Index with the Web Console](create-search-index-ui.md).

You must create a Search index before you can [run a search](simple-search-ui.md) with the Search Service.

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../../current/manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../../current/manage/manage-buckets/create-bucket.md).
* Your user account has the **Search Admin** role for the bucket where you want to create the index.
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To use the Couchbase Server Web Console's Quick Editor to create a Search index:

1. Go to **Search**.
2. Click **Quick Index**.
3. In the **Index Name** field, enter a name for the index.  
> [!NOTE]  
> Your index name must start with an alphabetic character (a-z or A-Z). It can only contain alphanumeric characters (a-z, A-Z, or 0-9), hyphens (-), or underscores (\_).  
>  
> For Couchbase Server version 7.6 and later, your index name must be unique inside your selected bucket and scope. You cannot have 2 indexes with the same name inside the same bucket and scope.
4. In the first **Keyspace** list, select the bucket where you want to create the index.
5. In the second **Keyspace** list, select the scope where you want to create the index.
6. In the third **Keyspace** list, select the collection where you want to create the index.
7. In the **Select Fields** box, click a field in the document that you want to add to the index.  
> [!TIP]  
> You can randomly select a new document from your chosen keyspace by clicking **Refresh** above the **Select Fields** display.
8. In the **Type** list, select the field's data type.  
For more information about the available data types, see [Field Data Types](field-data-types-reference.md).
9. Set the field's options.  
For more information about the available field options, see [Quick Index Field Options](quick-index-field-options.md).
10. Click **Add**.
11. (Optional) Repeat the previous steps for each field you want to add to the Search index.
12. Click **Create Index**.

## [](#next-steps)Next Steps

You can [customize your index](customize-index.md) with the standard Search index editor to improve your Search index's performance and the quality of your search results.

> [!CAUTION]
> If you edit your Search index with the [standard editor](create-search-index-ui.md), you cannot return to Quick Mode and keep any advanced settings.

To run a search and test the contents of your Search index, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md). You can run a search before **Indexing progress** reaches 100% and return partial results.