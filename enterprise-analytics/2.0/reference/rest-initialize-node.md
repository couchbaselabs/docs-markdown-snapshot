---
title: Initializing a Node
description: A node can be initialized, by means of the REST API.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/reference/pages/rest-initialize-node.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/2.0/reference/rest-initialize-node.html)

# Initializing a Node

> A node can be initialized, by means of the REST API. 

## [](#http-method-and-uri)HTTP Method and URI

POST /nodes/self/controller/settings

## [](#description)Description

Initializes a node, prior to its being provisioned as a one-node cluster. This means to establish local paths for on-disk storage required by the Data, Index, Analytics, and Eventing Services; and to establish a local path for a JRE, to be used by the Analytics Service. Once established, these paths continue to be used by the node subsequent to its provisioning with services, memory-allocations, administrator username and password, and other details. Indeed, these paths will continue to be used by the node even subsequent to the node’s addition to another cluster.

If one or more paths are not specified (or if initialization with this interface is left entirely unperformed), defaults are provided when provisioning occurs.

Prior to establishment of username and password by the administrator who is configuring the single-node cluster, initialization can be performed repeatedly, with new values established each time. After establishment of username and password, initialization can no longer be performed.

Per platform, the default data-folder locations for all services are:

* _Linux_: `/opt/enterprise-analytics/var/lib/couchbase/data`
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
  -d 'path=%2Fopt%2Fcouchbase%2Fvar%2Flib%2Fcouchbase%2Fdata&' \
  -d 'index_path=%2Fopt%2Fcouchbase%2Fvar%2Flib%2Fcouchbase%2Fidata&' \
  -d 'cbas_path=%2Fopt%2Fcouchbase%2Fvar%2Flib%2Fcouchbase%2Fadata&' \
  -d 'eventing_path=%2Fopt%2Fcouchbase%2Fvar%2Flib%2Fcouchbase%2Fedata&'

## [](#see-also)See Also

The sequence of tasks divided into _initialization_ and _provisioning_ is explained in [Cluster Initialization and Provisioning](rest-cluster-init-and-provisioning.md).

For each of the specific steps required in the provisioning process, see [Configuring Memory](rest-configure-memory.md), [Naming a Node](rest-name-node.md), [Naming a Cluster](rest-name-cluster.md), [Assigning Services](#reference:rest-set-up-services.adoc), and [Establishing Credentials](rest-establish-credentials.md).

information about nodes is provided in [Nodes](#learn:clusters-and-availability/nodes.adoc).

For further information about initialization and provisioning — using the UI, the CLI, and the REST API — see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).