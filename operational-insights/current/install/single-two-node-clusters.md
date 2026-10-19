---
title: Single-Node and Two-Node Clusters
description: The number of nodes in an Operational Insights deployment may
  impact both maintenance requirements and feature availability.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/single-two-node-clusters.adoc
  xref: xref:enterprise-analytics:install:single-two-node-clusters.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/single-two-node-clusters.html)

# Single-Node and Two-Node Clusters

> The number of nodes in an Operational Insights deployment may impact both maintenance requirements and feature availability. 

When setting up the Operational Insights deployment, the number of nodes in that deployment impact the features that are available. The number of nodes also heavily impact how you maintain deployment in production. For these reasons, Couchbase does not recommend running an Operational Insights deployment of less than 3 nodes in production. After evaluating a use case, Couchbase may grant support for specific use cases that require single-node or two-node clusters. This topic highlights some of the feature differences and considerations that you need to take into account when setting up and running a small deployment.

## [](#2-node-deployments)2-Node Deployments

The following limitations apply to deployments with 2 nodes:

* **No auto-failover functionality**  
When a deployment of Operational Insights has fewer than 3 nodes, auto-failover is disabled. With fewer than 3 nodes in the deployment, it's not easy to determine which node has an issue to avoid a split-brain configuration.
* **Run the cluster at < 50% load capacity**  
When running a Couchbase deployment with 2 nodes, we recommend running the cluster at 50% capacity. In the event of a failure, running the cluster at this level ensures that the remaining node is not overloaded.

### [](#metadata-management)Metadata Management

Operational Insights manages metadata by means of Chronicle, which is a consensus-based system, based on the [Raft](https://raft.github.io/) algorithm. Due to the consistency with which topology-related metadata is managed, in the event of a quorum failure, you cannot modify nodes, buckets, scopes, and collections until you resolve it. A quorum failure is the unresponsiveness of at least half of the cluster's nodes — for example, the unresponsiveness of 1 node in a 2-node cluster.

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