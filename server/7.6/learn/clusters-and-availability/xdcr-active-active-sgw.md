---
title: XDCR Active-Active with Sync Gateway
description: You can use XDCR with Sync Gateway mobile clusters in a
  bi-directional, active-active replication, but you must make sure that both
  the Server and the Sync Gateway versions support this option. Otherwise, using
  XDCR with Sync Gateway buckets in a bi-directional replication can cause data
  corruption.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/learn/pages/clusters-and-availability/xdcr-active-active-sgw.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.6@server:learn:clusters-and-availability/xdcr-active-active-sgw.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/learn/clusters-and-availability/xdcr-active-active-sgw.html)

# XDCR Active-Active with Sync Gateway

> You can use XDCR with Sync Gateway mobile clusters in a bi-directional, active-active replication, but you must make sure that both the Server and the Sync Gateway versions support this option. Otherwise, using XDCR with Sync Gateway buckets in a bi-directional replication can cause data corruption. 

## [](#xdcr-active-active-sgw-intro)Introduction

> [!NOTE]
> To set up XDCR bi-directional replication with Sync Gateway (SGW), the minimum required version for Server is 7.6.6 and SGW is 4.0.0\.

In the versions earlier than Server 7.6.6 and Sync Gateway (SGW) 4.0+, only an active-passive setup was supported with both XDCR and SGW. XDCR Active-Active replication with Sync Gateway for XDCR-Mobile interoperability configuration is introduced in the Server 7.6.6 version, where you can configure an active-active XDCR setup with Sync Gateway (SGW) and mobile applications both on the XDCR source and target clusters.

For more information about how Sync Gateway 4.0+ version works with Couchbase Server's XDCR, see [XDCR - Server Compatibility](../../../../sync-gateway/current/server-compatibility/server-compatibility-xdcr.md).

