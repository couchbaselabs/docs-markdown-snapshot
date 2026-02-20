---
title: Orphaned Requests Logging
description: In addition to request tracing and metrics reporting, logging
  orphaned requests provides additional insight into why an operation might have
  timed out (or got cancelled for a different reason).
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/howtos/pages/observability-orphan-logger.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:c-sdk:howtos:observability-orphan-logger.adoc[]
---

[View original HTML](/c-sdk/current/howtos/observability-orphan-logger.html)

# Orphaned Requests Logging

> In addition to request tracing and metrics reporting, logging orphaned requests provides additional insight into why an operation might have timed out (or got cancelled for a different reason). 

While tracing and metrics can also be consumed through external interfaces, getting information about orphaned requests only works through the built-in mechanism.

The way it works is that every time a response is in the process of being completed, when the SDK detects that the original caller is not listening anymore (likely because of a timeout), it will send this "orphaned" response to a reporting utility which aggregates all responses and in regular intervals logs them in a specific format.

When you spot a `TimeoutException` in your log file, you can look for the output of the `OrphanReporter` and correlate the information.

## [](#output-format)Output Format

Since orphans usually indicate a state that is not desirable, the log level for those events is `WARN`. By default they will be aggregated and logged every 10 seconds, if there are orphans to report. This makes sure that the log line will appear close to the corresponding `LCB_ERR_TIMEOUT` in the logs, while not spamming the log file if there is nothing to report. See the next section on how to customize this behavior.

The actual body of the message consists of the text `Orphaned requests found`, followed by a compact JSON representation of the aggregated orphans. The following code snippet shows a prettified version of such a JSON blob:

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

Each individual request has the following format:

```json
{
  "total_duration_us": 1200,
  "encode_duration_us": 100,
  "last_dispatch_duration_us": 40,
  "total_dispatch_duration_us": 40,
  "last_server_duration_us": 2,
  "timeout_ms": 75000,
  "operation_name": "upsert",
  "last_local_id": "66388CF5BFCF7522/18CC8791579B567C",
  "operation_id": "0x23",
  "last_local_socket": "10.211.55.3:52450",
  "last_remote_socket": "10.112.180.101:11210"
}
```

__Table 1\. Experimental JSON Output Format Descriptions__
| Property                      | Description                                                          |
| ----------------------------- | -------------------------------------------------------------------- |
| total\_duration\_us           | The duration of the orphaned request.                                |
| encode\_duration\_us          | The duration of the encode span, if present.                         |
| last\_dispatch\_duration\_us  | The duration of the last dispatch span if present.                   |
| total\_dispatch\_duration\_us | The duration of all dispatch spans, summed up.                       |
| last\_server\_duration\_us    | The server duration attribute of the last dispatch span, if present. |
| operation\_name               | The name of the outer request span, with “cb.” prefix removed.       |
| last\_local\_id               | The local\_id from the last dispatch span, if present.               |
| operation\_id                 | The operation\_id from the outer request span, if present.           |
| last\_local\_socket           | The local\_address from the last dispatch span, if present.          |
| last\_remote\_socket          | The remote\_address from the last dispatch span, if present.         |
| timeout\_ms                   | The operation timeout in milliseconds.                               |

If a field is not available, it will not be included in the output.

## [](#configuration)Configuration

The orphan logger can be configured through the connection string, or using `lcb_cntl` calls. See the [tracing orphaned logging options](../ref/client-settings.md#tracing-orphaned-logging-options) for details.

The following properties can be configured:

__Table 2\. OrphanReporterConfig Properties__
| Property     | Default    | Description                                   |
| ------------ | ---------- | --------------------------------------------- |
| emitInterval | 10 seconds | The interval where found orphans are emitted. |
| sampleSize   | 128        | The number of samples to store per service.   |