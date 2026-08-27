---
title: SG Collect Info
description: Using <em>sgcollect_info</em> to gather system information,
  diagnostics and metrics
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/manage/pages/sgcollect-info.adoc
  xref: xref:sync-gateway:manage:sgcollect-info.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/manage/sgcollect-info.html)

# SG Collect Info

> Using _sgcollect\_info_ to gather system information, diagnostics and metrics  
> This topic describes the command line utility, _sgcollect\_info_, its use and the output it collates.

> [!IMPORTANT]
> Constraints
> 
> Do not use the `logs` directory as a storage location for files that should not be there. Permission issues with those files can prevent Sync Gateway from starting.

## [](#introduction)Introduction

The command line utility `sgcollect_info` provides detailed statistics for a specific Sync Gateway node. This tool must be run on each node individually, not on all simultaneously.

`sgcollect_info` outputs the following statistics in a zip file:

1. Logs
2. Configuration
3. Expvars (exported variables) that contain important stats
4. System Level OS stats
5. Golang profile output (runtime memory and cpu profiling info)

## [](#cli-command-and-parameters)CLI Command and Parameters

To see the CLI command line parameters, run:

```bash
./sgcollect_info --help
```

In Sync Gateway 3.3 and later, the `--sync-gateway-password` option has been removed from `sgcollect_info` as a security precaution. When you specify the `--sync-gateway-username` option, `sgcollect_info` prompts you to enter the password interactively. Attempting to use the `--sync-gateway-password` option causes an error, with instructions for next steps.

Alternatively, you can specify credentials using the `SG_USERNAME` and `SG_PASSWORD` environment variables to avoid the prompt.

You can use `sgcollect_info` to collect and save information locally, or to collect and upload the information to Couchbase — see: [Example 1](#ex-collect).

Example 1\. Using sgcollect\_info

* Collect and Save Locally
* Collect and Upload to Couchbase

```bash
./sgcollect_info \
  --sync-gateway-url=https://127.0.0.1:4985 \
  --sync-gateway-username=Admin \
  /tmp/sgcollect_info.zip
```

When prompted, enter the password.

Collect Sync Gateway diagnostics and upload them to Couchbase Support:

```bash
./sgcollect_info \
  --sync-gateway-url=https://127.0.0.1:4985 \
  --sync-gateway-username=Admin \
  --log-redaction-level=partial \
  --upload-host=uploads.couchbase.com \
  --customer=Acme \
  --ticket=123 \
  /tmp/sgcollect_info.zip
```

When prompted, enter the password.

## [](#rest-endpoint)REST Endpoint

You can also run `sgcollect_info` from the Admin REST API using the [\_sgcollect\_info](../rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/post%5F%5Fsgcollect%5Finfo) endpoint.

## [](#zipfile-contents)Zipfile Contents

The tool creates the following log files in the output file.

| Log file                          | Description                                                                                                                                           |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| sync\_gateway\_access.log         | The http access log for sync gateway (i.e which GETs and PUTs it has received and from which IPs)                                                     |
| sg\_accel\_access.log             | The http access log for sg\_accel (i.e which GETs and PUTs it has received and from which IPs)                                                        |
| sg\_accel\_error.log              | The error log (all logging sent to stderr by sg\_accel) for the sg\_accel process                                                                     |
| sync\_gateway\_error.log          | The error log (all logging sent to stderr by sync\_gateway) for the sync\_gateway process                                                             |
| server\_status.log                | The output of http://localhost:4895 for the running sync gateway                                                                                      |
| db\_db\_name\_status.log          | The output of http://localhost:4895/db\_name for the running sync gateway                                                                             |
| sync\_gateway.json                | The on-disk configuration file used by sync\_gateway when it was launched                                                                             |
| sg\_accel.json                    | The on-disk configuration file used by sg\_accel when it was launched                                                                                 |
| running\_server\_config.log       | The configuration used by sync gateway as it is running (may not match the on-disk config as it can be changed on-the-fly)                            |
| running\_db\_db\_name\_config.log | The config used by sync gateway for the database specified by db\_name                                                                                |
| expvars\_json.log                 | The expvars (global exposed variables - see <https://www.mikeperham.com/2014/12/17/expvar-metrics-for-golang/> for the running sync gateway instance) |
| sgcollect\_info\_options.log      | The command line arguments passed to sgcollect\_info for this particular output                                                                       |
| sync\_gateway.log                 | OS-level System Stats                                                                                                                                 |
| expvars\_json.log                 | Exported Variables (expvars) from Sync Gateway which show runtime stats                                                                               |
| goroutine.pdf/raw/txt             | Goroutine pprof profile output                                                                                                                        |
| heap.pdf/raw/txt                  | Heap pprof profile output                                                                                                                             |
| profile.pdf/raw/txt               | CPU profile pprof profile output                                                                                                                      |
| syslog.tar.gz                     | System level logs like /var/log/dmesg on Linux                                                                                                        |
| sync\_gateway                     | The Sync Gateway binary executable                                                                                                                    |
| pprof\_http\_\*.log               | The pprof output that collects directly via an http client rather than using go tool, in case Go is not installed                                     |

### [](#file-concatenation)File Concatenation

SGCollect Info has been updated to use the [continuous logging](logging.md#continuous-logging) feature introduced in 2.1, and collects the four leveled files (**sg\_error.log**, **sg\_warn.log**, **sg\_info.log** and **sg\_debug.log**).

These new log files are rotated and compressed by Sync Gateway, so `sgcollect_info` decompresses these rotated logs, and concatenates them back into a single file upon collection.

For example, if you have **sg\_debug.log**, and **sg\_debug-2018-04-23T16-57-13.218.log.gz** and then run `sgcollect_info` as normal, both of these files get put into a **sg\_debug.log** file inside the zip output folder.

## [](#log-redaction)Log Redaction

SGCollect Info now supports log redaction post-processing. In order to utilize this, Sync Gateway needs to be run with the `logging.redaction_level` property set to "partial".

Two new command line options have been added to `sgcollect_info`:

* `--log-redaction-level=REDACT_LEVEL`: redaction level for the logs collected, `none` and `partial` supported. Defaults to `none`.  
When `--log-redaction-level` is set to partial, two zip files are produced, and tagged contents in the redacted one should be hashed in the same way as `cbcollect_info`:  
```bash  
$ ./sgcollect_info --log-redaction-level=partial sgout.zip  
...  
Zipfile built: sgout-redacted.zip  
Zipfile built: sgout.zip  
```
* `--log-redaction-salt=SALT_VALUE`: salt used in the hashing of tagged data when enabling redaction. Defaults to a random uuid.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)