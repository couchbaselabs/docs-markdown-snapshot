---
title: XDCR Advanced Filtering Reference
description: XDCR Advanced Filtering allows specified subsets of documents to be
  replicated from the source bucket.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/xdcr-reference/pages/xdcr-filtering-reference-intro.adoc
  xref: xref:7.2@server:xdcr-reference:xdcr-filtering-reference-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/xdcr-reference/xdcr-filtering-reference-intro.html)

# XDCR Advanced Filtering Reference

> XDCR Advanced Filtering allows specified subsets of documents to be replicated from the source bucket. 

## [](#configure-xdcr-filtering)Configuring XDCR Filtering

Full, Cluster, and XDCR Administrators can configure XDCR filtering. For a conceptual overview, see [XDCR Advanced Filtering](../learn/clusters-and-availability/xdcr-filtering.md).

XDCR Advanced Filtering can be performed on documents that contain a JSON object — with the keys and values surrounded by curly braces. It _cannot_ be performed on documents that contain only a JSON array — with the elements surrounded only by square brackets.

_Regular_ and _filtering_ expressions are applied, on the source cluster, to documents' keys, values, and metadata: documents that provide a match are replicated to the target; other documents are _not_ replicated.

Multiple expressions can be used by a single replication: the expressions should be `ORed`, as follows: `filterExpression0|filterExpression1`. For example, the expression `airline|hotel` would match both `unitedairline` and `marriothotel`.

Filtering can be established when a replication is created, by means of Couchbase Web Console, CLI, or REST API. Once a replication is underway, its established filtering-expression can be modified; and the replication then either restarted or allowed to continue.

Filtering does not impact conflict resolution, and can be used with either the _revision-based_ or the _timestamp-based_ conflict resolution policy. Filtering does not affect the ability to pause and resume replications. When multiple filtered replications are being established from the same source, expressions should typically be defined so as avoid the unnecessary re-replication of individual documents.

Note that filtering may impact replication-performance; resulting in higher load, reduced throughput, and increased latency.

A full account of XDCR Advanced Filtering expression-syntax is provided in [XDCR Regular Expressions](xdcr-regular-expressions.md) and [XDCR Filtering Expressions](xdcr-filtering-expressions.md). Note that expressions that attempt to compare values whose data types differ from one another must be handled either by _data-type conversion_ or by _collation comparison_. These procedures, which are performed implicitly, are described in [ XDCR Data-Type Conversion](xdcr-filtering-data-type-conversion.md).