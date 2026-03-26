---
title: Create a Basic Search Index with the Web Console
description: You can create a Search index with the Couchbase Server Web Console.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/create-search-index-ui.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:search:create-search-index-ui.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/search/create-search-index-ui.html)

# Create a Basic Search Index with the Web Console

> You can create a Search index with the Couchbase Server Web Console. 

Use the [Quick Editor](create-quick-index.md) if you do not need full customization or advanced settings to quickly create a Search index and [type mappings](customize-index.md#type-mappings).

You must create a Search index before you can [run a search](simple-search-ui.md) with the Search Service.

You can also [Import a Search Index Definition with the Web Console](import-search-index.md).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
* Your user account has the [Search Admin](../learn/security/roles.md#search-admin) role for the bucket where you want to create the index.
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To create a Search index with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click **Add Index**.
3. In the **Index Name** field, enter a name for the index.  
> [!NOTE]  
> Your index name must start with an alphabetic character (a-z or A-Z). It can only contain alphanumeric characters (a-z, A-Z, or 0-9), hyphens (-), or underscores (\_).  
>  
> For Couchbase Server version 7.6 and later, your index name must be unique inside your selected bucket and scope. You cannot have 2 indexes with the same name inside the same bucket and scope.
4. In the **Bucket** list, select the bucket where you want to create the index.
5. Expand **Customize Index**.
6. (Optional) To create the index on a scope other than `_default`, select **Use non-default scope/collection(s)**.

  1. In the **Scope** list, select the scope where you want to create the index.
  2. Under **Mappings**, clear **\# default | dynamic**.
  3. Click **\+ Add Type Mapping**.
  4. In the **Collection** list, choose the collection where you want to create the index.
  5. Click **OK**.
7. Click **Create Index**.

## [](#next-steps)Next Steps

This basic index includes all documents from the bucket, scope, and collection you selected. You can run a search against this index, but it's recommended that you customize your index to improve performance and reduce the index size.

For more information about how to customize an index, see [Customize a Search Index with the Web Console](customize-index.md).

For more information about how to run a search, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md). You can run a search before **Indexing progress** reaches 100% and return partial results.