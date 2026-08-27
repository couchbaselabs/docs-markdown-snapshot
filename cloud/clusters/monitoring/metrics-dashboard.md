---
title: View Monitoring Dashboards
description: Couchbase Capella provides monitoring dashboards with metrics for
  each cluster so you can view and monitor cluster performance.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/monitoring/metrics-dashboard.adoc
  xref: xref:cloud:clusters:monitoring/metrics-dashboard.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/monitoring/metrics-dashboard.html)

# View Monitoring Dashboards

> Couchbase Capella provides monitoring dashboards with metrics for each cluster so you can view and monitor cluster performance. 

> [!NOTE]
> The [Metrics Explorer](#metrics-explorer-dashboard) dashboard is still available for you to view cluster metrics. Use this dashboard to add or remove specific metrics according to your monitoring needs.

The metrics available on the **Monitoring** dashboards provide insight into your cluster's performance and can help identify runtime outliers. These dashboards can help you investigate intermittent issues with multi-metric views and adjustable timeframes.

Capella has the following real-time monitoring dashboards:

* [Cluster Overview](#cluster-overview)
* [Data Service](#data-service)
* [Index Service](#index-service)
* [Query Service](#query-service)
* [Node Metrics](#node-metrics)
* [Metrics Explorer](#metrics-explorer-dashboard)

These monitoring dashboards show metric charts with the following elements:

| Element         | Description                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Metrics**     | Each monitoring dashboard has metric charts for every available metric. In the **Metrics Explorer** dashboard, use the **Metrics** list to add or remove a metric by selecting its entry.                                                                                                                                                                                                          |
| **Time Range**  | The timeframe filters allow you to switch between preselected timeframes moving backward from the current time or a custom timeframe. The **Auto-refresh** option is off by default. When turned on, it refreshes the dashboard with the most recent data based on the chosen refresh rate—**1m** or **2m**. Auto-refresh is only available with the **30m**, **1h**, or **2h** timeframe options. |
| **Metric tile** | The Monitoring dashboards show each metric as a tile. A tile includes a title, a graph with labeled X and Y axis, and data lines.                                                                                                                                                                                                                                                                  |

## [](#cluster-overview)View Cluster Overview

The **Cluster Overview** dashboard presents a general summary of your cluster's metrics, health status, and configuration settings. It displays key cluster workload insights, along with summaries from Health Advisor and the Activity Log.

To get an overview of your cluster's status and metrics, go to **Monitoring** **Cluster Overview**.

You can adjust the metric charts by timeframe. For more information, see [Adjust Metrics](#use-metrics).

For detailed metrics by Service and node, see the [Workload Dashboards](#workload-monitoring).

## [](#workload-monitoring)View Workload Dashboards

The **Workload Monitoring** dashboards provide you with metrics specific to the Services deployed in your cluster, as well as the nodes they run on. You can monitor the performance and resource usage of individual Services and nodes to better understand their contribution on the overall health and efficiency of your cluster.

The metrics available are dependent on the Services running in your cluster. For example, if your cluster only has the Data Service, then only Data Service related metrics are available.

You can explore the breakdown of these metrics in following dashboards:

* [Data Service](#data-service)
* [Index Service](#index-service)
* [Query Service](#query-service)
* [Node Metrics](#node-metrics)

Use the data from these dashboards to support your cluster's performance, troubleshoot failures, and optimize resource allocation.

### [](#data-service)Data Service

The **Data Service** dashboard provides a focused view of bucket health and resource usage. It presents metrics such as:

* Latency, to identify bottlenecks.
* Data read/write throughput and failures, to measure workload.
* Memory and disk usage, to identify resource availability.

Go to **Monitoring** **Data Service** for the full list of data metrics.

You can adjust the metric charts by timeframe. For more information, see [Adjust Metrics](#use-metrics).

### [](#index-service)Index Service

The **Index Service** dashboard offers metrics related to index performance and resource usage. It presents metrics such as:

* Index mutation lag, to detect indexing delays.
* Cache hits and misses, to identify index efficiency.
* Index resident ratio, to identify in-memory data caching.

Go to **Monitoring** **Index Service** for the full list of index metrics.

You can adjust the metric charts by timeframe. For more information, see [Adjust Metrics](#use-metrics).

### [](#query-service)Query Service

The **Query Service** dashboard offers metrics related to query errors and slow queries. It presents metrics such as:

* Average query request and execution time, to measure application responsiveness.
* Query result size, to monitor data volume.
* Slow queries, to identify query performance issues.

Go to **Monitoring** **Query Service** for the full list of query metrics.

You can adjust the metric charts by timeframe. For more information, see [Adjust Metrics](#use-metrics).

#### [](#slow-queries)Slow Queries

Couchbase Capella categorizes slow queries as those running [longer than 1000ms](../../../server/current/n1ql/n1ql-manage/monitoring-n1ql-query.md#completed-threshold). Slow queries can indicate insufficient cluster resources, poor indexing, or query optimization issues.

Data on slow queries is sourced from [system keyspaces](../../n1ql/n1ql-intro/sysinfo.md#querying-keyspaces), which provide real-time monitoring details and statistics about individual queries and the Query Service. This data is transient, tied to the current Query Service instance and not saved to disk. If the Service restarts, this data may change or be lost. For more information, see [Manage and Monitor Queries](../../n1ql/n1ql-manage/monitoring-n1ql-query.md).

> [!NOTE]
> Viewing Slow Queries
> 
> Capella provides built-in safeguards and optimizations for **Slow Queries** and their data in the **Query Service** dashboard. This helps the data remain efficient and responsive, even under heavy workloads. If you do not see any **Slow Queries**, it may be because of 1 of the following limits:
> 
> * Capella only retains the most recent [4,000 completed requests](../../../server/current/n1ql/n1ql-manage/monitoring-n1ql-query.md#completed-limit) with run times longer than 1000 ms. If no slow query data is available, your queries might not meet the criteria or your filter settings need adjustment.
> * Capella sets a default query memory quota of 30 MB for the **Slow Queries** displayed in the dashboard. If you encounter a query memory quota error, it indicates that the system queries used to populate **Slow Queries** in the dashboard require more memory than the current limit allows. To adjust this limit:
> 
>   * If your cluster has enough available memory, try doubling the current limit. For example, you can adjust it from 30 MB to 60 MB.
>   * If your query nodes are operating under memory constraints, try increasing the limit incrementally. For example, you can increase the limit by 10 MB at a time, until the **Slow Queries** load and display in the dashboard.

### [](#node-metrics)Node Metrics

The **Node Metrics** dashboard provides a per-node view of key metrics for all the nodes in your cluster. It presents metrics such as:

* CPU utilization, to monitor processing load.
* Disk IOPS, to measure storage performance.
* Network bytes, to track received and transmitted data.

Go to **Monitoring** **Node Metrics** for the full list of node metrics.

You can adjust the metric charts by timeframe. For more information, see [Adjust Metrics](#use-metrics).

## [](#metrics-explorer-dashboard)View Metrics Explorer

The **Metrics Explorer** dashboard provides a customizable collection of Service and node level metrics of your operational cluster.

You can select from a list of available cluster metrics, including those for your cluster's Services and nodes. Adjust your dashboard by adding or removing the metrics that suit your specific monitoring needs. You can customize the view to support detailed performance analysis and targeted troubleshooting workflows.

You can adjust the charts by timeframe and resolution. For more information, see [Adjust Metrics](#use-metrics).

### [](#add-metrics)Add Metrics

You can customize the **Metrics Explorer** dashboard to only display the metrics you want to track.

To add metrics to the **Monitoring** dashboard:

1. In the **Metrics** list, select the metric you want to display.  
Repeat this step to add multiple metrics.

### [](#remove-metrics)Remove Metrics

To remove metrics from your **Metrics Explorer** dashboard:

* On the metric tile you want to remove, click **Close** ().

Metrics appear highlighted when on the dashboard.

### [](#chart-resolution)Chart Resolution

> [!TIP]
> Capella draws metrics charts down to 60-second (1-minute) resolution. This resolution is available for graphs using the **30m**, **1h**, and **2h** timeframes.
> 
> When you select a longer timeframe, Capella automatically adjusts the chart data resolution. These chart data resolutions are:
> 
> * **1d** \- 360 seconds (6 minutes)
> * **2d** \- 720 seconds (12 minutes)
> * **7d** \- 2520 seconds (42 minutes)
> * **30d** \- 10800 seconds (3 hours)

Moving your mouse pointer over a metric chart provides date, time, and resource information for the part of the chart you're pointing at. You can also zoom in on areas of a chart by clicking and dragging your pointer over the region you want to focus on.

Zooming in on a chart updates the [timeframe](#timeframes) to match your current selection for all metrics on the dashboard.

## [](#use-metrics)Adjust Metrics

Each metric tile in any of the **Monitoring** dashboards shows you a chart representing data from the chosen timeframe.

### [](#timeframes)Choose Time Range

By default, the **Workload Monitoring** dashboards displays metrics from the past hour, while the **Metrics Explorer** dashboard shows metrics from the past day. Using the time range buttons, you can choose from the following preselected time ranges:

* 30 minutes
* 1 hour
* 2 hour
* 1 day
* 2 days
* 7 days
* 30 days

You can also choose to show data from a timeframe you specify. Specifying a timeframe is most helpful when examining metrics over an event.

To specify a timeframe:

1. Click the clock icon ().
2. Select the **From** date and time picker and choose a date and time from when you want to start showing activity.  
The **Metrics Explorer** dashboard automatically refreshes in the background for the new date.
3. Use the **To** date and time picker to update the end date and time.  
By default, the **To** date is the current date and time.
4. With a timeframe chosen, select a blank area of the **Metrics Explorer** dashboard to close the open date and time picker.

For **Workload Monitoring** dashboards, you can return to the default timeframe by selecting the **1hr** option. For the **Metrics Explorer** dashboard, you can return to the default timeframe by selecting the **1d** option.

## [](#see-also)See Also

* [View Health Advisor](health-advisor.md)
* [View Activity Logs](activity-log.md)
* [Receive Alerts](alerts.md)