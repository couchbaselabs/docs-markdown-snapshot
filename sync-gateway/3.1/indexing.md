---
title: Indexes versus Views
description: Using Indexes to minimize system downtime in Sync Gateway
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/indexing.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.1@sync-gateway::indexing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/indexing.html)

# Indexes versus Views

> Using Indexes to minimize system downtime in Sync Gateway  
> Explains the switch from System Views to GSI

Related _Deploy_ topics: [Deployment](deployment.md) | [REST API Access](rest-api-access.md) | [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#overview)Overview

Sync Gateway uses GSI and SQL++ to perform a variety of internal operations, including authentication and replication. Prior to Sync Gateway 2.1, it used system _Views_ instead.

One of the key advantages GSI is that it supports _index replicas_, which enables Sync Gateway to reduce the downtime — say, during a server upgrade, re-balance or failover — from several hours to a few seconds. It also improves overall query performance.

Note that this only impacts system views. Users can continue to define views through the [Sync Gateway Admin REST API](rest-api-admin.md#/query).

## [](#configuration)Configuration

This capability is enabled by default and is supported by two properties in the configuration file which can be adjusted:

* [databases.$db.use\_views](configuration-schema-database.md#database-use%5Fviews)
* [databases.$db.num\_index\_replicas](configuration-schema-database.md#database-num%5Findex%5Freplicas)

Use of GSI requires Couchbase Server 5.5, with at least one node running the Index Service. Users wanting to run Sync Gateway 2.1 with an older version of Couchbase Server will need to continue to use views, by setting the `use_views` property.

Sync Gateway requires the Index Service to be running on at least two Couchbase Server nodes (required for index replica). However, users can run with a single Index Service node by setting Sync Gateway’s `num_index_replicas` property to zero. Doing so, may result in increased downtime in the event of an index node failure.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

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