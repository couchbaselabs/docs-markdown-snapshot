---
title: Memory
description: Couchbase Server memory-management ensures high performance and scalability.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/learn/pages/buckets-memory-and-storage/memory.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:learn:buckets-memory-and-storage/memory.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/learn/buckets-memory-and-storage/memory.html)

# Memory

> Couchbase Server memory-management ensures high performance and scalability. 

## [](#service-memory-quotas)Service Memory Quotas

You must configure your memory quota allocations for each service in Couchbase Server, except for the [Query Service](../services-and-indexes/services/query-service.md) and [Backup Service](../services-and-indexes/services/backup-service.md). You can change the availability of memory resources in your cluster based on how you assign your services to each node.

The memory quota you allocate for a service applies to every instance of that service across your cluster. For example, if you allocate 2048 MB to the [Analytics Service](../services-and-indexes/services/analytics-service.md), and you run the Analytics Service on three of a cluster's five nodes, each instance of the service has 2048 MB of memory.

> [!NOTE]
> You can't allocate different amounts of memory for different instances of the same service in a cluster.

Couchbase recommends that you allocate no more than 90% of a node's memory (80% on nodes with a small amount of total memory) to a server and its services.

The firm limits for server memory allocation can be calculated by:

\\(max(total\\\_memory - 1, 80\\% \\times total\\\_memory)\\)

where `total_memory` is the maximum memory on the node in GiB.

