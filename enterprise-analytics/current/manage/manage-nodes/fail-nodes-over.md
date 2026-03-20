---
title: Failover
description: Nodes can be <em>failed over</em>, and thereby removed safely from
  a cluster in the event of unavoidable downtime, without any break in the
  serving of data to applications.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/manage/pages/manage-nodes/fail-nodes-over.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:manage:manage-nodes/fail-nodes-over.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-nodes/fail-nodes-over.html)

# Failover

> Nodes can be _failed over_, and thereby removed safely from a cluster in the event of unavoidable downtime, without any break in the serving of data to applications. 

Failover allows a node to be removed from a cluster reactively, because the node has become unresponsive or unstable.

## [](#understanding-failover)Understanding Failover

Failover drops a node from a cluster _reactively_, because the node has become unresponsive or unstable. It’s manually or automatically initiated.

The automatic initiation of Failover is known as _automatic_ failover, and is configured by means of the [Node Availability](../manage-settings/general-settings.md#node-availability) panel of the **General** settings screen of Enterprise Analytics Web Console, or by means of equivalent CLI and REST API commands. The current page explains how to initiate Failover _manually_.

A complete conceptual description of failover and its variants (including hard) is provided in [Failover](../../../../server/current/learn/clusters-and-availability/failover.md).

### [](#connectivity-considerations)Connectivity Considerations

When performing a failover, it’s important to follow the connectivity best practices outlined in [Cluster Connectivity and Topology Management](cluster-connectivity-topology-management.md). The procedures on failover vary based on the addressing model in use (Active Load Balancer, Passive Load Balancer, or DNS-Only). To minimize disruptions to client applications, ensure that you follow the procedures detailed in [Failover Procedures](cluster-connectivity-topology-management.md#failover-procedures) section.

## [](#examples-on-this-page-hard-failover)Examples on This Page

The examples in the subsections below perform the same _hard_ failover, on the same two-node cluster; using the [UI](#manage:manage-nodes/failover-hard.adoc#failover-with-the-ui), the [CLI](#manage:manage-nodes/failover-hard.adoc#failover-with-the-cli), and the [REST API](#manage:manage-nodes/failover-hard.adoc#failover-with-the-rest-api) respectively. The examples assume:

* A two-node cluster already exists; as at the conclusion of [Join a Cluster and Rebalance](join-cluster-and-rebalance.md).
* The cluster has the Full Administrator username of `Administrator`, and password of `password`.

## [](#failover-with-the-ui)Failover with the UI

Proceed as follows:

1. Access the Enterprise Analytics Web Console **Servers** screen, on node `10.142.181.101`, by clicking on the **Servers** tab in the left-hand navigation bar. The display shows the current two-node cluster with both nodes `10.142.181.101` and `10.142.181.102` listed in the servers table.
2. To see further details of the node to be failed over, which in this example will be `10.142.181.102`, click on the row for the node. The row expands vertically to reveal additional information about the node, including its services, storage paths, and system details.
3. To initiate failover, click on the **Failover** button, located at the lower right of the expanded row for `10.142.181.102`. The **Confirm Failover Dialog** now appears with options for configuring the failover operation. Select the check box for **Confirm failover**.

Enterprise Analytics shows you an additional warning dialog about potential data loss. Failing over the node forcibly terminates and removes it from the cluster, transferring responsibility of its storage partitions to remaining nodes in the cluster. Executing queries will be aborted and the operations will be temporarily unavailable while the cluster processes the failover. Rebalancing will be required to add the node back into the cluster.

In this case, you must select **Confirm failover** to acknowledge the risk and continue the Failover.

1. Confirm the Failover by clicking the **Failover Node** button.  
Enterprise Analytics performs the Failover on the node. When it finishes, the **Servers** screen shows that the failover has successfully completed, with the node `10.142.181.102` now marked as failed over. The interface indicates that a rebalance is required to complete the reduction of the two-node cluster to one node.
2. Click the **Rebalance** button at the upper right to initiate rebalance. When the rebalance process is complete, the **Servers** screen shows only the remaining node `10.142.181.101`. Node `10.142.181.102` has successfully been removed from the cluster.

Note that if rebalance fails, notifications are duly provided. These are described in [Rebalance Failure Notification](add-node-and-rebalance.md#rebalance-failure-notification). See also the information provided on [Automated Rebalance-Failure Handling](add-node-and-rebalance.md#automated-rebalance-failure-handling), and the procedure for its set-up, described in [Rebalance Settings](../manage-settings/general-settings.md#rebalance-settings).

### [](#resetting-auto-failover-quota)Resetting the Auto-Failover Quota

In cases where a node has become unresponsive, and _auto-failover_ has been configured, a **Reset Auto-Failover Quota** button may appear to the left of the **Rebalance** button on the Servers screen.

Clicking on the **Reset Auto-Failover Quota** button causes the current count of already-occurred, successive auto-failovers to be reset to zero.

Note that a rebalance, which can be started by clicking on the **Rebalance** button, also resets this count to zero on successful completion.

An overview of auto-failover is provided in [Automatic Failover](../../../../server/current/learn/clusters-and-availability/automatic-failover.md). information about how to configure auto-failover is provided in [Node Availability](../manage-settings/general-settings.md#node-availability).

### [](#failover-of-multiple-nodes)Failover of Multiple Nodes

Failover of one or more nodes can be managed by means of the **FAILOVER** tab, located toward the upper right of the **Servers** screen.

For clusters with multiple nodes, the Servers screen displays all nodes in a tabular format with their current status. Click on the **FAILOVER** tab to access the multiple node failover interface.

This brings up the **Failover Multiple Nodes** dialog, which provides a list of all nodes in the cluster with checkboxes for selection.

The dialog provides the following **Data Loss Warning**: _For Failover of multiple nodes, each Couchbase bucket must have at least as many replicas as the total number of nodes failed over or you WILL lose data. Since Failover removes nodes immediately it may also result in failure of in-flight operations._

If you wish to perform a Failover on multiple nodes, select those nodes using the checkboxes next to their names, then click on the **Failover Nodes** button to start the Failover process. When this has completed, a rebalance will, as usual, be required.

#### [](#failover-with-unresponsive-nodes)Failover of Multiple Unresponsive Nodes

When Failover is required due to multiple nodes being unresponsive, the **Failover Multiple Nodes** dialog displays unresponsive nodes with visual indicators (typically marked with a red status indicator).

If you select the checkboxes for unresponsive nodes and click the **Failover Nodes** button, a warning dialog may appear indicating that Failover of these nodes will be _unsafe_.

The unsafe failover warning dialog explains the risks associated with performing an unsafe Failover and requests confirmation before proceeding. For information about unsafe Failover, see [Performing an Unsafe Failover](../../../../server/current/learn/clusters-and-availability/hard-failover.md#performing-an-unsafe-failover).

If you wish to proceed with the unsafe Failover, check the checkboxes again for each node to be failed over, and click on the **Failover Nodes: Unsafe Mode** button. Failover of the selected nodes then occurs.

## [](#failover-with-the-cli)Failover with the CLI

To perform a Failover on a node, use the `failover` command with the `--hard` flag.

/opt/enterprise-analytics/bin/couchbase-cli -c 10.142.181.101
--username Administrator \
--password password \
--server-failover 10.142.181.102:8091 --hard

When the progress completes successfully, the following output is displayed:

SUCCESS: Server failed over

The cluster can now be rebalanced with the following command, to remove the failed-over node:

/opt/enterprise-analytics/bin/couchbase-cli
--username Administrator \
--password password --server-remove 10.142.181.102:8091

Progress is displayed as console output. If successful, the operation gives the following output:

SUCCESS: Rebalance complete

In certain circumstances, an attempted Failover will not be executed by Enterprise Analytics: for information, see [Failover in Default and Unsafe Modes](../../../../server/current/learn/clusters-and-availability/hard-failover.md#default-and-unsafe). Such an attempt therefore fails, with an `ERROR: Received unexpected status 504` notification. If Failover must nevertheless be performed, the `failover` CLI expression should be re-entered: this time, with the `--force` flag used, in addition to the `--hard` flag. This produces an _unsafe_ Failover.

For more information about `failover` with the CLI, see [failover](../../cli/couchbase-cli-failover.md). For more information about `rebalance` with the CLI, see [rebalance](../../cli/couchbase-cli-rebalance.md).

## [](#failover-with-the-rest-api)Failover with the REST API

To perform a Failover on a node, by means of the REST API, use the `/controller/failover` URI, specifying the node to be failed over, as follows:

curl -v -X POST -u Administrator:password \
http://10.142.181.101:8091/controller/failOver \
-d 'otpNode=ns_1@10.142.181.102'

Subsequently, the cluster can be rebalanced, and the failed-over node removed, with the `/controller/rebalance` URI:

curl  -u Administrator:password -v -X POST \
http://10.142.181.101:8091/controller/rebalance \
-d 'ejectedNodes=ns_1%4010.142.181.102' \
-d 'knownNodes=ns_1%4010.142.181.101%2Cns_1%4010.142.181.102'

For more information about `/controller/failover`, see [Failing Over Nodes](../../reference/rest-node-failover.md). For more information about `/controller/rebalance`, see [Rebalancing Nodes](../../reference/rest-cluster-rebalance.md).

In certain circumstances, an attempted Failover will not be executed by Enterprise Analytics: for information, see [Hard Failover in Default and Unsafe Modes](#learn:clusters-and-availability/hard-failover.adoc#default-and-unsafe). Such an attempt therefore fails, with a `Cannot safely perform a failover at the moment` notification. If Failover must nevertheless be performed, the `POST /controller/rebalance` expression should be re-entered, with the same parameters as before; but this time, with the addition of the `-d allowUnsafe=true` parameter. This produces an _unsafe_ Failover.

## [](#next-steps-after-failover)Next Steps

A node that has been failed over can be recovered and reintegrated into the cluster. See [Recover a Node](recover-nodes.md).