---
title: Prerequisites
description: Requirements — Python, a Couchbase cluster, uv or Docker, and an
  MCP client — you need in place before using the Couchbase MCP Server.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/get-started/pages/prerequisites.adoc
  xref: xref:mcp-server:get-started:prerequisites.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/get-started/prerequisites.html)

# Prerequisites

> Requirements — Python, a Couchbase cluster, uv or Docker, and an MCP client — you need in place before using the Couchbase MCP Server. 

Before using the Couchbase MCP Server, ensure you have the following:

## [](#required)Required

* **Python 3.10—3.14**: The Couchbase MCP Server aims to support [Python versions](https://devguide.python.org/versions/#supported-versions) in security or bug-fix (maintenance) status. Python versions that have reached their [End-of-Life date](https://endoflife.date/python) are not supported.
* **A running Couchbase cluster**: Either:

  * [Couchbase Capella](https://docs.couchbase.com/cloud/get-started/create-account.html#getting-started) (free tier available) - fully managed cloud version
  * A self-hosted Couchbase Server instance  
  > [!NOTE]  
  > Compatibility  
  >  
  > The MCP Server is compatible with **Couchbase Server 7.6+** (Operational Cluster). The following services are **not supported**: Couchbase Analytics, Sync Gateway, Couchbase Lite, and Capella AI Services.
* **[uv](https://docs.astral.sh/uv/) or [Docker](https://www.docker.com/)**: uv is the recommended way to run the server. Docker is an alternative if you prefer containerized deployments.
* **An MCP client**: Such as [Claude Desktop](https://claude.ai/download), [Cursor](https://cursor.sh/), [VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers), [Windsurf](https://docs.windsurf.com/windsurf/cascade/mcp), or any [MCP-compatible client](https://modelcontextprotocol.io/clients).

## [](#setup-couchbase-server)Setup Couchbase Server

If you do not already have a Couchbase cluster, you can set one up using either option:

* **Couchbase Capella** (recommended) - [Create a free-tier account](https://docs.couchbase.com/cloud/get-started/create-account.html#getting-started) for a fully managed cloud deployment.
* **Self-Managed Couchbase Server**: [Install Couchbase Server](https://docs.couchbase.com/server/current/install/install-intro.html) on your own infrastructure.

## [](#getting-sample-data-optional)Getting Sample Data (Optional)

* **Couchbase Capella**: [Import sample datasets](https://docs.couchbase.com/cloud/clusters/data-service/import-data-documents.html#import-sample-data) like `travel-sample` or import your own data.
* **Self-Managed Couchbase Server**: [Install sample buckets](https://docs.couchbase.com/server/current/manage/manage-settings/install-sample-buckets.html) like `travel-sample` from the Couchbase Server Web Console.

## [](#setup-authentication)Setup Authentication

Configure your Couchbase cluster with one of the following authentication methods:

* **Basic Authentication**: A username and password with access to the required buckets.
* **mTLS Authentication**: A client certificate and key for mutual TLS authentication.

For Basic Authentication setup, see [Manage Database Credentials](https://docs.couchbase.com/cloud/clusters/manage-database-users.html) (Capella) or [Manage Users and Roles](https://docs.couchbase.com/server/current/manage/manage-security/manage-users-and-roles.html) (self-managed).

For mTLS setup, see [Configure Client Certificate Authentication](https://docs.couchbase.com/server/current/manage/manage-security/configure-client-certificates.html).

Ensure that:

* The cluster is accessible from the machine running the MCP server.
* If using Capella, the machine's IP address is [allowed](https://docs.couchbase.com/cloud/clusters/allow-ip-address.html).  
This is only required when the MCP server reaches Capella over the public Internet.  
If you host the MCP server in a VPC or on a network privately connected to Capella, IP allow-listing is not needed.  
Connectivity between the MCP server and Capella follows the same rules as any Couchbase SDK client.
* The database user has proper permissions to access at least one bucket.