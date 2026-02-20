---
title: Add Private Endpoints
description: Private endpoints connect a Capella cluster to a chosen resource or service.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/security/pages/private-endpoints.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:security:private-endpoints.adoc[]
---

[View original HTML](/cloud/security/private-endpoints.html)

# Add Private Endpoints

> Private endpoints connect a Capella cluster to a chosen resource or service. 

A private endpoint peers your cloud service provider (CSP) with a Capella cluster using the same CSP. This connection can reduce latency and egress costs for applications hosted in the same region.

Private endpoints do not support [cross data center replication (XDCR)](../clusters/xdcr/xdcr.md) or [Prometheus metrics](../clusters/monitoring/prometheus.md). If you require XDCR or Prometheus metrics, use VPC Peering.

> [!TIP]
> VPC Peering
> 
> A VPC Peering connection provides an added layer of security for organizations by avoiding communication over the Internet. For details, see [Configure a VPC Peering Connection](../clouds/private-network.md).

## [](#procedures)Procedures

* [Add an AWS PrivateLink Connection](add-aws-private-link.md)
* [Add an Azure Private Link Connection](add-azure-private-link.md)
* [Add a GCP Private Service Connection](add-gcp-private-link.md)