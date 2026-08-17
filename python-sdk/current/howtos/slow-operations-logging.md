---
title: Slow Operations Logging
description: Tracing information on slow operations can be found in the logs as
  threshold logging, orphan logging, and other span metrics.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/release/4.6/modules/howtos/pages/slow-operations-logging.adoc
  xref: xref:python-sdk:howtos:slow-operations-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/current/howtos/slow-operations-logging.html)

# Slow Operations Logging

> Tracing information on slow operations can be found in the logs as threshold logging, orphan logging, and other span metrics. Change the settings to alter how much information you collect 

To improve debuggability certain metrics are automatically measured and logged. These include slow queries, responses taking beyond a certain threshold, and orphanned responses.

## [](#threshold-logging-reporting)Threshold Logging Reporting

> [!NOTE]
> As of v4.6.0 the Threshold Logger is native to the Python SDK. In previous versions the underlying C++ core was responsible for threshold logging.

Threshold logging is the recording of slow operations — useful for diagnosing when and where problems occur in a distributed environment.

### [](#configuring-threshold-logging)Configuring Threshold Logging

By default the a threshold log report can be emitted every 10 seconds, but you can customize the emit interval, along with operation thresholds:

```python
tracing_opts = ClusterTracingOptions(
    tracing_threshold_queue_flush_interval=timedelta(seconds=5),
    tracing_threshold_queue_size=10,
    tracing_threshold_kv=timedelta(milliseconds=500))

auth = PasswordAuthenticator("Administrator", "password")
cluster_opts = ClusterOptions(authenticator=auth, tracing_options=tracing_opts)

cluster = Cluster.connect("couchbase://your-ip", cluster_opts)
```

The `ThresholdLogger` can be configured via `ClusterTracingOptions` as shown above. The following table shows the currently available properties:

__Table 1\. ClusterTracingOptions Properties__
| Property                                   | Default          | Description                                              |
| ------------------------------------------ | ---------------- | -------------------------------------------------------- |
| tracing\_enable\_tracing                   | true             | If tracing should be enabled.                            |
| tracing\_threshold\_kv                     | 500 milliseconds | The key-value operations threshold.                      |
| tracing\_threshold\_view                   | 1 second         | The view query operations threshold.                     |
| tracing\_threshold\_query                  | 1 second         | The query operations threshold.                          |
| tracing\_threshold\_search                 | 1 second         | The search query operations threshold.                   |
| tracing\_threshold\_analytics              | 1 second         | The analytics query operations threshold.                |
| tracing\_threshold\_eventing               | 1 second         | The eventing operations threshold.                       |
| tracing\_threshold\_management             | 1 second         | The management operations threshold.                     |
| tracing\_threshold\_queue\_size            | 10               | The top number of operations to report.                  |
| tracing\_threshold\_queue\_flush\_interval | 10 seconds       | The interval at which a threshold report can be emitted. |

Note that the Threshold Logger is set as the cluster level `Tracer` implementation.

#### [](#json-output-format-logging)JSON Output Format & Logging

You should expect to see output in JSON format in the logs for the services encountering problems:

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
  "total_server_duration_us": 2,
  "operation_name": "upsert",
  "last_local_id": "66388CF5BFCF7522/18CC8791579B567C",
  "operation_id": "0x23",
  "last_local_socket": "10.211.55.3:52450",
  "last_remote_socket": "10.112.180.101:11210"
}
```

If a field is not present (because for example dispatch did not happen), it will not be included.