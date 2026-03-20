---
title: Getting Rebalance-Retry Status
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/reference/pages/rest-get-rebalance-retry.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:reference:rest-get-rebalance-retry.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/reference/rest-get-rebalance-retry.html)

# Getting Rebalance-Retry Status

## [](#http-method-and-uri)HTTP method and URI

GET /pools/default/pendingRetryRebalance

## [](#description)Description

This returns status on pending rebalance retries. The information can subsequently be used to cancel the retries.

For an overview of rebalance and rebalance retries, see [Rebalance](#learn:clusters-and-availability/rebalance.adoc).

## [](#curl-syntax)Curl Syntax

curl -X GET -u <administrator>:<password>
http://<host>:<port>/pools/default/pendingRetryRebalance

## [](#responses)Responses

Success gives `200 OK`, and returns an object containing status on pending rebalance retries. Failure to authenticate gives `401 Unauthorized`. A malformed URI gives `404 Object Not Found`.

## [](#example)Example

The following example obtains information about pending reblance-retries. Note that the command is piped to the [jq](https://stedolan.github.io/jq/) tool, to facilitate output-readability.

curl -u Administrator:password -v -X GET \
http://10.143.192.101:8091/pools/default/pendingRetryRebalance | jq '.'

If successful, the command returns the following object:

{
  "retry_rebalance": "pending",
  "rebalance_id": "ff5845cdce693db2dce9a9308cbf885d",
  "type": "rebalance",
  "attempts_remaining": 2,
  "retry_after_secs": 291,
  "known_nodes": [
    "ns_1@10.143.192.101",
    "ns_1@10.143.192.103"
  ],
  "eject_nodes": [],
  "delta_recovery_buckets": "all"
}

This indicates that the status of `retry_rebalance` is `pending`; and provides a `rebalance_id` for the process, of `ff5845cdce693db2dce9a9308cbf885d`. This id can be used to cancel the retry. The output also lists the cluster’s nodes, indicates that `2` retry attempts are scheduled to occur if necessary after the current one, and indicates that `291` seconds are still to elapse before the pending retry.

Note that if no rebalance is pending, the following object is returned:

{
  "retry_rebalance": "not_pending"
}

## [](#see-also)See Also

For an overview of rebalance with the Data Service and other services, see [Rebalance](#learn:clusters-and-availability/rebalance.adoc). For practical examples of adding a node, rebalancing, and cancelling rebalance retries, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md). For information about using the REST API to cancel pending rebalance retries, see [Cancel Rebalance Retries](rest-cancel-rebalance-retry.md).

For information about configuring rebalance-retry settings, see [Configure Rebalance Retries](rest-configure-rebalance-retry.md). For information about obtaining and reading _rebalance reports_, see the [Rebalance Reference](#rebalance-reference:rebalance-reference.adoc).