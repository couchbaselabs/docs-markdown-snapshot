---
title: Slow Operations Logging
description: Tracing information on slow operations can be found in the logs as
  threshold logging, orphan logging, and other span metrics.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.5/modules/howtos/pages/slow-operations-logging.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:python-sdk:howtos:slow-operations-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/current/howtos/slow-operations-logging.html)

# Slow Operations Logging

> Tracing information on slow operations can be found in the logs as threshold logging, orphan logging, and other span metrics. Change the settings to alter how much information you collect 

To improve debuggability certain metrics are automatically measured and logged. These include slow queries, responses taking beyond a certain threshold, and orphanned responses.

## [](#threshold-logging-reporting)Threshold Logging Reporting

Threshold logging is the recording of slow operations — useful for diagnosing when and where problems occur in a distributed environment.

### [](#configuring-threshold-logging)Configuring Threshold Logging

To configure threshold logging, adjust the `ClusterTracingOptions`. For example setting the `tracing_threshold_kv` and `tracing_threshold_queue_size` on the Threshold Logger:

```python
# configure logging
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
# setup couchbase logging
logger = logging.getLogger()
couchbase.configure_logging(logger.name, level=logger.level)

tracing_opts = ClusterTracingOptions(
    tracing_threshold_queue_size=10,
    tracing_threshold_kv=timedelta(milliseconds=500))

cluster_opts = ClusterOptions(authenticator=PasswordAuthenticator(
    "Administrator",
    "password"),
    tracing_options=tracing_opts)

cluster = Cluster(
    "couchbase://your-ip",
    cluster_opts
)
```

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
  "operation_name": "upsert",
  "last_local_id": "66388CF5BFCF7522/18CC8791579B567C",
  "operation_id": "0x23",
  "last_local_socket": "10.211.55.3:52450",
  "last_remote_socket": "10.112.180.101:11210"
}
```

If a field is not present (because for example dispatch did not happen), it will not be included.