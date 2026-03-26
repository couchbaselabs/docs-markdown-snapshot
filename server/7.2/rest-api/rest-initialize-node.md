---
title: Initializing a Node
description: A node can be initialized, by means of the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-initialize-node.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:rest-api:rest-initialize-node.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/rest-api/rest-initialize-node.html)

# Initializing a Node

> A node can be initialized, by means of the REST API. 

## [](#http-method-and-uri)HTTP Method and URI

POST /nodes/self/controller/settings

## [](#description)Description

Initializes a node, prior to its being provisioned as a one-node cluster. This means to establish local paths for on-disk storage required by the Data, Index, Analytics, and Eventing Services; and to establish a local path for a JRE, to be used by the Analytics Service. Once established, these paths continue to be used by the node subsequent to its provisioning with services, memory-allocations, administrator username and password, and other details. Indeed, these paths will continue to be used by the node even subsequent to the node's addition to another cluster.

If one or more paths are not specified (or if initialization with this interface is left entirely unperformed), defaults are provided when provisioning occurs.

Prior to establishment of username and password by the administrator who is configuring the single-node cluster, initialization can be performed repeatedly, with new values established each time. After establishment of username and password, initialization can no longer be performed.

Per platform, the default data-folder locations for all services are:

* _Linux_: `/opt/couchbase/var/lib/couchbase/data`
* _Windows_: `C:\Program Files\Couchbase\Server\var\lib\couchbase/data`
* _MacOS_: `/Library/Application Support/Couchbase/var/lib/couchbase/data`

## [](#curl-syntax)Curl Syntax

curl -X POST http://<node-ip-address-or-domain-name>:8091/nodes/self/controller/settings
  -u <username>:<password>
  -d path=<data-path>
  -d index_path=<index-path>
  -d cbas_path=<analytics-path>
  -d eventing_path=<eventing-path>
  -d java_home=<jre-path>

Specified directory paths must be writable by user `couchbase`.

## [](#responses)Responses

Success returns `200 OK`. If a directory is not writable by user `couchbase`, `400 Bad Request` is returned, with a message such as: `["Could not set analytics storage. All directories must be writable by 'couchbase' user."].`An incorrectly specified URL or data parameter returns `404 Object Not Found`.

An attempt to re-initialize after username and password have been established returns `400 Bad Request`, with a message such as: `["Changing paths of nodes that are part of provisioned cluster is not supported"]`.

## [](#example)Example

The following example establishes the paths for the Data, Index, Analytics, and Eventing Services.

curl -X POST \
  http://10.142.181.103:8091/nodes/self/controller/settings \
  -d 'path=/opt/couchbase/var/lib/couchbase/data&' \
  -d 'index_path=/opt/couchbase/var/lib/couchbase/idata&' \
  -d 'cbas_path=/opt/couchbase/var/lib/couchbase/adata&' \
  -d 'eventing_path=/opt/couchbase/var/lib/couchbase/edata&'

## [](#see-also)See Also

The sequence of tasks divided into _initialization_ and _provisioning_ is explained in [Cluster Initialization and Provisioning](rest-cluster-init-and-provisioning.md).

For each of the specific steps required in the provisioning process, see [Configuring Memory](rest-configure-memory.md), [Naming a Node](rest-name-node.md), [Naming a Cluster](rest-name-cluster.md), [Assigning Services](rest-set-up-services.md), and [Establishing Credentials](rest-establish-credentials.md).

Information on nodes is provided in [Nodes](../learn/clusters-and-availability/nodes.md).

For further information on initialization and provisioning — using the UI, the CLI, and the REST API — see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).