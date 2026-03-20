---
title: View Metrics for a Capella Analytics Cluster
description: Capella Analytics provides metrics that allow you to monitor your clusters.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/monitoring/view-metrics.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:analytics:admin:monitoring/view-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/admin/monitoring/view-metrics.html)

# View Metrics for a Capella Analytics Cluster

> Capella Analytics provides metrics that allow you to monitor your clusters. 

You can use the Capella Analytics Monitoring dashboard to access a customizable collection of metrics and gain insight into the performance of your cluster.

With the Monitoring dashboard, you can:

* Investigate issues and identify runtime outliers
* Customize the dashboard to only track specific metrics
* View all of those metrics in one place

The Monitoring dashboard includes the following elements:

| Element         | Description                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Metrics**     | The metrics list includes every metric available for Capella Analytics clusters. You can select metrics to add or remove them from your dashboard.                                                                                                                                                                                                                                                   |
| **Timeframe**   | The timeframe filter lets you switch between preselected timeframes or set your own custom timeframe. By default, the **Auto refresh** option is turned off. When turned on, it refreshes the dashboard with the most recent data based on the the 1-minute or 2-minute refresh rate you choose. The auto-refresh feature is only available with the 30-minute, 1-hour, or 2-hour timeframe options. |
| **Metric tile** | The tiles that populate when you choose metrics from the metrics list.                                                                                                                                                                                                                                                                                                                               |

## [](#view-dashboard)Monitor Metrics in the Monitoring Dashboard

To monitor your metrics in the Monitoring dashboard:

1. In your Capella Analytics cluster, go to **Monitoring**.
2. Select the metric you want to monitor from the **Metrics** drop-down. For a list of all metrics available, see [available metrics.](#available-metrics)
3. Select a timeframe to apply to the metric. You can choose one of the predetermined timeframes, or click  to set a custom timeframe. The dashboard then populates a metric tile with information about the metric and timeframe you selected.

After you have populated the dashboard with a metric tile, you can view details about that metric:

* Hold the mouse pointer over a specific part of the metric chart to display information about its date, time, and resources.
* Hold and drag the mouse pointer over a timeframe on the chart to zoom in on details about that specific timeframe. Doing this updates the timeframe for all metric tiles on your dashboard.

> [!TIP]
> Capella Analytics draws metrics charts down to 60-second (1-minute) resolution. This resolution is available for charts using the **30m**, **1h**, and **2h** timeframes.
> 
> When you select a longer timeframe, Capella Analytics automatically updates the chart data resolution to the following:
> 
> * **1d** down to 360 seconds (6 minutes) resolution
> * **2d** down to 720 seconds (12 minutes) resolution
> * **7d** down to 2520 seconds (42 minutes) resolution
> * **30d** down to 10800 seconds (3 hours) resolution

### [](#available-metrics)Available Metrics

The following metrics are available in the Capella Analytics Monitoring dashboard:

| Metric                                   | Description                                                                                                                     |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Connections                              | The number of connections to the cluster.                                                                                       |
| CPU Utilization by Node                  | The CPU utilization % by node.                                                                                                  |
| Ingested Bytes Rate by Link/Bucket       | The per second rate of incoming bytes ingested by Analytics, averaged over the last five minutes by link and bucket.            |
| Total Ingested Bytes Rate by Link/Bucket | The total number of incoming bytes ingested by Analytics by link and bucket.                                                    |
| Linked Ops Rate by Link/Bucket           | The per second rate of linked record operations processed by Analytics, averaged over the last five minutes by link and bucket. |
| Total Linked Ops Rate by Link/Bucket     | The total number of linked record operations processed by Analytics by link and bucket.                                         |
| Memory Available by Node                 | The amount of memory available by node.                                                                                         |
| Parse Failure Rate by Link/Bucket        | The per second rate of record parsing failures from linked items, averaged over the last five minutes by link and bucket.       |
| Total Parse Failure Rate by Link/Bucket  | The total number of record parsing failures from linked items.                                                                  |
| Read Rate by Node                        | The per second rate at which disk bytes are read for the Analytics Service, averaged over the last five minutes by node.        |
| Write Rate by Node                       | The per second rate at which disk bytes are written for the Analytics Service, averaged over the last five minutes by node.     |
| System Load per Node                     | The system workload by node.                                                                                                    |
| Total Requests per Second                | The total number of received Analytics requests for the entire cluster over the last five minutes.                              |
| Total Requests per Second by Node        | The total number of received Analytics requests by node over the last five minutes.                                             |

## [](#see-also)See Also

* [View the Activity Log for a Cluster](view-activity.md)
* [Receive Alerts for a Cluster](receive-alerts.md)