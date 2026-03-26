---
title: Create A Paid Cluster
description: Create a cluster to store and access data in Couchbase Capella.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/create-database.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cloud:clusters:create-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/create-database.html)

# Create A Paid Cluster

> Create a cluster to store and access data in Couchbase Capella. 

To modify options for an existing Capella cluster, see [Modify a Paid Cluster](modify-database.md).

> [!NOTE]
> This section does not apply to Capella free tier operational clusters. To get started with a free tier operational cluster in Capella, see [Create an Account and Deploy Your Free Tier Operational Cluster](../get-started/create-account.md).

## [](#prerequisites)Prerequisites

* You have a project in your organization. For more information about projects, see [Manage Projects](../projects/manage-projects.md).
* You have the **Project Owner** or **Cluster Manager** role for that project. For more information about project roles, see [Project Roles](../projects/project-roles.md).
* Capella allows only one free tier operational cluster per organization at any time. These clusters also have limited configuration options.

## [](#procedure)Procedure

To create a new cluster in a Capella project:

1. In the navigation breadcrumbs in the Capella UI, click your organization name and go to **Operational**.
2. Click **\+ Create Cluster**.
3. Choose the project where you want to create your new cluster.  
> [!TIP]  
> To find a project or filter your list of projects, enter a project name in the **Project** list.
4. Click **Continue**.
5. Choose your **Cluster Option** to pre-configure settings for your cluster. For more information about the available cluster options, see [Basic Cluster Options](databases.md#option).
6. Enter a **Cluster Name** and **Description**.
7. Choose your preferred Cloud Service Provider and **Region**. For more information about the available Cloud Service Providers for Capella, see [Cloud Service Provider, Region, and CIDR Block](databases.md#cloud-provider).
8. Enter a **CIDR Block** for your cluster, or accept the default. For more information about how to configure a CIDR block, see [Cloud Service Provider, Region, and CIDR Block](databases.md#cloud-provider).  
> [!NOTE]  
> Restrict public access  
>  
> If Couchbase has given your organization access to the restrict public access feature, this option appears here. When you restrict public access, you're restricting access to your cluster only through Capella's private networking options. For more information, see [Restrict Public Access](../security/security.md#public-access).
9. Choose a version of Couchbase Server to deploy on your cluster. For more information about Couchbase Server versions, see [Supported Couchbase Server Version](databases.md#cluster-version).
10. Do one of the following:

  1. For a **Free** cluster, choose a cloud service provider and your preferred region.
  2. For a **Single Node** cluster, choose your Services and node compute and storage amount.
  3. For a **Multi-Node** cluster, choose a base node template, then customize your node's compute, storage, and IOPS configuration.
  4. For a **Custom** cluster, add Service Groups, then assign nodes with a specific compute, storage, and IOPS configuration to each Group.  
For more information, see [Services and Service Groups](databases.md#couchbase-services), [Node Configuration](databases.md#nodes), [Compute Configuration](databases.md#compute), or [Storage Configuration](databases.md#storage).
11. Choose a **Support Plan** for your cluster. For more information about Support Plans, see [Support Plan](databases.md#plan).  
If you pay for your usage with [pre-paid credits](../billing/billing.md#pre-paid-credits), Couchbase recommends choosing a plan where you have an available pre-paid credit balance. Capella displays a warning if you choose a plan with no pre-paid credits, or that has a [low credit balance](../billing/billing.md#low-credits) and might incur [pay-as-you-go credit charges](../billing/billing.md#pay-as-you-go-credits).
12. Choose the **Availability Zone** configuration for your cluster. For more information about Availability Zone configurations, see [Availability Zones](databases.md#availability).
13. Click **Create Cluster**.

> [!NOTE]
> Accounts with a paid plan can deploy a free tier operational cluster alongside their paid operational clusters.

## [](#next-steps)Next Steps

Capella creates and deploys your cluster in your chosen cloud provider's region. The process typically takes less than 5 minutes, but this can change based on cluster size and cloud provider performance.

After your cluster shows a status of **Healthy**, you can:

* [Choose which IP addresses can connect to your cluster](allow-ip-address.md)
* [Create cluster access credentials](manage-database-users.md)
* [Connect to your cluster](../get-started/connect.md)
* [Create and manage buckets for your data](data-service/manage-buckets.md)
* [Create and manage scopes and collections for your data](data-service/scopes-collections.md)
* [Explore other ways to start developing with Capella](../develop/intro.md)