---
title: High Connection Count Workloads
description: Each SDK application instance opens multiple connections to every
  node in the cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/advanced-use-cases/pages/high-connection-count-workloads.adoc
  xref: xref:cloud-native-gateway:advanced-use-cases:high-connection-count-workloads.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/advanced-use-cases/high-connection-count-workloads.html)

# High Connection Count Workloads

> Each SDK application instance opens multiple connections to every node in the cluster. 

## [](#connection-concentration-model)Connection Concentration Model

As you scale your app, the total connection count grows fast. Cloud Native Gateway cuts this overhead thanks to how gRPC works:

* Multiplexing - gRPC sends hundreds of request streams over 1 TCP link. Cloud Native Gateway sets the max stream limit to 512.
* Sticky connections - gRPC connections stay open for a long time. The TCP/TLS handshake happens far less often.

Cloud Native Gateway also keeps a pool of connections to the cluster and reuses them across client requests.

### [](#clustered-deployments)Clustered Deployments

You can take this model further by scaling Cloud Native Gateway across more nodes. With the Couchbase Kubernetes Operator, Cloud Native Gateway runs as a sidecar and scales with the cluster. Adding a data node also adds a Cloud Native Gateway instance. As a standalone service, you can scale Cloud Native Gateway on its own as needed. Place a load balancer in front of the Cloud Native Gateway fleet to spread traffic. Each application instance then holds just 1 connection to the load balancer. The load balancer splits this traffic across all Cloud Native Gateway nodes.