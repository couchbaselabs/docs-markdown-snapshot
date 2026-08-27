---
title: Take Database Offline/Online
description: How to take a <em>Sync&nbspGateway</em> database offline and bring back online.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/manage/pages/database-offline.adoc
  xref: xref:sync-gateway:manage:database-offline.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/manage/database-offline.html)

# Take Database Offline/Online

> How to take a _Sync Gateway_ database offline and bring back online.  

Sync Gateway enables you to take a database offline and bring it back online without stopping the Sync Gateway instance and without affecting other databases it serves.

The change of status (online or offline) of a database occurs only in the specific Sync Gateway instance addressed. It's not reflected by other Sync Gateway instances using that database. If you want to make changes in multiple Sync Gateway instances, you need to coordinate individual change operations in each instance.

## [](#when-to-take-a-database-offlineonline)When To Take a Database Offline/Online

You may need to take a database offline or bring it back online in the following scenarios:

* You need to take a single database offline without affecting other databases.
* You need to change the configuration properties for a database without restarting Sync Gateway.
* You need to [resynchronize a database](resync.md) while it's offline.
* You created a database in an offline state, so you can postpone or coordinate the start of service delivery for the database across Sync Gateway instances.
* You need to run a Couchbase Server upgrade.

### [](#state-diagram)State Diagram

The state diagram in [Figure 1](#fig-state-diag) represents the states for Sync Gateway and the connection between it and a Couchbase Server database.

![state diagram offline 12](../_images/state-diagram-offline-12.png) 

Figure 1\. State Change Diagram

The state diagram illustrates 2 types of operations:

* **Instance-level operations**: Starting or stopping a Sync Gateway instance affects the connections to all of the databases that the instance serves.
* **Database-level operations**: You can perform operations on specific databases independently. For example, 2 databases could be online, while you take a third database offline, resynchronize it, and then bring it back online.

## [](#sync-gateway-configuration-mode-considerations)Sync Gateway Configuration Mode Considerations

The workflow for taking databases offline/online differs depending on your configuration mode:

### [](#persistent-configuration)Persistent Configuration

If you use the **Persistent Configuration** mode for Sync Gateway (default since Sync Gateway 3.0), Couchbase Server stores your configuration.

When you take a database offline or bring it online using the `POST /{db}/_config` endpoint with `{"offline": true/false}`, Sync Gateway updates the database configuration in the bucket and propagates the change automatically to all Sync Gateway nodes.

> [!IMPORTANT]
> Use `POST /{db}/_config` for this, not `PUT /{db}/_config`. `PUT /{db}/_config` replaces the entire database configuration with whatever payload you send. If your request body contains only `{"offline": true}` and omits the rest of the database's current configuration, `PUT` resets those omitted fields to their defaults. `POST /{db}/_config` performs a partial update instead: it changes only the fields you include and leaves everything else untouched. Because the offline/online examples here send just a single field, `POST` is the safer choice unless you are certain you're submitting the complete current configuration.

The state transition is asynchronous. Database states transition through: Offline → Starting → Online or Online → Stopping → Offline. This transition is typically quick (1 second or less), unless going from Offline → Online and Sync Gateway needs to build indexes.

You can use a Load Balancer for configuration changes in persistent configuration mode. For more information about Load Balancers, see [Load Balancer](../deploy/load-balancer.md).

> [!NOTE]
> With this configuration mode, you cannot use the `/{db}/_offline` and `/{db}/_online` endpoints as these are node-local only.

### [](#non-persistent-configuration-legacy)Non-Persistent Configuration (Legacy)

If you use the **Non-Persistent Configuration** mode for Sync Gateway, local config files store your configuration.

You must coordinate any changes to your configuration across all Sync Gateway nodes manually. You cannot use a Load Balancer for configuration changes.

With this configuration mode, you must use the `POST /{db}/_offline` and `POST /{db}/_online` endpoints on each individual node you want to take offline or bring online.

## [](#take-a-database-offline-manually)Take a Database Offline Manually

This section describes how to manually take a database offline.

* Persistent Configuration
* Non-Persistent Configuration

Use this method when your Sync Gateway configuration is stored in Couchbase Server (default since Sync Gateway 3.0).

1. Make a POST request to [/{db}/\_config](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/post%5Fdb-%5Fconfig) with `{"offline": true}`.  
This updates the database configuration persisted in the bucket, and all nodes go offline.  
You can use a Load Balancer for this operation.  
> [!NOTE]  
> The state transition is asynchronous. The database transitions from Online → Stopping → Offline, typically in less than 1 second.

Use this method when local config files store your Sync Gateway configuration (legacy mode).

1. Make a POST request to [/{db}/\_offline](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Foffline) on each node individually.  
This modifies the state on the current node only.  
Do not use a Load Balancer.

## [](#take-a-database-online-manually)Take a Database Online Manually

This section describes how to manually bring a database online.

* Persistent Configuration
* Non-Persistent Configuration

Use this method when Couchbase Server stores your Sync Gateway configuration (default since Sync Gateway 3.0).

1. Make a POST request to [/{db}/\_config](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/post%5Fdb-%5Fconfig) with `{"offline": false}`.  
This updates the database configuration persisted in the bucket, and all nodes will go online.  
You can use a Load Balancer for this operation.  
> [!NOTE]  
> The state transition is asynchronous. The database transitions from Offline → Starting → Online, typically in less than 1 second unless Sync Gateway needs to build indexes.

Use this method when local config files store your Sync Gateway configuration (legacy mode).

1. Make a POST request to [/{db}/\_online](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Fonline) on each node individually.  
This modifies the state on the current node only.  
Do not use a Load Balancer.

## [](#starting-with-a-database-offline)Starting with a Database Offline

By default, when Sync Gateway starts, it brings all databases that the configuration file defines online.

To keep a database offline when Sync Gateway starts, you can add the `offline` configuration property to the database configuration properties. For more information, see [Database Configuration](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration).

Later, to bring the database online, use the appropriate method for your configuration mode as described in [Take a Database Online Manually](#take-a-database-online-manually).

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