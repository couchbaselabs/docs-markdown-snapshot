---
title: Add Private Endpoints for the Data API
description: Private endpoints for the Data API enable you to connect a client
  app directly to the Couchbase Data API, assuming that they both use the same
  cloud service provider (CSP).
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/data-api-guide/pages/data-api-private.adoc
  xref: xref:cloud:data-api-guide:data-api-private.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/data-api-guide/data-api-private.html)

# Add Private Endpoints for the Data API

> Private endpoints for the Data API enable you to connect a client app directly to the Couchbase Data API, assuming that they both use the same cloud service provider (CSP). 

This feature allows your application to connect to the network encompassing your Capella infrastructure, so that your data does not have to flow over the Internet. This can improve security while also lowering ingestion costs.

Currently, private endpoints for the Data API are available using Amazon Web Services (AWS) and Microsoft Azure.

> [!NOTE]
> To use private endpoints for the Data API, the client VPC and the Data API VPC must be within the same region, for example `us-east-1`.

## [](#procedures)Procedures

* [Manage AWS Private Endpoints for the Data API](data-api-private-aws.md)
* [Manage Azure Private Endpoints for the Data API](data-api-private-azure.md)