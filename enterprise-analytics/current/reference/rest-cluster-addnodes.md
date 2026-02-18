---
title: Adding Nodes to Clusters
description: Nodes are added to clusters with the <code>POST
  /controller/addNode</code> HTTP method and URI.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/reference/pages/rest-cluster-addnodes.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/current/reference/rest-cluster-addnodes.html)

# Adding Nodes to Clusters

> Nodes are added to clusters with the `POST /controller/addNode` HTTP method and URI. 

## [](#http-method-and-uri)HTTP method and URI

POST /controller/addNode

## [](#description)Description

This adds a server node to the cluster. One or more services can be specified to run on the added node. These are `kv` (data) and `cbas` (analytics). If no services are specified, the Data Service is enabled by default.

Enterprise Analytics provides heightened security for adding nodes to clusters. You must provision a node with conformant certificates before you add it to a cluster. The new node is now always added over an encrypted connection. See [Adding and Joining New Nodes](../manage/manage-security/configure-server-certificates.md#adding-new-nodes).

In consequence, a server to be added can be prefixed with the scheme `https://`, and/or can be suffixed with the port `18091`): if no scheme or port is specified, `https://` and `18091` are used as defaults. The scheme `http://` cannot be used; nor can the port `8091`, since in 7.1+, addition takes place only over a secure connection.

To further increase cluster security in Enterprise Analytics, you can restrict node additions by establishing node-naming conventions. Only nodes whose names correspond to at least one of the stipulated conventions can be added. For information, see [Restrict Node-Addition](rest-specify-node-addition-conventions.md).

### [](#node-certificate-validation)Validating Node Certificates

In Couchbase Enterprise Server Version 7.2 or later, the node-name _must_ be correctly identified in the node certificate as a Subject Alternative Name. If such identification is not correctly configured, failure may occur when attempting to add or join the node to a cluster. For information, see [Node-Certificate Validation](#learn:security/certificates.adoc#node-certificate-validation).

## [](#curl-syntax)Curl Syntax

curl -u [admin]:[password]
  http://[localhost]:8091/controller/addNode
  -d hostname=[IPaddress]
  -d user=[username]
  -d password=[password]
  -d services=[kv|cbas]

> [!NOTE]
> The administrative username and password must be specified. If the new node has not yet been provisioned, placeholder names must be provided.

## [](#responses)Responses

Success gives `200 OK`, and returns an object of the form `{"otpNode":"ns_1@ip-address-of-added-node"}`, to confirm that the node has been added. Specifying an unknown service gives `400 Bad Request`, and an object of the form `["Unknown services: [\"unknown-service-name\"]"]`. If the node to be added has already been provisioned, and its administrative credentials are not properly specified, `400 Bad Request` is given, and an object is returned of the form `["Prepare join failed. Authentication failed. Verify username and password."]`

If the IP address of the new node cannot be reached, `400 Bad Request` is given, and an object is returned of the form `["Failed to reach erlang port mapper at node \"ip-address-of-new-node\". Error: ehostunreach"]`. If the IP address of the host cluster is not accurately specified, or otherwise cannot be reached, the request times out, giving `Empty reply from server`. Failure to authenticate with the cluster gives `401 Unauthorized`.

If an attempt is made to specify a node to be added with the scheme `http://` and/or the suffix `8091`, the request fails with `400 Bad Request`, and the error-message `http is prohibited due to security reasons, please use https`.

When failure results from [Certificate Checking](#learn:security/certificates.adoc#certificate-checking), a message of the following form is provided: `Attention: Prepare join failed. Unable to validate certificate on host: 127.0.0.1. Please make sure the certificate on this host contains host name '127.0.0.1' in Subject Alternative Name. Refer to Couchbase docs for more info on how to create node certificates.`

## [](#example)Example

The following example adds a server node, `10.143.190.103`, to the cluster at `10.143.190.101:8091`, establishing the Data Services on the new node. The IP address for the new server and its administrative credentials are provided.

curl -v -X POST -u Administrator:password \
http://10.143.190.101:8091/controller/addNode \
-d 'hostname=https://10.143.190.103' \
-d 'user=Administrator' \
-d 'password=password' \
-d 'services=kv'

If successful, Enterprise Analytics responds as follows, identifying the node that has been added:

{"otpNode":"ns_1@10.143.190.103"}

Subsequent to addition, the node must be rebalanced into the cluster. See [Rebalancing the Cluster](rest-cluster-rebalance.md).

## [](#see-also)See Also

For a conceptual overview of nodes, including options for adding nodes to clusters, see [Nodes](../../../server/current/learn/clusters-and-availability/nodes.md). For information about rebalancing, see [Rebalancing the Cluster](rest-cluster-rebalance.md). For information about adding nodes and rebalancing by means of Couchbase Web Console and the CLI, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md). For information about correctly specifying the node-name on its certificate, see [Node-Certificate Validation](../../../server/current/learn/security/certificates.md#node-certificate-validation).