> [!IMPORTANT]
> Here are a few limitations to the _XDCR Active-Active with Sync Gateway_ feature.
> 
> * If you use the _user created extended attributes (user xattrs)_ in your documents, and you have more than 10 user xattrs in a document, then you cannot use the feature _XDCR Active-Active with Sync Gateway_. This is due to an internal limitation of managing extended attributes in a document. If you try to use the feature _XDCR Active-Active with Sync Gateway_ when you have more than 10 user xattrs in your document, the XDCR replication **silently skips** replicating that document. As a result, the data in the replication-skipped document will not be consistent between the target and source clusters. The only way you will know this skip occured is because the Prometheus stat `subdoc_cmd_docs_skipped` will be incremented and the document will _not_ be consistent between the target and source.
> * If you use Eventing service functions that update documents in XDCR-replicated buckets (Eventing source bucket mutations), ensure your functions do not cause continuous replication loops. In bi-directional active-active XDCR environments, Eventing functions that trigger document updates can lead to "ping-pong" replication unless you implement logic to prevent infinite loops. Always add safeguards to avoid redundant updates and unwanted replication behavior in bi-directional setups. For more information, see [XDCR Active-Active and Eventing](#sync-gateway:xdcr-active-active-eventing.adoc).

You can configure XDCR Active-Active with Sync Gateway for XDCR-Mobile interoperability using one of the following methods:

* [Greenfield deployment](#xdcr-active-active-sgw-greenfield-deployment): Set up a new active-active configuration with both XDCR and SGW.
* [Upgrading an existing setup](#xdcr-active-active-sgw-upgrade): Convert an existing active-passive XDCR-SGW configuration to an active-active XDCR-SGW setup.

> [!NOTE]
> When using the feature _XDCR Active-Active with Sync Gateway_, where Sync Gateway version is 4.0\* or a later version and Server version is 7.6.6, the replication target XDCR inbound user must have the RBAC roles, [XDCR Inbound](../security/roles.md#xdcr-inbound) role and [Data Writer](../security/roles.md#data-writer) role.

## [](#xdcr-active-active-sgw-prerequisites)Prerequisites

Set the bucket property `enableCrossClusterVersioning` to use the setting `mobile=Active` during the processes [Create a Replication](../../manage/manage-xdcr/create-xdcr-replication.md) and [Manage XDCR](../../manage/manage-xdcr/xdcr-management-overview.md). To enable the bucket property `enableCrossClusterVersioning` using the REST API, see [Modify the bucket property enableCrossClusterVersioning](xdcr-enable-crossclusterversioning.md#modify-enablecrossclusterversioning) or [Example: Turning on enableCrossClusterVersioning, when Editing](../../rest-api/rest-bucket-create.md#example-enablecrossclusterversioning-edit).

## [](#xdcr-active-active-sgw-greenfield-deployment)Greenfield Deployment

To configure a new active-active XDCR with Sync Gateway setup, do the following:

1. Create two clusters on Server 7.6.6 or a later version with _all_ the nodes of the clusters. For example, cluster A and cluster B (or you can upgrade the existing Server clusters to 7.6.6 or a later version).
2. Create buckets, for example, B1 and B2 in cluster A and cluster B respectively, between which XDCR will be set up. Now, do the following:

  1. Enable the ECCV setting on B1\. All the mutations in B1 will have a new metadata called HLV.
  2. Enable the ECCV setting on B2\. All the mutations in B2 will have a new metadata called HLV.  
  > [!NOTE]  
  > ECCV refers to the bucket property `enableCrossClusterVersioning`. If there are more than two buckets in the replication topology, you must enable ECCV for all those buckets.
3. Create an XDCR from B1 to B2 by setting `mobile=Active`. Also, create an XDCR from B2 to B1 by setting `mobile=Active`.  
For information about creating an XDCR by setting `mobile=Active` through the REST API, see [Creating a Replication](../../rest-api/rest-xdcr-create-replication.md).  
For information about creating an XDCR by setting `mobile=Active` from the UI, see [Create an XDCR Replication with the UI](../../manage/manage-xdcr/create-xdcr-replication.md#create-an-xdcr-replication-with-the-ui).
4. Configure SGW 4.0+ version on each cluster, cluster A and cluster B.

This setup can handle application traffic on both buckets B1 and B2 of the respective clusters along with SGW import into both the buckets simultaneously.

## [](#xdcr-active-active-sgw-upgrade)Upgrading an existing setup

You can convert an existing active-passive XDCR-Sync Gateway (SGW) setup into an active-active XDCR-Sync Gateway setup.

For illustration, there are two clusters, A and B. An SGW is connected to cluster A and this cluster is active. Cluster B is passive with XDCR setup from bucket B1 in cluster A to bucket B2 in cluster B. The current application traffic should be only on bucket B1 of cluster A.

![xdcr active sgw before upgrade](../_images/clusters-and-availability/xdcr-active-sgw-before-upgrade.png) 

Figure 1\. Replication before upgrade: XDCR Active-Passive with SGW

1. Upgrade both clusters A and B with _all_ the nodes of the clusters to Server 7.6.6 or a later version.
2. Enable ECCV on bucket B1\. All the mutations in B1, after this point of time, will have a new metadata called HLV.  
> [!NOTE]  
> ECCV refers to the bucket property `enableCrossClusterVersioning`. If there are more than two buckets in the replication topology, you must enable ECCV for all those buckets.
3. Enable ECCV on bucket B2\. All the mutations in B2, after this point of time, will have a new metadata called HLV.  
> [!NOTE]  
> If there are more than two buckets in the replication topology, you must enable ECCV for all those buckets.
4. Update the replication settings to `mobile=Active` of the already existing XDCR from B1 to B2.  
You can use the REST API or the XDCR UI to update an existing replication. For information about using the REST API to modify the replication settings for an existing replication, see [Change Settings for an Existing Replication to Set mobile=Active](../../rest-api/rest-xdcr-adv-settings.md#change-existing-replication-with-mobile-active) in [Managing Advanced Settings](../../rest-api/rest-xdcr-adv-settings.md).
5. Create an XDCR from B2 to B1 with the replication settings as `mobile=Active`.
6. Upgrade SGW on cluster A to the version 4.0+.
7. Connect SGW version 4.0+ to cluster B.
8. Enable application active traffic on cluster B.

This setup can handle application traffic on both buckets B1 and B2 of the respective clusters along with SGW import into both the buckets simultaneously.

This is an illustration of the final configuration:

![xdcr active sgw after upgrade](../_images/clusters-and-availability/xdcr-active-sgw-after-upgrade.png) 

Figure 2\. Replication after upgrade: XDCR Active-Active with SGW