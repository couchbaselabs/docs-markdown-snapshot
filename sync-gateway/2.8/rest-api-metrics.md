---
title: Metrics REST API
description: Description of the Sync Gateway Metrics Rest API
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/rest-api-metrics.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::rest-api-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/rest-api-metrics.html)

# Metrics REST API

> Description of the Sync Gateway Metrics Rest API  
> Use the API explorer to find out more about Sync Gateway’s endpoints by functionality.

Related _REST API_ topics: [Public REST API](../current/rest-api/rest-api.md) | [Admin REST API](../current/rest-api/rest-api-admin.md) | [Use the REST API?](#sync-gateway::rest-api-client-app.adoc) | [Monitor](../current/manage/stats-monitoring.md) | [Prometheus Integration](../current/deploy/stats-prometheus.md)

## [](#introduction)Introduction

Sync Gateway makes collecting performance data easy and secure by providing a Metrics REST API. This API, separate from both the Public and Admin REST APIs, is available by default on port `4986` — see [Configuration](#lbl-act) for how to change this, if needed. It exposes Sync Gateway’s stats on two endpoints, which deliver the same data in one of two formats:

* The `_metrics` endpoint returns Sync Gateway statistics in [Prometheus![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#prometheus) format.  
For example: `GET host:4986/_metrics`  
For information on integration with Prometheus — see [Prometheus Integration](../current/deploy/stats-prometheus.md) and our blog entry [Monitoring and Visualization of Couchbase Sync Gateway with Prometheus and Grafana](https://blog.couchbase.com/monitoring-and-visualization-of-couchbase-sync-gateway-with-prometheus-and-grafana/).
* The `_expvars` endpoint returns Sync Gateway statistics in JSON format.

## [](#lbl-act)Configuration

The Metrics REST API is enabled by default on port 4986\. To change this you need to edit your `sync-gateway-config.json` configuration file.

Locate the `metricsInterface` setting and define the Sync Gateway URL and the port you want the API served on (for example: 4986) — see: [Example 1](#ex-activate).

Example 1\. Setting metrics interface endpoint

```json
"metricsInterface": "127.0.0.1:4986" (1)
```

| **1** | Here we define the Sync Gateway URL and the port (4986 in this instance) that we require the Metrics REST API to be served on. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------ |

## [](#api-explorer)API Explorer

You can browse the API using the explorer below. The explorer groups all the endpoints by functionality. Just click a label to expand the endpoints. You can also generate curl requests if required, for each endpoint.

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