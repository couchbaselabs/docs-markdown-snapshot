---
title: Monitor
description: Monitoring of Couchbase Server can be performed by means of
  Couchbase Web Console, the CLI, and the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/manage/pages/monitor/monitor-intro.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:manage:monitor/monitor-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/manage/monitor/monitor-intro.html)

# Monitor

> Monitoring of Couchbase Server can be performed by means of Couchbase Web Console, the CLI, and the REST API. 

This page summarizes the options available for monitoring Couchbase Server and provides links to more detailed interface-descriptions.

## [](#monitoring-with-the-ui)Monitoring with the UI

Couchbase-Server statistics can be monitored by means of Couchbase Web Console.

Users with the **Full Admin** or **Bucket Admin** role can assemble statistics as _groups_ of _charts_, on the **Dashboard** of Couchbase Web Console. This is visible by default after login; and can at any time be displayed by left-clicking on the **Dashboard** tab, in the left-hand navigation bar:

Note that the UI returns the last 30 days of statistics.

![DBaccessDB](../_images/manage-statistics/DBaccessDB.png) 

Initially, prior to any definitions having been made, the **Dashboard** appears as follows:

![DBblankInitial](../_images/manage-statistics/DBblankInitial.png) 

From this point, charts can be assembled interactively, and statistics for Couchbase Server and all services thereby monitored. For step-by-step instructions, see [Manage Statistics](../manage-statistics/manage-statistics.md).

## [](#monitoring-with-cbstats)Monitoring with `cbstats`

The `cbstats` tool provides Data-Service statistics, for an individual, specified node. The complete interface for `cbstats` is documented in [cbstats](../../cli/cbstats-intro.md).

## [](#monitoring-with-the-rest-api)Monitoring with the REST API

Couchbase Server provides a REST API for [Getting Cluster Statistics](../../rest-api/rest-statistics.md). Statistics are retrieved based on the specification of one or more _metrics_. Optionally, the statistics can be further defined through the specifying of a _function_; and/or _labels_ with values. An instance of _Prometheus_ runs on each node of the cluster, and the metrics for each node are duly stored in that node's instance of Prometheus.

For a complete list of metrics, see the [Metrics Reference](../../metrics-reference/metrics-reference.md).

## [](#additional-monitoring-options)Additional Monitoring Options

Statistics for the Index Service can be managed by means of Couchbase Web Console: this is described in [Monitor Indexes](monitoring-indexes.md).

The monitoring of statistics related to the Query Service is described in [Manage and Monitor Queries](../../n1ql/n1ql-manage/monitoring-n1ql-query.md).

The progressive desynchronization of nodes whose clock has been previously synchronized can be monitored, as described in [Monitor Clock Drift](xdcr-monitor-timestamp-conflict-resolution.md).

## [](#monitoring-couchbase-metrics-with-prometheus)Monitoring Couchbase Metrics with Prometheus

It's also possible to set up a [Prometheus](https://prometheus.io/) monitor to consume metrics data from a Couchbase cluster. You can find an introduction on how to do this in [Configure Prometheus to Collect Couchbase Metrics](set-up-prometheus-for-monitoring.md)