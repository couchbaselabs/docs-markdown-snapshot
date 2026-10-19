---
title: Connect Data to Agents with Managed MCP Server
description: Use the Couchbase AI Data Plane to deploy a remote Model Context
  Protocol (MCP) server that you can use with your Capella operational clusters.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase MCP Server
    version: managed
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/cloud/modules/ROOT/pages/about-managed-mcp.adoc
  xref: xref:managed@mcp-server::about-managed-mcp.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/managed/about-managed-mcp.html)

# Connect Data to Agents with Managed MCP Server

> Use the Couchbase AI Data Plane to deploy a remote Model Context Protocol (MCP) server that you can use with your Capella operational clusters. 

Using the AI Data Plane Managed MCP Server removes the infrastructure and operational overhead requirements of hosting your own [Couchbase MCP Server](#1.0@mcp-server:get-started:overview.adoc), while still allowing you to:

* Access data stored in a Capella operational cluster.
* Query your operational cluster using natural language.
* Analyze and get recommendations for query performance using Couchbase Index Advisor.

> [!NOTE]
> A Managed MCP Server cannot connect to a Couchbase Server cluster. You must use your Managed MCP Server with a Capella operational cluster.

The AI Data Plane Managed MCP Server works with any MCP-compatible client and any model that supports function calling.

## [](#access-control-configuration)Access Control Configuration

Create an API key to set the buckets, scopes, and collections that your agent can access on your Capella operational cluster. Your API key also controls the specific [tools](learn/tools.md) that your agent can use to interact with the data in your selected keyspace or keyspaces. For more information about configuring an API key, see [Generate a Managed MCP Server API Key](deploy-connect-mcp.md#generate-api-key).

> [!NOTE]
> If you want to change the tools an agent can use through your Managed MCP Server, you must generate a new API key with a new list of tools.

A Managed MCP Server has its own separate list of allowed IP addresses. Add an IP address to your MCP Server's list of allowed IP addresses to control agent and MCP client access. For more information, see [Add an Allowed IP Address to Your Managed MCP Server](deploy-connect-mcp.md#add-allowed-ip).

By default, an AI Data Plane Managed MCP Server runs in read-only mode. If you want your agents to modify data on your operational cluster, you must change this setting when you deploy your Managed MCP Server.

## [](#cluster-reqs)Supported Cluster Requirements

A Managed MCP Server can be linked to only 1 operational cluster. This operational cluster must meet the following requirements:

|                               | Requirement                                             |
| ----------------------------- | ------------------------------------------------------- |
| Couchbase Server Version      | 8.0 or later                                            |
| Cloud Service Provider        | AWS                                                     |
| Cloud Service Provider Region | US East (N. Virginia) Europe (London)                   |
| Cluster Support Plan          | [Enterprise](../../cloud/billing/billing.md#enterprise) |

## [](#see-also)See Also

* [Deploy and Connect to Your Managed MCP Server](deploy-connect-mcp.md)
* [Managed MCP Server Tools Reference](learn/tools.md)