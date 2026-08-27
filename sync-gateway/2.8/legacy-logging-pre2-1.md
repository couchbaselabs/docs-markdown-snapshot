---
title: Log Rotation [DEPRECATED]
description: This log rotation content was deprecated in Sync Gateway.1 and
  applies only to pre-2.1 versions.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/legacy-logging-pre2-1.adoc
  xref: xref:2.8@sync-gateway::legacy-logging-pre2-1.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/legacy-logging-pre2-1.html)

# Log Rotation [DEPRECATED]

> This log rotation content was deprecated in Sync Gateway.1 and applies only to pre-2.1 versions. 

## [](#built-in-log-rotation)Built-in log rotation

By default, Sync Gateway outputs the logs to standard out with the "HTTP" log key and can also output logs to a file. Prior to 1.4, the two main configuration options were `log` and `logFilePath` at the root of the configuration file.

```javascript
{
    "log": ["*"],
    "logFilePath": "/var/log/sync_gateway/sglogfile.log"
}
```

In Couchbase Mobile 1.4, Sync Gateway can now be configured to perform log rotation in order to minimize disk space usage.

### [](#log-rotation-configuration)Log rotation configuration

The log rotation configuration is specified under the `logging` key. The following example demonstrates where the log rotation properties reside in the configuration file.

```javascript
{
  "logging": {
    "default": {
      "logFilePath": "/var/log/sync_gateway/sglogfile.log",
      "logKeys": ["*"],
      "logLevel": "debug",
      "rotation": {
        "maxsize": 1,
        "maxage": 30,
        "maxbackups": 2,
        "localtime": true
      }
    }
  },
  "databases": {
    "db": {
      "server": "http://localhost:8091",
      "bucket": "default",
      "users": {"GUEST": {"disabled": false,"admin_channels": ["*"]}}
    }
  }
}
```

As shown above, the `logging` property must contain a single named logging appender called `default`. Note that if the "logging" property is specified, it will override the top level `log` and `logFilePath` properties.

The descriptions and default values for each logging property can be found on the [Sync Gateway configuration](configuration-properties.md) page.

### [](#example-output)Example Output

If Sync Gateway is running with the configuration shown above, after a total of 3.5 MB of log data, the contents of the `/var/log/sync_gateway` directory would have 3 files because `maxsize` is set to 1 MB.

```bash
/var/log/sync_gateway
├── sglogfile.log
├── sglogfile-2017-01-25T23-35-23.671.log
└── sglogfile-2017-01-25T22-25-39.662.log
```

### [](#windows-configuration)Windows Configuration

On MS Windows `logFilePath` supports the following path formats.

```javascript
"C:/var/tmp/sglogfile.log"
`C:\var\tmp\sglogfile.log`
`/var/tmp/sglogfile.log`
"/var/tmp/sglogfile.log"
```

Log rotation will not work if `logFilePath` is set to the path below as it is reserved for use by the Sync Gateway Windows service wrapper.

```bash
C:\Program Files (x86)\Couchbase\var\lib\couchbase\logs\sync_gateway_error.log
```

### [](#deprecation-notice)Deprecation notice

The current proposal is to remove the top level `log` and `logFilePath` properties in Sync Gateway 2.0\. For users that want to migrate to the new logging config to write to a log file but do not need log rotation they should use a default logger similar to the following:

```javascript
{
    "logging": {
        "default": {
            "logFilePath": "/var/log/sync_gateway/sglogfile.log",
            "logKeys": ["*"],
            "logLevel": "debug"
        }
    }
}
```

## [](#os-log-rotation)OS log rotation

In production environments it is common to rotate log files to prevent them from taking too much disk space, and to support log file archival.

By default Sync gateway will write log statements to stderr, normally stderr is redirected to a log file by starting Sync Gateway with a command similar to the following:

```bash
sync_gateway sync_gateway.json 2>> sg_error.log
```

On Linux the logrotate tool can be used to monitor log files and rotate them at fixed time intervals or when they reach a certain size. Below is an example of a logrotate configuration that will rotate the Sync Gateway log file once a day or if it reaches 10M in size.

```none
/home/sync_gateway/logs/*.log {
    daily
    rotate 1
    size 10M
    delaycompress
    compress
    notifempty
    missingok
```

The log rotation is achieved by renaming the log file with an appended timestamp. The idea is that Sync Gateway should recreate the default log file and start writing to it again. The problem is Sync Gateway will follow the renamed file and keep writing to it until Sync gateway is restarted. By adding the copy truncate option to the logrotate configuration, the log file will be rotated by making a copy of the log file, and then truncating the original log file to zero bytes.

```none
/home/sync_gateway/logs/*.log {
    daily
    rotate 1
    size 10M
    copytruncate
    delaycompress
    compress
    notifempty
    missingok
}
```

Using this approach there is a possibility of loosing log entries between the copy and the truncate, on a busy Sync Gateway instance or when verbose logging is configured the number of lost entries could be large.

In Sync Gateway 1.1.0 a new configuration option has been added that gives Sync Gateway control over the log file rather than relying on **stderr**. To use this option call Sync Gateway as follows:

```bash
sync_gateway -logFilePath=sg_error.log sync_gateway.json
```

The **logFilePath** property can also be set in the configuration file at the [server level](../current/configuration/configuration-properties-legacy.md#server-configuration).

If the option is not used then Sync Gateway uses the existing stderr logging behavior. When the option is passed Sync Gateway will attempt to open and write to a log file at the path provided. If a Sync Gateway process is sent the `SIGHUP` signal it will close the open log file and then reopen it, on Linux the `SIGHUP` signal can be manually sent using the following command:

```bash
pkill -HUP sync_gateway
```

This command can be added to the logrotate configuration using the 'postrotate' option:

```none
/home/sync_gateway/logs/*.log {
    daily
    rotate 1
    size 10M
    delaycompress
    compress
    notifempty
    missingok
    postrotate
        /usr/bin/pkill -HUP sync_gateway > /dev/null
    endscript
}
```

After renaming the log file logrotate will send the `SIGHUP` signal to the `sync_gateway` process, Sync Gateway will close the existing log file and open a new file at the original path, no log entries will be lost.