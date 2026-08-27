---
title: Create a Basic Search Index with the Web Console
description: You can create a Search index with the Couchbase Server Web Console.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/search/pages/create-search-index-ui.adoc
  xref: xref:7.2@server:search:create-search-index-ui.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/search/create-search-index-ui.html)

# Create a Basic Search Index with the Web Console

> You can create a Search index with the Couchbase Server Web Console. 

You must create a Search index before you can [run a search](simple-search-ui.md) with the Search Service.

## [](#prerequisites)Prerequisites

* You've deployed the Search Service on a node in your database.
* You have a bucket with scopes and collections in your database.
* Your user account has the **Search Admin** role for the bucket where you want to create the index.
* You've logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To create a Search index with the Couchbase Server Web Console:

1. Go to **Search**.
2. Click **Add Index**.
3. In the **Index Name** field, enter a name for the index.  
> [!NOTE]  
> Your index name must start with an alphabetic character (a-z or A-Z). It can only contain alphanumeric characters (a-z, A-Z, or 0-9), hyphens (-), or underscores (\_).
4. In the **Bucket** list, select the bucket where you want to create the index.
5. Expand **Customize Index**.
6. (Optional) To create the index on a scope other than `_default`, select **Use non-default scope/collection(s)**.

  1. In the **Scope** list, select the scope where you want to create the index.
7. Click **Create Index**.

## [](#next-steps)Next Steps

This basic index includes all documents from the bucket and scope you selected. You can run a search against this index, but it's recommended that you customize your index to improve performance and reduce the index size.

For more information about how to customize an index, see [Customize a Search Index with the Web Console](customize-index.md).

For more information about how to run a search, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).