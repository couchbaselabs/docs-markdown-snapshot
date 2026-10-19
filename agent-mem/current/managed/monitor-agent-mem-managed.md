---
title: Monitor Managed Agent Memory
description: Monitor the requests, models, extraction queue, and health of your
  Managed Agent Memory server in Capella, and receive alerts when it needs
  attention.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Couchbase Agent Memory
    version: "1.1"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-agentmemory/edit/release/1.1/modules/managed/pages/monitor-agent-mem-managed.adoc
  xref: xref:agent-mem:managed:monitor-agent-mem-managed.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/agent-mem/current/managed/monitor-agent-mem-managed.html)

# Monitor Managed Agent Memory

> Monitor the requests, models, extraction queue, and health of your Managed Agent Memory server in Capella, and receive alerts when it needs attention. 

Capella collects metrics from every node in your Managed Agent Memory server. You can view them on the Agent Memory monitoring dashboard, and receive alerts through the same channels as your other Capella alerts.

## [](#prerequisites)Prerequisites

* You have deployed a Managed Agent Memory server. For more information, see [Deploy Managed Agent Memory](deploy-agent-mem-managed.md).
* You have a Capella role that can view Agent Memory servers in the project. For more information, see [Control Access to Managed Agent Memory](access-agent-mem-managed.md).

## [](#dashboard)View the Monitoring Dashboard

To view the monitoring dashboard for your Agent Memory server:

1. Go to **AI Data Plane** **Monitoring**.
2. Click the **Agent Memory** tab.
3. In the **Agent Memory** list, choose your server.
4. (Optional) Choose a time window for the charts.

The dashboard starts with your server's status and its number of critical and warning alerts. The rest of the dashboard has the following sections. For the metric behind each card and chart, see [Metrics](../reference/metrics-alerts-agent-mem-managed.md#metrics).

### [](#api)API

| Card or chart           | What it shows                                                                                                                                                                                            |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Requests total          | Requests per second, across all API endpoints.                                                                                                                                                           |
| API errors total        | Error responses per second, including both caller errors (4xx) and service errors (5xx).                                                                                                                 |
| Blocks added            | Memory blocks added per second. This count does not decrease when you delete memory, and does not measure storage size.                                                                                  |
| Request Duration        | The 99th percentile request latency for each API endpoint, including search. The first request to add memory takes longer, while Agent Memory initializes the tokenizer that counts each block's tokens. |
| Tokens per Memory Block | The 95th percentile token count of incoming memory blocks, for messages and facts.                                                                                                                       |

### [](#models)Models & Search

| Card or chart                 | What it shows                                                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Embedding failures            | Failed calls to your embedding model per second.                                                                                           |
| Context failures              | Failed calls to your LLM per second.                                                                                                       |
| Embedding Generation Duration | The 99th percentile embedding latency, for each model. Agent Memory generates embeddings when your agent adds memory and when it searches. |
| Context Generation Duration   | The 99th percentile LLM latency for extraction and summarization, for each model.                                                          |

### [](#ingestion-queue)Ingestion Queue

| Card or chart           | What it shows                                                                                                                                                                                            |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Queue size              | Memory blocks waiting for extraction.                                                                                                                                                                    |
| Queue capacity          | The total queue capacity across all nodes, which is your **Queue max size** setting multiplied by the number of nodes. When a node's queue is full, requests to add memory on that node return HTTP 429. |
| Extraction success rate | The share of extractions that succeed.                                                                                                                                                                   |
| Extraction failures     | Failed extractions per second.                                                                                                                                                                           |
| Queue Wait Time         | The 99th percentile time a memory block waits in the queue before extraction starts.                                                                                                                     |
| Extraction Duration     | The 99th percentile time extraction takes once it starts.                                                                                                                                                |

Together, **Queue Wait Time** and **Extraction Duration** show how long a new memory block takes to become searchable.

### [](#rate-budget)Rate Budget

| Card               | What it shows                                                                                                        |
| ------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Tokens available   | Model tokens remaining in the current minute, across all nodes.                                                      |
| Max token budget   | Each node's share of your **Tokens per minute** setting, which is the setting divided by the number of live nodes.   |
| Requests available | Model requests remaining in the current minute, across all nodes.                                                    |
| Max request budget | Each node's share of your **Requests per minute** setting, which is the setting divided by the number of live nodes. |

When the available tokens or requests reach 0, extraction waits until more budget is available.

### [](#health)Health

| Card              | What it shows                                                                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Overall health    | Whether the dispatcher, the background processing loop, and the connection to your cluster are all healthy. The Model health card covers your models. |
| Dispatcher health | Whether the process that dispatches memory blocks for extraction is healthy.                                                                          |
| Async loop health | Whether the background processing loop is healthy.                                                                                                    |
| Database health   | Whether your server can reach your cluster.                                                                                                           |
| Model health      | Whether your server can reach your embedding model and LLM.                                                                                           |
| Live nodes        | The number of nodes in your server that are running.                                                                                                  |

## [](#alerts)Receive Alerts

Capella monitors your Agent Memory server and sends alerts through the Capella UI and email.

Capella sets the conditions for each alert. You cannot change them. For the alerts that Capella sends and their conditions, see [Alerts](../reference/metrics-alerts-agent-mem-managed.md#alerts).

For more information about how to receive Capella alerts, see [Receive Alerts](../../../cloud/clusters/monitoring/alerts.md).

## [](#see-also)See Also

* [Managed Agent Memory Metrics and Alerts Reference](../reference/metrics-alerts-agent-mem-managed.md)
* [Deploy Managed Agent Memory](deploy-agent-mem-managed.md)
* [Alert Integrations](../../../cloud/clusters/monitoring/alert-integration.md)