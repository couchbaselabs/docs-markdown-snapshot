---
title: Resync
description: Recalculating routing and data access following Sync Function changes
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/manage/pages/resync.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.0@sync-gateway:manage:resync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/4.0/manage/resync.html)

# Resync

> Recalculating routing and data access following Sync Function changes  
> This content explains the resync feature

Related _sync_ topics: [Admin REST API](../rest-api/rest-api-admin.md) | [Database Configuration](../configuration/configuration-schema-database.md) | [database.sync](../configuration/configuration-schema-database.md#database-sync) | [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

## [](#introduction)Introduction

The _Sync Function_ computes both the document routing to channels and the user access to channels at document write time.

If you change the Sync Function, Sync Gateway needs to reprocess all existing documents in the bucket to recalculate the routing and access assignments. A resync operation does this reprocessing.

### [](#when-to-use-resync)When to Use Resync

You need to run a resync operation when:

* You have modified the Sync Function in a way that affects document routing to channels.
* You have changed access control rules in the Sync Function.
* You want the changes to apply to all existing documents in the database.

You'll not need to run the resync operation if either:

* The modifications to the Sync Function only impact write security, and not routing/access.
* You only want changes to channel/access rules to apply to documents written after you made the change.

### [](#resync-api)Resync API

The Admin REST API provides a [POST /{db}/\_resync](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Fresync) endpoint that enables you to start or stop a resync operation. Starting the resync initiates the reprocessing of every document in the database.

The resync operation runs asynchronously. Use [GET /{db}/\_resync](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/get%5Fdb-%5Fresync) to monitor the current status of a resync operation.

> [!IMPORTANT]
> When using nonpersistent (legacy) configuration, the resync action is carried out **only** on the node that the POST is made to. It is not cross-node aware. In a multi-node cluster, the resync must only run on 1 node. Starting resync on more than 1 node results in multiple instances running, with undefined system behavior. When using persistent configuration (default since Sync Gateway 3.0), resync operations work across all nodes automatically.

> [!NOTE]
> There's also a 'support-only' option to regenerate sequences while resyncing.

## [](#update-sync-function-and-resync)Update Sync Function and Resync

This section describes how to update your Sync Function and perform a full resync of your database.

> [!IMPORTANT]
> This is an expensive operation because the new function must process every document in the database. The database cannot accept requests until resync is complete because Sync Gateway cannot determine any user's full access privileges until it scans all documents. Therefore, the Sync Function update results in application downtime while the database is offline.

* Persistent Configuration
* Non-Persistent Configuration

Use this method when Couchbase Server stores your Sync Gateway configuration (default since Sync Gateway 3.0).

Prerequisites

* The database is online.  
Procedure

  1. Update the configuration file of the Sync Gateway instance.
  2. Restart Sync Gateway.
  3. [Take the database offline](database-offline.md#%5Fpersistent%5Fconfiguration) using `PUT /{db}/_config` with `{"offline": true}` (can use Load Balancer).  
  This updates the database configuration persisted in the bucket, and all nodes will go offline.
  4. Run resync using [POST /{db}/\_resync](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Fresync) (you can call this on any node or through Load Balancer).
  5. Monitor resync status using [GET /{db}/\_resync](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/get%5Fdb-%5Fresync).  
  The message body of the response contains the number of changes that resync made.
  6. [Bring the database back online](database-offline.md#%5Fpersistent%5Fconfiguration%5F2) using `PUT /{db}/_config` with `{"offline": false}` (can use Load Balancer).  
  This updates the database configuration persisted in the bucket, and all nodes go online.

Use this method when local config files store your Sync Gateway configuration (legacy mode).

Prerequisites

* The database is online.  
Procedure

  1. Update the configuration file on all nodes.
  2. Restart Sync Gateway.
  3. [Take the database offline](database-offline.md#%5Fnon%5Fpersistent%5Fconfiguration) by calling `POST /{db}/_offline` on each node individually (do not use Load Balancer).  
  This modifies the state on the current node only.
  4. Run resync using [POST /{db}/\_resync](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Fresync) on a single node only (do not use Load Balancer).
  5. Monitor resync status using [GET /{db}/\_resync](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/get%5Fdb-%5Fresync).  
  The message body of the response contains the number of changes that resync made.
  6. [Bring the database back online](database-offline.md#%5Fnon%5Fpersistent%5Fconfiguration%5F2) by calling `POST /{db}/_online` on each node individually (do not use Load Balancer).  
  This modifies the state on the current node only.

## [](#resync-considerations)Resync Considerations

This section covers important considerations when running a resync operation.

### [](#resync-context)Resync Context

When running a resync operation, the context in the Sync Function is the admin user. For that reason, calling the methods `requireUser`, `requireAccess`, and `requireRole` always succeeds. You may use those functions in production to govern write operations. But in a resync operation, all the documents are already written to the database. For that reason, it's recommended to use resync for changing the assignment to channels only (i.e. reads).

### [](#revoking-access)Revoking Access

If you change the sync function to revoke a user's access to a document, the access only takes effect once you save a new revision to that document on Sync Gateway. Running a resync operation does not revoke access to that document.

### [](#maintaining-availability-during-resync)Maintaining Availability During Resync

If you need to verify access to the database during a Sync function update and resync, you can create a read-only backup of the Sync Gateway's bucket beforehand, then run a secondary Sync Gateway on the backup bucket in read-only mode. Once you detect the resync is complete, switch back to the main Sync Gateway and bucket.

### [](#monitoring-resync-status)Monitoring Resync Status

Resync runs asynchronously. Monitor its status with [GET /{db}/\_resync](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/get%5Fdb-%5Fresync).

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](../access-control/sync-function/sync-function.md)
* [Import filter](../sync/import-processing.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Add/Update Sync Function](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
* [Sync Function Overview](../access-control/sync-function/sync-function.md)

###### [](#-3)

Reference material …​

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)