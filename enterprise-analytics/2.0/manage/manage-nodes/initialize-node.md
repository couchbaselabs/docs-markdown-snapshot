---
title: Initialize a Node
description: A new Enterprise Analytics node can be <em>initialized</em>, to
  establish node-specific paths for local storage.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/manage/pages/manage-nodes/initialize-node.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:manage:manage-nodes/initialize-node.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/manage/manage-nodes/initialize-node.html)

# Initialize a Node

> A new Enterprise Analytics node can be _initialized_, to establish node-specific paths for local storage. 

## [](#understanding-initialization)Understanding Initialization

Following installation and start-up of Enterprise Analytics, a node must be:

* _Initialized_, whereby its disk-paths for data, indexes, analytics, and eventing can be established.
* _Provisioned_, whereby all other details, including Full Administrator credentials, service assignments, and memory quota-definitions are established.

Optionally, _initialization_ can be performed explicitly and independently of provisioning, as a prior process, in order to establish custom disk-paths. When the node is subsequently provisioned, these are preserved (unless, as is possible with UI-based provisioning, they are optionally overwritten, and the node is thus re-initialized).

If initialization is not explicitly performed, it will occur as part of the eventual provisioning process, and default disk-path values will be applied.

Note that disk-paths cannot be changed after a node has been _provisioned_, and has thus either become a cluster of one node, or has been added to a cluster of other nodes.

Note also that initialization allows a node to be _named_. Before assigning a name to the node, read the information provided in [Naming Clusters and Nodes](https://docs.couchbase.com/server/current/learn/clusters-and-availability/nodes.html#naming-clusters-and-nodes).

## [](#examples-on-this-page-node-initialization)Examples on This Page

The examples in the subsections below show how to initialize the same node; using the [CLI](#initialize-a-node-with-the-cli), and the [REST API](#initialize-a-node-with-the-rest-api) respectively.

The examples assume:

* Enterprise Analytics has been installed and started.
* The IP address of the node is `10.142.181.103`.

### [](#using-the-ui-to-initialize)Using the UI to Initialize

UI-based initialization can only be performed as part of the overall _provisioning_ process. This is described in [Create a Cluster](create-cluster.md).

Note that in Enterprise Analytics UI-based initialization provides _additional options_ for establishing the _address family_ for the cluster: if you wish to _restrict_ (rather than merely _require_) your cluster to use either IPv4 or IPv6, initialize by means of the UI, as described in [Create a Cluster](create-cluster.md).

The instructions provided below for CLI and REST allow you to _require_ either IPv4 or IPv6 as the address family for the cluster: thus, if connectivity by means of the selected address family is not available for some reason, the cluster and its services do not start; and corrective action can be taken. Once connectivity is established with the required address family, communications by means of the other address family are still permitted.

information about managing address families for the cluster _after_ the cluster has been established are provided in [Manage Address Families](manage-address-families.md).

## [](#initialize-a-node-with-the-cli)Initialize a Node with the CLI

To initialize a node with the CLI, use the `node-init` command, as follows:

/opt/enterprise-analytics/bin/couchbase-cli node-init -c 10.142.181.103 \
-u placeholdername -p placeholderpwd \
--node-init-data-path /opt/enterprise-analytics/var/lib/couchbase/data \
--node-init-hostname node1-devcluster.com \
--ipv4

This initializes the disk-paths for data, indexes, eventing, and analytics on node `10.142.181.103` to the values shown. Note that the command requires that a username and password be specified, although the node has not yet been provisioned with credentials. Placeholders are therefore provided: these can be overwritten during subsequent provisioning. The command specifies IPv4 as the address family for the node, and assigns the node a hostname of `node1-devcluster.com`. (To specify IPv6, use the `--ipv6` flag instead.) The command also specifies an administrator-created folder, `/opt/enterprise-analytics/bin/java`, as the path for an alternative Java Runtime Environment (JRE), already installed on the current node, to be used for the Analytics Service.

If successful, the operation returns the following:

SUCCESS: Node initialized

For more information, see the reference for the [node-init](../../cli/couchbase-cli-node-init.md) command.

## [](#initialize-a-node-with-the-rest-api)Initialize a Node with the REST API

To initialize a node with the REST API, use the `POST /nodes/self/controller/settings` http method and URI, as follows:

curl  -u Administrator:password -v -X POST \
  http://10.142.181.103:8091/nodes/self/controller/settings \
  -d 'data_path=%2Fopt%2Fcouchbase%2Fvar%2Flib%2Fcouchbase%2Fdata&' \
  -d 'cbas_path=%2Fopt%2Fcouchbase%2Fvar%2Flib%2Fcouchbase%2Fadata&' \
  -d 'java_home=%2Fopt%2Fcouchbase%2Fbin%2Fjava'

This initializes the disk-paths for data(metadata), and analytics(storage) on node `10.142.181.103` to the values shown.

To assign a name to the node, the `POST /node/controller/rename` http method and URI can be used, as follows:

curl -v -X POST -u Administrator:password \
http://10.143.192.103:8091/node/controller/rename \
-d hostname=node1-devcluster.com

This assigns the name `node1-devcluster.com` to the node.

## [](#next-steps-after-initializing)Next Steps

Following initialization, a node can be _provisioned_ so as to become a Couchbase Cluster of one node. See [Create a Cluster](create-cluster.md) for details.