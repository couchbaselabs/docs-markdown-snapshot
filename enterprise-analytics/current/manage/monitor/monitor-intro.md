[View original HTML](/enterprise-analytics/current/manage/monitor/monitor-intro.html)

> Monitoring of Enterprise Analytics can be performed by means of Enterprise Analytics Web Console, the CLI, and the REST API. 

This page summarizes the options available for monitoring Enterprise Analytics; and provides links to more detailed interface-descriptions.

## [](#monitoring-with-the-ui)Monitoring with the UI

Couchbase-Server statistics can be monitored by means of Enterprise Analytics Web Console.

Users with the **Full Admin** or **Bucket Admin** role can assemble statistics as _groups_ of _charts_, on the **Dashboard** of Enterprise Analytics Web Console. The Dashboard is visible by default after login and can be accessed at any time by clicking on the **Dashboard** tab in the left-hand navigation bar of the Enterprise Analytics Web Console.

When you first access the Dashboard, before any statistics groups or charts have been defined, you’ll see an empty dashboard interface with options to add new chart groups. The interface provides controls for creating custom monitoring displays and organizing statistics into meaningful collections.

From this point, charts can be assembled interactively, and statistics for Enterprise Analytics and all services thereby monitored. For step-by-step instructions, see [Manage Statistics](../manage-statistics/manage-statistics.md).

## [](#monitoring-with-the-rest-api)Monitoring with the REST API

Enterprise Analytics provides a REST API for [Getting Cluster Statistics](../../reference/rest-statistics.md). Statistics are retrieved based on the specification of one or more _metrics_. Optionally, the statistics can be further defined through the specifying of a _function_; and/or _labels_ with values. An instance of _Prometheus_ runs on each node of the cluster; and the metrics for each node are duly stored in that node’s instance of Prometheus.

For a complete list of metrics, see the [Metrics Reference](../../metrics-reference/metrics-reference.md).

## [](#monitoring-couchbase-metrics-with-prometheus)Monitoring Couchbase Metrics with Prometheus

It’s also possible to set up a [Prometheus](https://prometheus.io/) monitor to consume metrics data from a Couchbase cluster. You can find an introduction on how to do this in [Configure Prometheus to Collect Couchbase Metrics](set-up-prometheus-for-monitoring.md)