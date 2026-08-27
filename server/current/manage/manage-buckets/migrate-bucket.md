---
title: Migrate a Bucket&#8217;s Storage Backend
description: Full and Cluster Administrators can migrate a bucket's storage
  backend by calling the REST API and then performing full restores on the nodes
  containing the bucket.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/manage/pages/manage-buckets/migrate-bucket.adoc
  xref: xref:server:manage:manage-buckets/migrate-bucket.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/manage/manage-buckets/migrate-bucket.html)

# Migrate a Bucket&#8217;s Storage Backend

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

## [](#storage-backend-migration-overview)Storage Backend Migration Overview

You can migrate a bucket's storage backend if you find the bucket's current performance is not meeting your needs. For example, you can migrate a bucket from Couchstore to Magma if the bucket's working set grows beyond its memory quota. You can migrate from Couchstore to Magma, or from Magma to Couchstore. Migrating to a Magma bucket always results in a bucket with 1024 vBuckets, regardless of the number of vBuckets in the original bucket.

> [!NOTE]
> The backend migration described in this section does not support migrating between buckets with different numbers of vBuckets. You cannot migrate a Couchstore or Magma bucket with 1024 vBuckets to a Magma bucket with 128 vBuckets. Similarly, you cannot migrate from a Magma bucket with 128 vBuckets to a Couchstore or a Magma bucket with 1024 vBuckets. To migrate between buckets with different number of vBuckets, you can use a local cross datacenter replication (XDCR). See [XDCR Storage Backend Migration](#xdcr-migration) for more information.

You start a bucket's migration by calling the REST API to edit the bucket's [storageBackend](../../rest-api/rest-bucket-create.md#storagebackend) setting. This call changes the bucket's global storage backend parameter. However, it does not trigger an immediate conversion of the vBuckets to the new backend. Instead, Couchbase adds override settings to each node to indicate its vBuckets still use the old storage backend. To complete the migration, you must force the vBuckets to be rewritten. The two ways to trigger this rewrite are to perform a swap rebalance or a graceful failover followed by a full recovery. As Couchbase writes the vBuckets during these processes, it removes the storage override and saves the vBuckets using the new storage backend.

> [!NOTE]
> When migrating a bucket between storage backends, you can edit only the bucket's [ramQuota](../../rest-api/rest-bucket-create.md#ramQuota), [evictionPolicy](../../rest-api/rest-bucket-create.md#evictionpolicy), and [storageBackend](../../rest-api/rest-bucket-create.md#storagebackend) parameters. Couchbase Server prevents you from making changes to the other bucket parameters.

## [](#prerequisites)Prerequisites

Before migrating a bucket, verify that the bucket's parameters meet the requirements for the new storage backend. For example, a Magma bucket must have a memory quota of at least 1 GB. The REST API call to change the bucket's storage backend returns an error if the bucket does not meet the new storage backend's requirements. See [Storage Engines](../../learn/buckets-memory-and-storage/storage-engines.md) for a list of storage backend requirements.

If you're planning to migrate from Couchstore to Magma, also consider the current disk usage on the nodes containing the bucket. Magma's default fragmentation settings can result in higher disk use. See [Disk Use Under Couchstore Verses Magma](#disk%5Fusage) for more information.

You should also consider changing the bucket's ejection policy. The Full Ejection policy works well for Magma buckets, especially when the ratio of memory to data storage is low. Magma allows you to set a memory to data storage ratio as low as 1%. Couchstore buckets usually work best with Value Only Ejection. See [Ejection](../../learn/buckets-memory-and-storage/memory.md#ejection) for more information about ejection policies.

You can change the ejection policy at the same time you change the storage backend. If you choose to do so, you must set the `noRestart` parameter to `true` in the REST API call to change the storage backend. This setting prevents Couchbase Server from restarting the bucket after changing the storage backend. If you do not set `noRestart` to `true`, Couchbase Server does not change the ejection policy. Instead of taking effect after a bucket restart, the new ejection policy takes effect after you finish the backend migration.

See [Change Ejection Policy During a Backend Storage Migration](change-ejection-policy.md#change-during-migration) for more information.

## [](#perform%5Fmigration)Perform a Migration

1. Call the REST API to change the bucket's `storageBackend` parameter. For example, the following command changes the storage backend of the travel-sample bucket to Magma.  
```console  
curl -X POST -u Administrator:password \  
  http://localhost:8091/pools/default/buckets/travel-sample \
  -d 'storageBackend=magma'  
```  
If you also want to change the bucket's ejection policy, you can do so at the same time by adding the `evictionPolicy` and `noRestart` parameters to the REST API call. For example, the following command changes the storage backend of the `travel-sample` bucket to Magma and sets the ejection policy to Full Ejection without restarting the bucket immediately:  
```console  
curl -X POST -u Administrator:password \  
  http://localhost:8091/pools/default/buckets/travel-sample \
  -d 'storageBackend=magma' \
  -d 'evictionPolicy=fullEviction' \
  -d 'noRestart=true'  
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

Magma's default fragmentation threshold is 50%. Couchbase Server treats this threshold differently than the Couchstore threshold. It does not perform a full compaction with the goal of reducing the bucket's fragmentation to 0%. Instead, Couchbase Server compacts a Magma bucket to maintain its fragmentation at the threshold value. This maintenance of the default 50% fragmentation can result in greater disk use for a Magma-backed bucket verses the Couchstore-backed bucket.

If a bucket you migrated to Magma has higher sustained disk use that interferes with the node's performance, you have two options:

* Reduce the fragmentation threshold of the Magma bucket. For example, you could choose to reduce the fragmentation threshold to 30%. You should only consider changing the threshold if the bucket's workload is not write-intensive. For write-intensive workloads, the best practice for Magma buckets is to leave the fragmentation setting at 50%. See [Auto-Compaction](../manage-settings/configure-compact-settings.md) to learn how to change the bucket's database fragmentation setting.
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

You can roll back the migration by:

1. Changing the bucket's backend setting to its original value.
2. Force any migrated nodes to rewrite their vBuckets back to the old backend.

You do not have to perform any steps for nodes you did not migrate.

For example, to roll back the migration shown in [Perform a Migration](#perform%5Fmigration), you would follow these steps:

1. Call the REST API to change the bucket's backend back to Couchstore:  
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
For the migration shown in [Perform a Migration](#perform%5Fmigration), the output looks like this:  
```json  
"node3.:8091"  
"magma"  
"node2.:8091"  
null  
"node1.:8091"  
null  
```  
In this case, you must roll back node3 because you migrated it to Magma.
3. For each node that you have already migrated, perform another [swap rebalance](../../install/upgrade-procedure-selection.md#swap-rebalance) or a [graceful failover](../../learn/clusters-and-availability/graceful-failover.md) followed by a [full recovery](../../learn/clusters-and-availability/recovery.md#full-recovery) and [rebalance](../../learn/clusters-and-availability/rebalance.md) to roll the vBuckets on the node back to the previous backend.  
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
4. Repeat the previous step until all nodes that you'd migrated have rolled back to their original storage backend.

## [](#xdcr-migration)XDCR Storage Backend Migration

You can use [Cross Data Center Replication (XDCR)](../../learn/clusters-and-availability/xdcr-overview.md) to migrate data between two buckets with different storage backends, including between Magma buckets using different numbers of vBuckets. You can perform this migration on the same cluster or between two clusters.

> [!NOTE]
> Versions of Couchbase Server before 8.0 do not support XDCR replication between buckets with different numbers of vBuckets. They also do not support Magma buckets with 128 vBuckets. Due to both these limitations, you cannot replicate from a pre-8.0 cluster to a Magma bucket with 128 vBuckets. You can replicate in the opposite direction (from a Magma bucket with 128 vBuckets to a pre-8.0 cluster) because Magma buckets on Couchbase Server 8.0 and later can replicate to buckets with a different number of vBuckets. However, you should avoid doing so because bidirectional replication is impossible in this configuration.

To perform an XDCR storage backed migration on the same cluster, it must have enough memory and storage for two copies of the bucket's data. After the migration, you can drop the original bucket to free the resources it uses.

The process for performing a backend migration using XDCR is similar to configuring any other XDCR replication. The only difference is that the source and destination of the replication are the same cluster.

The following steps demonstrate migrating a Magma bucket with 128 vBuckets named `travel-sample` to a Magma bucket with 1024 vBuckets named `travel-sample-1024`:

1. Create a new bucket named `travel-sample-1024` using the Magma storage backend with 1024 vBuckets. For more information about creating a bucket, see [Create a Bucket](create-bucket.md). The following example uses the REST API to create the new bucket:  
```console  
curl -X POST http://127.0.0.1:8091/pools/default/buckets \
     -u Administrator:password \
     -d name=travel-sample-1024 \
     -d storageBackend=magma \
     -d numVbuckets=1024 \
     -d ramQuota=1024  
```
2. Recreate any scopes and collections in the new bucket that are in the original bucket. Replication does not recreating missing scopes and collections for you. You can create the scopes and collections manually or reuse any deployment scripts you have. See [Manage Scopes and Collections](../manage-scopes-and-collections/manage-scopes-and-collections.md) for details on creating scopes and collections.  
You can also create a script to recreate the scopes and collections in the new bucket. For example, the following Python script uses the Python SDK to accomplish this task:  
```python  
from couchbase.cluster import Cluster  
from couchbase.options import ClusterOptions  
from couchbase.auth import PasswordAuthenticator  
from couchbase.management.collections import CollectionManager, CollectionSpec  
from couchbase.exceptions import ScopeAlreadyExistsException, CollectionAlreadyExistsException  
# Connect to source and target clusters  
# Here, the target and source are the the same.  
src_cluster = Cluster('couchbase://127.0.0.1', ClusterOptions(PasswordAuthenticator('Administrator', 'password')))  
tgt_cluster = Cluster('couchbase://127.0.0.1', ClusterOptions(PasswordAuthenticator('Administrator', 'password')))  
src_bucket = src_cluster.bucket('travel-sample')  
tgt_bucket = tgt_cluster.bucket('travel-sample-1024')  
src_coll_mgr = src_bucket.collections()  
tgt_coll_mgr = tgt_bucket.collections()  
# Get all scopes and their collections from source  
scopes = src_coll_mgr.get_all_scopes()  
for scope in scopes:  
    scope_name = scope.name  
    if scope_name.startswith('_'):  
        continue # Skip system scopes  
    # Create scope in target  
    try:  
        print(f"Creating scope: {scope_name}")  
        tgt_coll_mgr.create_scope(scope_name)  
    except ScopeAlreadyExistsException:  
        pass  
    except Exception as e:  
        print(f"Error creating scope {scope_name}: {e}")  
        exit(1)  
    # Create collections in target  
    for collection in scope.collections:  
        try:  
            print(f"Creating collection: {collection.name} in scope: {scope_name}")  
            tgt_coll_mgr.create_collection(scope_name, collection.name)  
        except CollectionAlreadyExistsException:  
            pass  
        except Exception as e:  
            print(f"Error creating collection {collection.name} in scope {scope_name}: {e}")  
            exit(1)  
```
3. Add a loopback reference to the cluster. The following example uses the REST API to add an XDCR reference named `self` to the cluster that uses the loopback IP address as the hostname:  
```console  
 curl -X POST http://127.0.0.1:8091/pools/default/remoteClusters -u Administrator:password \
-d username=Administrator \
-d password=password \
-d hostname=127.0.0.1 \
-d name=self \
-d demandEncryption=0 | jq  
```  
The out of previous command is:  
```json  
{  
  "connectivityErrors": null,  
  "deleted": false,  
  "hostname": "127.0.0.1:8091",  
  "name": "self",  
  "network_type": "",  
  "secureType": "none",  
  "uri": "/pools/default/remoteClusters/self",  
  "username": "Administrator",  
  "uuid": "a43e930240738b5aee16e2688a65d08f",  
  "validateURI": "/pools/default/remoteClusters/self?just_validate=1"  
}  
```
4. Create an XDCR replication from the original bucket to the new bucket. The following example uses the REST API to create the replication:  
```console  
curl -v -X POST -u Administrator:password \  
http://127.0.0.1:8091/controller/createReplication \
-d fromBucket=travel-sample \
-d toCluster=self \
-d toBucket=travel-sample-1024 \
-d replicationType=continuous \
-d createTarget=true \
-d enableCompression=1 | jq  
```  
The result of the previous command looks like this:  
```json  
{  
  "id": "a43e930240738b5aee16e2688a65d08f/travel-sample/travel-sample-1024"  
}  
```  
The replication process starts.
5. Monitor the replication process until it completes. You can monitor the replication process [via the Couchbase Server Web Console](../manage-xdcr/create-xdcr-replication.md#monitor-current-replications) or by [calling the REST API](../../rest-api/rest-xdcr-statistics.md). Once the replication has duplicated all of the documents in the original bucket without errors, you can stop and delete it. Then you can drop the original bucket.  
> [!IMPORTANT]  
> Be sure to update all clients to use the new bucket before you stop the replication.