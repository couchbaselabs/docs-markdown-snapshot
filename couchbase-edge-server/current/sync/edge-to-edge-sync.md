---
title: Sync with Edge Server
description: Deploy multiple Edge Servers at the edge, each serving a subset of
  local clients and set up the edge servers to sync data with each other to
  enable eventual consistency of data on all the local clients. This topology
  can also be leveraged to deploy Edge Servers in a primary-secondary
  configuration for High Availability (HA).
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.1/modules/sync/pages/edge-to-edge-sync.adoc
  xref: xref:couchbase-edge-server:sync:edge-to-edge-sync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/current/sync/edge-to-edge-sync.html)

# Sync with Edge Server

![edge to edge sync diagram](_images/edge-to-edge-sync-diagram.png) 

## [](#concepts)Concepts

Edge Servers can directly sync data with each other over WebSockets. This is useful when there are multiple Edge Servers that need to keep in sync at the edge, or you can set up Edge Server in a primary-backup configuration.

You can use this configuration to allow for High Availability of your application, by switching to a synced Edge Server replica of your primary database.

## [](#prerequisites)Prerequisites

* You must have specified the host information, including the base URL and port.
* You must have specified TLS certificate information.
* If necessary, you must have specified an HTTP Basic username and password. The user must have the role required to carry out the API call.

To configure Edge Server for REST-based access, see [Get Started with the REST API](../rest-based-access/rest-api-start.md).

## [](#sync-your-changes-between-edge-servers)Sync Your Changes Between Edge Servers

The following example shows a configuration for continuous bidirectional replication between two Edge Server instances. The `source` is the address of the remote Edge Server database. The `target` is the name of the local database.

```json5
{
  databases: {
    travel: {
      path: "/opt/couchbase-edge-server/database/travel.cblite2",
      create: true,
      enable_client_sync: true
    }
  },
  interface: "0.0.0.0:59841",
  users: "/opt/couchbase-edge-server/users/users.json",
  replications: [
    {
      source: "ws://edge-server-2.example.com:59841/travel",
      target: "travel",
      bidirectional: true,
      continuous: true,
      collections: [
        "travel.airlines",
        "travel.routes",
        "travel.airports",
        "travel.landmarks",
        "travel.hotels"
      ],
      auth: {
        user: "admin_user",
        password: "s3cr3t"
      }
    }
  ]
}
```

For more information about continuous replication, see [Start Replication Automatically](../rest-based-access/replication.md#start-replication-automatically).

You can also start replication using the REST API. You do not need to set up replication in the configuration file to do this. Instead, you pass the replication options in the JSON request body.

For more information, see [REST API Replication](../rest-based-access/replication.md#start-replication-with-the-rest-api).

For information about monitoring and pushing changes, see [Push Changes](../rest-based-access/changes-feed.md#push-changes).

## [](#see-also)See Also

* [Sync](sync-landing.md)
* [Remote Sync with App Services / Sync Gateway](remote-sync.md)
* [Edge Sync with Couchbase Lite](edge-sync-cbl.md)