---
title: Manage Statistics
description: Statistics on Enterprise Analytics can be monitored; per database,
  per node, per service, and per cluster.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/manage/pages/manage-statistics/manage-statistics.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:manage:manage-statistics/manage-statistics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/manage/manage-statistics/manage-statistics.html)

# Manage Statistics

> Statistics on Enterprise Analytics can be monitored; per database, per node, per service, and per cluster. By means of Enterprise Analytics Web Console, appropriate combinations of statistics can be selected for display, across multiple interactive dashboards. 

## [](#understanding-statistics-management)Understanding Statistics Management

Enterprise Analytics provides statistics; which are updated continuously, and so always represent the current state of the cluster. Statistics refer to buckets, nodes, clusters, and services.

Statistics can be viewed by means of [Enterprise Analytics Web Console](#manage-statistics-with-the-ui), the Couchbase [CLI](#manage-statistics-with-the-cli), and the [REST API](#manage-statistics-with-the-rest-api).

## [](#manage-statistics-with-the-ui)Manage Statistics with the UI

Users with the **Full Admin** role can assemble statistics as _groups_ of _charts_, on the **Dashboard** of Enterprise Analytics Web Console. This is visible by default after login and can at any time be displayed by navigating to the **Dashboard** section in the navigation bar.

Initially, prior to any definitions having been made, the **Dashboard** displays a blank interface ready for chart configuration.

At the bottom of the **Dashboard**, numbers are displayed to indicate which cluster-nodes are **active**, **failed-over**, **pending rebalance**, and **inactive**. The services present on the cluster are also indicated.

The **Dashboard** is divided into two main sections: the upper section contains **Stat Interval** and **Nodes**, while the lower section displays the charts themselves.

Additional information can be displayed by clicking on the **Node Resources** and **Enterprise Analytics** controls.

### [](#dashboard-access)Dashboard Access

All chart-content is provided by _Nodes_. Users whose roles allow them both to access Enterprise Analytics Web Console _and_ see administrative details on one or more nodes are able to see the default chart-content for those nodes. For example, the **Full Admin**, **Cluster Admin**, **Read Only Admin**, **Local User Security Admin**, and **External User Security Admin** roles permit display of charts for all nodes defined on the cluster.

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

## [](#manage-statistics-with-the-cli)Manage Statistics with the CLI

On the command-line, statistics can be managed with the [cbstats](../../../../server/current/cli/cbstats-intro.md) tool. This allows a bucket to be specified as the source of statistics. Port 11210 must be specified.

For example, the `memory` option returns statistics on memory for the specified bucket:

/opt/enterprise-analytics/bin/cbstats
localhost:11210 memory

If successful, the command returns the following:

 bytes:                     38010040
 ep_blob_num:               31591
 ep_blob_overhead:          2159511
 ep_item_num:               3584
 ep_kv_size:                24495752
 ep_max_size:               104857600
 ep_mem_high_wat:           89128960
 ep_mem_high_wat_percent:   0.85
 ep_mem_low_wat:            78643200
 ep_mem_low_wat_percent:    0.75
 ep_oom_errors:             0
 ep_overhead:               5194392
 ep_storedval_num:          31591
 ep_storedval_overhead:     2159511
 ep_storedval_size:         2527280
 ep_tmp_oom_errors:         0
 ep_value_size:             22306240
 mem_used:                  38010040
 mem_used_estimate:         38010040
 mem_used_merge_threshold:  524288
 total_allocated_bytes:     67864856
 total_fragmentation_bytes: 4220648
 total_heap_bytes:          111050752
 total_metadata_bytes:      6175864
 total_resident_bytes:      103907328
 total_retained_bytes:      18448384

The `vbucket` option returns statistics for all vBuckets for the specified bucket. The output can be filtered, so that a particular vBucket can be examined:

/opt/enterprise-analytics/bin/cbstats
localhost:11210 vbucket | grep 1014

This produces the following output:

 vb_1014: active

For more information about available options, see server:cli:cbstats-intro.adoc\[cbstats\].

## [](#manage-statistics-with-the-rest-api)Manage Statistics with the REST API

The Couchbase-Server REST API allows statistics to be gathered either from the _cluster_ or from the _individual bucket_.