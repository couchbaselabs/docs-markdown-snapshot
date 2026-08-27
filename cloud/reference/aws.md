---
title: Amazon Web Services (AWS)
description: Couchbase Capella supports deploying clusters onto Amazon Web Services (AWS).
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/reference/pages/aws.adoc
  xref: xref:cloud:reference:aws.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/reference/aws.html)

# Amazon Web Services (AWS)

> Couchbase Capella supports deploying clusters onto Amazon Web Services (AWS). 

Couchbase Capella provides fully managed Couchbase Server clusters that can be deployed onto AWS. This page describes the various regions and configurations that are available to you when using Capella with AWS.

## [](#supported-regions)Supported Regions

Couchbase Capella's fully managed DBaaS supports the following AWS regions.

* Americas
* Europe
* Middle East and Africa
* Asia Pacific
* Australia and New Zealand

| AWS Region       | Location                  |
| ---------------- | ------------------------- |
| **us-east-1**    | US East (N. Virginia)     |
| **us-east-2**    | US East (Ohio)            |
| **us-west-2**    | US West (Oregon)          |
| **ca-central-1** | Canada (Central)          |
| **sa-east-1**    | South America (São Paulo) |
| **mx-central-1** | Mexico (Mexico City)      |

| AWS Region       | Location           |
| ---------------- | ------------------ |
| **eu-central-1** | Europe (Frankfurt) |
| **eu-west-1**    | Europe (Ireland)   |
| **eu-west-2**    | Europe (London)    |
| **eu-west-3**    | Europe (Paris)     |
| **eu-north-1**   | Europe (Stockholm) |
| **eu-south-1**   | Europe (Milan)     |
| **eu-central-2** | Europe (Zurich)    |

| AWS Region       | Location              |
| ---------------- | --------------------- |
| **il-central-1** | Israel (Tel Aviv)     |
| **me-central-1** | Middle East (UAE)     |
| **me-south-1**   | Middle East (Bahrain) |
| **af-south-1**   | Africa (Cape Town)    |

| AWS Region         | Location                 |
| ------------------ | ------------------------ |
| **ap-southeast-1** | Asia Pacific (Singapore) |
| **ap-northeast-1** | Asia Pacific (Tokyo)     |
| **ap-northeast-2** | Asia Pacific (Seoul)     |
| **ap-south-1**     | Asia Pacific (Mumbai)    |
| **ap-east-1**      | Asia Pacific (Hong Kong) |
| **ap-south-2**     | Asia Pacific (Hyderabad) |
| **ap-southeast-3** | Asia Pacific (Jakarta)   |
| **ap-southeast-7** | Asia Pacific (Thailand)  |

| AWS Region         | Location              |
| ------------------ | --------------------- |
| **ap-southeast-2** | Australia (Sydney)    |
| **ap-southeast-4** | Australia (Melbourne) |

## [](#availability-zones)Availability Zones

Every AWS region includes a number of independent Availability Zones. These consist of one or more discrete data centers that are isolated from failures in other Availability Zones. Capella can automatically distribute cluster nodes across multiple Availability Zones in a region for the highest availability. Every operational cluster in Capella is deployed with a minimum of 3 [nodes](#nodes).

The **Multiple Availability Zones** option is the default when creating clusters using the Developer Pro or Enterprise [Support Plans](../billing/billing.md#support-plans).

> [!NOTE]
> The option to deploy across multiple AWS Availability Zones is only available for clusters that use the Developer Pro or Enterprise Support Plans. Clusters using the Basic Support Plan deploy all nodes to the same Availability Zone.

## [](#configuration-options)Configuration Options

Clusters deployed onto AWS can be customized to suit your needs.

### [](#nodes)Nodes

Clusters have a minimum of 3 nodes and a maximum of 27.

Clusters consist of Service Groups that include the Couchbase services deployed and system resources. Each Service Group has a node quantity to represent the number of nodes in the cluster with that configuration. Individual Service Groups can have between 2 and 27 nodes but cannot collectively exceed 27\. The Service Group that includes the [Data Service](../clusters/data-service/data-service.md) requires at least 3 nodes.

> [!NOTE]
> As they're intended for evaluation purposes only, free tier operational clusters only include 1 node. For paid single-node clusters deployed under a Basic or Developer Pro plan, Couchbase does not offer SLAs.

### [](#compute-and-memory)Compute and Memory

Capella provides the following compute configurations for clusters deployed onto AWS.

__Table 1\. AWS compute configurations__
| vCPU                         | Memory |
| ---------------------------- | ------ |
| 2 vCPUs \[[1](#footnote-1)\] | 8 GB   |
| 4 vCPUs                      | 16 GB  |
| 4 vCPUs                      | 32 GB  |
| 8 vCPUs                      | 16 GB  |
| 8 vCPUs                      | 32 GB  |
| 8 vCPUs                      | 64 GB  |
| 16 vCPUs                     | 32 GB  |
| 16 vCPUs                     | 64 GB  |
| 16 vCPUs                     | 128 GB |
| 32 vCPUs                     | 64 GB  |
| 32 vCPUs                     | 128 GB |
| 32 vCPUs                     | 256 GB |
| 48 vCPUs                     | 96 GB  |
| 48 vCPUs                     | 192 GB |
| 48 vCPUs                     | 384 GB |
| 64 vCPUs                     | 128 GB |
| 64 vCPUs                     | 256 GB |
| 64 vCPUs                     | 512 GB |

\[[1](#aws-configurations)\] This configuration is only available for [free tier](https://cloud.couchbase.com/sign-up) and paid single node operational clusters.

### [](#storage-size)Storage Size

Capella clusters deployed onto AWS use the SSDs in AWS EBS. You have the option to choose between the GP3 and IO2 volume types per Service Group.

The amount of storage available per node in your cluster is configurable from a minimum of 50 GB to a maximum of 16 TB.

> [!NOTE]
> Free tier operational clusters only allow 10 GB of data storage.

Clusters deployed on AWS support disk auto-expansion. For details, see [Storage Auto-Expansion](../clusters/scale-database.md#Storage-Auto-Expansion).

### [](#storage-speed)Storage Speed

Each Service Group has an input/output operations per second (IOPS) rate. This storage speed is configurable based on the volume type used:

* **gp3**: 3000 to 16000 IOPS
* **io2**: 3000 to 64000 IOPS

> [!IMPORTANT]
> Adjusting the IOPS rate affects performance and cost. When creating or modifying a cluster with gp3 or io2 volume types and choosing a storage option, Capella uses recommended defaults for the IOPS field. You can replace the default IOPS value with one higher than the default but not lower. For the recommended IOPS values for clusters using AWS gp3 or io2 volume types with typical enterprise workloads, see [IOPS Defaults](../clusters/scale-database.md#IOPS-Defaults).

## [](#see-also)See Also

* [AWS Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions%5Faz/)
* [Amazon EBS SSD-backed volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#solid-state-drives)

### [](#next-steps)Next Steps

To create or modify a Couchbase Capella cluster deployed onto AWS, see:

* [Create a cluster](../clusters/create-database.md)
* [Modify a cluster](../clusters/modify-database.md)