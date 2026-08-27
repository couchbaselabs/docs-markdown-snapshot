---
title: Remove a Node and Rebalance
description: Enterprise Analytics allows a cluster node to be removed, and the
  remaining nodes rebalanced.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/manage/pages/manage-nodes/remove-node-and-rebalance.adoc
  xref: xref:enterprise-analytics:manage:manage-nodes/remove-node-and-rebalance.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-nodes/remove-node-and-rebalance.html)

# Remove a Node and Rebalance

> Enterprise Analytics allows a cluster node to be removed, and the remaining nodes rebalanced. 

## [](#understanding-removal-and-rebalance)Understanding Removal and Rebalance

The rebalance operation redistributes query workloads and responsibility for storage partitions across available cluster nodes to in optimal fashion. This allows the best possible data-availability to be maintained after nodes have been added or removed. Examples of using rebalance after node-addition have already been provided, in [Add a Node and Rebalance](add-node-and-rebalance.md) and [Join a Cluster and Rebalance](join-cluster-and-rebalance.md).

Nodes can also be rebalanced following removal: this is demonstrated in the current section.

This page provides the steps to be taken for node-removal and rebalance. For a conceptual explanation of removal, see [Removal](../../../../server/current/learn/clusters-and-availability/removal.md).

### [](#connectivity-considerations)Connectivity Considerations

When removing a node from a cluster, it is important to follow the connectivity best practices outlined in [Cluster Connectivity and Topology Management](cluster-connectivity-topology-management.md). The scale in procedures vary based on the addressing model in use (Active Load Balancer, Passive Load Balancer, or DNS-Only). To minimize disruptions to client applications, ensure that you follow the procedures detailed in [Scale In (Remove Node)](cluster-connectivity-topology-management.md#scale-in-remove-node) section.

## [](#examples-on-this-page-node-removal)Examples on This Page

The examples in the subsections below show how to remove the same node from the same two-node cluster; using the [UI](#remove-a-node-with-the-ui), the [CLI](#remove-a-node-with-the-cli), and the [REST API](#remove-a-node-with-the-rest-api) respectively. The examples assume:

* A two-node cluster already exists; as at the conclusion of [List Cluster Nodes](list-cluster-nodes.md).
* The cluster has the Full Administrator username of `Administrator`, and password of `password`.

## [](#remove-a-node-with-the-ui)Remove a Node with the UI

Proceed as follows:

1. Access the **Servers** screen of Enterprise Analytics Web Console by clicking on the **Servers** tab in the left-hand navigation bar. The screen displays the two-node cluster with both nodes `10.142.181.101` and `10.142.181.102` listed in a tabular format showing their current status, services, resource utilization, and data distribution.
2. Click on the row for node `10.142.181.102` to expand it and reveal additional details. The row expands vertically to show comprehensive information about the node including:

  * Node details (name, version, uptime, OS)
  * Service configurations and RAM quotas
  * Address and security settings
  * Current resource utilization metrics
3. To initiate removal, click on the **Remove** button located at the lower left of the expanded row. This button allows you to flag the node for removal from the cluster.  
The **Confirm Server Removal** dialog appears, asking you to confirm the removal operation. The dialog warns about the implications of removing the node and requests confirmation that you want to proceed.  
Click on the **Remove Server** confirmation button to proceed. The **Servers** screen reappears showing that node `10.142.181.102` has been flagged for removal. The node status now indicates that it is "flagged for removal" and is "Still available to take traffic". A rebalance must be performed to complete removal.
4. Click on the **Rebalance** button at the upper right of the screen to begin the rebalancing process. Rebalancing now occurs, redistributing the data from the node being removed to the remaining nodes in the cluster.  
A progress dialog appears providing status information about the rebalance operation, including: - Progress bars showing completion percentage.

> [!NOTE]
> If rebalance fails, notifications are duly provided.

These are described in [Rebalance Failure Notification](add-node-and-rebalance.md#rebalance-failure-notification).

See also the information provided on [Automated Rebalance-Failure Handling](add-node-and-rebalance.md#automated-rebalance-failure-handling), and the procedure for its set-up, described in [Rebalance Settings](../manage-settings/general-settings.md#rebalance-settings).

## [](#remove-a-node-with-the-cli)Remove a Node with the CLI

A node can be removed from the cluster by means of the CLI. Note that the node does not have to be _failed over_ prior to removal.

To remove the node and perform the necessary rebalance, use the `rebalance` command with the `--server-remove` option.

/opt/enterprise-analytics/bin/couchbase-cli
--username Administrator \
--password password --server-remove 10.0.0.1:8091

This initiates the rebalance process. As it continues, progress is shown as console output:

Rebalancing
[================================                 ] 31.67%

For more information, see the command reference for [rebalance](../../cli/couchbase-cli-rebalance.md).

## [](#remove-a-node-with-the-rest-api)Remove a Node with the REST API

To remove a node from a cluster with the REST API, and rebalance the remaining nodes, use the `/controller/rebalance` URI. This requires that all known nodes be specified, and that the nodes to be ejected also be specified:

curl  -u Administrator:password -v -X POST \
http://10.142.181.101:8091/controller/rebalance \
-d 'ejectedNodes=ns_1%4010.142.181.102' \
-d 'knownNodes=ns_1%4010.142.181.101%2Cns_1%4010.142.181.102'

The command returns no output.

## [](#next-steps-after-remove-nodes)Next Steps

Nodes can be _failed over_, so that an unhealthy or unresponsive node can be removed from the cluster without application-access being affected. See [Fail Nodes Over](fail-nodes-over.md).