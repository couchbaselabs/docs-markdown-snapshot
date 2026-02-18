---
title: Sizing Guidelines
description: Evaluate the overall performance and capacity goals that you have
  for Couchbase, and use that information to determine the necessary resources
  that you'll need in your deployment.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/install/pages/sizing-general.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/install/sizing-general.html)

# Sizing Guidelines

> Evaluate the overall performance and capacity goals that you have for Couchbase, and use that information to determine the necessary resources that you’ll need in your deployment. 

The most common and important questions you need to ask when deploying a new Couchbase Server cluster are how many nodes you need, and what size they need to be.

With the increasing number of Couchbase services and the flexibility of the Couchbase Data Platform, the answer to this question can be challenging. This guide aims to help you better size your deployment.

If you want detailed recommendations for your specific deployment, you can contact Couchbase Support.

> [!NOTE]
> The sizing recommendations and calculations discussed in this guide are based on an analysis of performance data and common use-cases.

## [](#general-considerations)General Considerations

The sizing of your Couchbase Server cluster is critical to its overall stability and performance. While there are some [basic system requirements](pre-install.md) to run Couchbase Server, you still need to evaluate the overall performance and capacity requirements for your workload and dataset, and then divide that into the hardware and resources you have available.

Your application wants the majority of reads to come out of the cache, and to have the I/O capacity to handle the writes. There needs to be enough capacity in all areas to support everything the system is doing while maintaining the required level of performance.

### [](#multi-dimensional-scaling)Multi-Dimensional Scaling

Couchbase Services allow you to access and maintain your data. You can deploy, maintain, and provision these services independently of each other. This independent service model allows you to take advantage of Multi-Dimensional Scaling.

Multi-Dimensional Scaling lets you fine-tune your cluster for optimal handling of changing workload-requirements, for each individual Couchbase Service.

Every Service has different demands on hardware resources. Multi-Dimensional Scaling plays an important role when sizing your Couchbase cluster, both pre and post-deployment. For example, core Data Service operations can often benefit from scaling out smaller commodity nodes. Low latency operations with the Query Service might see a greater benefit from scaling up hardware resources on a given node.

For more information about the nature and resource demands of each Couchbase Service, see [Services](../learn/services-and-indexes/services/services.md).

## [](#about-couchbase-server-resources)About Couchbase Server Resources

This guide discusses four types of resources that you should consider when sizing a Couchbase Server cluster node:

CPU

CPU controls the number of cores and the clock speed required to run your workload.

RAM

RAM is often the most crucial area to size. Cached documents provide low-latency reads and consistently high throughput.

Your RAM represents the main memory you allocate to Couchbase Server. Determine your allocation based on the following factors:

* How much free RAM is available beyond your OS and other applications.
* How much data you want to store in main memory.
* How much latency you expect from your Data, Indexing, and Query Service performance.

Some components that require RAM are:

* All index storage types which need sufficient memory quota allocation for proper functioning.
* The Search Service.

__Table 1\. Minimum RAM Quota for Couchbase Server Components__
| Component                                 | Minimum RAM                                          |
| ----------------------------------------- | ---------------------------------------------------- |
| Data Service                              | 256 MB                                               |
| Index Service (Standard Global Secondary) | 256 MB                                               |
| Indexing Service (Memory-Optimized)       | 256 MB minimum, 1024 MB and above recommended        |
| Search Service (Full-Text Search)         | 256 MB minimum; 2048 MB and above recommended        |
| Query Service                             | The Query Service does not require a RAM allocation. |
| Eventing Service                          | 256 MB                                               |
| Analytics Service                         | 1024 MB                                              |

Storage (disk space)

Requirements for your disk subsystem are:

* **Disk size** — Specifies the disk storage space needed to hold your entire dataset.
* **Disk I/O** — Combines your sustained read/write rate, database file compaction, and any other operations that requires disk access.

To better support Couchbase Server, keep in mind the following:

* Disk space continues to grow if fragmentation ratio keeps climbing. To mitigate this, add enough buffer in your disk space to store all of the data. Monitor your cluster’s fragmentation ratio in the Couchbase Server Web Console and trigger compaction processes as needed.
* Couchbase recommends using Solid State Drives (SSD) when possible. An SSD gives much better performance than a Hard Disk Drive (HDD) when it comes to disk throughput and latency.

