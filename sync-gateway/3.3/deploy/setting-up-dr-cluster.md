---
title: Setting up Disaster Recovery
description: How to set up a Sync Gateway mobile cluster for Disaster Recovery
  (DR) using Couchbase Server's Cross Data Center Replication (XDCR)
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/deploy/pages/setting-up-dr-cluster.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.3@sync-gateway:deploy:setting-up-dr-cluster.adoc[]
---

[View original HTML](/sync-gateway/3.3/deploy/setting-up-dr-cluster.html)

# Setting up Disaster Recovery

> How to set up a Sync Gateway mobile cluster for Disaster Recovery (DR) using Couchbase Server’s Cross Data Center Replication (XDCR)  

## [](#introduction)Introduction

[Couchbase Server Cross Data Center Replication](../../../server/current/learn/clusters-and-availability/xdcr-overview.md) (XDCR) replicates data between two or more autonomous Couchbase Server clusters. It serves an important role in supporting Disaster Recovery (DR) and Data Migration, even where Sync Gateway is the normal replicator of choice for mobile data.

## [](#recommended-deployment-models)Recommended Deployment Models

### [](#clusters-in-same-region)Clusters in Same Region

This model caters for situations where the Active and Disaster Recovery clusters are in the same region or data center — see: [Figure 1](#fig-dr-same-regn). It includes an optional optimization step, which will ensure that there is no downtime during the activation stage.

Set Up

To set up and maintain a disaster recovery cluster:

1. \[_Optional step — for optimization_\] Connect Sync Gateway to the Disaster Recovery cluster just long enough to create indexes. Having everything reindexed lowers switching costs.  
If you skip this test, you will incur latency when Sync Gateway is switched to the Disaster Recovery cluster and Sync Gateway rebuilds its indexes.
2. Connect Sync Gateway to your Primary cluster.
3. Initiate the **unidirectional** XDCR from the Primary cluster to the Disaster Recovery cluster.

![sgw xdcr dr same regn setup](../_images/sgw-xdcr-dr-same-regn-setup.png) 

Figure 1\. DR Cluster Setup (Clusters in Same Regions)

Activation

When you are ready to switch to Disaster Recovery operations:

1. Stop the replication (XDCR) from the Primary cluster to Disaster Recovery cluster.
2. **When XDCR is stopped:** Switch the Load Balancer to point to the Sync Gateway on the Disaster Recovery cluster. This maintains the deployment of Sync Gateway at only one end of the XDCR replication.
3. Promote the Disaster Recovery cluster to Primary and the **old** Primary to Disaster Recovery.
4. Flush all replicated buckets in the Primary cluster; as a precaution against any spurious writes coming into the Primary cluster that had not been replicated when XDCR was stopped.
5. Reverse the XDCR to replicate from the newly promoted Primary to the old Primary to set up a new Backup.

![sgw xdcr dr same regn in recovery](../_images/sgw-xdcr-dr-same-regn-in-recovery.png) 

Figure 2\. DR Cluster In-recovery (Clusters in Same Regions)

### [](#clusters-in-different-regions-or-data-centers)Clusters in Different Regions or Data Centers

This model caters for situations where the Active and Disaster Recovery clusters are in different regions or data centers. Although the model has a separate Sync Gateway cluster attached to the Disaster Recovery cluster, it maintains the deployment of Sync Gateway at only one end of the XDCR replication. The optional optimization step will ensure that there is no downtime during the activation stage.

Set Up

To set up and maintain a disaster recovery cluster - see: [Figure 3](#fig-dr-diff-regn-setup):

1. \[_Optional step — for optimization_\] Turn on _Sync Gateway_ in the Disaster Recovery cluster just long enough to create indexes. Having everything re-indexed lowers switching costs.  
If you skip this test, you will incur latency when Sync Gateway is switched to the Disaster Recovery cluster and Sync Gateway rebuilds its indexes.
2. \[_Critical step_\] Turn off **all** the Sync Gateways in the Disaster Recovery cluster.
3. Initiate the **unidirectional** XDCR from the Primary cluster to the Disaster Recovery cluster.

![sgw xdcr dr diff regn setup](../_images/sgw-xdcr-dr-diff-regn-setup.png) 

Figure 3\. DR Cluster Setup (Clusters in Different Regions)

Activation

When you are ready to switch to Disaster Recovery operations — see: [Figure 4](#fig-dr-diff-regn-in-recovery):

1. Stop Sync Gateway on the Primary cluster
2. Stop the replication (XDCR) from the Primary cluster to the Disaster Recovery cluster.
3. Ensure that any and all Load Balancer(s) are updated to direct all traffic to the new Sync Gateway cluster(s).
4. Turn on the Sync Gateway cluster(s) in the Disaster Recovery cluster.
5. Promote the Disaster Recovery cluster to be the **new** Primary cluster, and make the **old** Primary cluster the **new** Disaster Recovery cluster
6. Flush all replicated buckets in the Primary cluster; as a precaution against any spurious writes coming into the Primary cluster that had not been replicated when XDCR was stopped.
7. Reverse the original XDCR to replicate from the newly promoted Primary to the old Primary, to set up a new Backup.

![sgw xdcr dr diff regn in recovery](../_images/sgw-xdcr-dr-diff-regn-in-recovery.png) 

Figure 4\. DR In-Recovery (clusters in different regions)

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