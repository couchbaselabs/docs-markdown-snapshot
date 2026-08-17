---
title: Slow Operations Logging
description: Tracing information on slow operations can be found in the logs as
  threshold logging, orphan logging, and other span metrics.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/release/3.5/modules/howtos/pages/slow-operations-logging.adoc
  xref: xref:3.5@dotnet-sdk:howtos:slow-operations-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.5/howtos/slow-operations-logging.html)

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