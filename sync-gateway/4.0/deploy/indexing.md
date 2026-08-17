---
title: Indexing
description: Using Indexes to minimize system downtime in Sync Gateway
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/deploy/pages/indexing.adoc
  xref: xref:4.0@sync-gateway:deploy:indexing.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/4.0/deploy/indexing.html)

# Indexing

> Using Indexes to minimize system downtime in Sync Gateway  
> Explains the use of Global Secondary Indexes

Related _Deploy_ topics: [Deployment](deployment.md) | [REST API Access](../rest-api/rest-api-access.md) | [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

## [](#overview)Overview

Sync Gateway uses GSI (Global Secondary Indexes) and SQL++ to perform a variety of internal operations, including authentication and replication.

One of the key advantages GSI is that it supports index replicas, which enables Sync Gateway to reduce the downtime — say, during a server upgrade, re-balance or failover — from several hours to a few seconds. It also improves overall query performance.

Sync Gateway 3.3 supports partitioned indexes. This enables you to divide and spread a large index across multiple nodes. For details, see [Partitioned Indexes](index-partitions.md).

## [](#configuration)Configuration

This capability is enabled by default and is supported by two properties in the configuration file which can be adjusted:

* [databases.$db.use\_views](../configuration/configuration-schema-database.md#use%5Fviews)
* [databases.$db.index.num\_replicas](../configuration/configuration-schema-database.md#index.num%5Freplicas)

Use of GSI requires Couchbase Server 5.5 or later, with at least one node running the Index Service. Users wanting to run Sync Gateway 2.1 with an older version of Couchbase Server will need to continue to use views, by setting the `use_views` property.

Sync Gateway requires the Index Service to be running on at least two Couchbase Server nodes (required for index replica). However, users can run with a single Index Service node by setting Sync Gateway's `index.num_replicas` property to zero. Doing so may result in increased downtime in the event of an index node failure.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)