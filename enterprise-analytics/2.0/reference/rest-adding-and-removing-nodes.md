---
title: Node Addition and Removal
description: Nodes can be added to and removed from a cluster, by means of the REST API.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/reference/pages/rest-adding-and-removing-nodes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.0@enterprise-analytics:reference:rest-adding-and-removing-nodes.adoc[]
---

[View original HTML](/enterprise-analytics/2.0/reference/rest-adding-and-removing-nodes.html)

# Node Addition and Removal

> Nodes can be added to and removed from a cluster, by means of the REST API. 

## [](#apis-in-this-section)APIs in this Section

A Couchbase-Server cluster consists of one or more nodes, each of which is a system running an instance of Enterprise Analytics. Nodes can be added to and removed from the cluster, by means of the REST API.

The routine for _adding_ a new node to the existing cluster is executed on the existing cluster. The routine for _joining_ an existing cluster is executed on the new node. These procedures are described in detail in [Nodes](#learn:clusters-and-availability/nodes.adoc).

_Removal_ provides the most highly controlled means of taking a node out of a cluster. Any node, whatever its service-configuration, can be removed. However, removal should be used only when all nodes in the cluster are responsive, and those intended to remain in the cluster after removal have the capacity to support the results. This is described in detail in [Removal](#learn:clusters-and-availability/removal.adoc).

The REST API described in this section is summarized below.

| HTTP Method | URI                            | Documented at                                              |
| ----------- | ------------------------------ | ---------------------------------------------------------- |
| POST        | /controller/addNode            | [Adding Nodes to Clusters](rest-cluster-addnodes.md)       |
| POST        | /node/controller/doJoinCluster | [Joining Nodes to Clusters](rest-cluster-joinnode.md)      |
| POST        | /controller/ejectNode          | [Removing Nodes from Clusters](rest-cluster-removenode.md) |