---
title: Create a Search Index with the Capella UI
description: You can create a Search index using the Couchbase Capella UI to
  generate a properly formatted Search index definition.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/create-search-index-ui.adoc
  xref: xref:cloud:search:create-search-index-ui.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/search/create-search-index-ui.html)

# Create a Search Index with the Capella UI

> You can create a Search index using the Couchbase Capella UI to generate a properly formatted Search index definition. 

You must create a Search index before you can [run a search](simple-search-ui.md) with the Search Service.

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have a bucket with scopes and collections in your operational cluster. For more information, see [Manage Buckets](../clusters/data-service/manage-buckets.md).
* You have logged in to the Couchbase Capella UI.

## [](#procedure)Procedure

To use the Capella UI to create a Search index:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with the Search Service.
3. Go to **Data Tools** **Search**.
4. Click **Create Search Index**.
5. (Optional) To add additional customization options to your Search index, click **Enable Advanced Mode**.
6. In the **Index Name** field, enter a name for the Search index.  
> [!NOTE]  
> Your index name must start with an alphabetic character (a-z or A-Z). It can only contain alphanumeric characters (a-z, A-Z, or 0-9), hyphens (-), or underscores (\_).  
>  
> For Couchbase Server version 7.6 and later, your index name must be unique inside your selected bucket and scope. You cannot have 2 indexes with the same name inside the same bucket and scope.
7. In the **Bucket** and **Scope** lists, choose the bucket and scope where you want to create your Search index.
8. In the **Collections** list, select the collections you want to include in your Search index, or accept the default of **All**.  
If you select specific collections, you can only use documents from these collections in your Search index.
9. In the **Choose a Collection or Document Field** panel, click a collection name.
10. Click **Index everything from: $COLLECTION\_NAME**.
11. Click **Index All Fields**.
12. Click **Add to Index**.
13. (Optional) [Choose to add and configure advanced settings on your Search index](set-advanced-settings.md).
14. (Optional) Expand **Replicas & Partitions** and configure your **Number of Replicas** and **Number of Partitions**.  
For more information, see [Replica and Partition Settings](customize-index.md#replica).
15. Click **Create Index**.

## [](#next-steps)Next Steps

Your Search index will contain documents that match the collection type mapping you specified. You can run a search against your index, but it's recommended that you create more [specific type mappings](create-type-mapping.md) to improve performance and reduce the index size.

For more information about the different features you can add to your Search index to improve performance and search results, see [Search Index Features](customize-index.md).

For more information about how to run a search, see [Run A Simple Search with the Capella UI](simple-search-ui.md).