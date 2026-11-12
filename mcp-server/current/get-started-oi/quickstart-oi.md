---
title: Quick Start
description: Get the Couchbase MCP Server running in under 5 minutes by
  configuring an MCP client, connection string, and authentication.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: procedure
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/get-started-oi/pages/quickstart-oi.adoc
  xref: xref:mcp-server:get-started-oi:quickstart-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/get-started-oi/quickstart-oi.html)

# Quick Start

> Get the Couchbase MCP Server running in under 5 minutes by configuring an MCP client, connection string, and authentication. 

Get the Couchbase MCP Server running in under 5 minutes.

## [](#prerequisites)Prerequisites

Make sure you complete the [prerequisites](prerequisites-oi.md) before proceeding.

## [](#step-1-configure-your-mcp-client)Step 1: Configure Your MCP Client

Select your MCP client and add the Couchbase MCP Server configuration, using the `operational-insights` subcommand.

> [!NOTE]
> The Docker instructions in this Quick Start run the server in `stdio` mode, where the MCP client starts the container. To run the server in Docker over Streamable HTTP, see [Streamable HTTP Transport Mode](../configuration-oi/streamable-http-oi.md).

* Claude Desktop
* Cursor
* Windsurf
* VS Code
* JetBrains
* Factory

You can integrate the Couchbase MCP Server into [Claude Desktop](https://claude.ai/download/) by following these steps:

1. Open the Claude Desktop configuration file:

  * **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
  * **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Couchbase MCP Server configuration. For detailed instructions, see the [MCP quickstart guide](https://modelcontextprotocol.io/quickstart/user).

  * uvx
  * Docker  
```json  
{  
  "mcpServers": {  
    "couchbase-oi": {  
      "command": "uvx",  
      "args": ["couchbase-mcp-server", "operational-insights"],  
      "env": {  
        "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING": "https://your-oi-endpoint",  
        "CB_OPERATIONAL_INSIGHTS_USERNAME": "your-username",  
        "CB_OPERATIONAL_INSIGHTS_PASSWORD": "your-password"  
      }  
    }  
  }  
}  
```  
```json  
{  
  "mcpServers": {  
    "couchbase-oi": {  
      "command": "docker",  
      "args": [  
        "run", "--rm", "-i",  
        "-e", "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING=https://your-oi-endpoint",  
        "-e", "CB_OPERATIONAL_INSIGHTS_USERNAME=your-username",  
        "-e", "CB_OPERATIONAL_INSIGHTS_PASSWORD=your-password",  
        "couchbase/mcp-server", "operational-insights"  
      ]  
    }  
  }  
}  
```

**Logs:** `~/Library/Logs/Claude` (macOS), `%APPDATA%\Claude\Logs` (Windows)

You can integrate the Couchbase MCP Server into [Cursor](https://cursor.com/download) using either of the following methods.

**Option 1: Add via the Cursor MCP Links**

[![Add Couchbase MCP server to Cursor](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en-US/install-mcp?name=Couchbase-OI&config=eyJjb21tYW5kIjogInV2eCIsICJhcmdzIjogWyJjb3VjaGJhc2UtbWNwLXNlcnZlciIsICJvcGVyYXRpb25hbC1pbnNpZ2h0cyJdLCAiZW52IjogeyJDQl9PUEVSQVRJT05BTF9JTlNJR0hUU19DT05ORUNUSU9OX1NUUklORyI6ICJodHRwczovL3lvdXItb2ktZW5kcG9pbnQiLCAiQ0JfT1BFUkFUSU9OQUxfSU5TSUdIVFNfVVNFUk5BTUUiOiAidXNlcm5hbWUiLCAiQ0JfT1BFUkFUSU9OQUxfSU5TSUdIVFNfUEFTU1dPUkQiOiAicGFzc3dvcmQifX0%3D)

> [!NOTE]
> The [install link](https://cursor.com/docs/mcp/install-links) uses placeholder values from the configuration examples. Update the connection string and credentials after installation.

**Option 2: Manual Addition**

1. Go to **Cursor > Cursor Settings > Tools & Integrations > MCP Tools**. See the [Cursor MCP documentation](https://cursor.com/docs/mcp) for details.
2. Add the Couchbase MCP Server configuration.  
You may need to add the server configuration under a parent key of `mcpServers`.

  * uvx
  * Docker  
```json  
{  
  "mcpServers": {  
    "couchbase-oi": {  
      "command": "uvx",  
      "args": ["couchbase-mcp-server", "operational-insights"],  
      "env": {  
        "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING": "https://your-oi-endpoint",  
        "CB_OPERATIONAL_INSIGHTS_USERNAME": "your-username",  
        "CB_OPERATIONAL_INSIGHTS_PASSWORD": "your-password"  
      }  
    }  
  }  
}  
```  
```json  
{  
  "mcpServers": {  
    "couchbase-oi": {  
      "command": "docker",  
      "args": [  
        "run", "--rm", "-i",  
        "-e", "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING=https://your-oi-endpoint",  
        "-e", "CB_OPERATIONAL_INSIGHTS_USERNAME=your-username",  
        "-e", "CB_OPERATIONAL_INSIGHTS_PASSWORD=your-password",  
        "couchbase/mcp-server", "operational-insights"  
      ]  
    }  
  }  
}  
```

**Logs:** `Bottom panel > Output list > Cursor MCP`

You can integrate the Couchbase MCP Server into [Windsurf](https://windsurf.com/download) by following these steps:

1. Navigate to **Command Palette > Windsurf MCP Configuration Panel** or **Windsurf - Settings > Advanced > Cascade > Model Context Protocol (MCP) Servers**. See the [official documentation](https://docs.windsurf.com/windsurf/cascade/mcp#adding-a-new-mcp-plugin) for details.
2. Click **Add Server** \> **Add custom server**.
3. Add the Couchbase MCP Server configuration.

  * uvx
  * Docker  
```json  
{  
  "mcpServers": {  
    "couchbase-oi": {  
      "command": "uvx",  
      "args": ["couchbase-mcp-server", "operational-insights"],  
      "env": {  
        "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING": "https://your-oi-endpoint",  
        "CB_OPERATIONAL_INSIGHTS_USERNAME": "your-username",  
        "CB_OPERATIONAL_INSIGHTS_PASSWORD": "your-password"  
      }  
    }  
  }  
}  
```  
```json  
{  
  "mcpServers": {  
    "couchbase-oi": {  
      "command": "docker",  
      "args": [  
        "run", "--rm", "-i",  
        "-e", "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING=https://your-oi-endpoint",  
        "-e", "CB_OPERATIONAL_INSIGHTS_USERNAME=your-username",  
        "-e", "CB_OPERATIONAL_INSIGHTS_PASSWORD=your-password",  
        "couchbase/mcp-server", "operational-insights"  
      ]  
    }  
  }  
}  
```

**Logs:** Check Windsurf output panel

You can integrate the Couchbase MCP Server into [VS Code](https://code.visualstudio.com/download) using either of the following methods.

**Option 1: MCP Server bundled with Couchbase VS Code Extension** (Preferred)

The [Couchbase VS Code Extension](https://marketplace.visualstudio.com/items?itemName=Couchbase.vscode-couchbase) (v3.0.0+) bundles the MCP server out-of-the-box. It auto-prompts to start MCP server on cluster connect in stdio transport mode.

From Command Palette (Ctrl+Shift+P / Cmd+Shift+P):

* `Couchbase: Start MCP Server` \- Start the server
* `Couchbase: Get MCP Server Config` \- Inspect config JSON
* `Couchbase: MCP Server Settings` \- Customize disabled tools, elicitation for tools, read-only mode, export paths, and so on.

Quick Start: Install extension → Connect cluster → Accept prompt to start MCP Server.

![vs code mcp](_images/vs-code-mcp.gif) 

Figure 1\. VS Code Extension Installation

**Option 2: Manual Configuration**

See the [VS Code MCP documentation](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) for details.

1. Create a configuration file using one of two scopes:

  * **Workspace**: Create `.vscode/mcp.json` in your project root. Settings apply only to that project.
  * **Global (User)**: Run **MCP: Open User Configuration** from the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`). Settings apply to all projects. On macOS, you can find this file at `~/Library/Application Support/Code/User/mcp.json`.
2. Add the Couchbase MCP Server configuration.

> [!NOTE]
> VS Code uses `servers` as the top-level JSON property, not `mcpServers`.

* uvx
* Docker

```json
{
  "servers": {
    "couchbase-oi": {
      "command": "uvx",
      "args": ["couchbase-mcp-server", "operational-insights"],
      "env": {
        "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING": "https://your-oi-endpoint",
        "CB_OPERATIONAL_INSIGHTS_USERNAME": "your-username",
        "CB_OPERATIONAL_INSIGHTS_PASSWORD": "your-password"
      }
    }
  }
}
```

```json
{
  "servers": {
    "couchbase-oi": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-e", "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING=https://your-oi-endpoint",
        "-e", "CB_OPERATIONAL_INSIGHTS_USERNAME=your-username",
        "-e", "CB_OPERATIONAL_INSIGHTS_PASSWORD=your-password",
        "couchbase/mcp-server", "operational-insights"
      ]
    }
  }
}
```

**Logs:** `Command Palette > MCP: List Servers > Show Output`

You can integrate the Couchbase MCP Server into [JetBrains IDEs](https://www.jetbrains.com/) using either of the following methods.

1. Install the [AI Assistant](https://www.jetbrains.com/help/ai-assistant/mcp.html) or [Junie](https://junie.jetbrains.com/docs/junie-cli-mcp-configuration.html) plug-in.
2. Navigate to **Settings > Tools > AI Assistant (or Junie) > MCP Server**.
3. Click **"+"** to add the Couchbase MCP Server configuration and click **Save**.

  * uvx
  * Docker  
```json  
{  
  "mcpServers": {  
    "couchbase-oi": {  
      "command": "uvx",  
      "args": ["couchbase-mcp-server", "operational-insights"],  
      "env": {  
        "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING": "https://your-oi-endpoint",  
        "CB_OPERATIONAL_INSIGHTS_USERNAME": "your-username",  
        "CB_OPERATIONAL_INSIGHTS_PASSWORD": "your-password"  
      }  
    }  
  }  
}  
```  
```json  
{  
  "mcpServers": {  
    "couchbase-oi": {  
      "command": "docker",  
      "args": [  
        "run", "--rm", "-i",  
        "-e", "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING=https://your-oi-endpoint",  
        "-e", "CB_OPERATIONAL_INSIGHTS_USERNAME=your-username",  
        "-e", "CB_OPERATIONAL_INSIGHTS_PASSWORD=your-password",  
        "couchbase/mcp-server", "operational-insights"  
      ]  
    }  
  }  
}  
```

**Logs:** `Help > Show Log in Finder/Explorer > mcp > couchbase`

You can integrate the Couchbase MCP Server into [Factory](https://factory.ai/) using any of the following methods.

See the [Factory AI MCP documentation](https://docs.factory.ai/cli/configuration/mcp) for details.

**Option 1: Droid CLI**

Run the following command in the Droid CLI:

```bash
droid mcp add couchbase-mcp-oi 'uvx couchbase-mcp-server operational-insights' --env CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING=https://your-oi-endpoint --env CB_OPERATIONAL_INSIGHTS_USERNAME=your-username --env CB_OPERATIONAL_INSIGHTS_PASSWORD=your-password --type stdio
```

**Option 2: Configuration File**

Navigate to the MCP configuration file at `~/.factory/mcp.json` and add the Couchbase MCP Server configuration.

* uvx
* Docker

```json
{
  "mcpServers": {
    "couchbase-oi": {
      "command": "uvx",
      "args": ["couchbase-mcp-server", "operational-insights"],
      "env": {
        "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING": "https://your-oi-endpoint",
        "CB_OPERATIONAL_INSIGHTS_USERNAME": "your-username",
        "CB_OPERATIONAL_INSIGHTS_PASSWORD": "your-password"
      }
    }
  }
}
```

```json
{
  "mcpServers": {
    "couchbase-oi": {
      "command": "docker",
      "args": [
        "run", "--rm", "-i",
        "-e", "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING=https://your-oi-endpoint",
        "-e", "CB_OPERATIONAL_INSIGHTS_USERNAME=your-username",
        "-e", "CB_OPERATIONAL_INSIGHTS_PASSWORD=your-password",
        "couchbase/mcp-server", "operational-insights"
      ]
    }
  }
}
```

**Option 3: Factory MCP Registry**

To configure the Couchbase MCP server using the Factory MCP registry, type `/mcp` in the chat interface to launch the interactive UI. Alternatively, type `/mcp` in the Droid CLI to access the MCP management menu. Browse the registry for the Couchbase MCP server and add it. Once added, Factory appends the Couchbase MCP configuration template to `~/.factory/mcp.json`. Update the placeholder values with your specific settings.

**Logs:** `~/.factory/logs/`

> [!TIP]
> Replace the placeholder values with your actual Operational Insights credentials. See [Environment Variables](../configuration-oi/environment-variables-oi.md) for all available options.

## [](#step-2-set-your-connection-string)Step 2: Set Your Connection String

> [!IMPORTANT]
> The Operational Insights MCP server supports only self-managed deployments. Capella-hosted Operational Insights is not supported.

The connection string is an HTTP(S) URL to your Operational Insights cluster:

```bash
http://your-oi-host:8095
https://your-oi-host:18095
```

Use `https://` if you enable TLS on your Operational Insights cluster.

To find your host and credentials, see the Couchbase Server Web Console: database users are under **Security** ([Manage Users and Roles](https://docs.couchbase.com/server/current/manage/manage-security/manage-users-and-roles.html)).

If your Operational Insights cluster runs on the host machine and you're using Docker, use `host.docker.internal` instead of the hostname in the connection string. See the [Docker networking documentation](https://docs.docker.com/desktop/features/networking/#i-want-to-connect-from-a-container-to-a-service-on-the-host) for more details.

## [](#step-3-set-up-authentication)Step 3: Set Up Authentication

Configure authentication for your MCP server. Choose one of the following methods.

### [](#basic-authentication-username-and-password)Basic Authentication (Username and Password)

For Basic Authentication setup, see [Manage Users and Roles](https://docs.couchbase.com/server/current/manage/manage-security/manage-users-and-roles.html) (self-managed).

Set `CB_OPERATIONAL_INSIGHTS_USERNAME` and `CB_OPERATIONAL_INSIGHTS_PASSWORD` in your MCP client configuration:

```json
{
  "env": {
    "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING": "https://your-oi-endpoint",
    "CB_OPERATIONAL_INSIGHTS_USERNAME": "your-username",
    "CB_OPERATIONAL_INSIGHTS_PASSWORD": "your-password"
  }
}
```

### [](#mtls-mutual-tls)mTLS (Mutual TLS)

Set `CB_OPERATIONAL_INSIGHTS_CLIENT_CERT_PATH` and `CB_OPERATIONAL_INSIGHTS_CLIENT_KEY_PATH`. If your client key or PKCS#12 bundle is encrypted, also set `CB_OPERATIONAL_INSIGHTS_CLIENT_CERT_PASSWORD`:

```json
{
  "env": {
    "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING": "https://your-oi-endpoint",
    "CB_OPERATIONAL_INSIGHTS_CLIENT_CERT_PATH": "/path/to/client-certificate.pem",
    "CB_OPERATIONAL_INSIGHTS_CLIENT_KEY_PATH": "/path/to/client.key"
  }
}
```

See [Configuring Authentication](../configuration-oi/environment-variables-oi.md#configuring-authentication) for full details.

## [](#step-4-validate-the-setup)Step 4: Validate the Setup

Save your configuration and restart your MCP client.

**Check server status** 

Ask your AI assistant:

"What's the status of the Couchbase MCP server?"

The assistant calls `get_server_configuration_status` and returns the server's configuration, including transport mode, read-only mode status, and loaded tools.

If the tool is not available, the server did not start correctly. Check the logs for your client (listed in the preceding client tabs).

**Check connectivity** 

"List the databases in my Operational Insights cluster."

The assistant calls `operational_insights_get_databases_in_cluster`, which connects to the Operational Insights cluster and returns the list of databases.

If the connection fails, verify your `CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING`, `CB_OPERATIONAL_INSIGHTS_USERNAME`, and `CB_OPERATIONAL_INSIGHTS_PASSWORD` values.

## [](#read-only-mode)Read Only Mode

By default, the server runs in **read-only mode** (`CB_MCP_READ_ONLY_MODE=true`):

* SQL++ queries run with the server-side `readonly` option, so the Operational Insights cluster itself rejects data and structure modifications.
* `COPY …​ TO` (export) statements are also blocked client-side.

To enable write operations, set `CB_MCP_READ_ONLY_MODE=false` in your configuration. See [Read-Only Mode](../configuration-oi/read-only-mode-oi.md) for details.

## [](#next-steps)Next Steps

* Review all available [Tools](../learn-oi/tools-oi.md)
* Explore [Configuration](../configuration-oi/index-oi.md) options
* Want to customize or build from source? See [Build from Source](../reference/build-from-source.md)
* Having issues? See [Troubleshooting](../configuration-oi/troubleshooting-oi.md)