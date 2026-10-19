---
title: Monitoring Queries
description: This page explains how to monitor queries in Operational Insights.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sources/pages/monitoring-queries.adoc
  xref: xref:enterprise-analytics:sources:monitoring-queries.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sources/monitoring-queries.html)

# Monitoring Queries

The Monitor screen is a UI that allows you to monitor the current state of the Analytics Service.

To display the Monitor, in the UI, select **Workbench** in the navigation bar and click the **Monitor** tab at the top of the page.

The Monitor screen shows the analytics queries that are Active or currently running and Completed or recently run. Statistics information for the Analytics Service is displayed at the bottom of the page. Different information may be shown depending on the user's access control role.

The information about these queries is automatically updated every 5 seconds. To freeze the display updates, click **pause**. When paused, a **resume** button becomes available to let you restart automatic updates. You can sort the query information table by clicking on any of the column headers.

## [](#active-queries)Active Queries

The **Active Requests** page displays the currently running queries.

For each query, this page shows the query syntax, the node address where the query is running, the duration, the current state of the query, and the user who initiated the query. Click **Edit** to edit a particular query in the **Workbench** tab. To cancel a long running query, click **Cancel**.

To display the **Active Requests** page, make sure the Monitor screen is displayed, then if necessary click **Active Requests**.

## [](#completed-queries)Completed Queries

The **Completed Requests** page shows a table of completed queries.

For each query, this page shows the query syntax, the node address where the query ran, the duration, the final state of the query, the timestamp when the query was run, and the user who initiated the query. Click **Edit** to edit a particular query in the **Workbench** tab.

To display the **Completed Requests** page, make sure the Monitor screen is displayed, and then if necessary click **Completed Requests**.

## [](#open-queries)Open Queries

The **Open Requests** page shows a table of open queries. Open queries include all active queries and completed asynchronous queries, until they're explicitly discarded or reach their TTL.

For each query, this page shows the query syntax, the node address where the query ran, the duration, the final state of the query, the timestamp when the query was run, and the user who initiated the query. Click **Edit** to edit a particular query in the **Workbench** tab.

To display the **Open Requests** page, make sure the Monitor screen is displayed, then if necessary click **Open Requests**.

To discard a completed asynchronous query, you must use the Operational Insights Service REST API. For more information, see [Discard Request Result](../analytics-rest-service/index.md#operation/delete%5Frequest%5Fresult).