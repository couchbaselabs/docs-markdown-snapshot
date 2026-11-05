---
title: Release Notes
description: Version history and release notes for the Couchbase MCP Server.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase MCP Server
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/reference/pages/release-notes.adoc
  xref: xref:1.1@mcp-server:reference:release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/1.1/reference/release-notes.html)

# Release Notes

> Version history and release notes for the Couchbase MCP Server. 

## [](#version-history)Version History

The list below covers each release, newest first.

### [](#v1-1-november-2026)v1.1 (November 2026)

A feature release that adds Operational Insights support, audit logging, and a large set of new tools for cluster health, Search, and vector workloads, organized by category below.

#### [](#new-features)New Features

* **Operational Insights support**: The Couchbase MCP Server now supports self-managed Couchbase Operational Insights deployments. Run it with the new `operational-insights` subcommand (`couchbase-mcp-server operational-insights`). The subcommand ships in the same package and Docker image as the operational server, and uses its own `CB_OPERATIONAL_INSIGHTS_*` connection and credential settings, default HTTP port (`8001`), and set of `operational_insights_`\-prefixed tools. Capella-hosted Operational Insights is not supported. See [Operational Insights Overview](../get-started-oi/overview-oi.md).
* **Multiple MCP servers in one package**: The `couchbase-mcp-server` package now hosts more than one server behind CLI subcommands. The `operational` subcommand is the default, so existing configurations keep working unchanged. See [Architecture](common-architecture.md).
* **Audit logging**: Record tool calls, authorization denials, and guardrail blocks, with the caller identity the server saw, in a dedicated audit log. Audit logging covers both the operational and Operational Insights servers. It writes to `stderr`, to a file, or to both, and supports both time-based and size-based rotation. Enable it with `CB_MCP_AUDIT_LOG_ENABLED`. See [Audit Logging](../configuration/audit-logging.md).
* **Vertical scaling with workers**: The operational server can now run several worker processes on one machine in Streamable HTTP mode. Set `CB_MCP_WORKERS` or `--workers` to the number of workers. Workers run in stateless mode, which `CB_MCP_STATELESS_HTTP` also controls. The Operational Insights server does not support multiple workers. See [Scaling with Workers](../configuration/streamable-http.md#scaling-with-workers).
* **Health endpoint**: In Streamable HTTP mode, the server now exposes `GET /health` for liveness probes. The endpoint reports process liveness only, never contacts the cluster, and needs no authentication. See [Health Check](../configuration/streamable-http.md#health-check).
* **Cluster health and diagnostics tools**: The following tools were added to Cluster Setup & Health.

  * `get_client_connectivity_report` reports the SDK's cached connection state per endpoint.
  * `get_cluster_health_snapshot` returns the health of the cluster as a whole from the Server APIs.
  * `get_cluster_metrics` retrieves cluster statistics over a historic time window.
  * `discover_tool_input_values` finds the exact input values that `get_cluster_metrics` requires, such as valid metric names. The tool is available on self-managed Couchbase Server only.
  * `get_cluster_tasks` lists the tasks the cluster is handling, such as rebalance, index build, compaction, XDCR, and backup.
  * `get_cluster_system_events` returns cluster system events for root-cause correlation.
  * `get_cluster_query_vitals` returns the current Query Service statistics.
  * `get_index_stats` returns Index Service statistics.
  * `get_bucket_config` returns the configuration and live state of one bucket or of every bucket.
* **Query and Index tools**: The following tools were added: `get_active_queries`, `delete_active_query`, and `create_query_index`. `create_query_index` creates regular and vector indexes by running SQL++ rather than using the SDK index manager.
* **Search Operations tools**: The following tools were added: `list_search_indexes`, `get_search_index_definition`, `run_search`, `upsert_search_index`, and `drop_search_index`.
* **Vector search**: Configure an embedding model when you start the MCP server, then run vector search on the Index service (GSI) with `run_vector_query`, or on the Search Service with `run_vector_search`. The server supports the `capella`, `openai`, `cohere`, `voyage`, and `bedrock` embedding providers. See [Embedding Providers](../configuration/environment-variables.md#embedding-providers).
* **Large result handling for Operational Insights**: The query tools return the full result by default. Set `CB_MCP_OPERATIONAL_INSIGHTS_QUERY_RESULT_MAX_SIZE` to limit the result size, up to 4 MB. When a result exceeds the limit, the response reports `truncated: true`. The async query tools use a 30 second timeout for each request to the cluster, so `operational_insights_get_async_query_results` can fetch larger results. Set `CB_MCP_OPERATIONAL_INSIGHTS_ASYNC_QUERY_RESULT_TIMEOUT` or `--operational-insights-async-query-result-timeout` to change it, up to 600 seconds. To keep a large result out of the conversation, `operational_insights_run_query_sync` and `operational_insights_run_query_async` can export it to object storage with the `copy_to_*` arguments. See [Large Result Handling](../configuration-oi/large-results-oi.md).

#### [](#enhancements)Enhancements

* **Active cluster health checks**: `get_cluster_health_and_services` now actively pings cluster services and reports reachability, latency, and connection details. You can filter the check to specific services with `service_types`.
* **Read-only mode coverage**: `upsert_search_index` and `drop_search_index` are disabled when `CB_MCP_READ_ONLY_MODE=true`, in line with the other write-capable tools. `delete_active_query` and `create_query_index` follow the same rule.
* **Index listing**: `list_indexes` now returns both vector and non-vector indexes.
* **Separate Operational Insights log files**: The Operational Insights server writes `mcp_server_operational_insights.<level>.log` by default, so it does not share files with the Operational server.
* **Restructured documentation**: The documentation now has separate Couchbase Server and Operational Insights sections, with shared Reference and Architecture pages.

#### [](#bug-fixes)Bug Fixes

* [DA-2232](https://couchbasecloud.atlassian.net/browse/DA-2232): `get_schema_for_collection` now takes a `num_sample_values` argument. It sets the number of example values that the schema reports for each field. Leave it unset to use the server default, or pass `0` to return the structure without example values.
* [DA-2302](https://jira.issues.couchbase.com/browse/DA-2302): Fixes elicitation, which was not working for tools that require confirmation.
* [DA-1866](https://couchbasecloud.atlassian.net/browse/DA-1866): Fixes the KV write tools swallowing all exceptions and returning only `False`, so callers can now see the underlying cause of a failure.
* [DA-2307](https://jira.issues.couchbase.com/browse/DA-2307): Fixes `mutate_subdocument` passing the unsupported create-parents option to `array_insert`.

#### [](#deprecations)Deprecations

* **`create_index`**: This tool is deprecated. It remains available with a deprecation warning. Use `create_query_index` instead.

#### [](#removals)Removals

* **Python 3.10 support**: The server now requires Python 3.11 to 3.14, because Python 3.10 reached end of life.

### [](#v1-0-1-august-2026)v1.0.1 (August 2026)

A maintenance release with new tools, OAuth and logging enhancements, and bug fixes, organized by category below.

#### [](#new-features-2)New Features

* **Tools**: The following tools were added: `lookup_subdocument`, `mutate_subdocument`, `create_scope`, `delete_scope`, `create_collection`, `delete_collection`, `create_index`, `build_index`, `drop_index`.

#### [](#enhancements-2)Enhancements

* **OAuth Authentication**: This release introduces scope labels to let operators remap the `couchbase-mcp:read`/`couchbase-mcp:write` scope strings to match the naming convention used by their IdP.
* **Logging**: This release introduces enhanced logging capabilities for the Couchbase MCP Server, providing better log retention control, granular size management per log level, and persistent environment logging.

#### [](#bug-fixes-2)Bug Fixes

Bugs:

* [DA-1945](https://couchbasecloud.atlassian.net/browse/DA-1945): Fixes a SQL++ parser error that incorrectly rejected the `WITHIN` keyword.
* [DA-1997](https://couchbasecloud.atlassian.net/browse/DA-1997): Resolves underlying issues with the Lark parser.
* [DA-2002](https://couchbasecloud.atlassian.net/browse/DA-2002): Addresses security vulnerability findings reported for the MCP Server.

Other Issues:

* Fixed a potential SQL++ identifier injection vulnerability in `get_schema_for_collection`.
* Addressed an issue where `disabled_tools` fails silently instead of blocking.
* Fixed non-portability of the Capella root CA path.
* Prevent silent fallback to password authentication when client-certificate configuration is incomplete.
* Ensures KV write tools return failure reasons rather than just a boolean.
* Correct inconsistent operator matching during `EXPLAIN` evaluation.
* Enable previously inactive Bandit security rules.

#### [](#deprecations-2)Deprecations

* `CB_MCP_LOG_MAX_BYTES` is deprecated. While the functionality continues to be supported, it's recommended to use `CB_MCP_LOG_ROTATION_MAX_SIZE_MB`.

#### [](#removals-2)Removals

* _None in this release._

### [](#v1-0-0-june-30-2026)v1.0.0 (June 30, 2026)

The first 1.0 release, organized by category below.

#### [](#new-features-3)New Features

* **OAuth Authentication**: Secure the Streamable HTTP endpoint with OAuth 2.1 JWT token verification and scope-based authorization (`couchbase-mcp:read` / `couchbase-mcp:write`), with optional Protected Resource Metadata (PRM) for Dynamic Client Registration. See [OAuth](../configuration/oauth-overview.md).
* **Logging**: Configurable structured logging with log levels (`CB_MCP_LOG_LEVEL`), multiple output sinks (`CB_MCP_LOG_SINKS` — console, file, or both), and file output (`CB_MCP_LOG_FILE`). See [Logging](../configuration/logging.md).

#### [](#enhancements-3)Enhancements

* _None in this release._

#### [](#bug-fixes-3)Bug Fixes

* _None in this release._

#### [](#deprecations-3)Deprecations

* _None in this release._

#### [](#removals-3)Removals

* **Removed `CB_MCP_READ_ONLY_QUERY_MODE`**: The previously deprecated read-only query mode has been removed. Use `CB_MCP_READ_ONLY_MODE` instead, which blocks all write operations (KV and SQL++). See [Read-Only Mode](../configuration/read-only-mode.md).
* **Removed SSE transport**: The previously deprecated Server-Sent Events (SSE) transport has been removed. Use the [Streamable HTTP](../configuration/streamable-http.md) transport (`CB_MCP_TRANSPORT=http`) instead.

### [](#v0-8-0-may-27-2026)v0.8.0 (May 27, 2026)

* **Python 3.14 Support**: The Couchbase MCP Server is now compatible with Python 3.14, allowing users to take advantage of the latest features and improvements in the Python ecosystem.
* **List Indexes Tool**: List indexes tool will be powered by SQL++ for Couchbase Server versions 8.0 and above. Users can set `return_raw_index_stats=true` to return the unprocessed index information.
* **Migrate to FastMCP SDK**: The server has been updated to use the native [FastMCP SDK](https://gofastmcp.com/getting-started/welcome) instead of the native [MCP SDK](https://py.sdk.modelcontextprotocol.io/).
* **Docker Base Image Update**: The base images for the prebuilt Docker images have been updated to `python:3.13-slim-trixie` for security and performance improvements.

### [](#v0-7-1-april-9-2026)v0.7.1 (April 9, 2026)

* **Fix for test\_cluster\_connection Tool**: Resolved an issue where the `test_cluster_connection` tool could cause an exception with the latest Couchbase SDK (4.6.0). The tool now accurately reflects the connection status in its response.
* **Update Development Dependencies**: Updated development dependencies for pytest and pytest-asyncio to latest versions.

### [](#v0-7-0-april-1-2026)v0.7.0 (April 1, 2026)

* **Explain Query Tool**: New `explain_sql_plus_plus_query` tool returns query execution plans for LLM analysis and optimization.
* **Elicitation for Tool Calls**: New `CB_MCP_CONFIRMATION_REQUIRED_TOOLS` setting enables user confirmation prompts for specified tools before execution.

**Note:** The tool call for `test_cluster_connection` has a [bug](https://github.com/couchbase/mcp-server-couchbase/issues/127) with the Couchbase Python SDK 4.6.0\. The solution is to downgrade the SDK version in the MCP server to 4.5.0 or upgrade the MCP server to version 0.7.1.

### [](#v0-6-1-february-6-2026)v0.6.1 (February 6, 2026)

* **Read-Only Mode**: New `CB_MCP_READ_ONLY_MODE` setting disables all write operations (KV write tools not loaded, SQL++ write queries blocked). Enabled by default for safety.
* **Tool Disabling**: Disable individual tools via `CB_MCP_DISABLED_TOOLS` (comma-separated list or file path).
* **Expanded CRUD Support**: Added `insert_document_by_id`, `replace_document_by_id`, and `delete_document_by_id` tools in addition to existing get and upsert operations.
* **IDE Support**: Added support for VS Code and JetBrains IDEs (AI Assistant and Junie plugins).

### [](#v0-5-3-december-10-2025)v0.5.3 (December 10, 2025)

* **Query Performance Analysis**: Added 7 tools for identifying slow-running queries, frequently executed queries, primary index usage, non-covering indexes, non-selective queries, large response sizes, and large result counts.

### [](#v0-5-2-november-13-2025)v0.5.2 (November 13, 2025)

* **MCP Registry Support**: MCP server added to the [MCP Registry](https://modelcontextprotocol.io/registry) for easier discovery and installation by clients.

### [](#v0-5-1-november-3-2025)v0.5.1 (November 3, 2025)

* **List Indexes**: New `list_indexes` tool with optional filtering by bucket, scope, collection, and index name.
* **Index Recommendations**: New `get_index_advisor_recommendations` tool using the Couchbase Index Advisor.
* **Cluster Health**: New `get_cluster_health_and_services` tool for monitoring cluster status and service latency.

## [](#checking-your-version)Checking Your Version

```bash
uvx couchbase-mcp-server --version
```

## [](#installation-channels)Installation Channels

| Channel        | Update Method                                                |  |
| -------------- | ------------------------------------------------------------ |  |
| **PyPI**       | uvx couchbase-mcp-server always runs the latest version      |  |
| **Docker Hub** | Pull the latest tag: docker pull couchbase/mcp-server:latest |  |
| **Source**     | git pull and uv sync                                         |  |