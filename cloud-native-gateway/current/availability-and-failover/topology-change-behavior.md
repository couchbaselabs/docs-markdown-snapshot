---
title: Topology Change Behavior
description: How Cloud Native Gateway handles cluster topology changes including
  rebalances, failovers, node additions, and service configuration changes,
  transparently to client applications.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/availability-and-failover/pages/topology-change-behavior.adoc
  xref: xref:cloud-native-gateway:availability-and-failover:topology-change-behavior.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/availability-and-failover/topology-change-behavior.html)

# Topology Change Behavior

> How Cloud Native Gateway handles cluster topology changes including rebalances, failovers, node additions, and service configuration changes, transparently to client applications. 

## [](#rebalance)Rebalance

Rebalance is the most common topology change in Couchbase Server. It redistributes data (vBuckets) across nodes when nodes are added, removed, or when data distribution needs to be equalized.

### [](#cloud-native-gateway-behavior-during-rebalance)Cloud Native Gateway Behavior During Rebalance

1. **Configuration updates** \- Cloud Native Gateway receives updated cluster configurations as the rebalance progresses. These updates include the evolving vBucket map.
2. **vBucket migration handling** \- During rebalance, vBuckets are moved between nodes. When Cloud Native Gateway sends a KV request to a node that no longer owns the target vBucket, the node responds with `NOT_MY_VBUCKET`. Cloud Native Gateway's IO layer handles this by:

  * Updating the local vBucket map with the information from the `NOT_MY_VBUCKET` response.
  * Retrying the request against the correct node.
  * This retry is invisible to the client.
3. **Connection management** \- Cloud Native Gateway establishes connections to new nodes as they appear in the configuration and gracefully closes connections to removed nodes after the rebalance completes.
4. **Service endpoint updates** \- As nodes with Query, Search, or Analytics services are added or removed, Cloud Native Gateway updates its endpoint lists accordingly.

### [](#client-impact)Client Impact

Clients experience **no disruption** during a rebalance when using Cloud Native Gateway. The Cloud Native Gateway layer absorbs the complexity of vBucket migration, temporary routing misses, and endpoint changes. Clients may experience slightly elevated latency for KV operations that hit a migrating vBucket (due to the retry), but this is typically not noticeable.

This is a significant advantage over direct SDK connections, where the SDK must handle `NOT_MY_VBUCKET` responses, update its own vBucket map, and potentially reconnect to new nodes.

## [](#failover)Failover

Failover is a critical topology change that occurs when a node becomes unavailable or is manually removed from the cluster. Cloud Native Gateway handles both automatic and manual failover scenarios transparently, ensuring minimal client disruption.

### [](#auto-failover)Auto-Failover

When Couchbase Server detects a node failure and triggers auto-failover:

1. The failed node is removed from the cluster topology.
2. Replica vBuckets on surviving nodes are promoted to active.
3. Cloud Native Gateway receives the updated configuration with the new vBucket map.
4. Cloud Native Gateway stops routing requests to the failed node.
5. Subsequent requests are routed to the nodes that now own the promoted vBuckets.

The failover window — the time between the node failure and Cloud Native Gateway receiving the updated configuration — may result in some requests failing or experiencing timeouts. Cloud Native Gateway will retry eligible operations automatically.

### [](#hard-failover)Hard Failover

Hard failover (manual or automatic) works the same as auto-failover from Cloud Native Gateway's perspective. The key difference is that data on the failed node that was not yet replicated may be lost. Cloud Native Gateway does not influence data durability - this is determined by the Couchbase Server durability settings on each operation.

### [](#graceful-failover)Graceful Failover

Graceful failover synchronizes all data from the node being removed before completing the failover. From Cloud Native Gateway's perspective, this looks like a rebalance followed by the node's removal. There is no data loss and minimal client impact.

## [](#node-addition)Node Addition

When a new Couchbase Server node is added to the cluster (before rebalance):

1. Cloud Native Gateway detects the new node in the cluster configuration and establishes connections to the new node's services.
2. The new node does not yet own any vBuckets, so no KV traffic is routed to it.
3. Once a rebalance is triggered, vBuckets are migrated to the new node and Cloud Native Gateway begins routing traffic to it.

## [](#service-configuration-changes)Service Configuration Changes

When the services running on a node change (e.g., adding the Query Service to a node that previously only ran KV):

1. Cloud Native Gateway receives the updated cluster configuration listing the new service endpoints and adds the new endpoint to its service routing table.
2. Subsequent requests to that service type may be routed to the newly available endpoint.

## [](#routing-updates-to-clients)Routing Updates to Clients

If clients have subscribed to routing updates via the `WatchRouting` RPC:

* Cloud Native Gateway emits a new `WatchRoutingResponse` message on the stream whenever the cluster topology changes.
* The response includes updated service routing information (number of local and group servers per service) and vBucket routing data (if a bucket was specified).
* Clients can use this information for client-side optimizations such as zone-aware load balancing, but it is not required for correct operation.

## [](#transparent-topology-changes-a-key-benefit)Transparent Topology Changes: A Key Benefit

One of the fundamental design goals of Cloud Native Gateway is to make topology changes invisible to client applications. In the traditional SDK model, clients must understand and react to topology changes: they receive `NOT_MY_VBUCKET` errors, must parse new cluster maps, and may need to establish new connections.

With Cloud Native Gateway, the client's view is a stable, single gRPC endpoint. All of the following topology changes are handled transparently by Cloud Native Gateway:

* Node additions and removals
* Rebalances
* Failovers (auto and manual)
* Service scaling (adding/removing Query, Search, or Analytics services)
* Server upgrades (rolling restart with Cloud Native Gateway handling the transient unavailability of individual nodes)

This enables Couchbase deployments to perform operational changes — including infrastructure-level changes like moving a bucket between clusters — with zero client-side impact, as long as the Cloud Native Gateway endpoint remains reachable.