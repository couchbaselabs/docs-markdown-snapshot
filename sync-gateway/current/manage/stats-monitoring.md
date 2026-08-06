---
title: View Statistics and Metrics
description: This content covers the statistics and metrics collected and made
  available by Sync Gateway
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/manage/pages/stats-monitoring.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:sync-gateway:manage:stats-monitoring.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/manage/stats-monitoring.html)

# View Statistics and Metrics

> This content covers the statistics and metrics collected and made available by Sync Gateway  
> Sync Gateway's statistics and metrics provide under-the-hood data on the performance, resource utilization and health of it nodes. This is increasingly important as deployments scale to support a large numbers of connected mobile and edge components.

Related _inter-syncgateway_ topics: [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md) | [Metrics REST API](../rest-api/rest-api-metrics.md) | [Prometheus Integration](../deploy/stats-prometheus.md)

## [](#introduction)Introduction

Deployments are increasingly scaling to support large numbers of connected mobile and edge clients. This places added emphasis on the effective monitoring of the health and performance of Sync Gateway nodes.

Sync Gateway's Metrics REST API\_ facilitates the process of gathering this essential data by providing access to node metrics covering:

* Performance
* Resource utilization
* Health

It also provides for integration with Prometheus.

Use the Metrics REST API to request the statistics in either [JSON](stats-monitoring-json.md) or [Prometheus](stats-monitoring-prometheus.md) format.

## [](#advantages-of-json-format)Advantages of JSON format

The custom [JSON](stats-monitoring-json.md) format was created specifically to describe Sync Gateway metrics, and provides rich, nested data.

## [](#advantages-of-prometheus-format)Advantages of Prometheus format

As with all Couchbase services, Sync Gateway exposes a [Prometheus](stats-monitoring-prometheus.md)\-compatible format in flat JSON. This familiar and consistent format is simple yet attractive for powerful comparisons using Prometheus, potentially across multiple services.