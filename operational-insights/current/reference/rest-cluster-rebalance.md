---
title: Rebalancing the Cluster
description: A cluster is rebalanced with the <code>POST
  /controller/rebalance</code> HTTP method and URI.
pubDate: 2026-10-28T04:21:06.350Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-cluster-rebalance.adoc
  xref: xref:enterprise-analytics:reference:rest-cluster-rebalance.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-cluster-rebalance.html)

# Rebalancing the Cluster

> A cluster is rebalanced with the `POST /controller/rebalance` HTTP method and URI. 

## [](#http-method-and-uri)HTTP method and URI

POST /controller/rebalance

## [](#rest-cluster-rebalance-description)Description

Clusters can be _rebalanced_. When one or more nodes have been brought into a cluster, or have been taken out of a cluster, _rebalance_ redistributes the work of the Analytics Service among the available nodes.

An overview of nodes, and how they are combined into clusters, is provided in [Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).

This REST API reference explains the `POST /controller/rebalance` command usage after:

* The node additions and removals.
* A hard failover.

## [](#curl-syntax)Curl Syntax

curl -v -X POST -u [admin]:[password]
  http://[localhost]:8091/controller/rebalance
  [-d knownNodes | -d ejectedNodes]

The parameters are:

* `knownNodes`. Must always be specified. The value is a list containing all nodes that are in the cluster at the start of the rebalance process.
* `ejectedNodes`. Specified when one or more nodes are to be ejected from the cluster by the rebalance process. The value is a list containing all nodes to be ejected.  
The node-list specified by `ejectedNodes` is thus a subset of that specified by `knownNodes`.

For information about rebalance, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md).

## [](#responses)Responses

Success gives the status `200 OK`, with no object returned.

If either parameter specifies an unknown node, or if a node currently in the cluster is omitted from the value of `knownNodes`, the status `400 Bad Request` is given, and the following object is returned:

{"mismatch":1}

If `knownNodes` is _not_ specified and `ejectedNodes` _is_ specified, the status `400 Bad Request` is given, and the following object is returned:

{"empty_known_nodes":1}

## [](#examples)Examples

The following examples demonstrate how to determine which nodes are currently in the cluster; how to rebalance after a hard failover; how to rebalance in order to eject a node from the cluster; and how to re-add an ejected node to a cluster.

For information about how to retrieve status on an ongoing rebalance, see [Getting Rebalance Progress](rest-get-rebalance-progress.md) and [Getting Cluster Tasks](rest-get-cluster-tasks.md).

### [](#return-cluster-nodes)Return Cluster Nodes

To determine which nodes are currently in the cluster, use the `GET /pools/default` HTTP method and URI. In this example, the (extensive) output is piped to the `jq` tool to be formatted, and the lines featuring the `hostname` are then filtered by `grep`, to ensure readability.

curl  -u Administrator:password -X GET \
http://10.143.190.101:8091/pools/default | jq '.' | grep hostname

The output contains the following lines, which specify all nodes currently in the cluster:

"hostname": "10.143.190.101:8091",
"hostname": "10.143.190.102:8091",
"hostname": "10.143.190.103:8091",

For more information about this method and URI, see [Viewing Cluster Details](rest-cluster-details.md).

### [](#perform-rebalance-following-a-hard-failover)Perform Rebalance Following a Hard Failover

The _hard failover_ of a node results in that node continuing to be a member of the cluster, but no longer taking part in its work. The cluster is then in an _imbalanced state_, which requires rebalance.

For more information, see [Failover](../manage/manage-nodes/fail-nodes-over.md). For information about performing a hard failover, see [Failing over Nodes](rest-node-failover.md).

To perform the rebalance, specify all cluster-nodes in the value for the `knownNodes` parameter, including the one or ones to which hard failover is known to have been applied:

curl  -u Administrator:password -v -X POST \
http://10.143.190.101:8091/controller/rebalance \
-d 'knownNodes=ns_1%4010.143.190.101%2Cns_1%4010.143.190.102%2Cns_1%4010.143.190.103'

