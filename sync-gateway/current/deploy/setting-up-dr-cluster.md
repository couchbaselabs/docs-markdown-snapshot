---
title: Setting up Disaster Recovery
description: How to set up a Sync Gateway mobile cluster for Disaster Recovery
  (DR) using Couchbase Server's Cross Data Center Replication (XDCR)
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/deploy/pages/setting-up-dr-cluster.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/current/deploy/setting-up-dr-cluster.html)

# Setting up Disaster Recovery

> How to set up a Sync Gateway mobile cluster for Disaster Recovery (DR) using Couchbase Server’s Cross Data Center Replication (XDCR)  

## [](#introduction)Introduction

[Couchbase Server Cross Data Center Replication](../../../server/current/learn/clusters-and-availability/xdcr-overview.md) (XDCR) replicates data between two or more autonomous Couchbase Server clusters. It plays an important role in supporting Disaster Recovery (DR) and Data Migration, even where Sync Gateway is the normal replicator of choice for mobile data.

## [](#recommended-deployment-models)Recommended Deployment Models

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

Figure 1\. DR Cluster Setup (Active-Active)

Activation

To activate disaster recovery:

1. Update load balancer configuration to redirect traffic to the disaster recovery cluster.  
This process requires no Sync Gateway service interruption.
2. Verify disaster recovery cluster is handling traffic properly.
3. Maintain bi-directional replication for recovery preparedness.  
The original primary becomes the new DR cluster automatically and requires no manual XDCR reconfiguration.

### [](#clusters-in-same-region)Clusters in Same Region

This model caters for situations where the Active and Disaster Recovery clusters are in the same region or datacenter — see: [Figure 2](#fig-dr-same-regn). It includes an optional optimization step, which confirms that there is no downtime during the activation stage.

Set Up

To set up and maintain a disaster recovery cluster:

1. \[**Optional step — for optimization**\] Start Sync Gateway with `offline: true` in the Disaster Recovery cluster to asynchronously create indexes. Creating all indexes beforehand reduces switching costs.  
If you skip this test, you’ll incur latency when Sync Gateway switches to the Disaster Recovery cluster and Sync Gateway rebuilds its indexes.
2. Connect Sync Gateway to your Primary cluster.
3. Start the **unidirectional** XDCR from the Primary cluster to the Disaster Recovery cluster.

![sgw xdcr dr same regn setup](../_images/sgw-xdcr-dr-same-regn-setup.png) 

Figure 2\. DR Cluster Setup (Clusters in Same Regions)

Activation

When you’re ready to switch to Disaster Recovery operations:

1. Stop the replication (XDCR) from the Primary cluster to Disaster Recovery cluster.
2. **After you stop XDCR:** Switch the Load Balancer to point to the Sync Gateway on the Disaster Recovery cluster. This approach keeps the deployment of Sync Gateway at only 1 end of the XDCR replication.
3. Promote the Disaster Recovery cluster to Primary and the **old** Primary to Disaster Recovery.
4. Flush all replicated buckets in the Primary cluster as a precaution against any spurious writes that enter the Primary cluster and XDCR fails to replicate when you stop it.
5. Reverse the XDCR to replicate from the newly promoted Primary to the old Primary to set up a new Backup.

![sgw xdcr dr same regn in recovery](../_images/sgw-xdcr-dr-same-regn-in-recovery.png) 

Figure 3\. DR Cluster In-recovery (Clusters in Same Regions)

### [](#clusters-in-different-regions-or-data-centers)Clusters in Different Regions or Data Centers

This model caters for situations where the Active and Disaster Recovery clusters are in different regions or data centers. Although the model has a separate Sync Gateway cluster attached to the Disaster Recovery cluster, this approach keeps the deployment of Sync Gateway at only 1 end of the XDCR replication. The optional optimization step confirms that there is no downtime during the activation stage.

Set Up

To set up and maintain a disaster recovery cluster - see: [Figure 4](#fig-dr-diff-regn-setup):

1. \[**Optional step — for optimization**\] Start Sync Gateway with `offline: true` in the Disaster Recovery cluster to asynchronously create indexes. If you skip this test, you’ll incur latency when you switch Sync Gateway to the Disaster Recovery cluster and Sync Gateway rebuilds its indexes.
2. \[**Critical step**\] Turn off **all** the Sync Gateways in the Disaster Recovery cluster.
3. Start the **unidirectional** XDCR from the Primary cluster to the Disaster Recovery cluster.

![sgw xdcr dr diff regn setup](../_images/sgw-xdcr-dr-diff-regn-setup.png) 

Figure 4\. DR Cluster Setup (Clusters in Different Regions)

Activation

When you’re ready to switch to Disaster Recovery operations — see: [Figure 5](#fig-dr-diff-regn-in-recovery):

1. Stop Sync Gateway on the Primary cluster
2. Stop the replication (XDCR) from the Primary cluster to the Disaster Recovery cluster.
3. Verify that any and all Load Balancer updates to direct all traffic to the new Sync Gateway clusters.
4. Turn on the Sync Gateway cluster in the Disaster Recovery cluster.
5. Assign the Disaster Recovery cluster to be the **new** Primary cluster, and make the **old** Primary cluster the **new** Disaster Recovery cluster.
6. Flush all replicated buckets in the Primary cluster as a precaution against any spurious writes coming into the Primary cluster that XDCR did not replicate when you stopped it.
7. Reverse the original XDCR to replicate from the newly promoted Primary to the old Primary, to set up a new Backup.

![sgw xdcr dr diff regn in recovery](../_images/sgw-xdcr-dr-diff-regn-in-recovery.png) 

Figure 5\. DR In-Recovery (clusters in different regions)

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)