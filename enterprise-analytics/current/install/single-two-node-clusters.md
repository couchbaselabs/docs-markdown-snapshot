---
title: 2-Node and Single-Node Clusters
description: The number of nodes in an Enterprise Analytics deployment may
  impact both maintenance requirements and feature availability.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/install/pages/single-two-node-clusters.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/current/install/single-two-node-clusters.html)

# 2-Node and Single-Node Clusters

> The number of nodes in an Enterprise Analytics deployment may impact both maintenance requirements and feature availability. 

When setting up the Enterprise Analytics deployment, the number of nodes in that deployment impact the features that are available. The number of nodes also heavily impact how you maintain deployment in production. For these reasons, Couchbase does not recommend running an Enterprise Analytics deployment of less than 3 nodes in production. After evaluating a use case, Couchbase may grant support for specific use cases that require a 1-node or 2-node clusters. This topic highlights some of the feature differences and considerations that you need to take into account when setting up and running a small deployment.

## [](#2-node-deployments)2-Node Deployments

The following limitations apply to deployments with 2 nodes:

* **No auto-failover functionality**  
When a deployment of Enterprise Analytics has fewer than 3 nodes, auto-failover is disabled. With fewer than 3 nodes in the deployment, it’s not easy to determine which node has an issue to avoid a split-brain configuration.
* **Run the cluster at < 50% load capacity**  
When running a Couchbase deployment with 2 nodes, we recommend running the cluster at 50% capacity. In the event of a failure, running the cluster at this level ensures that the remaining node is not overloaded.

### [](#metadata-management)Metadata Management

In Enterprise Analytics 7.0+, you can manage metadata by means of Chronicle; which is a consensus-based system, based on the [Raft](https://raft.github.io/) algorithm. Due to the consistency with which topology-related metadata is managed, in the event of a quorum failure, you cannot modify nodes, buckets, scopes, and collections until you resolve it. A quorum failure is the unresponsiveness of at least half of the cluster’s nodes — for example, the unresponsiveness of 1 node in a 2-node cluster.

## [](#single-node-deployments)Single-Node Deployments

All of the limitations that apply to deployments with 2 nodes also hold true for single node deployments, including no auto-failover capability.

* **Node failure means recreating the cluster and restoring data**  
In a single-node deployment, any failure of the node implies downtime and possible recovery from a backup.
* **No failover (in addition to no auto-failover)**  
When running a single node-cluster, a node cannot failover if there are issues.
* **No rolling upgrade (offline only)**  
To upgrade a single node deployment, the node must be offline as an upgrade using a rebalance is not an option with a single server.
* **No rolling restart (offline only)**  
Any restart of the single node for maintenance reasons results in 100% downtime as there are no other nodes to take over this work.
* **Hostname or IP address must be set explicitly**  
When creating a single-node deployment, set the hostname and IP address at the time of creation.