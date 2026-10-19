---
title: Supported Cloud Providers
description: The cloud providers supported by Operational Insights services.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Capella
    version: ""
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/reference/pages/cloud-providers.adoc
  xref: xref:analytics:reference:cloud-providers.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights-cloud/reference/cloud-providers.html)

# Supported Cloud Providers

Operational Insights services supports deploying clusters on the below cloud service providers:

* [Amazon Web Services (AWS)](aws.md)
* [Google Cloud Platform](gcp.md)
* [Microsoft Azure](azure.md)

> [!NOTE]
> The cloud service providers for Operational Insights are different from those in Capella operational. To see the details of the cloud service providers for Capella operational, see [Supported Cloud Providers](../../cloud/clouds/cloud-providers.md).

> [!CAUTION]
> In the event of unexpected unavailability of the Cloud Service Provider's remote object storage, the Operational Insights service may experience temporary interruptions. Once the storage is available again, the service may take a few minutes to ensure data consistency before resuming normal operations.