---
title: Monitoring Reference
description: This reference lists the metric graphs displayed in the Capella AI
  Services UI Monitoring dashboards.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/reference/pages/monitoring-reference.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ai:reference:monitoring-reference.adoc[]
---

[View original HTML](/ai/reference/monitoring-reference.html)

# Monitoring Reference

> This reference lists the metric graphs displayed in the Capella AI Services UI Monitoring dashboards. 

The Capella AI Services **Monitoring** dashboards display a set of metric graphs for unstructured data, structured data, and models, enabling users to monitor AI Services performance in real time.

For more information about Capella’s Monitoring dashboards, see [View Monitoring Dashboards](../admin/monitor-dashboard.md).

This monitoring reference lists:

* The **Graph Name** as displayed in the Capella UI.
* A **Description** of what this metric graph entails.
* The **Metric** calculation method for this metric.

These monitoring dashboards offer the following metrics:

### Unstructured Data

All the metrics shown in the Unstructured Data dashboard.

| Graph Name                           | Description                                                       | Metric                                                                                                                           |
| ------------------------------------ | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Documents in Workflow                | Total number of JSON documents written to KV Store in a workflow. | sum by (workflowId) (uds\_workflow\_number\_of\_documents\_loaded{databaseId="<databaseId>",tenantId="<tenantId>"})              |
| Number of Workflow Operations        | Total number of successful files in workflow operations.          | sum by (workflowId) (uds\_workflow\_number\_of\_files\_succeeded\_in\_workflow{databaseId="<databaseId>",tenantId="<tenantId>"}) |
| Number of Failed Workflow Operations | Total number of failed files in workflow operations.              | sum by (workflowId) (uds\_workflow\_number\_of\_files\_failed\_in\_workflow{databaseId="<databaseId>",tenantId="<tenantId>"})    |
| Pages in Workflow                    | Total number of pages processed in a workflow.                    | sum by (workflowId) (uds\_workflow\_number\_of\_pages\_in\_workflow{databaseId="<databaseId>",tenantId="<tenantId>"})            |
| Pending Files in Workflow            | Total number of pending files to be processed in a workflow.      | sum by (workflowId) (uds\_workflow\_number\_of\_files\_pending\_in\_workflow{databaseId="<databaseId>",tenantId="<tenantId>"})   |
| Total Files in Workflow              | Total number of files in a workflow.                              | sum by (workflowId) (uds\_workflow\_number\_of\_files\_in\_workflow{databaseId="<databaseId>",tenantId="<tenantId>"})            |

### Structured Data

All the metrics shown in the Structured Data monitoring dashboard.

| Graph Name                         | Description                                                                                      | Metric                                                                                                                                                                                                                                                             |
| ---------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Average Embedding Response Latency | Histogram of embedding service response times for requests made in a workflow.                   | avg by (workflowId) (embedding\_service\_response\_duration\_seconds{databaseId="<databaseId>",tenantId="<tenantId>"})                                                                                                                                             |
| Number of Embeddings Written       | Total number of embedding write attempts to source documents that were successful in a workflow. | sum by (workflowId) (embedding\_writes\_total{databaseId="<databaseId>",status="success",tenantId="<tenantId>"})                                                                                                                                                   |
| Number of Queries Errored Out      | Number of queries processed successfully vs number of queries errored out in a workflow.         | sum by (workflowId) (embedding\_service\_failures\_total{databaseId="<databaseId>",tenantId="<tenantId>",type=\~"timeout\|4xx|5xx"} + embedding\_writes\_total{cause=\~"timeout|too\_big|other",databaseId="<databaseId>",status="failure",tenantId="<tenantId>"}) |
| Number of Failed Mutations         | Total number of mutations processed unsuccessfully in a workflow.                                | sum by (workflowId) (mutations\_processed\_total{cause=\~"too\_big\|other",databaseId="<databaseId>",tenantId="<tenantId>",type="failure"})                                                                                                                        |
| Number of Requests                 | Total number of batch requests sent to the embedding model in a workflow.                        | sum by (workflowId) (batch\_requests\_total{databaseId="<databaseId>",tenantId="<tenantId>",type=\~"full\|timeout\_triggered"})                                                                                                                                    |
| Number of Requests per Second      | Total number of batch requests sent to the embedding model per second in a workflow.             | sum by (workflowId) (rate(batch\_requests\_total{databaseId="<databaseId>",tenantId="<tenantId>",type=\~"full\|timeout\_triggered"}\[5m\]))                                                                                                                        |
| Workflow Write Success Rate        | Total number of embedding write attempts to source documents that were successful in a workflow. | avg by (workflowId) ((embedding\_writes\_total{databaseId="<databaseId>",status="success",tenantId="<tenantId>"} / embedding\_writes\_total{databaseId="<databaseId>",tenantId="<tenantId>"}) \* 100)                                                              |
| Number of Successful Mutations     | Total number of mutations processed successfully in a workflow.                                  | sum by (workflowId) (mutations\_processed\_total{databaseId="<databaseId>",tenantId="<tenantId>",type="success"})                                                                                                                                                  |
| Number of Tokens Processed         | Total number of tokens consumed in a workflow.                                                   | sum by (workflowId) (tokens\_processed\_total{databaseId="<databaseId>",tenantId="<tenantId>"})                                                                                                                                                                    |
| Number of Documents                | Total number of documents processed in a workflow.                                               | sum by (workflowId) (total\_docs{databaseId="<databaseId>",tenantId="<tenantId>"})                                                                                                                                                                                 |

