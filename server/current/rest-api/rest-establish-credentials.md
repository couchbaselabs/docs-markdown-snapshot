---
title: Establishing Credentials
description: By means of the REST API, credentials can be established for the
  administrator who is provisioning a new, single-node cluster.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-establish-credentials.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:rest-api:rest-establish-credentials.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/rest-api/rest-establish-credentials.html)

# Establishing Credentials

> By means of the REST API, credentials can be established for the administrator who is provisioning a new, single-node cluster. 

## [](#http-method-and-uri)HTTP Method and URI

POST /settings/web

## [](#description)Description

Establishes username and password for the administrator who is setting up a new, single-node cluster. The administrator will have Full Admin permissions, but will not appear as a listed administrator in the Security window of Couchbase Web Console. The administrator will be able to add other administrators, with specific roles, including administrators with Full Admin permissions: all will appear in the Security window of Couchbase Web Console.

During the process of provisioning a new single-node cluster, prior to the establishing of a username and password, no authentication is required to execute the APIs that support provisioning. This permits [Naming a Node](rest-name-node.md), [Naming a Cluster](rest-name-cluster.md), [Configuring Memory](rest-configure-memory.md), and [Assigning Services to a New Single Node](rest-set-up-services.md) to be performed without any username or password being specified. However, once a username and password have been established, all further calls, including those used in provisioning, require authentication.

Following the establishment of username and password, the single-node cluster can no longer be initialized; nor can services be assigned to the node. If no services have been assigned prior to the username and password being assigned, the default list of services is assigned to the node, using the default memory allocations. See [Memory](../learn/buckets-memory-and-storage/memory.md).

Following the establishment of username and password, the node-name can continue to be assigned and reassigned, provided that the node remains a single-node cluster. Memory allocations and cluster name can also continue to be modified, including after the cluster has become a multi-node cluster.

## [](#curl-syntax)Curl Syntax

curl -X POST http://<ip-address-or-domain-name>:8091/settings/web
  -d password=<password>
  -d username=<username>
  -d port=SAME

The `password` and `username` arguments are respectively the password and username that must be used for authentication following the call; giving the administrator the Full Admin role.

The REST API port must be specified, with `SAME` as the default value.

## [](#responses)Responses

Success returns `200 OK`, and a message confirming the IP address of the node, such as: `{"newBaseUri":"http://10.144.220.101:8091/"}`. Failure to specify a username, password, or port-number returns `400 Bad Request`, and an error message such as: `{"errors":{"port":"The value must be supplied"}}`. Failure correctly to specify the URI returns `404 Object Not Found`.

## [](#example)Example

The following example specifies the username as `Administrator`, the password as `password`, and the port as the default value of `SAME`.

curl -X POST http://<ip-address-or-domain-name>:8091/settings/web \
-d 'password=password&username=Administrator&port=SAME'

## [](#see-also)See Also

Couchbase Server roles are described in [Roles](../learn/security/roles.md).

For each of the specific steps required in the provisioning process, see [Configuring Memory](rest-configure-memory.md), [Naming a Node](rest-name-node.md), [Naming a Cluster](rest-name-cluster.md), [Assigning Services to a New Single Node](rest-set-up-services.md), and [Establishing Credentials](rest-establish-credentials.md).

For further information on initialization and provisioning — using the UI, the CLI, and the REST API — see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).