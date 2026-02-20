---
title: Assigning Services to an Existing Node
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-set-up-services-existing-nodes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:rest-api:rest-set-up-services-existing-nodes.adoc[]
---

[View original HTML](/server/current/rest-api/rest-set-up-services-existing-nodes.html)

# Assigning Services to an Existing Node

> Use the REST API to assign or remove services on an existing node in a cluster, and rebalance the cluster. 

### [](#http-method-and-uri)HTTP Method and URI

POST /controller/rebalance

## [](#description)Description

Use the following REST API to add or remove non-Data services on the existing nodes in a cluster. Then trigger a rebalance operation.

> [!NOTE]
> * Follow the [Prerequisites](../manage/manage-nodes/modify-services-and-rebalance.md#prerequisites) in [Modify Services and Rebalance](../manage/manage-nodes/modify-services-and-rebalance.md) before using the REST API.
> * For information about using the `POST /controller/rebalance` REST API to rebalance after node additions and removals, after a graceful failover and recovery, and after a hard failover, see [Rebalancing the Cluster](rest-cluster-rebalance.md).

> [!WARNING]
> When you modify (add or remove) services on existing nodes in a cluster, rebalance is triggered immediately to apply the changes. Removing a service instance reduces the cluster’s capacity for that service. For certain services, such as the Index Service, removing the service may result in loss of replicas or entire indexes if no replicas exist, which can cause queries to fail.
> 
> Removing all instances of a service deletes all data and metadata associated with that service, which means effectively removing the service from the cluster. For example, removing the last Index Service node deletes all indexes. For the Backup Service, physical backup repositories outside the cluster remain, but the Backup Service metadata about those repositories is deleted.

### [](#curl-syntax)curl Syntax

You must specify all known nodes in the cluster and the necessary cluster services topology.

curl -v -X POST -u [admin]:[password] \
http://[localhost]:8091/controller/rebalance \
[-d knownNodes | -d topology]

These are services related parameters:

* `knownNodes`: The value is a list containing all nodes that are in the cluster at the start of the rebalance process.
* `topology`: The value is a list of services and the nodes in which services must reside, after the rebalance operation completes.  
The value is `topology[<service>]=<list of nodes>`.  
Where,

  * `<service>` can be one of the following services:

    * `fts` for the Search Service.
    * `index` for the Index Service.
    * `n1ql` for the Query Service.
    * `backup` for the Backup Service.
    * `cbas` for the Analytics Service.
  * `<list of nodes>` indicate the nodes on which the `<service>` must reside in after the rebalance operation is complete. The node names are separated by commas.
  * For example, `-d topology[<service>]="otp_node1,otp_node2"`.
  * To remove or exclude one of the above listed services from the cluster, do not list any nodes for that service. For example, `-d topology[<service>]=""`.

> [!NOTE]
> The rebalance occurs even if no `<service>` is changed.

Each service you assign uses the memory quota currently configured for that service on the cluster. You can modify the services memory quotas, if needed, prior to running the services reconfiguration command for the cluster nodes.

For information about allocating memory per service, see [Configuring Memory](rest-configure-memory.md).

To fetch the details of current memory allocation for each service, see [Getting Memory Information](rest-get-memory-information.md).

## [](#required-permissions)Required Permissions

`Full Admin` role.

## [](#responses)Responses

| Value                                                                   | Description                                                            |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 200 OK and JSON array containing the expired backups and their details. | Successful call.                                                       |
| 400                                                                     | Invalid parameter.                                                     |
| 400 Object Not found                                                    | The repository in the endpoint URI does not exist.                     |
| 401 Unauthorized                                                        | Authorization failure due to incorrect username or password.           |
| 403 Forbidden, plus a JSON message explaining the minimum permissions.  | The provided username has insufficient privileges to call this method. |
| 404 Object Not Found                                                    | Error in the URI path.                                                 |
| 500 Internal Server Error                                               | Error in Couchbase Server.                                             |

### [](#example)Example

For example, a cluster with 5 nodes could have the following service configuration:

* 172.23.108.69 – Data, Index, Query
* 172.23.108.70 – Data, Search, Query
* 172.23.108.71 – Query
* 172.23.108.72 – Backup
* 172.23.108.73 – Analytics

You could reconfigure the services on the existing nodes to match the following:

* 172.23.108.69 – Data, Query
* 172.23.108.70 – Data, Index
* 172.23.108.71 – Index, Query
* 172.23.108.72 – Search, Query
* 172.23.108.73 – Analytics

After the topology change and rebalance, 2 nodes (172.23.108.71 and 172.23.108.72) that did not have any services using the index disk storage path will now have services using it.

Also, using the following command, you remove the Backup Service from the cluster by not listing any nodes in `-d topology[backup]=`.

To reconfigure the 5 nodes to the new topology, run the following command:

curl -u Administrator:password -X POST 172.23.108.69:8091/controller/rebalance \
-d knownNodes="ns_1@172.23.108.69,ns_1@172.23.108.70,ns_1@172.23.108.71,ns_1@172.23.108.72,ns_1@172.23.108.73"  \
-d topology[index]="ns_1@172.23.108.70,ns_1@172.23.108.71"  \
-d topology[fts]="ns_1@172.23.108.72"  \
-d topology[n1ql]="ns_1@172.23.108.69,ns_1@172.23.108.71,ns_1@172.23.108.72" \
-d topology[backup]="" \
-d topology[cbas]="ns_1@172.23.108.73"

## [](#see-also)See Also

* To retrieve the list of services running on a node, see [Listing Node Services](rest-list-node-services.md).
* For more information about allocating memory per service, see [Configuring Memory](rest-configure-memory.md).
* To fetch the details of current memory allocation for each service, see [Getting Memory Information](rest-get-memory-information.md).
* For more information about assigning services to existing nodes from the UI and CLI, see [Modify Services and Rebalance](../manage/manage-nodes/modify-services-and-rebalance.md).
* For more information about assigning services to a new node, see [Assigning Services to a New Single Node](rest-set-up-services.md).
* For more information about rebalancing, see [Rebalancing the Cluster](rest-cluster-rebalance.md).