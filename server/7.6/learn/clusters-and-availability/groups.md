---
title: Server Group Awareness
description: Individual server-nodes can be assigned to specific
  <em>groups</em>, within a Couchbase Cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/learn/pages/clusters-and-availability/groups.adoc
  xref: xref:7.6@server:learn:clusters-and-availability/groups.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/learn/clusters-and-availability/groups.html)

# Server Group Awareness

> Individual server-nodes can be assigned to specific _groups_, within a Couchbase Cluster. This allows both _active vBuckets_ and GSI _indexes_ to be maintained on groups different from those of their corresponding _replica vBuckets_ and _index replicas_; so that if a group goes offline, and active vBuckets and indexes are thereby lost, replicas remain available on one or more other groups. 

## [](#understanding-server-group-awareness)Understanding Server Group Awareness

_Server Group Awareness_ provides enhanced availability. Specifically, it protects a cluster from large-scale infrastructure failure, through the definition of _groups_. Each group is created by an appropriately authorized administrator, and specified to contain a subset of the nodes within a Couchbase Cluster. Following group-definition and rebalance, the active vBuckets for any defined bucket are located on one group, while the corresponding replicas are located on another group: indexes and _index replicas_, maintained by the Index Service, are distributed across groups in a similar way.

A server group can be automatically _failed over_: thus, if the entire group goes offline, and active vBuckets and indexes are thereby inaccessible, then the replica vBuckets and replica indexes that remain available on another group can be automatically promoted to active status.

