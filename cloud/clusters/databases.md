---
title: Configure Your Cluster
description: Understand the different configuration options available to
  customize your Couchbase Capella cluster.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/databases.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:clusters:databases.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/databases.html)

# Configure Your Cluster

> Understand the different configuration options available to customize your Couchbase Capella cluster. 

A Capella cluster is a managed deployment of [Couchbase Server](../../server/current/learn/architecture-overview.md). Clusters are 1 or more instances of Couchbase Server, which run on independent nodes inside Couchbase’s Virtual Private Cloud (VPC) and your chosen cloud provider region.

Clusters exist inside [projects](../projects/projects.md). You can create projects inside your [organization](../organizations/organizations.md) to control user access to your specific clusters.

## [](#cluster-configuration-options)Cluster Configuration Options

When you [Create A Paid Cluster](create-database.md), you can configure the following options:

* Your cluster name and description
* [A basic cluster option](#option)
* [Cloud service provider, region, and CIDR block](#cloud-provider)
* [Couchbase Server version](#cluster-version)
* [Services and Service Groups](#couchbase-services)
* [Nodes](#nodes)
* [Compute configuration](#compute)
* [Storage configuration](#storage)
* [Support Plan](#plan)
* [Availability Zones](#availability)

After you create a cluster, if you want to [Modify a Paid Cluster](modify-database.md), you can only change:

* Your cluster name and description
* [Support Plan](#plan)
* [Your cluster recovery authorization](../billing/support-pre-auth.md)
* [Services and Service Groups](#couchbase-services)
* [Compute configuration](#compute)
* [Storage configuration](#storage)
* [Your deletion protection settings](modify-database.md#deletion-protection)

### [](#option)Basic Cluster Options

When you create a new paid cluster, you can choose a basic option to automatically choose some of your cluster’s settings:

| Cluster Option  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Single Node** | Deploy a cluster on a single node configuration. Single Node clusters are best for prototyping or learning. You can only use a single [Service Group](#couchbase-services) and a single [Availability Zone](#availability).                                                                                                                                                                                                                                                                                          |
| **Multi-Node**  | Deploy a cluster on a Multi-Node configuration by choosing from one of the available pre-configured templates for a 3 node, 5 node, or 7 node cluster. Using the Multi-Node option helps you quickly configure multiple [Service Groups](#couchbase-services) and choose the best [compute](#compute) and [storage](#storage) configuration. Multi-Node clusters also support multiple [Availability Zones](#availability).                                                                                          |
| **Custom**      | Deploy a cluster with a custom configuration suited to your needs. Custom configurations are best for heavy, enterprise workloads. Create [Service Groups](#couchbase-services) and assign a specific number of [nodes](#nodes) to each Group. You can also customize the [compute](#compute) and [storage](#storage) for the nodes in each Group. By default, Custom configurations start with 4 Service Groups with a total of 9 nodes. Custom clusters also support multiple [Availability Zones](#availability). |

### [](#cloud-provider)Cloud Service Provider, Region, and CIDR Block

Capella offers cluster deployments through the following Cloud Service Providers (CSPs):

* [Amazon Web Services (AWS)](../reference/aws.md)
* [Google Cloud Platform (GCP)](../reference/gcp.md)
* [Microsoft Azure](../reference/azure.md)

Your chosen CSP for your cluster changes your available configuration options, such as the region where you deploy your cluster, [compute](#compute) options, and the [disk type, storage size, and IOPS](#storage) for your [nodes](#nodes).

For the available regions for each CSP, see:

* [AWS Supported Regions](../reference/aws.md#supported-regions)
* [GCP Supported Regions](../reference/gcp.md#supported-regions)
* [Azure Supported Regions](../reference/azure.md#supported-regions)

Your chosen region can change your available [Availability Zone](#availability) options.

You can choose to customize the CIDR block for your Capella cluster or leave it as the default value. Use IPv4 syntax to define your CIDR block for your cluster.

> [!TIP]
> If you plan to use [private networks (VPC or VNet Peering)](../clouds/private-network.md) with your Capella cluster, make sure to customize your CIDR block to avoid overlap between your VPC CIDR and Capella.

### [](#cluster-version)Supported Couchbase Server Version

For the best experience with your Couchbase Capella cluster, always create and deploy a new cluster with the latest version of [Couchbase Server](#home::server.adoc).

The latest supported version of Couchbase Server for Capella operational clusters is 8.0.

You can choose a previous version of Couchbase Server to maintain compatibility with existing applications.

Capella deploys new and upgraded clusters with the latest available patch version available for each minor Couchbase Server release automatically. Capella provides version upgrades for clusters when they become available.

> [!NOTE]
> [Organization Owners](../organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Owners](../projects/project-roles.md#project-owner-role) can schedule certain upgrade maintenance jobs when they become available. To see the upgrades available to you, go to [Schedule a Maintenance Job](upgrade-database.md#schedule-maintenance-jobs).

For more information about how to upgrade or schedule maintenance for a cluster, see [Upgrading a Cluster](upgrade-database.md).

#### [](#guardrails)Couchbase Server Guardrails

For safe and reliable cluster operations, and to minimize the severity of cluster outages, Capella clusters using Couchbase Server 7.6 or later have guardrails in place. These guardrails proactively monitor for specific system thresholds. When a cluster meets these thresholds, these guardrails automatically prevent the following cluster operations, which during these conditions can put the cluster at severe risk of outage and downtime:

* Bucket writes
* Bucket creation
* Collection creation
* Topology changes that involve rebalancing

Server-level enforcement thresholds are designed to ensure the optimal and reliable usage of available system resources by various workloads. These thresholds are as follows:

| Cluster Metric                           | Threshold               |
| ---------------------------------------- | ----------------------- |
| Data Service Resident Ratio (Couchstore) | <= 1%                   |
| Data Service Resident Ratio (Magma)      | <= 0.1%                 |
| Free Disk Space                          | <= 4%                   |
| \# of Buckets                            | <= 0.2 cores per bucket |

### [](#couchbase-services)Services and Service Groups

Use Services to use and maintain your data on your Capella cluster.

Deploy Services through Service Groups, which can contain 1 or more [nodes](#nodes):

* If you chose the [Single Node option](#single), you can create a single Service Group on a single node.
* If you chose the [Multi-Node option](#multi) you can choose a pre-configured set of Services and nodes to add to your cluster. You can choose to add or remove specific Services from your configuration.
* If you chose the [Custom option](#custom), you can create multiple Service Groups and assign a specific number and node configuration for each Service Group, up to a maximum of 27 nodes across all Service Groups.

For more information about the default node and Service Group configurations, see [Node Configuration](#nodes).

You can deploy, maintain, and provision Services independently with Multi-Dimensional Scaling and customize your nodes to suit each Service.

The following Services can be deployed on a Capella cluster:

| Service               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Further Information                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Data Service**      | Use the Couchbase Data Service to store, set, and retrieve data items with a key on your Capella cluster. Every cluster must have at least 1 [node](#nodes) running the Data Service. It’s recommended to run the Data Service on at least 3 nodes in a production environment. Make sure to deploy the Data Service on a virtual machine that has a large amount of memory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [Manage Your Data](data-service/data-service.md)                                                                                     |
| **Query Service**     | Use the Query Service to run queries on your data with the [SQL++ query language](../n1ql/n1ql-language-reference/index.md) and get results. To use the Query Service, you must deploy the Data Service and the Index Service. The Query Service requires a minimum of 2 nodes for best results in a production environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [Query Data with SQL++](../n1ql/query.md)                                                                                            |
| **Index Service**     | Use the Index Service to create primary and secondary indexes on your data and get better query performance with the Query Service. The Index Service requires a minimum of 2 nodes for best results in a production environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Primary and Secondary Index Reference](../indexes/indexing-overview.md)                                                             |
| **Search Service**    | Use the Search Service to create Search indexes and add near real-time search capabilities to your applications. Search indexes support search for structured or unstructured text, vectors, dates, numbers, CIDR notations, and geospatial data. The Search Service requires a minimum of 2 nodes for best results in a production environment. You cannot deploy the Search Service on a [Single Node](#single) cluster using the 2vCPU 8 GB RAM [compute configuration](#compute). To use the Search Service on a Single Node cluster, you must use the 4vCPU 16 GB RAM configuration.                                                                                                                                                                                                                                                                                                               | [Add Search to Your Application](../search/search.md) [Vector Search Using Search Vector Indexes](../vector-search/vector-search.md) |
| **Eventing Service**  | Use the Eventing Service to create custom JavaScript snippets that run in response to document mutations or as scheduled by timers. These custom code snippets can support near real-time handling of data changes. The Eventing Service requires a minimum of 2 nodes for best results in a production environment. You cannot deploy the Eventing Service on a [Single Node](#single) cluster using the 2vCPU 8 GB RAM [compute configuration](#compute). To use the Eventing Service on a Single Node cluster, you must use the 4vCPU 16 GB RAM configuration.                                                                                                                                                                                                                                                                                                                                       | [Run a Function on Data Change](../eventing/eventing-overview.md)                                                                    |
| **Analytics Service** | Use the Analytics Service to analyze large datasets with complex analytical queries. The Analytics Service supports large join, set, aggregation, and grouping operations, which can be long-running use a lot of memory and CPU resources. You can create shadow copies of the data you want to analyze and link from external data sources. The Analytics Service uses the SQL++ for Analytics query language. For more information about SQL++ for Analytics, see the [SQL++ for Analytics Reference](../../server/current/analytics/1%5Fintro.md). The Analytics Service requires a minimum of 2 nodes for best results in a production environment. You cannot deploy the Analytics Service on a [Single Node](#single) cluster using the 2vCPU 8 GB RAM [compute configuration](#compute). To use the Analytics Service on a Single Node cluster, you must use the 4vCPU 16 GB RAM configuration. | [Analyze Large Datasets](analytics-service/analytics-service.md)                                                                     |

> [!NOTE]
> You can only add a Service once to a cluster.

### [](#nodes)Node Configuration

Add and configure nodes in a Capella cluster to change the computing resources available to your [Service Groups](#couchbase-services).

A single Service Group can contain 1 or more nodes. All nodes in a Service Group share the same [Compute Configuration](#compute) and [Storage Configuration](#storage).

| Cluster Option  | Available Node Configurations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Single Node** | 1 node with the Data Service, Index Service, and Query Service. If you choose the default [compute configuration](#single-compute), you can add the Search, Analytics, or Eventing Services.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Multi-Node**  | Choose between: **3 nodes** with 1 Service Group for the Data Service, Query Service, and Index Service **5 nodes** with 2 Service Groups: Service Group 1: Data Service with 3 nodes Service Group 2: Query and Index Service with 2 nodes **7 nodes** with the choice between 2 Service Group Configurations Option 1 Service Group 1: Data Service with 3 nodes Service Group 2: Query Service with 2 nodes Service Group 3: Index Service with 2 nodes Option 2 Service Group 1: Data Service with 3 nodes Service Group 2: Query and Index Service with 2 nodes Service Group 3: Search Service with 2 nodes |
| **Custom**      | Defaults to 4 Service Groups: Service Group 1: Data Service with 3 nodes Service Group 2: Query Service with 2 nodes Service Group 3: Index Service with 2 nodes Service Group 4: Search Service with 2 nodes Can add up to a maximum of 27 total nodes across all [Service Groups](#couchbase-services)                                                                                                                                                                                                                                                                                                          |

You can add and remove nodes from Services and Service Groups after you deploy your cluster. For more information, see [Add or Remove Nodes](modify-database.md#add-remove-nodes).

### [](#compute)Compute Configuration

For each [Service Group](#couchbase-services) in your Capella cluster, you must choose the compute configuration for your [nodes](#nodes).

Your compute configuration controls the CPU cores and total RAM for each node in that Service Group. RAM is measured in capacity (GB) and CPU is measured by the number of vCPUs.

Different Services might have different CPU and RAM needs. If a Service Group needs more computing resources, you can [change your compute configuration](modify-database.md#change-computee) any time after you deploy your cluster.

> [!TIP]
> Node RAM Allocations
> 
> If you deploy multiple Services in a Service Group, Capella distributes the memory allocated to each node in that group between the operating system and all deployed Services.
> 
> Capella gives 20% of the available RAM on a node to the operating system. It divides the remaining RAM evenly between Services in the Service Group. For example, if there was 25 GB of RAM available on a node in a Service Group that needed to run 3 Services, each Service would get 8.3 GB of RAM (25/3).
> 
> If you plan to run more than 1 Service on the nodes in your Service Groups, make sure to size your nodes with appropriate compute resources. For production clusters, consider running each of your Services with their own dedicated nodes to give them enough RAM.

Your available compute configuration options depend on the your chosen cluster option and cloud service provider (CSP). For more information about the available compute configurations for each cluster option and CSP, see:

* [AWS Compute and Memory](../reference/aws.md#compute-and-memory)
* [GCP Compute and Memory](../reference/gcp.md#compute-and-memory)
* [Azure Compute and Memory](../reference/azure.md#compute-and-memory)

> [!NOTE]
> If you choose a compute configuration that cannot support your [Storage Configuration](#storage), Capella displays a warning.

### [](#storage)Storage Configuration

For each [Service Group](#couchbase-services) in your Capella cluster, you must choose the storage configuration for your [nodes](#nodes).

Your chosen [cluster option](#option) and [cloud service provider (CSP)](#cloud-provider) changes your available storage options. Different CSPs have different storage sizes, available disk types, supported IOPS values, and auto-scaling support.

Your [Compute Configuration](#compute) must be large enough to support your chosen storage configuration. Capella displays a warning if your compute cannot support your chosen storage configuration.

| Cluster Option  | Storage Expandable?                                                                                                                                                                                                                    | Disk Type Configurable?                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | IOPS Configurable?                                                                                                                                                                                                                                                                          |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Single Node** | Storage can only be expanded up to 100 GB with the [Default Compute Configuration](#single-compute)                                                                                                                                    | AWS GP3 only. GCP PD-SSD only. Azure Choose between Premium SSD disk options.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | AWS Your IOPS value depends on your storage. There’s a minimum of 3000 IOPS for all storage options. GCP Your IOPS value is chosen based on your storage size, with 30 read and write IOPS per GB of storage. Azure Your IOPS value is chosen or limited based on your chosen storage size. |
| **Multi-Node**  | Total storage is based on disk type and your chosen cloud provider: [AWS Storage Size](../reference/aws.md#storage-size) [GCP Storage Size](../reference/gcp.md#storage-size) [Azure Storage Size](../reference/azure.md#storage-size) | AWS Choose between GP3 or IO2\. GP3 disks are general-purpose and provide the best balance of price and performance, for provisioning performance and storage capacity independently. IO2 disks have higher performance, more durability, and better reliability. GCP PD-SSD only - best for higher performance with lower latency and more IOPS. Azure Choose between Premium SSD or Ultra disks. Premium SSDs are best for higher performance with lower latency and more IOPS. Ultra Disks are best for intensive, transaction-heavy workloads with low latency and consistent IOPS. | AWS Your IOPS range depends on your disk type. GCP Your IOPS value is chosen based on your storage size, with 30 read and write IOPS per GB of storage. Azure Your IOPS value is chosen or limited based on your chosen storage size.                                                       |
| **Custom**      | Total storage is based on disk type and your chosen cloud provider: [AWS Storage Size](../reference/aws.md#storage-size) [GCP Storage Size](../reference/gcp.md#storage-size) [Azure Storage Size](../reference/azure.md#storage-size) | AWS Choose between GP3 or IO2\. GP3 disks are general-purpose and provide the best balance of price and performance, for provisioning performance and storage capacity independently. IO2 disks have higher performance, more durability, and better reliability. GCP PD-SSD only - best for higher performance with lower latency and more IOPS. Azure Choose between Premium SSD or Ultra disks. Premium SSDs are best for higher performance with lower latency and more IOPS. Ultra Disks are best for intensive, transaction-heavy workloads with low latency and consistent IOPS. | AWS Your IOPS range depends on your disk type. GCP Your IOPS value is chosen based on your storage size, with 30 read and write IOPS per GB of storage. Azure Your IOPS value is chosen or limited based on your chosen storage size.                                                       |

> [!IMPORTANT]
> Adjusting your IOPS value affects performance and cost for your cluster. For AWS GP3, AWS IO2, and Azure Ultra Disk, Capella uses the recommended defaults for your IOPS. You can go higher than the default IOPS value, but you cannot go lower. For more information about IOPS, see [IOPS Defaults](scale-database.md#IOPS-Defaults).

#### [](#auto-scaling-configuration)Auto-Scaling Configuration

Auto-Scale configuration is based on your chosen cloud provider and [cluster option](#option).

##### [](#single-node-clusters)Single Node Clusters

Auto-Scaling is always on for Single Node clusters.

> [!CAUTION]
> Even with Auto-Scale enabled, Couchbase Capella support will contact you to reduce your storage usage if your Single Node cluster exceeds your chosen storage configuration of 50 GB or 100 GB. Try not to exceed your chosen storage configuration when using a Single Node cluster.

AWS clusters can only auto-expand storage once every 6 hours. For more information about AWS storage scaling limitations, see the [AWS limitations documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-volume-requirements.html#elastic-volumes-limitations).

After you expand storage on any cluster, your storage size cannot automatically decrease. To decrease storage capacity, you must replace and rebalance nodes, which can result in data movement and a slower process, based on your data size and available computing resources.

##### [](#multi-node-and-custom-clusters)Multi-Node and Custom Clusters

For Multi-Node or Custom clusters deployed on AWS or GCP, automatic storage scaling is always on. You cannot turn off Auto-Scaling.

AWS clusters can only auto-expand storage once every 6 hours. For more information about AWS storage scaling limitations, see the [AWS limitations documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-volume-requirements.html#elastic-volumes-limitations).

For Multi-Node or Custom clusters deployed on Azure, Auto-Scaling is turned off by default, as it requires replacing and rebalancing nodes. This results in data movement and can affect performance until Auto-Scaling completes. You can choose whether to turn on Auto-Scale, or leave it turned off.

After you expand storage on any cluster, your storage size cannot automatically decrease. To decrease storage capacity, you must replace and rebalance nodes, which can result in data movement and a slower process, based on your data size and available computing resources.

For more information about cluster scaling, see [Cluster Scaling](scale-database.md) or [Storage Auto-Expansion](scale-database.md#Storage-Auto-Expansion).

### [](#plan)Support Plan

Choose the Support Plan for your cluster to change the level of support you receive from Couchbase Capella Support for that cluster.

Your Support Plan affects the hourly billing price for your cluster and can affect your access to some Capella features.

If you pay for your cluster usage with [pre-paid credits](../billing/billing.md#pre-paid-credits), by default, Capella chooses a [Support Plan](../billing/billing.md#support-plans) where you have an available pre-paid credit balance.

If you use pre-paid credits and you deploy a new paid operational cluster that does not have a pre-paid credit balance for your chosen Support Plan, Capella automatically bills you under the [pay-as-you-go system](../billing/billing.md#pay-as-you-go-credits). Capella will warn you before you deploy a new cluster if you choose a Support Plan that [could incur pay-as-you-go charges within your first month of usage](../billing/billing.md#low-credits).

For more information about how to change your Support Plan after you have already deployed a cluster, see [Change a Cluster’s Plan and Support Timezone](../billing/change-support-plan.md).

| Cluster Option  | Available Support Plans                                                           |
| --------------- | --------------------------------------------------------------------------------- |
| **Single Node** | Basic Developer Pro (default selection if no available credit balance)            |
| **Multi-Node**  | Basic Developer Pro (default selection if no available credit balance) Enterprise |
| **Custom**      | Basic Developer Pro Enterprise (default selection if no available credit balance) |

### [](#availability)Availability Zones

Based on your chosen [cluster option](#option), [CSP](#cloud-provider) region, and [Support Plan](#plan), you can choose between a **Single** or **Multiple** Availability Zones for your cluster.

Availability Zones can help minimize downtime and make sure your data remains highly available and fault resistant. It’s recommended to use **Multiple** Availability Zones for production clusters with the Multi-Node or Custom [cluster option](#option).

> [!NOTE]
> Clusters on the **Basic** [Support Plan](#plan) support only a **Single** Availability Zone.

| Cluster Option  | Availability Zones                                               |
| --------------- | ---------------------------------------------------------------- |
| **Single Node** | 1 Availability Zone                                              |
| **Multi-Node**  | Multiple Availability Zones, based on [region](#cloud-provider). |
| **Custom**      | Multiple Availability Zones, based on [region](#cloud-provider). |

#### [](#aws-availability-zones)AWS Availability Zones

If you deploy a cluster on AWS, you can choose the specific Availability Zone or Zones to use with your cluster.

Capella provides the physical zone location names for AWS Availability Zones, using AZ IDs. These IDs may be different from the labels you would see in your own AWS configurations. For more information about AZ IDs, see the [AWS Elastic Compute Cloud documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#az-ids)

## [](#see-also)See Also

See the following pages for more information about managing clusters:

* [Create A Paid Cluster](create-database.md)
* [Modify a Paid Cluster](modify-database.md)
* [Cluster Scaling](scale-database.md)
* [Sizing a Cluster](sizing.md)
* [Delete a Cluster](delete-database.md)