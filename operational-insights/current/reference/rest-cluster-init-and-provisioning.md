---
title: Cluster Initialization and Provisioning
description: The Couchbase REST API can be used to initialize an individual
  node; and to provision it, so that it becomes a single-node cluster, to which
  further nodes can then be added.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-cluster-init-and-provisioning.adoc
  xref: xref:enterprise-analytics:reference:rest-cluster-init-and-provisioning.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-cluster-init-and-provisioning.html)

# Cluster Initialization and Provisioning

> The Couchbase REST API can be used to initialize an individual node; and to provision it, so that it becomes a single-node cluster, to which further nodes can then be added. 

## [](#understanding-initialization-and-provisioning)Understanding Initialization and Provisioning

Once a newly installed instance of Operational Insights has been started for the first time, the Couchbase REST API can be used to:

* _Initialize_. This means optionally to specify, for the current node, the following:

  * Custom disk paths for the Data and Analytics services.
  * A custom location for the Java Runtime Environment to be used by the Analytics Service.
  * A node-name.
* _Provision_. This means to establish, for the current node:

  * The default disk paths for the Data and Analytics Services, in cases where custom disk paths have not been previously established through initialization.
  * The default location for the Java Runtime Environment to be used by the Analytics Service; in cases where no custom location has been previously established through initialization.
  * A node-name, in cases where no such name has been previously established through initialization.
  * A name for the entire cluster.
  * The memory allocations for the Data and Analytics Services. Every node runs exactly these two services, so there are no services to choose.
  * A username and password for the administrator creating the cluster — the administrator will have Full Admin credentials.  
  Once the username and password are established, the node is considered a fully provisioned single-node cluster, and the cluster's instance of Couchbase Web Console can be accessed by means of user login.  
  Following the establishment of username and password, the single-node cluster can no longer be initialized. If no memory allocations have been made prior to the username and password being assigned, the default memory allocations are used. See [Configuring Memory](rest-configure-memory.md).  
  Following the establishment of username and password, the node-name can continue to be assigned and reassigned, provided that the node remains a single-node cluster. Memory allocations and cluster name can also continue to be modified, including after the cluster has become a multi-node cluster.  
  If username and password are established _before_ the other provisioning APIs have been used, any such calls made subsequently must be authenticated: however, prior to username and password being established, the other provisioning APIs can be used without authentication. For information about roles, see [Role Based Access Control (RBAC)](../manage/manage-security/rbac-overview.md).

Note the following:

* Operational Insights requires object storage. Configure the object storage with `POST /settings/operationalInsights` before calling `POST /clusterInit`; otherwise, `POST /clusterInit` fails validation. For the settings, see [Service Settings API](rest-cluster-management.md#service-settings-api); for the supported object stores, see [Configure Object Storage](../manage/manage-nodes/object-storage.md).
* The custom access-paths established for the node during _initializing_ will be retained even if the node is subsequently added to a different cluster.
* Once the one-node cluster has been provisioned, and is thus a single-node cluster, it can be made part of a multi-node cluster: _either_ by adding other individual nodes to it; or by adding it to another, already existing cluster.
* When a provisioned node is added to another cluster, the node loses all aspects of its provisioning; and must be reprovisioned, as part of the node-addition process.

For detailed information about initialization, provisioning and all other principal aspects of node-management, see [Nodes and Clusters](../manage/manage-nodes/node-management-overview.md), [Initialize a Node](../manage/manage-nodes/initialize-node.md) and [Create a Cluster](../manage/manage-nodes/create-cluster.md). For information about specifying a Java Runtime Environment, see the description of [Additional Requirements](../install/additional-req.md) provided for the install process.

## [](#options-for-initializing-and-provisioning)Options for Initializing and Provisioning

Each of the principal tasks required to initialize and provision a single-node cluster is granted its own HTTP method and URI. These are listed in the table immediately below. Also listed is the `POST` method with the `/clusterInit` URI: this API effectively combines all of the others, in order to provide the option of making a single call, whereby the cluster is instantly initialized and provisioned.

## [](#apis-in-this-section)APIs in this Section

The REST APIs described in this section are listed below.

| HTTP Method | URI                             | Documented at                                             |
| ----------- | ------------------------------- | --------------------------------------------------------- |
| POST        | /clusterInit                    | [Initialize a Cluster](rest-initialize-cluster.md)        |
| POST        | /nodes/self/controller/settings | [Initializing a Node](rest-initialize-node.md)            |
| POST        | /settings/web                   | [Establishing Credentials](rest-establish-credentials.md) |
| POST        | /node/controller/rename         | [Naming a Node](rest-name-node.md)                        |
| POST        | /pools/default                  | [Configuring Memory](rest-configure-memory.md)            |
| POST        | /pools/default                  | [Naming a Cluster](rest-name-cluster.md)                  |