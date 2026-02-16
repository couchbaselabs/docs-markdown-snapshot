[View original HTML](/server/current/learn/services-and-indexes/services/services.html)

> Couchbase Server Services provide data access and maintenance. You can deploy services flexibly across available hardware to support Multi-Dimensional Scaling, which allows the tuning of the cluster for optimal performance as workloads change. 

Services in Couchbase Server are configured and deployed during initialization on 1 or more nodes by a Full Administrator. During configuration, the administrator can select a subset of services for each node and assign memory to each service individually.

Each service provides a specific type of data access. Couchbase recommends deploying only required services. To handle heavy workloads, you can deploy a service across multiple nodes in the cluster to improve performance and resource availability.

In Couchbase Server 7.6 and later versions, you can add 1 or more arbiter nodes to your cluster. An arbiter node helps your cluster in two ways:

* It provides [fast failover](../../clusters-and-availability/nodes.md#fast-failover) which helps decrease the cluster’s latency when reacting to a failover.
* It provides [quorum arbitration](../../../install/deployment-considerations-lt-3nodes.md#quorum-arbitration) that helps avoid contention issues if the nodes in the cluster become partitioned.

## [](#services-and-multi-dimensional-scaling)Services and Multi-Dimensional Scaling

Couchbase Server provides the following services:

* [Data Service](data-service.md): Stores, updates, and retrieves data items by key.
* [Query Service](query-service.md): Parses and executes SQL++ queries, and returns results. Interacts with the Data and Index services.
* [Index Service](index-service.md): Creates indexes, for use by the Query and Analytics services.
* [Search Service](search-service.md): Creates indexes for a fully customizable search experience. Supports near real-time search capabilities for a diverse range of data types, such as structured or unstructured text, dates, numbers, CIDR notation, geospatial data, and vectors.
* [Analytics Service](analytics-service.md): Performs join, set, aggregation, and grouping operations. Designed for large, long-running workloads that require significant memory and CPU resources.
* [Eventing Service](eventing-service.md): Handles near real-time responses to data changes. Executes code in response to document mutations or on scheduled timers.
* [Backup Service](backup-service.md): Schedules full and incremental backups for specific buckets or all buckets in a cluster. Supports merging and pruning of existing backups.

With Multi-Dimensional Scaling (MDS), you can deploy, maintain, and provision these services independently to optimize performance as business needs and workloads change.

## [](#setting-up-services)Setting Up Services

Services are configured per node. Each node can run 1 instance of a service and up to 7 services in total. In Couchbase Enterprise Server 7.6 and later, you can configure a node to run no services.

The Data Service must run on at least 1 node in the cluster. Some services are interdependent and require at least 1 instance of each dependency to be running. For example, the Query Service depends on the Index and Data services.

When you initialize the first node in a cluster, that node’s service configuration becomes the default for nodes added later. You can change the default configuration for individual nodes by removing services, adding services, or both.

In Couchbase Server 8.0 and later versions, you can add or remove the following non-Data Services on-demand on existing nodes in a cluster, without adding or removing nodes.

* index (Index Service).
* n1ql (Query Service).
* fts (Search Service).
* cbas (Analytics Service).
* eventing (Eventing Service).
* backup (Backup Service).

Then a rebalance operation is automatically triggered to distribute the service workload across the nodes and complete the modification. For more information about adding or removing non-Data Services on an existing node, see [Modify Services and Rebalance](../../../manage/manage-nodes/modify-services-and-rebalance.md).

Adding or removing of the Data Service (kv) on an existing node is supported only through adding or removing nodes. For more information about adding or removing the Data Service on an existing node, see [Adding or Removing the Data Service on Existing Nodes](../../../manage/manage-nodes/manage-data-service-and-rebalance.md).

You can change the services running on nodes to support Multi-Dimensional Scaling (MDS). This flexibility lets you adjust the cluster as per your requirements.

For example, you may start with a small cluster where some nodes run multiple services, such as Index and Search, because you have more need for services than the available nodes. As your requirements grow, you can add nodes and move services to those new nodes to free resources on the original nodes. If a service becomes resource-constrained, you can add it to more nodes in the cluster to increase its capacity and meet demand.

When you allocate a service to a node, you must assign it a memory quota. This quota becomes the standard for that service across all its instances in the cluster. The Query and Backup services are exceptions and do not require a memory quota.

You must design your service allocation based on workload analysis. If a service is expected to handle a heavy workload, assign it a larger memory quota and consider running it as the only service on the node. For development clusters, you can allocate services quickly and conveniently, with some quotas set equally.

The following example shows how 4 services such as Data, Index, Query, and Search that can be evenly allocated across 5 nodes in a development cluster:

![Couchbase Server Cluster for Development](../../_images/diag-527455154b76239ea01ae93adbe9fb32fc1ff508.svg) 

Figure 1\. Couchbase Server Cluster for Development

This configuration may provide adequate performance for development and testing. However, if large volumes of data require intensive indexing and querying with Search, the following production configuration is more efficient:

![Couchbase Server Cluster for Production](../../_images/diag-1a07eeba4146bf13d7c26f4b8ec8216a9b04ab39.svg) 

Figure 2\. Couchbase Server Cluster for Production

In the revised configuration, the Data Service runs exclusively on 3 nodes, the Index Service runs on 2 nodes, and the Query and Search services share the sixth node.

For more information about:

* Service memory quotas, see [Memory](../../buckets-memory-and-storage/memory.md).
* Initializing a cluster, see [Create a Cluster](../../../manage/manage-nodes/create-cluster.md).
* Adding or removing the Data Service on a node, see [Adding or Removing the Data Service on Existing Nodes](../../../manage/manage-nodes/manage-data-service-and-rebalance.md).
* Adding or removing non-Data services on a node, see [Modify Services and Rebalance](../../../manage/manage-nodes/modify-services-and-rebalance.md).
* Using the REST API to assign services to a new single node cluster, see [Assigning Services to a New Single Node](../../../rest-api/rest-set-up-services.md).
* Using the REST API to assign services to an existing node of a cluster, see [Assigning Services to an Existing Node](../../../rest-api/rest-set-up-services-existing-nodes.md).

## [](#multi-dimensional-scaling)Multi-Dimensional Scaling

Couchbase Services can be deployed flexibly across hardware resources to support Multi-Dimensional Scaling. This allows you to fine-tune a cluster for optimal performance as workloads change.

For example, if Search workloads increase, you can remove other services from 1 or more non-Search nodes and reconfigure those nodes to run the Search Service in the cluster.

You can also add hardware resources such as CPU, memory, or disk capacity to specific nodes to improve the performance of key services. Because services can be provisioned independently, you can scale their performance up or down as needed. This flexibility helps meet changing business requirements and redeploy resources efficiently.