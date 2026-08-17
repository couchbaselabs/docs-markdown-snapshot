---
title: What&#8217;s New
description: Couchbase Sync Gateway -- What's new in the latest release
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/whatsnew.adoc
  xref: xref:2.8@sync-gateway::whatsnew.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/whatsnew.html)

# What&#8217;s New

> Couchbase Sync Gateway — What's new in the latest release  
> This content covers the new features and behaviors introduced in Sync Gateway 2.8

## [](#release-2-8-1-february-2021)Release 2.8.1 (February 2021)

### [](#highlights)Highlights

Metrics REST API

Release 2.8.1 sees the transition to general availability of Couchbase Sync Gateway's Metrics REST API, which was introduced as a _developer preview_ in release 2.8.0.

This feature exposes Sync Gateway's extensive stats in both JSON and Prometheus-compatible format. For more on how to enable the integration of Sync Gateway's metrics with one of the most popular monitoring and alerting solutions — see: [Prometheus Integration](../current/deploy/stats-prometheus.md) and [Metrics REST API](../current/rest-api/rest-api-metrics.md).

### [](#other-enhancements)Other Enhancements

#### [](#custom-response-headers)Custom Response Headers

It is now possible to remove product versions from Sync Gateway responses using the `hide_product_versions` setting in the Config file. This customization of responses avoids revealing the version of the Sync Gateway to HTTP requests to the root path — see: [Hide Product Version in Headers](configuration-properties.md#hide%5Fproduct%5Fversion) and [CBG-1235](https://issues.couchbase.com/browse/CBG-1235)

#### [](#connection-string-overrides)Connection String Overrides

It is now possible to use the server connection string to override the current heuristic-driven behavior for selecting internal/external networking matches — see: [Couchbase Server Connection String](configuration-properties.md#databases-this%5Fdb-server) and [CBG-1276](https://issues.couchbase.com/browse/CBG-1276)

This release also contains a number of bug fixes for Sync Gateway — see: [Release Notes 2.8.1](release-notes.md#lbl-release-notes281) for contents.

## [](#release-2-8-0-october-2020)Release 2.8.0 (October 2020)

In addition to significant performance and resilience enhancements Sync Gateway 2.8 introduces enhanced support for inter-Sync Gateway replication and a developer preview of metrics API that allows integration with Prometheus/Grafana.

##### [](#inter-syncgateway-replication)Inter-Sync Gateway Replication

Couchbase Sync Gateway's _[Inter-Sync Gateway Replication![glossary icon](images/icons/glossaryIconImage2.png)](glossary.md#inter-sync-gateway-replication)_ feature supports _[cloud-to-edge![glossary icon](images/icons/glossaryIconImage2.png)](glossary.md#cloud-to-edge) synchronization_ use cases, where data changes must be synchronized between a centralized cloud cluster and a large number of edge clusters whilst still enforcing fine grained access control. This is an increasingly important enterprise-level requirement.

Read More . . . [Inter-Sync Gateway Replication](../current/sync/sync-inter-syncgateway-overview.md)

##### [](#prometheus-monitoring-support-developer-preview)Prometheus Monitoring Support (Developer Preview)

This release gives developers the chance to try-out Couchbase Sync Gateway's new metrics API, which exposes stats in a Prometheus compatible format. This enables the integration of Sync Gateway's metrics with one of the most popular monitoring and alerting solutions, without resorting to external data transformation.

Read More . . . [Metrics REST API](../current/rest-api/rest-api-metrics.md)

### [](#fixes-and-enhancements)Fixes and Enhancements

This release also contains a number of bug fixes and enhancements for Sync Gateway.

Highlights include the addition of a new OpenID Connect (OIDC) library, which broadens Sync Gateway's support of OIDC providers. This includes enabling developers to configure token attributes to use as the Sync Gateway user name ([username\_claim](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-oidc-providers-this%5Fprovider-username%5Fclaim)).

Read More . . . [Release Notes 2.8.0](release-notes.md#lbl-release-notes280)