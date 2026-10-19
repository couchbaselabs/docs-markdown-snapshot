---
title: Server Group API
description: The <em>Server Groups REST API</em> manages <em>Server Group Awareness</em>.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-rza.adoc
  xref: xref:enterprise-analytics:reference:rest-rza.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-rza.html)

# Server Group API

> The _Server Groups REST API_ manages _Server Group Awareness_. This enables logical server-groupings to be defined across the cluster: each group may be physically located on a specific rack or availability zone. 

## [](#description)APIs in this Section

_Server Group Awareness_ provides enhanced availability. Specifically, it protects a cluster from large-scale infrastructure failure, through the definition of _groups_. Each group is created by an appropriately authorized administrator, and specified to contain a subset of the nodes within an Operational Insights cluster.

For a complete overview, see [Manage Server Groups](../manage/manage-groups/manage-groups.md). For information about _Role-Based Access Control_, see [Role-Based Access Control](../manage/manage-security/rbac-overview.md).

For a list of all methods and URIs covered in this section, see the table provided below.

| HTTP Method | URI                                         | Documented at                                                   |
| ----------- | ------------------------------------------- | --------------------------------------------------------------- |
| GET         | /pools/default/serverGroups                 | [Getting Group Information](rest-servergroup-get.md)            |
| POST        | /pools/default/serverGroups                 | [Creating Groups](rest-servergroup-post-create.md)              |
| POST        | /pools/default/serverGroups/<:uuid>/addNode | [Adding Nodes to Groups](rest-servergroup-post-add.md)          |
| PUT         | /pools/default/serverGroups/<:uuid>         | [Renaming Groups](rest-servergroup-put.md)                      |
| PUT         | /pools/default/serverGroups?rev=<:number>   | [Updating Group Membership](rest-servergroup-put-membership.md) |
| DELETE      | /pools/default/serverGroups/<:uuid>         | [Deleting Groups](rest-servergroup-delete.md)                   |