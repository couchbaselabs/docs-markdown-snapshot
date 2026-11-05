---
title: Microsoft Azure
description: Operational Insights supports deploying clusters onto Microsoft Azure.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Operational Insights Capella
    version: ""
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/reference/pages/azure.adoc
  xref: xref:analytics:reference:azure.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights-cloud/reference/azure.html)

# Microsoft Azure

> Operational Insights supports deploying clusters onto Microsoft Azure. 

This page describes the regions and configurations available when using Operational Insights with Azure.

## [](#supported-regions)Supported Regions

Operational Insights supports the following Azure regions.

| Azure Region | Location               | Availability Zones |
| ------------ | ---------------------- | ------------------ |
| **eastus2**  | East US 2 (Virginia)   | Single or multiple |
| **westus2**  | West US 2 (Washington) | Single only        |

> [!NOTE]
> Sweden Central is no longer supported. Existing clusters in this region continue to run, but you need to migrate them to a supported region.

## [](#availability-zones)Availability Zones

Each Operational Insights cluster on Azure must run in a single region. Within that region, you can deploy the cluster in a single Availability Zone (AZ) or across multiple Availability Zones. Deploying across multiple Availability Zones helps keep your data highly available and protect against downtime. The available options depend on the region. For the options in each region, see [Supported Regions](#supported-regions).

When you create a cluster, select **Single** or **Multiple** under **Availability Zones** in the Operational Insights UI.

> [!NOTE]
> The option to deploy a single node is only available for clusters that use a single Availability Zone and the Developer Pro plan.

## [](#configuration-options)Configuration Options

Clusters deployed onto Azure can be customized to suit your needs.

### [](#nodes)Nodes

Clusters can have a minimum of 1 node and a maximum of 32 nodes.

### [](#compute)Compute

Operational Insights provides user-managed compute configurations for databases deployed onto Azure. The compute resources are used when loading data, executing queries, and performing other DML operations. You can manually scale compute to increase or decrease performance.

Operational Insights supports the following compute configurations for databases deployed onto Azure.

__Table 1\. Azure compute configurations__
| vCPU     | Memory |
| -------- | ------ |
| 4 vCPUs  | 32 GB  |
| 8 vCPUs  | 32 GB  |
| 8 vCPUs  | 64 GB  |
| 16 vCPUs | 64 GB  |
| 16 vCPUs | 128 GB |

## [](#see-also)See Also

* [Azure geographies](https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/)
* [Azure availability zones](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-overview)

### [](#next-steps)Next Steps

To create or modify an Operational Insights cluster deployed onto Azure, see:

* [Create a Cluster](../admin/prepare-project.md)