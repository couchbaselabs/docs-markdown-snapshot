---
title: Getting Rebalance-Retry Status
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-get-rebalance-retry.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:rest-api:rest-get-rebalance-retry.adoc[]
---

[View original HTML](/server/7.2/rest-api/rest-get-rebalance-retry.html)

# Getting Rebalance-Retry Status

## [](#http-method-and-uri)HTTP method and URI

GET /pools/default/pendingRetryRebalance

## [](#description)Description

This returns status on pending rebalance retries. The information can subsequently be used to cancel the retries.

For an overview of rebalance and rebalance retries, see [Rebalance](../learn/clusters-and-availability/rebalance.md).

## [](#curl-syntax)Curl Syntax

curl -X GET -u <administrator>:<password>
http://<host>:<port>/pools/default/pendingRetryRebalance

## [](#responses)Responses

Success gives `200 OK`, and returns an object containing status on pending rebalance retries. Failure to authenticate gives `401 Unauthorized`. A malformed URI gives `404 Object Not Found`.

## [](#example)Example

The following example obtains information on pending reblance-retries. Note that the command is piped to the [jq](https://stedolan.github.io/jq/) tool, to facilitate output-readability.

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

For an overview of rebalance with the Data Service and other services, see [Rebalance](../learn/clusters-and-availability/rebalance.md). For practical examples of adding a node, rebalancing, and cancelling rebalance retries, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md). For information on using the REST API to cancel pending rebalance retries, see [Cancel Rebalance Retries](rest-cancel-rebalance-retry.md).

For information on configuring rebalance-retry settings, see [Configure Rebalance Retries](rest-configure-rebalance-retry.md). For information on obtaining and reading _rebalance reports_, see the [Rebalance Reference](../rebalance-reference/rebalance-reference.md).