Network

Enough network bandwidth is vital to the performance of Couchbase Server. A reliable high-speed network for intra-cluster and inter-cluster communications has a huge effect on overall performance and scalability of Couchbase Server.

Most deployments can achieve optimal performance with 1 Gbps interconnects, but some may need 10 Gbps.

## [](#sizing-data-service-nodes)Sizing Data Service Nodes

Data Service nodes handle data service operations, such as create/read/update/delete (CRUD). The following sizing information applies to both the Couchstore and Magma storage engines.

Couchbase recommends reviewing the differences between the available storage engines before attempting to size the Data Service nodes in your cluster. For information, see [Storage Engines](../learn/buckets-memory-and-storage/storage-engines.md).

It’s important to keep use-cases and application workloads in mind since different application workloads have different resource requirements. For example, if your working set needs to be fully in-memory, your cluster might need more RAM. If your application requires only 10% of data in-memory, you need disks with enough space to store all of the data, and that are fast enough for your read/write operations.

### [](#ram-sizing-for-data-service-nodes)RAM Sizing for Data Service Nodes

You can start sizing the Data Service nodes by answering the following questions:

* Is the application primarily using individual document access?
* Do you plan to use XDCR?
* What’s your working set size and what are your data operation throughput and latency requirements?

Answers to the above questions can help you better understand the capacity requirement of your cluster and provide a better estimation for sizing.

The following tables show an example use-case for sizing RAM:

__Table 2\. Input Variables for Sizing RAM__
| Input Variable           | Value        |
| ------------------------ | ------------ |
| documents\_num           | 1,000,000    |
| ID\_size                 | 100 bytes    |
| value\_size              | 10,000 bytes |
| number\_of\_replicas     | 1            |
| working\_set\_percentage | 20%          |

__Table 3\. Constants for Sizing RAM__
| Constants               | Value    |
| ----------------------- | -------- |
| Type of Storage         | SSD      |
| overhead\_percentage    | 25%      |
| metadata\_per\_document | 56 bytes |
| high\_water\_mark       | 85%      |

Based on the provided data, a rough sizing guideline formula would be:

__Table 4\. Guideline Formula for Sizing a Cluster__
| Variable                   | Calculation                                                                          |
| -------------------------- | ------------------------------------------------------------------------------------ |
| no\_of\_copies             | 1 + number\_of\_replicas                                                             |
| total\_metadata            | (documents\_num) \* (metadata\_per\_document + ID\_size) \* (no\_of\_copies)         |
| total\_dataset             | (documents\_num) \* (value\_size) \* (no\_of\_copies)                                |
| working\_set               | total\_dataset \* (working\_set\_percentage)                                         |
| Cluster RAM quota required | (total\_metadata + working\_set) \* (1 + overhead\_percentage) / (high\_water\_mark) |
| Number of nodes            | Cluster RAM quota required / per\_node\_ram\_quota                                   |

Based on the above formula, these are the suggested sizing guidelines:

__Table 5\. Suggested Sizing Guideline__
| Variable                   | Calculation                                                               |
| -------------------------- | ------------------------------------------------------------------------- |
| no\_of\_copies             | \= 1 for original and 1 for replica                                       |
| total\_metadata            | \= 1,000,000 \* (100 + 56) \* (2) = 312,000,000 bytes                     |
| total\_dataset             | \= 1,000,000 \* (10,000) \* (2) = 20,000,000,000 bytes                    |
| working\_set               | \= 20,000,000,000 \* (0.2) = 4,000,000,000 bytes                          |
| Cluster RAM quota required | \= (312,000,000 + 4,000,000,000) \* (1+0.25)/(0.85) = 6,341,176,470 bytes |

This tells you that the RAM requirement for the whole cluster is 7 GB.

> [!NOTE]
> This amount is in addition to the RAM requirements for the operating system and any other software that runs on the cluster nodes.

### [](#disk-sizing-for-data-service-nodes)Disk Sizing for Data Service Nodes

A key concept to remember about Couchbase Server’s data storage is that it’s an append-only system. When an application mutates or deletes a document, the old version of the document is not immediately removed from disk. Instead, Couchbase Server marks them as stale. They remain on disk until a compaction process runs that reclaims the disk space. When sizing disk space for your cluster, you take this behavior into account by applying an append-only multiplier to your data size.

