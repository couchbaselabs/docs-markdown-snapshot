---
title: Logging
description: Introducing Couchbase Sync Gateway's logging functionality
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/logging.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@sync-gateway::logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/logging.html)

# Logging

> Introducing Couchbase Sync Gateway's logging functionality  
> Sync Gateway's \_Continuous Logging\_ feature delivers flexible log generation and retention, without compromising the availability of diagnostic information necessary to provide effective support and maintenance.

> [!NOTE]
> Constraints
> 
> Do not use the `logs` directory as a storage location for files that should not be there. Permission issues with those files can prevent Sync Gateway from starting.

## [](#overview)Overview

Sync Gateway provides a robust [Continuous Logging](#lbl-continuous-logging)\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] solution that delivers flexibility in terms of how logs are generated and retained, whilst also maintaining the level of logging required by Couchbase Support for investigation of issues. Its logs are written to [separate log files](#log-file-outputs) filtered by log level, with each log level supporting individual retention policies. You control what is logged using the `sync-gateway-config.json` configuration file settings for [logging](configuration-properties.md#logging).

In addition to the log files, you can also independently configure and control [Console Logging](#lbl-console-logs), which is a convenient method of accessing diagnostic information during debugging scenarios. With _console logging_, system administrators can easily fine-tune diagnostic output to suit specific debug scenarios. All without interfering with the logging required by Couchbase Support for the investigation of issues.

## [](#configuration)Configuration

You configure your _continuous_ and _console_ logging requirements in the `sync-gateway-config.json` file, using the [logging](configuration-properties.md#logging) properties — see: [Example 1](#sample-log-cfg).

Example 1\. Sample Logging Configuration

```json
{
  "logging": {
    "log_file_path": "/var/tmp/sglogs", (1)
    "redaction_level": "partial", (2)
    "console": { (3)
      "log_level": "debug",
      "log_keys": ["*"]
      }, (4)
    "error": { (5)
      "enabled": true,
      "rotation": {
        "max_size": 20,
        "max_age": 180
        }
      },
    "warn": { (6)
      "enabled": true,
      "rotation": {
        "max_size": 20,
        "max_age": 90
        }
      },
    "info": { (7)
      "enabled": false
    },
    "debug": { (8)
      "enabled": false
      }
    },
  "databases": {
    "db": {
      "server": "couchbase://localhost",
      "username": "username",
      "password": "password",
      "bucket": "default",
      "users": {"GUEST": {"disabled": false,"admin_channels": ["*"]}},
      "allow_conflicts": false,
      "revs_limit": 20
      }
    }
  }
```

| **1** | Set the path to the log file(s)                                                                                                                                                                                                                                    |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | Define the optional redaction level, here we select "partial" redaction — see: [Log Redaction](#lbl-log-redaction)                                                                                                                                                 |
| **3** | Here we define the [Console Logging](#lbl-console-logs) levels we require for debugging. In this instance turning on _debug_ level output for _all_ available log\_keys — see: [console log](configuration-properties.md#logging-console) configuration properties |
| **4** | The following logging properties enable, or disable, [Continuous Logging](#lbl-continuous-logging) at the specified level — see: [continuous logging](configuration-properties.md#logging-$level) configuration properties:                                        |
| **5** | Here we set error level logging on and define the log-file rotation, for _errors_ messages                                                                                                                                                                         |
| **6** | Here we set warn level logging on and define the log-file rotation, for _warnings_ messages                                                                                                                                                                        |
| **7** | Here we set info level logging off; we do not define the log-file rotation                                                                                                                                                                                         |
| **8** | Here we set debug level logging off; we do not define the log-file rotation                                                                                                                                                                                        |

See: [Configuration Properties](../current/configuration/configuration-properties-legacy.md) for more information on these settings.

## [](#lbl-log-redaction)Log Redaction

All log outputs — _console_ or _continuous_ — can optionally be redacted, which will remove any user-data considered private.

You enable this feature by setting the [\`logging.redaction\_level\`](configuration-properties.md#logging-redaction%5Flevel) property.

## [](#lbl-console-logs)Console Logging

**In this section**: [Log Levels](#lbl-log-levels) | [Admin REST API](#lbl-log-api) | [Log Keys](#lbl-log-keys) | [Set Log Color](#lbl-log-color) | [Redirect Console Log](#lbl-log-redirect)

> [!TIP]
> By default only HTTP logging is enabled

Console logs are your go-to resource for diagnostic information. You can easily fine-tune their diagnostic content to meet the needs of a particular debugging scenario, perhaps by increasing the verbosity and filtering out unnecessary log\_keys to better focus on the problem area.

Changes to _console logging_ are independent of continuous logging, so you can, for example, tweak any of the following without compromising the core continuous logging streams:

* Increase the verbosity using [Log Levels](#lbl-log-levels) to generate additional diagnostic information
* Focus on the area under investigation by enabling or disabling specific [Log Keys](#lbl-log-keys)
* Enhance readability by setting a [color](#log-color) for log output based on log level

### [](#lbl-log-api)Admin REST API

You can define console log settings in the configuration file, or more conveniently, you can use the Admin REST API to adjust them — see: [Example 2](#eg-setloggingwithapi).

Example 2\. Setting log\_level and log\_keys with API

```console
curl --location --request POST 'http://localhost:4985/_logging?logLevel=trace' \ (1)
--header 'Content-Type: application/json' \
--data-raw '{"HTTP":false, "WS": true, "WSFrame": true, "Replicate": true}' (2)
```

| **1** | Here we define the _log\_level_ to be trace for maximum verbosity                                                    |
| ----- | -------------------------------------------------------------------------------------------------------------------- |
| **2** | Here we specify the particular _log\_keys_ we want to focus on; perhaps we suspect a websocket or replication issue? |

The console log will show the following after this command:

```console
2021-01-08T13:26:23.884Z [INF] HTTP:  #110: POST /_logging?logLevel=trace (as ADMIN)
2021-01-08T13:26:23.885Z [INF] Setting log level to: trace
2021-01-08T13:26:23.885Z [INF] Setting log keys to: [DCP Replicate WS WSFrame]
---
```

### [](#lbl-log-levels)Log Levels

> [!TIP]
> When debugging, setting the _console log's_ log-level to `debug` or `trace` can provide valuable additional information

Console logs have six levels of verbosity — see: [Table 1](#tbl-loglevels). The default _log level_ is **`info`**

Note that the log levels are inclusive, so if you enable `info` level, then `warn` and `error` logs are also enabled.

You can define console log levels using the configuration file (see [logging-console-log\_level](configuration-properties.md#logging-console-log%5Flevel)) and by using the Admin REST API (see: [Example 2](#eg-setloggingwithapi)).

One approach might be to set your base level in the configuration file and then use the Admin REST API for specific debugging scenarios.

__Table 1\. Console Logging — Available Log Levels__
| Log Level | Appearance | Description                                                            |
| --------- | ---------- | ---------------------------------------------------------------------- |
| none      | \-         | Disables log output                                                    |
| error     | \[ERR\]    | Displays errors that need urgent attention                             |
| warn      | \[WRN\]    | Displays warnings that need some attention                             |
| info      | \[INF\]    | Displays information about normal operations that don't need attention |
| debug     | \[DBG\]    | Displays verbose output that might be useful when debugging            |
| trace     | \[TRC\]    | Displays extremely verbose output that might be useful when debugging  |

### [](#lbl-log-keys)Log Keys

> [!TIP]
> Select log keys relevant to the area you are debugging, providing them as a comma-delimited list, such as: `"log_keys": ["HTTP", "CRUD", "Import"]` in the config or see [Example 2](#eg-setloggingwithapi) for how to provide them using the Admin REST API.

Log keys provide fine-grained control over the information types that Sync Gateway outputs to the console log. By default, only **`HTTP`** related information is enabled, but a range of other keys are available to meet specific diagnostic needs — see: [Table 2](#tbl-logkeylist).

You can define the required [\`logging.console.log\_keys\`](configuration-properties.md#logging-console-log%5Fkeys) within your configuration file and-or use the Admin REST API (see: [Example 2](#eg-setloggingwithapi)).

__Table 2\. List of Available Log Keys__
| Log Key    | Description                                                                                                                                                                                                                                                                                            |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| \*         | This wildcard log key, enables all log keys curl --location --request PUT 'http://localhost:4985/\_logging?logLevel=trace' \\ \--header 'Content-Type: application/json' \\ \--data-raw '{"\*": true}'                                                                                                 |
| none       | Disable all log keys; no logging output curl --location --request PUT 'http://localhost:4985/\_logging?logLevel=trace' \\ \--header 'Content-Type: application/json' \\ \--data-raw '{"none": true}'                                                                                                   |
| Admin      | Admin processes in Sync Gateway.                                                                                                                                                                                                                                                                       |
| Access     | Anytime an access() call is made in the sync function.                                                                                                                                                                                                                                                 |
| Auth       | Authentication.                                                                                                                                                                                                                                                                                        |
| Bucket     | Sync Gateway interactions with the bucket (trace level only).                                                                                                                                                                                                                                          |
| Cache      | Interactions with Sync Gateway's in-memory channel cache.                                                                                                                                                                                                                                              |
| Changes    | Processing of /{db}/\_changes requests.                                                                                                                                                                                                                                                                |
| CRUD       | Updates made by Sync Gateway to documents.                                                                                                                                                                                                                                                             |
| DCP        | DCP-feed processing.                                                                                                                                                                                                                                                                                   |
| Events     | Event processing (webhooks).                                                                                                                                                                                                                                                                           |
| gocb       | All logging emitted by the GoCB SDK                                                                                                                                                                                                                                                                    |
| HTTP       | All requests made to the Sync Gateway REST APIs.                                                                                                                                                                                                                                                       |
| HTTP+      | Additional information about HTTP requests (response times, status codes).                                                                                                                                                                                                                             |
| Import     | Introduced in Sync Gateway 1.5 to help troubleshoot the import process of a document (this is the Sync Gateway process to make a document that was added through N1QL or the Server SDKs mobile-aware). This log key can be useful to troubleshoot why a given document was not successfully imported. |
| Javascript | All logging from Javascript. This includes: sync function, import filters, webhook filter function, and the custom ISGR conflict resolvers                                                                                                                                                             |
| Migrate    | Logs messages that show when old inline document metadata is upgraded to xattrs                                                                                                                                                                                                                        |
| Query      | Query is used for Sync Gateway code related to N1QL queries                                                                                                                                                                                                                                            |
| Replicate  | Log messages related to replications between Sync Gateways (using sg-replicate). This tag cannot be used for replications initiated by Couchbase Lite.                                                                                                                                                 |
| SGCluster  | Log messages related to the sharded import and HA sg-replicate                                                                                                                                                                                                                                         |
| Sync       | Activity which relates to synchronization between Couchbase Lite and Sync Gateway                                                                                                                                                                                                                      |
| SyncMsg    | Can be used for additional Sync logging output                                                                                                                                                                                                                                                         |
| WS         | Websocket replication log messages                                                                                                                                                                                                                                                                     |
| WSFrame    | Can be used for additional WS logging output                                                                                                                                                                                                                                                           |

### [](#lbl-log-color)Set Log Color

You may set a color for log output based on log level by using [\`logging.console.color\_enabled\`](configuration-properties.md#logging-console-color%5Fenabled) set to `true`

> [!NOTE]
> This setting is always disabled on Windows for compatibility reasons.

### [](#lbl-log-redirect)Redirect Console Log

You can easily redirect the console log output to a file. This can be useful not only for diagnostic sessions, but also when you have specialized logging requirements, such as centralized logging. Just redirect the output and then apply your own log collection mechanism to feed that data elsewhere — see [Example 3](#eg-console-log-redirect).

Example 3\. Console Log Redirection

```console
# Start Sync Gateway and redirect console output to a file
./sync-gateway > my_sg_logs.txt 2>&1

# Start log collection to send to a centralized log aggregator.
logcollector my_sg_logs.txt
```

## [](#lbl-continuous-logging)Continuous Logging

**In this section**: [Log File Outputs](#lbl-logoutputs) | [Log File Rotation](#lbl-logrotate)

_Continuous logging_ produces a set of log files aimed primarily at providing appropriate diagnostic information for the Couchbase Support team should their intervention be required. You define continuous logging settings in the configuration file — see: [Example 1](#sample-log-cfg).

With continuous logging the logs for each level are written to [separate log files](#lbl-logoutputs) — see: [Table 3](#tbl-contlogoutputs). You can set individual retention policies for each log-level.

### [](#lbl-logoutputs)Log File Outputs

The log files output from continuous logging are intended **solely** for the use of _Couchbase Support_.

> [!TIP]
> If you require special log handling, for example for centralized logging, then use the [Redirect Console Log](#lbl-log-redirect) feature to create a log file for this purpose from the console output stream.

Sync Gateway produces four separate log files, split by log level. Each log file has its own guaranteed retention period - as shown in [Table 3](#tbl-contlogoutputs)

You can collect the log files, for analysis by Couchbase Support when diagnosing Sync Gateway issues, using [SG Collect](../current/manage/sgcollect-info.md).

__Table 3\. Continous Logging - Log File Outputs__
| Log File | Level                                                | Description   | Default enabled | Default max\_age | Minimum max\_age |
| -------- | ---------------------------------------------------- | ------------- | --------------- | ---------------- | ---------------- |
| ERROR    | Critical error messages.                             | sg\_error.log | true            | 360 Days         | 180 Days         |
| WARN     | Something is wrong but SG can still service requests | sg\_warn.log  | true            | 180 Days         | 90 Days          |
| INFO     | Important diagnostics for support and customers      | sg\_info.log  | true            | 6 Days           | 3 Days           |
| DEBUG    | Lower level development analysis                     | sg\_debug.log | false           | 2 Days           | 1 Day            |

> [!TIP]
> Each log level and its parameters are defined using the [logging.$level](configuration-properties.md#logging-$level) property.

### [](#lbl-logrotate)Log File Rotation

Log files are _rotated_ when they exceed a threshold `max_size` (megabytes). Once rotated, they are compressed (gzip) to reduce the disk usage.

Aged logs are cleaned up once their age exceeds `max_age` days — see: [Table 3](#tbl-contlogoutputs)

Configure log rotation using the [logging-$level-rotation](configuration-properties.md#logging-$level-rotation) property.

For pre-2.1 log rotation — see: [Log Rotation pre-2.1](#sync-gateway::legacy-logging-pre2-1.adoc)

## [](#related-content)Related Content

###### [](#)

API Topics

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-2)

Reference

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

---

[1](#%5Ffootnoteref%5F1). Introduced in Sync Gateway version 2.1