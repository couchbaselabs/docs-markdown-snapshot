---
title: Import a Search Index Definition with the Web Console
description: Use the Couchbase Server Web Console to import a JSON Search index
  definition or Search index alias.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/import-search-index.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/search/import-search-index.html)

# Import a Search Index Definition with the Web Console

> Use the Couchbase Server Web Console to import a JSON Search index definition or Search index alias. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
* Your user account has the [Search Admin](../learn/security/roles.md#search-admin) role for the bucket where you want to create the index.
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To import a [Search index definition](create-search-indexes.md) or [Search alias](index-aliases.md) with the Couchbase Server Web Console:

1. Go to **Search**.
2. Do one of the following:

  1. To import a Search index definition, click **Add Index**.
  2. To import a Search index alias definition, click **\+ Add Alias**.
3. Click **Import**.
4. In the Import Index window, paste the JSON definition of your Search index or index alias.
5. Click **Import**.
6. (Optional) Make any changes to your Search index or index alias settings.  
For more information, see [Customize a Search Index with the Web Console](customize-index.md) or [Create a Search Index Alias with the Web Console](create-search-index-alias.md).
7. Click **Create Index** or **Create Index Alias**.

## [](#next-steps)Next Steps

For more information about the settings you can change for your imported Search index, see [Customize a Search Index with the Web Console](customize-index.md).

To run a search with your Search index or index alias, see [Run A Simple Search with the Web Console](simple-search-ui.md) or [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).