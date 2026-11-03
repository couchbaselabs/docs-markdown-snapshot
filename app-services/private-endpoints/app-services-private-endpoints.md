---
title: Private Endpoints for App Services
description: Private endpoints for App Services let applications in your cloud
  provider's private network connect to App Services without sending data across
  the public Internet.
pubDate: 2026-11-03T04:28:31.731Z
meta:
  component:
    title: Capella App Services
    version: ""
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/private-endpoints/app-services-private-endpoints.adoc
  xref: xref:app-services::private-endpoints/app-services-private-endpoints.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/private-endpoints/app-services-private-endpoints.html)

# Private Endpoints for App Services

> Private endpoints for App Services let applications in your cloud provider's private network connect to App Services without sending data across the public Internet. 

A private endpoint connects the private network where your applications run to the network that contains your Capella infrastructure. Your application traffic stays on your cloud provider's network. This can improve security and lower data transfer costs.

## [](#what-you-can-reach-over-a-private-endpoint)What You Can Reach Over a Private Endpoint

Applications in your private network can reach the following over a private endpoint:

* Couchbase Lite sync
* Admin API access
* Metrics API access, such as Prometheus exporters

Private endpoint connections and public Internet connections provide the same App Services capabilities. You can use a private endpoint for some operations and the public Internet for others.

## [](#private-endpoints-and-public-access)Private Endpoints and Public Access

Private endpoints do not replace the public App Endpoint. Couchbase Lite clients outside your private network, such as mobile devices, still connect through the public Internet using TLS. Through the public Internet, the Admin API and Metrics API accept connections only from IP addresses on your allowed IP list.

## [](#requirements)Requirements

* Your application's private network and App Services must use the same cloud provider and run in the same region.
* Capella supports private endpoints for App Services on Amazon Web Services only.

## [](#see-also)See Also

* [Manage AWS Private Endpoints Using the Capella UI](app-services-private-endpoints-aws-ui.md)
* [Manage AWS Private Endpoints Using the Management API](app-services-private-endpoints-aws-api.md)