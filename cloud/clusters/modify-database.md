---
title: Modify a Paid Cluster
description: Review, modify, and rename Couchbase Capella clusters.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/modify-database.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:clusters:modify-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/modify-database.html)

# Modify a Paid Cluster

> Review, modify, and rename Couchbase Capella clusters. 

Use the procedures on this page to modify an existing Couchbase Capella cluster. If you want to learn about scaling a cluster, see [Cluster Scaling](scale-database.md).

> [!NOTE]
> For scaling a Single Node cluster, see the limitations of different [cluster configuration options](#modify-existing-service).

## [](#prerequisites)Prerequisites

* You have the [Project Owner](../projects/project-roles.md#project-owner-role) or [Cluster Manager](../projects/project-roles.md#project-cluster-manager-role) role for the project with the cluster you’re modifying.

## [](#view-config)View Cluster Node Configurations

Before modifying a cluster, you can review a list of all individual nodes running on it. This list includes the hostname, status, and services associated with each node. It also describes each node’s CPU, RAM, and disk usage. Node statuses are Normal, Deploying, and Unhealthy.

1. Open the **Settings** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your settings.
  3. Go to **Settings**.
2. In the navigation pane, click **Nodes**:  
![Database nodes page](_images/database-settings-service.png)  
To modify service configurations, see [Modify the Cluster Configuration](#modify-existing-service).

## [](#modify-existing-service)Modify the Cluster Configuration

Cluster configuration options depend on the chosen cloud provider. For more information about the configuration options available for each cloud provider, see [Amazon Web Services (AWS)](../reference/aws.md) and [Google Cloud Platform (GCP)](../reference/gcp.md).

### [](#add-service)Add a Service

> [!TIP]
> You can enable Couchbase Capella’s [Storage Auto-Expansion](#clusters:modules/scale-cluster.adoc#Storage-Auto-Expansion) feature to automatically increase your storage capacity as your data grows.

Service groups allow you to create node configurations for specified [Couchbase services](databases.md#couchbase-services).

1. Open the **Settings** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your settings.
  3. Go to **Settings**.
2. In the navigation pane, click **Services**.
3. Use the **Services** list to select the services you want to add:  
![Adding services to cluster](_images/adding-services.png)  
You can also add another service group by clicking **Add Service Group**.  
Once you add a service to a new or existing service group, you may need to adjust its hardware configuration. For more information about sizing a cluster, see [Sizing a Cluster](sizing.md).  
> [!TIP]  
> Node RAM Allocations  
>  
> If you deploy multiple Services in a Service Group, Capella distributes the memory allocated to each node in that group between the operating system and all deployed Services.  
>  
> Capella gives 20% of the available RAM on a node to the operating system. It divides the remaining RAM evenly between Services in the Service Group. For example, if there was 25 GB of RAM available on a node in a Service Group that needed to run 3 Services, each Service would get 8.3 GB of RAM (25/3).  
>  
> If you plan to run more than 1 Service on the nodes in your Service Groups, make sure to size your nodes with appropriate compute resources. For production clusters, consider running each of your Services with their own dedicated nodes to give them enough RAM.
4. If you have no other changes, [review and apply the new configuration](#apply-changes).

> [!NOTE]
> Limitations
> 
> * You cannot add a service when that service already exists on the cluster. To deploy the Search, Analytics, or Eventing Services on a Single Node cluster, you must use a 4vCPU 16 GB RAM compute configuration. For more information, see [Compute Configuration](databases.md#compute).
> * You cannot add additional Service Groups to Single Node clusters. You can add and redistribute them when you scale out your cluster.

### [](#remove-service)Remove a Service

1. Open the **Settings** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your settings.
  3. Go to **Settings**.
2. In the navigation pane, click **Services**.
3. To remove a service, click the **x** icon for the service you’re removing in the **Services** list:  
![Deleting a cluster service](_images/deleting-service.png)
4. If you have no other changes, [review and apply the new configuration](#apply-changes).

> [!NOTE]
> Limitations
> 
> You cannot remove the Data Service.

### [](#add-remove-nodes)Add or Remove Nodes

1. Open the **Settings** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your settings.
  3. Go to **Settings**.
2. In the navigation pane, click **Services**.
3. Using the **Nodes** list in the service group you’re modifying, choose a new number of nodes for this configuration.
4. If you have no other changes, [review and apply the new configuration](#apply-changes).

> [!NOTE]
> Limitations
> 
> * Services require a minimum of 2 nodes, except for the Data Service, which needs a minimum of 3.
> * A cluster can have a maximum of 27 nodes.
> * A Single Node cluster must scale out to at least 3 nodes for the first Service Group. For additional Service Groups, the 2 node option is available.
> * After scaling out, you cannot scale back to a Single Node cluster. You can only scale back to a minimum of 3 nodes.

### [](#change-compute)Change Compute

1. Open the **Settings** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your settings.
  3. Go to **Settings**.
2. In the navigation pane, click **Services**.
3. Use the **Compute** drop-down in the service group you’re modifying to choose a new compute instance type.  
The compute dictates the number of vCPUs and memory provisioned for each node in a service group.
4. If you have no other changes, [review and apply the new configuration](#apply-changes).

> [!NOTE]
> Limitations
> 
> * The minimum compute configuration required to scale out a Single Node cluster is 4vCPUs 16 GB RAM.
> * Your instance type options are limited to those available in the **Compute** list of the Service Group you’re modifying.

### [](#change-disk)Change Disk Type

1. Open the **Settings** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your settings.
  3. Go to **Settings**.
2. In the navigation pane, click **Services**.
3. Use the **Disk Type** control to change disk types for the configuration you’re modifying.
4. If you have no other changes, [review and apply the new configuration](#apply-changes).

> [!NOTE]
> Limitations
> 
> * **GCP**: Only supports PD-SSD.

### [](#increase-storage)Increase Storage

1. Open the **Settings** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your settings.
  3. Go to **Settings**.
2. In the navigation pane, click **Services**.
3. Using the **Storage** box of the service group you’re modifying, enter the amount of storage you want per node for this configuration. If the cluster uses Azure, you must choose a new disk type to increase storage.
4. If you have no other changes, [review and apply the new configuration](#apply-changes).

> [!NOTE]
> Limitations
> 
> Storage cannot be removed from a service configuration once added.
> 
> * **Azure**: You can only increase storage by choosing a new disk type.

### [](#change-iops)Change IOPS

> [!IMPORTANT]
> Adjusting the IOPS rate affects performance and cost. When creating or modifying a cluster with AWS gp3, AWS io2, or Azure Ultra Disk and choosing a storage option, Capella uses recommended defaults for the IOPS field. You can replace the default IOPS value with one higher than the default but not lower. For the recommended IOPS values for clusters using AWS gp3, AWS io2, or Azure Ultra Disk, see [IOPS Defaults](scale-database.md#IOPS-Defaults).

1. Open the **Settings** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your settings.
  3. Go to **Settings**.
2. In the navigation pane, click **Services**.
3. Using the **IOPS** box, enter the IOPS value for the service group you’re modifying.  
This field isn’t shown when a cluster uses GCP as its cloud provider. If you’re using Azure’s Premium SSD disk type, you can’t change the value of this field.
4. If you have no other changes, [review and apply the new configuration](#apply-changes).

> [!NOTE]
> Limitations
> 
> * **GCP**: IOPS (Input/Output Operations per Second) isn’t a directly configurable value. Instead, it’s automatically set at 30 reads and 30 writes IOPS per GB of storage provisioned.
> * **Azure**: IOPS for the Premium SSD (P) disk type are based on the chosen Premium SSD disk size. The IOPS for the Ultra disk type can be set, but the possible range depends on the chosen storage size.

## [](#apply-changes)Review and Apply Changes

1. Review and update configuration  
All the changes you make to a cluster are on the **Service** page. Review this new configuration to ensure it meets your requirements.  
Any warnings about your proposed changes appear on the **Service** page and can prevent you from updating the configuration until you resolve them. If you need to discard your changes, click **Cancel**.
2. Once you have reviewed the changes, click **Save**.

The cluster [rebalances](scale-database.md#rebalance) and redistributes service data over the new superset of nodes. The amount of time taken for the new nodes to rebalance into the cluster depends on the service of the new nodes, and how much data is redistributed. The cluster remains available during the rebalance, but you can’t make further changes until the rebalancing is complete.

## [](#rename-database)Rename a Cluster

1. Open the **Settings** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your settings.
  3. Go to **Settings**.
2. In the **Cluster Name** field, enter a new name for the cluster.
3. Click **Save**.

## [](#deletion-protection)Change Your Deletion Protection

Turn on deletion protection to stop accidental deletion of a cluster from the Capella UI, the [Management API](../management-api-reference/index.md#tag/Clusters/operation/deleteCluster), or any other external tools, such as Terraform. If you turn on deletion protection, Capella will also automatically turn on deletion protection for any [App Services](#app-services:index.adoc) linked to your cluster.

Cluster deletion protection also prevents bucket deletion or [bucket flushing](data-service/manage-buckets.md#flush).

You can change this setting even when a cluster is [turned off](off-on-database.md).

> [!IMPORTANT]
> To change deletion protection settings, you must have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) role in your organization, or one of the following [project roles](../projects/project-roles.md) for the project that contains your cluster:
> 
> * [Project Owner](../projects/project-roles.md#project-owner-role)
> * [Cluster Manager](../projects/project-roles.md#project-cluster-manager-role)

To change the deletion protection setting for a cluster:

1. Open the **Settings** page for your cluster:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to make changes to your settings.
  3. Go to **Settings**.
2. Select or clear **Enable Deletion Protection**.
3. Click **Save**.

## [](#see-also)See Also

* [Sizing a Cluster](sizing.md)
* [Cluster Scaling](scale-database.md)
* [Upgrading a Cluster](upgrade-database.md)
* [Delete a Cluster](delete-database.md)