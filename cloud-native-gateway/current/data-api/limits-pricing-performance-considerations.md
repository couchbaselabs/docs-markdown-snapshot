---
title: Limits, Pricing, and Performance Considerations
description: Rate limits, message size constraints, and performance
  characteristics of the Data API served by Cloud Native Gateway.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/data-api/pages/limits-pricing-performance-considerations.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:data-api:limits-pricing-performance-considerations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/data-api/limits-pricing-performance-considerations.html)

# Limits, Pricing, and Performance Considerations

> Rate limits, message size constraints, and performance characteristics of the Data API served by Cloud Native Gateway. 

## [](#request-size-limits)Request Size Limits

The Data API and the underlying gRPC Protostellar interface enforce the following size limits:

| Limit                                          | Value                                    |
| ---------------------------------------------- | ---------------------------------------- |
| Maximum gRPC request/response message size     | 25 MiB                                   |
| Maximum Data API document body size            | 20 MiB, enforced by Cloud Native Gateway |
| HTTP request header read timeout               | 5 seconds                                |
| HTTP connection idle timeout                   | 60 seconds                               |
| Maximum concurrent gRPC streams per connection | 512                                      |

## [](#rate-limiting)Rate Limiting

Cloud Native Gateway includes a built-in global rate limiter, turned off by default. When requests exceed the rate limit, the Data API returns an HTTP `429 Too Many Requests` response.

The rate limiter uses a fixed window mechanism:

* You can set a maximum number of requests per time period.
* The window resets at fixed boundaries for predictable behavior.
* You can update the rate limit at runtime without restarting Cloud Native Gateway.

You can enable rate limiting at deployment time. The system applies no limits if you do not configure them.

In Couchbase Capella, additional rate limits may apply at the platform level.

## [](#performance-considerations)Performance Considerations

The following sections describe the performance characteristics and considerations for the Data API.

### [](#latency-overhead)Latency Overhead

The Data API adds a small amount of additional latency compared to direct client-to-cluster communication. This overhead comes from HTTP translation and the network hop through Cloud Native Gateway. For most workloads, this overhead is negligible. Query, Search, and Analytics operations typically take milliseconds to seconds to complete. The Data API translation overhead is proportionally insignificant for these use cases.

### [](#throughput)Throughput

These factors influence Cloud Native Gateway throughput:

* **CPU allocation** — Protocol translation and TLS termination are CPU-intensive. Make sure Cloud Native Gateway has adequate CPU resources.
* **Connection pool size** — Cloud Native Gateway has a default pool of 8 Memcached connections per data node. This works for most cases, but you can tune the value for high-throughput use.
* **HTTP/2 multiplexing** — HTTP/2 lets clients send concurrent requests over 1 TCP connection. This cuts overhead but caps throughput at the connection's bandwidth.
* **Number of Cloud Native Gateway instances** — In sidecar mode, Cloud Native Gateway scales with the cluster. In standalone mode, add more Cloud Native Gateway instances to meet your throughput needs.

### [](#data-api-vs-grpc-performance)Data API vs gRPC Performance

The gRPC interface is generally more efficient than the Data API for high-throughput workloads:

* **Protobuf serialization** is more compact and faster to parse than JSON.
* **HTTP/2 stream multiplexing** in gRPC allows more concurrent requests per connection than HTTP/1.1.
* **Streaming results** for Query and Search operations deliver rows incrementally over gRPC streams, reducing time-to-first-row.

The Data API is best suited for lightweight use cases, integrations, and environments where gRPC is not practical. For latency-sensitive, high-throughput production workloads, use a Couchbase SDK with the `couchbase2://` connection scheme.

## [](#capella-pricing)Capella Pricing

Couchbase Capella meters and bills Data API usage as part of your Capella plan. See the [Couchbase Capella pricing documentation](https://www.couchbase.com/pricing) for per-operation costs, free-tier allowances, and rate limit tiers.

For self-managed deployments, there is no per-operation charge for using the Data API. Cloud Native Gateway comes with the Couchbase Server Enterprise Edition license.