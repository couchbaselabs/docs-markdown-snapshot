---
title: Prerequisites
description: Requirements — Python, a Couchbase cluster, uv or Docker, and an
  MCP client — you need in place before using the Couchbase MCP Server.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase MCP Server
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/get-started-oi/pages/prerequisites-oi.adoc
  xref: xref:1.1@mcp-server:get-started-oi:prerequisites-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/1.1/get-started-oi/prerequisites-oi.html)

# Prerequisites

> Requirements — Python, a Couchbase cluster, uv or Docker, and an MCP client — you need in place before using the Couchbase MCP Server. 

Before using the Couchbase MCP Server, make sure you have the following:

## [](#required)Required

* **Python 3.11—3.14**: The Couchbase MCP Server aims to support [Python versions](https://devguide.python.org/versions/#supported-versions) in security or bug-fix (maintenance) status. Python versions that have reached their [End-of-Life date](https://endoflife.date/python) are not supported.
* **A running Operational Insights cluster**: A self-hosted Couchbase Operational Insights instance.  
> [!IMPORTANT]  
> The Operational Insights MCP server supports only self-managed deployments. Capella-hosted Operational Insights is not supported.  
> [!NOTE]  
> Compatibility  
>  
> The MCP Server is compatible with **Operational Insights 2.0+**. The following services are **not supported**: Sync Gateway, Couchbase Lite, and Capella AI Services.
* **[uv](https://docs.astral.sh/uv/) or [Docker](https://www.docker.com/)**: uv is the recommended way to run the server. Docker is an alternative if you prefer containerized deployments.
* **An MCP client**: Such as [Claude Desktop](https://claude.ai/download), [Cursor](https://cursor.sh/), [VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers), [Windsurf](https://docs.windsurf.com/windsurf/cascade/mcp), or any [MCP-compatible client](https://modelcontextprotocol.io/clients).

## [](#setup-operational-insights)Setup Operational Insights

If you do not already have an Operational Insights cluster, see the [quick install guide](https://docs.couchbase.com/enterprise-analytics/current/intro/do-a-quick-install.html) to install one on your own infrastructure.

## [](#getting-sample-data-optional)Getting Sample Data (Optional)

To try the server with sample data, import the `travel-sample` collections. See [Import the travel-sample collections](https://docs.couchbase.com/enterprise-analytics/current/intro/connecting-to-data-sources.html#import-the-travel-sample-collections).

## [](#setup-authentication)Setup Authentication

Configure your Operational Insights cluster with one of the following authentication methods:

* **Basic Authentication**: A username and password with access to the required databases.
* **mTLS Authentication**: A client certificate and key for mutual TLS authentication.

For Basic Authentication setup, see [Manage Users and Roles](https://docs.couchbase.com/server/current/manage/manage-security/manage-users-and-roles.html) (self-managed).

For mTLS setup, see [Configure Client Certificate Authentication](https://docs.couchbase.com/server/current/manage/manage-security/configure-client-certificates.html).

Verify the following:

* The cluster is accessible from the machine running the MCP server.
* The database user has proper permissions to access at least one database.