---
title: Slow Operations Logging
description: Tracing information on slow operations can be found in the logs as
  threshold logging, orphan logging, and other span metrics.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.3/modules/howtos/pages/slow-operations-logging.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:4.3@php-sdk:howtos:slow-operations-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/4.3/howtos/slow-operations-logging.html)

# Slow Operations Logging

> Tracing information on slow operations can be found in the logs as threshold logging, orphan logging, and other span metrics. Change the settings to alter how much information you collect. 

> [!WARNING]
> the Logging implementation has changed substantially in 4.0 and is not currently fully documented. This will be resolved in a future 4.x release.

To improve debuggability certain metrics are automatically measured and logged. These include slow queries, responses taking beyond a certain threshold, and orphaned responses.

## [](#threshold-logging-reporting)Threshold Logging Reporting

Threshold logging is the recording of slow operations — useful for diagnosing when and where problems occur in a distributed environment.

### [](#configuring-threshold-logging)Configuring Threshold Logging

To configure threshold logging with PHP SDK 3.x you will need to set the tracer configuration via the cluster connection string.

Before setting this up, however, you must ensure that your log level is high enough to display tracing messages.

```php
ini_set("couchbase.log_level", "INFO");
```

Next, add the tracer settings to the connection when initialising a cluster:

```php
$connectionString = "couchbase://127.0.0.1?" .
    "tracing_threshold_queue_flush_interval=3&" . /* every 3 seconds */
    "tracing_threshold_kv=0.01"; /* 10 milliseconds */

$cluster = new Cluster($connectionString, $options);
$bucket = $cluster->bucket("travel-sample");
$collection = $bucket->scope("inventory")->collection("airport");
```

This will set our threshold for key-value operations to 10 milliseconds, and log the found operations every 3 seconds.

Here is an example that shows upserting a document that causes longer processing on the server side.

```php
/*
 * Create a new document
 */
$document = ["answer" => 42, "updated_at" => date("r")];
$collection->upsert("foo", $document);

/*
 * Replace the document with a big body and very small deadline which should trigger a 
 * client-side timeout, in which case the server response will be reported as orphan
 */
$options = new UpsertOptions();
$options->timeout(1);
/*
 * Generate a document with 10M payload, that should be unfriendly to the compressing function
 * and longer to process on the server side
 */
$document = ["noise" => base64_encode(random_bytes(15_000_000))];
$numberOfTimeouts = 0;
while (true) {
    try {
        $collection->upsert("foo", $document, $options);
    } catch (TimeoutException $e) {
        $numberOfTimeouts++;
        if ($numberOfTimeouts > 3) {
            break;
        }
    }
}
```

You should expect to see output in JSON format in the logs for operations over the specified threshold (prettified for readability):

```json
[cb,INFO] (tracer L:149 I:1734870558) Operations over threshold: {
   "count":5,
   "service":"kv",
   "top":[
      {
         "operation_name":"php/upsert",
         "total_us":1584965
      },
      {
         "last_local_address":"127.0.0.1:55956",
         "last_local_id":"3918037d7eb01092/c14128c7238454cb",
         "last_operation_id":"0x2",
         "last_remote_address":"127.0.0.1:11210",
         "operation_name":"upsert",
         "server_us":153489,
         "total_us":1479441
      },
      {
         "operation_name":"php/request_encoding",
         "total_us":78730
      },
      {
         "operation_name":"php/request_encoding",
         "total_us":75922
      },
      {
         "operation_name":"php/upsert",
         "total_us":10862
      }
   ]
}
```

The `count` represents the total amount of recorded items in each interval per service, which in this case is the `KV` service. You can also see more information about each item/operation in the `top` array.

