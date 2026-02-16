[View original HTML](/couchbase-edge-server/current/sync/edge-sync-cbl.html)

Deploy edge clients in a mixed configuration, with HTTP clients accessing data through the REST API and Couchbase Lite clients supporting offline-first data synchronization.

![sync with cbl diagram](_images/sync-with-cbl-diagram.png) 

## [](#concepts)Concepts

Couchbase Lite applications running on mobile and desktop edge clients can synchronize data with a local Edge Server using a WebSocket-based replication protocol.

Couchbase Mobile uses a replication protocol based on WebSockets for replication. To use this protocol the replication URL should specify WebSockets as the URL scheme. See [configure target](../../../couchbase-lite/current/c/replication.md#lbl-cfg-tgt).

You can use Couchbase Lite API support for secure, bi-directional,synchronization of data changes between mobile applications and a central server database such as Couchbase Edge Server. It does so by using a replicator to interact with Sync Gateway.

* Pull Replication - The process by which clients running Couchbase Lite download database changes from the remote (server) source database to the local target database.
* Push Replication - The process by which clients running Couchbase Lite upload database changes from the local source database to the remote (server) target database.

## [](#prerequisites)Prerequisites

To deploy Couchbase Edge Server in a mixed configuration with Couchbase Lite clients supporting offline-first data synchronization downstream and HTTP clients accessing data upstream through the REST API:

* If you’re using a self-signed certificate, Couchbase Lite requires a copy of the server’s certificate to set as a pinned cert in the replicator attributes, see [certificate pinning](../../../couchbase-lite/current/c/replication.md#lbl-cert-pinning).
* `database.enable_client_sync` must not be set to `false` in your [configuration schema](../configuration/edge-server-configuration.md#json-schema).
* You must have created an App Service connected to the Couchbase Capella database you want to replicate.
* You must have created an App Endpoint connected to the App Service, with access to the collections you want to replicate.
* The App Endpoint must be active.
* You must have set up a username, password, and authentication providers to enable Edge Server to connect to the App Endpoint.
* You must have allowed [IP access](../../../app-services/app-services/accessing-admin-apis.md) from the address that the Edge Server client will use.
* You must have copied the public connection URL for the App Endpoint.

## [](#push-changes-to-couchbase-edge-server)Push Changes To Couchbase Edge Server

You can monitor changes in a keyspace using the keyspaces’s changes feed. The changes feed is based on _sequences_, which are abstract integer counters applied to documents. The changes feed returns the metadata (and optionally the contents) of documents that have changed since a specified sequence.

Couchbase Edge Server adopts a "push, not poll" approach to changes using two methods:

* `Longpoll` mode - Waiting until changes are present to report to update.
* `Continuous` mode - Each change is reported as a separate JSON object, delimited by a newline (`\n`). The server sends all current changes, but never ends the response; instead it sends more changes as they occur.

For more information, see [Push Changes](../rest-based-access/changes-feed.md#push-changes).

## [](#syncing-your-changes)Syncing Your Changes

The replicate endpoint enables you to synchronize Couchbase Edge Server with another server.

You can configure Edge Server so that replication starts automatically when Edge Server starts. This is usually used for continuous replication.

For more information about continuous replication, see [Start Replication Automatically](../rest-based-access/replication.md#start-replication-automatically).

You can also start replication using the REST API. You don’t need to set up reduplication in the configuration file to do this. Instead, you pass the replication options in the JSON request body.

For more information, see [REST API Replication](../rest-based-access/replication.md#start-replication-with-the-rest-api).

For more information about how Couchbase Lite can handle downstream replication, see [Couchbase Lite - C, Sync](../../../couchbase-lite/current/c/replication.md#introduction).

## [](#see-also)See Also

* [Monitor Changes with Edge Server](../rest-based-access/changes-feed.md)
* [Manage Replication with Edge Server](../rest-based-access/replication.md)
* [Sync](sync-landing.md)
* [Remote Sync with App Services / Sync Gateway](remote-sync.md)
* [Sync with Edge Server](edge-to-edge-sync.md)