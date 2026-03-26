---
title: Get a Search Index Definition from the Web Console
description: Use the Couchbase Server Web Console to copy and paste a JSON
  Search index definition for use in the REST API or another cluster.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/search/pages/export-search-index.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:search:export-search-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/search/export-search-index.html)

# Get a Search Index Definition from the Web Console

> Use the Couchbase Server Web Console to copy and paste a JSON Search index definition for use in the REST API or another cluster. 

> [!NOTE]
> You cannot export a Search index definition as a downloadable file. You can only copy the Search index definition from an existing index.

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your cluster. For more information about how to deploy a new node and Services on your cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* You have a bucket with scopes and collections in your cluster. For more information about how to create a bucket, see [Create a Bucket](../manage/manage-buckets/create-bucket.md).
* Your user account has the [Search Admin](../learn/security/roles.md#search-admin) role for the bucket where you want to export an index definition.
* You have created a Search index.  
For more information about how to create a Search index, see [Create a Basic Search Index with the Web Console](create-search-index-ui.md) or [Create a Search Index with the REST API and curl/HTTP](create-search-index-rest-api.md).
* You have logged in to the Couchbase Server Web Console.

## [](#procedure)Procedure

To copy a Search index definition from the Server Web Console:

1. Go to **Search**.
2. Click the name of the Search index definition you want to copy.
3. Expand **Show index definition JSON**.
4. Click **Copy to Clipboard**.

> [!TIP]
> When you [create a Search index with the Server Web Console](create-search-index-ui.md), you can also click **copy to clipboard** on the **Index Definition Preview** to copy the Search index definition.

## [](#next-steps)Next Steps

You can paste the copied definition into a new `.json` file to import it into a new cluster, or use the definition with the [Search REST API](create-search-index-rest-api.md).

To import your Search index definition into a new Couchbase Server cluster through the Web Console, see [Import a Search Index Definition with the Web Console](import-search-index.md).

To import your Search index into a Couchbase Capella cluster, see [Import a Search Index Definition with the Capella UI](../../../cloud/search/import-search-index.md).