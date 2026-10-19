---
title: Supported Object Storage Solutions
description: Operational Insights employs a compute-storage separation
  architecture that requires an object store as its persistent storage.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/supported-object-storage.adoc
  xref: xref:enterprise-analytics:install:supported-object-storage.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/supported-object-storage.html)

# Supported Object Storage Solutions

> Operational Insights employs a compute-storage separation architecture that requires an object store as its persistent storage. 

## [](#supported-object-storage-solutions)Supported Object Storage Solutions

Operational Insights employs a compute-storage separation architecture that allows for scaling compute and storage independently. As a result, it requires an object store as its persistent storage. The certified supported object storage solutions are:

* [Amazon S3](../manage/manage-nodes/aws-s3.md)
* [S3-Compatible Storage](../manage/manage-nodes/s3-compatible-storage.md)
* [Azure Blob Storage](../manage/manage-nodes/azure-blob-storage.md)
* [Google Cloud Storage (GCS)](../manage/manage-nodes/google-cloud-storage.md)

For step-by-step configuration instructions for each provider, see [Configure Object Storage](../manage/manage-nodes/object-storage.md).