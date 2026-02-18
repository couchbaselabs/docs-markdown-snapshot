---
title: Deleting a Reference
description: To delete an XDCR reference to a target cluster, use the
  <code>DELETE /pools/default/remoteClusters/</code> HTTP method and URI.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-xdcr-delete-ref.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/rest-api/rest-xdcr-delete-ref.html)

# Deleting a Reference

> To delete an XDCR reference to a target cluster, use the `DELETE /pools/default/remoteClusters/` HTTP method and URI. 

## [](#description)Description

Deletes an existing XDCR reference to a target cluster. To be deleted, the reference cannot be in support of any ongoing replication. After deletion, replications to the corresponding target cluster cannot be created, until a new reference is created.

The Full Admin, Cluster Admin, or XDCR Admin role is required.

## [](#http-method-and-uri)HTTP method and URI

DELETE /pools/default/remoteClusters/<target-cluster-name>

The `target-cluster-name` must be the local name already established for the target cluster whose reference is to be deleted. See [Create a Reference](rest-xdcr-create-ref.md).

## [](#curl-syntax)Curl Syntax

curl -v -X DELETE -u <username>:<password>
  http://<ip-address-or-domain-name>:8091/pools/default/remoteClusters/<target-cluster-name>

## [](#responses)Responses

Success returns `200 OK`, and the message `"ok"`.

An attempt to delete a reference that supports a current, ongoing replication returns `400 Bad Request` and the message: `` {"_":"Cannot delete remote cluster `TargetCluster` since it is referenced by replications [2b5dcd1b0101a9d52f31a802d8c4231e/travel-sample/ts]"} `` (where `2b5dcd1b0101a9d52f31a802d8c4231e` is the universally unique identifier for the reference, `travel-sample` is the source bucket, and `ts` is the target bucket).

An improperly specified URI returns `405 Method Not Allowed`. Failure to authenticate returns `401 Unauthorized`.

## [](#example)Example

The following example deletes an existing reference to the locally named cluster `TargetCluster`.

curl -X DELETE -u Administrator:password \
  http://localhost:8091/pools/default/remoteClusters/TargetCluster

If successful, execution returns the following message:

"ok"

## [](#see-also)See Also

A complete overview of XDCR is provided in [Cross Data Center Replication (XDCR)](../learn/clusters-and-availability/xdcr-overview.md). Further examples of reference deletion — by means of UI, CLI, and REST API — are provided in [Delete a Reference](../manage/manage-xdcr/delete-xdcr-reference.md).