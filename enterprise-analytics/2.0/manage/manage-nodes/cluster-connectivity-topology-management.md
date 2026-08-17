---
title: Cluster Addressing and Topology Management
description: ""
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/manage/pages/manage-nodes/cluster-connectivity-topology-management.adoc
  xref: xref:2.0@enterprise-analytics:manage:manage-nodes/cluster-connectivity-topology-management.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/manage/manage-nodes/cluster-connectivity-topology-management.html)

# Cluster Addressing and Topology Management

This section describes the addressing models supported by the Analytics SDKs for access to Enterprise Analytics clusters, outlines pros and cons for each, and provides best-practice operational procedures for handling cluster topology changes such as adding or removing nodes. It also covers configuration settings that can help ensure smooth failover and rebalance operations.

## [](#analytics-sdk-addressing-methods)Analytics SDK Addressing Methods

Enterprise Analytics supports three primary ways for client applications to connect to a cluster:

### [](#active-load-balancer)Active Load Balancer

A Layer-7 load balancer actively probes the health of Enterprise Analytics nodes and routes traffic only to healthy nodes. Clients resolve a DNS hostname that maps to one or more load balancer nodes via A records.

#### [](#example-sdk-connection-string)Example SDK Connection String

```none
https://ea-cluster.example.com
```

