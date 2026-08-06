---
title: Choose an Upgrade Procedure
description: Multiple procedures are available for the upgrade of Enterprise
  Analytics. An appropriate procedure should be selected, based on a variety of
  factors.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/install/pages/upgrade-procedure-selection.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:install:upgrade-procedure-selection.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/install/upgrade-procedure-selection.html)

# Choose an Upgrade Procedure

> Multiple procedures are available for the upgrade of Enterprise Analytics. An appropriate procedure should be selected, based on a variety of factors. 

## [](#understanding-upgrade-procedure-selection)How to Choose an Upgrade Procedure

Choosing an upgrade procedure for an Enterprise Analytics cluster depends on whether:

* Your cluster is online and serving data at full capacity.
* Your cluster is online and serving data at reduced capacity.
* Your cluster is offline.

Use the information on this page to choose the right procedure based on your specific use case.

## [](#upgrade-and-availability)Upgrades and Availability

Upgrade of Enterprise Analytics occurs node by node. When every node has been upgraded to the latest version of Enterprise Analytics, the whole cluster is considered upgraded. To be upgraded, each node must be offline: this means that although it's still **up** and **network-accessible**, it's **not** part of a cluster that's serving data. To upgrade all the nodes in the cluster, choose 1 of the following methods:

Cluster Offline

All nodes in the cluster are taken offline together and the cluster stops serving data. While the cluster is offline, each node is upgraded. During the upgrade, each node is recognized as non-communicative by the other nodes. Nodes are recognized as communicative again when the upgrade is complete.

When all nodes have been individually upgraded, the cluster is brought back online, and the cluster resumes serving data. No rebalance is required, since data has remained unmodified during the upgrade.

This upgrade method offers the greatest simplicity. However, it requires cluster downtime.

Cluster Online

Each individual node is taken offline, upgraded, and then reintroduced to the cluster by adding or joining. This means that while any given node is offline, all other nodes remain online.

This upgrade method is more complex, but allows the cluster to continue serving data with minimal disruption. It introduces more overhead by requiring a full [Rebalance](../../../server/current/learn/clusters-and-availability/rebalance.md) for every node. This consumes more cluster resources.