To see all the available options for the tracing settings refer to the [Tracing Options](#tracing%5Fsettings) section of this guide.

## [](#orphaned-response-reporting)Orphaned Response Reporting

Orphan response reporting acts as an auxiliary tool to the tracing and metrics capabilities. It does not expose an external API to the application and is very focused on its feature set.

The way it works is that every time a response is in the process of being completed, when the SDK detects that the original caller is not listening anymore (likely because of a timeout), it will send this “orphan” response to a reporting utility which then aggregates it. and at regular intervals logs them in a specific format.

When the user then sees timeouts in their logs, they can go look at the output of the orphan reporter and correlate certain properties that aid debugging in production. For example, if a single node is slow but the rest of the cluster is responsive, this would be visible from orphan reporting.

### [](#configuring-orphan-logging)Configuring Orphan Logging

Configuring orphan logging is very similar to how we configured the threshold logging, the only difference is the property passed to the cluster connection string:

```php
$connectionString = "couchbase://127.0.0.1?" .
    "tracing_orphaned_queue_flush_interval=5&"; /* every 5 seconds */

$cluster = new Cluster($connectionString, $options);
$bucket = $cluster->bucket("travel-sample");
$collection = $bucket->scope("inventory")->collection("airport");
```

The same code example from the threshold logging section can be used to demonstrate orphaned responses.

```php
/*
 * Create a new document
 */
$document = ["answer" => 42, "updated_at" => date("r")];
$collection->upsert("foo", $document);

/*
 * Replace the document with a big body and very small deadline which should trigger a 
 * client-side timeout, in which case the server response will be reported as orphan
 */
$options = new UpsertOptions();
$options->timeout(1);
/*
 * Generate a document with 10M payload, that should be unfriendly to the compressing function
 * and longer to process on the server side
 */
$document = ["noise" => base64_encode(random_bytes(15_000_000))];
$numberOfTimeouts = 0;
while (true) {
    try {
        $collection->upsert("foo", $document, $options);
    } catch (TimeoutException $e) {
        $numberOfTimeouts++;
        if ($numberOfTimeouts > 3) {
            break;
        }
    }
}
```

The expected output should be something similar to the log below:

```json
[cb,WARN] (tracer L:147 I:4044469160) Orphan responses observed: {
   "count":2,
   "service":"kv",
   "top":[
      {
         "last_local_address":"127.0.0.1:55653",
         "last_local_id":"fe4cb476e16ce16b/91c55f8ed6e3f1ae",
         "last_operation_id":"0x6",
         "last_remote_address":"127.0.0.1:11210",
         "operation_name":"upsert",
         "server_us":0,
         "total_us":476244
      },
      {
         "last_local_address":"127.0.0.1:55653",
         "last_local_id":"fe4cb476e16ce16b/91c55f8ed6e3f1ae",
         "last_operation_id":"0x9",
         "last_remote_address":"127.0.0.1:11210",
         "operation_name":"upsert",
         "server_us":0,
         "total_us":173575
      }
   ]
}
```

## [](#tracing%5Fsettings)Tracing Options

The table below describes all the allowed properties that can be set for tracing and their default values.

__Table 1\. Allowed Tracer Properties__
| Key                                            | Type     | Default | Description                                                                                  |
| ---------------------------------------------- | -------- | ------- | -------------------------------------------------------------------------------------------- |
| **enable\_tracing**                            | bool     | true    | Activate/deactivate end-to-end tracing.                                                      |
| **tracing\_orphaned\_queue\_size**             | int      | 128     | Size of orphaned spans queue in default tracer.                                              |
| **tracing\_orphaned\_queue\_flush\_interval**  | duration | 10.0    | Flush interval for orphaned spans queue in default tracer.                                   |
| **tracing\_threshold\_queue\_size**            | int      | 128     | Size of threshold queue in default tracer.                                                   |
| **tracing\_threshold\_queue\_flush\_interval** | duration | 10.0    | Flush interval for spans with total time over threshold in default tracer.                   |
| **tracing\_threshold\_kv**                     | duration | 0.5     | Minimum time for the tracing span of KV service to be considered by threshold tracer.        |
| **tracing\_threshold\_query**                  | duration | 1.0     | Minimum time for the tracing span of QUERY service to be considered by threshold tracer.     |
| **tracing\_threshold\_view**                   | duration | 1.0     | Minimum time for the tracing span of VIEW service to be considered by threshold tracer.      |
| **tracing\_threshold\_search**                 | duration | 1.0     | Minimum time for the tracing span of FTS service to be considered by threshold tracer.       |
| **tracing\_threshold\_analytics**              | duration | 1.0     | Minimum time for the tracing span of ANALYTICS service to be considered by threshold tracer. |

The duration properties are given in **seconds** with fractions after floating point (e.g. "2.5" is 2 seconds and 500 milliseconds).