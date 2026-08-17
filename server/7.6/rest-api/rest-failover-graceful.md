---
title: Performing Graceful Failover
description: Graceful failover can be performed by means of the REST API.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-failover-graceful.adoc
  xref: xref:7.6@server:rest-api:rest-failover-graceful.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/rest-api/rest-failover-graceful.html)

# Performing Graceful Failover

> Graceful failover can be performed by means of the REST API. 

## [](#http-method-and-uri)HTTP method and URI

POST /controller/startGracefulFailover

## [](#description)Description

Initiates graceful failover for one or more server nodes. The Full Admin or Cluster Admin role is required.

## [](#curl-syntax)Curl Syntax

POST /controller/startGracefulFailover
    [ -d <node-to-be-gracefully-failed-over> ]

Each server node to be gracefully failed over is specified with the `<node-to-be-gracefully-failed-over>` parameter. This must consist of the string `otpNode=ns_1@` followed by the IP address or domain-name of the node. If multiple nodes are to be gracefully failed over, each should be specified separately, with multiple occurrences of the `-d` flag.

Note that the progress of graceful failover can be tracked: see [Getting Cluster Tasks](rest-get-cluster-tasks.md).

Subsequent to a successful graceful failover, the cluster must be rebalanced. See [Rebalance](rest-rebalance-overview.md).

## [](#responses)Responses

Success returns `200 OK`. Failure to specify a node correctly returns `400 Bad Request`, and an error message such as `Unknown server given: ["ns_1@10.144.220.108"]`. Failure to authenticate returns `401 Unauthorized`. Incorrect specification of the URI returns `404 Object Not Found`.

## [](#example)Example

The following example gracefully fails over two nodes from a cluster.

curl -u Administrator:password  \
http://10.144.220.101:8091/controller/startGracefulFailover  \
-d otpNode=ns_1%4010.144.220.103  \
-d otpNode=ns_1%4010.144.220.104

If graceful failover is successfully initiated and completed, the cluster should then be rebalanced, specifying all nodes in the cluster (including those gracefully failed over) as `knownNodes`, and additionally specifying those gracefully failed over as `ejectedNodes`. For example:

curl  -u Administrator:password -v -X POST \
http://10.144.220.101:8091/controller/rebalance \
-d 'knownNodes=ns_1@10.144.220.101,ns_1@10.144.220.102,ns_1@10.144.220.103,ns_1@10.144.220.104&ejectedNodes=ns_1@10.144.220.103,ns_1@10.144.220.104'

## [](#see-also)See Also

For a conceptual overview of nodes and their management, see [Nodes](../learn/clusters-and-availability/nodes.md). For practical examples of node management by means of UI, CLI, and REST API, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).

For information on tracking an ongoing graceful failover, see [Getting Cluster Tasks](rest-get-cluster-tasks.md). For information on rebalancing a cluster with the REST API, see [Rebalance](rest-rebalance-overview.md).