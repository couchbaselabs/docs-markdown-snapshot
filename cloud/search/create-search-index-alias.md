---
title: Create a Search Index Alias with the Capella UI
description: Use a Search index alias to run a Search query across multiple
  buckets, scopes, or Search indexes.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/create-search-index-alias.adoc
  xref: xref:cloud:search:create-search-index-alias.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/search/create-search-index-alias.html)

# Create a Search Index Alias with the Capella UI

> Use a Search index alias to run a Search query across multiple buckets, scopes, or Search indexes. 

For more information about Search index aliases, see [Create Search Index Aliases](index-aliases.md).

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have created at least one Search index. For more information, see [Create a Search Index with the Capella UI](create-search-index-ui.md).
* You have logged in to the Couchbase Capella UI.

## [](#procedure)Procedure

To create a Search index alias with the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with the Search Service.
3. Click **Create Search Alias**.

## [](#next-steps)Next Steps

To customize a Search index, see [Search Index Features](customize-index.md).

To run a search and test the contents of your Search index or Search index alias, see [Run A Simple Search with the Capella UI](simple-search-ui.md).