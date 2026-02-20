---
title: Manage Nodes and Clusters
description: A Couchbase-Server <em>cluster</em> consists of one or more
  <em>nodes</em>, each of which is a system running an instance of Couchbase
  Server.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/manage/pages/manage-nodes/node-management-overview.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:manage:manage-nodes/node-management-overview.adoc[]
---

[View original HTML](/server/7.6/manage/manage-nodes/node-management-overview.html)

# Manage Nodes and Clusters

> A Couchbase-Server _cluster_ consists of one or more _nodes_, each of which is a system running an instance of Couchbase Server. 

## [](#managing-nodes-and-clusters)Managing Nodes and Clusters

A Couchbase Server _node_ is a physical or virtual machine that hosts a single instance of Couchbase Server. A conceptual overview is provided in [Nodes](../../learn/clusters-and-availability/nodes.md). The current section provides step-by-step procedures for node-management. This includes:

* _Initializing_ and _provisioning_ a node, thereby making it a one-node cluster.
* _Adding_ and _removing_ nodes from clusters.
* _Listing_ nodes currently in the cluster.
* Performing _failover_ on nodes, when they need to be removed from the cluster.
* _Rebalancing_ the cluster, after a node has been removed for scheduled or otherwise planned maintenance.
* _Recovering_ a node, following failover.
* _Applying_ node-to-node encryption, to ensure security of communications across the cluster.
* _Changing_ the cluster’s address family.

## [](#prerequisites)Prerequisites

Before proceeding with the instructions in this section, you must have installed and started Couchbase Server.

For links to all per platform installation-instructions, see [Install](../../install/install-intro.md).

For information on starting and stopping Couchbase Server on different platforms, see [Startup and Shutdown](../../install/startup-shutdown.md).

## [](#certificate-management)Certificate Management

The examples in this section assume that nodes are protected with the out-of-the-box, _self-signed_ SSL/TLS certificate that is provided with Couchbase Server by default. This allows nodes to be added to the cluster with no need for explicit certificate-related management; since each node has the same certificate. However, this certificate is only intended for use in pre-production environments.

If, across the cluster, an _authority-signed_ certificate is substituted for the default (as would be required for production deployments), no further node can subsequently be added until a certificate signed by the same authority has been installed on it. An attempt incorporate into a cluster a new node that is not appropriately certificate-protected results in an error. For more information, see [Node Certificates](../../learn/clusters-and-availability/nodes.md#node-certificates).

## [](#node-management-and-community-edition)Node Management and Community Edition

Couchbase has modified the license restrictions to its Community Edition package for Couchbase Server Version 7.0 and higher. In consequence, the size of an individual cluster running Community Edition is restricted to _five_ nodes. See [Couchbase Modifies License of Free Community Edition Package](https://blog.couchbase.com/couchbase-modifies-license-free-community-edition-package/), for further information on the new restrictions.

If an administrator attempts to add a sixth node to a five-node cluster running Community Edition Version 7.0 or higher, the following notification is provided, at the lower-left of Couchbase Web Console:

![sixth node addition message ce](../_images/manage-nodes/sixth-node-addition-message-ce.png) 

Community-Edition administrators who wish to upgrade cluster of six or more nodes to Couchbase Server Version 7.0 or later are recommended to consult [Couchbase Modifies License of Free Community Edition Package](https://blog.couchbase.com/couchbase-modifies-license-free-community-edition-package/), for guidance.