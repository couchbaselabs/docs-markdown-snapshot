---
title: Performing Compaction Manually
description: Couchbase Server allows a bucket's data to be compacted manually.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-compact-post.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:rest-api:rest-compact-post.adoc[]
---

[View original HTML](/server/7.2/rest-api/rest-compact-post.html)

# Performing Compaction Manually

> Couchbase Server allows a bucket’s data to be compacted manually. 

## [](#description)Description

Couchbase Server allows a specified bucket’s data to be compacted by the administrator, manually. _Full Admin_ and _Cluster Admin_ permissions are required.

## [](#http-methods-and-uris)HTTP methods and URIs

The following methods and URIs allow explicit initiation and cancellation of data-compaction for a specified bucket:

POST /pools/default/buckets/[bucket-name]/controller/compactBucket

POST /pools/default/buckets/[bucket-name]/controller/cancelBucketCompaction

## [](#curl-syntax)Curl Syntax

curl -i -X POST -u [admin]:[password]
  http://[localhost]:8091/pools/default/buckets/[bucket-name]/controller/compactBucket

curl -i -X POST -u [admin]:[password]
  http://[localhost]:8091/pools/default/buckets/[bucket-name]/controller/cancelBucketCompaction

## [](#responses)Responses

If the call is successful, `200 OK` is given, and an object containing group-related information is returned. An incorrectly specified bucket-name or URI gives `404 Object Not Found`. Failure to authenticate gives `401 Unauthorized`.

## [](#example)Example

The following example performs compaction on the bucket `travel-sample`:

curl -i -v -X POST -u Administrator:password \
http://10.143.193.101:8091/pools/default/buckets/travel-sample/controller/compactBucket

Once initiated, the compaction-process can be terminated, with a call such as the following:

curl -i -v -X POST -u Administrator:password \
http://10.143.193.101:8091/pools/default/buckets/travel-sample/controller/cancelBucketCompaction

## [](#see-also)See Also

REST APIs for establishing and retrieving auto-compaction settings are provided in [Auto-Compaction: Global](rest-autocompact-global.md) and [Auto-Compaction: Per Bucket](rest-autocompact-per-bucket.md).

See [Auto-Compaction](../manage/manage-settings/configure-compact-settings.md), for information on managing auto-compaction with Couchbase Web Console.