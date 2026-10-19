---
title: Rebalance
description: When one or more nodes have been brought into or taken out of a
  cluster, <em>rebalance</em> redistributes the work of the Analytics Service
  among available nodes.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-rebalance-overview.adoc
  xref: xref:enterprise-analytics:reference:rest-rebalance-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-rebalance-overview.html)

# Rebalance

> When one or more nodes have been brought into or taken out of a cluster, _rebalance_ redistributes the work of the Analytics Service among available nodes. Rebalance can be performed and configured by means of the REST API. 

## [](#apis-in-this-section)APIs in this Section

_Rebalance_ must be performed whenever the number of nodes in a cluster has changed. For more information, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md) and [Remove a Node and Rebalance](../manage/manage-nodes/remove-node-and-rebalance.md).

The REST API for rebalance is as follows:

| HTTP Method | URI                                             | Documented at                                                                     |
| ----------- | ----------------------------------------------- | --------------------------------------------------------------------------------- |
| POST        | /controller/rebalance                           | [Rebalancing the Cluster](rest-cluster-rebalance.md)                              |
| GET         | /pools/default                                  | [Getting Rebalance Reason Codes](rest-retrieve-cluster-rebalance-reason-codes.md) |
| GET         | /pools/default/rebalanceProgress                | [Getting Rebalance Progress](rest-get-rebalance-progress.md)                      |
| GET         | /settings/retryRebalance                        | [Configuring Rebalance Retries](rest-configure-rebalance-retry.md)                |
| POST        | /settings/retryRebalance                        | [Configuring Rebalance Retries](rest-configure-rebalance-retry.md)                |
| GET         | /pools/default/pendingRetryRebalance            | [Getting Rebalance-Retry Status](rest-get-rebalance-retry.md)                     |
| POST        | /controller/cancelRebalanceRetry/<rebalance-id> | [Canceling Rebalance Retries](rest-cancel-rebalance-retry.md)                     |