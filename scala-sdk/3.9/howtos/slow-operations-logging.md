---
title: Slow Operations Logging
description: Tracing information on slow operations can be found in the logs as
  threshold logging, orphan logging, and other span metrics.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.9/modules/howtos/pages/slow-operations-logging.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.9@scala-sdk:howtos:slow-operations-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/3.9/howtos/slow-operations-logging.html)

# Slow Operations Logging

> Tracing information on slow operations can be found in the logs as threshold logging, orphan logging, and other span metrics. Change the settings to alter how much information you collect 

To improve debuggability certain metrics are automatically measured and logged. These include slow queries, responses taking beyond a certain threshold, and orphanned responses.

## [](#threshold-logging-reporting)Threshold Logging Reporting

Threshold logging is the recording of slow operations — useful for diagnosing when and where problems occur in a distributed environment.

### [](#configuring-threshold-logging)Configuring Threshold Logging

To configure threshold logging, adjust the [ThresholdRequestTracer](../ref/client-settings.md#general-options). You should expect to see output in JSON format in the logs for the services encountering problems:

```json
{
  "<service-a>": {
    "total_count": 1234,
    "top_requests": [{<entry>}, {<entry>},...]
  },
  "<service-b>": {
    "total_count": 1234,
    "top_requests": [{<entry>}, {<entry>},...]
  },
}
```

The `total_count` represents the total amount of over-threshold recorded items in each interval per service. The number of entries in "top\_requests" is configured by the `sampleSize`. The service placeholder is replaced with each service — "kv", "query", etc. Each entry looks like this, with all fields populated:

```json
{
  "total_duration_us": 1200,
  "encode_duration_us": 100,
  "last_dispatch_duration_us": 40,
  "total_dispatch_duration_us": 40,
  "last_server_duration_us": 2,
  "operation_name": "upsert",
  "last_local_id": "66388CF5BFCF7522/18CC8791579B567C,
  "operation_id": "0x23",
  "last_local_socket": "10.211.55.3:52450",
  "last_remote_socket": "10.112.180.101:11210"
}
```

If a field is not present (because for example dispatch did not happen), it will not be included.

## [](#orphaned-response-reporting)Orphaned Response Reporting

Orphan response reporting acts as an auxiliary tool to the tracing and metrics capabilities. It does not expose an external API to the application and is very focussed on its feature set.

The way it works is that every time a response is in the process of being completed, when the SDK detects that the original caller is not listening anymore (likely because of a timeout), it will send this "orphan" response to a reporting utility which then aggregates it and in regular intervals logs them in a specific format.

When the user then sees timeouts in their logs, they can go look at the output of the orphan reporter and correlate certain properties that aid debugging in production. For example, if a single node is slow but the rest of the cluster is responsive, this would be visible from orphan reporting.

### [](#configuring-orphan-logging)Configuring Orphan Logging

The OrphanResponseReporter is very similar in principle to the ThresholdRequestTracer, but instead of tracking responses which are over a specific threshold it tracks those responses which are "orphaned".

The `emitInterval` and `sampleSize` can be adjusted (defaults are 10s and 10 samples per service, respectively). The overall structure looks like this (here prettified for readability):

```json
{
  “<service-a>”: {
    “total_count”: 1234,
    “top_requests”: [{<entry>}, {<entry>},...]
  },
  “<service-b>”: {
    “total_count”: 1234,
    “top_requests”: [{<entry>}, {<entry>},...]
  },
}
```

The total\_count represents the total amount of recorded items in each interval per service. The number of entries in "top\_requests" is configured by the sampleSize. The service placeholder is replaced with each service, i.e. "kv", "query" etc. Each entry looks like this, with all fields populated:

```json
{
  "total_duration_us": 1200,
  "encode_duration_us": 100,
  "last_dispatch_duration_us": 40,
  "total_dispatch_duration_us": 40,
  "last_server_duration_us": 2,
  “timeout_ms”: 75000,
  "operation_name": "upsert",
  "last_local_id": "66388CF5BFCF7522/18CC8791579B567C,
  "operation_id": "0x23",
  "last_local_socket": "10.211.55.3:52450",
  "last_remote_socket": "10.112.180.101:11210"
}
```

If a field is not present (because for example dispatch did not happen), it will not be included.