### Models

All the metrics shown in the Model monitoring dashboard.

| Graph Name              | Description                                                            | Metric                                                                                                                                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cache Hit Rate          | Number of cache hits as a percentage of total cache requests per node. | sum by (couchbaseNode) ai\_model\_service\_gateway\_cache\_hits{databaseId="<databaseId>",tenantId="<tenantId>"} / (ai\_model\_service\_gateway\_cache\_hits{databaseId="<databaseId>",tenantId="<tenantId>"} + ai\_model\_service\_gateway\_cache\_misses{databaseId="<databaseId>",tenantId="<tenantId>"} \* 100) |
| Cache Hits              | Number of cache hits per node.                                         | sum by (couchbaseNode) (ai\_model\_service\_gateway\_cache\_hits{databaseId="<databaseId>",tenantId="<tenantId>"})                                                                                                                                                                                                  |
| Cache Misses            | Number of cache misses per node.                                       | sum by (couchbaseNode) (ai\_model\_service\_gateway\_cache\_misses{databaseId="<databaseId>",tenantId="<tenantId>"})                                                                                                                                                                                                |
| Cache Completion Tokens | Number of tokens generated from cache (response tokens) per node.      | sum by (couchbaseNode) (ai\_model\_service\_gateway\_cached\_completion\_tokens{databaseId="<databaseId>",tenantId="<tenantId>"})                                                                                                                                                                                   |
| CPU Usage               | CPU utilization percentage usage per node.                             | sum by (couchbaseNode) (node\_cpu\_util\_rate{databaseId="<databaseId>",tenantId="<tenantId>"} \* 100)                                                                                                                                                                                                              |
| Disk Usage              | Total disk space currently consumed on each node.                      | sum by (couchbaseNode) (node\_disk\_used{databaseId="<databaseId>",tenantId="<tenantId>"})                                                                                                                                                                                                                          |
| Error Rate Trends       | Number of queries that resulted in errors per second per node.         | sum by (couchbaseNode) (rate(ai\_model\_service\_gateway\_error\_count{databaseId="<databaseId>",tenantId="<tenantId>"}\[5m\]))                                                                                                                                                                                     |
| Error Count             | Number of queries that resulted in errors per node.                    | sum by (couchbaseNode) (ai\_model\_service\_gateway\_error\_count{databaseId="<databaseId>",tenantId="<tenantId>"})                                                                                                                                                                                                 |
| Guardrail Violations    | Number of guardrail violations detected per node.                      | sum by (couchbaseNode) (ai\_model\_service\_gateway\_guardrail\_violations{databaseId="<databaseId>",tenantId="<tenantId>"})                                                                                                                                                                                        |
| Processed Prompt Tokens | Number of tokens processed (prompt tokens) per node.                   | sum by (couchbaseNode) (ai\_model\_service\_gateway\_prompt\_tokens{databaseId="<databaseId>",tenantId="<tenantId>"})                                                                                                                                                                                               |
| API Requests            | Total number of API requests processed per node.                       | sum by (couchbaseNode) (ai\_model\_service\_gateway\_total\_requests\_count{databaseId="<databaseId>",tenantId="<tenantId>"})                                                                                                                                                                                       |
| Token Generation Rate   | Number of tokens generated (response tokens) per second per node.      | sum by (couchbaseNode) (rate(ai\_model\_service\_gateway\_completion\_tokens{databaseId="<databaseId>",tenantId="<tenantId>"}\[5m\]))                                                                                                                                                                               |

## [](#see-also)See Also

[View Monitoring Dashboards](../admin/monitor-dashboard.md)