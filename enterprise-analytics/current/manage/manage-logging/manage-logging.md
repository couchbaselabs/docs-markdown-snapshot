---
title: Manage Logging
description: The <em>Logging</em> facility allows a record to be maintained of
  important events that occur on Enterprise Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/manage/pages/manage-logging/manage-logging.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:manage:manage-logging/manage-logging.adoc[]
---

[View original HTML](/enterprise-analytics/current/manage/manage-logging/manage-logging.html)

# Manage Logging

> The _Logging_ facility allows a record to be maintained of important events that occur on Enterprise Analytics. 

## [](#logging%5Foverview)Logging Overview

The Enterprise Analytics _Logging_ facility records important events, and saves the details to log files, on disk. Additionally, events of cluster-wide significance are displayed on the **Logs** screen, in Enterprise Analytics Web Console.

The **Logs** screen provides a comprehensive view of cluster events, displaying log messages with timestamps, severity levels, and detailed descriptions of system activities.

By default, on Linux systems, log files are saved to `/opt/enterprise-analytics/var/lib/couchbase/logs`.

## [](#collecting%5Finformation)Collecting Information

On each node within an Enterprise Analytics-cluster, logging is performed continuously. _A subset_ of the results can be reviewed in the Enterprise Analytics Web Console **Logs** screen; while _all_ details are saved to the `logs` directory, as described above.

> [!NOTE]
> The `logs` directory may include `audit.log`.

This is a special log file, used to manage cluster-security, and is handled separately from the other log files. The information provided throughout the remainder of this page — on collecting, uploading, redacting, and more — _does not_ apply to `audit.log`. For information about `audit.log`, see [Auditing](../../../../server/current/learn/security/auditing.md).

Additionally, _explicit logging_ can be performed by the user. This allows comprehensive and fully updated information to be generated as required. The output includes everything currently on disk, together with additional data that is gathered in real time. Explicit logging can either be performed for all nodes in the cluster, or for one or more individual nodes. The results are saved as zip files: each zip file contains the log-data generated for an individual node.

Explicit logging can be performed by means of the Enterprise Analytics CLI utility `cbcollect_info`. The documentation for this utility, provided [here](../../../../server/current/cli/cbcollect-info-tool.md), includes a complete list of the log files that can be created, and a description of the contents of each.

Additionally, administrators with either the **Full Admin** or **Cluster Admin** role can perform explicit logging by means of Enterprise Analytics Web Console: on the **Logs** page, click on the **Collect Information** tab, located near the top.

> [!NOTE]
> For administrators without either of these roles, this tab does not appear.

This opens the **Collect Information** screen, which allows logs and diagnostic information to be collected either from all or from selected nodes within the cluster.

The **Collect Information** screen includes the following options:

