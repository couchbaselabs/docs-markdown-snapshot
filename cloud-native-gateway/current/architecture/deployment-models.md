---
title: Deployment Models
description: Cloud Native Gateway supports sidecar, standalone, and internal
  Capella deployment models, each suited to different infrastructure and
  operational requirements.
editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/architecture/pages/deployment-models.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:cloud-native-gateway:architecture:deployment-models.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/architecture/deployment-models.html)

# Deployment Models

> Cloud Native Gateway supports sidecar, standalone, and internal Capella deployment models, each suited to different infrastructure and operational requirements. 

## [](#sidecar-deployment)Sidecar Deployment

In Kubernetes and OpenShift, the sidecar deployment model is the deployment model. Cloud Native Gateway is managed by the Couchbase Kubernetes Operator. For more information, see [Introduction to Kubernetes Operator](../../../operator/current/overview.md).

In this model, a Cloud Native Gateway container runs as a sidecar alongside every Couchbase Server pod in the cluster. Resources for Cloud Native Gateway in this deployment model are allocated from the Couchbase pod's resources from the server class.

### [](#how-it-works)How It Works

The Couchbase Kubernetes Operator provisions each Couchbase Server pod with Cloud Native Gateway injected as a sidecar container. Cloud Native Gateway bootstraps by connecting to the local node over `localhost`. Kubernetes then creates a `Service` object selecting all gateway sidecars. This exposes a single endpoint for client applications and Kubernetes load-balances traffic across gateway instances.

### [](#characteristics)Characteristics

* **Low latency** \- Cloud Native Gateway communicates with the local Couchbase node over localhost, minimizing network overhead for the bootstrap connection. For KV operations, Cloud Native Gateway still routes requests to the correct node based on the vbucket map, which may be a remote node.
* **Co-located lifecycle** \- Cloud Native Gateway starts and stops with the Couchbase pod, simplifying lifecycle management.
* **Automatic scaling** \- Adding Couchbase nodes to the cluster automatically adds Cloud Native Gateway capacity.
* **No separate infrastructure** \- The deployment requires no additional pods, deployments, or resource allocations beyond the Couchbase cluster itself.

### [](#when-to-use)When to Use

* Kubernetes or OpenShift deployments managed by Couchbase Kubernetes Operator.
* Standard production deployments where Cloud Native Gateway capacity should scale with the cluster.
* Environments where minimizing operational complexity is a priority.

## [](#standalone-deployment)Standalone Deployment

In a standalone deployment, Cloud Native Gateway runs as a container, separate from the Couchbase Server nodes. Cloud Native Gateway connects to the cluster via the network using a provided connection string and credentials.

### [](#how-it-works-2)How It Works

Deploy Cloud Native Gateway as a set of containers with network access to the Couchbase cluster. Configure Cloud Native Gateway with a connection string pointing to 1 or more Couchbase Server management endpoints.

Cloud Native Gateway discovers the full cluster topology through the management API and establishes connections to all relevant services. Client applications connect to the Cloud Native Gateway endpoints.

### [](#characteristics-2)Characteristics

* **Independent scaling** \- You can scale Cloud Native Gateway instances independently of the Couchbase cluster based on client connection load rather than data node count.
* **Deployment flexibility** \- You can run Cloud Native Gateway on different hardware, in a different Kubernetes namespace, or even in a different network zone than the Couchbase cluster.
* **Multiple instances** \- You may configure Cloud Native Gateway to run multiple internal gRPC server instances via `NumInstances` within a single process for higher throughput on larger multi-core machines.
* **Network overhead** \- Cloud Native Gateway and Couchbase exchange all communication through the network rather than localhost.

### [](#when-to-use-2)When to Use

* Self-managed Couchbase deployments outside of Kubernetes.
* Environments where you need to scale Cloud Native Gateway independently of the data tier.
* Development and testing environments.
* Situations where the Couchbase cluster is not managed by Couchbase Kubernetes Operator.

## [](#capella-deployment)Capella Deployment

In Couchbase Capella, Cloud Native Gateway is deployed as an infrastructure component to provide Data API interfaces to Capella managed Couchbase Server clusters. Note at this time, the Protostellar gRPC interface is not available on Capella. For more information, see [Get Started with the Data API](../../../cloud/data-api-guide/data-api-start.md).

### [](#architecture)Architecture

The Capella deployment runs Cloud Native Gateway on each Couchbase Server node similar to the side-car model used in Kubernetes:

* **Ingress scalability** \- Data API will scale with the number of nodes in the Capella managed cluster.
* **Security allow-lists** \- Enforces Capella's IP allow-list and access control policies.
* **Workload management** \- Supports Capella's ability to pause, resume, and upgrade workloads within infrastructure.
* **Private networking** \- Provides the service endpoint for AWS PrivateLink, GCP Private Service Connect, and Azure Private Link connections.

### [](#characteristics-3)Characteristics

* **Fully managed** — Capella handles all deployment, configuration, and lifecycle management.
* **Multi-tenant isolation** — Cloud Native Gateway enforces tenant-level security boundaries.
* **Transparent to users** — Capella users connect to Cloud Native Gateway through the Capella-provided endpoint without needing to manage Cloud Native Gateway configuration.

### [](#when-to-use-3)When to Use

Couchbase Capella exclusively uses this deployment model.