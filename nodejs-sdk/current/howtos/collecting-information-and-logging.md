---
title: Logging
description: Node.js SDK logging.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.7/modules/howtos/pages/collecting-information-and-logging.adoc
  xref: xref:nodejs-sdk:howtos:collecting-information-and-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/current/howtos/collecting-information-and-logging.html)

# Logging

> Node.js SDK logging. 

## [](#node-js-logging)Node.js Logging

With the release of v4.7.0, the SDK now features a native logging abstraction. This interface is the primary mechanism for capturing and exporting the native Threshold Logging and Metrics data also introduced in v4.7.0.

> [!IMPORTANT]
> Logging on the Node.js side is still separate from the underlying C++ core logging. Integration with the C++ core logging is planned for a future release.

```typescript
interface Logger {
  trace?(message: string, ...args: any[]): void
  debug?(message: string, ...args: any[]): void
  info?(message: string, ...args: any[]): void
  warn?(message: string, ...args: any[]): void
  error?(message: string, ...args: any[]): void
}
```

A console logger can be created programmatically using the `createConsoleLogger()` function.

```typescript
import { connect, createConsoleLogger, LogLevel } from 'couchbase'

const cluster = await connect('couchbase://localhost', {
  username: 'Administrator',
  password: 'password',
  logger: createConsoleLogger(LogLevel.INFO)
})
```

### [](#environmental-settings)Environmental Settings

In the command line environment, the `CNLOGLEVEL` variable is set as follows:

GNU/Linux and Mac

```console
export CNLOGLEVEL=<log-level>
```

Windows

```console
set CNLOGLEVEL=<log-level>
```

The following values are accepted (case-insensitive):

* error — error messages.
* warn — error notifications.
* info — useful notices, not often.
* debug — diagnostic information, minimum level required to investigate problems.
* trace — detailed diagnostic information, often required to investigate problems.

Invalid values will be ignored, and the SDK will default to no logging.

## [](#library-logging)Library logging

The Node.js SDK allows logging via the `CBPPLOGLEVEL` environment variable.

Note that these logs will go to `stderr` — on most developers' laptops, `stderr` will be redirected to `stdout` (standard output), and displayed in the terminal running the app. Redirection to a log file may depend upon which shell you use. For the `BASH` shell, for example, see the [Bash Scripting Guide](https://tldp.org/LDP/abs/html/io-redirection.html).

### [](#environmental-settings-2)Environmental Settings

In the command line environment, the `CBPPLOGLEVEL` variable is set as follows:

GNU/Linux and Mac

```console
export CBPPLOGLEVEL=<log-level>
```

Windows

```console
set CBPPLOGLEVEL=<log-level>
```

Version 4.4.3 of the SDK introduces the `CBPPLOGFILE` variable that can be used in conjunction with `CBPPLOGLEVEL`. Set `CBPPLOGFILE` to a filename in order to have the log output to a file (instead of `stderr`).

In the command line environment, the `CBPPLOGFILE` variable is set as follows:

GNU/Linux and Mac

```console
export CBPPLOGFILE=<filename>
```

Windows

```console
set CBPPLOGFILE=<filename>
```

## [](#log-levels)Log Levels

You can increase the log level for greater verbosity (more information) in the logs:

* off — disables all logging, which is normally set by default.
* error — error messages.
* warn — error notifications.
* info — useful notices, not often.
* debug — diagnostic information, minimum level required to investigate problems.
* trace — detailed diagnostic information, often required to investigate problems.

When logging is turned on, the SDK will output messages similar to this:

```console
[2022-05-17 15:23:46.221] [85833,13741777] [debug] 1ms, [2aed64fd-5d38-416a-cc09-e67c371b8444]: use default CA for TLS verify
```

## [](#sdk-telemetry-from-the-server)SDK Telemetry from the Server

In addition to Tracing and other metrics, and client logging, SDK telemetry is also sent to the Server — available from 8.0, and in new Capella Operational clusters — for ingestion with other Prometheus metrics. Capella Operational exposes these metrics through the UI.

For self-managed Server, collection can be disabled and enabled through the REST API:

```console
curl --user Administrator:password http://172.17.0.2:8091/settings/appTelemetry -d enabled=true
```

And the Prometheus-format metrics fetched with:

```console
curl --user Administrator:password http://172.17.0.2:8091/metrics
```

Further details can be found in the [Application Telemetry](../../../server/current/rest-api/application-telemetry.md) page.

There may be advantages to collecting information this way, but note that metrics are collected per node, and a central Prometheus instance should be set to collect all metrics so that information is not lost in case of a sudden failover.

Also note that if the cluster is behind a load balancer, the collected metrics may not accurately record the actual correct node with which the SDK interacts.