When sizing disk space for the Data Service nodes, you first must determine the following information:

* The total number of documents that you plan to store in the cluster. If this value constantly grows, consider the growth rate into the future when sizing.
* The average size of each document.
* Whether the documents can be compressed, and if they can, what compression ratio Couchbase Server can achieve. Couchbase Server always compresses documents when storing them on disk. See [Compression](../learn/buckets-memory-and-storage/compression.md) for more information about compression in Couchbase Server. Documents containing JSON data or binaries can be compressed. Binary data that’s already compressed (such as compressed images or videos) cannot be compressed further.  
Couchbase Server uses the [Snappy](https://en.wikipedia.org/wiki/Snappy%5F%28compression%29) compression algorithm, which prioritizes speed while still providing reasonable compression. You can estimate the compression ratio Couchbase Server can achieve for your data by compressing a sample set of documents using a snappy-based command line tool such as `snzip`. Otherwise, you can choose to use an estimated compression ratio of 0.7 for JSON documents.
* The number of replicas for your buckets. See [Intra-Cluster Replication](../learn/clusters-and-availability/intra-cluster-replication.md) for more information about replicas.
* The number of documents that you plan to delete each day. This number includes both the number of documents directly deleted by your applications and those that expire due to TTL (time to live) settings. See [Expiration](../learn/data/expiration.md) for more information about document expiration.  
This value is important because in the short term, deletions actually take a bit more disk space rather than less. Because of Couchbase Server’s append-only system, the deleted documents remain on disk until a compaction process runs. Also, Couchbase Server creates a tombstone record for each deleted document. This record consumes a small amount of additional disk space.
* The metadata purge interval you’ll use. This purge process removes tombstones that records the deletion of documents. The default purge interval is 3 days. For more information about the purge interval, see [Metadata Purge Interval](../manage/manage-settings/configure-compact-settings.md#tombstone-purge-interval).
* Which storage engine your cluster will use. The storage engine affects the append-only multiplier that you use when sizing disk space. See [Storage Engines](../learn/buckets-memory-and-storage/storage-engines.md) for more information

To determine the amount of storage you need in your cluster:

1. Calculate the size of the dataset by multiplying the total number of documents by the average document size. If the documents are compressible, also multiply by the estimated compression ratio:  
\\\[S\_{\\mathrm{dataset}} = \\text{# of documents} \\times \\text{avg. document size} \\times \\text{compression ratio}\\\]
2. Calculate the total metadata size by multiplying the total number of documents by 56 bytes (the average metadata size per document):  
\\\[S\_{\\mathrm{metadata}} = \\text{# of documents} \\times 56\\\]
3. Calculate the key storage overhead by multiplying the total number of documents by the average key size.  
\\\[S\_{\\mathrm{keys}} = \\text{# of documents} \\times \\text{avg. key size}\\\]
4. Calculate the tombstone space in bytes using the following formula:  
\\\[\\begin{equation} \\begin{split} S\_{\\mathrm{tombstones}} = & ( \\text{avg. key size} + 60 ) \\times \\text{purge frequency in days} \\\\ & \\times ( \\text{# of replicas} + 1 ) \\times \\text{# documents deleted per day} \\end{split} \\end{equation}\\\]
5. Calculate the total disk space required using the following formula:  
\\\[\\begin{equation} \\begin{split} \\text{total disk space} = & ( ( S\_{\\mathrm{dataset}} \\times (\\text{# replicas} + 1) \\\\ & + S\_{\\mathrm{metadata}} + S\_{\\mathrm{keys}} ) \\times F\_{\\text{append-multiplier}} ) + S\_{\\mathrm{tombstones}} \\end{split} \\end{equation}\\\]  
Where \\(F\_{\\text{append-multiplier}}\\) is the append-only multiplier. This value depends on the storage engine you use:

  * For Couchstore storage engine, use an append-only multiplier of 3.
  * For Magma storage engine, use an append-only multiplier of 2.2.

For example, suppose you’re planning a cluster with the following characteristics:

* Total number of documents: 1,000,000
* The average document size: 10,000 bytes.
* The documents contain JSON data that have an estimated compression ratio of 0.7.
* Average key size: 32 bytes.
* Number of replicas: 1
* Number of documents deleted per day: 5,000
* Purge frequency in days: 3
* Storage engine: Magma

Using the formulas above, you can calculate the total disk space required as follows:

1. Calculate the dataset:  
\\\[S\_{\\mathrm{dataset}} = 1,000,000 \\times 10,000 \\times 0.7 = 7,000,000,000 \\text{bytes}\\\]
2. Calculate the total metadata size:  
\\\[S\_{\\mathrm{metadata}} = 1,000,000 \\times 56 = 56,000,000 \\text{bytes}\\\]
3. Calculate the total key size:  
\\\[S\_{\\mathrm{keys}} = 1,000,000 \\times 32 = 32,000,000 \\text{bytes}\\\]
4. Calculate the tombstone space:  
\\\[S\_{\\mathrm{tombstones}} = (32 + 60) \\times 3 \\times (1 + 1) \\times 5,000 = 2,760,000 \\text{bytes}\\\]
5. Calculate the total disk space:  
\\\[\\begin{equation} \\begin{split} \\text{total disk space} = & ( 7,000,000,000 \\times (1 + 1) \\\\ & + 56,000,000 + 32,000,000 ) \\\\ & \\times 2.2 \\\\ & + 2,760,000 \\\\ & = 30,996,360,000 \\text{bytes} \\end{split} \\end{equation}\\\]

Therefore, for the cluster in this example, you need at least 31 GB of disk space to store your data.

## [](#cpu-overhead)CPU Overhead

When sizing, you must account for raw CPU overhead when using a high number of buckets.

* Your best practice is to allocate 0.2 cores per bucket on each node to maintain operational stability. This overhead does not account for any front-end workloads. You should allocate additional CPU cores for these workloads.
* For more information about monitoring CPU usage and System Limits, see [Monitor](../manage/monitor/monitor-intro.md).

## [](#sizing-index-service-nodes)Sizing Index Service Nodes

To create and maintain secondary indexes and perform index scans for SQL++ queries, you need to size your Index Service nodes.

Similar to the nodes that run the Data Service, answer the following questions to take care of your application needs:

* What is the length of your document keys?
* Which fields need to be indexed?
* Will you be using simple or compound indexes?
* What is the minimum, maximum, or average value size of the indexed fields?
* How many indexes do you need?
* How many documents need to be indexed?
* What is the working set percentage of index required memory?

Answers to these questions can help you better understand the capacity requirement of your cluster, and provide a better estimation for sizing.

**The following is an example use-case for sizing RAM for the Index service:**

Use the following sizing guide to compute the memory requirement for each individual index and to determine the total RAM quota required for the Index Service.

__Table 6\. Input Variables for Sizing RAM__
| Input Variable                                     | Value          |
| -------------------------------------------------- | -------------- |
| num\_entries (Number of index entries)             | 10,000,000     |
| ID\_size (Size of DocumentID)                      | 30 bytes       |
| index\_entry\_size (Size of secondary key)         | 50 bytes       |
| working\_set\_percentage (Nitro, Plasma, ForestDB) | 100%, 20%, 20% |

__Table 7\. Constants for Sizing RAM__
| Constants                                       | Value                                          |
| ----------------------------------------------- | ---------------------------------------------- |
| overhead\_percentage                            | 25%                                            |
| metadata\_back\_index (Nitro, Plasma, ForestDB) | 46, 46, 40 bytes                               |
| metadata\_main\_index (Nitro, Plasma, ForestDB) | 74, 74, 70 bytes                               |
| metadata\_per\_entry (Nitro, Plasma, ForestDB)  | metadata\_back\_index \+ metadata\_main\_index |

Based on the provided data, a rough sizing guideline formula would be:

__Table 8\. Guideline Formula for Sizing a Cluster__
| Variable                                                    | Calculation                                                                   |
| ----------------------------------------------------------- | ----------------------------------------------------------------------------- |
| total\_index\_data(secondary index) (Nitro)                 | (num\_entries) \* (metadata\_per\_entry + ID\_size + index\_entry\_size)      |
| total\_index\_data(secondary index) (Plasma, ForestDB)      | (num\_entries) \* (metadata\_per\_entry + ID\_size + index\_entry\_size) \* 2 |
| total\_index\_data(primary index) (Nitro, Plasma, ForestDB) | (num\_entries) \* (metadata\_main\_index + ID\_size + index\_entry\_size)     |
| index\_memory\_required(100% resident) (memdb)              | total\_index\_data \* (1 + overhead\_percentage)                              |
| index\_memory\_required(20% resident) (Plasma, ForestDB)    | total\_index\_data \* (1 + overhead\_percentage) \* working\_set              |

Based on the above formula, these are the suggested sizing guidelines:

__Table 9\. Suggested Sizing Guideline__
| Variable                                         | Calculation                                           |
| ------------------------------------------------ | ----------------------------------------------------- |
| total\_index\_data(secondary index) (Nitro)      | (10000000) \* (120 + 30 + 50) = 2000000000 bytes      |
| total\_index\_data(secondary index) (Plasma)     | (10000000) \* (120 + 30 + 50) \* 2 = 4000000000 bytes |
| total\_index\_data(secondary index) (ForestDB)   | (10000000) \* (80 + 30 + 50) \* 2 = 3200000000 bytes  |
| index\_memory\_required(100% resident) (Nitro)   | (2000000000) \* (1 + 0.25) = 2500000000 bytes         |
| index\_memory\_required(20% resident) (Plasma)   | (2000000000) \* (1 + 0.25) \* 0.2 = 1000000000 bytes  |
| index\_memory\_required(20% resident) (ForestDB) | (3200000000) \* (1 + 0.25) \* 0.2 = 800000000 bytes   |

The previous example shows the memory requirement of a secondary index with 10M index entries, each with a 50 bytes secondary key and a 30 bytes DocumentID. The memory usage requirements are 2.5 GB (Nitro, 100% resident), 1 GB (plasma, 20% resident), 800 MB (ForestDB, 20% resident).

> [!NOTE]
> The storage engine used in the sizing calculation corresponds to the storage mode chosen for Index Service as explained in the table below.

__Table 10\. Storage engine and storage mode__
| Storage Engine                        | Storage Mode |
| ------------------------------------- | ------------ |
| Standard GSI (Community Edition)      | ForestDB     |
| Standard GSI(Enterprise Edition)      | Plasma       |
| Memory-Optimized (Enterprise Edition) | Nitro        |

## [](#sizing-query-service-nodes)Sizing Query Service Nodes

A node that runs the Query Service executes queries for your application needs.

Since the Query Service does not need to persist data to disk, there are minimal resource requirements for disk space and disk I/O. You only need to consider CPU and memory.

Answer the following questions to help size the Query Service nodes on your cluster:

* What types of queries do you need to run?
* Do you need to run `stale=ok` or `stale=false` queries?
* Are the queries simple or complex? For example, do you need to use JOINs?
* What are the throughput and latency requirements for your queries?

Different queries have different resource requirements. A simple query might return results within milliseconds while a complex query may require several seconds.

The formula used to calculate the number of queries that’s processed simultaneously is `CPU_cores * 4`. The formula used to calculate the maximum queue-length for queries is `CPU_cores * 256`. If you reach either limit, the system rejects additional queries with a 503 error.

## [](#sizing-analytics-service-nodes)Sizing Analytics Service Nodes

The Analytics engine is a full-fledged parallel query processor that supports parallel joins, aggregations, and sorting for JSON data.

The Analytics Service is dependent on the Data Service and requires the Data service to be running on at least one of the cluster nodes.

### [](#data-space)Data space

* Make sure that the data space for your Analytics Service nodes takes into account metadata replicas. The Analytics Service only replicates the metadata and not the actual data. There’s a small overhead for metadata replicas as metadata is generally small.
* When evaluating a query, the Analytics engine uses temporary disk space. The type of query you want to run determines the required amount of temporary disk space.  
For example, queries with heavy JOINs, aggregates, windowing, or additional predicates require more temporary disk space. Typically, the temporary disk space can be 2x the data space.
* The percent of data shadowed, which is dependent on your use case.
* When you load data from the Data Service into the Analytics Service, you can apply a filter to reduce both the loaded data size and the Analytics Service storage requirements proportionally.

### [](#disk-types-and-partitioning)Disk Types and Partitioning

During query execution, the Analytics query engine concurrently reads and processes data from all partitions. The Input/Output Operations per Second (IOPS) of the physical disk that hosts the data partitions plays a major role in determining the query execution time. Modern storage devices such as SSDs have much higher IOPS and can deal better with concurrent reads than HDDs. A single data partition underutilizes high IOPS devices.

To simplify setup for nodes with a single modern storage device, the Analytics Service creates multiple data partitions on the same storage device. It does this only when you specify a single Analytics disk path during node initialization. The Analytics Service determines the number of partitions using the following formula:

* `Maximum partitions to create = Min((Analytics Memory in MB / 1024), 16)`
* `Actual created partitions = Min(node virtual cores, Maximum partitions to create)`

For example, if a node has 8 virtual cores and the Analytics Service has at least 8 GB of memory, the system creates 8 data partitions on that node. Similarly, for a node with 32 virtual cores and 16 GB memory, the system creates 16 partitions, the maximum for automatic partitioning.

### [](#index-considerations)Index Considerations

The size of a secondary index is around the total size of indexed fields in the Analytics collection. For example, if a collection has 20 fields and only 1 of those fields appears in the secondary index, the secondary index size is \~1/20 of the collection size.

## [](#sizing-eventing-service-nodes)Sizing Eventing Service Nodes

Eventing is a compute-oriented service. By default, the Eventing Service has 1 worker and each worker has 2 threads of execution. You can scale the Eventing Service both vertically by adding more workers or horizontally by adding more nodes. The Eventing Service partitions the vBuckets across the number of available nodes.

### [](#cpu)CPU

Eventing runs arbitrary JavaScript code. This flexibility makes it difficult to define a precise sizing formula. You cannot define a precise formula unless you know the function designs, their KV operations, query operations, cURL operations, and the expected mutation rate.

For example, if you process 100K mutations per second and only match 1 out of 1000 patterns, then perform some intense computation on the matched 100 items in your Eventing Function, you need 100X less compute than if you performed the intense computation on each mutation.

Eventing also can perform I/O to external REST endpoints through a synchronous HTTP/S cURL call. Eventing typically blocks on I/O and requires little CPU. Achieving high throughput to overcome bandwidth requires additional workers and cores.

Use 8 vCPUs or 4 physical cores to run Eventing Functions.

### [](#ram)RAM

For more information about how to size your Eventing memory quota, see [Eventing Service Memory Quota](../eventing/eventing-memory-quota.md).

### [](#eventing-storage-collection-previously-metadata-bucket)Eventing Storage Collection (previously Metadata Bucket)

Each Eventing function stores fewer than 2048 documents in its Eventing storage collection. If timers are not used or if the active timers count does not exceed the per-function document limit, store the Eventing storage collection in a 100 MB bucket.

Using timers requires additional storage for each active timer. Each active timer requires 800 bytes, plus the size of the passed context, which represents the state supplied to the function at future execution.

A 200-byte context results in 1 KB of storage per active timer. 100,000 active timers require 100 MB of additional bucket space.

As a best practice, keep this collection fully resident in-memory to make sure you have constant availability.

> [!NOTE]
> All Eventing functions use this collection.

## [](#sizing-backup-service-nodes)Sizing Backup Service Nodes

The hardware requirements for running a backup cluster are as follows:

__Table 11\. Hardware requirements__
|        | Minimum     | Recommended  |
| ------ | ----------- | ------------ |
| CPUs   | 4 CPU cores | 16 CPU cores |
| Memory | 8 GiB       | 16 GiB       |

## [](#sizing-for-replication-xdcr)Sizing for Replication (XDCR)

Before setting up a replication, you must make sure your cluster is appropriately configured and provisioned.

Your cluster must be properly sized to be able to handle new XDCR streams.

For example, XDCR needs 1-2 additional CPU cores per stream. In some cases, it also requires additional RAM and network resources. If a cluster is not sized to handle both the existing workload and the new XDCR streams, the performance of both XDCR and the cluster overall might be negatively impacted.

For information about preparing your cluster for replication, see [Prepare for XDCR](../manage/manage-xdcr/prepare-for-xdcr.md).