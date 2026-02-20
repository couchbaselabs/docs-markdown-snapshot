---
title: Monitoring Queries
description: How to monitor queries in Couchbase Analytics.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.6/modules/analytics/pages/monitor.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:analytics:monitor.adoc[]
---

[View original HTML](/server/7.6/analytics/monitor.html)

# Monitoring Queries

The Monitor screen is a UI that allows you to monitor the current state of the Analytics service.

To display the Monitor, from **Couchbase Web Console** \> **Analytics**, click the **Monitor** tab at the top of the page.

![monitor](_images/monitoring.png) 

The Monitor screen shows the analytics queries that are Active (currently running) and Completed (recently run). Statistics information for the analytics service is displayed at the bottom of the page. Different information may be shown depending on the user’s access control role.

The information about these queries is automatically updated every 5 seconds. To freeze the display updates, click **pause** located above the query table, next to the page heading. When paused, a **resume** button becomes available to let you restart automatic updates. You can sort the query information table by clicking on any of the column headers.

## [](#active-queries)Active Queries

The **Active Analytics Queries** page displays the currently running queries.

![active analytics queries](_images/monitoring-active.png) 

For each query, this page shows the query syntax, the node address where the query is running, the duration, the current state of the query, and the user who initiated the query. Click the **Edit** link to edit a particular query in the [Workbench](run-query.md#Using%5Fanalytics%5Fworkbench). To cancel a long running query, click the **Cancel** link located on the right side of the row.

To display the Active Analytics Queries page, make sure the Monitor screen is displayed, then if necessary click the **Active** button.

## [](#completed-queries)Completed Queries

The **Completed Analytics Queries** page shows a table of completed queries.

![completed analytics queries](_images/monitoring-completed.png) 

For each query, this page shows the query syntax, the node address where the query ran, the duration, the final state of the query, the timestamp when the query was run, and the user who initiated the query. Click the **Edit** link to edit a particular query in the [Workbench](run-query.md#Using%5Fanalytics%5Fworkbench).

To display the Completed Analytics Query page, make sure the Monitor screen is displayed, and then if necessary click the **Completed** button.