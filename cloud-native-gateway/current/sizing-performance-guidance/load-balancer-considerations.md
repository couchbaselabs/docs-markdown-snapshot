---
title: Load Balancer Considerations
description: ""
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/sizing-performance-guidance/pages/load-balancer-considerations.adoc
  xref: xref:cloud-native-gateway:sizing-performance-guidance:load-balancer-considerations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/sizing-performance-guidance/load-balancer-considerations.html)

# Load Balancer Considerations

When deploying multiple Cloud Native Gateway instances, the choice of load balancer depends on which interface you use.

For the gRPC interface, use an L7 load balancer with gRPC support. gRPC connections are persistent and multiplexed. Once a client connects to a Cloud Native Gateway instance, that instance serves all streams on that connection. An L4/TCP load balancer distributes connections when clients connect, but cannot rebalance streams mid-connection. A small number of long-lived clients can therefore pin disproportionate load to a single instance. An L7 load balancer distributes at the request level, spreading load evenly across instances regardless of connection count.

For the HTTP Data API interface, an L4/TCP load balancer is sufficient. HTTP requests are short-lived and stateless, so the TCP layer naturally distributes connections across instances.

#### [](#health-checks)Health Checks

Cloud Native Gateway exposes liveness and readiness endpoints on the metrics port, which defaults to 9091\. Configure your load balancer to use the readiness endpoint, not the liveness endpoint.

* `/live` — always returns HTTP 200 while the process is running, regardless of backend connectivity.
* `/ready`, also available as `/health` — returns HTTP 200 only when Cloud Native Gateway has connected to the Couchbase cluster, and HTTP 503 otherwise.

Using `/live` for health checks risks routing traffic to an unavailable instance. An instance that's running but has lost its cluster connection appears healthy to the load balancer but cannot serve requests.

#### [](#tls-passthrough-and-mutual-tls)TLS Passthrough and Mutual TLS

If the load balancer handles TLS, it strips client certificates before requests reach Cloud Native Gateway. This disables mTLS, even if Cloud Native Gateway uses a client CA certificate. To preserve mTLS end-to-end, configure the load balancer to use TLS passthrough instead.

If mTLS is not a requirement, TLS handling at the load balancer is safe and simplifies certificate management.

#### [](#idle-connection-timeouts)Idle Connection Timeouts

Load balancers typically enforce an idle connection timeout on established connections. AWS ALB, for example, defaults to 60 seconds. For the gRPC interface, a long-lived connection that's quiet between request bursts can appear idle to the load balancer. The load balancer can then close the connection and cause unexpected resets on the client. Set the idle timeout on the load balancer to a value longer than the keep-alive interval on your gRPC clients to prevent this.