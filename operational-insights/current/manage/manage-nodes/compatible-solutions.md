---
title: Compatible Solutions
description: Third-party S3-compatible object storage solutions that implement
  the required S3 API operations may work with Operational Insights.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/manage/pages/manage-nodes/compatible-solutions.adoc
  xref: xref:enterprise-analytics:manage:manage-nodes/compatible-solutions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/manage/manage-nodes/compatible-solutions.html)

# Compatible Solutions

> Third-party S3-compatible object storage solutions that implement the required S3 API operations may work with Operational Insights. 

In addition to [Certified Solutions](certified-solutions.md), the following S3-compatible object storage solutions implement the S3 API operations that Operational Insights requires:

* MinIO
* Nutanix
* IBM Cloud Object Storage
* Pure Storage FlashBlade Object Store
* Dell ECS
* OCI Object Storage
* RustFS
* SeaweedFS

> [!IMPORTANT]
> Operational Insights has not certified these solutions. Before you deploy any of them in production, confirm that your chosen solution and version supports all of the operations described in [S3-Compatible Storage](s3-compatible-storage.md).

## [](#next-steps)Next Steps

* [Initialize a Node](initialize-node.md)