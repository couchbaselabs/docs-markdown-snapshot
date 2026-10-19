---
title: Getting a Single Statistic
description: The REST API allows cluster-statistics to be retrieved from a single metric.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-statistics-single.adoc
  xref: xref:enterprise-analytics:reference:rest-statistics-single.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-statistics-single.html)

# Getting a Single Statistic

> The REST API allows cluster-statistics to be retrieved from a single metric. 

## [](#http-methods-and-uris)HTTP Method and URI

GET /pools/default/stats/range/<metric_name>/[function-expression]

## [](#description)Description

This method and URI allow cluster-statistics to be retrieved, based on the specification of a single metric. Optionally, the cluster-statistics can be further defined through the specifying of a _function_; and/or _labels_ with values.

An instance of _Prometheus_ runs on each node of the cluster; and the metrics for each node are duly stored in that node's instance of Prometheus.

## [](#curl-syntax)Curl Syntax

curl -X GET -u <username:password> \
http://<ip-address-or-domain-name>:<port-number>/pools/default/stats/range/<metric-name>/
  [function-expression]

When present, the optional `function-expression` should take the following form:

[[<function>?][<label>=<val>&]*]

As this indicates, any number of `<label>=<val>` pairs can be specified, with or without a preceding `<function>`. If a function is specified, it is applied to all statistics; if none is specified, all statistics are returned unmodified.

A `<function>` can be specified with or without one or more `<label>=<val>` pairs. If a `<function>` and at least one `<label>=<val>` pair are specified, the `<function>` must be followed with the `?` character. If multiple `<label>=<val>` pairs are specified, each is separated from the next with the `&` character.

All syntactic elements are described in the subsections immediately below.

### [](#function)`function`

The optional `function` parameter can be specified as follows:

<function> := rate | irate | increase | avg_over_time | min_over_time | max_over_time | deriv | delta | idelta | sum | min | max | avg | p[1-99]

* `rate`. The per-second average rate of increase of the time series, over the time window used when retrieving the time series. If the time window is not explicitly specified, it defaults to 1 minute (see the description of the optional timeWindow parameter).  
The `rate` function exposed by this API is the same as the Prometheus `rate` function.
* `irate`. The per-second instant rate of increase of the time series in the range vector. This is based on the last two data points.  
The `irate` function exposed by this API is the same as the Prometheus `irate` function.
* `increase`. The increase in the time series in the range vector.  
The `increase` function exposed by this API is the same as the Prometheus `increase` function.
* `avg_over_time`. The average value over a specified time window.
* `min_over_time`. The minimum value over a specified time window.
* `max_over_time`. The maximum value over a specified time window.
* `deriv`. The per-second derivative of the time series in a range vector, using simple linear regression.
* `delta`. The difference between the first and last value of each time series element in a range vector, returning an instant vector with the given deltas and equivalent labels. The delta is extrapolated to cover the full time range as specified in the range vector selector, so that it is possible to get a non-integer result even if the sample values are all integers.
* `idelta`. The difference between the last two samples in the range vector, returning an instant vector with the given deltas and equivalent labels.
* `sum`. The sum of values retrieved over the sample period.
* `min`. The minimum value retrieved over the sample period.
* `max`. The maximum value retrieved over the sample period.
* `avg`. The average of values retrieved over the sample period.
* `p[1-99]`The number of results to be displayed per page.

### [](#label-and-val)`label` and `val`

Supported _labels_ are of two kinds; which are _general_ and _service-specific_.

### [](#general-labels)General Labels

The possible specifications and associated values, are as follows.

* `start`. The starting timestamp for the sample period, in milliseconds. This value must be specified as a negative integer: the integer represents the number of milliseconds prior to `end` at which sampling commences. The default value is `-60`.
* `end`. The ending timestamp for the sample period, in milliseconds. The default value is the timestamp of the current time when sampling concludes. Therefore, if `start` is `-60`, the default value of `end` ensures that sampling runs for `60` milliseconds. By contrast, if `start` is `-60` and `end` is `-30`, this ensures that sampling runs for `30` milliseconds.
* `step`. The interval between successive value-retrievals, over the sample period, in milliseconds. The default is `10`. Therefore if `step`, `start`, and `end` all have their default values, sampling proceeds over six intervals; which are delineated by seven timestamps — these being the starting and ending timestamps, and the five in between.
* `nodes`. A specific node that is to be queried. If none is specified, all are queried.
* `nodesAggregation`. Whether and how aggregation of retrieved statistics is to be performed. Possible values are `max`, `min`, `sum`, and `avg`. The default is that no aggregation is performed.
* `timeWindow`. A time window, such as is required by the functions `rate`, `irate`, `avg_over_time`, and `max_over_time`; specified in milliseconds. The default value is `6` minutes.
* `timeout`. The period after which execution times out, in milliseconds. The default is `5` minutes.
* `alignTimestamps`. Whether to align timestamps so that each is a multiple of `10` milliseconds. The value can be `true` or `false` (which is the default). For example, if the value is `false`, consecutive timestamps might be `1617274978`, `1617274988`, and `1617274998`; whereas if the value is `true`, they might be `1617275000`, `1617275010`, and `1617275020`.

### [](#service-specific-labels)Service-Specific Labels

The possible specifications and associated values, are as follows.

