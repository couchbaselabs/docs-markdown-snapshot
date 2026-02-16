[View original HTML](/server/current/manage/manage-nodes/node-management-overview.html)

> A Couchbase-Server _cluster_ consists of one or more _nodes_, each of which is a system running an instance of Couchbase Server. 

## [](#managing-nodes-and-clusters)Managing Nodes and Clusters

A Couchbase Server node is a physical or virtual machine that hosts a single instance of Couchbase Server. A conceptual overview is provided in [Nodes](../../learn/clusters-and-availability/nodes.md). The current section provides step-by-step procedures for node-management. This includes:

* Initializing and provisioning a node, thereby making it a one-node cluster.
* Adding and removing nodes from clusters.
* Listing nodes currently in the cluster.
* Performing failover on nodes, when they need to be removed from the cluster.
* Rebalancing the cluster, after a node has been removed for scheduled or otherwise planned maintenance.
* Recovering a node, following failover.
* Modifying services on nodes, to add or remove Multi-Dimensional Scaling (MDS) services, and rebalancing.
* Applying node-to-node encryption, to ensure security of communications across the cluster.
* Changing the cluster’s address family.

## [](#prerequisites)Prerequisites

Before proceeding with the instructions in this section, you must have installed and started Couchbase Server.

For links to all per platform installation-instructions, see [Install](../../install/install-intro.md).

For information on starting and stopping Couchbase Server on different platforms, see [Startup and Shutdown](../../install/startup-shutdown.md).

## [](#certificate-management)Certificate Management

The examples in this section assume that nodes are protected with the out-of-the-box, self-signed SSL/TLS certificate that is provided with Couchbase Server by default. This allows nodes to be added to the cluster with no need for explicit certificate-related management; since each node has the same certificate. However, this certificate is only intended for use in pre-production environments.

If, across the cluster, an authority-signed certificate is substituted for the default (as would be required for production deployments), no further node can subsequently be added until a certificate signed by the same authority has been installed on it. An attempt incorporate into a cluster a new node that is not appropriately certificate-protected results in an error. For more information, see [Node Certificates](../../learn/clusters-and-availability/nodes.md#node-certificates).

## [](#node-management-and-community-edition)Node Management and Community Edition

Couchbase has modified the license restrictions to its Community Edition package for Couchbase Server Version 7.0 and higher. In consequence, the size of an individual cluster running Community Edition is restricted to 5 nodes. See [Couchbase Modifies License of Free Community Edition Package](https://blog.couchbase.com/couchbase-modifies-license-free-community-edition-package/), for further information on the new restrictions.

If an administrator attempts to add a sixth node to a five-node cluster running Community Edition Version 7.0 or higher, the following notification is provided, at the lower-left of Couchbase Web Console:

![sixth node addition message ce](../_images/manage-nodes/sixth-node-addition-message-ce.png) 

Community-Edition administrators who wish to upgrade cluster of six or more nodes to Couchbase Server Version 7.0 or later are recommended to consult [Couchbase Modifies License of Free Community Edition Package](https://blog.couchbase.com/couchbase-modifies-license-free-community-edition-package/), for guidance.