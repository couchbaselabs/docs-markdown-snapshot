---
title: Slow Operations Logging
description: Tracing information on slow operations can be found in the logs as
  threshold logging, orphan logging, and other span metrics.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.11/modules/howtos/pages/slow-operations-logging.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.11@go-sdk:howtos:slow-operations-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.11/howtos/slow-operations-logging.html)

# Slow Operations Logging

> Tracing information on slow operations can be found in the logs as threshold logging, orphan logging, and other span metrics. Change the settings to alter how much information you collect 

To improve debuggability certain metrics are automatically measured and logged. These include slow queries, responses taking beyond a certain threshold, and orphanned responses.

## [](#threshold-logging-reporting)Threshold Logging Reporting

Threshold logging is the recording of slow operations — useful for diagnosing when and where problems occur in a distributed environment.

## [](#output-format)Output Format

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

The `total_count` represents the total amount of over-threshold recorded items in each interval per service. The number of entries in "top\_requests" is configured by the `SampleSize`. The service placeholder is replaced with each service — "kv", "query", etc. Each entry looks like this, with all fields populated:

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

## [](#configuring-threshold-logging)Configuring Threshold Logging

Configuration of the `ThresholdLoggingTracer` is done on the tracer itself, at creation time. If no tracer is configured using `ClusterOptions.Tracer` then the default `ThresholdLoggingTracer` will be used.

```golang
	tracerOpts := &gocb.ThresholdLoggingOptions{
		Interval:   10 * time.Second,
		SampleSize: 10,
	}
	tracer := gocb.NewThresholdLoggingTracer(tracerOpts)

	opts := gocb.ClusterOptions{
		Authenticator: gocb.PasswordAuthenticator{
			Username: "Administrator",
			Password: "password",
		},
		Tracer: tracer,
	}
```

The following properties can be configured:

| Property            | Default          | Description                                                                            |
| ------------------- | ---------------- | -------------------------------------------------------------------------------------- |
| Interval            | 10 seconds       | The interval where found slow operations are emitted.                                  |
| SampleSize          | 10               | The number of samples to store per service.                                            |
| KVThreshold         | 500 milliseconds | The threshold over which the request is taken into account for the KV service.         |
| ViewsThreshold      | 1 second         | The threshold over which the request is taken into account for the views service.      |
| QueryThreshold      | 1 second         | The threshold over which the request is taken into account for the query service.      |
| SearchThreshold     | 1 second         | The threshold over which the request is taken into account for the search service.     |
| AnalyticsThreshold  | 1 second         | The threshold over which the request is taken into account for the analytics service.  |
| ManagementThreshold | 1 second         | The threshold over which the request is taken into account for the management service. |