---
title: Sizing Guidelines
description: Evaluate the overall performance and capacity goals that you have
  for Couchbase, and use that information to determine the necessary resources
  that you'll need in your deployment.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/install/pages/sizing-general.adoc
  xref: xref:7.6@server:install:sizing-general.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/install/sizing-general.html)

# Sizing Guidelines

> Evaluate the overall performance and capacity goals that you have for Couchbase, and use that information to determine the necessary resources that you'll need in your deployment. 

When you plan to deploy a Couchbase Server cluster, perhaps the most common (and important) question that comes up is: how many nodes do I need and what size do they need to be?

With the increasing number of Couchbase services and the flexibility of the Couchbase Data Platform, the answer to this question can be challenging. This guide aims to help you better size your deployment.

If you want detailed recommendations for your specific deployment, you can contact Couchbase Support.

> [!NOTE]
> The sizing recommendations and calculations discussed in this guide are based on an analysis of performance data and common use-cases.

## [](#general-considerations)General Considerations

The sizing of your Couchbase Server cluster is critical to its overall stability and performance. While there are some [basic system requirements](pre-install.md) to run Couchbase Server, you still need to evaluate the overall performance and capacity requirements for your workload and dataset, and then divide that into the hardware and resources you have available.

Your application wants the majority of reads to come out of the cache, and to have the I/O capacity to handle the writes. There needs to be enough capacity in all areas to support everything the system is doing while maintaining the required level of performance.

### [](#multi-dimensional-scaling)Multi-Dimensional Scaling

Couchbase Services are what allow you to access and maintain your data. These services can be deployed, maintained, and provisioned independently of one another. This independent service model allows you to take advantage of _Multi-Dimensional Scaling_, whereby a cluster can be fine-tuned for optimal handling of emergent workload-requirements, on a service-by-service basis.

Since each service has different demands on hardware resources, Multi-Dimensional Scaling plays an important role when sizing your Couchbase cluster, both pre and post-deployment. For example, core Data Service operations can often benefit greatly from the _scale out_ of smaller commodity nodes, whereas low latency operations with the Query Service may see a greater benefit from the _scale up_ of hardware resources on a given node.

For more information about the nature and resource demands of each Couchbase Service, refer to [Services](../learn/services-and-indexes/services/services.md).

## [](#about-couchbase-server-resources)About Couchbase Server Resources

This guide discusses four types of resources that you should consider when sizing a Couchbase Server cluster node:

CPU

CPU refers to the number of cores and clock speed that are required to run your workload.

RAM

RAM is frequently one of the most crucial areas to size correctly. Cached documents allow the reads to be served at very low latency and consistently high throughput.

This resource represents the main memory that you allocate to Couchbase Server and should be determined by the following factors:

* How much free RAM is available beyond OS and other applications
* How much data do you want to store in main memory
* How much latency you expect from KV/indexing/query performance

Some components that require RAM are:

* All index storage types which need sufficient memory quota allocation for proper functioning.
* Full Text Search (FTS)

__Table 1\. Minimum RAM Quota for Couchbase Server Components__
| Component                                 | Minimum RAM                                     |
| ----------------------------------------- | ----------------------------------------------- |
| Data Service                              | 256 MB                                          |
| Index Service (Standard Global Secondary) | 256 MB                                          |
| Indexing Service (Memory-Optimized)       | 256 MB minimum, 1024 MB and above recommended   |
| Search Service (Full-Text Search)         | 256 MB minimum; 2048 MB and above recommended   |
| Query Service                             | No RAM-allocation is required for this service. |
| Eventing Service                          | 256 MB                                          |
| Analytics Service                         | 1024 MB                                         |

Storage (disk space)

Requirements for your disk subsystem are:

* _Disk size_ — which refers to the amount of the disk storage space that is needed to hold your entire data set.
* _Disk I/O_ — which is a combination of your sustained read/write rate, the need for compacting the database files, and anything else that requires disk access.

To better support Couchbase Server, keep in mind the following:

* Disk space continues to grow if fragmentation ratio keeps climbing. To mitigate this, add enough buffer in your disk space to store all of the data. Also, keep an eye on the fragmentation ratio in the Couchbase user interfaces and trigger compaction processes when needed.
* Solid State Drives (SSDs) are desired, but not required. An SSD will give much better performance than a Hard Disk Drive (HDD) when it comes to disk throughput and latency.

Network

Enough network bandwidth is vital to the performance of Couchbase Server. A reliable high-speed network for intra-cluster and inter-cluster communications has a huge effect on overall performance and scalability of Couchbase Server.

Most deployments can achieve optimal performance with 1 Gbps interconnects, but some may need 10 Gbps.

## [](#sizing-data-service-nodes)Sizing Data Service Nodes

