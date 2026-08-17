---
title: Migrate a Bucket&#8217;s Storage Backend
description: Full and Cluster Administrators can migrate a bucket's storage
  backend by calling the REST API and then performing full restores on the nodes
  containing the bucket.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/manage/pages/manage-buckets/migrate-bucket.adoc
  xref: xref:7.6@server:manage:manage-buckets/migrate-bucket.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/manage/manage-buckets/migrate-bucket.html)

# Migrate a Bucket&#8217;s Storage Backend

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

## [](#storage-backend-migration-overview)Storage Backend Migration Overview

You can migrate a bucket's storage backend if you find the bucket's current performance is not meeting your needs. For example, you can migrate a bucket from Couchstore to Magma if the bucket's working set grows beyond its memory quota.

You can migrate from Couchstore to Magma, or from Magma to Couchstore. You start a bucket's migration by calling the REST API to edit the bucket's `storageBackend` setting. This call changes the bucket's global storage backend parameter. However, it does not trigger an immediate conversion of the vBuckets to the new backend. Instead, Couchbase adds override settings to each node to indicate its vBuckets still use the old storage backend. To complete the migration, you must force the vBuckets to be rewritten. The two ways to trigger this rewrite are to perform a swap rebalance or a graceful failover followed by a full recovery. As Couchbase writes the vBuckets during these processes, it removes the storage override and saves the vBuckets using the new storage backend.

> [!NOTE]
> While you're migrating a bucket between storage backends, you can only change the bucket's `ramQuota` and `storageBackend` parameters. Couchbase Server prevents you from making changes to the bucket's other parameters.

## [](#prerequisites)Prerequisites

Before migrating a bucket, verify that the bucket's parameters meet the requirements for the new storage backend. For example, a Magma bucket must have a memory quota of at least 1 GB. The REST API call to change the bucket's storage backend returns an error if the bucket does not meet the new storage backend's requirements. See [Storage Engines](../../learn/buckets-memory-and-storage/storage-engines.md) for a list of storage backend requirements.

