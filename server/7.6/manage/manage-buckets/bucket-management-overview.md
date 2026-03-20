---
title: Manage Buckets
description: <em>Buckets</em>, which Couchbase Server uses to store data, can be
  created, edited, flushed, and deleted.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/manage/pages/manage-buckets/bucket-management-overview.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:manage:manage-buckets/bucket-management-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/manage/manage-buckets/bucket-management-overview.html)

# Manage Buckets

> _Buckets_, which Couchbase Server uses to store data, can be created, edited, flushed, and deleted. 

## [](#bucket-management-overview)Bucket Management Overview

Couchbase _buckets_, used to store data, can be created, edited, flushed, and deleted; by means of Couchbase Web Console, the CLI, and the REST API. A maximum of 30 buckets can be created per cluster. This section provides the basic procedures for bucket-management.

For a complete conceptual and architectural overview of Couchbase buckets, see [Buckets](../../learn/buckets-memory-and-storage/buckets.md).

Couchbase offers two different storage engines for storing the underlying data in buckets: `Couchstore` and `Magma`. For an overview of the backend storage mechanisms, see [Storage Engines](../../learn/buckets-memory-and-storage/storage-engines.md).