---
title: List Cluster Nodes
description: The nodes of a cluster can be listed, and details on each retrieved.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/manage/pages/manage-nodes/list-cluster-nodes.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:manage:manage-nodes/list-cluster-nodes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/manage/manage-nodes/list-cluster-nodes.html)

# List Cluster Nodes

> The nodes of a cluster can be listed, and details on each retrieved. 

## [](#listing-nodes)Listing Nodes

Enterprise Analytics allows the nodes of a cluster to be listed, and data retrieved on each.

## [](#examples-on-this-page-node-listing)Examples on This Page

The examples in the subsections below show how the nodes of the same cluster can be listed, using the [UI](#list-nodes-with-the-ui), the [CLI](#list-nodes-with-the-cli), and the [REST API](#list-nodes-with-the-rest-api) respectively.

The examples assume:

* A two-node cluster already exists; as at the conclusion of [Join a Cluster and Rebalance](join-cluster-and-rebalance.md).
* The cluster has the Full Administrator username of `Administrator`, and password of `password`.

## [](#list-nodes-with-the-ui)List Nodes with the UI

All nodes in the current cluster can be viewed on the **Servers** screen of Enterprise Analytics Web Console. Note that this display is identical for all nodes in the cluster: therefore, whether you open the console on node one or node two of a two-node cluster, the same information is provided.

Proceed as follows:

1. Access the Enterprise Analytics Web Console **Servers** screen, on either node `10.142.181.101` or node `101.142.181.102`, by clicking on the **Servers** tab in the left-hand navigation bar. The **Servers** screen displays a tabular view showing the cluster currently consists of the nodes `10.142.181.101` and `101.142.181.102`. Each row in the table represents a node and provides the following details in columns across the interface:

  * **name**: The name of the node. In this case, each node is named after its IP address.
  * **group**: The _Group_ occupied by the node. For information, see [Server Group Awareness](../../../../server/current/learn/clusters-and-availability/groups.md).
  * **CPU**: The percentage of available CPU resources currently occupied.
  * **RAM**: The percentage of available RAM currently occupied. For information about Couchbase memory-management, see [Memory](../../../../server/current/learn/buckets-memory-and-storage/memory.md).
  * **swap**: The percentage of available swap space in use.
  * **disk used**: The amount of disk space currently used, in megabytes.
2. To see further details of each node, click on the row for the node. The row expands vertically to reveal additional detailed information about the selected node. The additional information now shown includes:

  * **Addresses** section showing the internal IP address and any external (alternate) addresses if configured.
  * **Address Family** indicating IPv4 or IPv6 configuration.
  * **Node-to-Node Encryption** status showing whether encryption is enabled or disabled.
  * **OS** version, Enterprise Analytics **Version**, **Uptime**, and **RAM Quota**.
  * **Storage Paths** specified during node-initialization.
  * Currently available memory and disk-space statistics.
3. Click on the **Statistics** tab for `10.142.181.101`, at the right-hand side of the row. The **Statistics** screen is displayed, providing comprehensive statistics related to each of the buckets on the cluster. These statistics include information about the **Active Data Size**, **Data Total Disk Size**, and **Data Fragmentation**, along with various performance metrics and operational data. For more information, see [Monitor with the UI](../monitor/monitor-intro.md).

## [](#list-nodes-with-the-cli)List Nodes with the CLI

To list the nodes of a cluster with the CLI, use the `server-list` command, as follows:

/opt/enterprise-analytics/bin/couchbase-cli
--username Administrator \
--password password

The output is as follows:

ns_1@10.142.181.101 10.142.181.101:8091 healthy active
ns_1@10.142.181.102 10.142.181.102:8091 healthy active

On occasions when a node is inactive or failed, output of the following kind is produced:

ns_1@10.142.181.101 10.142.181.101:8091 healthy active
ns_1@10.142.181.102 10.142.181.102:8091 healthy inactiveFailed

Alternatively, the CLI `host-list` command can be used:

/opt/enterprise-analytics/bin/couchbase-cli

Note that the command above specifies the second node in the cluster: any node-name in the cluster can be used, with the same results. The output is as follows:

10.142.181.101:8091
10.142.181.102:8091

Thus, the command returns a list of IP addresses and Enterprise Analytics Web Console port numbers.

For more information, see the command reference for [server-list](../../cli/couchbase-cli-server-list.md) and [host-list](../../cli/couchbase-cli-host-list.md).

## [](#list-nodes-with-the-rest-api)List Nodes with the REST API

To list all nodes in a cluster by means of the REST API, use the `/pools/default` URI. A Couchbase _pool_ represents computing resources (such as machines, memory, CPU, and disks) that are used to host Couchbase buckets. Enterprise Analytics clusters support a single pool, named `default`.

The method returns a large amount of information, which includes many of the details used in the Enterprise Analytics Web Console `Statistics` panel, described above. The output may be unformatted, and thereby difficult to read until formatting is applied.

The following call passes the result to the [jq](https://stedolan.github.io/jq/) command-line JSON processor for formatting, and then uses the standard command-line utility `egrep` to reduce the output to available hostnames and otpNode names:

curl  -u Administrator:password -v -X GET \
http://10.142.181.101:8091/pools/default | jq '.' | egrep 'hostname|otpNode'

The output is as follows:

"otpNode": "ns_1@10.142.181.101",
"hostname": "10.142.181.101:8091",
"otpNode": "ns_1@10.142.181.102",
"hostname": "10.142.181.102:8091",

As shown in the example REST API command below, the otpNode value can be used with the `/nodes/<otpNode>` URI to retrieve detailed information about the node, including the storage paths for the services:

curl -u Administrator:password -v -X GET \
http://10.142.181.101:8091/nodes/ns_1@10.142.181.101 | jq '.'

For more information, see [Retrieving Cluster Information](../../reference/rest-cluster-get.md).

## [](#next-steps-after-list-nodes)Next Steps

Now that you have built a cluster and examined the nodes it contains, learn details on how to [Remove a Node and Rebalance](remove-node-and-rebalance.md).