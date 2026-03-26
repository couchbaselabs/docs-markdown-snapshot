---
title: Couchbase Server Logging
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.6/modules/ROOT/pages/concept-couchbase-logging.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.6@operator::concept-couchbase-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.6/concept-couchbase-logging.html)

# Couchbase Server Logging

> Couchbase Server generates logs that can be used for auditing and troubleshooting purposes. 

Couchbase Server produces a [variety](../../server/current/manage/manage-logging/manage-logging.md#log-file-listing) of log files. A robust solution for storing and accessing Couchbase Server logs is required for a cluster to be considered [supportable](best-practices.md#table-pv-requirements-for-cluster-supportability).

## [](#default-logging)Default Logging

By default, Couchbase cluster deployments process logs within the Couchbase Server container. When a Couchbase cluster deployment is configured to use [persistent volumes](concept-persistent-volumes.md) — as is [recommended](best-practices.md#storage) for all production deployments — log files are written to either the `default` or `logs` volume.

When using default logging, logs cannot be collected from the Couchbase Server container's standard console output, as is [typical](https://kubernetes.io/docs/concepts/cluster-administration/logging/) in Kubernetes environments. Instead, the Autonomous Operator package is distributed with a support tool — [cao](tools/cao.md) — which can be used to collect a log snapshot at any time. This tool is often used for collecting resources, logs, and events from the Kubernetes cluster for use in Couchbase Support requests. It is also capable of collecting just Couchbase-related logs via its `--collectinfo` option.

The [cao](tools/cao.md) tool only captures a snapshot of the current logs at the time it was run, and is not intended to capture 100% of all logs at all times (rotated log files are not included in the snapshot). In addition, the tool requires `pods/exec` permissions in order to execute log collection scripts and run the [cbcollect\_info](../../server/current/cli/cbcollect-info-tool.md) command locally on each pod belonging to a Couchbase cluster, which may not be desirable for security and performance reasons. To avoid these limitations, you can choose to configure [log forwarding](#log-forwarding) as an alternative method for logging.

Learn More

* [Manage Couchbase Server Logging](howto-manage-couchbase-logging.md)

## [](#log-forwarding)Log Forwarding

Log forwarding can be used in addition to, or as an alternative for, [default logging](#default-logging). Although Couchbase Server doesn't natively support log forwarding, the Autonomous Operator can optionally deploy and manage a third-party log processor on each Couchbase pod that enables Couchbase Server logs to be forwarded to the log processor's standard console output as well as other destinations. Forwarding logs to standard console output is desirable since it allows for [simple debugging](https://kubernetes.io/docs/tasks/debug-application-cluster/debug-running-pod/#examine-pod-logs) and standards-based integration with centralized log management systems running in the Kubernetes cluster.

### [](#how-log-forwarding-works)How Log Forwarding Works

There are two primary components that provide log forwarding:

1. A _log processor image_ is used by the Autonomous Operator to deploy the `logging` sidecar container onto each Couchbase Server pod. The log processor reads the logs that Couchbase Server has written to a persistent volume, processes them, and then forwards them to a destination such as standard console output.
2. The _log forwarding configuration_, stored in a Kubernetes Secret, that gets consumed by the `logging` sidecar container and which controls its behavior.

When log forwarding is enabled, the Autonomous Operator uses Couchbase-provided [defaults](#default-log-forwarding-image-and-configuration) for both of these components.

> [!NOTE]
> A Kubernetes Secret for configuration per Couchbase cluster is recommended, rather than sharing configuration across clusters in the same Kubernetes namespace. The Kubernetes Secret is owned by the first cluster that creates it, so when that cluster is removed, the Kubernetes Secret is removed as well. Different Kubernetes namespaces require different Kubernetes Secrets, so the same name can be reused across Kubernetes namespaces. If a Kubernetes Secret is used that is created externally (e.g. for custom configuration), then ownership is not transferred so these can be reused in the same Kubernetes namespace.

![logging sidecar overview](_images/logging-sidecar-overview.png) 

Figure 1\. Log Forwarding Architecture

Learn More

* [Configure Log Forwarding](howto-couchbase-log-forwarding.md)
* [Forwarding Couchbase Logs with Fluent Bit](tutorial-couchbase-log-forwarding.md)

### [](#default-log-forwarding-image-and-configuration)About the Default Log Forwarding Image and Configuration

Log forwarding can be enabled via the [CouchbaseCluster](resource/couchbasecluster.md) resource specification (it is _disabled_ by default). When log forwarding is enabled, the Autonomous Operator defaults to a Couchbase-supplied [_log processor image_](https://hub.docker.com/r/couchbase/fluent-bit) that is based on [Fluent Bit](https://fluentbit.io/). The Autonomous Operator also automatically deploys a default _log forwarding configuration_ in the form of a Kubernetes Secret that gets consumed by the `logging` sidecar container.

The default, Couchbase-supplied log processor image provides several benefits, such as built-in _parsers_, _filters_, and optional log _redaction_ (another type of filtering), as well as the ability to restart Fluent Bit without having to restart the entire pod, thus providing better performance and higher availability than the standard Fluent Bit image. The built-in parsers and filters are stored in individual configuration files, which are then combined to provide the default [_main configuration_](https://docs.fluentbit.io/manual/administration/configuring-fluent-bit/configuration-file) deployed by the Autonomous Operator. Alternatively, these built-in parsers and filters can be selectively invoked by a custom, user-supplied main configuration that can be used instead of the default one provided by the Autonomous Operator.

The default log forwarding configuration outputs log events to the `logging` container's standard console output. However, a custom configuration can include more than one output, allowing specific logs to be [routed](https://docs.fluentbit.io/manual/concepts/data-pipeline/router) to different — even multiple — destinations.

### [](#log-parsing)Log Parsing

Couchbase logs generally store events in unstructured, sometimes multi-line formats. Since this type of unstructured data can't readily be used by standard log processors, Couchbase logs need to be [_parsed_](https://docs.fluentbit.io/manual/concepts/data-pipeline/parser) into _structured_ key-value pairs before events can be adequately filtered, mutated, and forwarded by a log processor like Fluent Bit.

The default log processor image provides built-in default parsers for several Couchbase logs. These built-in parsers primarily use regular expressions (regex) to extract the _timestamp_, _log level_, and _message_ of a particular event, though a few of the logs have some extra fields extracted. For those logs with multi-line output, the parser attempts to capture everything up to the next log statement. In some cases this includes large content (e.g. Java thread dumps), but this is all treated as part of the log message. (User-provided second-stage parsing or filtering can be done, but is not provided by default; a downstream log tool could also do further analysis.)

An Event from `goxdcr.log` _Before_ Processing

2021-04-16T18:13:40.603Z INFO GOXDCR.PipelineMgr: Replication Status = map[]

An Event from `goxdcr.log` _After_ Processing

[0] couchbase.log.xdcr: [1618596820.603000000, {"filename"=>"/opt/couchbase/var/lib/couchbase/logs/goxdcr.log", "timestamp"=>"2021-04-16T18:13:40.603Z", "level"=>"INFO", "message"=>" GOXDCR.PipelineMgr: Replication Status = map[]", "pod"=>"1a525bc96099", "logshipper"=>"couchbase.sidecar.fluentbit"}]

Each processed log event is a structured message made up of keys and values:

* `"timestamp"⇒"2021-04-16T18:13:40.603Z"`
* `"level"⇒"INFO"`
* `"message"⇒" GOXDCR.PipelineMgr: Replication Status = map[]"`

Every processed log event is [_tagged_](https://docs.fluentbit.io/manual/concepts/key-concepts#tag) individually with the name of the log file that the event came from (`couchbase.log._<name-of-log_`\>). This allows events to be [_matched_](https://docs.fluentbit.io/manual/concepts/key-concepts#match) for further manipulation and redirection. Additional helpful information is also added to the event, including file name, pod, and log processor.

#### [](#available-log-parsers)Available Log Parsers

The current Couchbase-supplied [_log processor image_](https://hub.docker.com/r/couchbase/fluent-bit) — based on Fluent Bit — contains built-in default parsers for several Couchbase logs, all stored in a single configuration file ([parsers-couchbase.conf](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/parsers-couchbase.conf)). Each parser currently defaults to parsing one or more specific logs.

[Table 1](#table-log-support-for-forwarding) lists each Couchbase log, along with its corresponding default parser.

__Table 1\. Log Forwarding Supported Features__
| Log File                                                                                                   | Default Parser                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| audit.log                                                                                                  | [_couchbase\_json\_log\_nanoseconds_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-audit-log.conf)            |
| babysitter.log                                                                                             | [_couchbase\_erlang\_multiline_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-erlang-multiline-log.conf)      |
| couchdb.log                                                                                                | [_couchbase\_erlang\_multiline_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-erlang-multiline-log.conf)      |
| crash-log.bin                                                                                              | None                                                                                                                                           |
| debug.log (Includes subsets error.log and info.log)                                                        | [_couchbase\_erlang\_multiline_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-erlang-multiline-log.conf)      |
| eventing.log                                                                                               | [_couchbase\_simple\_log\_mixed_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-eventing-fts-log.conf)         |
| fts.log                                                                                                    | [_couchbase\_simple\_log\_mixed_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-eventing-fts-log.conf)         |
| goxdcr.log                                                                                                 | [_couchbase\_simple\_log\_utc_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-xdcr-log.conf)                   |
| http\_access.log                                                                                           | [_couchbase\_http_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-http-log.conf)                               |
| http\_access\_internal.log                                                                                 | [_couchbase\_http_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-http-log.conf)                               |
| indexer.log                                                                                                | [_couchbase\_simple\_log_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-indexer-projector-log.conf)           |
| json\_rpc.log                                                                                              | [_couchbase\_erlang\_multiline_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-erlang-multiline-log.conf)      |
| mapreduce\_errors.log                                                                                      | None                                                                                                                                           |
| memcached.log                                                                                              | [_couchbase\_simple\_log\_space\_separated_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-memcached-log.conf) |
| metakv.log                                                                                                 | [_couchbase\_erlang\_multiline_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-erlang-multiline-log.conf)      |
| ns\_couchdb.log                                                                                            | [_couchbase\_erlang\_multiline_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-erlang-multiline-log.conf)      |
| projector.log                                                                                              | [_couchbase\_simple\_log_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-indexer-projector-log.conf)           |
| rebalance.log                                                                                              | [_couchbase\_rebalance\_report_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-rebalance-report.conf)          |
| reports.log                                                                                                | [_couchbase\_erlang\_multiline_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-erlang-multiline-log.conf)      |
| ssl\_proxy.log                                                                                             | None                                                                                                                                           |
| stats.log                                                                                                  | None                                                                                                                                           |
| views.log                                                                                                  | None                                                                                                                                           |
| xdcr.log                                                                                                   | None                                                                                                                                           |
| xdcr\_errors.log                                                                                           | None                                                                                                                                           |
| xcdr\_trace.log                                                                                            | None                                                                                                                                           |
| analytics\_access.log                                                                                      | None                                                                                                                                           |
| analytics\_cbas\_debug.log                                                                                 | None                                                                                                                                           |
| analytics\_dcpdebug.log                                                                                    | None                                                                                                                                           |
| analytics\_dcp\_failed\_ingestion.log                                                                      | None                                                                                                                                           |
| analytics\_debug.log (Includes subsets analytics\_info.log, analytics\_warn.log, and analytics\_error.log) | [_couchbase\_java\_multiline_](https://github.com/couchbase/couchbase-fluent-bit/blob/main/conf/couchbase/in-java-log.conf)                    |
| analytics\_shutdown.log                                                                                    | None                                                                                                                                           |

> [!NOTE]
> Some Couchbase log files contain a subset of events that are found in other log files. For example, `analytics_debug.log` includes everything in `analytics_info.log`, which in turn includes everything in `analytics_warn.log` and `analytics_error.log`. Similarly, `debug.log` includes everything in `info.log`, which in turn includes everything in `error.log`.
> 
> These "subset" logs are not parsed by default, since parsing them would put unnecessary load on the log processor and lead to duplicate log events being forwarded. However, for convenience, these logs are listed in [Table 1](#table-log-support-for-forwarding) under their respective superset logs.

### [](#log-redaction)Log Redaction

When Couchbase Server writes an event to a log file, it encases certain [sensitive information](../../server/current/manage/manage-logging/manage-logging.md#understanding%5Fredaction) in special tags. The Couchbase-supplied [log processor image](https://hub.docker.com/r/couchbase/fluent-bit) provides optional support for redacting this tagged information from Couchbase log events before they are forwarded to standard console output or other locations.

Log redaction is currently facilitated by a [LUA filter](https://docs.fluentbit.io/manual/pipeline/filters/lua) that leverages a Couchbase-supplied [LUA script](https://github.com/couchbase/couchbase-fluent-bit/blob/main/redaction/redaction.lua) and a third-party [SHA-1 hashing library](https://github.com/mpeterv/sha1), both of which are included in the default log processor image. The LUA filter hashes and replaces the contents of the `<ud>…​</ud>` tags in each log event. When log redaction is configured for a Couchbase deployment, a worker thread on each Kubernetes node is dedicated to handling the LUA parsing.

Log redaction isn't enabled by default, and therefore must be [enabled and configured](howto-couchbase-log-forwarding.md#configuring-log-redaction) by an administrator. The following are some important notes worth considering when enabling log redaction:

* Log redaction may hash away useful identifiers for things like internal usage, making debugging more difficult.
* Running a regex and string substitution can be resource-intensive, which has performance implications for both the log processor and Couchbase Server.
* By default, logs are only forwarded to standard console output, and not exported externally. A user would have to use a custom configuration to ship them elsewhere at which point the redaction can also be configured (and tuned for just the streams being exported).
* The log processor can feed into a standard Kubernetes log pipeline architecture that already provides redaction. For example, Fluentd has a [sanitizer plugin](https://github.com/fluent/fluent-plugin-sanitizer).