---
title: Buckets API
description: The Buckets REST API creates, deletes, flushes, and retrieves
  information about buckets and bucket operations.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-bucket-intro.adoc
  xref: xref:7.6@server:rest-api:rest-bucket-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/rest-api/rest-bucket-intro.html)

# Buckets API

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

> The Buckets REST API creates, deletes, flushes, and retrieves information about buckets and bucket operations. 

## [](#apis-in-this-section)APIs in this Section

The REST API allows buckets to be created, edited, flushed, and deleted. For a list of all methods and URIs covered in this section, see the table provided below.

| HTTP Method | URI                                                                 | Documented at                                                |
| ----------- | ------------------------------------------------------------------- | ------------------------------------------------------------ |
| POST        | /pools/default/buckets                                              | [Creating and Editing Buckets](rest-bucket-create.md)        |
| POST        | /pools/default/buckets/<bucketName>                                 | [Creating and Editing Buckets](rest-bucket-create.md)        |
| GET         | /pools/default/buckets                                              | [Getting Bucket Information](rest-buckets-summary.md)        |
| GET         | /pools/default/buckets/<bucket-name>                                | [Getting Bucket Information](rest-buckets-summary.md)        |
| POST        | /pools/default/buckets/<bucket-name>/nodes                          | [Listing Nodes by Bucket](rest-retrieve-bucket-nodes.md)     |
| GET         | /pools/default/stats/range/\[metric\_name\]/\[function-expression\] | [Getting a Single Statistic](rest-statistics-single.md)      |
| POST        | /pools/default/stats/range                                          | [Getting Multiple Statistics](rest-statistics-multiple.md)   |
| GET         | /pools/default/buckets/default                                      | [Getting Bucket Streaming URI](rest-buckets-streamingURI.md) |
| DELETE      | /pools/default/buckets/\[bucket-name\]                              | [Deleting Buckets](rest-bucket-delete.md)                    |
| DELETE      | /pools/default/buckets/\[bucket-name\]                              | [Deleting Buckets](rest-bucket-delete.md)                    |
| POST        | /pools/default/buckets/\[bucket-name\]/controller/doFlush           | [Flushing Buckets](rest-bucket-flush.md)                     |
| GET         | /sampleBuckets                                                      | [Managing Sample Buckets](rest-sample-buckets.md)            |
| POST        | /sampleBuckets/install                                              | [Managing Sample Buckets](rest-sample-buckets.md)            |