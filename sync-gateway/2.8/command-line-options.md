---
title: Using the Command Line
description: Start a Sync Gateway instance using command line options and
  securely sync enterprise data from cloud to edge
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/command-line-options.adoc
  xref: xref:2.8@sync-gateway::command-line-options.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/command-line-options.html)

# Using the Command Line

> Start a Sync Gateway instance using command line options and securely sync enterprise data from cloud to edge  
> Introduces the options available when running Sync Gateway from the command line

Related _Deploy_ topics: [Deploy](../current/deploy/deployment.md) | [REST API Access](../current/rest-api/rest-api-access.md) | [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

## [](#overview)Overview

You can configure some Sync Gateway features by specifying command-line options when you start it.

For more comprehensive configuration, use a JSON configuration file - see: [Configuration Properties](../current/configuration/configuration-properties-legacy.md).

## [](#configuration)Configuration

Configuration determines the runtime behavior of Sync Gateway, including server configuration and the database or set of databases with which a Sync Gateway instance can interact.

> [!NOTE]
> Command-line options can only specify a sub-set of the available configuration properties, and cannot be used to configure multiple databases.

Two command-line options do not have corresponding configuration properties: `-help` and `-verbose`.

## [](#option-format)Option Format

When specifying command-line options use the format shown in [Example 1](#option-fmt)

* Command-line options are case-insensitive.
* You can prefix command-line options with one hyphen (-) or with two hyphens (--).
* For command-line options that take an argument, you specify the argument after an equal sign (=).  
For example, `-bucket=db`, or as a following item on the command line, for example, `-bucket db`.

Example 1\. Command line options

* Format
* List CLI Arguments

When specifying command-line options use this format:

```bash
sync_gateway [ -{option} ]
```

| **1** | Seperate multiple options by a comma or a space |
| ----- | ----------------------------------------------- |

You can check the latest position by navigating to the folder containing the Sync Gateway executable and using:

```bash
$ ./sync_gateway -help (1)
```

| **1** | This command lists all Sync Gateway's current command line arguments |
| ----- | -------------------------------------------------------------------- |

## [](#available-options)Available Options

The following command-line options can be used when starting Sync Gateway see [Table 1](#cmd-opts)

> [!WARNING]
> **Deprecation Notice**
> 
> The `-bucket` command line option, deprecated at Release 2.7, will be removed following release 2.8.  
> Use the JSON configuration file option `bucket` — see [this\_db\_bucket](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-bucket).

__Table 1\. Available command-line options__
| Option               | Default             | Description                                                                                                                                                                                                                                                                         |
| -------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ‑adminInterface      | 127.0.0.1:4985      | Port or TCP network address (IP address and the port) that the Admin REST API listens on.                                                                                                                                                                                           |
| \-bucket             | sync\_gateway       | **_Deprecated_** Name of the Couchbase Server bucket.Instead use [this\_db\_bucket](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-bucket)                                                                                                         |
| \-cacertpath         | none                | Root CA certificate path                                                                                                                                                                                                                                                            |
| \-certpath           | none                | Client certificate path                                                                                                                                                                                                                                                             |
| \-configServer       | none                | URL of server that can return database configs                                                                                                                                                                                                                                      |
| \-dbname             | sync\_gateway       | Name of the Couchbase Server database to serve through the Public REST API.                                                                                                                                                                                                         |
| \-defaultLogFilePath | none                | Path to log files, as a fallback default value when logFilePath is not specified. This option is generally used in service scripts.                                                                                                                                                 |
| \-deploymentID       | none                | Customer/project identifier for stats reporting                                                                                                                                                                                                                                     |
| \--help              | none                | Lists the available options and exits.                                                                                                                                                                                                                                              |
| \-interface          | :4984               | Port or TCP network address (IP address and the port) that the Public REST API listens on.                                                                                                                                                                                          |
| \-keypath            | none                | Client certificate key path                                                                                                                                                                                                                                                         |
| \-log                | HTTP                | A comma-separated list of log keywords to be enabled.The log keyword HTTP is enabled by default, which means that HTTP requests and error responses are always logged.Omitting HTTP from your list does not disable HTTP logging. You can disable HTTP logging using the Admin API. |
| \-logFilePath        | none                | Path to log files.                                                                                                                                                                                                                                                                  |
| \-pool               | default             | Name of the Couchbase Server pool in which to find buckets.                                                                                                                                                                                                                         |
| \-pretty             | false               | Pretty-print JSON responses to improve readability. This is useful for debugging, but reduces performance.                                                                                                                                                                          |
| \-profileInterface   |                     | Address to bind the profile interface to                                                                                                                                                                                                                                            |
| \-url                | DefaultServer       | The URL of the database server                                                                                                                                                                                                                                                      |
| \-verbose            | Non-verbose logging | Logs more information about requests.                                                                                                                                                                                                                                               |

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