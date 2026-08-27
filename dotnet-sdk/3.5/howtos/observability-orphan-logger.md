---
title: Orphaned Requests Logging
description: In addition to request tracing and metrics reporting, logging
  orphaned requests provides additional insight into why an operation might have
  timed out (or got cancelled for a different reason).
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/release/3.5/modules/howtos/pages/observability-orphan-logger.adoc
  xref: xref:3.5@dotnet-sdk:howtos:observability-orphan-logger.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.5/howtos/observability-orphan-logger.html)

# Orphaned Requests Logging

> In addition to request tracing and metrics reporting, logging orphaned requests provides additional insight into why an operation might have timed out (or got cancelled for a different reason). 

While tracing and metrics can also be consumed through external interfaces, getting information about orphaned requests only works through the built-in mechanisms.

The way it works is that every time a response is in the process of being completed, when the SDK detects that the original caller is not listening anymore (likely because of a timeout), it will send this "orphaned" response to a reporting utility which aggregates all responses and in regular intervals logs them in a specific format.

When you spot a `TimeoutException` in your log file, you can look for the output of the `OrphanReporter` and correlate the information.

## [](#output-format)Output Format

The `OrphanReporter` raises an `OrphansRecordedEvent` which in turn is going to be logged alongside all other SDK logs. Since orphans usually indicate a state that is not desirable, the log level for those events is `WARN`. By default they will be aggregated and logged every 10 seconds, but the event will be skipped if there are no orphans to report. This makes sure that the log line will appear close to the corresponding `TimeoutException` in the logs, while not spamming the log file if there is nothing to report. See the next section on how to customize this behavior.

The actual body of the message consists of the text `Orphaned requests found`, followed by a compact JSON representation of the aggregated orphans. The following code snippet shows a prettified version of such a JSON blob:

```json
[
   {
      "top":[
         {
            "b":"travel-sample",
            "r":"127.0.0.1:11210",
            "s":"get",
            "c":"9DACF45F00000001/0000000077CB4DAA",
            "d":8,
            "t":2500,
            "i":"0x6af7",
            "l":"127.0.0.1:62836"
         },
         {
            "b":"travel-sample",
            "r":"127.0.0.1:11210",
            "s":"get",
            "c":"9DACF45F00000001/0000000077CB4DAA",
            "d":8,
            "t":2500,
            "i":"0x5dcf",
            "l":"127.0.0.1:62836"
         },
         {
            "b":"travel-sample",
            "r":"127.0.0.1:11210",
            "s":"get",
            "c":"9DACF45F00000001/0000000077CB4DAA",
            "d":15,
            "t":2500,
            "i":"0x38f",
            "l":"127.0.0.1:62836"
         }
      ],
      "service":"kv",
      "count":3
   }
]
```

The fields are kept compact so that the logs don't get too big, but since they are abbreviations it is handy to have the following table available for reference:

__Table 1\. JSON Output Format Descriptions__
| Property | Description                                      |
| -------- | ------------------------------------------------ |
| b        | Name of the bucket                               |
| r        | Remote hostname if dispatched                    |
| l        | Local hostname if dispatched                     |
| s        | The name/type of the request                     |
| c        | The Channel ID to correlate with the server logs |
| d        | The server duration in microseconds if present   |
| t        | The configured timeout in milliseconds           |
| i        | The operation ID (i.e. opaque for Key/Value)     |

Please note that in future releases this format is planned to change for easier readability, so we do not provide any stability guarantees on the logging output format and it might change between minor versions.

If you want to enable the new output format, for now you have to set the `com.couchbase.orphanReporterNewOutputFormat` system property to `true`. Once enabled, the overall new structure looks like this:

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

__Table 2\. Experimental JSON Output Format Descriptions__
| Property                      | Description                                                          |
| ----------------------------- | -------------------------------------------------------------------- |
| total\_duration\_us           | The duration of the orphaned request.                                |
| encode\_duration\_us          | The duration of the encode span, if present.                         |
| last\_dispatch\_duration\_us  | The duration of the last dispatch span if present.                   |
| total\_dispatch\_duration\_us | The duration of all dispatch spans, summed up.                       |
| last\_server\_duration\_us    | The server duration attribute of the last dispatch span, if present. |
| operation\_name               | The name of the outer request span, with "cb." prefix removed.       |
| last\_local\_id               | The local\_id from the last dispatch span, if present.               |
| operation\_id                 | The operation\_id from the outer request span, if present.           |
| last\_local\_socket           | The local\_address from the last dispatch span, if present.          |
| last\_remote\_socket          | The remote\_address from the last dispatch span, if present.         |
| timeout\_ms                   | The operation timeout in milliseconds.                               |

If a field is not available, it will not be included in the output.

## [](#configuration)Configuration

The orphan logger can be configured through the `OrphanReporterConfig`.

The following properties can be configured:

__Table 3\. OrphanReporterConfig Properties__
| Property     | Default    | Description                                                          |
| ------------ | ---------- | -------------------------------------------------------------------- |
| emitInterval | 10 seconds | The interval where found orphans are emitted.                        |
| sampleSize   | 10         | The number of samples to store per service.                          |
| queueLength  | 1024       | Maximum buffer size of orphans to store to pick up for the reporter. |

In addition to those properties, if you want to try out the new logging format you can set the `com.couchbase.orphanReporterNewOutputFormat` system property to `true`.