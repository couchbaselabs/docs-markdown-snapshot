---
title: Delete a Cluster
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/delete-database.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/clusters/delete-database.html)

# Delete a Cluster

> Deleting a cluster securely deletes all data. 

> [!TIP]
> You can turn on deletion protection for sensitive clusters to stop accidental deletion. A cluster cannot be deleted from the UI, the [Management API](../management-api-reference/index.md#tag/Clusters/operation/deleteCluster), or external tools like Terraform, when deletion protection is turned on. For more information about deletion protection, see [Change Your Deletion Protection](modify-database.md#deletion-protection). This setting also turns on deletion protection for [App Services](#app-services:deployment/creating-an-app-service.adoc#deletion-protection).

## [](#prerequisites)Prerequisites

> [!IMPORTANT]
> Permissions Required
> 
> You need the [Project Owner](../projects/project-roles.md#project-owner-role) or [Cluster Manager](../projects/project-roles.md#project-cluster-manager-role) role for the project containing the cluster you’re deleting.

## [](#procedure)Procedure

> [!WARNING]
> * Deleting a cluster deletes all of its data.
> * Deleting a cluster deletes its backups.
> * Deleting a cluster is a permanent action which you cannot reverse.

To delete a Couchbase Capella cluster:

1. Open the **Settings** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your settings.
  3. Go to **Settings**.
2. Click **Delete Cluster**.
3. Confirm the cluster delete request:

  1. In the confirmation field, enter the name of the cluster that you want to delete.
  2. Click **Delete Cluster**.

Once you delete a cluster, it’s queued for automatic deletion and remains visible with the Destroying status. This process can take up to 15 minutes.