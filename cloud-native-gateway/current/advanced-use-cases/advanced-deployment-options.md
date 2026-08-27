---
title: Advanced Deployment Options
description: The location of Cloud Native Gateway relative to your Couchbase
  cluster can hugely affect the Cloud Native Gateway-to-Cluster latency.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/advanced-use-cases/pages/advanced-deployment-options.adoc
  xref: xref:cloud-native-gateway:advanced-use-cases:advanced-deployment-options.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/advanced-use-cases/advanced-deployment-options.html)

# Advanced Deployment Options

> The location of Cloud Native Gateway relative to your Couchbase cluster can hugely affect the Cloud Native Gateway-to-Cluster latency. 

## [](#cloud-native-gateway-to-cluster-communication)Cloud Native Gateway to Cluster Communication

Therefore in a self-managed deployment consider:

* Cloud Native Gateway on same hardware as the Cluster. This allows Cloud Native Gateway to reach the cluster over localhost.
* Cloud Native Gateway in same VPC/Subnet. Allows for private IP addressing, avoiding overhead of the public Internet.

Since your Couchbase Cluster nodes span multiple locations to increase resilience, no single Cloud Native Gateway instance can be optimally placed for all of them. Therefore deploy a fleet of Cloud Native Gateway nodes, 1 per node AZ for example, and have a load balancer spread requests across the Cloud Native Gateway instances. Since the client has no awareness of which Cloud Native Gateway instance is optimal for a given request, some still have to cross the AZ boundary.

## [](#functions-as-a-service)Functions-as-a-Service

FaaS environments present a unique challenge because the system creates and destroys function instances at high frequency, and each invocation may create a new connection. Without Cloud Native Gateway, this creates massive connection churn on the Couchbase cluster.

With Cloud Native Gateway:

* Function instances connect to a single Cloud Native Gateway endpoint.
* Connection establishment is fast - 1 TCP connection with TLS.
* The function does not need cluster topology discovery.
* Cloud Native Gateway uses an existing pool of connections to service the request efficiently.
* Warm function instances can reuse their gRPC connection across invocations.
* Even cold-start invocations add only a single connection to Cloud Native Gateway.

For FaaS deployments, consider:

* Deploying Cloud Native Gateway as a standalone service, not as a sidecar, with dedicated resources sized for the expected connection count.
* Enabling rate limiting to protect the cluster from unexpected traffic spikes.

## [](#large-microservice-fleets)Large Microservice Fleets

For environments with thousands of microservice instances:

* Deploy Cloud Native Gateway in sidecar mode for simplicity if using Couchbase Kubernetes Operator.
* Verify that the Cloud Native Gateway service's load balancer uses Layer 4, or TCP, pass-through.
* Monitor the `grpc_connections_total` and `grpc_connections` metrics to track connection utilization.

## [](#multi-tenant-environments)Multi-Tenant Environments

When multiple tenants share a Couchbase cluster:

* Cloud Native Gateway's per-request authentication ensures tenant isolation at the data use level.
* Connection concentration means tenant count does not linearly increase cluster connection pressure.
* You can apply rate limiting at the Cloud Native Gateway level to prevent any single tenant from overwhelming the cluster.