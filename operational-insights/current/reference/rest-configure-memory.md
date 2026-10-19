---
title: Configuring Memory
description: Use REST API to configure custom memory allocation per service.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-configure-memory.adoc
  xref: xref:enterprise-analytics:reference:rest-configure-memory.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-configure-memory.html)

# Configuring Memory

> Use REST API to configure custom memory allocation per service. 

## [](#http-method-and-uri)HTTP Method and URI

POST /pools/default

## [](#description)Description

Allows a custom memory quota to be established for the Data and Analytics Services. If no custom quota was specified during configuration for 1 or more services, those services retain the default allocations.

* `memoryQuota`: the quota for the Data Service (`kv`), in MiB. On Operational Insights this quota is fixed at 100 MiB: 100 is the only value accepted, and any other value is rejected.
* `cbasMemoryQuota`: the quota for the Analytics Service (`cbas`), in MiB. This is the quota that determines the memory available to Operational Insights. The minimum allowed value is 1024 MiB.

## [](#curl-syntax)Curl Syntax

curl  -v -X POST http://10.144.220.101:8091/pools/default \
  -d memoryQuota=<integer> \
  -d cbasMemoryQuota=<integer> \
  -u <username>:<password>

During the process of provisioning a single-node cluster, `username` and `password` are required after the administrator has established credentials, as explained in [Establishing Credentials](rest-establish-credentials.md).

## [](#responses)Responses

| Value                                                                  | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 200 OK                                                                 | Successful call.                                                       |
| 400                                                                    | Invalid parameter.                                                     |
| 401 Unauthorized                                                       | Authorization failure due to incorrect username or password.           |
| 403 Forbidden, plus a JSON message explaining the minimum permissions. | The provided username has insufficient privileges to call this method. |
| 404 Object Not Found                                                   | Error in the URI path.                                                 |
| 500 Internal Server Error                                              | Error in Operational Insights.                                         |

## [](#example)Example

The following example establishes the minimum allowed value for each service:

curl  -v -X POST http://10.144.220.101:8091/pools/default \
-u Administrator:password \
-d 'memoryQuota=100' \
-d 'cbasMemoryQuota=1024'

## [](#see-also)See Also

* For more information about the other aspects of provisioning a single-node cluster, see [Initializing a Node](rest-initialize-node.md), [Naming a Node](rest-name-node.md), [Naming a Cluster](rest-name-cluster.md), and [Establishing Credentials](rest-establish-credentials.md).
* For more information about initialization and provisioning — using the UI, the CLI, and the REST API — see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).
* For more information about retrieving memory information for services using the REST API, see [Getting Memory Information](../../../server/current/rest-api/rest-get-memory-information.md).