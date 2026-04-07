---
title: Metrics REST API
description: Description of the Sync Gateway Metrics REST API
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/rest-api/pages/rest-api-metrics.adoc
pubDate: 2026-04-07T05:16:09.470Z
link: xref:sync-gateway:rest-api:rest-api-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/rest-api/rest-api-metrics.html)

# Metrics REST API

> Description of the Sync Gateway Metrics REST API  

Related _REST API_ topics: [Public REST API](rest-api.md) | [Admin REST API](rest-api-admin.md) | [Monitor](../manage/stats-monitoring.md) | [Prometheus Integration](../deploy/stats-prometheus.md)

## [](#introduction)Introduction

Sync Gateway makes collecting performance data easy and secure by providing a Metrics REST API. It exposes Sync Gateway's stats on two endpoints, which deliver the same data in one of two formats:

* The `metrics` endpoint returns Sync Gateway statistics in [Prometheus![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#prometheus) format.  
For example: `GET host:4986/metrics`  
For information on integration with Prometheus — see [Prometheus Integration](../deploy/stats-prometheus.md) and our blog entry [Monitoring Couchbase Sync Gateway with Prometheus and Grafana](https://blog.couchbase.com/monitoring-sync-gateway-prometheus-grafana/).
* The `_expvar` endpoint returns Sync Gateway statistics in JSON format.

This API, separate from both the Public and Admin REST APIs, is available by default on port `4986` — see [Configuration](#lbl-act) for how to change this, if needed. To allow users to access the Metrics API up you need to create a Couchbase Server-based RBAC-user for them — see: [REST API Access](rest-api-access.md).

## [](#lbl-act)Configuration

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

## [](#api-reference)API Reference

The [API reference](rest%5Fapi%5Fmetric.md) groups all the endpoints by functionality. For more information, refer to [View Statistics and Metrics](../manage/stats-monitoring.md).

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

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