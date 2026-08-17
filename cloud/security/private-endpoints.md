---
title: Add Private Endpoints
description: Private endpoints connect a Capella cluster to a chosen resource or service.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/security/pages/private-endpoints.adoc
  xref: xref:cloud:security:private-endpoints.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/security/private-endpoints.html)

# Add Private Endpoints

> Private endpoints connect a Capella cluster to a chosen resource or service. 

A private endpoint peers your cloud service provider (CSP) with a Capella cluster using the same CSP. This connection can reduce latency and egress costs for applications hosted in the same region.

Private endpoints on AWS and GCP supports [cross data center replication (XDCR)](../clusters/xdcr/xdcr.md) and [Prometheus Server](../clusters/monitoring/prometheus.md). For availability details, prerequisites, and any limitations, see the cloud-specific procedures below.

> [!TIP]
> VPC Peering
> 
> A VPC Peering connection provides an added layer of security for organizations by avoiding communication across public internet connections. For details, see [Configure a VPC Peering Connection](../clouds/private-network.md).

## [](#procedures)Procedures

* [Add an AWS PrivateLink Connection](add-aws-private-link.md)
* [Add an Azure Private Link Connection](add-azure-private-link.md)
* [Add a GCP Private Service Connection](add-gcp-private-link.md)