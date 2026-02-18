---
title: Log Streaming
description: Log Streaming provides a mechanism for real-time streaming of App
  Services operational logs to third-party observability platforms or
  self-hosted HTTP logs collectors.
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/monitoring/log-streaming.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/app-services/monitoring/log-streaming.html)

# Log Streaming

> Log Streaming provides a mechanism for real-time streaming of App Services operational logs to third-party observability platforms or self-hosted HTTP logs collectors. This is a crucial tool to gain instant insights into application behavior, enabling rapid issue detection and resolution to enhance application reliability, performance, and security. 

Capella App Services implements a managed, distributed service using multiple nodes. In a self-hosted service, like Couchbase’s Sync Gateway, you can directly connect to a node to figure figuring out the root cause and fix for issues with access control and synchronization. With a managed service, however, access to a given node’s logging data is not exposed directly.

With the opt-in Log Streaming feature, logs stream from each of the nodes to an industry standard log collector for full analysis.

Log Streaming has implications for [cost and sizing](#resource-consideration), and is turned off by default.

> [!WARNING]
> When configuring Log Streaming for App Services, you must make sure that all streamed log data complies with your company’s security and privacy standards as well as with any regulatory standards you adhere to.

## [](#supported-providers)Supported Log Collector Providers

> [!WARNING]
> Couchbase is not responsible for any third-party endpoints you configure.

We support log streaming to [Datadog](https://www.datadoghq.com/), [Sumo Logic](https://www.sumologic.com/), [Elasticsearch](https://www.elastic.co/elasticsearch), [Grafana Loki](https://grafana.com/oss/loki/), [Splunk](https://www.splunk.com/), [Dynatrace](https://www.dynatrace.com/) and to self-hosted log collectors via HTTP.

You can configure log streaming [using the Capella UI](configure-log-collector-app-service.md) or programmatically [using the Management API](manage-log-streaming.md).

You must set up your Log Collector as a prerequisite to using the Log Streaming feature.

> [!IMPORTANT]
> Capella App Services supports only Elasticsearch versions 8+. Capella App Services supports only the `basic auth` method with Elasticsearch. Elasticsearch creates and uses an `Elasticsearch Index` named `capella-app-services`.

## [](#resource-consideration)Resource Considerations

The amount of data depends on factors such as:

* Which logging filters and level you have requested.
* How many App Services endpoints are running.
* The number and size of documents in the cluster.
* Read/write/import throughput.
* Number of client connections per node.

You’ll incur egress data charges from the App Services nodes for the logging data. It’s therefore important to configure this feature precisely, to make sure that you receive useful information at a reasonable cost.

> [!TIP]
> Do not enable log streaming until you have validated what data you want, and understand the costs and resources involved in streaming it for your current and predicted data patterns.

By default, we stream everything from `Info` level and below, and enable a preset set of filters as detailed in [App Endpoint configuration page](configure-log-streaming-app-endpoint.md).

The log level and log filters are configurable, and can dramatically affect the amount of data streamed, which has cost implications.

Couchbase recommends keeping the defaults until you have verified that you need the data, and understand the costs involved.

> [!NOTE]
> In addition to network traffic, a node that’s streaming logs has some marginal effect on CPU and RAM usage.

## [](#troubleshooting)Troubleshooting

### [](#prerequisites)Prerequisites

Log Streaming is available for App Services on version 3.1.2 or later. Upgrade your App Services clusters to the newest version if you want to use this feature.

You must set up your Log Collector (see [Enable Log Streaming](configure-log-collector-app-service.md)), verify that it’s reachable, and configure its location in the Capella UI.

You must make sure that the log collector is able to handle the rate of logs streamed. App Services do not indefinitely buffer or maintain logs, therefore if the log collector falls behind, then you may lose logs. See [Log rotation and retention](#log-rotation-and-retention).

### [](#restarts-and-redeployments)Restarts and Redeployments

The logs are transient in App Services. Therefore if you redeploy (including to effect a log configuration change), then any logs that were not already streamed before the restart are lost.

When App Services comes back again, logging also restarts, with an entirely fresh set of logs.

### [](#turning-the-app-service-or-cluster-off-or-on)Turning the App Service or Cluster Off or On

When an [App Service turns Off](../app-services/turn-on-off.md), any Log Streaming, if enabled for those App Services, will also be turned off.

This also holds when the when the [Capella cluster turns Off](../../cloud/clusters/off-on-database.md) to reduce costs, and any linked App Services are also turned off.

When App Services restarts, Log Streaming resumes in the same state it was in before shutdown (Paused or Running).

### [](#log-rotation-and-retention)Log rotation and retention

You may want to know Capella App Services log retention, to understand the maximum partition window. This may help identify if there is any danger of missing logs due to disruption.

Due to the various factors discussed in [Resource Considerations](#resource-consideration) which affect your log streaming throughput (flow rate), a general figure cannot be provided. However, once you know that rate, you can calculate a value for your use-case.

For example, if you stream at 10 MB/hour/node, then the partition window is 100 hours (1 GB/node log retention, divided by 10 MB/hour/node).

Calculate the log streaming throughput from the Prometheus metric `fluentbit_output_proc_bytes_total`.

## [](#role-based-access)Role-Based Access

Roles enforce the following permissions for Log Streaming:

| Role                     | Permissions                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Org Owner, Project Owner | Ability to update and view log.                                                                                                          |
| Cluster Manager          | Streaming configuration for App Services associated with projects that the user has access to.                                           |
| Cluster Viewer           | Ability to only view log streaming configuration for App Services associated with projects that the user has access to.                  |
| Org Member               | Depends on the project-level access granted to the user. Users with only Org Member role and no project access cannot use this feature." |
| Data Reader, Data Writer | Cannot view or update configuration.                                                                                                     |

## [](#compatibility-guarantees)Compatibility guarantees

The structure of the JSON logs (the key names and type of values sent) is stable.

> [!NOTE]
> The contents of the message string in the JSON `log` field are an internal detail. The format and contents of this string are subject to change.

### [](#migration-from-sync-gateway)Migration from Sync Gateway

The underlying logging uses [Sync Gateway logging](../../sync-gateway/current/manage/logging.md). This means that existing self-managed users of Sync Gateway should find the logging format familiar from console logging, and should in general be able to point App Services log streaming to any existing Datadog or Sumo Logic log collector agents.

Your log processing code on prem should continue to work with Capella App Services log streaming with no or minimal changes.

> [!WARNING]
> Though the structure of the logs is stable, if your processing code relies on specific format of the `log` message, it may not work after migration. Scraping information from this field is not recommended.

## [](#billing)Billing

Couchbase bills data transfer costs for Log Streaming at the same rate as all other egress costs from App Services, and bundles these costs together in your account statement.

## [](#next-steps)Next Steps

* [Enable Log Streaming](configure-log-collector-app-service.md)
* [Configure Log Streaming for an App Endpoint](configure-log-streaming-app-endpoint.md)
* [Manage Log Streaming with the Management API](manage-log-streaming.md)