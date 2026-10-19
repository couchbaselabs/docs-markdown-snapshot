---
title: Managed Agent Memory Metrics and Alerts Reference
description: Reference for the metrics on the Managed Agent Memory monitoring
  dashboard and the alerts that Capella sends for a Managed Agent Memory server.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/reference/pages/metrics-alerts-agent-mem-managed.adoc
  xref: xref:agent-mem:reference:metrics-alerts-agent-mem-managed.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/reference/metrics-alerts-agent-mem-managed.html)

# Managed Agent Memory Metrics and Alerts Reference

> Reference for the metrics on the Managed Agent Memory monitoring dashboard and the alerts that Capella sends for a Managed Agent Memory server. 

For how to view the dashboard and receive alerts, see [Monitor Managed Agent Memory](../managed/monitor-agent-mem-managed.md).

## [](#metrics)Metrics

The following table lists the Agent Memory server metric behind each card and chart on the [monitoring dashboard](../managed/monitor-agent-mem-managed.md#dashboard). Rates and percentiles use a 5-minute window.

| Section         | Card or chart                 | Metric                                                | Calculation                                                                                 |
| --------------- | ----------------------------- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| API             | Requests total                | agentmemory\_requests\_total                          | Rate per second, summed across endpoints.                                                   |
| API             | API errors total              | agentmemory\_api\_errors\_total                       | Rate per second, summed across status codes.                                                |
| API             | Blocks added                  | agentmemory\_blocks\_added\_total                     | Rate per second, summed across block types.                                                 |
| API             | Request Duration              | agentmemory\_request\_duration\_seconds               | 99th percentile, for each endpoint.                                                         |
| API             | Tokens per Memory Block       | agentmemory\_tokens\_per\_block                       | 95th percentile, for each type.                                                             |
| Models & search | Embedding failures            | agentmemory\_embedding\_failures\_total               | Rate per second.                                                                            |
| Models & search | Context failures              | agentmemory\_context\_generation\_failures\_total     | Rate per second.                                                                            |
| Models & search | Embedding Generation Duration | agentmemory\_embedding\_generation\_duration\_seconds | 99th percentile, for each model.                                                            |
| Models & search | Context Generation Duration   | agentmemory\_context\_generation\_duration\_seconds   | 99th percentile, for each model.                                                            |
| Ingestion queue | Queue size                    | agentmemory\_async\_batch\_queue\_size                | Sum of queued items across nodes. Items in progress are not included.                       |
| Ingestion queue | Queue capacity                | agentmemory\_config\_queue\_max\_size                 | Sum across nodes. Equals your **Queue max size** setting multiplied by the number of nodes. |
| Ingestion queue | Extraction success rate       | agentmemory\_async\_batch\_process\_outcomes\_total   | Successful outcomes as a share of all outcomes.                                             |
| Ingestion queue | Extraction failures           | agentmemory\_async\_batch\_process\_outcomes\_total   | Rate per second of failed outcomes.                                                         |
| Ingestion queue | Queue Wait Time               | agentmemory\_queue\_wait\_time\_seconds               | 99th percentile.                                                                            |
| Ingestion queue | Extraction Duration           | agentmemory\_async\_batch\_process\_duration\_seconds | 99th percentile.                                                                            |
| Rate budget     | Tokens available              | agentmemory\_rate\_budget\_available\_tokens          | Sum across nodes.                                                                           |
| Rate budget     | Max token budget              | agentmemory\_rate\_budget\_max\_tokens                | Maximum across nodes. Equals each node's share of your **Tokens per minute** setting.       |
| Rate budget     | Requests available            | agentmemory\_rate\_budget\_available\_requests        | Sum across nodes.                                                                           |
| Rate budget     | Max request budget            | agentmemory\_rate\_budget\_max\_requests              | Maximum across nodes. Equals each node's share of your **Requests per minute** setting.     |
| Health          | Overall health                | agentmemory\_health\_check\_status                    | Lowest value of the dispatcher, async loop, and database components. 1 means healthy.       |
| Health          | Dispatcher health             | agentmemory\_health\_check\_status                    | Dispatcher component. 1 means healthy.                                                      |
| Health          | Async loop health             | agentmemory\_health\_check\_status                    | Async loop component. 1 means healthy.                                                      |
| Health          | Database health               | agentmemory\_health\_check\_status                    | Database component. 1 means healthy.                                                        |
| Health          | Model health                  | agentmemory\_health\_check\_status                    | Lowest value of the embedding model and LLM components. 1 means healthy.                    |
| Health          | Live nodes                    | agentmemory\_cluster\_live\_node\_count               | Maximum across nodes.                                                                       |

## [](#alerts)Alerts

Capella sends the following alerts for each Agent Memory server. Capella checks each alert on each node, except the 2 retrieval latency alerts. You cannot change their conditions.

| Alert                                                                                   | Severity | Fires when                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Agent Memory Read/Write Error Rate                                                      | Critical | More than 2% of requests return a service error (5xx) over 5 minutes, with at least 10 service errors.                                                                                                                                              |
| Agent Memory Model Provider Error Rate                                                  | Critical | More than 5% of calls to your embedding model or LLM fail over 5 minutes, with at least 10 errors. Check the status of your model provider and your OpenAI integrations.                                                                            |
| Agent Memory Queue Depth                                                                | Critical | The extraction queue, including items in progress, is more than 90% full. When the queue is full, requests to add memory return HTTP 429 with a Retry-After header.                                                                                 |
| Agent Memory Model/DB Unreachable                                                       | Critical | Your server cannot reach your models or your cluster for more than 5 consecutive health checks.                                                                                                                                                     |
| Agent Memory Key Revoked                                                                | Critical | The OpenAI API key for your embedding model or LLM is deleted or revoked. Your server needs a valid key.                                                                                                                                            |
| Agent Memory KV retrieval latency has degraded and requires investigation.              | Critical | The 99th percentile latency of key-value reads over 5 minutes is more than twice the 99th percentile for the previous hour, with at least 20 samples.                                                                                               |
| Agent Memory semantic search retrieval latency has degraded and requires investigation. | Critical | The 99th percentile latency of semantic search over 5 minutes is more than twice the 99th percentile for the previous hour, with at least 20 samples.                                                                                               |
| Agent Memory Custom Prompt Fallback                                                     | Warning  | Within the last 15 minutes, Agent Memory extracted memory with the default prompt because it could not load a custom prompt. For more information, see [Customize Extraction and Summarization Prompts](../develop/customize-prompts-agent-mem.md). |
| Agent Memory Storage Capacity Warning                                                   | Warning  | A node has used 80% or more of its disk storage. If the disk fills, requests to add memory fail.                                                                                                                                                    |

## [](#see-also)See Also

* [Monitor Managed Agent Memory](../managed/monitor-agent-mem-managed.md)
* [Deploy Managed Agent Memory](../managed/deploy-agent-mem-managed.md)