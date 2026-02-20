---
title: Sync with Edge Server
description: Deploy multiple Edge Servers at the edge, each serving a subset of
  local clients and set up the edge servers to sync data with each other to
  enable eventual consistency of data on all the local clients. This topology
  can also be leveraged to deploy Edge Servers in a primary-secondary
  configuration for High Availability (HA).
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.0/modules/sync/pages/edge-to-edge-sync.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:couchbase-edge-server:sync:edge-to-edge-sync.adoc[]
---

[View original HTML](/couchbase-edge-server/current/sync/edge-to-edge-sync.html)

# Sync with Edge Server

![edge to edge sync diagram](_images/edge-to-edge-sync-diagram.png) 

## [](#concepts)Concepts

Edge Servers can directly sync data with each other over web sockets. This is useful when there are multiple Edge Servers that need to keep in sync at the edge or you can setup Edge Server in a primary-backup configuration.

You can use this configuration to allow for High Availability of your application, by switching to a synced Edge Server replica of your primary database.

## [](#prerequisites)Prerequisites

To make an API call with the Edge Server REST API, you must have configured Edge Server for REST-based access.

* You must have specified the host information, including the base URL and port.
* You must have specified TLS certificate information.
* If necessary, you must have specified a HTTP Basic user name and password. The user specified must have the role required to carry out the API call.

To configure Edge Server for REST-based access, see [Get Started with the REST API](../rest-based-access/rest-api-start.md).

## [](#push-changes-to-couchbase-edge-server)Push Changes to Couchbase Edge Server

You can monitor changes in a keyspace using the keyspaces’s changes feed. The changes feed is based on _sequences_, which are abstract integer counters applied to documents. The changes feed returns the metadata (and optionally the contents) of documents that have changed since a specified sequence.

Couchbase Edge Server adopts a "push, not poll" approach to changes using two methods:

* `Longpoll` mode - Waiting until changes are present to report to update.
* `Continuous` mode - Each change is reported as a separate JSON object, delimited by a newline (`\n`). The server sends all current changes, but never ends the response; instead it sends more changes as they occur.

For more information, see [Push Changes](../rest-based-access/changes-feed.md#push-changes).

## [](#sync-your-changes-between-edge-servers)Sync Your Changes Between Edge Servers

The replicate endpoint enables you to synchronize Couchbase Edge Server with another server.

You can configure Edge Server so that replication starts automatically when Edge Server starts. This is usually used for continuous replication.

For more information about continuous replication, see [Start Replication Automatically](../rest-based-access/replication.md#start-replication-automatically).

You can also start replication using the REST API. You don’t need to set up reduplication in the configuration file to do this. Instead, you pass the replication options in the JSON request body.

For more information, see [REST API Replication](../rest-based-access/replication.md#start-replication-with-the-rest-api).

## [](#see-also)See Also

* [Sync](sync-landing.md)
* [Remote Sync with App Services / Sync Gateway](remote-sync.md)
* [Edge Sync with Couchbase Lite](edge-sync-cbl.md)