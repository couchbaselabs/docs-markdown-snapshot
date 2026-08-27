---
title: Two-Node and Single-Node Clusters
description: The number of nodes in a Couchbase-Server deployment may impact
  both maintenance-requirements and feature-availability.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/install/pages/deployment-considerations-lt-3nodes.adoc
  xref: xref:server:install:deployment-considerations-lt-3nodes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/install/deployment-considerations-lt-3nodes.html)

# Two-Node and Single-Node Clusters

> The number of nodes in a Couchbase-Server deployment may impact both maintenance-requirements and feature-availability. 

When setting up a Couchbase Server deployment, the number of nodes in that deployment impact the features that are available. The number of nodes also heavily impact how the deployment is maintained in production. For these reasons, we do not recommend running a Couchbase Server deployment of less than three nodes in production. Support for specific use cases that require a one-node or two-node clusters may be granted by Couchbase after an evaluation of the use case. This topic highlights some of the feature differences and considerations that need to be taken into account when setting up and running a small deployment.

## [](#two-node-deployments)Two-Node Deployments

The following limitations apply to deployments with two nodes:

* **No auto-failover functionality**  
When a deployment of Couchbase Server has fewer than three nodes, auto-failover is disabled. This is because with fewer than three nodes in the deployment, it's not easy to determine which node is having an issue and thus avoid a split-brain configuration. You can optionally add an arbiter node to your cluster to provide [quorum arbitration](#quorum-arbitration).
* **Maximum number of replicas is 1**  
A Couchbase Server deployment can have multiple replicas. However, when a deployment has only two nodes, you can only have a maximum of one replica since the Active and Replica of a vBucket cannot exist on the same server.
* **Run the cluster at < 50% load capacity**  
When running a Couchbase deployment with two nodes, we recommend running the cluster at 50% capacity. In the event of a failure, running the cluster at this level ensures that the remaining node is not overloaded.

### [](#quorum-arbitration)Quorum Arbitration

If you're deploying a two-node database or a database with two server groups, consider adding an arbiter node to your cluster. An arbiter node is part of the Couchbase Server cluster, but it doesn't any service other than the [Cluster Manager](../learn/clusters-and-availability/cluster-manager.md) which joins it to the cluster. The arbiter node helps your cluster in two ways:

