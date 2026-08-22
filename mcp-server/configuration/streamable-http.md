---
title: Streamable HTTP Transport Mode
description: Run the Couchbase MCP Server in Streamable HTTP transport mode to
  allow multiple clients to connect over HTTP.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/configuration/pages/streamable-http.adoc
  xref: xref:mcp-server:configuration:streamable-http.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/configuration/streamable-http.html)

# Streamable HTTP Transport Mode

> Run the Couchbase MCP Server in Streamable HTTP transport mode to allow multiple clients to connect over HTTP. 

Run the server in [Streamable HTTP](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#streamable-http) transport mode to allow multiple clients to connect to the same server instance via HTTP.

> [!TIP]
> When the server is exposed over HTTP, any client that can reach the endpoint can call its tools. To secure it, see [OAuth](oauth-overview.md).

> [!WARNING]
> The server serves plain HTTP and does not terminate TLS. For any non-local or production deployment, run it behind a reverse proxy that terminates TLS so traffic is encrypted in transit. See [Securing the Endpoint with TLS](#securing-the-endpoint-with-tls).

* uvx
* Docker

**Start the server:**

```bash
uvx couchbase-mcp-server \
  --connection-string='couchbases://your-connection-string' \
  --username='your-username' \
  --password='your-password' \
  --read-only-mode=true \
  --transport=http
```

The server will be available at `<http://localhost:8000/mcp>` by default.

**MCP client configuration:**

```json
{
  "mcpServers": {
    "couchbase-http": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

Set `CB_MCP_PORT` or `--port` to use a different port. Set `CB_MCP_HOST=0.0.0.0` or `--host=0.0.0.0` to allow external connections.

**Run the MCP server as an independent container:**

```bash
docker run --rm -i \
  -e CB_CONNECTION_STRING='<couchbase_connection_string>' \
  -e CB_USERNAME='<database_user>' \
  -e CB_PASSWORD='<database_password>' \
  -e CB_MCP_TRANSPORT='http' \
  -e CB_MCP_READ_ONLY_MODE='true' \
  -e CB_MCP_HOST=0.0.0.0 \
  -e CB_MCP_PORT=9001 \
  -p 9001:9001 \
  couchbase/mcp-server
```

> [!WARNING]
> Setting `CB_MCP_HOST=0.0.0.0` exposes the MCP server to anyone who can reach the container. For production use cases, make sure you configure Docker networking to secure it.

> [!NOTE]
> You can specify the container's networking with `--network=<your_network>`. The default is `bridge`. See [Docker network drivers](https://docs.docker.com/engine/network/drivers/).

**MCP client configuration:**

```json
{
  "mcpServers": {
    "couchbase-http": {
      "url": "http://localhost:9001/mcp"
    }
  }
}
```

## [](#securing-the-endpoint-with-tls)Securing the Endpoint with TLS

The server serves **plain HTTP** and does not terminate TLS itself. Over plain HTTP, all request and response data travels unencrypted and can be intercepted — including OAuth bearer tokens in the `Authorization` header when [OAuth](oauth-overview.md) is enabled.

For any non-local or production deployment, run the server behind a **reverse proxy that terminates TLS** (for example nginx) and forwards traffic to the server's HTTP port. Clients then connect to the proxy's `https://` URL.

![reverse proxy reference architecture v1.0](_images/reverse-proxy-reference-architecture-v1.0.png) 

Figure 1\. Reverse Proxy Reference Architecture