---
title: Connectivity
description: Couchbase Server handles client-to-cluster, node-to-node, and
  cluster-to-cluster communications.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/learn/pages/clusters-and-availability/connectivity.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/learn/clusters-and-availability/connectivity.html)

# Connectivity

> Couchbase Server handles client-to-cluster, node-to-node, and cluster-to-cluster communications. It also provides connectivity to a number of third-party products. 

## [](#communication-summary)Communication Summary

The network-communication options supported by Couchbase Server are as follows:

* _Client-to-Cluster_. Client applications communicate with a Couchbase Server-cluster through a set of server-defined access-points, each of which provides ports for both clear and encrypted communication. For detailed information, see [Couchbase Server Ports](../../install/install-ports.md).
* _Node-to-Node_. Cluster-nodes intercommunicate in order to replicate data, maintain indexes, check the health of nodes, communicate changes to the cluster-configuration, and more. See [Cluster Manager](cluster-manager.md), for detailed information. For information on how to encrypt the communications between nodes, see [Node-to-Node Encryption](node-to-node-encryption.md).
* _Cluster-to-Cluster_. Couchbase Server-clusters communicate with one another by means of _Cross Data Center Replication_. See [Cross Data Center Replication (XDCR)](xdcr-overview.md), for detailed information.
* _Cluster-to-Connector_. Couchbase Server-clusters communicate with third party products; by means of _connectors_. Connectors are provided for _Elasticsearch_, _Hadoop_, _Kafka_, _Spark_, and _Talend_. Drivers are provided for _ODBC_ and _JDBC_. See [Connector Guides](../../connectors/intro.md), for detailed information.

## [](#connectivity-phases)Connectivity Phases

Client connectivity is established in three phases: _Authentication and Authorization_, _Discovery_, and _Service Connection_.

1. _Authentication and Authorization_: The client authenticates with _username_ and _password_. If these are associated with a Couchbase-Server defined _role_, itself associated with appropriate privileges on the resource access to which is being requested, the client is authorized, and access is granted. Otherwise, access is denied. See [Authorization](../security/authorization-overview.md) for details.
2. _Discovery_: A cluster-map is returned to the client. This indicates the current cluster-topology; including the list of nodes, the data-distribution across the nodes, and the service-distribution across the nodes.
3. _Service Connection_: Once in possession of the cluster-map, the client determines the connections needed to establish and perform service-level operations. Additional authorizations may be required, depending on the operations being attempted. Note that in the event of topology-changes, a service connection-request may result in an exception; in which case discovery must be re-run, and operations retried with new connections.

## [](#managing-ip-address-families)Managing IP-Address Families

Couchbase Server supports both the IPv4 and IPv6 address families. The address family can be established as part of a cluster’s initial configuration: see [Create a Cluster](../../manage/manage-nodes/create-cluster.md) and [Initialize a Node with the CLI](../../manage/manage-nodes/initialize-node.md#initialize-a-node-with-the-cli), for details on how to do this with the UI and CLI respectively.

For information on using the CLI to change the address family for an existing cluster, see [Manage Address Families](../../manage/manage-nodes/manage-address-families.md).

### [](#services-and-ip-address-families)Services and IP-Address Families

_All_ Couchbase [Services](../services-and-indexes/services/services.md) bind on _all_ their assigned ports with the same address family — either IPv4 or IPv6, depending on which address family has been established for the cluster; either at initial configuration, or subsequently by means of the CLI. If a service cannot bind on all its assigned ports with the established address family, the service does not start. For more information, see [Couchbase Server Ports](../../install/install-ports.md).

## [](#alternate-addresses)Alternate Addresses

Couchbase Server allows an _alternate address_ to be assigned to any individual cluster-node, and an _alternate port number_ to be assigned to any service running on that node. For a list of services, and the standard ports they occupy, see [Couchbase Server Ports](../../install/install-ports.md).

When assigning an alternate address and using different port numbers than the expected, port forwarding must be enabled on the host machine. For example, on a virtual machine:

```console
iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 9000 -j REDIRECT --to-port 8093
```

This command will create a redirection from the external port 9000 to the _query service_ running on port 8093.

The assigning of alternate addresses and port numbers, which can be accomplished by means of the CLI and the REST API, may facilitate communication with external applications that are not permitted to contact a cluster’s nodes directly; but have access to a router or other networked entity that provides externally visible addresses on the nodes’ behalf. Note that an alternate address can be used to specify an XDCR _target cluster_: see [Create a Reference](../../manage/manage-xdcr/create-xdcr-reference.md).

Two possible use cases are given below.

### [](#internal-network-or-cloud-access)Internal Network or Cloud Access

Access to nodes within an internal network or cloud is shown by the following illustration:

![externalAddressDiagram01](../_images/clusters-and-availability/externalAddressDiagram01.png) 

The annotations to this diagram are as follows:

1. Within an internal network or cloud environment, two nodes are accessible by means of their principal IP addresses, which are 10.0.0.1 and 10.0.0.2.
2. Each node is configured with an alternate address. This is not validated by the node on which it is configured: the operating system for the node is in most cases unaware of the external address. The router typically makes the alternate address available to the Network Address Translation (_NAT_) facility for the network; after which it is used as the external address for the node. Thus, it can be referenced by external applications.
3. A publicly available DNS server lists the alternate addresses for the nodes.
4. An external application resolves the domain name for each node to its corresponding alternate address.
5. The external application contacts the NAT by means of the alternate addresses. The NAT translates the alternate address to the internal, and communication between the nodes and the external application continues on that basis.

### [](#dual-network)Dual Network

Applications' access to nodes can be _segregated_, by means of a _Dual Network_, in order to optimize security. This is shown by the following illustration:

![externalAddressDiagram02](../_images/clusters-and-availability/externalAddressDiagram02.png) 

The annotations to this diagram are as follows:

1. A cluster can be accessed by its principal address, 10.0.0.100, or its alternate, 10.1.0.100\. Within the cluster are two nodes, each of which can be accessed internally by means of a primary or secondary IP address.
2. The path to the cluster by which application-requests are routed may depend on whether the cluster’s principal or alternate address is used.
3. When in possession of both principal and alternate addresses, applications generally default to use of the principal; but may be able to override the default, and use the alternate. Here indeed, Application 2 uses the alternate.
4. Within the cluster, node-access by external applications is managed according to the mappings for the cluster’s principal and alternate addresses. Here, the principal address is mapped to the nodes’ primary addresses, and the alternate address is mapped to the nodes’ secondary addresses.

### [](#assigning-alternate-addresses)Assigning Alternate Addresses

Couchbase Server allows alternate addresses to be assigned by means of:

* The CLI. See the reference page for [setting-alternate-address](../../cli/cbcli/couchbase-cli-setting-alternate-address.md). Note that the `--list` parameter lists the current alternate address and all current port-number settings.
* The REST API. See the reference page for [Managing Alternate Addresses](../../rest-api/rest-set-up-alternate-address.md). See also the page for [Listing Node Services](../../rest-api/rest-list-node-services.md), whereby current settings can be inspected.