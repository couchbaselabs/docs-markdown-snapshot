---
title: Export a Search Index Definition from the Capella UI
description: Use the Couchbase Capella UI to export a JSON Search index
  definition for use in another cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/search/pages/export-search-index.adoc
  xref: xref:cloud:search:export-search-index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/search/export-search-index.html)

# Export a Search Index Definition from the Capella UI

> Use the Couchbase Capella UI to export a JSON Search index definition for use in another cluster. 

## [](#prerequisites)Prerequisites

* You have the Search Service enabled on a node in your operational cluster. For more information about how to change Services on your operational cluster, see [Modify a Paid Cluster](../clusters/modify-database.md).
* You have a bucket with scopes and collections in your operational cluster. For more information, see [Manage Buckets](../clusters/data-service/manage-buckets.md).
* You have created a Search index.  
For more information about how to create a Search index, see [Create a Search Index with the Capella UI](create-search-index-ui.md).
* You have logged in to the Couchbase Capella UI.

## [](#procedure)Procedure

To export a Search index definition from the Capella UI:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Operational**.
  * Click your current project name or search for a project and go to **Operational**.
  * Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to work with the Search Service.
3. Go to **Data Tools** **Search**.
4. On the Search index you want to export, click ![download](_images/download.png).

## [](#next-steps)Next Steps

Capella downloads a `.json` file containing the definition for your Search index.

To import your Search index definition into a new Couchbase Server cluster through the Web Console, see [Import a Search Index Definition with the Web Console](../../server/current/search/import-search-index.md).

To import your Search index into a Couchbase Capella cluster, see [Import a Search Index Definition with the Capella UI](import-search-index.md).