---
title: Microsoft Azure
description: Capella Analytics supports deploying clusters onto Microsoft Azure.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/reference/pages/azure.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:analytics:reference:azure.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/reference/azure.html)

# Microsoft Azure

> Capella Analytics supports deploying clusters onto Microsoft Azure. 

This page describes the regions and configurations available when using Capella Analytics with Azure.

## [](#supported-regions)Supported Regions

| Azure Region      | Location               |
| ----------------- | ---------------------- |
| **swedencentral** | Sweden Central (Gävle) |

## [](#availability-zones)Availability Zones

Each Capella Analytics cluster on Azure must be deployed across a single Availability Zone (AZ) or two Availability Zones in a single region to verify fault tolerance. You can select the desired number of AZ deployments from the Capella Analytics UI.

> [!NOTE]
> The option to deploy a single node is only available for clusters that use a single Availability Zone and the Developer Pro plan.

## [](#configuration-options)Configuration Options

Clusters deployed onto Azure can be customized to suit your needs.

### [](#nodes)Nodes

Clusters can have a minimum of 1 node and a maximum of 32 nodes.

### [](#compute)Compute

Capella Analytics provides user-managed compute configurations for databases deployed onto Azure. The compute resources are used when loading data, executing queries, and performing other DML operations. You can manually scale compute to increase or decrease performance.

Capella Analytics supports the following compute configurations for databases deployed onto Azure.

__Table 1\. Azure compute configurations__
| vCPU     | Memory |
| -------- | ------ |
| 4 vCPUs  | 32 GB  |
| 8 vCPUs  | 32 GB  |
| 8 vCPUs  | 64 GB  |
| 16 vCPUs | 64 GB  |
| 16 vCPUs | 128 GB |
| 32 vCPUs | 128 GB |
| 32 vCPUs | 256 GB |

## [](#see-also)See Also

* [Azure geographies](https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/)
* [Azure availability zones](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)

### [](#next-steps)Next Steps

To create or modify a Capella Analytics cluster deployed onto Azure, see:

* [Create a Cluster](../admin/prepare-project.md)