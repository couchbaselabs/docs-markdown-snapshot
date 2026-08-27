---
title: About Cloud Native Gateway
description: Cloud Native Gateway (CNG) is a gRPC-based ingress to consolidate
  application connectivity to Couchbase Server for public and private cloud
  environments.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/intro/pages/about-cng.adoc
  xref: xref:cloud-native-gateway:intro:about-cng.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/intro/about-cng.html)

# About Cloud Native Gateway

> Cloud Native Gateway (CNG) is a gRPC-based ingress to consolidate application connectivity to Couchbase Server for public and private cloud environments. 

## [](#whats-cloud-native-gateway)What's Cloud Native Gateway?

Cloud Native Gateway is a translation layer between applications using Couchbase SDKs or gRPC clients and Couchbase Server. It enables access to Couchbase services through 2 endpoints. One is a gRPC endpoint — defined by the [Protostellar protocol](https://github.com/couchbase/protostellar). Through this, applications can access a range of Couchbase services including Key-Value (Data), Query (SQL++), and Search (Full-Text Search) services.

In traditional Couchbase deployments, SDKs connect directly to every node in the cluster. The SDK must subscribe to and get updates on the cluster topology: which nodes host which services and how to react when the topology changes. The underlying connections are protocol specific.

Cloud Native Gateway changes this to move all communication between SDKs and the cluster to use a single, unified gRPC endpoint. Because Cloud Native Gateway uses gRPC, you can expose it through standard cloud infrastructure like load balancers, API gateways, and service meshes. Applications connect to a single hostname and port, and Cloud Native Gateway handles all topology awareness, protocol translation, and request routing internally.

## [](#why-cloud-native-gateway)Why Cloud Native Gateway?

Modern cloud infrastructure — Kubernetes, OpenShift, AWS PrivateLink, GCP Private Service Connect — use **service endpoints**: single network locations that abstract away service location and implementation details. These platforms provide a mature ecosystem of load balancers, ingress controllers, service meshes (Istio, Envoy), API gateways, and observability tools — all built on the assumption that services communicate over HTTP-based protocols.

Couchbase's traditional multi-port, multi-protocol networking provides certain advantages with performance and observability. However, it makes networking configuration complicated in environments that expect to hide network topology details. Cloud Native Gateway bridges this gap by presenting Couchbase as a standard gRPC-over-HTTP/2 service, which means:

* **Kubernetes and OpenShift integration** \- Cloud Native Gateway can expose a Couchbase Cluster's data and services through standard Kubernetes `Ingress`, `LoadBalancer`, or OpenShift `Route` objects.
* **Private networking** \- Cloud Native Gateway works naturally with AWS PrivateLink, GCP Private Service Connect, and Azure Private Link, which expect a single service endpoint.
* **Service mesh compatibility** \- Istio, Envoy, or any HTTP/2-compatible proxy can manage, observe, and secure Cloud Native Gateway traffic.
* **Observability** \- Standard gRPC tooling, metrics exporters, and tracing infrastructure work out of the box.

## [](#how-it-works)How It Works

Cloud Native Gateway translates the Protostellar gRPC interface into the native Couchbase protocols used by the cluster's internal services:

1. An application using a Couchbase SDK configured with the `couchbase2://` connection scheme sends a gRPC request to Cloud Native Gateway.
2. Cloud Native Gateway authenticates the request through Couchbase's credential system, `cbauth`, or via TLS client certificates.
3. Cloud Native Gateway translates the gRPC request into the appropriate native protocol — Memcached binary protocol for KV operations, or HTTP for Query, Search, and Analytics.
4. Cloud Native Gateway translates the response from the Couchbase service back into a Protostellar gRPC response and returns it to the client.

Because the network requests are stateless and context-reduced, any request can be independently routed and load-balanced. Cloud Native Gateway nodes maintain no session state between requests, which means its instances can scale horizontally and work behind standard load balancers without session affinity.

## [](#data-api)Data API

In addition to the gRPC Protostellar interface used by Couchbase SDKs, Cloud Native Gateway also serves the **Data API**. This RESTful HTTP interface enables document operations with topology transparent access to Couchbase services like Query and SQL++.

The Data API is useful for environments where a native SDK is not available. It supports lightweight integrations such as Functions-as-a-Service (FaaS/Lambda) deployments.

See [About Data API](../data-api/data-API-overview.md) for details.

## [](#next-steps)Next Steps

* [Key Features](key-features.md) — Detailed overview of Cloud Native Gateway capabilities.
* [Supported and Unsupported Capabilities](supported-unsupported-capabilities.md) — What services and SDKs work with Cloud Native Gateway, and known limitations.