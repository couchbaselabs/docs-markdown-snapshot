---
title: Add Private Endpoints
description: Private endpoints connect a Capella cluster to a chosen resource or service.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/security/pages/private-endpoints.adoc
pubDate: 2026-03-04T03:42:46.143Z
link: xref:cloud:security:private-endpoints.adoc[]
---

[View original HTML](/cloud/security/private-endpoints.html)

# Add Private Endpoints

> Private endpoints connect a Capella cluster to a chosen resource or service. 

A private endpoint peers your cloud service provider (CSP) with a Capella cluster using the same CSP. This connection can reduce latency and egress costs for applications hosted in the same region.

> [!IMPORTANT]
> XDCR and Prometheus Metrics
> 
> AWS PrivateLink and GCP Private Service Connect can support [Cross Datacenter Replication (XDCR)](../clusters/xdcr/xdcr.md) or [Prometheus metrics](../clusters/monitoring/prometheus.md). These features are only available upon request and are subject to specific conditions.
> 
> For more information about the XDCR conditions, see [Replicate Data Across a Private Endpoint Connection](../clusters/xdcr/manage-xdcr-security.md#private-endpoints). For more information about the Prometheus conditions, see [Prometheus metrics](../clusters/monitoring/prometheus.md).

## [](#procedures)Procedures

* [Add an AWS PrivateLink Connection](add-aws-private-link.md)
* [Add an Azure Private Link Connection](add-azure-private-link.md)
* [Add a GCP Private Service Connection](add-gcp-private-link.md)