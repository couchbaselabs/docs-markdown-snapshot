---
title: Release Notes
description: Version history and release notes for the Couchbase MCP Server.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/reference/pages/release-notes.adoc
  xref: xref:mcp-server:reference:release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/reference/release-notes.html)

# Release Notes

> Version history and release notes for the Couchbase MCP Server. 

## [](#version-history)Version History

The list below covers each release, newest first.

### [](#v1-0-1-august-2026)v1.0.1 (August 2026)

A maintenance release with new tools, OAuth and logging enhancements, and bug fixes, organized by category below.

#### [](#new-features)New Features

* **Tools**: The following tools were added: `lookup_subdocument`, `mutate_subdocument`, `create_scope`, `delete_scope`, `create_collection`, `delete_collection`, `create_index`, `build_index`, `drop_index`.

#### [](#enhancements)Enhancements

* **OAuth Authentication**: This release introduces scope labels to let operators remap the `couchbase-mcp:read`/`couchbase-mcp:write` scope strings to match the naming convention used by their IdP.
* **Logging**: This release introduces enhanced logging capabilities for the Couchbase MCP Server, providing better log retention control, granular size management per log level, and persistent environment logging.

#### [](#bug-fixes)Bug Fixes

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

#### [](#deprecations)Deprecations

* `CB_MCP_LOG_MAX_BYTES` is deprecated. While the functionality continues to be supported, it's recommended to use `CB_MCP_LOG_ROTATION_MAX_SIZE_MB`.

#### [](#removals)Removals

* _None in this release._

### [](#v1-0-0-june-30-2026)v1.0.0 (June 30, 2026)

The first 1.0 release, organized by category below.

#### [](#new-features-2)New Features

* **OAuth Authentication**: Secure the Streamable HTTP endpoint with OAuth 2.1 JWT token verification and scope-based authorization (`couchbase-mcp:read` / `couchbase-mcp:write`), with optional Protected Resource Metadata (PRM) for Dynamic Client Registration. See [OAuth](../configuration/oauth-overview.md).
* **Logging**: Configurable structured logging with log levels (`CB_MCP_LOG_LEVEL`), multiple output sinks (`CB_MCP_LOG_SINKS` — console, file, or both), and file output (`CB_MCP_LOG_FILE`). See [Logging](../configuration/logging.md).

#### [](#enhancements-2)Enhancements

* _None in this release._

#### [](#bug-fixes-2)Bug Fixes

* _None in this release._

#### [](#deprecations-2)Deprecations

* _None in this release._

#### [](#removals-2)Removals

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

## [](#upcoming-features)Upcoming Features

* **Search-Based Tools**: Tools for Full Text Search (FTS).

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