You can reduce the overhead and resource consumption using [Swap Rebalance](#swap-rebalance). If you do not want to serve data at a reduced capacity during an upgrade, you must [use spare nodes](#using-spare-nodes) during the upgrade to maintain full capacity.

### [](#swap-rebalance)Swap Rebalance

Enterprise Analytics automatically performs a **Swap Rebalance** when all the following conditions apply:

* One or more nodes have been introduced into the cluster.
* One or more nodes have been taken out of the cluster.
* The introduced nodes are identical in number and configuration to the nodes that have been taken out.
* Rebalance is triggered by the administrator.

Since the introduced nodes are recognized by Enterprise Analytics to have equivalent capacities and configurations to those that have been taken out, rebalance is performed as a **swap rebalance**; which largely confines its activity to the incoming and outgoing nodes. Thus, for example, if one Data Service node is removed and another added, the swap rebalance ensures that the vBucket layout of the outgoing node is created identically on the incoming node; with the layouts of other Data Service nodes not requiring modification.

> [!NOTE]
> Make sure you're familiar with the effects of a rebalance on your Enterprise Analytics cluster. See [Rebalance](../reference/rest-rebalance-overview.md).

#### [](#using-spare-nodes)Using Spare Nodes

A swap rebalance requires introducing and removing an identical number and configuration of nodes. This requires using spare nodes.

A **spare** node is any node that's not currently a member of the cluster.

For example, if you wanted to upgrade your Enterprise Analytics cluster 1 node at a time, you must introduce a spare node into the cluster to remove 1 of the existing nodes. The swap rebalance operation is limited to those 2 nodes. When the swap rebalance completes, the spare node takes over the role of the node you removed to upgrade.

Then, after the upgrade completes, you can add or join the upgraded node back into the cluster, and remove the spare node. This triggers another swap rebalance for those 2 nodes, where vBuckets or other forms of data are copied back to the upgraded node.

Using spare nodes lets your cluster continue to serve data at full capacity during an upgrade. See [Cluster Online: Swap Rebalance at Full Capacity](#cluster-online-swap-rebalance-at-full-capacity).

If you do not have additional machines available to use as spade nodes, you must decide if you can maintain acceptable cluster performance with 1 or more nodes removed from your cluster during an upgrade.

If you can maintain acceptable performance, remove nodes from your cluster to upgrade them and run a full rebalance. Your smaller cluster can continue to serve data at a lower performance level, and you can use the removed nodes as spare nodes for swap rebalance throughout your upgrade. See [Cluster Online: Swap Rebalance with Capacity Reduced](#cluster-online-swap-rebalance-with-capacity-reduced).

#### [](#using-failover)Using Failover

If it's possible to remove one or more Data Service nodes from the cluster, and run the cluster at reduced capacity for the duration of the upgrade procedure, [Failover](../manage/manage-nodes/fail-nodes-over.md) can be used to bring individual Data Service nodes out of the cluster, and so allow them to be upgraded. The Failover procedure ensures that all the cluster's active vBuckets continue to be available, on the remaining Data Service nodes, after the node to be upgraded has been failed over. Subsequently, the upgraded node is restored to the cluster using [Recovery](../cli/couchbase-cli-recovery.md).

The main advantages of Graceful Failover and Delta Recovery in this context are simpler management and a lower consumption of cluster-resources: since to upgrade a node, no **spare** node is required, and no copying of data across nodes (such as is performed by rebalance) need occur. The main constraint of this option is that it can **only** be used for nodes running the Data Service alone.

Further considerations are provided in [Advantages and Disadvantages](../../../server/current/learn/clusters-and-availability/graceful-failover.md#advantages-and-disadvantages).

## [](#summaries-of-upgrade-procedures)Summaries of Upgrade Procedures

In accordance with the dependency-definitions provided above, in [Upgrades and Availability](#upgrade-and-availability), this section summarizes the individual, recommended procedures for upgrading a Couchbase-Server cluster.

### [](#online-upgrade)Upgrade with Cluster Online

For a multi-node cluster, an **online upgrade** means that the cluster continues to serve data while its nodes are progressively upgraded. Online upgrade can be performed in either of the following ways.

#### [](#cluster-online-swap-rebalance-at-full-capacity)Cluster Online: Swap Rebalance at Full Capacity

One or more spare nodes, which exist in addition to those committed to the cluster, are prepared for addition to the cluster. When these nodes are added to the cluster, the same number are removed. Addition occurs by means of either **joining** or **adding**, as described in [Clusters](#server:learn:clusters-and-availability/nodes.html#clusters).

> [!NOTE]
> Configuration of the added nodes must match that of the removed nodes. When rebalance is triggered by the administrator, Enterprise Analytics performs a **swap rebalance**.

Removed nodes are kept **up** and **network-accessible**: and in this state, are upgraded to the latest version of Enterprise Analytics. Then, following the upgrade procedure, the upgraded nodes are re-introduced into the cluster; and are given configurations that match the configurations of the spare nodes; and the spare nodes are themselves now removed. Finally, a further [Rebalance](../../../server/current/learn/clusters-and-availability/rebalance.md) is performed, and the upgraded nodes become full members of the cluster.

Once all nodes have been processed in this way, the entire cluster has been upgraded.

New features of Enterprise Analytics may not be available while the upgrade of an online cluster is in progress; since the cluster is during this period running two different versions of Enterprise Analytics, and the features of the later version are not available until all nodes have been upgraded.

#### [](#cluster-online-swap-rebalance-with-capacity-reduced)Cluster Online: Swap Rebalance with Capacity Reduced

An assessment is made of how many nodes can be removed from the cluster while maintaining acceptable data-serving performance. A number of nodes no greater than the ascertained number is then removed, and a rebalance performed. The diminished cluster continues to serve data.

Upgrade now commences. One or more nodes are added to the cluster, and the same number are removed. The added nodes are configured such that when rebalance is triggered by the administrator, Enterprise Analytics performs a **swap rebalance**. Removed nodes are kept **up** and **network-accessible**: and in this state, are upgraded to the latest version of Enterprise Analytics. Then, following the upgrade procedure, the upgraded nodes are re-introduced into the cluster: each can either be **joined** or **added**, as described in [Clusters](../../../server/current/learn/clusters-and-availability/nodes.md#clusters). The configuration of added nodes must match that of the spare nodes that are now removed. Finally, a further [Rebalance](../../../server/current/learn/clusters-and-availability/rebalance.md) is performed, and the upgraded nodes become full members of the cluster.

Once all nodes have been processed in this way, the entire cluster has been upgraded.

New features of Enterprise Analytics may not be available while the upgrade of an online cluster is in progress. Since the cluster is during this period running two different versions of Enterprise Analytics, and the features of the later version are not available until all nodes have been upgraded.

### [](#offline-upgrade)Upgrade with Cluster Offline

When an entire multi-node cluster is **offline**, it's not accessible to applications, and therefore serves no data. A maintenance window must therefore be formally established prior to offline upgrade commencing.

During offline upgrade, even though the cluster serves no data, it continues to function as a cluster: individual nodes continue to be **up** and **network-accessible**; and continue to be recognized by their peers and by the [Cluster Manager](../../../server/current/learn/clusters-and-availability/cluster-manager.md) as cluster-members.

Before the upgrade of any node is performed, [Automatic Failover](../../../server/current/learn/clusters-and-availability/automatic-failover.md) should be **disabled** and must be **re-enabled** only when the entire cluster-upgrade is complete. Each individual node, while undergoing upgrade, is recognized as unavailable by the other nodes; but is recognized as available again when its upgrade is complete. No rebalance is required at any stage, since no data is modified during the cluster-upgrade process.

Each node in turn should be failed over, upgraded, and then, by the restarting of Enterprise Analytics, restored to the cluster. When all nodes have been restored, the cluster can then brought back online, so that the serving of data can resume.