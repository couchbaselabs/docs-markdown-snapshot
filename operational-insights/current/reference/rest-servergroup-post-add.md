---
title: Adding Nodes to Groups
description: A node can be added to the cluster and simultaneously added to an
  existing server group with the <code>POST
  /pools/default/serverGroups/<:uuid>/addNode</code> HTTP method and URI.
pubDate: 2026-10-28T04:21:06.350Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-servergroup-post-add.adoc
  xref: xref:enterprise-analytics:reference:rest-servergroup-post-add.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-servergroup-post-add.html)

# Adding Nodes to Groups

> A node can be added to the cluster and simultaneously added to an existing server group with the `POST /pools/default/serverGroups/<:uuid>/addNode` HTTP method and URI. 

## [](#http-method-and-uri)HTTP method and URI

POST /pools/default/serverGroups/<:uuid>/addNode

## [](#description)Description

This adds a node to a cluster, and assigns it to the specified group.

For an overview of nodes, and of the process of adding nodes to clusters, see [Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).

> [!NOTE]
> The node to be added needs only to have been installed and started. If it has been _initialized_, data-paths so established will be retained, following addition. However, if the node to be added has been _provisioned_, all results of that provisioning will be deleted by the addition-process. This includes memory-quotas, and all established usernames and passwords.

Following successful addition, rebalance is required. For an overview, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md). For examples of performing rebalance, see [Rebalancing Nodes](rest-cluster-rebalance.md).

## [](#curl-syntax)Curl Syntax

curl -X POST -d hostname=<host>:<port>
  -d user=<administrator>
  -d password=<password>
  -u <administrator>:<password>
  http://<host>:<port>/pools/default/serverGroups/<uuid>/addNode

The syntax includes the following:

* `hostname`. The hostname and port of the node to be added.
* `user` and `password`. The username and password for the node to be added. If the node has not yet been provisioned, placeholder username and password should be specified.
* `uuid`. This path-parameter identifies the server group to which the node is to be assigned. To retrieve this prior to node-addition, use the procedure described in [Getting Server Group Information](rest-servergroup-get.md).

## [](#responses)Responses

Success gives `200 OK`, and returns an object signifying that the nodes specified for addition has been duly added to the cluster (see the example given below). An incorrectly specified `uuid` gives `404 Object Not Found`, and returns an object of the form `["Could not find group with uuid: <submitted-uuid>"]`. Failure to authenticate gives `401 Unauthorized`. Failure to specify username and password for the node to be added gives `400 Bad Request`, and returns an object of the form `["user is missing","password is missing"]`.

## [](#example)Example

The following example assumes that the cluster has two groups, `Group 1` and `Group 2`. The `uuid` for `Group 2` has been returned as `246b5de857e100dbfd8b6dee0406420a`. The following request therefore adds a new node, `10.143.190.104` to the cluster, and assigns it to `Group 2`.

curl -X POST -d hostname=10.143.190.104:8091 \
-d user=Administrator -d password=password \
-u Administrator:password \
http://10.143.190.101:8091/pools/default/serverGroups/\
3b66b3c3177f44a3ffa6771ffeb31f36/addNode

If successful, the request returns the following object, which indicates that the new node has been added to the cluster:

{"otpNode":"ns_1@10.143.190.104"}

## [](#see-also)See Also

For an overview of nodes, and of the process of adding nodes to clusters, see [Nodes and Clusters](../manage/manage-nodes/node-management-overview.md). See [Getting Server Group Information](rest-servergroup-get.md) for getting information about the current node-to-group configuration for the server.