> [!NOTE]
> For the vBuckets and replica indexes to be automatically promoted to active, the conditions specified in [Auto-failover Constraints](automatic-failover.md#auto-failover-constraints) must apply.

Note that in 7.1+, automatic failover can fail over more than three nodes concurrently: this has permitted the removal of pre-7.1 interfaces that were specific to triggering auto-failover for server groups.  
Consequently, for auto-failover of a server group to be possible, the maximum count for auto-failover must be established by the administrator as a value equal to or greater than the number of nodes in the server group.  
Due to the removal of the pre-7.1 interfaces, applications that attempt to use the interfaces with 7.1+ will _fail._

> [!IMPORTANT]
> For auto-failover to occur, all of the auto-failover constraints listed in [Auto-failover Constraints](automatic-failover.md#auto-failover-constraints) must be met, including the majority quorum requirement: i.e., the remaining nodes must be able to form a majority quorum to be able to initiate an auto-failover.  
> If, for example, you have two server groups, with equal number of nodes in each, and if all the nodes in one of the server groups fail at the same time, even if you have the maximum count for auto-failover set to a value equal to or greater than the number of nodes in the server group that failed, auto-failover cannot occur since the remaining nodes in the remaining server group cannot form a majority quorum.
> 
> The [quorum constraint](../../install/deployment-considerations-lt-3nodes.md#quorum-arbitration) is a critical part of auto-failover since the cluster must be able to form a quorum to initiate a failover, following the failure of the nodes. For Server Groups, this means that if you have two server groups with equal number of nodes, for auto-failover of all nodes in one server group to be able to occur, you must have a third server group with at least one node that will allow the remaining nodes to form a quorum. The node in the third server group can be an [arbiter node](nodes.md#adding-arbiter-nodes), a type of node introduced in 7.6 Server that does not run any services and only exists to allow forming a quorum.

See [Automatic Failover](automatic-failover.md). See [Adding Arbiter Nodes](nodes.md#adding-arbiter-nodes) for more information on the use of arbiter nodes for [fast failover](nodes.md#fast-failover) and [quorum arbitration](#install:deployment-considerations-lt-3nodes.html#quorum-arbitration).

Groups should be defined in accordance with the physical distribution of cluster-nodes. For example, a group should only include the nodes that are in a single _server rack_, or in the case of cloud deployments, a single _availability zone_. Thus, if the server rack or availability zone becomes unavailable due to a power or network failure, all the nodes in the group can be automatically failed over, to allow continued access to the affected data.

Note the following:

* Server Group Awareness is only available in Couchbase Server Enterprise Edition.
* Server Group Awareness only applies to the Data and Index Services.
* When a new Couchbase Server cluster is initialized, and no server groups are explicitly defined, the first node, and all subsequently added nodes, are automatically placed in a server group named Group 1\. Once additional server groups are created, a destination server group must be specified for every node that is subsequently added to the cluster.

For information on failover, see [Failover and Rebalance](../../manage/manage-nodes/fail-nodes-over.md). For information on vBuckets, see [Buckets](../buckets-memory-and-storage/buckets.md). For information on the standard (non-Group-based) distribution of replica vBuckets across a cluster, see [Availability](replication-architecture.md).

## [](#server-groups-and-vbuckets)Server Groups and vBuckets

The distribution of vBuckets across groups is exemplified below. In each illustration, all servers are assumed to be running the Data Service, except for the arbiter node server, which does not run any service.

### [](#vbucket-distribution-across-equal-groups)Equal Groups

The following illustration shows how vBuckets are distributed across two groups; each group containing four of the cluster's nodes. The third group only contains one node, an arbiter node, which exists to allow a quorum to be formed if all the nodes in server group 1 or 2 fails.

![groups two equal updated](../_images/clusters-and-availability/groups-two-equal_updated.png) 

Note that Group 2 contains all the replica vBuckets that correspond to active vBuckets on Group 1; while conversely, Group 1 contains all the replica vBuckets that correspond to active vBuckets on Group 2.

Note also that for auto-failover of Group 1 or Group 2 nodes to be possible, the auto-failover majority quorum requirement must be met. Therefore, a third server group is always recommended, and it can include a single [arbiter node](nodes.md#adding-arbiter-nodes) that is not running any services.

### [](#unequal-groups)Unequal Groups

A number of constraints come into play when allocating active and replica vBuckets across server groups:

| **rack-zone**       | all replicas of a given vBucket must reside in separate server groups.                         |
| ------------------- | ---------------------------------------------------------------------------------------------- |
| **active balance**  | there should be approximately the same number of active vBuckets on each node in the cluster.  |
| **replica balance** | there should be approximately the same number of replica vBuckets on each node in the cluster. |

Not all the constraints can be satisfied when the buckets are allocated across uneven groups. In this scenario, the `active balance` and `rack-zone` constraints will take priority: when the vBucket map is generated, we will ensure that there are approximately the same number of active vBuckets on each node in the cluster and that replicas of a given vBucket must reside in separate groups.

The following illustration shows how vBuckets are distributed across two groups: Group 1 contains four nodes, while Group 2 contains five.

![groups two unequal rack zone constraint](../_images/clusters-and-availability/groups-two-unequal-rack-zone-constraint.png) 

Group 1 contains all the replica vBuckets that correspond to active vBuckets in Group 2.

Group 2 contains all the replica vBuckets that correspond to active vBuckets in Group 1.

However, in order to ensure that replicas of a VBucket must reside in a separate group, then we may have a situation where there are vBuckets from Server 9 replicated to Group 1, but there are no additional vBuckets in Group 1 to provide balance in Group 2.

> [!IMPORTANT]
> Smaller server groups will carry more replica vBuckets, which means there is greater memory pressure on memcached so more fetches go to disk which means higher worst case GET latencies.
> 
> Additionally, more replicas mean more writes to disk and a greater compaction burden which will also affect latencies.
> 
> Customers will notice this as the smaller server groups will "perform" worse than the later server groups. So for reasons of consistency of performance Couchbase strongly recommends that customers endeavor to maintain an equal number of nodes across server groups.

For more information on optimizing your cluster configuration, consult the [Sizing Guidelines](../../install/sizing-general.md).

### [](#node-failover-across-groups)Node-Failover Across Groups

When an individual node within a group goes offline, rebalance provides a _best effort_ redistribution of replica vBuckets. This keeps all data available, but results in some data being no longer protected by the Groups mechanism. This is shown by the following illustration, in which Server 2, in Group 1, has gone offline, and a rebalance and failover have occurred.

![groups two failover one node](../_images/clusters-and-availability/groups-two-failover-one-node.png) 

With the active vBuckets on Server 2 no longer accessible, the replica vBuckets for Server 2 have been promoted to active status, on the servers of Group 2\. The data originally active on Server 2 is thereby kept available. Note, however, that if Group 2 were now to go offline, the data originally active on Server 2 would be lost, since it now exists only on Group 2 servers.

## [](#server-groups-and-indexes)Server Groups and Indexes

Indexes and index replicas can only be located on nodes that run the Index Service.

As described in [Index Replication](../services-and-indexes/indexes/index-replication.md#index-replication), the Index Service allows index replicas to be defined in either of two ways:

* By establishing the number of replicas required, for a given index, without the actual node-locations of the replicas being specified. This is itself accomplished in either of the following ways:

  * By providing, as the argument to the `WITH` clause, the `num_replica` key, with an accompanying integer that is the desired number of replicas.
  * By specifying the number of index-replicas to be created by the Index Service whenever `CREATE INDEX` is invoked.
* By establishing the number of replicas required, for a given index, with the actual node-locations for the index itself and each of its replicas being specified. This is accomplished by providing, as the argument to the `WITH` clause, an array of nodes.

Examples of these different forms of replica-definition are provided in [Index Replication](../services-and-indexes/indexes/index-replication.md#index-replication).

If the node-locations for index and replicas _are_ specified, by means of the `WITH` clause and node-array, this user-defined topology is duly followed in the locating of index and replicas across the cluster, and any server groups that may have been defined. In this case, it is the administrator's responsibility to ensure that optimal index-availability has been achieved, so as to handle possible instances of node or group failure.

If the node-locations for index and replicas are _not_ specified, the node-locations are automatically provided by Couchbase Server, based on its own estimates of how to provide the highest index-availability. Such distributions are exemplified as follows.

### [](#optimal-distribution)Optimal Distribution

When the number of index replicas created for a given index is at least one less than the total number of groups for the cluster, and each group contains sufficient nodes running the Index Server, automatic distribution ensures that each index and index replica resides on its own group. (Indexes and index replicas always exist each on their own Index Server node, with index-creation failing if there is an insufficiency of such nodes to accommodate the specified number of index replicas — see [Index Replication](../services-and-indexes/indexes/index-replication.md#index-replication).)

For example:

![groups indexes two equal](../_images/clusters-and-availability/groups-indexes-two-equal.png) 

Here, two groups have been defined. Each group contains one Index Server node. Two indexes have been defined, each with one index replica. Therefore, automatic distribution has assigned both indexes to the Index Server node in group 1, and both index replicas to the Index Server node in group 2\. This ensures that, should either group become inaccessible, the surviving group continues to bear an instance of the Index Server, with both indexes thus available.

Note that an alternative outcome to the automatic distribution would have been for each index to be assigned to a different group, and each index replica to be assigned to the group on which its corresponding index did _not_ reside.

### [](#best-effort-distribution)Best-Effort Distribution

When the number of index replicas created for a given index is not at least one less than the total number of groups for the cluster, but the cluster bears enough Index Server nodes to accommodate all defined indexes and index replicas, automatic distribution produces an outcome based on _best effort_. For example:

![groups indexes three unequal 1](../_images/clusters-and-availability/groups-indexes-three-unequal-1.png) 

Here, again, two groups have been defined. Each group now contains two Index Server nodes. Two indexes have been defined: one with two index replicas, the other with one. Automatic distribution has assigned each index to its own node in Group 1; and has assigned, for each index, a corresponding index replica to its own node in Group 2\. However, since one index has _two_ replicas defined, the second of these has been assigned to the second Index Server node in Group 1\. Consequently, an index and one of its replicas have both been assigned to the same group; and will both be lost, in the event of that group becoming inaccessible.

Note that an alternative outcome to the automatic distribution would have been for the second index replica to be assigned to Server 8, in Group 2\. Consequently, both the index replicas of one index would be assigned to the same group; and both would be lost, in the event of that group becoming inaccessible.

## [](#adding-multiple-groups)Adding Multiple Groups

When multiple groups are to be added to a cluster simultaneously, the additions should all be executed on a _single node_ of the cluster: this simplifies the reconfiguration process, and so protects against error.

## [](#group-failover-and-service-availability)Group Failover and Service Availability

When groups are defined to correspond to racks or availability zones, all services required for data access — such as the Index Service and the Search Service — should be deployed so as to ensure their own continued availability, during the outage of a rack or zone.

For example, given a cluster:

* Whose Data Service deployment supports two Server Groups, each corresponding to one of two racks
* Whose data must be continuously accessed by the Index and Search Services

At a minimum, one instance of the Index Service and one instance of the Search Service should be deployed on each rack.

Also, for auto-failover to be possible, the service-specific auto-failover constraints must be met — the policy information is documented in [Service-Specific Auto-Failover Policy](automatic-failover.md#failover-policy) — it lists the number of nodes that each service must be running on and explains the [Data Service Preference](automatic-failover.md#data-service-preference) when a service is co-located with the Data Service.

## [](#defining-groups-and-enabling-group-failover)Defining Groups and Enabling Failover of All a Group's Nodes

To define and manage groups:

* With Couchbase Web Console, see [Manage Groups](../../manage/manage-groups/manage-groups.md).
* With CLI, see [group-manage](../../cli/cbcli/couchbase-cli-group-manage.md).
* With the REST API, see [Server Groups API](../../rest-api/rest-rza.md).

To enable the failover of all nodes in a group:

* With Couchbase Web Console, see the information provided for the **General** settings panel, in [Node Availability](../../manage/manage-settings/general-settings.md#node-availability).
* With CLI, see [setting-autofailover](../../cli/cbcli/couchbase-cli-setting-autofailover.md).
* With the REST API, see [Enabling and Disabling Auto-Failover](../../rest-api/rest-cluster-autofailover-enable.md).