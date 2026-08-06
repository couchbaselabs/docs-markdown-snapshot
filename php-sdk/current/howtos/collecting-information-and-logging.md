---
title: Logging
description: Logging with the SDK using the default logger implementation in PHP.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.5/modules/howtos/pages/collecting-information-and-logging.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:php-sdk:howtos:collecting-information-and-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/current/howtos/collecting-information-and-logging.html)

# Logging

> Logging with the SDK using the default logger implementation in PHP. 

## [](#logging)Logging

> [!WARNING]
> The Logging implementation has changed substantially in 4.0 and is not currently fully documented. This will be resolved in a future 4.x release.

The Couchbase PHP SDK has no hard dependency on a specific logger implementation. By default it uses built-in means to report events. The only thing you may change is the log level, which is controlled by `couchbase.log_level` in `php.ini`.

You can increase the log level for greater verbosity (more information) in the logs:

* off — disables all logging, which is normally set by default.
* error — error messages.
* warn — error notifications.
* info — useful notices, not often.
* debug — diagnostic information, required to investigate problems.
* trace — the most verbose level.

The PHP SDK is configured to send logs to standard output (when [error\_log](http://php.net/error%5Flog) is set to NULL). You can set it to `syslog` to redirect all logs (including the PHP SDK) to the syslog device. For example, the script below:

```php
$options = new ClusterOptions();
$options->credentials("Administrator", "password");

$cluster = new Cluster('couchbase://localhost', $options);
$bucket = $cluster->bucket('travel-sample');

$collection = $bucket->scope('inventory')->collection('airline');
$getResult = $collection->get('airline_10');

print_r($getResult->content());
```

…​along with this `php.ini` snippet:

```ini
error_log = syslog

extension = couchbase.so
couchbase.log_level = debug
```

Alternatively, if you do not wish to make changes in your `ini` file, you can use the `COUCHBASE_LOG_LEVEL` variable as follows:

GNU/Linux and Mac

```console
$ export COUCHBASE_LOG_LEVEL=<log-level>
```

Windows

```console
$ set COUCHBASE_LOG_LEVEL=<log-level>
```

When logging is turned on, the SDK will output messages similar to this:

```console
[2022-05-25 11:51:20.180] [72937,15083872] [debug] 0ms, [3d1ad384-ca9b-4983-b701-ea6ef15909ee/725383a6-e68b-460a-d782-56ee249fba58/plain/-] <localhost:11210> attempt to establish MCBP connection
[2022-05-25 11:51:20.182] [72937,15083872] [debug] 2ms, [3d1ad384-ca9b-4983-b701-ea6ef15909ee/725383a6-e68b-460a-d782-56ee249fba58/plain/-] <localhost:11210> connecting to ::1:11210, timeout=2000ms
[2022-05-25 11:51:20.182] [72937,15083872] [debug] 0ms, [3d1ad384-ca9b-4983-b701-ea6ef15909ee/725383a6-e68b-460a-d782-56ee249fba58/plain/-] <localhost:11210> connected to ::1:11210
[2022-05-25 11:51:20.182] [72937,15083872] [debug] 0ms, [3d1ad384-ca9b-4983-b701-ea6ef15909ee/725383a6-e68b-460a-d782-56ee249fba58/plain/-] <localhost/::1:11210> user_agent={"a":"cxx/1.0.0/","i":"3d1ad384-ca9b-4983-b701-ea6ef15909ee/725383a6-e68b-460a-d782-56ee249fba58"}, requested_features=[tcp_nodelay, mutation_seqno, xattr, xerror, select_bucket, json, duplex, alt_request_support, tracing, sync_replication, vattr, collections, subdoc_create_as_deleted, preserve_ttl, unordered_execution, clustermap_change_notification, snappy]
```

> [!NOTE]
> By default, `php-fpm` redirects the standard output and error streams to `/dev/null` for performance and FastCGI conformance reasons. In order to capture the logs in this setup, you must explicitly configure `catch_workers_output = yes`.

## [](#sdk-telemetry-from-the-server)SDK Telemetry from the Server

In addition to Tracing and other metrics, and client logging, SDK telemetry is also sent to the Server — available from 8.0, and in new Capella Operational clusters — for ingestion with other Prometheus metrics. Capella Operational exposes these metrics through the UI.

For self-managed Server, collection can be disabled and enabled through the REST API:

```console
curl --user Administrator:password http://172.17.0.2:8091/settings/appTelemetry -d enabled=true
```

And the Prometheus-format metrics fetched with:

```console
curl --user Administrator:password http://172.17.0.2:8091/metrics
```

Further details can be found in the [Application Telemetry](../../../server/current/rest-api/application-telemetry.md) page.

There may be advantages to collecting information this way, but note that metrics are collected per node, and a central Prometheus instance should be set to collect all metrics so that information is not lost in case of a sudden failover.

Also note that if the cluster is behind a load balancer, the collected metrics may not accurately record the actual correct node with which the SDK interacts.