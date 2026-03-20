---
title: Glossary
description: Principal terms and their meanings.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/learn/pages/glossary.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:learn:glossary.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/learn/glossary.html)

# Glossary

> Principal terms and their meanings. 

The following glossary introduces the principal terms used in descriptions of Couchbase Server-technology. Use the links to locate the full descriptions of each.

* [Server](../introduction/intro.md): An instance of _Couchbase Server_ — an open source, distributed, NoSQL document-oriented engagement database, specialized to provide low-latency data management for large-scale interactive web, mobile, and other applications. Each instance runs on its own physical or virtual machine.
* [Cluster](clusters-and-availability/clusters-and-availability.md): One or more instances of Couchbase Server, each running on an independent node; but cooperating with any and all others, so as to form a unified system; whereby resources are shared, and a single interface provided for data-access and management.
* [Bucket](buckets-memory-and-storage/buckets.md): A logical, user-named entity that groups items; allowing them to be accessed, indexed, replicated, and access-controlled. There are three types:

  * **Couchbase**: Retains data both in memory and on disk.
  * **Ephemeral**: Retains data in memory only.
  * **Memcached**: Deprecated in 7.0, this has been intended for use in the context of other database platforms, such as ones employing relational database technology, in order to provide a managed memory-cache for frequently-used data.
