---
title: Remote Sync with App Services / Sync Gateway
description: Read and write data or listen for data changes from Edge Server
  over a RESTful interface from any HTTP client.
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.0/modules/sync/pages/remote-sync.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:1.0@couchbase-edge-server:sync:remote-sync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/1.0/sync/remote-sync.html)

# Remote Sync with App Services / Sync Gateway

![remote upstream sync diagram](_images/remote-upstream-sync-diagram.png) 

## [](#concepts)Concepts

When Internet connectivity is available, the Edge Server can synchronize data with a remote App Services using a WebSocket-based replication protocol.

You can read and write data or listen for data changes from Edge Server over a RESTful interface from any HTTP client, such as [Insomnia](https://insomnia.rest/) or [Postman](https://www.postman.com/).

## [](#prerequisites)Prerequisites

To set up replication, you must first configure Sync Gateway, Couchbase Capella App Services, or another Edge Server installation, to allow Edge Server to connect.

To replicate with a Couchbase Capella database:

* You must have created an App Service connected to the Couchbase Capella database you want to replicate.
* You must have created an App Endpoint connected to the App Service, with access to the collections you want to replicate.
* The App Endpoint must be active.
* You must have set up a username, password, and authentication providers to enable Edge Server to connect to the App Endpoint.
* You must have allowed [IP access](../../../app-services/app-services/accessing-admin-apis.md) from the address that the Edge Server client uses.
* You must have copied the public connection URL for the App Endpoint.

For more information about Capella App Services, see [cloud:app-services:index.adoc](#cloud:app-services:index.adoc).

To replicate with a remote Sync Gateway:

* You must have access to a working Couchbase Server deployment configured for Sync Gateway. See [Configure Server for Sync Gateway](#sync-gateway:ROOT:get-started-prepare.adoc#configure-server).
* You must have configured the [appropriate RBAC Roles on Sync Gateway](../../../sync-gateway/current/rest-api/rest-api-access.md#lbl-rbac-roles).
* You must have set `database.import_docs` and `database.enable_shared_bucket_access` to true in the [Sync Gateway Database Configuration Schema](../../../sync-gateway/current/configuration/configuration-schema-database.md#%5Fdatabase).

For more information about Couchbase Sync Gateway, see [Sync Gateway](../../../sync-gateway/current/introduction.md).

## [](#sync-your-changes)Sync Your Changes

The replicate endpoint enables you to synchronize Couchbase Edge Server with another server.

You can configure Edge Server so that replication starts automatically when Edge Server starts. This is used for continuous replication.

The following example shows a configuration that replicates a local database to a remote {sync-gateway-name} instance continuously, using basic authentication.

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

For more information about continuous replication, see [Start Replication Automatically](../rest-based-access/replication.md#start-replication-automatically).

You can also start replication using the REST API. You do not need to set up replication in the configuration file to do this. Instead, you pass the replication options in the JSON request body.

For more information, see [REST API Replication](../rest-based-access/replication.md#start-replication-with-the-rest-api).

For information about monitoring and pushing changes, see [Push Changes](../rest-based-access/changes-feed.md#push-changes).

## [](#see-also)See Also

* [Sync](sync-landing.md)
* [Edge Sync with Couchbase Lite](edge-sync-cbl.md)
* [Sync with Edge Server](edge-to-edge-sync.md)