---
title: Enable Log Streaming
description: Enable real-time streaming of operational logs from App Services to
  a third-party or self-hosted log collector.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/monitoring/configure-log-collector-app-service.adoc
  xref: xref:app-services::monitoring/configure-log-collector-app-service.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/monitoring/configure-log-collector-app-service.html)

# Enable Log Streaming

> Enable real-time streaming of operational logs from App Services to a third-party or self-hosted log collector. 

This page describes how to configure log streaming using the Capella UI. To configure log streaming programmatically using the Management API, see [Manage Log Streaming with the Management API](manage-log-streaming.md).

## [](#setting-up-your-log-collector)Setting Up Your Log Collector

Enable Log Streaming in App Services Settings, under the Log Streaming tab.

Each option you choose has different configuration. See your third-party provider's documentation for full details on the collector endpoint setup.

> [!WARNING]
> Couchbase is not responsible for any third-party endpoints you configure.

[Datadog](https://www.datadoghq.com/)

* Requires an API access key.
* Enter the appropriate DataDog log intake URL.

[Sumo Logic](https://www.sumologic.com/)

* Sumo Logic uses a signed URL for secure log transmission, so no separate access key is necessary.

[Elasticsearch](https://www.elastic.co/elasticsearch)

* You can configure a target URL for log ingestion and a username and password. This username and password is then used in the HTTP Basic Authentication header sent to the log collector when sending logs.
* Authentication via an API key is not supported.
* App Services supports only Elasticsearch versions 8+.

[Grafana Loki](https://grafana.com/oss/loki/)

* You can configure a target URL for log ingestion and a username and password. This username and password is then used in the HTTP Basic Authentication header sent to the log collector when sending logs.

[Splunk](https://www.splunk.com/)

* Requires an HTTP Event Collector (HEC) token and the appropriate HEC endpoint URL. Splunk uses token-based authentication through the HEC interface, so you do not need a separate username and password.
* For Splunk Enterprise, you must enable HEC. See [Splunk documentation](https://docs.splunk.com/Documentation) for configuration details.
* Splunk Cloud Platform enables HEC by default with configuration managed through Splunk Web.

[Dynatrace](https://www.dynatrace.com/)

* Requires an API token for authentication.
* Enter the appropriate Dynatrace log URL for your environment.

Custom HTTP Collector

* You may use this to accommodate self-hosted log collectors.
* You can configure a target URL for log ingestion and an optional username and password. This username and password is then used in the HTTP Basic Authentication header sent to the log collector when sending logs.

Enabling Log Streaming begins data transmission to the chosen collector.

### [](#default-configuration)Default Configuration

App Services configures Log Streaming with an appropriate preset.

The Log Level defaults to `Info`, which is the most verbose level.

Log Level

Info

Couchbase recommends some default Log Filters as the most common useful data for most needs.

Cache

Logs related to App Services in-memory channel cache

Changes

Logs related to processing `/{db}/_changes` requests

CRUD

Logs about document updates, made by App Services

HTTP

Logs for all requests made to the App Services REST API

HTTP+

Additional information about HTTP logs (response times, status codes)

Query

Logs about SQL++ queries in App Services

You cannot change these preset keys here in the App Service settings. Instead, see the [App Endpoint Log Streaming configuration](#configure-log-streaming-app-endpoint.adoc) for more granular control over log data.

## [](#managing-the-log-collector)Managing the Log Collector

You may pause, turn off, or change the Log Streaming configuration (such as target URL and Access Credentials) at any time, except:

* while the App Service is not in a healthy state.
* during a transitional phase, such as enabling Log Streaming.

To change the collector type, turn off and re-enable Log Streaming.

## [](#troubleshooting)Troubleshooting

You must set up the Log Collector, make sure that it's reachable, and configure the location in the Capella UI.

You must make sure that the log collector is able to handle the rate of logs streamed. App Services cannot indefinitely buffer or maintain logs, therefore if the log collector falls behind, then you may lose logs.