* [Collection](data/scopes-and-collections.md): A data container, defined on Couchbase Server, within a bucket whose type is either _Couchbase_ or _Ephemeral_.
* [Scope](data/scopes-and-collections.md): A mechanism for the grouping of multiple collections.
* [Durability](data/durability.md): The atomic commitment of a single-document data-write, which ensures the write’s greatest likelihood of surviving an unexpected anomaly, such as a node-outage, prior to the write’s propagation throughout the entire cluster.
* [Memory](buckets-memory-and-storage/memory.md): An automatically managed caching layer, supporting high-speed data-access.
* [Storage](buckets-memory-and-storage/storage-settings.md): The persistent retention of items on disk, in compressed form, with high-speed threaded access.
* [Data](data/data.md): Items, each of which consists of a key by which the item is referenced; and an associated value, which must be either binary or a JSON document.

  * Access: The creation, update, and deletion of items, as supported by [Couchbase Web Console](../manage/manage-ui/manage-ui.md) and the [Couchbase SDK](#home:ROOT:sdk.adoc).
  * [Model](data/document-data-model.md): A lightweight, flexible schema; which can be progressively evolved by applications over time, and allows information to be stored in the form of items.
* [Node](clusters-and-availability/nodes.md): A computer (potentially, a virtual machine) running an instance of Couchbase Server.

  * [Addition](../manage/manage-nodes/add-node-and-rebalance.md): The ability to add a Couchbase Cluster of one node to another existing cluster, so that a single, combined cluster is produced. Following addition, rebalance ensures that data, indexes, event processing, and query processing are optimally distributed across all available nodes.
  * [Failover](clusters-and-availability/failover.md): The ability to allow healthy nodes to continue functioning as a cluster, potentially without data-loss, when one node has gone offline. Rebalance ensures that data, indexes, event processing and query processing are optimally distributed across all available nodes. Failover can be automated.
  * [Removal](../manage/manage-nodes/remove-node-and-rebalance.md): The ability to remove a node from a cluster. Following removal, rebalance ensures that data, indexes, event processing and query processing are optimally distributed across all available nodes.
* [Rebalance](clusters-and-availability/rebalance.md): The process of redistributing data, indexes, event processing, and query processing optimally among the available nodes of a cluster. This should be performed whenever a cluster-configuration has changed.
* [Availability](clusters-and-availability/clusters-and-availability.md): The preservation of data from system-failure, by the following means:

  * [Backup and Restore](services-and-indexes/services/backup-service.md): The storing in archive-repositories of the current state of data, indexes, and bucket configurations; and the restoration of such state to a running cluster.
  * [Cross Data Center Replication](clusters-and-availability/xdcr-overview.md) (_XDCR_): The replication of data between clusters, to ensure the least chance of data-loss in the event of data-center failure, and to provide high-performance data-access for globally distributed applications.
  * [Data Recovery](../cli/cbcli/couchbase-cli-recovery.md): The restoration of current data to a node that is recovered from failure: either by updating data still held locally, or by substituting current data from other nodes.
  * [Intra-Cluster Replication](clusters-and-availability/intra-cluster-replication.md): The maintenance and continuous update of data-copies, distributed across the nodes of a cluster, to ensure the least chance of data-loss in the event of single-node failure.
* [Deployment](../install/get-started.md): The installation of a single instance of Couchbase Server, subsequent to the appropriate resourcing and configuration of an underlying platform.

  * [Cloud](../cloud/couchbase-cloud-deployment.md): Couchbase Server runs on a pre-established cloud-configuration.
  * [Container](../cloud/couchbase-cloud-deployment.md): Couchbase Server runs within a software container or virtual machine.
  * [Native](../install/install-intro.md): Couchbase Server runs on an individual, physical machine.
* [Initialization](../manage/manage-nodes/initialize-node.md): The configuration of a new instance of Couchbase Server, either as the first node in a new cluster, or as an additional node for an existing cluster.
* [Security](security/security-overview.md): Couchbase-Server Authentication, Authorization, Auditing, and Encryption.

  * [Authentication](security/authentication.md): To access Couchbase Server, administrators and applications must be authenticated. Authentication is a process for identifying a user who is attempting to access a system. Authentication can be attempted by passing credentials, or by means of certificates.
  * [Authorization](security/authorization-overview.md): Role-Based Access Control (_RBAC_), whereby access-privileges are assigned to fixed roles that are assigned to administrators and applications.
  * [Auditing](security/auditing.md): The detailed, automated recording of actions performed on Couchbase Server, allowing administrative review; in order to ensure that system-management tasks are being appropriately performed.
  * [Encryption](security/encryption-overview.md): The protection of data on the wire, at rest, and in applications; by means of encoding.
* [Services](services-and-indexes/services/services.md): Couchbase Server-facilities that support different forms of data-access:

  * [Analytics](services-and-indexes/services/analytics-service.md): Supports join, set, aggregation, and grouping operations that are expected to be large, long-running, and highly consumptive of memory and CPU resources.
  * [Data](services-and-indexes/services/data-service.md): Supports the storing, setting, and retrieving of data-items, specified by key.
  * [Eventing](../eventing/eventing-overview.md): Supports near real-time handling of changes to data: code can be executed both in response to document-mutations, and as scheduled by timers.
  * [Index](services-and-indexes/services/index-service.md): Creates indexes, for use by the Query Service.
  * [Query](services-and-indexes/services/query-service.md): Parses input specified in the N1QL query-language, executes queries, and returns results. The Query Service interacts with both the Data and Index services.
  * [Search](../search/search.md): Creates indexes specially purposed for Full Text Search. This supports language-aware searching; allowing users to search for, say, the word beauties, and additionally obtain results for beauty and beautiful.
  * [Backup](services-and-indexes/services/backup-service.md): Allows the scheduling of backups and merges of data.
* [Scaling](services-and-indexes/services/services.md): The optional allocation of services to cluster-nodes in accordance with workload-requirements. For example, if a particular service is expected to handle a heavy workload, it can be allocated a large memory quota, and might be deployed as the only service on its node, to ensure optimal availability of CPU cycles.
* [Tools](../manage/management-overview.md#couchbase-server-tools): Provided by Couchbase Server to support cluster-management:

  * [CLI](../cli/cli-intro.md): Command-line-based management.
  * [Couchbase Web Console](../manage/manage-ui/manage-ui.md): UI-based management.
  * [REST API](../rest-api/rest-intro.md): RESTful management. Note that the REST API, as well as being directly available to the administrator, also underlies the features of the Couchbase Web Console and CLI.
* [SDK](../../../java-sdk/current/hello-world/start-using-sdk.md): Libraries that support cluster-access for applications written in multiple languages.
* [Transactions](data/transactions.md): Operations that ensure that when multiple documents need to be modified such that only the successful modification of all justifies the modification of any, either all the modifications do occur successfully; or none of them occurs.
* [Chronicle](clusters-and-availability/metadata-management.md): The Couchbase-Server methodology for consensus-based metadata management, based on the [Raft](https://raft.github.io/) algorithm.

## [](#further-reading)Further Reading

Glossaries are available for:

* [Couchbase SDKs](../../../java-sdk/current/ref/glossary.md)
* [Couchbase Eventing Service](../eventing/eventing-Terminologies.md)
* [Couchbase Lite (Android)](../../../couchbase-lite/current/android/refer-glossary.md)
* [Sync Gateway](../../../sync-gateway/current/glossary.md)