Data Service nodes handle data service operations, such as create/read/update/delete (CRUD). The sizing information provided below applies both to the _Couchstore_ and _Magma_ storage engines: however, the _differences_ between these storage engines should also be reviewed, before sizing is attempted. For information, see [Storage Engines](../learn/buckets-memory-and-storage/storage-engines.md).

It's important to keep use-cases and application workloads in mind since different application workloads have different resource requirements. For example, if your working set needs to be fully in memory, you might need large RAM size. On the other hand, if your application requires only 10% of data in memory, you will need disks with enough space to store all of the data, and that are fast enough for your read/write operations.

You can start sizing the Data Service nodes by answering the following questions:

1. Is the application primarily (or even exclusively) using individual document access?
2. Do you plan to use XDCR?
3. What's your working set size and what are your data operation throughput and latency requirements?

Answers to the above questions can help you better understand the capacity requirement of your cluster and provide a better estimation for sizing.

**The following is an example use-case for sizing RAM:**

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

This tells you that the RAM requirement for the whole cluster is 7 GB. Note that this amount is in addition to the RAM requirements for the operating system and any other software that runs on the cluster nodes.

## [](#cpu-overhead)CPU Overhead

When sizing, you must account for raw CPU overhead when using a high number of buckets.

* Your best practice is to allocate 0.4 cores per bucket on each node to maintain operational stability. This overhead does not account for any front-end workloads. You should allocate additional CPU cores for these workloads.
* [Monitoring](../manage/monitor/monitor-intro.md) is recommended for CPU usage and System Limits

## [](#sizing-index-service-nodes)Sizing Index Service Nodes

A node running the Index Service must be sized properly to create and maintain secondary indexes and to perform index scan for SQL++ queries.

Similar to the nodes that run the Data Service, answer the following questions to take care of your application needs:

1. What is the length of the document key?
2. Which fields need to be indexed?
3. Will you be using simple or compound indexes?
4. What is the minimum, maximum, or average value size of the index field?
5. How many indexes do you need?
6. How many documents need to be indexed?
7. What is the working set percentage of index required in memory?

Answers to these questions can help you better understand the capacity requirement of your cluster, and provide a better estimation for sizing.

**The following is an example use-case for sizing RAM for the Index service:**

The following sizing guide can be used to compute the memory requirement for each individual index and can be used to determine the total RAM quota required for the Index service.

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

The above example shows the memory requirement of a secondary index with 10M index entries, each with 50 bytes size of secondary key and 30 bytes size of documentID. The memory usage requirements are 2.5GB(Nitro, 100% resident), 1GB(plasma, 20% resident), 800MB(Forestdb, 20% resident).

Note that the storage engine used in the sizing calculation corresponds to the storage mode chosen for Index Service in the following way:

__Table 10\. Storage engine and storage mode__
| Storage Engine                        | Storage Mode |
| ------------------------------------- | ------------ |
| Standard GSI (Community Edition)      | ForestDB     |
| Standard GSI(Enterprise Edition)      | Plasma       |
| Memory-Optimized (Enterprise Edition) | Nitro        |

## [](#sizing-query-service-nodes)Sizing Query Service Nodes

A node that runs the Query Service executes queries for your application needs.

Since the Query Service doesn't need to persist data to disk, there are very minimal resource requirements for disk space and disk I/O. You only need to consider CPU and memory.

There are a few questions that will help size the cluster:

1. What types of queries do you need to run?
2. Do you need to run `stale=ok` or `stale=false` queries?
3. Are the queries simple or complex (requiring JOINs, for example)?
4. What are the throughput and latency requirements for your queries?

Different queries have different resource requirements. A simple query might return results within milliseconds while a complex query may require several seconds.

The number of queries that may be processed simultaneously may be approximated with the formula _CPU\_cores \* 4_. The maximum queue-length for queries may be approximated with the formula _CPU\_cores \* 256_. If either limit is reached, additional queries are rejected with a `503` error.

## [](#sizing-analytics-service-nodes)Sizing Analytics Service Nodes

The Analytics engine is a full-fledged parallel query processor that supports parallel joins, aggregations, and sorting for JSON data.

The Analytics Service is dependent on the Data Service and requires the Data service to be running on at least one of the cluster nodes.

### [](#data-space)Data space

* Ensure that the data space for Analytics node takes into account metadata replicas. The Analytics Service currently only replicates metadata and not the actual data. There is a small overhead for metadata replicas as metadata is usually small.
* When evaluating a query, the Analytics engine uses temporary disk space. The type of query being executed can impact the amount of temporary disk space required. For example, a query with heavy JOINs, aggregates, windowing, or more predicates will require more temporary disk space. Typically, the temporary disk space can be 2x the data space.
* The percent of data shadowed, which is dependent on your use case.
* When ingesting data from the the Data Service into the Analytics Service a filter can be provided that reduces the size of the data that is ingested and also the storage size for the Analytics Service proportionally.

