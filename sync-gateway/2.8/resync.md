---
title: Resync
description: Recalculating routing and data access following Sync Function changes
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/resync.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@sync-gateway::resync.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/resync.html)

# Resync

> Recalculating routing and data access following Sync Function changes  
> This content explains the resync feature

Related _Syc_ topics: [Configuration Properties](../current/configuration/configuration-properties-legacy.md) | [Admin REST API](../current/rest-api/rest-api-admin.md) | [databases](../current/configuration/configuration-properties-legacy.md#databases) | [sync](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-sync)

## [](#introduction)Introduction

The _Sync Function_ computes both the document routing to channels and the user access to channels at document write time.

If the Sync Function is changed, Sync Gateway needs to reprocess all existing documents in the bucket to recalculate the routing and access assignments.

To this end, the Admin REST API provides a resync endpoint that enables you initiate the reprocessing of every document in the database again.

## [](#updating-the-sync-function)Updating the Sync Function

To update the Sync Function and fully resync, you are recommended to follow the steps in [Steps to Update and Resync](#steps-to-resync).

> [!NOTE]
> This is an expensive operation because it requires every document in the database to be processed by the new function.

The database can accept no requests until this process is complete because no user's full access privileges are known until all documents have been scanned. Therefore, the Sync Function update will result in application downtime whilst the database is offline (that is, between the call to the `/{db}/_offline` and `/{db}/_online` endpoints in [Steps to Update and Resync](#steps-to-resync).

Steps to Update and Resync

1. Update the configuration file of the Sync Gateway instance
2. Restart Sync Gateway
3. Take the database offline  
Use this Admin REST API endpoint:  
[/{db}/\_offline](../current/rest-api/rest-api-admin.md#/database/post%5F%5Fdb%5F%5F%5Foffline)
4. Resync the database  
Use this Admin REST API endpoint:  
[/{db}/\_resync](../current/rest-api/rest-api-admin.md#/database/post\/post<em>db</em>%5Fresync)  
The message body of the response contains the number of changes that were made as a result of calling resync
5. Bring the database back online  
Use this Admin REST API endpoint:  
[/{db}/\_online](../current/rest-api/rest-api-admin.md#/database/post%5F%5Fdb%5F%5F%5Fonline)

## [](#when-to-run-resync)When To Run Resync?

When running a resync operation, the context in the Sync Function is the admin user. For that reason, calling the `requireUser`, `requireAccess` and `requireRole` methods will always succeed. It is very likely that you are using those functions in production to govern write operations. But in a resync operation, all the documents are already written to the database. For that reason, it is recommended to use resync for changing the assignment to channels only (i.e. reads).

If the modifications to the Sync Function only impact write security (and not routing/access), you won't need to run the resync operation.

If you wish to change the channel/access rules, but only want those rules to apply to documents written after the change was made, then you don't need to run the resync operation.

If you change the sync function to revoke a user's access to a document, the access will only take affect once a new revision to that document is saved on Sync Gateway. Running a resync operation does not revoke access to that document.

If you need to ensure access to the database during the update, you can create a read-only backup of the Sync Gateway's bucket beforehand, then run a secondary Sync Gateway on the backup bucket, in read-only mode. After the update is complete, switch to the main Gateway and bucket.

In a clustered environment with multiple Sync Gateway instances sharing the load, all the instances need to share the same configuration, so they all need to be taken offline either by stopping the process or taking them offline using the [/{db}/\_offline](../current/rest-api/rest-api-admin.md#/database/post%5F%5Fdb%5F%5F%5Foffline) endpoint. After the configuration is updated, **one** instance should be brought up so it can update the database—​if more than one is running at this time, they'll conflict with each other. After the first instance finishes opening the database, the others can be started.

## [](#related-content)Related Content

###### [](#)

Learn more …​

* [Sync Function](../current/access-control/sync-function/sync-function.md)
* [Import filter](../current/sync/import-processing.md)
* [Inter-Sync Gateway Replication](../current/sync/sync-inter-syncgateway-overview.md)
* [Sync with Couchbase Server](../current/sync/sync-with-couchbase-server.md)

###### [](#-2)

Reference material …​

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)