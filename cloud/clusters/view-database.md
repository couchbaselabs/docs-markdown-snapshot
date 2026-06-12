---
title: View Your Clusters
description: You can view, copy, or download a list of all Couchbase Capella
  clusters in a project, along with their status and key configuration details.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/view-database.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:cloud:clusters:view-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/view-database.html)

# View Your Clusters

> You can view, copy, or download a list of all Couchbase Capella clusters in a project, along with their status and key configuration details. 

## [](#prerequisites)Prerequisites

* You have at least the [Cluster Viewer](../projects/project-roles.md#project-cluster-viewer-role) role for the project containing the clusters you want to view, copy, or download.

## [](#view-your-clusters)View Your Clusters

To view the clusters in your organization or project:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Operational**.
  * Click your current project name or search for a project and go to **Operational**.
2. To find a specific cluster:

  * Use the search bar to find your cluster by **Name**.
  * Use filters to narrow the list of clusters by:

    * Project
    * Cloud service provider ([AWS](../reference/aws.md), [GCP](../reference/gcp.md), or [Azure](../reference/azure.md))
    * [Cluster status](scale-database.md#cluster-status)

The **Operational Clusters** page lists all clusters in your organization or selected project. Each row displays:

* Cluster name
* Current status
* Cloud service provider (CSP) and region
* Linked App Service, if applicable
* Name of the user who created the cluster
* Couchbase Server version

## [](#copy-or-download-the-cluster-list)Copy or Download the Cluster List

> [!NOTE]
> Check your filters before downloading or copying the cluster table. Your active filters determine which clusters appear in the downloaded or copied data.

To copy the current page of the cluster table to your clipboard in TSV (tab-separated values) format, click . To include all pages, download the cluster table instead.

To download the cluster table as a CSV (comma-separated values) file, click . This includes clusters across all pages if the table is paginated.

When you copy or download the cluster table, each row displays:

* Cluster name
* Associated project name
* Current status
* Cluster type
* Cloud service provider (CSP) and region
* Linked App Service, if applicable
* Name of the user who created the cluster
* Couchbase Server version
* Cluster activities

## [](#see-also)See Also

* [Create A Paid Cluster](create-database.md)
* [Modify a Paid Cluster](modify-database.md)
* [Cluster Scaling](scale-database.md)
* [Upgrading a Cluster](upgrade-database.md)
* [Delete a Cluster](delete-database.md)
* [Project Roles](../projects/project-roles.md)