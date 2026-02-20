---
title: Monitor a Capella Analytics Cluster
description: Monitor your Capella Analytics cluster through metrics, queries,
  activity logs, and alerts.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/monitoring/monitor-cluster.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:analytics:admin:monitoring/monitor-cluster.adoc[]
---

[View original HTML](/analytics/admin/monitoring/monitor-cluster.html)

# Monitor a Capella Analytics Cluster

> Monitor your Capella Analytics cluster through metrics, queries, activity logs, and alerts. 

## [](#cluster-metrics)Cluster Metrics

Cluster metrics allow you to monitor the current and past performances of your Capella Analytics cluster. You can view these metrics using the Monitoring dashboard.

The Monitoring dashboard lets you access a customizable collection of metrics to track and chart your cluster data over specified timeframes.

With the Monitoring dashboard, you can:

* Investigate issues and identify runtime outliers
* Customize the dashboard to only track specific metrics
* View all of those metrics in one place

For more information about the Metrics dashboard, see [View Metrics for a Cluster](view-metrics.md).

## [](#query-monitoring)Query Monitoring

Query monitoring allows you to monitor query requests that are actively running or that have already been completed in your Capella Analytics cluster.

You can use SQL++ queries to analyze these query requests and improve your cluster’s performance and efficiency.

For more information about query monitoring, see [Use Queries to Monitor a Cluster](monitor-query.md).

## [](#activity-logs)Activity Logs

Activity logs provide a complete timeline of user and control plane system events happening in your Capella Analytics cluster.

> [!NOTE]
> Activity logs do not include events involving activities caused to the data in your cluster.

Each event in an activity log includes a summary of the event, the severity of the event, the resource affected by the event, and the time at which the event occurred.

You can filter your activity log by cluster, severity, tag, and timeframe to narrow down the events you’re looking for.

For more information about activity logs, including event severity and event tags, see [View the Activity Log for a Cluster](view-activity.md).

## [](#alerts)Alerts

Alerts notify you when events with a warning or critical severity level occur in your Capella Analytics cluster.

You can view alerts in the UI, or turn on notifications to receive email alerts. The activity logs keep a record of all current and past alerts.

For more information about alerts, see [Receive Alerts for a Cluster](receive-alerts.md).

## [](#see-also)See Also

* [Alert Reference](../../reference/alerts.md)
* [Metrics Reference](#reference:metrics.adoc)