> [!NOTE]
> * Recommended to configure load balancer listeners on `:80` for HTTP and `:443` for HTTPS, so SDK clients can omit the port in the connection string.
> * The `ea-cluster.example.com` hostname should resolve only to the load balancer VIP (or redundant IPs), not directly to backend node IPs.
> * In the event [legacy SDK connectivity](#legacy-sdks) is required, compatible access to the cluster (exposing memcached ports for all nodes) will also need to be provided.

#### [](#pros)Pros

* Timely remove of a failed nodes due to active health checks
* Reduced burden on admins to manually manage node availability, thanks to active health checks
* Can be made highly available with multiple load balancer instances
* Can perform SSL offloading (if desired)

#### [](#cons)Cons

* Requires additional infrastructure (load balancer instances, configuration, maintenance)
* Potential single point of failure if load balancer itself is not highly available
* Misconfigured health checks can cause false positives or delayed failover

### [](#passive-load-balancer)Passive Load Balancer

A Layer-4 or TCP-level load balancer that distributes connections without actively probing node health. Failover is handled by connection retries from the client until manual intervention. Clients resolve a DNS hostname that maps to one or more load balancer nodes via A records.

#### [](#example-sdk-connection-string-2)Example SDK connection string

```none
https://ea-cluster.example.com
```

> [!NOTE]
> * As with Active Load Balancer, `:80` or `:443` recommended for default SDK behavior.
> * The `ea-cluster.example.com` hostname should resolve only to the load balancer VIP (or redundant IPs), not directly to backend node IPs.
> * In the event [legacy SDK connectivity](#legacy-sdks) is required, compatible access to the cluster (exposing memcached ports for all nodes) will also need to be provided.

#### [](#pros-2)Pros

* Simple configuration
* Can be made highly available with multiple load balancer instances

#### [](#cons-2)Cons

* Less responsive to node failures
* May continue sending traffic to unhealthy nodes for an extended period- until TCP connections fail or load balancer configuration updated
* Potential single point of failure if load balancer itself is not highly available
* In addition to reduced failover recovery, rebalance out (scale-in) operations must remove exiting nodes manually from the load balancer pool prior to starting the rebalance operation to avoid client errors

### [](#dns-only)DNS-Only

Clients resolve a DNS hostname that resolves configured cluster nodes via multiple A records. The number of A records may need to be limited to enable reliable DNS resolution, limiting the number of nodes the application can contact.

#### [](#example-sdk-connection-string-3)Example SDK connection string

```none
https://<dns hostname>:18095
```

> [!NOTE]
> Enterprise Analytics nodes listen on `:8095` for HTTP and `:18095` for HTTPS.

#### [](#pros-3)Pros

* No additional infrastructure
* Simple to set up if DNS is already managed centrally

#### [](#cons-3)Cons

* DNS caching means changes, for example, node removal, are not immediately effective — must wait for TTL expiry.
* Client behavior varies — some cache DNS results for longer than TTL.
* Some DNS servers struggle with very large record sets, which may occur if the cluster has many nodes, either mandating a load balancer or limiting the number of nodes that can be addressed.
* No active health probing — clients will continue to route requests to unhealthy nodes until manually removed from DNS, subject to any failure circuit-breaker logic within the SDK clients.

## [](#configuration)Configuration

### [](#load-balancer-and-dns-configuration-recommendations)Load Balancer and DNS Configuration Recommendations

#### [](#active-load-balancer-2)Active Load Balancer

* Configure health check interval and unhealthy threshold to detect node failures quickly without false positives, and coordinate the settings with the `rebalanceEjectDelaySeconds` setting ([details](#rebalanceEjectDelaySeconds)) on the Enterprise Analytics cluster.
* Prefer **Fail-Closed** behavior after an unhealthy threshold is reached to avoid sending requests to unstable (failed-over or rebalanced-out) nodes.
* If supported by the load balancer, enable **Connection Draining** to allow in-flight requests to complete before closing backend connections.
* Ensure DNS hostname resolves only to load balancer VIPs, not directly to backend node IPs.

#### [](#passive-load-balancer-2)Passive Load Balancer

* Keep health checks disabled (by design) and rely on application retries for failover.
* Use fail-closed routing once a backend connection fails (e.g., TCP connection refused) to minimize latency spikes.
* If supported, configure short TCP connection timeouts to fail quickly.
* Ensure DNS hostname resolves only to load balancer VIPs.

#### [](#dns-only-2)DNS-Only

* Keep DNS TTLs low enough to allow timely failover (e.g., ≤ 30 seconds if possible).
* Update DNS A records promptly when adding or removing nodes.
* Avoid CNAME chains when possible, as they can add unpredictable TTL behavior.
* Configure clients to honor DNS TTL and retry failed connections on alternate IPs.

### [](#relevant-enterprise-analytics-settings)Relevant Enterprise Analytics Settings

There are several settings that should be configured in accordance with your selected addressing model, and the configuration of your environment.

These settings are primarily related to the rebalance & failover operations, and should be configured to correspond with your addressing mode and configuration.

| Property                                    | Description                                                                                                                                                                                                            | Default |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| rebalanceEjectDelaySeconds                  | The minimum time (in seconds) a node will continue to accept requests once a rebalance out for the node has been initiated. The Health Check API will report 503 on ejecting nodes during this period. (0 \= disabled) | 0       |
| cloudAccessPreemptiveRefreshIntervalSeconds | Interval at which to preemptively verify cloud storage access. If access is revoked, halts immediately. (0 \= disabled)                                                                                                | 15      |
| cloudAccessRefreshHaltTimeoutSeconds        | Maximum time to wait for verification before halting. (0 \= wait forever)                                                                                                                                              | 120     |

This check is in addition to access checks performed before writes. It allows detection of unhealthy nodes even if no writes are occurring.

### [](#configuring-rebalanceejectdelayseconds)Configuring `rebalanceEjectDelaySeconds`

The `rebalanceEjectDelaySeconds` setting controls the minimum delay (in seconds) before a node is ejected from the cluster during rebalance out. This delay ensures clients and load balancers have adequate time to stop routing traffic to the node, minimizing failures during topology changes.

Configure `rebalanceEjectDelaySeconds` according to your cluster's addressing method:

#### [](#active-load-balancer-3)Active Load Balancer

Set to at least `load balancer health check interval × (load balancer unhealthy threshold + 1)`This accounts for the time needed by the load balancer to detect the node as unhealthy and stop routing requests before the node is removed.

> [!NOTE]
> The extra `+1` ensures worst-case timing when the health check just occurred before the node starts returning `503`.

#### [](#passive-load-balancer-3)Passive Load Balancer

Can be set to `0` (disabled), since passive load balancers do not actively probe node health. This allows rebalance operations to proceed with minimal delay.

#### [](#dns-only-3)DNS-Only

Set to at least `DNS TTL (Time-to-Live) × 2`

This accounts for DNS caching behavior, ensuring clients have sufficient time to expire cached IP addresses of the removed node before it is ejected.

Adjust this setting carefully to align with your environment's load balancer polling intervals, DNS TTL values, and client caching behavior to minimize disruption.

## [](#topology-change-procedures)Topology Change Procedures

This section describes the recommended procedures for adding or removing nodes from an Enterprise Analytics cluster, based on the addressing model in use.

### [](#rebalance-in-scale-out)Rebalance In (Scale-Out)

A rebalance in operation is used to add one or more nodes to the Enterprise Analytics cluster. This is typically done when scaling-out, during upgrade, or when replacing nodes.

#### [](#active-load-balancer-4)Active Load Balancer

1. Ensure joining node is added to the load balancer backend pool.
2. Add node to Enterprise Analytics cluster & initiate rebalance.
3. load balancer health checks monitor node readiness and start routing only after health check returns `204`.

#### [](#passive-load-balancer-4)Passive Load Balancer

1. Add node to Enterprise Analytics cluster & initiate rebalance.
2. Wait for rebalance completion.
3. Add node to load balancer backend pool.

#### [](#dns-only-4)DNS-Only

1. Add node to Enterprise Analytics cluster & initiate rebalance.
2. Wait for rebalance completion.
3. Add node's IP to DNS A records.
4. It may take up to DNS TTL seconds for client applications to start to use new node.

> [!NOTE]
> All mentions of "node" in this section can refer to any quantity of nodes being added in the rebalance operation.

### [](#rebalance-out-scale-in)Rebalance Out (Scale-In)

A rebalance out operation is used to remove one or more nodes from the Enterprise Analytics cluster. This is typically done when scaling-in, during upgrade, or when replacing nodes.

#### [](#active-load-balancer-5)Active Load Balancer

1. Start rebalance out.
2. Node will remain usable for a minimum of `rebalanceEjectDelaySeconds` ([details](#rebalanceEjectDelaySeconds)).
3. Node terminates upon rebalance completion.
4. Remove node from load balancer backend pool if not intended to be added back later.

#### [](#passive-load-balancer-5)Passive Load Balancer

1. Remove node from load balancer backend pool.
2. Start rebalance out.
3. Node will remain usable for a minimum of `rebalanceEjectDelaySeconds` ([details](#rebalanceEjectDelaySeconds)).
4. Node terminates upon rebalance completion.

#### [](#dns-only-5)DNS-Only

1. Remove node's IP from DNS A records.
2. Start rebalance out.
3. Node will remain usable for a minimum of `rebalanceEjectDelaySeconds` ([details](#rebalanceEjectDelaySeconds)).
4. Node terminates upon rebalance completion.

> [!NOTE]
> All mentions of "node" in this section can refer to any quantity of nodes being removed in the rebalance operation.
> 
> The rebalance process respects active connections and allows them to complete gracefully, so no additional wait is required after removing the node from the load balancer pool.

### [](#failover-node-reachable-by-quorum)Failover - Node Reachable by Quorum

Failover Procedures by Addressing Model

#### [](#active-load-balancer-6)Active Load Balancer

1. Node is automatically or manually failed over.
2. Node terminates, responsibilities from the failed node is transferred to surviving nodes.
3. Once failed health check thresholds are met, load balancer stops routing traffic to the failed node.
4. Remove node from load balancer backend pool unless it is being added back to the cluster.

> [!NOTE]
> * Until the failed health check thresholds are met and the load balancer removes the failed node from the backend pool, any requests that are routed to the failed node will get connection refused.
> * Running queries involving the failed node will fail upon node failover. Note that most queries utilize all nodes on the cluster, and therefore will fail on the failover.

#### [](#passive-load-balancer-6)Passive Load Balancer

1. Node is automatically or manually failed over.
2. Node terminates, responsibilities from the failed node is transferred to surviving nodes.
3. Requests routed to the failed node will get connection refused, which will trigger the load balancer to remove the node from the active backend pool.
4. Remove node from load balancer backend pool unless it is being added back to the cluster.

> [!NOTE]
> * Depending on the specific load balancer and its configuration, some client requests may experience errors (e.g. `503`) for requests that get routed to the failed node, until the load balancer removes the node from the active backend pool. Other configurations may retry the refused connections on another node.
> * Running queries involving the failed node will fail upon node failover. Note that most queries utilize all nodes on the cluster, and therefore will fail on the failover.

#### [](#dns-only-6)DNS-Only

1. Node is automatically or manually failed over.
2. Node terminates, responsibilities from the failed node is transferred to surviving nodes.
3. Requests routed to the failed node will get connection refused, which will trigger the SDK to retry another IP in the DNS record.
4. Remove the node's IP from the DNS record unless it is being added back to the cluster.

### [](#failover-node-unreachable-by-quorum-e-g-network-partition)Failover - Node Unreachable by Quorum (e.g. Network Partition)

Failover Procedures by Addressing Model

#### [](#active-load-balancer-7)Active Load Balancer

1. Node is automatically or manually failed over.
2. Responsibilities of the failed node are transferred to surviving nodes.
3. The failed nodes will continue to accept load balancer connections until it realizes it has been failed over. This can take up to:

  1. `cloudAccessPreemptiveRefreshIntervalSeconds` if the node is still able to access cloud storage, or…​
  2. up to `cloudAccessRefreshHaltTimeoutSeconds` if it is not.
4. Once the node stops accepting connections, load balancer health checks will start failing against that node.
5. Once failed health check thresholds are met, load balancer stops routing traffic to the failed node.
6. Remove node from load balancer backend pool unless it is being added back to the cluster.

> [!NOTE]
> * Running queries involving the failed node will fail upon node failover. Note that most queries utilize all nodes on the cluster, and therefore will fail on the failover.
> * Requests accepted by the failed node before it realizes it has been failed over will fail. Depending on the specifics of the network partition, this can include `503` errors, or requests that will timeout or abort once the node terminates.

#### [](#passive-load-balancer-7)Passive Load Balancer

1. Node is automatically or manually failed over.
2. Responsibilities of the failed node are transferred to surviving nodes.
3. The failed nodes will continue to accept load balancer connections until it realizes it has been failed over. This can take up to:

  1. `cloudAccessPreemptiveRefreshIntervalSeconds` if the node is still able to access cloud storage, or…​
  2. up to `cloudAccessRefreshHaltTimeoutSeconds` if it is not.
4. Requests routed to the failed node will then get connection refused, which will trigger the load balancer to remove the node from the active backend pool.
5. Remove node from load balancer backend pool unless it is being added back to the cluster.

> [!NOTE]
> * Depending on the specific load balancer and its configuration, some client requests may experience errors (e.g. `503`) for requests that get routed to the failed node, until the load balancer removes the node from the active backend pool. Other configurations may retry the refused connections on another node.
> * Running queries involving the failed node will fail upon node failover. Note that most queries utilize all nodes on the cluster, and therefore will fail on the failover.
> * Requests accepted by the failed node before it realizes it has been failed over will fail. Depending on the specifics of the network partition, this can include `503` errors, or requests that will timeout or abort once the node terminates.

#### [](#dns-only-7)DNS-Only

1. Node is automatically or manually failed over.
2. Responsibilities of the failed node are transferred to surviving nodes.
3. The failed nodes will continue to accept load balancer connections until it realizes it has been failed over. This can take up to:

  1. `cloudAccessPreemptiveRefreshIntervalSeconds` if the node is still able to access cloud storage, or…​
  2. up to `cloudAccessRefreshHaltTimeoutSeconds` if it is not.
4. Requests routed to the failed node will get connection refused, which will trigger the SDK to retry another IP in the DNS record.
5. Remove the node's IP from the DNS record unless it is being added back to the cluster.

> [!NOTE]
> * Running queries involving the failed node will fail upon node failover. Most queries utilize all nodes on the cluster, and therefore will fail on the failover.
> * Requests accepted by the failed node before it realizes it has been failed over will fail. Depending on the specifics of the network partition, this can include `503` errors, or requests that will timeout or abort once the node terminates.

## [](#recommendations)Recommendations

* Prefer Active Load Balancer in production for fastest and most reliable failover behavior.
* Set load balancer listeners on `:80` / `:443` for HTTP/HTTPS to simplify SDK connection strings.
* Always coordinate `rebalanceEjectDelaySeconds` with load balancer health check configuration.
* For DNS-only deployments, keep TTL short (e.g., 30–60 seconds) to minimize client exposure to outdated records.

## [](#legacy-sdks)Connectivity for Connectors Based on Legacy SDKs

Some connectors compatible with Enterprise Analytics clusters are based on legacy SDKs and are not directly compatible with the new addressing architecture described above. These include:

1. Tableau Connector
2. Power BI Connector
3. Apache Superset Connector

These connectors utilize legacy Couchbase SDKs which require the ability to directly connect to services (e.g., data service for cluster topology bootstrap and monitoring, and Enterprise Analytics service to issue queries) on all cluster nodes. To configure access to an Enterprise Analytics cluster, steps must be followed based on the addressing method selected for Analytics SDK access.

### [](#active-load-balancer-8)Active Load Balancer

An Active Load Balancer setup, which performs Layer-7 (HTTP/HTTPS) routing for Enterprise Analytics APIs, can have a complimentary Layer-4 (TCP) load balancer configured on the same or different hosts to enable access from legacy SDKs. This Layer-4 load balancer can be configured for legacy SDK access as described [here](#legacy-sdks-passive-lb).

> [!NOTE]
> Colocating the Layer-4 load balancer on the same hosts as the Layer-7 load balancer is recommended to simplify connection string management. Given a DNS-name of `ea-cluster.example.com`, the connection strings for secure (TLS) access would be as follows:
> 
> * Analytics SDKs: `<https://ea-cluster.example.com>`+
> * Legacy SDKs: `couchbases://ea-cluster.example.com`
> 
> Otherwise, use the corresponding DNS name of the Layer-4 load balancer for the legacy SDK usages.

### [](#legacy-sdks-passive-lb)Passive Load Balancer

The Layer-4 load balancer should be configured to forward TCP connections on the standard Couchbase service ports required by the legacy SDKs:

* `8091`/`18091` (Cluster management service, non-SSL/SSL)
* `8095`/`18095` (Analytics service, non-SSL/SSL)
* `11210`/`11207` (Data service, non-SSL/SSL)

The legacy SDKs require the ability to contact all nodes in the Enterprise Analytics cluster on the above ports.

The simplest way to achieve this is to allow the SDK applications to address the individual cluster nodes directly at their configured hostnames and ports. Otherwise, alternate address configuration must be used to allow the legacy SDKs to know how to connect to the services on individual nodes.

#### [](#alternate-address-configuration)Alternate Address Configuration

The Layer-4 load balancer can be configured with ports which route to the above ports on individual Enterprise Analytics nodes. These services need to be configured as alternate addresses in the cluster to enable the legacy SDKs to know how to connect to them.

See [Managing Alternate Addresses](../../reference/rest-set-up-alternate-address.md) for more info.

### [](#dns-only-8)DNS-Only

As with the Active Load Balancer recommended setup, given a DNS-name of `ea-cluster.example.com`, the connection strings for secure (TLS) access would be as follows:

* Analytics SDKs: `<https://ea-cluster.example.com>`+
* Legacy SDKs: `couchbases://ea-cluster.example.com`

The legacy SDKs require the ability to contact all nodes in the Enterprise Analytics cluster on the service ports listed in the above [Passive Load Balancer](#legacy-sdks-passive-lb) section.

The simplest way to achieve this is to allow the SDK applications to address the individual cluster nodes directly at their configured hostnames and ports. Otherwise, alternate address configuration must be used to allow the legacy SDKs to know how to connect to the services on individual nodes.

#### [](#alternate-address-configuration-2)Alternate Address Configuration

If the legacy SDK need to connect to the services on the individual nodes on an IP or hostname different from the one configured on the node, these services need to be configured as alternate addresses.

See [Managing Alternate Addresses](../../reference/rest-set-up-alternate-address.md) for more info.