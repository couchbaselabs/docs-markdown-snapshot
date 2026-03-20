---
title: Server Groups API
description: The <em>Server Groups REST API</em> manages <em>Server Group Awareness</em>.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/reference/pages/rest-rza.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:reference:rest-rza.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/reference/rest-rza.html)

# Server Groups API

> The _Server Groups REST API_ manages _Server Group Awareness_. This enables logical server-groupings to be defined across the cluster: each group may be physically located on a specific rack or availability zone. 

## [](#description)APIs in this Section

_Server Group Awareness_, which is only available in Enterprise Analytics Enterprise Edition, provides enhanced availability. Specifically, it protects a cluster from large-scale infrastructure failure, through the definition of _groups_. Each group is created by an appropriately authorized administrator, and specified to contain a subset of the nodes within a Couchbase Cluster. Following group-definition and rebalance, the active vBuckets for any defined bucket are located on one group, while the corresponding replicas are located on another group. This allows _Group Failover_ to be enabled, so that if an entire group goes offline, its replica vBuckets, which remain available on another group, can be automatically promoted to active status.

For a complete conceptual overview, see [Server Group Awareness](#learn:clusters-and-availability/groups.adoc). For information about Couchbase _Role-Based Access Control_, see [Roles](#learn:security/roles.adoc).

For a list of all methods and URIs covered in this section, see the table provided below.

| HTTP Method | URI                                         | Documented at                                                   |
| ----------- | ------------------------------------------- | --------------------------------------------------------------- |
| GET         | /pools/default/serverGroups                 | [Getting Group Information](rest-servergroup-get.md)            |
| POST        | /pools/default/serverGroups                 | [Creating Groups](rest-servergroup-post-create.md)              |
| POST        | /pools/default/serverGroups/<:uuid>/addNode | [Adding Nodes to Groups](rest-servergroup-post-add.md)          |
| PUT         | /pools/default/serverGroups/<:uuid>         | [Renaming Groups](rest-servergroup-put.md)                      |
| PUT         | /pools/default/serverGroups?rev=<:number>   | [Updating Group Membership](rest-servergroup-put-membership.md) |
| DELETE      | /pools/default/serverGroups/<:uuid>         | [Deleting Groups](rest-servergroup-delete.md)                   |