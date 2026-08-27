---
title: Integrate Prometheus
description: Integrating Sync Gateway and Prometheus for Stats Monitoring and Alerts
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/stats-prometheus.adoc
  xref: xref:2.8@sync-gateway::stats-prometheus.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/stats-prometheus.html)

# Integrate Prometheus

> Integrating Sync Gateway and Prometheus for Stats Monitoring and Alerts  
> This content explains how to integrate Sync Gateway and Prometheus to provide effective monitoring and alerts for Sync Gateway events

Related _Statistics_ topics: [Metrics REST API](../current/rest-api/rest-api-metrics.md) | [Monitor](../current/manage/stats-monitoring.md)

## [](#introduction)Introduction

Sync Gateway's Metrics REST API exposes stats in a [Prometheus![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#prometheus) compatible and JSON formats.

## [](#lbl-prom-act)Configuration

The Metrics REST API is enabled by default on port 4986\. To change this you need to edit your `sync-gateway-config.json` configuration file.

Locate the `metricsInterface` setting and define the Sync Gateway URL and the port you want the API served on (for example: 4986) — see: [Example 1](#ex-activate).

Example 1\. Setting metrics interface endpoint

```json
"metricsInterface": "127.0.0.1:4986" (1)
```

| **1** | Here we define the Sync Gateway URL and the port (4986 in this instance) that we require the Metrics REST API to be served on. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------ |

## [](#integration)Integration

You will need to integrate Sync Gateway's metrics feed with your Prometheus deployment. Couchbase provide both a configuration file and a sample rules file to make this integration with Prometheus easier.

Copy both the Prometheus configuration file (`prometheus.yml`) file and the baseline rules directory (`rules/sync-gateway.rules.yml`) from Sync Gateway's release package into Prometheus's `/etc` directory.

Example 2\. Files in-situ

```bash
/etc/prometheus/prometheus.yml (1)
/etc/prometheus/rules/sync-gateway.rules.yml (2)
```

| **1** | You can change this location by specifying the path using the command line flag \--config.file when starting Prometheus                          |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | You can specify a different location for the rules file by editing the path in the rule\_files section of the prometheus.yml configuration file. |

See also our blog entry [Monitoring and Visualization of Couchbase Sync Gateway with Prometheus and Grafana](https://blog.couchbase.com/monitoring-and-visualization-of-couchbase-sync-gateway-with-prometheus-and-grafana/).

## [](#configuration)Configuration

Configuration of Prometheus to work with Sync Gateway is governed by two files, starter copies of which are provided with Sync Gateway — see: [Example 3](#ex-promyaml) for sample file contents.

Prometheus Configuration File

The provided `prometheus.yml` file specifies the configuration required to scrape the Sync Gateway metrics target. In this instance it defines Sync Gateway's `metricsInterface` as being accessible on `sync_gateway:4986/_metrics`. If you have multiple Sync Gateways, you can specify all their endpoints here (as `targets`).

Prometheus Rules File

Prometheus's rules files enable you to specify both _recording_ and _alerting_ rules. Sync Gateway's out-of-the-box rule set provides a starting point, which you can customize as needed. The rules include:

* A total queries record that adds up all query counts and saves it as `sgw::gsi::total_queries`
* A few example alerts

Example 3\. Sample file contents

* Config — prometheus.yaml
* Rules - sync-gateway-rules.yaml

The config file (`prometheus.yml`) specifies the configuration that the Prometheus server is launched with.

```yaml
global:
  scrape_interval:     5s (1)
  evaluation_interval: 5s

rule_files: (2)
  - '/etc/prometheus/rules/*'

scrape_configs:
  - job_name: swg
    metrics_path: /_metrics
    static_configs:
      - targets: (3)
          - sync_gateway:4986
```

| **1** | The scrape\_interval specifies the polling interval.This interval determines the frequency at which Prometheus will scrape data from this endpoint. You can adjust it to your needs.                                            |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | rules\_files specifies the path to the Prometheus Rules file(s).The rules file defines any custom alerts based on the collected stats.                                                                                          |
| **3** | The targets property specifies the list of targets making statistics available to Prometheus; here we specify Sync Gateway's metricsInterface.If you have multiple Sync Gateways, you can specify each of their endpoints here. |

The rules file (`sync-gateway-rules.yml`) specifies the alerting and recording rules.

```yaml
groups:
  - name: sync-gateway.rules
    rules:
      - record: sgw::gsi::total_queries (1)
        expr: sum by (instance, database, job) ({__name__=~"sgw_gsi_views_.*_count"})
      - alert: TooManyAuthFailuresInLastHour
        expr: increase(sgw_security_auth_failed_count[1h]) > 1000
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: Too Many Auth Failures in Last Hour
      - alert: TooManyDocumentAccessFailuresInLastHour (2)
        expr: increase(sgw_security_num_access_errors[1h]) > 1000
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: Too many Document Access Failures in last hour
      - alert: TooManyDocumentRejectionFailuresInLastHour
        expr: increase(sgw_security_num_docs_rejected[1h]) > 1000
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: Too many Document Rejection Failures in last hour
      - alert: HighRevCacheMissRate
        expr: sgw_cache_rev_cache_misses / (sgw_cache_rev_cache_misses + sgw_cache_rev_cache_hits) >= 0.8
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: High Rev Cache Miss Rate
      - alert: HighChannelCacheMissRate
        expr: sgw_cache_chan_cache_misses / (sgw_cache_chan_cache_misses + sgw_cache_chan_cache_hits) >= 0.8
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: High Channel Cache Miss Rate
      - alert: HighDeltaCacheMissRate
        expr: sgw_delta_sync_delta_sync_miss / (sgw_delta_sync_delta_sync_miss + sgw_delta_sync_delta_cache_hit) >= 0.8
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: High Delta Cache Miss Rate
      - alert: GlobalErrorCount
        expr: increase(sgw_resource_utilization_error_count[1h]) > 1
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: An error occurred in the last hour
      - alert: WarnXattrSizeCount
        expr: increase(sgw_database_warn_xattr_size_count[1h]) > 0
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: A document had larger sync data than the maximum allowed by xattrs in the last hour
      - alert: SGRNumDocsFailedToPull
        expr: increase(sgw_replication_sgr_num_docs_failed_to_pull[1h]) > 0
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: At least one document failed to be pulled with Inter Sync Gateway Replication in the last hour
      - alert: SGRNumDocsFailedToPush
        expr: increase(sgw_replication_sgr_num_docs_failed_to_push[1h]) > 0
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: At least one document failed to be pushed with Inter Sync Gateway Replication in the last hour
```

| **1** | Here we define a recording rule.Recording rules allow you to compute and save the results of frequently used (or computationally expensive) expressions.              |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we define an alerting rule.Alerting rules allow you to define alert conditions based on an expression and to send notifications when the expression is satisfied |

## [](#related-content)Related Content

###### [](#)

API Topics

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-2)

Reference

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)