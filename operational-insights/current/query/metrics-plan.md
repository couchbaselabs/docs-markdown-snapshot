---
title: View Query Metrics or Plan
description: The workbench for Operational Insights provides metrics for each
  query you run, and a detailed query plan in both text and graphical format.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/query/pages/metrics-plan.adoc
  xref: xref:enterprise-analytics:query:metrics-plan.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/query/metrics-plan.html)

# View Query Metrics or Plan

> The workbench for Operational Insights provides metrics for each query you run, and a detailed query plan in both text and graphical format. 

## [](#prerequisites)Prerequisites

To use the Operational Insights UI, you need the `**Operational Insights Access**` role along with specific privileges.

## [](#review-query-metrics)Review Query Metrics

When a query finishes, metrics for that query appear on the workbench between the query editor and the query results panes. The metrics are:

* **elapsed** — Shows the overall query time.
* **execution** — Shows the query execution time.
* **waiting in queue** — Shows the query wait time in the queue before beginning execution.
* **docs scanned** — Shows the number of scanned JSON documents.
* **docs returned** — Shows the number of returned JSON documents.
* **size** — Shows the size of the query results, in bytes.

## [](#plan)View the Query Plan and Plan Text

When you execute a query from the Workbench, the plan is automatically returned as part of the response.

You can view the query plan in the query results pane: select the **Plan** tab.

The **Plan** tab presents the query execution plan in a graphical format.

The **Plan Text** tab presents the query execution plan in JSON format.

Operational Insights uses rule-based optimization to query your collections until you run an `ANALYZE COLLECTION` statement on each collection involved in a query. The `ANALYZE` statement samples the data in a collection so that cost-based optimization (CBO) can be applied. As the data in a collection changes, you can run `ANALYZE COLLECTION` periodically to update the information used for CBO.

## [](#see-also)See Also

* [Query and Explore with the Workbench](workbench.md)
* [Cost-Based Optimizer](../sqlpp/5b%5Fcbo.md)
* [About SQL++](../sqlpp/1%5Fintro.md)