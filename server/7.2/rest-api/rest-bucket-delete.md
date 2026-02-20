---
title: Deleting Buckets
description: To delete buckets, use the <code>DELETE
  /pools/default/buckets/[bucket-name]</code> HTTP method and URI.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-bucket-delete.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:rest-api:rest-bucket-delete.adoc[]
---

[View original HTML](/server/7.2/rest-api/rest-bucket-delete.html)

# Deleting Buckets

> To delete buckets, use the `DELETE /pools/default/buckets/[bucket-name]` HTTP method and URI. 

## [](#description)Description

Bucket deletion is a synchronous operation. When a cluster has multiple servers, some servers might not be able to delete the bucket within the standard 30 second timeout period.

* If the bucket is deleted on all servers within the standard timeout of 30 seconds, a `200` response code is returned.
* If the bucket is not deleted on all servers within the 30 second timeout, a `500` error code is returned.
* If the bucket is not deleted on all servers and another request is made to delete the bucket, a `404` error code is returned.
* If the bucket is not deleted on all servers and a request is made to create a new bucket with the same name, an error might be returned indicating that the bucket is still being deleted.

> [!WARNING]
> This operation is data destructive. The service makes no attempt to double check with the user. It simply moves forward. Clients applications performing the delete operation are advised to double check with the end user before sending the request.

## [](#http-method-and-uri)HTTP method and URI

DELETE /pools/default/buckets/[bucket-name]

| **Request data**            | None |
| --------------------------- | ---- |
| **Response data**           | None |
| **Authentication required** | Yes  |

## [](#syntax)Syntax

Curl request syntax:

curl -X DELETE -u [admin]:[password]
http://[localhost]:8091//pools/default/buckets/[bucket-name]

Raw HTTP request syntax:

DELETE /pools/default/buckets/[bucket-name]
Host: [localhost]:8091
Authorization: Basic xxxxxxxxxxxxxxxxxxx

## [](#example)Example

Curl request example to delete the bucket named myTestBucket:

curl -X DELETE -u Administrator:password \
http://10.5.2.54:8091/pools/default/buckets/myTestBucket

Raw HTTP request example to delete the bucket named myTestBucket:

DELETE /pools/default/buckets/myTestBucket
Host: 10.5.2.54:8091
Authorization: Basic xxxxxxxxxxxxxxxxxxx

## [](#response-codes)Response codes

| Response codes | Description                                  |
| -------------- | -------------------------------------------- |
| 200            | OK Bucket Deleted on all nodes               |
| 401            | Unauthorized                                 |
| 404            | Object Not Found                             |
| 500            | Bucket could not be deleted on all nodes     |
| 503            | Buckets cannot be deleted during a rebalance |