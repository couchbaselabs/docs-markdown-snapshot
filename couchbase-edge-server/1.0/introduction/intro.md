---
title: Introducing Couchbase Edge Server
description: Couchbase Edge Server is a lightweight standalone database for
  resource-constrained edge, based on Couchbase Lite Core.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.0/modules/introduction/pages/intro.adoc
  xref: xref:1.0@couchbase-edge-server:introduction:intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/1.0/introduction/intro.html)

# Introducing Couchbase Edge Server

Couchbase Edge Server is a lightweight standalone database for resource-constrained edge, based on Couchbase Lite Core.

With Couchbase Edge Server, you can perform scalable, offline-first data sync at the edge in resource constrained environments.

![Couchbase Edge Server Architecture](../sync/_images/edge-server-architecture.png) 

Figure 1\. Couchbase Edge Server Architecture

The diagram above illustrates how Couchbase Edge Server builds on Couchbase Lite Core engine to deliver its foundational elements.

Couchbase Edge Server provides a REST API for CRUD operations, SQL++ queries, and push notifications. It also supports remote sync with upstream Sync Gateway/App Services and edge sync with downstream Couchbase Lite applications.

## Why Use Couchbase Edge Server?

* Resource efficiency: Compact \~10 MB codebase with typically < 50 MB RAM usage, perfect for edge environments.
* Offline-first synchronization: Enables reliable data sync even in intermittent connectivity scenarios.
* Flexible deployment: Functions as both a sync server for local Couchbase Lite clients and a sync client for upstream services, supporting various edge topologies.
* Real-time updates: Push notifications for data changes reduce bandwidth and latency compared to polling.
* High availability: Support for multiple Edge Server configurations including primary-backup setups for redundancy.

## Key Capabilities

* REST API: RESTful interface for any HTTP client, including browser applications.
* Remote Sync: Syncs data with upstream Sync Gateway/App Services via WebSockets replication protocol.
* Edge Sync: Enables downstream Couchbase Lite applications to sync with Couchbase Edge Server.
* Advanced querying: Supports SQL++ queries for complex data operations.
* Flexible data handling: Serves existing Couchbase Lite database files or creates CRUD-based document access.
* High Availability (HA): Connects multiple Edge Servers via upstream and downstream sync interfaces.

# 

> [!TIP]
> For more information about the latest changes to Couchbase Edge Server, see [New In 1.0](whats-new.md).

## Getting Started

Get started with Couchbase Edge Server, from installing to building and running the product.

* [Getting Started](../get-started/get-started-landing.md)
* [Prerequisites](../get-started/prereqs.md)
* [Install and Verify](../get-started/install.md)

## Configuration

Learn how to configure Couchbase Edge Server to your specifications.

* [Edge Server Configuration](../configuration/edge-server-configuration.md)
* [Edge Server Configuration](../configuration/edge-server-configuration.md)

## REST Based Access

Use Couchbase Edge Server REST API capabilities to perform CRUD operations, SQL++ queries, push notifications and more in your applications.

* [Edge Server REST API](../rest-based-access/rest-api-landing.md)
* [Database Operations with Edge Server](../rest-based-access/database-operations.md)
* [Document Access with Edge Server](../rest-based-access/document-access.md)
* [Monitor Changes with Edge Server](../rest-based-access/changes-feed.md)
* [Run Queries with Edge Server](../rest-based-access/queries-api.md)
* [Manage Replication with Edge Server](../rest-based-access/replication.md)
* [Edge Server Public REST API](../public-api-reference/index.md)

## Sync

Sync data between Couchbase Edge Server and your application, Couchbase Lite, or Capella.

* [Sync](../sync/sync-landing.md)
* [Remote Sync with App Services / Sync Gateway](../sync/remote-sync.md)
* [Edge Sync with Couchbase Lite](../sync/edge-sync-cbl.md)
* [Sync with Edge Server](../sync/edge-to-edge-sync.md)

## Administer

Perform administrative tasks with Couchbase Edge Server.

* [Administer](../administer/administer-landing.md)
* [Operational Logging](../administer/operational-logging.md)
* [Audit Logging](../administer/audit-logging.md)

## Product Notes

View supported platforms, product compatibility and more detailed release notes for Couchbase Edge Server.

* [Product Notes](../product-notes/product-notes-landing.md)
* [Product Compatibility](../product-notes/compatibility.md)
* [Supported Platforms](../product-notes/supported-platforms.md)
* [Release Notes](../product-notes/release-notes.md)