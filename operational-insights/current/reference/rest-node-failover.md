---
title: Performing Hard Failover
description: <em>Hard</em> failover can be used to take a node out of a cluster,
  when the node has become unresponsive.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-node-failover.adoc
  xref: xref:enterprise-analytics:reference:rest-node-failover.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-node-failover.html)

# Performing Hard Failover

> _Hard_ failover can be used to take a node out of a cluster, when the node has become unresponsive. 

## [](#http-method-and-uri)HTTP Method and URI

POST /controller/failOver

## [](#description)Description

When a node has become unresponsive, hard failover should be used to take the unresponsive node out of the cluster.

When hard failover is complete, the failed-over node no longer takes part in the work of the Analytics Service, but the node has not yet been fully taken out of the cluster. The cluster is at this point considered to be in a _degraded state_, in terms of availability, and may lack resources for handling a further node-outage. Rebalance should therefore be performed.

Hard failover should _not_ be used as part of regular, planned maintenance activities that can be conducted with all cluster-nodes available. For information, see [Failover](../manage/manage-nodes/fail-nodes-over.md).

## [](#curl-syntax)Curl Syntax

curl -v -X POST -u <username>:<password>
  http://<ip-address-or-hostname>:<port>/controller/failOver
  -d [otpNode=node_1@<hostname>]
  -d allowUnsafe=< true | false >

The value of each specified `otpNode` parameter must be the name of a node that will be hard-failed over.

The value of `allowUnsafe` must be either `true` or `false` (which is the default); indicating whether or not hard failover should be attempted in _unsafe_ mode. For information, see [Failover of Multiple Unresponsive Nodes](../manage/manage-nodes/fail-nodes-over.md#failover-with-unresponsive-nodes).

## [](#responses)Responses

Success returns `200 OK`.

Incorrectly specifying the target cluster returns `Failed to connect`. Incorrectly specifying the URI returns a `404 Object Not Found` error, and a `Requested resource not found` notification.

Specifying an unknown server to be failed over returns a `400 Bad Request` notification, and an error message such as the following: `Unknown server given: ["ns_1@10.143.201.106"]`.

Failure to authenticate returns a `401 Unauthorized` notification.

## [](#examples)Examples

The following curl statement performs a hard failover of node `10.142.180.102` from a cluster identified as `10.142.180.1`.

```bourne
curl -v -X POST -u Administrator:password \
http://10.142.180.1:8091/controller/failOver \
-d 'otpNode=ns_1@10.142.180.102'
```

The following performs a hard failover of nodes `10.142.180.102` and `10.142.180.103` from a cluster identified as `10.142.180.1`. Note that multi-node failover is always _hard_ failover.

```bourne
curl -v -X POST -u Administrator:password \
http://10.142.180.1:8091/controller/failOver \
-d 'otpNode=ns_1@10.142.180.102' \
-d 'otpNode=ns_1@10.142.180.103'
```

The following performs an _unsafe_, hard failover of nodes `10.142.180.102` and `10.142.180.103` from a cluster identified as `10.142.180.1`.

```bourne
curl -v -X POST -u Administrator:password \
http://10.142.180.1:8091/controller/failOver \
-d otpNode=ns_1%4010.142.180.102\&otpNode=ns_1%4010.142.180.103 \
-d allowUnsafe=true
```

## [](#see-also)See Also

For information about managing failover with the UI, CLI, and the REST API, see [Fail a Node Over and Rebalance](../manage/manage-nodes/fail-nodes-over.md). For information about _unsafe_ hard failover, see [Failover of Multiple Unresponsive Nodes](../manage/manage-nodes/fail-nodes-over.md#failover-with-unresponsive-nodes). For information about recovering a failed-over node, see [Recover a Node and Rebalance](../manage/manage-nodes/recover-nodes.md).