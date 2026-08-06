---
title: Network Flow and Connectivity
description: How requests flow from client applications through Cloud Native
  Gateway to Couchbase Server services, including request routing, topology
  awareness, and metadata propagation.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/architecture/pages/network-flow-connectivity.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:architecture:network-flow-connectivity.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/architecture/network-flow-connectivity.html)

# Network Flow and Connectivity

> How requests flow from client applications through Cloud Native Gateway to Couchbase Server services, including request routing, topology awareness, and metadata propagation. 

## [](#client-to-gateway-to-cluster-communication)Client to Gateway to Cluster Communication

The request lifecycle in a Cloud Native Gateway deployment follows a three-tier path: client application, Cloud Native Gateway, and Couchbase Server.

### [](#inbound-client-to-cloud-native-gateway)Inbound: Client to Cloud Native Gateway

Client applications connect to Cloud Native Gateway over 1 of 2 interfaces:

* **Protostellar (gRPC)** \- Couchbase SDKs using the `couchbase2://` connection scheme establish a TLS-encrypted gRPC (HTTP/2) connection to Cloud Native Gateway's data port (default 18098). HTTP/2 streams multiplex multiple concurrent requests over this single connection. Clients send authentication credentials as gRPC metadata (the `Authorization` header) with every request.
* **Data API (HTTPS)** \- HTTP clients connect to Cloud Native Gateway's Data API port over TLS. Each HTTP request is independent and carries authentication in the `Authorization` header. The Data API supports keep-alive connections for connection reuse.

Both interfaces require TLS. Cloud Native Gateway supports dynamic certificate rotation - you can update certificates at runtime without restarting the gateway.

### [](#internal-cloud-native-gateway-to-couchbase-server)Internal: Cloud Native Gateway to Couchbase Server

Cloud Native Gateway maintains persistent connections to the Couchbase cluster:

* **KV (Data) connections** \- A pool of persistent TCP connections using the Memcached binary protocol, maintained to each data node. The default pool size is 8 connections per data node. These connections use the credentials from requests over multiplexed request/response pairs for efficiency.
* **HTTP connections** \- Standard HTTP/1.1 connections (or HTTP/2 when available) to Query, Search, Analytics, and Management service endpoints. These use connection pooling with idle timeout management (default 90-second idle timeout).
* **Management connections** \- Used for cluster configuration polling, cbauth registration, and administrative API calls. Cloud Native Gateway maintains a separate HTTP transport for startup management operations.

Cloud Native Gateway discovers all service endpoints through the cluster configuration API. It automatically updates its connection topology when you add, remove or rebalance nodes. When you configure TLS between Cloud Native Gateway and the cluster using the `couchbases://` scheme, it encrypts all internal connections with the cluster's CA certificate.

## [](#service-level-request-routing)Service Level Request Routing

Cloud Native Gateway routes each incoming request to the appropriate backend service based on the gRPC service and method (for Protostellar) or the URL path (for Data API).

### [](#kv-request-routing)KV Request Routing

KV operations require routing to a specific data node based on the document key:

1. Cloud Native Gateway routes each incoming request to the appropriate backend service based on the gRPC service and method (for Protostellar) or the URL path (for Data API).
2. Cloud Native Gateway hashes the document key to determine the vBucket number.
3. Cloud Native Gateway consults the current vBucket map to identify which data node owns that vBucket.
4. Cloud Native Gateway dispatches the request to the owning node through a Memcached binary protocol connection pool.
5. If the vBucket map changes during operation (due to a rebalance), Cloud Native Gateway receives a `NOT_MY_VBUCKET` response and retries the request against the correct node using the updated map.

For replica read operations like `GetAllReplicas` or `GetAnyReplica`, Cloud Native Gateway sends requests to active and replica nodes and returns results as they arrive.

### [](#query-search-and-analytics-routing)Query, Search, and Analytics Routing

Cloud Native Gateway accesses these services via HTTP from the cluster:

* Cloud Native Gateway selects an appropriate service endpoint from its discovered endpoint list.
* Cloud Native Gateway sends the request as an HTTP request to the selected endpoint.
* For streaming results such as Query rows and Search hits, Cloud Native Gateway reads the response incrementally. It then translates each batch into gRPC stream messages for Protostellar.

### [](#data-api-passthrough-routing)Data API Passthrough Routing

The Data API's passthrough proxy (`/_p/` path prefix) forwards HTTP requests directly to the appropriate Couchbase service REST API:

* `/_p/query/` — Proxied to the Query Service.
* `/_p/fts/` — Proxied to the Search Service.
* `/_p/cbas/` — Proxied to the Analytics Service.

The proxy forwards requests under the credentials of the requesting user. It rewrites the target URL and forwards the request to the backend service. The backend service streams responses back to the client unmodified. You can optionally block administrative API access through the proxy for security.

## [](#topology-awareness-and-metadata-propagation)Topology Awareness and Metadata Propagation

Cloud Native Gateway maintains a real-time view of the cluster topology and propagates relevant information to connected clients.

### [](#cluster-configuration-monitoring)Cluster Configuration Monitoring

Cloud Native Gateway continuously monitors the cluster configuration through two mechanisms:

* **HTTP configuration polling** \- Periodically fetches the cluster configuration from the management API to detect node additions, removals, service changes, and rebalance operations.
* **Streaming configuration updates** \- Receives push-based configuration updates through the Memcached protocol's configuration change notification mechanism.

When a topology change is detected, Cloud Native Gateway:

1. Updates its internal vBucket map and service endpoint lists.
2. Establishes connections to any new nodes and closes connections to removed nodes.
3. Reconfigures the cbauth subsystem with the updated management endpoint list.
4. Emits updated routing information to any clients subscribed via the `WatchRouting` RPC.

### [](#routing-information-for-clients)Routing Information for Clients

Clients that call `WatchRouting` receive `WatchRoutingResponse` messages containing:

* **Service routing** \- For each service type such as KV, Query, Search, Analytics, and Views, the number of servers available in the local group and in remote server groups.
* **vBucket routing** (when a bucket name is specified) - The total number of vBuckets and the mapping of vBucket IDs to local and group server indices.

This routing information enables advanced clients to perform zone-aware load balancing. For example, in a multi-availability-zone cloud deployment, a client can use service discovery to route traffic to the Cloud Native Gateway instance in the same availability zone, minimizing cross-zone network costs.

### [](#metadata-propagation)Metadata Propagation

Cloud Native Gateway propagates several pieces of metadata between clients and the cluster:

* **Request deadlines** \- Cloud Native Gateway respects gRPC deadlines from client requests throughout the request lifecycle. It cancels in-flight backend operations when deadlines expire.
* **User-Agent** \- Cloud Native Gateway tracks client user-agent strings and reports them through metrics. This provides fleet-wide visibility into SDK versions and client types.
* **Server identification** — Cloud Native Gateway identifies itself to clients via gRPC server headers, enabling version-specific compatibility handling if needed.