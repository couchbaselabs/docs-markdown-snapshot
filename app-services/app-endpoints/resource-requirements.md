---
title: App Endpoint Resource Requirements
description: Understand the minimum and recommended memory requirements for App
  Endpoints to ensure reliable App Service performance and avoid resource
  contention.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/app-endpoints/resource-requirements.adoc
  xref: xref:app-services::app-endpoints/resource-requirements.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/app-endpoints/resource-requirements.html)

# App Endpoint Resource Requirements

> Understand the minimum and recommended memory requirements for App Endpoints to ensure reliable App Service performance and avoid resource contention. 

## [](#overview)Overview

Each App Endpoint you create on an App Service maps to an underlying Sync Gateway database. Every Sync Gateway database requires a baseline allocation of system memory to handle DCP feeds, buffers, and caches, regardless of whether there is any active client workload.

Couchbase defines two memory thresholds per App Endpoint:

* **Minimum**: 500 MB — the lowest allocation required for idle or very low traffic operation
* **Recommended**: 1 GB — the allocation required for normal operation with active replication traffic and client connections

> [!NOTE]
> Memory requirements are scoped per database (App Endpoint), not per collection. Whether an App Endpoint has 1 collection or 500, the minimum and recommended values remain the same.

## [](#why-this-matters)Why This Matters

Deploying more App Endpoints than your App Service node can support causes resource contention. Under these conditions, App Service nodes remain stable until replication traffic begins. When replication traffic starts, nodes can enter an out-of-memory loop, resulting in application downtime and poor customer experience.

To prevent this, size your App Service nodes based on the number of App Endpoints you plan to deploy.

## [](#memory-allocation)Memory Allocation

Use the following formulas to calculate the memory required for your App Service node:

Minimum Memory (MB)     = Number of App Endpoints × 500 MB
Recommended Memory (MB) = Number of App Endpoints × 1024 MB

> [!IMPORTANT]
> The minimum values support idle or very low traffic operation only. Use the recommended values when sizing nodes for deployments with active replication traffic and client connections.

## [](#see-also)See Also

* [Scale an App Service](../app-services/scaling-a-deployed-app-service.md)