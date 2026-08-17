---
title: Database Management
description: Describes the various database management functions available to
  maintain an efficient sync gateway database
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/ROOT/pages/database-management.adoc
  xref: xref:sync-gateway::database-management.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/database-management.html)

# Database Management

> Describes the various database management functions available to maintain an efficient sync gateway database  
> Revisions are at the heart of Couchbase Mobile's ability to respond flexibly and securely to changing data from server to edge.

## [](#lbl-prune)Revision Pruning

In the section

[Algorithm](#lbl-alg) | [Controls](#lbl-rtctrl) | [Constraints](#lbl-rtcons) | [Learn More](#lbl-rt-more)

Pruning is the process of removing obsolete revisions. It automatically runs whenever a new revision is generated.

> [!TIP]
> Use the Admin Rest API endpoint for [Database Configuration](rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration) or [Database Configuration](rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration) to provision any configuration changes to properties described in this content.

### [](#lbl-alg)Algorithm

Although fundamentally the same, the pruning algorithm works slightly differently between Sync Gateway and Couchbase Lite.

On Sync Gateway, the pruning algorithm retains a configurable number of revisions (revs\_limit) and removes all older revisions.

### [](#lbl-rtctrl)Controls

You can vary the number of retained revisions using the Configuration File's [revs\_limit](configuration/configuration-schema-database.md#database-revs%5Flimit) setting.

So, for example, with a `revs_limit` of 1,000 the algorithm keeps the last 1,000 revisions in the shortest non-tombstoned branch and remove any others from that branch.

---

Sync Gateway 4.x uses automatic conflict resolution with Last Write Wins strategy, allowing `revs_limit` values as low as 1\. In earlier versions, setting `revs_limit` below 100 when `allow_conflicts = true` can lead to data loss during conflict resolution due to insufficient revision history. ---

### [](#lbl-rtcons)Constraints

The presence of multiple unresolved conflicts in a revision tree can impair the pruning process.

### [](#lbl-rt-more)Learn More

To learn more about revision pruning and database size management in general see: [Pruning — Managing DB Sizes in Couchbase Mobile](https://blog.couchbase.com/database-sizes-and-conflict-resolution/#pruning).

## [](#lbl-tomb-purge)Purging Tombstones

Sync Gateway automatically purges tombstones from the bucket based on the server's metadata purge interval.

Tombstones can also be manually removed via Sync Gateway's [/{keyspace}/\_purge](rest-api/rest%5Fapi%5Fadmin.md#tag/Document/operation/post%5Fkeyspace-%5Fpurge) endpoint.

Purging of tombstones is also required on Couchbase Lite. For example, you might decide that if a Couchbase Lite client deletes a document, you want to purge the document (on that device) as soon as the delete replicates to Sync Gateway.

## [](#lbl-tomb-cache)Cache Ejection

Deleted/expired tombstones are not automatically ejected from Sync Gateway's in-memory channel caches. See [Table 1](#tbl-tomb-cache), which shows when channel caches are ejected.

__Table 1\. Flushing Sync Gateway channel caches__
| **TombstonePurged On** | Value of enable\_shared\_bucket\_access                                                   |                                                                                                                                                                                                                                   |
| ---------------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **false**              | true                                                                                      |                                                                                                                                                                                                                                   |
| **Couchbase Server**   | Restarting Sync Gateway flushes the cache                                                 | Restarting Sync Gateway flushes the cache Running the [/{db}/\_compact](rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Fcompact) endpoint removes purged tombstones from the channel cache {fn-211} |
| **Sync Gateway**       | Restarting Sync Gateway flushes the cache. Starting in 2.1.1, this is done automatically. | Restarting Sync Gateway flushes the cache. Starting in 2.1.1, this is done automatically.                                                                                                                                         |

## [](#compacting)Compacting

Attachments added post 3.0 are automatically removed from the bucket upon reference removal, document delete or document purge. This contrasts with the behavior of Legacy attachments, which can remain in the bucket even after their reference removal, document delete or document purge.

The compaction garbage collection process (`/{db}/_compact`) will remove these legacy attachments and reclaim the underlying storage.

You can run the garbage collection process in one of two modes:

* tombstone  
Purges the JSON bodies of non-leaf revisions.
* attachment  
Removes redundant legacy attachments.  
The legacy attachment compaction process scans all documents in the bucket, removing unreferenced attachments.

See the REST API call endpoint [{db}/\_compact](rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Fcompact).

## [](#resync)Resync

### [](#why)Why

The _Sync Function_ computes both the document routing to channels and the user access to channels at document write time.

If the Sync Function is changed, Sync Gateway needs to reprocess all existing documents in the bucket to recalculate the routing and access assignments.

To this end, the Admin REST API provides a `/{db}/_resync` endpoint that enables you to initiate the reprocessing of every document in the database again.

### [](#how)How

To update the Sync Function and fully `resync`, you're recommended to follow the steps in [Steps to Update and Resync](#steps-to-resync).

> [!NOTE]
> This is an expensive operation because the new function must process every document in the database.

The database cannot accept requests until this process completes because the database does not know any user's full access privileges until it scans all documents. Therefore, the Sync Function update results in application downtime whilst the database is offline (that's between the call to the `/{db}/_offline` and `/{db}/_online` endpoints in [Steps to Update and Resync](#steps-to-resync).

Steps to Update and Resync

1. Update the configuration file of the Sync Gateway instance.
2. Restart Sync Gateway.
3. Take the database offline. Use this Admin REST API endpoint: [/{db}/\_offline](rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Foffline)
4. Resync the database. Use this Admin REST API endpoint: [/{db}/\_resync](rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Fresync)  
The message body of the response contains the number of changes that were made as a result of calling resync.
5. Bring the database back online. Use this Admin REST API endpoint:  
[/{db}/\_online](rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Fonline)

### [](#uses)Uses

#### [](#changing-channel-assignment)Changing Channel Assignment

When running a resync operation, the context in the Sync Function is the admin user. For that reason, calling the methods `requireUser`, `requireAccess`, and `requireRole` always succeeds. You may be using these functions in production to govern write operations. But in a resync operation, all the documents are already written to the database. For that reason, it's recommended to use resync for changing the assignment to channels only (i.e. reads).

#### [](#changing-write-security-only)Changing Write Security Only

If the modifications to the Sync Function only impact write security (and not routing/access), you'll not need to run the resync operation.

#### [](#changing-channelaccess-rules)Changing Channel/Access Rules

If you want to change the channel/access rules, but only want those rules to apply to documents written after the change was made, then you do not need to run the resync operation.

#### [](#access-revocation)Access Revocation

If you change the sync function to revoke a user's access to a document, the access only takes effect once a new revision to that document saves on Sync Gateway. Running a resync operation does not revoke access to that document.

### [](#database-availability)Database Availability

If you need to ensure access to the database during the update, you can create a read-only backup of the Sync Gateway's bucket beforehand, then run a secondary Sync Gateway on the backup bucket, in read-only mode. After the update is complete, switch to the main Gateway and bucket.

In a clustered environment with multiple Sync Gateway instances sharing the load, all the instances need to share the same configuration, so they all need to be taken offline either by stopping the process or taking them offline using the [/{db}/\_offline](rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Management/operation/post%5Fdb-%5Foffline) endpoint. After the configuration is updated, **one** instance should be brought up so it can update the database—​if more than one is running at this time, they'll conflict with each other. After the first instance finishes opening the database, the others can be started.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](access-control/sync-function/sync-function.md)
* [Import filter](sync/import-processing.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api/rest-api.md)
* [Admin REST API](rest-api/rest-api-admin.md)
* [Metrics REST API](rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)