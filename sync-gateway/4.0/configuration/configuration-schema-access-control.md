---
title: Access Control Configuration
description: Using Sync Gateway's Admin REST API and the Sync function to configure access
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/configuration/pages/configuration-schema-access-control.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.0@sync-gateway:configuration:configuration-schema-access-control.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/4.0/configuration/configuration-schema-access-control.html)

# Access Control Configuration

> [!IMPORTANT]
> Pre-3.0 Legacy Configuration Equivalents
> 
> This content describes configuration for Sync Gateway 3.0 and higher — for legacy configuration, see: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

## [](#introduction)Introduction

The sync function is crucial to the security of your application. It is in charge of data validation, access control and routing. The function executes every time a new revision/update is made to a document.

For more on the Sync Function and access control see: [Sync Function Overview](../access-control/sync-function/sync-function.md)

## [](#set-database-sync-function)Set Database Sync Function

To set or update the sync function for a database, see [{keyspace}/\_config/sync](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync).

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