* It provides [fast failover](../learn/clusters-and-availability/nodes.md#fast-failover) which decreases the cluster's latency when responding to a failover.
* It provides quorum arbitration, which allows Couchbase Server to execute a failover when it would otherwise refuse to do so.

In a two-node cluster without an arbiter node, when one node fails the other cannot differentiate between node failure and a network failure causing [network partitioning](https://en.wikipedia.org/wiki/Network%5Fpartition). The remaining node refuses to failover to avoid a split brain configuration where two groups of nodes independently alter data and risk potential data conflicts. The arbiter node eliminates the possibility of conflict by ensuring only one set of nodes can continue to operate. The arbiter provides a quorum to the remaining node, letting it know that it's safe to failover and take on the role of the failed node.

The arbiter node fulfills a similar role when there are two [server groups](../learn/clusters-and-availability/groups.md). In case of network partitioning, the arbiter node can make sure that only one server group continues processing. To play this role, the arbiter node should be in a third server group to maximize the chance of it remaining available if one of the server groups fails. Ideally, you should locate it in a separate rack when using physical hardware. When it runs in a container, cloud instance, or as a virtual machine, locate it on a separate host machine from the server groups.

To deploy an arbiter node, add or join a node to the cluster without assigning it any services. For instructions on adding a node, see:

* [Assigning Services](../rest-api/rest-set-up-services.md) to deploy via the REST API.
* [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md#arbiter-node-addition) and [Join a Cluster and Rebalance](../manage/manage-nodes/join-cluster-and-rebalance.md#arbiter-node-join) to deploy via the Couchbase Server Web Console.
* The [server-add](#cli:cbcli/couchbase-cli-server-add) command to deploy via the command line interface.

For more information about failover, see [Hard Failover](../learn/clusters-and-availability/hard-failover.md), and in particular, [Hard Failover in Default and Unsafe Modes](../learn/clusters-and-availability/hard-failover.md#default-and-unsafe).

#### [](#arbiter-nodes-and-licenses)Arbiter Nodes and Licenses

An arbiter node does not run any services other than the [Cluster Manager](../learn/clusters-and-availability/cluster-manager.md). This service is necessary to make the arbiter node part of the Couchbase Server cluster. Because it does not run other services, such as the [Data Service](../learn/services-and-indexes/services/data-service.md), the arbiter node does not require an additional license to run. It's essentially free aside from the cost of running the physical hardware, container, or cloud instance.

#### [](#sizing-recommendations-for-arbiter-nodes)Sizing Recommendations for Arbiter Nodes

Because the arbiter node runs only the Cluster Manager service, it often does not require the same resources as other nodes in the cluster. Your best option for choosing hardware or a cloud instance for an arbiter node is to start with the smallest instance you plan to or are already using in your cluster. Then monitor the arbiter node's CPU and RAM usage when your cluster experiences failovers and rebalanaces. Rebalances in the cluster cause the highest CPU loads and memory use on the arbiter node. If you find the arbiter is not using all of the CPU and RAM you allocated to it, you can choose to downsize it. The arbiter's RAM and CPU use grow as the number of nodes, buckets, and collections grow in your cluster. Therefore, continue to monitor the RAM and CPU use of your arbiter node, especially after you expand your cluster.

### [](#metadata-management)Metadata Management

In Couchbase Server 7.0 and later versions, metadata is managed by means of _Chronicle_; which is a _consensus-based_ system, based on the [Raft](https://raft.github.io/) algorithm. Due to the strong consistency with which topology-related metadata is thus managed, in the event of a _quorum failure_ (meaning, the unresponsiveness of at least half of the cluster's nodes — for example, the unresponsiveness of one node in a two-node cluster), no modification of nodes, buckets, scopes, and collections can take place until the quorum failure is resolved.

For a complete overview of how all metadata is managed by Couchbase Server, see [Metadata Management](../learn/clusters-and-availability/metadata-management.md). For information on _unsafe failover_ and its consequences, see [Performing an Unsafe Failover](../learn/clusters-and-availability/hard-failover.md#performing-an-unsafe-failover).

## [](#single-node-deployments)Single-Node Deployments

Many features of Couchbase Server do not work in a single-node deployment. All of the limitations that apply to deployments with two nodes also hold true for single node deployments, including no auto-failover functionality.

* **Node failure means recreating the cluster and restoring data**  
In a single-node deployment, any failure of the node implies downtime and possible recovery from a backup.
* **Failure creates a high likelihood of irrecoverable data loss (no in-memory replicas)**  
When a node fails or restarts, there is 100% downtime until it is recovered. In a single-node cluster, there is no replica that can take over the traffic when the node is not responding.
* **Constant warning in the user interface reminding you that you have no replicas**  
The Couchbase Server Web Console will tell you that your data is not replicated and that you are running in an unsafe configuration. This is how the cluster manager alerts the administrator if there are not enough replicas to protect your data.
* **No failover (in addition to no auto-failover)**  
When running a single node-cluster, a node cannot failover if there are issues.
* **No ability to add services dynamically**  
With multidimensional scaling, each node in a deployment can have multiple roles. However, to be able to change these roles, the node must be removed from the deployment first. With a single-node deployment, the only option is to take the deployment offline, add the service, and restore the deployment.
* **No rolling upgrade (offline only)**  
To upgrade a single node deployment, the node must be offline as an upgrade using a rebalance is not an option with a single server.
* **No rolling restart (offline only)**  
Any restart of the single node for maintenance reasons results in 100% downtime as there are no other nodes to take over this work.
* **Host name or IP address must be set explicitly**  
When creating a single-node deployment, set the host name and IP address at the time of creation.