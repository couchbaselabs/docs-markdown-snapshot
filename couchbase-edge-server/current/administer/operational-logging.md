---
title: Operational Logging
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.1/modules/administer/pages/operational-logging.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-edge-server:administer:operational-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/current/administer/operational-logging.html)

# Operational Logging

## [](#file-based-logging)File-Based Logging

File-based logging creates multiple log files in the configured directory, one per level. The naming scheme is `cbl_`, the log level, the creation timestamp, `.cbllog`.

Log files are rotated (a new file created) when they reach the `maxSize` or when the server restarts. There will be up to `rotateCount` \+ 1 files of each log level; older files are deleted.

Keeping a separate file for each log level makes log rotation more effective: Logs of the important but less common levels `warning` and `error` will be kept around longer, since their log files grow more slowly.

The binary format is recommended because it is significantly faster to write, and more compact.

Log files can be read with the `cbl-log` tool. It decodes the binary format and merges all the log levels together sorted by timestamp.

Couchbase Lite groups log messages into named **domains** based on their subject. Common log domains are "Default", "REST", "Listener", "DB", "Query", "Sync".

The "REST" domain is used by the HTTP server to log client connections and requests. Its default level is "info", since a server typically logs these.

Other domains default to "warning", i.e. they log only warnings and errors, but for troubleshooting purposes the `--verbose` CLI flag overrides this and sets every domain to "info".

You can customize the level of each domain by adding a `domains` object to the logging configuration. Each key is a domain name and its value is the minimum level of messages to log.

### [](#logging-configuration)Logging Configuration

__Table 1\. Logging Configuration Options__
| Key                     | Type          | Value                                                            |
| ----------------------- | ------------- | ---------------------------------------------------------------- |
| domains.domain          | String        | Log level of domain: "error", "warning", "info", "verbose".      |
| console                 | Boolean       | Whether to log to stdout/stderr - default: true.                 |
| file                    | Object        | Configuration for file-based logging - default: none.            |
| file.dir                | String        | Path of directory for log files. **Required for file logging.**  |
| file.format             | String        | Format of log files: binary (default) or text.                   |
| file.maxSize            | Integer       | Size in bytes at which files are rotated, min 1024; default 1MB. |
| file.rotateCount        | Integer       | Number of older log files that are preserved - default 0.        |
| audit                   | Object        | Configuration for audit logging.                                 |
| audit.file              | String        | Filename of audit log.                                           |
| audit.omit\_description | Boolean       | If true, audit events omit their description.                    |
| audit.enable            | Array or "\*" | Array of audit events to enable, "\*" enables all events.        |
| audit.disable           | Array or "\*" | Array of audit events to disable, "\*" disables all events.      |

## [](#see-also)See Also

* [Administer](administer-landing.md)
* [Audit Logging](audit-logging.md)