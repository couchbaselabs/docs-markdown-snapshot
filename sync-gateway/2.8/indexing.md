---
title: Indexes versus Views
description: Using Indexes to minimize system downtime in Sync Gateway
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/indexing.adoc
  xref: xref:2.8@sync-gateway::indexing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/indexing.html)

# Indexes versus Views

> Using Indexes to minimize system downtime in Sync Gateway  
> Explains the switch from System Views to GSI

Related _Deploy_ topics: [Deploy](../current/deploy/deployment.md) | [REST API Access](../current/rest-api/rest-api-access.md) | [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

## [](#overview)Overview

Sync Gateway uses GSI and N1QL to perform a variety of internal operations, including authentication and replication. Prior to Sync Gateway 2.1, it used system _Views_ instead.

One of the key advantages GSI is that it supports _index replicas_, which enables Sync Gateway to reduce the downtime — say, during a server upgrade, re-balance or failover — from several hours to a few seconds. It also improves overall query performance.

Note that this only impacts system views. Users can continue to define views through the [Sync Gateway Admin REST API](../current/rest-api/rest-api-admin.md#/query).

## [](#configuration)Configuration

This capability is enabled by default and is supported by two properties in the configuration file which can be adjusted:

* [databases.$db.use\_views](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-use%5Fviews)
* [databases.$db.num\_index\_replicas](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-num%5Findex%5Freplicas)

Use of GSI requires Couchbase Server 5.5, with at least one node running the Index Service. Users wanting to run Sync Gateway 2.1 with an older version of Couchbase Server will need to continue to use views, by setting the `use_views` property.

Sync Gateway requires the Index Service to be running on at least two Couchbase Server nodes (required for index replica). However, users can run with a single Index Service node by setting Sync Gateway's `num_index_replicas` property to zero. Doing so, may result in increased downtime in the event of an index node failure.

## [](#related-content)Related Content

###### [](#)

API Topics

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-2)

Reference

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)