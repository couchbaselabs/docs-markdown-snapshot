---
title: Using the Command Line
description: Start a Sync Gateway instance using command line options and
  securely sync enterprise data from cloud to edge
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/command-line-options.adoc
  xref: xref:3.1@sync-gateway::command-line-options.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/command-line-options.html)

# Using the Command Line

> Start a Sync Gateway instance using command line options and securely sync enterprise data from cloud to edge  
> Introduces the options available when running Sync Gateway from the command line

Related _Deploy_ topics: [Deployment](deployment.md) | [REST API Access](rest-api-access.md) | [Bootstrap Configuration](configuration-schema-bootstrap.md)

## [](#overview)Overview

You can configure some _Sync Gateway_ features by specifying command-line options when you start it.

For more comprehensive configuration options see: [Configuration Overview](configuration-overview.md)

## [](#configuration)Configuration

Configuration determines the runtime behavior of Sync Gateway, including server configuration and the database or set of databases with which a sync gateway instance can interact.

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

The command-line options that can be used when starting Sync Gateway are outlined in [Table 1](#cmd-opts-starter-cfg) and [Table 2](#cmd-opts-other).

__Table 1\. Configuration-related CLI flags__
| Option                                                | Default | Description                                                                                                                                                                                                                                                                         |
| ----------------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \-bootstrap.group\_id                                 |         | The config group ID to use when discovering databases. Allows for non-homogenous configuration                                                                                                                                                                                      |
| \-bootstrap.config\_update\_frequency                 |         | How often to poll Couchbase Server for new config changes                                                                                                                                                                                                                           |
| \-bootstrap.server                                    |         | Couchbase Server connection string/URL The connection must point to a node running the data service.                                                                                                                                                                                |
| \-bootstrap.username                                  |         | Username for authenticating to server                                                                                                                                                                                                                                               |
| \-bootstrap.password                                  |         | Password for authenticating to server                                                                                                                                                                                                                                               |
| \-bootstrap.ca\_cert\_path                            | none    | Root CA certificate path                                                                                                                                                                                                                                                            |
| \-bootstrap.x509\_cert\_path                          | none    | Client certificate path                                                                                                                                                                                                                                                             |
| \-bootstrap.x509\_key\_path                           | none    | Client private key path                                                                                                                                                                                                                                                             |
| \-bootstrap.server\_tls\_skip\_verify                 | false   | Set to ignore certificate validation — development and testing mode **only**                                                                                                                                                                                                        |
| \-bootstrap.use\_tls\_server                          | true    | Forces the connection to Couchbase Server to use TLS.Set to false to allow non-secure protocols for communication with Couchbase Server — development and testing mode **only**                                                                                                     |
| api.public\_interface                                 | :4984   | Network interface to bind public API to                                                                                                                                                                                                                                             |
| api.admin\_interface                                  | :4985   | Network interface to bind admin API to                                                                                                                                                                                                                                              |
| api.metrics\_interface                                | :4986   | Network interface to bind metrics API to                                                                                                                                                                                                                                            |
| api.profile\_interface                                |         | Network interface to bind profiling API to                                                                                                                                                                                                                                          |
| api.admin\_interface\_authentication                  |         | Whether the admin API requires authentication                                                                                                                                                                                                                                       |
| api.metrics\_interface\_authentication                |         | Whether the metrics API requires authentication                                                                                                                                                                                                                                     |
| api.enable\_admin\_authentication\_permissions\_check |         | Whether to enable the DP permissions check feature of admin auth                                                                                                                                                                                                                    |
| api.server\_read\_timeout                             |         | Maximum duration.Second before timing out read of the HTTP(S) request                                                                                                                                                                                                               |
| api.server\_write\_timeout                            |         | Maximum duration.Second before timing out write of the HTTP(S) response                                                                                                                                                                                                             |
| api.read\_header\_timeout                             |         | The amount of time allowed to read request headers                                                                                                                                                                                                                                  |
| api.idle\_timeout                                     |         | The maximum amount of time to wait for the next request when keep-alives are enabled                                                                                                                                                                                                |
| api.pretty                                            |         | Pretty-print JSON responses                                                                                                                                                                                                                                                         |
| api.max\_connections                                  |         | Max number of incoming HTTP connections to accept                                                                                                                                                                                                                                   |
| api.compress\_responses                               |         | If false, disables compression of HTTP responses                                                                                                                                                                                                                                    |
| api.hide\_product\_version                            |         | Whether product versions removed from Server headers and REST API responses                                                                                                                                                                                                         |
| api.https.tls\_minimum\_version                       |         | The minimum allowable TLS version for the REST APIs                                                                                                                                                                                                                                 |
| api.https.tls\_cert\_path                             |         | The TLS certificate filepath to use for the REST APIs                                                                                                                                                                                                                               |
| api.https.tls\_key\_path                              |         | The TLS key filepath to use for the REST APIs                                                                                                                                                                                                                                       |
| api.cors.origin                                       |         | List of comma separated allowed origins. Use '\*' to allow access from everywhere                                                                                                                                                                                                   |
| api.cors.login\_origin                                |         | List of comma separated allowed login origins                                                                                                                                                                                                                                       |
| api.cors.headers                                      |         | List of comma separated allowed headers                                                                                                                                                                                                                                             |
| api.cors.max\_age                                     |         | Maximum age of the CORS Options request                                                                                                                                                                                                                                             |
| logging.log\_file\_path                               |         | Absolute or relative path on the filesystem to the log file directory. A relative path is from the directory that contains the Sync Gateway executable file                                                                                                                         |
| logging.redaction\_level                              |         | Redaction level to apply to log output. Options: none, partial, full, unset                                                                                                                                                                                                         |
| logging.console.enabled                               |         |                                                                                                                                                                                                                                                                                     |
| logging.console.rotation.max\_size                    |         |                                                                                                                                                                                                                                                                                     |
| logging.console.rotation.max\_age                     |         |                                                                                                                                                                                                                                                                                     |
| logging.console.rotation.localtime                    |         |                                                                                                                                                                                                                                                                                     |
| logging.console.rotation.rotated\_logs\_size\_limit   |         |                                                                                                                                                                                                                                                                                     |
| logging.console.collation\_buffer\_size               |         |                                                                                                                                                                                                                                                                                     |
| logging.console.log\_level                            |         | Options: none, error, warn, info, debug, trace                                                                                                                                                                                                                                      |
| logging.console.log\_keys                             | HTTP    | A comma-separated list of log keywords to be enabled.The log keyword HTTP is enabled by default, which means that HTTP requests and error responses are always logged.Omitting HTTP from your list does not disable HTTP logging. You can disable HTTP logging using the Admin API. |
| logging.console.color\_enabled                        |         |                                                                                                                                                                                                                                                                                     |
| logging.console.file\_output                          |         | Can be used to override the default stderr output, and write to the file specified inst                                                                                                                                                                                             |
| logging.error.enabled                                 |         |                                                                                                                                                                                                                                                                                     |
| logging.error.rotation.max\_size                      |         |                                                                                                                                                                                                                                                                                     |
| logging.error.rotation.max\_age                       |         |                                                                                                                                                                                                                                                                                     |
| logging.error.rotation.localtime                      |         |                                                                                                                                                                                                                                                                                     |
| logging.error.rotation.rotated\_logs\_size\_limit     |         |                                                                                                                                                                                                                                                                                     |
| logging.error.collation\_buffer\_size                 |         |                                                                                                                                                                                                                                                                                     |
| logging.warn.enabled                                  |         |                                                                                                                                                                                                                                                                                     |
| logging.warn.rotation.max\_size                       |         |                                                                                                                                                                                                                                                                                     |
| logging.warn.rotation.max\_age                        |         |                                                                                                                                                                                                                                                                                     |
| logging.warn.rotation.localtime                       |         |                                                                                                                                                                                                                                                                                     |
| logging.warn.rotation.rotated\_logs\_size\_limit      |         |                                                                                                                                                                                                                                                                                     |
| logging.warn.collation\_buffer\_size                  |         |                                                                                                                                                                                                                                                                                     |
| logging.info.enabled                                  |         |                                                                                                                                                                                                                                                                                     |
| logging.info.rotation.max\_size                       |         |                                                                                                                                                                                                                                                                                     |
| logging.info.rotation.max\_age                        |         |                                                                                                                                                                                                                                                                                     |
| logging.info.rotation.localtime                       |         |                                                                                                                                                                                                                                                                                     |
| logging.info.rotation.rotated\_logs\_size\_limit      |         |                                                                                                                                                                                                                                                                                     |
| logging.info.collation\_buffer\_size                  |         |                                                                                                                                                                                                                                                                                     |
| logging.debug.enabled                                 |         |                                                                                                                                                                                                                                                                                     |
| logging.debug.rotation.max\_size                      |         |                                                                                                                                                                                                                                                                                     |
| logging.debug.rotation.max\_age                       |         |                                                                                                                                                                                                                                                                                     |
| logging.debug.rotation.localtime                      |         |                                                                                                                                                                                                                                                                                     |
| logging.debug.rotation.rotated\_logs\_size\_limit     |         |                                                                                                                                                                                                                                                                                     |
| logging.debug.collation\_buffer\_size                 |         |                                                                                                                                                                                                                                                                                     |
| logging.trace.enabled                                 |         |                                                                                                                                                                                                                                                                                     |
| logging.trace.rotation.max\_size                      |         |                                                                                                                                                                                                                                                                                     |
| logging.trace.rotation.max\_age                       |         |                                                                                                                                                                                                                                                                                     |
| logging.trace.rotation.localtime                      |         |                                                                                                                                                                                                                                                                                     |
| logging.trace.rotation.rotated\_logs\_size\_limit     |         |                                                                                                                                                                                                                                                                                     |
| logging.trace.collation\_buffer\_size                 |         |                                                                                                                                                                                                                                                                                     |
| logging.stats.enabled                                 |         |                                                                                                                                                                                                                                                                                     |
| logging.stats.rotation.max\_size                      |         |                                                                                                                                                                                                                                                                                     |
| logging.stats.rotation.max\_age                       |         |                                                                                                                                                                                                                                                                                     |
| logging.stats.rotation.localtime                      |         |                                                                                                                                                                                                                                                                                     |
| logging.stats.rotation.rotated\_logs\_size\_limit     |         |                                                                                                                                                                                                                                                                                     |
| logging.stats.collation\_buffer\_size                 |         |                                                                                                                                                                                                                                                                                     |
| auth.bcrypt\_cost                                     |         | Most to use for bcrypt password hashes                                                                                                                                                                                                                                              |
| replicator.max\_heartbeat                             |         | Max heartbeat value for \_changes request                                                                                                                                                                                                                                           |
| replicator.blip\_compression                          |         | LIP data compression level (0-9)                                                                                                                                                                                                                                                    |
| unsupported.stats\_log\_frequency                     |         | How often should stats be written to stats logs                                                                                                                                                                                                                                     |
| unsupported.use\_stdlib\_json                         |         | Bypass the jsoniter package and use Go's stdlib instead                                                                                                                                                                                                                             |
| unsupported.http2.enabled                             |         | Whether HTTP2 support is enabled                                                                                                                                                                                                                                                    |
| max\_file\_descriptors                                |         | Max number of open file descriptors (RLIMIT\_NOFILE)                                                                                                                                                                                                                                |

__Table 2\. Other CLI flags__
| Option                        | Default             | Description                                                                                                                         |
| ----------------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| \-configServer                | none                | URL of server that can return database configs                                                                                      |
| \-dbname                      | sync\_gateway       | Name of the Couchbase Server database to serve through the Public REST API.                                                         |
| \-disable\_persistent\_config | false               | Set this property 'true' to continue using the legacy configuration mode (File-based Configuration)                                 |
| \-defaultLogFilePath          | none                | Path to log files, as a fallback default value when logFilePath is not specified. This option is generally used in service scripts. |
| \-deploymentID                | none                | Customer/project identifier for stats reporting                                                                                     |
| \--help                       | none                | Lists the available options and exits.                                                                                              |
| \-pool                        | default             | Name of the Couchbase Server pool in which to find buckets.                                                                         |
| \-pretty                      | false               | Pretty-print JSON responses to improve readability. This is useful for debugging, but reduces performance.                          |
| \-profileInterface            |                     | Address to bind the profile interface to                                                                                            |
| \-url                         | DefaultServer       | The URL of the database server                                                                                                      |
| \-verbose                     | Non-verbose logging | Logs more information about requests.                                                                                               |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)