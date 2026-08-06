---
title: Monitoring and Metrics
description: Available metrics, Prometheus integration, and OpenTelemetry
  support in Cloud Native Gateway.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/configuration-management/pages/monitoring-metrics.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:configuration-management:monitoring-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/configuration-management/monitoring-metrics.html)

# Monitoring and Metrics

> Available metrics, Prometheus integration, and OpenTelemetry support in Cloud Native Gateway. 

Cloud Native Gateway exposes metrics through Prometheus and optionally exports them via OpenTelemetry using OTLP. Cloud Native Gateway serves metrics on a dedicated web port. The default is `9091`. This port also provides health check endpoints.

## [](#available-metrics)Available Metrics

This section summarizes the metrics that Cloud Native Gateway emits for gRPC, Data API, and Couchbase client activity. Use these metrics to monitor request volume, latency, connection health, and authentication behavior.

### [](#prometheus-endpoint)Prometheus Endpoint

Cloud Native Gateway exposes metrics in Prometheus exposition format at:

```none
http://<cng-host>:9091/metrics
```

Cloud Native Gateway serves this endpoint over plain HTTP on the web port for cluster-internal scraping.

### [](#grpc-metrics)gRPC Metrics

Cloud Native Gateway reports the following metrics under the `com.couchbase.cloud-native-gateway` instrumentation scope:

| Metric                   | Type          | Description                                                                                                        |
| ------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------ |
| grpc\_connections\_total | Counter       | Total number of gRPC connections created since the gateway started.                                                |
| grpc\_connections        | UpDownCounter | Number of active gRPC connections.                                                                                 |
| grpc\_client\_names      | Counter       | Count of requests by Couchbase SDK client name, extracted from the User-Agent metadata. Labeled with client\_name. |

### [](#data-api-metrics)Data API Metrics

Cloud Native Gateway reports the following metrics for Data API HTTPS operations. They use separate instrumentation scopes internal to the Data API and OpenAPI components:

| Metric                               | Type      | Description                                                                                |
| ------------------------------------ | --------- | ------------------------------------------------------------------------------------------ |
| oapi\_server\_requests               | Counter   | Total number of Data API requests, labeled by operation\_id and http\_status\_code.        |
| oapi\_server\_duration\_milliseconds | Histogram | Request duration in milliseconds, labeled by operation\_id and http\_status\_code.         |
| dataapi\_client\_request\_count      | Counter   | Count of Data API requests by recognized Couchbase client name, labeled with client\_name. |

### [](#couchbase-client-metrics)Couchbase Client Metrics

The `gocbcorex` client library reports metrics through Cloud Native Gateway's global OpenTelemetry provider. These metrics are always active and appear in both the Prometheus endpoint and any configured OTLP export.

The following metrics use the `github.com/couchbase/gocbcorex` instrumentation scope:

| Metric                            | Type      | Description                                                                                                                                                |
| --------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| db.client.operation.duration      | Histogram | Duration of Couchbase operations in seconds. Labeled with db.system, server.address, server.port, db.namespace for the bucket name, and db.operation.name. |
| db.client.connection.count        | Gauge     | Current number of open connections to Couchbase Server nodes.                                                                                              |
| db.client.connection.create\_time | Histogram | Time taken to establish a connection to a Couchbase Server node, in seconds.                                                                               |
| db.client.connection.failures     | Counter   | Total number of connection establishment failures.                                                                                                         |

The following metrics use the `github.com/couchbase/gocbcorex/cbauthx` instrumentation scope:

| Metric                          | Type      | Description                                             |
| ------------------------------- | --------- | ------------------------------------------------------- |
| cbauth.authcheck.duration       | Histogram | Duration of authentication checks, in seconds.          |
| cbauth.certcheck.duration       | Histogram | Duration of certificate validation checks, in seconds.  |
| cbauth.revrpc.total\_heartbeats | Counter   | Total number of cbauth reverse-RPC heartbeats received. |
| cbauth.revrpc.total\_dbupdates  | Counter   | Total number of cbauth database update events received. |

### [](#opentelemetry-grpc-server-metrics)OpenTelemetry gRPC Server Metrics

When you enable OpenTelemetry, Cloud Native Gateway also reports standard gRPC server metrics via `otelgrpc`, including per-RPC latency and status code distributions. These metrics follow the OpenTelemetry semantic conventions for gRPC.

### [](#opentelemetry-integration)OpenTelemetry Integration

Cloud Native Gateway supports exporting metrics and traces to an OpenTelemetry Collector via gRPC using OTLP:

```console
$ ./cloud-native-gateway --otlp-endpoint otel-collector.monitoring:4317
```

| Flag                     | Description                                                                           |
| ------------------------ | ------------------------------------------------------------------------------------- |
| \--otlp-endpoint         | The gRPC address of the OpenTelemetry Collector.                                      |
| \--disable-metrics       | Disable all metrics collection.                                                       |
| \--disable-traces        | Disable all trace collection.                                                         |
| \--disable-otlp-metrics  | Disables OTLP metric export. The Prometheus endpoint remains active.                  |
| \--disable-otlp-traces   | Disable exporting traces to OTLP.                                                     |
| \--trace-everything      | Enables tracing for all requests. By default, the parent context determines sampling. |
| \--otel-exporter-headers | Comma-separated list of headers for the OTLP exporter — for example, api-key=secret.  |

Cloud Native Gateway always enables the Prometheus exporter, and metrics collection is enabled by default. When you specify `--otlp-endpoint`, Cloud Native Gateway also adds an OTLP exporter as an additional metrics reader.

The OpenTelemetry resource includes:

* Service name: `couchbase-cloud-native-gateway`
* Process, host, and telemetry SDK attributes.
* Build version of Cloud Native Gateway.

## [](#monitoring-limitations)Monitoring Limitations

* **No built-in dashboards** — Cloud Native Gateway does not ship with pre-built Grafana or monitoring dashboards. You must create dashboards based on the metrics documented in this topic.
* **Unencrypted web port** — Cloud Native Gateway serves the metrics and health endpoint on port `9091` over plain HTTP. In production, make sure this port is not exposed outside the cluster network.
* **Per-instance metrics** — In sidecar deployments, each Cloud Native Gateway instance reports its own metrics independently. Use Prometheus service discovery or Kubernetes pod labels to aggregate across instances.
* **OTLP export is gRPC only** — The OTLP exporter uses gRPC via `otlpmetricgrpc` and `otlptracegrpc`. HTTP-based OTLP export is not supported.