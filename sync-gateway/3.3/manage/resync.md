---
title: Resync
description: Recalculating routing and data access following Sync Function changes
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/manage/pages/resync.adoc
  xref: xref:3.3@sync-gateway:manage:resync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.3/manage/resync.html)

# Resync

> Recalculating routing and data access following Sync Function changes  
> This content explains the resync feature

Related _sync_ topics: [Admin REST API](../rest-api/rest-api-admin.md) | [Database Configuration](../configuration/configuration-schema-database.md) | [database.sync](../configuration/configuration-schema-database.md#database-sync) | [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

## [](#introduction)Introduction

The _Sync Function_ computes both the document routing to channels and the user access to channels at document write time.

If the Sync Function is changed, Sync Gateway needs to reprocess all existing documents in the bucket to recalculate the routing and access assignments.

## [](#resync-api)Resync API

The Admin REST API provides a [POST /{db}/\_resync](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Fresync) endpoint that enables you to start or stop a resync operation. Starting the resync will initiate the reprocessing of every document in the database again.

There is also a 'support-only' option to regenerate sequences whilst resyncing.

The resync action is carried out **only** on the node that the POST is made to. It is not cross-node aware.

In a multi-node cluster, the resync must be only run on one node. Users should take other nodes offline before initiating this action. Starting resync on more than one node will result in multiple instances running, with undefined system behavior.

The resync operation is run asynchronously. Use [GET /{db}/\_resync](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/get%5Fdb-%5Fresync) to establish the current status of a resync operation.

## [](#updating-the-sync-function)Updating the Sync Function

To update the Sync Function and fully resync, you are recommended to follow the steps in [Steps to Update and Resync](#steps-to-resync).

> [!NOTE]
> This is an expensive operation because it requires every document in the database to be processed by the new function.

The database can accept no requests until resync is complete because no user's full access privileges are known until all documents have been scanned. Therefore, the Sync Function update will result in application downtime whilst the database is offline (that is, between the call to the `/{db}/_offline` and `/{db}/_online` endpoints in [Steps to Update and Resync](#steps-to-resync).

You won't need to run the resync operation, if either:

* The modifications to the Sync Function only impact write security (and not routing/access), or,
* You only want changes to channel/access rules to apply to documents written after the change was made.

Steps to Update and Resync

1. Update the configuration file of the Sync Gateway instance.
2. Restart Sync Gateway.
3. Take the database offline. Use this Admin REST API endpoint: [/{db}/\_offline](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Foffline)
4. Resync the database. Use this Admin REST API endpoint: [POST /{db}/\_resync](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Fresync)
5. Monitor the resync status using [GET /{db}/\_resync](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/get%5Fdb-%5Fresync) to see when it completes.  
The message body of the response contains the number of changes that were made as a result of calling resync.
6. Bring the database back online. Use this Admin REST API endpoint: [/{db}/\_online](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Fonline)

## [](#running-resync)Running Resync

Resync is run asynchronously. Its status can be monitored using [GET /{db}/\_resync](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/get%5Fdb-%5Fresync).

Be sure to take the database offline using [/{db}/\_offline](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Foffline).

### [](#resync-context)Resync Context

When running a resync operation, the context in the Sync Function is the admin user. For that reason, calling the methods `requireUser`, `requireAccess`, and `requireRole` will always succeed. It is very likely that you are using those functions in production to govern write operations. But in a resync operation, all the documents are already written to the database. For that reason, it is recommended to use resync for changing the assignment to channels only (i.e. reads).

### [](#revoking-access)Revoking Access

If you change the sync function to revoke a user's access to a document, the access will only take effect once a new revision to that document is saved on Sync Gateway. Running a resync operation does not revoke access to that document.

### [](#availability)Availability

If you need to ensure access to the database during a Sync function update and resync, you can create a read-only backup of the Sync Gateway's bucket beforehand, then run a secondary Sync Gateway on the backup bucket, in read-only mode. Once you detect the resync is complete, switch back to the main Sync Gateway and bucket.

### [](#updating-clusters)Updating Clusters

In a clustered environment with multiple Sync Gateway instances sharing the load, all the instances need to share the same configuration. To ensure this happens, you must taken all instances offline using the [/{db}/\_offline](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Foffline) endpoint.

After the configuration is updated, **one** instance should be brought up so it can update the database—​if more than one is running at this time, they'll conflict with each other. After the first instance finishes opening the database, the others can be started.

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