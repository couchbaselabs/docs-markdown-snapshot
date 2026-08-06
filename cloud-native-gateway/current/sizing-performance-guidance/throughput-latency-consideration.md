---
title: Throughput and Latency Considerations
description: ""
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/sizing-performance-guidance/pages/throughput-latency-consideration.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:sizing-performance-guidance:throughput-latency-consideration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/sizing-performance-guidance/throughput-latency-consideration.html)

# Throughput and Latency Considerations

## [](#latency)Latency

Cloud Native Gateway acts as a thin protocol translation layer. Its contribution to end-to-end latency is minimal. In most deployments, the Couchbase cluster determines observed latency, not Cloud Native Gateway.

### [](#network-proximity-to-the-cluster)Network Proximity to the Cluster

Cloud Native Gateway is a proxy: every client request travels from the client to Cloud Native Gateway, and then from Cloud Native Gateway to the cluster. The Cloud Native Gateway-to-cluster leg is on the critical path of every operation. A high-latency or congested link between Cloud Native Gateway and the cluster adds directly to end-to-end latency in a way that scaling Cloud Native Gateway cannot offset.

Treat the network between Cloud Native Gateway and the cluster with the same care as intra-cluster networking. Where possible, deploy Cloud Native Gateway within the same network layer as the cluster rather than routing traffic across network boundaries or availability zones. The ideal configuration is co-location on a cluster node, which reduces the Cloud Native Gateway-to-cluster hop to localhost. Co-located deployments add at most 10% CPU overhead on a 2 vCPU instance, which is an acceptable trade-off for typical workloads.

For deployment patterns that achieve low-latency Cloud Native Gateway-to-cluster connectivity, see [Deploying Cloud Native Gateway](#server:cloud:cng-deployment.adoc).

### [](#tls-handshake-cost)TLS Handshake Cost

TLS establishes once per connection, not per request. Streams on an established connection do not pay the handshake cost again. Clients that open a new connection per request pay this cost on every operation and add unnecessary CPU load to Cloud Native Gateway.

Maintain long-lived connections and multiplex requests across streams to amortize this cost. For short-lived clients or serverless functions, use a connection pool or singleton client to persist connections across invocations.

## [](#throughput)Throughput

### [](#rate-limiting)Rate Limiting

Cloud Native Gateway supports a per-instance request rate limit via the `rate-limit` setting. The default is 0, which disables rate limiting. Set a non-zero value to cap the number of requests per second a single instance processes.

When running multiple Cloud Native Gateway instances behind a load balancer, the effective rate limit across the deployment is the per-instance value multiplied by the number of instances.

### [](#connection-reuse)Connection Reuse

Each gRPC connection supports up to 512 concurrent streams. Clients that reuse connections can drive high concurrency from a small number of connections. Clients that open a new connection per request consume connection slots and file descriptors on Cloud Native Gateway without using stream multiplexing.

## [](#client-side-considerations)Client-Side Considerations

### [](#request-deadlines)Request Deadlines

Set a deadline on every gRPC request. A request without a deadline can hold a stream slot open indefinitely if the cluster is slow to respond. Under high concurrency, blocked slots reduce available capacity for other requests on the same connection and increase observed latency.

### [](#keep-alive-configuration)Keep-Alive Configuration

Configure gRPC keep-alives on the client to detect dead connections quickly. A client unaware that a connection has closed waits for a timeout rather than reconnecting immediately.

Keep-alive intervals on the client should be shorter than the idle connection timeout on your load balancer. See [Load Balancer Considerations](load-balancer-considerations.md) for guidance on setting load balancer idle timeouts.