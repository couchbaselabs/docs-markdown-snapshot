---
title: Deploy and Connect to Your Managed MCP Server
description: Deploy and configure a new Couchbase AI Data Plane Managed MCP
  Server to use data from an operational cluster directly in your agent.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase MCP Server
    version: managed
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/cloud/modules/ROOT/pages/deploy-connect-mcp.adoc
  xref: xref:managed@mcp-server::deploy-connect-mcp.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/managed/deploy-connect-mcp.html)

# Deploy and Connect to Your Managed MCP Server

> Deploy and configure a new Couchbase AI Data Plane Managed MCP Server to use data from an operational cluster directly in your agent. 

For more information about the AI Data Plane Managed MCP Server, see [Connect Data to Agents with Managed MCP Server](about-managed-mcp.md).

## [](#prerequisites)Prerequisites

* You have a Capella account with the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) role, or 1 of the following project roles in the project where you want to deploy your Managed MCP Server:

  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
  * [Cluster Manager](../../cloud/projects/project-roles.md#project-cluster-manager-role)  
  > [!TIP]  
  > If you have the [Cluster Viewer](../../cloud/projects/project-roles.md#project-cluster-viewer-role) role, you can view deployed Managed MCP Servers and API keys.
* You have an MCP-compatible client that supports tool calling, such as:

  * [Claude](https://claude.com/download)
  * [Cursor](https://cursor.com/)
  * [VS Code](https://code.visualstudio.com/)
  * [Devin AI (formerly Windsurf)](https://devin.ai/)
* You have deployed an operational cluster that [meets the requirements for Managed MCP Server](about-managed-mcp.md#cluster-reqs).
* You have logged in to the Couchbase Capella UI.

## [](#procedure)Procedure

To use a Managed MCP Server:

1. [Deploy a new MCP Server](#deploy).
2. [Generate an API key](#generate-api-key).
3. [Add an allowed IP address](#add-allowed-ip).
4. [Add the MCP configuration to your client](#add-config).
5. [Check your connection](#check-connection).

### [](#deploy)Deploy Your Managed MCP Server

To deploy a new Managed MCP Server on the Couchbase AI Data Plane:

1. In the navigation breadcrumbs, click your organization name.
2. Go to **AI Data Plane** **MCP Server**.
3. Click **Deploy MCP Server**.
4. Choose the cluster you want to connect to your Managed MCP Server.  
The cluster you choose determines the project, region, availability zones, and support plan for your Managed MCP Server. The cluster must meet the [requirements for Managed MCP Server](about-managed-mcp.md#cluster-reqs).
5. Click **Continue**.
6. In the **MCP Server Name** field, enter a name for your new Managed MCP Server or accept the default generated name.
7. In **Compute tier**, choose the compute size for your new Managed MCP Server.  
Choose the vCPUs and memory that can handle your expected agent workload for your MCP Server.
8. In the **Nodes** list, select the total number of nodes you want to deploy with your selected **Compute tier**.  
The options available depend on your linked cluster's Availability Zone.  
> [!NOTE]  
> You cannot change the number of nodes or compute resources for a Managed MCP Server. If you need to change your Managed MCP Server configuration, deploy a new server.
9. In **Access**, choose whether agents should have **Read** or **Read & Write** access to the data on your connected operational cluster.  
You cannot change this setting later.
10. Click **Deploy MCP Server**.

### [](#generate-api-key)Generate a Managed MCP Server API Key

To generate a new API key for a Managed MCP Server:

1. In the navigation breadcrumbs, click your organization name.
2. Go to **AI Data Plane** **Access Control** **MCP**.  
> [!TIP]  
> You can also create API keys for a specific Managed MCP Server by doing the following:  
>  
> 1. Go to **AI Data Plane** **MCP Server**.  
> 2. Click the Managed MCP Server where you want to create a new API key.  
> 3. In **Access**, click **Generate API Key**.
3. Click **Generate API Key**.
4. In the **MCP Server** list, select the Managed MCP Server where you want to create your API key.
5. In the **API Key Name** field, enter a name for the API key.
6. Choose when the API key should expire.  
Setting an API key expiration is recommended for production environments.
7. (Optional) In the **Description** field, enter a description for the API key.
8. In **Data Access**, choose the **Bucket**, **Scope**, and **Collection** that you want the API key to access on your Managed MCP Server's connected operational cluster.

  1. (Optional) To add a new keyspace, click **\+ Add** and choose another bucket, scope, and collection.
9. In **Tools**, choose the tools that you want the API key to use with your Managed MCP Server and connected operational cluster.  
You can search for a tool by name or expand the tool categories and select a tool from the list. Tools are marked as **Read** or **Write**.  
For an overview of all available tools, see [Managed MCP Server Tools Reference](learn/tools.md).  
> [!TIP]  
> Make sure that you add `get_server_configuration_status` and `test_cluster_connection` to your API key so you can [Check the Connection to Your Managed MCP Server](#check-connection).
10. Click **Generate API Key**.
11. Copy your **API Key ID** and **API Key Token** or click **Download Key**.  
You cannot view your key again once you close the **Save API Key Information** pane. Make sure to save your API key information so you can [Add the MCP Configuration to Your Client](#add-config).

### [](#add-allowed-ip)Add an Allowed IP Address to Your Managed MCP Server

To add a new allowed IP address for connections to your Managed MCP Server:

1. In the navigation breadcrumbs, click your organization name.
2. Go to **AI Data Plane** **Access Control** **MCP**.  
> [!TIP]  
> You can also add an allowed IP address for a specific Managed MCP Server by doing the following:  
>  
> 1. Go to **AI Data Plane** **MCP Server**.  
> 2. Click the Managed MCP Server where you want to add an allowed IP address.  
> 3. In **Access**, click **Add allowed IPs** or **Edit allowed IPs**.
3. Click **Add Allowed IP**.
4. In the **MCP Server** list, choose the Managed MCP Server where you want to add a new allowed IP address.
5. Do 1 of the following:

  * Choose **Add IP Address Manually** and enter the IP address or CIDR block where you want to allow connections, in [ipv4 format](https://en.wikipedia.org/wiki/IPv4).
  * Choose **Add Current IP Address**.
  * Choose **Allow Access from Anywhere**.
6. (Optional) In the **Comment** field, enter a comment for the allowed IP.
7. Click **Add Allowed IP Address**.

### [](#add-config)Add the MCP Configuration to Your Client

To add the configuration for your Managed MCP Server to your client:

1. In the navigation breadcrumbs, click your organization name.
2. Go to **AI Data Plane** **Access Control** **MCP**.
3. Expand the entry for the Managed MCP Server that you want to connect to.
4. In **Connect your agent**, click  (**Copy**) to copy your connection information.
5. Follow the steps for your MCP client to add the configuration to your MCP JSON file:

  * [Claude](https://code.claude.com/docs/en/mcp-quickstart#edit-mcp-json-directly)
  * [Cursor](https://cursor.com/docs/mcp#using-mcpjson)
  * [VS Code](https://code.visualstudio.com/docs/agent-customization/mcp-servers#%5Fconfigure-the-mcpjson-file)
  * [Devin AI (formerly Windsurf)](https://docs.devin.ai/cli/extensibility/mcp/configuration#via-config-file)  
  For example, your MCP JSON file could look like the following:  
```json  
{  
  "mcpServers": {  
    "couchbase-mcp": {  
      "headers": {  
        "Accept": "application/json",  
        "Authorization": "Bearer {token/api-key}",  
        "Content-Type": "application/json"  
      },  
      "serverUrl": "https://{managed-mcp-server-host}/mcp"  
    }  
  }  
}  
```

### [](#check-connection)Check the Connection to Your Managed MCP Server

To check the connection to your Managed MCP Server from your agent:

1. Open your MCP client.
2. Ask your agent `What’s the status of the Couchbase MCP Server?`

#### [](#troubleshoot-connection-errors)Troubleshoot Connection Errors

If your agent cannot run the `get_server_configuration_status` tool and return the status of your Managed MCP Server:

* Check that you have correctly added the Managed MCP Server configuration to your client's MCP JSON file.  
The file must be valid JSON and include the `Authorization` header and `serverUrl` field.
* Check that the IP address you're trying to connect from is on your Managed MCP Server's list of allowed IP addresses.  
If the IP address you're trying to use to connect is not on the allowed list of IP addresses, [add it as an allowed IP](#add-allowed-ip).
* Check that you added `get_server_configuration_status` and `test_cluster_connection` as available tools on your API key.  
If these tools are not available with your API key, you must [generate a new API key](#generate-api-key) to add them and check your connection.

## [](#next-steps)Next Steps

For a detailed reference of the tools you can use with your Managed MCP Server, see [Managed MCP Server Tools Reference](learn/tools.md).