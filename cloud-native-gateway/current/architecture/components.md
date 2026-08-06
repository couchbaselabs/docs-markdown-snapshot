---
title: Components
description: The internal components that make up Cloud Native Gateway,
  including the gRPC server, Data API server, protocol translation layer,
  authentication system, and supporting infrastructure.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/architecture/pages/components.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:architecture:components.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/architecture/components.html)

# Components

> The internal components that make up Cloud Native Gateway, including the gRPC server, Data API server, protocol translation layer, authentication system, and supporting infrastructure. 

## [](#cloud-native-gateway-container)Cloud Native Gateway Container

Cloud Native Gateway runs as a single container image (`Couchbase/cloud-native-gateway`) alongside Couchbase Server. The container hosts 2 primary server processes and several supporting subsystems.

### [](#grpc-server-protostellar)gRPC Server (Protostellar)

The gRPC server serves as the primary interface for Couchbase SDK clients that use the `couchbase2://` connection scheme. It listens on a configurable TLS‑encrypted port (default 18098) and registers the following Protostellar service implementations:

| gRPC Service           | Purpose                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| KvService              | Key-value document operations (CRUD, Sub-Document operations, counters, locking, replicas) |
| QueryService           | SQL++ query execution with streaming results                                               |
| SearchService          | Full-Text Search queries, including facets, sorting, highlighting, and vector search       |
| TransactionsService    | Server-managed distributed ACID transactions                                               |
| BucketAdminService     | Bucket lifecycle management (create, update, delete, list)                                 |
| CollectionAdminService | Scope and collection management                                                            |
| QueryAdminService      | Query index administration                                                                 |
| SearchAdminService     | Search index administration                                                                |
| RoutingService         | Cluster topology and routing updates delivered through server-side streaming               |
| Health (gRPC standard) | Standard gRPC health checks for liveness and readiness probes                              |

### [](#data-api-server-https)Data API Server (HTTPS)

The Data API server is an HTTPS server that listens on a separate configurable port and provides the following endpoints:

1. `/v1/` — Data API endpoints defined by an OpenAPI 3.0 specification. These endpoints provide RESTful document operations (CRUD, Sub-Document operations, binary operations, locking) and utility endpoints such as caller identity.
2. `/_p/` — A reverse proxy that provides passthrough access to Couchbase service REST APIs (Query, Search, Analytics). This allows clients to execute SQL++, Full-Text Search, or Analytics queries through the Data API endpoint without requiring direct connectivity to individual services.

### [](#protocol-translation-layer)Protocol Translation Layer

The protocol translation layer forms the core of Cloud Native Gateway. It consists of service-specific server implementations that translate Protostellar requests into native Couchbase protocol operations:

1. **KV server** — Translates gRPC KV requests into Memcached binary protocol operations by using the `gocbcorex` client library. Handles vBucket routing, collection resolution, compression, and error mapping.
2. **Query server** — Translates gRPC query requests into HTTP POST requests to the SQL++ Query Service and streams results as they arrive.
3. **Search server** — Translates gRPC search requests into HTTP requests to the Full-Text Search (FTS) service.
4. **Analytics server** — Translates gRPC analytics requests into HTTP requests to the Analytics (CBAS) service.
5. **Admin server** — Translates gRPC administrative requests into the corresponding Couchbase management REST API calls.

Each server implementation pairs with an AuthHandler that extracts and validates credentials from incoming requests. A shared ErrorHandler maps native Couchbase errors to appropriate gRPC status codes with rich contextual information.

### [](#authentication-subsystem)Authentication Subsystem

Cloud Native Gateway supports 2 authentication modes:

1. **Multi-user mode (cbauth)** — This is the default mode for production deployments. Cloud Native Gateway registers with the internal Couchbase authentication service (cbauth) to validate credentials per request. It supports username and password authentication, TLS client certificates, and On-Behalf-Of semantics for multi-tenant scenarios. Cloud Native Gateway monitors cluster configuration changes and dynamically updates cbauth endpoints as cluster nodes join or leave.
2. **Single-user mode** — This is a simplified mode for development and testing. It authenticates all requests with a single configured username and password.