If you're planning to migrate from Couchstore to Magma, also consider the current disk usage on the nodes containing the bucket. Magma's default fragmentation settings can result in higher disk use. See [Disk Use Under Couchstore Verses Magma](#disk%5Fusage) for more information.

## [](#perform%5Fmigration)Perform a Migration

1. Call the REST API to change the bucket's `storageBackend` parameter. For example, the following command changes the storage backend of the travel-sample bucket to Magma.  
```console  
curl -X POST -u Administrator:password \  
  http://localhost:8091/pools/default/buckets/travel-sample \
  -d 'storageBackend=magma'  
```
2. Verify that the nodes containing the bucket now have storage backend override settings for their vBuckets. The following example calls the REST API to get the bucket configuration and filters the result through the `jq` command to list the node names and their storage backend formats.  
```console  
curl -s GET -u Administrator:password \  
    http://localhost:8091/pools/default/buckets/travel-sample \
    | jq '.nodes[] | .hostname,.storageBackend'  
```  
The output of the previous command lists each node and the backend storage format used locally by the vBuckets:  
	"node3.:8091"  
	"couchstore"  
	"node2.:8091"  
	"couchstore"  
	"node1.:8091"  
	"couchstore"
3. For every node that contains the bucket, perform either a [swap rebalance](../../install/upgrade-procedure-selection.md#swap-rebalance) or a [graceful failover](../../learn/clusters-and-availability/graceful-failover.md) followed by a [full recovery](../../learn/clusters-and-availability/recovery.md#full-recovery) and [rebalance](../../learn/clusters-and-availability/rebalance.md) to rewrite the vBuckets on the node. Both of these methods have their own limitations. Swap rebalance requires that you add an additional node to the cluster. The graceful failover and full recovery method temporarily removes a node from your cluster which can cause disruptions.  
You can take these steps via the UI, the command-line tool, or REST API calls. The following example demonstrates using the REST API to perform a graceful failover and full recovery on a node named node3.

  1. Perform a graceful failover of node3:  
  ```console  
  curl -X POST -u Administrator:password \  
       http://localhost:8091/controller/startGracefulFailover \
     -d 'otpNode=ns_1@node3.'  
  ```
  2. Wait until the failover is complete. Then perform a full recovery on the node:  
  ```console  
  curl -X POST -u Administrator:password \  
      http://localhost:8091/controller/setRecoveryType \
    -d 'otpNode=ns_1@node3.' \
    -d 'recoveryType=full'  
  ```
  3. When recovery is complete, perform a rebalance:  
  ```console  
  curl -X POST -u Administrator:password  \  
      http://localhost:8091/controller/rebalance \
    -d 'knownNodes=ns_1@node1.,ns_1@node2.,ns_1@node3.'  
  ```
4. After triggering each node to rewrite its vBuckets, verify the node is now using the new storage backend. Re-run the command from step 2 to list the nodes and any storage backend overrides:  
```console  
curl -s GET -u Administrator:password \  
    http://localhost:8091/pools/default/buckets/travel-sample \  
    jq '.nodes[] | .hostname,.storageBackend'  
"node3.:8091"  
null  
"node2.:8091"  
"couchstore"  
"node1.:8091"  
"couchstore"  
```  
The `null` under node3 indicates that it does not have a storage backend override. It has migrated to the new storage backend.
5. Repeat the previous two steps for the remaining nodes in the cluster.

## [](#disk%5Fusage)Disk Use Under Couchstore Verses Magma

If you migrate a bucket's storage from Couchstore to Magma, you may see increased disk usage. Couchstore's default threshold for fragmentation is 30%. When a Couchstore bucket reaches this threshold, Couchbase Server attempts to fully compact the bucket. If the bucket has a low write workload, Couchbase Server may be able to compact the bucket to 0% fragmentation.

Magma's default fragmentation threshold is 50%. Couchbase Server treats this threshold differently than the Couchstore threshold. Couchbase Server does not perform a full compaction with the goal of reducing the bucket's fragmentation to 0%. Instead, Couchbase Server compacts a Magma bucket to maintain its fragmentation at the threshold value. This maintenance of the default 50% fragmentation can result in greater disk use for a Magma-backed bucket verses the Couchstore-backed bucket.

If a bucket you migrated to Magma has higher sustained disk use that interferes with the node's performance, you have two options:

* Reduce the fragmentation threshold of the Magma bucket. For example, you can choose to reduce the fragmentation threshold to 30%. You must consider changing the threshold only if the bucket's workload is not write-intensive. For write-intensive workloads, the best practice for Magma buckets is to leave the fragmentation setting at 50%. See [Auto-Compaction](../manage-settings/configure-compact-settings.md) to learn how to change the bucket's database fragmentation setting.
* Roll back the migration. You can revert a bucket from Magma back to Couchstore during or after a migration. See the next section for more information.

## [](#rolling-back-a-migration)Rolling Back a Migration

As you migrate each node's vBuckets to a new storage backend, you may decide that the migration is not meeting your needs. For example, you may see increased disk usage when moving from Couchstore to Magma as explained in [Disk Use Under Couchstore Verses Magma](#disk%5Fusage).

### [](#prerequisites-2)Prerequisites

You can rollback a migration from Magma to Couchstore by deactivating the history retention on the buckets, where Magma is the backend storage.

Follow these steps to rollback storage from Magma to Couchstore:

1. Run the following command to deactivate the parameter `historyRetentionCollectionDefault` for all the collections within the bucket.  
```console  
curl -v -X POST http://localhost:8091/pools/default/buckets/testbucket -u Administrator -d historyRetentionCollectionDefault=false  
```  
For more information, see the [historyRetentionCollectionDefault](../../rest-api/rest-bucket-create.md#historyretentioncollectiondefault) parameter details.
2. Run the following command for each existing collections to deactivate the associated history retention on the bucket.  
```console  
curl -X PATCH -u Administrator http://localhost:8091/pools/default/buckets/testbucket/scopes/_default/collections/_default -d history=false  
```  
For more information about creating and editing a collection, see [Creating and Editing a Collection](../../rest-api/creating-a-collection.md#description).

### [](#procedure)Procedure

You can roll back the migration by doing the following:

1. Changing the bucket's backend setting to its original value.
2. Force any migrated nodes to rewrite their vBuckets back to the old backend.

Perform the steps only for the nodes you migrated.

For example, to roll back the migration explained in [Perform a Migration](#perform%5Fmigration), follow these steps:

1. Call the REST API to change back the bucket's backend storage to Couchstore:  
```console  
curl -X POST -u Administrator:password \  
  http://localhost:8091/pools/default/buckets/travel-sample \
  -d 'storageBackend=couchstore'  
```
2. Determine which nodes you have already migrated by calling the REST API to get the bucket's metadata:  
```console  
curl -s GET -u Administrator:password \  
    http://localhost:8091/pools/default/buckets/travel-sample \
    | jq '.nodes[] | .hostname,.storageBackend'  
```  
For the migration explained in [Perform a Migration](#perform%5Fmigration), the output appears as follows:  
```json  
"node3.:8091"  
"magma"  
"node2.:8091"  
null  
"node1.:8091"  
null  
```  
In this case, you must roll back node3 because you migrated it to Magma.
3. For each node that you have already migrated, perform another [swap rebalance](../../install/upgrade-procedure-selection.md#swap-rebalance) or a [graceful failover](../../learn/clusters-and-availability/graceful-failover.md), then perform a [full recovery](../../learn/clusters-and-availability/recovery.md#full-recovery) and [rebalance](../../learn/clusters-and-availability/rebalance.md) to roll back the vBuckets on the node to the previous backend.  
To roll back node3, follow these steps:

  1. Perform a graceful failover of node3:  
  ```console  
  curl -X POST -u Administrator:password \  
       http://localhost:8091/controller/startGracefulFailover \
     -d 'otpNode=ns_1@node3.'  
  ```
  2. Wait until the failover is complete. Then perform a full recovery on the node:  
  ```console  
  curl -X POST -u Administrator:password \  
      http://localhost:8091/controller/setRecoveryType \
    -d 'otpNode=ns_1@node3.' \
    -d 'recoveryType=full'  
  ```
  3. When recovery is complete, perform a rebalance:  
  ```console  
  curl -X POST -u Administrator:password  \  
      http://localhost:8091/controller/rebalance \
    -d 'knownNodes=ns_1@node1.,ns_1@node2.,ns_1@node3.'  
  ```
4. Repeat the previous step until you have rolled back all of the migrated nodes to their original storage backend.