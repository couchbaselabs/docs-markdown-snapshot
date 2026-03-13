---
title: Orphaned Requests Logging
description: In addition to request tracing and metrics reporting, logging
  orphaned requests provides additional insight into why an operation might have
  been cancelled (for example, because a timeout was applied by the caller).
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/observability-orphan-logger.adoc
pubDate: 2026-03-13T03:41:17.220Z
link: xref:rust-sdk:howtos:observability-orphan-logger.adoc[]
---

[View original HTML](/rust-sdk/current/howtos/observability-orphan-logger.html)

# Orphaned Requests Logging

> In addition to request tracing and metrics reporting, logging orphaned requests provides additional insight into why an operation might have been cancelled (for example, because a timeout was applied by the caller). 

While tracing and metrics can also be consumed through external interfaces, getting information about orphaned requests only works through the built-in mechanisms.

The way it works is that every time a response is in the process of being completed, when the SDK detects that the original caller is not listening anymore (beacuse the future was dropped), it will send this "orphaned" response to a reporting utility which aggregates all responses and in regular intervals logs them in a specific format.

When you spot that an operation `Future` has been dropped (e.g. due to a caller-side timeout), you can look for the output of the `OrphanReporter` and correlate the information.

## [](#output-format)Output Format

Since orphans usually indicate a state that is not desirable, The `OrphanReporter` logs orphaned requests at the `WARN` level, which is going to be logged alongside all other SDK logs. By default, orphans will be aggregated and logged every 10 seconds, but the output will be skipped if there are no orphans to report. This makes sure that the log line will appear close to the point in time when the corresponding `Future` was dropped, while not spamming the log file if there is nothing to report. See the next section on how to customize this behavior.

The actual body of the message consists of the text `Orphaned responses observed:`, followed by a compact JSON representation of the aggregated orphans. The following code snippet shows a prettified version of such a JSON blob:

```json
{
  "kv": {
    "total_count": 3,
    "top_requests": [
      {
        "last_server_duration_us": 8000,
        "total_server_duration_us": 8000,
        "operation_name": "Get",
        "last_local_id": "66388CF5BFCF7522/18CC8791579B567C",
        "operation_id": "0x3",
        "last_local_socket": "10.211.55.3:52450",
        "last_remote_socket": "10.112.180.101:11210"
      },
      {
        "last_server_duration_us": 1200,
        "total_server_duration_us": 1200,
        "operation_name": "Get",
        "last_local_id": "66388CF5BFCF7522/18CC8791579B567C",
        "operation_id": "0x1",
        "last_local_socket": "10.211.55.3:52450",
        "last_remote_socket": "10.112.180.101:11210"
      }
    ]
  }
}
```

The overall structure groups orphans by service (currently only `kv`), and for each service reports the total count of orphaned operations seen during the interval, along with the top sampled requests sorted by server duration (descending).

__Table 1\. JSON Output Format Descriptions__
| Property                    | Description                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------ |
| total\_count                | Total number of orphaned operations observed during the reporting interval.          |
| top\_requests               | Array of the top sampled orphaned requests, ordered by server duration (descending). |
| last\_server\_duration\_us  | The server duration in microseconds from the last dispatch, if present.              |
| total\_server\_duration\_us | The total accumulated server duration in microseconds across all dispatches.         |
| operation\_name             | The name of the operation (e.g. Get, Upsert).                                        |
| last\_local\_id             | The connection ID associated with the last dispatch, if present.                     |
| operation\_id               | The operation ID (opaque value for Key/Value operations).                            |
| last\_local\_socket         | The local socket address of the last dispatch, if present.                           |
| last\_remote\_socket        | The remote socket address of the last dispatch, if present.                          |

If a field is not available, it will not be included in the output.

## [](#configuration)Configuration

The orphan logger can be configured through the [OrphanReporterOptions](../ref/client-settings.md#orphan%5Freporter%5Foptions) in the `ClusterOptions`.

The following properties can be configured:

__Table 2\. OrphanReporterOptions Properties__
| Property           | Default    | Description                                                                    |
| ------------------ | ---------- | ------------------------------------------------------------------------------ |
| enabled            | true       | Whether the orphan reporter is enabled.                                        |
| reporter\_interval | 10 seconds | The interval at which accumulated orphans are emitted.                         |
| sample\_size       | 10         | The maximum number of top orphaned requests to retain and report per interval. |