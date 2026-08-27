---
title: Create a Cluster
description: This topic includes the procedures you follow to create Capella
  Analytics clusters.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/prepare-project.adoc
  xref: xref:analytics:admin:prepare-project.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/admin/prepare-project.html)

# Create a Cluster

> This topic includes the procedures you follow to create Capella Analytics clusters. 

Within a Capella organization, you set up projects to which you can add one or more Capella Analytics clusters.

* Settings that you configure at the organization level apply to all projects.
* Settings that you configure at the project level apply to all of the Capella Analytics clusters in that project.

If you choose to add both Capella Analytics clusters and Capella operational databases to the same project, your project-level settings apply to both.

## [](#projects-and-clusters)Projects and Clusters

To get started, an authorized user for the organization sets up one or more projects using the Capella UI. Projects organize and manage clusters. For example, you could create separate projects for your production and development environments, for different business units within your company, or for each of your applications. See [Create a Project](../../cloud/projects/manage-projects.md#create-project).

After you create a project, you set up one or more clusters. A cluster is a cloud storage environment dedicated to use by Capella Analytics services. See [Create a Capella Analytics Cluster](#cluster).

Before you can set up any data sources and collections, or connect an app to Capella Analytics services, you must use the Capella UI to [create a project](../../cloud/projects/manage-projects.md#create-project) and a Capella Analytics cluster.

## [](#prerequisites)Prerequisites

To create a Capella Analytics cluster, you must have the Project Owner or Project Manager project role and at least one project must exist. See [Project Roles](../../cloud/projects/project-roles.md).

### [](#cluster)Create a Capella Analytics Cluster

1. In the Capella UI, select the **Capella Analytics** tab.
2. Click **Create Cluster**.
3. Select a project and then click **Continue**. The Create Capella Analytics Cluster page opens.

  * Select a region.
  * Provide an identifying name for the cluster and an optional description.
  * Select a **Compute** option to dictate the number of vCPUs and memory provisioned for each node.
  * Select from 1 to 32 **Nodes**.
4. Click **Create Cluster**. The Capella Analytics page opens with a list of clusters. Your new cluster displays with a status of **Deploying**.

For each new cluster, Capella Analytics supplies a `Default` database with a `Default` scope. When your cluster is ready, you can click its name to open the workbench. See [Query and Explore with the Workbench](../query/workbench.md).

You can now create a link and add a collection to the `Default.Default` database and scope, or create your own databases and scopes before adding links and collections. See [Access and Organize Data in Capella Analytics Services](../sources/database-objects.md).

## [](#see-also)See Also

* [Manage Organizations and Access](../../cloud/organizations/organization-projects-overview.md)
* [Use a Couchbase SDK with Capella Analytics Services](../dev/use-sdk.md)
* [Access and Organize Data in Capella Analytics Services](../sources/database-objects.md)