---
title: Behavior During Node Failures
description: How Cloud Native Gateway handles Couchbase Server node failures,
  Cloud Native Gateway instance failures, and the impact on client applications.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/availability-and-failover/pages/behavior-during-node-failures.adoc
  xref: xref:cloud-native-gateway:availability-and-failover:behavior-during-node-failures.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/availability-and-failover/behavior-during-node-failures.html)

# Behavior During Node Failures

> How Cloud Native Gateway handles Couchbase Server node failures, Cloud Native Gateway instance failures, and the impact on client applications. 

## [](#couchbase-server-node-failure)Couchbase Server Node Failure

When a Couchbase Server node fails, Cloud Native Gateway detects the failure and adapts its routing behavior.

### [](#kv-data-node-failure)KV (Data) Node Failure

1. **Connection failure detection** \- Cloud Native Gateway's IO layer detects that connections to the failed node are broken (TCP reset, timeout, or connection refused).
2. **Request rerouting** \- Requests targeted at data nodes owned by the failed node will receive errors. Cloud Native Gateway's retry logic may retry these operations if they're safe to retry.
3. **Configuration update** \- Cloud Native Gateway receives an updated cluster configuration reflecting the failover. Once you update the configuration map, Cloud Native Gateway routes new requests to the nodes that have taken over for the failed node.
4. **Client impact** \- Clients may experience errors or increased latency during the failover window as Cloud Native Gateway detects the failure and receives the updated configuration. Once you update the configuration, operations resume automatically without any client action.

This behavior is dependent on how the failure is detected and handled by the Couchbase Server cluster in your deployment.

### [](#query-and-search-node-failure)Query and Search Node Failure

You can access these services at their HTTP endpoints, and Cloud Native Gateway distributes requests across available endpoints:

1. Cloud Native Gateway detects that the failed node's service endpoint is unreachable.
2. Subsequent requests are routed to other available endpoints for that service.
3. Once the cluster configuration is updated to remove the failed node, Cloud Native Gateway stops attempting to use it.

For these services, the impact on clients is minimal as long as other nodes with the same service are available.

## [](#cloud-native-gateway-instance-failure)Cloud Native Gateway Instance Failure

Cloud Native Gateway instances can fail in different deployment scenarios. The following sections describe how failures are handled in each scenario.

### [](#sidecar-deployment)Sidecar Deployment

In sidecar deployments, a Cloud Native Gateway instance failure means the Cloud Native Gateway container on a specific Couchbase pod has crashed or become unresponsive.

1. **Health check failure** \- The Kubernetes liveness probe detects the Cloud Native Gateway container failure.
2. **Container restart** \- Kubernetes automatically restarts the Cloud Native Gateway container.
3. **Service removal** \- While the Cloud Native Gateway container is restarting, Kubernetes removes the pod's endpoint from the Cloud Native Gateway Service. Configured gateways (load balancers or routes) stop sending traffic to this instance.
4. **Client impact** \- Clients with active connections to the failed instance experience connection drops. These may manifest as errors in applications, or may be transparently retried automatically. The gRPC client in the SDK reconnects to another available Cloud Native Gateway instance (routed by a gateway or load balancer).
5. **Recovery** \- Once the Cloud Native Gateway container restarts and passes its health check, Kubernetes adds the endpoint back to the Service and the load balancer resumes sending traffic.

Since there are multiple Cloud Native Gateway instances (1 per Couchbase pod), the failure of a single instance does not cause an outage. Instead, traffic is redistributed to the remaining instances.

### [](#standalone-deployment)Standalone Deployment

In standalone deployments with multiple Cloud Native Gateway replicas behind a load balancer:

1. The load balancer's health check detects the failed instance.
2. Traffic is redirected to healthy instances.
3. Kubernetes (or the orchestrator) restarts the failed instance.
4. Clients reconnect through the load balancer.

## [](#graceful-shutdown)Graceful Shutdown

Cloud Native Gateway implements graceful shutdown to minimize disruption during planned maintenance. By sending a shutdown signal to the Cloud Native Gateway process, the following actions occur:

1. **Stop accepting new connections** \- Cloud Native Gateway stops accepting new gRPC connections and HTTP requests.
2. **Drain existing requests** \- In-flight requests are allowed to complete within the shutdown timeout (default 30 seconds).
3. **gRPC graceful stop** \- The gRPC server performs a `GracefulStop`, allowing active RPCs to finish.
4. **HTTP keep-alive disable** \- The Data API server disables keep-alive connections and waits for active requests to complete.
5. **Force shutdown** \- If requests do not complete within the timeout, remaining connections are forcefully closed.

In Kubernetes, this is triggered by the pod receiving a `SIGTERM` signal during a rolling update or scaling event. Configure the pod's `terminationGracePeriodSeconds` to be at least as long as Cloud Native Gateway's shutdown timeout to allow graceful drainage.