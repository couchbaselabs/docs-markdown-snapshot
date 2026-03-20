---
title: Change a Bucket&#8217;s Ejection Policy
description: You can change the ejection method of a bucket using the Couchbase
  Server Web Console or the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/manage/pages/manage-buckets/change-ejection-policy.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:manage:manage-buckets/change-ejection-policy.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/manage/manage-buckets/change-ejection-policy.html)

# Change a Bucket&#8217;s Ejection Policy

> You can change the ejection method of a bucket using the Couchbase Server Web Console or the REST API. The bucket’s ejection policy (also known as its eviction method) controls how Couchbase Server removes documents from memory as the bucket approaches its memory quota. See [Ejection](../../learn/buckets-memory-and-storage/memory.md#ejection) for more information about ejection policies. 

You initially set the ejection policy when you create a Couchbase bucket. However, you can change the ejection policy of an existing bucket.

You may want to change the ejection policy of a Couchbase bucket when migrating its [storage engine](../../learn/buckets-memory-and-storage/storage-engines.md). For example, when migrating a bucket from Couchstore to Magma, you should consider changing the bucket’s ejection policy to Full Ejection. This policy works well for Magma buckets that have a low memory to storage ratio. You can change both the storage backend and the ejection policy at the same time. See [Migrate a Bucket’s Storage Backend](migrate-bucket.md) for steps to perform both operations.

## [](#change-the-ejection-policy-using-the-couchbase-server-web-console)Change the Ejection Policy Using the Couchbase Server Web Console

You can edit a bucket’s ejection policy using the Couchbase Server Web Console.

> [!IMPORTANT]
> When you change the ejection policy of a Couchbase bucket using the Couchbase Server Web Console, Couchbase Server automatically restarts the bucket. Restarting the bucket closes all open connections and results in some downtime. Do not change the ejection policy of a bucket in production unless you’re prepared this downtime. You can also change the ejection policy using REST API which lets you avoid downtime. See [Change Couchbase Bucket Ejection Policy Using the REST API](#rest-api) for more details.
> 
> Changing the ejection policy of an ephemeral bucket does not require a bucket restart or other additional steps. The new setting takes effect immediately.

To change the ejection policy of a bucket, follow these steps:

1. In the Web Console, click **Buckets**. The **Buckets** page opens, listing all of the buckets in the cluster.  
![bucketsViewInitialEdit](../_images/manage-buckets/bucketsViewInitialEdit.png)
2. Click the row containing the bucket that you want to edit to expand it.  
![bucketsViewWithExpandedBucketRow](../_images/manage-buckets/bucketsViewWithExpandedBucketRow.png)
3. Click **Edit** to edit the bucket’s settings.  
![bucket edit dialog initial](../_images/manage-buckets/bucket-edit-dialog-initial.png)
4. Click **Advanced bucket settings** to expand the section containing the ejection policy setting.  
![bucket edit dialog expanded](../_images/manage-buckets/bucket-edit-dialog-expanded.png)
5. Change the **Ejection Method** setting the new value you want. The available settings depend on the bucket’s type:  
Couchbase buckets

  * **Value-only**: Couchbase Server removes a document’s data, but keeps its keys and metadata in memory. Keeping these values in memory helps lessen the performance overhead of removing the document from memory.
  * **Full**: Couchbase Server removes the entire document from memory.  
Ephemeral buckets

  * **No ejection**: If the bucket reaches its memory quota, the Data Service does not eject data. Instead, it refuses to load any new data until memory becomes available.
  * **Eject data when RAM is full**: If the bucket approaches its memory quota, the Data Service ejects the least-recently used documents to make space for new data.  
If you change the setting of a Couchbase bucket, the Couchbase Server Web Console warns you of the consequences of changing the ejection policy.
6. Click **Save** to save the changes. If you changed the ejection policy of a Couchbase bucket, Couchbase Server restarts the bucket to apply the new ejection policy. If you changed the ejection policy of an ephemeral bucket, the new setting takes effect immediately.

## [](#ephemeral-rest-api)Change Ephemeral Bucket Ejection Policy Using the REST API

You can change the ejection policy for an ephemeral bucket by sending a POST request to the `/pools/default/buckets/{BUCKETNAME}` endpoint to change the `evictionPolicy` setting. Unlike changing a Couchbase bucket’s ejection policy, changing the ejection policy of an ephemeral bucket does not require a bucket restart or other additional steps. The new setting takes effect immediately.

The following steps demonstrate how to change the ejection policy of an ephemeral bucket named `sample-ephemeral` to `nruEviction` using the REST API.

1. View the current ejection policy of the bucket by sending a GET request to the `/pools/default/buckets/{BUCKETNAME}` endpoint. The following command calls the REST API to get the configuration of the `sample-ephemeral` bucket. It filters the result through the `jq` command to show just the `evictionPolicy` value:  
```console  
curl -s GET -u Administrator:password \  
     http://localhost:8091/pools/default/buckets/sample-ephemeral \
     | jq '{ (.name): .evictionPolicy }'  
```  
The output of the previous command shows that the `evictionPolicy` of the `sample-ephemeral` bucket is set to `noEviction`:  
```json  
{  
  "sample-ephemeral": "noEviction"  
}  
```
2. Send a POST request to the `/pools/default/buckets/{BUCKETNAME}` endpoint to change the `evictionPolicy` setting to the new ejection policy that you want. The following command changes the ejection policy of the `sample-ephemeral` bucket to `nruEviction`:  
```console  
curl -s -X POST http://localhost:8091/pools/default/buckets/sample-ephemeral \
     -u Administrator:password \
     -d evictionPolicy="nruEviction"  
```  
The call to the REST API returns no output if it succeeds.
3. Verify that the ejection policy has changed by sending another GET request to `/pools/default/buckets/{BUCKETNAME}` as shown in step 1\. The output shows the new `evictionPolicy` value:  
```json  
{  
  "sample-ephemeral": "nruEviction"  
}  
```

See [Creating and Editing Buckets](../../rest-api/rest-bucket-create.md) for more information about changing a bucket’s settings.

## [](#rest-api)Change Couchbase Bucket Ejection Policy Using the REST API

You can change the ejection policy for a Couchbase bucket using the REST API. You change the ejection policy by sending a POST request to the `/pools/default/buckets/{BUCKETNAME}` endpoint to change the `evictionPolicy` setting.

Unlike the Couchbase Server Web Console, using the REST API to change a Couchbase bucket’s ejection policy lets you prevent the downtime caused by restarting a Couchbase bucket. When you call the REST API to change the ejection policy, can set the `noRestart` parameter to `true` to prevent Couchbase Server from restarting the bucket after you make the change. If you do not allow Couchbase Server to restart the Couchbase bucket, you must take additional steps to apply the change.

If you do not set the `noRestart` parameter or set it to `false` for a Couchbase bucket, Couchbase Server may automatically restart the bucket after you change the ejection policy. Couchbase Server only automatically restarts the bucket if you’re not changing the ejection policy during a backend storage migration. If you’re changing the ejection policy during a backend storage migration, you must set `noRestart` to `true` to prevent Couchbase Server from restarting the bucket. See [Change Ejection Policy During a Backend Storage Migration](#change-during-migration) for an explanation.

> [!NOTE]
> The `noRestart` parameter has no effect when changing the ejection policy of an ephemeral bucket. Changing the ejection policy of an ephemeral bucket takes effect without a bucket restart or other additional steps. See [Change Ephemeral Bucket Ejection Policy Using the REST API](#ephemeral-rest-api) for more details.

How you apply the ejection policy change for a Couchbase bucket depends on whether you’re changing the ejection policy during a backend storage migration.

### [](#change-during-migration)Change Ejection Policy During a Backend Storage Migration

You can change the ejection policy of a Couchbase bucket while you’re migrating the storage engine it uses. You often want to change the ejection policy during migration because the Couchstore and Magma storage engines work best with different ejection policies. See [Storage Engines](../../learn/buckets-memory-and-storage/storage-engines.md) for information about storage engines and [Migrate a Bucket’s Storage Backend](migrate-bucket.md) for information about migrating a bucket’s storage backend.

If you choose to change the ejection policy while migrating the storage backend, you must set `noRestart` to `true`. This setting prevents Couchbase Server from restarting the bucket after changing the policy. If you set this option to `false` or do not include it from your REST API call, Couchbase Server does not change the ejection policy.

After you change the ejection policy while migrating the storage backend, the policy does not take effect until you complete the migration. You complete the migration by performing 1 of the following procedures:

* a [swap rebalance](../../install/upgrade-procedure-selection.md#swap-rebalance) on all nodes in the cluster running the data service.
* a [graceful failover](../../learn/clusters-and-availability/graceful-failover.md) followed by a [full recovery](../../learn/clusters-and-availability/recovery.md#full-recovery) and [rebalance](../../learn/clusters-and-availability/rebalance.md) for all nodes running the data service in the cluster.

See [Migrate a Bucket’s Storage Backend](migrate-bucket.md) for information about migrating a bucket’s storage backend and complete steps to change the ejection policy while performing a migration.

### [](#standalone-ejection-policy-change)Standalone Ejection Policy Change

You can change a Couchbase bucket’s ejection policy when you’re not migrating its storage backend using the REST API. In this case, you can choose whether to have Couchbase Server restart the bucket after you change the ejection policy. You control this behavior using the `noRestart` parameter in the REST API POST method to `/pools/default/buckets/{BUCKETNAME}`:

* To trigger the automatic bucket restart, set the `noRestart` parameter to `false` or do not supply it in the REST API call. Couchbase Server automatically restart the bucket once the REST API call completes. Restarting the bucket is disruptive—​it closes all open connections and results in some downtime. Do not change the ejection policy of a bucket in production unless you’re prepared this downtime.
* To prevent the automatic bucket restart, set the `noRestart` parameter to `true`. The new ejection setting does not take effect until you perform one of the following procedures:

  * a [swap rebalance](../../install/upgrade-procedure-selection.md#swap-rebalance) on all nodes in the cluster running the data service.
  * the following steps for all nodes running the data service in the cluster:

    1. A [graceful failover](../../learn/clusters-and-availability/graceful-failover.md)
    2. A [delta recovery](../../learn/clusters-and-availability/recovery.md#delta-recovery) or a [full recovery](../../learn/clusters-and-availability/recovery.md#full-recovery)
    3. A [rebalance](../../learn/clusters-and-availability/rebalance.md)

The following procedure shows you how to change the ejection policy of a bucket using the REST API. It then demonstrates performing a graceful failover followed by a delta recovery and rebalance to apply the change.

1. Send a POST request to the `/pools/default/buckets/{BUCKETNAME}` REST API endpoint to edit the bucket, and change the `evictionPolicy` parameter to the new ejection policy that you want. Also set the `noRestart` parameter to `true` to prevent Couchbase Server from restarting the bucket.  
The following command changes the ejection policy of the `travel-sample` bucket to Full Ejection without restarting the bucket:  
```console  
curl -v -X POST http://localhost:8091/pools/default/buckets/travel-sample \
     -u Administrator:password \
     -d evictionPolicy="fullEviction" \
     -d noRestart=true  
```
2. At this point, the bucket’s ejection policy has changed at the bucket level. However, each node has an override setting that has them use the old ejection policy.  
You can compare the bucket and node settings to see which nodes have an override by sending a GET request to the `/pools/default/buckets/{BUCKETNAME}` REST API endpoint. The following command calls the REST API to get the configuration of the `travel-sample` bucket. It filters the result through the `jq` command to show just the `evictionPolicy` values from the bucket level and the individual nodes:  
```console  
curl -s GET -u Administrator:password \  
    http://localhost:8091/pools/default/buckets/travel-sample \
    | jq '[ .nodes[] | { (.hostname): .evictionPolicy }] + [{ (.name): .evictionPolicy }]'  
```  
The output of the previous command shows that the bucket’s `evictionPolicy` parameter has changed to `fullEviction`, but the nodes are still using the old `valueOnly` ejection policy:  
```json  
[  
  {  
    "node3.:8091": "valueOnly"  
  },  
  {  
    "node2.:8091": "valueOnly"  
  },  
  {  
    "node1.:8091": "valueOnly"  
  },  
  {  
    "travel-sample": "fullEviction"  
  }  
]  
```
3. Send a POST request to the `/controller/startGracefulFailover` REST API endpoint to perform a graceful failover on 1 of the nodes running the data service. See [Performing Graceful Failover](../../rest-api/rest-failover-graceful.md) for more information about performing a graceful failover.  
The following calls the REST API to perform a graceful failover on a node named `node3`:  
```console  
curl -X POST -u Administrator:password \  
     http://localhost:8091/controller/startGracefulFailover \
     -d 'otpNode=ns_1@node3.'  
```
4. Wait until the failover completes. Then send a POST request to the `/controller/setRecoveryType` REST API endpoint to set the type of recovery for the node to `delta`. See [Setting Recovery Type](../../rest-api/rest-node-recovery-incremental.md) for more information about setting the recovery type.  
The following calls the REST API to set the recovery type for `node3` to `delta`:  
```console  
curl -X POST -u Administrator:password \  
    http://localhost:8091/controller/setRecoveryType \
    -d 'otpNode=ns_1@node3.' \
    -d 'recoveryType=delta'  
```
5. When the recovery completes, send a POST request to the `/controller/rebalance` REST API endpoint to rebalance the cluster. See [Rebalancing the Cluster](../../rest-api/rest-cluster-rebalance.md) for more information about rebalancing a cluster.  
The following calls the REST API to rebalance a three-node cluster containing the nodes named `node1`, `node2`, and `node3`:  
```console  
curl -X POST -u Administrator:password  \  
    http://localhost:8091/controller/rebalance \
    -d 'knownNodes=ns_1@node1.,ns_1@node2.,ns_1@node3.'  
```
6. After the rebalance completes, repeat steps 3 through 5 for the rest of the data nodes in the cluster.  
You can verify which nodes still need to have the change applied to them by sending another GET request to `/pools/default/buckets/{BUCKETNAME}` as shown in step 2\. For example, suppose you have performed a graceful failover, full recovery, and rebalance steps on nodes `node3` and `node2`. Then the output of the command from step 2 shows that the `evictionPolicy` for `node1` is still set to `valueOnly`:  
```json  
[  
  {  
    "node3.:8091": null  
  },  
  {  
    "node2.:8091": null  
  },  
  {  
    "node1.:8091": "valueOnly"  
  },  
  {  
    "travel-sample": "fullEviction"  
  }  
]  
```