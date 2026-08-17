---
title: Private Endpoints for App Services
description: Private endpoints for App Services enable you to connect a client
  app directly to Couchbase App Services, assuming that they both use the same
  cloud service provider (CSP).
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/private-endpoints/app-services-private-endpoints.adoc
  xref: xref:app-services::private-endpoints/app-services-private-endpoints.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/private-endpoints/app-services-private-endpoints.html)

# Private Endpoints for App Services

> Private endpoints for App Services enable you to connect a client app directly to Couchbase App Services, assuming that they both use the same cloud service provider (CSP). 

This feature allows your mobile or IoT infrastructure to connect to the network encompassing your Capella infrastructure, so that your data does not have to flow over the internet. This can improve security whilst also lowering ingestion costs.

> [!NOTE]
> Private endpoints for App Services cover all App Services connectivity, including:
> 
> * Couchbase Lite sync
> * Admin API access
> * Metrics API access (for example, Prometheus exporters)

Currently, private endpoints for App Services are only available using Amazon Web Services (AWS).

> [!NOTE]
> To use private endpoints for App Services, the client VPC and App Services VPC must be within the same region, for example `us-east-1`.

> [!TIP]
> Both methods provide identical functionality. You can switch between methods for different operations.

## [](#procedures)Procedures

* [Manage AWS Private Endpoints Using the Capella UI](app-services-private-endpoints-aws-ui.md)
* [Manage AWS Private Endpoints Using the Management API](app-services-private-endpoints-aws-api.md)