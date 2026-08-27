---
title: Logging
description: ""
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.4/modules/howtos/pages/collecting-information-and-logging.adoc
  xref: xref:cxx-sdk:howtos:collecting-information-and-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/current/howtos/collecting-information-and-logging.html)

# Logging

> 

The Couchbase C++ SDK allows logging to be configured programmatically. Internally, the SDK uses the [spdlog](https://github.com/gabime/spdlog) logging library.

Once the logger has been initialized, The default log level is `info`.

The following log levels are supported (in order of increasing amount of information logged):

1. off
2. critical
3. error
4. warning
5. info
6. debug
7. trace

The C++ SDK can be configured to send logs to standard output, or to a file. The logger can be initialized and logging level changed like so:

```c++
#import <couchbase/logger.hxx>

void
initialize_logger()
{
    // Initialize logging to standard output
    couchbase::logger::initialize_console_logger();

    // Initialize logging to a file
    couchbase::logger::initialize_file_logger("/path/to/file");

    // Set log level
    couchbase::logger::set_level(couchbase::logger::log_level::warn);
}
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