* `scope`. A specific scope that is to be queried. If none is specified, all are queried.
* `collection`. A specific collection that is to be queried. If none is specified, all are queried.
* `connection_type`. A specific connection-type that is to be queried. If none is specified, all are queried.

## [](#responses)Responses

A malformed URI returns `404 Object Not Found`. Failure to authenticate returns `401 Unauthorized`. If an internal error causes the call the fail, `500` is returned.

If the URI is correct, and authentication succeeds, the operation is deemd successful. Success returns `200 OK`, and an object of the following kind. Note that incorrect specification of `metric-name` or `function-expression` does not produce execution-failure: indications of errors appear in the returned object.

{
  "data": [
    {
      "metric": <NameAndMetricLabels>,
      "values": [
        [ <Timestamp>, <Value> ],
        ...
      ]
    }
  ],
  "errors": [{"node": <NodeName>,
              "error": <Reason>}]
  "startTimestamp": <Value>,
  "endTimestamp": <Value>
}

The value of `data` is thus an array containing a single object. Within this object are represented:

* `metric`. Values include the specified `nodes`, and the `instance` (such as `kv`, `ns_server`, or `cbas`) from which the returned statistics were derived; and the specific `name` of the metric (such as `cbas_thread_count`).
* `values`. An array of arrays, each of which contains a timestamp and the value collected at that time.
* `errors`. An array of objects, each of which contains two key-value pairs: one providing the name of the `node` on which an error occurred, and the other the reason for the `error`.
* `startTimestamp`. The timestamp at which information-gathering commenced.
* `endTimestamp`. The timestamp at which information-gathering ended.

Successful location of a specified repository returns `200 OK` and an object containing information about the repository. If the specified repository is not located, `404` is returned, with the following object: `{"status": 404, "msg": "no repositories found"}`.

## [](#examples)Examples

The following examples demonstrate how the method and URI can be used.

### [](#retrieve-cpu-rate)Retrieve CPU Rate

The following expression retrieves the CPU rate for the specified node, using [jq](https://jqlang.org/) to format the output for readability:

curl -v -X GET \
http://10.144.210.101:8091/pools/default/stats/range/sys_cpu_sys_rate \
-u Administrator:password | jq '.'

If successful, the call returns an object such as the following:

{
  "data": [
    {
      "metric": {
        "nodes": [
          "10.144.210.101:8091"
        ],
        "category": "system",
        "instance": "ns_server",
        "name": "sys_cpu_sys_rate"
      },
      "values": [
        [
          1617698532,
          "15.899122807017545"
        ],
        [
          1617698542,
          "40.451977401129945"
        ],
        [
          1617698552,
          "25.087514585764293"
        ],
        [
          1617698562,
          "40"
        ],
        [
          1617698572,
          "34.420697412823394"
        ],
        [
          1617698582,
          "39.71238938053097"
        ],
        [
          1617698592,
          "35.75547866205306"
        ]
      ]
    }
  ],
  "errors": [],
  "startTimestamp": 1617698532,
  "endTimestamp": 1617698592
}

### [](#retrieve-cpu-rate-with-a-metric-specific-label)Retrieve CPU Rate, with a Metric-Specific Label

The following expression retrieves the _sysproc_ CPU rate for the `ns_server` process, for the specified node:

curl -v -u Administrator:password -X GET http://10.144.210.101:8091/pools/default/stats/range/\
sysproc_cpu_utilization?proc=ns_server&start=-5 | jq '.'

If successful, the call returns an object such as the following:

{
  "data": [
    {
      "metric": {
        "nodes": [
          "10.144.210.101:8091"
        ]
      },
      "values": [
        [
          1617698567,
          "82486"
        ],
        [
          1617698577,
          "79234"
        ],
        [
          1617698587,
          "78214"
        ],
        [
          1617698597,
          "77824"
        ],
        [
          1617698607,
          "76826"
        ],
        [
          1617698617,
          "72067"
        ],
        [
          1617698627,
          "41213"
        ]
      ]
    }
  ],
  "errors": [],
  "startTimestamp": 1617698567,
  "endTimestamp": 1617698627
}

### [](#get-metric-rate)Get Metric-Rate

The following example uses the `irate` function to derive the rate of the `cbas_http_requests_total` metric:

curl -v -u Administrator:password  -X GET \
http://10.144.210.101:8091/pools/default/stats/range/cbas_http_requests_total/irate?start=-180&step=60 | jq '.'

If successful, the call returns an object such as the following:

{
  "data": [
    {
      "metric": {
        "nodes": [
          "10.144.210.101:8091"
        ],
        "instance": "cbas",
        "name": "cbas_http_requests_total"
      },
      "values": [
        [
          1791568829,
          "0.19994001799460162"
        ],
        [
          1791568889,
          "0.1999600079984003"
        ],
        [
          1791568949,
          "0.19998000199980004"
        ],
        [
          1791569009,
          "0.2"
        ]
      ]
    }
  ],
  "errors": [],
  "startTimestamp": 1791568829,
  "endTimestamp": 1791569009
}

## [](#see-also)See Also

Multiple statistics can be returned by means of a single call. See [Getting Multiple Statistics](rest-statistics-multiple.md). For a complete list of available metrics that can be queried, see the [Metrics Reference](../metrics-reference/metrics-reference.md).