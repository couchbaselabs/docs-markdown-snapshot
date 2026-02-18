---
title: Naming a Cluster
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-name-cluster.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/rest-api/rest-name-cluster.html)

# Naming a Cluster

> A cluster can be named, by means of the REST API. 

## [](#http-method-and-uri)HTTP Method and URI

POST /pools/default

## [](#description)Description

Establishes a name for the cluster. Either the Full Admin or the Cluster Admin role is required.

Once defined, the cluster name provides a convenient, verbal reference, which will never be used in programmatic or networked access. The name can be of any length, can make use of any symbols (for example: %, $, !, #), and can include spaces. The name can be changed at any time during the life of the cluster, irrespective of the cluster’s configuration.

## [](#curl-syntax)Curl Syntax

curl -X POST http://<ip-address-or-domain-name>:8091/pools/default \
  -d clusterName=<cluster-name>
  -u <username>:<password>

The `cluster-name` argument is a string that is to be the name of the cluster.

Note that during the process of provisioning a single-node cluster, `username` and `password` are required after the administrator has established credentials, as described in [Establishing Credentials](rest-establish-credentials.md).

## [](#responses)Responses

Success returns `200 OK`. If a username and password have already been assigned, failure to authenticate returns `401 Unauthorized`. If the URI is incorrectly expressee, `404 Object Not Found` is returned. If the flag is incorrectly expressed, `400 Bad Request` is returned, with an error message such as: `{"errors":{"cl3usterName":"Unsupported key"}}`.

## [](#example)Example

The following example establishes a name for the cluster.

curl -X POST http://10.144.220.101:8091/pools/default \
-d clusterName=MyNewCluster -u Administrator:password

## [](#see-also)See Also

The sequence of tasks divided into _initialization_ and _provisioning_ is explained in [Cluster Initialization and Provisioning](rest-cluster-init-and-provisioning.md).

For each of the other specific steps required in the provisioning process, see [Configuring Memory](rest-configure-memory.md), [Naming a Node](rest-name-node.md), [Assigning Services](rest-set-up-services.md), and [Establishing Credentials](rest-establish-credentials.md).

For general information on naming, see [Naming Clusters and Nodes](../learn/clusters-and-availability/nodes.md#naming-clusters-and-nodes).

For further information on initialization and provisioning — using the UI, the CLI, and the REST API — see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).