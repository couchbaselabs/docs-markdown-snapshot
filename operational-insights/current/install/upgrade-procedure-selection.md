---
title: Upgrade Procedure Selection
description: Several procedures are available for upgrading an Operational
  Insights cluster. Choose one based on whether the cluster must stay online,
  and whether you have spare machines.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/upgrade-procedure-selection.adoc
  xref: xref:enterprise-analytics:install:upgrade-procedure-selection.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/upgrade-procedure-selection.html)

# Upgrade Procedure Selection

> Several procedures are available for upgrading an Operational Insights cluster. Choose one based on whether the cluster must stay online, and whether you have spare machines. 

## [](#understanding-upgrade-procedure-selection)How to Choose an Upgrade Procedure

Choose an upgrade procedure based on whether your cluster must:

* Stay online and serve requests at full capacity.
* Stay online, but can serve requests at reduced capacity.
* Go offline for a maintenance window.

Also check the [upgrade paths](upgrade.md#supported-upgrade-paths): a cluster running Enterprise Analytics 2.0.x can only be upgraded offline, or online after it has first been upgraded to Enterprise Analytics 2.2.x.

## [](#upgrade-and-availability)Upgrades and Availability

A cluster is upgraded one node at a time. When every node runs Operational Insights, the cluster is upgraded.

Cluster Online

Each Enterprise Analytics node is replaced by a freshly installed Operational Insights node, using _swap rebalance_. While any one node is being replaced, the other nodes continue to serve requests.

This method takes more steps, and each step includes a rebalance, but the cluster stays available throughout. A rebalance moves no data, since the data stays in object storage, so each step is quick regardless of how much data the cluster holds. Because each Operational Insights node starts as a new installation, an online upgrade needs no special handling for the change of package name and install directory.

If you have spare machines, the cluster can stay at full capacity throughout. If you do not, you can run the upgrade at reduced capacity. See [Using Spare Nodes](#using-spare-nodes).

Cluster Offline

All application access to the cluster stops, and each node is upgraded in turn, keeping its identity and its data. When every node has been upgraded, the cluster is brought back online. No rebalance is needed.

This method needs no spare machines, but it needs downtime. Because the package name and install directory change, each node follows a specific per-node procedure. See [Offline Upgrade from Enterprise Analytics to Operational Insights](upgrade-ea-to-oi.md), or [Offline Upgrade of a Docker Cluster from Enterprise Analytics to Operational Insights](upgrade-docker-cluster-offline.md) for Docker containers.

### [](#swap-rebalance)Swap Rebalance

Operational Insights performs a _swap rebalance_ when you add one or more nodes and remove the same number of nodes in a single rebalance.

A rebalance in Operational Insights reassigns which nodes serve each storage partition. It does not move data: the data stays in object storage, so a rebalance takes no longer for a cluster that holds more data. While a rebalance runs, ingestion from the cluster's links is suspended, and it resumes when the rebalance completes.

Each node caches data files from object storage on its local disk lazily, on first access. A node that has taken over a partition in a rebalance therefore starts with none of that partition's data cached, and the first queries that read it fetch the data from object storage, with higher latency than usual. Latency returns to normal as the node's cache warms. This applies to the default `selective` cache policy and to `lazy`. With the `eager` policy, a node caches all of its data when it starts. For more information, see [Memory and Caching](../reference/query-performance.md#%5Fmemory%5Fand%5Fcaching) and [Scaling](../intro/architecture-overview.md#%5Fscaling).

Every Operational Insights node runs the same fixed set of services, so you do not choose services for the nodes you add.

For more information about adding and removing nodes, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md) and [Remove a Node and Rebalance](../manage/manage-nodes/remove-node-and-rebalance.md).

### [](#using-spare-nodes)Using Spare Nodes

A swap rebalance needs a _spare node_: a machine, not currently part of the cluster, on which you install Operational Insights.

If you have a spare machine, install Operational Insights on it and swap it in for the first Enterprise Analytics node. The machine that node ran on is now free: uninstall Enterprise Analytics, install Operational Insights, and use it to replace the next Enterprise Analytics node. The cluster keeps the same number of nodes throughout, and serves requests at full capacity. See [Upgrade a Full-Capacity, Online Cluster](upgrade-cluster-online-full-capacity.md).

If you have no spare machine, decide whether the cluster can serve its workload acceptably with one node fewer. If it can, rebalance one Enterprise Analytics node out to free its machine, and use that machine as the spare. The cluster serves requests at reduced capacity until the last step, which adds the final node back. See [Upgrade a Reduced-Capacity, Online Cluster](upgrade-cluster-online-reduced-capacity.md).

### [](#using-failover)Failover Is Not an Upgrade Method

Couchbase Server offers an upgrade method that uses graceful failover and delta recovery to take a node out of the cluster and return it after upgrade. That method does not apply to Operational Insights:

* Graceful failover does not drain any Analytics work from the node, so it behaves like a hard failover.
* Delta recovery has no effect on the Analytics Service.
* A node upgraded from Enterprise Analytics to Operational Insights changes package and install directory, so it cannot simply be recovered in place.

Use swap rebalance instead.

## [](#summaries-of-upgrade-procedures)Summaries of Upgrade Procedures

### [](#online-upgrade)Upgrade with Cluster Online

#### [](#cluster-online-swap-rebalance-at-full-capacity)Cluster Online: Swap Rebalance at Full Capacity

You install Operational Insights on a spare machine, add it to the cluster, and remove one Enterprise Analytics node, in a single swap rebalance. You then uninstall Enterprise Analytics from the removed machine, install Operational Insights on it, and use it to replace the next Enterprise Analytics node. When every Enterprise Analytics node has been replaced, the last machine removed from the cluster is free for other use.

For the steps, see [Upgrade a Full-Capacity, Online Cluster](upgrade-cluster-online-full-capacity.md). For a cluster running in Docker, see [Upgrade an Online Docker Cluster, Full Capacity](upgrade-docker-cluster-online-full-capacity.md).

#### [](#cluster-online-swap-rebalance-with-capacity-reduced)Cluster Online: Swap Rebalance with Capacity Reduced

You rebalance one Enterprise Analytics node out of the cluster, and the cluster continues with one node fewer. You install Operational Insights on that machine, and swap it in for the next Enterprise Analytics node. You repeat until one machine remains outside the cluster, then add it back with an ordinary rebalance, which restores the cluster to full capacity.

For the steps, see [Upgrade a Reduced-Capacity, Online Cluster](upgrade-cluster-online-reduced-capacity.md).

New Operational Insights 3.0 features are not available until every Enterprise Analytics node has left the cluster. See [Feature Availability During Upgrade](upgrade-feature-availability.md).

### [](#offline-upgrade)Upgrade with Cluster Offline

When a cluster is offline, applications cannot access it, so plan a maintenance window before you start.

Disable auto-failover before you upgrade the first node, and enable it again only when every node has been upgraded. While a node is being upgraded, the other nodes see it as unavailable, and see it as available again when its upgrade is complete. Each node keeps its identity and data, so no rebalance is needed.

For the steps, see [Upgrade an Offline Cluster](upgrade-cluster-offline.md).