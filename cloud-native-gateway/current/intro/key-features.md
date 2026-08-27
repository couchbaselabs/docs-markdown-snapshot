---
title: Key Features
description: Cloud Native Gateway provides Protostellar protocol translation,
  Data API access, connection concentration, load balancer compatibility, and a
  stateless request model for cloud-native Couchbase deployments.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/intro/pages/key-features.adoc
  xref: xref:cloud-native-gateway:intro:key-features.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/intro/key-features.html)

# Key Features

> Cloud Native Gateway provides Protostellar protocol translation, Data API access, connection concentration, load balancer compatibility, and a stateless request model for cloud-native Couchbase deployments. 

## [](#protostellar-protocol-support)Protostellar Protocol Support

Cloud Native Gateway (CNG) implements the Protostellar protocol - a gRPC-based interface that unifies access to all major Couchbase services through a single endpoint. Protostellar consolidates multiple cluster networking protocols and ports into a single, multiplexed gRPC connection over HTTP/2.

The protocol provides operations for the following Couchbase services:

* **KV (Data) Service** \- Full key-value operations including Get, Upsert, Insert, Replace, Remove, Sub-Document lookups and mutations, atomic counters (Increment/Decrement), binary Append/Prepend, pessimistic locking (GetAndLock/Unlock), Touch, Exists, and replica reads.
* **Query (SQL++) Service** \- Query statement execution with streaming results, prepared statements, scan consistency options, and parameterized queries.
* **Search Service** \- Full-Text search queries supporting 21 query types, geo queries, KNN vector search, facets, sorting, and highlighting.

At this time, the Analytics Service and the Views Service are not supported through the Protostellar interface exposed by the gateway. Transactions are not yet supported through Cloud Native Gateway, whether using the Data Service or the Query Service.

Administrative operations are also available through dedicated service endpoints for bucket management, collection management, query index administration, and Search index administration.

Couchbase SDKs connect to Cloud Native Gateway using the `couchbase2://` connection scheme. No changes needed to the application's data access code - only the connection string changes.

## [](#restful-data-api)RESTful Data API

Cloud Native Gateway also hosts the Couchbase Data API on a separate HTTPS port. The Data API is a RESTful interface defined by an OpenAPI 3.0 specification that provides:

* **Basic document operations** \- Create, read, update, and delete single documents using standard HTTP methods (GET, POST, PUT, DELETE).
* **Sub-Document operations** \- Lookup and mutate specific fields within a document without retrieving the entire document.
* **Binary operations** \- Append, prepend, increment, and decrement operations on binary and counter documents.
* **Locking operations** \- Pessimistic lock acquisition and release.
* **Service passthrough** \- Proxied access to Couchbase Query and Search REST APIs, enabling SQL++ queries and search queries to execute through the same endpoint.
* **Caller identity** \- An endpoint to verify the authenticated identity of the current request, useful for checking and verifying the access control.

## [](#connection-concentration)Connection Concentration

In traditional Couchbase deployments, each SDK instance opens connections to every node in the cluster. Large-scale environments with tens of thousands of application instances or Functions-as-a-Service deployments create numerous TCP connections to each Couchbase node.

Cloud Native Gateway acts as a natural connection concentrator. Application instances connect only to a single Cloud Native Gateway node, and the gateway maintains a managed pool of connections to the Couchbase cluster using its own internal IO layer. This may dramatically reduce the total connection count on the cluster in the following instances:

* Large microservice deployments with numerous pods.
* FaaS/Lambda environments where connection in-rush is common.
* Multi-tenant environments where multiple applications share a cluster.

Because Protostellar requests are stateless, Cloud Native Gateway connections can be efficiently multiplexed over HTTP/2 streams without requiring session affinity.

## [](#compatibility-with-load-balancers-and-proxies)Compatibility with Load Balancers and Proxies

Cloud Native Gateway uses gRPC (HTTP/2) and HTTPS, which most modern infrastructure platforms support as standard protocols. This design allows Cloud Native Gateway to integrate cleanly with common networking, security, and traffic management components:

* **Kubernetes Services** \- Run and manage Cloud Native Gateway as a standard Kubernetes Service by using the Gateway API or Ingress API.
* **OpenShift Routes** \- Expose Cloud Native Gateway externally by using an OpenShift Route to enable access from outside the OpenShift cluster.
* **Cloud load balancers** \- Deploy Cloud Native Gateway behind AWS ALB or NLB, Google Cloud Load Balancer, or Azure Load Balancer, all of which support gRPC or HTTP/2 pass-through.
* **gRPC proxies** \- Deploy Envoy, HAProxy, NGINX (with the gRPC module), or other gRPC-aware proxies in front of Cloud Native Gateway to control and manage traffic.
* **Service meshes** \- Use Istio, Linkerd, or similar service meshes to secure and manage Cloud Native Gateway traffic with features such as mTLS, circuit breaking, observability, and traffic splitting.
* **Private networking** \- Integrate directly with AWS PrivateLink, GCP Private Service Connect, and Azure Private Link by using Cloud Native Gateway's single-endpoint model.
* **Network Security Platforms** \- Integrate Cloud Native Gateway with network security platforms such as Zscaler or Netskope for access control and monitoring when they support gRPC or HTTP/2\. These are not directly tested or supported by Couchbase.

## [](#stateless-request-model)Stateless Request Model

Every request is fully self-contained. Classic Couchbase networking maintains session state, cluster capabilities negotiation, and topology awareness at the client. Protostellar operations logically carry all necessary information - bucket, scope, collection, key, and authentication credentials - in each request.

This design has several important implications:

* **No cluster capabilities negotiation** \- The gateway gracefully handles differences in cluster capabilities across versions. You may send any request to any Cloud Native Gateway instance at any time.
* **No topology awareness is required at the client** \- The cluster identifies the node with the data entirely on the server side. Clients never need to know the cluster topology.
* **Independent request routing** \- Intermediate infrastructure can route, retry, and redirect requests.
* **Transparent topology changes** \- Cloud Native Gateway adapts to rebalances, failovers, and scaling events at the cluster side.

## [](#request-deadlines)Request Deadlines

All gRPC requests in Protostellar carry deadlines. When a request's deadline expires, the system can release resources without delay rather than continuing to process a request the client no longer cares about.

This improves upon the traditional protocol, which continues consuming server resources for timed-out requests and leaves orphaned network responses.

## [](#grpc-health-checking)gRPC Health Checking

Cloud Native Gateway implements the standard [gRPC Health Checking Protocol](https://grpc.io/docs/guides/health-checking/). Each registered gRPC service reports its serving status to Cloud Native Gateway. This enables compatibility with Kubernetes probes, load balancer health checks, and gRPC-aware monitoring systems.

## [](#rate-limiting)Rate Limiting

Cloud Native Gateway includes a built-in global rate limiter for both gRPC (Protostellar) and HTTP (Data API) traffic. The rate limiter uses a sliding window mechanism with configurable maximum requests per period. When requests exceed the limit, gRPC returns `RESOURCE_EXHAUSTED` status, and HTTP returns `429 Too Many Requests`.

You can use the rate limiter to protect the cluster when using either Protostellar or the Data API from unexpected traffic spikes. The spikes can occur in FaaS/Lambda environments or multi-tenant environments where many applications share a cluster.

## [](#observability-and-metrics)Observability and Metrics

Cloud Native Gateway emits rich metrics for Protostellar and Data API traffic: request counts, latencies, error rates, and rate limit rejections. Cloud Native Gateway exposes metrics in Prometheus format on a dedicated endpoint, enabling integration with Prometheus, Grafana, and other monitoring systems.