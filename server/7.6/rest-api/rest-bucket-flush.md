---
title: Flushing Buckets
description: Flushing a bucket, which deletes all data stored within the bucket,
  can be performed with the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/rest-bucket-flush.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:rest-api:rest-bucket-flush.adoc[]
---

[View original HTML](/server/7.6/rest-api/rest-bucket-flush.html)

# Flushing Buckets

> Flushing a bucket, which deletes all data stored within the bucket, can be performed with the REST API. 

## [](#http-method-and-uri)HTTP method and URI

POST /pools/default/buckets/default/controller/doFlush

## [](#description)Description

_Flushing_ a bucket deletes all data currently stored in the bucket. This operation can only be performed if the bucket has been configured with flushing _enabled_. Enablement is performed either when the bucket is created, or subsequently, by editing. For information, see [Creating and Editing Buckets](rest-bucket-create.md).

A bucket _cannot_ be flushed if it is currently the source for an outgoing XDCR replication. For information on XDCR, see [Cross Data Center Replication (XDCR)](../learn/clusters-and-availability/xdcr-overview.md).

Note that if the bucket contains a large number of documents, flushing causes a correspondingly high disk utilization.

## [](#curl-syntax)Curl Syntax

curl -X POST -u <username>:<password>
  <ip-address-or-domain-name>:8091/pools/default/buckets/<bucket-name>/controller/doFlush

The `bucket-name` is the name of the bucket that is to be flushed.

If flushing is disabled for the specified bucket, `400 Bad Request` is returned, with the following error message: `{"_":"Flush is disabled for the bucket"}`. If the URI is incorrectly specified, the operation fails with `404 Object Not Found`. Failure to authenticate returns `401 Unauthorized`.

If flushing is attempted on a bucket that is the source for an ongoing XDCR replication, the operation fails with `503 Service Unavailable`, and the following error message: `{"_":"Cannot flush buckets with outgoing XDCR"}`.

## [](#example)Example

The following example flushes the bucket `beer-sample`. The example assumes that flushing has already been enabled on the bucket.

curl -v -X POST \
http://10.144.220.101:8091/pools/default/buckets/beer-sample/controller/doFlush \
-u Administrator:password

## [](#see-also)See Also

For information on enabling flushing with the REST API, see [Creating and Editing Buckets](rest-bucket-create.md). Further options for enabling and flushing a bucket, with the UI or CLI, are described in [Flush a Bucket](../manage/manage-buckets/flush-bucket.md). An overview of buckets is provided in [Buckets](../learn/buckets-memory-and-storage/buckets.md).

For information on XDCR, see [Cross Data Center Replication (XDCR)](../learn/clusters-and-availability/xdcr-overview.md).