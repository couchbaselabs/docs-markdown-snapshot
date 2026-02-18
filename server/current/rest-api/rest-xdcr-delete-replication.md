---
title: Deleting a Replication
description: To delete an XDCR replication, use the <code>DELETE
  /controller/cancelXDCR</code> HTTP method and URI.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-xdcr-delete-replication.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/rest-api/rest-xdcr-delete-replication.html)

# Deleting a Replication

> To delete an XDCR replication, use the `DELETE /controller/cancelXDCR` HTTP method and URI. 

## [](#description)Description

When a replication is deleted, replication of data from the source to the target cluster is stopped. For replication of data to be resumed, a new replication must be created.

The Full Admin, Cluster Admin, or XDCR Admin role is required.

## [](#http-method-and-uri)HTTP method and URI

DELETE /controller/cancelXDCR/<replication_id>

The `replication_id` must take the form `[UUID]/[local-bucket-name]/[remote-bucket-name]`, and must be URL-encoded. Note that it can be obtained, in encoded format, by means of the `GET` method and `/pools/default/tasks` endpoint, applied to the _source_ cluster: in the output, the encoded id is provided as the value of the `cancelURI` key. See [Getting Cluster Tasks](rest-get-cluster-tasks.md).

## [](#curl-syntax)Curl Syntax

curl -v -X DELETE -u <username>:<password>
  http://[ip-address-or-domain-name]:8091/controller/cancelXDCR/<replication_id>

## [](#responses)Responses

Failure to specify the `replication_id` correctly returns `400 Bad Request` and the following error message: `{"errors":{"_":"requested resource not found"}}`. Failure to authenticate returns `401 Unauthorized`.

## [](#example)Example

In the following example, the existing replication from source bucket `travel-sample` to target bucket `ts` is deleted.

curl -v -X DELETE http://localhost:8091/controller/cancelXDCR/2b5dcd1b0101a9d52f31a802d8c4231e%2Ftravel-sample%2Fts
-u Administrator:password

If deletion succeeds, an empty array is returned:

[]

## [](#see-also)See Also

A complete overview of XDCR is provided in [Cross Data Center Replication (XDCR)](../learn/clusters-and-availability/xdcr-overview.md). Further examples of reference deletion — by means of UI, CLI, and REST API — are provided in [Delete a Replication](../manage/manage-xdcr/delete-xdcr-replication.md). Information on retrieving the uuid for a defined reference is provided in [Getting Cluster Tasks](rest-get-cluster-tasks.md).