On success, the status `200 OK` is given, and no object is returned. The failed-over node has been removed, and the work of the Analytics Service is now distributed across the surviving nodes. The successful node-removal is confirmed by again examining the current cluster nodes:

curl  -u Administrator:password -X GET \
http://10.143.190.101:8091/pools/default | jq '.' | grep hostname

The output indicates which nodes are still in the cluster:

"hostname": "10.143.190.101:8091",
"hostname": "10.143.190.102:8091",

This confirms that `10.143.190.103` has been removed.

### [](#add-a-node-to-a-cluster-then-rebalance)Add a Node to a Cluster, then Rebalance

Adding a node to a cluster is a two-step process.

1. The `POST /controller/addNode` HTTP method and URI are used to add the node. A placeholder username and password can be specified, when adding an unprovisioned node.
2. The `POST /controller/rebalance` HTTP method and URI are used to rebalance the added node into the cluster. Include the new node in the `knownNodes` node-list.

For example, the following command adds node `10.143.190.103` to the cluster from which it was removed:

curl -u Administrator:password -X POST \
http://10.143.190.101:8091/controller/addNode \
-d 'hostname=10.143.190.103&user=someName&password=somePassword'

If successful, this returns the following object, indicating that the node is now recognized as a member of the cluster:

{"otpNode":"ns_1@10.143.190.103"}

For more information about this method and URI, see [Adding Nodes to Clusters](rest-cluster-addnodes.md).

Next, the added node is rebalanced into the cluster. This allows it to take its share of the work.

curl  -u Administrator:password -v -X POST \
http://10.143.190.101:8091/controller/rebalance \
-d 'knownNodes=ns_1%4010.143.190.101%2Cns_1%4010.143.190.102%2Cns_1%4010.143.190.103'

On success, the response code `200 OK` is given, and no object is returned. The cluster is now rebalanced. At the conclusion, the cluster can again be checked for its current membership:

curl  -u Administrator:password -X GET \
http://10.143.190.101:8091/pools/default | jq '.' | grep hostname

The output now includes the following:

"hostname": "10.143.190.101:8091",
"hostname": "10.143.190.102:8091",
"hostname": "10.143.190.103:8091",

This confirms that `10.143.190.103` has been rebalanced into the cluster.

### [](#eject-a-node)Eject a Node

To eject a node, use the `POST /controller/rebalance` HTTP method and URI. Specify the entire current node-list for the cluster as the value of the `knownNodes` parameter. Specify the list of nodes to be ejected as the value of the `ejectedNodes` parameter.

For example, the following command ejects node `10.143.190.103` from the cluster:

curl  -u Administrator:password -v -X POST \
http://10.143.190.101:8091/controller/rebalance \
-d 'ejectedNodes=ns_1%4010.143.190.103' \
-d 'knownNodes=ns_1%4010.143.190.101%2Cns_1%4010.143.190.102%2Cns_1%4010.143.190.103'

On success, the response code `200 OK` is given, and no object is returned. At the conclusion, the cluster can again be checked for its current membership:

curl  -u Administrator:password -X GET \
http://10.143.190.101:8091/pools/default | jq '.' | grep hostname

The output now includes the following:

"hostname": "10.143.190.101:8091",
"hostname": "10.143.190.102:8091",

## [](#see-also)See Also

* For more information about rebalance, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md) and [Remove a Node and Rebalance](../manage/manage-nodes/remove-node-and-rebalance.md).
* For more information about how to retrieve the status of an ongoing rebalance, see [Getting Rebalance Progress](rest-get-rebalance-progress.md) and [Getting Cluster Tasks](rest-get-cluster-tasks.md).
* For more information about hard failover, see [Failover](../manage/manage-nodes/fail-nodes-over.md).
* For more information about performing a hard failover with the REST API, see [Failing over Nodes](rest-node-failover.md).
* For more information about retrieving the details of a cluster, including its current nodes, see [Viewing Cluster Details](rest-cluster-details.md).
* For more information about obtaining and reading rebalance reports, see the [Rebalance Reference](rebalance-reference.md).