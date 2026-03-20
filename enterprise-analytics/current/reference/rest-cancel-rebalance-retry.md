---
title: Canceling Rebalance Retries
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/reference/pages/rest-cancel-rebalance-retry.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:reference:rest-cancel-rebalance-retry.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/reference/rest-cancel-rebalance-retry.html)

# Canceling Rebalance Retries

## [](#http-method-and-uri)HTTP method and URI

POST /controller/cancelRebalanceRetry/<rebalance-id>

## [](#description)Description

This cancels a sequence of one or more pending rebalance retries.

For an overview of rebalance and rebalance retries, see [Rebalance](#learn:clusters-and-availability/rebalance.adoc).

## [](#curl-syntax)Curl Syntax

curl -X POST -u <administrator>:<password>
http://<host>:<port>/controller/cancelRebalanceRetry/<rebalance-id>

Prior to using this command, the `rebalance-id` must be obtained by means of the `GET /pools/default/pendingRetryRebalance` http method and URI; as described in [Get Rebalance-Retry Status](rest-get-rebalance-retry.md).

## [](#responses)Responses

Success gives `200 OK`. Failure to authenticate gives `401 Unauthorized`. A malformed URI gives `404 Object Not Found`.

## [](#example)Example

The following example cancels a retry-sequence whose id is `ff5845cdce693db2dce9a9308cbf885d`:

curl -u Administrator:password -v -X POST \
http://10.143.192.101:8091/controller/cancelRebalanceRetry/ff5845cdce693db2dce9a9308cbf885d

## [](#see-also)See Also

For an overview of rebalance with the Data Service and other services, see [Rebalance](#learn:clusters-and-availability/rebalance.adoc). For practical examples of adding a node, rebalancing, and cancelling rebalance retries, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md). For information about using the REST API to retrieve current rebalance-retry status, see [Get Rebalance-Retry Status](rest-get-rebalance-retry.md).

For information about configuring rebalance-retry settings, see [Configure Rebalance Retries](rest-configure-rebalance-retry.md). For information about obtaining and reading _rebalance reports_, see the [Rebalance Reference](#rebalance-reference:rebalance-reference.adoc).