---
title: Configure a VPC Peering Connection
description: Setting up a VPC peering connection enables your application to
  interact with Couchbase Capella over a private connection by co-locating them
  through VPC or VNet peering.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clouds/pages/private-network.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cloud:clouds:private-network.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clouds/private-network.html)

# Configure a VPC Peering Connection

> Setting up a VPC peering connection enables your application to interact with Couchbase Capella over a private connection by co-locating them through VPC or VNet peering. 

You can configure a VPC peering connection from Couchbase Capella clusters hosted with AWS, GCP, or Microsoft Azure to your application's VPC.

> [!CAUTION]
> Capella does not support VPC peering connections between different cloud providers. For example, you cannot set up VPC peering between a Capella cluster hosted in GCP with an application hosted on AWS.

Using a VPC peering connection provides an added layer of security for organizations by avoiding communication over the Internet. It also results in a significant reduction in latency and egress costs.

> [!TIP]
> Private Endpoints
> 
> Private endpoints connect a Capella cluster to a chosen resource or service. You can set up private endpoints with [AWS](../security/add-aws-private-link.md), [Azure](../security/add-azure-private-link.md), or [GCP](../security/add-gcp-private-link.md).

## [](#procedures)Procedures

* [Create a VPC Peering Connection with AWS](vpc-peering/peer-aws.md)
* [Create a VNet Peering Connection with Azure](vpc-peering/peer-azure.md)
* [Create a VPC Peering Connection with GCP](vpc-peering/peer-gcp.md)