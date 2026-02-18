---
title: Integrate Prometheus
description: Integrating Sync Gateway and Prometheus for Stats Monitoring and Alerts
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/deploy/pages/stats-prometheus.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/3.3/deploy/stats-prometheus.html)

# Integrate Prometheus

> Integrating Sync Gateway and Prometheus for Stats Monitoring and Alerts  
> This content explains how to integrate Sync Gateway and Prometheus to provide effective monitoring and alerts for Sync Gateway events

Related _Statistics_ topics: [Metrics REST API](../rest-api/rest-api-metrics.md) | [Monitor](../manage/stats-monitoring.md)

## [](#introduction)Introduction

Sync Gateway’s Metrics REST API exposes stats in a [Prometheus![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#prometheus) compatible and JSON formats.

## [](#lbl-prom-act)Configuration

The Metrics REST API is enabled by default on port 4986\. To change this you need to edit the `api.metricsInterface` setting in your [bootstrap configuration file](../configuration/configuration-schema-bootstrap.md) and define the Sync Gateway URL and the port you want the API served on (for example: 4986) — see: [Example 1](#ex-activate).

Alternatively

If you are using 2.x file-based configuration then edit the `metricsInterface` setting in the `sync-gateway-config.json` configuration file — see: [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

Example 1\. Setting metrics interface endpoint

* Persistent Configuration
* 2.x File-based Configuration

Within the bootstrap configuration file:

```json
"api.metricsInterface": "127.0.0.1:4986" (1)
```

Within the sync gateway configuration file:

```json
"metricsInterface": "127.0.0.1:4986" (1)
```

| **1** | Here we define the Sync Gateway URL and the port (4986 in this instance) that we require the Metrics REST API to be served on. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------ |

## [](#integration)Integration

You will need to integrate Sync Gateway’s metrics feed with your Prometheus deployment. Couchbase provide both a configuration file and a sample rules file, in the `/path/to/sync/gateway/examples` folder, to make this integration with Prometheus easier.

Copy both the Prometheus configuration file (`prometheus.yml`) file and the baseline rules directory (`rules/sync-gateway.rules.yml`) from Sync Gateway’s release package into Prometheus’s `/etc` directory.

Example 2\. Files in-situ

```bash
/etc/prometheus/prometheus.yml (1)
/etc/prometheus/rules/sync-gateway.rules.yml (2)
```

| **1** | You can change this location by specifying the path using the command line flag \--config.file when starting Prometheus                          |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | You can specify a different location for the rules file by editing the path in the rule\_files section of the prometheus.yml configuration file. |

See also our blog entry [Monitoring Couchbase Sync Gateway with Prometheus and Grafana](https://blog.couchbase.com/monitoring-sync-gateway-prometheus-grafana/).

## [](#configuration)Configuration

Configuration of Prometheus to work with Sync Gateway is governed by two files, starter copies of which are provided with Sync Gateway — see: [Example 3](#ex-promyaml) for sample file contents.

Prometheus Configuration File

The provided `prometheus.yml` file specifies the configuration required to scrape the Sync Gateway metrics target. In this instance it defines Sync Gateway’s `metricsInterface` as being accessible on `sync_gateway:4986/metrics`. If you have multiple Sync Gateways, you can specify all their endpoints here (as `targets`).

Prometheus Rules File

Prometheus’s rules files enable you to specify both _recording_ and _alerting_ rules. Sync Gateway’s out-of-the-box rule set provides a starting point, which you can customize as needed. The rules include:

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
  - job_name: sgw
    metrics_path: /metrics
    static_configs:
      - targets: (3)
          - sync_gateway:4986
```

| **1** | The scrape\_interval specifies the polling interval.This interval determines the frequency at which Prometheus will scrape data from this endpoint. You can adjust it to your needs.                                            |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | rules\_files specifies the path to the Prometheus Rules file(s).The rules file defines any custom alerts based on the collected stats.                                                                                          |
| **3** | The targets property specifies the list of targets making statistics available to Prometheus; here we specify Sync Gateway’s metricsInterface.If you have multiple Sync Gateways, you can specify each of their endpoints here. |

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

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)