[View original HTML](/enterprise-analytics/current/manage/manage-nodes/node-management-overview.html)

> A Couchbase-Server _cluster_ consists of one or more _nodes_, each of which is a system running an instance of Enterprise Analytics. 

## [](#managing-nodes-and-clusters)Managing Nodes and Clusters

An Enterprise Analytics _node_ is a physical or virtual machine that hosts a single instance of Enterprise Analytics. A conceptual overview is provided in [Nodes](../../../../server/current/learn/clusters-and-availability/nodes.md). The current section provides step-by-step procedures for node-management. This includes:

* _Initializing_ and _provisioning_ a node, thereby making it a one-node cluster.
* _Adding_ and _removing_ nodes from clusters.
* _Listing_ nodes currently in the cluster.
* Performing _failover_ on nodes, when they need to be removed from the cluster.
* _Rebalancing_ the cluster, after a node has been removed for scheduled or otherwise planned maintenance.
* _Recovering_ a node, following failover.
* _Applying_ node-to-node encryption, to ensure security of communications across the cluster.
* _Changing_ the cluster’s address family.

## [](#prerequisites)Prerequisites

Before proceeding with the instructions in this section, you must have installed and started Enterprise Analytics.

For links to all per platform installation-instructions, see [Install](../../install/supported-platform.md).

For information about starting and stopping Enterprise Analytics on different platforms, see [Start and Stop](../../install/start-stop-cb-enterprise-analytics.md).

## [](#certificate-management)Certificate Management

The examples in this section assume that nodes are protected with the out-of-the-box, _self-signed_ SSL/TLS certificate that is provided with Enterprise Analytics by default. This allows nodes to be added to the cluster with no need for explicit certificate-related management; since each node has the same certificate. However, this certificate is only intended for use in pre-production environments.

If, across the cluster, an _authority-signed_ certificate is substituted for the default (as would be required for production deployments), no further node can subsequently be added until a certificate signed by the same authority has been installed on it. An attempt incorporate into a cluster a new node that is not appropriately certificate-protected results in an error. For more information, see [Node Certificates](../../../../server/current/learn/clusters-and-availability/nodes.md#node-certificates).