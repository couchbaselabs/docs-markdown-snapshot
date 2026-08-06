---
title: Edge Sync with Couchbase Lite
description: Deploy edge clients in a mixed configuration, with HTTP clients
  accessing data through the REST API and Couchbase Lite clients supporting
  offline-first data synchronization.
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.1/modules/sync/pages/edge-sync-cbl.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-edge-server:sync:edge-sync-cbl.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/current/sync/edge-sync-cbl.html)

# Edge Sync with Couchbase Lite

Deploy edge clients in a mixed configuration, with HTTP clients accessing data through the REST API and Couchbase Lite clients supporting offline-first data synchronization.

![sync with cbl diagram](_images/sync-with-cbl-diagram.png) 

## [](#concepts)Concepts

Couchbase Lite applications running on mobile and desktop edge clients can synchronize data with a local Edge Server using a WebSocket-based replication protocol.

Couchbase Mobile uses a replication protocol based on WebSockets for replication. To use this protocol the replication URL should specify WebSockets as the URL scheme. See [configure target](../../../couchbase-lite/current/c/replication.md#lbl-cfg-tgt).

You can use Couchbase Lite API support for secure, bi-directional, synchronization of data changes between mobile applications and a central server database such as Couchbase Edge Server. It does so by using a replicator to interact with Sync Gateway.

* Pull Replication — The process by which clients running Couchbase Lite download database changes from the remote (server) source database to the local target database.
* Push Replication — The process by which clients running Couchbase Lite upload database changes from the local source database to the remote (server) target database.

## [](#prerequisites)Prerequisites

* If you're using a self-signed certificate, Couchbase Lite requires a copy of the server's certificate to set as a pinned cert in the replicator attributes. See [certificate pinning](../../../couchbase-lite/current/c/replication.md#lbl-cert-pinning).
* `database.enable_client_sync` must not be set to `false` in your [configuration schema](../configuration/edge-server-configuration.md#json-schema).

## [](#sync-your-changes)Sync Your Changes

Set `enable_client_sync` in the database configuration to control the direction of sync between Edge Server and Couchbase Lite clients.

| Value                 | Behavior                                              |
| --------------------- | ----------------------------------------------------- |
| pull                  | Clients can pull changes from Edge Server. Read-only. |
| push                  | Clients can push changes to Edge Server. Write-only.  |
| bidirectional or true | Clients can both push and pull changes.               |

The following example enables bidirectional sync for a local database.

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
  users: "/etc/edge-server/users.json"
}
```

For more information about continuous replication, see [Start Replication Automatically](../rest-based-access/replication.md#start-replication-automatically).

You can also start replication using the REST API. You do not need to set up replication in the configuration file to do this. Instead, you pass the replication options in the JSON request body.

For more information, see [REST API Replication](../rest-based-access/replication.md#start-replication-with-the-rest-api).

For more information about how Couchbase Lite handles downstream replication, see [Couchbase Lite - C, Sync](../../../couchbase-lite/current/c/replication.md#introduction).

For information about monitoring and pushing changes, see [Push Changes](../rest-based-access/changes-feed.md#push-changes).

## [](#see-also)See Also

* [Monitor Changes with Edge Server](../rest-based-access/changes-feed.md)
* [Manage Replication with Edge Server](../rest-based-access/replication.md)
* [Sync](sync-landing.md)
* [Remote Sync with App Services / Sync Gateway](remote-sync.md)
* [Sync with Edge Server](edge-to-edge-sync.md)