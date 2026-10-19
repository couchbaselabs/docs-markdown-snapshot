---
title: Metrics Dashboard
description: Statistics on Operational Insights can be monitored; per database,
  per node, per service, and per cluster.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/manage/pages/manage-statistics/manage-statistics.adoc
  xref: xref:enterprise-analytics:manage:manage-statistics/manage-statistics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/manage/manage-statistics/manage-statistics.html)

# Metrics Dashboard

> Statistics on Operational Insights can be monitored; per database, per node, per service, and per cluster. By means of Operational Insights Web Console, appropriate combinations of statistics can be selected for display, across multiple interactive dashboards. 

## [](#understanding-statistics-management)Understanding Statistics Management

Operational Insights provides statistics; which are updated continuously, and so always represent the current state of the cluster. Statistics refer to buckets, nodes, clusters, and services.

Statistics can be viewed by means of the [Operational Insights Web Console](#manage-statistics-with-the-ui).

## [](#manage-statistics-with-the-ui)Manage Statistics with the UI

Users with the **Full Admin** role can assemble statistics as _groups_ of _charts_, on the **Dashboard** of Operational Insights Web Console. This is visible by default after login and can at any time be displayed by navigating to the **Dashboard** section in the navigation bar.

Initially, prior to any definitions having been made, the **Dashboard** displays a blank interface ready for chart configuration.

At the bottom of the **Dashboard**, numbers are displayed to indicate which cluster-nodes are **active**, **failed-over**, **pending rebalance**, and **inactive**. The services present on the cluster are also indicated.

The **Dashboard** is divided into two main sections: the upper section contains **Stat Interval** and **Nodes**, while the lower section displays the charts themselves.

Additional information can be displayed by clicking on the **Node Resources** and **Operational Insights** controls.

### [](#dashboard-access)Dashboard Access

All chart-content is provided by _Nodes_. Users whose roles allow them both to access Operational Insights Web Console _and_ see administrative details on one or more nodes are able to see the default chart-content for those nodes. For example, the **Full Admin**, **Cluster Admin**, **Read Only Admin**, **Local User Security Admin**, and **External User Security Admin** roles permit display of charts for all nodes defined on the cluster.

### [](#dashboard-controls)Dashboard Controls

In the upper part of the screen, the following controls are available:

#### [](#stat-interval-control)Stat Interval Control

The first control reads **Stat Interval**. When clicked, it displays a dropdown menu with the following time granularity options:

* Minute
* Hour
* Day
* Week
* Month

This control allows you to specify the time interval for statistical data aggregation and display.

#### [](#node-selection-control)Node Selection Control

The second control reads **Nodes** and indicates in parentheses the number of nodes currently in the cluster. Click on this control to display the individual nodes available for selection.

The default selection allows data from all server nodes to be displayed simultaneously. By selecting an individual node from the dropdown menu, the displayed data is restricted to that corresponding to the selected node.

#### [](#working-with-charts)Working with Charts

Charts display statistical data with colored lines representing different metrics for each cluster node. For example, CPU statistics may show blue and orange lines providing the **CPU** statistic for each of the cluster's nodes.

##### [](#maximizing-charts)Maximizing Charts

To improve readability, click on any chart to maximize it. When maximized, charts provide:

* A detailed view of the selected statistics.
* A vertically minimized version of the chart at the bottom of the display.
* A magnifying-glass icon for time period selection.

##### [](#time-period-selection)Time Period Selection

In the maximized view, you can select specific time periods by:

1. Clicking at a starting point on the horizontal axis in the minimized chart.
2. Dragging the cursor left or right to select a time period.
3. The main chart will update to reflect the selected time period.

##### [](#time-granularity-adjustment)Time Granularity Adjustment

You can modify the time granularity for display by:

1. Accessing the control at the upper-center of the maximized chart.
2. Changing the time unit (for example, from **hour** to **minute**).
3. The chart will update to show data at the new granularity.

##### [](#minimizing-charts)Minimizing Charts

To return a maximized chart to its normal size, click the 'X' icon at the upper-right of the maximized chart view.

## [](#see-also)See Also

* [Monitoring Overview](../monitor/monitor-intro.md)
* [Configure Prometheus to Collect Couchbase Metrics](../monitor/set-up-prometheus-for-monitoring.md)
* [Alert Reference](../../reference/alerts.md)
* [Statistics](../../reference/rest-statistics.md)
* [Troubleshooting](../troubleshoot/troubleshoot.md)