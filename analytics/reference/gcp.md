---
title: Google Cloud Platform (GCP)
description: Capella Analytics supports deploying clusters onto Google Cloud Platform (GCP).
pubDate: 2026-09-10T04:23:38.872Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/reference/pages/gcp.adoc
  xref: xref:analytics:reference:gcp.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/reference/gcp.html)

# Google Cloud Platform (GCP)

> Capella Analytics supports deploying clusters onto Google Cloud Platform (GCP). 

This page describes the various regions and configurations that are available to you when using Capella Analytics with GCP.

## [](#supported-regions)Supported Regions

* Americas
* Europe
* Asia Pacific

| GCP Region      | Location                 |
| --------------- | ------------------------ |
| **us-central1** | US Central (Iowa)        |
| **us-east1**    | US East (South Carolina) |
| **us-east4**    | US East (North Virgina)  |

| GCP Region       | Location    |
| ---------------- | ----------- |
| **europe-west1** | Belgium     |
| **europe-west3** | Frankfurt   |
| **europe-west4** | Netherlands |

| GCP Region          | Location  |
| ------------------- | --------- |
| **asia-southeast1** | Singapore |

## [](#availability-zones)Availability Zones

Every Capella Analytics cluster must be deployed across a single availabilty zone (AZ) or two availability zones in a single region to ensure they tolerate failure of an entire availability zone. You can select the desired number of availability zone deployments from Capella Analytics.

## [](#configuration-options)Configuration Options

Clusters deployed onto GCP can be customized to suit your needs.

### [](#nodes)Nodes

Clusters can have a minimum of 1 node and a maximum of 32 nodes.

> [!NOTE]
> The option to deploy 1 node is only available for clusters that deploy in a single availability zone and DevPro plan.

### [](#compute)Compute

Capella Analytics provides user-managed compute configurations for databases deployed onto GCP. The compute resources are used when loading data, executing queries, and performing other DML operations. You can manually scale compute to increase or decrease performance.

Capella Analytics supports the following compute configurations for GCP:

__Table 1\. GCP compute configurations__
| vCPU     | Memory |
| -------- | ------ |
| 4 vCPUs  | 32 GB  |
| 8 vCPUs  | 32 GB  |
| 8 vCPUs  | 64 GB  |
| 16 vCPUs | 64 GB  |
| 16 vCPUs | 128 GB |

## [](#see-also)See Also

* [GCP Regions and Zones](https://cloud.google.com/compute/docs/regions-zones)
* [GCP storage performance limits](https://cloud.google.com/compute/docs/disks/performance#performance%5Flimits)

### [](#next-steps)Next Steps

To create or modify a Capella Analytics cluster deployed onto GCP, see:

* [Create a Cluster](../admin/prepare-project.md)