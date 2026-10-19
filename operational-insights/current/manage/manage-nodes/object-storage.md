---
title: Configure Object Storage
description: This page describes how to set up Couchbase Operational Insights
  with Object Storage.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/manage/pages/manage-nodes/object-storage.adoc
  xref: xref:enterprise-analytics:manage:manage-nodes/object-storage.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/manage/manage-nodes/object-storage.html)

# Configure Object Storage

Operational Insights employs compute-storage separation architecture that allows for scaling compute and storage independently. As a result, it requires an object store as its persistent storage. The certified supported object storage solutions are:

* [Amazon S3](aws-s3.md)
* [S3-Compatible Storage](s3-compatible-storage.md)
* [Azure Blob Storage](azure-blob-storage.md)
* [Google Cloud Storage (GCS)](google-cloud-storage.md)

## [](#next-steps)Next Steps

* [Initialize a Node](initialize-node.md)