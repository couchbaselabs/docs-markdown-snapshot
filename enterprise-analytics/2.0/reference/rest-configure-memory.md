---
title: Configuring Memory
description: By means of the REST API, custom memory-allocation can be performed
  per service.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/reference/pages/rest-configure-memory.adoc
  xref: xref:2.0@enterprise-analytics:reference:rest-configure-memory.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/reference/rest-configure-memory.html)

# Configuring Memory

> By means of the REST API, custom memory-allocation can be performed per service. 

## [](#http-method-and-uri)HTTP Method and URI

POST /pools/default

## [](#description)Description

Allows a custom memory quota to be established for the Data, Index, Search, Eventing, and Analytics Services. (The Query and Backup Services do not require a memory allocation.) If no custom quota is specified for one or more services, those services retain the default allocations: these are, for the Data Service 256 Mb; for the Search Service 256 Mb; for the Index Service 512 Mb; for the Eventing Service 256 Mb; and for the Analytics Service 1024 Mb. Note that in each case except the Analytics Service, the minimum allowed allocation is 256 Mb: for the Analytics Service, the minimum allowed allocation is 1024 Mb.

For information about the maximum memory allocation permitted for a node, see [Service Memory Quotas](#learn:buckets-memory-and-storage/memory.adoc#service-memory-quotas).

## [](#curl-syntax)Curl Syntax

curl  -v -X POST http://10.144.220.101:8091/pools/default \
  -d memoryQuota=<integer> \
  -d indexMemoryQuota=<integer> \
  -d eventingMemoryQuota=<integer> \
  -d ftsMemoryQuota=<integer> \
  -d cbasMemoryQuota=<integer> \
  -u <username>:<password>

Note that during the process of provisioning a single-node cluster, `username` and `password` are required after the administrator has established credentials, as described in [Establishing Credentials](rest-establish-credentials.md).

## [](#responses)Responses

Success returns `200 OK`. Failure to specify the URI correctly returns `404 Object Not Found`. Failure to specify a flag correctly returns `400 Bad Request`, and an error message such as: `{"errors":{"cbasMemoryQuo3ta":"Unsupported key"}}`.

If, as part of the provisioning process, a username and password have already been assigned to the cluster, failure to authenticate returns `401 Unauthorized`.

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

For information about the maximum memory allocation permitted for a node, see [Service Memory Quotas](#learn:buckets-memory-and-storage/memory.adoc#service-memory-quotas).

For the other aspects of the provisioning of a single-node cluster, see [Initializing a Node](rest-initialize-node.md), [Naming a Node](rest-name-node.md), [Naming a Cluster](rest-name-cluster.md), [Assigning Services](#reference:rest-set-up-services.adoc), and [Establishing Credentials](rest-establish-credentials.md).

For further information about initialization and provisioning — using the UI, the CLI, and the REST API — see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).