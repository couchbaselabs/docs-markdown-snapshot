---
title: View Monitoring Dashboards
description: Couchbase Capella provides metrics for Workflows and the Model
  Service for you to discover and trend model performance, identify performance
  issues, and more.
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/admin/pages/monitor-dashboard.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:ai:admin:monitor-dashboard.adoc[]
---

[View original HTML](/ai/admin/monitor-dashboard.html)

# View Monitoring Dashboards

> Couchbase Capella provides metrics for Workflows and the Model Service for you to discover and trend model performance, identify performance issues, and more. 

You can use the metrics from the **Monitoring** dashboards for troubleshooting your AI Services. Use the dashboards to investigate intermittent issues with multi-metric views and adjustable timeframes.

Capella AI Services has the following real-time monitoring dashboards for:

* [Workflows](#workflow-metrics), such as:

  * [Unstructured Data Workflows](#unstructured-data)
  * [Structured Data Workflows](#structured-data)
* [Models](#model-llm-emb)

These monitoring dashboards show metric charts with the following elements:

| Element         | Description                                                                                                                           |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| **Metrics**     | Each monitoring dashboard has metric charts for every available metric.                                                               |
| **Time Range**  | The timeframe filters allow you to switch between preselected timeframes moving backward from the current time or a custom timeframe. |
| **Metric tile** | The Monitoring dashboards show each metric as a tile. A tile includes a title, a graph with labeled X and Y axis, and data lines.     |

## [](#workflow-metrics)View Workflow Metrics

The workflow dashboards include metrics for [Unstructured Data Workflows](#unstructured-data) and [Structured Data Workflows](#structured-data).

### [](#unstructured-data)View Unstructured Data Metrics

The **Unstructured Data** dashboard presents a general summary of the metrics, health status, and active alerts for your Unstructured Data Workflows. It presents metrics such as:

* KV operations, to identify patterns in data retrieval.
* Pages processed, to identify workload size and processing throughput.
* Documents processed, to identify ingestion volume.

To see your **Unstructured Data** workflow’s status and metrics:

1. Go to **AI Services** **Monitoring**.
2. Select **Unstructured Data**.
3. In the workflow list, select the **Workflow** you want to view metrics for.

You can adjust the metric charts by timeframe. For more information, see [Adjust Metrics](#use-metrics).

For more information about Workflows, see [Process Your Data For Capella AI Services](../build/vectorization-service/data-processing.md).

### [](#structured-data)View Structured Data Metrics

The **Structured Data** dashboard presents a general summary of the metrics, health status, and active alerts for your Structured Data Workflows. It presents metrics such as:

* Number of tokens processed, to identify processing volume.
* Number of requests, to identify workload.
* Average embedding response latency, to identify model performance and responsiveness.

To see your **Structured Data** Workflow’s status and metrics:

1. Go to **AI Services** **Monitoring**.
2. Click **Structured Data**.
3. In the workflow list, select the **Workflow** you want to view metrics for.

You can adjust the metric charts by timeframe. For more information, see [Adjust Metrics](#use-metrics).

For more information about Workflows, see [Process Your Data For Capella AI Services](../build/vectorization-service/data-processing.md).

## [](#model-llm-emb)View Model Metrics

The **Model** dashboard presents a general summary of your model’s metrics, health status, and active alerts. It presents metrics such as:

* CPU usage, to identify how much processing power the model is consuming.
* Guardrail violations, to identify when the model generates unsafe or undesired outputs.
* Cache completion tokens, to identify how often the model returns results from cache instead of generating new ones.

To see your model’s status and metrics:

1. Go to **AI Services** **Monitoring**.
2. Click **Model**.
3. In the **Model** list, select the model you want to view metrics for.

You can adjust the metric charts by timeframe. For more information, see [Adjust Metrics](#use-metrics).

For more information about models on Capella AI Services, see [Deploy Models with the Capella Model Service](../build/model-service/model-service.md).

## [](#use-metrics)Adjust Metrics

Each metric tile in any of the **Monitoring** dashboards shows you a chart representing data from the chosen timeframe.

### [](#timeframes)Choose Time Range

By default, the **Monitoring** dashboards display metrics from the past hour. Using the time range buttons, you can choose from the following preselected time ranges:

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
The dashboard automatically refreshes in the background for the new date.
3. Use the **To** date and time picker to update the end date and time.  
By default, the **To** date is the current date and time.
4. With a timeframe chosen, select a blank area of the **Monitoring** dashboard to close the open date and time picker.

For **Monitoring** dashboards, you can return to the default timeframe by selecting the **1hr** option.

### [](#chart-resolution)Chart Resolution

Capella draws metrics charts down to 60-second (1-minute) resolution. This resolution is available for graphs using the **30m**, **1h**, and **2h** timeframes.

When you select a longer timeframe, Capella automatically adjusts the chart data resolution. These chart data resolutions are:

* **1d** \- 360 seconds (6 minutes)
* **2d** \- 720 seconds (12 minutes)
* **7d** \- 2520 seconds (42 minutes)
* **30d** \- 10800 seconds (3 hours)

## [](#see-also)See Also

* [Monitoring Reference](../reference/monitoring-reference.md)