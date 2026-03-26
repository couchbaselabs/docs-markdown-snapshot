---
title: Take Database Offline/Online
description: How to take a <em>Sync&nbspGateway</em> database offline and bring back online.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/database-offline.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.1@sync-gateway::database-offline.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/database-offline.html)

# Take Database Offline/Online

> How to take a _Sync Gateway_ database offline and bring back online.  

## [](#introduction)Introduction

Sync Gateway enables a database to be taken offline and brought back online. This is done without stopping the Sync Gateway instance and without affecting other databases served by it.

The change of status (online or offline) of a database occurs only in the specific Sync Gateway instance addressed. It is not reflected by other Sync Gateway instances using that database. To achieve that, you need to coordinate individual change operations in each of the required Sync Gateway instances.

## [](#use-cases)Use Cases

Specific uses for the database offline/online functionality include:

* Taking a database offline, without affecting other databases.
* Changing configuration properties for a database (while it is offline), without needing to restart Sync Gateway.
* Resynchronizing a database while it is offline.
* Detecting a lost DCP or TAP feed, and taking the database offline automatically.
* Creating a database in an offline state, so that the start of service delivery for the database can be postponed or coordinated across Sync Gateway instances.
* Performing a Couchbase Server upgrade.

## [](#actions)Actions

* Taking a database offline: [POST /{db}/\_offline](rest-api-admin.md#/database/post%5F%5Fdb%5F%5F%5Foffline)
* Taking a database online: [POST /{db}/\_online](rest-api-admin.md#/database/post%5F%5Fdb%5F%5F%5Fonline)

By default, when Sync Gateway starts, it brings all databases that are defined in the configuration file online. To keep a database offline when Sync Gateway starts, you can add the `offline` configuration property to the database configuration properties — see [Database Configuration](rest-api-admin.md#/Database%5FConfiguration/).

Later, to bring the database online, you can use the `POST /{db}/_online` Admin REST API request.

## [](#automatic-offlining)Automatic Offlining

Sync Gateway will take a database offline automatically if it loses the database's DCP and-or TAP feed. This enables the cause to be investigated and rectified.

Use an Admin REST API request to bring the database back online when the cause is addressed and the feed(s) restored.

## [](#state-diagram)State Diagram

The state diagram represents the states for Sync Gateway and the connection between it and a Couchbase Server database — see: [Figure 1](#fig-state-diag).

![state diagram offline 12](_images/state-diagram-offline-12.png) 

Figure 1\. State Change Diagram

In the state diagram (fig-state-diag):

* To the left of the gray dashed line, starting or stopping a Sync Gateway instance affects the connections to all of the databases that the instance serves.
* To the right of the gray dashed line, you perform operations on specific databases. For example, two databases could be online, while a third database could be taken offline, resynchronized, and then brought back online.

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