### [](#disk-types-and-partioning)Disk types and partioning

During query execution, Analytics's query engine attempts to concurrently read and process data from all data partitions. Because of that, the Input/Output Operations per Second (IOPS) of the actual physical disk in which each data partition resides plays a major role in determining the query execution time. Modern storage devices such as SSDs have much higher IOPS and can deal better with concurrent reads than HDDs. Therefore, having a single data partition on devices with high IOPS will not fully utilize their capabilities.

To simplify the setup of the typical case of a node having a single modern storage device, the Analytics service automatically creates multiple data partitions within the same storage device if and only if a single "Analytics Disk Path" is specified during the node initialization. The number of automatically created data partitions is based on this formula:

* `Maximum partitions to create = Min((Analytics Memory in MB / 1024), 16)`
* `Actual created partitions = Min(node virtual cores, Maximum partitions to create)`

For example, if a node has 8 virtual cores and the Analytics service was configured with memory >= 8GB, 8 data partitions will be created on that node. Similarly, if a node has 32 virtual cores and was configured with memory >= 16GB, only 16 partitions will be created as 16 is the upper bound for automatic partitioning.

### [](#index-considerations)Index considerations

The size of a secondary index is approximately the total size of indexed fields in the Analytics collection. For example, if a collection has 20 fields and only 1 of those fields appears in the secondary index, the secondary index size will be \~1/20 of the collection size.

## [](#sizing-eventing-service-nodes)Sizing Eventing Service Nodes

Eventing is a compute oriented service. By default, Eventing service has one worker and each worker has two threads of execution. You can scale eventing both vertically by adding more workers or horizontally by adding more nodes. The Eventing service will partition vBuckets across the number of available nodes.

### [](#cpu)CPU

Because Eventing allows arbitrary code, JavaScript, to be written and run, it is difficult to come up with a perfect sizing formula unless all Functions have been designed and their KV ops, Query ops, and cURLops are known along with the expected mutation rate.

For example, if you process 100K mutations per second and only match 1 out of 1000 patterns, then perform some intense computation on the matched 100 items in your Eventing Function, you need 100X less compute than if you performed the intense computation on each mutation.

Eventing also can perform I/O to external REST endpoints via a synchronous HTTP/S cURL call. In this case, Eventing typically blocks on I/O and doesn't need much CPU. However. if you want high throughput to overcome bandwidth, you will need more workers and thus more cores.

8 vCPUs or 4 physical cores should be considered a good start for running a few Eventing Functions.

### [](#ram)RAM

In general, the Eventing memory quota of 256 MB is sufficient for almost all workloads.

When scaling up vertically by adding more workers (in the handler's settings), you may see a stall in processing when the number exceeds 48 workers. In this case, raising the memory quota to 384 MB or even 512 would be justified. Do not add memory to the Eventing Service's memory quota without a justified need as it can create resource issues.

### [](#eventing-storage-collection-previously-metadata-bucket)Eventing Storage Collection (previously Metadata Bucket)

Eventing functions store less than 2048 docs per Function. If timers are not used or if you have less than a few thousand active timers, then the size of the Eventing storage collection can simply be in a bucket with a minimum size 100 MB.

However, if you use timers you will have to allocate an additional space of about 800 bytes + the size of the passed context (which is the state passed to the function when it is called in the future) per active timer.

Let's say you have a context of 200 bytes (total 1K/timer), then for 100,000 active timers you would need 100 MB of additional space in this bucket.

As a best practice, we recommend that you keep this collection 100% resident. Note that this collection can be shared across all your Eventing Functions.

## [](#sizing-backup-service-nodes)Sizing Backup Service Nodes

The hardware requirements for running a backup cluster are as follows:

__Table 11\. Hardware requirements__
|        | Minimum     | Recommended  |
| ------ | ----------- | ------------ |
| CPUs   | 4 CPU cores | 16 CPU cores |
| Memory | 8 GiB       | 16 GiB       |

## [](#sizing-for-replication-xdcr)Sizing for Replication (XDCR)

Before setting up a replication, you must make sure your cluster is appropriately configured and provisioned.

Your cluster must be properly sized in order to be able to handle new XDCR streams.

For example, XDCR needs 1-2 additional CPU cores per stream; and in some cases, will require additional RAM and network resources as well. If a cluster is not sized to handle _both_ the existing workload _and_ the new XDCR streams, the performance of both XDCR and the cluster overall may be negatively impacted.

For information on preparing your cluster for replication, see [Prepare for XDCR](../manage/manage-xdcr/prepare-for-xdcr.md).