* **Node selection**: Choose to collect logs from all nodes or select specific nodes.
* **Redact Logs** panel: Specify a log redaction level (described in [Applying Redaction](#applying%5Fredaction)).
* **Specify custom temp directory** checkbox: Specify the absolute pathname of a directory for temporary data storage during collection.
* **Specify custom destination directory** checkbox: Specify the absolute pathname for completed zip files.
* **Upload to Couchbase** checkbox: Enable direct upload to Couchbase Support (described in [Uploading Log Files](#uploading%5Flog%5Ffiles)).

To start the collection process, follow these steps:

1. Click the **Start Collecting** button.
2. A notification displays indicating that the collection process is running.
3. A stop button is provided to allow the collection process to be stopped if necessary.
4. When the collection process completes for each node, a notification displays the progress.
5. When the process has completed for all nodes, the system shows the results with details about the created log files.

A set of log files is created for each node in the cluster. Each file is saved as a zip file in the specified temporary location.

## [](#uploading%5Flog%5Ffiles)Uploading Log Files

Log files can be uploaded to Couchbase, for inspection by Couchbase Support.

For information about performing upload at the command-prompt, see [cbcollect\_info](../../../../server/current/cli/cbcollect-info-tool.md).

To upload by means of Enterprise Analytics Web Console, before starting the collection process, check **Upload to Couchbase**.

When the **Upload to Couchbase** option is selected, the interface expands to show additional fields:

* **Upload to Host** field: Contains the server location to which the customer data is uploaded.
* **Customer Name** field (required): Your organization or customer name.
* **Upload Proxy** field (optional): Hostname of a remote system for proxy upload.
* **Bypass Reachability Checks** checkbox: When unchecked (default), attempts to gather and upload without pre-verifying upload specifications. When checked, upload specifications are verified before collection begins.
* **Ticket Number** field (optional): Support ticket number if available.

When all required information has been entered, click the **Start Collecting** button to begin information collection. When collection and upload have been completed, the URL of the uploaded zip file is displayed.

## [](#getting-a-cluster-summary)Getting a Cluster Summary

A summary of the cluster’s status can be acquired by means of a link available in the **Collect Information** panel.

Click **Get cluster summary**, which opens the **Cluster Summary Info** dialog.

This dialog displays a JSON document containing detailed status on the current configuration and status of the entire cluster. The information can be copied to the clipboard using a **Copy to Clipboard** button. This information can then be manually shared with Couchbase Support, either in addition to, or as an alternative to log collection.

## [](#understanding%5Fredaction)Understanding Redaction

Optionally, log files can be _redacted_. This means that user-data, considered to be private, is removed. Such data includes:

* Key/value pairs in JSON documents
* Usernames
* Query-fields that reference key/value pairs and/or usernames
* Names and email addresses retrieved during product registration
* Extended attributes

This redaction of user-data is referred to as _partial_ redaction. (_Full_ redaction, which will be available in a forthcoming version of Enterprise Analytics, additionally redacts _meta-data_.)

In each modified log file, hashed text (achieved with SHA1) is substituted for redacted text. For example, the following log file fragment displays private data — a Couchbase username:

```bash
0ms [I0] {2506} [INFO] (instance - L:421) Effective connection string:
couchbase://127.0.0.1?username=Administrator&console_log_level=5&;.
Bucket=default
```

The redacted version of the log file might appear as follows:

```bash
0ms [I0] {2506} [INFO] (instance - L:421) Effective connection string:
<UD>e07a9ca6d84189c1d91dfefacb832a6491431e95</UD>.
Bucket=<UD>e16d86f91f9fd0b110be28ad00e348664b435e9e</UD>
```

> [!NOTE]
> Redaction may eliminate some parameters containing non-private data, as well as all parameters containing private.

Redaction of log files may have one or both of the following consequences:

* Logged issues are harder to diagnose, by both the user and Couchbase Support.
* Log-collection is more time-consumptive, since redaction is performed at collection-time.

## [](#applying%5Fredaction)Applying Redaction

Redaction of log files saved on the cluster can be applied as required, when performing _explicit logging_, by means of either `cbcollect_info` or the **Logs** facility of Enterprise Analytics Web Console.

For information about performing explicit logging with redaction at the command-prompt, see [cbcollect\_info](../../../../server/current/cli/cbcollect-info-tool.md).

To perform explicit logging with redaction by means of Enterprise Analytics Web Console, before starting the collection process, access the **Redact Logs** panel, on the **Collect Information** screen. This panel features two radio buttons:

* **No Redaction**: Collects logs without redaction
* **Partial Redaction**: Removes sensitive user data from logs

Select the **Partial Redaction** radio button to enable redaction. Guidance on redaction is displayed in the interface to help you understand the implications.

Click the **Start Collecting** button to begin the process. A notification explains that the collection process is now running. When the process has completed, a notification appears, specifying the location (local or remote) of each created zip file.

> [!NOTE]
> When redaction has been specified, two zip files are provided for each node: one file containing redacted data, the other unredacted data.

## [](#redacting-log-files-outside-the-cluster)Redacting Log Files Outside the Cluster

Certain Couchbase technologies — such as `cbbackupmgr`, the SDK, connectors, and Mobile — create log files saved outside the Couchbase Cluster. These can be redacted by means of the command-line tool `cblogredaction`. Multiple log files can be specified simultaneously. Each file must be specified as plain text. Optionally, the salt to be used can be automatically generated.

For example:

```bash
$ cblogredaction /Users/username/testlog.log -g -o /Users/username -vv
2018/07/17T11:27:06 WARNING: Automatically generating salt. This will make it difficult to cross reference logs
2018/07/17T11:27:07 DEBUG: /Users/username/testlog.log - Starting redaction file size is 19034284 bytes
2018/07/17T11:27:07 DEBUG: /Users/username/testlog.log - Log redacted using salt: <ud>COeAtexHB69hGEf3</ud>
2018/07/17T11:27:07 INFO: /Users/username/testlog.log - Finished redacting, 50373 lines processed, 740 tags redacted, 0 lines with unmatched tags
```

For more information, see the corresponding man page, or run the command with the `--h` (help) option.

## [](#log-file-locations)Log File Locations

Enterprise Analytics creates log files in the following locations.

| Platform | Location                                           |
| -------- | -------------------------------------------------- |
| Linux    | _/opt/enterprise-analytics/var/lib/couchbase/logs_ |

## [](#log-file-listing)Log File Listing

The following table lists the log files to be found on Enterprise Analytics. Unless otherwise specified, each file is named with the `.log` extension.

| File                              | Log Contents                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| audit                             | Security audit log for administrators.                                                                                                                                                                                                                                                                                                                   |
| babysitter                        | Troubleshooting log for the babysitter process which is responsible for spawning all Enterprise Analytics processes and respawning them where necessary.                                                                                                                                                                                                 |
| couchdb                           | Troubleshooting log for the couchdb subsystem which underlies map-reduce.                                                                                                                                                                                                                                                                                |
| debug                             | Debug-level troubleshooting for the Cluster Manager.                                                                                                                                                                                                                                                                                                     |
| error                             | Error-level troubleshooting log for the Cluster Manager.                                                                                                                                                                                                                                                                                                 |
| http\_access                      | The admin access log records server requests (including administrator logins) to the REST API or Enterprise Analytics Web Console. It is output in common log format and contains several important fields such as remote client IP, timestamp, GET/POST request and resource requested, HTTP status code, and so on.                                    |
| http\_access\_internal            | The admin access log records internal server requests (including administrator logins) to the REST API or Enterprise Analytics Web Console. It is output in common log format and contains several important fields such as remote client IP, timestamp, GET/POST request and resource requested, HTTP status code, and so on.                           |
| info                              | Info-level troubleshooting log for the Cluster Manager.                                                                                                                                                                                                                                                                                                  |
| json\_rpc                         | Log used by the cluster manager.                                                                                                                                                                                                                                                                                                                         |
| mapreduce\_errors                 | JavaScript and other view-processing errors are reported in this file.                                                                                                                                                                                                                                                                                   |
| memcached                         | Contains information relating to the core memcached component, including DCP stream requests and slow operations.It is possible to adjust the logging for slow operations. See [\[adjust-threshold-slow-op-logging\]](#adjust-threshold-slow-op-logging) for details.                                                                                    |
| metakv                            | Troubleshooting log for the metakv store, a cluster-wide metadata store.                                                                                                                                                                                                                                                                                 |
| ns\_couchdb                       | Contains information related to starting up the couchdb subsystem.                                                                                                                                                                                                                                                                                       |
| prometheus                        | Log for the instance of [Prometheus](https://prometheus.io) that runs on the current node, supporting the gathering and management of Couchbase-Server _metrics_ . (See the [Metrics Reference](../../metrics-reference/metrics-reference.md), for more information.)                                                                                    |
| rebalance                         | Contains reports on rebalances that have occurred. Up to the last _five_ reports are maintained. Each report is named in accordance with the time it was run: for example, rebalance\_report\_2020-03-17T11:10:17Z.json. See the [Rebalance Reference](../../../../server/current/rebalance-reference/rebalance-reference.md), for detailed information. |
| reports                           | Contains progress and crash reports for the Erlang processes. Due to the nature of Erlang, processes crash and restart upon an error.                                                                                                                                                                                                                    |
| ssl\_proxy                        | Troubleshooting log for the ssl proxy spawned by the Cluster Manager.                                                                                                                                                                                                                                                                                    |
| stats                             | Contains periodic statistic dumps from the Cluster Manager.                                                                                                                                                                                                                                                                                              |
| analytics\_access                 | information about access attempts made to the REST/HTTP port of the Analytics Service.                                                                                                                                                                                                                                                                   |
| analytics\_cbas\_debug            | Debugging information, related to the Analytics Service.                                                                                                                                                                                                                                                                                                 |
| analytics\_dcpdebug               | DCP-specific debugging information related to the Analytics Service.                                                                                                                                                                                                                                                                                     |
| analytics\_dcp\_failed\_ingestion | information about documents that have failed to be imported/ingested from the Data Service into the Analytics Service.                                                                                                                                                                                                                                   |
| analytics\_debug                  | Events logged by the Analytics Service at the DEBUG logging level.                                                                                                                                                                                                                                                                                       |
| analytics\_error                  | Events logged by the Analytics Service at the ERROR logging level.                                                                                                                                                                                                                                                                                       |
| analytics\_info                   | Events logged by the Analytics Service at the INFO logging level.                                                                                                                                                                                                                                                                                        |
| analytics\_shutdown               | Information concerning the shutting down of the Analytics Service.                                                                                                                                                                                                                                                                                       |
| analytics\_warn                   | Events logged by the Analytics Service at the WARN logging level.                                                                                                                                                                                                                                                                                        |

## [](#log-file-rotation)Log File Rotation

The `memcached` log file is rotated when it has reached 10MB in size; twenty rotations being maintained — the current file, plus nineteen compressed rotations. Other logs are automatically rotated after they have reached 40MB in size; ten rotations being maintained — the current file, plus nine compressed rotations.

To provide custom rotation-settings for each component, add the following to the `static_config` file:

{disk_sink_opts_disk_debug,
        [{rotation, [{size, 10485760},
        {num_files, 10}]}]}.

This rotates the `debug.log` at 10MB, and keeps ten copies of the log: the current log and nine compressed logs.

Log rotation settings can be changed.

> [!NOTE]
> This is not advised, and only the default log rotation settings are supported by Couchbase.

## [](#changing-log-file-locations)Changing Log File Locations

The default log location on Linux systems is _/opt/enterprise-analytics/var/lib/couchbase/logs_. The location can be changed.

> [!NOTE]
> This is not advised, and only the default log location is supported by Couchbase.

To change the location, proceed as follows:

1. Log in as `root` or `sudo` and navigate to the directory where Enterprise Analytics is installed. For example: `/opt/enterprise-analytics/etc/couchbase/static_config`.
2. Edit the _static\_config_ file: change the `error_logger_mf_dir` variable, specifying a different directory. For example: `{error_logger_mf_dir, "/home/user/cb/opt/enterprise-analytics/var/lib/couchbase/logs"}`
3. Stop and restart Enterprise Analytics. See [Startup and Shutdown](../../../../server/current/install/startup-shutdown.md).

## [](#changing-log-file-levels)Changing Log File Levels

The default logging level for all log files is _debug_, except for `couchdb`, which is set to _info_. Logging levels can be changed.

> [!NOTE]
> This is not advised, and only the default logging levels are supported by Couchbase.

Either _persistent_ or _dynamic_ changes can be made to logging levels.

### [](#persistent-changes)Persistent Changes

_Persistent_ means that changes continue to be implemented, should an Enterprise Analytics reboot occur. To make a persistent change on Linux systems, proceed as follows:

1. Log in as `root` or `sudo`, and navigate to the directory where you installed Couchbase. For example: `/opt/enterprise-analytics/etc/couchbase/static_config`.
2. Edit the _static\_config_ file and change the desired log component. (Parameters with the `loglevel_` prefix establish logging levels.)
3. Stop and restart Enterprise Analytics. See [Startup and Shutdown](../../../../server/current/install/startup-shutdown.md).

### [](#dynamic-changes)Dynamic Changes

_Dynamic_ means that if an Enterprise Analytics reboot occurs, the changed logging levels revert to the default. To make a dynamic change, execute a `curl POST` command, using the following syntax:

curl -X POST -u adminName:adminPassword HOST:PORT/diag/eval \
              -d 'ale:set_loglevel(<log_component>,<logging_level>).'

* `log_component`: The default log level (except `couchdb`) is `debug`; for example `ns_server`.
* `logging_level`: The available log levels are `debug`, `info`, `warn`, and `error`.  
curl -X POST -u Administrator:password http://127.0.0.1:8091/diag/eval \
                -d 'ale:set_loglevel(ns_server,error).'

## [](#collecting-logs-using-cli)Collecting Logs Using the CLI

To collect logs, use the CLI command [cbcollect\_info](../../../../server/current/cli/cbcollect-info-tool.md).

To start and stop log-collection, and to collect log-status, use:

* [collect-logs-start](#server:cli:couchbase-cli-collect-logs-start.adoc)
* [collect-logs-stop](#server:cli:couchbase-cli-collect-logs-stop.adoc)
* [collect-logs-status](#server:cli:couchbase-cli-collect-logs-status.adoc)

## [](#collecting-logs-using-rest)Collecting Logs Using the REST API

The Logging REST API provides the endpoints for retrieving log and diagnostic information.

To retrieve log information use the `/diag` and `/sasl_logs` [REST endpoints](../../../../server/current/rest-api/logs-rest-api.md).

### [](#getting-threshold-details)Getting Threshold Details

The current settings are retrieved by using the `mcctl` cli to execute the `get sla` command:

> [!IMPORTANT]
> These settings only apply to the nodes _where the changes are made._
> 
> You must implement the changes on each node to ensure they are applied across the cluster.
> 
> You must also configure the node to run the `data service`.

Getting threshold details

```bash
/opt/enterprise-analytics/bin/mcctl
get sla
```

Result

```json
{"comment":"Current MCBP SLA configuration",
"version":1,
"default":{"slow":"500 ms"}},
"COMPACT_DB":{"slow":"1800 s"},
"DELETE_BUCKET":{"slow":"10 s"},
"SEQNO_PERSISTENCE":{"slow":"30 s"}
}
```

The JSON message returned gives details of the operation being logged and the threshold time that will cause a timing message to be logged.