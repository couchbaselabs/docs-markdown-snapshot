---
title: Logging
description: Log format, log levels, and log management for Cloud Native Gateway.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/configuration-management/pages/logging.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:configuration-management:logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/configuration-management/logging.html)

# Logging

> Log format, log levels, and log management for Cloud Native Gateway. 

Cloud Native Gateway uses structured JSON logging powered by the [zap](https://pkg.go.dev/go.uber.org/zap) logging library. Cloud Native Gateway writes logs to `stdout`, making them compatible with standard container log collection in Kubernetes and OpenShift environments.

## [](#log-format-and-structure)Log Format and Structure

Cloud Native Gateway emits all log entries as single-line JSON objects with the following fields:

| Field      | Description                                                               |
| ---------- | ------------------------------------------------------------------------- |
| level      | The log severity: debug, info, warn, or error.                            |
| ts         | The timestamp in ISO 8601 format — for example, 2024-01-15T10:30:00.000Z. |
| caller     | The source file and line number that produced the log entry.              |
| msg        | A human-readable description of the event.                                |
| stacktrace | Included automatically for error\-level messages.                         |

Cloud Native Gateway includes additional structured fields depending on the event. For example, connection events include `connectionString` and `User` fields, and error events include an `error` field with the error message.

### [](#example-log-output)Example Log Output

```json
{"level":"info","ts":"2024-01-15T10:30:00.000Z","caller":"gateway/gateway.go:150","msg":"linking to couchbase cluster","connectionString":"localhost","User":"Administrator"}
{"level":"info","ts":"2024-01-15T10:30:01.000Z","caller":"gateway/gateway.go:180","msg":"connected to couchbase cluster"}
{"level":"info","ts":"2024-01-15T10:30:01.500Z","caller":"system/system.go:200","msg":"starting to run protostellar system","boundPsPort":18098,"boundDapiPort":18099}
```

### [](#log-levels)Log Levels

Use the `--log-level` flag or the `STG_LOG_LEVEL` environment variable to set the log level. The default is `info`:

```console
$ ./cloud-native-gateway --self-sign --log-level debug
```

Supported levels, from most to least verbose:

* `debug` — Detailed diagnostic information, including request-level tracing and internal state changes.
* `info` — Normal operational events such as startup, connection, and configuration changes.
* `warn` — Unexpected but non-critical conditions, such as failed cluster pings during retry or configuration mismatches.
* `error` — Failures that require attention, such as connection failures or TLS certificate errors.

You can change the log level at runtime without restarting Cloud Native Gateway:

* **SIGHUP** — Send a `SIGHUP` signal to trigger a configuration reload. If the `--log-level` value has changed in the configuration file, the new level takes effect.
* **Config file watch** — When started with `--watch-config`, Cloud Native Gateway automatically detects changes to the configuration file and applies the new log level.

### [](#component-level-logging)Component-Level Logging

Cloud Native Gateway uses named loggers for its internal components. Each component's log entries include the component name in the `caller` or logger name field, making it straightforward to filter logs:

* `gateway` — Core gateway lifecycle and cluster connection.
* `gateway.data-impl` — Protostellar gRPC data operations.
* `gateway.dapi-impl` — Data API HTTP operations.
* `gateway.gateway-system` — gRPC and HTTP server management.
* `gateway.cbauth` — Authentication subsystem.
* `gateway.gocbcorex` — Couchbase cluster client.

## [](#log-redaction)Log Redaction

Cloud Native Gateway does not emit user data — such as document keys or document content — in `info`, `warn`, or `error` level log messages. Sensitive credentials (such as the Couchbase Server password) are explicitly excluded from configuration logging.

When running with `--log-level debug`, Cloud Native Gateway logs additional request-level detail. In production environments, use `info` or `warn` log levels to minimize the risk of logging sensitive information.

> [!NOTE]
> Log redaction tags as used by Couchbase Server are not applied by Cloud Native Gateway. If you require tagged log redaction for compliance, filter or post-process Cloud Native Gateway logs before forwarding them to a shared log aggregator.

## [](#prepare-logs-for-support)Prepare Logs for Support

Collect logs that cover the full issue window, including startup and shutdown events when possible.

### [](#kubernetes-deployments)Kubernetes Deployments

In Kubernetes deployments managed by the Couchbase Kubernetes Operator, Cloud Native Gateway runs as a sidecar container. To view Cloud Native Gateway logs for a specific pod:

```console
$ kubectl logs pod/mycluster-0000 -c cloud-native-gateway
```

To capture logs from all Cloud Native Gateway sidecars in a namespace:

```console
$ kubectl logs -l app=couchbase -c cloud-native-gateway -n my-namespace --prefix
```

Cloud Native Gateway logs are also collected automatically by the `cbopinfo` tool when generating a Couchbase Kubernetes Operator diagnostics archive.

### [](#self-managed-deployments)Self-Managed Deployments

For self-managed deployments, redirect `stdout` to a file or log aggregator:

```console
$ ./cloud-native-gateway --self-sign 2>&1 | tee /var/log/cng/gateway.log
```

Most log aggregation tools can load the structured JSON format directly without additional parsing.

### [](#information-to-include-in-support-tickets)Information to Include in Support Tickets

When filing a support ticket, include:

* Cloud Native Gateway logs at the most granular level possible, ideally `debug`, covering the time window of the issue.
* The Cloud Native Gateway version (shown in the startup log entry).
* The Couchbase Server version and cluster topology.
* The Cloud Native Gateway configuration flags or config file, with credentials redacted.
* Client SDK version and connection string used.