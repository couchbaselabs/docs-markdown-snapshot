---
title: Large Result Handling
description: Limit the size of Operational Insights query results, export a
  large result to object storage, and set the timeout for fetching async
  results.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/configuration-oi/pages/large-results-oi.adoc
  xref: xref:mcp-server:configuration-oi:large-results-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/configuration-oi/large-results-oi.html)

# Large Result Handling

> Limit the size of Operational Insights query results, export a large result to object storage, and set the timeout for fetching async results. 

An agent sends tool results to an LLM, so a large result uses a lot of the model context. By default, the server returns the full result of a query without truncation. To limit the size, set a maximum. To keep a large result out of the conversation, export it to object storage.

What happens to a large response after the server returns it depends on your MCP client.

> [!NOTE]
> Some MCP clients save a large response to a file and give the LLM the path to that file. This is client behavior, and the server cannot change it.

## [](#limiting-the-result-size)Limiting the Result Size

Set `CB_MCP_OPERATIONAL_INSIGHTS_QUERY_RESULT_MAX_SIZE`, or the `--operational-insights-query-result-max-size` argument, to the maximum size in bytes. The limit applies to `operational_insights_run_query_sync` and `operational_insights_get_async_query_results`.

* **Not set**: the server returns the full result. This is the default.
* **Set**: the server reads rows as a stream and stops when the next row would exceed the limit. The limit is a hard maximum.
* **Maximum value**: 4,194,304 bytes (4 MB). The server reduces a larger value to 4 MB and logs a warning at startup.
* **Minimum value**: none. A value of `0` is a real limit of zero bytes.

When the server stops reading, the response has `truncated: true`. You cannot retrieve the remaining rows by calling the tool again. Narrow the statement, or export the result. For an async result, the metadata can be empty, because the server reports it only after you read every row.

If the first row alone exceeds the limit, the tool returns no rows and an error message. The message says the result is not empty: matching rows exist, but they're too wide to return.

The size limit applies only to the Operational Insights server. The Couchbase Server tools do not apply this limit.

## [](#exporting-a-result-to-object-storage)Exporting a Result to Object Storage

`operational_insights_run_query_sync` and `operational_insights_run_query_async` can write the result to object storage instead of returning it. The server wraps your statement in `COPY …​ TO`. The tool returns a confirmation with the destination and no rows, so a large result uses no model context.

| Argument         | Description                                                                |
| ---------------- | -------------------------------------------------------------------------- |
| copy\_to\_link   | Name of an existing external link, such as an S3 link. Required to export. |
| copy\_to\_bucket | Destination bucket in the external store. Required to export.              |
| copy\_to\_path   | Path prefix inside that bucket, such as exports/run1. Required to export.  |
| copy\_to\_format | Output format: json (default) or parquet.                                  |

The synchronous tool waits for the whole upload to finish before it returns. For a large export, use `operational_insights_run_query_async` and poll with `operational_insights_get_async_query_results`.

> [!IMPORTANT]
> Read-only mode blocks `COPY …​ TO`, including an export that you request with the `copy_to_*` arguments. A token without the write scope blocks it too.

## [](#timeout-for-async-query-tools)Timeout for Async Query Tools

The four async query tools share one timeout:

* `operational_insights_run_query_async`
* `operational_insights_get_async_query_results`
* `operational_insights_discard_async_query_results`
* `operational_insights_cancel_async_query`

The timeout is a deadline for each request that a tool makes to the cluster. For `operational_insights_get_async_query_results`, the deadline covers the whole fetch, including the time to stream the rows. A large result on a slow network can need more time than the default allows.

Set `CB_MCP_OPERATIONAL_INSIGHTS_ASYNC_QUERY_RESULT_TIMEOUT`, or the `--operational-insights-async-query-result-timeout` argument, to the number of seconds.

* **Default**: 30 seconds.
* **Maximum**: 600 seconds, which is 10 minutes.
* **Any value other than a positive integer**: for example `0`, `-2`, `1.5`, or `abc`. The server uses the default and logs a warning.
* **A value larger than the maximum**: the server uses 600 and logs a warning.

If a fetch times out, the query itself finished on the cluster. Fetching again can fail the same way, because the timeout covers the whole download, so raise the timeout.

A high value has a cost. Every call to an async query tool shares the timeout, so a status, discard, or cancel call can wait that long when the cluster stops responding.

## [](#see-also)See Also

* [Tools](../learn-oi/tools-oi.md)
* [Environment Variables & Command Line Arguments](environment-variables-oi.md)
* [Read-Only Mode](read-only-mode-oi.md)
* [Troubleshooting Large Results](troubleshooting-oi.md#large-result-issues)