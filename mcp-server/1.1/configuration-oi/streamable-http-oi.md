---
title: Streamable HTTP Transport Mode
description: Run the Couchbase MCP Server in Streamable HTTP transport mode to
  allow multiple clients to connect over HTTP.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase MCP Server
    version: "1.1"
  topic_type: procedure
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/configuration-oi/pages/streamable-http-oi.adoc
  xref: xref:1.1@mcp-server:configuration-oi:streamable-http-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/1.1/configuration-oi/streamable-http-oi.html)

# Streamable HTTP Transport Mode

> Run the Couchbase MCP Server in Streamable HTTP transport mode to allow multiple clients to connect over HTTP. 

Run the server in [Streamable HTTP](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#streamable-http) transport mode to allow multiple clients to connect to the same server instance via HTTP.

> [!TIP]
> When you expose the server over HTTP, any client that can reach the endpoint can call its tools. To secure it, see [OAuth](oauth-overview-oi.md).

> [!WARNING]
> The server serves plain HTTP and does not terminate TLS. For any non-local or production deployment, run it behind a reverse proxy that terminates TLS, so TLS encrypts traffic in transit. See [Securing the Endpoint with TLS](#securing-the-endpoint-with-tls).

* uvx
* Docker

**Start the server:**

```bash
uvx couchbase-mcp-server operational-insights \
  --connection-string='https://your-oi-endpoint' \
  --username='your-username' \
  --password='your-password' \
  --read-only-mode=true \
  --transport=http
```

The server is available at `<http://localhost:8001/mcp>` by default.

**MCP client configuration:**

```json
{
  "mcpServers": {
    "couchbase-oi-http": {
      "url": "http://localhost:8001/mcp"
    }
  }
}
```

Set `CB_MCP_PORT` or `--port` to use a different port. Set `CB_MCP_HOST=0.0.0.0` or `--host=0.0.0.0` to allow external connections.

**Run the MCP server as an independent container:**

```bash
docker run --rm -i \
  -e CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING='<operational_insights_connection_string>' \
  -e CB_OPERATIONAL_INSIGHTS_USERNAME='<database_user>' \
  -e CB_OPERATIONAL_INSIGHTS_PASSWORD='<database_password>' \
  -e CB_MCP_TRANSPORT='http' \
  -e CB_MCP_READ_ONLY_MODE='true' \
  -e CB_MCP_HOST=0.0.0.0 \
  -e CB_MCP_PORT=9001 \
  -p 9001:9001 \
  couchbase/mcp-server operational-insights
```

> [!WARNING]
> Setting `CB_MCP_HOST=0.0.0.0` exposes the MCP server to anyone who can reach the container. For production use cases, make sure you configure Docker networking to secure it.

> [!NOTE]
> You can specify the container's networking with `--network=<your_network>`. The default is `bridge`. See [Docker network drivers](https://docs.docker.com/engine/network/drivers/).

**MCP client configuration:**

```json
{
  "mcpServers": {
    "couchbase-oi-http": {
      "url": "http://localhost:9001/mcp"
    }
  }
}
```

## [](#stateless-mode-and-workers)Stateless Mode and Workers

The Operational Insights server accepts `--stateless-http` or `CB_MCP_STATELESS_HTTP` with a single worker. Stateless mode removes the need for sticky sessions for the MCP session, but not for the async query tools. Those tools keep query handles in the memory of one server, so route all requests for a handle to the same server. See [Async Query Issues](troubleshooting-oi.md#async-query-issues).

The Operational Insights server does not support multiple workers. It refuses to start when you set `--workers` or `CB_MCP_WORKERS` to more than `1`.

## [](#health-check)Health Check

In Streamable HTTP mode, the server exposes `GET /health` for liveness probes, such as a Kubernetes liveness probe.

```bash
curl http://localhost:8001/health
```

The endpoint returns a JSON object:

```json
{"status": "ok", "server": "<server-id>"}
```

The endpoint reports process liveness only. It never contacts the Operational Insights cluster, so a credential or cluster fault does not cause a restart loop. It needs no authentication, even when you enable [OAuth](oauth-overview-oi.md).

## [](#securing-the-endpoint-with-tls)Securing the Endpoint with TLS

The server serves **plain HTTP** and does not terminate TLS itself. Over plain HTTP, anyone on the network can read or intercept all request and response data, including OAuth bearer tokens in the `Authorization` header when you enable [OAuth](oauth-overview-oi.md).

For any non-local or production deployment, run the server behind a **reverse proxy that terminates TLS** (for example, nginx). The proxy forwards traffic to the server's HTTP port. Clients then connect to the proxy's `https://` URL.

![reverse proxy reference architecture v1.0](_images/reverse-proxy-reference-architecture-v1.0.png) 

Figure 1\. Reverse Proxy Reference Architecture