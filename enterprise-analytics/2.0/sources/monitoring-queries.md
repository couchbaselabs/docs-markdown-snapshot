---
title: Monitoring Queries
description: This page explains how to monitor queries in Couchbase Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sources/pages/monitoring-queries.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/2.0/sources/monitoring-queries.html)

# Monitoring Queries

The Monitor screen is a UI that allows you to monitor the current state of the Analytics Service.

To display the Monitor, in the UI, select the **Workbench** tab and click **monitor** at the top of the page

The Monitor screen shows the analytics queries that are Active or currently running and Completed or recently run. Statistics information for the Analytics Service is displayed at the bottom of the page. Different information may be shown depending on the user’s access control role.

The information about these queries is automatically updated every 5 seconds. To freeze the display updates, click **pause**. When paused, a **resume** button becomes available to let you restart automatic updates. You can sort the query information table by clicking on any of the column headers.

## [](#active-queries)Active Queries

The **Active Enterprise Analytics Queries** page displays the currently running queries.

For each query, this page shows the query syntax, the node address where the query is running, the duration, the current state of the query, and the user who initiated the query. Click **Edit** to edit a particular query in the **Workbench** tab. To cancel a long running query, click **Cancel**.

To display the Active Enterprise Analytics Queries page, make sure the Monitor screen is displayed, then if necessary click **Active**.

## [](#completed-queries)Completed Queries

The **Completed Enterprise Analytics Queries** page shows a table of completed queries.

For each query, this page shows the query syntax, the node address where the query ran, the duration, the final state of the query, the timestamp when the query was run, and the user who initiated the query. Click **Edit** to edit a particular query in the **Workbench** tab.

To display the Completed Enterprise Analytics Query page, make sure the Monitor screen is displayed, and then if necessary click **Completed**.