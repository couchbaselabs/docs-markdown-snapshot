---
title: Sizing Cloud Native Gateway Deployments
description: ""
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/sizing-performance-guidance/pages/sizing-cng-guidelines.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:sizing-performance-guidance:sizing-cng-guidelines.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/sizing-performance-guidance/sizing-cng-guidelines.html)

# Sizing Cloud Native Gateway Deployments

## [](#general-sizing-considerations)General Sizing Considerations

Cloud Native Gateway acts as a thin protocol translation proxy that maintains minimal state, so it's efficient with both CPU and memory. Resource requirements depend on your workload's size and resource demands, and the size of the cluster it's running against.

When Cloud Native Gateway concentrates a high number of client connections, the fixed backend connection pool typically becomes the throughput constraint before CPU or RAM. This assumes you follow the recommendations in this topic. In this scenario, deploy an additional Cloud Native Gateway instance and load balance across both.

Given the efficiency of gRPC and Go routines, cluster performance tends to become the bottleneck before Cloud Native Gateway does.

### [](#cpu)CPU

Cloud Native Gateway acts as a thin protocol translation proxy and should use minimal CPU cycles. Performance tests show that co-deploying Cloud Native Gateway on a Couchbase Server node on a 2 vCPU instance increased CPU utilization by up to 10%. This increase did not scale with concurrent operations. Under normal conditions, CPU is not a bottleneck.

As a minimum, deploy Cloud Native Gateway on an instance with at least 1 vCPU. 2 vCPUs is the recommended production allocation. A burst of concurrent TLS handshakes can cause a temporary CPU spike, and the additional vCPU provides headroom to absorb it without throttling.

### [](#ram)RAM

Cloud Native Gateway is stateless: it holds no document data or session caches between requests, so memory usage is stable and predictable under constant load.

The main factors influencing memory usage are:

* **Connection count** — each persistent gRPC connection requires memory to hold TLS session state. Each gRPC connection supports up to 512 concurrent streams, so connection counts remain manageable when connections are properly reused. Cloud Native Gateway does not cap gRPC connections at the application level; the OS file descriptor limit per process determines the maximum.
* **In-flight streams** — Cloud Native Gateway holds documents of up to 25 MiB in stream buffers while servicing a request. Workloads that concurrently read or write large documents can therefore increase memory usage beyond the minimum.

Unless your workload involves concurrent large-document operations, 512 MiB of RAM is a reasonable minimum starting point.

### [](#networking)Networking

Incoming gRPC connections support multiplexing of up to 512 concurrent streams per connection.

All standard Couchbase Server networking requirements apply to the cluster that Cloud Native Gateway sits in front of. Refer to [Couchbase Server Sizing Guidelines](../../../server/current/install/sizing-general.md) for guidance on bandwidth and network configuration for the cluster itself.