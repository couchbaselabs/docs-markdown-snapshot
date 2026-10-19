---
title: Identifying the Orchestrator Node
description: The node currently running the <em>orchestrator</em> (sometimes
  referred to as the <em>Master Services</em>) can be identified by means of the
  REST API.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-identify-orchestrator.adoc
  xref: xref:enterprise-analytics:reference:rest-identify-orchestrator.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-identify-orchestrator.html)

# Identifying the Orchestrator Node

> The node currently running the _orchestrator_ (sometimes referred to as the _Master Services_) can be identified by means of the REST API. 

## [](#http-method-and-uri)HTTP Method and URI

GET /pools/default/terseClusterInfo

## [](#description)Description

The _orchestrator_ handles operations with cluster-wide impact; such as failover and rebalance. Every Operational Insights node contains an instance of the orchestrator. However, at any given time, on a multi-node cluster, only one instance of the orchestrator, on one particular node, is active; and thereby responsible for performing _all_ the cluster-wide operations. If a hitherto active instance becomes unavailable, another instance, on another node, takes over.

The `GET /pools/default/terseClusterInfo` http method and URI identify the node on which the active orchestrator currently resides.

For more information about the orchestrator and the cluster manager, see [Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).

This http method and URI are available in Operational Insights.

## [](#curl-syntax)Curl Syntax

curl -v -X GET -u <username>:<password>
  http://<ip-address-or-domain-name>:8091/pools/default/terseClusterInfo

The `ip-address-or-domain-name` should specify a node within the cluster whose orchestrator-location is to be determined: information returned by the call is that which is _known to the specified node_. The `username` and `password` must a user with one of the roles listed in the next section.

## [](#required-privileges)Required Privileges

You must have one of the following roles to call this method:

* Full Admin
* Cluster Admin
* Analytics Admin
* Analytics Reader
* Read-Only Admin
* Security Admin
* Read-Only Security Admin
* Local User Admin
* External User Admin

For information about these roles, see [User Role Privileges](../manage/manage-security/user-roles-privileges.md).

## [](#responses)Responses

Success returns `200 OK`, and an object that contains the following key-value pairs:

* `clusterUUID`. The universally unique identifier of the cluster whose orchestrator-node is being returned.
* `orchestrator`. A reference to the node on which the orchestrator is believed, by the specified node, to be running at the time the call is executed. This value is `"undefined"` if, for any reason, the specified node is unaware of the orchestrator-location. In particular, if the orchestrator node is rebalanced out, the value of this attribute will be `"undefined"` during the time-period that starts immediately after the node is rebalanced out, and lasts until a new orchestrator is elected: this period is _10 seconds_ in duration.  
Note that the location of the orchestrator may change at any time, including at a point subsequent to execution of the call but prior to the return of a value; meaning that the returned value is already incorrect. Note also that in cases where the cluster has undergone an unexpected network partition, different specified nodes may return different values.
* `isBalanced`. The value is `true` if the specified node believes that data is distributed evenly, topology-aware services are in balance, and no rebalance is required. Otherwise, the value is `false`.
* `clusterCompatVersion`. The minimum Operational Insights _compatibilty version_ for the cluster. This is the compatibility version of the oldest node in the cluster.

Failure to authenticate returns `401 Unauthorized`. An incorrectly specified URI returns `404 Object Not Found`.

## [](#example)Example

The following example returns the orchestrator-location for a cluster that includes a node whose IP address is `10.143.210.102`. Note that the output is piped to the [jq](https://jqlang.org/) command, to facilitate readability:

curl -v -X GET -u Administrator:password \
http://10.143.210.102:8091/pools/default/terseClusterInfo | jq '.'

If the call is successful, `200 OK` is returned, with the following output:

{
  "clusterUUID": "58ea8d6385837b4aa60755a9a6ab81bb",
  "orchestrator": "ns_1@node3.",
  "isBalanced": true,
  "clusterCompatVersion": "8.0"
}

The output thus provides the UUID of the cluster, and the orchestrator-location (which is the node whose IP address is `10.143.210.101`). It also verifies that the cluster currently does not require rebalance, and that its minimum compatibility version is 8.0.

## [](#see-also)See Also

For more information about nodes and the cluster, see [Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).