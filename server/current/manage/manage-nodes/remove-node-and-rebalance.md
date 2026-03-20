---
title: Remove a Node and Rebalance
description: Couchbase Server allows a cluster node to be removed, and the
  remaining nodes rebalanced.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/manage/pages/manage-nodes/remove-node-and-rebalance.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:manage:manage-nodes/remove-node-and-rebalance.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/manage/manage-nodes/remove-node-and-rebalance.html)

# Remove a Node and Rebalance

> Couchbase Server allows a cluster node to be removed, and the remaining nodes rebalanced. 

## [](#understanding-removal-and-rebalance)Understanding Removal and Rebalance

The _rebalance_ operation distributes active and replica vBuckets across available cluster nodes in optimal fashion. This allows the best possible data-availability to be maintained after nodes have been added or removed. Examples of using rebalance after node-addition have already been provided, in [Add a Node and Rebalance](add-node-and-rebalance.md) and [Join a Cluster and Rebalance](join-cluster-and-rebalance.md). In particular, reference was made in both locations to the data initially resident on a single node being replicated and distributed, across two nodes, following node-addition.

Nodes can also be rebalanced following removal: this is demonstrated in the current section. When a node is flagged for _removal_ (as opposed to _failover_), new replica vBuckets will be created on the remaining nodes, as node-removal occurs. This has the effect of reducing available memory for the specified number of replicas.

This page provides the steps to be taken for node-removal and rebalance. For a conceptual explanation of removal, see [Removal](../../learn/clusters-and-availability/removal.md).

## [](#examples-on-this-page-node-removal)Examples on This Page

The examples in the subsections below show how to remove the same node from the same two-node cluster; using the [UI](#remove-a-node-with-the-ui), the [CLI](#remove-a-node-with-the-cli), and the [REST API](#remove-a-node-with-the-rest-api) respectively. The examples assume:

* A two-node cluster already exists; as at the conclusion of [List Cluster Nodes](list-cluster-nodes.md).
* The cluster has the Full Administrator username of `Administrator`, and password of `password`.

## [](#remove-a-node-with-the-ui)Remove a Node with the UI

Proceed as follows:

1. Access the **Servers** screen of Couchbase Web Console, by means of the **Servers** tab in the left-hand navigation bar. The screen appears as follows:  
![twoNodeClusterAfterRebalanceCompressedView](../_images/manage-nodes/twoNodeClusterAfterRebalanceCompressedView.png)
2. Left-click on the row for node `10.142.181.102`. The row expands vertically, as follows:  
![twoNodeClusterAfterRebalance](../_images/manage-nodes/twoNodeClusterAfterRebalance.png)
3. To initiate removal, left-click on the **Remove** button, at the lower left of the row:  
![removeButton](../_images/manage-nodes/removeButton.png)  
The **Confirm Server Removal** dialog appears:  
![confirmServerRemoval](../_images/manage-nodes/confirmServerRemoval.png)  
Left-click on the **Remove Server** confirmation button. The **Servers** screen reappears as follows:  
![twoNodeClusterFollowingRemoval](../_images/manage-nodes/twoNodeClusterFollowingRemoval.png)  
This indicates that node `10.142.181.102` has been `flagged for removal`, and is `Still available to take traffic`. A rebalance must be performed to complete removal.
4. Left-click on the **Rebalance** button, at the upper right:  
![rebalanceButton](../_images/manage-nodes/rebalanceButton.png)  
Rebalancing now occurs. A dialog appears, providing status on progress.  
![rebalanceProgressRemoveNode](../_images/manage-nodes/rebalanceProgressRemoveNode.png)  
Following the rebalance, the **Servers** screen confirms that a single node remains. All **Items** (from the `travel-sample` bucket) are again solely located on `10.142.181.101`, with no replicas (since at least two nodes are required for replication to occur).

Note that if rebalance fails, notifications are duly provided. These are described in [Rebalance Failure Notification](add-node-and-rebalance.md#rebalance-failure-notification). See also the information provided on [Automated Rebalance-Failure Handling](add-node-and-rebalance.md#automated-rebalance-failure-handling), and the procedure for its set-up, described in [Rebalance Settings](../manage-settings/general-settings.md#rebalance-settings).

## [](#remove-a-node-with-the-cli)Remove a Node with the CLI

A node can be removed from the cluster by means of the CLI. Note that the node does not have to be _failed over_ prior to removal.

To remove the node and perform the necessary rebalance, use the `rebalance` command with the `--server-remove` option.

couchbase-cli rebalance -c 10.142.181.102:8091 \
--username Administrator \
--password password --server-remove 10.142.180.102:8091

This initiates the rebalance process. As it continues, progress is shown as console output:

Rebalancing
Bucket: 01/01 (travel-sample)             0 docs remaining
[================================                 ] 31.67%

For more information, see the command reference for [rebalance](../../cli/cbcli/couchbase-cli-rebalance.md).

## [](#remove-a-node-with-the-rest-api)Remove a Node with the REST API

To remove a node from a cluster with the REST API, and rebalance the remaining nodes, use the `/controller/rebalance` URI. This requires that all known nodes be specified, and that the nodes to be ejected also be specified:

curl  -u Administrator:password -v -X POST \
http://10.142.181.101:8091/controller/rebalance \
-d 'ejectedNodes=ns_1%4010.142.181.102' \
-d 'knownNodes=ns_1%4010.142.181.101%2Cns_1%4010.142.181.102'

The command returns no output.

## [](#next-steps-after-remove-nodes)Next Steps

Nodes can be _failed over_, so that an unhealthy or unresponsive node can be removed from the cluster without application-access being affected. See [Fail Nodes Over](fail-nodes-over.md).