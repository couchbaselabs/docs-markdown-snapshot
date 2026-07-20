---
title: Edge Server Configuration Schema
description: Full reference for all Couchbase Edge Server configuration
  properties and their default values.
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.0/modules/configuration/pages/configuration-schema.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:1.0@couchbase-edge-server:configuration:configuration-schema.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/1.0/configuration/configuration-schema.html)

# Edge Server Configuration Schema

Full reference for all Couchbase Edge Server configuration properties and their default values.

The configuration file is parsed as [JSON5 format](https://json5.org/).

> [!WARNING]
> Couchbase does not recommend setting `enable_adhoc_queries` to `true` for production environments. Slow-running queries can be used as denial-of-service attacks.

For an overview of authentication configuration, see [Authentication](authentication.md).


{
   [$schema](#$schema): "https://packages.couchbase.com/couchbase-edge-server/config_schema.json",
   [databases](#databases): {
      [{database_name...}](#databases-{database%5Fname}): {
         [collections](#databases-{database%5Fname}-collections): array,object,
         [create](#databases-{database%5Fname}-create): false,
         [enable_adhoc_queries](#databases-{database%5Fname}-enable%5Fadhoc%5Fqueries): false,
         [enable_client_sync](#databases-{database%5Fname}-enable%5Fclient%5Fsync): boolean or string,
         [enable_client_writes](#databases-{database%5Fname}-enable%5Fclient%5Fwrites): false,
         [password](#databases-{database%5Fname}-password): "string",
         [path](#databases-{database%5Fname}-path): "string",
         [placeholder_uuid](#databases-{database%5Fname}-placeholder%5Fuuid): "string",
         [queries](#databases-{database%5Fname}-queries): {
            [{query...}](#databases-{database%5Fname}-queries-{query}): "string"
         }
      }
   },
   [enable_anonymous_users](#enable%5Fanonymous%5Fusers): false,
   [https](#https): {
      [client_cert_path](#https-client%5Fcert%5Fpath): "string",
      [tls_cert_path](#https-tls%5Fcert%5Fpath): "string",
      [tls_key_path](#https-tls%5Fkey%5Fpath): "string"
   },
   [interface](#interface): "0.0.0.0:59840",
   [logging](#logging): {
      [audit](#logging-audit): {
         [disable](#logging-audit-disable): string,array,
         [enable](#logging-audit-enable): string,array,
         [file](#logging-audit-file): "string",
         [omit_description](#logging-audit-omit%5Fdescription): false
      },
      [console](#logging-console): true,
      [domains](#logging-domains): {
         [{domain...}](#logging-domains-{domain}): "warning"
      },
      [file](#logging-file): {
         [dir](#logging-file-dir): "string",
         [format](#logging-file-format): "binary",
         [maxSize](#logging-file-maxSize): 1000000,
         [rotateCount](#logging-file-rotateCount): 0
      }
   },
   [replications](#replications): [
      [auth](#replications-auth): {
         [openid_token](#replications-auth-openid%5Ftoken): "string",
         [password](#replications-auth-password): "string",
         [session_cookie](#replications-auth-session%5Fcookie): "string",
         [tls_client_cert](#replications-auth-tls%5Fclient%5Fcert): "string",
         [tls_client_cert_key](#replications-auth-tls%5Fclient%5Fcert%5Fkey): "string",
         [user](#replications-auth-user): "string"
      },
      [bidirectional](#replications-bidirectional): false,
      [channels](#replications-channels): ["string"...],
      [collections](#replications-collections): _default,
      [continuous](#replications-continuous): false,
      [doc_ids](#replications-doc%5Fids): ["string"...],
      [headers](#replications-headers): {
         [{header...}](#replications-headers-{header}): "string"
      },
      [pinned_cert](#replications-pinned%5Fcert): "string",
      [proxy](#replications-proxy): {
         [auth](#replications-proxy-auth): {
            [openid_token](#replications-proxy-auth-openid%5Ftoken): "string",
            [password](#replications-proxy-auth-password): "string",
            [tls_client_cert](#replications-proxy-auth-tls%5Fclient%5Fcert): "string",
            [tls_client_cert_key](#replications-proxy-auth-tls%5Fclient%5Fcert%5Fkey): "string",
            [user](#replications-proxy-auth-user): "string"
         },
         [host](#replications-proxy-host): "string",
         [port](#replications-proxy-port): 0,
         [type](#replications-proxy-type): "HTTP"
      },
      [source](#replications-source): "string",
      [target](#replications-target): "string",
      [trusted_root_certs](#replications-trusted%5Froot%5Fcerts): "string"
   ],
   [users](#users): "string"
}

#### `$schema`

Type

string

Default

https://packages.couchbase.com/couchbase-edge-server/config\_schema.json

Description

Allows config files to declare they conform to this schema. Otherwise ignored.

#### `databases`

Type

object

Description

The databases to be served. Keys are the URI names to use.

#### `databases.{database_name…​}`

Type

object

Description

A database configuration.

#### `databases.{database_name…​}.collections`

Type

array,object

Description

Collections to share. If omitted, all collections are shared. If it's an array, the items are the names of the collections to share (and create, if create is true). If it's an object, each key is a collection name and the value is an object describing the collection.

#### `databases.{database_name…​}.create`

Type

boolean

Description

If true, database will be created on startup if it doesn't exist.

#### `databases.{database_name…​}.enable_adhoc_queries`

Type

boolean

Description

If true, clients can submit freeform SQL++ `SELECT` queries.

Not recommended in production due to potential for abuse: slow-running queries can be used as DoS attacks.

#### `databases.{database_name…​}.enable_client_sync`

Type

boolean or string

Description

Enables client sync connections. `pull` is read-only, `push` is write-only, `bidirectional` or true enables both. Defaults to `false`, that is, sync is not allowed.

#### `databases.{database_name…​}.enable_client_writes`

Type

boolean

Description

Enables writing to database via PUT / POST / DELETE requests. Lets clients write to the documents via the REST API. It does not affect clients syncing. So it's possible to disallow writes via REST but allow them via push replication, or vice versa.

This does not affect upstream replication or client sync. To prevent clients from writing to the database via sync, `enable_client_sync` must be omitted or set to `pull`.

#### `databases.{database_name…​}.password`

Type

string

Description

Database password, or raw AES256 key encoded as 64 hex digits.

#### `databases.{database_name…​}.path`

Type

string

Description

Path of database file.

#### `databases.{database_name…​}.placeholder_uuid`

Type

string

Description

Database UUID to be replaced on first launch. The `placeholder_uuid` property should be used if the database has been copied from elsewhere. Every database file contains a universally unique ID (UUID); copying a database file means this is no longer unique, and that will cause problems with replication. If a canned initial database file is to be deployed to a number of Edge Servers, its current UUID can be set as the value of this property. The first time each server starts up, it will replace that UUID with a new, actually-unique one. You can find a database file's UUID via `cblite info -v db.cblite2`.

#### `databases.{database_name…​}.queries`

Type

object

Description

SQL++ queries clients can invoke. Keys are query names, values are SQL++.

#### `databases.{database_name…​}.queries.{query…​}`

Type

string

Description

A SQL++ 'SELECT' query.

#### `enable_anonymous_users`

Type

boolean

Description

If true, unauthenticated requests are allowed (guest access).

#### `https`

Type

object

Description

TLS settings. If present, `tls_cert_path` and `tls_key_path` are required.

#### `https.client_cert_path`

Type

string

Description

Path of file containing CA cert for authenticating clients (mTLS).

If present, clients must connect using TLS client certificates. Only certs signed by this CA cert will be accepted. The Common Name (CN) field of the client cert will be used as the username for purposes of logging.

#### `https.tls_cert_path`

Type

string

Description

Path of file containing TLS server certificate.

#### `https.tls_key_path`

Type

string

Description

Path of file containing matching private key.

#### `interface`

Type

string

Default

0.0.0.0:59840

Description

Listening interface IP address and port, separated by a colon. The interface address is _optional_ and defaults to 0.0.0.0, i.e. all interfaces. A useful value for testing is 127.0.0.1, which allows only clients on the same device to connect. The default port number is 59840.

#### `logging`

Type

object

Description

Logging configuration.

#### `logging.audit`

Type

object

Description

Configuration for audit logging.

#### `logging.audit.disable`

Type

string,array

Description

Array of integer event IDs to disable, or "\*" to disable all - (`enable` overrides these).

#### `logging.audit.enable`

Type

string,array

Description

Array of integer event IDs to enable, or "\*" to enable all. (Takes priority over 'disable').

#### `logging.audit.file`

Type

string

Description

Filename of audit log.

#### `logging.audit.omit_description`

Type

boolean

Description

If true, audit events will omit the `description` property.

The `description` property can be useful for human readers, but is quite verbose and will significantly increase log file size.

#### `logging.console`

Type

boolean

Default

true

Description

Whether to log to stdout/stderr.

#### `logging.domains`

Type

object

Description

Custom levels for specific logging domains. Keys are domain names. Common domains are `Default`, `REST`, `Listener`, `DB`, `Query`, `Sync`.

#### `logging.domains.{domain…​}`

Type

string

Default

warning

Description

Log level of the domain: `verbose`, `info`, `warning` or `error`

#### `logging.file`

Type

object

Description

Configuration for file-based logging.

#### `logging.file.dir`

Type

string

Description

Path of existing directory where log files will be created.

#### `logging.file.format`

Type

string

Default

binary

Description

Format of log files: `binary` or `text`.

#### `logging.file.maxSize`

Type

integer

Default

1000000

Description

Size in _bytes_ at which log files are rotated.

#### `logging.file.rotateCount`

Type

integer

Description

Number of older log files that are preserved.

#### `replications`

Type

array

Description

Replications to run when the server starts.

#### `replications.auth`

Type

object

Description

Authorization credentials.

#### `replications.auth.openid_token`

Type

string

Description

An OpenID Connect token.

#### `replications.auth.password`

Type

string

Description

Password for HTTP Basic auth to remote server. Requires 'user'.

#### `replications.auth.session_cookie`

Type

string

Description

A Sync Gateway session cookie.

#### `replications.auth.tls_client_cert`

Type

string

Description

This Edge Server's TLS client certificate, for mTLS. (Requires 'tls\_client\_cert\_key'.)

#### `replications.auth.tls_client_cert_key`

Type

string

Description

Private key of TLS client certificate. (Requires 'tls\_client\_cert'.)

#### `replications.auth.user`

Type

string

Description

Username for HTTP Basic auth to remote server. Requires 'password'.

#### `replications.bidirectional`

Type

boolean

Description

If true, replication is bidirectional.

#### `replications.channels`

Type

array

Description

Channel filter (incompatible with 'collections')

#### `replications.collections`

Type

array,object

Default

\_default

Description

Collections to replicate. If omitted, only the default collection is replicated.

#### `replications.continuous`

Type

boolean

Description

If true, replication is continuous, i.e. keeps running forever.

#### `replications.doc_ids`

Type

array

Description

Document IDs to replicate (incompatible with 'collections')

#### `replications.headers`

Type

object

Description

Extra HTTP headers; keys are header names, values are header values.

#### `replications.headers.{header…​}`

Type

string

Description

Header value

#### `replications.pinned_cert`

Type

string

Description

Path of file containing the _required_ server certificate.

#### `replications.proxy`

Type

object

Description

HTTP proxy settings

#### `replications.proxy.auth`

Type

object

Description

Proxy authorization credentials.

#### `replications.proxy.auth.openid_token`

Type

string

Description

An OpenID Connect token.

#### `replications.proxy.auth.password`

Type

string

Description

Password for HTTP Basic auth to proxy. Requires 'user'.

#### `replications.proxy.auth.tls_client_cert`

Type

string

Description

This Edge Server's TLS client certificate, for mTLS. (Requires 'tls\_client\_cert\_key'.)

#### `replications.proxy.auth.tls_client_cert_key`

Type

string

Description

Private key of TLS client certificate. (Requires 'tls\_client\_cert'.)

#### `replications.proxy.auth.user`

Type

string

Description

Username for HTTP Basic auth to proxy. Requires 'password'.

#### `replications.proxy.host`

Type

string

Description

Hostname of proxy server

#### `replications.proxy.port`

Type

integer

Description

Port number of proxy server

#### `replications.proxy.type`

Type

string

Default

HTTP

Description

Proxy type: 'HTTP' or 'HTTPS'

#### `replications.source`

Type

string

Description

The source database: a local name or remote 'wss:' URL.

#### `replications.target`

Type

string

Description

The destination database: a local name or remote 'wss:' URL.

#### `replications.trusted_root_certs`

Type

string

Description

Path of file containing one or more additional root certificates to be trusted.

#### `users`

Type

string

Description

Path to JSON file containing users and roles.