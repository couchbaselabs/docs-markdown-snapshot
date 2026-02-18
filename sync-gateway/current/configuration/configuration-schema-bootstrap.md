---
title: Bootstrap Configuration
description: Reference data on the contents of Sync Gateway's bootstrap
  configuration, which determines its run time behavior.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/configuration/pages/configuration-schema-bootstrap.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/current/configuration/configuration-schema-bootstrap.html)

# Bootstrap Configuration

> Reference data on the contents of Sync Gateway’s bootstrap configuration, which determines its run time behavior.  

_Related topics_: [Overview](configuration-overview.md) | [Bootstrap](configuration-schema-bootstrap.md) | [Database](configuration-schema-database.md) | [Database Security](configuration-schema-db-security.md) | [Access Control](configuration-schema-access-control.md) | [Import](configuration-schema-import-filter.md) | [Inter-Sync Gateway Replication](configuration-schema-isgr.md)

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#introduction)Introduction

The _Sync Gateway_ bootstrap configuration is provisioned in a JSON format file. The configuration properties define sync gateway’s runtime behavior. See the [schema](#lbl-schema) below for more details on these properties.

Sync gateway will look for the following configuration file unless you direct it otherwise:  
`/home/sync_gateway/sync_gateway.json`

Use the following command to run Sync Gateway with a configuration file:

```bash
sync_gateway sync-gateway-bootstrap.json
```

> [!NOTE]
> For reliable operation, all the nodes listed in the [bootstrap.server](#bootstrap-server) connection string must be data (KV) nodes.

## [](#lbl-schema)Bootstrap Configuration Schema

This schema identifies all the configurable properties.


{
   [api](#api): {
      [admin_interface](#api-admin%5Finterface): "127.0.0.1:4985",
      [admin_interface_authentication](#api-admin%5Finterface%5Fauthentication): true,
      [compress_responses](#api-compress%5Fresponses): true,
      cors: {
         [headers](#api-cors-headers): ["string"...],
         [login_origin](#api-cors-login%5Forigin): ["string"...],
         [max_age](#api-cors-max%5Fage): 0,
         [origin](#api-cors-origin): ["string"...]
      },
      [enable_advanced_auth_dp](#api-enable%5Fadvanced%5Fauth%5Fdp): true,
      [hide_product_version](#api-hide%5Fproduct%5Fversion): true,
      https: {
         [tls_cert_path](#api-https-tls%5Fcert%5Fpath): "string",
         [tls_key_path](#api-https-tls%5Fkey%5Fpath): "string",
         [tls_minimum_version](#api-https-tls%5Fminimum%5Fversion): "tlsv1.2"
      },
      [idle_timeout](#api-idle%5Ftimeout): "90s",
      [max_connections](#api-max%5Fconnections): 0,
      [metrics_interface](#api-metrics%5Finterface): "127.0.0.1:4986",
      [metrics_interface_authentication](#api-metrics%5Finterface%5Fauthentication): true,
      [profile_interface](#api-profile%5Finterface): "string",
      [public_interface](#api-public%5Finterface): ":4984",
      [read_header_timeout](#api-read%5Fheader%5Ftimeout): "5s",
      [server_read_timeout](#api-server%5Fread%5Ftimeout): "string",
      [server_write_timeout](#api-server%5Fwrite%5Ftimeout): "string"
   },
   auth: {
      [bcrypt_cost](#auth-bcrypt%5Fcost): 10
   },
   [bootstrap](#bootstrap): {
      [ca_cert_path](#bootstrap-ca%5Fcert%5Fpath): "string",
      [config_update_frequency](#bootstrap-config%5Fupdate%5Ffrequency): "10s",
      [group_id](#bootstrap-group%5Fid): "default",
      [password](#bootstrap-password): "string",
      [server](#bootstrap-server): "string",
      [server_tls_skip_verify](#bootstrap-server%5Ftls%5Fskip%5Fverify): false,
      [use_tls_server](#bootstrap-use%5Ftls%5Fserver): true,
      [username](#bootstrap-username): "string",
      [x509_cert_path](#bootstrap-x509%5Fcert%5Fpath): "string",
      [x509_key_path](#bootstrap-x509%5Fkey%5Fpath): "string"
   },
   [bucket_credentials](#bucket%5Fcredentials): {
      [{bucketname...}](#bucket%5Fcredentials-{bucketname}): {
         [password](#bucket%5Fcredentials-{bucketname}-password): "string",
         [username](#bucket%5Fcredentials-{bucketname}-username): "string",
         [x509_cert_path](#bucket%5Fcredentials-{bucketname}-x509%5Fcert%5Fpath): "string",
         [x509_key_path](#bucket%5Fcredentials-{bucketname}-x509%5Fkey%5Fpath): "string"
      }
   },
   [database_credentials](#database%5Fcredentials): {
      [{databasename...}](#database%5Fcredentials-{databasename}): {
         [password](#database%5Fcredentials-{databasename}-password): "string",
         [username](#database%5Fcredentials-{databasename}-username): "string",
         [x509_cert_path](#database%5Fcredentials-{databasename}-x509%5Fcert%5Fpath): "string",
         [x509_key_path](#database%5Fcredentials-{databasename}-x509%5Fkey%5Fpath): "string"
      }
   },
   [heap_profile_collection_threshold](#heap%5Fprofile%5Fcollection%5Fthreshold): 0,
   [heap_profile_disable_collection](#heap%5Fprofile%5Fdisable%5Fcollection): false,
   [logging](#logging): {
      [audit](#logging-audit): {
         [audit_log_file_path](#logging-audit-audit%5Flog%5Ffile%5Fpath): "string",
         [enabled](#logging-audit-enabled): false,
         [enabled_events](#logging-audit-enabled%5Fevents): [0...],
         rotation: {
            [localtime](#logging-audit-rotation-localtime): false,
            [max_age](#logging-audit-rotation-max%5Fage): 6,
            [max_size](#logging-audit-rotation-max%5Fsize): 100,
            [rotated_logs_size_limit](#logging-audit-rotation-rotated%5Flogs%5Fsize%5Flimit): 1024,
            [rotation_interval](#logging-audit-rotation-rotation%5Finterval): ""
         }
      },
      console: {
         [collation_buffer_size](#logging-console-collation%5Fbuffer%5Fsize): 10,
         [color_enabled](#logging-console-color%5Fenabled): false,
         [enabled](#logging-console-enabled): false,
         [file_output](#logging-console-file%5Foutput): "string",
         [log_keys](#logging-console-log%5Fkeys): ["CRUD,HTTP,Query"...],
         [log_level](#logging-console-log%5Flevel): "info",
         [rotation](#logging-console-rotation): {
            [localtime](#logging-console-rotation-localtime): false,
            [max_age](#logging-console-rotation-max%5Fage): 0,
            [max_size](#logging-console-rotation-max%5Fsize): 100,
            [rotated_logs_size_limit](#logging-console-rotation-rotated%5Flogs%5Fsize%5Flimit): 1024,
            [rotation_interval](#logging-console-rotation-rotation%5Finterval): ""
         }
      },
      [debug](#logging-debug): {
         [collation_buffer_size](#logging-debug-collation%5Fbuffer%5Fsize): 1000,
         [enabled](#logging-debug-enabled): false,
         rotation: {
            [localtime](#logging-debug-rotation-localtime): false,
            [max_age](#logging-debug-rotation-max%5Fage): 2,
            [max_size](#logging-debug-rotation-max%5Fsize): 100,
            [rotated_logs_size_limit](#logging-debug-rotation-rotated%5Flogs%5Fsize%5Flimit): 1024,
            [rotation_interval](#logging-debug-rotation-rotation%5Finterval): ""
         }
      },
      [error](#logging-error): {
         [collation_buffer_size](#logging-error-collation%5Fbuffer%5Fsize): 0,
         [enabled](#logging-error-enabled): true,
         rotation: {
            [localtime](#logging-error-rotation-localtime): false,
            [max_age](#logging-error-rotation-max%5Fage): 360,
            [max_size](#logging-error-rotation-max%5Fsize): 100,
            [rotated_logs_size_limit](#logging-error-rotation-rotated%5Flogs%5Fsize%5Flimit): 1024,
            [rotation_interval](#logging-error-rotation-rotation%5Finterval): ""
         }
      },
      [info](#logging-info): {
         [collation_buffer_size](#logging-info-collation%5Fbuffer%5Fsize): 0,
         [enabled](#logging-info-enabled): true,
         rotation: {
            [localtime](#logging-info-rotation-localtime): false,
            [max_age](#logging-info-rotation-max%5Fage): 6,
            [max_size](#logging-info-rotation-max%5Fsize): 100,
            [rotated_logs_size_limit](#logging-info-rotation-rotated%5Flogs%5Fsize%5Flimit): 1024,
            [rotation_interval](#logging-info-rotation-rotation%5Finterval): ""
         }
      },
      [log_file_path](#logging-log%5Ffile%5Fpath): "string",
      [redaction_level](#logging-redaction%5Flevel): "partial",
      [stats](#logging-stats): {
         [collation_buffer_size](#logging-stats-collation%5Fbuffer%5Fsize): 0,
         [enabled](#logging-stats-enabled): true,
         rotation: {
            [localtime](#logging-stats-rotation-localtime): false,
            [max_age](#logging-stats-rotation-max%5Fage): 6,
            [max_size](#logging-stats-rotation-max%5Fsize): 100,
            [rotated_logs_size_limit](#logging-stats-rotation-rotated%5Flogs%5Fsize%5Flimit): 1024,
            [rotation_interval](#logging-stats-rotation-rotation%5Finterval): ""
         }
      },
      [trace](#logging-trace): {
         [collation_buffer_size](#logging-trace-collation%5Fbuffer%5Fsize): 1000,
         [enabled](#logging-trace-enabled): false,
         rotation: {
            [localtime](#logging-trace-rotation-localtime): false,
            [max_age](#logging-trace-rotation-max%5Fage): 2,
            [max_size](#logging-trace-rotation-max%5Fsize): 100,
            [rotated_logs_size_limit](#logging-trace-rotation-rotated%5Flogs%5Fsize%5Flimit): 1024,
            [rotation_interval](#logging-trace-rotation-rotation%5Finterval): ""
         }
      },
      [warn](#logging-warn): {
         [collation_buffer_size](#logging-warn-collation%5Fbuffer%5Fsize): 0,
         [enabled](#logging-warn-enabled): true,
         rotation: {
            [localtime](#logging-warn-rotation-localtime): false,
            [max_age](#logging-warn-rotation-max%5Fage): 180,
            [max_size](#logging-warn-rotation-max%5Fsize): 100,
            [rotated_logs_size_limit](#logging-warn-rotation-rotated%5Flogs%5Fsize%5Flimit): 1024,
            [rotation_interval](#logging-warn-rotation-rotation%5Finterval): ""
         }
      }
   },
   [max_file_descriptors](#max%5Ffile%5Fdescriptors): 5000,
   replicator: {
      [blip_compression](#replicator-blip%5Fcompression): 0,
      [max_concurrent_changes_batches](#replicator-max%5Fconcurrent%5Fchanges%5Fbatches): 2,
      [max_concurrent_replications](#replicator-max%5Fconcurrent%5Freplications): 0,
      [max_concurrent_revs](#replicator-max%5Fconcurrent%5Frevs): 5,
      [max_heartbeat](#replicator-max%5Fheartbeat): "string"
   },
   [unsupported](#unsupported): {
      [allow_dbconfig_env_vars](#unsupported-allow%5Fdbconfig%5Fenv%5Fvars): true,
      [diagnostic_interface](#unsupported-diagnostic%5Finterface): "",
      http2: {
         [enabled](#unsupported-http2-enabled): false
      },
      [serverless](#unsupported-serverless): {
         [enabled](#unsupported-serverless-enabled): true,
         [min_config_fetch_interval](#unsupported-serverless-min%5Fconfig%5Ffetch%5Finterval): "1s"
      },
      [stats_log_frequency](#unsupported-stats%5Flog%5Ffrequency): "1m",
      [use_stdlib_json](#unsupported-use%5Fstdlib%5Fjson): false,
      [use_xattr_config](#unsupported-use%5Fxattr%5Fconfig): false
   }
}

#### `api`

Type

object (readOnly)

Description

Configuration settings for modifying how the REST API is interacted with.

#### `api.admin_interface`

Type

string

Default

127.0.0.1:4985

Description

Network interface to bind admin API to.

By default, this will only be accessible to the localhost.

#### `api.admin_interface_authentication`

Type

boolean

Default

true

Description

Whether the admin API requires authentication

#### `api.compress_responses`

Type

boolean

Default

true

Description

If false, disables compression of HTTP responses

#### `api.cors.headers`

Type

array

Description

List of allowed headers. These headers will be added the `Access-Control-Allow-Headers` response to a valid CORS request.

A recommended minimum set of values should be `["Accept-Encoding", "Authorization", "Content-Type", "If-Match"]`.

#### `api.cors.login_origin`

Type

array

Description

List of allowed origins to apply to public `/{db}/_session` API.

To use cors on `/{db}/_session`, the domain must be present in both `login_origin` and `origin`.

If configured, `Authorization` must be included in headers.

#### `api.cors.max_age`

Type

integer

Default

0

Description

Value for `Access-Control-Maximum-Age`. Uses 0 by default.

#### `api.cors.origin`

Type

array

Description

List of allowed origins for the public API. The request `Origin` header is checked against these values. If successful the `Origin` header is returned in the HTTP response header as `Access-Control-Allow-Origin`.

#### `api.enable_advanced_auth_dp`

Type

boolean

Description

Whether to enable the DP permissions check feature of admin auth.

Defaults to `true` if using Enterprise Edition or `false` if using Community Edition.

#### `api.hide_product_version`

Type

boolean

Description

Whether product versions removed from Server headers and REST API responses

#### `api.https.tls_cert_path`

Type

string

Description

The TLS cert file to use for the REST APIs

#### `api.https.tls_key_path`

Type

string

Description

The TLS key file to use for the REST APIs

#### `api.https.tls_minimum_version`

Type

string

Default

tlsv1.2

Description

The minimum allowable TLS version for the REST APIs

#### `api.idle_timeout`

Type

string

Default

90s

Description

The maximum amount of time to wait for the next request when keep-alives are enabled.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `api.max_connections`

Type

number

Default

0

Description

Max of incoming HTTP connections to accept

#### `api.metrics_interface`

Type

string

Default

127.0.0.1:4986

Description

Network interface to bind metrics API to.

By default, this will only be accessible to the localhost.

#### `api.metrics_interface_authentication`

Type

boolean

Default

true

Description

Whether the metrics API requires authentication

#### `api.profile_interface`

Type

string

Description

Network interface to bind profiling API to

#### `api.public_interface`

Type

string

Default

:4984

Description

Network interface to bind public API to

#### `api.read_header_timeout`

Type

string

Default

5s

Description

The amount of time allowed to read request headers.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `api.server_read_timeout`

Type

string

Description

Maximum duration before timing out read of the HTTP(S) request.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `api.server_write_timeout`

Type

string

Description

Maximum duration before timing out write of the HTTP(S) response.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `auth.bcrypt_cost`

Type

integer

Default

10

Description

Cost to use for bcrypt password hashes

#### `bootstrap`

Type

object (readOnly)

Description

Configuration settings for interacting with Couchbase Server.

#### `bootstrap.ca_cert_path`

Type

string

Description

Root CA cert path for TLS connection

#### `bootstrap.config_update_frequency`

Type

string

Default

10s

Description

How often to poll Couchbase Server for new config changes.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `bootstrap.group_id`

Type

string

Default

default

Description

The config group ID to use when discovering databases. Allows for non-homogenous configuration.

#### `bootstrap.password`

Type

string

Description

Password for authenticating to server

#### `bootstrap.server`

Type

string

Description

Couchbase Server connection string/URL for bootstrap configuration. The connection string should only reference Couchbase Server Data (KV) nodes. Using other node types (Query, Index, Analytics, or Search nodes) is not supported. **Connection String Format**Sync Gateway supports the ability to resolve DNS SRV records for alternate hostnames, or specifying multiple hostnames explicitly. See the [Couchbase Go SDK documentation on DNS SRV records](https://docs.couchbase.com/go-sdk/current/howtos/managing-connections.html#using-dns-srv-records) for more details. Sync Gateway supports both the couchbases:// for TLS and couchbase:// schemes for insecure connection. The supported schemes match that of the Couchbase Server SDKs. **Examples of valid server values:**

* `couchbases://nodeA.example.com`
* `couchbase://nodeA.example.com`
* `couchbases://nodeA.example.com,nodeB.example.com`
* `couchbase://nodeA.example.com,nodeB.example.com`
* `couchbases://nodeA.example.com:1234,nodeB.example.com:1234`
* `couchbase://nodeA.example.com:1234,nodeB.example.com:1234`
* `couchbases://127.0.0.1`
* `couchbase://127.0.0.1`On startup, Sync Gateway will try all hostnames until it is able to connect successfully. **Port Information**When using the couchbase:// or couchbases:// schemes, the port is not required as Sync Gateway will use the default Couchbase Server client-to-node ports (11210 for couchbase:// and 11207 for couchbases://). See the [Couchbase Server ports documentation](https://docs.couchbase.com/server/current/install/install-ports.html#ports-listed-by-communication-path) for more details. **Alternate Addresses**If your Couchbase Server cluster is running in a containerized, port mapped, or otherwise NATd environment like Docker or Kubernetes, Sync Gateway might need more information to connect to the cluster. In many cases the client is able to automatically select the correct set of addresses. If the detection heuristic fails in your environment, it is possible to override this behavior by adding a network parameter to the connection string. The network parameter can be:
* `external`: Force the use alternate addresses of Couchbase Server. Used when Sync Gateway should not share network used by Couchbase Server internally.
* `default`: Do not allow use of alternate addresses of Couchbase Server. Used when Sync Gateway and Couchbase Server are on the same network. Example: `"server": "couchbases://my-cbs-server?network=default"`Will force the connection to ignore any alternative external addresses configured on the Couchbase Server node. **Lost Connections**If the connection to Couchbase Server is lost during normal operations, Sync Gateway will automatically re-connect to another node in the cluster.

#### `bootstrap.server_tls_skip_verify`

Type

boolean

Description

Allow empty server CA Cert Path without attempting to use system root pool

#### `bootstrap.use_tls_server`

Type

boolean

Default

true

Description

Enforces a secure or non-secure server scheme

#### `bootstrap.username`

Type

string

Description

Username for authenticating to server.

#### `bootstrap.x509_cert_path`

Type

string

Description

Cert path (public key) for X.509 bucket auth

#### `bootstrap.x509_key_path`

Type

string

Description

Key path (private key) for X.509 bucket auth

#### `bucket_credentials`

Type

object (readOnly)

Description

A map of bucket names to credentials, that can be used instead of the bootstrap ones.

#### `bucket_credentials.{bucketname…​}`

Type

object

Description

The configuration for the credentials set.

#### `bucket_credentials.{bucketname…​}.password`

Type

string

Description

Password for authenticating to the bucket. This value is always redacted.

#### `bucket_credentials.{bucketname…​}.username`

Type

string

Description

Username for authenticating to the bucket

#### `bucket_credentials.{bucketname…​}.x509_cert_path`

Type

string

Description

Cert path (public key) for X.509 bucket auth

#### `bucket_credentials.{bucketname…​}.x509_key_path`

Type

string

Description

Key path (private key) for X.509 bucket auth

#### `database_credentials`

Type

object (readOnly)

Description

A map of database name to credentials, that can be used instead of the bootstrap ones.

#### `database_credentials.{databasename…​}`

Type

object

Description

The configuration for the credentials set.

#### `database_credentials.{databasename…​}.password`

Type

string

Description

Password for authenticating to the bucket. This value is always redacted.

#### `database_credentials.{databasename…​}.username`

Type

string

Description

Username for authenticating to the bucket

#### `database_credentials.{databasename…​}.x509_cert_path`

Type

string

Description

Cert path (public key) for X.509 bucket auth

#### `database_credentials.{databasename…​}.x509_key_path`

Type

string

Description

Key path (private key) for X.509 bucket auth

#### `heap_profile_collection_threshold`

Type

integer (readOnly)

Description

Threshold in bytes for automatic collection of heap profiles. If not specified, defaults to 85% of the lesser of cgroup or system memory.

#### `heap_profile_disable_collection`

Type

boolean (readOnly)

Description

Disables automatic heap profile collection.

#### `logging`

Type

object

Description

The configuration settings for modifying Sync Gateway logging.

#### `logging.audit.audit_log_file_path`

Type

string (readOnly)

Description

The path to write audit log files to

#### `logging.audit.enabled`

Type

boolean

Description

Toggle for this log output

#### `logging.audit.enabled_events`

Type

array (readOnly)

Description

List of enabled global audit events.

#### `logging.audit.rotation.localtime`

Type

boolean

Description

If true, it uses the computer's local time to format the backup timestamp.

#### `logging.audit.rotation.max_age`

Type

integer

Default

6

Description

The maximum number of days to retain old log files.

#### `logging.audit.rotation.max_size`

Type

integer

Default

100

Description

The maximum size in MB of the log file before it gets rotated.

#### `logging.audit.rotation.rotated_logs_size_limit`

Type

integer

Default

1024

Description

Max Size (in mb) of log files before deletion

#### `logging.audit.rotation.rotation_interval`

Type

string

Description

If set, the interval at which log files are rotated, even if max\_size is not reached.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `logging.console.collation_buffer_size`

Type

integer (readOnly)

Default

10

Description

The size of the log collation buffer. The default is 10 if the output is stderr, or 1000 if to a file.

#### `logging.console.color_enabled`

Type

boolean (readOnly)

Description

Log with color for the console output

#### `logging.console.enabled`

Type

boolean (readOnly)

Description

Toggle for this log output

#### `logging.console.file_output`

Type

string (readOnly)

Description

Override the default stderr output, and write to the file specified instead

#### `logging.console.log_keys`

Type

array

Description

Log Keys for the console output

#### `logging.console.log_level`

Type

string

Default

info

Description

Log Level for the console output

#### `logging.console.rotation.localtime`

Type

boolean

Description

If true, it uses the computer's local time to format the backup timestamp.

#### `logging.console.rotation.max_age`

Type

integer

Default

0

Description

The maximum number of days to retain old log files. By default, there is no rotation, max\_age=0.

#### `logging.console.rotation.max_size`

Type

integer

Default

100

Description

The maximum size in MB of the log file before it gets rotated.

#### `logging.console.rotation.rotated_logs_size_limit`

Type

integer

Default

1024

Description

Max Size (in mb) of log files before deletion

#### `logging.console.rotation.rotation_interval`

Type

string

Description

If set, the interval at which log files are rotated, even if max\_size is not reached.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `logging.debug`

Type

object

Description

Debug logging configuration.

#### `logging.debug.collation_buffer_size`

Type

integer (readOnly)

Default

1000

Description

The size of the log collation buffer

#### `logging.debug.enabled`

Type

boolean

Description

Toggle for this log output

#### `logging.debug.rotation.localtime`

Type

boolean

Description

If true, it uses the computer's local time to format the backup timestamp.

#### `logging.debug.rotation.max_age`

Type

integer

Default

2

Description

The maximum number of days to retain old log files.

#### `logging.debug.rotation.max_size`

Type

integer

Default

100

Description

The maximum size in MB of the log file before it gets rotated.

#### `logging.debug.rotation.rotated_logs_size_limit`

Type

integer

Default

1024

Description

Max Size (in mb) of log files before deletion

#### `logging.debug.rotation.rotation_interval`

Type

string

Description

If set, the interval at which log files are rotated, even if max\_size is not reached.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `logging.error`

Type

object

Description

Error logging configuration.

#### `logging.error.collation_buffer_size`

Type

integer (readOnly)

Default

0

Description

The size of the log collation buffer.

#### `logging.error.enabled`

Type

boolean

Default

true

Description

Toggle for this log output

#### `logging.error.rotation.localtime`

Type

boolean

Description

If true, it uses the computer's local time to format the backup timestamp.

#### `logging.error.rotation.max_age`

Type

integer

Default

360

Description

The maximum number of days to retain old log files.

#### `logging.error.rotation.max_size`

Type

integer

Default

100

Description

The maximum size in MB of the log file before it gets rotated.

#### `logging.error.rotation.rotated_logs_size_limit`

Type

integer

Default

1024

Description

Max Size (in mb) of log files before deletion

#### `logging.error.rotation.rotation_interval`

Type

string

Description

If set, the interval at which log files are rotated, even if max\_size is not reached.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `logging.info`

Type

object

Description

Info logging configuration.

#### `logging.info.collation_buffer_size`

Type

integer (readOnly)

Default

0

Description

The size of the log collation buffer

#### `logging.info.enabled`

Type

boolean

Default

true

Description

Toggle for this log output

#### `logging.info.rotation.localtime`

Type

boolean

Description

If true, it uses the computer's local time to format the backup timestamp.

#### `logging.info.rotation.max_age`

Type

integer

Default

6

Description

The maximum number of days to retain old log files.

#### `logging.info.rotation.max_size`

Type

integer

Default

100

Description

The maximum size in MB of the log file before it gets rotated.

#### `logging.info.rotation.rotated_logs_size_limit`

Type

integer

Default

1024

Description

Max Size (in mb) of log files before deletion

#### `logging.info.rotation.rotation_interval`

Type

string

Description

If set, the interval at which log files are rotated, even if max\_size is not reached.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `logging.log_file_path`

Type

string (readOnly)

Description

Absolute or relative path on the filesystem to the log file directory. A relative path is from the directory that contains the Sync Gateway executable file.

#### `logging.redaction_level`

Type

string (readOnly)

Default

partial

Description

Redaction level to apply to log output.

#### `logging.stats`

Type

object

Description

Trace logging configuration.

#### `logging.stats.collation_buffer_size`

Type

integer (readOnly)

Default

0

Description

The size of the log collation buffer

#### `logging.stats.enabled`

Type

boolean

Default

true

Description

Toggle for this log output

#### `logging.stats.rotation.localtime`

Type

boolean

Description

If true, it uses the computer's local time to format the backup timestamp.

#### `logging.stats.rotation.max_age`

Type

integer

Default

6

Description

The maximum number of days to retain old log files.

#### `logging.stats.rotation.max_size`

Type

integer

Default

100

Description

The maximum size in MB of the log file before it gets rotated.

#### `logging.stats.rotation.rotated_logs_size_limit`

Type

integer

Default

1024

Description

Max Size (in mb) of log files before deletion

#### `logging.stats.rotation.rotation_interval`

Type

string

Description

If set, the interval at which log files are rotated, even if max\_size is not reached.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `logging.trace`

Type

object

Description

Trace logging configuration.

#### `logging.trace.collation_buffer_size`

Type

integer (readOnly)

Default

1000

Description

The size of the log collation buffer

#### `logging.trace.enabled`

Type

boolean

Description

Toggle for this log output

#### `logging.trace.rotation.localtime`

Type

boolean

Description

If true, it uses the computer's local time to format the backup timestamp.

#### `logging.trace.rotation.max_age`

Type

integer

Default

2

Description

The maximum number of days to retain old log files.

#### `logging.trace.rotation.max_size`

Type

integer

Default

100

Description

The maximum size in MB of the log file before it gets rotated.

#### `logging.trace.rotation.rotated_logs_size_limit`

Type

integer

Default

1024

Description

Max Size (in mb) of log files before deletion

#### `logging.trace.rotation.rotation_interval`

Type

string

Description

If set, the interval at which log files are rotated, even if max\_size is not reached.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `logging.warn`

Type

object

Description

Warning logging configuration.

#### `logging.warn.collation_buffer_size`

Type

integer (readOnly)

Default

0

Description

The size of the log collation buffer

#### `logging.warn.enabled`

Type

boolean

Default

true

Description

Toggle for this log output

#### `logging.warn.rotation.localtime`

Type

boolean

Description

If true, it uses the computer's local time to format the backup timestamp.

#### `logging.warn.rotation.max_age`

Type

integer

Default

180

Description

The maximum number of days to retain old log files.

#### `logging.warn.rotation.max_size`

Type

integer

Default

100

Description

The maximum size in MB of the log file before it gets rotated.

#### `logging.warn.rotation.rotated_logs_size_limit`

Type

integer

Default

1024

Description

Max Size (in mb) of log files before deletion

#### `logging.warn.rotation.rotation_interval`

Type

string

Description

If set, the interval at which log files are rotated, even if max\_size is not reached.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `max_file_descriptors`

Type

number (readOnly)

Default

5000

Description

Max of open file descriptors (RLIMIT\_NOFILE)

#### `replicator.blip_compression`

Type

integer

Description

BLIP data compression level (0-9)

#### `replicator.max_concurrent_changes_batches`

Type

integer

Default

2

Description

Maximum number of changes batches to process concurrently per replication (1-5)"

#### `replicator.max_concurrent_replications`

Type

integer

Description

Maximum number of concurrent replication connections allowed. If set to 0 this limit will be ignored.

#### `replicator.max_concurrent_revs`

Type

integer

Default

5

Description

Maximum number of revs to process concurrently per replication (5-200)

#### `replicator.max_heartbeat`

Type

string

Description

Max heartbeat value for `_changes` request.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `unsupported`

Type

object (readOnly)

Description

Settings that are not officially supported. It is highly recommended these are **not** used.

#### `unsupported.allow_dbconfig_env_vars`

Type

boolean

Default

true

Description

Can be set to false to skip environment variable expansion in database configs

#### `unsupported.diagnostic_interface`

Type

string

Description

Network interface to bind diagnotic API to.

By default, this API will not be run unless this string is specified.

#### `unsupported.http2.enabled`

Type

boolean

Description

Whether HTTP2 support is enabled

#### `unsupported.serverless`

Type

object

Description

Configuration for when SG is running in serverless mode

#### `unsupported.serverless.enabled`

Type

boolean (readOnly)

Description

Run SG in to serverless mode

#### `unsupported.serverless.min_config_fetch_interval`

Type

string

Default

1s

Description

How long database configs should be kept for in Sync Gateway before refreshing. Set to 0 to fetch configs everytime. This is used for requested databases that SG does not know about.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `unsupported.stats_log_frequency`

Type

string

Default

1m

Description

How often should stats be written to stats logs.

This is a duration and therefore can be provided with units "h", "m", "s", "ms", "us", and "ns". For example, 5 hours, 20 minutes, and 30 seconds would be `5h20m30s`.

#### `unsupported.use_stdlib_json`

Type

boolean

Description

Bypass the jsoniter package and use Go's stdlib instead

#### `unsupported.use_xattr_config`

Type

boolean

Description

Store database configurations in system xattrs

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