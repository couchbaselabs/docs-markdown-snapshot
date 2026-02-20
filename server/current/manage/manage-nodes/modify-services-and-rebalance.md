---
title: Modify Services and Rebalance
description: Add or remove non-Data Services on existing nodes in a cluster and
  rebalance the cluster without adding or removing nodes.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/manage/pages/manage-nodes/modify-services-and-rebalance.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:manage:manage-nodes/modify-services-and-rebalance.adoc[]
---

[View original HTML](/server/current/manage/manage-nodes/modify-services-and-rebalance.html)

# Modify Services and Rebalance

> Add or remove non-Data Services on existing nodes in a cluster and rebalance the cluster without adding or removing nodes. 

You can dynamically add or remove the following Multi-Dimensional Scaling (MDS) services on existing nodes in a cluster from the Couchbase [UI](#modify-mds-services-from-ui), [REST API](../../rest-api/rest-set-up-services-existing-nodes.md), or [CLI](#modify-mds-services-using-cli):

* `index` (Index Service)
* `n1ql` (Query Service)
* `fts` (Search Service)
* `cbas` (Analytics Service)
* `eventing` (Eventing Service)
* `backup` (Backup Service)

Then a rebalance operation is automatically triggered to distribute the service workload across the nodes and complete the modification.

You do not have to add or remove a node to add or remove a non-Data Service on a node in a cluster.

> [!NOTE]
> You cannot add or remove the Data Service (kv) using this method. Adding or removing of the Data Service on an existing node is supported only through adding or removing nodes. For more information about adding or removing the Data Service on an existing node, see [Adding or Removing the Data Service on Existing Nodes](manage-data-service-and-rebalance.md).

> [!WARNING]
> When you modify (add or remove) services on existing nodes in a cluster, rebalance is triggered immediately to apply the changes. Removing a service instance reduces the cluster’s capacity for that service. For certain services, such as the Index Service, removing the service may result in loss of replicas or entire indexes if no replicas exist, which can cause queries to fail.
> 
> Removing all instances of a service deletes all data and metadata associated with that service, which means effectively removing the service from the cluster. For example, removing the last Index Service node deletes all indexes. For the Backup Service, physical backup repositories outside the cluster remain, but the Backup Service metadata about those repositories is deleted.

## [](#prerequisites)Prerequisites

Before modifying non-data services on nodes, make sure you have the following:

* The Couchbase Server cluster must be running the 8.0 or a later version.
* Full Administrator access. For more information, see [Full Admin](../../learn/security/roles.md#full-admin).
* A clear understanding of the current service distribution across the nodes.
* Service Memory Quota: When you add a service that was not earlier present in the cluster, the new service may use the service-specific default memory quota. This applies to the Index, Search, Eventing, and Analytics services.  
Verify that the memory quota for the new service meets your requirements using one of the following:

  * The REST API from [Getting Memory Information](../../rest-api/rest-get-memory-information.md).
  * The UI from [Configure General Settings with the UI](../manage-settings/general-settings.md#configure-general-settings-with-the-ui).  
  > [!NOTE]  
  > The service memory quota setting is per server node and is reflected in the `GET /pools/default` REST API response.
* Node Disk Storage Paths: The node disk storage paths are set for all services that require disk storage paths (Data, Indexes, Eventing, Analytics) when a node is initialized. These storage paths cannot be changed after the node becomes a part of a cluster. This means that if you are adding a service (Index, Search, Analytics, Eventing) to an existing node, that service is using the disk storage path that was specified when the node was initialized. Ensure that you know the node disk storage path set for the service that you are adding. For information on how to view the node disk storage paths, see [List Nodes with the REST API](list-cluster-nodes.md#list-nodes-with-the-rest-api). Use the `GET /pools/default` REST API to find the otpNode value for the node and then use the `GET /nodes/<otpNode>` REST API to view the disk storage paths.

## [](#modify-mds-services-from-ui)Modify Services from the UI

To manage non-Data services from the UI, follow these steps:

1. Open the Couchbase Server Web Console.
2. Click **Servers**.
3. Click **Modify Services**.  
The **Modify Cluster Services** dialog appears, which lists all the nodes in all the clusters and their current services.  
Services that can be modified are:

  * **index** (Index Service)
  * **n1ql** (Query Service)
  * **fts** (Search Service)
  * **cbas** (Analytics Service)
  * **eventing** (Eventing Service)
  * **backup** (Backup Service).  
kv (Data Service) cannot be modified.
4. Select the services you want to add for each node and deselect the services you want to remove from each node.  
> [!NOTE]  
> Adding or removing any service triggers a rebalance operation.
5. Click **Rebalance and Change Services**.  
If you’re only removing services, adding new instances of services that already exist on the cluster, or adding the backup service, then rebalancing is triggered immediately.
6. If you are adding a service that is not already on the cluster, and if that service has a memory quota setting option, then the **New Service Settings** dialog appears. This dialog lists the services you selected to add, the existing active services, and their current memory quotas.

  1. Enter the memory quota for each service you’re adding. You can also edit the memory quota for existing services.  
  For the Index Service, choose either **Standard Global Secondary** or **Memory-Optimized**. For more information about index storage, see [Index Storage Settings](../../indexes/storage-modes.md).  
  For more information about managing memory quotas for services from the UI, see [Memory Quotas](../manage-settings/general-settings.md#memory-quotas).
  2. Click **Save Settings**.

The rebalancing operation is automatically triggered, which distributes the service workload across the nodes and completes the modification. Status progress is displayed on the UI.

When the rebalance operation is successful, an acknowledgment message appears on the UI and you can download the rebalance report by clicking **Download Report**.

## [](#modify-mds-services-using-cli)Modify Services Using CLI

To modify non-Data services on the existing nodes of a cluster using the CLI, use the following `couchbase-cli rebalance` command:

couchbase-cli rebalance -c <network_address> \
--username <username> \
--password <password> \
--update-services [--index-[add|remove] <list-of-nodes>] [--n1ql-[add|remove] <list-of-nodes>] [--fts-[add|remove] <list-of-nodes>] [--cbas-[add|remove] <list-of-nodes>] [--eventing-[add|remove] <list-of-nodes>] [--backup-[add|remove] <list-of-nodes>]

These are the options for modifying non-data services:

* `--update-services`: Indicates that the rebalance will make changes to the services on the cluster.
* `--<service>-add <node>`: Adds the specified service to the specified node. `<service>` can be one of the following:

  * `index` for the Index Service.
  * `n1ql` for the Query Service.
  * `fts` for the Search Service.
  * `cbas` for the Analytics Service.
  * `eventing` for the Eventing Service.
  * `backup` for the Backup Service.
* `--<service>-remove <node>`: Removes the specified service from the specified node.

### [](#examples)Examples

* The `–fts-add` argument adds the full-text search service to the list of nodes.
* The `–index-remove` argument removes the index service from the list of nodes.
* To add the index service to `node2`, use the following command:  
couchbase-cli rebalance -c 127.0.0.1 -u Administrator -p password --update-services --index-add node2
* To remove the index service from `node3`, use the following command:  
couchbase-cli rebalance -c 127.0.0.1 -u Administrator -p password --update-services --index-remove node3
* Trying to remove a service that’s not present on the node results in an error. From the previous example, if `node3` was not running the index service, the following error occurs:  
ERROR: Node ns_1@node3 does not provide the index service

For more information about the `couchbase-cli rebalance` command, see [rebalance](../../cli/cbcli/couchbase-cli-rebalance.md).