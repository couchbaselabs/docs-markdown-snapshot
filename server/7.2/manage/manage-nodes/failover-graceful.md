---
title: Perform Graceful Failover
description: Graceful failover allows a node to be removed from a cluster
  proactively, when the cluster is healthy, and all data is available.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/manage/pages/manage-nodes/failover-graceful.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:manage:manage-nodes/failover-graceful.adoc[]
---

[View original HTML](/server/7.2/manage/manage-nodes/failover-graceful.html)

# Perform Graceful Failover

> Graceful failover allows a node to be removed from a cluster proactively, when the cluster is healthy, and all data is available. 

## [](#understanding-graceful-failover)Understanding Graceful Failover

_Graceful_ failover allows a Data Service node to be removed from the cluster _proactively_, in an orderly and controlled fashion (say, for the purposes of system-maintenance). It is manually initiated when the entire cluster is in a healthy state, and all active and replica vBuckets on all nodes are available.

A complete conceptual description of failover and its variants (including graceful) is provided in [Failover](../../learn/clusters-and-availability/failover.md).

## [](#examples-on-this-page-graceful-failover)Examples on This Page

The examples in the subsections below fail the same node over gracefully, from the same two-node cluster; using the [UI](#graceful-failover-with-the-ui), the [CLI](#graceful-failover-with-the-cli), and the [REST API](#graceful-failover-with-the-rest-api) respectively. The examples assume:

* A two-node cluster already exists; as at the conclusion of [Join a Cluster and Rebalance](join-cluster-and-rebalance.md).
* The cluster has the Full Administrator username of `Administrator`, and password of `password`.

## [](#graceful-failover-with-the-ui)Graceful Failover with the UI

Proceed as follows:

1. Access the Couchbase Web Console **Servers** screen, on node `10.142.181.101`, by left-clicking on the **Servers** tab in the left-hand navigation bar. The display is as follows:  
![twoNodeClusterAfterRebalanceCompressedView](../_images/manage-nodes/twoNodeClusterAfterRebalanceCompressedView.png)
2. To see further details of each node, left-click on the row for the node. The row expands vertically, as follows:  
![twoNodeClusterAfterRebalance](../_images/manage-nodes/twoNodeClusterAfterRebalance.png)
3. To initiate failover, left-click on the **Failover** button, at the lower right of the row for `101.142.181.102`:  
![failoverButton](../_images/manage-nodes/failoverButton.png)  
The **Confirm Failover Dialog** now appears:  
![confirmFailoverDialog](../_images/manage-nodes/confirmFailoverDialog.png)  
Two radio buttons are provided, to allow selection of either **Graceful** or **Hard** failover. **Graceful** is selected by default.
4. Confirm _graceful_ failover by left-clicking on the **Failover Node** button.  
Graceful failover is now initiated, and a rebalance occurs as part of the procedure. A progress dialog appears, summarizing overall progress:  
![rebalanceFollowingGracefulFailover7.0](../_images/manage-nodes/rebalanceFollowingGracefulFailover7.0.png)  
For server-level details of the graceful failover process, see the conceptual overview provided in [Graceful Failover](../../learn/clusters-and-availability/graceful-failover.md).  
When the process ends, the display is as follows:  
![gracefulFailoverFullScreenRebalanceNeeded](../_images/manage-nodes/gracefulFailoverFullScreenRebalanceNeeded.png)  
This indicates the graceful failover has successfully completed, but an additional rebalance is required to complete the reduction of the cluster to one node.
5. Left-click the **Rebalance** button, at the upper right, to initiate a further rebalance. When the process is complete, the **Server** screen appears as follows:  
![gracefulFailoverAfterRebalance](../_images/manage-nodes/gracefulFailoverAfterRebalance.png)  
Node `10.142.181.102` has successfully been removed.

Note that if rebalance fails, notifications are duly provided. These are described in [Rebalance Failure Notification](add-node-and-rebalance.md#rebalance-failure-notification). See also the information provided on [Automated Rebalance-Failure Handling](add-node-and-rebalance.md#automated-rebalance-failure-handling), and the procedure for its set-up, described in [Rebalance Settings](../manage-settings/general-settings.md#rebalance-settings).

## [](#graceful-failover-with-the-cli)Graceful Failover with the CLI

To fail a node over gracefully, use the `failover` command, as follows:

couchbase-cli failover -c 10.142.181.101:8091 \
--username Administrator \
--password password \
--server-failover 10.142.181.102:8091

The `--server-failover` flag specifies the name and port number of the node to be gracefully failed over.

Progress is displayed as console output:

Gracefully failing over
Bucket: 00/00 ()                                 0 docs remaining
[======================                                   ] 17.77

When the progress completes successfully, the following output is displayed:

SUCCESS: Server failed over

The cluster can now be rebalanced with the following command, to remove the failed-over node:

couchbase-cli rebalance -c 10.142.181.101:8091 \
--username Administrator \
--password password \
--server-remove 10.142.181.102:8091

If successful, the operation gives the following output:

SUCCESS: Rebalance complete

For more information on `failover`, see [failover](../../cli/cbcli/couchbase-cli-failover.md). For more information on `rebalance`, see [rebalance](../../cli/cbcli/couchbase-cli-rebalance.md).

## [](#graceful-failover-with-the-rest-api)Graceful Failover with the REST API

To fail a node over gracefully with the REST API, use the `/controller/startGracefulFailover` URI, specifying the node to be failed over, as follows:

curl -v -X POST -u Administrator:password \
http://10.142.181.101:8091/controller/startGracefulFailover \
-d 'otpNode=ns_1@10.142.181.102'

Subsequently, the cluster can be rebalanced, and the failed-over node removed, with the `/controller/rebalance` URI:

curl  -u Administrator:password -v -X POST \
http://10.142.181.101:8091/controller/rebalance \
-d 'knownNodes=ns_1@10.142.181.101,ns_1@10.142.181.102&ejectedNodes=ns_1@10.142.181.102'

For more information on `/controller/startGracefulFailover`, see [Setting Graceful Failover](../../rest-api/rest-failover-graceful.md). For more information on `/controller/rebalance`, see [Rebalancing Nodes](../../rest-api/rest-cluster-rebalance.md).

## [](#next-steps-after-graceful-failover)Next Steps

A _hard_ failover can be used when a node is unresponsive. See [Hard Failover](failover-hard.md).