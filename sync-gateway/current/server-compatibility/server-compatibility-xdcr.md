---
title: XDCR&#8201;&#8212;&#8201;Server Compatibility
description: How Sync Gateway works with Couchbase Server's <em>Cross Data
  Center Replication</em> (<em>XDCR</em>).
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/server-compatibility/pages/server-compatibility-xdcr.adoc
pubDate: 2026-03-12T03:41:48.873Z
link: xref:sync-gateway:server-compatibility:server-compatibility-xdcr.adoc[]
---

[View original HTML](/sync-gateway/current/server-compatibility/server-compatibility-xdcr.html)

# XDCR&#8201;&#8212;&#8201;Server Compatibility

> How Sync Gateway works with Couchbase Server’s _Cross Data Center Replication_ (_XDCR_).  
> Sync Gateway provides multiple approaches for replicating mobile data across clusters, with capabilities evolving significantly in version 4.0 to support bi-directional XDCR for active-active deployments.

_Related topics_: [Buckets](server-compatibility-buckets.md) | [Collections](server-compatibility-collections.md) | [Eventing](server-compatibility-eventing.md) | [Transactions](server-compatibility-transactions.md) | [XDCR](server-compatibility-xdcr.md) | [Backup and restore](server-compatibility-backups.md)

_Other Topics_: [Compatibility Matrix](../product-notes/compatibility.md)

## [](#introduction)Introduction

Couchbase Server provides the backing data store for Sync Gateway.

> [!TIP]
> See: [Compatibility Matrix](../product-notes/compatibility.md) for version compatibility information.

Both _Couchbase Mobile_ and [Couchbase Server Cross Data Center Replication](../../../server/current/learn/clusters-and-availability/xdcr-overview.md) (XDCR) provide for efficient and secure replication of data, using different replication technologies optimized for specific use cases.

Sync Gateway provides different replication approaches depending on your version and use case requirements:

* **Sync Gateway 4.0+**: Bi-directional XDCR with version vectors enables active-active mobile clusters
* **Sync Gateway < 4.0**: Inter-Sync Gateway Replication for active-active, unidirectional XDCR for specific scenarios

Here we provide details on how XDCR feature relates to the Couchbase Mobile ecosystem.

## [](#lbl-xdcr)Cross Data Center Replication (XDCR)

Couchbase Server’s Cross Data Center Replication ([XDCR](../../../server/current/manage/manage-xdcr/xdcr-management-overview.md)) replicates necessary Sync Gateway metadata along with associated documents, making it suitable for various mobile cluster replication scenarios.

### [](#lbl-bidirectional-xdcr)Bi-directional XDCR

Sync Gateway 4.0 introduces support for bi-directional XDCR between active mobile clusters through an architectural change from revision trees to version vectors.

This enables active-active deployments where multiple clusters can process writes simultaneously while maintaining data consistency across geographically distributed datacenters. Both clusters process reads and writes from mobile clients simultaneously.

Sync Gateway 4.0 uses automatic conflict resolution with a `Last-Write-Wins` method and hybrid logical clocks by default. Clients can switch seamlessly between clusters without data loss. This provides zero-downtime disaster recovery with immediate fail-over capabilities.

