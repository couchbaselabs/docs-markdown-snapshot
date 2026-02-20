---
title: Perform Hard Failover
description: Hard failover allows a node to be removed from a cluster
  reactively, because the node has become unresponsive or unstable.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/manage/pages/manage-nodes/failover-hard.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:manage:manage-nodes/failover-hard.adoc[]
---

[View original HTML](/server/current/manage/manage-nodes/failover-hard.html)

# Perform Hard Failover

> Hard failover allows a node to be removed from a cluster reactively, because the node has become unresponsive or unstable. 

## [](#understanding-hard-failover)Understanding Hard Failover

_Hard_ failover drops a node from a cluster _reactively_, because the node has become unresponsive or unstable. It is manually or automatically initiated, and occurs after the point at which active vBuckets have been lost.

The automatic initiation of hard failover is known as _automatic_ failover, and is configured by means of the [Node Availability](../manage-settings/general-settings.md#node-availability) panel of the **General** settings screen of Couchbase Web Console, or by means of equivalent CLI and REST API commands. The current page explains how to initiate hard failover _manually_.

A complete conceptual description of failover and its variants (including hard) is provided in [Failover](../../learn/clusters-and-availability/failover.md).

## [](#examples-on-this-page-hard-failover)Examples on This Page

The examples in the subsections below perform the same _hard_ failover, on the same two-node cluster; using the [UI](#hard-failover-with-the-ui), the [CLI](#hard-failover-with-the-cli), and the [REST API](#hard-failover-with-the-rest-api) respectively. The examples assume:

* A two-node cluster already exists; as at the conclusion of [Join a Cluster and Rebalance](join-cluster-and-rebalance.md).
* The cluster has the Full Administrator username of `Administrator`, and password of `password`.

## [](#hard-failover-with-the-ui)Hard Failover with the UI

Proceed as follows:

1. Access the Couchbase Web Console **Servers** screen, on node `10.142.181.101`, by left-clicking on the **Servers** tab in the left-hand navigation bar. The display is as follows:  
![twoNodeClusterAfterRebalanceCompressedView](../_images/manage-nodes/twoNodeClusterAfterRebalanceCompressedView.png)
2. To see further details of the node to be failed over, which in this example will be `10.142.181.102`, left-click on the row for the node. The row expands vertically, as follows:  
![twoNodeClusterAfterRebalance](../_images/manage-nodes/twoNodeClusterAfterRebalance.png)
3. To initiate failover, left-click on the **Failover** button, at the lower right of the row for `10.142.181.102`:  
![failoverButton](../_images/manage-nodes/failoverButton.png)  
The **Confirm Failover Dialog** now appears:  
![confirmFailoverDialog](../_images/manage-nodes/confirmFailoverDialog.png)  
Two radio buttons are provided, to allow selection of either **Graceful** or **Hard** failover. **Graceful** is selected by default.
4. Select **Hard Failover**:  
![confirmHardFailoverDialog](../_images/manage-nodes/confirmHardFailoverDialog.png)  
Read the warning message that appears. It explains that a hard failover may interrupt ongoing writes and replications. Therefore, you may want to [remove the node and rebalance](remove-node-and-rebalance.md) instead of performing a hard failover on a still-available Data Service node.  
If the node contains vBuckets that do not have replicas on other nodes, Couchbase Server shows you an additional warning about data loss:  
![hardFailoverWithDataLoss](../_images/manage-nodes/hardFailoverWithDataLoss.png)  
In this case, you must select **Confirm failover** to continue the hard failover.  
> [!WARNING]  
> Performing a hard failover on a node containing vBuckets that have no replicas on other nodes results in data loss.
5. Confirm the hard failover by clicking **Failover Node**.  
Couchbase Server performs the hard failover on the node. When it finishes, the **Servers** screen appears as follows:  
![twoNodeClusterAfterHardFailover](../_images/manage-nodes/twoNodeClusterAfterHardFailover.png)  
This indicates that hard failover has successfully completed, but a rebalance is required to complete the reduction of the two-node cluster to one node.
6. Left-click the **Rebalance** button, at the upper right, to initiate rebalance. When the process is complete, the **Server** screen appears as follows:  
![gracefulFailoverAfterRebalance](../_images/manage-nodes/gracefulFailoverAfterRebalance.png)  
Node `10.142.181.102` has successfully been removed.

Note that if rebalance fails, notifications are duly provided. These are described in [Rebalance Failure Notification](add-node-and-rebalance.md#rebalance-failure-notification). See also the information provided on [Automated Rebalance-Failure Handling](add-node-and-rebalance.md#automated-rebalance-failure-handling), and the procedure for its set-up, described in [Rebalance Settings](../manage-settings/general-settings.md#rebalance-settings).

### [](#resetting-auto-failover-quota)Resetting the Auto-Failover Quota

In cases where a node has become unresponsive, and _auto-failover_ has been configured, a button such as the following may appear, to the left of the **Rebalance** button:

![resetAutoFailoverQuotaButton](../_images/manage-nodes/resetAutoFailoverQuotaButton.png) 

Left-clicking on the **Reset Auto-Failover Quota** button causes the current count of already-occurred, successive auto-failovers to be reset to zero. Note that a rebalance, which can be started by left-clicking on the **Rebalance** button, also resets this count to zero, on successful completion. An overview of auto-failover is provided in [Automatic Failover](../../learn/clusters-and-availability/automatic-failover.md). Information on how to configure auto-failover is provided in [Node Availability](../manage-settings/general-settings.md#node-availability).

### [](#hard-failover-of-multiple-nodes)Hard Failover of Multiple Nodes

Hard failover of one or more nodes can be managed by means of the **FAILOVER** tab, toward the upper right of the **Servers** screen:

![serverScreenWithFailoverTab](../_images/manage-nodes/serverScreenWithFailoverTab.png) 

As the **Servers** screen here shows, this example features a cluster of three nodes. Left-click on the **FAILOVER** tab to perform hard failover on one or more of the three nodes:

![leftClickOnFailoverTab](../_images/manage-nodes/leftClickOnFailoverTab.png) 

This brings up the **Failover Multiple Nodes** dialog:

![hardFailoverMultipleNodesDialog](../_images/manage-nodes/hardFailoverMultipleNodesDialog.png) 

The dialog provides the following **Data Loss Warning**: _For hard failover of multiple nodes, each Couchbase bucket must have at least as many replicas as the total number of nodes failed over or you WILL lose data. Since hard failover removes nodes immediately it may also result in failure of in-flight operations._

If you wish to perform a hard failover on multiple nodes, select those nodes from the checkboxes, then left-click on the **Failover Nodes** button, to start hard failover. When this has completed, a rebalance will, as usual, be required.

#### [](#hard-failover-with-unresponsive-nodes)Hard Failover of Multiple Unresponsive Nodes

When hard failover is required due to multiple nodes being unresponsive, the **Failover Multiple Nodes** dialog appears as follows:

![hardFailoverMultipleNodesUnresponsiveDialog](../_images/manage-nodes/hardFailoverMultipleNodesUnresponsiveDialog.png) 

The three unresponsive nodes are those marked, at the left, with a red bar. If the checkbox for each of these nodes is selected, and the **Failover Nodes** button is left-clicked, the following dialog appears:

![hardFailoverDangerDialog](../_images/manage-nodes/hardFailoverDangerDialog.png) 

This indicates that hard failover of these nodes will be _unsafe_. For information on unsafe hard failover, see [Performing an Unsafe Failover](../../learn/clusters-and-availability/hard-failover.md#performing-an-unsafe-failover). If you wish to proceed, check the checkboxes again for each node to be failed over, and left-click on the **Failover Nodes: Unsafe Mode** button. Hard failover of the selected nodes then occurs.

## [](#hard-failover-with-the-cli)Hard Failover with the CLI

To perform a hard failover on a node, use the `failover` command with the `--hard` flag.

couchbase-cli failover -c 10.142.181.102:8091 \
--username Administrator \
--password password \
--server-failover 10.142.181.102:8091 --hard

When the progress completes successfully, the following output is displayed:

SUCCESS: Server failed over

The cluster can now be rebalanced with the following command, to remove the failed-over node:

couchbase-cli rebalance -c 10.142.181.101:8091 \
--username Administrator \
--password password --server-remove 10.142.181.102:8091

Progress is displayed as console output. If successful, the operation gives the following output:

SUCCESS: Rebalance complete

In certain circumstances, an attempted hard failover will not be executed by Couchbase Server: for information, see [Hard Failover in Default and Unsafe Modes](../../learn/clusters-and-availability/hard-failover.md#default-and-unsafe). Such an attempt therefore fails, with an `ERROR: Received unexpected status 504` notification. If hard failover must nevertheless be performed, the `failover` CLI expression should be re-entered: this time, with the `--force` flag used, in addition to the `--hard` flag. This produces an _unsafe_ hard failover.

For more information on `failover` with the CLI, see [failover](../../cli/cbcli/couchbase-cli-failover.md). For more information on `rebalance` with the CLI, see [rebalance](../../cli/cbcli/couchbase-cli-rebalance.md).

## [](#hard-failover-with-the-rest-api)Hard Failover with the REST API

To perform a hard failover on a node, by means of the REST API, use the `/controller/failover` URI, specifying the node to be failed over, as follows:

curl -v -X POST -u Administrator:password \
http://10.142.181.101:8091/controller/failOver \
-d 'otpNode=ns_1@10.142.181.102'

Subsequently, the cluster can be rebalanced, and the failed-over node removed, with the `/controller/rebalance` URI:

curl  -u Administrator:password -v -X POST \
http://10.142.181.101:8091/controller/rebalance \
-d 'ejectedNodes=ns_1%4010.142.181.102' \
-d 'knownNodes=ns_1%4010.142.181.101%2Cns_1%4010.142.181.102'

For more information on `/controller/failover`, see [Failing Over Nodes](../../rest-api/rest-node-failover.md). For more information on `/controller/rebalance`, see [Rebalancing Nodes](../../rest-api/rest-cluster-rebalance.md).

In certain circumstances, an attempted hard failover will not be executed by Couchbase Server: for information, see [Hard Failover in Default and Unsafe Modes](../../learn/clusters-and-availability/hard-failover.md#default-and-unsafe). Such an attempt therefore fails, with a `Cannot safely perform a failover at the moment` notification. If hard failover must nevertheless be performed, the `POST /controller/rebalance` expression should be re-entered, with the same parameters as before; but this time, with the addition of the `-d allowUnsafe=true` parameter. This produces an _unsafe_ hard failover.

## [](#next-steps-after-hard-failover)Next Steps

A node that has been failed over can be recovered and reintegrated into the cluster. See [Recover a Node](recover-nodes.md).