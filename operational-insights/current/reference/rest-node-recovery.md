---
title: Setting Recovery Type
description: Node recovery type is set with the <code>POST
  /controller/setRecoveryType</code> HTTP method and URI.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-node-recovery.adoc
  xref: xref:enterprise-analytics:reference:rest-node-recovery.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-node-recovery.html)

# Setting Recovery Type

> Node recovery type is set with the `POST /controller/setRecoveryType` HTTP method and URI. 

## [](#http-method-and-uri)HTTP method and URI

Sets the recovery type to be performed for a node that has been failed over. The recovery type for a node is set after the node is failed over and before rebalance. Rebalance is required to apply the recovery.

POST /controller/setRecoveryType

Specify `recoveryType=full`.

## [](#syntax)Syntax

POST /controller/setRecoveryType
    otpNode=[node@hostname]
    recoveryType=full

The `otpNode` parameter specifies the node to be recovered, in the form `ns_1@<hostname>`. The node must currently be failed over, or already marked for recovery.

## [](#example)Example

The following Curl request example sets full recovery for a failed-over node.

curl -u Administrator:password -d 'otpNode=ns_1@10.5.2.118' -d 'recoveryType=full' \
http://10.5.2.54:8091/controller/setRecoveryType

If successful, the call returns an empty array. The node must then be rebalanced back into the cluster: see [Rebalancing the Cluster](rest-cluster-rebalance.md).

## [](#response-codes)Response codes

200       // Request succeeded
400       // recoveryType and/or otpNode could not be understood by the server,
             or the node is not in a failed-over state

If the call fails, the response is an object that names each parameter in error. For example:

{"otpNode":"invalid node name or node can't be used for delta recovery"}

## [](#see-also)See Also

For an overview of recovering a node, see [Recover a Node and Rebalance](../manage/manage-nodes/recover-nodes.md). For information on failing a node over, see [Failover](../manage/manage-nodes/fail-nodes-over.md). To perform recovery with the CLI, see [recovery](../cli/couchbase-cli-recovery.md).