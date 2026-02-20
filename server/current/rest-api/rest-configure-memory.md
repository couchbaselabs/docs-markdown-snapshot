---
title: Configuring Memory
description: Use REST API to configure custom memory allocation per service.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-configure-memory.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:rest-api:rest-configure-memory.adoc[]
---

[View original HTML](/server/current/rest-api/rest-configure-memory.html)

# Configuring Memory

> Use REST API to configure custom memory allocation per service. 

## [](#http-method-and-uri)HTTP Method and URI

POST /pools/default

## [](#description)Description

Allows a custom memory quota to be established for the Multi-Dimensional Scaling (MDS) services Data, Index, Search, Eventing, and Analytics. The Query and Backup Services do not require a memory allocation. If no custom quota was specified during configuration for 1 or more services, those services retain the default allocations. These are the default allocations:

* 256 Mb for kv (Data Service)
* 256 Mb for fts (Search Service)
* 512 Mb for index (Index Service)
* 256 Mb for eventing (Eventing Service)
* 1024 Mb for cbas (Analytics Service)

For more information about the maximum memory allocation permitted for a node, see [Service Memory Quotas](../learn/buckets-memory-and-storage/memory.md#service-memory-quotas).

## [](#curl-syntax)Curl Syntax

curl  -v -X POST http://10.144.220.101:8091/pools/default \
  -d memoryQuota=<integer> \
  -d indexMemoryQuota=<integer> \
  -d eventingMemoryQuota=<integer> \
  -d ftsMemoryQuota=<integer> \
  -d cbasMemoryQuota=<integer> \
  -u <username>:<password>

During the process of provisioning a single-node cluster, `username` and `password` are required after the administrator has established credentials, as explained in [Establishing Credentials](rest-establish-credentials.md).

## [](#responses)Responses

| Value                                                                   | Description                                                            |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 200 OK and JSON array containing the expired backups and their details. | Successful call.                                                       |
| 400                                                                     | Invalid parameter.                                                     |
| 401 Unauthorized                                                        | Authorization failure due to incorrect username or password.           |
| 403 Forbidden, plus a JSON message explaining the minimum permissions.  | The provided username has insufficient privileges to call this method. |
| 404 Object Not Found                                                    | Error in the URI path.                                                 |
| 500 Internal Server Error                                               | Error in Couchbase Server.                                             |

## [](#example)Example

The following example establishes the minimum allowed value for each service:

curl  -v -X POST http://10.144.220.101:8091/pools/default \
-u Administrator:password
-d 'memoryQuota=256' \
-d 'indexMemoryQuota=256' \
-d 'eventingMemoryQuota=256' \
-d 'ftsMemoryQuota=256' \
-d 'cbasMemoryQuota=1024'

## [](#see-also)See Also

* For more information about the maximum memory allocation permitted for a node, see [Service Memory Quotas](../learn/buckets-memory-and-storage/memory.md#service-memory-quotas).
* For more information about the other aspects of provisioning a single-node cluster, see [Initializing a Node](rest-initialize-node.md), [Naming a Node](rest-name-node.md), [Naming a Cluster](rest-name-cluster.md), [Assigning Services to a New Single Node](rest-set-up-services.md), and [Establishing Credentials](rest-establish-credentials.md).
* For more information on initialization and provisioning — using the UI, the CLI, and the REST API — see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* For more information about retrieving memory information for services using the REST API, see [Getting Memory Information](rest-get-memory-information.md).