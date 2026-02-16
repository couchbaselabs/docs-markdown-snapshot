[View original HTML](/enterprise-analytics/2.0/reference/rest-name-node.html)

> A node can be named, by means of the REST API. 

## [](#http-method-and-uri)HTTP Method and URI

POST /node/controller/rename

## [](#description)Description

Names and, if required, renames an individual node. This API is therefore used as part of the node-provisioning process, and can also be used or reused subsequent to all other aspects of node-provisioning, including specification of username and password for the Full Administrator. However, the API can only be used while the node constitutes a _single-node cluster_: once the node has become part of a multi-node cluster, the API can no longer be used.

## [](#curl-syntax)Curl Syntax

curl -X POST -u <username>:<password> \
  http://<ip-address-or-domain-name>:8091/node/controller/rename \
  -d hostname=<name>

The `username` and `password` need only be specified if credentials have been configured for the administrator, as described in [Establishing Credentials](rest-establish-credentials.md).

The `name` argument must be one of the following:

* The IP address of the underlying host (either IPv4 or IPv6).
* A fully qualified hostname that corresponds, in the appropriate network maps, to the IP address of the underlying host.
* The loopback address, `127.0.0.1`.

## [](#responses)Responses

Success returns `200 OK`. Failure to specify the `name` argument correctly returns `400 Bad Request`, and a message such as the following: `["Could not listen on address \"10.144.220.107\": eaddrnotavail"]`. If a username and password have already been assigned, failure to authenticate returns `401 Unauthorized`. An incorrectly expressed URI or flag returns `404 Object Not Found`.

## [](#example)Example

The following example specifies the IP of the underlying host as the name of the node.

curl -X POST -u Administrator:password \
http://10.144.220.101:8091/node/controller/rename \
-d hostname='10.144.220.101'

## [](#see-also)See Also

The sequence of tasks divided into _initialization_ and _provisioning_ is explained in [Cluster Initialization and Provisioning](rest-cluster-init-and-provisioning.md).

For each of the other specific steps required in the provisioning process, see [Configuring Memory](rest-configure-memory.md), [Naming a Cluster](rest-name-cluster.md), [Assigning Services](#reference:rest-set-up-services.adoc), and [Establishing Credentials](rest-establish-credentials.md).

For general information about naming, see [Naming Clusters and Nodes](#learn:clusters-and-availability/nodes.adoc#naming-clusters-and-nodes).

For further information about initialization and provisioning — using the UI, the CLI, and the REST API — see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).