---
title: Microsoft Azure
description: Couchbase Capella supports deploying clusters onto Microsoft Azure.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/reference/pages/azure.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/reference/azure.html)

# Microsoft Azure

> Couchbase Capella supports deploying clusters onto Microsoft Azure. 

Couchbase Capella provides fully managed Couchbase Server clusters that you can deploy onto Microsoft Azure. This page describes the various regions and configurations available to you when using Capella with Azure.

## [](#supported-regions)Supported Regions

Couchbase Capella’s fully managed DBaaS supports the following Azure regions.

* North America
* South America
* Europe, Middle East, and Africa
* Asia Pacific

| Azure Region                     | Location                                      | Ultra Disk Support | Free Tier Support \[[1](#footnote-1)\] |
| -------------------------------- | --------------------------------------------- | ------------------ | -------------------------------------- |
| **eastus**                       | East US (Virginia)                            | **✔**              | **✔**                                  |
| **eastus2**                      | East US 2 (Virginia)                          | **✔**              |                                        |
| **centralus**                    | Central US (Iowa)                             | **✔**              |                                        |
| **southcentralus**               | South Central US (Texas) \[[2](#footnote-2)\] |                    |                                        |
| **canadacentral**                | Canada Central (Toronto)                      | **✔**              |                                        |
| **westus2** \[[2](#footnote-2)\] | West US 2 (Washington)                        | **✔**              |                                        |
| **westus3**                      | West US 3 (Arizona)                           | **✔**              |                                        |

| Azure Region    | Location                 | Ultra Disk Support | Free Tier Support \[[1](#footnote-1)\] |
| --------------- | ------------------------ | ------------------ | -------------------------------------- |
| **brazilsouth** | Brazil South (São Paulo) |                    |                                        |

| Azure Region                           | Location                         | Ultra Disk Support | Free Tier Support \[[1](#footnote-1)\] |
| -------------------------------------- | -------------------------------- | ------------------ | -------------------------------------- |
| **germanywestcentral**                 | Germany West Central (Frankfurt) | **✔**              |                                        |
| **norwayeast**                         | Norway East (Oslo)               |                    |                                        |
| **uksouth**                            | UK South (London)                | **✔**              |                                        |
| **westeurope** \[[2](#footnote-2)\]    | West Europe (Netherlands)        | **✔**              |                                        |
| **northeurope** \[[2](#footnote-2)\]   | North Europe (Ireland)           | **✔**              |                                        |
| **swedencentral**                      | Sweden Central (Gävle)           | **✔**              | **✔**                                  |
| **switzerlandnorth**                   | Switzerland North (Zürich)       |                    |                                        |
| **uaenorth**                           | UAE North (Dubai)                |                    |                                        |
| **spaincentral** \[[2](#footnote-2)\]  | Spain Central (Madrid)           |                    |                                        |
| **francecentral** \[[2](#footnote-2)\] | France Central (Paris)           |                    |                                        |

| Azure Region      | Location                         | Ultra Disk Support | Free Tier Support \[[1](#footnote-1)\] |
| ----------------- | -------------------------------- | ------------------ | -------------------------------------- |
| **australiaeast** | Australia East (New South Wales) | **✔**              |                                        |
| **koreacentral**  | Korea Central (Seoul)            |                    | **✔**                                  |
| **centralindia**  | Central India (Pune)             |                    |                                        |
| **eastasia**      | East Asia (Hong Kong)            |                    |                                        |
| **southeastasia** | South East Asia (Singapore)      | **✔**              |                                        |

\[[1](#supported-regions)\] A [free tier account](https://cloud.couchbase.com/sign-up) can deploy an operational cluster to this Azure region.

\[[2](#supported-regions)\] This Azure region is available only on request. For more information, [contact Couchbase Support](../support/manage-support.md#create-support-ticket).

## [](#availability-zones)Availability Zones

All the Microsoft Azure regions that Capella supports have Availability Zones. Availability Zones are data centers that Azure groups together within a region. They’re maintained in separate physical locations within a region and isolated from failures in other zones.

Capella can automatically distribute cluster nodes across multiple Availability Zones in a region for the highest availability. For example, a 3-node cluster could deploy 1 node to each of the 3 Availability Zones in a region. A failure in 1 of these Availability Zones wouldn’t impact the other 2 nodes that could remain in operation.

Except for free tier operational clusters, Capella clusters deploy with a minimum of 3 [nodes](#nodes). Clusters deployed with Azure use Couchbase Server 7.1 or later, which supports [unequal server groups](#learn:clusters-and-availability:groups.adoc#server-groups-and-vbuckets).

The **Multiple Zones** option is the default when creating clusters using the Developer Pro or Enterprise [Support Plans](../billing/billing.md#support-plans).

> [!NOTE]
> The option to deploy across multiple Azure Availability Zones is only available for clusters that use the Developer Pro or Enterprise Support Plans. Clusters using the Basic Support Plan deploy all nodes to the same Availability Zone.

## [](#configuration-options)Configuration Options

Customize the clusters you deploy with Microsoft Azure to fit your requirements using the following configuration options:

* [Number of nodes](#nodes)
* [Compute (vCPU and memory)](#compute-and-memory)
* [Disk type and storage](#storage)

### [](#nodes)Nodes

Clusters have a minimum of 3 nodes and a maximum of 27.

> [!NOTE]
> As they’re intended for evaluation purposes only, free tier operational clusters only include 1 node.

Clusters consist of Service Groups that include the services deployed and system resources. Each Service Group has a node quantity representing the number of nodes in the cluster with that configuration. Individual Service Groups can have between 2 and 27 nodes but cannot collectively exceed 27\. The Service Group that includes the [Data Service](../clusters/data-service/data-service.md) requires at least 3 nodes.

### [](#compute-and-memory)Compute and Memory

The following compute configuration options are available for clusters on Microsoft Azure.

| vCPU                         | Memory  |
| ---------------------------- | ------- |
| 2 vCPUs \[[2](#footnote-2)\] | 8 GiB   |
| 4 vCPUs                      | 16 GiB  |
| 4 vCPUs                      | 32 GiB  |
| 8 vCPUs                      | 16 GiB  |
| 8 vCPUs                      | 32 GiB  |
| 8 vCPUs                      | 64 GiB  |
| 16 vCPUs                     | 32 GiB  |
| 16 vCPUs                     | 64 GiB  |
| 16 vCPUs                     | 128 GiB |
| 20 vCPUs                     | 160 GiB |
| 32 vCPUs                     | 64 GiB  |
| 32 vCPUs                     | 128 GiB |
| 32 vCPUs                     | 256 GiB |
| 48 vCPUs                     | 96 GiB  |
| 48 vCPUs                     | 192 GiB |
| 48 vCPUs                     | 384 GiB |
| 64 vCPUs                     | 128 GiB |
| 64 vCPUs                     | 256 GiB |
| 64 vCPUs                     | 512 GiB |
| 72 vCPUs                     | 144 GiB |

\[[2](#azure-configurations)\] This configuration is only available for [free tier](https://cloud.couchbase.com/sign-up) and paid single node operational clusters.

### [](#storage)Storage

The Capella clusters you deploy onto Azure can use Premium SSDs (v1) or Ultra disks.

When using Azure’s Premium SSDs (v1), the amount of storage available per node in your cluster depends on the chosen disk type. For example, if you want the 256 GiB of storage, you could choose the P15 disk configuration. If you’re using the Ultra Disk type, you can choose between fixed storage size options.

> [!NOTE]
> Free tier operational clusters only allow 10 GB of data storage.

IOPS (input/output operations per second) measures the storage speed of a cluster. Premium storage disk speed is based on the chosen disk type and cannot be separately set. Ultra Disk speed can be set, but the possible range depends on the chosen disk size.

For clusters deployed on Microsoft Azure, you can enable or disable disk auto-expansion for each Service Group in the cluster. Auto-expansion for Azure requires replacing and rebalancing nodes, which results in data movement. For details, see [Storage Auto-Expansion](../clusters/scale-database.md#Storage-Auto-Expansion).

* For more information about Premium SSDs and disk types that Capella offers, see [Premium SSD Type](#premium-ssd).
* For more information about Ultra disks and the configuration options that Capella offers, see [Ultra Disks](#ultra-disk).

#### [](#premium-ssd)Premium SSD

Azure premium SSDs are best for high-performance cluster needs that require lower latency and more IOPS. The following Azure premium SSD sizes are available in Capella:

| Type | Disk size (GiB) | Provisioned IOPS per disk \[[3](#footnote-3)\] |
| ---- | --------------- | ---------------------------------------------- |
| P6   | 64              | 240                                            |
| P10  | 128             | 500                                            |
| P15  | 256             | 1,100                                          |
| P20  | 512             | 2,300                                          |
| P30  | 1,024           | 5,000                                          |
| P40  | 2,048           | 7,500                                          |
| P50  | 4,096           | 7,500                                          |
| P60  | 8,192           | 16,000                                         |

\[[3](#premium-disks)\] The guaranteed number of IOPS per the disk specification. See [Premium SSD size](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types#premium-ssd-size) for more information.

#### [](#ultra-disk)Ultra Disk

Azure Ultra Disks are best for intensive and transaction-heavy workloads. They offer the lowest latency and consistent IOPS/throughput while providing scalability. Ultra Disks are available to clusters hosted in Azure regions that support it. To see what regions support this option, see the [regions list](#supported-regions).

The Ultra Disk option allows you to choose a storage size and IOPS. By default, this is 64 Gib, but you choose from the following:

| Disk size (GiB)                         | IOPS Cap |
| --------------------------------------- | -------- |
| 64                                      | 19,200   |
| 128                                     | 38,400   |
| 256                                     | 76,800   |
| 512                                     | 80,000   |
| 1,024 — 15,360 (In increments of 1 TiB) | 80,000   |

> [!IMPORTANT]
> Adjusting the IOPS rate affects performance and cost. When creating or modifying a cluster with the Azure Ultra Disk storage option, Capella uses recommended defaults for the IOPS field. You can replace a default IOPS value with one higher than the default but not lower. For the recommended IOPS values for clusters using Azure Ultra Disks with typical enterprise workloads, see [IOPS Defaults](../clusters/scale-database.md#IOPS-Defaults).

## [](#integrations-with-azure)Integrations with Azure

Couchbase Capella has further integrations with Azure, allowing you and your applications to use Capella more effectively with existing assets:

* Azure Virtual Network: [Configure a Private Network with Azure](../clouds/private-network.md#prerequisites).
* Azure Private Link: [Add an Azure Private Link Connection](../security/add-azure-private-link.md)
* Microsoft Entra ID: [Configure SSO authentication to the Capella UI with Azure AD](../organizations/ui-auth/add-sso-auth.md#configure-federated-sso-authentication).

## [](#see-also)See Also

For related information on Microsoft Azure, see:

* [Azure geographies](https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/#geographies)
* [Azure Disks — Premium SSDs](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types#premium-ssds)
* [Azure Disks — Ultra disks](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types#ultra-disks)

### [](#next-steps)Next Steps

To create or modify a Couchbase Capella cluster deployed onto Azure, see:

* [Create a cluster](../clusters/create-database.md)
* [Modify a cluster](../clusters/modify-database.md)