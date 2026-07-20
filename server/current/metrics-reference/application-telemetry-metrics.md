---
title: Application Telemetry Metrics
description: Couchbase can be configured to collect metrics related to Couchbase
  SDK calls made from applications.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/metrics-reference/pages/application-telemetry-metrics.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:server:metrics-reference:application-telemetry-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/metrics-reference/application-telemetry-metrics.html)

# Application Telemetry Metrics

> Couchbase can be configured to collect metrics related to Couchbase SDK calls made from applications. 

## [](#overview)Overview

Couchbase Server can be configured to collect metrics related to Couchbase SDK calls made from applications. The client SDKs send metrics to the Server that are then handled like regular server-side metrics, and you can access them through the Prometheus endpoint and the Stats API.

## [](#prerequisites)Prerequisites

You must enable application telemetry collection on your Couchbase Server installation. You can do this by executing the following curl command:

```bash
curl -u Administrator:password -X POST \
http[s]://{host}:{port}/settings/appTelemetry \
-d enabled=true
```

For more information about enabling application telemetry, see [Application Telemetry](../rest-api/application-telemetry.md)

## [](#telemetry-counters)Telemetry Counters

Couchbase can record the number of SDK calls made for specific services. The metrics follow the same basic patterns:

| Metric                      | Description                                        |
| --------------------------- | -------------------------------------------------- |
| sdk\_{service}\_r\_total    | The total number of operations                     |
| sdk\_{service}\_r\_canceled | The total number of operations that were canceled. |
| sdk\_{service}\_r\_timedout | The total number of operations that timed out.     |

To access the counter for a particular service, you replace `{service}` with one of the following:

* `kv`
* `query`
* `search`
* `analytics`
* `management`
* `eventing`

To access the number of calls that timed out for the Query Service, you would use the command: `sdk_query_r_timedout`.

## [](#histograms)Histograms

[Available Histograms](#available-histograms) below shows the available application telemetry metrics. The `_bucket` at the end of the metric names is a special suffix that signifies that the line should be interpreted as a bucket of that histogram. Also, there are 2 special metrics associated with each histogram: `_sum` and `_count` that represent the overall sum of all histogram buckets, and the total number of the points in the histogram. The `_sum` value should be a total sum of the points in milliseconds represented as an integer.

### [](#available-histograms)Available Histograms

* `sdk_kv_retrieval_duration_milliseconds_bucket`
* `sdk_kv_retrieval_duration_milliseconds_count`
* `sdk_kv_retrieval_duration_milliseconds_sum`
* `sdk_kv_mutation_nondurable_duration_milliseconds_bucket`
* `sdk_kv_mutation_nondurable_duration_milliseconds_count`
* `sdk_kv_mutation_nondurable_duration_milliseconds_sum`
* `sdk_kv_mutation_durable_duration_milliseconds_bucket`
* `sdk_kv_mutation_durable_duration_milliseconds_count`
* `sdk_kv_mutation_durable_duration_milliseconds_sum`
* `sdk_query_duration_milliseconds_bucket`
* `sdk_query_duration_milliseconds_count`
* `sdk_query_duration_milliseconds_sum`
* `sdk_search_duration_milliseconds_bucket`
* `sdk_search_duration_milliseconds_count`
* `sdk_search_duration_milliseconds_sum`
* `sdk_analytics_duration_milliseconds_bucket`
* `sdk_analytics_duration_milliseconds_count`
* `sdk_analytics_duration_milliseconds_sum`
* `sdk_eventing_duration_milliseconds_bucket`
* `sdk_eventing_duration_milliseconds_count`
* `sdk_eventing_duration_milliseconds_sum`
* `sdk_management_duration_milliseconds_bucket`
* `sdk_management_duration_milliseconds_count`
* `sdk_management_duration_milliseconds_sum`

Example 1\. Histogram output

```none
sdk_kv_retrieval_duration_milliseconds_bucket{le="1"} 24054
sdk_kv_retrieval_duration_milliseconds_bucket{le="10"} 33444
sdk_kv_retrieval_duration_milliseconds_bucket{le="100"} 100392
sdk_kv_retrieval_duration_milliseconds_bucket{le="500"} 129389
sdk_kv_retrieval_duration_milliseconds_bucket{le="1000"} 133988
sdk_kv_retrieval_duration_milliseconds_bucket{le="2500"} 139823
sdk_kv_retrieval_duration_milliseconds_bucket{le="+Inf"} 144320
sdk_kv_retrieval_duration_milliseconds_sum{} 53423000
sdk_kv_retrieval_duration_milliseconds_count{} 144320
```

[Example 1](#histogram-output) demonstrates a series of `kv` retrieval times for the buckets in a node. Each line gives the retrieval count for a particular range. For example, the `le="1"` label is the upper bound of the latency bucket, so that range is \\$le 1 ms\\$. The value would fall into all buckets where the upper bound is higher. As shown for the retrieval duration values, the requests completed in \\$le 1\\$ ms total 24,054, those in \\$le 10\\$ ms total 33,444 and so on.

There are 2 special metrics associated with each histogram: `_sum` and `_count` that represent the overall sum of all buckets, and total number of the points in the histogram.