The [Data Service](../services-and-indexes/services/data-service.md) must run on at least one node in any cluster. Every [bucket](#buckets.adoc) you create on a node has its own memory quota. The available memory for a bucket comes from the quota you assign to the Data Service. For more information on bucket memory quotas, see the [Bucket Memory Quotas](#bucket-memory) section.

When you add a new node, you can use the same configuration and services from the first node in the cluster. You can also choose to customize the new node's settings and change its assigned services.

For more information about how to add nodes and allocate memory to a service when you initialize a cluster, see [Create a Cluster](../../manage/manage-nodes/create-cluster.md).

The **Memory Quotas** panel in the [General settings screen](../../manage/manage-settings/general-settings.md) of the Couchbase Server Web Console lists all the services running on a cluster. It also shows the memory allocated to each service. You can use the panel to change the memory allocations in your cluster. If a change doesn't meet the required minimum or exceeds the available memory for a cluster, the Memory Quotas panel displays an error.

The following table contains the minimum required memory quotas for each service in Couchbase Server:

| Service   | Minimum Memory Quota (in MB) |
| --------- | ---------------------------- |
| Data      | 256                          |
| Index     | 256                          |
| Search    | 256                          |
| Analytics | 1024                         |
| Eventing  | 256                          |

The Query Service and the Backup Service don't require an administrator-specified memory quota.

## [](#bucket-memory)Bucket Memory Quotas

You must specify a memory quota for each bucket you create. This quota is allocated for the bucket on a per node basis and must be less than the total memory quota for the cluster.

Set the memory quota based on the expected size of your dataset. The memory quota for a bucket must support the minimum memory resident ratio of its [storage engine](storage-engines.md):

* **Couchstore**: The memory quota is recommended to be at least 10% of your expected dataset size.
* **Magma**: The memory quota is recommended to be at least 1% of your expected dataset size.

For example, if you expect to have about 2TBs of data per node in your cluster and want to use the **Magma** engine, you could set the memory quota for a bucket to 20GiB.

> [!NOTE]
> These values are recommendations only. The specific memory quota requirements for your bucket are dependent on access patterns, data density, and other factors.

For more information on how to create a bucket and configure its memory quota, see [Create a Bucket](../../manage/manage-buckets/create-bucket.md).

## [](#initialization-and-warmup)Initialization and Warmup

When Couchbase Server is restarted on a node, the node goes through a _warmup process_ before it restarts the handling of data requests. During this warmup process, data on disk is sequentially reloaded into memory for each bucket. The time required for the reload depends on the size and configuration of the system, the amount of data persisted on the node, and the ejection policy configured for the buckets.

Warmup behavior controls how and when data is loaded from disk into memory after a bucket or node restarts. The `warmupBehavior` setting determines this process:

* **background** (default): The bucket starts serving requests as soon as metadata and some data are loaded into memory, while the rest of the data continues loading in the background. This allows for faster bucket availability and minimal downtime.
* **blocking**: The bucket does not serve any requests until all data is fully loaded into memory. This ensures that all items are available immediately when the bucket becomes active, but can increase startup time.
* **none**: The warmup process is skipped, and the bucket serves only items that are already in memory. Data is loaded on-demand as requests are made for items not yet loaded.

Choosing the appropriate warmup behavior lets you balance between quicker bucket availability and having more data pre-loaded for immediate access after a restart.

On a given Data Service node, a bucket's data is loaded in accordance with determinations made by the _access scanner_.

The access scanner periodically identifies the most frequently used keys and writes them to an access log. During server warmup, Couchbase Server uses this log to prioritize loading the most-accessed documents into memory. By default, the access scanner runs every 24 hours at 10:00 AM GMT, but you can adjust its schedule to minimize performance impact and avoid conflicts with index updates.

It checks the _resident ratio_ — which is the percentage of items in active and replica vBuckets that are currently in memory on the node:

* If the ratio is below 95%, the access scanner generates a new _access log_, which records the documents that have been most frequently accessed during the last 24 hours. If and when data-loading subsequently occurs, the new access log is consulted, the recorded document-keys obtained, and the corresponding documents loaded with the highest priority.
* If the ratio is above 95%, the access scanner does _not_ generate a new access log. Instead, it deletes any existing access log, and exits. If and when data-loading subsequently occurs, since no access log exists, loading occurs with no priority-order (this being, in cases of extremely high resident ratio, the more performative loading procedure).

> [!NOTE]
> The settings `warmup_min_items_threshold`, `warmup_min_memory_threshold`, and enabling access scanner are no longer supported through `cbepctl`. These settings are replaced by a new setting `warmupBehavior` and `accessScannerEnabled`, which can be configured using REST APIs.

### [](#configuring-the-access-scanner)Configuring the Access Scanner

You can configure the access scanner using the REST API. For more information, see [accessScannerEnabled](../../rest-api/rest-bucket-create.md#accessscannerenabled).

> [!NOTE]
> The access scanner is a highly CPU-intensive process.

### [](#configuring-the-warmup-behaviour)Configuring the Warmup Behaviour

You can configure the warmup process using the REST API. For more information, see [warmupBehavior](../../rest-api/rest-bucket-create.md#warmupbehavior).

## [](#ejection)Ejection

If a bucket's memory use gets close to its memory quota, the Data Service may eject data from memory. See [Memory Watermarks](#watermarks) for more information about how Couchbase Server manages memory use. You assign an ejection policy (also known as an eviction method) to each bucket that determines if and how the Data Service ejects data from memory. Couchbase and Ephemeral buckets each have their own ejection policies.

> [!NOTE]
> Capella refers to Couchbase buckets as Memory and Disk buckets, and Ephemeral buckets as Memory Only buckets.

The two ejection policies available for Couchbase buckets are:

Value-only

The Data Service only ejects a document's data when it ejects it from memory. It keeps the document's keys and metadata in memory. Retaining the keys and metadata help limit the performance impact of ejecting the document from memory. This is the default policy for Couchbase buckets. Choose this method if you need better performance, but be aware that it uses more system memory.

Full

The Data Service removes the entire document, including its metadata and keys, when it ejects a document from memory. Choose this method if you want to reduce your memory overhead requirement.

> [!NOTE]
> Use the Full Ejection policy for buckets using the [Magma storage engine](storage-engines.md#storage-engine-magma). This setting works well when the ratio of memory to data is low. In these cases, retaining just the keys and metadata of documents can still consume significant portions of the allocated memory. Magma allows you to set a memory to data ratio as low as 1%.

For more information about Couchbase bucket ejection policies, see the blog post [A Tale of Two Ejection Methods: Value-only vs. Full](https://blog.couchbase.com/a-tale-of-two-ejection-methods-value-only-vs-full/)

The two ejection methods available for Ephemeral buckets are:

No ejection

If the bucket reaches its memory quota, the Data Service does not eject data. Instead, it refuses to load any new data until memory becomes available. Memory can become available when users delete documents or documents expire because of [expiration settings](../data/expiration.md)).

Eject data when RAM is full

If the bucket approaches its memory quota, the Data Service ejects documents to make space for new data. It chooses the documents to eject based on the Not Recently Used (NRU) algorithm. This algorithm uses metadata to determine which documents have not been accessed recently.

> [!IMPORTANT]
> Data ejected from an Ephemeral bucket is lost because it's never persisted to disk.
> 
> Ejecting data from a Couchbase bucket does not remove the data from disk, so it's still available. The only effect is that the next access to the data is slower because the Data Service has to read it from disk instead of from memory.

### [](#changing-ejection-policy)Changing the Ejection Policy of a Couchbase Bucket

You can change the ejection policy of an existing bucket. When you change the ejection policy for an ephemeral bucket, the change takes effect immediately. When you change the ejection policy for a Couchbase bucket, the change does not take effect until you perform one of the following procedures:

* Restart the bucket, which is the default behavior unless you set the `noRestart` parameter to `true` in the REST API call to change the ejection policy.
* If you set the `noRestart` parameter to `true`, you must perform one of the following processes:

  * Swap rebalance each node in the cluster running the Data Service.
  * Perform a graceful failover followed by a delta or full recovery and rebalance of each node running the Data Service.

You may want to change the ejection policy of a bucket if you're changing the storage engine it uses. For example, suppose you're changing a bucket from using the [Couchstore](storage-engines.md#storage-engine-couchstore) to the [Magma](storage-engines.md#storage-engine-magma). Then you should consider changing the ejection policy to Full Ejection, which is better for buckets with low memory to storage ratios. See [Migrate a Bucket's Storage Backend](../../manage/manage-buckets/migrate-bucket.md) for more information about migrating a bucket to a different storage engine.

> [!NOTE]
> If you change the ejection policy while performing a backend storage migration, you must use a full recovery when you recover a node after a graceful failover. The storage migration requires the full recovery to complete its migration. You also cannot allow Couchbase Server to restart the bucket after changing the ejection policy during a migration.

See [Change a Bucket's Ejection Policy](../../manage/manage-buckets/change-ejection-policy.md) for more information about changing a bucket's ejection policy.

### [](#watermarks)Memory Watermarks

For each bucket, Couchbase Server manages available memory using two watermarks: `memoryLowWatermark` and `memoryHighWatermark`. The `memoryHighWatermark` watermark is the threshold where Couchbase Server takes action to prevent the bucket from exceeding its memory allocation. When memory use reaches this watermark, the Data Service ejects items if the bucket's ejection policy allows item ejection. It continues ejecting items until the bucket's memory use drops to the `memoryLowWatermark` watermark. If ejection cannot free enough space, the Data Service stops ingesting data, sends error messages to clients, and displays an insufficient memory notification. When enough memory becomes available, data ingestion resumes.

> [!NOTE]
> The settings `mem_high_wat`, and `mem_low_wat` are no longer supported through `cbepctl`. These settings are replaced by new settings `memoryLowWatermark` and `memoryHighWatermark`, which can be configured using REST APIs.

Couchbase Server selects items for ejection based on metadata that shows whether the item is Not Recently Used (NRU). If an item was not used recently, it becomes a candidate for ejection.

The relationship of `memoryLowWatermark` and `memoryHighWatermark` to the bucket's overall memory quota is illustrated as follows:

![tunableMemory](../_images/buckets-memory-and-storage/tunableMemory.png) 

The default setting for `memoryLowWatermark` is 75%. The default setting for `memoryHighWatermark` is 85%. The default settings can be changed using the REST API. See [set flush\_param](../../cli/cbepctl/set-flush%5Fparam.md) for more information about changing these values.

## [](#expiry-pager)Expiry Pager

Scans for items that have expired, and erases them from memory and disk; after which, a _tombstone_ remains for a default period of 3 days. The expiry pager runs every 10 minutes by default.

> [!NOTE]
> The setting `exp_pager_stime` is no longer supported through `cbepctl`. This setting is replaced by a new setting `expiryPagerSleepTime`, which can be configured using REST APIs.

For information on changing the interval using the REST API, see [expiryPagerSleepTime](../../rest-api/rest-bucket-create.md#expirypagersleeptime).

For more information on item-deletion and tombstones, see [Expiration](../data/expiration.md).

## [](#active-memory-defragmenter)Active Memory Defragmenter

Over time, Couchbase Server-memory can become fragmented. Each page in memory is typically responsible for holding documents of a specific size-range. Over time, if memory pages assigned to a specific size-range become sparsely populated (due to documents of that size being ejected, or to items changing in size), the unused space in those pages cannot be used for documents of other sizes, until a complete page is free, and that page is re-assigned to a new size. Such effects, which are highly workload-dependent, may result in memory that cannot be used efficiently.

Couchbase Server provides an _Active Memory Defragmenter_, which periodically scans the cache, to identify pages that are sparsely used. It then repacks the items on those pages, to free up space.