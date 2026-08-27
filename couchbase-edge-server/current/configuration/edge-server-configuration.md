---
title: Edge Server Configuration
description: Configure Couchbase Edge Server using a JSON configuration file.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.1/modules/configuration/pages/edge-server-configuration.adoc
  xref: xref:couchbase-edge-server:configuration:edge-server-configuration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/current/configuration/edge-server-configuration.html)

# Edge Server Configuration

Configure Couchbase Edge Server using a JSON configuration file.

> [!NOTE]
> The configuration file is parsed as [JSON5 format](https://json5.org/).

## [](#minimal-configuration)Minimal Configuration

The following is the minimum configuration required to start Couchbase Edge Server with a single local database and enable client sync connections.

```json5
{
  databases: {
    my-database: {
      path: "/var/lib/edge-server/my-database.cblite2",
      create: true,
      enable_client_sync: true
    }
  },
  interface: "0.0.0.0:59840",
  users: "/etc/edge-server/users.json"
}
```

For a full reference of all configuration properties and their default values, see [Edge Server Configuration Schema](configuration-schema.md).

## [](#configuration-examples)Configuration Examples

The following examples show common Couchbase Edge Server configuration scenarios. All examples use JSON5 format, which permits comments and unquoted keys.

### [](#continuous-replication)Continuous Replication to Sync Gateway

A configuration that replicates a local database to a remote {sync-gateway-name} instance using basic auth, with a continuous bidirectional replication.

```json5
{
  databases: {
    travel-sample: {
      path: "/var/lib/edge-server/travel-sample.cblite2",
      create: true,
      enable_client_sync: "bidirectional"
    }
  },
  interface: "0.0.0.0:59840",
  users: "/etc/edge-server/users.json",
  replications: [
    {
      source: "travel-sample",
      target: "wss://sync-gateway.example.com/travel-sample",
      continuous: true,
      auth: {
        user: "replicator",
        password: "s3cr3t"
      }
    }
  ]
}
```

### [](#tls-and-logging)TLS and File Logging

A production-oriented configuration with TLS enabled and file-based logging.

```json5
{
  databases: {
    my-database: {
      path: "/var/lib/edge-server/my-database.cblite2",
      create: true,
      enable_client_sync: true
    }
  },
  interface: "0.0.0.0:59840",
  users: "/etc/edge-server/users.json",
  https: {
    tls_cert_path: "/etc/edge-server/server.crt",
    tls_key_path: "/etc/edge-server/server.key"
  },
  logging: {
    console: false,
    file: {
      dir: "/var/log/edge-server",
      format: "text",
      maxSize: 5000000,
      rotateCount: 5
    }
  }
}
```

## [](#see-also)See Also

* [Edge Server Configuration Schema](configuration-schema.md)
* [Authentication](authentication.md)