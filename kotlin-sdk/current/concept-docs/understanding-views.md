---
title: MapReduce Views
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/release/3.9/modules/concept-docs/pages/understanding-views.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:kotlin-sdk:concept-docs:understanding-views.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/current/concept-docs/understanding-views.html)

# MapReduce Views

> You can use MapReduce views to create queryable indexes in Couchbase Server. 

> [!WARNING]
> Although still maintained and supported for legacy use, Views date from the earliest days of Couchbase Server development, and as such are rarely the best choice over, say, [our Query service](n1ql-query.md) for your application, see [our guide to choosing the right service](data-services.md).

# [](#mapreduce-views)MapReduce Views

Views are stored in design documents. The SDK provides convenient methods to create, retrieve, and remove design documents. To set up views, you create design documents that contain one or more view definitions, and then insert the design documents into a bucket.

## [](#creating-design-documents)Creating design documents

Each view in a design document is represented by a name and a set of MapReduce functions. The mandatory map function describes how to select and transform the data from the bucket, and the optional reduce function describes how to aggregate the results.

## [](#retrieving-design-documents)Retrieving design documents

To inspect design documents, you can either retrieve them by name or iterate through a list of documents.