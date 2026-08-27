---
title: Getting Rebalance Progress
description: The progress of rebalance can be ascertained with the <code>GET
  /pools/default/rebalanceProgress</code> HTTP method and URI.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/reference/pages/rest-get-rebalance-progress.adoc
  xref: xref:enterprise-analytics:reference:rest-get-rebalance-progress.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/reference/rest-get-rebalance-progress.html)

# Getting Rebalance Progress

> The progress of rebalance can be ascertained with the `GET /pools/default/rebalanceProgress` HTTP method and URI. 

## [](#http-method-and-uri)HTTP method and URI

GET /pools/default/rebalanceProgress

## [](#rest-cluster-rebalance-description)Description

When one or more nodes have been brought into a cluster, or have been taken out of a cluster, _rebalance_ is used to redistribute data, indexes, event processing, and query processing among available nodes. The ongoing progress of the rebalance operation can be retrieved.

## [](#curl-syntax)Curl Syntax

curl -v -X GET -u [admin]:[password]
  http://[localhost]:8091/pools/default/rebalanceProgress

## [](#response)Response

Success gives the response code `200 OK`, and returns an object containing information about the current status of the ongoing rebalance. See the examples provided below.

## [](#examples)Examples

In the following example, node `10.143.190.103` has been added to a cluster of two nodes, which are `10.143.190.101` and `10.143.190.102`. Rebalance is then initiated. During rebalance, progress is ascertained by means of the `GET /pools/default/rebalanceProgress` HTTP method and URI, with output being piped to the tool `jq`, to ensure readability.

curl -u Administrator:password -v -X GET 10.143.190.101:8091/pools/default/rebalanceProgress | jq '.'

On success, the response code `200 OK` is given, and the following object is returned:

{
  "status": "running",
  "ns_1@10.143.190.101": {
    "progress": 0.1103515625
  },
  "ns_1@10.143.190.102": {
    "progress": 0.1095890410958904
  },
  "ns_1@10.143.190.103": {
    "progress": 0.3299120234604106
  }
}

The output thus features `progress`, specified as a ten-place floating-point number, for each of the three nodes. (Note that if Couchbase Web Console is simultaneously used to monitor the rebalance, these decimals are represented as _11.0%_, _10.9%_, and _32.9%_ respectively. See the example provided in [Add a Node with the UI](../manage/manage-nodes/add-node-and-rebalance.md#rebalance-progress-add-node).)

When rebalance has concluded, re-running the method returns the response code `200 OK`, and the following object:

{
  "status": "none"
}

## [](#see-also)See Also

Examples of adding a node and rebalancing by means of the UI, CLI, and REST API are provided in [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md). A conceptual introduction to nodes is provided in [Nodes](#learn:clusters-and-availability/nodes.adoc). The REST method and URI for node-addition is provided in [Adding Nodes to Clusters](rest-cluster-addnodes.md). The REST method and URI for rebalance is explained in [Rebalancing Nodes](rest-cluster-rebalance.md).

For additional information about retrieving status on ongoing cluster-tasks, including rebalance, see [Getting Cluster Tasks](rest-get-cluster-tasks.md). For information about obtaining and reading _rebalance reports_, see the [Rebalance Reference](#rebalance-reference:rebalance-reference.adoc).