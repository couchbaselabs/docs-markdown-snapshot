---
title: Manage Replication Security
description: Configure your Cross Datacenter Replication (XDCR) to securely
  replicate data between source and destination buckets.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/xdcr/manage-xdcr-security.adoc
pubDate: 2026-03-07T03:34:43.923Z
link: xref:cloud:clusters:xdcr/manage-xdcr-security.adoc[]
---

[View original HTML](/cloud/clusters/xdcr/manage-xdcr-security.html)

# Manage Replication Security

> Configure your Cross Datacenter Replication (XDCR) to securely replicate data between source and destination buckets. 

XDCR supports different security models to protect data as it travels between source and target clusters. Data replication can be:

* [Between 2 Capella operational clusters](manage-xdcr-replications.md#between-capella-dbs).
* [From a self-managed cluster to a Capella operational cluster](manage-xdcr-replications.md#from-on-prem-to-capella).
* [From a Capella operational cluster to a self-managed cluster](manage-xdcr-replications.md#replicate-to-self-managed-target).

Capella supports both public and private connectivity, allowing you to secure XDCR based on your network architecture and security requirements. By default, Capella secures data replication between 2 Capella operational clusters. For replications involving a self-managed cluster deployed on-premises or in a non-Capella cloud, your replication security depends on the deployment model and cloud service provider (CSP) of your source and destination clusters.

You can secure your replication using 1 of the following approaches:

* [Public Internet](#public-internet)
* [VPC Peering](#vpc-peering)
* [Private Endpoint Service](#private-endpoints)

Choose the option that best fits your cluster’s configuration and security requirements.

> [!CAUTION]
> Once you create a replication, you cannot modify how its securely routed. To make changes, you need to [create a new replication](manage-xdcr-replications.md#create-replication).

## [](#prerequisites)Prerequisites

* You have created a single node or multi-node cluster that you want to use for replication, either as a source or destination cluster.
* To view and manage replications for a cluster, you need the [Project Owner](../../projects/project-roles.md#project-owner-role) role.
* To create a new replication, you need the [Project Owner](../../projects/project-roles.md#project-owner-role) role for the projects that contain your source cluster and destination cluster.

## [](#public-internet)Replicate Data Over the Public Internet

Capella supports public Internet-based XDCR for all replication configurations with self-managed clusters. Replicating data over the public Internet provides the broadest compatibility, but it does not offer network-level isolation.

> [!NOTE]
> If your replication is between a Capella operational cluster and a self-managed cluster with a different cloud provider or in an on-premises environment, you can only connect through the public Internet.

### [](#enable-replication-over-the-public-internet)Enable Replication Over the Public Internet

If you do not have a private network configured before creating a replication, Capella defaults to TLS-secured, public Internet-based replication.

To enable replication over the public Internet:

1. Create a replication. Choose 1 of the following options and follow the steps for securing replication over the public Internet:

  1. [Create a replication to Capella from a self-managed cluster](manage-xdcr-replications.md#from-on-prem-to-capella).
  2. [Create a replication from Capella to a self-managed cluster](manage-xdcr-replications.md#from-capella-to-self-managed).

## [](#vpc-peering)Replicate Data Over a VPC Peering Connection

VPC Peering can secure XDCR by replicating data over a private network. This approach avoids exposure to the public Internet and provides stronger network isolation than public Internet connectivity.

> [!NOTE]
> You can only use VPC Peering when your replication is between an Capella operational cluster and a self-managed cluster with the same CSP.

### [](#enable-replication-over-vpc-peering)Enable Replication Over VPC Peering

To enable replication over VPC Peering:

1. Configure a VPC Peering Connection. For more information, see [Configure a VPC Peering Connection](../../clouds/private-network.md).
2. Create a replication. Choose 1 of the following options and follow the steps for securing replication over a peered VPC network:

  1. [Create a replication from Capella to a self-managed cluster](manage-xdcr-replications.md#from-capella-to-self-managed).
  2. [Create a replication to Capella from a self-managed cluster](manage-xdcr-replications.md#from-on-prem-to-capella).

## [](#private-endpoints)Replicate Data Over a Private Endpoint Connection

> [!NOTE]
> This is only available upon request from Capella Support. To open a Support ticket, see [Create a Support Ticket](../../support/manage-support.md#create-support-ticket).

Private endpoints expose a service-specific endpoint for XDCR, allowing clusters to replicate without network-level peering or public Internet exposure. [Enabling XDCR over a private endpoint connection](#enable-pe-xdcr) is only available through the [Management REST API](../../management-api-reference/index.md#tag/Private-Endpoint-Service).

For an overview of the Management API, see [Manage Deployments with the Management API](../../management-api-guide/management-api-intro.md).

To enable XDCR over a private endpoint connection, your cluster and replication configurations must meet specific requirements. If your configurations do not meet the requirements for private endpoint security, use [VPC Peering](#vpc-peering).

Replicating data over a private endpoint connection is only available with the following conditions:

| Supported Replications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Supported Clusters                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Additional Requirements                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Replications [from a self-managed cluster to a Capella operational cluster](manage-xdcr-replications.md#from-on-prem-to-capella) with the same [CSP and region](../../clouds/cloud-providers.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Clusters deployed on [AWS](../../reference/aws.md) with either: A source self-managed cluster running Couchbase Server version [7.6.9](../../../server/7.6/release-notes/relnotes.md#release-769) or earlier, or [8.0](../../../server/current/release-notes/relnotes.md#release-801). The destination Capella operational cluster must be co-located with all Services running on every node. The destination cluster is not restricted to a specific version. A source self-managed cluster running Couchbase Server version [7.6.10](../../../server/7.6/release-notes/relnotes.md#release-7610) or [8.0.1](../../../server/current/release-notes/relnotes.md#release-801). The destination Capella operational cluster can use any Service deployment topology and is not restricted to a specific version. | Clusters deployed on [AWS](../../reference/aws.md): Can have a maximum of 20 nodes. If you previously contacted Capella Support to map Query nodes separately with 1:1 node mapping over private endpoints, enabling XDCR over private endpoints limits your cluster to a maximum of 13 nodes.\[[1](#footnote-1)\] Require an additional inbound rule allowing ports 20091-20117 from the same VPC IPv4 CIDR when configuring an AWS PrivateLink connection. This rule is in addition to the existing port ranges required for the private endpoint. For more information, see [Add an Inbound Rule](../../security/add-aws-private-link.md#add-inbound-rule). |
| Clusters deployed on [GCP](../../reference/gcp.md) with either: A source self-managed cluster running Couchbase Server version [7.6.9](../../../server/7.6/release-notes/relnotes.md#release-769) or earlier, or [8.0](../../../server/current/release-notes/relnotes.md#release-801). The destination Capella operational cluster must be co-located with all Services running on every node. The destination cluster is not restricted to a specific version. A source self-managed cluster running Couchbase Server version [7.6.10](../../../server/7.6/release-notes/relnotes.md#release-7610) or [8.0.1](../../../server/current/release-notes/relnotes.md#release-801). The destination Capella operational cluster can use any Service deployment topology and is not restricted to a specific version. | There are no additional requirements for GCP clusters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

\[[1](#node-caution)\] Enabling both 1:1 Query mapping and XDCR requires the Data and Query Services to have dedicated listeners on each node, which reduces the number of nodes you can have to 13\. For more information, contact [Capella Support](../../support/manage-support.md#create-support-ticket).

### [](#enable-pe-xdcr)Enable Replication Over a Private Endpoint Connection

To enable replication over a private endpoint connection:

1. Enable XDCR with the [Management REST API](../../management-api-reference/index.md#tag/Private-Endpoint-Service):

  1. If you’re enabling the private endpoint service for the first time, use the [POST v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService](../../management-api-reference/index.md#tag/Private-Endpoint-Service/operation/enablePrivateEndpointService) endpoint.
  2. If you want to enable XDCR after enabling the private endpoint service, use the [PUT /v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}/privateEndpointService](../../management-api-reference/index.md#tag/Private-Endpoint-Service/operation/updatePrivateEndpointService) endpoint.
2. [Create a replication to Capella from a self-managed cluster](manage-xdcr-replications.md#from-on-prem-to-capella) and follow the steps for securing a replication over a private endpoint.

## [](#see-also)See Also

* [Cross Data Center Replication (XDCR)](xdcr.md)
* [Manage Replications](manage-xdcr-replications.md)
* [Management API Reference](../../management-api-reference/index.md)