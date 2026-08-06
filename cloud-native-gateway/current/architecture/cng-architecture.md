---
title: Cloud Native Gateway Architecture
description: An architectural overview of how Cloud Native Gateway translates
  Protostellar gRPC requests into native Couchbase protocols, multiplexes
  services over a single endpoint, and manages cluster discovery.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/architecture/pages/cng-architecture.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:architecture:cng-architecture.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/architecture/cng-architecture.html)

# Cloud Native Gateway Architecture

> An architectural overview of how Cloud Native Gateway translates Protostellar gRPC requests into native Couchbase protocols, multiplexes services over a single endpoint, and manages cluster discovery. 

## [](#protocol-translation-using-protostellar)Protocol Translation Using Protostellar

Cloud Native Gateway acts as a protocol translation layer between the Protostellar gRPC interface and the native protocols used by Couchbase Server's internal services.

When Cloud Native Gateway receives a gRPC request, it performs the following steps:

1. Accept the request: Cloud Native Gateway accepts the request on the Protostellar port (default 18098) over TLS‑encrypted HTTP/2.
2. Authenticate the caller: An authentication interceptor validates the caller's credentials against Couchbase's internal authentication service (cbauth). Cloud Native Gateway authenticates the caller by using 1 of the following:

  * HTTP Basic or Bearer credentials in the gRPC metadata
  * TLS client certificate.
3. Route the request: Cloud Native Gateway routes the request to the appropriate service implementation based on the gRPC service and method:

  * Key-value (KV) operations: Cloud Native Gateway translates KV operations (Get, Upsert, Remove, Sub-Document operations, and others) into the Memcached binary protocol and sends them to the appropriate data node. Cloud Native Gateway resolves the target node by using the cluster's vBucket map, so the client does not need to determine key ownership.
  * Query operations: Cloud Native Gateway translates Query operations into HTTP requests and forwards them to the Query (N1QL) service on an appropriate node.
  * Search operations: Cloud Native Gateway translates Search operations into HTTP requests for the Full Text Search (FTS) service.
  * Analytics operations: Cloud Native Gateway translates Analytics operations into HTTP requests for the Analytics (CBAS) service.
  * Administrative operations: Cloud Native Gateway translates administrative operations (such as bucket, scope, collection, and index management) into the corresponding Couchbase management REST API calls.
4. Return the response: Cloud Native Gateway translates the response from the native Couchbase service into the Protostellar protobuf format and returns it to the client through the gRPC stream.

For streaming operations, such as Query results, Search results, and routing topology updates, Cloud Native Gateway uses gRPC server‑side streaming to send results incrementally as the backend service produces them.

## [](#service-multiplexing-over-grpc-transport)Service Multiplexing Over gRPC Transport

A key characteristic of the Cloud Native Gateway architecture is that it multiplexes all Couchbase services over a single gRPC endpoint. In a traditional deployment, an SDK maintains separate connections to multiple ports across multiple nodes:

* Port 11210 (Key-Value / Memcached) on every data node
* Port 8093 (Query) on query nodes
* Port 8094 (Search) on search nodes
* Port 8095 (Analytics) on analytics nodes
* Port 8091 (Management) for cluster management

With Cloud Native Gateway, a single TLS‑encrypted gRPC port consolidates all of these services. HTTP/2 multiplexing enables numerous concurrent requests to share a single TCP connection. Different service types avoid application-level head-of-line blocking.

Cloud Native Gateway configures the gRPC server with the following settings:

* Maximum message size: Cloud Native Gateway allows messages up to 25 MiB to support large document bodies and query result sets.
* Maximum concurrent streams: Cloud Native Gateway allows up to 512 concurrent streams per connection, which provides high concurrency while protecting against resource exhaustion.
* Observability: Cloud Native Gateway enables OpenTelemetry instrumentation for distributed tracing and metrics collection.

## [](#bootstrap-and-cluster-discovery)Bootstrap and Cluster Discovery

When an SDK connects by using the `couchbase2://` connection scheme, it follows a simplified bootstrap process compared to the classic protocol:

1. Establish the connection: The SDK establishes a TLS‑encrypted gRPC connection to the Cloud Native Gateway endpoint.
2. Authenticate requests: The SDK authenticates each request by using gRPC metadata (the Authorization header) or a TLS client certificate. The connection does not require a separate authentication handshake or SASL negotiation.
3. Receive routing updates (optional): The SDK can subscribe to routing updates by calling the WatchRouting RPC. This call opens a server‑side stream that delivers WatchRoutingResponse messages whenever the cluster topology changes.

Cloud Native Gateway eliminates several bootstrap steps required by the classic protocol. The SDK does not negotiate cluster capabilities, perform HELLO or SASL exchanges, or discover and connect to individual nodes. Instead, the SDK sends requests directly to Cloud Native Gateway and receives responses through the established gRPC connection.