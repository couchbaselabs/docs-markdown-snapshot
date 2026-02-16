[View original HTML](/server/7.2/learn/services-and-indexes/indexes/index-replication.html)

> The Index Service ensures availability and performance through replication and partitioning. You can control the scan consistency for individual queries. 

Examples on this Page

The examples in this topic use the travel-sample dataset which is shipped with Couchbase Server. For instructions on how to install the sample bucket, see [Sample Buckets](../../../manage/manage-settings/install-sample-buckets.md).

To use the examples on this page, you must set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../../../n1ql/n1ql-intro/queriesandresults.md#query-context).

## [](#index-replication)Index Replication

Secondary indexes can be replicated across cluster-nodes. This ensures:

* _Availability_: If one Index-Service node is lost, the other continues to provide access to replicated indexes.
* _High Performance_: If original and replica copies are available, incoming queries are load-balanced across them.

Index-replicas can be created with the SQL++ `CREATE INDEX` statement. Note that whenever a given number of index-replicas is specified for creation, the number must be less than the number of cluster-nodes currently running the [Index Service](../services/index-service.md). If it is not, the index creation fails. Note also that if, following creation of the maximum number of copies, the number of nodes running the Index Service decreases, Couchbase Server progressively assigns replacement index-replicas to any and all Index-Service nodes subsequently be added to the cluster, until the required number of index-replicas again exists for each replicated index.

Index-replicas can be created as follows:

* Specifying, by means of the `WITH` clause, the destination nodes. In the following example, an index with two replicas is created. The active index is on `node1`, and the replicas are on `node2` and `node3`:  
```sqlpp  
CREATE INDEX country_idx ON airport(country, city)  
WITH {"nodes": ["node1:8091", "node2:8091", "node3:8091"]};  
```
* Specifying _no_ destination nodes; but specifying instead, by means of the `WITH` clause and the `num_replica` attribute, only the _number_ of replicas required. The replicas are automatically distributed across those nodes of the cluster that are running the Index Service: the distribution-pattern is based on a projection of optimal index-availability, given the number and disposition of Index-Service nodes across defined server-groups.  
In the following example, an index is created with two replicas, with no destination-nodes specified:  
```sqlpp  
CREATE INDEX country_idx ON airport(country, city)  
WITH {"num_replica": 2};  
```  
Note that if `nodes` and `num_replica` are both specified in the `WITH` clause, the specified number of nodes must be _one greater_ than `num_replica`.
* Specifying a number of index-replicas to be created by the Index Service whenever `CREATE INDEX` is invoked. The default is `0`. If the default is changed to, say, `2`, creation of a single index is henceforth accompanied by the creation of two replicas, which are automatically distributed across the nodes of the cluster running the Index Service. No explicit specification within the `CREATE INDEX` statement is required.  
With credentials that provide appropriate authorization, this default can be changed by means of the `curl` command, as follows:  
```sh  
curl -X POST -u 'Administrator:password' \  
'http://localhost:8091/settings/indexes' \
-d 'numReplica=2'  
```  
Here, `numReplica` is an integer that establishes the default number of replicas that must be created whenever `CREATE INDEX` is invoked. Note that this call only succeeds if the cluster contains enough Index Service nodes to host each new index and its replicas: for example, if `2` is specified as the default number of replicas, the Index Service must have been established on at least 3 nodes.  
Note also that whenever explicit specification of replica-numbers is made within the `CREATE INDEX` statement, this explicit specification takes precedence over any established default.

You can change index replication settings via the [UI](../../../manage/manage-settings/general-settings.md#index-storage-mode) or the [REST API](../../../manage/manage-settings/general-settings.md#index-settings-via-rest). For further information on using SQL++, refer to [Query Fundamentals](../../../n1ql/query.md).

## [](#index-partitioning)Index Partitioning

_Index Partitioning_ increases query performance, by dividing and spreading a large index of documents across multiple nodes. This feature is available only in Couchbase Server Enterprise Edition.

The benefits include:

* The ability to scale out horizontally, as index size increases.
* Transparency to queries, requiring no change to existing queries.
* Reduction of query latency for large, aggregated queries; since partitions can be scanned in parallel.
* Provision of a low-latency range query, while allowing indexes to be scaled out as needed.

For detailed information, refer to [Index Partitioning](../../../n1ql/n1ql-language-reference/index-partitioning.md).

## [](#index-consistency)Index Consistency

Whereas Couchbase Server handles data-mutations with _full consistency_ — all mutations to a given key are applied to the same vBucket, and become immediately available — it maintains indexes with degrees of _eventual consistency_, determined by means of the following query consistency-options, specified per query:

* `not_bounded`: Executes the query immediately, without requiring any consistency for the query. If index-maintenance is running behind, out-of-date results may be returned.
* `at_plus`: Executes the query, requiring indexes first to be updated to the timestamp of the last update. If index-maintenance is running behind, the query waits for it to catch up.
* `request_plus`: Executes the query, requiring the indexes first to be updated to the timestamp of the current query-request. If index-maintenance is running behind, the query waits for it to catch up.
* `statement_plus`: Executes the query with strong consistency per statement. Before processing each statement, the service obtains a current vector timestamp and uses it as a lower bound for that statement.

For SQL++, the default consistency is `not_bounded`.

You can specify the scan consistency via the [run-time preferences](../../../tools/query-workbench.md#query-preferences) in the Query Workbench, or by setting the [scan\_consistency](../../../settings/query-settings.md#scan%5Fconsistency) request-level parameter.

## [](#index-snapshots)Index Snapshots

One or more _index snapshots_ are maintained on disk, to permit rapid recovery if node-failures are experienced. In cases where recovery requires an Index-Service node to be restarted, the node’s indexes are rebuilt from the snapshots retained on disk.

By default, two index snapshots are stored on disk. You can change index snapshot settings via the [CLI](../../../manage/manage-settings/general-settings.md#index-storage-settings-via-cli) or the [REST API](../../../manage/manage-settings/general-settings.md#index-settings-via-rest).

## [](#index-rollback)Index Rollback

The index service also maintains a [DCP failover log](../../clusters-and-availability/intra-cluster-replication.md#database-change-protocol). If necessary, the data service can request the index service to return to a specified rollback point and update its history.

You can change index rollback settings via the [CLI](../../../manage/manage-settings/general-settings.md#index-storage-settings-via-cli) or the [REST API](../../../manage/manage-settings/general-settings.md#index-settings-via-rest).

### [](#index-rollback-after-failover)Index Rollback After Failover

When a data node [fails over](../../clusters-and-availability/failover.md), a replica data node is promoted to active. If the index service has more recent data than the new active data node, the data node issues a rollback request to the index service.

In Couchbase Server 6.5 and later, when the index service receives the rollback request, it first attempts to revert to a stored index snapshot. If successful, the index service does not need to rebuild its indexes from scratch when the data node fails over. The index service can continue servicing query clients without interruption.

If the index service cannot revert to a current index snapshot, it rebuilds all indexes from scratch.

|  | If [scan consistency](#index-consistency) is set to not\_bounded, the index service may return stale data for a short time after reverting to a snapshot, until the index service is fully up-to-date with the new active data node. If [scan consistency](#index-consistency) is set to request\_plus, the index service will not perform any scans until a consistent snapshot is created. In this case, stale results are not returned. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |