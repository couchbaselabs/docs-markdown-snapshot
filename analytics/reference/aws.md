---
title: Amazon Web Services (AWS)
description: Capella Analytics supports deploying clusters onto Amazon Web Services (AWS).
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/reference/pages/aws.adoc
  xref: xref:analytics:reference:aws.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/reference/aws.html)

# Amazon Web Services (AWS)

> Capella Analytics supports deploying clusters onto Amazon Web Services (AWS). 

Capella Analytics provides fully managed analytical databases that can be deployed onto AWS. This page describes the various regions and configurations that are available to you when using Capella Analytics with AWS.

## [](#supported-regions)Supported Regions

Capella Analytics supports the following AWS regions.

* Americas
* Europe
* Asia Pacific

| AWS Region    | Location              |
| ------------- | --------------------- |
| **us-east-1** | US East (N. Virginia) |
| **us-east-2** | US East (Ohio)        |
| **us-west-2** | US West (Oregon)      |

| AWS Region       | Location           |
| ---------------- | ------------------ |
| **eu-central-1** | Europe (Frankfurt) |
| **eu-west-1**    | Europe (Ireland)   |
| **eu-north-1**   | Europe (Stockholm) |

| AWS Region         | Location                 |
| ------------------ | ------------------------ |
| **ap-southeast-1** | Asia Pacific (Singapore) |
| **ap-southeast-2** | Asia Pacific (Sydney)    |
| **ap-south-1**     | Asia Pacific (Mumbai)    |
| **ap-northeast-1** | Asia-Pacific (Tokyo)     |

## [](#availability-zones)Availability Zones

Every AWS region includes a number of independent availability zones. These consist of one or more discrete data centers that are isolated from failures in other availability zones. Capella Analytics can automatically distribute cluster [nodes](#nodes) across multiple availability zones in a region for the highest availability.

The **Single Availability Zone** option is the default when creating clusters using the Developer Pro or Enterprise [Service Plans](#billing:billing.adoc#support-plans).

## [](#configuration-options)Configuration Options

Clusters deployed onto AWS can be customized to suit your needs.

### [](#nodes)Nodes

Clusters can have a minimum of 1 node and a maximum of 32 nodes.

> [!NOTE]
> The option to deploy across multiple AWS availability zones is only available for clusters that deploy with a minimum of 2 nodes.

### [](#compute-and-memory)Compute and Memory

Capella Analytics provides the following compute configurations for databases deployed onto AWS.

__Table 1\. AWS compute configurations__
| vCPU     | Memory |
| -------- | ------ |
| 4 vCPUs  | 32 GB  |
| 8 vCPUs  | 32 GB  |
| 8 vCPUs  | 64 GB  |
| 16 vCPUs | 64 GB  |
| 16 vCPUs | 128 GB |

## [](#see-also)See Also

* [AWS Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions%5Faz/)

### [](#next-steps)Next Steps

To create or modify a Capella Analytics cluster deployed onto AWS, see:

* [Create a Cluster](../admin/prepare-project.md)