> [!TIP]
> For detailed technical implementation and configuration requirements, see: [Bi-directional XDCR Active-Active with Mobile Clusters](../../../server/current/learn/clusters-and-availability/xdcr-active-active-sgw.md#xdcr-active-active-sgw-prerequisites).

![xdcr active active replication](../_images/xdcr-active-active-replication.png) 

Figure 1\. Bi-directional Active-Active XDCR

### [](#unidirectional-xdcr)Unidirectional XDCR

Unidirectional XDCR remains valuable for scenarios where you need to replicate the entire dataset from a source bucket to a target bucket without requiring bi-directional synchronization.

In these deployments, you should deploy Sync Gateway only at one end of the XDCR-replicated bucket (source or target) — see: [Example 1](#ex-xdcr-data-repl).

Example 1\. Unidirectional XDCR Replication

In this example XDCR deployment:

* XDCR runs unidirectionally, pushing data from the primary datacenter to the secondary datacenter
* Data gets pulled by Sync Gateway for downstream clients at the target location
* Sync Gateway deploys at both ends but operates in **read-only** mode at the target end to prevent write conflicts

![xdcr data replication to read only](../_images/xdcr-data-replication-to-read-only.png) 

Figure 2\. Unidirectional XDCR Replication

## [](#lbl-prov-drc)Disaster Recovery Scenarios

XDCR serves important roles in mobile cluster disaster recovery, supporting both traditional backup scenarios and modern zero-downtime active-active deployments.

### [](#traditional-disaster-recovery)Traditional Disaster Recovery

In traditional disaster recovery scenarios, XDCR supports data migration and backup operations where Sync Gateway operates at only one end of the unidirectional XDCR replication.

### [](#zero-downtime-active-active-disaster-recovery)Zero Downtime Active-Active Disaster Recovery

This model provides zero-downtime disaster recovery using bi-directional XDCR between two active mobile clusters. This requires running Sync Gateway 4.0+ on both sides of the active-active XDCR setup. Both clusters remain operational, with seamless fail-over through load balancer switching. You must configure both clusters with `import_docs=true`.

Set Up

To set up zero-downtime disaster recovery:

1. Configure bi-directional XDCR between the Primary and disaster recovery clusters.  
Enable automatic filtering of cluster specific metadata.
2. Deploy Sync Gateway in active mode on both clusters.
3. Configure users, roles, and databases independently on both clusters.  
XDCR replicates documents and attachments, but you must configure users, roles, and databases separately on each cluster.
4. Configure your load balancer to route traffic primarily to the Primary cluster.
5. Verify replication health between the two active clusters.

![xdcr active active replication](../_images/xdcr-active-active-replication.png) 

Figure 3\. DR Cluster Setup (Active-Active)

Activation

To activate disaster recovery:

1. Update load balancer configuration to redirect traffic to the disaster recovery cluster.  
This process requires no Sync Gateway service interruption.
2. Verify disaster recovery cluster is handling traffic properly.
3. Maintain bi-directional replication for recovery preparedness.  
The original primary becomes the new DR cluster automatically and requires no manual XDCR reconfiguration.

### [](#clusters-in-same-region)Clusters in Same Region

This model caters for situations where the Active and Disaster Recovery clusters are in the same region or datacenter — see: [Figure 4](#fig-dr-same-regn). It includes an optional optimization step, which confirms that there is no downtime during the activation stage.

Set Up

To set up and maintain a disaster recovery cluster:

1. Connect Sync Gateway to your Primary cluster.
2. \[**Optional step — for optimization**\] Pre-initialize Sync Gateway indexes on the Disaster Recovery cluster:

  1. Temporarily reconfigure the Sync Gateway cluster to connect to the Disaster Recovery cluster with the database in offline mode (`offline: true` in the database configuration) so that indexes are built asynchronously.
  2. After the indexes are created, reconfigure the Sync Gateway cluster to connect back to the Primary cluster.  
  Creating all indexes beforehand reduces switching costs. If you skip this step, you’ll incur latency when Sync Gateway switches to the Disaster Recovery cluster and Sync Gateway rebuilds its indexes.
3. Start the **unidirectional** XDCR from the Primary cluster to the Disaster Recovery cluster.

![sgw xdcr dr same regn setup](../_images/sgw-xdcr-dr-same-regn-setup.png) 

Figure 4\. DR Cluster Setup (Clusters in Same Regions)

Activation

When you’re ready to switch to Disaster Recovery operations:

1. Stop the replication (XDCR) from the Primary cluster to Disaster Recovery cluster.
2. Reconfigure the Sync Gateway cluster to connect to the Disaster Recovery cluster instead of the Primary cluster.
3. Make the Disaster Recovery cluster the **new** Primary and the **old** Primary the **new** Disaster Recovery.
4. Flush all replicated buckets in the Primary cluster as a precaution against any spurious writes that enter the Primary cluster and XDCR fails to replicate when you stop it.
5. Reverse the XDCR to replicate from the newly promoted Primary to the old Primary to set up a new Backup.

![sgw xdcr dr same regn in recovery](../_images/sgw-xdcr-dr-same-regn-in-recovery.png) 

Figure 5\. DR Cluster In-recovery (Clusters in Same Regions)

### [](#clusters-in-different-regions)Clusters in Different Regions

This model caters for situations where the Active and Disaster Recovery clusters are in different regions or data centers. Although the model has a separate Sync Gateway cluster attached to the Disaster Recovery cluster, this approach keeps the deployment of Sync Gateway at only 1 end of the XDCR replication. The optional optimization step confirms that there is no downtime during the activation stage.

Set Up

To set up and maintain a disaster recovery cluster - see: [Figure 6](#fig-dr-diff-regn-setup):

1. \[**Optional step — for optimization**\] Initialize Sync Gateway indexes on the Disaster Recovery cluster:

  1. Configure Sync Gateway to point to the Disaster Recovery cluster.
  2. Start the database in offline mode (`offline: true` in the database configuration) to build indexes asynchronously.
  3. Once indexes are created, shut down Sync Gateway on the Disaster Recovery cluster.  
  This pre-initialization allows XDCR to maintain the indexes in the background during normal operations, reducing latency during disaster recovery activation. If you skip this step, you’ll incur latency when switching to the Disaster Recovery cluster as Sync Gateway rebuilds its indexes from scratch.
2. \[**Critical step**\] Ensure **all** Sync Gateways in the Disaster Recovery cluster remain offline.
3. Start the **unidirectional** XDCR from the Primary cluster to the Disaster Recovery cluster.

![sgw xdcr dr diff regn setup](../_images/sgw-xdcr-dr-diff-regn-setup.png) 

Figure 6\. DR Cluster Setup (Clusters in Different Regions)

Activation

When you’re ready to switch to Disaster Recovery operations — see: [Figure 7](#fig-dr-diff-regn-in-recovery):

1. Stop Sync Gateway on the Primary cluster
2. Stop the replication (XDCR) from the Primary cluster to the Disaster Recovery cluster.
3. Verify that any and all Load Balancer updates to direct all traffic to the new Sync Gateway clusters.
4. Turn on the Sync Gateway cluster in the Disaster Recovery cluster.
5. Assign the Disaster Recovery cluster to be the **new** Primary cluster, and make the **old** Primary cluster the **new** Disaster Recovery cluster.
6. Flush all replicated buckets in the Primary cluster as a precaution against any spurious writes coming into the Primary cluster that XDCR did not replicate when you stopped it.
7. Reverse the original XDCR to replicate from the newly promoted Primary to the old Primary, to set up a new Backup.

![sgw xdcr dr diff regn in recovery](../_images/sgw-xdcr-dr-diff-regn-in-recovery.png) 

Figure 7\. DR In-Recovery (clusters in different regions)

## [](#lbl-isgr)Inter Sync Gateway Replication

For Sync Gateway versions prior to 4.0, Inter-Sync Gateway Replication was the primary solution for active-active mobile cluster deployments.

> [!IMPORTANT]
> Sync Gateway 4.0 introduces native bi-directional XDCR support for active-active mobile clusters, providing a simpler and more efficient alternative to Inter-Sync Gateway Replication. See [Bi-directional XDCR](#lbl-bidirectional-xdcr).

Inter-Sync Gateway replication was specifically designed to keep mobile clusters in different data centers in sync, with the ideal use-case being edge clusters containing active Sync Gateway nodes replicated between geographically separate cloud-based Sync Gateway deployments.

See: [Inter Sync Gateway Sync - Overview](../sync/sync-inter-syncgateway-overview.md) for complete implementation details.

Inter-Sync Gateway replication provides bi-directional read/write replications that verify:

* Sync Gateway observes cluster-specific security by invoking the appropriate Sync Function
* Sync Gateway maintains the integrity of security history with historical access rules held in metadata
* All clusters use a consistent Revision Id, allowing clients to identify a revision regardless of cluster location
* Cluster-specific `_sync` documents remain local and are not replicated to other mobile clusters

![icr active mobile sync](../_images/icr-active-mobile-sync.png) 

Figure 8\. Inter-Sync Gateway Active-to-Active Replication

> [!TIP]
> To upgrade to Sync Gateway 4.0 and enable bi-directional XDCR for active-active mobile clusters, see: [Upgrading Sync Gateway](../upgrading.md).

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](../access-control/sync-function/sync-function.md)
* [Import filter](../sync/import-processing.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Add/Update Sync Function](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
* [Sync Function Overview](../access-control/sync-function/sync-function.md)

###### [](#-3)

Reference material …​

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)