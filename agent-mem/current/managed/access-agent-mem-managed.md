---
title: Control Access to Managed Agent Memory
description: Capella roles control who can deploy and manage Managed Agent
  Memory servers, and API keys control what your agent can do on a server.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/managed/pages/access-agent-mem-managed.adoc
  xref: xref:agent-mem:managed:access-agent-mem-managed.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/managed/access-agent-mem-managed.html)

# Control Access to Managed Agent Memory

> Capella roles control who can deploy and manage Managed Agent Memory servers, and API keys control what your agent can do on a server. 

Managed Agent Memory has 3 kinds of access:

Server management

Deploying and deleting servers, creating and deleting API keys, and managing allowed IP addresses. Your Capella organization and project roles control these actions, in the Capella UI or through the Management API.

Memory access through the API

Storing, searching, and deleting memory through the Agent Memory Python SDK or REST API. An Agent Memory API key's access level controls these actions.

Direct cluster data access

Reading or changing the documents where Agent Memory stores memory in your bucket. Project roles with data access and cluster access credentials control this access, the same as for any other data on the cluster.

## [](#capella-roles-for-server-management)Capella Roles for Server Management

The following table lists the access each Capella role has to Agent Memory servers, their API keys, and their allowed IP addresses. Full means the role can create, view, and delete.

| Role                                                                                                                                                                                                      | Servers | API keys | Allowed IP addresses |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- | -------------------- |
| [Organization Owner](../../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner)                                                                                        | Full    | Full     | Full                 |
| [Project Owner](../../../cloud/projects/project-roles.md#project-owner-role)                                                                                                                              | Full    | Full     | Full                 |
| [Project Cluster Manager](../../../cloud/projects/project-roles.md#project-cluster-manager-role)                                                                                                          | View    | View     | Full                 |
| [Project Cluster Viewer](../../../cloud/projects/project-roles.md#project-cluster-viewer-role)                                                                                                            | View    | View     | View                 |
| [Project Data Reader](../../../cloud/projects/project-roles.md#project-cluster-data-reader) and [Project Data Reader/Writer](../../../cloud/projects/project-roles.md#project-cluster-data-reader-writer) | View    | None     | None                 |

## [](#api-key-access-levels-for-memory-access)API Key Access Levels for Memory Access

Each Agent Memory API key works with 1 server and has a Read, Write, or Admin access level. For what each access level can do, see [Access Levels](../api-guide/managed/api-intro.md#access-level).

Each access level corresponds to an Agent Memory role: Read is `ams_ro`, Write is `ams_rw`, and Admin is `ams_admin`. If a request fails with HTTP `403`, the error message names the role the operation needs, for example `Insufficient permissions. Required role: ams_rw or higher`.

Choose the lowest access level your agent needs:

* An agent runtime that stores and searches memory needs Write.
* A dashboard or analytics integration that only reads memory needs Read.
* An operator who manages [custom prompts](../develop/customize-prompts-agent-mem.md) needs Admin.

## [](#direct-access-to-stored-memory)Direct Access to Stored Memory

Agent Memory stores its data in collections in your bucket. Any role or cluster access credential that can read the `agentmemory` scope in your bucket, such as [Project Data Reader](../../../cloud/projects/project-roles.md#project-cluster-data-reader), can read your stored memory directly. [Project Data Reader/Writer](../../../cloud/projects/project-roles.md#project-cluster-data-reader-writer) can also change or delete it.

## [](#allowed-ip-addresses)Allowed IP Addresses

Each Agent Memory server accepts requests only from IP addresses on its allowed IP address list. For more information, see [Allowed IP Addresses](../api-guide/managed/api-start.md#agent-memory-allowed-ips).

## [](#api-key-revocation)API Key Revocation

When you delete an API key, every node in the server rejects it within about 30 seconds.

If a node cannot confirm that a key still exists, it keeps accepting a key it has already validated for up to 5 minutes. After that, it rejects requests with HTTP `503` and the error code `AUTH_UNAVAILABLE` until it can confirm the key again. Retry these requests.

## [](#see-also)See Also

* [Deploy Managed Agent Memory](deploy-agent-mem-managed.md)
* [Agent Memory APIs for Managed Deployments](../api-guide/managed/api-intro.md)
* [Project Roles](../../../cloud/projects/project-roles.md)
* [Organization Roles](../../../cloud/organizations/organization-user-roles.md)