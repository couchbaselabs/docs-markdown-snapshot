---
title: Upgrade an Online Docker Cluster, Full Capacity
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/install/pages/upgrade-docker-cluster-online-full-capacity.adoc
  xref: xref:7.6@server:install:upgrade-docker-cluster-online-full-capacity.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/install/upgrade-docker-cluster-online-full-capacity.html)

# Upgrade an Online Docker Cluster, Full Capacity

> A Docker cluster with multiple nodes can be upgraded live, while maintaining full capacity. 

## [](#understanding-the-full-capacity-upgrade)Understanding the Full Capacity Upgrade

The context and overall requirements for upgrading a live cluster without the introduction of one or more additional nodes are described in [Upgrade-Procedure Selection](upgrade-procedure-selection.md): this explains the node-by-node upgrade of the cluster, using the _swap rebalance_ process to minimize overhead.

> [!NOTE]
> It is not possible to upgrade a Docker cluster with a single node. A second node will needed to ensure data is transferred.

The precise steps for this procedure are detailed on this page, below. A full understanding of the information in [Upgrade-Procedure Selection](upgrade-procedure-selection.md) should be acquired, before proceeding. Yous should also be familiar with using [Docker commands to create nodes](getting-started-docker.md). The procedure assumes that:

* The cluster to be upgraded must continue to serve data throughout the cluster-upgrade process.
* A single, additional node can be created to act as a _swap_ node.
* During the cluster-upgrade process, _swap_ nodes and _upgraded_ nodes will be introduced to the cluster by the _node-addition_ procedure; while _failed over spare nodes_ and _nodes to be upgraded_ will be withdrawn from the cluster by means of the _node removal_ and _swap rebalance_ procedures.  
For information on node-addition, see [Clusters](../learn/clusters-and-availability/nodes.md#clusters). For information on node-removal, see [Removal](../learn/clusters-and-availability/removal.md). For information on _swap rebalance_, see [Swap Rebalance](upgrade-procedure-selection.md#swap-rebalance).
* Nodes will be upgraded _one at a time_.

## [](#prepare-the-cluster)1\. Prepare the Cluster

Carry out a _full_ backup of the cluster's data. This can be done using the [REST-API](../rest-api/backup-trigger-backup.md) or the [Backup Service](../manage/manage-backup-and-restore/manage-backup-and-restore.md).

## [](#create-the-spare-node)2\. Create the Spare Node

Use the standard Docker tools to create your node. (For more information read [Install Couchbase Server Using Docker](getting-started-docker.md)). In this case, you will create a node that can act as cluster manager. For example:

```console
docker run -d --name sparenode -p 28091-28096:8091-8096 -p 11310-11311:11210-11211 couchbase:latest
```

will create a new node (`sparenode`) using the latest Couchbase server image. Note that the port mappings have been set so as not to clash with the external port settings of the existing node that is managing the cluster.

> [!IMPORTANT]
> The node must be created as managing cluster. Later on, the existing managing node will be removed and upgraded, so the new node will be needed to communicate with the cluster.

## [](#add-the-spare-node-to-the-cluster-and-rebalance-the-cluster)3\. Add the Spare Node to the Cluster and Rebalance the Cluster

The new node must be added to the cluster, then the cluster must be rebalanced. This can be done through the administration console, or the REST-API. (For information on adding nodes and rebalancing, read [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md)).

> [!NOTE]
> Ensure that the `sparenode` can be used to access the cluster through the administration console. It will use the same IP address, but a different port number. (In the [example above](#docker-create-sparenode), this is defined as `28091`).

## [](#remove-node-for-upgrading)4\. Remove a Node For Upgrading

Using the `sparenode`, remove one of the nodes for upgrading from the cluster and rebalance the cluster.

## [](#delete-the-node-container)5\. Delete the Node Container

The `docker` command is used to delete the node and its associated volume. For example:

```console
docker rm -f nodename
docker volume prune
```

Re-using existing volumes

You cannot re-use existing volumes when replacing a docker container, so it is not possible to use the same data set by pointing the new container at an existing volume.

**This does mean that it is not possible to upgrade a Docker Couchbase container with only a single node available for use.**

To prevent unusable volumes from building up during upgrades, it's important to delete the unused volumes during the process to decrease the chances of running out of disk space.

## [](#upgrade-the-node-container)6\. Upgrade the Node Container

The command used to upgrade the node depends on whether it is a standard node, or the node that used to administer the cluster. When recreating the container for the administration node, the `docker` command must set up the ports to match the settings of the node that has been removed.

* Standard Node
* Administration Node

The following command will create a new container for the standard node.

```console
docker run -d --name nodename couchbase:latest
```

The following command will create a new container for the administration node.

```console
docker run -d --name nodename -p 8091-8096:8091-8096 -p 11210-11211:11210-11211 couchbase:latest
```

Note that the external port addresses match those of the administration node that has been removed.

## [](#add-new-node-and-rebalance)7\. Add the New Node to the Cluster and Rebalance

Use the `sparenode` to add the new node to the cluster, then rebalance the cluster. This can be done through the administration console, or the REST-API. (For information on adding nodes and rebalancing, read [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md)).

## [](#repeat-for-all-nodes-in-cluster)8\. Repeat for all nodes in cluster

Now repeat steps from \[[Section 4](#remove-node-for-upgrading)\] to \[[Section 7](#add-new-node-and-rebalance)\] to remove and upgrade each node in the cluster, except the spare node used for administration.

> [!CAUTION]
> Care should be taken not to remove the spare node by mistake; this is the node that is used for adding the other nodes and rebalancing.

## [](#remove-the-spare-node)9\. Remove the Spare Node

The upgraded administration node can be used to remove the spare node from the cluster and rebalance the cluster. Once this has been done, then the `docker` command can be used to remove the spare node's container and volume.

```console
docker rm -f sparenode
docker volume prune
```

The cluster is now fully upgraded.